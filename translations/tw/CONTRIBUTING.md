<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:34:07+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tw"
}
-->
# 貢獻 Co-op Translator

這個專案歡迎大家貢獻和提出建議。大多數貢獻都需要你同意一份貢獻者授權協議（CLA），聲明你有權利並且確實授予我們使用你的貢獻的權利。詳情請參考 https://cla.opensource.microsoft.com。

當你提交 pull request 時，CLA 機器人會自動判斷你是否需要提供 CLA，並在 PR 上做出相應標記（例如狀態檢查、留言）。只要按照機器人的指示操作即可。你只需要在所有使用我們 CLA 的 repo 中做一次這個步驟。

## 開發環境設定

建議使用 Poetry 來管理這個專案的依賴。我們用 `pyproject.toml` 來管理專案依賴，因此安裝依賴時請使用 Poetry。

### 建立虛擬環境

#### 使用 pip

```bash
python -m venv .venv
```

#### 使用 Poetry

```bash
poetry init
```

### 啟動虛擬環境

#### pip 和 Poetry 都適用

- Windows：

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux：

    ```bash
    source .venv/bin/activate
    ```

#### 使用 Poetry

```bash
poetry shell
```

### 安裝套件及必要依賴

#### 使用 Poetry（根據 pyproject.toml）

```bash
poetry install
```

### 手動測試

在提交 PR 前，請務必用真實文件測試翻譯功能：

1. 在根目錄建立一個測試資料夾：
    ```bash
    mkdir test_docs
    ```

2. 把你想翻譯的 markdown 文件和圖片複製到測試資料夾。例如：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 在本地安裝套件：
    ```bash
    pip install -e .
    ```

4. 在你的測試文件上執行 Co-op Translator：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. 檢查 `test_docs/translations` 和 `test_docs/translated_images` 內的翻譯檔案，確認：
   - 翻譯品質
   - metadata 註解正確
   - 原本的 markdown 結構有保留
   - 連結和圖片都能正常顯示

這樣的手動測試可以確保你的修改在實際情境下運作良好。

### 環境變數

1. 在根目錄用 `.env.template` 檔案複製出 `.env` 檔。
1. 按照指示填寫環境變數。

