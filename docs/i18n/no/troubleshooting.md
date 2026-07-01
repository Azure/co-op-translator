# Feilsøking

Bruk denne siden når en oversettelseskjøring lykkes uventet, mislykkes under konfigurasjon, eller produserer utdata som trenger gjennomgang.

## Start her

1. Run a focused command first, such as `translate -l "ko" -md`.
2. Add `-d` for console debug logs.
3. Add `-s` to save debug logs under `<root-dir>/logs/`.
4. Run `co-op-review` after translation to check freshness, structure, and local links.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfigurasjonsfeil

### Ingen leverandør av språkmodell

Feil:

```text
No language model configuration found.
```

Løsning:

- Konfigurer Azure OpenAI eller OpenAI.
- Verifiser at variablene er i miljøet der kommandoen kjøres.
- For lokal bruk, plasser dem i `.env` i prosjektets rotmappe.

Se [Konfigurasjon](configuration.md).

### Bildeoversettelse uten Azure AI Vision

Feil:

```text
Image translation requested but Azure AI Service is not configured.
```

Løsning:

- Legg til `AZURE_AI_SERVICE_API_KEY`.
- Legg til `AZURE_AI_SERVICE_ENDPOINT`.
- Eller kjør en tekst-kommando som `translate -l "ko" -md`.

### Ugyldig nøkkel eller endepunkt

Symptomer kan inkludere `401`, maskerte tillatelsesfeil, eller tilgangsfeil til endepunktet.

Løsning:

- Bekreft at nøkkelen tilhører samme Azure-ressurs som endepunktet.
- Bekreft at ressursen støtter Vision når du bruker `-img`.
- Bekreft at Azure OpenAI-distribusjonsnavn og API-versjon samsvarer med din distribusjon.
- Kjør med debug-logger: `translate -l "ko" -md -d -s`.

## Ingen filer ble oversatt

Vanlige årsaker:

- De valgte flaggene matcher ikke filene dine.
- Oversatte filer finnes allerede.
- Kildefiler ligger i ekskluderte kataloger.
- Kommandoen kjøres fra feil prosjektrot.

Sjekk:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Bruk `--root-dir` når kommandoen kjøres utenfor prosjektroten.

## Uventet lenkeatferd

Omskriving av lenker avhenger av valgte innholdstyper:

- `-nb` inkludert: notatboklenker kan peke til oversatte notatbøker.
- `-nb` ekskludert: notatboklenker kan fortsatt peke til opprinnelige notatbøker.
- `-img` inkludert: bildelenker kan peke til oversatte bilder.
- `-img` ekskludert: bildelenker kan fortsatt peke til kildebilder.

Kjør en full innholdsoversettelse når alle interne lenker skal foretrekke oversatte utdata:

```bash
translate -l "ko" -md -nb -img
```

Kjør lenke-gjennomgang etter oversettelse:

```bash
co-op-review -l "ko"
```

## Problemer med Markdown-rendering

Hvis oversatt Markdown gjengis feil:

- Sjekk at frontmatter starter og slutter med `---`.
- Sjekk at antall kodegjerder samsvarer mellom kilde- og oversatte filer.
- Kjør `co-op-review` for å fange vanlige strukturproblemer.
- Oversett den spesifikke filen på nytt hvis output ble ødelagt.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action kjørte, men ingen pull request ble opprettet

Hvis `peter-evans/create-pull-request` rapporterer at branchen ikke ligger foran base, fant workflowen ingen filer å committe.

Sannsynlige årsaker:

- Oversettelseskjøringen produserte ingen endringer.
- `.gitignore` ekskluderer `translations/`, `translated_images/`, eller oversatte notatbøker.
- `add-paths` samsvarer ikke med de genererte utdata-katalogene.
- Oversettelsestrinnet avsluttet tidlig.

Løsninger:

1. Bekreft at genererte filer finnes i `translations/` eller `translated_images/`.
2. Bekreft at `.gitignore` ikke ignorerer genererte utdata.
3. Bruk matchende `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Legg midlertidig til debug-flagg i translate-kommandoen:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Bekreft at workflow-tillatelser inkluderer:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Oversettelseskvalitet

Maskinoversettelser kan trenge menneskelig gjennomgang. Bruk `evaluate` kun når du ønsker eksperimentell kvalitetsvurdering og reparasjonsarbeidsflyter ved lav tillit.

!!! warning "Eksperimentell"
    `evaluate` kan bruke regelbaserte og LLM-baserte kontroller, og dens poengmodell og metadataoppførsel kan endre seg. Hold den utenfor obligatoriske CI-gates med mindre arbeidsflyten din er forberedt på endringer.

For deterministiske CI-sjekker, bruk `co-op-review` i stedet.