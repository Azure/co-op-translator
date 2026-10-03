# Python API

穩定的公開 Python API 是從 `co_op_translator.api` 匯出。大多數整合使用以下其中一種工作流程：

| 情境 | 在何種情況使用 | 主要 API |
| --- | --- | --- |
| 翻譯單一檔案或文件 | 您的應用程式讀取來源內容，呼叫 Co-op Translator 進行翻譯，並決定儲存結果的位置。 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| 準備給主機代理翻譯的內容 | 您的 MCP 主機或應用模型會翻譯分塊，而 Co-op Translator 負責分割與重組。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 翻譯整個程式庫 | 您希望 Python API 的行為像 CLI，一併處理偵測、輸出路徑、元資料、清理與寫入。 | `run_translation` |

位於 `core`、`config`、`review` 與 `utils` 底下的大多數較低階模組，是這些 API 入口點所使用的實作細節。

MCP 用戶端可透過 [MCP Server](mcp.md) 使用相同的公開 API。直接從 Python 呼叫時請使用本頁，當要向代理或編輯器公開 Co-op Translator 時請參考 MCP 指南。如果您在 CLI、Python API 與 MCP 之間抉擇，請從 [選擇您的工作流程](workflows.md) 開始。

## 首次使用 API 流程

如果您從 Python 程式碼呼叫 Co-op Translator，請從這裡開始：

1. 如 [Configuration](configuration.md) 所述設定 LLM 提供者，除非您只是在為 host-agent 翻譯準備 Markdown 或 notebook 的分塊。
2. 決定您的應用程式是否負責檔案的輸入/輸出。
3. 當您的應用程式讀寫單一檔案時，使用內容 API。
4. 若希望 Co-op Translator 像 CLI 一樣處理整個程式庫，請使用 `run_translation`。
5. 若在自動化中需要確定性的檢查，翻譯後請使用 `run_review`。

| 目標 | 建議使用的 API |
| --- | --- |
| 翻譯一個 Markdown 字串或檔案 | `translate_markdown_content` |
| 翻譯一個 notebook 內容 | `translate_notebook_content` |
| 翻譯一張圖片 | `translate_image_content` |
| 讓主機代理翻譯 Markdown 或 notebook 的分塊 | `start_markdown_agent_translation` 或 `start_notebook_agent_translation` |
| 選擇輸出路徑後重寫已翻譯的連結 | `rewrite_markdown_paths` 或 `rewrite_notebook_paths` |
| 翻譯整個程式庫 | `run_translation` |
| 審查已翻譯的輸出 | `run_review` |

## 情境 1：翻譯單一檔案或文件

當您已經有檔案、編輯器緩衝、notebook 內容、MCP 請求或自訂流程輸入時，請使用這個工作流程。您的程式負責檔案 I/O：

1. 讀取來源內容。
2. 呼叫內容翻譯的 API。
3. 若翻譯後的內容會寫入專案的翻譯資料夾，則可選擇呼叫路徑重寫 API。
4. 由您的應用程式儲存或回傳結果。

內容翻譯的 API 不會執行專案偵測、不會寫入元資料、不會附加免責聲明，且不會自動重寫連結。

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

如果翻譯後的 Markdown 不會放在 Co-op Translator 的專案結構中，請跳過 `rewrite_markdown_paths`，直接儲存翻譯後的字串。

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

`translate_notebook_content` 會翻譯 Markdown 儲存格並保留非 Markdown 儲存格。路徑重寫僅套用於 Markdown 儲存格。

### 圖像檔案

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

`translate_image_content` 會讀取原始影像並回傳一個已渲染的 `PIL.Image.Image`。它不會寫入已翻譯的影像元資料。

## 情境 2：翻譯整個儲存庫

當您希望 Python API 的行為類似 `translate` CLI 時，請使用此工作流程。`run_translation` 會偵測受支援的檔案、翻譯所選的內容類型、重寫路徑、寫出輸出檔案、更新元資料，並執行翻譯維護工作，例如清理。

