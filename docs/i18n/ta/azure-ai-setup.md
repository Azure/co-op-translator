# Azure AI அமைப்பு

Use this guide when you want to configure Azure OpenAI for text translation and Azure AI Vision for image text extraction.

## முன் நிபந்தனைகள்

- ஒரு Azure சந்தா.
- Azure AI வளங்கள் மற்றும் மாடல் நிலைப்படுத்தல்களை உருவாக்க அல்லது பயன்படுத்த அனுமதி.
- Azure AI Foundry-இல் ஒரு திட்டம் அல்லது Azure OpenAI மற்றும் Azure AI Vision வளங்களுக்கு சமமான அணுகல்.

## Azure AI திட்டம் உருவாக்குங்கள்

1. Open [Azure AI Foundry](https://ai.azure.com).
2. ஒரு திட்டத்தை உருவாக்கவும் அல்லது தேர்ந்தெடுக்கவும்.
3. திட்டத்திற்காக ஒரு AI ஹப் உருவாக்கவும் அல்லது தேர்ந்தெடுக்கவும்.
4. உருவாக்கத்தின் பின்னர் திட்டத்தின் மேலோட்டத்தை திறக்கவும்.

## Azure OpenAI மாடலை நிலைப்படுத்தவும்

1. திட்டத்தில் **Models + endpoints** ஐத் திறக்கவும்.
2. **Deploy model** ஐத் தேர்வுசெய்க.
3. `gpt-4o` போன்ற ஒரு GPT மாடலைத் தேர்வு செய்யவும்.
4. மாடலினை நிலைப்படுத்தவும்.
5. endpoint, deployment name, model name, API key, மற்றும் API version-ஐ பதிவுசெய்க.

!!! note
    Azure OpenAI API பதிப்பு Azure AI Foundry-இல் காட்சி அளிக்கப்படும் மாடல் பதிப்பிலிருந்து தனித்துவமாக இருக்கிறது. உங்கள் நிலைப்படுத்தலுக்குப் பொருத்தமான ஆதரிக்கப்பட்ட API பதிப்பை தேர்வு செய்யவும்.

## Azure AI Vision அமைக்க

பட மொழிபெயர்ப்பிற்கு முன் மூல படங்களில் இருந்து உரையை எடுவதற்கு Azure AI Vision பயன்படுத்தப்படுகிறது.

உங்கள் Azure AI திட்டத்தில், Azure AI Services சாவி மற்றும் endpoint-ஐ கண்டறியவும்.

![Find Azure AI service information](../../assets/find-azure-ai-info.png)

பதிவுசெய்க:

- Azure AI Service endpoint
- Azure AI Service API key

## சூழல் மாறிகள்

Add the credentials to your `.env` file or CI secrets.

```bash
# பட மொழிபெயர்ப்பிற்கு Azure AI Vision தேவையானது
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# உரை மொழிபெயர்ப்பிற்கு Azure OpenAI தேவையானது
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

## அடுத்த நடவடிக்கைகள்

- உள்ளூரு அல்லது CI சூழல் மாறிகளை அமைக்க [Configuration](configuration.md) இற்கு திரும்பிச் செல்லவும்.
- மொழிபெயர்ப்பு கட்டளைகளுக்காக [CLI Reference](cli.md) ஐ பயன்படுத்தவும்.
- மொழிபெயர்ப்பு pull requests-ஐ தானாகச் செய்ய [GitHub Actions](github-actions.md) ஐப் பயன்படுத்தவும்.