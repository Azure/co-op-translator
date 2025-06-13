<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:28:58+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "cs"
}
-->
# Vytvoření souboru *.env* v kořenovém adresáři

V tomto návodu vás provedeme nastavením proměnných prostředí pro služby Azure pomocí souboru *.env*. Proměnné prostředí vám umožňují bezpečně spravovat citlivé údaje, jako jsou API klíče, aniž byste je museli přímo zapisovat do kódu.

> [!IMPORTANT]
> - Je potřeba nakonfigurovat pouze jednu službu jazykového modelu (Azure OpenAI nebo OpenAI). Vyplňte proměnné prostředí pro preferovanou službu. Pokud jsou nastaveny proměnné prostředí pro více jazykových modelů, překladatel zvolí jednu podle priority.
> - Pokud nejsou nastaveny proměnné prostředí pro Computer Vision, překladatel se automaticky přepne do [režimu pouze Markdown](./markdown-only-mode.md).

> [!NOTE]
> Tento průvodce se zaměřuje především na služby Azure, ale můžete si vybrat jakýkoli podporovaný jazykový model ze [seznamu podporovaných modelů a služeb](../README.md#-supported-models-and-services).

## Vytvoření souboru *.env*

V kořenovém adresáři vašeho projektu vytvořte soubor s názvem *.env*. Tento soubor bude uchovávat všechny vaše proměnné prostředí v jednoduchém formátu.

> [!WARNING]
> Soubor *.env* neukládejte do verzovacích systémů jako Git. Přidejte *.env* do souboru .gitignore, abyste zabránili nechtěnému commitování.

1. Přejděte do kořenového adresáře vašeho projektu.

1. V kořenovém adresáři projektu vytvořte soubor *.env*.

1. Otevřete soubor *.env* a vložte následující šablonu:

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
> Pokud chcete najít své API klíče a koncové body, můžete se podívat do [set-up-azure-ai.md](../set-up-azure-ai.md).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.