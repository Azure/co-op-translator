# Referencia CLI

Co-op Translator nainštaluje tieto príkazové vstupné body:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Príkazy `translate`, `evaluate`, `migrate-links` a `co-op-review` sú smerované cez `co_op_translator.__main__`, ktorý vyberá implementáciu príkazu na základe názvu spusteného skriptu. MCP server používa priamo `co_op_translator.mcp.server`.

Ak sa rozhodujete medzi CLI, Python API a MCP, začnite s [Vyberte si pracovný tok](workflows.md).

## Konzolový výstup

Interaktívne terminály používajú formátovanie Rich pre hlavičku príkazu, priebeh a súhrny. CI a neinteraktívny výstup sa automaticky prepne na obyčajný text.

Nastavte `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` pre vynútenie obyčajného výstupu, alebo `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` pre vynútenie Rich výstupu. Nastavte `CO_OP_TRANSLATOR_NO_PROGRESS=1` pre zachovanie súhrnov pri potlačení živých priebehových pruhov.

Použite `translate --json-events progress.ndjson` keď iný systém potrebuje
strojovo čitateľný priebeh. CLI pokračuje vo vykresľovaní výstupu pre používateľov, zatiaľ čo
súbor NDJSON prijíma verzované `co-op.translation.event.v1` udalosti so
stabilnými poľami ako `type`, `stage_key`, `completed`, `total` a
`current_path`.

## Postup pri prvom použití CLI

Začnite tu, ak používate Co-op Translator z terminálu:

1. Nakonfigurujte poskytovateľa LLM podľa pokynov v [Konfigurácia](configuration.md).
2. Vyberte typ obsahu, ktorý chcete prekladať.
3. Najprv spustite zameraný príkaz, napríklad preklad iba Markdownu.
4. Použite `--dry-run` pred rozsiahlymi zmenami v repozitári.
5. Použite `co-op-review` po preklade na kontrolu štruktúry a aktuálnosti.

| Cieľ | Príkaz na začatie |
| --- | --- |
| Preložiť Markdown dokumenty | `translate -l "ko" -md` |
| Preložiť notebooky | `translate -l "ko" -nb` |
| Preložiť text na obrázkoch | `translate -l "ko" -img` |
| Náhľad práce bez zapisovania súborov | `translate -l "ko" -md --dry-run` |
| Skontrolovať existujúce preklady | `co-op-review -l "ko"` |
| Aktualizovať odkazy v notebookoch a Markdown súboroch | `migrate-links -l "ko" --dry-run` |
| Sprístupniť nástroje klientovi MCP | Nakonfigurujte [MCP Server](mcp.md) namiesto priameho spúšťania CLI príkazov. |

## translate

Prekladajte Markdown súbory, notebooky a texty na obrázkoch do jedného alebo viacerých cieľových jazykov.

```bash
translate -l "ko ja fr"
```

### Bežné príklady

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

Aktualizovať existujúce preklady odstránením a opätovným vytvorením:

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

Zapisovať štruktúrované udalosti priebehu:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Možnosti

| Možnosť | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-codes` | Áno | Kódy jazykov oddelené medzerou, napríklad `"es fr de"`, alebo `"all"`. |
| `-r`, `--root-dir` | Nie | Projektový koreň. Predvolene aktuálny adresár. |
| `-u`, `--update` | Nie | Odstrániť existujúce preklady pre vybrané jazyky a znovu ich vytvoriť. |
| `-img`, `--images` | Nie | Prekladať len súbory s obrázkami. |
| `-md`, `--markdown` | Nie | Prekladať len Markdown súbory. |
| `-nb`, `--notebook` | Nie | Prekladať len Jupyter notebook súbory. |
| `-d`, `--debug` | Nie | Povoliť debug logovanie v konzole. |
| `-s`, `--save-logs` | Nie | Uložiť logy úrovne DEBUG do `<root-dir>/logs/`. |
| `--json-events` | Nie | Zapisovať strojovo čitateľné udalosti priebehu prekladu ako NDJSON. |
| `-x`, `--fix` | Nie | Preložiť znovu Markdown súbory s nízkou dôverou na základe predchádzajúcich výsledkov hodnotenia. |
| `-c`, `--min-confidence` | Nie | Prahová hodnota dôvery pre `--fix`. Predvolene `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Nie | Pridať alebo potlačiť upozornenie o strojovom preklade. V CLI sú predvolene povolené. |
| `-f`, `--fast` | Nie | Zastaraný rýchly režim pre obrázky. |
| `-y`, `--yes` | Nie | Automaticky potvrdzovať výzvy, užitočné v CI. |
| `--repo-url` | Nie | URL repozitára používaná v oznámení sparse-checkout tabuľky jazykov v README. |
| `--migrate-language-folders` | Nie | Premenovať staršie aliasové priečinky, napr. `cn` alebo `tw`, na kanonické priečinky podľa BCP 47. |
| `--dry-run` | Nie | Náhľad migrácie priečinkov jazykov a odhadov prekladu bez zápisu súborov. |

