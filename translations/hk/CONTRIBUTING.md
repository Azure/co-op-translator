<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:27:53+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hk"
}
-->
# Contributing to Co-op Translator

呢個項目歡迎你嘅貢獻同建議。大部分貢獻都需要你同意一份Contributor License Agreement (CLA)，聲明你有權利並確實授權我哋使用你嘅貢獻。詳情請瀏覽 https://cla.opensource.microsoft.com。

當你提交 pull request 時，CLA bot 會自動判斷你係咪需要提供 CLA，並適當標示 PR（例如狀態檢查、留言）。只要跟住 bot 嘅指示做就得，所有使用我哋 CLA 嘅 repo 只需做一次。

## Development environment setup

要為呢個項目設置開發環境，我哋建議用 Poetry 管理依賴。我哋用 `pyproject.toml` 管理項目依賴，所以安裝依賴時應該用 Poetry。

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

提交 PR 前，好重要係用真實嘅文件測試翻譯功能：

1. 喺根目錄建立一個 test 目錄：
    ```bash
    mkdir test_docs
    ```

2. 複製啲你想翻譯嘅 markdown 文件同圖片入 test 目錄。例如：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 本地安裝呢個 package：
    ```bash
    pip install -e .
    ```

4. 喺你嘅測試文件上運行 Co-op Translator：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. 喺 `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` 睇翻譯後嘅文件。
1. 按指引填寫環境變量。

> [!TIP]
>
> ### 其他開發環境選項
>
> 除咗本地運行，你亦可以用 GitHub Codespaces 或 VS Code Dev Containers 作為替代嘅開發環境設置。
>
> #### GitHub Codespaces
>
> 你可以用 GitHub Codespaces 虛擬運行呢啲範例，唔需要額外設定。
>
> 呢個按鈕會喺瀏覽器打開一個基於 web 嘅 VS Code 實例：
>
> 1. 打開模板（可能需幾分鐘）：
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### 用 VS Code Dev Containers 本地運行
>
> ⚠️ 呢個選項只適用於 Docker Desktop 至少分配咗 16 GB RAM。如果你冇咁多 RAM，可以試下 [GitHub Codespaces 選項](../..) 或 [本地設置](../..)。
>
> 另一個選項係用 VS Code Dev Containers，會喺本地 VS Code 用 [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 打開項目：
>
> 1. 啟動 Docker Desktop（如果未裝就裝）
> 2. 打開項目：
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

我哋用 [Black](https://github.com/psf/black) 作為 Python 程式碼格式化工具，保持項目嘅代碼風格一致。Black 係一個嚴格嘅格式化工具，會自動將 Python 代碼格式化到符合 Black 嘅風格。

#### Configuration

Black 嘅設定寫喺我哋嘅 `pyproject.toml`：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Installing Black

你可以用 Poetry（建議）或者 pip 安裝 Black：

##### Using Poetry

開發環境設置時會自動安裝 Black：
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

1. 格式化項目內所有 Python 檔案：
    ```bash
    poetry run black .
    ```

2. 格式化指定檔案或資料夾：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### With pip

1. 格式化項目內所有 Python 檔案：
    ```bash
    black .
    ```

2. 格式化指定檔案或資料夾：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 建議你設定編輯器喺儲存時自動用 Black 格式化代碼。大部分現代編輯器都有擴充或插件支持。

## Running Co-op Translator

用 Poetry 喺你嘅環境運行 Co-op Translator，跟住以下步驟：

1. 去到你想做翻譯測試嘅目錄，或者建立一個臨時資料夾做測試。

2. 執行以下命令。`-l ko` with the language code you wish to translate into. The `-d` 係指 debug 模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 執行命令前，確保你已啟動 Poetry 環境（poetry shell）。

## Maintainers

### Commit message and Merge strategy

為咗保持項目嘅 commit 記錄一致同清晰，我哋喺用 **Squash and Merge** 策略時，對 **最終 commit message** 有特定格式要求。

當 pull request (PR) 合併時，所有獨立 commit 會被壓縮成一個 commit。最終 commit message 應該跟下面格式，保持歷史乾淨同一致。

#### Commit message format (for squash and merge)

我哋用以下格式寫 commit message：

```bash
<type>: <description> (#<PR number>)
```

- **type**: 指明 commit 類型。我哋用以下類型：
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
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原文的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或誤釋概不負責。