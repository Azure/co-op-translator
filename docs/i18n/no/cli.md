# CLI-referanse

Co-op Translator installerer disse kommandolinje-tilgangspunktene:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Kommandoene `translate`, `evaluate`, `migrate-links`, og `co-op-review` rutes gjennom `co_op_translator.__main__`, som velger kommandorealiseringen basert på det påkallte skriptnavnet. MCP-serveren bruker `co_op_translator.mcp.server` direkte.

Hvis du skal velge mellom CLI, Python-API og MCP, start med [Velg arbeidsflyt](workflows.md).

## Konsollutdata

Interaktive terminaler bruker Rich-formatering for kommandohode, fremdrift og sammendrag. CI og ikke-interaktiv utdata faller automatisk tilbake til ren tekst.

Sett `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` for å tvinge ren utdata, eller `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` for å tvinge Rich-utdata. Sett `CO_OP_TRANSLATOR_NO_PROGRESS=1` for å beholde sammendrag mens live fremdriftslinjer undertrykkes.

Bruk `translate --json-events progress.ndjson` når et annet system trenger
maskin-lesbar fremdrift. CLI-en fortsetter å vise menneskevennlig utdata, mens
NDJSON-filen mottar versjonerte `co-op.translation.event.v1`-hendelser med
stabile felt som `type`, `stage_key`, `completed`, `total`, og
`current_path`.

## Førstegangs CLI-flyt

Start her hvis du bruker Co-op Translator fra en terminal:

1. Konfigurer en LLM-leverandør som beskrevet i [Konfigurasjon](configuration.md).
2. Velg hvilken innholdstype du vil oversette.
3. Kjør en fokusert kommando først, for eksempel kun Markdown-oversettelse.
4. Bruk `--dry-run` før store endringer i depotet.
5. Bruk `co-op-review` etter oversettelse for å kontrollere struktur og ferskhet.

| Mål | Kommando å starte med |
| --- | --- |
| Oversett Markdown-dokumenter | `translate -l "ko" -md` |
| Oversett notatbøker | `translate -l "ko" -nb` |
| Oversett bildetekst | `translate -l "ko" -img` |
| Forhåndsvis arbeid uten å skrive filer | `translate -l "ko" -md --dry-run` |
| Gå gjennom eksisterende oversettelser | `co-op-review -l "ko"` |
| Oppdater notatbok- og Markdown-lenker | `migrate-links -l "ko" --dry-run` |
| Eksponer verktøy for en MCP-klient | Konfigurer [MCP-serveren](mcp.md) i stedet for å kjøre CLI-kommandoer direkte. |

## translate

Oversett Markdown-filer, notatbøker og bildetekst til ett eller flere mål-språk.

```bash
translate -l "ko ja fr"
```

### Vanlige eksempler

Oversett kun Markdown:

```bash
translate -l "de" -md
```

Oversett kun notatbøker:

```bash
translate -l "zh-CN" -nb
```

Oversett Markdown og bilder:

```bash
translate -l "pt-BR" -md -img
```

Oppdater eksisterende oversettelser ved å slette og gjenskape dem:

```bash
translate -l "ko" -u
```

Kjør uten interaktive spørsmål:

```bash
translate -l "ko ja" -md -y
```

Lagre logger:

```bash
translate -l "ko" -s
```

Skriv strukturerte fremdriftshendelser:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Valg

