<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:29:45+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "hr"
}
-->
# Kreirajte *.env* datoteku u korijenskom direktoriju

U ovom vodiču ćemo vas provesti kroz postavljanje varijabli okoline za Azure usluge koristeći *.env* datoteku. Varijable okoline omogućuju vam sigurno upravljanje osjetljivim podacima, poput API ključeva, bez da ih unosite direktno u vaš kod.

> [!IMPORTANT]
> - Potrebno je konfigurirati samo jednu uslugu jezičnog modela (Azure OpenAI ili OpenAI). Unesite varijable okoline za uslugu koju želite koristiti. Ako su postavljene varijable za više jezičnih modela, prevoditelj će odabrati jedan prema prioritetu.
> - Ako varijable okoline za Computer Vision nisu postavljene, prevoditelj će se automatski prebaciti u [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Ovaj vodič se uglavnom fokusira na Azure usluge, ali možete odabrati bilo koji podržani jezični model s [popisa podržanih modela i usluga](../README.md#-supported-models-and-services).

## Kreirajte *.env* datoteku

U korijenskom direktoriju vašeg projekta, kreirajte datoteku nazvanu *.env*. U njoj ćete pohraniti sve varijable okoline u jednostavnom formatu.

> [!WARNING]
> Nemojte dodavati svoju *.env* datoteku u sustave za kontrolu verzija poput Gita. Dodajte *.env* u svoju .gitignore datoteku kako biste spriječili slučajno dodavanje.

1. Idite u korijenski direktorij vašeg projekta.

1. Kreirajte *.env* datoteku u korijenskom direktoriju vašeg projekta.

1. Otvorite *.env* datoteku i zalijepite sljedeći predložak:

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
> Ako želite pronaći svoje API ključeve i krajnje točke, možete pogledati [set-up-azure-ai.md](../set-up-azure-ai.md).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.