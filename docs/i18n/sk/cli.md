# CLI Reference

Co-op Translator inštaluje tieto príkazové vstupné body:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Príkazy `translate`, `evaluate`, `migrate-links` a `co-op-review` sa odosielajú cez `co_op_translator.__main__`, ktorý vyberie implementáciu príkazu na základe názvu spusteného skriptu. MCP server používa priamo `co_op_translator.mcp.server`.

Ak sa rozhodujete medzi CLI, Python API a MCP, začnite s [Vyberte si pracovný postup](workflows.md).

## First-Time CLI Flow

Začnite tu, ak používate Co-op Translator z terminálu:

1. Nakonfigurujte poskytovateľa LLM podľa pokynov v [Configuration](configuration.md).
2. Vyberte typ obsahu, ktorý chcete preložiť.
3. Najprv spustite zameraný príkaz, napríklad preklad iba Markdown.
4. Pred rozsiahlymi zmenami v repozitári použite `--dry-run`.
5. Po preklade použite `co-op-review` na skontrolovanie štruktúry a aktuálnosti.

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

Prekladajte súbory Markdown, notebooky a text na obrázkoch do jedného alebo viacerých cieľových jazykov.

```bash
translate -l "ko ja fr"
```

### Common examples

Preložiť iba Markdown:

```bash
translate -l "de" -md
```

Preložiť iba notebooky:

```bash
translate -l "zh-CN" -nb
```

Preložiť Markdown a obrázky:

```bash
translate -l "pt-BR" -md -img
```

Aktualizovať existujúce preklady ich odstránením a obnovením:

```bash
translate -l "ko" -u
```

Spustiť bez interaktívnych výziev:

```bash
translate -l "ko ja" -md -y
```

Uložiť logy:

```bash
translate -l "ko" -s
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Medzerou oddelené kódy jazykov, napríklad `"es fr de"`, alebo `"all"`. |
| `-r`, `--root-dir` | No | Koreň projektu. Predvolené je aktuálny adresár. |
| `-u`, `--update` | No | Odstrániť existujúce preklady pre vybrané jazyky a znovu ich vytvoriť. |
| `-img`, `--images` | No | Preložiť iba súbory s obrázkami. |
| `-md`, `--markdown` | No | Preložiť iba súbory Markdown. |
| `-nb`, `--notebook` | No | Preložiť iba Jupyter notebook súbory. |
| `-d`, `--debug` | No | Zapnúť debug logging v konzole. |
| `-s`, `--save-logs` | No | Uložiť DEBUG-úrovňové logy do `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Preložiť znovu Markdown súbory s nízkou dôverou na základe predchádzajúcich výsledkov hodnotenia. |
| `-c`, `--min-confidence` | No | Prah dôvery pre `--fix`. Predvolené je `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Pridať alebo potlačiť upozornenia o strojovom preklade. V CLI je predvolene povolené. |
| `-f`, `--fast` | No | Zastaralý režim rýchleho spracovania obrázkov. |
| `-y`, `--yes` | No | Automaticky potvrdiť výzvy, užitočné v CI. |
| `--repo-url` | No | URL repozitára používané v odporúčaní sparse-checkout tabuľky jazykov v README. |
| `--migrate-language-folders` | No | Premenovať staršie alias priečinky, ako `cn` alebo `tw`, na kanonické BCP 47 priečinky. |
| `--dry-run` | No | Náhľad migrácie priečinkov jazykov a odhadov prekladu bez zápisu súborov. |

Ak nie je zadaný žiadny typový parameter, `translate` spracuje Markdown, notebooky a obrázky. Preklad obrázkov vyžaduje konfiguráciu Azure AI Vision.

## evaluate

Vyhodnoťte kvalitu preloženého Markdownu pre jeden jazyk.

!!! warning "Experimentálne"
    `evaluate` je experimentálne. Môže používať pravidlové a LLM-založené kontroly kvality, zapisuje výsledky hodnotenia do metadát prekladu a jeho model hodnotenia a správanie s metadátami sa môžu meniť.

```bash
evaluate -l "ko"
```

### Common examples

Použiť prísnejší prah pre nízku dôveru:

```bash
evaluate -l "es" -c 0.8
```

Spustiť len pravidlové kontroly:

```bash
evaluate -l "fr" -f
```

Spustiť len LLM-založené kontroly:

```bash
evaluate -l "ja" -D
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Jediný kód jazyka na vyhodnotenie. Alias kódy sú normalizované. |
| `-r`, `--root-dir` | No | Koreň projektu. Predvolené je aktuálny adresár. |
| `-c`, `--min-confidence` | No | Prah používaný pri vypisovaní prekladov s nízkou dôverou. Predvolené je `0.7`. |
| `-d`, `--debug` | No | Zapnúť debug logging. |
| `-s`, `--save-logs` | No | Uložiť DEBUG-úrovňové logy do `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Iba pravidlové hodnotenie. |
| `-D`, `--deep` | No | Iba LLM-založené hodnotenie. |

Predvolene `evaluate` používa oba prístupy: pravidlové aj LLM-založené hodnotenie. Výsledky sa zapisujú do metadát prekladu a sumarizujú v konzole.

## co-op-review

Spustite deterministické kontroly údržby prekladov bez prihlasovacích údajov API.

!!! note "Beta"
    `co-op-review` je beta deterministický príkaz na revíziu. Neposkytuje volania poskytovateľov modelov ani nezapisuje súbory, avšak jeho kontroly a schéma výstupu problémov sa môžu vyvíjať.

```bash
co-op-review -l "ko"
```

### Common examples

Skontrolovať kórejské a japonské preklady z aktuálneho adresára:

```bash
co-op-review -l "ko ja"
```

Skontrolovať konkrétny koreň projektu:

```bash
co-op-review -l "fr" -r ./my-course
```

Skontrolovať iba zdrojové súbory zmenené oproti základnému refu:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Vytlačiť výstup vo formáte GitHub-flavored Markdown pre súhrny CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Kód jazyka na kontrolu. Môže byť zadaný viackrát alebo ako medzerou oddelená hodnota. Predvolene všetky zistené jazyky prekladov. |
| `-r`, `--root-dir` | No | Koreň projektu. Predvolené je aktuálny adresár. |
| `--changed-from` | No | Git ref používaný na obmedzenie revízie na zmenené zdrojové súbory. |
| `--format` | No | Formát výstupu: `text` alebo `github`. Predvolené je `text`. |

`co-op-review` momentálne kontroluje chýbajúce preložené súbory, chýbajúce alebo zastarané metadáta prekladu, integritu frontmatteru v Markdown a ohraničení kódu, neplatný preložený notebook JSON a chýbajúce miestne cieľové odkazy v Markdown alebo obrázkoch. Chýbajúce odkazy sú predvolene varovania; štrukturálne a aktuálne problémy ukončia príkaz s chybou.

## co-op-translator-mcp

Spustite MCP server Co-op Translator pre agentov, editorov a klientov kompatibilných s MCP.

```bash
co-op-translator-mcp
```

Predvolený transport je `stdio`. Pozrite si príručku [MCP Server](mcp.md) pre konfiguráciu klienta, nástroje, zdroje a bezpečnostné poznámky.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, alebo `sse`. Predvolené je `stdio`. |

## migrate-links

Znovu spracovať preložené súbory Markdown a aktualizovať odkazy v notebookoch tak, aby smerovali na preložené notebooky, ak sú dostupné.

```bash
migrate-links -l "ko ja"
```

### Common examples

Náhľad aktualizácií odkazov:

```bash
migrate-links -l "ko" --dry-run
```

Spracovať všetky podporované jazyky bez potvrdenia:

```bash
migrate-links -l "all" -y
```

Prepísať odkazy iba keď existujú preložené notebooky:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Medzerou oddelené kódy jazykov, alebo `"all"`. |
| `-r`, `--root-dir` | No | Koreň projektu. Predvolené je aktuálny adresár. |
| `--image-dir` | No | Adresár preložených obrázkov relatívny ku koreňu. Predvolené je `translated_images`. |
| `--dry-run` | No | Zobraziť súbory, ktoré by sa zmenili, bez zápisu aktualizácií. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Použiť pôvodné odkazy na notebooky, keď chýbajú preložené notebooky. Predvolené je povolené. |
| `-d`, `--debug` | No | Zapnúť debug logging. |
| `-s`, `--save-logs` | No | Uložiť DEBUG-úrovňové logy do `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Automaticky potvrdiť výzvy pri spracovaní všetkých jazykov. |

## Environment

Všetky príkazy vyžadujú aspoň jedného nakonfigurovaného poskytovateľa LLM:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Alebo OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Preklad obrázkov navyše vyžaduje Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Textové preklady sa zapisujú do:

```text
translations/<language-code>/<original-path>
```

Výstup preložených obrázkov sa zapisuje do:

```text
translated_images/<language-code>/<original-path>
```

Napríklad, preložením `README.md` a `docs/setup.md` do kórejčiny vznikne:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

Preložiť Markdown do troch jazykov:

```bash
translate -l "ko ja fr" -md
```

Preložiť len notebooky:

```bash
translate -l "zh-CN" -nb
```

Preložiť len obrázky:

```bash
translate -l "pt-BR" -img
```

Náhľad prekladu Markdown bez zápisu súborov:

```bash
translate -l "de es" -md --dry-run
```

Opraviť preklady Markdown s nízkou dôverou:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Spustiť CI-friendly preklad Markdown:

```bash
translate -l "ko ja" -md -y -s
```

Skontrolovať preložený výstup:

```bash
co-op-review -l "ko ja"
```

Náhľad migrácie odkazov:

```bash
migrate-links -l "ko" --dry-run
```