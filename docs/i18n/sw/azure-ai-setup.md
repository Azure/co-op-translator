# Usanidi wa Azure AI

Tumia mwongozo huu unapotaka kusanidi Azure OpenAI kwa tafsiri ya maandishi na Azure AI Vision kwa uchukuaji wa maandishi kutoka kwa picha.

## Mahitaji

- Usajili wa Azure.
- Ruhusa ya kuunda au kutumia rasilimali za Azure AI na uenezaji wa modeli.
- Mradi katika Azure AI Foundry au upatikanaji sawa kwa rasilimali za Azure OpenAI na Azure AI Vision.

## Unda Mradi wa Azure AI

1. Fungua [Azure AI Foundry](https://ai.azure.com).
2. Unda au chagua mradi.
3. Unda au chagua AI hub kwa mradi.
4. Fungua muhtasari wa mradi baada ya kuundwa.

## Weka mfano wa Azure OpenAI

1. Katika mradi, fungua **Models + endpoints**.
2. Select **Deploy model**.
3. Chagua modeli ya GPT kama `gpt-4o`.
4. Deploy the model.
5. Rekodi endpoint, jina la uenezaji, jina la modeli, API key, na toleo la API.

!!! note
    Toleo la API la Azure OpenAI ni tofauti na toleo la modeli linaloonyeshwa katika Azure AI Foundry. Chagua toleo la API linaloungwa mkono kwa uenezaji wako.

## Sanidi Azure AI Vision

Tafsiri ya picha inatumia Azure AI Vision kuchukua maandishi kutoka kwa picha za chanzo kabla ya maandishi kutafsiriwa.

Katika mradi wako wa Azure AI, pata funguo na endpoint ya Azure AI Services.

![Tafuta taarifa za huduma ya Azure AI](../../assets/find-azure-ai-info.png)

Record:

- Azure AI Service endpoint
- Azure AI Service API key

## Vigezo vya Mazingira

Add the credentials to your `.env` file or CI secrets.

```bash
# Azure AI Vision, inahitajika kwa tafsiri ya picha
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, inahitajika kwa tafsiri ya maandishi
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator pia inaunga mkono seti za vitambulisho za mbadala. Nakili seti kamili ya mtoa huduma na viambishi kama `_1` au `_2`; vigezo vyote katika seti ya mbadala lazima viwe na kiambishi kimoja.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Hatua Zifuatazo

- Rudi kwenye [Usanidi](configuration.md) ili kusanidi vigezo vya mazingira vya eneo au vya CI.
- Use [CLI Reference](cli.md) for translation commands.
- Use [GitHub Actions](github-actions.md) to automate translation pull requests.