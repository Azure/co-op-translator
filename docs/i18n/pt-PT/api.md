# API em Python

A API pública estável em Python é exportada a partir de `co_op_translator.api`. A maioria das integrações usa um destes fluxos de trabalho:

| Cenário | Use isto quando | APIs principais |
| --- | --- | --- |
| Traduzir ficheiros ou documentos individuais | A sua aplicação lê o conteúdo fonte, chama o Co-op Translator para tradução e decide onde guardar o resultado. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Preparar conteúdo para tradução por agente anfitrião | O seu host MCP ou modelo da aplicação irá traduzir os fragmentos, enquanto o Co-op Translator trata do particionamento e da reconstrução. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Traduzir um repositório inteiro | Quer que a API Python se comporte como a CLI e trate da descoberta, dos caminhos de saída, dos metadados, da limpeza e das escritas. | `run_translation` |

A maioria dos módulos de baixo nível em `core`, `config`, `review` e `utils` são detalhes de implementação usados por estes pontos de entrada da API.

Os clientes MCP usam a mesma API pública através do [Servidor MCP](mcp.md). Use esta página quando chamar Python diretamente, e o guia MCP quando expor o Co-op Translator a um agente ou editor. Se estiver a decidir entre a CLI, a API Python e o MCP, comece por [Escolha o seu fluxo de trabalho](workflows.md).

## Fluxo inicial da API

Comece aqui se estiver a chamar o Co-op Translator a partir de código Python:

1. Configure um fornecedor LLM conforme descrito em [Configuração](configuration.md), a menos que esteja apenas a preparar fragmentos Markdown ou de notebooks para tradução por agente anfitrião.
2. Decida se a sua aplicação gere a E/S de ficheiros.
3. Use as APIs de conteúdo quando a sua aplicação lê e escreve ficheiros individuais.
4. Use `run_translation` quando o Co-op Translator deve processar um repositório como a CLI.
5. Use `run_review` após a tradução se precisar de verificações determinísticas em automação.

| Objetivo | API para começar |
| --- | --- |
| Traduzir uma string ou ficheiro Markdown | `translate_markdown_content` |
| Traduzir um payload de notebook | `translate_notebook_content` |
| Traduzir uma imagem | `translate_image_content` |
| Permitir que um agente anfitrião traduza fragmentos Markdown ou de notebooks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Reescrever links traduzidos após escolher o caminho de saída | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Traduzir um repositório completo | `run_translation` |
| Rever a saída traduzida | `run_review` |

## Cenário 1: Traduzir Ficheiros ou Documentos Individuais

Utilize este fluxo de trabalho quando já tiver um ficheiro, um buffer do editor, um payload de notebook, um pedido MCP ou uma entrada de pipeline personalizada. O seu código gere a E/S de ficheiros:

1. Leia o conteúdo fonte.
2. Chame uma API de tradução de conteúdo.
3. Opcionalmente chame uma API de reescrita de caminhos se o conteúdo traduzido for gravado numa pasta de tradução do projeto.
4. Guarde ou devolva o resultado a partir da sua aplicação.

As APIs de tradução de conteúdo não executam a descoberta de projeto, não escrevem metadados, não acrescentam isenções de responsabilidade, e não reescrevem links automaticamente.

### Ficheiro Markdown

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Se o Markdown traduzido não ficar numa estrutura de projeto do Co-op Translator, ignore `rewrite_markdown_paths` e guarde a string traduzida diretamente.

### Ficheiro de Notebook

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` traduz células Markdown e preserva células não-Markdown. A reescrita de caminhos é aplicada apenas às células Markdown.

### Ficheiro de Imagem

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` lê a imagem de origem e devolve um `PIL.Image.Image` renderizado. Não escreve metadados de imagem traduzidos.

## Cenário 2: Traduzir um Repositório Inteiro

Use este fluxo de trabalho quando quiser que a API Python se comporte como a CLI `translate`. O `run_translation` descobre ficheiros suportados, traduz tipos de conteúdo selecionados, reescreve caminhos, escreve ficheiros de saída, atualiza metadados e executa tarefas de manutenção de tradução como limpeza.

`run_translation` é o ponto de entrada preferido para orquestração do projecto. `translate_project` é exportado como um alias de compatibilidade com o mesmo comportamento.

