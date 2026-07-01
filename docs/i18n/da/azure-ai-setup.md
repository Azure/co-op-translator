# Azure AI-opsætning

Brug denne vejledning, når du vil konfigurere Azure OpenAI til tekstoversættelse og Azure AI Vision til ekstraktion af tekst fra billeder.

## Forudsætninger

- Et Azure-abonnement.
- Tilladelse til at oprette eller bruge Azure AI-ressourcer og modelimplementeringer.
- Et projekt i Azure AI Foundry eller tilsvarende adgang til Azure OpenAI og Azure AI Vision-ressourcer.

## Opret et Azure AI-projekt

1. Åbn [Azure AI Foundry](https://ai.azure.com).
2. Opret eller vælg et projekt.
3. Opret eller vælg et AI-hub til projektet.
4. Åbn projektoversigten efter oprettelse.

## Udrul en Azure OpenAI-model

1. I projektet, åbn **Models + endpoints**.
2. Vælg **Deploy model**.
3. Vælg en GPT-model såsom `gpt-4o`.
4. Udrul modellen.
5. Notér endepunkt, udrulningsnavn, modelnavn, API-nøgle og API-version.

!!! note
    Azure OpenAI API-versionen er adskilt fra modelversionen vist i Azure AI Foundry. Vælg en understøttet API-version til din udrulning.

## Konfigurer Azure AI Vision

Billedoversættelse bruger Azure AI Vision til at udtrække tekst fra kildebilleder, før teksten oversættes.

I dit Azure AI-projekt finder du Azure AI Services-nøglen og endepunktet.

![Find oplysninger om Azure AI-tjenesten](../../assets/find-azure-ai-info.png)

Notér:

- Azure AI Service-endepunkt
- Azure AI Service API-nøgle

## Miljøvariabler

Tilføj legitimationsoplysningerne til din `.env`-fil eller CI-sekreter.

```bash
# Azure AI Vision, påkrævet til billedoversættelse
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, påkrævet til tekstoversættelse
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator understøtter også valgfrie fallback-legitimationssæt. Dupliker et komplet udbydersæt med suffikser såsom `_1` eller `_2`; alle variabler i et fallback-sæt skal have samme suffiks.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Næste skridt

- Gå tilbage til [Konfiguration](configuration.md) for at konfigurere lokale eller CI-miljøvariabler.
- Brug [CLI Reference](cli.md) til oversættelseskommandoer.
- Brug [GitHub Actions](github-actions.md) til at automatisere translation pull requests.