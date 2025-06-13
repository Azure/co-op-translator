<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:28:28+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "tl"
}
-->
# Gumawa ng *.env* na file sa root directory

Sa tutorial na ito, gagabayan ka namin sa pag-setup ng iyong environment variables para sa mga Azure services gamit ang isang *.env* na file. Pinapayagan ka ng environment variables na ligtas na pamahalaan ang mga sensitibong kredensyal, tulad ng API keys, nang hindi kinakailangang i-hard-code ang mga ito sa iyong codebase.

> [!IMPORTANT]
> - Isa lamang sa mga language model service (Azure OpenAI o OpenAI) ang kailangang i-configure. Punan ang environment variables para sa serbisyong gusto mo. Kung may environment variables na naka-set para sa maraming language models, pipiliin ng co-op translator ang isa base sa prayoridad.
> - Kung hindi naka-set ang Computer Vision environment variables, awtomatikong lilipat ang translator sa [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Pangunahing nakatuon ang gabay na ito sa Azure services, pero maaari kang pumili ng anumang suportadong language model mula sa [listahan ng mga suportadong modelo at serbisyo](../README.md#-supported-models-and-services).

## Gumawa ng *.env* na file

Sa root directory ng iyong proyekto, gumawa ng isang file na pinangalanang *.env*. Sa file na ito ilalagay ang lahat ng iyong environment variables sa isang simpleng format.

> [!WARNING]
> Huwag i-commit ang iyong *.env* na file sa version control systems tulad ng Git. Idagdag ang *.env* sa iyong .gitignore file upang maiwasan ang hindi sinasadyang pag-commit.

1. Pumunta sa root directory ng iyong proyekto.

1. Gumawa ng isang *.env* na file sa root directory ng iyong proyekto.

1. Buksan ang *.env* na file at i-paste ang sumusunod na template:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> Kung nais mong hanapin ang iyong mga API keys at endpoints, maaari mong tingnan ang [set-up-azure-ai.md](../set-up-azure-ai.md).

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami na maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-katiyakan. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.