Traduza ficheiros Markdown no repositório atual para coreano e japonês:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Traduza apenas notebooks a partir de uma raiz de projecto específica:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Pré-visualize o volume de tradução sem escrever ficheiros:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Registe eventos de progresso estruturados para uma integração:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Armazene a carga útil na sua tabela de eventos de trabalho ou transmita-a para a sua interface do utilizador.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Os eventos usam o esquema versionado `co-op.translation.event.v1`. As integrações devem
depender de campos estáveis como `type` e `stage_key`, não do texto de consola
ou `stage_label`.

Traduza várias raízes de conteúdo numa só chamada:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Escreva traduções em grupos de saída explícitos:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Use um marcador por idioma quando cada idioma deve conter um subdiretório aninhado:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

Se nenhum dos parâmetros `markdown`, `notebook` ou `images` estiver definido, a API traduz todos os tipos suportados: Markdown, notebooks e imagens.

### Preservar edições humanas aceites com um fornecedor de estado de tradução

Por predefinição, o Co-op Translator mantém o seu comportamento existente ao nível do ficheiro: quando uma
origem em Markdown está desactualizada, todo o ficheiro traduzido é regenerado. Integrações alojadas
podem opcionalmente passar um `TranslationStateProvider` para preservar edições humanas
em blocos de origem que não foram alterados.

O fornecedor fornece o último par origem/destino aceite e regista cada novo
candidato. A aceitação continua a ser da responsabilidade da integração—por exemplo,
depois de um pull request de tradução ser mesclado:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

Para ficheiros Markdown com uma linha de base aceite válida, o Co-op Translator alinha
blocos Markdown de nível superior. Os blocos de origem não alterados reutilizam os blocos traduzidos
actuais, incluindo edições feitas por pessoas; blocos de origem alterados ou adicionados são enviados
para tradução; blocos de origem eliminados são removidos. Se o alinhamento for ambíguo,
a estrutura de destino tiver mudado, uma tradução de bloco for inválida, ou não houver linha de
base disponível, o Co-op Translator recorre em segurança ao caminho existente de
tradução de ficheiro completo.

Esta API armazena o estado de tradução do documento, não uma memória de tradução de frases ou
segmentos entre documentos. Actualmente aplica-se à tradução de projectos Markdown.
O comportamento de notebooks e imagens permanece inalterado. Passar `update=True`
ainda solicita a regeneração completa.

Se um ou mais ficheiros não puderem ser traduzidos, `run_translation` lança um
`RuntimeError` depois de o fluxo de trabalho do projecto terminar em vez de reportar um
sucesso com saída em falta. As integrações devem tratar isto como um trabalho falhado
e reter o estado de tradução aceite anterior.

## Rever a Saída Traduzida

`run_review` executa verificações determinísticas de tradução sem credenciais LLM ou Vision.

