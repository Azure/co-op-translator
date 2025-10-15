<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-10-15T04:59:38+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "et"
}
-->
# Loo *.env* fail juurkataloogi

Selles juhendis näitame, kuidas seadistada oma keskkonnamuutujad Azure teenuste jaoks kasutades *.env* faili. Keskkonnamuutujad võimaldavad sul turvaliselt hallata tundlikke andmeid, nagu API võtmed, ilma et peaksid neid otse koodi sisse kirjutama.

> [!IMPORTANT]
> - Vaja on seadistada ainult üks keelemudeli teenus (Azure OpenAI või OpenAI). Täida keskkonnamuutujad oma eelistatud teenuse jaoks. Kui mitme keelemudeli keskkonnamuutujad on määratud, valib co-op tõlkija ühe vastavalt prioriteedile.
> - Kui Computer Visioni keskkonnamuutujad pole määratud, lülitub tõlkija automaatselt [ainult Markdown režiimi](./markdown-only-mode.md).

> [!NOTE]
> See juhend keskendub peamiselt Azure teenustele, kuid võid valida ükskõik millise toetatud keelemudeli [toetatud mudelite ja teenuste nimekirjast](../README.md#-supported-models-and-services).

## Loo *.env* fail

Loo oma projekti juurkataloogi fail nimega *.env*. Selles failis hoitakse kõiki sinu keskkonnamuutujaid lihtsas vormingus.

> [!WARNING]
> Ära lisa oma *.env* faili versioonihaldussüsteemi nagu Git. Lisa *.env* oma .gitignore faili, et vältida kogemata üleslaadimist.

1. Liigu oma projekti juurkataloogi.

1. Loo *.env* fail oma projekti juurkataloogi.

1. Ava *.env* fail ja kleebi sinna järgmine mall:

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
> Kui soovid leida oma API võtmeid ja lõpp-punkte, vaata [set-up-azure-ai.md](../set-up-azure-ai.md).

---

**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokumenti selle algses keeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgendamise eest.