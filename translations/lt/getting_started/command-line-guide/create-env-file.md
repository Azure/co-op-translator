<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-10-15T04:59:22+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "lt"
}
-->
# Sukurkite *.env* failą pagrindiniame kataloge

Šioje instrukcijoje parodysime, kaip nustatyti aplinkos kintamuosius Azure paslaugoms naudojant *.env* failą. Aplinkos kintamieji leidžia saugiai tvarkyti jautrius duomenis, tokius kaip API raktai, jų nekoduojant tiesiogiai programos kode.

> [!IMPORTANT]
> - Konfigūruoti reikia tik vieną kalbos modelio paslaugą (Azure OpenAI arba OpenAI). Užpildykite aplinkos kintamuosius pasirinktam paslaugų tiekėjui. Jei bus nustatyti kelių kalbos modelių kintamieji, kooperacinis vertėjas pasirinks vieną pagal prioritetą.
> - Jei nebus nustatyti Computer Vision aplinkos kintamieji, vertėjas automatiškai persijungs į [tik Markdown režimą](./markdown-only-mode.md).

> [!NOTE]
> Ši instrukcija daugiausia skirta Azure paslaugoms, tačiau galite pasirinkti bet kurį palaikomą kalbos modelį iš [palaikomų modelių ir paslaugų sąrašo](../README.md#-supported-models-and-services).

## Sukurkite *.env* failą

Pagrindiniame projekto kataloge sukurkite failą pavadinimu *.env*. Šiame faile bus saugomi visi jūsų aplinkos kintamieji paprastu formatu.

> [!WARNING]
> Neįtraukite savo *.env* failo į versijų kontrolės sistemas, tokias kaip Git. Įtraukite *.env* į .gitignore failą, kad išvengtumėte netyčinio įkėlimo.

1. Eikite į pagrindinį projekto katalogą.

1. Sukurkite *.env* failą pagrindiniame projekto kataloge.

1. Atidarykite *.env* failą ir įklijuokite šį šabloną:

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
> Jei norite rasti savo API raktus ir galinius taškus, galite pasižiūrėti [set-up-azure-ai.md](../set-up-azure-ai.md).

---

**Atsakomybės atsisakymas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.