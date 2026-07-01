# Fejlfinding

Brug denne side, når en oversættelseskørsel lykkes uventet, fejler under konfiguration, eller producerer output, der har brug for gennemgang.

## Kom i gang

1. Kør først en fokuseret kommando, for eksempel `translate -l "ko" -md`.
2. Tilføj `-d` for konsolens debuglogfiler.
3. Tilføj `-s` for at gemme debuglogs under `<root-dir>/logs/`.
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

- Konfigurer Azure OpenAI eller OpenAI.
- Bekræft, at variablerne er i det miljø, hvor kommandoen kører.
- For lokal brug, placér dem i `.env` i projektets rodmappe.

Se [Konfiguration](configuration.md).

### Billedoversættelse uden Azure AI Vision

Fejl:

```text
Image translation requested but Azure AI Service is not configured.
```

Løsning:

- Tilføj `AZURE_AI_SERVICE_API_KEY`.
- Tilføj `AZURE_AI_SERVICE_ENDPOINT`.
- Eller kør en tekstbaseret kommando såsom `translate -l "ko" -md`.

### Ugyldig nøgle eller endpoint

Symptomer kan omfatte `401`, maskerede tilladelsesfejl eller adgangsfejl til endpoint.

Løsning:

- Bekræft, at nøglen hører til den samme Azure-ressource som endpoint.
- Bekræft, at ressourcen understøtter Vision ved brug af `-img`.
- Bekræft, at Azure OpenAI udrulningsnavn og API-version matcher din udrulning.
- Kør med debuglogs: `translate -l "ko" -md -d -s`.

## Ingen filer blev oversat

Almindelige årsager:

- De valgte flags matcher ikke dine filer.
- Oversatte filer eksisterer allerede.
- Kildefiler ligger i udelukkede mapper.
- Kommandoen køres fra det forkerte projektrod.

Kontroller:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Brug `--root-dir`, når kommandoen køres uden for projektets rodmappe.

## Uventet linkadfærd

Omskrivning af links afhænger af valgte indholdstyper:

- `-nb` inkluderet: notebook-links kan pege på oversatte notebooks.
- `-nb` ekskluderet: notebook-links kan forblive pegende på kilde-notebooks.
- `-img` inkluderet: billedlinks kan pege på oversatte billeder.
- `-img` ekskluderet: billedlinks kan forblive pegende på kilde-billeder.

Kør en fuld indholdsoversættelse, når alle interne links bør foretrække oversatte output:

```bash
translate -l "ko" -md -nb -img
```

Kør linkgennemgang efter oversættelsen:

```bash
co-op-review -l "ko"
```

## Problemer med Markdown-rendering

Hvis oversat Markdown gengives forkert:

- Kontroller, at frontmatter starter og slutter med `---`.
- Kontroller, at antal code fences matcher mellem kilde- og oversatte filer.
- Kør `co-op-review` for at fange almindelige strukturproblemer.
- Oversæt den specifikke fil igen, hvis outputtet blev beskadiget.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action kørte, men ingen pull request blev oprettet

Hvis `peter-evans/create-pull-request` rapporterer, at branchen ikke ligger foran base, fandt workflowet ingen filer at committe.

Sandsynlige årsager:

- Oversættelseskørslen producerede ingen ændringer.
- `.gitignore` udelukker `translations/`, `translated_images/` eller oversatte notebooks.
- `add-paths` matcher ikke de genererede outputmapper.
- Oversættelsestrinnet afsluttede tidligt.

Løsninger:

1. Bekræft, at genererede filer findes i `translations/` eller `translated_images/`.
2. Bekræft, at `.gitignore` ikke ignorerer genererede outputs.
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

Maskinoversættelser kan kræve menneskelig gennemgang. Brug `evaluate` kun, når du ønsker eksperimentel kvalitetsvurdering og lavtillids-reparationsarbejdsgange.

!!! warning "Eksperimentel"
    `evaluate` kan bruge regelbaserede og LLM-baserede kontroller, og dets scoringsmodel og metadataadfærd kan ændre sig. Hold det ude af krævede CI-gates, medmindre din workflow er forberedt på ændringer.

For deterministiske CI-kontroller, brug `co-op-review` i stedet.