`run_translation` 是建議的專案協調進入點。`translate_project` 以相同行為匯出為相容別名。

將目前儲存庫中的 Markdown 檔案翻譯為韓語和日語：

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
    # 將有效載荷儲存到你的 job-event 資料表，或串流到你的使用者介面。


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

事件使用版本化的 schema `co-op.translation.event.v1`。整合應該
依賴像 `type` 與 `stage_key` 這類穩定欄位，而不是依賴面向使用者的
主控台文字或 `stage_label`。

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

當每個語言應包含巢狀子目錄時，使用每語言的佔位符：

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

如果沒有設定 `markdown`、`notebook` 或 `images`，API 將翻譯所有受支援的類型：Markdown、筆記本，以及影像。

### 使用翻譯狀態提供者來保留已接受的人為編輯

預設情況下，Co-op Translator 保持其現有的檔案層級行為：當一個
Markdown 原始內容陳舊時，整個已翻譯檔案會被重新產生。託管的
整合可以選擇傳入 `TranslationStateProvider` 來保留人為
在未變動的來源區塊中的編輯。

該提供者會提供最後一組已接受的來源/目標配對，並記錄每一個新的
候選。接受仍然是整合方的責任——例如，
在翻譯的 pull request 被合併後：

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

對於具有有效已接受基線的 Markdown 檔案，Co-op Translator 會對齊
頂層的 Markdown 區塊。未變動的來源區塊會重用目前的已翻譯
區塊，包括人為所做的編輯；已變更或新增的來源區塊會被送出
以供翻譯；被刪除的來源區塊則會移除。如果對齊不明確，
目標結構已變更、區塊翻譯無效，或沒有可用的基線，
Co-op Translator 會安全地退回到現有的整檔
翻譯流程。

此 API 儲存的是文件的翻譯狀態，而不是跨文件的片語或
段落翻譯記憶。它目前適用於 Markdown 專案
翻譯。Notebook 和影像的行為不變。傳入 `update=True`
仍然會要求完全重新產生。

如果一個或多個檔案無法翻譯，`run_translation` 會在專案工作流程完成後拋出一個
`RuntimeError`，而不是回報一個有缺少輸出的成功執行。
整合應將此視為失敗的
工作並保留先前已接受的翻譯狀態。

## 審閱已翻譯的輸出

`run_review` 在沒有 LLM 或 Vision 憑證的情況下執行確定性的翻譯檢查。

!!! note "測試版"
    `run_review` 是一個 beta 的確定性審查 API。它不會呼叫模型提供者或寫入檔案，但檢查和議題架構可能會演變。

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

