# Referenční příručka CLI

Co-op Translator nainstaluje tyto příkazové spouštěče:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Příkazy `translate`, `evaluate`, `migrate-links` a `co-op-review` jsou směrovány přes `co_op_translator.__main__`, který vybere implementaci příkazu na základě názvu vyvolaného skriptu. MCP server používá přímo `co_op_translator.mcp.server`.

Pokud si vybíráte mezi CLI, Python API a MCP, začněte u [Vyberte svůj pracovní postup](workflows.md).

## Výstup v konzoli

Interaktivní terminály používají formátování Rich pro hlavičku příkazu, průběh a souhrny. CI a neinteraktivní výstup se automaticky přepnou na prostý text.

Nastavte `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` pro vynucení prostého výstupu, nebo `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` pro vynucení Rich výstupu. Nastavte `CO_OP_TRANSLATOR_NO_PROGRESS=1` pro zachování souhrnů při potlačení živých indikátorů průběhu.

Použijte `translate --json-events progress.ndjson` když jiný systém potřebuje
strojově čitelný průběh. CLI i nadále zobrazuje výstup pro lidi, zatímco
soubor NDJSON přijímá verzované události `co-op.translation.event.v1` s
stabilními poli, jako jsou `type`, `stage_key`, `completed`, `total` a
`current_path`.

## Postup při prvním použití CLI

Začněte zde, pokud používáte Co-op Translator z terminálu:

1. Nakonfigurujte poskytovatele LLM podle pokynů v [Konfigurace](configuration.md).
2. Vyberte typ obsahu, který chcete překládat.
3. Nejprve spusťte zaměřený příkaz, například překlad pouze Markdownu.
4. Před rozsáhlými změnami v repozitáři použijte `--dry-run`.
5. Po překladu použijte `co-op-review` k ověření struktury a aktuálnosti.

| Cíl | Příkaz k zahájení |
| --- | --- |
| Přeložit Markdown dokumenty | `translate -l "ko" -md` |
| Přeložit notebooky | `translate -l "ko" -nb` |
| Přeložit text na obrázcích | `translate -l "ko" -img` |
| Náhled práce bez zápisu souborů | `translate -l "ko" -md --dry-run` |
| Zkontrolovat existující překlady | `co-op-review -l "ko"` |
| Aktualizovat odkazy v noteboocích a Markdownu | `migrate-links -l "ko" --dry-run` |
| Zpřístupnit nástroje klientovi MCP | Nakonfigurujte [MCP Server](mcp.md) místo přímého spouštění CLI příkazů. |

## translate

Překládejte soubory Markdown, notebooky a text z obrázků do jednoho nebo více cílových jazyků.

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

Aktualizovat existující překlady odstraněním a znovuvytvořením:

```bash
translate -l "ko" -u
```

Spustit bez interaktivních výzev:

```bash
translate -l "ko ja" -md -y
```

Uložit záznamy:

```bash
translate -l "ko" -s
```

Zapsat strukturované události průběhu:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Možnosti

