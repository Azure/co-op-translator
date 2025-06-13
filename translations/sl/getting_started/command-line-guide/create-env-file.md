<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:29:57+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "sl"
}
-->
# Ustvarite datoteko *.env* v korenski mapi

V tem vodiču vas bomo vodili skozi nastavitev okoljskih spremenljivk za Azure storitve z uporabo datoteke *.env*. Okoljske spremenljivke omogočajo varno upravljanje občutljivih podatkov, kot so API ključi, brez da bi jih vpisovali neposredno v kodo.

> [!IMPORTANT]
> - Konfigurirati je treba le eno storitev jezikovnega modela (Azure OpenAI ali OpenAI). Vnesite okoljske spremenljivke za storitev, ki jo želite uporabljati. Če so nastavljene okoljske spremenljivke za več jezikovnih modelov, bo prevajalec izbral enega glede na prednost.
> - Če okoljske spremenljivke za Computer Vision niso nastavljene, bo prevajalec samodejno preklopil v [Markdown-only način](./markdown-only-mode.md).

> [!NOTE]
> Ta vodič se osredotoča predvsem na Azure storitve, lahko pa izberete kateri koli podprt jezikovni model s [seznama podprtih modelov in storitev](../README.md#-supported-models-and-services).

## Ustvarite datoteko *.env*

V korenski mapi vašega projekta ustvarite datoteko z imenom *.env*. V tej datoteki boste shranjevali vse okoljske spremenljivke v preprosti obliki.

> [!WARNING]
> Datoteke *.env* ne dodajajte v sisteme za nadzor različic, kot je Git. Dodajte *.env* v datoteko .gitignore, da preprečite nenamerne potrditve.

1. Odprite korensko mapo vašega projekta.

1. Ustvarite datoteko *.env* v korenski mapi vašega projekta.

1. Odprite datoteko *.env* in prilepite naslednjo predlogo:

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
> Če želite najti svoje API ključe in končne točke, si lahko pomagate z [set-up-azure-ai.md](../set-up-azure-ai.md).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.