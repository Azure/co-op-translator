# MCP szerver

A Co-op Translator tartalmaz egy Model Context Protocol szervert ügynökök, szerkesztők és MCP-kompatibilis kliensek számára.

Az alapértelmezett helyi beállításnál a felhasználóknak nem kell külön szervert kézzel futtatniuk. Beállítják MCP kliensüket, és a kliens automatikusan elindítja a `co-op-translator-mcp` folyamatot `stdio` felett, amikor szüksége van a Co-op Translator eszközeire.

Ha a CLI, a Python API és az MCP közül dönt, kezdje a [Válassza ki a munkafolyamatot](workflows.md) lappal.

Használja az MCP-t, amikor egy ügynöknek vagy szerkesztőnek közvetlenül kell hívnia a Co-op Translatort:

| Felhasználói cél | MCP eszközök |
| --- | --- |
| Fordítson le egy Markdown dokumentumot, jegyzetfüzetet (notebookot) vagy képet | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Fordítson Markdown-ot vagy notebook tartalmat a host ügynök modelljével | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Írja át a lefordított Markdown- vagy notebook-hivatkozásokat az output útvonal kiválasztása után | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Fordítson le egy teljes repozitóriumot, mint a CLI | `run_translation`, `translate_project` |
| Ellenőrizze a lefordított kimenetet LLM hitelesítő adatok nélkül | `run_review` |
| Ellenőrizze a képességeket és a környezeti állapotot | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Az MCP szerver a [Python API](api.md)-ban dokumentált ugyanezen publikus Python API-t burkolja. A szolgáltató által támogatott eszközök ugyanazokat a beállított szolgáltatókat használják, mint a CLI és a Python API. Az ügynök által segített eszközök darabokra bontják a tartalmat, amelyet az MCP host ügynök lefordít, majd a Co-op Translator segítségével rekonstruálják a végleges Markdown-t vagy notebookot.

## 1. lépés: A Co-op Translator telepítése és konfigurálása

Telepítse a Co-op Translatort abba a Python környezetbe, amelyet az MCP kliens használni fog:

```bash
pip install co-op-translator
```

Helyi fejlesztéshez ebből a repóból, telepítse a csomagot szerkeszthető módban:

```bash
pip install -e .
```

Válassza ki azt a fordítási módot, amelyet az MCP kliens használni fog:

| Mód | Ezt használd | Hitelesítési adatok |
| --- | --- | --- |
| Szolgáltató-támogatott | A Co-op Translator hívja a `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` vagy a `run_translation` függvényeket. | Markdown és notebook fordításhoz Azure OpenAI vagy OpenAI szükséges. Képfordításhoz emellett Azure AI Vision is szükséges. |
| Ügynök által segített | Az MCP host ügynök lefordítja a `start_markdown_agent_translation` vagy `start_notebook_agent_translation` által visszaadott darabokat. | Markdown vagy notebook darabokhoz nincs szükség Co-op Translator LLM szolgáltató hitelesítő adatokra. A képfordítás jelenleg még nincs lefedve az ügynök által segített módban. |

Ha ügynökben, például Codex vagy Claude Code környezetben kezdi a Markdown vagy notebook fordítást, kezdjen az ügynök által segített móddal. Használjon szolgáltató-támogatott módot, amikor azt szeretné, hogy maga a Co-op Translator hívja a konfigurált szolgáltatókat, amikor képeket fordít, vagy amikor repozitóriumszintű fordítást futtat, mint a CLI.

Állítsa be a szolgáltató hitelesítő adatokat csak a szolgáltató-támogatott munkafolyamatokhoz:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

A szolgáltató-támogatott képfordításhoz továbbiak szükségesek:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Az ügynök által segített mód jelenleg a Markdownot és a notebook Markdown-cella fordítását fedi le. A képfordítás továbbra is a szolgáltató-támogatott képfolyamatot használja, és OCR-hez és elrendezésérzékeny rendereléshez Azure AI Vision szükséges.

## 2. lépés: Az MCP kliens konfigurálása

A normál helyi `stdio` beállításhoz adja hozzá a Co-op Translatort az MCP kliens konfigurációjához. A kliens automatikusan elindítja és leállítja a folyamatot.

