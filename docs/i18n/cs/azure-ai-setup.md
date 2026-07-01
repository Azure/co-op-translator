# Nastavení Azure AI

Použijte tento průvodce, když chcete nakonfigurovat Azure OpenAI pro překlad textu a Azure AI Vision pro extrakci textu z obrázků.

## Požadavky

- Předplatné Azure.
- Oprávnění k vytváření nebo používání Azure AI prostředků a nasazení modelů.
- Projekt v Azure AI Foundry nebo ekvivalentní přístup k prostředkům Azure OpenAI a Azure AI Vision.

## Vytvoření projektu Azure AI

1. Otevřete [Azure AI Foundry](https://ai.azure.com).
2. Vytvořte nebo vyberte projekt.
3. Vytvořte nebo vyberte AI hub pro projekt.
4. Po vytvoření otevřete přehled projektu.

## Nasazení modelu Azure OpenAI

1. V projektu otevřete **Models + endpoints**.
2. Vyberte **Deploy model**.
3. Zvolte GPT model, například `gpt-4o`.
4. Nasaďte model.
5. Zaznamenejte koncový bod, název nasazení, název modelu, API klíč a verzi API.

!!! note
    Verze Azure OpenAI API se liší od verze modelu zobrazené v Azure AI Foundry. Vyberte pro své nasazení podporovanou verzi API.

## Konfigurace Azure AI Vision

Překlad obrázků používá Azure AI Vision k extrakci textu z původních obrázků, než je text přeložen.

Ve svém projektu Azure AI najděte klíč a koncový bod služby Azure AI.

![Najděte informace o službě Azure AI](../../assets/find-azure-ai-info.png)

Zaznamenejte:

- Koncový bod služby Azure AI
- API klíč služby Azure AI

## Proměnné prostředí

Přidejte přihlašovací údaje do souboru `.env` nebo do tajemství CI.

```bash
# Azure AI Vision, vyžadováno pro překlad obrázků
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, vyžadováno pro překlad textu
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator také podporuje volitelné náhradní sady přihlašovacích údajů. Zduplikujte kompletní sadu poskytovatele s příponami jako `_1` nebo `_2`; všechny proměnné v náhradní sadě musí mít stejnou příponu.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Další kroky

- Vraťte se na [Configuration](configuration.md) a nastavte lokální nebo CI proměnné prostředí.
- Použijte [CLI Reference](cli.md) pro příkazy překladu.
- Použijte [GitHub Actions](github-actions.md) k automatizaci pull requestů překladu.