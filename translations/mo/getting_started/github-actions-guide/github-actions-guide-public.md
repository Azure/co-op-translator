<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-06-12T19:23:25+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "mo"
}
-->
# 使用 Co-op Translator GitHub Action（公開設定）

**目標讀者：** 本指南適用於大多數公共或私有儲存庫中，且標準 GitHub Actions 權限足夠的使用者。它使用內建的 `GITHUB_TOKEN`。

輕鬆自動化您儲存庫文件的翻譯工作，透過 Co-op Translator GitHub Action。本指南將帶您完成設定此 Action，使其在您的原始 Markdown 檔案或圖片變更時，自動建立包含更新翻譯的拉取請求。

> [!IMPORTANT]
>
> **選擇合適的指南：**
>
> 本指南詳述使用標準 `GITHUB_TOKEN` 的**簡易設定**。這是大多數使用者推薦的方法，因為它不需要管理敏感的 GitHub App 私鑰。
>

## 先決條件

在設定 GitHub Action 之前，請確保您已準備好必要的 AI 服務憑證。

**1. 必要：AI 語言模型憑證**  
您需要至少一組受支援語言模型的憑證：

- **Azure OpenAI**：需要 Endpoint、API Key、Model/Deployment 名稱、API 版本。  
- **OpenAI**：需要 API Key，（可選：Org ID、Base URL、Model ID）。  
- 詳情請參閱 [Supported Models and Services](../../../../README.md)。

**2. 選擇性：AI 視覺憑證（用於圖片翻譯）**

- 僅在您需要翻譯圖片中的文字時才需提供。  
- **Azure AI Vision**：需要 Endpoint 和 Subscription Key。  
- 若未提供，Action 將預設使用[僅 Markdown 模式](../markdown-only-mode.md)。

## 設定與配置

請依照以下步驟，使用標準 `GITHUB_TOKEN` 在您的儲存庫中配置 Co-op Translator GitHub Action。

### 步驟 1：了解認證機制（使用 `GITHUB_TOKEN`）

此工作流程使用 GitHub Actions 內建的 `GITHUB_TOKEN`。該令牌會根據第 3 步的設定，自動授予工作流程與您的儲存庫互動的權限。

### 步驟 2：設定儲存庫秘密

您只需將**AI 服務憑證**以加密秘密的形式新增至儲存庫設定。

1. 進入目標 GitHub 儲存庫。  
2. 前往 **Settings** > **Secrets and variables** > **Actions**。  
3. 在 **Repository secrets** 下，點選 **New repository secret**，為下方列出的每個必需 AI 服務秘密新增。

    ![Select setting action](../../../../translated_images/select-setting-action.32e2394813d09dc148494f34daea40724f24ff406de889f26cbbbf05f98ed621.mo.png) *(圖片參考：顯示新增秘密的位置)*

**必要的 AI 服務秘密（根據您的先決條件，請全部新增適用的）：**

| 秘密名稱                         | 說明                                   | 來源                            |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`            | Azure AI 服務（電腦視覺）的金鑰               | 您的 Azure AI Foundry             |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI 服務（電腦視覺）的端點               | 您的 Azure AI Foundry             |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI 服務的金鑰                      | 您的 Azure AI Foundry             |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI 服務的端點                      | 您的 Azure AI Foundry             |
| `AZURE_OPENAI_MODEL_NAME`           | 您的 Azure OpenAI 模型名稱                    | 您的 Azure AI Foundry             |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | 您的 Azure OpenAI 部署名稱                     | 您的 Azure AI Foundry             |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI 的 API 版本                       | 您的 Azure AI Foundry             |
| `OPENAI_API_KEY`                    | OpenAI 的 API 金鑰                          | 您的 OpenAI 平台                  |
| `OPENAI_ORG_ID`                     | OpenAI 組織 ID（選填）                      | 您的 OpenAI 平台                  |
| `OPENAI_CHAT_MODEL_ID`              | 特定 OpenAI 模型 ID（選填）                   | 您的 OpenAI 平台                  |
| `OPENAI_BASE_URL`                   | 自訂 OpenAI API 基底 URL（選填）              | 您的 OpenAI 平台                  |

### 步驟 3：設定工作流程權限

GitHub Action 需要透過 `GITHUB_TOKEN` 授予權限，以便簽出程式碼並建立拉取請求。

1. 在您的儲存庫中，前往 **Settings** > **Actions** > **General**。  
2. 滾動至 **Workflow permissions** 區段。  
3. 選擇 **Read and write permissions**。這將授予 `GITHUB_TOKEN` 執行此工作流程所需的 `contents: write` 與 `pull-requests: write` 權限。  
4. 確認已勾選 **Allow GitHub Actions to create and approve pull requests**。  
5. 點選 **Save**。

![Permission setting](../../../../translated_images/permission-setting.cb1f57fdb5194f0743b1f6932f221e404ae2928ee88d77f1de39aba46fbf774a.mo.png)

### 步驟 4：建立工作流程檔案

最後，建立定義自動化工作流程的 YAML 檔案，使用 `GITHUB_TOKEN`。

1. 在您的儲存庫根目錄中，若尚未存在，請建立 `.github/workflows/` 目錄。  
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
  - **[!IMPORTANT] 目標語言：** 如有需要，請在 `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` 步驟中調整。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於翻譯的準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。