# Python API

A API pública estável em Python é exportada de `co_op_translator.api`. A maioria das integrações usa um destes fluxos de trabalho:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Seu aplicativo lê o conteúdo fonte, chama o Co-op Translator para tradução e decide onde salvar o resultado. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Seu host MCP ou modelo de aplicação irá traduzir fragmentos, enquanto o Co-op Translator lida com o particionamento e reconstrução. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Você quer que a API Python se comporte como a CLI e gerencie descoberta, caminhos de saída, metadados, limpeza e gravações. | `run_translation` |

A maioria dos módulos de baixo nível em `core`, `config`, `review` e `utils` são detalhes de implementação usados por estes pontos de entrada da API.

Clientes MCP usam a mesma API pública através do [Servidor MCP](mcp.md). Use esta página quando chamar Python diretamente, e o guia MCP ao expor o Co-op Translator a um agente ou editor. Se você estiver decidindo entre CLI, API Python e MCP, comece com [Escolha Seu Fluxo de Trabalho](workflows.md).

## Fluxo inicial da API

Comece aqui se você estiver chamando o Co-op Translator a partir de código Python:

1. Configure um provedor LLM conforme descrito em [Configuração](configuration.md), a menos que você esteja apenas preparando fragmentos de Markdown ou notebook para tradução por um agente host.
2. Decida se seu aplicativo é responsável por E/S de arquivos.
3. Use as APIs de conteúdo quando seu aplicativo lê e grava arquivos individuais.
4. Use `run_translation` quando o Co-op Translator deve processar um repositório como a CLI.
5. Use `run_review` após a tradução se você precisar de verificações determinísticas em automação.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

Use este fluxo de trabalho quando você já tiver um arquivo, buffer do editor, conteúdo de notebook, solicitação MCP ou entrada de pipeline personalizada. Seu código é responsável pela E/S de arquivos:

1. Leia o conteúdo fonte.
2. Chame uma API de tradução de conteúdo.
3. Opcionalmente, chame uma API de reescrita de caminhos se o conteúdo traduzido for gravado em uma pasta de tradução do projeto.
4. Salve ou retorne o resultado pelo seu aplicativo.

As APIs de tradução de conteúdo não executam descoberta de projeto, não escrevem metadados, não acrescentam avisos de isenção de responsabilidade e não reescrevem links automaticamente.

### Markdown File

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

Se o Markdown traduzido não residir em um layout de projeto do Co-op Translator, pule `rewrite_markdown_paths` e salve a string traduzida diretamente.

### Notebook File

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

### Image File

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

`translate_image_content` lê a imagem fonte e retorna um `PIL.Image.Image` renderizado. Ele não grava metadados da imagem traduzida.

## Scenario 2: Translate an Entire Repository

Use este fluxo quando você quiser que a API Python se comporte como a CLI `translate`. `run_translation` descobre arquivos suportados, traduz tipos de conteúdo selecionados, reescreve caminhos, grava arquivos de saída, atualiza metadados e executa tarefas de manutenção de tradução, como limpeza.

`run_translation` é o ponto de entrada preferido para orquestração de projetos. `translate_project` é exportado como um alias de compatibilidade com o mesmo comportamento.

Traduza arquivos Markdown no repositório atual para coreano e japonês:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Traduza apenas notebooks de uma raiz de projeto específica:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Pré-visualize o volume de tradução sem gravar arquivos:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Traduza múltiplas raízes de conteúdo em uma única chamada:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Grave traduções em grupos de saída explícitos:

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

## Revisar Saída Traduzida

`run_review` executa verificações determinísticas de tradução sem credenciais LLM ou Vision.

!!! note "Beta"
    `run_review` é uma API beta de revisão determinística. Ela não chama provedores de modelos nem grava arquivos, mas os esquemas de verificações e problemas podem evoluir.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Revise apenas arquivos alterados em relação a uma referência base e imprima saída no formato GitHub:

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

Traduza e reescreva links Markdown:

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

As APIs de tradução de conteúdo destinam-se a integrações que já possuem conteúdo em memória, como uma extensão de editor, ferramenta MCP, processador de notebooks ou pipeline personalizado.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Assíncrono. Traduz apenas conteúdo Markdown. Não reescreve links, não escreve metadados e não acrescenta avisos de isenção de responsabilidade. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Assíncrono. Traduz células Markdown e preserva células não-Markdown. Não reescreve links, não escreve metadados e não acrescenta avisos de isenção de responsabilidade. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Síncrono. Extrai e traduz o texto da imagem, então retorna uma imagem renderizada. Não salva metadados da imagem traduzida. |

`translate_markdown_content` e `translate_notebook_content` aceitam um `source_path` opcional através de suas opções. O caminho é passado como contexto para o tradutor; os chamadores continuam responsáveis por qualquer reescrita de caminhos específica do projeto após a tradução.

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

