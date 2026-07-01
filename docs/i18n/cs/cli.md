# CLI Referenční příručka

Co-op Translator nainstaluje tyto příkazy příkazového řádku:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Příkazy `translate`, `evaluate`, `migrate-links` a `co-op-review` jsou předávány přes `co_op_translator.__main__`, který vybere implementaci příkazu podle názvu spouštěného skriptu. MCP server používá `co_op_translator.mcp.server` přímo.

Pokud si vybíráte mezi CLI, Python API a MCP, začněte s [Vyberte svůj pracovní postup](workflows.md).

## První spuštění CLI

Začněte zde, pokud používáte Co-op Translator z terminálu:

1. Nakonfigurujte poskytovatele LLM, jak je popsáno v [Configuration](configuration.md).
2. Vyberte typ obsahu, který chcete překládat.
3. Nejprve spusťte zaměřený příkaz, například překlad pouze Markdown.
4. Před rozsáhlými změnami v repozitáři použijte `--dry-run`.
5. Po překladu použijte `co-op-review` k prověření struktury a aktuálnosti.

| Cíl | Příkaz ke spuštění |
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

### Běžné příklady

Přeložit pouze Markdown:

```bash
translate -l "de" -md
```

Přeložit pouze notebooky:

```bash
translate -l "zh-CN" -nb
```

Přeložit Markdown a obrázky:

```bash
translate -l "pt-BR" -md -img
```

Aktualizovat existující překlady jejich smazáním a znovuvytvořením:

```bash
translate -l "ko" -u
```

Spustit bez interaktivních výzev:

```bash
translate -l "ko ja" -md -y
```

Uložit logy:

```bash
translate -l "ko" -s
```

### Možnosti

| Možnost | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Kódy jazyků oddělené mezerami, například `"es fr de"`, nebo `"all"`. |
| `-r`, `--root-dir` | No | Kořen projektu. Implicitně aktuální adresář. |
| `-u`, `--update` | No | Odstraní existující překlady pro vybrané jazyky a znovu je vytvoří. |
| `-img`, `--images` | No | Přeložit pouze soubory obrázků. |
| `-md`, `--markdown` | No | Přeložit pouze Markdown soubory. |
| `-nb`, `--notebook` | No | Přeložit pouze soubory Jupyter notebooků. |
| `-d`, `--debug` | No | Povolit debug logování v konzoli. |
| `-s`, `--save-logs` | No | Uložit logy na úrovni DEBUG do `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Znovu přeložit Markdown soubory s nízkou důvěrou na základě výsledků předchozího hodnocení. |
| `-c`, `--min-confidence` | No | Prahová hodnota důvěry pro `--fix`. Implicitně `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Přidat nebo potlačit upozornění o strojovém překladu. Ve výchozím nastavení je v CLI povoleno. |
| `-f`, `--fast` | No | Zastaralý režim rychlého zpracování obrázků. |
| `-y`, `--yes` | No | Automaticky potvrdit výzvy, užitečné v CI. |
| `--repo-url` | No | URL repozitáře používaná v doporučení pro sparse-checkout v tabulce jazyků v README. |
| `--migrate-language-folders` | No | Přejmenuje starší alias složky, jako `cn` nebo `tw`, na kanonické BCP 47 složky. |
| `--dry-run` | No | Náhled migrace složek jazyků a odhadů překladu bez zápisu souborů. |

Pokud není zadán žádný typový přepínač, `translate` zpracuje Markdown, notebooky a obrázky. Překlad obrázků vyžaduje konfiguraci Azure AI Vision.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Běžné příklady

Použít přísnější práh pro nízkou důvěru:

```bash
evaluate -l "es" -c 0.8
```

Spustit pouze pravidlové kontroly:

```bash
evaluate -l "fr" -f
```

Spustit pouze kontroly založené na LLM:

```bash
evaluate -l "ja" -D
```

### Možnosti

