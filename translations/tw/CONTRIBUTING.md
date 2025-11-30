<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T10:19:53+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tw"
}
-->
# 參與 Co-op Translator 專案貢獻

本專案歡迎各種貢獻與建議。大多數貢獻需要您同意一份貢獻者授權協議（Contributor License Agreement，CLA），聲明您有權利且確實授權我們使用您的貢獻。詳細資訊請參考 https://cla.opensource.microsoft.com。

當您提交 Pull Request 時，CLA 機器人會自動判斷您是否需要提供 CLA，並在 PR 上標註相應狀態（例如狀態檢查、留言）。只需依照機器人指示操作即可。您只需在所有使用我們 CLA 的倉庫中完成一次此流程。

## 開發環境設定

建議使用 Poetry 來管理本專案的相依套件。我們使用 `pyproject.toml` 來管理專案相依性，因此安裝相依套件時，請使用 Poetry。

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

#### pip 與 Poetry 通用

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

### 安裝套件與必要相依套件

#### 使用 Poetry（根據 pyproject.toml）

```bash
poetry install
```

### 手動測試

在提交 PR 前，請務必使用真實文件測試翻譯功能：

1. 在專案根目錄建立一個測試資料夾：
    ```bash
    mkdir test_docs
    ```

2. 將您想翻譯的 Markdown 文件與圖片複製到測試資料夾。例如：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 在本地安裝套件：
    ```bash
    pip install -e .
    ```

4. 對測試文件執行 Co-op Translator：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. 檢查 `test_docs/translations` 與 `test_docs/translated_images` 中的翻譯結果，確認：
   - 翻譯品質
   - 元資料註解正確
   - 原始 Markdown 結構未被破壞
   - 連結與圖片正常顯示

此手動測試有助於確保您的修改在實際情境中運作良好。

### 環境變數

1. 複製提供的 `.env.template` 檔案，並在根目錄建立 `.env` 檔案。
2. 按照指示填寫環境變數。

