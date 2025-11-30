<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T10:07:36+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "zh"
}
-->
# 参与 Co-op Translator 项目贡献

本项目欢迎贡献和建议。大多数贡献需要您同意一份贡献者许可协议（CLA），声明您有权利且确实授予我们使用您贡献内容的权利。详情请访问 https://cla.opensource.microsoft.com。

当您提交拉取请求时，CLA 机器人会自动判断您是否需要提供 CLA，并相应地标注 PR（例如状态检查、评论）。只需按照机器人提供的指示操作即可。您只需在所有使用我们 CLA 的仓库中完成一次此操作。

## 开发环境搭建

建议使用 Poetry 来管理本项目的依赖。我们使用 `pyproject.toml` 管理项目依赖，因此安装依赖时应使用 Poetry。

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

3. 本地安装包：
    ```bash
    pip install -e .
    ```

4. 在测试文档上运行 Co-op Translator：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. 检查 `test_docs/translations` 和 `test_docs/translated_images` 中的翻译文件，确认：
   - 翻译质量
   - 元数据注释正确
   - 保持原始 Markdown 结构
   - 链接和图片正常显示

此手动测试有助于确保您的修改在实际场景中表现良好。

### 环境变量

1. 通过复制提供的 `.env.template` 文件，在根目录创建 `.env` 文件。
2. 按照指引填写环境变量。

> [!TIP]
>
> ### 额外的开发环境选项
>
> 除了本地运行项目外，您还可以使用 GitHub Codespaces 或 VS Code Dev Containers 作为替代的开发环境。
>
> #### GitHub Codespaces
>
> 您可以通过 GitHub Codespaces 虚拟运行示例，无需额外设置。
>
> 点击按钮将在浏览器中打开基于 Web 的 VS Code 实例：
>
> 1. 打开模板（可能需要几分钟）：
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### 使用 VS Code Dev Containers 本地运行
>
> ⚠️ 此选项仅在您的 Docker Desktop 分配了至少 16 GB 内存时有效。如果内存不足 16 GB，您可以尝试 [GitHub Codespaces 选项](../..) 或 [本地搭建](../..)。
>
> 相关选项是 VS Code Dev Containers，它会使用 [Dev Containers 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本地 VS Code 中打开项目：
>
> 1. 启动 Docker Desktop（如果未安装请先安装）
> 2. 打开项目：
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### 代码风格

我们使用 [Black](https://github.com/psf/black) 作为 Python 代码格式化工具，以保持项目代码风格一致。Black 是一款严格的代码格式化工具，会自动将 Python 代码格式化为符合 Black 风格的样式。

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

使用 Poetry 运行 Co-op Translator，请按以下步骤操作：

1. 进入您想进行翻译测试的目录，或新建一个临时文件夹用于测试。

2. 执行以下命令。将 `-l ko` 替换为您想翻译成的语言代码。`-d` 参数表示调试模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 运行命令前请确保已激活 Poetry 环境（poetry shell）。

## 贡献新语言支持

欢迎贡献新语言支持。提交 PR 前，请完成以下步骤以确保顺利审核。

1. 添加语言到字体映射
   - 编辑 `src/co_op_translator/fonts/font_language_mappings.yml`
   - 添加条目，包含：
     - `code`：类似 ISO 的语言代码（例如 `vi`）
     - `name`：友好的显示名称
     - `font`：`src/co_op_translator/fonts/` 中支持该文字脚本的字体文件
     - `rtl`：如果是从右向左书写则为 `true`，否则为 `false`

2. 包含所需字体文件（如有）
   - 如果需要新字体，请确认其许可证允许开源分发
   - 将字体文件添加到 `src/co_op_translator/fonts/`

3. 本地验证
   - 对小样本（Markdown、图片、笔记本等）运行翻译
   - 确认输出正确渲染，包括字体和 RTL 布局（如适用）

4. 更新文档
   - 确保语言出现在 `getting_started/supported-languages.md`
   - 无需修改 `getting_started/README_languages_template.md`，它由支持列表自动生成

5. 提交 PR
   - 描述新增语言及字体/许可证相关事项
   - 如可能，附上渲染效果截图

示例 YAML 条目：

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### 测试新语言

您可以通过以下命令测试新语言：

```bash
# 创建并激活虚拟环境
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# 安装开发包
pip install -e .
# 运行翻译
translate -l "new_lang"
```

## 维护者指南

### 提交信息和合并策略

为确保项目提交历史清晰一致，我们在使用 **Squash and Merge** 策略时，要求最终提交信息遵循特定格式。

当拉取请求（PR）合并时，所有提交会被压缩成一个提交。最终提交信息应遵循以下格式，以保持历史整洁。

#### 提交信息格式（适用于 squash and merge）

提交信息格式如下：

```bash
<type>: <description> (#<PR编号>)
```

- **type**：提交类别。我们使用以下类型：
  - `Docs`：文档更新。
  - `Build`：构建系统或依赖相关变更，包括配置文件、CI 工作流或 Dockerfile 更新。
  - `Core`：项目核心功能或特性修改，特别是涉及 `src/co_op_translator/core` 目录的文件。

- **description**：简洁的变更摘要。
- **PR number**：关联的拉取请求编号。

**示例**：

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> 目前，**`Docs`**、**`Core`** 和 **`Build`** 前缀会根据修改的源代码标签自动添加到 PR 标题。只要标签正确，通常无需手动修改 PR 标题。只需确认前缀生成正确即可。

#### 合并策略

我们默认使用 **Squash and Merge** 策略合并 PR。此策略确保提交信息符合格式要求，即使单个提交不符合。

**原因**：

- 保持项目历史清晰、线性。
- 提交信息一致。
- 减少琐碎提交带来的噪音（如“修正拼写错误”）。

合并时，请确保最终提交信息符合上述格式。

**Squash and Merge 示例**

如果 PR 包含以下提交：

- `fix typo`
- `update README`
- `adjust formatting`

合并后应为：
`Docs: Improve documentation clarity and formatting (#65)`

### 发布流程

本节介绍维护者发布 Co-op Translator 新版本的最简流程。

#### 1. 在 `pyproject.toml` 中更新版本号

1. 确定下一个版本号（遵循语义化版本号：`MAJOR.MINOR.PATCH`）。
2. 编辑 `pyproject.toml`，更新 `[tool.poetry]` 下的 `version` 字段。
3. 提交一个专门修改版本号（及自动更新的锁文件/元数据文件，如有）的 PR。
4. 审核通过后，使用 **Squash and Merge**，确保最终提交信息符合上述格式。

#### 2. 创建 GitHub Release

1. 进入 GitHub 仓库页面，打开 **Releases** → **Draft a new release**。
2. 从 `main` 分支创建新标签（例如 `v0.13.0`）。
3. 设置发布标题为版本号（例如 `v0.13.0`）。
4. 点击 **Generate release notes** 自动生成更新日志。
5. 可选编辑文本（例如突出新增语言或重要变更）。
6. 发布该版本。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->