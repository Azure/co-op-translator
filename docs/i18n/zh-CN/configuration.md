# 配置

Co-op 翻译器需要一个语言模型提供者。图像翻译另外需要 Azure AI Vision。

配置从环境变量读取。对于本地项目，请将它们放在项目根目录的 `.env` 文件中。

有关 Azure 资源设置，请参阅 [Azure AI 设置](azure-ai-setup.md)。

## 本地运行时设置

在本地运行 CLI 之前请使用虚拟环境。Co-op 翻译器支持 Python 3.11 到 3.14。

对于常规 CLI 使用，请在虚拟环境中安装已发布的包：

### Windows（PowerShell）

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### 仓库开发

对于仓库开发，请从项目根目录安装依赖：

```bash
poetry install
poetry run translate --help
```

在 CLI 可用后，在 `.env` 中配置一个语言模型提供者。

## 提供者选择

该工具按以下顺序自动检测提供者：

1. Azure OpenAI
2. OpenAI
3. Anthropic

翻译需要提供者凭据，但诸如 `translate -l "ko" -md --dry-run` 之类的预览除外。`migrate-links`、`co-op-review` 和 `run_review` 是确定性的维护操作，不需要提供者凭据。

## 模型客户端后端

从 Co-op 翻译器 0.22.0 开始，Azure OpenAI、OpenAI 和 Anthropic 默认使用 Microsoft Agent Framework。常规使用无需设置后端。

Semantic Kernel 暂时仍可用于兼容性。要显式选择它，请设置：

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

使用 Semantic Kernel 会发出弃用警告。计划在 0.23.0 中将 Semantic Kernel 移至可选依赖，并在 0.24.0 中移除该集成，具体取决于兼容性结果和用户反馈。Anthropic 需要 `agent-framework`；在 Anthropic 情况下显式选择 `semantic-kernel` 会导致配置错误。无效的值会在基于提供者的翻译器初始化期间失败，而不是静默回退。请关注推出进度并在 [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543) 中报告阻碍问题。

## Azure OpenAI

当您的模型部署在 Azure AI Foundry 或 Azure OpenAI Service 时使用 Azure OpenAI。

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

在开始翻译之前，连通性检查会使用端点、API 密钥、API 版本和部署名称进行验证。

## OpenAI

直接调用 OpenAI API 时使用 OpenAI。

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` 是必需的，因为翻译器在进行 API 调用时需要明确的聊天模型。

在默认设置下保持 `OPENAI_ORG_ID` 和 `OPENAI_BASE_URL` 不设置。仅在您的帐户需要时添加组织 ID，或仅在使用自定义端点时添加 base URL。不要为可选设置复制占位符值。

## Anthropic Claude

直接调用 Claude API 时使用 Anthropic。创建一个 [Anthropic API 密钥](https://platform.claude.com/docs/en/get-started) 并选择一个支持的 [Claude 模型 ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)。

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` 和 `ANTHROPIC_MODEL` 是必需的。您无需设置 `CO_OP_TRANSLATOR_MODEL_CLIENT`；Agent Framework 是默认的后端。

对于 Anthropic API，保持 `ANTHROPIC_BASE_URL` 不设置。仅在使用自定义端点时设置它。

`ANTHROPIC_MAX_TOKENS` 的默认值为 `8192`，这为诸如 Meitei Mayek 等高密度标记脚本留下了空间。如果您的模型或与 Anthropic 兼容的端点将输出限制在此以下，请将其降低。

## Azure AI Vision

图像翻译需要 Azure AI Vision，以便工具在配置的语言模型进行翻译之前从图像中提取文本。Anthropic 可以像 Azure OpenAI 或 OpenAI 一样翻译提取的文本。

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

如果通过 `-img`、`images=True` 或未使用内容类型筛选选择了图像翻译，工具会在翻译开始之前验证 Vision 配置。

## 多重凭证集

配置层通过在变量后添加相同索引的后缀来支持多个凭证集：

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

每个凭证集必须完整。健康检查会在继续翻译之前选择一个可用的凭证集。

OpenAI 和 Anthropic 支持相同的后缀约定。请将凭证集中所有变量保留在相同的后缀下，包括诸如 `OPENAI_BASE_URL_1` 或 `ANTHROPIC_BASE_URL_1` 等可选值。

## 命令要求

| 命令或 API | 是否需要 LLM | 是否需要 Vision | 说明 |
| --- | --- | --- | --- |
| `translate -md` | 是 | 否 | 仅翻译 Markdown。 |
| `translate -nb` | 是 | 否 | 仅翻译笔记本。 |
| `translate -img` | 是 | 是 | 仅翻译图像。 |
| `translate` 在未指定类型标志时 | 是 | 是 | 默认模式包含 Markdown、笔记本和图像。 |
| `evaluate` | 是 | 否 | 使用 LLM 进行评估，除非选择了 `--fast`。 |
| `migrate-links` | 否 | 否 | 在不调用提供者的情况下执行本地链接迁移。 |
| `co-op-review` | 否 | 否 | 执行确定性的翻译结构、新鲜度、Markdown、笔记本和本地链接检查。 |
| `run_translation(markdown=True)` | 是 | 否 | 面向程序的 Markdown 翻译。 |
| `run_translation(images=True)` | 是 | 是 | 面向程序的图像翻译。 |
| `run_review(...)` | 否 | 否 | 面向程序的确定性审查。 |

## 输出目录

默认文本翻译输出：

```text
translations/<language-code>/<source-relative-path>
```

默认翻译后图像输出：

```text
translated_images/<language-code>/<source-relative-path>
```

Python API 可以使用 `translations_dir` 和 `image_dir` 覆盖这些目录。