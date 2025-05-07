<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-05-06T17:20:54+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tw"
}
-->
# Contributing to Co-op Translator

這個專案歡迎各種貢獻與建議。大部分的貢獻都需要你同意一份Contributor License Agreement (CLA)，聲明你有權利並且確實授權我們使用你的貢獻。詳細資訊請參考 https://cla.opensource.microsoft.com。

當你提交 pull request 時，CLA 機器人會自動判斷你是否需要提供 CLA，並在 PR 上做相應標示（例如狀態檢查、留言）。只要照著機器人指示操作即可。你只需在所有使用我們 CLA 的倉庫中做一次。

## Development environment setup

要設定這個專案的開發環境，我們建議使用 Poetry 來管理相依套件。我們使用 `pyproject.toml` 來管理專案相依，因此安裝相依時應使用 Poetry。

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

在提交 PR 前，測試翻譯功能是否正常非常重要，請用真實文件做測試：

1. 在專案根目錄建立一個測試資料夾：
    ```bash
    mkdir test_docs
    ```

2. 將你想翻譯的 markdown 文件和圖片複製到測試資料夾，例如：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 在本地安裝此套件：
    ```bash
    pip install -e .
    ```

4. 對測試文件執行 Co-op Translator：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. 查看翻譯後的檔案，位置在 `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`。
1. 按指示填寫環境變數。

> [!TIP]
>
> ### 額外的開發環境選項
>
> 除了在本機執行專案外，你也可以使用 GitHub Codespaces 或 VS Code Dev Containers 作為替代開發環境。
>
> #### GitHub Codespaces
>
> 你可以透過 GitHub Codespaces 虛擬執行這些範例，不需額外設定。
>
> 按鈕會在瀏覽器中開啟基於網頁的 VS Code：
>
> 1. 開啟範本（可能需幾分鐘）：
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### 使用 VS Code Dev Containers 在本機執行
>
> ⚠️ 這個選項只會在你的 Docker Desktop 分配至少 16 GB RAM 時才有效。如果 RAM 少於 16 GB，可以考慮使用 [GitHub Codespaces 選項](../..) 或 [在本機設定開發環境](../..)。
>
> 另一個選擇是 VS Code Dev Containers，會使用 [Dev Containers 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本機 VS Code 中開啟專案：
>
> 1. 啟動 Docker Desktop（若尚未安裝請先安裝）
> 2. 開啟專案：
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

我們使用 [Black](https://github.com/psf/black) 作為 Python 程式碼格式化工具，確保整個專案的程式碼風格一致。Black 是一個不妥協的格式化工具，會自動將 Python 程式碼格式化成符合 Black 風格的樣式。

#### Configuration

Black 的設定寫在我們的 `pyproject.toml`：

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

若使用 pip，可以直接安裝 Black：
```bash
pip install black
```

#### Using Black

##### With Poetry

1. 格式化專案中所有 Python 檔案：
    ```bash
    poetry run black .
    ```

2. 格式化特定檔案或資料夾：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### With pip

1. 格式化專案中所有 Python 檔案：
    ```bash
    black .
    ```

2. 格式化特定檔案或資料夾：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 建議設定你的編輯器，在存檔時自動用 Black 格式化程式碼。大多數現代編輯器都支援透過擴充功能或外掛做到這點。

## Running Co-op Translator

要在你的環境用 Poetry 執行 Co-op Translator，請依照以下步驟：

1. 切換到你想執行翻譯測試的資料夾，或建立一個暫存資料夾用於測試。

2. 執行下列指令。`-l ko` with the language code you wish to translate into. The `-d` 參數表示啟用除錯模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 執行指令前請確認已啟用 Poetry 環境（poetry shell）。

## Maintainers

### Commit message and Merge strategy

為了保持專案提交紀錄的一致性與清晰度，我們在使用 **Squash and Merge** 策略時，對 **最終提交訊息** 採用特定格式。

當 pull request (PR) 被合併時，所有個別提交會被壓縮成一個提交。最終提交訊息應遵守以下格式，以維持乾淨且一致的歷史紀錄。

#### Commit message format (for squash and merge)

我們使用以下格式撰寫提交訊息：

```bash
<type>: <description> (#<PR number>)
```

- **type**：指定提交類別。我們使用以下類別：
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
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於翻譯的準確性，但請注意自動翻譯可能會有錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤譯負責。