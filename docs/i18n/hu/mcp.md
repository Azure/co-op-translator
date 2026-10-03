# MCP szerver

A Co-op Translator tartalmaz egy Model Context Protocol szervert ügynököknek, szerkesztőknek és MCP-kompatibilis klienseknek.

Az alapértelmezett helyi beállításnál a felhasználóknak nem kell külön szervert kézzel futtatniuk. Beállítják MCP kliensüket, és a kliens automatikusan elindítja a `co-op-translator-mcp`-t a `stdio` fölött, amikor szüksége van a Co-op Translator eszközeire.

Ha a CLI, a Python API és az MCP között dönt, kezdje a [Válassza ki a munkafolyamatot](workflows.md) oldallal.

Használja az MCP-t, amikor egy ügynöknek vagy szerkesztőnek közvetlenül kell meghívnia a Co-op Translatort:

| Felhasználói cél | MCP eszközök |
| --- | --- |
| Egy Markdown-dokumentum, jegyzetfüzet vagy kép lefordítása | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Markdown- vagy jegyzetfüzet-tartalom fordítása a hoszt ügynök modelljével | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| A lefordított Markdown- vagy jegyzetfüzet-hivatkozások átírása a kimeneti útvonal kiválasztása után | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Egy teljes tároló fordítása, mint a CLI | `run_translation`, `translate_project` |
| A lefordított kimenet áttekintése LLM-hitelesítő adatok nélkül | `run_review` |
| Képességek és környezeti állapot ellenőrzése | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Az MCP szerver ugyanazt a publikus Python API-t csomagolja, amely a [Python API](api.md) dokumentációban található. A szolgáltató-alapú eszközök ugyanazokat a beállított szolgáltatókat használják, mint a CLI és a Python API. Az ügynöksegített eszközök darabokat készítenek elő az MCP hosztügynök számára fordításhoz, majd a Co-op Translator segítségével rekonstruálják a végső Markdown-t vagy jegyzetfüzetet.

## 1. lépés: Telepítse és konfigurálja a Co-op Translatort

Telepítse a Co-op Translatort abba a Python-környezetbe, amelyet az MCP kliens használni fog:

```bash
pip install co-op-translator
```

Helyi fejlesztéshez ebből a tárolóból telepítse a csomagot szerkeszthető módban:

```bash
pip install -e .
```

Válassza ki azt a fordítási módot, amelyet az MCP kliens fog használni:

| Mód | Mire használható | Hitelesítő adatok |
| --- | --- | --- |
| Szolgáltató-alapú | A Co-op Translator meghívja a `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` vagy a `run_translation` függvényt. | A fordításhoz Azure OpenAI, OpenAI vagy Anthropic szükséges. A képfordításhoz továbbá Azure AI Vision is szükséges. |
| Ügynöksegített | Az MCP hosztügynök fordítja azokat a darabokat, amelyeket a `start_markdown_agent_translation` vagy a `start_notebook_agent_translation` ad vissza. | A Markdown- vagy jegyzetfüzet-darabokhoz nem szükséges Co-op Translator LLM-szolgáltató hitelesítő adat. A képfordítás még nem támogatott az ügynöksegített módban. |

Ha egy ügynökben, például Codexben vagy Claude Code-ban kezdi a Markdown- vagy jegyzetfüzet-fordítást, kezdje az ügynöksegített móddal. Használja a szolgáltató-alapú módot, ha azt szeretné, hogy maga a Co-op Translator hívja meg a beállított szolgáltatókat, ha képeket fordít, vagy ha tárolószintű fordítást futtat, mint a CLI.

Állítson be egy szolgáltatót a szolgáltató-alapú munkafolyamatokhoz:

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

A szolgáltató-alapú képfordításhoz emellett szükség van:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Az ügynök által segített mód jelenleg a Markdown és a notebook Markdown celláira terjed ki. A képek fordítása továbbra is a szolgáltató által támogatott kép-pipeline-t használ, és OCR-hez, valamint az elrendezés-érzékeny rendereléshez Azure AI Visiont igényel.

## 2. lépés: Konfigurálja az MCP kliensét

A normál helyi `stdio`-beállításnál adja hozzá a Co-op Translatort az MCP kliens konfigurációjához. A kliens automatikusan elindítja és leállítja a folyamatot.

Telepített csomag konfigurációja:

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

