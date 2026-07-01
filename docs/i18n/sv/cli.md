# CLI-referens

Co-op Translator installerar dessa kommandoradsingångspunkter:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

The `translate`, `evaluate`, `migrate-links`, and `co-op-review` commands dispatch through `co_op_translator.__main__`, which selects the command implementation based on the invoked script name. The MCP server uses `co_op_translator.mcp.server` directly.

If you are deciding between CLI, Python API, and MCP, start with [Välj ditt arbetsflöde](workflows.md).

## Första gången med CLI

Börja här om du använder Co-op Translator från en terminal:

1. Konfigurera en LLM-leverantör enligt beskrivningen i [Konfiguration](configuration.md).
2. Välj den innehållstyp du vill översätta.
3. Kör först ett fokuserat kommando, till exempel endast Markdown-översättning.
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
| Gör verktyg tillgängliga för en MCP-klient | Konfigurera [MCP-servern](mcp.md) istället för att köra CLI-kommandon direkt. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

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

Uppdatera befintliga översättningar genom att ta bort dem och återskapa dem:

```bash
translate -l "ko" -u
```

Kör utan interaktiva uppmaningar:

```bash
translate -l "ko ja" -md -y
```

Spara loggar:

```bash
translate -l "ko" -s
```

### Alternativ

| Alternativ | Obligatoriskt | Beskrivning |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Språkkoder separerade med mellanslag, såsom "es fr de", eller "all". |
| `-r`, `--root-dir` | Nej | Projektrot. Standard är den aktuella katalogen. |
| `-u`, `--update` | Nej | Ta bort befintliga översättningar för valda språk och återskapa dem. |
| `-img`, `--images` | Nej | Översätt endast bildfiler. |
| `-md`, `--markdown` | Nej | Översätt endast Markdown-filer. |
| `-nb`, `--notebook` | Nej | Översätt endast Jupyter-notebook-filer. |
| `-d`, `--debug` | Nej | Aktivera debug-loggning i konsolen. |
| `-s`, `--save-logs` | Nej | Spara DEBUG-nivå loggar under `<root-dir>/logs/`. |
| `-x`, `--fix` | Nej | Översätt igen Markdown-filer med låg konfidens baserat på tidigare utvärderingsresultat. |
| `-c`, `--min-confidence` | Nej | Konfidensgräns för `--fix`. Standard är `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nej | Lägg till eller undertryck ansvarsfriskrivningar för maskinöversättning. Som standard aktiverat i CLI. |
| `-f`, `--fast` | Nej | Föråldrat snabbt bildläge. |
| `-y`, `--yes` | Nej | Bekräfta uppmaningar automatiskt, användbart i CI. |
| `--repo-url` | Nej | Repository-URL som används i README:s språktabell för sparse-checkout-råd. |
| `--migrate-language-folders` | Nej | Byt namn på äldre aliasmappar, såsom `cn` eller `tw`, till kanoniska BCP 47-mappar. |
| `--dry-run` | Nej | Förhandsgranska migration av språkmappar och uppskattningar av översättning utan att skriva filer. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Utvärdera kvaliteten på översatt Markdown för ett språk.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Vanliga exempel

Använd en striktare tröskel för låg konfidens:

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

| Alternativ | Obligatoriskt | Beskrivning |
| --- | --- | --- |
| `-l`, `--language-code` | Ja | En enda språkkod att utvärdera. Alias-koder normaliseras. |
| `-r`, `--root-dir` | Nej | Projektrot. Standard är den aktuella katalogen. |
| `-c`, `--min-confidence` | Nej | Tröskel som används när lågkonfidensöversättningar listas. Standard är `0.7`. |
| `-d`, `--debug` | Nej | Aktivera debug-loggning. |
| `-s`, `--save-logs` | Nej | Spara DEBUG-nivå loggar under `<root-dir>/logs/`. |
| `-f`, `--fast` | Nej | Endast regelbaserad utvärdering. |
| `-D`, `--deep` | Nej | Endast LLM-baserad utvärdering. |

Som standard använder `evaluate` både regelbaserad och LLM-baserad utvärdering. Resultaten skrivs till översättningsmetadata och sammanfattas i konsolen.

## co-op-review

Kör deterministiska underhållskontroller för översättningar utan API-referenser.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

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

Granska endast källfiler som ändrats jämfört med en basref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Skriv ut GitHub-flavored Markdown-utdata för CI-sammanfattningar:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Alternativ

| Alternativ | Obligatoriskt | Beskrivning |
| --- | --- | --- |
| `-l`, `--language-code` | Nej | Språkkod att granska. Kan passeras flera gånger eller som ett värde separerat med mellanslag. Som standard alla upptäckta översättningsspråk. |
| `-r`, `--root-dir` | Nej | Projektrot. Standard är den aktuella katalogen. |
| `--changed-from` | Nej | Git-ref som används för att begränsa granskningen till ändrade källfiler. |
| `--format` | Nej | Utdataformat: `text` eller `github`. Standard är `text`. |

`co-op-review` kontrollerar för närvarande saknade översatta filer, saknad eller föråldrad översättningsmetadata, integriteten hos Markdown frontmatter och kodavgränsare, ogiltig översatt notebook JSON, och saknade lokala Markdown- eller bildlänkmål. Saknade länkar är varningar som standard; strukturella och aktualitetsproblem gör att kommandot misslyckas.

## co-op-translator-mcp

Kör Co-op Translator MCP-servern för agenter, redaktörer och MCP-kompatibla klienter.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP-servern](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Alternativ

| Alternativ | Obligatoriskt | Beskrivning |
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

Skriv bara om länkar när översatta notebooks finns:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Alternativ

| Alternativ | Obligatoriskt | Beskrivning |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Språkkoder separerade med mellanslag, eller "all". |
| `-r`, `--root-dir` | Nej | Projektrot. Standard är den aktuella katalogen. |
| `--image-dir` | Nej | Översatt bildmapp relativt roten. Standard är `translated_images`. |
| `--dry-run` | Nej | Visa filer som skulle ändras utan att skriva uppdateringar. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nej | Använd ursprungliga notebook-länkar när översatta notebooks saknas. Aktiverat som standard. |
| `-d`, `--debug` | Nej | Aktivera debug-loggning. |
| `-s`, `--save-logs` | Nej | Spara DEBUG-nivå loggar under `<root-dir>/logs/`. |
| `-y`, `--yes` | Nej | Bekräfta uppmaningar automatiskt när alla språk bearbetas. |

## Miljö

Alla kommandon kräver en konfigurerad LLM-leverantör:

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

Bildöversättning kräver dessutom Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Utdata-layout

Textöversättningar skrivs under:

```text
translations/<language-code>/<original-path>
```

Översatt bildutdata skrivs under:

```text
translated_images/<language-code>/<original-path>
```

Till exempel, att översätta `README.md` och `docs/setup.md` till koreanska ger:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopiera-klistra CLI-exempel

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

Åtgärda Markdown-översättningar med låg konfidens:

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

Förhandsgranska länk-migrering:

```bash
migrate-links -l "ko" --dry-run
```