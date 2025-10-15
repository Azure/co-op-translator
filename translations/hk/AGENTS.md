<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:22:11+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hk"
}
-->
## 專案概覽

Co‑op Translator 是一個 Python 指令行工具及 GitHub Actions 工作流程，能將 Markdown 文件、Jupyter 筆記本及圖片文字翻譯成多種語言。翻譯結果會按語言分類存放，並保持與原始內容同步。此專案以 Poetry 管理，並設有 CLI 入口點。

### 架構概覽

- CLI 入口點（`translate`、`migrate-links`、`evaluate`）會呼叫統一的 CLI，分派至翻譯、連結遷移及評估流程。
- 設定載入器會讀取 `.env`，自動偵測 LLM 供應商（Azure OpenAI 或 OpenAI），如有需要亦會偵測影像供應商（Azure AI Service）以提取圖片文字。
- 翻譯核心負責 Markdown 及筆記本；影像流程於使用 `-img` 時提取圖片文字。
- 輸出會按語言存放於 `translations/<lang>/`（文字）及 `translated_images/`（圖片），保留原有結構。

### 主要技術及框架

- Python 3.10–3.12，Poetry 作為套件管理
- CLI：`click`
- LLM/AI SDK：Azure OpenAI、OpenAI
- 影像：Azure AI Service（Computer Vision）
- HTTP 及資料：`httpx`、`pydantic`
- 影像處理：`pillow`、`opencv-python`、`matplotlib`
- 工具：`pytest`、`black`、`ruff`

## 安裝指令

### 先決條件

- Python 3.10–3.12
- Azure 訂閱（選用，供 Azure AI 服務）
- 可連接網絡以使用 LLM/影像 API（如 Azure OpenAI/OpenAI、Azure AI Vision）

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

## 最終用戶使用方法

### Docker（已發佈映像）

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

備註：
- 預設入口點為 `translate`。如需遷移連結，請用 `--entrypoint migrate-links`。
- 請確保 GHCR 套件設為公開，方便匿名拉取。

### CLI（pip）

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### 環境設定

請於倉庫根目錄建立 `.env` 檔，並填寫所選語言模型及（選用）影像服務的憑證/端點。各供應商的詳細設定請參閱 `getting_started/set-up-azure-ai.md`。

### 必需環境變數

至少需設定一個 LLM 供應商。如需圖片翻譯，亦必須設定 Azure AI Service。

- Azure OpenAI（文字翻譯）：
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI（文字翻譯替代）：
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID`（選用）
  - `OPENAI_CHAT_MODEL_ID`（使用 OpenAI 供應商時必需）
  - `OPENAI_BASE_URL`（選用，預設 `https://api.openai.com/v1`）

- Azure AI Service（圖片文字提取，使用 `-img` 時必需）：
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

備註：

- 工具會自動偵測可用的 LLM 供應商；只需設定 Azure OpenAI 或 OpenAI 其中之一。
- 圖片翻譯需同時設定 `AZURE_AI_SERVICE_API_KEY` 及 `AZURE_AI_SERVICE_ENDPOINT`。
- 如缺少必需變數，CLI 會清楚提示錯誤。

## 開發流程

- 原始碼存放於 `src/co_op_translator`，測試於 `tests/`。
- 主要 CLI（經入口點安裝）：

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

更多使用說明請參閱 `getting_started/`。

## 測試指引

於倉庫根目錄執行測試。部分測試需 API 憑證，如無可略過。

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

## 程式碼風格指引

- 格式化工具：Black（於 `pyproject.toml` 設定，行長 88）
- 靜態檢查：Ruff（於 `pyproject.toml` 設定，行長 120）
- 型別檢查：mypy（已設配置，如有安裝可啟用）

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

請將 Python 原始碼放於 `src/`，測試放於 `tests/`，並優先使用明確的套件命名空間匯入（`co_op_translator.*`）。

## 建構及部署

建構產物會發佈至 `dist/`。

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

支援 GitHub Actions 自動化，詳見：

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### 容器映像（GHCR）

- 官方映像：`ghcr.io/azure/co-op-translator:<tag>`
- 標籤：`latest`（main 分支）、語意標籤如 `vX.Y.Z`、及 `sha` 標籤
- 多架構：Buildx 支援 `linux/amd64, linux/arm64`
- Dockerfile 模式：於 builder 階段建構依賴（需 `build-essential` 及 `python3-dev`），於運行階段由本地 wheelhouse 安裝（`pip install --no-index --find-links=/wheels`）
- 工作流程：`.github/workflows/docker-publish.yml` 負責建構及推送至 GHCR

## 安全注意事項

- 請將 API 金鑰及端點存放於 `.env` 或 CI 機密庫，切勿提交敏感資料。
- 如需圖片翻譯，必須提供 Azure AI Vision 金鑰及端點；否則可省略 `-img`。
- 執行大量翻譯時，請確認供應商配額及速率限制。

## Pull Request 指引

### 提交前

1. **測試你的更改：**
   - 完整執行受影響的筆記本
   - 確認所有 cell 無錯誤
   - 檢查輸出是否合適

2. **文件更新：**
   - 新增概念時請更新 `README.md`
   - 複雜程式碼請於筆記本加註解
   - 確保 markdown cell 說明用途

3. **檔案更動：**
   - 請勿提交 `.env`（請用 `.env.example`）
   - 不要提交 `venv/` 或 `__pycache__/` 目錄
   - 筆記本輸出如有示範概念可保留
   - 刪除臨時檔及備份筆記本（如 `*-backup.ipynb`）

4. **風格及格式：**
   - 請遵守風格及格式指引
   - 執行 `poetry run black .` 及 `poetry run ruff check .` 檢查格式

5. **新增/更新測試及 CLI 說明：**
   - 更改行為時請新增或更新測試
   - CLI 說明需與更改保持一致


### Commit 訊息及合併策略

預設採用 Squash and Merge。最終 squash commit 訊息格式如下：

```bash
<type>: <description> (#<PR number>)
```

允許類型：
- `Docs` — 文件更新
- `Build` — 建構系統、依賴、設定/CI
- `Core` — 核心功能及特性（如 `src/co_op_translator/core`）

範例：
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

備註：
- PR 標題通常會根據標籤自動加前綴，請確認自動產生的前綴正確。

### PR 標題格式

請用清晰、簡潔的標題。建議與最終 squash commit 結構一致：
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## 除錯及疑難排解

- 常見問題及解決方法：`getting_started/troubleshooting.md`
- 支援語言及注意事項（包括字型/已知問題）：`getting_started/supported-languages.md`
- 筆記本連結問題，請重新執行：`migrate-links -l "all" -y`

## 給 Agents 的備註

- 建議使用 Poetry 以確保環境可重現；如無則用 `requirements.txt`。
- 於 CI 執行 CLI 時，請以環境變數或 `.env` 注入所需機密。
- 如為 monorepo 用戶，本倉庫可獨立使用，無需協調子套件。

- 多架構指引：如需支援 ARM 用戶（Apple Silicon/ARM 伺服器），請保留 `linux/arm64`；否則只用 `linux/amd64` 亦可簡化流程。
- 如用戶偏好容器，請指引至 `README.md` 的 Docker 快速入門；因引號差異，請同時提供 Bash 及 PowerShell 範例。

---

**免責聲明**：
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能會包含錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。我們不會對因使用本翻譯而引起的任何誤解或錯誤負責。