| Valg | Obligatorisk | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Mellomromseparerte språkkoder, som `"es fr de"`, eller `"all"`. |
| `-r`, `--root-dir` | No | Prosjektrot. Standard er gjeldende katalog. |
| `-u`, `--update` | No | Slett eksisterende oversettelser for valgte språk og gjenskap dem. |
| `-img`, `--images` | No | Oversett kun bildefiler. |
| `-md`, `--markdown` | No | Oversett kun Markdown-filer. |
| `-nb`, `--notebook` | No | Oversett kun Jupyter-notatbøker. |
| `-d`, `--debug` | No | Aktiver debug-logging i konsollen. |
| `-s`, `--save-logs` | No | Lagre DEBUG-nivå logger under `<root-dir>/logs/`. |
| `--json-events` | No | Skriv maskin-lesbare oversettelsesfremdriftshendelser som NDJSON. |
| `-x`, `--fix` | No | Oversett på nytt Markdown-filer med lav konfidens basert på tidligere evalueringsresultater. |
| `-c`, `--min-confidence` | No | Konfidensterskel for `--fix`. Standard er `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Legg til eller undertrykk maskinoversettelsesansvarsfraskrivelser. Aktivert som standard i CLI. |
| `-f`, `--fast` | No | Avviklet rask bildemodus. |
| `-y`, `--yes` | No | Bekreft spørsmål automatisk, nyttig i CI. |
| `--repo-url` | No | Depot-URL brukt i README-språk-tabellens sparse-checkout-anbefaling. |
| `--migrate-language-folders` | No | Gi nytt navn til eldre alias-mapper, som `cn` eller `tw`, til kanoniske BCP 47-mapper. |
| `--dry-run` | No | Forhåndsvis migrering av språkmapper og oversettelsesestimat uten å skrive filer. |

Hvis ingen type-flagg er oppgitt, behandler `translate` Markdown, notatbøker og bilder. Bildeoversettelse krever Azure AI Vision-konfigurasjon.

## evaluate

Evaluer kvaliteten på oversatt Markdown for ett språk.

!!! warning "Eksperimentell"
    `evaluate` er eksperimentell. Den kan bruke regelbaserte og LLM-baserte kvalitetskontroller, skriver evalueringsresultater i oversettelsesmetadata, og dens scoringsmodell og metadataoppførsel kan endre seg.

```bash
evaluate -l "ko"
```

### Vanlige eksempler

Bruk en strengere lav-konfidensterskel:

```bash
evaluate -l "es" -c 0.8
```

Kjør kun regelbaserte kontroller:

```bash
evaluate -l "fr" -f
```

Kjør kun LLM-baserte kontroller:

```bash
evaluate -l "ja" -D
```

### Valg

| Valg | Obligatorisk | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Enkel språkkode som skal evalueres. Alias-koder normaliseres. |
| `-r`, `--root-dir` | No | Prosjektrot. Standard er gjeldende katalog. |
| `-c`, `--min-confidence` | No | Terskel brukt ved oppføring av lav-konfidens-oversettelser. Standard er `0.7`. |
| `-d`, `--debug` | No | Aktiver debug-logging. |
| `-s`, `--save-logs` | No | Lagre DEBUG-nivå logger under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Kun regelbasert evaluering. |
| `-D`, `--deep` | No | Kun LLM-basert evaluering. |

Som standard bruker `evaluate` både regelbasert og LLM-basert evaluering. Resultatene skrives inn i oversettelsesmetadata og oppsummeres i konsollen.

## co-op-review

Kjør deterministiske vedlikeholdskontroller for oversettelser uten API-legitimasjon.

!!! note "Beta"
    `co-op-review` er en beta deterministisk gjennomgangskommando. Den kaller ikke modellleverandører eller skriver filer, men sjekkene og skjemaet for feilutdata kan utvikle seg.

```bash
co-op-review -l "ko"
```

### Vanlige eksempler

Gå gjennom koreanske og japanske oversettelser fra gjeldende katalog:

```bash
co-op-review -l "ko ja"
```

Gå gjennom et spesifikt prosjektrot:

```bash
co-op-review -l "fr" -r ./my-course
```

Gå kun gjennom README etter en oversettelse som bare var README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignorerer andre dokumenter og innfelte README-er. Den feiler hvis rotens `README.md` mangler. Kombinert med `--changed-from` gjennomgår den kun README når den kildefilen endret seg. README-only-oversettelse lar kilde-README være uendret, inkludert eventuelle delte seksjonsmarkører.




Gå kun gjennom kildefiler som er endret mot en base-ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Skriv ut GitHub-flavored Markdown-utdata for CI-sammendrag:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Valg

| Valg | Obligatorisk | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-code` | No | Språkkode å gjennomgå. Kan gis flere ganger eller som en mellomrom-separert verdi. Standard er alle oppdagede oversettelsesspråk. |
| `-r`, `--root-dir` | No | Prosjektrot. Standard er gjeldende katalog. |
| `--changed-from` | No | Git-ref brukt for å begrense gjennomgangen til endrede kildefiler. |
| `--readme-only` | No | Gå kun gjennom rotens `README.md`-oversettelse. |
| `--format` | No | Utdataformat: `text` eller `github`. Standard er `text`. |

