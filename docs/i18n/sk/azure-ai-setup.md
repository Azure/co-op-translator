# Nastavenie Azure AI

Použite tento návod, keď chcete nakonfigurovať Azure OpenAI na preklad textu a Azure AI Vision na extrakciu textu z obrázkov.

## Požiadavky

- Predplatné Azure.
- Oprávnenie na vytváranie alebo používanie zdrojov Azure AI a nasadení modelov.
- Projekt v Azure AI Foundry alebo ekvivalentný prístup k zdrojom Azure OpenAI a Azure AI Vision.

## Vytvorenie projektu Azure AI

1. Otvorte [Azure AI Foundry](https://ai.azure.com).
2. Vytvorte alebo vyberte projekt.
3. Vytvorte alebo vyberte AI hub pre projekt.
4. Po vytvorení otvorte prehľad projektu.

## Nasadenie modelu Azure OpenAI

1. V projekte otvorte **Models + endpoints**.
2. Vyberte **Deploy model**.
3. Vyberte model GPT, napríklad `gpt-4o`.
4. Nasadiť model.
5. Zaznamenajte koncový bod, názov nasadenia, názov modelu, API kľúč a verziu API.

!!! note
    Verzia Azure OpenAI API je oddelená od verzie modelu zobrazeného v Azure AI Foundry. Vyberte podporovanú verziu API pre vaše nasadenie.

## Konfigurácia Azure AI Vision

Preklad obrázkov používa Azure AI Vision na extrahovanie textu zo zdrojových obrázkov pred samotným prekladom.

Vo svojom projekte Azure AI nájdite kľúč a koncový bod služby Azure AI.

![Nájdite informácie o službe Azure AI](../../assets/find-azure-ai-info.png)

Zaznamenajte:

- Koncový bod služby Azure AI
- API kľúč služby Azure AI

## Premenné prostredia

Pridajte poverenia do svojho súboru `.env` alebo do tajomstiev CI.

```bash
# Azure AI Vision, potrebné na preklad obrázkov
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, potrebné na preklad textu
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator tiež podporuje voliteľné záložné sady poverení. Duplikujte kompletnú sadu poskytovateľa s príponami, ako sú `_1` alebo `_2`; všetky premenné v záložnej sade musia mať rovnakú príponu.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Ďalšie kroky

- Vráťte sa na [Konfigurácia](configuration.md) a nastavte lokálne alebo CI premenné prostredia.
- Použite [Referencia CLI](cli.md) pre príkazy na preklad.
- Použite [GitHub Actions](github-actions.md) na automatizáciu pull requestov s prekladmi.