# Python API

穩定的公開 Python API 是從 `co_op_translator.api` 匯出的。大多數整合會使用下列工作流程之一：

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| 翻譯個別檔案或文件 | 您的應用程式讀取來源內容，呼叫 Co-op Translator 進行翻譯，並決定將結果儲存到哪裡。 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| 為主機代理翻譯準備內容 | 您的 MCP 主機或應用程式模型會翻譯各個區塊，而 Co-op Translator 則負責區塊切分與重組。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 翻譯整個儲存庫 | 您希望 Python API 的行為像 CLI，並處理探索、輸出路徑、元資料、清理與寫入。 | `run_translation` |

大多數位於 `core`, `config`, `review`, 和 `utils` 底下的較低階模組，都是供這些 API 入口點使用的實作細節。

MCP 用戶端透過 [MCP 伺服器](mcp.md) 使用相同的公開 API。當直接以 Python 呼叫時，請使用此頁面；當要向代理或編輯器公開 Co-op Translator 時，請參考 MCP 指南。如果您在 CLI、Python API 與 MCP 之間抉擇，請從 [選擇您的工作流程](workflows.md) 開始。

## 首次使用 API 流程

如果您從 Python 程式碼呼叫 Co-op Translator，請從這裡開始：

1. 根據 [設定](configuration.md) 設定 LLM 提供者，除非您只是在準備供主機代理翻譯的 Markdown 或 notebook 區塊。
2. 決定您的應用程式是否負責檔案 I/O。
3. 當您的應用程式讀寫個別檔案時，使用內容 API。
4. 當 Co-op Translator 應該像 CLI 一樣處理儲存庫時，使用 `run_translation`。
5. 如果您在自動化中需要確定性的檢查，翻譯後使用 `run_review`。

| Goal | API to start with |
| --- | --- |
| 翻譯一個 Markdown 字串或檔案 | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| 讓主機代理翻譯 Markdown 或筆記本區塊 | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| 在選擇輸出路徑後重寫已翻譯的連結 | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## 情境 1：翻譯個別檔案或文件

當您已經擁有檔案、編輯器緩衝區、notebook 載荷、MCP 請求，或自訂管線輸入時，請使用此工作流程。您的程式負責檔案 I/O：

1. Read the source content.
2. Call a content translation API.
3. 如果要將翻譯後的內容寫入專案的翻譯資料夾，可選擇呼叫路徑重寫 API。
4. 在您的應用程式中儲存或回傳結果。

內容翻譯 API 不會執行專案偵測、不會寫入 metadata、不會附加免責聲明，也不會自動重寫連結。

### Markdown 檔案

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

如果翻譯後的 Markdown 並不會放在 Co-op Translator 的專案佈局中，請跳過 `rewrite_markdown_paths` 並直接儲存翻譯後的字串。

### 筆記本檔案

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

`translate_notebook_content` 會翻譯 Markdown 儲存格並保留非 Markdown 儲存格。路徑重寫僅套用到 Markdown 儲存格。

### 圖片檔案

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

`translate_image_content` 會讀取來源圖像並回傳已渲染的 `PIL.Image.Image`。它不會寫入翻譯後的圖像中繼資料。

## 情境 2：翻譯整個儲存庫

當您希望 Python API 的行為像 `translate` CLI 時，請使用此工作流程。`run_translation` 會偵測支援的檔案、翻譯所選的內容類型、重寫路徑、寫出輸出檔案、更新元資料，並執行翻譯維護任務，例如清理。

`run_translation` 是建議的專案協調進入點。`translate_project` 以相容別名匯出並具有相同行為。

將目前儲存庫中的 Markdown 檔案翻譯成韓語和日語:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

只翻譯來自特定專案根目錄的筆記本：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

在不寫入檔案的情況下預覽翻譯量：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

為整合記錄結構化進度事件：

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # 將 payload 儲存在你的 job-event 資料表中，或將其串流到你的 UI。


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Events use the versioned schema `co-op.translation.event.v1`. Integrations should
depend on stable fields such as `type` and `stage_key`, not on human-facing
console text or `stage_label`.

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

當每種語言應包含巢狀子目錄時，使用每語言佔位符:

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

如果未設定 `markdown`、`notebook` 或 `images` 中的任何一個，API 會翻譯所有支援的類型：Markdown、筆記本與影像。

### 使用翻譯狀態提供者保留已接受的人為編輯

