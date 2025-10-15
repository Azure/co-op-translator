<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:22:32+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tw"
}
-->
## 專案概述

Co‑op Translator 是一款 Python 命令列工具及 GitHub Actions 工作流程，能將 Markdown 檔案、Jupyter 筆記本及圖片文字翻譯成多種語言。翻譯結果會依語言分類存放，並與原始內容保持同步。此專案以 Poetry 管理，並提供 CLI 入口點。

### 架構概覽

- CLI 入口點（`translate`、`migrate-links`、`evaluate`）會呼叫統一的 CLI，分派至翻譯、連結遷移及評估流程。
- 設定載入器會讀取 `.env`，自動偵測 LLM 提供者（Azure OpenAI 或 OpenAI），如有需求也會偵測影像服務（Azure AI Service）以擷取圖片文字。
- 翻譯核心負責 Markdown 與筆記本，影像流程在使用 `-img` 時擷取圖片文字。
- 輸出會依語言存放於 `translations/<lang>/`，圖片則在 `translated_images/`，保留原始結構。

### 主要技術與框架

- Python 3.10–3.12，使用 Poetry 打包
- CLI：`click`
- LLM/AI SDK：Azure OpenAI、OpenAI
- 影像：Azure AI Service（Computer Vision）
- HTTP 與資料：`httpx`、`pydantic`
- 影像處理：`pillow`、`opencv-python`、`matplotlib`
- 工具：`pytest`、`black`、`ruff`

## 安裝指令

### 先決條件

- Python 3.10–3.12
- Azure 訂閱（選用，若需 Azure AI 服務）
- 可連網以存取 LLM/影像 API（如 Azure OpenAI/OpenAI、Azure AI Vision）

### 方案 A：Poetry（推薦）

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

## 最終使用者操作

### Docker（已發佈映像檔）

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

注意事項：
- 預設入口點為 `translate`。如需連結遷移，請用 `--entrypoint migrate-links` 覆蓋。
- GHCR 套件需設為公開，匿名拉取才可用。

### CLI（pip）

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### 環境設定

請在專案根目錄建立 `.env` 檔，並填入所選語言模型及（選用）影像服務的憑證/端點。各提供者詳細設定請參考 `getting_started/set-up-azure-ai.md`。

### 必要環境變數

至少需設定一個 LLM 提供者。若需圖片翻譯，亦須設定 Azure AI Service。

- Azure OpenAI（文字翻譯）：
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI（文字翻譯替代）：
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID`（選用）
  - `OPENAI_CHAT_MODEL_ID`（使用 OpenAI 時必填）
  - `OPENAI_BASE_URL`（選用，預設 `https://api.openai.com/v1`）

- Azure AI Service（圖片文字擷取，使用 `-img` 時必填）：
  - `AZURE_AI_SERVICE_API_KEY`（建議）或舊版 `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

`.env` 範例片段：

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

- 工具會自動偵測可用的 LLM 提供者，請設定 Azure OpenAI 或 OpenAI 其中之一。
- 圖片翻譯需同時設定 `AZURE_AI_SERVICE_API_KEY` 及 `AZURE_AI_SERVICE_ENDPOINT`。
- 若缺少必要變數，CLI 會明確提示錯誤。

## 開發流程

- 原始碼位於 `src/co_op_translator`，測試在 `tests/`。
- 主要 CLI（透過 entry points 安裝）：

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

更多使用說明請見 `getting_started/`。

## 測試說明

請於專案根目錄執行測試。有些測試需 API 憑證，若無可略過。

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

選用覆蓋率（需安裝 `coverage`）：

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## 程式風格規範

- 格式化工具：Black（`pyproject.toml` 設定，行長 88）
- 靜態檢查：Ruff（`pyproject.toml` 設定，行長 120）
- 型別檢查：mypy（已設定，安裝後可啟用）

指令：

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

請將 Python 原始碼放在 `src/`，測試放在 `tests/`，並優先使用明確的套件命名空間匯入（如 `co_op_translator.*`）。

## 建置與部署

建置產物會發佈至 `dist/`。

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

支援 GitHub Actions 自動化，詳見：

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### 容器映像檔（GHCR）

- 官方映像：`ghcr.io/azure/co-op-translator:<tag>`
- 標籤：`latest`（main 分支）、語意標籤如 `vX.Y.Z`、`sha` 標籤
- 多架構：支援 `linux/amd64, linux/arm64`（Buildx）
- Dockerfile 範例：在 builder 階段建 wheel（含 `build-essential`、`python3-dev`），runtime 階段從本地 wheelhouse 安裝（`pip install --no-index --find-links=/wheels`）
- 工作流程：`.github/workflows/docker-publish.yml` 負責建置並推送至 GHCR

## 安全注意事項

- API 金鑰及端點請存放於 `.env` 或 CI 機密庫，切勿提交至版本控制。
- 若需圖片翻譯，必須提供 Azure AI Vision 金鑰/端點；否則請勿使用 `-img`。
- 執行大量翻譯時，請確認提供者配額/速率限制。

## Pull Request 指南

### 提交前

1. **測試你的修改：**
   - 完整執行受影響的筆記本
   - 確認所有 cell 無錯誤
   - 檢查輸出是否合理

2. **文件更新：**
   - 新增概念時請更新 `README.md`
   - 複雜程式請在筆記本加註解
   - Markdown cell 需說明用途

3. **檔案變更：**
   - 請勿提交 `.env`（請用 `.env.example`）
   - 不要提交 `venv/` 或 `__pycache__/` 目錄
   - 筆記本輸出如有示範意義可保留
   - 刪除暫存檔及備份筆記本（如 `*-backup.ipynb`）

4. **風格與格式：**
   - 請遵循風格與格式規範
   - 執行 `poetry run black .` 及 `poetry run ruff check .` 檢查格式

5. **新增/更新測試與 CLI 說明：**
   - 行為有變更時請新增或更新測試
   - CLI 說明需與修改一致


### Commit 訊息與合併策略

預設採用 Squash and Merge。最終 squash commit 訊息格式如下：

```bash
<type>: <description> (#<PR number>)
```

允許類型：
- `Docs` — 文件更新
- `Build` — 建置系統、相依、設定/CI
- `Core` — 核心功能與特性（如 `src/co_op_translator/core`）

範例：
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

注意：
- PR 標題通常會依標籤自動加前綴，請確認產生的前綴正確。

### PR 標題格式

請用清楚、簡潔的標題。建議與最終 squash commit 結構一致：
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## 除錯與疑難排解

- 常見問題與解法：`getting_started/troubleshooting.md`
- 支援語言與注意事項（含字型/已知問題）：`getting_started/supported-languages.md`
- 筆記本連結問題，請重新執行：`migrate-links -l "all" -y`

## 給代理人的備註

- 建議使用 Poetry 以確保環境可重現；否則可用 `requirements.txt`。
- 在 CI 執行 CLI 時，請以環境變數或 `.env` 注入必要機密。
- 若為 monorepo 使用者，本 repo 為獨立套件，無需協調子套件。

- 多架構建議：如需支援 ARM（Apple Silicon/ARM 伺服器），請保留 `linux/arm64`；否則僅 `linux/amd64` 亦可簡化流程。
- 若用戶偏好容器，請指引至 `README.md` 的 Docker 快速入門，並提供 Bash 與 PowerShell 範例（因引號用法不同）。

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不精確之處。原始語言的文件應視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。