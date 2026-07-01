# Azure AI Postavljanje

Use this guide when you want to configure Azure OpenAI for text translation and Azure AI Vision for image text extraction.

## Preduvjeti

- Pretplata na Azure.
- Dozvola za stvaranje ili korištenje Azure AI resursa i implementacija modela.
- Projekt u Azure AI Foundry ili ekvivalentan pristup resursima Azure OpenAI i Azure AI Vision.

## Stvorite Azure AI projekt

1. Otvorite [Azure AI Foundry](https://ai.azure.com).
2. Stvorite ili odaberite projekt.
3. Stvorite ili odaberite AI hub za projekt.
4. Otvorite pregled projekta nakon stvaranja.

## Rasporedite Azure OpenAI model

1. U projektu otvorite **Modeli + krajnje točke**.
2. Odaberite **Rasporedi model**.
3. Odaberite GPT model poput `gpt-4o`.
4. Rasporedite model.
5. Zabilježite krajnju točku, naziv rasporeda, naziv modela, API ključ i verziju API-ja.

!!! note
    Verzija Azure OpenAI API-ja je odvojena od verzije modela prikazane u Azure AI Foundry. Odaberite podržanu verziju API-ja za svoje raspoređivanje.

## Konfigurirajte Azure AI Vision

Prevođenje slika koristi Azure AI Vision za izdvajanje teksta iz izvornih slika prije nego što se tekst prevede.

U svom Azure AI projektu pronađite ključ i krajnju točku Azure AI Services.

![Pronađite informacije o Azure AI usluzi](../../assets/find-azure-ai-info.png)

Zabilježite:

- Azure AI Service krajnja točka
- Azure AI Service API ključ

## Varijable okruženja

Dodajte vjerodajnice u svoju `.env` datoteku ili CI tajne.

```bash
# Azure AI Vision, potreban za prevođenje slika
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, potreban za prevođenje teksta
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator također podržava opcionalne rezervne skupove vjerodajnica. Duplikajte kompletan skup pružatelja s nastavcima poput `_1` ili `_2`; sve varijable u rezervnom skupu moraju imati isti nastavak.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Sljedeći koraci

- Vratite se na [Konfiguracija](configuration.md) kako biste postavili lokalne ili CI varijable okruženja.
- Upotrijebite [Referenca CLI](cli.md) za naredbe prevođenja.
- Koristite [GitHub Actions](github-actions.md) za automatizaciju zahtjeva za povlačenje prijevoda.