!!! note "Beta"
    `run_review` é uma API de revisão determinística em versão beta. Não chama fornecedores de modelos nem escreve ficheiros, mas as verificações e os esquemas das issues podem evoluir.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Após uma tradução apenas do README, use o mesmo âmbito para a revisão:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` revê apenas `README.md` sob cada raiz de origem configurada,
incluindo `groups` personalizados e diretórios de saída. Outros documentos e
READMEs são excluídos. Um README de origem em falta levanta `ValueError`; falhas
às verificações de tradução levantam `RuntimeError`.

Rever apenas ficheiros alterados em relação a um ref base e imprimir saída no formato GitHub:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Exemplos de API para copiar e colar

Traduzir conteúdo Markdown sem escrever ficheiros:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Traduzir e reescrever ligações Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Traduzir um repositório a partir do Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Traduzir múltiplas raízes:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Preservar termos do glossário:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Pontos de Entrada Públicos

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## APIs de Tradução de Conteúdo

As APIs de tradução de conteúdo destinam-se a integrações que já têm conteúdo em memória, como uma extensão de editor, uma ferramenta MCP, um processador de notebooks ou um pipeline personalizado.

| Função | Entrada | Saída | I/O de ficheiro | Notas |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Não | Assíncrono. Traduz apenas conteúdo Markdown. Não reescreve ligações, não escreve metadados nem anexa avisos. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Não | Assíncrono. Traduz células Markdown e preserva células não-Markdown. Não reescreve ligações, não escreve metadados nem anexa avisos. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Lê apenas a imagem de origem | Síncrono. Extrai e traduz o texto da imagem, depois retorna uma imagem renderizada. Não guarda metadados da imagem traduzida. |

`translate_markdown_content` e `translate_notebook_content` aceitam um `source_path` opcional através das suas opções. O caminho é passado como contexto ao tradutor; os chamadores continuam responsáveis por qualquer reescrita de caminhos específica do projeto após a tradução.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

As mesmas opções podem ser passadas como dicionários:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## APIs de Tradução Assistida por Agente

As APIs assistidas por agente não chamam o fornecedor LLM configurado pelo Co-op Translator. Preparam pedaços (chunks) de Markdown ou notebook para um agente anfitrião traduzir e depois reconstruem o conteúdo final a partir dos pedaços traduzidos.

| Função | Finalidade |
| --- | --- |
| `start_markdown_agent_translation` | Retorna um trabalho Markdown autónomo com chunks, prompts e estado de reconstrução. |
| `finish_markdown_agent_translation` | Reconstrói Markdown a partir de um trabalho e de chunks traduzidos pelo agente anfitrião. |
| `start_notebook_agent_translation` | Retorna um trabalho de notebook com chunks de células Markdown para tradução pelo agente anfitrião. |
| `finish_notebook_agent_translation` | Reconstrói o JSON do notebook preservando células de código, saídas e metadados. |

Este fluxo de trabalho destina-se principalmente a hosts MCP. Se precisar de tradução de repositório em produção com o Co-op Translator a gerir chamadas a fornecedores, use `translate_markdown_content`, `translate_notebook_content` ou `run_translation`.

## APIs de Reescrita de Caminhos

As APIs de reescrita de caminhos não realizam tradução. Atualizam ligações e caminhos no frontmatter depois de os chamadores conhecerem o caminho de origem, o caminho alvo traduzido e a estrutura do projeto.

| Função | Âmbito | Notas |
| --- | --- | --- |
| `rewrite_markdown_paths` | Corpo Markdown e frontmatter | Reescreve ligações Markdown e campos de caminho suportados no frontmatter para um alvo traduzido. |
| `rewrite_notebook_paths` | Células Markdown no JSON do notebook | Aplica a reescrita de caminhos Markdown a cada célula Markdown e deixa as células não-Markdown inalteradas. |

O argumento `policy` pode ser um dicionário com estes campos:

| Campo | Obrigatório | Finalidade |
| --- | --- | --- |
| `language_code` | Sim | Código de idioma alvo, como `"ko"` ou `"pt-BR"`. |
| `root_dir` | Não | Raiz do projeto fonte. Por omissão é `"."`. |
| `translations_dir` | Não | Diretório de saída de tradução de texto. Por omissão `translations` sob `root_dir`. |
| `translated_images_dir` | Não | Diretório de saída para imagens traduzidas. Por omissão `translated_images` sob `root_dir`. |
| `translation_types` | Não | Tipos de tradução ativados. Por omissão Markdown, notebooks e imagens. |
| `lang_subdir` | Não | Subdiretório opcional sob cada pasta de idioma. |

## Parâmetros de Tradução do Projeto

| Parâmetro | Tipo | Predefinição | Finalidade |
| --- | --- | --- | --- |
| `language_codes` | `str` | Obrigatório | Códigos de idiomas alvo separados por espaços, como `"ko ja fr"`, ou `"all"`. Códigos de alias são normalizados para valores canónicos BCP 47. |
| `root_dir` | `str` | `"."` | Raiz do projeto para um único alvo de tradução. Ignorado quando `root_dirs` ou `groups` são fornecidos. |
| `update` | `bool` | `False` | Eliminar e recriar traduções existentes para os idiomas selecionados. |
| `images` | `bool` | `False` | Incluir tradução de imagens. Requer configuração do Azure AI Vision. |
| `markdown` | `bool` | `False` | Incluir tradução de Markdown. |
| `notebook` | `bool` | `False` | Incluir tradução de notebooks Jupyter. |
| `debug` | `bool` | `False` | Ativar registo de depuração. |
| `save_logs` | `bool` | `False` | Gravar ficheiros de log de nível DEBUG sob o diretório raiz `logs/`. |
| `yes` | `bool` | `True` | Confirmar automaticamente os prompts para utilização programática e em CI. |
| `add_disclaimer` | `bool` | `False` | Adicionar avisos de tradução automática ao Markdown e aos notebooks traduzidos. |
| `translations_dir` | `str \| None` | `None` | Diretório de saída personalizado para tradução de texto. Caminhos relativos são resolvidos em relação a cada raiz. |
| `image_dir` | `str \| None` | `None` | Diretório de saída personalizado para imagens traduzidas. Caminhos relativos são resolvidos em relação a cada raiz. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Múltiplas raízes que partilham as mesmas definições de saída. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pares explícitos `(root_dir, translations_dir)`. Tem precedência sobre `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL do repositório usado ao renderizar a orientação da tabela de idiomas do README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termos de glossário a preservar durante a tradução. Termos duplicados e vazios são normalizados. |
| `dry_run` | `bool` | `False` | Estimar o volume de tradução e pré-visualizar o comportamento de migração sem gravar ficheiros. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Adaptador de persistência opcional para baseline aceite e candidato para atualizações incrementais de Markdown. Omiti-lo preserva o comportamento existente de ficheiro completo. |