預設情況下，Co-op Translator 保持其既有的檔案層級行為：當一個
Markdown 原始檔案過時，整個翻譯後的檔案會被重新產生。託管的
整合可以選擇傳遞 `TranslationStateProvider` 來保留人為
未變更的來源區塊中的編輯。

該提供者會提供最後一組已接受的來源/目標對並記錄每一個新的
候選。接受仍然是整合方的責任—例如，
在翻譯的 pull request 合併之後：

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

對於具有有效已接受基準的 Markdown 檔案，Co-op Translator 會對齊
頂層的 Markdown 區塊。未變更的來源區塊會重用目前的翻譯後
區塊，包括人為所做的編輯；已變更或新增的來源區塊會被送去
翻譯；已刪除的來源區塊則會被移除。如果對齊不明確、
目標結構已改變、區塊翻譯無效，或沒有可用的基準，
Co-op Translator 就會安全地回退到既有的整檔案
翻譯流程。

此 API 儲存文件的翻譯狀態，而不是跨文件的片語或
片段翻譯記憶。它目前適用於 Markdown 專案
翻譯。筆記本與圖片的行為保持不變。傳送 `update=True`
仍會要求完全重新產生。

如果一個或多個檔案無法翻譯，`run_translation` 會引發一個
`RuntimeError`，在專案工作流程結束後拋出，而不是回報一個
成功執行但輸出缺失的結果。整合應將此視為失敗的
作業，並保留先前接受的翻譯狀態。

## 審閱已翻譯的輸出

`run_review` 在沒有 LLM 或 Vision 憑證的情況下執行確定性的翻譯檢查。

!!! note "測試版"
    `run_review` 是測試版的確定性審查 API。它不會呼叫模型提供者或寫入檔案，但檢查規則與議題結構可能會變動。

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

