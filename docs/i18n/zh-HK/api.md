# Python API

穩定的公共 Python API 由 `co_op_translator.api` 匯出。大多數整合會使用下列其中一種工作流程：

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

大多數位於 `core`、`config`、`review` 和 `utils` 底下的低階模組是由這些 API 入口點使用的實作細節。

MCP 用戶端透過 [MCP Server](mcp.md) 使用相同的公共 API。若直接從 Python 呼叫請使用這一頁，而若要向代理或編輯器暴露 Co-op Translator，請參閱 MCP 指南。若您在 CLI、Python API 與 MCP 之間選擇，請先參考 [選擇您的工作流程](workflows.md)。

## First-Time API Flow

如果您從 Python 程式碼呼叫 Co-op Translator，請從這裡開始：

1. 如非僅準備送給 host-agent 翻譯的 Markdown 或 notebook 分段，請依照 [Configuration](configuration.md) 中的說明設定 LLM 提供者。
2. 決定您的應用程式是否負責檔案 I/O。
3. 當您的應用程式讀寫單一檔案時，使用內容 API。
4. 當 Co-op Translator 應像 CLI 一樣處理整個倉庫時，使用 `run_translation`。
5. 如需在自動化中進行確定性的檢查，翻譯後使用 `run_review`。

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

當您已經有檔案、編輯器緩衝區、notebook 載荷、MCP 請求或自訂管線輸入，且您的程式負責檔案 I/O，請使用此工作流程：

1. 讀取來源內容。
2. 呼叫內容翻譯 API。
3. 若翻譯後的內容將寫入專案翻譯資料夾，則可選地呼叫路徑重寫 API。
4. 將結果儲存或回傳給您的應用程式。

內容翻譯 API 不會執行專案探索、不會寫入 metadata、不會附加免責聲明，且不會自動重寫連結。

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

如果翻譯後的 Markdown 不會放在 Co-op Translator 的專案結構中，請跳過 `rewrite_markdown_paths`，直接儲存翻譯後的字串。

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

`translate_notebook_content` 會翻譯 Markdown 儲存格並保留非 Markdown 儲存格。路徑重寫僅套用於 Markdown 儲存格。

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

`translate_image_content` 讀取來源影像並回傳已渲染的 `PIL.Image.Image`。它不會寫入已翻譯影像的 metadata。

## Scenario 2: Translate an Entire Repository

當您希望 Python API 的行為像 `translate` CLI 一樣時，使用此工作流程。`run_translation` 會發現支援的檔案、翻譯選定的內容類型、重寫路徑、寫出輸出檔案、更新 metadata，並執行翻譯維護工作（例如清理）。

`run_translation` 是首選的專案協調入口。`translate_project` 作為相容性別名匯出，其行為相同。

將當前倉庫中的 Markdown 檔案翻譯成韓文與日文：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

只翻譯特定專案根目錄中的 notebooks：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

預覽翻譯量而不寫入檔案：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

一次呼叫翻譯多個內容根目錄：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

將翻譯寫入明確的輸出群組：

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

當每個語言都應包含巢狀子目錄時，使用 per-language 的佔位符：

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

如果未設定 `markdown`、`notebook` 或 `images`，API 將翻譯所有支援類型：Markdown、notebooks 和 images。

## Review Translated Output

`run_review` 在沒有 LLM 或 Vision 憑證的情況下執行確定性的翻譯檢查。

!!! note "Beta"
    `run_review` 是一個測試階段的確定性審查 API。它不會呼叫模型提供者或寫入檔案，但檢查與問題的 schema 可能會演進。

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

只檢查相對於基底 ref 有變更的檔案，並輸出 GitHub 風格的格式：

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

## Copy-Paste API Examples

翻譯 Markdown 內容而不寫檔：

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

翻譯並重寫 Markdown 連結：

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

從 Python 翻譯一個倉庫：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

翻譯多個根目錄：

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

保留詞彙表術語：

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

## Public Entry Points

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

## Content Translation APIs

