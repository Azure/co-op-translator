# Python API

穩定的公開 Python API 由 `co_op_translator.api` 匯出。大多數整合會使用下列其中一種工作流程：

| 情境 | 何時使用 | 主要 API |
| --- | --- | --- |
| 翻譯單一檔案或文件 | 您的應用程式讀取原始內容，呼叫 Co-op Translator 進行翻譯，並決定儲存結果的位置。 | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| 為主機代理翻譯準備內容 | 您的 MCP 主機或應用模型會翻譯區塊，而 Co-op Translator 負責切割區塊和重組。 | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| 翻譯整個儲存庫 | 您希望 Python API 的行為像 CLI 一樣，處理檔案探索、輸出路徑、元資料、清理與寫入。 | `run_translation` |

大多數位於 `core`、`config`、`review` 與 `utils` 下的較低階模組，都是被這些 API 入口點使用的實作細節。

MCP 用戶端透過 [MCP 伺服器](mcp.md) 使用相同的公開 API。直接以 Python 呼叫時使用此頁面；當要將 Co-op Translator 對外暴露給代理人或編輯器時，請參閱 MCP 指南。如果您在 CLI、Python API 與 MCP 之間選擇，請先參閱 [選擇您的工作流程](workflows.md)。

## 首次使用 API 流程

如果您從 Python 程式碼呼叫 Co-op Translator，請從這裡開始：

1. 如 [設定](configuration.md) 所述，設定 LLM 提供者，除非您只是為主機代理翻譯準備 Markdown 或 notebook 區塊。
2. 決定您的應用程式是否負責檔案 I/O。
3. 當您的應用程式讀寫單一檔案時，使用內容 API。
4. 當 Co-op Translator 應像 CLI 一樣處理整個儲存庫時，使用 `run_translation`。
5. 若在自動化中需要確定性的檢查，翻譯後使用 `run_review`。

| 目標 | 建議使用的 API |
| --- | --- |
| 翻譯一個 Markdown 字串或檔案 | `translate_markdown_content` |
| 翻譯一個 notebook 內容 | `translate_notebook_content` |
| 翻譯一張影像 | `translate_image_content` |
| 讓主機代理翻譯 Markdown 或 notebook 的區塊 | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| 在選擇輸出路徑後重寫已翻譯的連結 | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| 翻譯整個儲存庫 | `run_translation` |
| 審查已翻譯的輸出 | `run_review` |

## 情境 1：翻譯單一檔案或文件

當您已經有檔案、編輯器緩衝、notebook 內容、MCP 請求或自訂流程輸入時，使用此工作流程。由您的程式碼負責檔案 I/O：

1. 讀取原始內容。
2. 呼叫內容翻譯 API。
3. 若要將已翻譯的內容寫入專案翻譯資料夾，則可選擇呼叫路徑重寫 API。
4. 由您的應用程式儲存或回傳結果。

內容翻譯 API 不會執行專案探索、不會寫入元資料、不會附加免責聲明，且不會自動重寫連結。

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

如果已翻譯的 Markdown 不會放在 Co-op Translator 的專案佈局中，則跳過 `rewrite_markdown_paths`，直接儲存已翻譯的字串。

### Notebook 檔案

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

`translate_image_content` 會讀取來源影像並回傳已渲染的 `PIL.Image.Image`。它不會寫入翻譯後的影像中繼資料。

## 情境 2：翻譯整個儲存庫

當您希望 Python API 的行為類似 `translate` CLI 時，使用此工作流程。`run_translation` 會發現支援的檔案、翻譯所選內容類型、重寫路徑、寫入輸出檔案、更新中繼資料，並執行翻譯維護工作（例如清理）。

`run_translation` 是建議的專案協調進入點。`translate_project` 作為相容別名匯出，具有相同行為。

將目前儲存庫中的 Markdown 檔案翻譯成韓語和日語：

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

只從特定專案根目錄翻譯 Notebook：

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

為整合記錄結構化的進度事件：

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # 將有效載荷儲存於您的工作事件資料表中，或將其串流到您的使用者介面。


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

事件使用版本化的 schema `co-op.translation.event.v1`。整合應該
依賴像 `type` 和 `stage_key` 這類穩定欄位，而不是依賴面向使用者的
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

當每個語言應包含一個巢狀子目錄時，請使用每語言的佔位符：

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

如果未設定 `markdown`、`notebook` 或 `images`，API 會翻譯所有支援的類型：Markdown、notebook 和圖像。

### 使用翻譯狀態提供者保留已接受的人為編輯

預設情況下，Co-op Translator 保持其既有的檔案層級行為：當一個
Markdown 原始檔已過時時，整個已翻譯的檔案會被重新產生。託管的
整合可以選擇性地傳入 `TranslationStateProvider` 以保留尚未變更的
來源區塊中的人為編輯。

