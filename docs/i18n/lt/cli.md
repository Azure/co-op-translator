# CLI nuoroda

Co-op Translator įdiegia šiuos komandinės eilutės įėjimo taškus:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Komandos `translate`, `evaluate`, `migrate-links` ir `co-op-review` perduodamos per `co_op_translator.__main__`, kuris pasirenka komandos įgyvendinimą pagal iškvietimo skripto pavadinimą. MCP serveris naudoja `co_op_translator.mcp.server` tiesiogiai.

Jei renkatės tarp CLI, Python API ir MCP, pradėkite nuo [Pasirinkite savo darbo eigą](workflows.md).

## Pradinis CLI srautas

Pradėkite čia, jei naudojate Co-op Translator iš terminalo:

1. Sukonfigūruokite LLM tiekėją, kaip aprašyta [Konfigūracijoje](configuration.md).
2. Pasirinkite turinio tipą, kurį norite versti.
3. Pirmiausia paleiskite siaurą komandą, pvz., tik Markdown vertimą.
4. Prieš atliekant didelius repozitorijaus pakeitimus naudokite `--dry-run`.
5. Po vertimo naudokite `co-op-review`, kad patikrintumėte struktūrą ir atnaujinimo būtinumą.

| Tikslas | Pradinė komanda |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### Dažni pavyzdžiai

Translate only Markdown:

```bash
translate -l "de" -md
```

Translate only notebooks:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

Update existing translations by deleting and recreating them:

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

Save logs:

```bash
translate -l "ko" -s
```

### Parinktys