Forráskivétel konfiguráció Windows rendszeren:

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

Forráskivétel konfiguráció macOS-en vagy Linuxon:

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

Az MCP kliens konfigurációjának megváltoztatása után indítsa újra vagy töltse újra a klienst, hogy felfedezhesse az új szervert.

## 3. lépés: Ellenőrizze a szervert a kliensben

Kérje meg az MCP klienst, hogy sorolja fel az elérhető eszközöket, vagy először hívjon meg egyet a csak-olvasású segédfüggvények közül:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Hasznos első ellenőrzések:

| Eszköz | Mit ellenőrizzen |
| --- | --- |
| `get_api_overview` | Megerősíti, hogy a szerver elérhető, és megmutatja az elérhető munkafolyamatokat. |
| `list_supported_languages` | Megerősíti, hogy a csomagolt nyelvi adatok betölthetők. |
| `get_configuration_status` | Megerősíti az LLM és Vision szolgáltatók elérhetőségét anélkül, hogy titkos értékeket fedne fel. |

## 4. lépés: Válasszon munkafolyamatot

### Egyedi fájlok vagy dokumentumok fordítása

Használja a szolgáltató-alapú tartalmi eszközöket, ha az MCP kliens már rendelkezik a dokumentum tartalmával vagy egy képelérési útvonallal, és a Co-op Translatornek kell meghívnia a beállított fordítószolgáltatókat.

Markdown esetén:

1. Hívja meg a `translate_markdown_content` függvényt a `document`, `language_code` és opcionálisan a `source_path` paraméterekkel.
2. Ha a lefordított eredményt a Co-op Translator kimeneti elrendezésébe írják, hívja meg a `rewrite_markdown_paths` függvényt.
3. Hagyja, hogy a kliens írja vagy adja vissza a végső `content` értékét.

For notebooks:

1. Hívja meg a `translate_notebook_content` függvényt a jegyzetfüzet JSON-jával és a `language_code` paraméterrel.
2. Hívja meg a `rewrite_notebook_paths` függvényt, ha a lefordított jegyzetfüzet-hivatkozásokat a célútvonalhoz kell igazítani.
3. Írja ki, vagy adja vissza a végső jegyzetfüzet JSON-t.

Képek esetén:

1. Hívja meg a `translate_image_content` függvényt az `image_path`, `language_code`, és opcionális `root_dir` vagy `fast_mode` paraméterekkel.
2. Olvassa be a visszaadott `data_base64` és `mime_type` értékeket.
3. Ha meg van adva az `output_path`, a lefordított kép el is mentésre kerül erre az útvonalra.

A tartalmi eszközök nem végeznek projektfelderítést, metaadat-frissítéseket, felelősségkizárásokat vagy automatikus útvonal-átírást. Ha azt szeretné, hogy a hosztügynök a Markdown- vagy jegyzetfüzet-darabokat Co-op Translator LLM szolgáltató hitelesítő adatok nélkül fordítsa le, használja az alábbi ügynöksegített munkafolyamatot.

### Fordítás a hosztügynök modelljével

Használja az ügynöksegített eszközöket, amikor azt szeretné, hogy az MCP hosztügynök, például egy kódoló asszisztens állítsa elő a lefordított szöveget ahelyett, hogy Co-op Translator számára LLM szolgáltatót konfigurálna.

Egy chat-alapú MCP kliensben általában nincs szükség arra, hogy maga írja meg az eszköz JSON-ját. Kérje meg az ügynököt, hogy használja az ügynöksegített munkafolyamatot:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Jegyzetfüzeteknél alkalmazza ugyanazt a mintát:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ha az MCP kliens támogatja a szerver-promptokat, használja az `agent_assisted_markdown_translation_prompt`-ot, hogy a kliens betöltse ugyanazokat a munkafolyamat-utasításokat.

Markdown esetén:

1. Hívja meg a `start_markdown_agent_translation` függvényt a `document`, `language_code`, és opcionálisan a `source_path` paraméterekkel.
2. Fordítsa le a hosztügynökben a visszaadott darabokat a bennük található `prompt` alapján.
3. Hívja meg a `finish_markdown_agent_translation` függvényt az eredeti `job`-bal és a lefordított darabokkal, megadva a `chunk_id`-t és a `translated_text`-et.
4. Ha a tartalom egy lefordított célútvonalra kerül írásra, hívja meg a `rewrite_markdown_paths`-t.