在僅翻譯 README 之後，對審查使用相同的範圍：

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` reviews only `README.md` under each configured source root,
including custom `groups` and output directories. Other documents and nested
READMEs are excluded. A missing source README raises `ValueError`; failed
translation checks raise `RuntimeError`.

僅審查相對於 base ref 有變更的檔案，並列印 GitHub 風格的輸出：

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

## 複製貼上 API 範例

翻譯 Markdown 內容而不寫入檔案：

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

## 公開入口點

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

## 內容翻譯 API

內容翻譯 API 適用於已在記憶體中持有內容的整合，例如編輯器擴充套件、MCP 工具、筆記本處理器或自訂管線。

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | 非同步。僅翻譯 Markdown 內容。它不會重寫連結、寫入 metadata，或附加免責聲明。 |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | 非同步。翻譯 Markdown 儲存格並保留非 Markdown 儲存格。它不會重寫連結、寫入 metadata，或附加免責聲明。 |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | 同步。擷取並翻譯影像文字，然後回傳已渲染的圖片。它不會儲存已翻譯圖片的 metadata。 |

`translate_markdown_content` and `translate_notebook_content` accept an optional `source_path` through their options. 該路徑會作為上下文傳遞給翻譯器；呼叫方仍需對任何專案特定的路徑重寫負責。

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

相同的選項也可作為字典傳遞：

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## 代理協助翻譯 API

由代理協助的 API 不會呼叫 Co-op Translator 所配置的 LLM 提供者。它們會為宿主代理準備要翻譯的 Markdown 或筆記本片段，然後從已翻譯的片段重建最終內容。

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | 回傳一個自包含的 Markdown 工作，內含片段、提示和重建狀態。 |
| `finish_markdown_agent_translation` | 從工作與宿主代理翻譯的片段重建 Markdown。 |
| `start_notebook_agent_translation` | 回傳一個筆記本工作，內含供宿主代理翻譯的 Markdown 儲存格片段。 |
| `finish_notebook_agent_translation` | 在保留程式碼儲存格、輸出和 metadata 的同時重建筆記本 JSON。 |

此工作流程主要針對 MCP 主機。如果您需要由 Co-op Translator 管理 provider 呼叫的生產儲存庫翻譯，請使用 `translate_markdown_content`、`translate_notebook_content` 或 `run_translation`。

## 路徑重寫 API

路徑重寫 API 不執行任何翻譯。它們會在呼叫方知道來源路徑、翻譯後的目標路徑和專案佈局之後，更新連結和 frontmatter 路徑。

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown 內容與 frontmatter | 為翻譯後的目標重寫 Markdown 連結與受支援的 frontmatter 路徑欄位。 |
| `rewrite_notebook_paths` | notebook JSON 中的 Markdown 儲存格 | 將 Markdown 路徑重寫套用到每個 Markdown 儲存格，並保留非 Markdown 儲存格不變。 |

`policy` 參數可以是一個包含下列欄位的字典：

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | 否 | 啟用的翻譯類型。預設為 Markdown、notebooks 與 images。 |
| `lang_subdir` | 否 | 每個語言資料夾下的可選子目錄。 |

## 專案翻譯參數

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | 必要 | 以空格分隔的目標語言代碼，例如 `"ko ja fr"` 或 `"all"`。別名代碼會標準化為 BCP 47 的正規值。 |
| `root_dir` | `str` | `"."` | 單一翻譯目標的專案根目錄。當提供 `root_dirs` 或 `groups` 時會被忽略。 |
| `update` | `bool` | `False` | 刪除並重新建立所選語言的現有翻譯。 |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | 將 DEBUG 級別的日誌檔儲存在根目錄 `logs/` 下。 |
| `yes` | `bool` | `True` | 自動確認提示，適用於程式化與 CI 用途。 |
| `add_disclaimer` | `bool` | `False` | 在翻譯後的 Markdown 與筆記本中加入機器翻譯的免責聲明。 |
| `translations_dir` | `str \| None` | `None` | 自訂文字翻譯輸出目錄。相對路徑會相對於每個根目錄解析。 |
| `image_dir` | `str \| None` | `None` | 自訂翻譯後影像輸出目錄。相對路徑會相對於每個根目錄解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 多個共享相同輸出設定的根目錄。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 明確的 `(root_dir, translations_dir)` 配對。優先於 `root_dirs`。 |
| `repo_url` | `str \| None` | `None` | 在呈現 README 語言表格指引時使用的儲存庫 URL。 |
| `glossaries` | `Iterable[str] \| None` | `None` | 在翻譯期間要保留的詞彙表術語。重複與空白術語會被正規化。 |
| `dry_run` | `bool` | `False` | 估算翻譯量並預覽遷移行為，但不寫入檔案。 |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | 可選的 accepted-baseline 和 candidate 持久化適配器，用於增量 Markdown 更新。省略時保留既有的整檔行為。 |

## 審查參數

`run_review` 有意在可能的情況下對應 `run_translation` 的簽名，讓自動化能以最少的分支在翻譯與審核工作流程間切換。

| 參數 | 類型 | 預設值 | 用途 |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | 要審查的目標語言資料夾。接受以空格分隔的字串與可疊代物件。`"all"` 會審查所有偵測到的翻譯語言。 |
| `root_dir` | `str` | `"."` | 單一審查目標的專案根目錄。忽略當提供 `root_dirs` 或 `groups` 時。 |
| `markdown` | `bool` | `False` | 包含 Markdown 與 MDX 原始檔案。 |
| `notebook` | `bool` | `False` | 包含 Jupyter 筆記本原始檔案。 |
| `images` | `bool` | `False` | 保留以與翻譯選項一致。影像的連結參考會從 Markdown 中檢查。 |
| `translations_dir` | `str \| None` | `None` | 自訂文字翻譯輸出目錄。相對路徑會相對於每個根目錄解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 多個共享相同輸出設定的根目錄。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 明確的 `(root_dir, translations_dir)` 配對。優先於 `root_dirs`。 |
| `changed_from` | `str \| None` | `None` | 用來限制審查到已改動原始檔案的 Git ref。 |
| `readme_only` | `bool` | `False` | 只審查每個來源根目錄下的 `README.md`。缺少來源 README 會引發 `ValueError`。 |
| `output_format` | `str` | `"text"` | 審查輸出格式。支援的值為 `"text"` 與 `"github"`。 |
| `fail_on_warnings` | `bool` | `False` | 將警告連同錯誤一併視為失敗。 |
| `debug` | `bool` | `False` | 啟用除錯日誌。 |
| `save_logs` | `bool` | `False` | 將 DEBUG-level 的日誌檔存至根目錄下的 `logs/` 目錄。 |

如果未設定 `markdown`、`notebook` 或 `images` 其中任何一項，API 會在適用的情況下審查 Markdown、筆記本以及影像連結參考。審查不會呼叫 LLM 提供者，也不需要 API 金鑰。

## 設定需求

由提供者支援的翻譯 API 在翻譯前需要先進行提供者設定：

- Markdown 和 notebook 的翻譯需要 LLM 提供者。請設定 Azure OpenAI、OpenAI 或 Anthropic。
- 影像翻譯除了需要 LLM 提供者外，還需要 Azure AI Vision。
- `run_translation` 會在專案翻譯開始前執行輕量的連線檢查。
- 由代理協助的 `start_*_agent_translation` 和 `finish_*_agent_translation` API 不會呼叫 Co-op Translator 的 LLM 提供者。主機應用程式或 MCP 代理會翻譯已準備好的區塊。
- `rewrite_markdown_paths`、`rewrite_notebook_paths` 與 `run_review` 是確定性的，且不需要提供者憑證。

所需的 Azure OpenAI 變數：

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

所需的 OpenAI 變數：

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

所需的 Anthropic 變數：

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` 和 `ANTHROPIC_MAX_TOKENS` 為選用。從 Co-op Translator 0.22.0 起，Microsoft Agent Framework 為所有提供者的預設模型用戶端。仍可暫時用 `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` 選擇 Semantic Kernel，但如此做會發出棄用警告；有關分階段移除計畫，請參閱 [設定](configuration.md#model-client-backend)。

影像翻譯所需的 Azure AI Vision 變數：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` 是決定性的，且不需要 LLM 或 Azure AI Vision 設定。

## 行為說明

- 內容翻譯 API 將翻譯與專案路徑重寫分開。當已翻譯的內容需要為目標位置調整專案相對連結時，請明確呼叫 `rewrite_markdown_paths` 或 `rewrite_notebook_paths`。
- 專案編排 API 在內容翻譯周圍加入專案行為，包括檔案偵測、寫入、路徑重寫、中繼資料、清理，以及可選的免責聲明。
- `run_translation` 透過 CLI 使用的同一個由 Rich 支援的報告器列印進度與估算摘要。非互動式輸出會退回為純文字。
- `dry_run=True` 使用虛擬 README 更新來計算估算，但不會寫入 README 或翻譯檔案。
- `groups` 會依序處理。開始工作前會列印單一彙總估算。
- 選擇影像翻譯時，如果缺少 Vision 設定，會在翻譯開始前引發錯誤。
- 會偵測現有基於別名的語言資料夾，並可在執行期間將它們遷移為規範的語言資料夾名稱。
- `run_review` 會在以下情況失敗：翻譯檔案遺失、翻譯中繼資料遺失或過時、Markdown frontmatter/程式碼區塊格式錯誤，以及翻譯後的 notebook JSON 無效。
- `run_review` 預設會將本地 Markdown 與影像連結目標遺失回報為警告。

## 內部呼叫路徑

此 API 會委派給 CLI 使用的相同核心實作：

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. 專注於專案翻譯的 mixins，適用於 Markdown、筆記本與圖像。
8. 在 `co_op_translator.core` 底下的 Markdown、notebook、文字與影像翻譯器。

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

以下類別對維護者有用，但不會以套件層級的穩定 API 匯出。

| 類別 | 模組 | 職責 |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | 協調專案層級的翻譯、目錄管理、每語言的 metadata 正規化，並委派給 Markdown、筆記本與影像翻譯器。 |
| `TranslationManager` | `co_op_translator.core.project.translation` | 執行 Markdown、筆記本、影像的非同步檔案處理作業、過期檢測，以及翻譯 metadata 更新。 |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | 協調 Markdown 檔案讀取、內容翻譯、路徑改寫、metadata、免責聲明與寫入。 |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | 協調筆記本檔案讀取、Markdown 儲存格翻譯、路徑改寫、metadata、免責聲明與寫入。 |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | 協調來源影像發現、影像翻譯、輸出路徑、metadata 與寫入。 |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 尋找翻譯後的 Markdown 配對、評估翻譯品質，並讀取信心度 metadata 以進行低信心度修復工作流程。 |
| `ReviewRunner` | `co_op_translator.review.runner` | 協調跨來源檔案、目標語言與已設定翻譯根目錄的確定性審查檢查。 |
| `ReviewTarget` | `co_op_translator.review.targets` | 描述一個來源根目錄以及為該根目錄審查的翻譯輸出目錄。 |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | 偵測舊有的別名語言資料夾，並準備正規的 BCP 47 資料夾遷移計畫。 |
| `Config` | `co_op_translator.config.base_config` | 載入 `.env` 檔並檢查是否已設定必要的 LLM 與選用的 Vision 提供者。 |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | 自動偵測 Azure OpenAI、OpenAI 或 Anthropic，驗證所需環境變數，並執行提供者連線檢查。 |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | 偵測 Azure AI Vision 設定並為影像翻譯執行連線檢查。 |