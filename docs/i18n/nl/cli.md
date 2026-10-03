# CLI-referentie

Co-op Translator installeert deze opdrachtregel-entrypoints:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

De `translate`, `evaluate`, `migrate-links` en `co-op-review` opdrachten worden via `co_op_translator.__main__` aangestuurd, die de commandimplementatie selecteert op basis van de aangeroepen scriptnaam. De MCP-server gebruikt `co_op_translator.mcp.server` direct.

Als u moet kiezen tussen CLI, Python API en MCP, begin dan met [Kies uw workflow](workflows.md).

## Console-uitvoer

Interactieve terminals gebruiken Rich-opmaak voor de commandokop, voortgang en samenvattingen. CI en niet-interactieve uitvoer vallen automatisch terug op platte tekst.

Stel `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` in om platte uitvoer af te dwingen, of `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` om Rich-uitvoer af te dwingen. Stel `CO_OP_TRANSLATOR_NO_PROGRESS=1` in om samenvattingen te behouden terwijl live voortgangsbalken worden onderdrukt.

Gebruik `translate --json-events progress.ndjson` wanneer een ander systeem
machinaal leesbare voortgang nodig heeft. De CLI blijft menselijke uitvoer renderen, terwijl
het NDJSON-bestand versiegecodeerde `co-op.translation.event.v1`-gebeurtenissen ontvangt met
stabiele velden zoals `type`, `stage_key`, `completed`, `total` en
`current_path`.

## Eerste CLI-werkstroom

Begin hier als u Co-op Translator vanuit een terminal gebruikt:

1. Configureer een LLM-provider zoals beschreven in [Configuratie](configuration.md).
2. Kies het inhoudstype dat u wilt vertalen.
3. Voer eerst een gerichte opdracht uit, zoals alleen Markdown-vertaling.
4. Gebruik `--dry-run` vóór grote repositorywijzigingen.
5. Gebruik `co-op-review` na vertaling om structuur en actualiteit te controleren.

| Doel | Opdracht om mee te beginnen |
| --- | --- |
| Vertaal Markdown-documenten | `translate -l "ko" -md` |
| Vertaal notebooks | `translate -l "ko" -nb` |
| Vertaal afbeeldingstekst | `translate -l "ko" -img` |
| Voorvertoning van werk zonder bestanden te schrijven | `translate -l "ko" -md --dry-run` |
| Controleer bestaande vertalingen | `co-op-review -l "ko"` |
| Werk notebook- en Markdown-links bij | `migrate-links -l "ko" --dry-run` |
| Stel tools beschikbaar voor een MCP-client | Configureer de [MCP Server](mcp.md) in plaats van CLI-opdrachten direct uit te voeren. |

## translate

Vertaal Markdown-bestanden, notebooks en afbeeldingstekst naar één of meer doeltalen.

```bash
translate -l "ko ja fr"
```

### Veelvoorkomende voorbeelden

Vertaal alleen Markdown:

```bash
translate -l "de" -md
```

Vertaal alleen notebooks:

```bash
translate -l "zh-CN" -nb
```

Vertaal Markdown en afbeeldingen:

```bash
translate -l "pt-BR" -md -img
```

Werk bestaande vertalingen bij door ze te verwijderen en opnieuw aan te maken:

```bash
translate -l "ko" -u
```

Voer uit zonder interactieve prompts:

```bash
translate -l "ko ja" -md -y
```

Logs opslaan:

```bash
translate -l "ko" -s
```

Schrijf gestructureerde voortgangsgebeurtenissen:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Opties

