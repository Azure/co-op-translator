<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:28:47+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "hu"
}
-->
# Hozd létre a *.env* fájlt a gyökérkönyvtárban

Ebben a bemutatóban végigvezetünk az Azure szolgáltatásokhoz szükséges környezeti változók beállításán egy *.env* fájl segítségével. A környezeti változók lehetővé teszik, hogy biztonságosan kezeld az érzékeny hitelesítő adatokat, például az API kulcsokat, anélkül, hogy azokat közvetlenül a kódbázisba írnád.

> [!IMPORTANT]
> - Csak egy nyelvi modell szolgáltatást (Azure OpenAI vagy OpenAI) kell konfigurálni. Töltsd ki a környezeti változókat a preferált szolgáltatásodhoz. Ha több nyelvi modell környezeti változói is be vannak állítva, a kooperatív fordító prioritás alapján választ egyet.
> - Ha a Computer Vision környezeti változók nincsenek beállítva, a fordító automatikusan [Markdown-only módra](./markdown-only-mode.md) vált.

> [!NOTE]
> Ez az útmutató elsősorban az Azure szolgáltatásokra fókuszál, de bármely támogatott nyelvi modellt választhatod a [támogatott modellek és szolgáltatások listájából](../README.md#-supported-models-and-services).

## Hozd létre a *.env* fájlt

A projekted gyökérkönyvtárában hozz létre egy *.env* nevű fájlt. Ebben a fájlban egyszerű formátumban tárolhatod az összes környezeti változót.

> [!WARNING]
> Ne add hozzá a *.env* fájlt verziókezelő rendszerekhez, például Githez. Tedd fel a *.env* fájlt a .gitignore listádra, hogy elkerüld a véletlen feltöltést.

1. Navigálj a projekted gyökérkönyvtárába.

1. Hozz létre egy *.env* fájlt a projekt gyökérkönyvtárában.

1. Nyisd meg a *.env* fájlt, és illeszd be a következő sablont:

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
> Ha meg szeretnéd találni az API kulcsaidat és végpontjaidat, nézd meg a [set-up-azure-ai.md](../set-up-azure-ai.md) útmutatót.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.