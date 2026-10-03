# CLI-referens

Co-op Translator installerar följande kommandoradsingångar:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Kommandona `translate`, `evaluate`, `migrate-links` och `co-op-review` vidarebefordras via `co_op_translator.__main__`, som väljer kommandots implementation baserat på det anropade skriptnamnet. MCP-servern använder `co_op_translator.mcp.server` direkt.

Om du väljer mellan CLI, Python API och MCP, börja med [Välj ditt arbetsflöde](workflows.md).

## Konsolutdata

Interaktiva terminaler använder Rich-formattering för kommandots rubrik, förlopp och sammanfattningar. CI och icke-interaktivt utdata faller automatiskt tillbaka till vanlig text.

Sätt `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` för att tvinga enkel utdata, eller `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` för att tvinga Rich-utdata. Sätt `CO_OP_TRANSLATOR_NO_PROGRESS=1` för att behålla sammanfattningar samtidigt som live-förloppsindikatorer undertrycks.

Använd `translate --json-events progress.ndjson` när ett annat system behöver
maskinläsbart förlopp. CLI fortsätter att återge användarvänligt utdata, medan
NDJSON-filen får versionerade `co-op.translation.event.v1`-händelser med
stabila fält såsom `type`, `stage_key`, `completed`, `total` och
`current_path`.

## Första CLI-flödet

Börja här om du använder Co-op Translator från en terminal:

1. Konfigurera en LLM-leverantör enligt beskrivningen i [Konfiguration](configuration.md).
2. Välj vilken innehållstyp du vill översätta.
3. Kör först ett fokuserat kommando, till exempel översättning endast av Markdown.
4. Använd `--dry-run` före stora ändringar i repot.
5. Använd `co-op-review` efter översättning för att kontrollera struktur och aktualitet.

| Mål | Kommando att börja med |
| --- | --- |
| Översätt Markdown-dokument | `translate -l "ko" -md` |
| Översätt notebooks | `translate -l "ko" -nb` |
| Översätt text i bilder | `translate -l "ko" -img` |
| Förhandsgranska arbete utan att skriva filer | `translate -l "ko" -md --dry-run` |
| Granska befintliga översättningar | `co-op-review -l "ko"` |
| Uppdatera länkar i notebooks och Markdown | `migrate-links -l "ko" --dry-run` |
| Gör verktygen tillgängliga för en MCP-klient | Konfigurera [MCP Server](mcp.md) istället för att köra CLI-kommandon direkt. |

## translate

Översätt Markdown-filer, notebooks och bildtext till ett eller flera målspråk.

```bash
translate -l "ko ja fr"
```

### Vanliga exempel

Översätt endast Markdown:

```bash
translate -l "de" -md
```

Översätt endast notebooks:

```bash
translate -l "zh-CN" -nb
```

Översätt Markdown och bilder:

```bash
translate -l "pt-BR" -md -img
```

Uppdatera befintliga översättningar genom att ta bort och återskapa dem:

```bash
translate -l "ko" -u
```

Kör utan interaktiva promptar:

```bash
translate -l "ko ja" -md -y
```

Spara loggar:

```bash
translate -l "ko" -s
```

Skriv strukturerade förloppshändelser:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Alternativ

