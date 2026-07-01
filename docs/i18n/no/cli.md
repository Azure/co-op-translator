# CLI-referanse

Co-op Translator installerer disse kommandolinje-kommandoene:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Kommandoene `translate`, `evaluate`, `migrate-links` og `co-op-review` ruter gjennom `co_op_translator.__main__`, som velger kommandoimplementasjonen basert på det påkallte skriptnavnet. MCP-serveren bruker `co_op_translator.mcp.server` direkte.

Hvis du skal velge mellom CLI, Python-API og MCP, start med [Velg arbeidsflyt](workflows.md).

## Førstegangs CLI-flyt

Start her hvis du bruker Co-op Translator fra en terminal:

1. Konfigurer en LLM-leverandør som beskrevet i [Konfigurasjon](configuration.md).
2. Velg innholdstypen du vil oversette.
3. Kjør først en fokusert kommando, for eksempel kun Markdown-oversettelse.
4. Bruk `--dry-run` før store endringer i depotet.
5. Bruk `co-op-review` etter oversettelse for å sjekke struktur og aktualitet.

| Mål | Kommando å starte med |
| --- | --- |
| Oversett Markdown-dokumenter | `translate -l "ko" -md` |
| Oversett notatbøker | `translate -l "ko" -nb` |
| Oversett tekst i bilder | `translate -l "ko" -img` |
| Forhåndsvis arbeid uten å skrive filer | `translate -l "ko" -md --dry-run` |
| Gjennomgå eksisterende oversettelser | `co-op-review -l "ko"` |
| Oppdater lenker i notatbøker og Markdown | `migrate-links -l "ko" --dry-run` |
| Eksponer verktøy for en MCP-klient | Konfigurer [MCP-serveren](mcp.md) i stedet for å kjøre CLI-kommandoer direkte. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

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

### Alternativer

| Alternativ | Påkrevd | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Mellomromseparerte språkkoder, for eksempel "es fr de", eller "all". |
| `-r`, `--root-dir` | Nei | Prosjektrot. Standard er den gjeldende katalogen. |
| `-u`, `--update` | Nei | Slett eksisterende oversettelser for valgte språk og opprett dem på nytt. |
| `-img`, `--images` | Nei | Oversett kun bildefiler. |
| `-md`, `--markdown` | Nei | Oversett kun Markdown-filer. |
| `-nb`, `--notebook` | Nei | Oversett kun Jupyter-notatbøker. |
| `-d`, `--debug` | Nei | Aktiver feilsøkingslogging i konsollen. |
| `-s`, `--save-logs` | Nei | Lagre DEBUG-nivå logger under `<root-dir>/logs/`. |
| `-x`, `--fix` | Nei | Oversett på nytt Markdown-filer med lav konfidens basert på tidligere evalueringsresultater. |
| `-c`, `--min-confidence` | Nei | Konfidensgrense for `--fix`. Standard er `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nei | Legg til eller undertrykk fraskrivelser om maskinoversettelse. Standard er aktivert i CLI. |
| `-f`, `--fast` | Nei | Utfaset rask bildemodus. |
| `-y`, `--yes` | Nei | Bekreft spørsmål automatisk, nyttig i CI. |
| `--repo-url` | Nei | Depot-URL brukt i README-språk-tabellens anbefaling om sparse-checkout. |
| `--migrate-language-folders` | Nei | Gi nytt navn til eldre alias-mapper, som `cn` eller `tw`, til kanoniske BCP 47-mapper. |
| `--dry-run` | Nei | Forhåndsvis migrering av språkmapper og oversettelsesestimater uten å skrive filer. |

Hvis ingen typeflagg er angitt, behandler `translate` Markdown, notatbøker og bilder. Bildeoversettelse krever konfigurasjon av Azure AI Vision.

## evaluate

Evaluer kvaliteten på oversatt Markdown for ett språk.

!!! warning "Eksperimentell"
    `evaluate` er eksperimentell. Den kan bruke regelbaserte og LLM-baserte kvalitetskontroller, skriver evalueringsresultater til oversettelsesmetadata, og scoringsmodellen og metadata-atferden kan endres.

```bash
evaluate -l "ko"
```

### Vanlige eksempler

Bruk en strengere terskel for lav konfidens:

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

### Alternativer

| Alternativ | Påkrevd | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-code` | Ja | Enkel språkkode som skal evalueres. Alias-koder normaliseres. |
| `-r`, `--root-dir` | Nei | Prosjektrot. Standard er den gjeldende katalogen. |
| `-c`, `--min-confidence` | Nei | Terskel brukt når man lister opp oversettelser med lav konfidens. Standard er `0.7`. |
| `-d`, `--debug` | Nei | Aktiver debug-logging. |
| `-s`, `--save-logs` | Nei | Lagre DEBUG-nivå logger under `<root-dir>/logs/`. |
| `-f`, `--fast` | Nei | Kun regelbasert evaluering. |
| `-D`, `--deep` | Nei | Kun LLM-basert evaluering. |

