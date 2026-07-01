# Azure AI-oppsett

Bruk denne veiledningen når du vil konfigurere Azure OpenAI for tekstoversettelse og Azure AI Vision for å hente tekst fra bilder.

## Forutsetninger

- Et Azure-abonnement.
- Tillatelse til å opprette eller bruke Azure AI-ressurser og modelldistribusjoner.
- Et prosjekt i Azure AI Foundry eller tilsvarende tilgang til Azure OpenAI og Azure AI Vision-ressurser.

## Opprett et Azure AI-prosjekt

1. Åpne [Azure AI Foundry](https://ai.azure.com).
2. Opprett eller velg et prosjekt.
3. Opprett eller velg et AI-hub for prosjektet.
4. Åpne prosjektoversikten etter opprettelse.

## Distribuer en Azure OpenAI-modell

1. I prosjektet, åpne **Models + endpoints**.
2. Velg **Deploy model**.
3. Velg en GPT-modell som for eksempel `gpt-4o`.
4. Distribuer modellen.
5. Noter endepunktet, distribusjonsnavnet, modellnavnet, API-nøkkelen og API-versjonen.

!!! note
    Azure OpenAI API-versjonen er separat fra modellversjonen som vises i Azure AI Foundry. Velg en støttet API-versjon for distribusjonen din.

## Konfigurer Azure AI Vision

Bildeoversettelse bruker Azure AI Vision for å trekke ut tekst fra kildebilder før teksten oversettes.

I Azure AI-prosjektet ditt, finn Azure AI Services-nøkkelen og endepunktet.

![Finn informasjon om Azure AI-tjenesten](../../assets/find-azure-ai-info.png)

Noter:

- Azure AI Service-endepunkt
- Azure AI Service API-nøkkel

## Miljøvariabler

Legg legitimasjonen til i `.env`-filen eller i CI-hemmelighetene.

```bash
# Azure AI Vision, kreves for bildeoversettelse
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, kreves for tekstoversettelse
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator støtter også valgfrie fallback-legitimasjonssett. Dupliser et komplett leverandørsett med suffikser som `_1` eller `_2`; alle variablene i et fallback-sett må ha samme suffiks.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Neste trinn

- Gå tilbake til [Konfigurasjon](configuration.md) for å sette opp lokale eller CI-miljøvariabler.
- Bruk [CLI-referanse](cli.md) for oversettelseskommandoer.
- Bruk [GitHub Actions](github-actions.md) for å automatisere oversettelses pull-forespørsler.