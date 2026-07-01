# Azure AI सेटअप

हा मार्गदर्शक वापरा जेव्हा तुम्हाला मजकूर भाषांतरासाठी Azure OpenAI आणि प्रतिमेमधील मजकूर काढण्यासाठी Azure AI Vision कॉन्फिगर करायचा असेल.

## पूर्वआवश्यकता

- एक Azure सदस्यता.
- Azure AI संसाधने आणि मॉडेल डिप्लॉयमेंट तयार करण्याची किंवा वापरण्याची परवानगी.
- Azure AI Foundry मध्ये एक प्रकल्प किंवा Azure OpenAI आणि Azure AI Vision संसाधनांमध्ये समकक्ष प्रवेश.

## Azure AI प्रकल्प तयार करा

1. [Azure AI Foundry](https://ai.azure.com) उघडा.
2. एक प्रकल्प तयार करा किंवा निवडा.
3. प्रकल्पासाठी एआय हब तयार करा किंवा निवडा.
4. तयार झाल्यावर प्रकल्प अवलोकन उघडा.

## Azure OpenAI मॉडेल तैनात करा

1. प्रकल्पात, **Models + endpoints** उघडा.
2. **Deploy model** निवडा.
3. `gpt-4o` सारखे GPT मॉडेल निवडा.
4. मॉडेल तैनात करा.
5. endpoint, deployment name, model name, API key, आणि API version नोंद करा.

!!! note
    Azure OpenAI API आवृत्ती Azure AI Foundry मध्ये दाखवल्या जाणाऱ्या मॉडेल आवृत्तीपासून वेगळी असते. आपल्या डिप्लॉयमेंटसाठी एक समर्थित API आवृत्ती निवडा.

## Azure AI Vision कॉन्फिगर करा

प्रतिमा भाषांतर करण्यासाठी आधी Azure AI Vision द्वारे स्रोत प्रतिमांमधून मजकूर काढला जातो.

आपल्या Azure AI प्रकल्पात, Azure AI Services ची key आणि endpoint शोधा.

![Azure AI सेवा माहिती शोधा](../../assets/find-azure-ai-info.png)

Record:

- Azure AI Service endpoint
- Azure AI Service API key

## Environment Variables

आपली प्रमाणपत्रे आपल्या `.env` फाइलमध्ये किंवा CI secrets मध्ये जोडा.

```bash
# Azure AI Vision, प्रतिमा अनुवादासाठी आवश्यक आहे
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, मजकूर अनुवादासाठी आवश्यक आहे
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator देखील ऐच्छिक fallback credential सेट्सना समर्थन करतो. `_1` किंवा `_2` सारख्या suffix सह पूर्ण प्रदायक सेट डुप्लिकेट करा; fallback सेटमधील सर्व व्हेरिएबल्ससाठी समान suffix असणे आवश्यक आहे.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## पुढील पावले

- [Configuration](configuration.md) वर परत जा आणि स्थानिक किंवा CI environment variables सेट करा.
- भाषांतर आदेशांसाठी [CLI Reference](cli.md) वापरा.
- अनुवाद पुल विनंत्या स्वयंचलित करण्यासाठी [GitHub Actions](github-actions.md) वापरा.