該提供者會提供最後一個已接受的來源/目標配對，並記錄每一個新的
候選。接受仍然是整合方的責任——例如，
在翻譯的拉取請求合併後：

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
頂層的 Markdown 區塊。不變的來源區塊會重用當前的已翻譯
區塊，包括人為所做的編輯；已變更或新增的來源區塊會被送出
進行翻譯；已刪除的來源區塊會被移除。如果對齊不明確、
目標結構已變更、區塊翻譯無效，或沒有可用的基準，
Co-op Translator 會安全地回退到既有的整個檔案
翻譯流程。

此 API 儲存的是文件翻譯狀態，而不是跨文件的片語或
片段翻譯記憶庫。它目前適用於 Markdown 專案的
翻譯。Notebook 和圖像的行為則不變。傳入 `update=True`
仍會要求完全重新產生。

如果一或多個檔案無法被翻譯，`run_translation` 會拋出一個
`RuntimeError`，在專案工作流程完成後，而不是報告
成功執行但缺少輸出。整合應將此視為失敗的
工作，並保留先前已接受的翻譯狀態。

## 審閱已翻譯的輸出

`run_review` 執行確定性翻譯檢查，無需 LLM 或 Vision 的憑證。

!!! note "Beta"
    `run_review` 是一個測試階段的確定性審查 API。它不會呼叫模型提供者或寫入檔案，但檢查與問題結構可能會變更。

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