Ak nie je zadaný žiadny typový prepínač, `translate` spracuje Markdown, notebooky a obrázky. Preklad obrázkov vyžaduje konfiguráciu Azure AI Vision.

## evaluate

Ohodnoťte kvalitu prekladu Markdownu pre jeden jazyk.

!!! warning "Experimentálne"
    `evaluate` je experimentálny. Môže používať pravidlové a LLM-poháňané kontroly kvality, zapisuje výsledky hodnotenia do metadát prekladu a jeho hodnotiaci model a správanie metadát sa môžu zmeniť.

```bash
evaluate -l "ko"
```

### Bežné príklady

Použiť prísnejší prah pre nízku dôveru:

```bash
evaluate -l "es" -c 0.8
```

Spustiť len kontroly založené na pravidlách:

```bash
evaluate -l "fr" -f
```

Spustiť len LLM-poháňané kontroly:

```bash
evaluate -l "ja" -D
```

### Možnosti

| Možnosť | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-code` | Áno | Jediný kód jazyka na vyhodnotenie. Aliasové kódy sú normalizované. |
| `-r`, `--root-dir` | Nie | Projektový koreň. Predvolene aktuálny adresár. |
| `-c`, `--min-confidence` | Nie | Prahová hodnota použitá pri vypisovaní prekladov s nízkou dôverou. Predvolene `0.7`. |
| `-d`, `--debug` | Nie | Povoliť debug logovanie. |
| `-s`, `--save-logs` | Nie | Uložiť logy úrovne DEBUG do `<root-dir>/logs/`. |
| `-f`, `--fast` | Nie | Len hodnotenie založené na pravidlách. |
| `-D`, `--deep` | Nie | Len LLM-poháňané hodnotenie. |

Predvolene `evaluate` využíva obe – pravidlové aj LLM-poháňané hodnotenie. Výsledky sa zapíšu do metadát prekladu a zhrnú v konzole.

## co-op-review

Spustiť deterministické kontroly údržby prekladov bez API poverení.

!!! note "Beta"
    `co-op-review` je beta deterministický kontrolný príkaz. Nevolá poskytovateľov modelov ani nezapisuje súbory, ale jeho kontroly a schéma výstupu problémov sa môžu vyvíjať.

```bash
co-op-review -l "ko"
```

### Bežné príklady

Skontrolovať kórejské a japonské preklady z aktuálneho adresára:

```bash
co-op-review -l "ko ja"
```

Skontrolovať konkrétny koreň projektu:

```bash
co-op-review -l "fr" -r ./my-course
```

Skontrolovať iba README po preklade, ktorý zahŕňal len README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignoruje ostatné dokumenty a vnorené README. Zlyhá, ak chýba koreňový
`README.md`. V kombinácii s `--changed-from` kontroluje README len
keď sa daný zdrojový súbor zmenil. Preklad zameraný len na README ponecháva zdrojové README
nezmenené, vrátane akýchkoľvek značiek spoločných sekcií.

Skontrolovať len zdrojové súbory zmenené oproti základnému ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Vypísať výstup v GitHub-flavored Markdown pre CI súhrny:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Možnosti

| Možnosť | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-code` | Nie | Kód jazyka na kontrolu. Dá sa zadať viackrát alebo ako hodnota oddelená medzerou. Predvolene všetky zistené jazyky prekladu. |
| `-r`, `--root-dir` | Nie | Projektový koreň. Predvolene aktuálny adresár. |
| `--changed-from` | Nie | Git ref používaný na obmedzenie kontroly na zmenené zdrojové súbory. |
| `--readme-only` | Nie | Skontrolovať len koreňový `README.md` preklad. |
| `--format` | Nie | Formát výstupu: `text` alebo `github`. Predvolene `text`. |