在僅翻譯 README 後，對審查使用相同的範圍：

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` 僅會審查每個已配置來源根目錄下的 `README.md`，
包括自訂的 `groups` 及輸出目錄。其他文件與巢狀
README 則會被排除。缺少來源 README 會引發 `ValueError`；失敗的
翻譯檢查會引發 `RuntimeError`。

只審查相對於 base ref 有變更的檔案，並輸出 GitHub 風格的結果：

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

翻譯 Markdown 內容但不寫入檔案：

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

用 Python 翻譯儲存庫：

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

保留詞彙表用語：

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

內容翻譯 API 適用於已將內容載入記憶體的整合情境，例如編輯器擴充、MCP 工具、筆記本處理器或自訂管線。

| 函式 | 輸入 | 輸出 | 檔案 I/O | 備註 |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | 否 | 非同步。僅翻譯 Markdown 內容。不會改寫連結、寫入元資料，或附加免責聲明。 |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | 否 | 非同步。翻譯 Markdown 儲存格並保留非 Markdown 儲存格。不會改寫連結、寫入元資料，或附加免責聲明。 |
| `translate_image_content` | Image path | `PIL.Image.Image` | 僅讀取來源影像 | 同步。擷取並翻譯影像文字，然後回傳呈現後的影像。它不會儲存翻譯後的影像元資料。 |

`translate_markdown_content` 和 `translate_notebook_content` 可透過其選項接收一個可選的 `source_path`。該路徑會作為上下文傳遞給翻譯器；呼叫端仍需在翻譯後負責任何專案特定的路徑重寫。

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

相同的選項也可以以字典傳遞：

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## 代理輔助翻譯 API

代理協助的 API 不會由 Co-op Translator 呼叫已配置的 LLM 提供者。它們會準備供主機代理翻譯的 Markdown 或 notebook 區塊，然後從已翻譯的區塊重建最終內容。

| 函式 | 用途 |
| --- | --- |
| `start_markdown_agent_translation` | 回傳一個自包含的 Markdown 工作，包含區塊、提示，以及重建狀態。 |
| `finish_markdown_agent_translation` | 從工作與主機代理翻譯的區塊重建 Markdown。 |
| `start_notebook_agent_translation` | 回傳一個筆記本工作，含供主機代理翻譯的 Markdown 儲存格區塊。 |
| `finish_notebook_agent_translation` | 在保留程式碼儲存格、輸出與元資料的同時重建筆記本 JSON。 |

此工作流程主要適用於 MCP hosts。如果你需要在生產環境翻譯儲存庫，並由 Co-op Translator 管理提供者呼叫，請使用 `translate_markdown_content`、`translate_notebook_content`，或 `run_translation`。

## 路徑重寫 API

路徑重寫 API 不會執行任何翻譯。它們會在呼叫端知道來源路徑、已翻譯的目標路徑和專案佈局之後更新連結和 frontmatter 路徑。

| 函式 | 範圍 | 備註 |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown 內文與 frontmatter | 為已翻譯的目標改寫 Markdown 連結與受支援的 frontmatter 路徑欄位。 |
| `rewrite_notebook_paths` | Notebook JSON 中的 Markdown 儲存格 | 將 Markdown 路徑改寫套用到每個 Markdown 儲存格，並保持非 Markdown 儲存格不變。 |

`policy` 參數可以是一個包含以下欄位的字典：

| 欄位 | 必要 | 用途 |
| --- | --- | --- |
| `language_code` | 是 | 目標語言代碼，例如 `"ko"` 或 `"pt-BR"`。 |
| `root_dir` | 否 | 來源專案根目錄。預設為 `"."`。 |
| `translations_dir` | 否 | 文字翻譯輸出目錄。預設為 `root_dir` 下的 `translations`。 |
| `translated_images_dir` | 否 | 翻譯後影像輸出目錄。預設為 `root_dir` 下的 `translated_images`。 |
| `translation_types` | 否 | 啟用的翻譯類型。預設為 Markdown、筆記本與影像。 |
| `lang_subdir` | 否 | 在每個語言資料夾下的可選子目錄。 |

## 專案翻譯參數

| 參數 | 型別 | 預設 | 用途 |
| --- | --- | --- | --- |
| `language_codes` | `str` | 必填 | 以空格分隔的目標語言代碼，例如 `"ko ja fr"` 或 `"all"`。別名代碼會規範化為標準 BCP 47 值。 |
| `root_dir` | `str` | `"."` | 單一翻譯目標的專案根目錄。當提供 `root_dirs` 或 `groups` 時會被忽略。 |
| `update` | `bool` | `False` | 刪除並重新建立所選語言的現有翻譯。 |
| `images` | `bool` | `False` | 包含影像翻譯。需要 Azure AI Vision 設定。 |
| `markdown` | `bool` | `False` | 包含 Markdown 翻譯。 |
| `notebook` | `bool` | `False` | 包含 Jupyter 筆記本翻譯。 |
| `debug` | `bool` | `False` | 啟用除錯日誌。 |
| `save_logs` | `bool` | `False` | 將 DEBUG 級別的日誌檔儲存在根目錄下的 `logs/` 目錄。 |
| `yes` | `bool` | `True` | 於程式化及 CI 使用時自動確認提示。 |
| `add_disclaimer` | `bool` | `False` | 在翻譯後的 Markdown 與筆記本中加入機器翻譯免責聲明。 |
| `translations_dir` | `str \| None` | `None` | 自訂文字翻譯輸出目錄。相對路徑依每個根目錄解析。 |
| `image_dir` | `str \| None` | `None` | 自訂翻譯後圖片輸出目錄。相對路徑依每個根目錄解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 共用相同輸出設定的多個根目錄。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 明確的 `(root_dir, translations_dir)` 配對。優先於 `root_dirs`。 |
| `repo_url` | `str \| None` | `None` | 用於繪製 README 語言表格說明的儲存庫 URL。 |
| `glossaries` | `Iterable[str] \| None` | `None` | 翻譯時要保留的詞彙表條目。重複和空白條目會被標準化。 |
| `dry_run` | `bool` | `False` | 在不寫入檔案的情況下估算翻譯量並預覽遷移行為。 |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | 用於增量 Markdown 更新的選擇性已接受基線與候選項持久化適配器。省略時保留現有的整檔行為。 |

## 審查參數

`run_review` 在可能情況下有意地模仿 `run_translation` 的簽名，這樣自動化可以僅需最少分支就能在翻譯與審查工作流程之間切換。

| 參數 | 類型 | 預設值 | 用途 |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | 要檢閱的目標語言資料夾。接受以空格分隔的字串與可疊代物。`"all"` 將檢閱所有偵測到的翻譯語言。 |
| `root_dir` | `str` | `"."` | 單一檢閱目標的專案根目錄。當提供 `root_dirs` 或 `groups` 時會被忽略。 |
| `markdown` | `bool` | `False` | 包含 Markdown 與 MDX 原始檔案。 |
| `notebook` | `bool` | `False` | 包含 Jupyter 筆記本原始檔案。 |
| `images` | `bool` | `False` | 為與翻譯選項保持對稱而保留。會從 Markdown 檢查圖片連結參考。 |
| `translations_dir` | `str \| None` | `None` | 自訂文字翻譯輸出目錄。相對路徑依每個根目錄解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 共用相同輸出設定的多個根目錄。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 明確的 `(root_dir, translations_dir)` 配對。優先於 `root_dirs`。 |
| `changed_from` | `str \| None` | `None` | 用來限制檢閱至變更過的原始檔案的 Git 參考。 |
| `readme_only` | `bool` | `False` | 僅檢閱每個來源根目錄下的 `README.md`。若來源 README 缺失會拋出 `ValueError`。 |
| `output_format` | `str` | `"text"` | 檢閱輸出格式。支援的值為 `"text"` 與 `"github"`。 |
| `fail_on_warnings` | `bool` | `False` | 除了錯誤外也將警告視為失敗。 |
| `debug` | `bool` | `False` | 啟用偵錯日誌。 |
| `save_logs` | `bool` | `False` | 將 DEBUG 級別的日誌檔儲存於根目錄的 `logs/` 目錄下。 |

若未設定 `markdown`、`notebook` 或 `images`，API 將在適用情況下檢閱 Markdown、筆記本與圖片連結參考。檢閱不會呼叫 LLM 提供者，也不需要 API 金鑰。

## 設定需求

有提供者支援的翻譯 API 在翻譯前需要提供者的設定：

- Markdown 與筆記本翻譯需要 LLM 提供者。請設定 Azure OpenAI、OpenAI，或 Anthropic。
- 除了 LLM 提供者外，圖片翻譯還需要 Azure AI Vision。
- `run_translation` 在專案翻譯開始前會執行輕量連線檢查。
- 代理協助的 `start_*_agent_translation` 與 `finish_*_agent_translation` API 不會呼叫 Co-op Translator 的 LLM 提供者。由主機應用程式或 MCP 代理翻譯已準備好的區塊。
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, 與 `run_review` 是確定性的，且不需要提供者憑證。

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

必要的 Anthropic 變數：

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` 和 `ANTHROPIC_MAX_TOKENS` 為選用。自 Co-op Translator 0.22.0 起，Microsoft Agent Framework 為所有提供者的預設模型客戶端。仍可暫時以 `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` 選擇 Semantic Kernel，但這會產生棄用警告；請參閱 [設定](configuration.md#model-client-backend) 以了解分階段移除計畫。

圖片翻譯所需的 Azure AI Vision 變數：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` 是確定性的，且不需要 LLM 或 Azure AI Vision 的設定。

## 行為說明

- 內容翻譯 API 將翻譯與專案路徑重寫分開。當翻譯後的內容需要為目標位置調整以專案為相對的連結時，請明確呼叫 `rewrite_markdown_paths` 或 `rewrite_notebook_paths`。
- 專案編排 API 在內容翻譯周圍加入專案行為，包括檔案偵測、寫入、路徑重寫、元資料、清理，以及選用的免責聲明。
- `run_translation` 透過與 CLI 相同、由 Rich 支援的報告器列印進度與估算摘要。非互動輸出會退回為純文字。
- 設為 `dry_run=True` 時會使用虛擬的 README 更新來計算估算，但不會寫入 README 或翻譯檔案。
- `groups` 會依序處理。工作開始前會列印單一的總體估算。
- 當選擇圖片翻譯時，若 Vision 設定缺失會在翻譯開始前引發錯誤。
- 系統會偵測現有基於別名的語言資料夾，並可在執行期間將其遷移為規範語言資料夾名稱。
- `run_review` 於以下情況會失敗：翻譯後的檔案遺失、翻譯元資料遺失或陳舊、Markdown frontmatter/程式碼區塊語法不良，以及翻譯後的筆記本 JSON 無效。
- `run_review` 預設將遺失的本地 Markdown 與圖片連結目標報告為警告。

## 內部呼叫路徑

API 會委派給與 CLI 相同的核心實作：

翻譯：

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. 專注於 Markdown、筆記本與圖片之專案翻譯 mixin。
8. 位於 `co_op_translator.core` 下的 Markdown、筆記本、文字與圖片翻譯器。

審查：

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. 位於 `co_op_translator.review.checks` 下的確定性檢查

下列類別對維護者有用，但不作為套件層級的穩定 API 匯出。

| 類別 | 模組 | 職責 |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | 協調專案層級的翻譯、目錄管理、每語言的元資料標準化，以及委派給 Markdown、筆記本與圖片翻譯器。 |
| `TranslationManager` | `co_op_translator.core.project.translation` | 執行 Markdown、筆記本、圖片的非同步檔案處理工作、陳舊偵測，以及翻譯元資料更新。 |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | 協調 Markdown 檔案讀取、內容翻譯、路徑重寫、元資料、免責聲明與寫入。 |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | 協調筆記本檔案讀取、Markdown 儲存格翻譯、路徑重寫、元資料、免責聲明與寫入。 |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | 協調來源圖片的發現、圖片翻譯、輸出路徑、元資料與寫入。 |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 尋找翻譯後的 Markdown 配對、評估翻譯品質，並讀取低信心修復工作流程所需的信心元資料。 |
| `ReviewRunner` | `co_op_translator.review.runner` | 協調跨原始檔案、目標語言與已設定翻譯根目錄的確定性檢查。 |
| `ReviewTarget` | `co_op_translator.review.targets` | 描述一個來源根目錄以及為該根目錄檢閱的翻譯輸出目錄。 |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | 偵測舊有的別名語言資料夾，並準備遷移至規範 BCP 47 資料夾的計畫。 |
| `Config` | `co_op_translator.config.base_config` | 載入 `.env` 檔並檢查是否已設定必要的 LLM 與選用的 Vision 提供者。 |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | 自動偵測 Azure OpenAI、OpenAI 或 Anthropic，驗證必要的環境變數，並執行提供者連線檢查。 |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | 偵測 Azure AI Vision 的設定，並為圖片翻譯執行連線檢查。 |