在僅翻譯 README 後，使用相同的範圍進行審查：

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` 只會審查每個已配置來源根目錄下的 `README.md`，
包括自訂的 `groups` 與輸出目錄。其他文件與巢狀
README 則會被排除。缺少來源 README 會引發 `ValueError`；失敗的
翻譯檢查會引發 `RuntimeError`。

只審查相對於基準參照有所變動的檔案，並輸出 GitHub 風格的結果：

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

翻譯並重寫 Markdown 連結：

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

從 Python 翻譯整個儲存庫：

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

內容翻譯 API 適用於已在記憶體中擁有內容的整合情境，例如編輯器擴充、MCP 工具、筆記本處理器或自訂的管線。

| 函式 | 輸入 | 輸出 | 檔案 I/O | 備註 |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | 否 | 非同步。僅翻譯 Markdown 內容。不會重寫連結、寫入元資料，或附加免責聲明。 |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | 否 | 非同步。翻譯 Markdown 儲存格並保留非 Markdown 儲存格。不會重寫連結、寫入元資料，或附加免責聲明。 |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | 同步。擷取並翻譯影像文字，然後回傳已渲染的影像。不會儲存翻譯後影像的元資料。 |

`translate_markdown_content` 和 `translate_notebook_content` 接受一個可選的 `source_path` 作為其選項。該路徑會作為上下文傳遞給翻譯器；呼叫者仍然需負責在翻譯後進行任何專案特定的路徑重寫。

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

相同的選項也可以以字典形式傳入：

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## 代理協助翻譯 API

代理協助的 API 不會呼叫 Co-op Translator 中設定的 LLM 提供者。它們會準備供主機代理翻譯的 Markdown 或筆記本切片，然後從翻譯後的切片重建最終內容。

| 函式 | 用途 |
| --- | --- |
| `start_markdown_agent_translation` | 回傳一個自包含的 Markdown 工作，含切片、提示與重建狀態。 |
| `finish_markdown_agent_translation` | 從工作與主機代理翻譯的切片重建 Markdown。 |
| `start_notebook_agent_translation` | 回傳一個筆記本工作，包含供主機代理翻譯的 Markdown 儲存格切片。 |
| `finish_notebook_agent_translation` | 重建筆記本 JSON，同時保留程式碼儲存格、輸出與元資料。 |

此工作流程主要供 MCP 主機使用。如果您需要由 Co-op Translator 管理提供者呼叫的生產環境儲存庫翻譯，請使用 `translate_markdown_content`、`translate_notebook_content` 或 `run_translation`。

## 路徑重寫 API

路徑重寫 API 不會執行翻譯。在呼叫者知道來源路徑、翻譯後目標路徑與專案佈局後，這些 API 會更新連結與 frontmatter 路徑。

| 函式 | 範圍 | 備註 |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown 內容與 frontmatter | 針對翻譯後的目標重寫 Markdown 連結與支援的 frontmatter 路徑欄位。 |
| `rewrite_notebook_paths` | 筆記本 JSON 中的 Markdown 儲存格 | 對每個 Markdown 儲存格套用 Markdown 路徑重寫，並保留非 Markdown 儲存格不變。 |

`policy` 參數可能是一個具有下列欄位的字典：

| 欄位 | 必要 | 用途 |
| --- | --- | --- |
| `language_code` | 是 | 目標語言代碼，例如 `"ko"` 或 `"pt-BR"`。 |
| `root_dir` | 否 | 來源專案根目錄。預設為 `"."`。 |
| `translations_dir` | 否 | 文字翻譯輸出目錄。預設為位於 `root_dir` 下的 `translations`。 |
| `translated_images_dir` | 否 | 翻譯後影像的輸出目錄。預設為位於 `root_dir` 下的 `translated_images`。 |
| `translation_types` | 否 | 啟用的翻譯類型。預設包含 Markdown、筆記本與影像。 |
| `lang_subdir` | 否 | 每個語言資料夾下的可選子目錄。 |

## 專案翻譯參數

| 參數 | 類型 | 預設 | 用途 |
| --- | --- | --- | --- |
| `language_codes` | `str` | 必要 | 以空格分隔的目標語言代碼，例如 `"ko ja fr"` 或 `"all"`。別名代碼會被標準化為正式的 BCP 47 值。 |
| `root_dir` | `str` | `"."` | 單一翻譯目標的專案根目錄。當提供 `root_dirs` 或 `groups` 時會被忽略。 |
| `update` | `bool` | `False` | 刪除並重新建立所選語言的既有翻譯。 |
| `images` | `bool` | `False` | 包含影像翻譯。需要 Azure AI Vision 的設定。 |
| `markdown` | `bool` | `False` | 包含 Markdown 翻譯。 |
| `notebook` | `bool` | `False` | 包含 Jupyter 筆記本翻譯。 |
| `debug` | `bool` | `False` | 啟用除錯日誌。 |
| `save_logs` | `bool` | `False` | 將 DEBUG 級別的日誌檔案儲存在根目錄的 `logs/` 目錄下。 |
| `yes` | `bool` | `True` | 自動確認提示以供程式化和 CI 環境使用。 |
| `add_disclaimer` | `bool` | `False` | 在已翻譯的 Markdown 和筆記本中加入機器翻譯免責聲明。 |
| `translations_dir` | `str \| None` | `None` | 自訂文字翻譯輸出目錄。相對路徑會相對每個根目錄解析。 |
| `image_dir` | `str \| None` | `None` | 自訂已翻譯影像輸出目錄。相對路徑會相對每個根目錄解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 多個共用相同輸出設定的根目錄。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 明確的 `(root_dir, translations_dir)` 配對。優先於 `root_dirs`. |
| `repo_url` | `str \| None` | `None` | 在渲染 README 語言表格指引時使用的儲存庫 URL。 |
| `glossaries` | `Iterable[str] \| None` | `None` | 翻譯時要保留的詞彙表術語。重複和空白詞條會被標準化。 |
| `dry_run` | `bool` | `False` | 估算翻譯量並預覽遷移行為，但不寫入檔案。 |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | 可選的已接受基線與候選項持久化適配器，用於增量 Markdown 更新。不指定時維持既有的整檔行為。 |

## 審查參數

`run_review` 故意在可能的情況下模仿 `run_translation` 的簽名，讓自動化能以最少的分支在翻譯與審核工作流程之間切換。

| 參數 | 類型 | 預設 | 目的 |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | 目標要審查的語言資料夾。接受以空格分隔的字串和可疊代物件。`"all"` 會審查所有已發現的翻譯語言。 |
| `root_dir` | `str` | `"."` | 單一審查目標的專案根目錄。當提供 `root_dirs` 或 `groups` 時會被忽略。 |
| `markdown` | `bool` | `False` | 包含 Markdown 和 MDX 原始檔案。 |
| `notebook` | `bool` | `False` | 包含 Jupyter 筆記本原始檔案。 |
| `images` | `bool` | `False` | 為與翻譯選項保持一致而保留。圖片連結參考會從 Markdown 中檢查。 |
| `translations_dir` | `str \| None` | `None` | 自訂文字翻譯輸出目錄。相對路徑會相對每個根目錄解析。 |
| `root_dirs` | `Iterable[str] \| None` | `None` | 多個共用相同輸出設定的根目錄。 |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | 明確的 `(root_dir, translations_dir)` 配對。優先於 `root_dirs`. |
| `changed_from` | `str \| None` | `None` | 用於限制審查範圍至已變更原始檔的 Git 參考。 |
| `readme_only` | `bool` | `False` | 僅審查每個來源根目錄下的 `README.md`。缺少來源 README 會引發 `ValueError`。 |
| `output_format` | `str` | `"text"` | 審查輸出格式。支援的值為 `"text"` 和 `"github"`。 |
| `fail_on_warnings` | `bool` | `False` | 除了錯誤外，也將警告視為失敗。 |
| `debug` | `bool` | `False` | 啟用除錯日誌。 |
| `save_logs` | `bool` | `False` | 將 DEBUG-level 日誌檔儲存在根目錄下的 `logs/` 目錄。 |

如果未設定 `markdown`、`notebook` 或 `images`，API 會在適用情況下審查 Markdown、筆記本以及圖片連結參考。審查不會呼叫 LLM 提供者，且不需要 API 金鑰。

## 設定需求

需要在翻譯前進行提供者設定：

- Markdown 與筆記本的翻譯需要一個 LLM 提供者。請配置 Azure OpenAI、OpenAI 或 Anthropic。
- 圖像翻譯除了 LLM 提供者外，還需要 Azure AI Vision。
- `run_translation` 在專案翻譯開始前執行輕量的連線檢查。
- 由代理協助的 `start_*_agent_translation` 和 `finish_*_agent_translation` API 不會呼叫 Co-op Translator 的 LLM 提供者。主機應用程式或 MCP 代理會翻譯已準備好的區塊。
- `rewrite_markdown_paths`、`rewrite_notebook_paths` 和 `run_review` 是確定性的，且不需要提供者憑證。

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

`ANTHROPIC_BASE_URL` 和 `ANTHROPIC_MAX_TOKENS` 是可選的。Microsoft Agent Framework 是自 Co-op Translator 0.22.0 起所有提供者的預設模型客戶端。仍可暫時以 `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` 選擇 Semantic Kernel，但這會發出棄用警告；請參閱 [設定](configuration.md#model-client-backend) 以了解分階段移除計劃。

影像翻譯所需的 Azure AI Vision 變數：

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` 是確定性的，並且不需要 LLM 或 Azure AI Vision 的設定。