## Parâmetros de Revisão

`run_review` espelha intencionalmente a assinatura de `run_translation` sempre que possível para que a automação possa alternar entre fluxos de trabalho de tradução e revisão com ramificação mínima.

| Parâmetro | Tipo | Padrão | Propósito |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Pastas de idiomas alvo a rever. São aceites strings separadas por espaços e iteráveis. `"all"` revê todas as línguas de tradução descobertas. |
| `root_dir` | `str` | `"."` | Raiz do projeto para um único alvo de revisão. Ignorado quando `root_dirs` ou `groups` são fornecidos. |
| `markdown` | `bool` | `False` | Incluir ficheiros fonte Markdown e MDX. |
| `notebook` | `bool` | `False` | Incluir ficheiros fonte de Jupyter notebooks. |
| `images` | `bool` | `False` | Reservado para paridade com as opções de tradução. As referências por link para imagens são verificadas a partir do Markdown. |
| `translations_dir` | `str \| None` | `None` | Diretório de saída personalizado para tradução de texto. Caminhos relativos são resolvidos em relação a cada raiz. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Múltiplas raízes que partilham as mesmas definições de saída. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pares explícitos `(root_dir, translations_dir)`. Tem precedência sobre `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Ref do Git usada para limitar a revisão aos ficheiros fonte alterados. |
| `readme_only` | `bool` | `False` | Rever apenas `README.md` em cada raiz de origem. Um README de origem em falta provoca um `ValueError`. |
| `output_format` | `str` | `"text"` | Formato de saída da revisão. Valores suportados são `"text"` e `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Tratar avisos como falhas, além dos erros. |
| `debug` | `bool` | `False` | Ativar logging de debug. |
| `save_logs` | `bool` | `False` | Gravar ficheiros de log ao nível DEBUG no diretório raiz `logs/`. |

Se nenhum de `markdown`, `notebook` ou `images` estiver definido, a API revê Markdown, notebooks e referências de links de imagem quando aplicável. A revisão não chama um fornecedor LLM e não requer chaves de API.

## Requisitos de Configuração

As APIs de tradução suportadas por fornecedores requerem configuração do fornecedor antes de traduzir:

- A tradução de Markdown e notebooks requer um fornecedor LLM. Configure Azure OpenAI, OpenAI ou Anthropic.
- A tradução de imagens requer Azure AI Vision além do fornecedor LLM.
- `run_translation` executa verificações de conectividade leves antes de começar a tradução do projeto.
- As APIs assistidas por agente `start_*_agent_translation` e `finish_*_agent_translation` não chamam os fornecedores LLM do Co-op Translator. A aplicação anfitriã ou o agente MCP traduz os blocos preparados.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` e `run_review` são determinísticos e não requerem credenciais do fornecedor.

Variáveis obrigatórias do Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Variáveis obrigatórias do OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Variáveis obrigatórias da Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` e `ANTHROPIC_MAX_TOKENS` são opcionais. O Microsoft Agent Framework é o cliente de modelo predefinido para todos os fornecedores a partir do Co-op Translator 0.22.0. O Semantic Kernel ainda pode ser selecionado temporariamente com `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, mas fazê-lo emite um aviso de obsolescência; consulte [configuração](configuration.md#model-client-backend) para o plano de remoção faseada.

Variáveis obrigatórias do Azure AI Vision para tradução de imagens:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` é determinístico e não requer configuração de LLM ou Azure AI Vision.

