# 配置

Co-op Translator requires one language model provider. Image translation additionally requires Azure AI Vision.

配置从环境变量中读取。对于本地项目，请将它们放在项目根目录的 `.env` 文件中。

有关 Azure 资源设置，请参阅 [Azure AI 设置](azure-ai-setup.md)。

## 本地运行时设置

在本地运行 CLI 之前，请使用虚拟环境。Co-op Translator 支持 Python 3.10 到 3.12。

对于常规 CLI 使用，请在虚拟环境中安装已发布的软件包：

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

对于仓库开发，请改从项目根目录安装依赖项：

```bash
poetry install
poetry run translate --help
```

在 CLI 可用后，在 `.env` 中配置一个语言模型提供程序。

## Provider selection

该工具按以下顺序自动检测提供程序：

1. Azure OpenAI
2. OpenAI

如果未配置任一提供程序，`translate`、`evaluate`、`migrate-links` 和 `run_translation` 将在配置检查期间失败。`co-op-review` 和 `run_review` 是确定性的维护检查，不需要提供程序凭据。

## Azure OpenAI

当您的模型部署在 Azure AI Foundry 或 Azure OpenAI Service 时，请使用 Azure OpenAI。

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

连接性检查在翻译开始之前会使用端点、API 密钥、API 版本和部署名称。

## OpenAI

当直接调用 OpenAI API 时，请使用 OpenAI。

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # 可选
OPENAI_BASE_URL="..."        # 可选
```

`OPENAI_CHAT_MODEL_ID` 是必需的，因为翻译器在进行 API 调用时需要明确的聊天模型。

## Azure AI Vision

图像翻译需要 Azure AI Vision，以便工具在翻译之前从图像中提取文本。

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

如果通过 `-img`、`images=True` 选择图像翻译，或未设置内容类型过滤器，工具将在翻译开始之前验证 Vision 配置。

## Multiple credential sets

配置层通过在变量后附加相同的索引来支持多组凭据：

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

每组必须完整。健康检查会在翻译继续之前选择一个可用的凭据集。

## Command requirements

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | Yes | No | Translates Markdown only. |
| `translate -nb` | Yes | No | Translates notebooks only. |
| `translate -img` | Yes | Yes | Translates images only. |
| `translate` with no type flags | Yes | Yes | Default mode includes Markdown, notebooks, and images. |
| `evaluate` | Yes | No | Uses LLM evaluation unless `--fast` is selected. |
| `migrate-links` | Yes | No | Performs link migration, but still runs shared configuration checks. |
| `co-op-review` | No | No | Runs deterministic translation structure, freshness, Markdown, notebook, and local link checks. |
| `run_translation(markdown=True)` | Yes | No | Programmatic Markdown translation. |
| `run_translation(images=True)` | Yes | Yes | Programmatic image translation. |
| `run_review(...)` | No | No | Programmatic deterministic review. |

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