Telepített csomag konfiguráció:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Forráskód checkout konfiguráció Windows-on:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Forráskód checkout konfiguráció macOS-en vagy Linuxon:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

A MCP kliens konfigurációjának megváltoztatása után indítsa újra vagy töltse újra a klienst, hogy felfedezhesse az új szervert.

## 3. lépés: Ellenőrizze a szervert a kliensben

Kérje meg az MCP klienst, hogy sorolja fel az elérhető eszközöket, vagy hívjon meg először valamelyik csak-olvasási segédfüggvényt:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Hasznos első ellenőrzések:

| Eszköz | Mit ellenőrizzen |
| --- | --- |
| `get_api_overview` | Megerősíti, hogy a szerver elérhető és megmutatja az elérhető munkafolyamatokat. |
| `list_supported_languages` | Megerősíti, hogy a csomagolt nyelvi adatok betölthetők. |
| `get_configuration_status` | Megerősíti az LLM és Vision szolgáltatók elérhetőségét anélkül, hogy titkos értékeket fedne fel. |

## 4. lépés: Válasszon munkafolyamatot

### Egyedi fájlok vagy dokumentumok fordítása

Használja a szolgáltató-támogatott tartalmi eszközöket, amikor az MCP kliens már rendelkezik a dokumentum tartalmával vagy egy képútvonallal, és a Co-op Translatornek kell hívnia a konfigurált fordító szolgáltatókat.

Markdown esetén:

1. Hívja meg a `translate_markdown_content`-et a `document`, `language_code` és opcionálisan `source_path` paraméterekkel.
2. Ha a lefordított eredményt egy Co-op Translator kimeneti elrendezésbe írják, hívja meg a `rewrite_markdown_paths`-t.
3. Engedje, hogy a kliens írja vagy adja vissza a végső `content`-et.

Notebookok esetén:

1. Hívja meg a `translate_notebook_content`-et a jegyzetfüzet JSON-nal és a `language_code`-dal.
2. Hívja meg a `rewrite_notebook_paths`-t, ha a lefordított jegyzetfüzet hivatkozásait a célútvonalhoz kell igazítani.
3. Írja vagy adja vissza a végső jegyzetfüzet JSON-t.

Képek esetén:

1. Hívja meg a `translate_image_content`-et az `image_path`, `language_code` és opcionális `root_dir` vagy `fast_mode` paraméterekkel.
2. Olvassa be a visszaadott `data_base64` és `mime_type` értékeket.
3. Ha `output_path` meg van adva, a lefordított kép el is lesz mentve arra az útvonalra.

A tartalmi eszközök nem végeznek projektfelderítést, metaadat-frissítést, jogi felelősségkorlátozásokat vagy automatikus útvonal-átírást. Ha azt szeretné, hogy a host ügynök Co-op Translator LLM szolgáltató hitelesítő adatok nélkül fordítsa a Markdown-ot vagy notebook darabjait, használja az alábbi ügynök által segített munkafolyamatot.

### Fordítás a host ügynök modellel

Használja az ügynök által segített eszközöket, amikor azt szeretné, hogy a MCP host ügynök, például egy kódoló asszisztens, előállítsa a lefordított szöveget ahelyett, hogy Azure OpenAI-t vagy OpenAI-t konfigurálna a Co-op Translatorhoz.

Egy csevegő-alapú MCP kliensben általában nincs szükség arra, hogy maga írja az eszköz JSON-t. Kérje meg az ügynököt, hogy használja az ügynök által segített munkafolyamatot:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Notebookoknál ugyanazt a mintát alkalmazza:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ha az MCP kliens támogatja a szerver promptokat, használja az `agent_assisted_markdown_translation_prompt`-ot, hogy a kliens betöltse ugyanazokat a munkafolyamat-utasításokat.

Markdown esetén:

1. Hívja meg a `start_markdown_agent_translation`-t a `document`, `language_code` és opcionálisan `source_path` paraméterekkel.
2. Fordítsa le az egyes visszaadott darabokat a host ügynökben a darab `prompt`-ja szerint.
3. Hívja meg a `finish_markdown_agent_translation`-t az eredeti `job`-bal és a lefordított darabokkal a `chunk_id` és `translated_text` használatával.
4. Ha a tartalmat lefordított célútvonalra írják, hívja meg a `rewrite_markdown_paths`-t.

