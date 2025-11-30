<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:31:22+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hk"
}
-->
# 參與 Co-op Translator 貢獻

本項目歡迎各位貢獻及提出建議。大部分貢獻都需要你同意一份貢獻者授權協議（CLA），聲明你有權並確實授予我們使用你的貢獻的權利。詳情請瀏覽 https://cla.opensource.microsoft.com。

當你提交 pull request 時，CLA 機械人會自動判斷你是否需要提供 CLA，並在 PR 上作出相應標示（例如狀態檢查、留言）。只需跟隨機械人的指示操作即可。你只需在所有使用我們 CLA 的倉庫中做一次。

## 開發環境設置

建議使用 Poetry 來管理本項目的依賴。我們用 `pyproject.toml` 管理項目依賴，因此安裝依賴時應使用 Poetry。

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

#### pip 和 Poetry 均適用

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

### 安裝套件及所需依賴

#### 使用 Poetry（根據 pyproject.toml）

```bash
poetry install
```

### 手動測試

提交 PR 前，請用真實文件測試翻譯功能：

1. 在根目錄建立一個測試資料夾：
    ```bash
    mkdir test_docs
    ```

2. 複製一些你想翻譯的 markdown 文件及圖片到測試資料夾。例如：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 本地安裝套件：
    ```bash
    pip install -e .
    ```

4. 在你的測試文件上執行 Co-op Translator：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. 檢查 `test_docs/translations` 和 `test_docs/translated_images` 內的翻譯檔案，確認：
   - 翻譯質素
   - 元數據註釋正確
   - 原有 markdown 結構有保留
   - 連結及圖片運作正常

這個手動測試有助確保你的更改在真實情境下運作良好。

### 環境變數

1. 在根目錄複製 `.env.template` 檔案並建立 `.env` 檔案。
1. 按指引填寫環境變數。

> [!TIP]
>
> ### 額外開發環境選項
>
> 除了本地執行項目外，你亦可使用 GitHub Codespaces 或 VS Code Dev Containers 作為另一種開發環境設置。
>
> #### GitHub Codespaces
>
> 你可以用 GitHub Codespaces 虛擬執行這些範例，無需額外設置。
>
> 按下按鈕會在瀏覽器開啟網頁版 VS Code：
>
> 1. 開啟模板（可能需時數分鐘）：
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### 使用 VS Code Dev Containers 本地執行
>
> ⚠️ 此選項只適用於你的 Docker Desktop 分配至少 16 GB RAM。如少於 16 GB RAM，可考慮 [GitHub Codespaces 選項](../..) 或 [本地設置](../..)。
>
> 另一選項是 VS Code Dev Containers，會用 [Dev Containers 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本地 VS Code 開啟項目：
>
> 1. 啟動 Docker Desktop（如未安裝請先安裝）
> 2. 開啟項目：
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>

### 程式碼風格

我們使用 [Black](https://github.com/psf/black) 作為 Python 程式碼格式化工具，確保項目程式碼風格一致。Black 會自動將 Python 程式碼重整至其標準格式。

#### 設定

Black 的設定已在 `pyproject.toml` 指定：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### 安裝 Black

你可以用 Poetry（建議）或 pip 安裝 Black：

##### 使用 Poetry

設置開發環境時會自動安裝 Black：
```bash
poetry install
```

##### 使用 pip

如用 pip，可直接安裝 Black：
```bash
pip install black
```

#### 使用 Black

##### 配合 Poetry

1. 格式化項目內所有 Python 檔案：
    ```bash
    poetry run black .
    ```

2. 格式化指定檔案或資料夾：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### 配合 pip

1. 格式化項目內所有 Python 檔案：
    ```bash
    black .
    ```

2. 格式化指定檔案或資料夾：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 建議你設定編輯器自動在儲存時用 Black 格式化程式碼。大部分現代編輯器都支援相關擴充或插件。

## 執行 Co-op Translator

如要在你的環境用 Poetry 執行 Co-op Translator，請依以下步驟：

1. 進入你想進行翻譯測試的目錄，或建立一個臨時資料夾作測試用途。

2. 執行以下指令。將 `-l ko` 換成你想翻譯的語言代碼。`-d` 參數代表除錯模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 執行指令前，請確保已啟動 Poetry 環境（poetry shell）。

## 貢獻新語言

歡迎你為本項目新增語言支援。開 PR 前，請完成以下步驟以便順利審核。

1. 加入語言至字型映射
   - 編輯 `src/co_op_translator/fonts/font_language_mappings.yml`
   - 新增一項，包括：
     - `code`：類似 ISO 的語言代碼（如 `vi`）
     - `name`：易讀的顯示名稱
     - `font`：在 `src/co_op_translator/fonts/` 內提供、支援該文字的字型
     - `rtl`：如為由右至左語言則設為 `true`，否則 `false`

2. 加入所需字型檔（如有需要）
   - 如需新字型，請確認其授權可用於開源分發
   - 把字型檔加入 `src/co_op_translator/fonts/`

3. 本地驗證
   - 執行小量翻譯測試（Markdown、圖片及 notebook 視乎需要）
   - 確認輸出能正確顯示，包括字型及 RTL 版面（如適用）

4. 更新文件
   - 確保語言已列於 `getting_started/supported-languages.md`
   - `README_languages_template.md` 無需更改；它會根據支援列表自動生成

5. 開 PR
   - 說明新增語言及任何字型／授權考慮
   - 如可行，附上渲染結果截圖

YAML 範例：

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## 維護者

### Commit 訊息及合併策略

為確保項目 commit 歷史一致及清晰，當使用 **Squash and Merge** 策略時，最終 commit 訊息需遵循特定格式。

當 PR 合併時，所有 commit 會合併成一個。最終 commit 訊息需依以下格式，保持歷史整潔一致。

#### Commit 訊息格式（Squash and Merge 適用）

我們採用以下格式：

```bash
<type>: <description> (#<PR number>)
```

- **type**：指定 commit 類型。我們使用以下類型：
  - `Docs`：文件更新。
  - `Build`：與建構系統或依賴相關的更改，包括設定檔、CI 工作流程或 Dockerfile。
  - `Core`：項目核心功能或特性修改，特別是涉及 `src/co_op_translator/core` 目錄的檔案。

- **description**：簡明扼要描述更改內容。
- **PR number**：與 commit 相關的 pull request 編號。

**範例**：

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> 目前，**`Docs`**、**`Core`** 和 **`Build`** 前綴會根據修改的原始碼標籤自動加到 PR 標題。只要標籤正確，一般毋須手動更新 PR 標題。你只需確認一切正確，前綴已正確生成。

#### 合併策略

我們預設使用 **Squash and Merge** 合併 PR。此策略可確保 commit 訊息格式一致，即使個別 commit 不一致。

**原因**：

- 保持項目歷史簡潔線性。
- commit 訊息一致。
- 減少瑣碎 commit（如 "fix typo"）帶來的雜訊。

合併時，請確保最終 commit 訊息符合上述格式。

**Squash and Merge 範例**
如一個 PR 包含以下 commit：

- `fix typo`
- `update README`
- `adjust formatting`

合併後應為：
`Docs: Improve documentation clarity and formatting (#65)`

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。我們致力於確保翻譯的準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。如涉及重要資訊，建議尋求專業人工翻譯。本公司不會對因使用本翻譯而引起的任何誤解或誤釋承擔責任。