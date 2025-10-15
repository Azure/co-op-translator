<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:21:26+00:00",
  "source_file": "AGENTS.md",
  "language_code": "zh"
}
-->
## 项目概述

Co‑op Translator 是一个 Python 命令行工具和 GitHub Actions 工作流，可以将 Markdown 文件、Jupyter 笔记本和图片中的文本翻译成多种语言。它会将输出内容按语言分类存放在对应文件夹下，并保持翻译内容与源内容同步。项目采用 Poetry 管理，提供 CLI 入口。

### 架构概览

- CLI 入口（`translate`、`migrate-links`、`evaluate`）统一调用 CLI，分别分发到翻译、链接迁移和评估流程。
- 配置加载器读取 `.env` 文件，并自动检测 LLM 提供商（Azure OpenAI 或 OpenAI），如需图片文本提取则检测视觉服务（Azure AI Service）。
- 翻译核心处理 Markdown 和笔记本；视觉管道在使用 `-img` 时提取图片文本。
- 输出内容按语言存放在 `translations/<lang>/`，图片存放在 `translated_images/`，保持原有结构。

### 主要技术和框架

- Python 3.10–3.12，Poetry 打包
- CLI：`click`
- LLM/AI SDK：Azure OpenAI、OpenAI
- 视觉：Azure AI Service（计算机视觉）
- HTTP 和数据：`httpx`、`pydantic`
- 图像处理：`pillow`、`opencv-python`、`matplotlib`
- 工具：`pytest`、`black`、`ruff`

## 安装命令

### 前置条件

- Python 3.10–3.12
- Azure 订阅（可选，用于 Azure AI 服务）
- 能访问 LLM/视觉 API 的网络（如 Azure OpenAI/OpenAI、Azure AI Vision）

### 方案 A：Poetry（推荐）

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### 方案 B：pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## 终端用户使用方法

### Docker（已发布镜像）

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

注意事项：
- 默认入口为 `translate`。如需迁移链接可用 `--entrypoint migrate-links`。
- GHCR 包需设置为公开，便于匿名拉取。

### CLI（pip 安装）

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### 环境配置

在仓库根目录创建 `.env` 文件，填写所选语言模型和（可选）视觉服务的凭据/端点。各提供商的详细配置见 `getting_started/set-up-azure-ai.md`。

### 必需环境变量

至少需配置一个 LLM 提供商。图片翻译还需配置 Azure AI Service。

- Azure OpenAI（文本翻译）：
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI（文本翻译备选）：
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID`（可选）
  - `OPENAI_CHAT_MODEL_ID`（使用 OpenAI 时必填）
  - `OPENAI_BASE_URL`（可选，默认 `https://api.openai.com/v1`）

- Azure AI Service（图片文本提取，使用 `-img` 时必填）：
  - `AZURE_AI_SERVICE_API_KEY`（推荐）或旧版 `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

`.env` 示例片段：

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

注意：

- 工具会自动检测可用的 LLM 提供商，只需配置 Azure OpenAI 或 OpenAI 之一。
- 图片翻译需同时配置 `AZURE_AI_SERVICE_API_KEY` 和 `AZURE_AI_SERVICE_ENDPOINT`。
- 如缺少必需变量，CLI 会报错并提示。

## 开发流程

- 源码位于 `src/co_op_translator`，测试代码在 `tests/`。
- 主要 CLI（通过入口点安装）：

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

更多用法见 `getting_started/`。

## 测试说明

在仓库根目录运行测试。部分测试需 API 凭据，如无可跳过。

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

可选覆盖率（需安装 `coverage`）：

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## 代码风格规范

- 格式化工具：Black（`pyproject.toml` 配置，行宽 88）
- 代码检查：Ruff（`pyproject.toml` 配置，行宽 120）
- 类型检查：mypy（已配置，如安装可启用）

命令：

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Python 源码放在 `src/`，测试放在 `tests/`，包内建议使用显式导入（如 `co_op_translator.*`）。

## 构建与发布

构建产物发布到 `dist/`。

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

支持 GitHub Actions 自动化，详见：

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### 容器镜像（GHCR）

- 官方镜像：`ghcr.io/azure/co-op-translator:<tag>`
- 标签：`latest`（主分支）、语义标签如 `vX.Y.Z`、`sha` 标签
- 多架构：通过 Buildx 支持 `linux/amd64, linux/arm64`
- Dockerfile 模式：在 builder 阶段构建依赖 wheel（需 `build-essential` 和 `python3-dev`），运行时从本地 wheelhouse 安装（`pip install --no-index --find-links=/wheels`）
- 工作流：`.github/workflows/docker-publish.yml` 构建并推送到 GHCR

## 安全注意事项

- API 密钥和端点请存放在 `.env` 或 CI 密钥库，切勿提交到代码库。
- 图片翻译需 Azure AI Vision 密钥和端点，否则不要使用 `-img`。
- 大批量翻译时请确认服务商配额和速率限制。

## Pull Request 指南

### 提交前须知

1. **测试你的更改：**
   - 完整运行受影响的笔记本
   - 确认所有单元格无报错
   - 检查输出内容是否合理

2. **文档更新：**
   - 新增概念时请更新 `README.md`
   - 复杂代码请在笔记本中添加注释
   - Markdown 单元格需说明用途

3. **文件变更：**
   - 不要提交 `.env` 文件（请用 `.env.example`）
   - 不要提交 `venv/` 或 `__pycache__/` 目录
   - 如输出内容有助于理解，可保留笔记本输出
   - 删除临时文件和备份笔记本（如 `*-backup.ipynb`）

4. **风格与格式：**
   - 遵循风格和格式规范
   - 运行 `poetry run black .` 和 `poetry run ruff check .` 检查格式和风格问题

5. **添加/更新测试和 CLI 帮助：**
   - 行为变更时请添加或更新测试
   - CLI 帮助需与更改保持一致


### 提交信息和合并策略

默认采用 Squash and Merge。最终 squash 提交信息格式如下：

```bash
<type>: <description> (#<PR number>)
```

允许类型：
- `Docs` — 文档更新
- `Build` — 构建系统、依赖、配置/CI
- `Core` — 核心功能和特性（如 `src/co_op_translator/core`）

示例：
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

注意：
- PR 标题通常会根据标签自动加前缀，请确认生成的前缀是否正确。

### PR 标题格式

标题需简明清晰，建议与最终 squash 提交结构一致：
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## 调试与故障排查

- 常见问题及解决方法见：`getting_started/troubleshooting.md`
- 支持语言及说明（含字体/已知问题）：`getting_started/supported-languages.md`
- 笔记本链接问题可重新运行：`migrate-links -l "all" -y`

## 代理人须知

- 推荐使用 Poetry 保证环境可复现，否则可用 `requirements.txt`。
- 在 CI 中调用 CLI 时，请通过环境变量或 `.env` 注入所需密钥。
- 对于 monorepo 用户，本仓库作为独立包使用，无需协调子包。

- 多架构建议：如需支持 ARM 用户（Apple Silicon/ARM 服务器），请保留 `linux/arm64`；如无需求，仅用 `linux/amd64` 更简单。
- 如用户偏好容器使用，请引导至 `README.md` 的 Docker 快速入门，并提供 Bash 和 PowerShell 两种命令格式（因引号不同）。

---

**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。