內容翻譯 API 適用於那些內容已在記憶中（例如編輯器外掛、MCP 工具、notebook 處理器或自訂管線）的整合。

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Translates Markdown content only. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Translates Markdown cells and preserves non-Markdown cells. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Extracts and translates image text, then returns a rendered image. It does not save translated image metadata. |

`translate_markdown_content` 和 `translate_notebook_content` 可透過它們的選項接受可選的 `source_path`。該路徑會作為上下文傳遞給翻譯器；呼叫方仍需在翻譯後負責任何專案特定的路徑重寫。

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

相同的選項也可以以字典形式傳遞：

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted API 不會由 Co-op Translator 呼叫 Azure OpenAI 或 OpenAI。它們會準備 Markdown 或 notebook 分段供 host agent 翻譯，然後從已翻譯的分段重建最終內容。

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

此工作流程主要針對 MCP 主機。如果您需要由 Co-op Translator 管理提供者呼叫的生產環境倉庫翻譯，請使用 `translate_markdown_content`、`translate_notebook_content` 或 `run_translation`。

## Path Rewriting APIs

路徑重寫 API 不執行任何翻譯。它們在呼叫方知道來源路徑、翻譯後的目標路徑與專案佈局後，更新連結與 frontmatter 路徑。

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

`policy` 參數可以是一個包含下列欄位的字典：

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Defaults to Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Space-separated target language codes, such as `"ko ja fr"`, or `"all"`. Alias codes are normalized to canonical BCP 47 values. |
| `root_dir` | `str` | `"."` | Project root for a single translation target. Ignored when `root_dirs` or `groups` are supplied. |
| `update` | `bool` | `False` | Delete and recreate existing translations for the selected languages. |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files under the root `logs/` directory. |
| `yes` | `bool` | `True` | Auto-confirm prompts for programmatic and CI usage. |
| `add_disclaimer` | `bool` | `False` | Add machine translation disclaimers to translated Markdown and notebooks. |
| `translations_dir` | `str \| None` | `None` | Custom text translation output directory. Relative paths resolve against each root. |
| `image_dir` | `str \| None` | `None` | Custom translated image output directory. Relative paths resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Multiple roots that share the same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. Takes precedence over `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository URL used when rendering README language table guidance. |
| `glossaries` | `Iterable[str] \| None` | `None` | Glossary terms to preserve during translation. Duplicates and blank terms are normalized. |
| `dry_run` | `bool` | `False` | Estimate translation volume and preview migration behavior without writing files. |

## Review Parameters

`run_review` 有意在可能的情況下模仿 `run_translation` 的簽名，以便自動化可以在翻譯與審查工作流程之間以最小分支切換。

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | 自訂文字翻譯輸出目錄。相對路徑會相對每個根目錄解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 共用相同輸出設定的多個根目錄。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 顯式的 `(root_dir, translations_dir)` 配對。優先於 `root_dirs`。 |
| `changed_from` | `str \| None` | `None` | 用於限制審查至已更改來源檔案的 Git ref。 |
| `output_format` | `str` | `"text"` | 審查輸出格式。支援的值為 `"text"` 和 `"github"`。 |
| `fail_on_warnings` | `bool` | `False` | 將警告視為與錯誤一樣的失敗。 |
| `debug` | `bool` | `False` | 啟用偵錯日誌紀錄。 |
| `save_logs` | `bool` | `False` | 將 DEBUG 級別的日誌檔案儲存於根目錄下的 `logs/` 目錄。 |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## 配置要求

需要由提供者支援的翻譯 API 在翻譯前先進行提供者設定：

- Markdown 和筆記本翻譯需要 LLM 提供者。請設定 Azure OpenAI 或 OpenAI 其中之一。
- 影像翻譯除了需要 LLM 提供者外，還需要 Azure AI Vision。
- `run_translation` 在專案翻譯開始前執行輕量的連線檢查。
- 受代理協助的 `start_*_agent_translation` 與 `finish_*_agent_translation` API 不會呼叫 Co-op Translator LLM 提供者。主機應用程式或 MCP 代理會翻譯已準備好的區塊。
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, 與 `run_review` 為決定性（deterministic）操作，且不需要提供者憑證。

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

## 行為說明

- 內容翻譯的 API 將翻譯與專案路徑重寫分開。當翻譯後的內容需要為目標位置調整專案相對連結時，請明確呼叫 `rewrite_markdown_paths` 或 `rewrite_notebook_paths`。
- 專案協調（orchestration）API 在內容翻譯周圍加入專案行為，包含檔案發現、寫入、路徑重寫、metadata、清理，以及可選的免責聲明。
- `run_translation` 透過 Click 列印進度與估算摘要，以符合 CLI 的使用者體驗。
- `dry_run=True` 使用虛擬的 README 更新來計算估算，但不會寫入 README 或翻譯檔案。
- `groups` 將依序處理。工作開始前會列印單一的總估算。
- 選擇影像翻譯時，若缺少 Vision 設定，會在翻譯開始前引發錯誤。
- 會偵測現有以別名為基礎的語言資料夾，並可在執行期間將其遷移至規範的語言資料夾名稱。
- `run_review` 會在翻譯檔案遺失、翻譯 metadata 遺失或過時、Markdown frontmatter/程式碼區塊（code fences）格式錯誤，或翻譯後的 notebook JSON 無效時失敗。
- `run_review` 預設會將本地 Markdown 與影像連結目標缺失報告為警告。

## 內部呼叫路徑

The API delegates to the same core implementation used by the CLI:

翻譯：

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` 用於記憶體內翻譯。
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` 用於明確的路徑後處理。
3. `co_op_translator.api.translation.run_translation` 用於完整的專案協調。
4. `co_op_translator.config.Config`, `LLMConfig` 與 `VisionConfig`。
5. `co_op_translator.core.project.ProjectTranslator`。
6. `co_op_translator.core.project.TranslationManager`。
7. 專注於專案翻譯的 mixin，用於 Markdown、筆記本與影像。
8. 位於 `co_op_translator.core` 下的 Markdown、筆記本、文字與影像翻譯器。

審查：

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. 位於 `co_op_translator.review.checks` 下的決定性檢查

下列類別對維護者有用，但並未作為套件等級的穩定 API 匯出。

| 類別 | 模組 | 責任 |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | 協調專案層級的翻譯、目錄管理、每語言 metadata 正規化，並委派給 Markdown、筆記本與影像翻譯器。 |
| `TranslationManager` | `co_op_translator.core.project.translation` | 執行 Markdown、筆記本、影像、過時檢測，以及翻譯 metadata 更新的非同步檔案處理工作。 |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | 協調 Markdown 檔案讀取、內容翻譯、路徑重寫、metadata、免責聲明，以及寫入。 |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | 協調筆記本檔案讀取、Markdown 儲存格翻譯、路徑重寫、metadata、免責聲明，以及寫入。 |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | 協調來源影像發現、影像翻譯、輸出路徑、metadata，以及寫入。 |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 尋找已翻譯的 Markdown 配對、評估翻譯品質，並讀取信心（confidence）metadata，用於低信心修復流程。 |
| `ReviewRunner` | `co_op_translator.review.runner` | 協調跨來源檔案、目標語言與已配置的翻譯根目錄的決定性審查檢查。 |
| `ReviewTarget` | `co_op_translator.review.targets` | 描述來源根目錄以及該根目錄所審查的翻譯輸出目錄。 |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | 偵測舊有別名的語言資料夾，並準備遷移至規範 BCP 47 資料夾的計畫。 |
| `Config` | `co_op_translator.config.base_config` | 載入 `.env` 檔案並檢查是否已設定必要的 LLM 與選用的 Vision 提供者。 |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | 自動偵測 Azure OpenAI 或 OpenAI、驗證必要的環境變數，並執行提供者連線檢查。 |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | 偵測 Azure AI Vision 設定並執行影像翻譯的連線檢查。 |