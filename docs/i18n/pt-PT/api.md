# API Python

A API pública estável em Python é exportada de `co_op_translator.api`. A maioria das integrações usa um destes fluxos de trabalho:

| Cenário | Use quando | Principais APIs |
| --- | --- | --- |
| Translate individual files or documents | A sua aplicação lê o conteúdo fonte, chama Co-op Translator para tradução, e decide onde guardar o resultado. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | O seu host MCP ou modelo de aplicação irá traduzir fragmentos, enquanto o Co-op Translator trata da divisão em blocos e da reconstrução. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Pretende que a API Python se comporte como a CLI e trate da descoberta, caminhos de saída, metadados, limpeza e escritas. | `run_translation` |

A maioria dos módulos de baixo nível sob `core`, `config`, `review` e `utils` são detalhes de implementação usados por estes pontos de entrada da API.

Os clientes MCP usam a mesma API pública através do [Servidor MCP](mcp.md). Use esta página ao chamar Python diretamente, e o guia MCP ao expor Co-op Translator a um agente ou editor. Se estiver a decidir entre CLI, API Python, e MCP, comece por [Escolha o seu fluxo de trabalho](workflows.md).

## Fluxo inicial da API

Comece aqui se estiver a chamar Co-op Translator a partir de código Python:

1. Configure um fornecedor de LLM conforme descrito em [Configuração](configuration.md), a menos que esteja apenas a preparar fragmentos Markdown ou de notebooks para tradução por um agente anfitrião.
2. Decida se a sua aplicação gere a E/S de ficheiros.
3. Use as APIs de conteúdo quando a sua aplicação lê e escreve ficheiros individuais.
4. Use `run_translation` quando o Co-op Translator deve processar um repositório como a CLI.
5. Use `run_review` depois da tradução se precisar de verificações determinísticas em automação.

| Objetivo | API para começar |
| --- | --- |
| Traduzir uma string ou ficheiro Markdown | `translate_markdown_content` |
| Traduzir um payload de notebook | `translate_notebook_content` |
| Traduzir uma imagem | `translate_image_content` |
| Permitir que um agente anfitrião traduza fragmentos de Markdown ou notebooks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Reescrever links traduzidos após escolher um caminho de saída | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Traduzir um repositório completo | `run_translation` |
| Rever a saída traduzida | `run_review` |

## Cenário 1: Traduzir Ficheiros ou Documentos Individuais

Use este fluxo de trabalho quando já tiver um ficheiro, buffer do editor, payload de notebook, pedido MCP, ou entrada de pipeline personalizada. O seu código gere a E/S de ficheiros:

1. Leia o conteúdo fonte.
2. Chame uma API de tradução de conteúdo.
3. Opcionalmente chame uma API de reescrita de caminhos se o conteúdo traduzido for gravado numa pasta de tradução do projeto.
4. Guarde ou devolva o resultado a partir da sua aplicação.

As APIs de tradução de conteúdo não executam a descoberta de projeto, não escrevem metadados, não acrescentam avisos, e não reescrevem links automaticamente.

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

Se o Markdown traduzido não ficar numa estrutura de projeto do Co-op Translator, omita `rewrite_markdown_paths` e guarde a string traduzida diretamente.

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

`translate_notebook_content` traduz células Markdown e preserva células não Markdown. A reescrita de caminhos é aplicada apenas às células Markdown.

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

`translate_image_content` lê a imagem fonte e devolve uma `PIL.Image.Image` renderizada. Não grava metadados da imagem traduzida.

## Cenário 2: Traduzir um Repositório Inteiro

Use este fluxo de trabalho quando quiser que a API Python se comporte como a CLI `translate`. O `run_translation` descobre ficheiros suportados, traduz tipos de conteúdo selecionados, reescreve caminhos, escreve ficheiros de saída, atualiza metadados, e executa tarefas de manutenção de tradução, como limpeza.

`run_translation` é o ponto de entrada preferido para orquestração de projeto. `translate_project` é exportado como um alias de compatibilidade com o mesmo comportamento.

Traduzir ficheiros Markdown no repositório atual para coreano e japonês:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Traduzir apenas notebooks a partir de uma raiz de projeto específica:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Pré-visualizar o volume de tradução sem gravar ficheiros:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Traduzir múltiplas raízes de conteúdo numa chamada:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Gravar traduções em grupos de saída explícitos:

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

