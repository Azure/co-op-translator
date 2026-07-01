# CLI-referentie

Co-op Translator installeert de volgende commandoregel-entrypoints:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

De `translate`, `evaluate`, `migrate-links` en `co-op-review` commando's dispatchen via `co_op_translator.__main__`, dat de commandoregelimplementatie selecteert op basis van de aangeroepen scriptnaam. De MCP-server gebruikt `co_op_translator.mcp.server` rechtstreeks.

Als u moet kiezen tussen CLI, Python API en MCP, begin dan met [Choose Your Workflow](workflows.md).

## Eerste CLI-stappen

Begin hier als u Co-op Translator vanaf een terminal gebruikt:

1. Configureer een LLM-provider zoals beschreven in [Configuration](configuration.md).
2. Kies het inhoudstype dat u wilt vertalen.
3. Voer eerst een gerichte opdracht uit, zoals alleen Markdown-vertaling.
4. Gebruik `--dry-run` voordat u grote repository-wijzigingen uitvoert.
5. Gebruik `co-op-review` na vertaling om structuur en actualiteit te controleren.

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

Vertaal Markdown-bestanden, notebooks en afbeeldings-tekst naar een of meer doeltalen.

```bash
translate -l "ko ja fr"
```

### Veelvoorkomende voorbeelden

Alleen Markdown vertalen:

```bash
translate -l "de" -md
```

Alleen notebooks vertalen:

```bash
translate -l "zh-CN" -nb
```

Markdown en afbeeldingen vertalen:

```bash
translate -l "pt-BR" -md -img
```

Bestaande vertalingen bijwerken door ze te verwijderen en opnieuw te maken:

```bash
translate -l "ko" -u
```

Zonder interactieve prompts uitvoeren:

```bash
translate -l "ko ja" -md -y
```

Logs opslaan:

```bash
translate -l "ko" -s
```

### Opties

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Spatie-gescheiden taalcodes, zoals "es fr de", of "all". |
| `-r`, `--root-dir` | No | Projectroot. Standaard de huidige map. |
| `-u`, `--update` | No | Verwijder bestaande vertalingen voor geselecteerde talen en maak ze opnieuw aan. |
| `-img`, `--images` | No | Alleen afbeeldingsbestanden vertalen. |
| `-md`, `--markdown` | No | Alleen Markdown-bestanden vertalen. |
| `-nb`, `--notebook` | No | Alleen Jupyter-notebookbestanden vertalen. |
| `-d`, `--debug` | No | Debug-logging in de console inschakelen. |
| `-s`, `--save-logs` | No | DEBUG-niveau logs opslaan onder `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Markdown-bestanden met lage betrouwbaarheid opnieuw vertalen op basis van eerdere evaluatieresultaten. |
| `-c`, `--min-confidence` | No | Betrouwbaarheiddrempel voor `--fix`. Standaard `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Machinevertaling-verklaringen toevoegen of onderdrukken. Standaard ingeschakeld in de CLI. |
| `-f`, `--fast` | No | Verouderde snelle afbeeldingsmodus. |
| `-y`, `--yes` | No | Prompts automatisch bevestigen, handig in CI. |
| `--repo-url` | No | Repository-URL gebruikt in de README talen-tabel sparse-checkout advisering. |
| `--migrate-language-folders` | No | Hernoem legacy alias-mappen, zoals `cn` of `tw`, naar canonieke BCP 47 mappen. |
| `--dry-run` | No | Voorvertoning van taalmapmigratie en vertaalschattingen zonder bestanden te schrijven. |

Als geen typevlag is opgegeven, verwerkt `translate` Markdown, notebooks en afbeeldingen. Afbeeldingvertaling vereist Azure AI Vision-configuratie.

## evaluate

Evalueer de kwaliteit van vertaalde Markdown voor één taal.

!!! warning "Experimenteel"
    `evaluate` is experimenteel. Het kan regelgebaseerde en LLM-gebaseerde kwaliteitscontroles gebruiken, schrijft evaluatieresultaten in vertaalmetadata, en het scoringsmodel en metadata-gedrag kunnen veranderen.

```bash
evaluate -l "ko"
```

### Veelvoorkomende voorbeelden

Gebruik een strengere drempel voor lage betrouwbaarheid:

```bash
evaluate -l "es" -c 0.8
```

Alleen regelgebaseerde controles uitvoeren:

```bash
evaluate -l "fr" -f
```

Alleen LLM-gebaseerde controles uitvoeren:

```bash
evaluate -l "ja" -D
```