As APIs assistidas por agente não chamam Azure OpenAI ou OpenAI a partir do Co-op Translator. Elas preparam fragmentos de Markdown ou notebook para um agente host traduzir e então reconstróem o conteúdo final a partir dos fragmentos traduzidos.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Retorna um job Markdown autocontido com fragmentos, prompts e estado de reconstrução. |
| `finish_markdown_agent_translation` | Reconstrói Markdown a partir de um job e fragmentos traduzidos pelo agente host. |
| `start_notebook_agent_translation` | Retorna um job de notebook com fragmentos de células Markdown para tradução por um agente host. |
| `finish_notebook_agent_translation` | Reconstrói o JSON do notebook preservando células de código, saídas e metadados. |

Este fluxo destina-se principalmente a hosts MCP. Se você precisa de tradução de repositório em produção com o Co-op Translator gerenciando chamadas a provedores, use `translate_markdown_content`, `translate_notebook_content` ou `run_translation`.

## APIs de Reescrita de Caminhos

As APIs de reescrita de caminhos não realizam tradução. Elas atualizam links e caminhos no frontmatter depois que os chamadores sabem o caminho fonte, o caminho alvo traduzido e o layout do projeto.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Reescreve links Markdown e campos de caminho no frontmatter suportados para um alvo traduzido. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Aplica a reescrita de caminhos Markdown a cada célula Markdown e deixa células não-Markdown inalteradas. |

O argumento `policy` pode ser um dicionário com estes campos:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Código do idioma alvo, como `"ko"` ou `"pt-BR"`. |
| `root_dir` | No | Raiz do projeto fonte. Padrão é `"."`. |
| `translations_dir` | No | Diretório de saída da tradução de texto. Padrão é `translations` dentro de `root_dir`. |
| `translated_images_dir` | No | Diretório de saída das imagens traduzidas. Padrão é `translated_images` dentro de `root_dir`. |
| `translation_types` | No | Tipos de tradução habilitados. Padrão são Markdown, notebooks e imagens. |
| `lang_subdir` | No | Subdiretório opcional sob cada pasta de idioma. |

## Parâmetros de Tradução de Projeto

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Códigos de idiomas alvo separados por espaço, como `"ko ja fr"`, ou `"all"`. Códigos de alias são normalizados para valores BCP 47 canônicos. |
| `root_dir` | `str` | `"."` | Raiz do projeto para um único alvo de tradução. Ignorado quando `root_dirs` ou `groups` são fornecidos. |
| `update` | `bool` | `False` | Excluir e recriar traduções existentes para os idiomas selecionados. |
| `images` | `bool` | `False` | Incluir tradução de imagens. Requer configuração do Azure AI Vision. |
| `markdown` | `bool` | `False` | Incluir tradução de Markdown. |
| `notebook` | `bool` | `False` | Incluir tradução de notebooks Jupyter. |
| `debug` | `bool` | `False` | Habilitar logs de depuração. |
| `save_logs` | `bool` | `False` | Salvar arquivos de log em nível DEBUG sob o diretório `logs/` na raiz. |
| `yes` | `bool` | `True` | Confirmar automaticamente prompts para uso programático e CI. |
| `add_disclaimer` | `bool` | `False` | Adicionar avisos de isenção de responsabilidade de tradução automática a Markdown e notebooks traduzidos. |
| `translations_dir` | `str \| None` | `None` | Diretório de saída de tradução de texto customizado. Caminhos relativos são resolvidos em relação a cada raiz. |
| `image_dir` | `str \| None` | `None` | Diretório de saída de imagens traduzidas customizado. Caminhos relativos são resolvidos em relação a cada raiz. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Múltiplas raízes que compartilham as mesmas configurações de saída. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pares explícitos `(root_dir, translations_dir)`. Tem precedência sobre `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL do repositório usado ao renderizar a orientação da tabela README por idioma. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termos de glossário a preservar durante a tradução. Duplicatas e termos em branco são normalizados. |
| `dry_run` | `bool` | `False` | Estimar o volume de tradução e pré-visualizar o comportamento de migração sem gravar arquivos. |

## Parâmetros de Revisão

`run_review` intencionalmente espelha a assinatura de `run_translation` quando possível para que a automação possa alternar entre fluxos de tradução e revisão com ramificação mínima.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Pastas de idioma alvo a revisar. Strings separadas por espaço e iteráveis são aceitos. `"all"` revisa todos os idiomas de tradução descobertos. |
| `root_dir` | `str` | `"."` | Raiz do projeto para um único alvo de revisão. Ignorado quando `root_dirs` ou `groups` são fornecidos. |
| `markdown` | `bool` | `False` | Incluir arquivos fonte Markdown e MDX. |
| `notebook` | `bool` | `False` | Incluir arquivos fonte de notebooks Jupyter. |
| `images` | `bool` | `False` | Reservado para paridade com opções de tradução. Referências a imagens são verificadas a partir de Markdown. |
| `translations_dir` | `str \| None` | `None` | Diretório de saída personalizado para traduções de texto. Caminhos relativos são resolvidos em relação a cada raiz. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Múltiplas raízes que compartilham as mesmas configurações de saída. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pares explícitos `(root_dir, translations_dir)`. Tem precedência sobre `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Ref do Git usada para limitar a revisão aos arquivos-fonte alterados. |
| `output_format` | `str` | `"text"` | Formato de saída da revisão. Valores suportados são `"text"` e `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Tratar avisos como falhas além de erros. |
| `debug` | `bool` | `False` | Habilitar logs de depuração. |
| `save_logs` | `bool` | `False` | Salvar arquivos de log em nível DEBUG no diretório raiz `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Requisitos de Configuração

