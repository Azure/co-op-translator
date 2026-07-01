# Válassza ki a munkafolyamatát

Co-op Translator háromféleképpen használható: CLI, Python API és MCP szerver. Ugyanazokat a fordítási képességeket kínálják, de mindegyik más munkafolyamathoz illik.

Használja ezt az oldalt, amikor dönt arról, hogy hol kezdje.

## Gyors döntés

| If you want to... | Use | Start here |
| --- | --- | --- |
| Fordítson vagy ellenőrizzen egy tárolót terminálból | CLI | [CLI referencia](cli.md) |
| Adjon fordítást egy Python szkriptbe, szolgáltatásba, jegyzetfüzetbe vagy CI munkába | Python API | [Python API](api.md) |
| Hagyja, hogy egy ügynök, szerkesztő vagy MCP-kompatibilis kliens fordítsa le a tartalmat | MCP Server | [MCP szerver](mcp.md) |
| Fordítson le egy Markdown dokumentumot, jegyzetfüzetet vagy képet, amelyet az alkalmazása már betöltött | Python API or MCP Server | [Python API](api.md) or [MCP szerver](mcp.md) |
| Fordítson le egy teljes tárolót szabványos kimeneti mappákkal és metaadatokkal | CLI or `run_translation` | [CLI referencia](cli.md) or [Python API](api.md) |

## Használja a CLI-t, ha

Válassza a CLI-t, ha egy személy vagy CI feladat a shellből vezérli a tároló fordítását.

A CLI a legegyszerűbb út, ha azt szeretné, hogy a Co-op Translator felfedezze a projektfájlokat, létrehozza a lefordított kimeneteket, megőrizze a projekt felépítését, frissítse a metaadatokat és lefuttassa az áttekintési parancsokat.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Jól illik:

- Terminálról fordít egy tárolót.
- Ismételhető parancsra van szüksége CI vagy kiadási munkafolyamatokhoz.
- Szüksége van beépített projektfelismerésre, kimeneti útvonalakra, metaadatokra, takarításra és áttekintésre.
- A parancssori felületet részesíti előnyben a Python-kód írásával szemben.

## Használja a Python API-t, ha

Válassza a Python API-t, ha az Ön kódjának kell irányítania a munkafolyamatot.

Az API hasznos alkalmazásokhoz, automatizált szkriptekhez, jegyzetfüzetekhez, szolgáltatásokhoz és egyedi csővezetékekhez. Lehetővé teszi alacsony szintű tartalomfordítási API-k meghívását egyes fájlokhoz, vagy ugyanazon a társzintű koordinációnak a futtatását, amelyet a CLI is használ.

Fordítson le egy Markdown dokumentumot és döntse el, hova mentse:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Futtasson egy tárolófordítást Pythonból:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Jól illik:

- Az alkalmazása már olvassa a fájlokat, puffereket, jegyzetfüzeteket vagy képbájtokat.
- Szüksége van egyedi érvényesítésre, tárolásra, naplózásra, újrapróbálkozásra vagy jóváhagyási folyamatokra.
- Egy dokumentumot, jegyzetfüzetet vagy képet szeretne lefordítani anélkül, hogy az egész tárolót feldolgozná.
- Tárolófordítást szeretne, de Python automatizációból a shell parancs helyett.

## Használja az MCP szervert, ha

Válassza az MCP szervert, ha egy ügynök, szerkesztő vagy MCP-kompatibilis kliens kell, hogy meghívja a Co-op Translator eszközeit.

A normál helyi beállításban a felhasználó nem tartja kézzel folyamatosan futó szerverként. Az MCP kliens elindítja a `co-op-translator-mcp`-t a `stdio` felett, amikor szüksége van az eszközökre.

Példák a felhasználói kérésekre, amelyeket egy ügynök kezelhet:

- "Fordítsa le ezt a Markdown fájlt koreaira, és tartsa helyesnek a linkeket."
- "Fordítsa le ezt a Markdown fájlt koreaira az ügynök által támogatott MCP munkafolyamattal, a fordított részekhez a saját modelljét használva."
- "Fordítsa le ezt a jegyzetfüzetet koreaira, őrizze meg a kódcellákat, és használja a Co-op Translator MCP-t a jegyzetfüzet rekonstruálásához."
- "Fordítsa le ezen kép szövegét japánra és mentse el az eredményt."
- "Végezzen dry-run jellegű tárolófordítást spanyolra, és mondja meg, mi változna."
- "Ellenőrizze, hogy a koreai fordítás kimenete naprakész-e."

Markdown és jegyzetfüzetek esetében az MCP két módban működhet:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | Az MCP host ügynöknek saját modelljével kell lefordítania a részeket, Co-op Translator LLM szolgáltatói hitelesítő adatok nélkül. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | A Co-op Translator hívja meg közvetlenül az Azure OpenAI-t vagy az OpenAI-t. | `translate_markdown_content`, `translate_notebook_content` |

MCP szolgáltató-támogatott Markdown eszköz hívás alakja:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP kép eszköz hívás alakja:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

A tárolófordítás alapértelmezés szerint dry-run módban történik az MCP-n keresztül:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Jól illik:

- Természetes nyelvű fordítási munkafolyamatokat szeretne egy ügynökön vagy szerkesztőn belül.
- Markdown vagy jegyzetfüzet fordítást szeretne, ahol a host ügynök modellje fordítja le az előkészített részeket.
- Azt szeretné, hogy az ügynök a kiválasztott tartalmat fordítsa, ahelyett, hogy az egész tárolót fordítaná.
- Jóváhagyási lépést szeretne a tárolóra kiterjedő írások előtt.
- Egyetlen felületet szeretne, amely elérhetővé teszi a Markdown-, jegyzetfüzet-, kép-, ellenőrzési és útvonal-átírási eszközöket.

## Hogyan illeszkednek egymáshoz

A CLI a legjobb alapértelmezett választás emberek számára, akik tárolókat fordítanak. A Python API akkor a legjobb, ha az Ön kódja birtokolja a munkafolyamatot. Az MCP szerver pedig akkor a legjobb, ha egy ügynök vagy szerkesztő birtokolja a munkafolyamatot.

Mindhárom út ugyanazt a nyilvános Co-op Translator API-t használja, így elkezdheti a CLI-vel, később automatizálhat Pythonnal, és ugyanezeket a képességeket teheti elérhetővé MCP kliens számára, amikor ügynökalapú munkafolyamatokra van szüksége.