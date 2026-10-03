# API em Python

A API pública estável em Python é exportada de `co_op_translator.api`. A maioria das integrações usa um destes fluxos de trabalho:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Traduzir arquivos ou documentos individuais | Seu aplicativo lê o conteúdo de origem, chama o Co-op Translator para tradução e decide onde salvar o resultado. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Preparar conteúdo para tradução por host-agente | Seu host MCP ou o modelo do aplicativo traduzirá chunks, enquanto o Co-op Translator cuida do chunking e da reconstrução. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Traduzir um repositório inteiro | Você quer que a API Python se comporte como a CLI e gerencie descoberta, caminhos de saída, metadados, limpeza e escritas. | `run_translation` |

A maioria dos módulos de nível mais baixo sob `core`, `config`, `review` e `utils` são detalhes de implementação usados por esses pontos de entrada da API.

Clientes MCP usam a mesma API pública através do [Servidor MCP](mcp.md). Use esta página ao chamar Python diretamente, e o guia MCP ao expor o Co-op Translator para um agente ou editor. Se você está decidindo entre CLI, API Python e MCP, comece com [Escolha seu fluxo de trabalho](workflows.md).

## Fluxo inicial da API

Comece aqui se você estiver chamando o Co-op Translator a partir de código Python:

1. Configure um provedor de LLM conforme descrito em [Configuração](configuration.md), a menos que você esteja apenas preparando chunks de Markdown ou notebook para tradução por host-agent.
2. Decida se sua aplicação irá gerenciar E/S de arquivos.
3. Use as APIs de conteúdo quando sua aplicação lê e grava arquivos individuais.
4. Use `run_translation` quando o Co-op Translator deve processar um repositório como o CLI.
5. Use `run_review` após a tradução se você precisar de verificações determinísticas em automação.