`co-op-review` v súčasnosti kontroluje chýbajúce preložené súbory, chýbajúce alebo zastarané metadáta prekladu, frontmatter v Markdown a integritu ohraničení kódu, neplatný preložený JSON notebooku a chýbajúce lokálne ciele odkazov v Markdown alebo obrázkoch. Chýbajúce odkazy sú predvolene varovania; štrukturálne problémy a problémy s aktuálnosťou spôsobia zlyhanie príkazu.

## co-op-translator-mcp

Spustiť MCP server Co-op Translator pre agentov, editory a MCP-kompatibilných klientov.

```bash
co-op-translator-mcp
```

Predvolený transport je `stdio`. Pozrite si príručku [MCP Server](mcp.md) pre konfiguráciu klienta, nástroje, zdroje a bezpečnostné poznámky.

### Možnosti

| Možnosť | Povinné | Popis |
| --- | --- | --- |
| `--transport` | Nie | MCP transport: `stdio`, `streamable-http`, alebo `sse`. Predvolene `stdio`. |

## migrate-links

Znovu spracovať preložené Markdown súbory a aktualizovať odkazy v notebookoch tak, aby smerovali na preložené notebooky, keď sú k dispozícii.

```bash
migrate-links -l "ko ja"
```

### Bežné príklady

Náhľad aktualizácií odkazov:

```bash
migrate-links -l "ko" --dry-run
```

Spracovať všetky podporované jazyky bez potvrdenia:

```bash
migrate-links -l "all" -y
```

Prepisovať odkazy len v prípade, že existujú preložené notebooky:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Možnosti

| Možnosť | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-codes` | Áno | Kódy jazykov oddelené medzerou, alebo `"all"`. |
| `-r`, `--root-dir` | Nie | Projektový koreň. Predvolene aktuálny adresár. |
| `--image-dir` | Nie | Adresár pre preložené obrázky vzhľadom na koreň. Predvolene `translated_images`. |
| `--dry-run` | Nie | Zobraziť súbory, ktoré by sa zmenili, bez zápisu aktualizácií. |
| `--fallback-to-original`, `--no-fallback-to-original` | Nie | Použiť pôvodné odkazy na notebook, keď chýbajú preložené notebooky. Predvolene povolené. |
| `-d`, `--debug` | Nie | Povoliť debug logovanie. |
| `-s`, `--save-logs` | Nie | Uložiť logy úrovne DEBUG do `<root-dir>/logs/`. |
| `-y`, `--yes` | Nie | Automaticky potvrdiť výzvy pri spracovaní všetkých jazykov. |

## Prostredie

Keď príkaz vyžaduje poverenia poskytovateľa, nakonfigurujte jednu z týchto sád poskytovateľov. `translate --dry-run` a `co-op-review` nevyžadujú poverenia poskytovateľa:

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

# Alebo Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Preklad obrázkov navyše vyžaduje Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Rozloženie výstupu

Textové preklady sa zapisujú do:

```text
translations/<language-code>/<original-path>
```

Výstup preložených obrázkov sa zapisuje do:

```text
translated_images/<language-code>/<original-path>
```

Napríklad preklad `README.md` a `docs/setup.md` do kórejčiny vytvorí:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Príklady CLI na kopírovanie

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

Náhľad prekladu Markdownu bez zápisu súborov:

```bash
translate -l "de es" -md --dry-run
```

Opraviť preklady Markdownu s nízkou dôverou:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Spustiť preklad Markdownu priateľný k CI:

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