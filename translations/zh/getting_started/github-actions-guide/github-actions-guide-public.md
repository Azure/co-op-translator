<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-05-07T14:01:07+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "zh"
}
-->
# 使用 Co-op Translator GitHub Action（公共设置）

**目标用户：** 本指南适用于大多数公共或私有仓库的用户，前提是标准的 GitHub Actions 权限已足够。它使用内置的 `GITHUB_TOKEN`。

使用 Co-op Translator GitHub Action，轻松实现仓库文档的自动翻译。本文将引导你设置该 Action，使其在源 Markdown 文件或图片发生更改时，自动创建包含更新翻译的拉取请求。

> [!IMPORTANT]
>
> **选择合适的指南：**
>
> 本指南介绍的是使用标准 `GITHUB_TOKEN` 的**简化设置方法**。这也是大多数用户推荐的方式，因为无需管理敏感的 GitHub App 私钥。
>

## 前提条件

在配置 GitHub Action 之前，请确保你已准备好所需的 AI 服务凭据。

**1. 必需：AI 语言模型凭据**  
你需要至少一个支持的语言模型的凭据：

- **Azure OpenAI**：需要 Endpoint、API Key、模型/部署名称、API 版本。  
- **OpenAI**：需要 API Key，（可选：组织 ID、基础 URL、模型 ID）。  
- 详情请参见 [Supported Models and Services](../../../../README.md)。

**2. 可选：AI 视觉凭据（用于图片翻译）**

- 仅当需要翻译图片中的文字时才需提供。  
- **Azure AI Vision**：需要 Endpoint 和订阅密钥。  
- 如果未提供，Action 将默认进入[仅 Markdown 模式](../markdown-only-mode.md)。

## 设置与配置

请按照以下步骤，使用标准 `GITHUB_TOKEN` 在你的仓库中配置 Co-op Translator GitHub Action。

### 步骤 1：了解身份验证（使用 `GITHUB_TOKEN`）

此工作流使用 GitHub Actions 提供的内置 `GITHUB_TOKEN`。该令牌根据第 3 步中配置的设置，自动赋予工作流与仓库交互的权限。

### 步骤 2：配置仓库 Secrets

你只需将**AI 服务凭据**作为加密的 Secrets 添加到仓库设置中。

1. 进入你的目标 GitHub 仓库。  
2. 打开 **Settings** > **Secrets and variables** > **Actions**。  
3. 依次点击 **New repository secret**，添加下面列出的每个所需 AI 服务 Secret。

![选择设置操作](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(图片参考：显示添加 Secrets 的位置)*

**必需的 AI 服务 Secrets（根据前提条件添加所有适用项）：**

| Secret 名称                         | 描述                                    | 值来源                           |
| :---------------------------------- | :-------------------------------------- | :------------------------------ |
| `AZURE_SUBSCRIPTION_KEY`            | Azure AI 服务（计算机视觉）的密钥           | 你的 Azure AI Foundry             |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI 服务（计算机视觉）的 Endpoint      | 你的 Azure AI Foundry             |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI 服务的密钥                     | 你的 Azure AI Foundry             |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI 服务的 Endpoint                | 你的 Azure AI Foundry             |
| `AZURE_OPENAI_MODEL_NAME`           | 你的 Azure OpenAI 模型名称                   | 你的 Azure AI Foundry             |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | 你的 Azure OpenAI 部署名称                    | 你的 Azure AI Foundry             |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI 的 API 版本                     | 你的 Azure AI Foundry             |
| `OPENAI_API_KEY`                    | OpenAI 的 API Key                         | 你的 OpenAI 平台                  |
| `OPENAI_ORG_ID`                     | OpenAI 组织 ID（可选）                      | 你的 OpenAI 平台                  |
| `OPENAI_CHAT_MODEL_ID`              | 特定的 OpenAI 模型 ID（可选）                 | 你的 OpenAI 平台                  |
| `OPENAI_BASE_URL`                   | 自定义 OpenAI API 基础 URL（可选）             | 你的 OpenAI 平台                  |

### 步骤 3：配置工作流权限

GitHub Action 需要通过 `GITHUB_TOKEN` 授权权限，才能检出代码并创建拉取请求。

1. 在仓库中，进入 **Settings** > **Actions** > **General**。  
2. 向下滚动到 **Workflow permissions** 部分。  
3. 选择 **Read and write permissions**。这将赋予 `GITHUB_TOKEN` 所需的 `contents: write` 和 `pull-requests: write` 权限。  
4. 确认勾选了 **Allow GitHub Actions to create and approve pull requests**。  
5. 点击 **Save**。

![权限设置](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### 步骤 4：创建工作流文件

最后，创建定义自动化工作流的 YAML 文件，使用 `GITHUB_TOKEN`。

1. 在仓库根目录下，如果不存在 `.github/workflows/` 文件夹，请创建它。  
2. 在 `.github/workflows/` 文件夹内，创建名为 `co-op-translator.yml` 的文件。  
3. 将以下内容粘贴到 `co-op-translator.yml` 中。

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
4. **自定义工作流：**  
  - **[!IMPORTANT] 目标语言：** 如有需要，可在 `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` 步骤中进行调整。

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们不承担任何责任。