| Goal | API to start with |
| --- | --- |
| Traduzir uma string ou arquivo Markdown | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Permitir que um agente host traduza trechos de Markdown ou de notebooks | `start_markdown_agent_translation` ou `start_notebook_agent_translation` |
| Reescrever links traduzidos após escolher um caminho de saída | `rewrite_markdown_paths` ou `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Cenário 1: Traduzir arquivos ou documentos individuais

Use este fluxo de trabalho quando você já tem um arquivo, buffer do editor, payload de notebook, requisição MCP ou entrada de pipeline personalizada. Seu código gerencia a E/S de arquivos:

1. Leia o conteúdo de origem.
2. Chame uma API de tradução de conteúdo.
3. Opcionalmente chame uma API de reescrita de caminhos se o conteúdo traduzido for gravado em uma pasta de tradução do projeto.
4. Salve ou retorne o resultado a partir da sua aplicação.

As APIs de tradução de conteúdo não executam descoberta de projeto, não escrevem metadados, não acrescentam avisos e não reescrevem links automaticamente.

### Arquivo Markdown

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

Se o Markdown traduzido não ficar em um layout de projeto do Co-op Translator, pule `rewrite_markdown_paths` e salve a string traduzida diretamente.

### Arquivo de Notebook

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

### Arquivo de Imagem

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

`translate_image_content` lê a imagem de origem e retorna uma `PIL.Image.Image` renderizada. Não grava metadados de imagem traduzidos.

## Cenário 2: Traduzir um Repositório Inteiro

Use este fluxo de trabalho quando você quiser que a API Python se comporte como a CLI `translate`. `run_translation` descobre arquivos suportados, traduz tipos de conteúdo selecionados, reescreve caminhos, grava arquivos de saída, atualiza metadados e executa tarefas de manutenção da tradução, como limpeza.

`run_translation` é o ponto de entrada preferido para orquestração do projeto. `translate_project` é exportado como um alias de compatibilidade com o mesmo comportamento.

Traduza arquivos Markdown no repositório atual para coreano e japonês:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Traduza apenas notebooks de um diretório raiz de projeto específico:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Visualize o volume de tradução sem gravar arquivos:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Registre eventos estruturados de progresso para uma integração:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Armazene a carga útil na sua tabela de eventos de jobs ou transmita-a para sua interface do usuário.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Eventos usam o esquema versionado `co-op.translation.event.v1`. Integrações devem
depender de campos estáveis como `type` e `stage_key`, não do texto voltado ao usuário
texto do console ou `stage_label`.

Traduza múltiplas raízes de conteúdo em uma única chamada:

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

Use um espaço reservado por idioma quando cada idioma deve conter um subdiretório aninhado:

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

Se nenhum de `markdown`, `notebook` ou `images` estiver definido, a API traduz todos os tipos suportados: Markdown, notebooks e imagens.

### Preservar edições humanas aceitas com um provedor de estado de tradução

Por padrão, o Co-op Translator mantém seu comportamento existente no nível de arquivo: quando um
uma fonte Markdown estiver desatualizada, o arquivo traduzido inteiro é regenerado. Integrações hospedadas
podem opcionalmente passar um `TranslationStateProvider` para preservar edições humanas
em blocos de origem que não foram alterados.

O provedor fornece o último par origem/destino aceito e registra cada novo
candidato. A aceitação permanece responsabilidade da integração—por exemplo,
após um pull request de tradução ser mesclado:

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

Para arquivos Markdown com uma linha de base aceita válida, o Co-op Translator alinha
os blocos Markdown de nível superior. Blocos de origem não alterados reutilizam os blocos traduzidos atuais
blocos, incluindo edições feitas por pessoas; blocos de origem alterados ou adicionados são enviados
para tradução; blocos de origem excluídos são removidos. Se o alinhamento for ambíguo,
a estrutura de destino mudou, uma tradução de bloco é inválida, ou nenhuma linha de base está
disponível, o Co-op Translator recorre com segurança ao caminho existente de tradução
de arquivo inteiro.

Esta API armazena o estado de tradução do documento, não uma memória de tradução de frases ou
segmentos entre documentos. Ele se aplica atualmente à tradução de projetos Markdown.
O comportamento de notebooks e imagens permanece inalterado. Passar `update=True`
ainda solicita regeneração completa.

Se um ou mais arquivos não puderem ser traduzidos, `run_translation` lança um
`RuntimeError` após o fluxo de trabalho do projeto terminar em vez de relatar um
execução bem-sucedida com saída faltando. Integrações devem tratar isto como um trabalho falho
e reter o estado de tradução aceito anterior.

## Revisar a Saída Traduzida

`run_review` executa verificações determinísticas de tradução sem credenciais de LLM ou Vision.

!!! note "Beta"
    `run_review` é uma API de revisão determinística em beta. Ela não chama provedores de modelos nem grava arquivos, mas os esquemas de verificações e issues podem evoluir.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Após uma tradução apenas do README, use o mesmo escopo para revisão:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` revisa apenas o `README.md` sob cada raiz de origem configurada,
incluindo `groups` personalizados e diretórios de saída. Outros documentos e nested
READMEs são excluídos. Um README de origem ausente lança `ValueError`; verificações
de tradução com falha lançam `RuntimeError`.

Revise apenas arquivos alterados em relação a uma referência base e imprima saída no estilo GitHub:

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

## Exemplos de API para Copiar e Colar

Traduza conteúdo Markdown sem gravar arquivos:

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

Traduza e reescreva links do Markdown:

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

Traduza um repositório a partir do Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Traduza múltiplas raízes:

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

Preserve termos do glossário:

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

As APIs de tradução de conteúdo destinam-se a integrações que já possuem conteúdo em memória, como uma extensão de editor, ferramenta MCP, processador de notebooks ou pipeline personalizado.

| Function | Entrada | Saída | I/O de Arquivo | Observações |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Não | Assíncrono. Traduz apenas conteúdo Markdown. Não reescreve links, não grava metadados, nem adiciona termos de isenção de responsabilidade. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Não | Assíncrono. Traduz células Markdown e preserva células não-Markdown. Não reescreve links, não grava metadados, nem adiciona termos de isenção de responsabilidade. |
| `translate_image_content` | Caminho da imagem | `PIL.Image.Image` | Lê apenas a imagem de origem | Síncrono. Extrai e traduz o texto da imagem, então retorna uma imagem renderizada. Não salva metadados da imagem traduzida. |

