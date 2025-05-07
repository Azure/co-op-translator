<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87bf95d45e684475ef1e67d8dae5f6eb",
  "translation_date": "2025-05-06T18:10:53+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "tw"
}
-->
# 使用 Co-op Translator GitHub Action（公開設定）

**目標讀者：** 本指南適用於大多數公共或私人倉庫，這些倉庫的標準 GitHub Actions 權限已足夠使用。本指南採用內建的 `GITHUB_TOKEN`。

使用 Co-op Translator GitHub Action，輕鬆自動化您倉庫文件的翻譯。當您的原始 Markdown 檔案或圖片有變動時，本指南會帶您設定該 Action，自動建立包含更新翻譯的拉取請求。

> [!IMPORTANT]
>
> **選擇正確的指南：**
>
> 本指南說明了使用標準 `GITHUB_TOKEN` 的**簡易設定**。這是大多數使用者推薦的方法，因為不需管理敏感的 GitHub App 私鑰。
>

## 前置條件

在設定 GitHub Action 前，請先準備好所需的 AI 服務憑證。

**1. 必備：AI 語言模型憑證**  
您需要至少一組支援的語言模型憑證：

- **Azure OpenAI**：需提供 Endpoint、API Key、Model/Deployment 名稱、API 版本。  
- **OpenAI**：需提供 API Key，（可選：組織 ID、Base URL、Model ID）。  
- 詳細資訊請參閱 [Supported Models and Services](../../../../README.md)。  
- 設定指南：[Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)。

**2. 選用：電腦視覺憑證（用於圖片翻譯）**

- 只有在需要翻譯圖片內文字時才需要。  
- **Azure Computer Vision**：需提供 Endpoint 與訂閱金鑰。  
- 若未提供，Action 預設以 [Markdown-only mode](../markdown-only-mode.md) 執行。  
- 設定指南：[Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md)。

## 設定與配置

請依照以下步驟，使用標準 `GITHUB_TOKEN` 在您的倉庫中設定 Co-op Translator GitHub Action。

### 步驟 1：了解認證機制（使用 `GITHUB_TOKEN`）

此工作流程使用 GitHub Actions 內建的 `GITHUB_TOKEN`。此 token 會根據 **步驟 3** 中設定的權限，自動授予工作流程與倉庫互動的權限。

### 步驟 2：設定倉庫密鑰

您只需在倉庫設定中，將**AI 服務憑證**以加密密鑰形式新增。

1. 進入目標 GitHub 倉庫。  
2. 點選 **Settings** > **Secrets and variables** > **Actions**。  
3. 在 **Repository secrets** 下，針對以下每個必要的 AI 服務密鑰點選 **New repository secret**。

    ![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(圖片參考：顯示新增密鑰位置)*

**必須的 AI 服務密鑰（請依前置條件新增所有適用項目）：**

| 密鑰名稱                           | 說明                                     | 來源                           |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`            | Azure AI 服務（電腦視覺）金鑰               | 您的 Azure AI Foundry             |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI 服務（電腦視覺）端點               | 您的 Azure AI Foundry             |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI 服務金鑰                       | 您的 Azure AI Foundry             |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI 服務端點                       | 您的 Azure AI Foundry             |
| `AZURE_OPENAI_MODEL_NAME`           | 您的 Azure OpenAI 模型名稱                   | 您的 Azure AI Foundry             |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | 您的 Azure OpenAI 部署名稱                    | 您的 Azure AI Foundry             |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API 版本                        | 您的 Azure AI Foundry             |
| `OPENAI_API_KEY`                    | OpenAI API Key                           | 您的 OpenAI 平台                  |
| `OPENAI_ORG_ID`                     | OpenAI 組織 ID（可選）                     | 您的 OpenAI 平台                  |
| `OPENAI_CHAT_MODEL_ID`              | 特定 OpenAI 模型 ID（可選）                  | 您的 OpenAI 平台                  |
| `OPENAI_BASE_URL`                   | 自訂 OpenAI API 基底 URL（可選）             | 您的 OpenAI 平台                  |

### 步驟 3：設定工作流程權限

GitHub Action 需要透過 `GITHUB_TOKEN` 授權，以檢出程式碼並建立拉取請求。

1. 在您的倉庫中，前往 **Settings** > **Actions** > **General**。  
2. 向下捲動至 **Workflow permissions** 區塊。  
3. 選擇 **Read and write permissions**。這會授予 `GITHUB_TOKEN` 執行此工作流程所需的 `contents: write` 和 `pull-requests: write` 權限。  
4. 確認勾選 **Allow GitHub Actions to create and approve pull requests**。  
5. 點選 **Save**。

![Permission setting](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### 步驟 4：建立工作流程檔案

最後，建立定義自動化工作流程的 YAML 檔案，使用 `GITHUB_TOKEN`。

1. 在倉庫根目錄下，若 `.github/workflows/` 目錄尚未存在，請先建立。  
2. 在 `.github/workflows/` 目錄內，建立名為 `co-op-translator.yml` 的檔案。  
3. 將以下內容貼入 `co-op-translator.yml`。

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```  
4. **自訂工作流程：**  
  - **[!IMPORTANT] 目標語言：** 若需要，請在 `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` 步驟中調整。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生之任何誤解或誤譯負責。