## 行為說明

- 內容翻譯的 API 將翻譯與專案路徑重寫分開。當已翻譯內容需要針對目標位置調整專案相對連結時，請明確呼叫 `rewrite_markdown_paths` 或 `rewrite_notebook_paths`。
- 專案協調 API 為內容翻譯加入專案層級行為，包括檔案發現、寫入、路徑重寫、元資料、清理與選用的免責聲明。
- `run_translation` 會透過與 CLI 相同、以 Rich 為基礎的報告器列印進度與估計摘要。非互動式輸出則退回到純文字。
- `dry_run=True` 使用虛擬 README 更新來計算估計，但不會寫入 README 或翻譯檔案。
- `groups` 會被依序處理。在開始工作前會列印單一的總體估計。
- 當選擇圖片翻譯時，缺少 Vision 的設定會在翻譯開始前引發錯誤。
- 會偵測現有以別名為基礎的語言資料夾，並可作為執行的一部分將它們遷移到規範的語言資料夾名稱。
- `run_review` 會在缺少已翻譯的檔案、缺少或過時的 translation metadata、Markdown frontmatter/code fences 格式錯誤，以及翻譯後的 notebook JSON 無效時失敗。
- `run_review` 預設會將缺少的本地 Markdown 與影像連結目標回報為警告。

## 內部呼叫路徑

API 會委派到 CLI 使用的相同核心實作:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. 專注專案的翻譯 mixins，包含 Markdown、筆記本與影像。
8. Markdown、筆記本、文字和圖片翻譯器位於 `co_op_translator.core` 之下。

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

下列類別對維護者有用，但不作為套件層級的穩定 API 匯出。

| 類別 | 模組 | 職責 |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | 協調專案層級翻譯、目錄管理、逐語言元資料標準化，並委派給 Markdown、筆記本與影像翻譯器。 |
| `TranslationManager` | `co_op_translator.core.project.translation` | 執行非同步檔案處理工作，包含 Markdown、筆記本、影像、過時檢測與翻譯元資料更新。 |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | 協調 Markdown 檔案讀取、內容翻譯、路徑重寫、元資料、免責聲明與寫入。 |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | 協調筆記本檔案讀取、Markdown 儲存格翻譯、路徑重寫、元資料、免責聲明與寫入。 |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | 協調來源影像發現、影像翻譯、輸出路徑、元資料與寫入。 |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | 尋找已翻譯的 Markdown 配對、評估翻譯品質，並讀取低信心修復工作流程所需的信心元資料。 |
| `ReviewRunner` | `co_op_translator.review.runner` | 協調跨來源檔案、目標語言與已設定翻譯根目錄的確定性審查檢查。 |
| `ReviewTarget` | `co_op_translator.review.targets` | 描述一個來源根目錄及其相對應的翻譯輸出目錄。 |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | 偵測舊有的別名語言資料夾，並準備為典範 BCP 47 資料夾的遷移計畫。 |
| `Config` | `co_op_translator.config.base_config` | 載入 `.env` 檔案並檢查所需的 LLM 與選用的 Vision 提供者是否已設定。 |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | 自動偵測 Azure OpenAI、OpenAI 或 Anthropic，驗證必要的環境變數，並執行提供者連線檢查。 |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | 偵測 Azure AI Vision 設定並執行影像翻譯的連線檢查。 |