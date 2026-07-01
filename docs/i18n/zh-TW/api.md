# Python API

穩定的公開 Python API 從 `co_op_translator.api` 匯出。大多數整合會使用下面的工作流程之一：

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

大多數位於 `core`、`config`、`review` 和 `utils` 底下的低階模組都是這些 API 入口點所使用的實作細節。

MCP 用戶端透過 [MCP Server](mcp.md) 使用相同的公開 API。當直接從 Python 呼叫時請使用此頁面；當要將 Co-op Translator 暴露給代理或編輯器時請參閱 MCP 指南。如果你正在在 CLI、Python API 和 MCP 之間做選擇，請從 [Choose Your Workflow](workflows.md) 開始。

## First-Time API Flow

如果你從 Python 程式碼呼叫 Co-op Translator，請從這裡開始：

1. 如 [Configuration](configuration.md) 所述設定 LLM 提供者，除非你只是為主機代理翻譯準備 Markdown 或 notebook 片段。
2. 決定你的應用程式是否負責檔案 I/O。
3. 當你的應用程式讀寫單一檔案時使用內容 API。
4. 當 Co-op Translator 應像 CLI 一樣處理整個 repository 時使用 `run_translation`。
5. 如果需要在自動化中進行確定性檢查，則在翻譯後使用 `run_review`。

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

當你已經有一個檔案、編輯器緩衝區、notebook 載荷、MCP 請求或自訂管線輸入時，請使用此工作流程。你的程式碼負責檔案 I/O：

1. 讀取來源內容。
2. 呼叫內容翻譯 API。
3. 若翻譯後的內容將被寫入專案翻譯資料夾，則可選地呼叫路徑改寫 API。
4. 從你的應用程式儲存或回傳結果。

內容翻譯 API 不會執行專案發現、不會寫入 metadata、不會加入免責聲明，也不會自動改寫連結。

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

如果翻譯後的 Markdown 不會存放在 Co-op Translator 的專案結構中，請跳過 `rewrite_markdown_paths` 並直接儲存翻譯後的字串。

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

`translate_notebook_content` 會翻譯 Markdown 儲存格並保留非 Markdown 儲存格。路徑改寫僅套用到 Markdown 儲存格。

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

`translate_image_content` 會讀取來源影像並回傳一個渲染後的 `PIL.Image.Image`。它不會寫入翻譯後的影像 metadata。

## Scenario 2: Translate an Entire Repository

當你希望 Python API 行為類似 `translate` CLI 時使用此工作流程。`run_translation` 會發現支援的檔案、翻譯選定的內容類型、改寫路徑、寫入輸出檔案、更新 metadata，並執行翻譯維護任務（例如清理）。

`run_translation` 是偏好的專案編排入口點。`translate_project` 作為相容性別名匯出，具有相同行為。

將當前 repository 的 Markdown 檔案翻譯成韓語與日語：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

僅翻譯來自特定專案根目錄的 notebooks：

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

在一次呼叫中翻譯多個內容根目錄：

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

當每個語言應包含巢狀子目錄時使用每語言的佔位子目錄：

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

如果未設定 `markdown`、`notebook` 或 `images`，API 將翻譯所有支援的類型：Markdown、notebooks 與 images。

## Review Translated Output

`run_review` 可在不需要 LLM 或 Vision 憑證的情況下執行確定性翻譯檢查。

!!! note "Beta"
    `run_review` 是一個測試中的確定性檢查 API。它不會呼叫模型提供者或寫入檔案，但檢查和 issue 架構可能會變動。

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

只檢查相對基準 ref 有變更的檔案並印出 GitHub 風格的輸出：

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

在不寫檔的情況下翻譯 Markdown 內容：

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

翻譯並改寫 Markdown 連結：

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

從 Python 翻譯一個 repository：

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

保留術語表詞彙：

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

內容翻譯 API 適用於已經在記憶體中擁有內容的整合，例如編輯器延伸、MCP 工具、notebook 處理器或自訂管線。

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Translates Markdown content only. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Translates Markdown cells and preserves non-Markdown cells. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Extracts and translates image text, then returns a rendered image. It does not save translated image metadata. |

`translate_markdown_content` 和 `translate_notebook_content` 接受可選的 `source_path`（透過其選項）。該路徑會作為上下文傳遞給翻譯器；呼叫者仍需負責在翻譯後執行任何專案特定的路徑改寫。

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

代理協助的 API 不會由 Co-op Translator 呼叫 Azure OpenAI 或 OpenAI。它們會為主機代理準備 Markdown 或 notebook 片段以供翻譯，然後從主機代理翻譯過的片段重建最終內容。

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

此工作流程主要針對 MCP 主機。如果你需要 Co-op Translator 管理提供者呼叫的生產環境 repository 翻譯，請使用 `translate_markdown_content`、`translate_notebook_content` 或 `run_translation`。

## Path Rewriting APIs

路徑改寫 API 不執行翻譯。它們在呼叫者知道來源路徑、翻譯後目標路徑以及專案佈局後更新連結和 frontmatter 路徑。

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

`policy` 參數可以是一個包含這些欄位的字典：

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

`run_review` 故意在可能的情況下與 `run_translation` 的簽名相互對應，以便自動化可以在翻譯與檢查工作流程之間以最少的分支切換。

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | 自訂文字翻譯輸出目錄。相對路徑相對於每個根目錄解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 共享相同輸出設定的多個根目錄。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 明確的 `(root_dir, translations_dir)` 配對。優先於 `root_dirs`。 |
| `changed_from` | `str \| None` | `None` | 用於將審查限制為已變更原始檔案的 Git 參考。 |
| `output_format` | `str` | `"text"` | 審查輸出格式。支援的值為 `"text"` 和 `"github"`。 |
| `fail_on_warnings` | `bool` | `False` | 除了錯誤外，將警告也視為失敗。 |
| `debug` | `bool` | `False` | 啟用偵錯日誌。 |
| `save_logs` | `bool` | `False` | 將 DEBUG 級別的日誌檔案儲存在根目錄下的 `logs/` 目錄中。 |

