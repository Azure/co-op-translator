<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:15:03+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "tw"
}
-->
# 設定 Azure OpenAI 進行語言翻譯

## 在 Azure AI Foundry 建立 Azure OpenAI 資源

要在 Azure AI Foundry 設定 Azure OpenAI，請依照以下步驟操作：

### 建立 Hub

1. 登入 [Azure AI Foundry 入口網站](https://ai.azure.com)：確定你已使用 Azure 帳戶登入。

2. 前往管理中心：從首頁左側選單選擇「管理中心」。

3. 建立新 Hub：點選「+ 新增 hub」，輸入必要資訊，如訂閱、資源群組及 Hub 名稱，我們建議將 Hub 部署在 East US，因為該區域支援認知視覺和 GPT 模型。

4. 檢查並建立：確認資訊無誤後，點選「建立」以完成 Hub 設定。

### 建立專案

1. 前往首頁：如果你還沒在首頁，請點選頁面左上角的「Azure AI Foundry」回到首頁。

2. 建立專案：點選「+ 建立專案」，並輸入專案名稱。

3. 選擇 Hub：如果你有多個 Hub，請選擇你要使用的 Hub。若想建立新 Hub，也可以在這一步驟完成。

4. 設定專案：依照提示設定專案需求。

5. 建立專案：點選「建立」完成專案設定。

### 部署 OpenAI 模型及端點

1. 登入 [Azure AI Foundry 入口網站](https://ai.azure.com)：確定你已使用擁有 Azure OpenAI 服務資源的 Azure 訂閱登入。

2. 前往模型與端點：在 Azure AI Foundry 首頁，找到「模型與端點」的區塊並選擇「Let's go.」或從左側選單點選「模型與端點」。

3. 如果尚未部署 GPT 模型，請選擇部署模型：建議使用 GPT-4o、GPT-4o-mini 或 o3-mini。

4. 存取你的資源：你會看到現有的 Azure OpenAI 服務資源，若有多個資源，請用選擇器選擇你要使用的資源。

欲取得更詳細的說明，請參考官方 Azure AI Foundry 文件。

[How to Create a project](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[How to Create resources](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[How to use OpenAI Model in AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[OpenAI Services in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們力求準確，但請注意，自動翻譯可能會包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所引起之任何誤解或誤釋負責。