`translate_markdown_content` e `translate_notebook_content` aceitam um `source_path` opcional através de suas opções. O caminho é passado como contexto para o tradutor; os chamadores continuam responsáveis por qualquer reescrita de caminho específica do projeto após a tradução.

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

As APIs assistidas por agente não chamam o provedor LLM configurado do Co-op Translator. Elas preparam trechos de Markdown ou notebook para um agente host traduzir e então reconstroem o conteúdo final a partir dos trechos traduzidos.

| Função | Propósito |
| --- | --- |
| `start_markdown_agent_translation` | Retorna um trabalho Markdown autocontido com blocos, prompts e estado de reconstrução. |
| `finish_markdown_agent_translation` | Reconstrói Markdown a partir de um job e dos blocos traduzidos pelo agente host. |
| `start_notebook_agent_translation` | Retorna um job de notebook com blocos de células Markdown para tradução pelo agente host. |
| `finish_notebook_agent_translation` | Reconstrói o JSON do notebook preservando células de código, saídas e metadados. |

Esse fluxo de trabalho destina-se principalmente a hosts MCP. Se você precisa de tradução de repositório em produção com o Co-op Translator gerenciando chamadas a provedores, use `translate_markdown_content`, `translate_notebook_content` ou `run_translation`.

## APIs de Reescrita de Caminhos

As APIs de reescrita de caminhos não realizam tradução. Elas atualizam links e caminhos do frontmatter depois que os chamadores conhecem o caminho de origem, o caminho traduzido de destino e o layout do projeto.

| Função | Escopo | Observações |
| --- | --- | --- |
| `rewrite_markdown_paths` | Corpo Markdown e frontmatter | Reescreve links do Markdown e campos de caminho do frontmatter suportados para um destino traduzido. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Aplica reescrita de caminhos Markdown a cada célula Markdown e deixa células não-Markdown inalteradas. |

O argumento `policy` pode ser um dicionário com estes campos:

| Campo | Obrigatório | Propósito |
| --- | --- | --- |
| `language_code` | Sim | Código de idioma alvo, como `"ko"` ou `"pt-BR"`. |
| `root_dir` | Não | Raiz do projeto fonte. Padrão é `"."`. |
| `translations_dir` | Não | Diretório de saída de tradução de texto. Padrão `translations` sob `root_dir`. |
| `translated_images_dir` | Não | Diretório de saída de imagens traduzidas. Padrão `translated_images` sob `root_dir`. |
| `translation_types` | Não | Tipos de tradução habilitados. Padrão: Markdown, notebooks e imagens. |
| `lang_subdir` | Não | Subdiretório opcional sob cada pasta de idioma. |

## Parâmetros de Tradução do Projeto