Notebookok esetén:

1. Hívja meg a `start_notebook_agent_translation`-t jegyzetfüzet JSON-nal és `language_code`-dal.
2. Fordítsa le az egyes visszaadott darabokat a host ügynökben.
3. Hívja meg a `finish_notebook_agent_translation`-t az eredeti `job`-bal és a lefordított darabokkal.
4. Hívja meg a `rewrite_notebook_paths`-t, ha a lefordított jegyzetfüzet hivatkozásait a célútvonalhoz kell igazítani.

Az ügynök által segített eszközök nem hívják az Azure OpenAI-t vagy OpenAI-t a Co-op Translatorból. A host ügynök a felelős a visszaadott darabok lefordításáért. A Co-op Translator kezeli a Markdown darabolást, a helyőrzők megőrzését, a frontmatter rekonstruálását, a notebook cellák cseréjét és az utó-fordítás normalizálását.

### Egy teljes repozitórium fordítása

Használja a `run_translation`-t, amikor a felhasználó azt szeretné, hogy a Co-op Translator úgy viselkedjen, mint a `translate` CLI.

A repozitórium fordítás alapértelmezés szerint `dry_run=true`, hogy egy ügynök megvizsgálhassa a hatókört a fájlok módosítása előtt:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Az írások engedélyezéséhez a hívónak mindkét `dry_run=false` és `confirm_write=true` értéket be kell állítania:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

A `translate_project` kompatibilitási alias a `run_translation`-höz.

### A lefordított kimenet áttekintése

Használja a `run_review`-t determinisztikus ellenőrzésekhez, amelyekhez nem szükséges LLM vagy Vision hitelesítő adat:

!!! note "Beta"
    Az MCP kiteszi a béta `run_review` API-t. Biztonságos csak-olvasási felülvizsgálati munkafolyamatokhoz, de a felülvizsgálati ellenőrzések és a hibasémák változhatnak.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Az eredmény tartalmazza a rögzített szöveges kimenetet és egy strukturált felülvizsgálati összefoglalót, ha elérhető.

## Kézi szerverfuttatások

A kézi futtatások elsősorban hibakeresésre vagy olyan szállításokra valók, amelyek hosszú életű szerverként viselkednek.

Hibakeresés az alapértelmezett stdio szervernél:

```bash
co-op-translator-mcp
```

Futtatás forráskódból:

```bash
python -m co_op_translator.mcp.server
```

Hosszú életű HTTP vagy SSE szerver futtatása:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Helyi szerkesztő- és ügynökintegrációkhoz előnyben részesítse a 2. lépésben említett kliens által kezelt `stdio` konfigurációt.

## Eszközök

| Eszköz | Célja | Fájlokat ír |
| --- | --- | --- |
| `translate_markdown_content` | Egy Markdown karakterlánc fordítása. | Nem |
| `translate_notebook_content` | Markdown cellák fordítása jegyzetfüzet JSON-ben. | Nem |
| `translate_image_content` | Szöveg fordítása egy képen és base64 képadat visszaadása. | Opcionális, csak ha `output_path` meg van adva |
| `start_markdown_agent_translation` | Markdown darabok előkészítése a host ügynök számára Co-op Translator LLM hitelesítők nélkül. | Nem |
| `finish_markdown_agent_translation` | Markdown rekonstruálása a host-ügynök által lefordított darabokból. | Nem |
| `start_notebook_agent_translation` | Notebook Markdown-cella darabok előkészítése a host ügynök számára fordításhoz. | Nem |
| `finish_notebook_agent_translation` | Notebook JSON rekonstruálása a host-ügynök által lefordított darabokból. | Nem |
| `rewrite_markdown_paths` | Markdown törzs és frontmatter útvonalak átírása egy lefordított célhoz. | Nem |
| `rewrite_notebook_paths` | Útvonalak átírása notebook Markdown cellákon belül. | Nem |
| `run_translation` | Projekt-szintű fordítás futtatása, mint a CLI. | Igen, ha `dry_run=false` és `confirm_write=true` |
| `translate_project` | Kompatibilitási alias a `run_translation`-höz. | Igen, ha `dry_run=false` és `confirm_write=true` |
| `run_review` | Determinisztikus felülvizsgálati ellenőrzések futtatása. | Nem |
| `get_configuration_status` | A beállított LLM és Vision szolgáltatók jelentése titkok nélkül. | Nem |
| `list_supported_languages` | A támogatott cél nyelvi kódok listázása. | Nem |
| `get_api_overview` | Az elérhető MCP munkafolyamatok és eszközök leírása. | Nem |