| Parinktis | Privaloma | Aprašymas |
| --- | --- | --- |
| `-l`, `--language-codes` | Taip | Tarpais atskirti kalbų kodai, pvz. `"es fr de"`, arba `"all"`. |
| `-r`, `--root-dir` | Ne | Projekto šaknis. Pagal nutylėjimą - dabartinis katalogas. |
| `-u`, `--update` | Ne | Ištrinti esamus pasirinktas kalbas atitinkančius vertimus ir juos atkurti. |
| `-img`, `--images` | Ne | Versti tik vaizdų failus. |
| `-md`, `--markdown` | Ne | Versti tik Markdown failus. |
| `-nb`, `--notebook` | Ne | Versti tik Jupyter užrašų knygeles (notebook). |
| `-d`, `--debug` | Ne | Įjungti derinimo (debug) įrašymą į konsolę. |
| `-s`, `--save-logs` | Ne | Išsaugoti DEBUG lygiu žurnalus aplanke `<root-dir>/logs/`. |
| `-x`, `--fix` | Ne | Iš naujo išversti mažo pasitikėjimo Markdown failus, remiantis ankstesnių vertinimų rezultatais. |
| `-c`, `--min-confidence` | Ne | Pasitikėjimo slenkstis `--fix`. Pagal nutylėjimą `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ne | Pridėti arba slopinti mašininio vertimo atsakomybės pastabas. Pagal nutylėjimą CLI įjungta. |
| `-f`, `--fast` | Ne | Pasenęs greito vaizdų režimas. |
| `-y`, `--yes` | Ne | Automatiškai patvirtinti raginimus, naudinga CI. |
| `--repo-url` | Ne | Saugyklos URL, naudojamas README kalbų lentelės sparse-checkout patarimui. |
| `--migrate-language-folders` | Ne | Pervardinti senas alias aplankus, pvz. `cn` arba `tw`, į kanoninius BCP 47 aplankus. |
| `--dry-run` | Ne | Peržiūrėti kalbų aplankų migraciją ir vertimo sąmatą neįrašant failų. |

Jei nebuvo nurodytas tipo žymeklis (type flag), `translate` apdoroja Markdown, užrašų knygeles ir vaizdus. Vaizdų vertimas reikalauja Azure AI Vision konfigūracijos.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Eksperimentinė"
    `evaluate` yra eksperimentinė. Ji gali naudoti taisyklėmis grįstus ir LLM pagrindu atliekamus kokybės patikrinimus, įrašo vertinimo rezultatus į vertimo metaduomenis, ir jos įvertinimo modelis bei metaduomenų elgsena gali keistis.

```bash
evaluate -l "ko"
```

### Dažni pavyzdžiai

Use a stricter low-confidence threshold:

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### Parinktys

| Parinktis | Privaloma | Aprašymas |
| --- | --- | --- |
| `-l`, `--language-code` | Taip | Vienas kalbos kodas, kurį reikia įvertinti. Alias kodai normalizuojami. |
| `-r`, `--root-dir` | Ne | Projekto šaknis. Pagal nutylėjimą - dabartinis katalogas. |
| `-c`, `--min-confidence` | Ne | Slenkstis, naudojamas išvardinant mažo pasitikėjimo vertimus. Pagal nutylėjimą `0.7`. |
| `-d`, `--debug` | Ne | Įjungti derinimo (debug) įrašymą. |
| `-s`, `--save-logs` | Ne | Išsaugoti DEBUG lygiu žurnalus aplanke `<root-dir>/logs/`. |
| `-f`, `--fast` | Ne | Tik taisyklėmis grįstas vertinimas. |
| `-D`, `--deep` | Ne | Tik LLM pagrindu atliekamas vertinimas. |

Pagal nutylėjimą `evaluate` naudoja tiek taisyklėmis grįstą, tiek LLM pagrindu atliekamą vertinimą. Rezultatai įrašomi į vertimo metaduomenis ir apibendrinami konsolėje.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Bandomoji"
    `co-op-review` yra bandomoji deterministinė peržiūros komanda. Ji nekviečia modelių tiekėjų ir neįrašo failų, tačiau jos patikrinimai ir išvesties problemų schema gali keistis.

```bash
co-op-review -l "ko"
```

### Dažni pavyzdžiai

Review Korean and Japanese translations from the current directory:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Review only source files changed against a base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown output for CI summaries:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Parinktys

| Parinktis | Privaloma | Aprašymas |
| --- | --- | --- |
| `-l`, `--language-code` | Ne | Kalbos kodas peržiūrai. Gali būti perduodamas kelis kartus arba kaip tarpu atskirtas reikšmė. Pagal nutylėjimą - visos aptiktos vertimo kalbos. |
| `-r`, `--root-dir` | Ne | Projekto šaknis. Pagal nutylėjimą - dabartinis katalogas. |
| `--changed-from` | Ne | Git ref, naudojamas peržiūrai apriboti tik pakeistiems šaltinio failams. |
| `--format` | Ne | Išvesties formatas: `text` arba `github`. Pagal nutylėjimą `text`. |

`co-op-review` šiuo metu tikrina trūkstamus išverstus failus, trūkstamus arba pasenusius vertimo metaduomenis, Markdown frontmatter ir kodo skyriklių vientisumą, neteisingą išversto notebook JSON struktūrą ir trūkstamus vietinius Markdown arba vaizdų nuorodų tikslus. Trūkstamos nuorodos pagal nutylėjimą yra įspėjimai; struktūrinės ir atnaujinimo (freshness) problemos sukelia komandos klaidą.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Parinktys

| Parinktis | Privaloma | Aprašymas |
| --- | --- | --- |
| `--transport` | Ne | MCP transportas: `stdio`, `streamable-http`, arba `sse`. Pagal nutylėjimą `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### Dažni pavyzdžiai

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

Process all supported languages without confirmation:

```bash
migrate-links -l "all" -y
```

Only rewrite links when translated notebooks exist:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Parinktys

| Parinktis | Privaloma | Aprašymas |
| --- | --- | --- |
| `-l`, `--language-codes` | Taip | Tarpais atskirti kalbų kodai arba `"all"`. |
| `-r`, `--root-dir` | Ne | Projekto šaknis. Pagal nutylėjimą - dabartinis katalogas. |
| `--image-dir` | Ne | Išverstų vaizdų katalogas, santykinis šakniniam katalogui. Pagal nutylėjimą `translated_images`. |
| `--dry-run` | Ne | Rodyti failus, kurie būtų pakeisti, neįrašant atnaujinimų. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ne | Naudoti originalias notebook nuorodas, kai išverstos notebook nėra. Pagal nutylėjimą įjungta. |
| `-d`, `--debug` | Ne | Įjungti derinimo (debug) įrašymą. |
| `-s`, `--save-logs` | Ne | Išsaugoti DEBUG lygiu žurnalus aplanke `<root-dir>/logs/`. |
| `-y`, `--yes` | Ne | Automatiškai patvirtinti raginimus apdorojant visas kalbas. |

## Environment

All commands require one configured LLM provider:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Arba OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Išvesties struktūra

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Kopijuoti/įklijuoti CLI pavyzdžiai

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

Preview Markdown translation without writing files:

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