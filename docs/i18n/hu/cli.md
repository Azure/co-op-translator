# CLI referencia

A Co-op Translator a következő parancssori belépési pontokat telepíti:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

A `translate`, `evaluate`, `migrate-links` és `co-op-review` parancsok a `co_op_translator.__main__`-en keresztül továbbítódnak, amely az indított script neve alapján választja ki a parancs implementációját. Az MCP szerver közvetlenül a `co_op_translator.mcp.server`-t használja.

Ha a CLI, a Python API és az MCP között döntesz, kezdd a [Válaszd ki a munkafolyamatot](workflows.md) lappal.

## Első CLI használat

Kezdj itt, ha terminálból használod a Co-op Translatort:

1. Állíts be egy LLM szolgáltatót a [Configuration](configuration.md) leírás szerint.
2. Válaszd ki a lefordítandó tartalomtípust.
3. Először futtass egy fókuszált parancsot, például csak Markdown fordítást.
4. Használd a `--dry-run` opciót nagy tárházmódosítások előtt.
5. Használd a `co-op-review`-t a fordítás után a szerkezet és frissesség ellenőrzésére.

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

Fordít Markdown fájlokat, notebookokat és képszöveget egy vagy több célnyelvre.

```bash
translate -l "ko ja fr"
```

### Gyakori példák

Csak Markdown fordítása:

```bash
translate -l "de" -md
```

Csak notebookok fordítása:

```bash
translate -l "zh-CN" -nb
```

Markdown és képek fordítása:

```bash
translate -l "pt-BR" -md -img
```

A meglévő fordítások frissítése törléssel és újrateremtéssel:

```bash
translate -l "ko" -u
```

Futtatás interaktív megerősítések nélkül:

```bash
translate -l "ko ja" -md -y
```

Naplók mentése:

```bash
translate -l "ko" -s
```

### Opciók

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, such as `"es fr de"`, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-u`, `--update` | No | Delete existing translations for selected languages and recreate them. |
| `-img`, `--images` | No | Translate only image files. |
| `-md`, `--markdown` | No | Translate only Markdown files. |
| `-nb`, `--notebook` | No | Translate only Jupyter notebook files. |
| `-d`, `--debug` | No | Enable debug logging in the console. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Retranslate low-confidence Markdown files based on previous evaluation results. |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Add or suppress machine translation disclaimers. Defaults to enabled in the CLI. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | No | Auto-confirm prompts, useful in CI. |
| `--repo-url` | No | Repository URL used in the README languages table sparse-checkout advisory. |
| `--migrate-language-folders` | No | Rename legacy alias folders, such as `cn` or `tw`, to canonical BCP 47 folders. |
| `--dry-run` | No | Preview language folder migration and translation estimates without writing files. |

Ha nem adsz meg típusjelzőt, a `translate` Markdown-t, notebookokat és képeket dolgoz fel. A képfordításhoz Azure AI Vision konfiguráció szükséges.

## evaluate

Értékeld a lefordított Markdown minőségét egy nyelvre.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Gyakori példák

Használj szigorúbb alacsony-bizalom küszöböt:

```bash
evaluate -l "es" -c 0.8
```

Csak szabályalapú ellenőrzések futtatása:

```bash
evaluate -l "fr" -f
```

Csak LLM-alapú ellenőrzések futtatása:

```bash
evaluate -l "ja" -D
```

### Opciók

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | No | Threshold used when listing low-confidence translations. Defaults to `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

Alapértelmezés szerint az `evaluate` mind szabályalapú, mind LLM-alapú értékelést használ. Az eredmények a fordítás metaadataiba kerülnek, és összefoglalva megjelennek a konzolon.

## co-op-review

Futtass determinisztikus fordítás-karbantartási ellenőrzéseket API hitelesítő adatok nélkül.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Gyakori példák

Ellenőrizd a koreai és japán fordításokat az aktuális könyvtárból:

```bash
co-op-review -l "ko ja"
```

Ellenőrizd egy konkrét projekt gyökérkönyvtárát:

```bash
co-op-review -l "fr" -r ./my-course
```

Ellenőrizd csak a forrásfájlokat, amelyek egy alap ref-hez képest változtak:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Nyomtasd GitHub-flavored Markdown kimenetet CI összefoglalókhoz:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opciók

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | Language code to review. Can be passed multiple times or as a space-separated value. Defaults to all discovered translation languages. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | No | Git ref used to limit review to changed source files. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

A `co-op-review` jelenleg ellenőrzi a hiányzó lefordított fájlokat, hiányzó vagy elavult fordítási metaadatokat, a Markdown frontmatter és kódkeret integritását, érvénytelen lefordított notebook JSON-t, és a hiányzó helyi Markdown vagy képlink célokat. A hiányzó linkek alapértelmezés szerint figyelmeztetések; a szerkezeti és frissességi problémák hibára futtatják a parancsot.

## co-op-translator-mcp

Futtasd a Co-op Translator MCP szervert ügynökök, szerkesztők és MCP-kompatibilis kliensek számára.

```bash
co-op-translator-mcp
```

A alapértelmezett szállító a `stdio`. Lásd az [MCP Server](mcp.md) útmutatót a kliens konfigurációhoz, eszközökhöz, erőforrásokhoz és biztonsági megjegyzésekhez.

### Opciók

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Újrafeldolgozza a lefordított Markdown fájlokat és frissíti a notebook linkeket, hogy szükség esetén a lefordított notebookokra mutassanak.

```bash
migrate-links -l "ko ja"
```

### Gyakori példák

Link frissítések előnézete:

```bash
migrate-links -l "ko" --dry-run
```

Minden támogatott nyelv feldolgozása megerősítés nélkül:

```bash
migrate-links -l "all" -y
```

Csak akkor írja át a linkeket, ha léteznek lefordított notebookok:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opciók

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--image-dir` | No | Translated image directory relative to the root. Defaults to `translated_images`. |
| `--dry-run` | No | Show files that would change without writing updates. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Use original notebook links when translated notebooks are missing. Enabled by default. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Auto-confirm prompts when processing all languages. |

## Környezet

Minden parancshoz szükség van legalább egy konfigurált LLM szolgáltatóra:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Vagy OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

A képfordításhoz emellett Azure AI Vision szükséges:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Kimeneti elrendezés

A szöveges fordítások az alábbi helyre kerülnek:

```text
translations/<language-code>/<original-path>
```

A lefordított képek kimenete az alábbi helyre kerül:

```text
translated_images/<language-code>/<original-path>
```

Például, ha a `README.md` és a `docs/setup.md` fájlokat koreai nyelvre fordítod, az így néz ki:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Beilleszthető CLI példák

Markdown fordítása három nyelvre:

```bash
translate -l "ko ja fr" -md
```

Csak notebookok fordítása:

```bash
translate -l "zh-CN" -nb
```

Csak képek fordítása:

```bash
translate -l "pt-BR" -img
```

Markdown fordítás előnézete fájlírás nélkül:

```bash
translate -l "de es" -md --dry-run
```

Alacsony bizalommal rendelkező Markdown fordítások javítása:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI-barát Markdown fordítás futtatása:

```bash
translate -l "ko ja" -md -y -s
```

A lefordított kimenet ellenőrzése:

```bash
co-op-review -l "ko ja"
```

Link migráció előnézete:

```bash
migrate-links -l "ko" --dry-run
```