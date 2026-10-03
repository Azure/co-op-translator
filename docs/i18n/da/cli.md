# CLI-reference

Co-op Translator installerer disse kommandolinje-kommandoer:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Kommandoerne `translate`, `evaluate`, `migrate-links` og `co-op-review` videresender via `co_op_translator.__main__`, som vælger kommandoimplementeringen baseret på det kaldte script-navn. MCP-serveren bruger `co_op_translator.mcp.server` direkte.

Hvis du skal vælge mellem CLI, Python API og MCP, start med [Vælg din arbejdsgang](workflows.md).

## Konsoloutput

Interaktive terminaler bruger Rich-formatering til kommandohovedet, fremdrift og resuméer. CI og ikke-interaktivt output falder automatisk tilbage til almindelig tekst.

Sæt `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` for at tvinge almindeligt output, eller `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` for at tvinge Rich-output. Sæt `CO_OP_TRANSLATOR_NO_PROGRESS=1` for at bevare resuméer samtidig med, at live-fremdriftsbjælker undertrykkes.

Brug `translate --json-events progress.ndjson`, når et andet system har brug for
maskinlæsbar fremdrift. CLI'en fortsætter med at gengive menneskeorienteret output, mens
NDJSON-filen modtager versionerede `co-op.translation.event.v1`-begivenheder med
stabile felter såsom `type`, `stage_key`, `completed`, `total` og
`current_path`.

## Førstegangs-CLI-flow

Start her, hvis du bruger Co-op Translator fra en terminal:

1. Konfigurer en LLM-udbyder som beskrevet i [Konfiguration](configuration.md).
2. Vælg den indholdstype, du vil oversætte.
3. Kør først en fokuseret kommando, såsom kun Markdown-oversættelse.
4. Brug `--dry-run` før større ændringer i dit repository.
5. Brug `co-op-review` efter oversættelsen for at kontrollere struktur og aktualitet.

| Mål | Startkommando |
| --- | --- |
| Oversæt Markdown-dokumenter | `translate -l "ko" -md` |
| Oversæt notebooks | `translate -l "ko" -nb` |
| Oversæt tekst i billeder | `translate -l "ko" -img` |
| Forhåndsvis arbejde uden at skrive filer | `translate -l "ko" -md --dry-run` |
| Gennemse eksisterende oversættelser | `co-op-review -l "ko"` |
| Opdater notebook- og Markdown-links | `migrate-links -l "ko" --dry-run` |
| Gør værktøjer tilgængelige for en MCP-klient | Konfigurer [MCP-server](mcp.md) i stedet for at køre CLI-kommandoer direkte. |

## translate

Oversæt Markdown-filer, notebooks og tekst i billeder til ét eller flere målsprog.

```bash
translate -l "ko ja fr"
```

### Almindelige eksempler

Oversæt kun Markdown:

```bash
translate -l "de" -md
```

Oversæt kun notebooks:

```bash
translate -l "zh-CN" -nb
```

Oversæt Markdown og billeder:

```bash
translate -l "pt-BR" -md -img
```

Opdater eksisterende oversættelser ved at slette og genskabe dem:

```bash
translate -l "ko" -u
```

Kør uden interaktive prompts:

```bash
translate -l "ko ja" -md -y
```

Gem logfiler:

```bash
translate -l "ko" -s
```

Skriv strukturerede fremdriftshændelser:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Indstillinger

| Indstilling | Påkrævet | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Sprogkoder adskilt af mellemrum, f.eks. `"es fr de"`, eller `"all"`. |
| `-r`, `--root-dir` | Nej | Projektrod. Standard er den aktuelle mappe. |
| `-u`, `--update` | Nej | Slet eksisterende oversættelser for valgte sprog og genskab dem. |
| `-img`, `--images` | Nej | Oversæt kun billedfiler. |
| `-md`, `--markdown` | Nej | Oversæt kun Markdown-filer. |
| `-nb`, `--notebook` | Nej | Oversæt kun Jupyter-notebookfiler. |
| `-d`, `--debug` | Nej | Aktivér fejlsøgningslogning i konsollen. |
| `-s`, `--save-logs` | Nej | Gem DEBUG-niveau logfiler under `<root-dir>/logs/`. |
| `--json-events` | Nej | Skriv maskinlæsbare oversættelsesfremdriftshændelser som NDJSON. |
| `-x`, `--fix` | Nej | Oversæt igen Markdown-filer med lav tillid baseret på tidligere evalueringsresultater. |
| `-c`, `--min-confidence` | Nej | Tillidsterskel for `--fix`. Standard er `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nej | Tilføj eller undertryk ansvarsfraskrivelser for maskinoversættelse. Standard er aktiveret i CLI'en. |
| `-f`, `--fast` | Nej | Forældet hurtig billedtilstand. |
| `-y`, `--yes` | Nej | Bekræft forespørgsler automatisk, nyttigt i CI. |
| `--repo-url` | Nej | Repository-URL brugt i README-sprogets tabel over sprog til sparse-checkout-rådgivning. |
| `--migrate-language-folders` | Nej | Omdøb ældre aliasmapper, såsom `cn` eller `tw`, til kanoniske BCP 47-mapper. |
| `--dry-run` | Nej | Forhåndsvis migration af sprogmapper og oversættelsesestimater uden at skrive filer. |

Hvis ingen type-flag er angivet, behandler `translate` Markdown, notebooks og billeder. Billedoversættelse kræver Azure AI Vision-konfiguration.

## evaluate

Evaluer kvaliteten af oversatte Markdown-filer for ét sprog.

!!! warning "Experimental"
    `evaluate` er eksperimentel. Den kan bruge regelbaserede og LLM-baserede kvalitetskontroller, skriver evalueringsresultater til oversættelsesmetadata, og dens scoringsmodel samt metadataadfærd kan ændre sig.

```bash
evaluate -l "ko"
```

### Almindelige eksempler

Brug en strengere tærskel for lav tillid:

```bash
evaluate -l "es" -c 0.8
```

Kør kun regelbaserede kontroller:

```bash
evaluate -l "fr" -f
```

Kør kun LLM-baserede kontroller:

```bash
evaluate -l "ja" -D
```

### Indstillinger

| Indstilling | Påkrævet | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-code` | Ja | Enkelt sprogkode at evaluere. Alias-koder normaliseres. |
| `-r`, `--root-dir` | Nej | Projektrod. Standard er den aktuelle mappe. |
| `-c`, `--min-confidence` | Nej | Tærskel brugt ved opregning af oversættelser med lav tillid. Standard er `0.7`. |
| `-d`, `--debug` | Nej | Aktivér fejlsøgningslogning. |
| `-s`, `--save-logs` | Nej | Gem DEBUG-niveau logfiler under `<root-dir>/logs/`. |
| `-f`, `--fast` | Nej | Kun regelbaseret evaluering. |
| `-D`, `--deep` | Nej | Kun LLM-baseret evaluering. |