| Možnost | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-codes` | Ano | Mezerou oddělené kódy jazyků, například `"es fr de"`, nebo `"all"`. |
| `-r`, `--root-dir` | Ne | Kořen projektu. Výchozí je aktuální adresář. |
| `-u`, `--update` | Ne | Smaže existující překlady pro vybrané jazyky a znovu je vytvoří. |
| `-img`, `--images` | Ne | Přeložit pouze soubory obrázků. |
| `-md`, `--markdown` | Ne | Přeložit pouze Markdown soubory. |
| `-nb`, `--notebook` | Ne | Přeložit pouze soubory Jupyter notebooků. |
| `-d`, `--debug` | Ne | Povolit ladicí protokolování v konzoli. |
| `-s`, `--save-logs` | Ne | Uložit záznamy úrovně DEBUG do `<root-dir>/logs/`. |
| `--json-events` | Ne | Zapsat strojově čitelné události průběhu překladu jako NDJSON. |
| `-x`, `--fix` | Ne | Přeložit znovu Markdown soubory s nízkou důvěrou na základě předchozích výsledků hodnocení. |
| `-c`, `--min-confidence` | Ne | Prahová hodnota důvěry pro `--fix`. Výchozí je `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Ne | Přidat nebo potlačit upozornění o strojovém překladu. Ve výchozím nastavení povoleno v CLI. |
| `-f`, `--fast` | Ne | Zastaralý rychlý režim zpracování obrázků. |
| `-y`, `--yes` | Ne | Automaticky potvrdit výzvy, užitečné v CI. |
| `--repo-url` | Ne | URL repozitáře použitá v doporučení pro sparse-checkout v tabulce jazyků v README. |
| `--migrate-language-folders` | Ne | Přejmenuje staré alias složky, například `cn` nebo `tw`, na kanonické složky podle BCP 47. |
| `--dry-run` | Ne | Náhled migrace složek jazyků a odhadů překladu bez zápisu souborů. |

Pokud není poskytnut žádný typový přepínač, `translate` zpracuje Markdown, notebooky a obrázky. Překlad obrázků vyžaduje konfiguraci Azure AI Vision.

## evaluate

Vyhodnoťte kvalitu přeloženého Markdownu pro jeden jazyk.

!!! warning "Experimentální"
    `evaluate` je experimentální. Může používat kontrolu kvality založenou na pravidlech i na LLM, zapisuje výsledky hodnocení do metadat překladu a jeho model skórování a chování s metadaty se může změnit.

```bash
evaluate -l "ko"
```

### Běžné příklady

Použijte přísnější prahovou hodnotu pro nízkou důvěru:

```bash
evaluate -l "es" -c 0.8
```

Spustit pouze kontroly založené na pravidlech:

```bash
evaluate -l "fr" -f
```

Spustit pouze kontroly založené na LLM:

```bash
evaluate -l "ja" -D
```

### Volby

| Možnost | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-code` | Ano | Kód jediného jazyka k vyhodnocení. Aliasové kódy jsou normalizovány. |
| `-r`, `--root-dir` | Ne | Kořen projektu. Výchozí je aktuální adresář. |
| `-c`, `--min-confidence` | Ne | Prahová hodnota použitá při výpisu překladů s nízkou důvěrou. Výchozí je `0.7`. |
| `-d`, `--debug` | Ne | Povolit ladicí protokolování. |
| `-s`, `--save-logs` | Ne | Uložit záznamy úrovně DEBUG do `<root-dir>/logs/`. |
| `-f`, `--fast` | Ne | Pouze hodnocení založené na pravidlech. |
| `-D`, `--deep` | Ne | Pouze hodnocení založené na LLM. |

Ve výchozím nastavení `evaluate` používá jak hodnocení založené na pravidlech, tak na LLM. Výsledky se zapisují do metadat překladu a shrnují v konzoli.

## co-op-review

Proveďte deterministické kontroly údržby překladu bez pověření API.

!!! note "Beta"
    `co-op-review` je beta deterministický kontrolní příkaz. Nevolá poskytovatele modelů ani nezapisuje soubory, ale jeho kontroly a schéma výstupu problémů se mohou vyvíjet.

```bash
co-op-review -l "ko"
```

### Běžné příklady

Zkontrolujte korejské a japonské překlady z aktuálního adresáře:

```bash
co-op-review -l "ko ja"
```

Zkontrolujte konkrétní kořen projektu:

```bash
co-op-review -l "fr" -r ./my-course
```

Zkontrolujte pouze README po překladu zaměřeném pouze na README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignoruje ostatní dokumenty a vnořená README. Selže, pokud kořenový
`README.md` chybí. V kombinaci s `--changed-from` přezkoumá pouze README
když se tento zdrojový soubor změnil. Překlad pouze README ponechává zdrojové README
nezměněné, včetně případných značek sdílených sekcí.

Zkontrolovat pouze zdrojové soubory změněné oproti základní referenci:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Vytisknout výstup ve formátu GitHub-flavored Markdown pro souhrny v CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Volby

| Možnost | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-code` | Ne | Kód jazyka k revizi. Lze zadat vícekrát nebo jako mezerou oddělenou hodnotu. Výchozí jsou všechny objevené překladové jazyky. |
| `-r`, `--root-dir` | Ne | Kořen projektu. Výchozí je aktuální adresář. |
| `--changed-from` | Ne | Git ref použitý k omezení kontroly na změněné zdrojové soubory. |
| `--readme-only` | Ne | Zkontrolovat pouze překlad kořenového `README.md`. |
| `--format` | Ne | Formát výstupu: `text` nebo `github`. Výchozí je `text`. |