| Parâmetro | Tipo | Padrão | Propósito |
| --- | --- | --- | --- |
| `language_codes` | `str` | Obrigatório | Códigos de idiomas alvo separados por espaço, como `"ko ja fr"`, ou `"all"`. Códigos de alias são normalizados para valores canônicos BCP 47. |
| `root_dir` | `str` | `"."` | Raiz do projeto para um único alvo de tradução. Ignorado quando `root_dirs` ou `groups` são fornecidos. |
| `update` | `bool` | `False` | Excluir e recriar traduções existentes para os idiomas selecionados. |
| `images` | `bool` | `False` | Incluir tradução de imagens. Requer configuração do Azure AI Vision. |
| `markdown` | `bool` | `False` | Incluir tradução de Markdown. |
| `notebook` | `bool` | `False` | Incluir tradução de notebooks Jupyter. |
| `debug` | `bool` | `False` | Ativar logs de depuração. |
| `save_logs` | `bool` | `False` | Salvar arquivos de log no nível DEBUG sob o diretório raiz `logs/`. |
| `yes` | `bool` | `True` | Confirma automaticamente prompts para uso programático e em CI. |
| `add_disclaimer` | `bool` | `False` | Adicionar avisos de tradução automática ao Markdown e notebooks traduzidos. |
| `translations_dir` | `str \| None` | `None` | Diretório personalizado de saída de tradução de texto. Caminhos relativos são resolvidos em relação a cada raiz. |
| `image_dir` | `str \| None` | `None` | Diretório personalizado de saída de imagens traduzidas. Caminhos relativos são resolvidos em relação a cada raiz. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Múltiplas raízes que compartilham as mesmas configurações de saída. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pares explícitos `(root_dir, translations_dir)`. Tem precedência sobre `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL do repositório usado ao renderizar a orientação da tabela de idiomas do README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termos de glossário a serem preservados durante a tradução. Termos duplicados e vazios são normalizados. |
| `dry_run` | `bool` | `False` | Estimar o volume de tradução e visualizar o comportamento da migração sem gravar arquivos. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Adaptador opcional de persistência accepted-baseline e candidate para atualizações incrementais de Markdown. Omiti-lo preserva o comportamento existente de arquivo completo. |

## Parâmetros de Revisão

`run_review` intencionalmente espelha a assinatura de `run_translation` quando possível para que a automação possa alternar entre fluxos de trabalho de tradução e revisão com ramificação mínima.

| Parâmetro | Tipo | Padrão | Propósito |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Pastas de idioma alvo para revisar. Strings separadas por espaço e iteráveis são aceitos. `"all"` revisa todos os idiomas de tradução descobertos. |
| `root_dir` | `str` | `"."` | Raiz do projeto para um único alvo de revisão. Ignorado quando `root_dirs` ou `groups` são fornecidos. |
| `markdown` | `bool` | `False` | Incluir arquivos fonte Markdown e MDX. |
| `notebook` | `bool` | `False` | Incluir arquivos fonte de notebooks Jupyter. |
| `images` | `bool` | `False` | Reservado para paridade com opções de tradução. Referências de links para imagens são verificadas a partir do Markdown. |
| `translations_dir` | `str \| None` | `None` | Diretório personalizado de saída de tradução de texto. Caminhos relativos são resolvidos em relação a cada raiz. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Múltiplas raízes que compartilham as mesmas configurações de saída. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pares explícitos `(root_dir, translations_dir)`. Tem precedência sobre `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Ref Git usado para limitar a revisão aos arquivos fonte alterados. |
| `readme_only` | `bool` | `False` | Revisar apenas `README.md` sob cada raiz de origem. A ausência do README de origem gera `ValueError`. |
| `output_format` | `str` | `"text"` | Formato de saída da revisão. Valores suportados são `"text"` e `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Tratar avisos como falhas além de erros. |
| `debug` | `bool` | `False` | Habilitar logs de depuração. |
| `save_logs` | `bool` | `False` | Salvar arquivos de log em nível DEBUG sob o diretório raiz `logs/`. |

Se nenhum de `markdown`, `notebook` ou `images` estiver definido, a API revisa Markdown, notebooks e referências de links de imagens quando aplicável. A revisão não chama um provedor LLM e não requer chaves de API.

## Requisitos de Configuração

APIs de tradução com suporte a provedores exigem configuração do provedor antes de traduzir:

- A tradução de Markdown e notebooks requer um provedor LLM. Configure Azure OpenAI, OpenAI ou Anthropic.
- A tradução de imagens requer Azure AI Vision além do provedor LLM.
- `run_translation` executa verificações de conectividade leves antes do início da tradução do projeto.
- As APIs assistidas por agentes `start_*_agent_translation` e `finish_*_agent_translation` não chamam os provedores LLM do Co-op Translator. O aplicativo host ou agente MCP traduz os blocos preparados.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` e `run_review` são determinísticos e não requerem credenciais de provedores.

