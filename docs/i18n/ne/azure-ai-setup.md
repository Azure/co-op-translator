# Azure AI सेटअप

यो मार्गदर्शक तब प्रयोग गर्नुहोस् जब तपाईंले पाठ अनुवादका लागि Azure OpenAI र छविहरूबाट पाठ निकाल्न Azure AI Vision कन्फिगर गर्न चाहनुहुन्छ।

## पूर्वआवश्यकताहरू

- एक Azure सदस्यता।
- Azure AI स्रोतहरू र मोडेल डिप्लोयमेन्टहरू सिर्जना वा प्रयोग गर्ने अनुमति।
- Azure AI Foundry मा एउटा परियोजना वा Azure OpenAI र Azure AI Vision स्रोतहरूमा समकक्ष पहुँच।

## Azure AI परियोजना सिर्जना गर्नुहोस्

1. खोल्नुहोस् [Azure AI Foundry](https://ai.azure.com).
2. परियोजना सिर्जना वा छान्नुहोस्।
3. परियोजनाको लागि AI हब सिर्जना वा छान्नुहोस्।
4. सिर्जना पछि परियोजना अवलोकन खोल्नुहोस्।

## Azure OpenAI मोडेल डिप्लोय गर्नुहोस्

1. परियोजनामा, **Models + endpoints** खोल्नुहोस्।
2. **Deploy model** चयन गर्नुहोस्।
3. `gpt-4o` जस्तै GPT मोडेल रोज्नुहोस्।
4. मोडेल डिप्लोय गर्नुहोस्।
5. endpoint, deployment name, model name, API key, र API version रेकर्ड गर्नुहोस्।

!!! note
    Azure OpenAI API संस्करण Azure AI Foundry मा देखाइएको मोडेल संस्करण भन्दा फरक हुन्छ। तपाइँको परिनियोजनका लागि समर्थित API संस्करण रोज्नुहोस्।

## Azure AI Vision कन्फिगर गर्नुहोस्

छवि अनुवादले पाठ अनुवाद हुनु अघि स्रोत छविहरूबाट पाठ निकाल्न Azure AI Vision प्रयोग गर्छ।

तपाईंको Azure AI परियोजनामा, Azure AI Services कुञ्जी र endpoint फेला पार्नुहोस्।

![Azure AI सेवा जानकारी फेला पार्नुहोस्](../../assets/find-azure-ai-info.png)

रेकर्ड:

- Azure AI Service endpoint
- Azure AI Service API key

## वातावरण भेरिएबलहरू

आफ्नो प्रमाणपत्रहरू `.env` फाइल वा CI secrets मा थप्नुहोस्।

```bash
# Azure AI Vision, छवि अनुवादका लागि आवश्यक
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, पाठ अनुवादका लागि आवश्यक
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator पनि वैकल्पिक फालब्याक क्रेडेन्सियल सेटहरूलाई समर्थन गर्छ। `_1` वा `_2` जस्ता उपसर्गहरूसँग एउटा पूरा प्रोभाइडर सेट डुप्लिकेट गर्नुहोस्; फालब्याक सेटमा भएका सबै भेरिएबलहरूले एउटै उपसर्ग साझा गर्नुपर्छ।

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## अर्को चरणहरू

- स्थानीय वा CI वातावरण भेरिएबलहरू सेटअप गर्न [Configuration](configuration.md) मा फर्कनुहोस्।
- अनुवाद आदेशहरूको लागि [CLI Reference](cli.md) प्रयोग गर्नुहोस्।
- अनुवाद पुल अनुरोधहरू स्वचालित गर्न [GitHub Actions](github-actions.md) प्रयोग गर्नुहोस्।