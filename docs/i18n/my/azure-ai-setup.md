# Azure AI စတင်ပြင်ဆင်ခြင်း

Use this guide when you want to configure Azure OpenAI for text translation and Azure AI Vision for image text extraction.

## Prerequisites

- An Azure subscription.
- Permission to create or use Azure AI resources and model deployments.
- A project in Azure AI Foundry or equivalent access to Azure OpenAI and Azure AI Vision resources.

## Create an Azure AI Project

1. [Azure AI Foundry](https://ai.azure.com) ကို ဖွင့်ပါ။
2. ပရောဂျက် အသစ် တစ်ခု ဖန်တီးရန် သို့မဟုတ် ရွေးချယ်ပါ။
3. ပရောဂျက်အတွက် AI hub တစ်ခု ဖန်တီးရန် သို့မဟုတ် ရွေးချယ်ပါ။
4. ဖန်တီးပြီးနောက် ပရောဂျက် အကျဉ်းချုံး ကို ဖွင့်ပါ။

## Deploy an Azure OpenAI Model

1. ပရောဂျက်တွင် **Models + endpoints** ကို ဖွင့်ပါ။
2. **Deploy model** ကို ရွေးပါ။
3. ဥပမာ `gpt-4o` အဖြစ် GPT မော်ဒယ် တစ်ခု ရွေးချယ်ပါ။
4. မော်ဒယ်ကို တပ်ဆင်ပါ။
5. endpoint, deployment name, model name, API key, နှင့် API version များကို မှတ်ထားပါ။

!!! note
    Azure OpenAI API version သည် Azure AI Foundry တွင် ပြသထားသော model version နှင့် သီးခြားပါသည်။ သင့် deployment အတွက် ထောက်ပံ့ထားသော API version ကို ရွေးချယ်ပါ။

## Configure Azure AI Vision

Image translation uses Azure AI Vision to extract text from source images before the text is translated.

In your Azure AI project, find the Azure AI Services key and endpoint.

![Azure AI service အချက်အလက်များ ရှာဖွေပါ](../../assets/find-azure-ai-info.png)

Record:

- Azure AI Service endpoint
- Azure AI Service API key

## Environment Variables

Add the credentials to your `.env` file or CI secrets.

```bash
# Azure AI Vision, ပုံဘာသာပြန်ခြင်းအတွက် လိုအပ်သည်
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, စာသားဘာသာပြန်ခြင်းအတွက် လိုအပ်သည်
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator also supports optional fallback credential sets. Duplicate a complete provider set with suffixes such as `_1` or `_2`; all variables in a fallback set must share the same suffix.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Next Steps

- Return to [ဆက်တင်](configuration.md) to set up local or CI environment variables.
- Use [CLI Reference](cli.md) for translation commands.
- Use [GitHub Actions](github-actions.md) to automate translation pull requests.