Variáveis Azure OpenAI obrigatórias:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Variáveis OpenAI obrigatórias:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Variáveis Anthropic obrigatórias:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` e `ANTHROPIC_MAX_TOKENS` são opcionais. Microsoft Agent Framework é o cliente de modelo padrão para todos os provedores a partir do Co-op Translator 0.22.0. O Semantic Kernel ainda pode ser selecionado temporariamente com `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, mas isso emite um aviso de descontinuação; veja [configuração](configuration.md#model-client-backend) para o plano de remoção em etapas.

Variáveis Azure AI Vision obrigatórias para tradução de imagens:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` é determinístico e não requer configuração de LLM ou Azure AI Vision.

## Notas de Comportamento

- As APIs de tradução de conteúdo mantêm a tradução separada da reescrita de caminhos do projeto. Chame `rewrite_markdown_paths` ou `rewrite_notebook_paths` explicitamente quando o conteúdo traduzido precisar de links relativos ao projeto ajustados para um local de destino.
- As APIs de orquestração de projeto adicionam comportamento de projeto em torno da tradução de conteúdo, incluindo descoberta de arquivos, escrita de arquivos, reescrita de caminhos, metadados, limpeza e avisos opcionais.
- `run_translation` imprime resumos de progresso e estimativas através do mesmo relatador baseado em Rich usado pela CLI. A saída não interativa recorre a texto simples.
- `dry_run=True` calcula estimativas usando atualizações virtuais do README, mas não grava o README nem os arquivos de tradução.
- `groups` são processados sequencialmente. Uma estimativa agregada única é impressa antes do início do trabalho.
- Quando a tradução de imagens é selecionada, a configuração ausente do Vision gera um erro antes do início da tradução.
- Pastas de idioma existentes baseadas em alias são detectadas e podem ser migradas para nomes canônicos de pastas de idioma como parte da execução.
- `run_review` falha em arquivos traduzidos ausentes, metadados de tradução ausentes ou obsoletos, frontmatter/fences de código Markdown malformados e JSON de notebook traduzido inválido.
- `run_review` relata alvos de links locais de Markdown e imagens ausentes como avisos por padrão.

## Caminho de Chamada Interna

A API delega à mesma implementação central usada pela CLI:

Tradução:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content` ou `translate_image_content` para tradução em memória.
2. `co_op_translator.api.translation.rewrite_markdown_paths` ou `rewrite_notebook_paths` para pós-processamento explícito de caminhos.
3. `co_op_translator.api.translation.run_translation` para orquestração completa do projeto.
4. `co_op_translator.config.Config`, `LLMConfig` e `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixins de tradução de projeto focados para Markdown, notebooks e imagens.
8. Tradutores de Markdown, notebook, texto e imagem sob `co_op_translator.core`.

Revisão:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Verificações determinísticas sob `co_op_translator.review.checks`

As seguintes classes são úteis para mantenedores, mas não são exportadas como API estável em nível de pacote.

| Classe | Módulo | Responsabilidade |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordena a tradução em nível de projeto, gerenciamento de diretório, normalização de metadados por idioma e delegação para tradutores de Markdown, notebook e imagem. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Executa o trabalho assíncrono de processamento de arquivos para Markdown, notebooks, imagens, detecção de obsolescência e atualizações de metadados de tradução. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orquestra a leitura de arquivos Markdown, tradução de conteúdo, reescrita de caminhos, metadados, avisos e gravação. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orquestra a leitura de arquivos de notebook, tradução de células Markdown, reescrita de caminhos, metadados, avisos e gravação. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orquestra a descoberta de imagens fonte, tradução de imagens, caminhos de saída, metadados e gravação. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Encontra pares de Markdown traduzidos, avalia a qualidade da tradução e lê metadados de confiança para fluxos de trabalho de reparo de baixa confiança. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordena verificações de revisão determinísticas entre arquivos fonte, idiomas alvo e raízes de tradução configuradas. |
| `ReviewTarget` | `co_op_translator.review.targets` | Descreve uma raiz de origem e o diretório de saída de tradução revisado para essa raiz. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detecta pastas de idioma legadas com aliases e prepara planos de migração para nomes canônicos de pastas BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Carrega arquivos `.env` e verifica se os provedores LLM obrigatórios e Vision opcionais estão configurados. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Auto-detecta Azure OpenAI, OpenAI ou Anthropic, valida as variáveis de ambiente obrigatórias e executa verificações de conectividade do provedor. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detecta configuração do Azure AI Vision e executa verificações de conectividade para tradução de imagens. |