Se nenhum de `markdown`, `notebook`, ou `images` estiver definido, a API traduz todos os tipos suportados: Markdown, notebooks, e imagens.

## Rever a Saída Traduzida

`run_review` executa verificações determinísticas de tradução sem credenciais LLM ou Vision.

!!! note "Beta"
    `run_review` é uma API de revisão determinística em beta. Não invoca fornecedores de modelos nem grava ficheiros, mas os esquemas de verificações e de issues podem evoluir.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Rever apenas ficheiros alterados em comparação com uma referência base e imprimir saída em formato GitHub:

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

Traduzir conteúdo Markdown sem gravar ficheiros:

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

Traduzir e reescrever links Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Traduzir um repositório a partir de Python:

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

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## APIs de Tradução de Conteúdo

As APIs de tradução de conteúdo destinam-se a integrações que já têm conteúdo em memória, como uma extensão de editor, ferramenta MCP, processador de notebooks, ou pipeline personalizada.

| Função | Entrada | Saída | E/S de Ficheiros | Notas |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Não | Assíncrono. Traduz apenas conteúdo Markdown. Não reescreve links, não escreve metadados, nem acrescenta avisos. |
| `translate_notebook_content` | Notebook JSON `str` ou `dict` | Notebook JSON `str` | Não | Assíncrono. Traduz células Markdown e preserva células não-Markdown. Não reescreve links, não escreve metadados, nem acrescenta avisos. |
| `translate_image_content` | Caminho da imagem | `PIL.Image.Image` | Lê apenas a imagem fonte | Síncrono. Extrai e traduz o texto da imagem, depois devolve uma imagem renderizada. Não guarda metadados da imagem traduzida. |

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

As APIs assistidas por agente não chamam o Azure OpenAI nem o OpenAI a partir do Co-op Translator. Preparam fragmentos Markdown ou de notebooks para o agente anfitrião traduzir, e depois reconstrói o conteúdo final a partir dos fragmentos traduzidos.

| Função | Finalidade |
| --- | --- |
| `start_markdown_agent_translation` | Devolve um trabalho Markdown autónomo com fragmentos, prompts e estado de reconstrução. |
| `finish_markdown_agent_translation` | Reconstrói Markdown a partir de um trabalho e dos fragmentos traduzidos pelo agente anfitrião. |
| `start_notebook_agent_translation` | Devolve um trabalho de notebook com fragmentos de células Markdown para tradução pelo agente anfitrião. |
| `finish_notebook_agent_translation` | Reconstrói o JSON do notebook preservando células de código, saídas e metadados. |

Este fluxo de trabalho destina-se principalmente a hosts MCP. Se precisar de tradução de repositório em produção com o Co-op Translator a gerir chamadas a fornecedores, use `translate_markdown_content`, `translate_notebook_content`, ou `run_translation`.

## APIs de Reescrita de Caminhos

As APIs de reescrita de caminhos não realizam tradução. Atualizam links e caminhos no frontmatter depois dos chamadores saberem o caminho fonte, o caminho alvo traduzido, e a estrutura do projeto.

| Função | Âmbito | Notas |
| --- | --- | --- |
| `rewrite_markdown_paths` | Corpo Markdown e frontmatter | Reescreve links Markdown e campos suportados de caminho no frontmatter para um alvo traduzido. |
| `rewrite_notebook_paths` | Células Markdown no JSON do notebook | Aplica a reescrita de caminhos Markdown a cada célula Markdown e deixa as células não Markdown inalteradas. |

O argumento `policy` pode ser um dicionário com estes campos:

| Campo | Obrigatório | Finalidade |
| --- | --- | --- |
| `language_code` | Sim | Código do idioma de destino, como `"ko"` ou `"pt-BR"`. |
| `root_dir` | Não | Raiz do projeto fonte. Por predefinição `"."`. |
| `translations_dir` | Não | Diretório de saída para tradução de texto. Por predefinição `translations` sob `root_dir`. |
| `translated_images_dir` | Não | Diretório de saída para imagens traduzidas. Por predefinição `translated_images` sob `root_dir`. |
| `translation_types` | Não | Tipos de tradução ativados. Por predefinição Markdown, notebooks e imagens. |
| `lang_subdir` | Não | Subdiretório opcional sob cada pasta de idioma. |