| Optie | Vereist | Beschrijving |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Door spaties gescheiden taalcodes, zoals `"es fr de"`, of `"all"`. |
| `-r`, `--root-dir` | Nee | Projectroot. Standaard de huidige map. |
| `-u`, `--update` | Nee | Verwijder bestaande vertalingen voor geselecteerde talen en maak ze opnieuw aan. |
| `-img`, `--images` | Nee | Vertaal alleen afbeeldingsbestanden. |
| `-md`, `--markdown` | Nee | Vertaal alleen Markdown-bestanden. |
| `-nb`, `--notebook` | Nee | Vertaal alleen Jupyter-notebookbestanden. |
| `-d`, `--debug` | Nee | Schakel debug-logging in de console in. |
| `-s`, `--save-logs` | Nee | Sla DEBUG-niveau logs op onder `<root-dir>/logs/`. |
| `--json-events` | Nee | Schrijf machinaal leesbare vertaagvoortgangsgebeurtenissen als NDJSON. |
| `-x`, `--fix` | Nee | Hertaal Markdown-bestanden met lage betrouwbaarheid op basis van eerdere evaluatieresultaten. |
| `-c`, `--min-confidence` | Nee | Drempel voor vertrouwen voor `--fix`. Standaard `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nee | Voeg of onderdruk disclaimers voor machinale vertaling. Standaard ingeschakeld in de CLI. |
| `-f`, `--fast` | Nee | Verouderde snelle afbeeldingsmodus. |
| `-y`, `--yes` | Nee | Bevestig prompts automatisch, handig in CI. |
| `--repo-url` | Nee | Repository-URL gebruikt in de README-taaltabel voor sparse-checkout-aanwijzingen. |
| `--migrate-language-folders` | Nee | Hernoem legacy alias-mappen, zoals `cn` of `tw`, naar canonieke BCP 47-mappen. |
| `--dry-run` | Nee | Voorvertoning van migratie van taalmappen en vertaalschattingen zonder bestanden te schrijven. |

Als geen type-vlag is opgegeven, verwerkt `translate` Markdown, notebooks en afbeeldingen. Afbeeldingsvertaling vereist Azure AI Vision-configuratie.

## evaluate

Beoordeel de kwaliteit van vertaalde Markdown voor één taal.

!!! warning "Experimental"
    `evaluate` is experimenteel. Het kan regelgebaseerde en LLM-gebaseerde kwaliteitscontroles gebruiken, schrijft evaluatieresultaten naar vertaalmetadata, en het scoremodel en het gedrag van metadata kunnen veranderen.

```bash
evaluate -l "ko"
```

### Veelvoorkomende voorbeelden

Gebruik een strengere drempel voor lage betrouwbaarheid:

```bash
evaluate -l "es" -c 0.8
```

Voer alleen regelgebaseerde controles uit:

```bash
evaluate -l "fr" -f
```

Voer alleen LLM-gebaseerde controles uit:

```bash
evaluate -l "ja" -D
```

### Opties

| Optie | Vereist | Beschrijving |
| --- | --- | --- |
| `-l`, `--language-code` | Ja | Enkele taalcode om te evalueren. Aliascodes worden genormaliseerd. |
| `-r`, `--root-dir` | Nee | Projectroot. Standaard de huidige map. |
| `-c`, `--min-confidence` | Nee | Drempel gebruikt bij het weergeven van lage-vertrouwen vertalingen. Standaard `0.7`. |
| `-d`, `--debug` | Nee | Schakel debug-logging in. |
| `-s`, `--save-logs` | Nee | Sla DEBUG-niveau logs op onder `<root-dir>/logs/`. |
| `-f`, `--fast` | Nee | Alleen regelgebaseerde evaluatie. |
| `-D`, `--deep` | Nee | Alleen LLM-gebaseerde evaluatie. |

Standaard gebruikt `evaluate` zowel regelgebaseerde als LLM-gebaseerde evaluatie. Resultaten worden in de vertaalmetadata geschreven en samengevat in de console.

## co-op-review

Voer deterministische onderhoudscontroles voor vertalingen uit zonder API-referenties.

!!! note "Beta"
    `co-op-review` is een bètacommand voor deterministische controles. Het roept geen modelproviders aan en schrijft geen bestanden, maar de controles en het schema voor issue-uitvoer kunnen veranderen.

```bash
co-op-review -l "ko"
```

### Veelvoorkomende voorbeelden

Controleer Koreaanse en Japanse vertalingen vanuit de huidige map:

```bash
co-op-review -l "ko ja"
```

Controleer een specifieke projectroot:

```bash
co-op-review -l "fr" -r ./my-course
```

Controleer alleen de README na een alleen-README-vertaling:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` negeert andere documenten en geneste READMEs. Het faalt als de root
`README.md` ontbreekt. Gecombineerd met `--changed-from` bekijkt het alleen de README
wanneer dat bronbestand is gewijzigd. Een alleen-README-vertaling laat de bron-README
ongewijzigd, inclusief eventuele markeringen voor gedeelde secties.

