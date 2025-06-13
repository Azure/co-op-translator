<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:28:18+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tw"
}
-->
# Contributing to Co-op Translator

這個專案歡迎貢獻與建議。大多數貢獻需要你同意一份
Contributor License Agreement (CLA)，聲明你有權利且確實授權我們
使用你的貢獻。詳細資訊請參考 https://cla.opensource.microsoft.com。

當你提交 pull request 時，CLA bot 會自動判斷你是否需要提供
CLA 並適當標示 PR（例如，狀態檢查、留言）。只要照著 bot 的指示操作即可。
你只需在所有使用我們 CLA 的倉庫中執行一次。

## Development environment setup

要為這個專案設定開發環境，我們建議使用 Poetry 來管理相依套件。我們用 `pyproject.toml` 來管理專案相依，因此安裝相依時，請使用 Poetry。

### Create a virtual environment

#### Using pip

```bash
python -m venv .venv
```

#### Using Poetry

```bash
poetry init
```

### Activate the virtual environment

#### For both pip and Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Using Poetry

```bash
poetry shell
```

### Installing the Package and required Packages

#### Using Poetry (from pyproject.toml)

```bash
poetry install
```

### Manual testing

在提交 PR 前，測試翻譯功能是否能正常運作非常重要，請用真實文件測試：

1. 在根目錄建立一個測試資料夾：
    ```bash
    mkdir test_docs
    ```

2. 複製你想翻譯的 markdown 文件和圖片到測試資料夾。例如：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 在本地安裝套件：
    ```bash
    pip install -e .
    ```

4. 在測試文件上執行 Co-op Translator：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. 檢查 `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` 裡的翻譯結果。
1. 按照指示填寫環境變數。

> [!TIP]
>
> ### 額外的開發環境選項
>
> 除了在本地執行專案外，你也可以使用 GitHub Codespaces 或 VS Code Dev Containers 作為替代的開發環境。
>
> #### GitHub Codespaces
>
> 你可以直接用 GitHub Codespaces 虛擬執行這些範例，不需額外設定。
>
> 按鈕會在瀏覽器開啟一個基於網頁的 VS Code：
>
> 1. 開啟範本（可能需要幾分鐘）：
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### 使用 VS Code Dev Containers 在本地執行
>
> ⚠️ 此選項只在你的 Docker Desktop 分配至少 16 GB RAM 時有效。如果你 RAM 不足 16 GB，可以嘗試 [GitHub Codespaces 選項](../..) 或 [本地設定](../..)。
>
> 另一個選項是 VS Code Dev Containers，會用 [Dev Containers 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本地 VS Code 開啟專案：
>
> 1. 啟動 Docker Desktop（若未安裝請先安裝）
> 2. 開啟專案：
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

我們使用 [Black](https://github.com/psf/black) 作為 Python 代碼格式化工具，確保專案內代碼風格一致。Black 是個不妥協的格式化工具，會自動將 Python 程式碼格式化成符合 Black 風格。

#### Configuration

Black 的設定在我們的 `pyproject.toml` 中指定：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installing Black

你可以用 Poetry（推薦）或 pip 安裝 Black：

##### Using Poetry

設定開發環境時會自動安裝 Black：
```bash
poetry install
```

##### Using pip

如果用 pip，可以直接安裝 Black：
```bash
pip install black
```

#### Using Black

##### With Poetry

1. 格式化專案內所有 Python 檔案：
    ```bash
    poetry run black .
    ```

2. 格式化指定檔案或資料夾：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### With pip

1. 格式化專案內所有 Python 檔案：
    ```bash
    black .
    ```

2. 格式化指定檔案或資料夾：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 建議設定你的編輯器在儲存時自動用 Black 格式化程式碼。大多數現代編輯器都支援這類擴充或外掛。

## Running Co-op Translator

要在你的環境用 Poetry 執行 Co-op Translator，請照以下步驟：

1. 進入你想測試翻譯的資料夾，或建立一個暫存資料夾。

2. 執行以下指令。`-l ko` with the language code you wish to translate into. The `-d` 參數表示除錯模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 執行指令前請確定 Poetry 環境已啟動（poetry shell）。

## Maintainers

### Commit message and Merge strategy

為了確保專案提交紀錄清晰一致，我們在使用 **Squash and Merge** 策略時，對最終 commit message 有特定格式要求。

當 PR 合併時，所有單一 commit 會被壓縮成一個 commit。最終 commit message 請依照以下格式，維持乾淨且一致的歷史紀錄。

#### Commit message format (for squash and merge)

我們的 commit message 格式如下：

```bash
<type>: <description> (#<PR number>)
```

- **type**：指定 commit 類別。我們使用以下類型：
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。本公司不對因使用本翻譯所引起之任何誤解或誤譯負責。