## Notas de Comportamento

- As APIs de tradução de conteúdo mantêm a tradução separada da reescrita de caminhos do projeto. Chame explicitamente `rewrite_markdown_paths` ou `rewrite_notebook_paths` quando o conteúdo traduzido necessitar de ajuste de links relativos ao projeto para um local de destino.
- As APIs de orquestração de projeto adicionam comportamento ao redor da tradução de conteúdo, incluindo descoberta de ficheiros, gravação, reescrita de caminhos, metadados, limpeza e avisos opcionais.
- `run_translation` imprime resumos de progresso e estimativas através do mesmo reportador suportado por Rich usado pela CLI. A saída não interativa recorre ao texto simples.
- `dry_run=True` calcula estimativas usando atualizações virtuais do README, mas não grava o README nem os ficheiros de tradução.
- Os `groups` são processados sequencialmente. Uma única estimativa agregada é impressa antes do início do trabalho.
- Quando a tradução de imagens é selecionada, a falta de configuração do Vision provoca um erro antes do início da tradução.
- As pastas de idioma existentes baseadas em aliases são detectadas e podem ser migradas para nomes canónicos de pastas de idioma como parte da execução.
- `run_review` falha em ficheiros traduzidos em falta, metadados de tradução em falta ou obsoletos, frontmatter/fences de código Markdown malformados e JSON de notebook traduzido inválido.
- `run_review` reporta alvos locais de Markdown e links de imagem em falta como avisos por omissão.

## Caminho de Chamada Interno

A API delega para a mesma implementação central usada pela CLI:

Tradução:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content` ou `translate_image_content` para tradução em memória.
2. `co_op_translator.api.translation.rewrite_markdown_paths` ou `rewrite_notebook_paths` para pós-processamento explícito de caminhos.
3. `co_op_translator.api.translation.run_translation` para orquestração completa do projeto.
4. `co_op_translator.config.Config`, `LLMConfig` e `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixins de tradução focados no projeto para Markdown, notebooks e imagens.
8. Tradutores de Markdown, notebook, texto e imagem em `co_op_translator.core`.

Revisão:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Verificações determinísticas em `co_op_translator.review.checks`

As seguintes classes são úteis para mantenedores, mas não são exportadas como API estável ao nível do pacote.

| Classe | Módulo | Responsabilidade |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordena a tradução ao nível do projeto, gestão de diretórios, normalização de metadados por idioma e delegação para tradutores de Markdown, notebook e imagem. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Executa o trabalho assíncrono de processamento de ficheiros para Markdown, notebooks, imagens, deteção de obsolescência e atualizações de metadados de tradução. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orquestra leituras de ficheiros Markdown, tradução de conteúdo, reescrita de caminhos, metadados, avisos e escrita. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orquestra leituras de ficheiros de notebook, tradução de células Markdown, reescrita de caminhos, metadados, avisos e escrita. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orquestra a descoberta de imagens de origem, tradução de imagens, caminhos de saída, metadados e escrita. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Encontra pares de Markdown traduzidos, avalia a qualidade da tradução e lê metadados de confiança para fluxos de trabalho de reparação de baixa confiança. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordena verificações determinísticas de revisão através de ficheiros fonte, línguas alvo e raízes de tradução configuradas. |
| `ReviewTarget` | `co_op_translator.review.targets` | Descreve uma raiz de origem e o diretório de saída de tradução revisto para essa raiz. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detecta pastas de idioma legadas baseadas em alias e prepara planos de migração para pastas canónicas BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Carrega ficheiros `.env` e verifica se fornecedores LLM obrigatórios e Vision opcionais estão configurados. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Deteta automaticamente Azure OpenAI, OpenAI ou Anthropic, valida as variáveis de ambiente obrigatórias e executa verificações de conectividade do fornecedor. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Deteta a configuração do Azure AI Vision e executa verificações de conectividade para tradução de imagens. |