Controleer alleen bronbestanden die zijn gewijzigd ten opzichte van een basisref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Geef GitHub-flavored Markdown-uitvoer weer voor CI-samenvattingen:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opties

| Optie | Vereist | Beschrijving |
| --- | --- | --- |
| `-l`, `--language-code` | Nee | Taalcode om te controleren. Kan meerdere keren worden opgegeven of als een spatie-gescheiden waarde. Standaard alle ontdekte vertaaltalen. |
| `-r`, `--root-dir` | Nee | Projectroot. Standaard de huidige map. |
| `--changed-from` | Nee | Git-ref gebruikt om beoordeling te beperken tot gewijzigde bronbestanden. |
| `--readme-only` | Nee | Controleer alleen de root `README.md`-vertaling. |
| `--format` | Nee | Uitvoerformaat: `text` of `github`. Standaard `text`. |

`co-op-review` controleert momenteel op ontbrekende vertaalde bestanden, ontbrekende of verouderde vertaalmetadata, integriteit van Markdown-frontmatter en code-fences, ongeldige vertaalde notebook-JSON en ontbrekende lokale Markdown- of afbeeldingslinkdoelen. Ontbrekende links zijn standaard waarschuwingen; structurele en actualiteitsproblemen laten de opdracht falen.

## co-op-translator-mcp

Draai de Co-op Translator MCP-server voor agents, editors en MCP-compatibele clients.

```bash
co-op-translator-mcp
```

De standaardtransport is `stdio`. Zie de [MCP Server](mcp.md)-gids voor clientconfiguratie, tools, bronnen en veiligheidsopmerkingen.

### Opties

| Optie | Vereist | Beschrijving |
| --- | --- | --- |
| `--transport` | Nee | MCP-transport: `stdio`, `streamable-http`, of `sse`. Standaard `stdio`. |

## migrate-links

Herverwerk vertaalde Markdown-bestanden en werk notebooklinks bij zodat ze wijzen naar vertaalde notebooks wanneer beschikbaar.

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

| Optie | Vereist | Beschrijving |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Door spaties gescheiden taalcodes, of `"all"`. |
| `-r`, `--root-dir` | Nee | Projectroot. Standaard de huidige map. |
| `--image-dir` | Nee | Map voor vertaalde afbeeldingen relatief aan de root. Standaard `translated_images`. |
| `--dry-run` | Nee | Toon bestanden die zouden veranderen zonder updates te schrijven. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nee | Gebruik originele notebooklinks wanneer vertaalde notebooks ontbreken. Standaard ingeschakeld. |
| `-d`, `--debug` | Nee | Schakel debug-logging in. |
| `-s`, `--save-logs` | Nee | Sla DEBUG-niveau logs op onder `<root-dir>/logs/`. |
| `-y`, `--yes` | Nee | Bevestig prompts automatisch bij het verwerken van alle talen. |

## Omgeving

Wanneer een opdracht provider-referenties vereist, configureer dan een van deze providersets. `translate --dry-run` en `co-op-review` vereisen geen provider-referenties:

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

# Of Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Afbeeldingsvertaling vereist daarnaast Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Uitvoerindeling

Tekstvertalingen worden weggeschreven naar:

```text
translations/<language-code>/<original-path>
```

Vertaalde afbeeldingsuitvoer wordt weggeschreven naar:

```text
translated_images/<language-code>/<original-path>
```

Bijvoorbeeld, het vertalen van `README.md` en `docs/setup.md` naar het Koreaans levert:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopieer-en-plak CLI-voorbeelden

Vertaal Markdown naar drie talen:

```bash
translate -l "ko ja fr" -md
```

Vertaal alleen notebooks:

```bash
translate -l "zh-CN" -nb
```

Vertaal alleen afbeeldingen:

```bash
translate -l "pt-BR" -img
```

Voorvertoning van Markdown-vertaling zonder bestanden te schrijven:

```bash
translate -l "de es" -md --dry-run
```

Herstel Markdown-vertalingen met lage betrouwbaarheid:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Voer CI-vriendelijke Markdown-vertaling uit:

```bash
translate -l "ko ja" -md -y -s
```

Controleer vertaalde output:

```bash
co-op-review -l "ko ja"
```

Voorvertoning van linkmigratie:

```bash
migrate-links -l "ko" --dry-run
```