For notebooks:

1. Hívja meg a `start_notebook_agent_translation` függvényt a jegyzetfüzet JSON-jával és a `language_code` paraméterrel.
2. Fordítsa le a visszaadott darabokat a hosztügynökben.
3. Hívja meg a `finish_notebook_agent_translation` függvényt az eredeti `job`-bal és a lefordított darabokkal.
4. Hívja meg a `rewrite_notebook_paths`-t, ha a lefordított jegyzetfüzet-hivatkozásokat a célútvonalhoz kell igazítani.

Az ügynöksegített eszközök nem hívják a Co-op Translatorhoz konfigurált LLM szolgáltatót. A hosztügynök felelős a visszaadott darabok lefordításáért. A Co-op Translator kezeli a Markdown darabolását, a helykitöltők megőrzését, a frontmatter rekonstruálását, a jegyzetfüzet-cella cseréjét és a fordítás utáni normalizációt.

### Egy teljes tároló fordítása

Használja a `run_translation` függvényt, ha a felhasználó azt szeretné, hogy a Co-op Translator a `translate` CLI-hez hasonlóan viselkedjen.

A tárolófordítás alapértelmezés szerint `dry_run=true`, így egy ügynök át tudja tekinteni a terjedelmet a fájlmódosítások előtt:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

A `run_translation` eredménye tartalmaz egy `events` tömböt verziózott
`co-op.translation.event.v1` előrehaladási eseményekkel. Az MCP klienseknek a
`type`, `stage_key`, `completed`, `total` és `current_path` mezőket kell használniuk az
rögzített konzol szövegének elemzése helyett. Adja meg a `json_events_path`-ot, ha az eseményeket
NDJSON fájlba is szeretné írni.

Az írások engedélyezéséhez a hívónak mindkettőt be kell állítania: `dry_run=false` és `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

A `translate_project` kompatibilitási aliaszként érhető el a `run_translation` számára.

### A lefordított kimenet áttekintése

Használja a `run_review`-t determinisztikus ellenőrzésekhez, amelyek nem igényelnek LLM vagy Vision hitelesítő adatokat:

!!! note "Beta"
    Az MCP a béta `run_review` API-t teszi elérhetővé. Ez biztonságos csak-olvasási áttekintési munkafolyamatokhoz, de az ellenőrzések és a hibasémák változhatnak.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Az eredmény tartalmazza a rögzített szöveges kimenetet és egy strukturált áttekintési összefoglalót, ha elérhető.

## Kézi szerver futtatások

A kézi futtatások elsősorban hibakereséshez vagy olyan transzportokhoz valók, amelyek hosszú ideig futó szerverként viselkednek.

A alapértelmezett stdio szerver hibakeresése:

```bash
co-op-translator-mcp
```

Futtatás forráskivételből:

```bash
python -m co_op_translator.mcp.server
```

Hosszú élettartamú HTTP vagy SSE szerver futtatása:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Helyi szerkesztő- és ügynökintegrációkhoz részesítse előnyben a 2. lépésben szereplő kliens által kezelt `stdio` konfigurációt.

## Eszközök

| Eszköz | Cél | Fájlokat ír |
| --- | --- | --- |
| `translate_markdown_content` | Egy Markdown szöveg lefordítása. | Nem |
| `translate_notebook_content` | Markdown cellák fordítása a jegyzetfüzet JSON-jában. | Nem |
| `translate_image_content` | Egy képben található szöveg fordítása és base64 képadat visszaadása. | Opcionális, csak ha meg van adva az `output_path` |
| `start_markdown_agent_translation` | Markdown darabok előkészítése a hosztügynök számára fordításhoz Co-op Translator LLM hitelesítő adatok nélkül. | Nem |
| `finish_markdown_agent_translation` | Markdown rekonstruálása a hosztügynök által lefordított darabokból. | Nem |
| `start_notebook_agent_translation` | Jegyzetfüzet Markdown-celláinak darabjainak előkészítése a hosztügynök számára fordításhoz. | Nem |
| `finish_notebook_agent_translation` | Jegyzetfüzet JSON rekonstruálása a hosztügynök által lefordított darabokból. | Nem |
| `rewrite_markdown_paths` | A Markdown törzsének és frontmatter útvonalainak átírása a lefordított célhoz. | Nem |
| `rewrite_notebook_paths` | Útvonalak átírása a jegyzetfüzet Markdown celláin belül. | Nem |
| `run_translation` | Projekt szintű fordítás futtatása, mint a CLI. | Igen, amikor `dry_run=false` és `confirm_write=true` |
| `translate_project` | Kompatibilitási alias a `run_translation` számára. | Igen, amikor `dry_run=false` és `confirm_write=true` |
| `run_review` | Determinisztikus ellenőrzések futtatása. | Nem |
| `get_configuration_status` | Jelenti a beállított LLM és Vision szolgáltatók elérhetőségét anélkül, hogy titkokat felfedne. | Nem |
| `list_supported_languages` | Támogatott célnyelv kódok listázása. | Nem |
| `get_api_overview` | Az elérhető MCP munkafolyamatok és eszközök leírása. | Nem |

## Erőforrások

| Erőforrás URI | Cél |
| --- | --- |
| `co-op://api` | JSON áttekintés a munkafolyamatokról és eszközökről. |
| `co-op://supported-languages` | JSON lista a támogatott nyelvkódokról. |
| `co-op://configuration` | JSON összefoglaló a szolgáltatók elérhetőségéről titkok nélkül. |

