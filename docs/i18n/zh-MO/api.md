# Python API

穩定的公開 Python API 從 `co_op_translator.api` 匯出。大多數整合使用下列其中一種工作流程：

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | 您的應用程式讀取來源內容，呼叫 Co-op Translator 進行翻譯，並決定儲存結果的位置。 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | 您的 MCP 主機或應用模型會翻譯區塊，而 Co-op Translator 負責區塊切分與重組。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | 您希望 Python API 的行為類似 CLI，並處理檔案發現、輸出路徑、metadata、清理與寫入。 | `run_translation` |

位於 `core`、`config`、`review` 和 `utils` 底下的大多數較低階模組是供這些 API 入口點使用的實作細節。

MCP 用戶端透過 [MCP Server](mcp.md) 使用相同的公開 API。直接從 Python 呼叫時使用本頁，當要將 Co-op Translator 暴露給 agent 或編輯器時則參考 MCP 指南。如果您在 CLI、Python API 與 MCP 之間抉擇，請從 [選擇您的工作流程](workflows.md) 開始。

## First-Time API Flow

如果您從 Python 程式碼呼叫 Co-op Translator，請從這裡開始：

1. 依照 [設定](configuration.md) 中的說明設定 LLM 提供者，除非您只是在為 host-agent 翻譯準備 Markdown 或 notebook 區塊。
2. 決定您的應用程式是否負責檔案 I/O。
3. 當應用程式需要讀寫單一檔案時，使用內容 API。
4. 如果要讓 Co-op Translator 類似 CLI 一樣處理一個 repository，請使用 `run_translation`。
5. 若在自動化流程需要確定性檢查，翻譯後請使用 `run_review`。

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

Use this workflow when you already have a file, editor buffer, notebook payload, MCP request, or custom pipeline input. Your code owns file I/O:

1. Read the source content.
2. Call a content translation API.
3. Optionally call a path rewriting API if the translated content will be written into a project translation folder.
4. Save or return the result from your application.

The content translation APIs do not run project discovery, do not write metadata, do not append disclaimers, and do not rewrite links automatically.

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

If the translated Markdown will not live in a Co-op Translator project layout, skip `rewrite_markdown_paths` and save the translated string directly.

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

`translate_notebook_content` translates Markdown cells and preserves non-Markdown cells. Path rewriting is applied only to Markdown cells.

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

`translate_image_content` reads the source image and returns a rendered `PIL.Image.Image`. It does not write translated image metadata.

## Scenario 2: Translate an Entire Repository

Use this workflow when you want the Python API to behave like the `translate` CLI. `run_translation` discovers supported files, translates selected content types, rewrites paths, writes output files, updates metadata, and performs translation maintenance tasks such as cleanup.

`run_translation` is the preferred project orchestration entry point. `translate_project` is exported as a compatibility alias with the same behavior.

Translate Markdown files in the current repository into Korean and Japanese:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Translate only notebooks from a specific project root:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Preview translation volume without writing files:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Translate multiple content roots in one call:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Write translations into explicit output groups:

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

Use a per-language placeholder when each language should contain a nested subdirectory:

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

If none of `markdown`, `notebook`, or `images` are set, the API translates all supported types: Markdown, notebooks, and images.

## Review Translated Output

`run_review` runs deterministic translation checks without LLM or Vision credentials.

!!! note "Beta"
    `run_review` is a beta deterministic review API. It does not call model providers or write files, but checks and issue schemas may evolve.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Review only files changed against a base ref and print GitHub-flavored output:

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

Translate Markdown content without file writes:

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

Translate and rewrite Markdown links:

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

Translate a repository from Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Translate multiple roots:

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

Preserve glossary terms:

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

內容翻譯 API 適用於已經在記憶體中擁有內容的整合，例如編輯器擴充、MCP 工具、notebook 處理器或自訂管線。

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | 否 | 非同步。僅翻譯 Markdown 內容。不會重寫連結、寫入 metadata 或附加免責聲明。 |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | 否 | 非同步。翻譯 Markdown cells 並保留非 Markdown cells。不會重寫連結、寫入 metadata 或附加免責聲明。 |
| `translate_image_content` | Image path | `PIL.Image.Image` | 僅讀取來源影像 | 同步。擷取並翻譯影像文字，然後回傳渲染後的影像。它不會儲存已翻譯影像的 metadata。 |

`translate_markdown_content` 與 `translate_notebook_content` 可透過其選項接受可選的 `source_path`。該路徑會作為上下文傳給翻譯器；呼叫者仍需負責翻譯後的任何專案特定路徑重寫。

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

The same options can be passed as dictionaries:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent 協助的 API 不會從 Co-op Translator 呼叫 Azure OpenAI 或 OpenAI。它們準備 Markdown 或 notebook 區塊供 host agent 翻譯，然後從已翻譯的區塊重建最終內容。

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | 回傳一個自包含的 Markdown 工作（包含區塊、提示與重組狀態）。 |
| `finish_markdown_agent_translation` | 根據工作與 host-agent 已翻譯的區塊重建 Markdown。 |
| `start_notebook_agent_translation` | 回傳一個 notebook 工作，包含供 host-agent 翻譯的 Markdown cell 區塊。 |
| `finish_notebook_agent_translation` | 在保留程式碼 cell、輸出與 metadata 的同時重建 notebook JSON。 |