## Erőforrások

| Resource URI | Cél |
| --- | --- |
| `co-op://api` | A munkafolyamatok és eszközök JSON áttekintése. |
| `co-op://supported-languages` | A támogatott nyelvi kódok JSON listája. |
| `co-op://configuration` | A szolgáltató elérhetőségének összefoglalója titkok nélkül. |

## Promptok

| Prompt | Cél |
| --- | --- |
| `translate_markdown_document_prompt` | Útmutatás egy MCP kliens számára tartalomfordításhoz és opcionális útvonal-átíráshoz. |
| `agent_assisted_markdown_translation_prompt` | Útmutatás egy MCP kliens számára host-ügynök Markdown fordításhoz Co-op Translator LLM szolgáltató hitelesítők nélkül. |
| `translate_repository_prompt` | Útmutatás egy MCP kliens számára, hogy először dry-run módon vizsgálja át a repozitórium fordítását. |

## Beilleszthető példák

Markdown tartalom fordítása:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Lefordított Markdown hivatkozások átírása:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Markdown fordítása a host ügynök modellel:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Miután a host ügynök lefordította az egyes visszaadott darabokat, fejezze be a munkát az `start_markdown_agent_translation` által visszaadott teljes `job` objektummal:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Repozitórium fordításának előnézete:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Hibakeresés

| Probléma | Mit próbáljon |
| --- | --- |
| Az MCP kliens nem találja a `co-op-translator-mcp`-t. | Használja az abszolút Python futtatható útvonalát és a `["-m", "co_op_translator.mcp.server"]` forráskód checkout konfigurációt. |
| A szerver szerepel a listában, de a fordítás sikertelen. | Hívja meg a `get_configuration_status`-t és erősítse meg, hogy van elérhető LLM szolgáltató. |
| Markdown vagy notebook fordítást szeretne Azure OpenAI/OpenAI kulcsok nélkül. | Használja a `start_markdown_agent_translation` / `finish_markdown_agent_translation` vagy a notebook megfelelőiket, hogy a host ügynök fordítsa a darabokat. |
| A képfordítás sikertelen. | Ellenőrizze, hogy az Azure AI Vision változók be vannak-e állítva, és hívja meg a `get_configuration_status`-t. |
| A repozitórium fordítása nem ír fájlokat. | Állítsa be a `dry_run=false` és `confirm_write=true` értékeket csak a felhasználó kifejezett jóváhagyása után. |
| A kliens konfigurációjának módosításai nem jelennek meg. | Indítsa újra vagy töltse újra az MCP klienst. |

## Biztonsági megjegyzések

- Az MCP eszközhívásokat a host alkalmazás modellje vezérli, ezért a repozitórium fordítása alapértelmezés szerint dry-run.
- A teljes repozitórium fordítása sok fájl létrehozásával, frissítésével vagy eltávolításával járhat. Kérjen kifejezett felhasználói jóváhagyást, mielőtt a `confirm_write=true`-t beállítja.
- A konfigurációs állapot eszköz soha nem ad vissza API kulcsokat, végpontokat vagy más titkos értékeket.
- A képfordítás base64 képadatot ad vissza. Nagy képek nagy eszközválaszokat eredményezhetnek.
- Az ügynök által segített eszközök forrásdarabokat és promptokat adnak vissza az MCP hostnak. Csak olyan tartalommal használja őket, amelyet a felhasználó kényelmesen megoszt a host ügynök modelljével.