<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:28:37+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "sw"
}
-->
# Unda faili la *.env* katika saraka kuu

Katika mafunzo haya, tutakuongoza jinsi ya kuweka vigezo vya mazingira kwa huduma za Azure kwa kutumia faili la *.env*. Vigezo vya mazingira vinakuwezesha kusimamia kwa usalama nyaraka nyeti, kama vile funguo za API, bila kuziandika moja kwa moja kwenye msimbo wako.

> [!IMPORTANT]
> - Huduma moja tu ya mfano wa lugha (Azure OpenAI au OpenAI) inahitaji kusanidiwa. Jaza vigezo vya mazingira kwa huduma unayopendelea. Ikiwa vigezo vya mazingira kwa mifano mingi ya lugha vimewekwa, mtafsiri wa ushirikiano atachagua moja kulingana na kipaumbele.
> - Ikiwa vigezo vya mazingira vya Computer Vision havijawekwa, mtafsiri atabadilisha moja kwa moja hadi [hali ya Markdown pekee](./markdown-only-mode.md).

> [!NOTE]
> Mwongozo huu unalenga zaidi huduma za Azure, lakini unaweza kuchagua mfano wowote wa lugha unaounga mkono kutoka kwenye [orodha ya mifano na huduma zinazotolewa](../README.md#-supported-models-and-services).

## Unda faili la *.env*

Katika saraka kuu ya mradi wako, unda faili linaloitwa *.env*. Faili hili litatunza vigezo vyote vya mazingira kwa muundo rahisi.

> [!WARNING]
> Usifanye commit faili lako la *.env* kwenye mifumo ya udhibiti wa matoleo kama Git. Ongeza *.env* kwenye faili lako la .gitignore ili kuzuia commits zisizokusudiwa.

1. Nenda kwenye saraka kuu ya mradi wako.

1. Unda faili la *.env* katika saraka kuu ya mradi wako.

1. Fungua faili la *.env* na ubandike kiolezo kifuatacho:

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
> Ikiwa unataka kupata funguo zako za API na endpoints, unaweza kurejelea [set-up-azure-ai.md](../set-up-azure-ai.md).

**Kionyozo**:  
Nyaraka hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Nyaraka ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatubebwi dhamana kwa kutoelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.