This workflow is mainly intended for MCP hosts. If you need production repository translation with Co-op Translator managing provider calls, use `translate_markdown_content`, `translate_notebook_content`, or `run_translation`.

## Path Rewriting APIs

路徑重寫 API 不執行翻譯。在呼叫者知道來源路徑、翻譯後目標路徑與專案佈局後，它們會更新連結與 frontmatter 路徑。

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | 重寫 Markdown 連結與支援的 frontmatter 路徑欄位，以用於翻譯後的目標。 |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | 對 notebook JSON 中的每個 Markdown cell 套用 Markdown 路徑重寫，並保持非 Markdown cells 不變。 |

The `policy` argument may be a dictionary with these fields:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | 是 | 目標語言代碼，例如 `"ko"` 或 `"pt-BR"`。 |
| `root_dir` | 否 | 來源專案根目錄。預設為 `"."`。 |
| `translations_dir` | 否 | 文字翻譯輸出目錄。預設為 `translations` under `root_dir`. |
| `translated_images_dir` | 否 | 已翻譯影像輸出目錄。預設為 `translated_images` under `root_dir`. |
| `translation_types` | 否 | 啟用的翻譯類型。預設為 Markdown、notebook 與影像。 |
| `lang_subdir` | 否 | 每個語言資料夾下的可選子目錄。 |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | 必要 | 以空格分隔的目標語言代碼，例如 `"ko ja fr"`、或 `"all"`。別名代碼會正規化為標準 BCP 47 值。 |
| `root_dir` | `str` | `"."` | 單一翻譯目標的專案根目錄。當提供 `root_dirs` 或 `groups` 時會被忽略。 |
| `update` | `bool` | `False` | 刪除並重新建立已選語言的現有翻譯。 |
| `images` | `bool` | `False` | 包含影像翻譯。需要 Azure AI Vision 的設定。 |
| `markdown` | `bool` | `False` | 包含 Markdown 翻譯。 |
| `notebook` | `bool` | `False` | 包含 Jupyter notebook 翻譯。 |
| `debug` | `bool` | `False` | 啟用除錯日誌。 |
| `save_logs` | `bool` | `False` | 將 DEBUG 等級的日誌檔儲存在根目錄下的 `logs/` 目錄。 |
| `yes` | `bool` | `True` | 自動確認提示，適用於程式化與 CI 使用。 |
| `add_disclaimer` | `bool` | `False` | 向翻譯後的 Markdown 與 notebook 新增機器翻譯免責聲明。 |
| `translations_dir` | `str \| None` | `None` | 自訂文字翻譯輸出目錄。相對路徑會相對每個根目錄解析。 |
| `image_dir` | `str \| None` | `None` | 自訂已翻譯影像輸出目錄。相對路徑會相對每個根目錄解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 多個共享相同輸出設定的根目錄。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 明確的 `(root_dir, translations_dir)` 配對。優先於 `root_dirs`。 |
| `repo_url` | `str \| None` | `None` | 在渲染 README 的語言表格指引時使用的儲存庫 URL。 |
| `glossaries` | `Iterable[str] \| None` | `None` | 翻譯期間要保留的詞彙表詞條。重複與空白詞條會被正規化。 |
| `dry_run` | `bool` | `False` | 估算翻譯量並預覽遷移行為而不寫入檔案。 |

## Review Parameters

`run_review` intentionally mirrors the `run_translation` signature where possible so automation can switch between translation and review workflows with minimal branching.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | 要審查的目標語言資料夾。接受以空格分隔的字串與可列舉集合。`"all"` 會審查所有被發現的翻譯語言。 |
| `root_dir` | `str` | `"."` | 單一審查目標的專案根目錄。當提供 `root_dirs` 或 `groups` 時會被忽略。 |
| `markdown` | `bool` | `False` | 包含 Markdown 與 MDX 原始檔案。 |
| `notebook` | `bool` | `False` | 包含 Jupyter notebook 原始檔案。 |
| `images` | `bool` | `False` | 保留以與翻譯選項一致。影像的連結參考會從 Markdown 中檢查。 |
| `translations_dir` | `str \| None` | `None` | 自訂文字翻譯輸出目錄。相對路徑會相對每個根目錄解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 多個共用相同輸出設定的根目錄。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 顯式的 (root_dir, translations_dir) 配對。優先於 `root_dirs`。 |
| `changed_from` | `str \| None` | `None` | 用於限制審查至已變更原始檔案的 Git 參考。 |
| `output_format` | `str` | `"text"` | 審查輸出格式。支援的值為 `"text"` 和 `"github"`。 |
| `fail_on_warnings` | `bool` | `False` | 除了錯誤之外，將警告也視為失敗。 |
| `debug` | `bool` | `False` | 啟用偵錯日誌。 |
| `save_logs` | `bool` | `False` | 將 DEBUG 級別的日誌檔案儲存在根目錄下的 `logs/` 目錄中。 |