Provider-backed translation APIs require provider configuration before translating:

- A tradução de Markdown e notebooks requer um provedor LLM. Configure Azure OpenAI ou OpenAI.
- A tradução de imagens requer Azure AI Vision além do provedor LLM.
- `run_translation` executa verificações de conectividade leves antes do início da tradução do projeto.
- As APIs assistidas por agente `start_*_agent_translation` e `finish_*_agent_translation` não chamam provedores LLM do Co-op Translator. A aplicação host ou o agente MCP traduz os blocos preparados.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` e `run_review` são determinísticos e não requerem credenciais de provedor.

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

`run_review` é determinístico e não requer configuração do Azure OpenAI, OpenAI, ou Azure AI Vision.

## Observações de Comportamento

- As APIs de tradução de conteúdo mantêm a tradução separada da reescrita de caminhos do projeto. Chame `rewrite_markdown_paths` ou `rewrite_notebook_paths` explicitamente quando o conteúdo traduzido precisar de ajustes nos links relativos ao projeto para um local de destino.
- As APIs de orquestração de projeto adicionam comportamento do projeto em torno da tradução de conteúdo, incluindo descoberta de arquivos, gravações, reescrita de caminhos, metadados, limpeza e isenções de responsabilidade opcionais.
- `run_translation` imprime resumos de progresso e estimativas através do Click, correspondendo à experiência do usuário CLI.
- `dry_run=True` calcula estimativas usando atualizações virtuais do README, mas não grava o README nem os arquivos de tradução.
- `groups` são processados sequencialmente. Uma única estimativa agregada é impressa antes do início do trabalho.
- Quando a tradução de imagens é selecionada, a falta de configuração do Vision gera um erro antes do início da tradução.
- Pastas de idioma existentes baseadas em alias são detectadas e podem ser migradas para nomes de pastas de idioma canônicos como parte da execução.
- `run_review` falha em arquivos traduzidos ausentes, metadados de tradução ausentes ou obsoletos, frontmatter/cercas de código Markdown malformadas, e JSON de notebook traduzido inválido.
- `run_review` relata destinos de links locais de Markdown e imagens ausentes como avisos por padrão.

## Caminho de Chamada Interno

The API delegates to the same core implementation used by the CLI:

Tradução:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` para tradução em memória.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` para pós-processamento explícito de caminhos.
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

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordena a tradução em nível de projeto, gerenciamento de diretório, normalização de metadados por idioma e delegação para tradutores de Markdown, notebook e imagem. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Realiza o processamento assíncrono de arquivos para Markdown, notebooks, imagens, detecção de obsolescência e atualizações de metadados de tradução. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orquestra a leitura de arquivos Markdown, tradução de conteúdo, reescrita de caminhos, metadados, isenções de responsabilidade e gravações. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orquestra a leitura de arquivos de notebook, tradução de células Markdown, reescrita de caminhos, metadados, isenções de responsabilidade e gravações. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orquestra a descoberta de imagens de origem, tradução de imagens, caminhos de saída, metadados e gravações. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Encontra pares de Markdown traduzidos, avalia a qualidade da tradução e lê metadados de confiança para fluxos de trabalho de reparo de baixa confiança. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordena verificações determinísticas de revisão entre arquivos de origem, idiomas-alvo e raízes de tradução configuradas. |
| `ReviewTarget` | `co_op_translator.review.targets` | Descreve uma raiz de origem e o diretório de saída de tradução revisado para essa raiz. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detecta pastas de idioma legadas com alias e prepara planos de migração para nomes de pasta canônicos BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Carrega arquivos `.env` e verifica se os provedores LLM necessários e Vision opcionais estão configurados. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Detecta automaticamente Azure OpenAI ou OpenAI, valida variáveis de ambiente necessárias e executa verificações de conectividade do provedor. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detecta a configuração do Azure AI Vision e executa verificações de conectividade para tradução de imagens. |