`co-op-review` aktuálně kontroluje chybějící přeložené soubory, chybějící nebo zastaralá metadata překladu, integritu Markdown frontmatter a ohraničení kódu, neplatné přeložené JSONy notebooků a chybějící místní cíle odkazů v Markdownu nebo u obrázků. Chybějící odkazy jsou ve výchozím nastavení varování; strukturální a problémy s aktuálností způsobí, že příkaz selže.

## co-op-translator-mcp

Spusťte MCP server Co-op Translatoru pro agenty, editory a klienty kompatibilní s MCP.

```bash
co-op-translator-mcp
```

Výchozí transport je `stdio`. Pro konfiguraci klienta, nástroje, zdroje a bezpečnostní poznámky si přečtěte průvodce [MCP server](mcp.md).

### Volby

| Možnost | Povinné | Popis |
| --- | --- | --- |
| `--transport` | Ne | MCP transport: `stdio`, `streamable-http`, nebo `sse`. Výchozí je `stdio`. |

## migrate-links

Znovu zpracujte přeložené Markdown soubory a aktualizujte odkazy v noteboocích tak, aby směřovaly na přeložené notebooky, pokud jsou k dispozici.

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

Přepisovat odkazy pouze pokud existují přeložené notebooky:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Volby

| Možnost | Povinné | Popis |
| --- | --- | --- |
| `-l`, `--language-codes` | Ano | Mezerou oddělené kódy jazyků, nebo `"all"`. |
| `-r`, `--root-dir` | Ne | Kořen projektu. Výchozí je aktuální adresář. |
| `--image-dir` | Ne | Adresář pro přeložené obrázky relativně ke kořeni. Výchozí je `translated_images`. |
| `--dry-run` | Ne | Ukázat soubory, které by se změnily, bez zápisu aktualizací. |
| `--fallback-to-original`, `--no-fallback-to-original` | Ne | Použít původní odkazy na notebooky, když přeložené notebooky chybí. Ve výchozím nastavení povoleno. |
| `-d`, `--debug` | Ne | Povolit ladicí protokolování. |
| `-s`, `--save-logs` | Ne | Uložit záznamy úrovně DEBUG do `<root-dir>/logs/`. |
| `-y`, `--yes` | Ne | Automaticky potvrdit výzvy při zpracování všech jazyků. |

## Prostředí

Když příkaz vyžaduje přihlašovací údaje poskytovatele, nakonfigurujte jednu z těchto sad poskytovatelů. `translate --dry-run` a `co-op-review` přihlašovací údaje poskytovatele nevyžadují:

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

# Nebo Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
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

Výstup přeložených obrázků se zapisuje do:

```text
translated_images/<language-code>/<original-path>
```

Například překlad `README.md` a `docs/setup.md` do korejštiny vytvoří:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Příklady CLI ke kopírování

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

Náhled překladu Markdownu bez zápisu souborů:

```bash
translate -l "de es" -md --dry-run
```

Opravit překlady Markdownu s nízkou důvěrou:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Spustit CI-přátelský překlad Markdownu:

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