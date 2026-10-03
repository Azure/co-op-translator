# 维护者指南

本页概述了 API、CLI 与文档站点如何协同工作。

## 公共 API 边界

稳定的 Python API 从以下位置导出：

```python
co_op_translator.api
```

公共 API 组织为内容翻译辅助、路径重写辅助、项目编排和审查：

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` 是托管集成的持久化边界。
它必须将生成的候选与已接受的基线分开存放，以便
未合并的翻译不会成为真实来源。

添加新的公共 API 时，更新：

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- 相关的 API 测试位于 `tests/co_op_translator/` 下，例如 `test_api.py` 或 `test_review_api.py`

避免将较低级别的 `core` 模块作为稳定 API 记录，除非项目打算直接支持它们。

## CLI 入口点

该包定义了这些 Poetry 脚本：

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` 根据脚本名称调度：

- `translate` 调用 `co_op_translator.cli.translate.translate_command`
- `evaluate` 调用 `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` 调用 `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` 调用 `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` 绕过 `__main__.py`，直接调用 `co_op_translator.mcp.server:main`。

添加或更改 CLI 选项时，更新：

- 相关的 `src/co_op_translator/cli/*.py` 命令
- `docs/cli.md`
- 如果行为发生改变，更新与 CLI 相关的测试

## MCP 服务器

MCP 服务器的实现位于：

```python
co_op_translator.mcp.server
```

服务器有意包装公共 Python API，而不是调用较低级别的 `core` 模块。保持此边界完整，以便 MCP 客户端、Python 调用者和 CLI 具有相同的行为。

添加或更改 MCP 工具时，更新：

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- 如果公共 API 面发生变化，更新 `docs/api.md`

仓库翻译工具可以通过 MCP 以模型方式调用并能写入多个文件。将 `dry_run=True` 保持为默认，并在非 dry-run 的项目翻译之前要求 `confirm_write=True`。

## 翻译流程

高层次的项目翻译流程为：

1. 解析 CLI 参数或 API 参数。
2. 使用 `LLMConfig` 验证 LLM 配置。
3. 当选择图像翻译时验证 Azure AI Vision。
4. 规范化语言代码。
5. 检测旧版语言文件夹别名。
6. 估算翻译量。
7. 在适用时更新 README 的语言/课程部分。
8. 将项目翻译委托给 `ProjectTranslator`。
9. `ProjectTranslator` 将文件处理委托给 `TranslationManager`。

`TranslationManager` 由面向文件类型的 mixin 组成：

- `ProjectMarkdownTranslationMixin` 处理 Markdown 文件读取、内容翻译、路径重写、元数据、免责声明和写入。
- `ProjectNotebookTranslationMixin` 处理笔记本文件读取、Markdown 单元格翻译、路径重写、元数据、免责声明和写入。
- `ProjectImageTranslationMixin` 处理图像发现、文本提取/翻译、渲染图像写入和元数据。

较低层次的内容 API 跳过项目工作流：

1. `translate_markdown_content` 和 `translate_notebook_content` 仅翻译内存中的内容。
2. `translate_image_content` 翻译单个图像中的文本并返回渲染后的图像对象。
3. `rewrite_markdown_paths` 和 `rewrite_notebook_paths` 是显式的后处理辅助函数。它们不执行翻译，也不进行项目写入。

## 审查流程

确定性的审查流程为：

1. 解析 CLI 参数或 API 参数。
2. 规范化请求的语言代码。
3. 从 `root_dir`、`root_dirs` 或 `groups` 构建一个或多个审查目标。
4. 可选择使用 `--changed-from` 限制源文件。
5. 对结构、翻译新鲜度、Markdown 完整性以及本地链接/图像路径运行确定性检查。
6. 输出文本或 GitHub 风格的 Markdown。
7. 当发现审查错误时以失败状态退出。

审查流程不需要 API 密钥，并且可用于本地检查或消费者选择加入的 CI。本仓库不会在每个 pull request 上自动运行 `co-op-review`。

## 文档站点

文档站点由以下内容配置：

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` 目录是规范的文档源。除非项目有意引入另一个发布的文档面，否则不要在该目录之外添加新的终端用户指南。

本地构建：

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

本地预览：

```bash
python -m mkdocs serve
```

生成的站点写入到 `site/`，该目录被 git 忽略。

## GitHub Pages 工作流

`.github/workflows/docs.yml` 在 pull request 上构建站点，并在推送到 `main` 时部署。

该工作流安装：

```bash
pip install -r requirements-docs.txt
```

文档工作流仅安装文档工具链。`mkdocs.yml` 将 `mkdocstrings` 指向 `src/`，因此可以在不安装完整运行时依赖集的情况下从源树渲染公共 API 页面。如果将来的 API 文档在构建期间需要导入可选的运行时提供者，请同时更新 `.github/workflows/docs.yml` 和本指南。

## 文档质量标准

在合并文档更改之前，运行：

```bash
python -m mkdocs build --strict
git diff --check
```

使用严格构建，以便损坏的链接、无效的导航条目和 API 渲染问题能尽早失败。