## Promptok

| Prompt | Cél |
| --- | --- |
| `translate_markdown_document_prompt` | Útmutatás egy MCP kliens számára a tartalom fordításához és az opcionális útvonal-átíráshoz. |
| `agent_assisted_markdown_translation_prompt` | Útmutatás egy MCP kliens számára a hosztügynök által végzett Markdown-fordításhoz Co-op Translator LLM szolgáltatói hitelesítő adatok nélkül. |
| `translate_repository_prompt` | Útmutatás egy MCP kliens számára a dry-run első tárolófordításhoz. |

## Másolás-beillesztés példák

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

A lefordított Markdown-hivatkozások átírása:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

Markdown fordítása a hosztügynök modelljével:

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

Miután a hosztügynök lefordította az egyes visszaadott darabokat, fejezze be a munkát a `start_markdown_agent_translation` által visszaadott teljes `job` objektummal:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Tárolófordítás előnézete:

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

| Probléma | Mit próbáljon meg |
| --- | --- |
| Az MCP kliens nem találja a `co-op-translator-mcp`. | Használja a Python végrehajtható fájl abszolút útvonalát és a `["-m", "co_op_translator.mcp.server"]` forráskivétel konfigurációt. |
| A szerver listázva van, de a fordítás meghiúsul. | Hívja meg a `get_configuration_status`-t és ellenőrizze, hogy elérhető-e LLM szolgáltató. |
| Markdown- vagy jegyzetfüzet-fordítást szeretne szolgáltató-hitelesítő adatok nélkül. | Használja a `start_markdown_agent_translation` / `finish_markdown_agent_translation`-t vagy a jegyzetfüzet megfelelőit, hogy a hosztügynök fordítsa le a darabokat. |
| A képfordítás meghiúsul. | Ellenőrizze, hogy az Azure AI Vision változók be vannak-e állítva, és hívja meg a `get_configuration_status`-t. |
| A tárolófordítás nem ír fájlokat. | Állítsa be a `dry_run=false` és a `confirm_write=true` értékeket csak a felhasználó kifejezett jóváhagyása után. |
| A kliens konfigurációjának változásai nem jelennek meg. | Indítsa újra vagy töltse újra az MCP klienst. |

## Biztonsági megjegyzések

- Az MCP eszközmeghívásokat a hoszt alkalmazás vezérli, ezért a tárolófordítás alapértelmezés szerint dry-run módban van.
- A teljes tároló fordítása sok fájlt hozhat létre, frissíthet vagy törölhet. Kérjen kifejezett felhasználói jóváhagyást, mielőtt beállítaná a `confirm_write=true`-t.
- A konfigurációs állapot eszköz soha nem ad vissza API-kulcsokat, végpontokat vagy más titkos értékeket.
- A képfordítás base64 képadatot ad vissza. Nagy képek nagy eszközválaszokat eredményezhetnek.
- Az ügynöksegített eszközök forrásdarabokat és promptokat adnak vissza az MCP hosztnak. Csak olyan tartalom esetén használja őket, amelyet a felhasználó kényelmesen megoszt a hosztügynök modellel.