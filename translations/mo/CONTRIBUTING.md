<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-14T12:46:48+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "mo"
}
-->
# 貢獻給 Co-op Translator

這個專案歡迎貢獻和建議。大多數貢獻需要您同意一份貢獻者授權協議 (CLA)，聲明您有權並且確實授予我們使用您的貢獻的權利。詳細資訊請訪問 https://cla.opensource.microsoft.com。

當您提交一個拉取請求時，CLA 機器人會自動判定您是否需要提供 CLA 並適當地裝飾 PR（例如，狀態檢查、評論）。只需按照機器人提供的指示操作即可。您只需在所有使用我們 CLA 的倉庫中做一次。

## 開發環境設置

為了設置此專案的開發環境，我們建議使用 Poetry 來管理依賴項。我們使用 `pyproject.toml` 來管理專案依賴項，因此，要安裝依賴項，您應使用 Poetry。

### 創建虛擬環境

#### 使用 pip

```bash
python -m venv .venv
```

#### 使用 Poetry

```bash
poetry init
```

### 激活虛擬環境

#### 適用於 pip 和 Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### 使用 Poetry

```bash
poetry shell
```

### 安裝套件和所需套件

#### 使用 Poetry（從 pyproject.toml）

```bash
poetry install
```

### 手動測試

在提交 PR 之前，使用真實文件測試翻譯功能是很重要的：

1. 在根目錄中創建一個測試目錄：
    ```bash
    mkdir test_docs
    ```

2. 將一些您想翻譯的 Markdown 文件和圖片複製到測試目錄中。例如：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 在本地安裝套件：
    ```bash
    pip install -e .
    ```

4. 在您的測試文件上運行 Co-op Translator：
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

1. Create an `.env` file in the root directory by copying the provided `.env.template` 文件中的翻譯文件。
1. 按指導填寫環境變數。

> [!TIP]
>
> ### 額外的開發環境選項
>
> 除了在本地運行專案外，您還可以使用 GitHub Codespaces 或 VS Code Dev Containers 來設置替代的開發環境。
>
> #### GitHub Codespaces
>
> 您可以使用 GitHub Codespaces 虛擬運行這些範例，並且不需要額外的設置或配置。
>
> 該按鈕將在您的瀏覽器中打開基於 Web 的 VS Code 實例：
>
> 1. 打開模板（這可能需要幾分鐘）：
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### 本地運行使用 VS Code Dev Containers
>
> ⚠️ 此選項僅在您的 Docker Desktop 分配至少 16 GB RAM 時有效。如果您的 RAM 少於 16 GB，可以嘗試 [GitHub Codespaces 選項](../..) 或 [在本地設置](../..)。
>
> 相關選項是 VS Code Dev Containers，這將使用 [Dev Containers 擴展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本地 VS Code 中打開專案：
>
> 1. 啟動 Docker Desktop（如果未安裝則安裝）
> 2. 打開專案：
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

### 代碼風格

我們使用 [Black](https://github.com/psf/black) 作為我們的 Python 代碼格式化工具，以在專案中維持一致的代碼風格。Black 是一個毫不妥協的代碼格式化工具，它會自動重新格式化 Python 代碼以符合 Black 代碼風格。

#### 配置

Black 的配置在我們的 `pyproject.toml` 中指定：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### 安裝 Black

您可以使用 Poetry（推薦）或 pip 安裝 Black：

##### 使用 Poetry

當您設置開發環境時，Black 會自動安裝：
```bash
poetry install
```

##### 使用 pip

如果您使用 pip，可以直接安裝 Black：
```bash
pip install black
```

#### 使用 Black

##### 使用 Poetry

1. 格式化專案中的所有 Python 文件：
    ```bash
    poetry run black .
    ```

2. 格式化特定文件或目錄：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### 使用 pip

1. 格式化專案中的所有 Python 文件：
    ```bash
    black .
    ```

2. 格式化特定文件或目錄：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 我們建議設置您的編輯器以在保存時自動使用 Black 格式化代碼。大多數現代編輯器都支持通過擴展或插件來實現此功能。

## 運行 Co-op Translator

要在您的環境中使用 Poetry 運行 Co-op Translator，請按照以下步驟操作：

1. 導航到您想進行翻譯測試的目錄或創建一個臨時文件夾以進行測試。

2. 執行以下命令。替換 `-l ko` with the language code you wish to translate into. The `-d` 標誌表示調試模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 在運行命令之前，請確保您的 Poetry 環境已激活（poetry shell）。

## 維護者

### 提交信息和合併策略

為了確保我們專案的提交歷史的一致性和清晰度，我們遵循特定的提交信息格式 **用於最終提交信息** 當使用 **Squash and Merge** 策略。

當拉取請求（PR）被合併時，個別提交將被壓縮為一個提交。最終提交信息應遵循以下格式以保持整潔和一致的歷史。

#### 提交信息格式（用於壓縮和合併）

我們使用以下格式的提交信息：

```bash
<type>: <description> (#<PR number>)
```

- **type**: 指定提交的類別。我們使用以下類型：
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: 更新安裝說明以提高清晰度 (#50)`
- `Core: 改進圖片翻譯處理 (#60)`

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

- `修正錯字`
- `更新 README`
- `調整格式`

They should be squashed into:
`Docs: 改善文件清晰度和格式 (#65)`

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們不對使用此翻譯所引起的任何誤解或誤釋承擔責任。