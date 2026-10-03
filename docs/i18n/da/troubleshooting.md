# Fejlfinding

Brug denne side, når en oversættelseskørsel lykkes uventet, fejler under konfigurationen eller genererer output, der skal gennemgås.

## Start her

1. Kør først en fokuseret kommando, f.eks. `translate -l "ko" -md`.
2. Tilføj `-d` for konsolens fejlsøgningslogs.
3. Tilføj `-s` for at gemme fejlsøgningslogs under `<root-dir>/logs/`.
4. Kør `co-op-review` efter oversættelsen for at tjekke aktualitet, struktur og lokale links.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfigurationsfejl

### Ingen sprogmodeludbyder

Fejl:

```text
No language model configuration found.
```

Løsning:

- Konfigurer Azure OpenAI, OpenAI eller Anthropic.
- Bekræft, at variablerne er i det miljø, hvor kommandoen kører.
- Til lokal brug skal du lægge dem i `.env` i projektets rodmappe.

Se [Konfiguration](configuration.md).

### Billedoversættelse uden Azure AI Vision

Fejl:

```text
Image translation requested but Azure AI Service is not configured.
```

Løsning:

- Tilføj `AZURE_AI_SERVICE_API_KEY`.
- Tilføj `AZURE_AI_SERVICE_ENDPOINT`.
- Eller kør en tekstbaseret kommando, f.eks. `translate -l "ko" -md`.

### Ugyldig nøgle eller endpoint

Symptomer kan inkludere `401`, tilladelsesfejl med skjulte oplysninger eller fejl ved adgang til endpointet.

Løsning:

- Bekræft, at nøglen tilhører den samme Azure-ressource som endpointet.
- Bekræft, at ressourcen understøtter Vision, når du bruger `-img`.
- Bekræft, at Azure OpenAI-deploymentnavnet og API-versionen matcher din deployment.
- Kør med fejlsøgningslogs: `translate -l "ko" -md -d -s`.

## Ingen filer blev oversat

Almindelige årsager:

- De valgte flag stemmer ikke overens med dine filer.
- Oversatte filer findes allerede.
- Kildefiler ligger i ekskluderede mapper.
- Kommandoen køres fra det forkerte projektrod.

Kontroller:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Brug `--root-dir`, når kommandoen køres uden for projektroden.

## Uventet linkadfærd

Omskrivning af links afhænger af de valgte indholdstyper:

- `-nb` inkluderet: notebook-links kan pege på oversatte notebooks.
- `-nb` ekskluderet: notebook-links kan forblive peget på kilde-notebooks.
- `-img` inkluderet: billedlinks kan pege på oversatte billeder.
- `-img` ekskluderet: billedlinks kan forblive peget på kildebilleder.

Kør en fuld indholdsoversættelse, når alle interne links skal foretrække oversatte output:

```bash
translate -l "ko" -md -nb -img
```

Kør linkgennemgang efter oversættelsen:

```bash
co-op-review -l "ko"
```

## Problemer med Markdown-rendering

Hvis oversat Markdown gengives forkert:

- Tjek, at frontmatter starter og slutter med `---`.
- Tjek, at antallet af kodehegn matcher mellem kilde- og oversatte filer.
- Kør `co-op-review` for at opdage almindelige strukturproblemer.
- Oversæt den specifikke fil igen, hvis outputtet blev korrupt.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action kørte, men der blev ikke oprettet en pull request

Hvis `peter-evans/create-pull-request` rapporterer, at branchen ikke ligger foran base, fandt workflowet ingen filer at commite.

Sandsynlige årsager:

- Oversættelseskørslen medførte ingen ændringer.
- `.gitignore` ekskluderer `translations/`, `translated_images/` eller oversatte notebooks.
- `add-paths` matcher ikke de genererede outputmapper.
- Oversættelsestrinet afsluttede tidligt.

Løsninger:

1. Bekræft, at genererede filer findes i `translations/` eller `translated_images/`.
2. Bekræft, at `.gitignore` ikke ignorerer de genererede outputs.
3. Brug matchende `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Tilføj midlertidigt debug-flags til translate-kommandoen:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Bekræft, at workflow-tilladelser inkluderer:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Oversættelseskvalitet

Maskinoversættelser kan kræve menneskelig gennemgang. Brug `evaluate` kun, når du ønsker eksperimentel kvalitetsvurdering og workflows til reparation ved lav tillid.

!!! warning "Eksperimentel"
    `evaluate` kan bruge regelbaserede og LLM-baserede kontroller, og dens scoremodel og metadataadfærd kan ændre sig. Hold den ude af påkrævede CI-gates, medmindre dit workflow er forberedt på ændringer.

Til deterministiske CI-kontroller skal du i stedet bruge `co-op-review`.