`co-op-review` sjekker for manglende oversatte filer, manglende eller utdaterte oversettelsesmetadata, Markdown frontmatter og kodegjerde-integritet, ugyldig oversatt notatbok-JSON, og manglende lokale Markdown- eller bildelenkemål. Manglende lenker er advarsler som standard; strukturelle og ferskhetsproblemer gjør at kommandoen feiler.

## co-op-translator-mcp

Kjør Co-op Translator MCP-serveren for agenter, redaktører og MCP-kompatible klienter.

```bash
co-op-translator-mcp
```

Standard transport er `stdio`. Se guiden for [MCP-serveren](mcp.md) for klientkonfigurasjon, verktøy, ressurser og sikkerhetsnotater.

### Valg

| Valg | Obligatorisk | Beskrivelse |
| --- | --- | --- |
| `--transport` | No | MCP-transport: `stdio`, `streamable-http`, eller `sse`. Standard er `stdio`. |

## migrate-links

Behandle oversatte Markdown-filer på nytt og oppdater notatboklenker slik at de peker til oversatte notatbøker når tilgjengelig.

```bash
migrate-links -l "ko ja"
```

### Vanlige eksempler

Forhåndsvis lenkeoppdateringer:

```bash
migrate-links -l "ko" --dry-run
```

Behandle alle støttede språk uten bekreftelse:

```bash
migrate-links -l "all" -y
```

Skriv kun om lenker når oversatte notatbøker finnes:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Valg

| Valg | Obligatorisk | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Mellomromseparerte språkkoder, eller `"all"`. |
| `-r`, `--root-dir` | No | Prosjektrot. Standard er gjeldende katalog. |
| `--image-dir` | No | Katalog for oversatte bilder relativt til rot. Standard er `translated_images`. |
| `--dry-run` | No | Vis filer som ville endres uten å skrive oppdateringer. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Bruk opprinnelige notatboklenker når oversatte notatbøker mangler. Aktivert som standard. |
| `-d`, `--debug` | No | Aktiver debug-logging. |
| `-s`, `--save-logs` | No | Lagre DEBUG-nivå logger under `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Bekreft spørsmål automatisk når alle språk behandles. |

## Miljø

Når en kommando krever leverandørlegitimasjon, konfigurer ett av disse leverandørsettene. `translate --dry-run` og `co-op-review` krever ikke leverandørlegitimasjon:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Eller OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Eller Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Bildeoversettelse krever i tillegg Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Utdataoppsett

Tekstoversettelser skrives under:

```text
translations/<language-code>/<original-path>
```

Oversatt bildeutdata skrives under:

```text
translated_images/<language-code>/<original-path>
```

For eksempel, å oversette `README.md` og `docs/setup.md` til koreansk gir:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopier-og-lim CLI-eksempler

Oversett Markdown til tre språk:

```bash
translate -l "ko ja fr" -md
```

Oversett kun notatbøker:

```bash
translate -l "zh-CN" -nb
```

Oversett kun bilder:

```bash
translate -l "pt-BR" -img
```

Forhåndsvis Markdown-oversettelse uten å skrive filer:

```bash
translate -l "de es" -md --dry-run
```

Reparer lavkonfidens Markdown-oversettelser:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Kjør CI-vennlig Markdown-oversettelse:

```bash
translate -l "ko ja" -md -y -s
```

Gjennomgå oversatt utdata:

```bash
co-op-review -l "ko ja"
```

Forhåndsvis lenkemigrering:

```bash
migrate-links -l "ko" --dry-run
```