> [!TIP]
>
> ### 其他開發環境選項
>
> 除了在本地執行專案，你也可以用 GitHub Codespaces 或 VS Code Dev Containers 來建立開發環境。
>
> #### GitHub Codespaces
>
> 你可以直接用 GitHub Codespaces 線上執行範例，無需額外設定。
>
> 點擊按鈕會在瀏覽器中開啟網頁版 VS Code：
>
> 1. 開啟範本（可能需要幾分鐘）：
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### 使用 VS Code Dev Containers 在本地執行
>
> ⚠️ 這個選項需要你的 Docker Desktop 至少分配 16 GB RAM。如果你的 RAM 不足 16 GB，可以考慮 [GitHub Codespaces 選項](../..) 或 [本地設定](../..)。
>
> 另一個選擇是 VS Code Dev Containers，會用 [Dev Containers 擴充套件](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本地 VS Code 開啟專案：
>
> 1. 啟動 Docker Desktop（如果還沒安裝請先安裝）
> 2. 開啟專案：
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>

### 程式碼風格

我們使用 [Black](https://github.com/psf/black) 作為 Python 程式碼格式化工具，確保整個專案的程式碼風格一致。Black 會自動將 Python 程式碼重新格式化成統一風格。

#### 設定

Black 的設定寫在 `pyproject.toml`：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### 安裝 Black

你可以用 Poetry（推薦）或 pip 安裝 Black：

##### 使用 Poetry

設定開發環境時會自動安裝 Black：
```bash
poetry install
```

##### 使用 pip

如果用 pip，可以直接安裝 Black：
```bash
pip install black
```

#### 使用 Black

##### 用 Poetry

1. 格式化專案內所有 Python 檔案：
    ```bash
    poetry run black .
    ```

2. 格式化指定檔案或資料夾：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### 用 pip

1. 格式化專案內所有 Python 檔案：
    ```bash
    black .
    ```

2. 格式化指定檔案或資料夾：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 建議你設定編輯器，在儲存時自動用 Black 格式化程式碼。大多數現代編輯器都支援這個功能（擴充套件或外掛）。

## 執行 Co-op Translator

要用 Poetry 在你的環境執行 Co-op Translator，請依照以下步驟：

1. 進入你想要測試翻譯的資料夾，或建立一個臨時資料夾來測試。

2. 執行以下指令。把 `-l ko` 換成你想翻譯的語言代碼。`-d` 參數代表除錯模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 執行指令前，請確認已啟動 Poetry 環境（poetry shell）。

## 貢獻新語言

歡迎大家貢獻新語言支援。開 PR 前，請完成以下步驟，讓審查流程更順利。

1. 新增語言到字型對應表
   - 編輯 `src/co_op_translator/fonts/font_language_mappings.yml`
   - 新增一筆資料，包含：
     - `code`：類似 ISO 的語言代碼（例如 `vi`）
     - `name`：易懂的顯示名稱
     - `font`：`src/co_op_translator/fonts/` 內有支援該文字的字型
     - `rtl`：如果是由右至左語言填 `true`，否則填 `false`

2. 加入必要的字型檔（如有需要）
   - 如果需要新字型，請確認授權可用於開源發佈
   - 把字型檔加到 `src/co_op_translator/fonts/`

3. 本地驗證
   - 用小型範例（Markdown、圖片、notebook 等）執行翻譯
   - 確認輸出能正確顯示，包括字型和 RTL 排版（如適用）

4. 更新文件
   - 確認語言已出現在 `getting_started/supported-languages.md`
   - 不需修改 `README_languages_template.md`，它會自動從支援清單產生

5. 開 PR
   - 說明新增的語言及字型/授權相關事項
   - 如有可能，附上輸出畫面截圖

YAML 範例：

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## 維護者

### Commit 訊息與合併策略

為了讓專案的 commit 歷史一致且清楚，我們在使用 **Squash and Merge** 策略時，最終 commit 訊息要遵循特定格式。

當 PR 合併時，所有 commit 會被壓縮成一個 commit。最終 commit 訊息請依照以下格式，保持歷史乾淨一致。

#### Commit 訊息格式（Squash and Merge 用）

我們的 commit 訊息格式如下：

```bash
<type>: <description> (#<PR number>)
```

- **type**：commit 類型。我們使用以下類型：
  - `Docs`：文件更新。
  - `Build`：與建置系統或依賴相關的變更，包括設定檔、CI 工作流程或 Dockerfile。
  - `Core`：專案核心功能或特色的修改，特別是 `src/co_op_translator/core` 目錄下的檔案。

- **description**：簡短說明這次變更。
- **PR number**：這次 commit 對應的 PR 編號。

**範例**：

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> 目前 **`Docs`**、**`Core`** 和 **`Build`** 前綴會根據 PR 標籤自動加到 PR 標題。只要標籤正確，通常不需要手動修改 PR 標題。你只需確認內容正確且前綴已正確產生。

#### 合併策略

我們預設使用 **Squash and Merge** 合併 PR。這個策略可以確保 commit 訊息符合我們的格式，即使每個 commit 本身沒有。

**原因**：

- 專案歷史乾淨、線性。
- commit 訊息一致。
- 減少雜訊（例如「fix typo」這類小 commit）。

合併時，請確保最終 commit 訊息符合上述格式。

**Squash and Merge 範例**
如果一個 PR 包含以下 commit：

- `fix typo`
- `update README`
- `adjust formatting`

合併後應壓縮成：
`Docs: Improve documentation clarity and formatting (#65)`

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。