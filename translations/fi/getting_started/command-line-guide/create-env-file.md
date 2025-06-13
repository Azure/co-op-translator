<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:27:37+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "fi"
}
-->
# Luo *.env* -tiedosto juurikansioon

Tässä ohjeessa opastamme sinua ympäristömuuttujien määrittämisessä Azure-palveluille käyttämällä *.env* -tiedostoa. Ympäristömuuttujat mahdollistavat arkaluontoisten tunnistetietojen, kuten API-avaimien, turvallisen hallinnan ilman, että niitä tarvitsee kovakoodata koodipohjaasi.

> [!IMPORTANT]
> - Vain yksi kielimallipalvelu (Azure OpenAI tai OpenAI) tarvitsee olla konfiguroitu. Täytä ympäristömuuttujat haluamallesi palvelulle. Jos useamman kielimallin ympäristömuuttujat on asetettu, yhteistyökääntäjä valitsee niistä yhden prioriteetin perusteella.
> - Jos Computer Visionin ympäristömuuttujia ei ole asetettu, kääntäjä vaihtaa automaattisesti [vain Markdown -tilaan](./markdown-only-mode.md).

> [!NOTE]
> Tämä ohje keskittyy pääasiassa Azure-palveluihin, mutta voit valita minkä tahansa tuetun kielimallin [tuettujen mallien ja palveluiden listalta](../README.md#-supported-models-and-services).

## Luo *.env* -tiedosto

Projektisi juurikansiossa luo tiedosto nimeltä *.env*. Tämä tiedosto tallentaa kaikki ympäristömuuttujasi yksinkertaisessa muodossa.

> [!WARNING]
> Älä tallenna *.env* -tiedostoa versionhallintajärjestelmiin, kuten Gitiin. Lisää *.env* .gitignore-tiedostoon välttääksesi vahingossa tapahtuvat commitit.

1. Siirry projektisi juurikansioon.

1. Luo *.env* -tiedosto projektisi juurikansioon.

1. Avaa *.env* -tiedosto ja liitä seuraava pohja:

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
> Jos haluat löytää API-avaimesi ja päätepisteesi, voit katsoa ohjeen [set-up-azure-ai.md](../set-up-azure-ai.md).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja omalla kielellään on virallinen lähde. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.