Som standard bruker `evaluate` både regelbasert og LLM-basert evaluering. Resultatene skrives inn i oversettelsesmetadata og oppsummeres i konsollen.

## co-op-review

Kjør deterministiske vedlikeholdskontroller for oversettelser uten API-legitimasjon.

!!! note "Beta"
    `co-op-review` er en beta deterministisk gjennomgangskommando. Den kaller ikke modelltilbydere eller skriver filer, men kontrollene og skjemaet for utdataene om problemer kan endres.

```bash
co-op-review -l "ko"
```

### Vanlige eksempler

Gjennomgå koreanske og japanske oversettelser fra gjeldende katalog:

```bash
co-op-review -l "ko ja"
```

Gjennomgå en spesifikk prosjektrot:

```bash
co-op-review -l "fr" -r ./my-course
```

Kun gjennomgå kildefiler endret i forhold til en base-ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Skriv ut GitHub-flavored Markdown-utdata for CI-oppsummeringer:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Alternativer

| Alternativ | Påkrevd | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-code` | Nei | Språkkode som skal gjennomgås. Kan sendes flere ganger eller som en mellomromseparert verdi. Standard er alle oppdagede oversettelsesspråk. |
| `-r`, `--root-dir` | Nei | Prosjektrot. Standard er den gjeldende katalogen. |
| `--changed-from` | Nei | Git-ref brukt for å begrense gjennomgangen til endrede kildefiler. |
| `--format` | Nei | Utdataformat: `text` eller `github`. Standard er `text`. |

`co-op-review` sjekker for manglende oversatte filer, manglende eller utdaterte oversettelsesmetadata, integriteten til Markdown-frontmatter og kodeblokker, ugyldig oversatt notatbok-JSON, og manglende lokale mål for Markdown- eller bildelenker. Manglende lenker er advarsler som standard; strukturelle og aktualitetsproblemer fører til at kommandoen feiler.

## co-op-translator-mcp

Kjør Co-op Translator MCP-serveren for agenter, redaktører og MCP-kompatible klienter.

```bash
co-op-translator-mcp
```

Standardtransport er `stdio`. Se [MCP-serveren](mcp.md)-veiledningen for klientkonfigurasjon, verktøy, ressurser og sikkerhetsmerknader.

### Alternativer

| Alternativ | Påkrevd | Beskrivelse |
| --- | --- | --- |
| `--transport` | Nei | MCP-transport: `stdio`, `streamable-http`, eller `sse`. Standard er `stdio`. |

## migrate-links

Reprosesser oversatte Markdown-filer og oppdater notatboklenker slik at de peker til oversatte notatbøker når disse er tilgjengelige.

```bash
migrate-links -l "ko ja"
```

### Vanlige eksempler

Forhåndsvis lenkeoppdateringer:

```bash
migrate-links -l "ko" --dry-run
```

Prosesser alle støttede språk uten bekreftelse:

```bash
migrate-links -l "all" -y
```

Skriv kun om lenker når oversatte notatbøker eksisterer:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Alternativer

| Alternativ | Påkrevd | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Mellomromseparerte språkkoder, eller `"all"`. |
| `-r`, `--root-dir` | Nei | Prosjektrot. Standard er den gjeldende katalogen. |
| `--image-dir` | Nei | Katalog for oversatte bilder relativt til roten. Standard er `translated_images`. |
| `--dry-run` | Nei | Vis filer som ville endres uten å skrive oppdateringer. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nei | Bruk originale notatboklenker når oversatte notatbøker mangler. Aktivert som standard. |
| `-d`, `--debug` | Nei | Aktiver feilsøkingslogging. |
| `-s`, `--save-logs` | Nei | Lagre DEBUG-nivå logger under `<root-dir>/logs/`. |
| `-y`, `--yes` | Nei | Bekreft forespørsler automatisk når alle språk behandles. |

## Miljø

Alle kommandoene krever én konfigurert LLM-leverandør:

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

## Kopier-og-lim-inn CLI-eksempler

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

Reparer Markdown-oversettelser med lav konfidens:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Kjør CI-vennlig Markdown-oversettelse:

```bash
translate -l "ko ja" -md -y -s
```

Gjennomgå oversatt innhold:

```bash
co-op-review -l "ko ja"
```

Forhåndsvis lenkemigrering:

```bash
migrate-links -l "ko" --dry-run
```