> [!TIP]
>
> ### 額外的開發環境選項
>
> 除了在本地執行專案外，您也可以使用 GitHub Codespaces 或 VS Code Dev Containers 作為替代的開發環境。
>
> #### GitHub Codespaces
>
> 您可以透過 GitHub Codespaces 虛擬執行此範例，無需額外設定。
>
> 按鈕會在瀏覽器中開啟基於網頁的 VS Code：
>
> 1. 開啟範本（可能需數分鐘）：
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### 使用 VS Code Dev Containers 本地執行
>
> ⚠️ 此選項僅在您的 Docker Desktop 分配至少 16 GB 記憶體時可用。若記憶體不足 16 GB，建議使用 [GitHub Codespaces 選項](../..) 或 [本地環境設定](../..)。
>
> 相關選項是 VS Code Dev Containers，會使用 [Dev Containers 擴充套件](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本地 VS Code 中開啟專案：
>
> 1. 啟動 Docker Desktop（若尚未安裝請先安裝）
> 2. 開啟專案：
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### 程式碼風格

我們使用 [Black](https://github.com/psf/black) 作為 Python 程式碼格式化工具，以維持專案中一致的程式碼風格。Black 是一款不妥協的程式碼格式化工具，會自動將 Python 程式碼格式化成符合 Black 風格的樣式。

#### 設定檔

Black 的設定在 `pyproject.toml` 中指定：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### 安裝 Black

您可以使用 Poetry（推薦）或 pip 安裝 Black：

##### 使用 Poetry

Black 會在您設定開發環境時自動安裝：
```bash
poetry install
```

##### 使用 pip

若使用 pip，您可以直接安裝 Black：
```bash
pip install black
```

#### 使用 Black

##### 使用 Poetry

1. 格式化專案中所有 Python 檔案：
    ```bash
    poetry run black .
    ```

2. 格式化特定檔案或目錄：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### 使用 pip

1. 格式化專案中所有 Python 檔案：
    ```bash
    black .
    ```

2. 格式化特定檔案或目錄：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 建議您設定編輯器在儲存時自動使用 Black 格式化程式碼。大多數現代編輯器都支援透過擴充套件或外掛實現此功能。

## 執行 Co-op Translator

若要在您的環境中使用 Poetry 執行 Co-op Translator，請依照以下步驟：

1. 切換到您想執行翻譯測試的目錄，或建立一個臨時資料夾用於測試。

2. 執行以下指令。將 `-l ko` 替換成您想翻譯成的語言代碼。`-d` 參數表示除錯模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 執行指令前，請確保已啟動 Poetry 環境（poetry shell）。

## 新增語言貢獻

我們歡迎新增語言的貢獻。開啟 PR 前，請先完成以下步驟以確保審查順利。

1. 新增語言至字型對應表
   - 編輯 `src/co_op_translator/fonts/font_language_mappings.yml`
   - 新增條目，包含：
     - `code`：類似 ISO 的語言代碼（例如 `vi`）
     - `name`：易讀的顯示名稱
     - `font`：位於 `src/co_op_translator/fonts/` 中支援該文字系統的字型檔
     - `rtl`：若為從右至左語言，設為 `true`，否則為 `false`

2. 包含必要的字型檔（如有）
   - 若需新增字型，請確認授權許可符合開源發佈
   - 將字型檔加入 `src/co_op_translator/fonts/`

3. 本地驗證
   - 對小範例執行翻譯（Markdown、圖片、筆記本等）
   - 確認輸出正確呈現，包括字型與 RTL 版面（如適用）

4. 更新文件
   - 確保語言出現在 `getting_started/supported-languages.md`
   - 不需修改 `getting_started/README_languages_template.md`，該檔由支援清單自動產生

5. 開啟 PR
   - 描述新增語言與字型/授權相關事項
   - 若可能，附上渲染結果截圖

YAML 範例條目：

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### 測試新語言

您可以透過以下指令測試新語言：

```bash
# 建立並啟用虛擬環境
python -m venv .venv
# Windows 系統
.venv\Scripts\activate
# macOS/Linux 系統
source .venv/bin/activate
# 安裝開發套件
pip install -e .
# 執行翻譯
translate -l "new_lang"
```

## 維護者指南

### Commit 訊息與合併策略

為確保專案 commit 歷史的一致性與清晰度，我們在使用 **Squash and Merge** 策略時，對最終 commit 訊息採用特定格式。

當 Pull Request (PR) 合併時，所有個別 commit 會被壓縮成一個 commit。最終 commit 訊息應遵循以下格式，以維持乾淨且一致的歷史紀錄。

#### Commit 訊息格式（Squash and Merge）

我們使用以下格式撰寫 commit 訊息：

```bash
<type>: <description> (#<PR 編號>)
```

- **type**：指定 commit 類別。我們使用以下類型：
  - `Docs`：文件更新。
  - `Build`：與建置系統或相依性相關的變更，包括設定檔、CI 工作流程或 Dockerfile 更新。
  - `Core`：專案核心功能或特性修改，特別是 `src/co_op_translator/core` 目錄下的檔案。

- **description**：簡潔描述變更內容。
- **PR number**：關聯的 Pull Request 編號。

**範例**：

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> 目前，**`Docs`**、**`Core`** 與 **`Build`** 前綴會根據修改的原始碼標籤自動加到 PR 標題。只要標籤正確，通常不需手動修改 PR 標題。您只需確認一切正確且前綴已自動產生。

#### 合併策略

我們預設使用 **Squash and Merge** 作為 PR 合併策略。此策略確保 commit 訊息符合格式，即使個別 commit 不符合。

**原因**：

- 保持專案歷史乾淨且線性。
- commit 訊息一致。
- 減少瑣碎 commit（例如「修正錯字」）的干擾。

合併時，請確保最終 commit 訊息符合上述格式。

**Squash and Merge 範例**

若 PR 包含以下 commit：

- `fix typo`
- `update README`
- `adjust formatting`

合併後應壓縮為：
`Docs: Improve documentation clarity and formatting (#65)`

### 發佈流程

本節說明維護者如何簡單地發佈 Co-op Translator 新版本。

#### 1. 調整 `pyproject.toml` 中的版本號

1. 決定下一個版本號（遵循語義版本控制：`MAJOR.MINOR.PATCH`）。
2. 編輯 `pyproject.toml`，更新 `[tool.poetry]` 下的 `version` 欄位。
3. 開啟專門修改版本號（及自動更新的鎖定/元資料檔案，如有）的 PR。
4. 經審查後，使用 **Squash and Merge**，並確保最終 commit 訊息符合上述格式。

#### 2. 建立 GitHub Release

1. 前往 GitHub 倉庫頁面，開啟 **Releases** → **Draft a new release**。
2. 從 `main` 分支建立新標籤（例如 `v0.13.0`）。
3. 將發佈標題設為相同版本號（例如 `v0.13.0`）。
4. 點選 **Generate release notes** 自動產生變更日誌。
5. 可選擇編輯文字（例如強調新增支援語言或重要變更）。
6. 發佈 Release。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->