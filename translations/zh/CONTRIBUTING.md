<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:26:45+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "zh"
}
-->
# 贡献给 Co-op Translator

本项目欢迎贡献和建议。大多数贡献需要您同意一份贡献者许可协议（CLA），声明您有权利且确实授予我们使用您贡献内容的权利。详情请访问 https://cla.opensource.microsoft.com。

当您提交拉取请求时，CLA 机器人会自动判断您是否需要提供 CLA 并相应地标注 PR（例如，状态检查、评论）。只需按照机器人提供的指示操作。对于使用我们 CLA 的所有仓库，您只需操作一次。

## 开发环境设置

建议使用 Poetry 来管理本项目的依赖。我们使用 `pyproject.toml` 来管理项目依赖，因此安装依赖时请使用 Poetry。

### 创建虚拟环境

#### 使用 pip

```bash
python -m venv .venv
```

#### 使用 Poetry

```bash
poetry init
```

### 激活虚拟环境

#### 适用于 pip 和 Poetry

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

### 安装包及所需依赖

#### 使用 Poetry（根据 pyproject.toml）

```bash
poetry install
```

### 手动测试

在提交 PR 之前，务必使用真实文档测试翻译功能：

1. 在根目录创建一个测试目录：
    ```bash
    mkdir test_docs
    ```

2. 将你想翻译的部分 Markdown 文档和图片复制到测试目录。例如：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 本地安装该包：
    ```bash
    pip install -e .
    ```

4. 在测试文档上运行 Co-op Translator：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. 检查 `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` 文件中的翻译结果。
1. 按照指引填写环境变量。

> [!TIP]
>
> ### 额外的开发环境选项
>
> 除了本地运行项目外，您还可以使用 GitHub Codespaces 或 VS Code Dev Containers 作为替代的开发环境设置。
>
> #### GitHub Codespaces
>
> 您可以使用 GitHub Codespaces 虚拟运行这些示例，无需额外设置。
>
> 点击按钮将在浏览器中打开基于网页的 VS Code 实例：
>
> 1. 打开模板（可能需要几分钟）：
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### 使用 VS Code Dev Containers 本地运行
>
> ⚠️ 此选项仅在您的 Docker Desktop 分配至少 16 GB RAM 时有效。如果内存不足 16 GB，您可以尝试[GitHub Codespaces 选项](../..)或[本地设置](../..)。
>
> 相关选项是 VS Code Dev Containers，它会通过 [Dev Containers 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)在本地 VS Code 中打开项目：
>
> 1. 启动 Docker Desktop（若未安装请先安装）
> 2. 打开项目：
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### 代码风格

我们使用 [Black](https://github.com/psf/black) 作为 Python 代码格式化工具，以保持项目代码风格一致。Black 是一个毫不妥协的代码格式化工具，会自动将 Python 代码格式化为 Black 的代码风格。

#### 配置

Black 的配置在我们的 `pyproject.toml` 中指定：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### 安装 Black

您可以通过 Poetry（推荐）或 pip 安装 Black：

##### 使用 Poetry

设置开发环境时会自动安装 Black：
```bash
poetry install
```

##### 使用 pip

如果使用 pip，可以直接安装 Black：
```bash
pip install black
```

#### 使用 Black

##### 使用 Poetry

1. 格式化项目中所有 Python 文件：
    ```bash
    poetry run black .
    ```

2. 格式化指定文件或目录：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### 使用 pip

1. 格式化项目中所有 Python 文件：
    ```bash
    black .
    ```

2. 格式化指定文件或目录：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 建议配置编辑器在保存时自动使用 Black 格式化代码。大多数现代编辑器通过扩展或插件支持此功能。

## 运行 Co-op Translator

在您的环境中使用 Poetry 运行 Co-op Translator，请按以下步骤操作：

1. 进入您想进行翻译测试的目录，或者新建一个临时文件夹用于测试。

2. 执行以下命令。`-l ko` with the language code you wish to translate into. The `-d` 参数表示调试模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 运行命令前请确保已激活 Poetry 环境（poetry shell）。

## 维护者

### 提交信息和合并策略

为确保项目提交历史的统一和清晰，我们在使用 **Squash and Merge** 策略时，要求**最终提交信息**遵循特定格式。

当拉取请求（PR）合并时，所有单个提交会被压缩成一个提交。最终提交信息应遵循以下格式，以保持历史的整洁和一致。

#### 提交信息格式（用于 squash and merge）

我们使用如下格式撰写提交信息：

```bash
<type>: <description> (#<PR number>)
```

- **type**：指定提交类别。我们使用以下类型：
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: 更新安装说明以提高清晰度 (#50)`
- `Core: 改进图片翻译处理 (#60)`

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

- `修正拼写错误`
- `更新 README`
- `调整格式`

They should be squashed into:
`Docs: 改进文档清晰度和格式 (#65)`

**免责声明**：  
本文件由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译而成。尽管我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始文件的原文版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译内容而产生的任何误解或误释，我们概不负责。