### Opties

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Enkele taalcode om te evalueren. Alias-codes worden genormaliseerd. |
| `-r`, `--root-dir` | No | Projectroot. Standaard de huidige map. |
| `-c`, `--min-confidence` | No | Drempel gebruikt bij het opsommen van vertalingen met lage betrouwbaarheid. Standaard `0.7`. |
| `-d`, `--debug` | No | Debug-logging inschakelen. |
| `-s`, `--save-logs` | No | DEBUG-niveau logs opslaan onder `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Alleen regelgebaseerde evaluatie. |
| `-D`, `--deep` | No | Alleen LLM-gebaseerde evaluatie. |

Standaard gebruikt `evaluate` zowel regelgebaseerde als LLM-gebaseerde evaluatie. Resultaten worden geschreven in vertaalmetadata en samengevat in de console.

## co-op-review

Voer deterministische onderhoudscontroles voor vertalingen uit zonder API-referenties.

!!! note "Bèta"
    `co-op-review` is een bètacommand die deterministische controles uitvoert. Het roept geen modelproviders aan en schrijft geen bestanden, maar de controles en het schema voor issue-uitvoer kunnen evolueren.

```bash
co-op-review -l "ko"
```

### Veelvoorkomende voorbeelden

Kijk Koreaanse en Japanse vertalingen na vanuit de huidige map:

```bash
co-op-review -l "ko ja"
```

Controleer een specifieke projectroot:

```bash
co-op-review -l "fr" -r ./my-course
```

Controleer alleen bronbestanden die gewijzigd zijn ten opzichte van een basisref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown-uitvoer voor CI-samenvattingen:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opties

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Taalcode om te controleren. Kan meerdere keren worden opgegeven of als spatie-gescheiden waarde. Standaard alle ontdekte vertaaltalen. |
| `-r`, `--root-dir` | No | Projectroot. Standaard de huidige map. |
| `--changed-from` | No | Git-ref gebruikt om de controle te beperken tot gewijzigde bronbestanden. |
| `--format` | No | Uitvoervorm: `text` of `github`. Standaard `text`. |

`co-op-review` controleert momenteel op ontbrekende vertaalde bestanden, ontbrekende of verouderde vertaalmetadata, Markdown-frontmatter en integriteit van codefences, ongeldig vertaald notebook JSON, en ontbrekende lokale Markdown- of afbeeldingslinkdoelen. Ontbrekende links zijn standaard waarschuwingen; structurele en actualiteitproblemen doen het commando falen.

## co-op-translator-mcp

Start de Co-op Translator MCP-server voor agents, editors en MCP-compatibele clients.

```bash
co-op-translator-mcp
```

De standaardtransportlaag is `stdio`. Zie de [MCP Server](mcp.md) gids voor clientconfiguratie, tools, resources en veiligheidsopmerkingen.

### Opties

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP-transport: `stdio`, `streamable-http`, of `sse`. Standaard `stdio`. |

## migrate-links

Herschrijf vertaalde Markdown-bestanden en werk notebooklinks bij zodat ze naar vertaalde notebooks verwijzen wanneer beschikbaar.

```bash
migrate-links -l "ko ja"
```

### Veelvoorkomende voorbeelden

Voorvertoning van linkupdates:

```bash
migrate-links -l "ko" --dry-run
```

Verwerk alle ondersteunde talen zonder bevestiging:

```bash
migrate-links -l "all" -y
```

Herschrijf links alleen wanneer vertaalde notebooks bestaan:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opties

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Spatie-gescheiden taalcodes, of `"all"`. |
| `-r`, `--root-dir` | No | Projectroot. Standaard de huidige map. |
| `--image-dir` | No | Vertaalde afbeeldingsmap relatief aan de root. Standaard `translated_images`. |
| `--dry-run` | No | Toon bestanden die zouden veranderen zonder updates te schrijven. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Gebruik originele notebooklinks wanneer vertaalde notebooks ontbreken. Standaard ingeschakeld. |
| `-d`, `--debug` | No | Debug-logging inschakelen. |
| `-s`, `--save-logs` | No | DEBUG-niveau logs opslaan onder `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Prompts automatisch bevestigen bij het verwerken van alle talen. |

## Omgeving

Alle commando's vereisen één geconfigureerde LLM-provider:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Of OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Afbeeldingvertaling vereist bovendien Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Uitvoerlayout

Tekstvertalingen worden weggeschreven onder:

```text
translations/<language-code>/<original-path>
```

Vertaalde afbeeldingsuitvoer wordt weggeschreven onder:

```text
translated_images/<language-code>/<original-path>
```

Bijvoorbeeld, het vertalen van `README.md` en `docs/setup.md` naar Koreaans produceert:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopieer-en-plak CLI-voorbeelden

Markdown naar drie talen vertalen:

```bash
translate -l "ko ja fr" -md
```

Alleen notebooks vertalen:

```bash
translate -l "zh-CN" -nb
```

Alleen afbeeldingen vertalen:

```bash
translate -l "pt-BR" -img
```

Markdownvertaling voorvertonen zonder bestanden te schrijven:

```bash
translate -l "de es" -md --dry-run
```

Markdownvertalingen met lage betrouwbaarheid repareren:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI-vriendelijke Markdownvertaling uitvoeren:

```bash
translate -l "ko ja" -md -y -s
```

Vertaald uitvoer beoordelen:

```bash
co-op-review -l "ko ja"
```

Voorvertoning van linkmigratie:

```bash
migrate-links -l "ko" --dry-run
```