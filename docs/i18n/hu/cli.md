# CLI referencia

A Co-op Translator a következő parancssori belépési pontokat telepíti:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

A `translate`, `evaluate`, `migrate-links` és `co-op-review` parancsok a `co_op_translator.__main__`-en keresztül kerülnek továbbításra, amely a meghívott script neve alapján választja ki a parancs megvalósítását. Az MCP szerver közvetlenül a `co_op_translator.mcp.server`-t használja.

Ha a CLI, a Python API és az MCP között dönt, kezdje a [Munkafolyamat kiválasztása](workflows.md) oldallal.

## Konzol kimenet

Az interaktív terminálok Rich formázást használnak a parancsfejléc, a folyamatjelző és az összegzések megjelenítéséhez. A CI és nem interaktív kimenet automatikusan egyszerű szövegre esik vissza.

Állítsa be a `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` értéket az egyszerű kimenet kényszerítéséhez, vagy `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` értéket a Rich kimenet kényszerítéséhez. Állítsa be a `CO_OP_TRANSLATOR_NO_PROGRESS=1`-et az összegzések megtartásához, miközben az élő folyamatjelző sávokat elnyomja.

Használja a `translate --json-events progress.ndjson` parancsot, amikor egy másik rendszer géppel olvasható előrehaladást igényel.
A CLI továbbra is ember számára olvasható kimenetet jelenít meg, míg
az NDJSON fájl verziózott `co-op.translation.event.v1` eseményeket kap
olyan stabil mezőkkel, mint a `type`, `stage_key`, `completed`, `total` és
`current_path`.

## Első CLI használat

Itt kezdje, ha terminálból használja a Co-op Translatort:

1. Konfiguráljon egy LLM-szolgáltatót az [Konfiguráció](configuration.md) leírás szerint.
2. Válassza ki a lefordítani kívánt tartalomtípust.
3. Először futtasson egy fókuszált parancsot, például csak Markdown fordítást.
4. Használja a `--dry-run` opciót nagy tárhely-változtatások előtt.
5. A fordítást követően használja a `co-op-review`-t a struktúra és frissesség ellenőrzéséhez.

| Cél | Kezdő parancs |
| --- | --- |
| Markdown dokumentumok fordítása | `translate -l "ko" -md` |
| Notebookok fordítása | `translate -l "ko" -nb` |
| Képszöveg fordítása | `translate -l "ko" -img` |
| Munka előnézete fájlok írása nélkül | `translate -l "ko" -md --dry-run` |
| Meglévő fordítások felülvizsgálata | `co-op-review -l "ko"` |
| Jegyzetfüzetek és Markdown hivatkozások frissítése | `migrate-links -l "ko" --dry-run` |
| Eszközök elérhetővé tétele egy MCP kliens számára | Ahelyett, hogy közvetlenül CLI parancsokat futtatna, konfigurálja a [MCP szerver](mcp.md)-t. |

## translate

Fordítsa le a Markdown fájlokat, notebookokat és képszöveget egy vagy több célnyelvre.

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

Meglévő fordítások frissítése azok törlésével és újra létrehozásával:

```bash
translate -l "ko" -u
```

Interaktív kérdések nélkül futtatás:

```bash
translate -l "ko ja" -md -y
```

Naplók mentése:

```bash
translate -l "ko" -s
```

Strukturált előrehaladás események írása:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Opciók

