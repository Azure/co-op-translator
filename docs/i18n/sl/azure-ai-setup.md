# Nastavitev Azure AI

Uporabite ta vodnik, ko želite konfigurirati Azure OpenAI za prevajanje besedila in Azure AI Vision za izvleček besedila iz slik.

## Predpogoji

- Naročnina Azure.
- Dovoljenje za ustvarjanje ali uporabo Azure AI virov in nameščanje modelov.
- Projekt v Azure AI Foundry ali enakovreden dostop do virov Azure OpenAI in Azure AI Vision.

## Ustvarite projekt Azure AI

1. Odprite [Azure AI Foundry](https://ai.azure.com).
2. Ustvarite ali izberite projekt.
3. Ustvarite ali izberite AI hub za projekt.
4. Po ustvarjanju odprite pregled projekta.

## Razmestitev modela Azure OpenAI

1. V projektu odprite **Models + endpoints**.
2. Izberite **Deploy model**.
3. Izberite GPT model, na primer `gpt-4o`.
4. Razmestite model.
5. Zabeležite končno točko, ime razmestitve, ime modela, API ključ in različico API-ja.

!!! note
    Različica Azure OpenAI API-ja je ločena od različice modela, prikazane v Azure AI Foundry. Za svojo razmestitev izberite podprto različico API-ja.

## Konfigurirajte Azure AI Vision

Prevajanje slik uporablja Azure AI Vision za izvleček besedila iz izvornih slik, preden se besedilo prevede.

V svojem projektu Azure AI poiščite ključ in končno točko storitve Azure AI.

![Poiščite informacije o storitvi Azure AI](../../assets/find-azure-ai-info.png)

Zabeležite:

- Končna točka storitve Azure AI
- API ključ storitve Azure AI

## Spremenljivke okolja

Dodajte poverilnice v datoteko `.env` ali v skrivnosti CI.

```bash
# Azure AI Vision, potreben za prevajanje slik
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, potreben za prevajanje besedil
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator podpira tudi izbirne nadomestne nize poverilnic. Podvojite celoten nabor ponudnika s priponami, kot so `_1` ali `_2`; vse spremenljivke v nadomestnem nizu morajo imeti enako pripono.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Naslednji koraki

- Vrnite se na [Konfiguracija](configuration.md) za nastavitev lokalnih ali CI spremenljivk okolja.
- Uporabite [Referenca CLI](cli.md) za ukaze za prevajanje.
- Uporabite [GitHub Actions](github-actions.md) za avtomatizacijo pull requestov za prevajanje.