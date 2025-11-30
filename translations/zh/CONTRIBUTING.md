<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:26:02+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "zh"
}
-->
# 参与 Co-op Translator 项目

欢迎大家为本项目贡献代码和提出建议。大多数贡献都需要你同意一份贡献者许可协议（CLA），声明你有权并实际授予我们使用你的贡献的权利。详情请访问 https://cla.opensource.microsoft.com。

当你提交 Pull Request 时，CLA 机器人会自动判断你是否需要签署 CLA，并在 PR 上做出相应标记（如状态检查、评论）。只需按照机器人的指示操作即可。你只需在所有使用我们 CLA 的仓库中做一次即可。

## 开发环境搭建

建议使用 Poetry 管理依赖。我们通过 `pyproject.toml` 管理项目依赖，因此安装依赖时请使用 Poetry。

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

#### pip 和 Poetry 通用

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

### 安装项目及依赖包

#### 使用 Poetry（从 pyproject.toml）

```bash
poetry install
```

### 手动测试

在提交 PR 前，建议用真实文档测试翻译功能：

1. 在项目根目录创建一个测试目录：
    ```bash
    mkdir test_docs
    ```

2. 把你想翻译的部分 markdown 文档和图片复制到测试目录。例如：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 本地安装包：
    ```bash
    pip install -e .
    ```

4. 在你的测试文档上运行 Co-op Translator：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. 检查 `test_docs/translations` 和 `test_docs/translated_images` 下的翻译文件，确认：
   - 翻译质量
   - 元数据注释是否正确
   - 原有 markdown 结构是否保留
   - 链接和图片是否正常

手动测试可以确保你的修改在实际场景下表现良好。

### 环境变量

1. 在根目录下复制 `.env.template` 文件，创建 `.env` 文件。
2. 按提示填写环境变量。

> [!TIP]
>
> ### 其他开发环境选项
>
> 除了本地运行项目，你还可以使用 GitHub Codespaces 或 VS Code Dev Containers 作为开发环境。
>
> #### GitHub Codespaces
>
> 你可以直接在 GitHub Codespaces 上运行示例，无需额外设置。
>
> 点击按钮将在浏览器中打开基于 Web 的 VS Code 实例：
>
> 1. 打开模板（可能需要几分钟）：
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### 本地使用 VS Code Dev Containers
>
> ⚠️ 只有当你的 Docker Desktop 至少分配了 16 GB 内存时，此选项才可用。如果内存不足 16 GB，可以尝试 [GitHub Codespaces 选项](../..) 或 [本地搭建](../..)。
>
> 相关选项是 VS Code Dev Containers，可以通过 [Dev Containers 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本地 VS Code 打开项目：
>
> 1. 启动 Docker Desktop（如未安装请先安装）
> 2. 打开项目：
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>

### 代码风格

我们使用 [Black](https://github.com/psf/black) 作为 Python 代码格式化工具，确保项目代码风格统一。Black 会自动将 Python 代码格式化为标准风格。

#### 配置

Black 的配置在我们的 `pyproject.toml` 文件中：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### 安装 Black

你可以通过 Poetry（推荐）或 pip 安装 Black：

##### 使用 Poetry

搭建开发环境时会自动安装 Black：
```bash
poetry install
```

##### 使用 pip

如果用 pip，可以直接安装 Black：
```bash
pip install black
```

#### 使用 Black

##### 配合 Poetry

1. 格式化项目所有 Python 文件：
    ```bash
    poetry run black .
    ```

2. 格式化指定文件或目录：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### 配合 pip

1. 格式化项目所有 Python 文件：
    ```bash
    black .
    ```

2. 格式化指定文件或目录：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 建议在编辑器中设置保存时自动用 Black 格式化代码。大多数现代编辑器都支持相关插件或扩展。

## 运行 Co-op Translator

在你的环境中使用 Poetry 运行 Co-op Translator，步骤如下：

1. 进入你想进行翻译测试的目录，或新建一个临时文件夹用于测试。

2. 执行以下命令。将 `-l ko` 替换为你想翻译的目标语言代码。`-d` 参数表示调试模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 运行命令前请确保已激活 Poetry 环境（poetry shell）。

## 新增语言支持

欢迎大家为项目添加新语言支持。请在提交 PR 前完成以下步骤，以便顺利审核。

1. 添加语言到字体映射
   - 编辑 `src/co_op_translator/fonts/font_language_mappings.yml`
   - 添加如下内容：
     - `code`：类似 ISO 的语言代码（如 `vi`）
     - `name`：易读的显示名称
     - `font`：`src/co_op_translator/fonts/` 下支持该文字的字体
     - `rtl`：如为从右到左则为 `true`，否则为 `false`

2. 添加所需字体文件（如有需要）
   - 如需新字体，请确认其开源分发许可兼容
   - 将字体文件添加到 `src/co_op_translator/fonts/`

3. 本地验证
   - 用少量样例（Markdown、图片、notebook 等）进行翻译
   - 检查输出是否正确显示，包括字体和 RTL 布局（如适用）

4. 更新文档
   - 确保该语言已在 `getting_started/supported-languages.md` 中列出
   - 无需修改 `README_languages_template.md`，该文件会根据支持列表自动生成

5. 提交 PR
   - 说明新增语言及字体/许可相关事项
   - 如有可能，附上渲染效果截图

YAML 示例：

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## 维护者须知

### 提交信息与合并策略

为保证项目提交历史的规范和清晰，采用特定的提交信息格式（仅用于最终提交信息），并使用 **Squash and Merge** 合并策略。

当合并 Pull Request（PR）时，所有提交会被压缩为一个提交。最终提交信息需遵循以下格式，以保持历史整洁一致。

#### 提交信息格式（Squash and Merge）

提交信息格式如下：

```bash
<type>: <description> (#<PR number>)
```

- **type**：提交类别。包括以下类型：
  - `Docs`：文档更新。
  - `Build`：构建系统或依赖相关更改，包括配置文件、CI 工作流或 Dockerfile 更新。
  - `Core`：项目核心功能或特性修改，尤其涉及 `src/co_op_translator/core` 目录的文件。

- **description**：简要说明更改内容。
- **PR number**：对应 PR 的编号。

**示例**：

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> 目前，**`Docs`**、**`Core`** 和 **`Build`** 前缀会根据修改的源代码标签自动添加到 PR 标题。只要标签正确，一般无需手动修改 PR 标题。只需确认无误且前缀已正确生成即可。

#### 合并策略

我们默认采用 **Squash and Merge** 策略合并 PR。即使单独提交信息不规范，最终合并时也会统一格式。

**原因**：

- 项目历史更简洁、线性。
- 提交信息一致。
- 减少琐碎提交（如“fix typo”）带来的噪音。

合并时请确保最终提交信息符合上述格式。

**Squash and Merge 示例**
如果一个 PR 包含如下提交：

- `fix typo`
- `update README`
- `adjust formatting`

最终应压缩为：
`Docs: Improve documentation clarity and formatting (#65)`

---

**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本应视为权威来源。对于关键信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。