| Opció | Kötelező | Leírás |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Szóközzel elválasztott nyelvkódok, például `"es fr de"`, vagy `"all"`. |
| `-r`, `--root-dir` | No | Projekt gyökérkönyvtár. Alapértelmezés a jelenlegi könyvtár. |
| `-u`, `--update` | No | Törli a kiválasztott nyelvek meglévő fordításait és újra létrehozza azokat. |
| `-img`, `--images` | No | Csak képfájlok fordítása. |
| `-md`, `--markdown` | No | Csak Markdown fájlok fordítása. |
| `-nb`, `--notebook` | No | Csak Jupyter notebook fájlok fordítása. |
| `-d`, `--debug` | No | Engedélyezi a hibakeresési naplózást a konzolon. |
| `-s`, `--save-logs` | No | DEBUG szintű naplókat menti a `<root-dir>/logs/` alá. |
| `--json-events` | No | Géppel olvasható fordítási előrehaladási eseményeket ír NDJSON formátumban. |
| `-x`, `--fix` | No | Alacsony megbízhatóságú Markdown fájlok újrafordítása korábbi értékelési eredmények alapján. |
| `-c`, `--min-confidence` | No | Megbízhatósági küszöb a `--fix` számára. Alapértelmezés `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Gépi fordítással kapcsolatos felelősségkizárás hozzáadása vagy elnyomása. A CLI-ben alapértelmezés szerint engedélyezve. |
| `-f`, `--fast` | No | Elavult gyors kép mód. |
| `-y`, `--yes` | No | Automatikusan megerősíti a kéréseket, hasznos CI-ben. |
| `--repo-url` | No | A README nyelvi táblázat sparse-checkout tanácsában használt tárhely URL. |
| `--migrate-language-folders` | No | Régi alias mappák átnevezése, mint például `cn` vagy `tw`, kanonikus BCP 47 mappákra. |
| `--dry-run` | No | Nyelvi mappa áthelyezés és fordítási becslések előnézete fájlok írása nélkül. |

Ha nincs megadva típus kapcsoló, a `translate` feldolgozza a Markdown fájlokat, notebookokat és képeket. A képfordításhoz Azure AI Vision konfiguráció szükséges.

## evaluate

Egy nyelvhez készült Markdown fordítások minőségének értékelése.

!!! warning "Kísérleti"
    `evaluate` kísérleti. Használhat szabály-alapú és LLM-alapú minőségellenőrzéseket, az értékelési eredményeket a fordítás metaadataiba írja, és a pontozási modellje valamint a metaadat viselkedése változhat.

```bash
evaluate -l "ko"
```

### Gyakori példák

Használjon szigorúbb alacsony-megbízhatósági küszöböt:

```bash
evaluate -l "es" -c 0.8
```

Csak szabály-alapú ellenőrzések futtatása:

```bash
evaluate -l "fr" -f
```

Csak LLM-alapú ellenőrzések futtatása:

```bash
evaluate -l "ja" -D
```

### Opciók

| Opció | Kötelező | Leírás |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Egy nyelvkód, amelyet értékelni kell. Az alias kódok normalizálásra kerülnek. |
| `-r`, `--root-dir` | No | Projekt gyökérkönyvtár. Alapértelmezés a jelenlegi könyvtár. |
| `-c`, `--min-confidence` | No | A küszöb, amelyet az alacsony megbízhatóságú fordítások listázásakor használnak. Alapértelmezés `0.7`. |
| `-d`, `--debug` | No | Hibakeresési naplózás engedélyezése. |
| `-s`, `--save-logs` | No | DEBUG szintű naplókat menti a `<root-dir>/logs/` alá. |
| `-f`, `--fast` | No | Csak szabály-alapú értékelés. |
| `-D`, `--deep` | No | Csak LLM-alapú értékelés. |

Alapértelmezésben az `evaluate` egyszerre használ szabály-alapú és LLM-alapú értékelést. Az eredményeket a fordítás metaadataiba írja és összegzi a konzolon.

## co-op-review

Determinisztikus fordítás-karbantartási ellenőrzések futtatása API hitelesítési adatok nélkül.

!!! note "Béta"
    `co-op-review` egy béta determinisztikus felülvizsgáló parancs. Nem hív modell szolgáltatókat, és nem ír fájlokat, de az ellenőrzései és a problémák kimeneti sémája változhat.

```bash
co-op-review -l "ko"
```

### Gyakori példák

Koreai és japán fordítások felülvizsgálata a jelenlegi könyvtárból:

```bash
co-op-review -l "ko ja"
```

Egy konkrét projekt gyökérkönyvtár felülvizsgálata:

```bash
co-op-review -l "fr" -r ./my-course
```

Csak a README felülvizsgálata README-only fordítás után:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` figyelmen kívül hagyja a többi dokumentumot és az egymásba ágyazott README-ket. Sikertelen lesz, ha a gyökér
`README.md` hiányzik. A `--changed-from`-mal kombinálva csak akkor vizsgálja a README-t, ha a forrásfájl megváltozott. A README-only fordítás érintetlenül hagyja a forrás README-t, beleértve az esetleges megosztott szakasz jelölőket is.



Csak a bázis referencia ellenében megváltozott forrásfájlok felülvizsgálata:

```bash
co-op-review -l "ko" --changed-from origin/main
```

GitHub-stílusú Markdown kimenet nyomtatása CI összegzésekhez:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opciók