| Alternativ | Krävs | Beskrivning |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Mellanslagsseparerade språkkoder, till exempel `"es fr de"`, eller `"all"`. |
| `-r`, `--root-dir` | Nej | Projektrot. Standard är den aktuella katalogen. |
| `-u`, `--update` | Nej | Ta bort befintliga översättningar för valda språk och återskapa dem. |
| `-img`, `--images` | Nej | Översätt endast bildfiler. |
| `-md`, `--markdown` | Nej | Översätt endast Markdown-filer. |
| `-nb`, `--notebook` | Nej | Översätt endast Jupyter-notebookfiler. |
| `-d`, `--debug` | Nej | Aktivera debug-loggning i konsolen. |
| `-s`, `--save-logs` | Nej | Spara DEBUG-nivå loggar under `<root-dir>/logs/`. |
| `--json-events` | Nej | Skriv maskinläsbara förloppshändelser som NDJSON. |
| `-x`, `--fix` | Nej | Översätt om Markdown-filer med låg förtroendenivå baserat på tidigare utvärderingsresultat. |
| `-c`, `--min-confidence` | Nej | Tröskel för förtroende för `--fix`. Standard är `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nej | Lägg till eller undertryck maskinöversättningsansvarsfriskrivningar. I CLI är det som standard aktiverat. |
| `-f`, `--fast` | Nej | Föråldrat snabbt bildläge. |
| `-y`, `--yes` | Nej | Automatiskt bekräfta promptar, användbart i CI. |
| `--repo-url` | Nej | Repository-URL som används i README:s språk-tabell och sparse-checkout-rådet. |
| `--migrate-language-folders` | Nej | Byt namn på gamla alias-mappar, som `cn` eller `tw`, till kanoniska BCP 47-mappar. |
| `--dry-run` | Nej | Förhandsgranska migration av språkmappar och översättningsuppskattningar utan att skriva filer. |

Om ingen typflagga anges behandlar `translate` Markdown, notebooks och bilder. Bildöversättning kräver konfiguration av Azure AI Vision.

## evaluate

Utvärdera kvaliteten på översatt Markdown för ett språk.

!!! warning "Experimental"
    `evaluate` är experimentellt. Det kan använda regelbaserade och LLM-baserade kvalitetskontroller, skriver utvärderingsresultat till översättningsmetadata, och dess poängmodell och metadata-beteende kan förändras.

```bash
evaluate -l "ko"
```

### Vanliga exempel

Använd en strängare tröskel för låg förtroendenivå:

```bash
evaluate -l "es" -c 0.8
```

Kör endast regelbaserade kontroller:

```bash
evaluate -l "fr" -f
```

Kör endast LLM-baserade kontroller:

```bash
evaluate -l "ja" -D
```

### Alternativ

| Alternativ | Krävs | Beskrivning |
| --- | --- | --- |
| `-l`, `--language-code` | Ja | Enskild språkkod att utvärdera. Alias-koder normaliseras. |
| `-r`, `--root-dir` | Nej | Projektrot. Standard är den aktuella katalogen. |
| `-c`, `--min-confidence` | Nej | Tröskel som används vid uppräkning av låg-förtroende-översättningar. Standard är `0.7`. |
| `-d`, `--debug` | Nej | Aktivera debug-loggning. |
| `-s`, `--save-logs` | Nej | Spara DEBUG-nivå loggar under `<root-dir>/logs/`. |
| `-f`, `--fast` | Nej | Endast regelbaserad utvärdering. |
| `-D`, `--deep` | Nej | Endast LLM-baserad utvärdering. |

Som standard använder `evaluate` både regelbaserad och LLM-baserad utvärdering. Resultaten skrivs i översättningsmetadata och sammanfattas i konsolen.

## co-op-review

Kör deterministiska underhållskontroller av översättningar utan API-uppgifter.

!!! note "Beta"
    `co-op-review` är ett beta-deterministiskt granskningskommando. Det anropar inte modellleverantörer eller skriver filer, men dess kontroller och formatet för rapporterade problem kan förändras.

```bash
co-op-review -l "ko"
```

### Vanliga exempel

Granska koreanska och japanska översättningar från den aktuella katalogen:

```bash
co-op-review -l "ko ja"
```

Granska en specifik projektrot:

```bash
co-op-review -l "fr" -r ./my-course
```

Granska endast README efter en README-översättning:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignorerar andra dokument och inbäddade README-filer. Det misslyckas om rotens
`README.md` saknas. Kombinerat med `--changed-from`, granskar det endast README
när den källfilen ändrats. README-endast-översättning lämnar käll-README
oförändrad, inklusive eventuella delade avsnittsmarkörer.

Granska endast källfiler som ändrats mot en basref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Skriv ut GitHub-flavored Markdown-utdata för CI-sammanfattningar:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Alternativ

| Alternativ | Krävs | Beskrivning |
| --- | --- | --- |
| `-l`, `--language-code` | Nej | Språkkod att granska. Kan anges flera gånger eller som ett mellanslagsseparerat värde. Standard är alla upptäckta översättningsspråk. |
| `-r`, `--root-dir` | Nej | Projektrot. Standard är den aktuella katalogen. |
| `--changed-from` | Nej | Git-ref som används för att begränsa granskningen till ändrade källfiler. |
| `--readme-only` | Nej | Granska endast rotens `README.md`-översättning. |
| `--format` | Nej | Utdataformat: `text` eller `github`. Standard är `text`. |

`co-op-review` kontrollerar för närvarande saknade översatta filer, saknad eller föråldrad översättningsmetadata, Markdown-frontmatter och kodblockens integritet, ogiltig översatt notebook-JSON, och saknade lokala Markdown- eller bildlänkmål. Saknade länkar är varningar som standard; strukturella och aktualitetsproblem gör att kommandot misslyckas.

## co-op-translator-mcp

Kör Co-op Translator MCP-servern för agenter, redaktörer och MCP-kompatibla klienter.

```bash
co-op-translator-mcp
```

Standardtransport är `stdio`. Se guiden [MCP Server](mcp.md) för klientkonfiguration, verktyg, resurser och säkerhetsanteckningar.

### Alternativ

| Alternativ | Krävs | Beskrivning |
| --- | --- | --- |
| `--transport` | Nej | MCP-transport: `stdio`, `streamable-http`, eller `sse`. Standard är `stdio`. |

## migrate-links

Bearbeta om översatta Markdown-filer och uppdatera notebook-länkar så att de pekar på översatta notebooks när sådana finns.

```bash
migrate-links -l "ko ja"
```

### Vanliga exempel

Förhandsgranska länkuppdateringar:

```bash
migrate-links -l "ko" --dry-run
```

Bearbeta alla stödda språk utan bekräftelse:

```bash
migrate-links -l "all" -y
```

Skriv endast om länkar när översatta notebooks finns:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Alternativ

| Alternativ | Krävs | Beskrivning |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Mellanslagsseparerade språkkoder, eller `"all"`. |
| `-r`, `--root-dir` | Nej | Projektrot. Standard är den aktuella katalogen. |
| `--image-dir` | Nej | Mapp för översatta bilder relativt rot. Standard är `translated_images`. |
| `--dry-run` | Nej | Visa filer som skulle ändras utan att skriva uppdateringar. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nej | Använd ursprungliga notebook-länkar när översatta notebooks saknas. Aktiverat som standard. |
| `-d`, `--debug` | Nej | Aktivera debug-loggning. |
| `-s`, `--save-logs` | Nej | Spara DEBUG-nivå loggar under `<root-dir>/logs/`. |
| `-y`, `--yes` | Nej | Automatiskt bekräfta promptar vid bearbetning av alla språk. |

## Miljö

När ett kommando kräver leverantörsbehörigheter, konfigurera en av dessa leverantörsuppsättningar. `translate --dry-run` och `co-op-review` kräver inte leverantörsbehörigheter:

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

Bildöversättning kräver dessutom Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Utdatastruktur

Textöversättningar skrivs till:

```text
translations/<language-code>/<original-path>
```

Översatt bildutdata skrivs till:

```text
translated_images/<language-code>/<original-path>
```

Till exempel, att översätta `README.md` och `docs/setup.md` till koreanska ger:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopiera/klistra-in CLI-exempel

Översätt Markdown till tre språk:

```bash
translate -l "ko ja fr" -md
```

Översätt endast notebooks:

```bash
translate -l "zh-CN" -nb
```

Översätt endast bilder:

```bash
translate -l "pt-BR" -img
```

Förhandsgranska Markdown-översättning utan att skriva filer:

```bash
translate -l "de es" -md --dry-run
```

Åtgärda Markdown-översättningar med lågt förtroende:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Kör CI-vänlig Markdown-översättning:

```bash
translate -l "ko ja" -md -y -s
```

Granska översatt utdata:

```bash
co-op-review -l "ko ja"
```

Förhandsgranska länk-migration:

```bash
migrate-links -l "ko" --dry-run
```