<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:29:08+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "sk"
}
-->
# Vytvorte súbor *.env* v koreňovom adresári

V tomto návode vás prevedieme nastavením environmentálnych premenných pre služby Azure pomocou súboru *.env*. Environmentálne premenné vám umožňujú bezpečne spravovať citlivé údaje, ako sú API kľúče, bez toho, aby ste ich priamo vkladali do vášho kódu.

> [!IMPORTANT]
> - Stačí nakonfigurovať len jednu službu jazykového modelu (Azure OpenAI alebo OpenAI). Vyplňte environmentálne premenné pre preferovanú službu. Ak sú nastavené premenné pre viaceré jazykové modely, prekladateľ vyberie jednu na základe priority.
> - Ak nie sú nastavené environmentálne premenné pre Computer Vision, prekladateľ automaticky prejde do [režimu iba pre Markdown](./markdown-only-mode.md).

> [!NOTE]
> Tento návod je zameraný predovšetkým na služby Azure, ale môžete si vybrať akýkoľvek podporovaný jazykový model zo [zoznamu podporovaných modelov a služieb](../README.md#-supported-models-and-services).

## Vytvorte súbor *.env*

V koreňovom adresári vášho projektu vytvorte súbor s názvom *.env*. Tento súbor bude obsahovať všetky vaše environmentálne premenné v jednoduchom formáte.

> [!WARNING]
> Nesťahujte súbor *.env* do verziovacieho systému ako Git. Pridajte *.env* do súboru .gitignore, aby ste predišli náhodnému commitnutiu.

1. Prejdite do koreňového adresára vášho projektu.

1. Vytvorte súbor *.env* v koreňovom adresári vášho projektu.

1. Otvorte súbor *.env* a vložte nasledujúcu šablónu:

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
> Ak chcete nájsť svoje API kľúče a endpointy, môžete sa pozrieť na [set-up-azure-ai.md](../set-up-azure-ai.md).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.