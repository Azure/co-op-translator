<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:29:16+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "ro"
}
-->
# Creează fișierul *.env* în directorul rădăcină

În acest tutorial, te vom ghida cum să configurezi variabilele de mediu pentru serviciile Azure folosind un fișier *.env*. Variabilele de mediu îți permit să gestionezi în siguranță credențialele sensibile, cum ar fi cheile API, fără a le introduce direct în codul sursă.

> [!IMPORTANT]
> - Este necesar să configurezi doar un singur serviciu de model de limbaj (Azure OpenAI sau OpenAI). Completează variabilele de mediu pentru serviciul pe care îl preferi. Dacă sunt setate variabile de mediu pentru mai multe modele de limbaj, translatorul colaborativ va alege unul în funcție de prioritate.
> - Dacă variabilele de mediu pentru Computer Vision nu sunt setate, translatorul va trece automat în [modul doar Markdown](./markdown-only-mode.md).

> [!NOTE]
> Acest ghid se concentrează în principal pe serviciile Azure, însă poți alege orice model de limbaj suportat din [lista modelelor și serviciilor suportate](../README.md#-supported-models-and-services).

## Creează fișierul *.env*

În directorul rădăcină al proiectului tău, creează un fișier numit *.env*. Acest fișier va stoca toate variabilele de mediu într-un format simplu.

> [!WARNING]
> Nu face commit fișierului *.env* în sistemele de control al versiunilor precum Git. Adaugă *.env* în fișierul tău .gitignore pentru a preveni commit-uri accidentale.

1. Navighează în directorul rădăcină al proiectului tău.

1. Creează un fișier *.env* în directorul rădăcină al proiectului.

1. Deschide fișierul *.env* și lipește următorul șablon:

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
> Dacă vrei să găsești cheile API și endpoint-urile, poți consulta [set-up-azure-ai.md](../set-up-azure-ai.md).

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.