如果未設定 `markdown`、`notebook` 或 `images`，API 將在適用的情況下審查 Markdown、notebook 與影像連結參考。審查不會調用 LLM 提供者，也不需要 API 金鑰。

## 設定需求

受提供者支援的翻譯 API 在翻譯前需要先設定提供者：

- Markdown 與 notebook 的翻譯需要一個 LLM 提供者。請設定 Azure OpenAI 或 OpenAI。
- 影像翻譯除了需要 LLM 提供者外，還需要 Azure AI Vision。
- `run_translation` 會在專案翻譯開始前執行輕量的連線檢查。
- 由代理協助的 `start_*_agent_translation` 與 `finish_*_agent_translation` API 不會調用 Co-op Translator 的 LLM 提供者。主機應用程式或 MCP 代理會翻譯已準備好的片段。
- `rewrite_markdown_paths`、`rewrite_notebook_paths` 與 `run_review` 是決定性的，且不需要提供者憑證。

必要的 Azure OpenAI 變數：

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

必要的 OpenAI 變數：

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

影像翻譯所需的 Azure AI Vision 變數：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` 是決定性的，且不需要 Azure OpenAI、OpenAI 或 Azure AI Vision 的設定。

## 行為說明

- 內容翻譯的 API 將翻譯與專案路徑重寫分離。當已翻譯的內容需要調整為目標位置的專案相對連結時，請明確呼叫 `rewrite_markdown_paths` 或 `rewrite_notebook_paths`。
- 專案協調 API 在內容翻譯周圍加入專案行為，包括檔案探索、寫入、路徑重寫、中繼資料、清理和可選的免責聲明。
- `run_translation` 透過 Click 輸出進度與估算摘要，符合 CLI 的使用者體驗。
- `dry_run=True` 使用虛擬的 README 更新來計算估算，但不會寫入 README 或翻譯檔案。
- `groups` 會依序處理。工作開始前會列印單一的總估算。
- 選擇影像翻譯時，若缺少 Vision 設定會在翻譯開始前拋出錯誤。
- 系統會偵測現有以別名為基礎的語言資料夾，並可在執行過程中將其遷移為規範的語言資料夾名稱。
- 若缺少已翻譯的檔案、缺失或陳舊的翻譯中繼資料、格式錯誤的 Markdown frontmatter/程式碼區塊（code fences），或無效的已翻譯 notebook JSON，`run_review` 將會失敗。
- `run_review` 預設會將本地缺失的 Markdown 與影像連結目標報告為警告。

## 內部呼叫路徑

API 會委派到與 CLI 相同的核心實作：

Translation:

1. 使用 `co_op_translator.api.translation.translate_markdown_content`、`translate_notebook_content` 或 `translate_image_content` 進行記憶體內翻譯。
2. 使用 `co_op_translator.api.translation.rewrite_markdown_paths` 或 `rewrite_notebook_paths` 進行明確的路徑後處理。
3. 使用 `co_op_translator.api.translation.run_translation` 進行完整的專案協調。
4. `co_op_translator.config.Config`、`LLMConfig` 與 `VisionConfig`。
5. `co_op_translator.core.project.ProjectTranslator`。
6. `co_op_translator.core.project.TranslationManager`。
7. 專注於 Markdown、notebook 與影像的專案翻譯 mixins。
8. 位於 `co_op_translator.core` 下的 Markdown、notebook、文字與影像翻譯器。

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. 位於 `co_op_translator.review.checks` 下的決定性檢查

下列類別對維護者有用，但不會作為封裝層級的穩定 API 匯出。

| 類別 | 模組 | 職責 |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | 協調專案層級的翻譯、目錄管理、各語言的中繼資料標準化，並委派給 Markdown、notebook 與影像翻譯器。 |
| `TranslationManager` | `co_op_translator.core.project.translation` | 執行 Markdown、notebook、影像的非同步檔案處理、陳舊偵測，以及翻譯中繼資料更新等工作。 |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | 協調 Markdown 檔案讀取、內容翻譯、路徑重寫、中繼資料、免責聲明與寫入。 |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | 協調 notebook 檔案讀取、Markdown 格式儲存格的翻譯、路徑重寫、中繼資料、免責聲明與寫入。 |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | 協調原始影像的發現、影像翻譯、輸出路徑、中繼資料與寫入。 |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 尋找已翻譯的 Markdown 配對、評估翻譯品質，並讀取低信心修復工作流程所需的信心中繼資料。 |
| `ReviewRunner` | `co_op_translator.review.runner` | 協調針對來源檔案、目標語言與已設定翻譯根目錄的決定性審查。 |
| `ReviewTarget` | `co_op_translator.review.targets` | 描述一個來源根目錄以及針對該根目錄所審查的翻譯輸出目錄。 |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | 偵測舊有的別名語言資料夾，並準備轉換為規範 BCP 47 資料夾的遷移計畫。 |
| `Config` | `co_op_translator.config.base_config` | 載入 `.env` 檔案，並檢查是否已設定必要的 LLM 與可選的 Vision 提供者。 |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | 自動偵測 Azure OpenAI 或 OpenAI，驗證必要的環境變數，並執行提供者連線檢查。 |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | 偵測 Azure AI Vision 的設定，並執行影像翻譯的連線檢查。 |