| Opció | Kötelező | Leírás |
| --- | --- | --- |
| `-l`, `--language-code` | No | A felülvizsgálandó nyelvkód. Többször is megadható, vagy szóközzel elválasztott értékként. Alapértelmezésben az összes felismert fordítási nyelv. |
| `-r`, `--root-dir` | No | Projekt gyökérkönyvtár. Alapértelmezés a jelenlegi könyvtár. |
| `--changed-from` | No | Git ref, amelyet a felülvizsgálat korlátozására használnak a megváltozott forrásfájlokra. |
| `--readme-only` | No | Csak a gyökér `README.md` fordításának felülvizsgálata. |
| `--format` | No | Kimeneti formátum: `text` vagy `github`. Alapértelmezés `text`. |

`co-op-review` jelenleg ellenőrzi a hiányzó lefordított fájlokat, hiányzó vagy elavult fordítási metaadatokat, a Markdown frontmatter és kódkorlátok integritását, az érvénytelen lefordított notebook JSON-t, valamint a hiányzó helyi Markdown vagy kép hivatkozások célpontjait. A hiányzó hivatkozások alapértelmezés szerint figyelmeztetések; a szerkezeti és frissességi problémák meghiúsítják a parancsot.

## co-op-translator-mcp

A Co-op Translator MCP szerver futtatása ügynökök, szerkesztők és MCP-kompatibilis kliensek számára.

```bash
co-op-translator-mcp
```

Az alapértelmezett transzport a `stdio`. A kliens konfigurációjához, eszközökhöz, forrásokhoz és biztonsági megjegyzésekhez lásd a [MCP szerver](mcp.md) útmutatót.

### Opciók

| Opció | Kötelező | Leírás |
| --- | --- | --- |
| `--transport` | No | MCP transzport: `stdio`, `streamable-http`, vagy `sse`. Alapértelmezés `stdio`. |

## migrate-links

A lefordított Markdown fájlok újrafeldolgozása és a notebook hivatkozások frissítése úgy, hogy lefordított notebookokra mutassanak, ha azok elérhetők.

```bash
migrate-links -l "ko ja"
```

### Gyakori példák

Hivatkozás-frissítések előnézete:

```bash
migrate-links -l "ko" --dry-run
```

Az összes támogatott nyelv feldolgozása megerősítés nélkül:

```bash
migrate-links -l "all" -y
```

Csak akkor írja át a hivatkozásokat, ha léteznek lefordított notebookok:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opciók

| Opció | Kötelező | Leírás |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Szóközzel elválasztott nyelvkódok, vagy `"all"`. |
| `-r`, `--root-dir` | No | Projekt gyökérkönyvtár. Alapértelmezés a jelenlegi könyvtár. |
| `--image-dir` | No | A lefordított képek könyvtára a gyökérhez viszonyítva. Alapértelmezés `translated_images`. |
| `--dry-run` | No | Megmutatja a megváltoztatandó fájlokat anélkül, hogy frissítéseket írna. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Az eredeti notebook hivatkozások használata, ha a lefordított notebookok hiányoznak. Alapértelmezés szerint engedélyezve. |
| `-d`, `--debug` | No | Hibakeresési naplózás engedélyezése. |
| `-s`, `--save-logs` | No | DEBUG szintű naplókat menti a `<root-dir>/logs/` alá. |
| `-y`, `--yes` | No | Automatikusan megerősíti a kéréseket, amikor az összes nyelvet dolgozza fel. |

## Környezet

Ha egy parancs szolgáltató hitelesítő adatokat igényel, konfiguráljon az alábbi szolgáltató készletek egyikét. A `translate --dry-run` és a `co-op-review` nem igényel szolgáltató hitelesítő adatokat:

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

# Vagy Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

A képfordításhoz emellett Azure AI Vision konfiguráció szükséges:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Kimeneti elrendezés

A szövegfordítások ide íródnak:

```text
translations/<language-code>/<original-path>
```

A lefordított képek kimenete ide íródik:

```text
translated_images/<language-code>/<original-path>
```

Például a `README.md` és a `docs/setup.md` koreaira fordítása a következőt eredményezi:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Másolható CLI példák

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

Markdown fordítás előnézete fájlok írása nélkül:

```bash
translate -l "de es" -md --dry-run
```

Alacsony megbízhatóságú Markdown fordítások javítása:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

CI-barát Markdown fordítás futtatása:

```bash
translate -l "ko ja" -md -y -s
```

A lefordított kimenet felülvizsgálata:

```bash
co-op-review -l "ko ja"
```

Hivatkozás migráció előnézete:

```bash
migrate-links -l "ko" --dry-run
```