如果未設定 `markdown`、`notebook` 或 `images`，API 會在適用時審查 Markdown、筆記本和影像連結參考。審查不會呼叫 LLM 提供者，且不需要 API 金鑰。

## 設定需求

Provider-backed translation APIs require provider configuration before translating:

- Markdown 和筆記本翻譯需要 LLM 提供者。請設定 Azure OpenAI 或 OpenAI 其中一者。
- 圖像翻譯除了 LLM 提供者外，還需要 Azure AI Vision。
- `run_translation` 在專案翻譯開始前會執行輕量的連線檢查。
- 由代理協助的 `start_*_agent_translation` 和 `finish_*_agent_translation` API 不會呼叫 Co-op Translator 的 LLM 提供者。主機應用程式或 MCP 代理會翻譯已準備的分塊。
- `rewrite_markdown_paths`、`rewrite_notebook_paths` 與 `run_review` 是決定性的，且不需要提供者憑證。

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

`run_review` 是決定性的，且不需要 Azure OpenAI、OpenAI 或 Azure AI Vision 的設定。

## 行為說明

- 內容翻譯的 API 將翻譯與專案路徑重寫分開。當已翻譯的內容需要調整專案相對連結以符合目標位置時，請明確呼叫 `rewrite_markdown_paths` 或 `rewrite_notebook_paths`。
- 專案協調 API 在內容翻譯周圍加入專案相關行為，包括檔案發現、寫入、路徑重寫、metadata（元資料）、清理，以及可選的免責聲明。
- `run_translation` 會透過 Click 列印進度與預估摘要，符合 CLI 使用者體驗。
- `dry_run=True` 使用虛擬的 README 更新來計算估算，但不會寫入 README 或翻譯檔案。
- `groups` 會依序處理。作業開始前會列印單一的總合估算。
- 選擇影像翻譯時，若缺少 Vision 設定，會在翻譯開始前引發錯誤。
- 會偵測到現有基於別名的語言資料夾，並可在執行期間將其遷移為正規的語言資料夾名稱。
- `run_review` 對於缺少翻譯檔案、缺失或過時的翻譯 metadata、格式錯誤的 Markdown frontmatter/程式碼區塊，以及無效的已翻譯筆記本 JSON 會判定為失敗。
- `run_review` 預設會將缺少的本地 Markdown 與影像連結目標報告為警告。

## 內部呼叫路徑

該 API 會委派到與 CLI 相同的核心實作：

翻譯：

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` 用於記憶體內翻譯。
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` 用於明確的路徑後處理。
3. `co_op_translator.api.translation.run_translation` 用於完整的專案協調。
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. 專注於 Markdown、筆記本和影像的專案翻譯 mixin。
8. 位於 `co_op_translator.core` 下的 Markdown、筆記本、文字與影像翻譯器。

審查：

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. 位於 `co_op_translator.review.checks` 下的決定性檢查

下列類別對維護者有用，但並未匯出為套件層級的穩定 API。

| 類別 | 模組 | 職責 |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | 協調專案層級的翻譯、目錄管理、每種語言的 metadata 正規化，並委派給 Markdown、筆記本與影像翻譯器。 |
| `TranslationManager` | `co_op_translator.core.project.translation` | 為 Markdown、筆記本、影像執行非同步檔案處理工作、過時偵測，以及翻譯 metadata 更新。 |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | 協調 Markdown 檔案的讀取、內容翻譯、路徑重寫、metadata、免責聲明與寫入。 |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | 協調筆記本檔案的讀取、Markdown 儲存格翻譯、路徑重寫、metadata、免責聲明與寫入。 |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | 協調來源影像的發現、影像翻譯、輸出路徑、metadata 與寫入。 |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 尋找已翻譯的 Markdown 配對、評估翻譯品質，並讀取低信心修復工作流程所需的信心度 metadata。 |
| `ReviewRunner` | `co_op_translator.review.runner` | 協調跨原始檔案、目標語言與已設定翻譯根目錄的決定性審查檢查。 |
| `ReviewTarget` | `co_op_translator.review.targets` | 描述一個來源根目錄以及為該根目錄所審查的翻譯輸出目錄。 |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | 偵測舊版別名語言資料夾，並準備規範的 BCP 47 資料夾遷移計畫。 |
| `Config` | `co_op_translator.config.base_config` | 載入 `.env` 檔案，並檢查是否已設定必要的 LLM 與可選的 Vision 提供者。 |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | 自動偵測 Azure OpenAI 或 OpenAI，驗證必要的環境變數，並執行提供者連線檢查。 |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | 偵測 Azure AI Vision 設定並為影像翻譯執行連線檢查。 |