| Možnost | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Jednotný kód jazyka k ohodnocení. Aliasové kódy jsou normalizovány. |
| `-r`, `--root-dir` | No | Kořen projektu. Implicitně aktuální adresář. |
| `-c`, `--min-confidence` | No | Prahová hodnota používaná při výpisu překladů s nízkou důvěrou. Implicitně `0.7`. |
| `-d`, `--debug` | No | Povolit debug logování. |
| `-s`, `--save-logs` | No | Uložit logy na úrovni DEBUG do `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Pouze pravidlové hodnocení. |
| `-D`, `--deep` | No | Pouze hodnocení založené na LLM. |

Ve výchozím nastavení `evaluate` používá jak pravidlové, tak LLM založené hodnocení. Výsledky jsou zapsány do metadat překladu a shrnuty v konzoli.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Běžné příklady

Zkontrolovat korejské a japonské překlady z aktuálního adresáře:

```bash
co-op-review -l "ko ja"
```

Zkontrolovat konkrétní kořen projektu:

```bash
co-op-review -l "fr" -r ./my-course
```

Zkontrolovat pouze zdrojové soubory změněné oproti základní větvi:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Vytisknout výstup ve formátu GitHub-flavored Markdown pro souhrny v CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Možnosti

| Možnost | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-code` | No | Kód jazyka k revizi. Lze předat vícekrát nebo jako hodnota oddělená mezerami. Implicitně všechny zjištěné překladové jazyky. |
| `-r`, `--root-dir` | No | Kořen projektu. Implicitně aktuální adresář. |
| `--changed-from` | No | Git ref používaný k omezení revize na změněné zdrojové soubory. |
| `--format` | No | Výstupní formát: `text` nebo `github`. Implicitně `text`. |

`co-op-review` aktuálně kontroluje chybějící přeložené soubory, chybějící nebo zastaralá metadata překladu, integritu frontmatteru v Markdown a kódových bloků, neplatné přeložené JSONy notebooků a chybějící místní odkazy v Markdown nebo obrázcích. Chybějící odkazy jsou ve výchozím nastavení varování; strukturální a aktuálnostní problémy způsobí neúspěch příkazu.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Možnosti

| Možnost | Povinné | Popis |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, nebo `sse`. Implicitně `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### Běžné příklady

Náhled aktualizací odkazů:

```bash
migrate-links -l "ko" --dry-run
```

Zpracovat všechny podporované jazyky bez potvrzení:

```bash
migrate-links -l "all" -y
```

Přepsat odkazy pouze pokud existují přeložené notebooky:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Možnosti

| Možnost | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Kódy jazyků oddělené mezerami, nebo `"all"`. |
| `-r`, `--root-dir` | No | Kořen projektu. Implicitně aktuální adresář. |
| `--image-dir` | No | Adresář přeložených obrázků relativně k rootu. Implicitně `translated_images`. |
| `--dry-run` | No | Zobrazit soubory, které by se změnily, bez zápisu aktualizací. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Použít původní odkazy na notebooky, když chybějí přeložené notebooky. Ve výchozím nastavení povoleno. |
| `-d`, `--debug` | No | Povolit debug logování. |
| `-s`, `--save-logs` | No | Uložit logy na úrovni DEBUG do `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Automaticky potvrdit výzvy při zpracování všech jazyků. |

## Prostředí

Všechny příkazy vyžadují jeden nakonfigurovaný poskytovatel LLM:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Nebo OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Překlad obrázků navíc vyžaduje Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Rozložení výstupu

Textové překlady jsou zapisovány do:

```text
translations/<language-code>/<original-path>
```

Přeložené obrázky jsou ukládány do:

```text
translated_images/<language-code>/<original-path>
```

Například přeložení `README.md` a `docs/setup.md` do korejštiny vytvoří:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Příklady CLI ke kopírování a vložení

Přeložit Markdown do tří jazyků:

```bash
translate -l "ko ja fr" -md
```

Přeložit pouze notebooky:

```bash
translate -l "zh-CN" -nb
```

Přeložit pouze obrázky:

```bash
translate -l "pt-BR" -img
```

Náhled překladu Markdown bez zápisu souborů:

```bash
translate -l "de es" -md --dry-run
```

Opravit přeložené Markdowny s nízkou důvěrou:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Spustit překlad Markdown vhodný pro CI:

```bash
translate -l "ko ja" -md -y -s
```

Zkontrolovat přeložený výstup:

```bash
co-op-review -l "ko ja"
```

Náhled migrace odkazů:

```bash
migrate-links -l "ko" --dry-run
```