# Feilsøking

Bruk denne siden når en oversettelseskjøring lykkes uventet, feiler under konfigurasjon eller produserer utdata som trenger gjennomgang.

## Kom i gang

1. Kjør først en fokusert kommando, for eksempel `translate -l "ko" -md`.
2. Legg til `-d` for konsollens debug-logger.
3. Legg til `-s` for å lagre debug-logger under `<root-dir>/logs/`.
4. Kjør `co-op-review` etter oversettelsen for å sjekke aktualitet, struktur og lokale lenker.

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

- Konfigurer Azure OpenAI, OpenAI eller Anthropic.
- Bekreft at variablene finnes i miljøet hvor kommandoen kjøres.
- For lokal bruk, legg dem i `.env` i prosjektets rotmappe.

Se [Konfigurasjon](configuration.md).

### Bildeoversettelse uten Azure AI Vision

Feil:

```text
Image translation requested but Azure AI Service is not configured.
```

Løsning:

- Legg til `AZURE_AI_SERVICE_API_KEY`.
- Legg til `AZURE_AI_SERVICE_ENDPOINT`.
- Eller kjør en tekstbasert kommando som `translate -l "ko" -md`.

### Ugyldig nøkkel eller endepunkt

Symptomer kan inkludere `401`, sensurerte tillatelsesfeil eller tilgangsfeil til endepunktet.

Løsning:

- Bekreft at nøkkelen tilhører samme Azure-ressurs som endepunktet.
- Bekreft at ressursen støtter Vision når du bruker `-img`.
- Bekreft at Azure OpenAI-distribusjonsnavnet og API-versjonen stemmer med din distribusjon.
- Kjør med debug-logger: `translate -l "ko" -md -d -s`.

## Ingen filer ble oversatt

Vanlige årsaker:

- Valgte flagg passer ikke til filene dine.
- Det finnes allerede oversatte filer.
- Kildefiler ligger i ekskluderte kataloger.
- Kommandoen kjøres fra feil prosjektrot.

Kontroller:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Bruk `--root-dir` når kommandoen kjøres utenfor prosjektroten.

## Uventet lenkeoppførsel

Omskriving av lenker avhenger av valgte innholdstyper:

- `-nb` inkludert: koblinger til notatbøker kan peke til oversatte notatbøker.
- `-nb` ekskludert: koblinger til notatbøker kan fortsatt peke til kilde-notatbøker.
- `-img` inkludert: bildelenker kan peke til oversatte bilder.
- `-img` ekskludert: bildelenker kan fortsatt peke til kildebilder.

Kjør en full innholdsoversettelse når alle interne lenker skal foretrekke oversatte utdata:

```bash
translate -l "ko" -md -nb -img
```

Kjør lenkegjennomgang etter oversettelsen:

```bash
co-op-review -l "ko"
```

## Problemer med Markdown-rendering

Hvis oversatt Markdown gjengis feil:

- Sjekk at frontmatter starter og slutter med `---`.
- Sjekk at antall kodegjerder (code fences) stemmer mellom kilde- og oversatte filer.
- Kjør `co-op-review` for å fange vanlige strukturelle problemer.
- Oversett den aktuelle filen på nytt hvis utdataene ble korrupte.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action kjørte, men ingen pull request ble opprettet

Hvis `peter-evans/create-pull-request` rapporterer at branchen ikke ligger foran base, fant arbeidsflyten ingen filer å commite.

Sannsynlige årsaker:

- Oversettelseskjøringen ga ingen endringer.
- `.gitignore` ekskluderer `translations/`, `translated_images/` eller oversatte notatbøker.
- `add-paths` stemmer ikke overens med de genererte utdata-katalogene.
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

5. Bekreft at arbeidsflytens tillatelser inkluderer:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Oversettelseskvalitet

Maskinoversettelser kan trenge menneskelig gjennomgang. Bruk `evaluate` kun når du ønsker eksperimentell kvalitetsvurdering og reparasjonsarbeidsflyter for lav tillit.

!!! warning "Eksperimentell"
    `evaluate` kan bruke regelbaserte og LLM-baserte sjekker, og dens scoremodell og metadataoppførsel kan endres. Hold den utenfor obligatoriske CI-gater med mindre arbeidsflyten din er forberedt på endringer.

For deterministiske CI-sjekker, bruk `co-op-review` i stedet.