Som standard bruger `evaluate` både regelbaseret og LLM-baseret evaluering. Resultaterne skrives til oversættelsesmetadata og opsummeres i konsollen.

## co-op-review

Kør deterministiske vedligeholdelsestjek af oversættelser uden API-adgangsoplysninger.

!!! note "Beta"
    `co-op-review` er en beta-deterministisk review-kommando. Den kalder ikke modeludbydere eller skriver filer, men dens tjek og issue-outputskema kan ændre sig.

```bash
co-op-review -l "ko"
```

### Almindelige eksempler

Gennemgå koreanske og japanske oversættelser fra den nuværende mappe:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Gennemgå kun README efter en README-only-oversættelse:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignorerer andre dokumenter og indlejrede READMEs. Den fejler, hvis roden
`README.md` mangler. Kombineret med `--changed-from` gennemgår den kun README'en
når den kildefil ændrede sig. README-only-oversættelsen lader kilde-README'en
uændret, inklusive eventuelle shared-section-mærker.

Gennemgå kun kildefiler, der er ændret i forhold til en base-ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Udskriv GitHub-flavored Markdown-output til CI-resuméer:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Indstillinger

| Valgmulighed | Påkrævet | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-code` | Nej | Sprogkode til gennemgang. Kan angives flere gange eller som en mellemrumsepareret værdi. Standard er alle opdagede oversættelsessprog. |
| `-r`, `--root-dir` | Nej | Projektrod. Standard er den aktuelle mappe. |
| `--changed-from` | Nej | Git-ref brugt til at begrænse gennemgangen til ændrede kildefiler. |
| `--readme-only` | Nej | Gennemgå kun oversættelsen af rod-`README.md`. |
| `--format` | Nej | Outputformat: `text` eller `github`. Standard er `text`. |

`co-op-review` tjekker i øjeblikket for manglende oversatte filer, manglende eller forældede oversættelsesmetadata, Markdown-frontmatter og kodefence-integritet, ugyldig oversat notebook-JSON og manglende lokale Markdown- eller billedelinkmål. Manglende links er advarsler som standard; strukturelle og aktualitetsproblemer får kommandoen til at fejle.

## co-op-translator-mcp

Kør Co-op Translator MCP-serveren for agenter, redaktører og MCP-kompatible klienter.

```bash
co-op-translator-mcp
```

Standardtransporten er `stdio`. Se [MCP Server](mcp.md)-guiden for klientkonfiguration, værktøjer, ressourcer og sikkerhedsnoter.

### Indstillinger

| Valgmulighed | Påkrævet | Beskrivelse |
| --- | --- | --- |
| `--transport` | Nej | MCP-transport: `stdio`, `streamable-http` eller `sse`. Standard er `stdio`. |

## migrate-links

Genbehandl oversatte Markdown-filer og opdater notebook-links, så de peger på oversatte notebooks, når de er tilgængelige.

```bash
migrate-links -l "ko ja"
```

### Almindelige eksempler

Forhåndsvis linkopdateringer:

```bash
migrate-links -l "ko" --dry-run
```

Bearbejd alle understøttede sprog uden bekræftelse:

```bash
migrate-links -l "all" -y
```

Omskriv kun links, når oversatte notebooks findes:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Indstillinger

| Valgmulighed | Påkrævet | Beskrivelse |
| --- | --- | --- |
| `-l`, `--language-codes` | Ja | Mellemrumseparerede sprogkoder, eller `"all"`. |
| `-r`, `--root-dir` | Nej | Projektrod. Standard er den aktuelle mappe. |
| `--image-dir` | Nej | Oversat billedmappe relativt til roden. Standard er `translated_images`. |
| `--dry-run` | Nej | Vis filer, der ville ændre sig uden at skrive opdateringer. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nej | Brug originale notebook-links når oversatte notebooks mangler. Aktiveret som standard. |
| `-d`, `--debug` | Nej | Aktivér debug-logning. |
| `-s`, `--save-logs` | Nej | Gem DEBUG-niveau logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | Nej | Auto-bekræft forespørgsler ved behandling af alle sprog. |

## Environment

Når en kommando kræver udbyder-legitimationsoplysninger, konfigurer et af disse udbydersæt. `translate --dry-run` og `co-op-review` kræver ikke udbyder-legitimationsoplysninger:

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

Billedoversættelse kræver desuden Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Uddata-layout

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Oversat billedoutput skrives under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopier-indsæt CLI-eksempler

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

Forhåndsvis Markdown-oversættelse uden at skrive filer:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```