## Parâmetros de Tradução de Projeto

| Parâmetro | Tipo | Predefinição | Finalidade |
| --- | --- | --- | --- |
| `language_codes` | `str` | Obrigatório | Códigos de idioma de destino separados por espaço, como `"ko ja fr"`, ou `"all"`. Códigos de alias são normalizados para valores BCP 47 canónicos. |
| `root_dir` | `str` | `"."` | Raiz do projeto para um único alvo de tradução. Ignorado quando `root_dirs` ou `groups` são fornecidos. |
| `update` | `bool` | `False` | Eliminar e recriar traduções existentes para as línguas selecionadas. |
| `images` | `bool` | `False` | Incluir tradução de imagens. Requer configuração do Azure AI Vision. |
| `markdown` | `bool` | `False` | Incluir tradução de Markdown. |
| `notebook` | `bool` | `False` | Incluir tradução de Jupyter notebooks. |
| `debug` | `bool` | `False` | Ativar logging de debug. |
| `save_logs` | `bool` | `False` | Guardar ficheiros de log ao nível DEBUG sob o diretório raiz `logs/`. |
| `yes` | `bool` | `True` | Auto-confirmar prompts para uso programático e CI. |
| `add_disclaimer` | `bool` | `False` | Adicionar avisos de tradução automática aos Markdown e notebooks traduzidos. |
| `translations_dir` | `str \| None` | `None` | Diretório de saída personalizado para tradução de texto. Caminhos relativos resolvem em relação a cada raiz. |
| `image_dir` | `str \| None` | `None` | Diretório de saída personalizado para imagens traduzidas. Caminhos relativos resolvem em relação a cada raiz. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Múltiplas raízes que partilham as mesmas definições de saída. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pares explícitos `(root_dir, translations_dir)`. Tem precedência sobre `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL do repositório usado ao renderizar a orientação da tabela de idiomas no README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termos de glossário a preservar durante a tradução. Duplicados e termos vazios são normalizados. |
| `dry_run` | `bool` | `False` | Estimar o volume de tradução e pré-visualizar o comportamento de migração sem gravar ficheiros. |

## Parâmetros de Revisão

`run_review` intencionalmente espelha a assinatura de `run_translation` sempre que possível para que a automação possa alternar entre fluxos de trabalho de tradução e revisão com ramificação mínima.

| Parâmetro | Tipo | Predefinição | Finalidade |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Pastas de idioma alvo a rever. Aceitam-se strings separadas por espaço e iteráveis. `"all"` revê todas as línguas de tradução descobertas. |
| `root_dir` | `str` | `"."` | Raiz do projeto para um único alvo de revisão. Ignorado quando `root_dirs` ou `groups` são fornecidos. |
| `markdown` | `bool` | `False` | Incluir ficheiros fonte Markdown e MDX. |
| `notebook` | `bool` | `False` | Incluir ficheiros fonte de Jupyter notebooks. |
| `images` | `bool` | `False` | Reservado para paridade com as opções de tradução. Referências a imagens são verificadas a partir do Markdown. |
| `translations_dir` | `str \| None` | `None` | Diretório de saída personalizado para tradução de texto. Caminhos relativos resolvem-se em relação a cada diretório raiz. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Vários diretórios raiz que partilham as mesmas definições de saída. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pares explícitos `(root_dir, translations_dir)`. Tem precedência sobre `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Referência Git usada para limitar a revisão a ficheiros de origem alterados. |
| `output_format` | `str` | `"text"` | Formato de saída da revisão. Valores suportados são `"text"` e `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Tratar avisos como falhas além dos erros. |
| `debug` | `bool` | `False` | Ativar o registo de depuração. |
| `save_logs` | `bool` | `False` | Guardar ficheiros de log de nível DEBUG no diretório raiz `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Requisitos de Configuração

As APIs de tradução suportadas por fornecedores requerem a configuração do fornecedor antes de traduzir:

- A tradução de Markdown e de notebooks requer um fornecedor LLM. Configure Azure OpenAI ou OpenAI.
- A tradução de imagens requer Azure AI Vision além do fornecedor LLM.
- `run_translation` executa verificações de conectividade leves antes de começar a tradução do projeto.
- As APIs assistidas por agente `start_*_agent_translation` e `finish_*_agent_translation` não invocam os fornecedores LLM do Co-op Translator. A aplicação anfitriã ou o agente MCP traduz os blocos preparados.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` are deterministic and do not require provider credentials.

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` is deterministic and does not require Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## Notas de Funcionamento

- As APIs de tradução de conteúdo mantêm a tradução separada da reescrita de caminhos do projeto. Chame `rewrite_markdown_paths` ou `rewrite_notebook_paths` explicitamente quando o conteúdo traduzido necessitar que os links relativos ao projeto sejam ajustados para um local de destino.
- As APIs de orquestração de projeto acrescentam comportamento de projeto em torno da tradução de conteúdo, incluindo descoberta de ficheiros, gravações, reescrita de caminhos, metadados, limpeza e avisos opcionais.
- `run_translation` imprime sumários de progresso e estimativas através do Click, correspondendo à experiência de utilizador da CLI.
- `dry_run=True` calcula estimativas usando atualizações virtuais do README, mas não escreve o README nem os ficheiros de tradução.
- `groups` são processados sequencialmente. Uma única estimativa agregada é impressa antes de o trabalho começar.
- Quando a tradução de imagens é selecionada, a falta de configuração do Vision gera um erro antes do início da tradução.
- Pastas de idioma baseadas em alias existentes são detetadas e podem ser migradas para nomes de pastas de idioma canónicos como parte da execução.
- `run_review` falha quando existem ficheiros traduzidos em falta, metadados de tradução em falta ou obsoletos, frontmatter/fences de código Markdown malformados, e JSON de notebooks traduzidos inválido.
- Por padrão, `run_review` reporta como avisos alvos locais de links Markdown e de imagens em falta.

## Caminho de Chamada Interno

A API delega na mesma implementação central usada pela CLI:

Tradução:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` para tradução em memória.
2. `co_op_translator.api.translation.rewrite_markdown_paths` ou `rewrite_notebook_paths` para pós-processamento explícito de caminhos.
3. `co_op_translator.api.translation.run_translation` para orquestração completa do projeto.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixins de tradução de projeto focados em Markdown, notebooks e imagens.
8. Tradutores de Markdown, notebook, texto e imagem sob `co_op_translator.core`.

Revisão:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Verificações determinísticas sob `co_op_translator.review.checks`

As seguintes classes são úteis para mantenedores, mas não são exportadas como API estável ao nível do pacote.

| Classe | Módulo | Responsabilidade |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordena a tradução ao nível do projeto, gestão de diretórios, normalização de metadados por idioma e delegação para os tradutores de Markdown, notebooks e imagens. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Executa o processamento assíncrono de ficheiros para Markdown, notebooks, imagens, deteção de ficheiros obsoletos e atualizações de metadados de tradução. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orquestra a leitura de ficheiros Markdown, tradução de conteúdo, reescrita de caminhos, metadados, avisos e escritas. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orquestra a leitura de ficheiros de notebooks, tradução de células Markdown, reescrita de caminhos, metadados, avisos e escritas. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orquestra a descoberta de imagens de origem, tradução de imagens, caminhos de saída, metadados e escritas. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Encontra pares Markdown traduzidos, avalia a qualidade da tradução e lê metadados de confiança para fluxos de trabalho de reparação de baixa confiança. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordena verificações determinísticas de revisão através dos ficheiros de origem, idiomas alvo e diretórios de tradução configurados. |
| `ReviewTarget` | `co_op_translator.review.targets` | Descreve uma raiz de origem e o diretório de saída de tradução revisto para essa raiz. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Deteta pastas de idiomas com aliases legados e prepara planos de migração para pastas canónicas BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Carrega ficheiros `.env` e verifica se os fornecedores LLM obrigatórios e o fornecedor Vision opcional estão configurados. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Deteta automaticamente Azure OpenAI ou OpenAI, valida as variáveis de ambiente obrigatórias e executa verificações de conectividade do fornecedor. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Deteta a configuração do Azure AI Vision e executa verificações de conectividade para tradução de imagens. |