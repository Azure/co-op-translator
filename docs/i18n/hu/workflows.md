# Válassza ki a munkafolyamatot

A Co-op Translator három módon használható: CLI, Python API és az MCP szerver. Ugyanazokat a fordítási képességeket kínálják, de mindegyik egy másik munkafolyamathoz illik.

Használja ezt az oldalt, amikor dönt arról, hol kezdjen.

**Ha kézzel szerkeszti a fordításokat:** az alapértelmezett CLI és Actions munkafolyamatok a módosított forrásfájlokat teljes egészében újrafordítják, így a megfogalmazásai felülíródhatnak. Tekintse át a differenciát, mielőtt elfogad egy frissítést. A Markdown blokk-szintű megtartásához az elfogadott szerkesztésekhez használja az opcionális [Python API fordítási állapot-kezelőt](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Gyors döntés

| Ha azt szeretné, hogy... | Használja | Kezdje itt |
| --- | --- | --- |
| Egy tároló fordítása vagy felülvizsgálata terminálról | CLI | [CLI referencia](cli.md) |
| Fordítás hozzáadása egy Python szkriptbe, szolgáltatásba, jegyzetfüzetbe (notebook) vagy CI feladatba | Python API | [Python API](api.md) |
| Hagyja, hogy egy agent, szerkesztő vagy MCP-kompatibilis kliens fordítsa le a tartalmat Ön helyett | MCP Server | [MCP Server](mcp.md) |
| Fordítson le egy Markdown dokumentumot, jegyzetfüzetet vagy képet, amelyet az alkalmazása már betöltött | Python API vagy MCP Server | [Python API](api.md) vagy [MCP Server](mcp.md) |
| Egy teljes tároló lefordítása szabványos kimeneti mappákkal és metaadatokkal | CLI vagy `run_translation` | [CLI referencia](cli.md) vagy [Python API](api.md) |

## Használja a CLI-t, amikor

Válassza a CLI-t, amikor egy személy vagy CI feladat shellből vezényli a tároló fordítását.

A CLI a legegyszerűbb út, ha azt szeretné, hogy a Co-op Translator megtalálja a projektfájlokat, létrehozza a lefordított kimeneteket, megőrizze a projekt felépítését, frissítse a metaadatokat és lefuttassa a felülvizsgálati parancsokat.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Ez a példa Markdown-t és jegyzetfüzeteket fordít. Az `-img` kapcsolót csak az [Azure AI Vision](configuration.md#azure-ai-vision) konfigurálása után adja hozzá. Ha az első futtatáskor csak Markdown-t szeretne, kövesse a [Első fordítás](first-translation.md).

Mikor illik jól:

- Egy tárolót fordít a terminálról.
- Ismételhető parancsra van szüksége CI vagy kiadási munkafolyamatokhoz.
- Szüksége van beépített projektfelismerésre, kimeneti utakra, metaadatokra, takarításra és felülvizsgálatra.
- A parancssoros felületet részesíti előnyben a Python-kód írásával szemben.

## Használja a Python API-t, amikor

Válassza a Python API-t, amikor az Ön saját kódjának kell irányítania a munkafolyamatot.

Az API hasznos alkalmazásokhoz, automatizálási szkriptekhez, jegyzetfüzetekhez, szolgáltatásokhoz és egyedi csővezetékekhez. Lehetővé teszi alacsony szintű tartalomfordítási API-k hívását egyedi fájlokhoz, vagy futtathatja ugyanazt a tároló-szintű szervezést, amelyet a CLI is használ.

Fordítson le egy Markdown dokumentumot, és döntsön arról, hová mentse:

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

Futtasson tárolófordítást Pythonból:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Jól illik:

- Az alkalmazása már olvas fájlokat, pufferelt tartalmakat, jegyzetfüzeteket vagy képbájtokat.
- Egyedi érvényesítésre, tárolásra, naplózásra, újrapróbálásokra vagy jóváhagyási folyamatokra van szüksége.
- Egyetlen dokumentumot, jegyzetfüzetet vagy képet szeretne fordítani anélkül, hogy az egész tárolót feldolgozná.
- Tároló-fordítást szeretne, de Python automatizálásból a shell parancs helyett.

## Használja az MCP szervert, amikor

Válassza az MCP szervert, amikor egy agent, szerkesztő vagy MCP-kompatibilis kliensnek kell a Co-op Translator eszközeit hívnia.

A normál helyi beállításban a felhasználó nem tartja kézzel futva a szervert. Az MCP kliens elindítja a `co-op-translator-mcp`-t `stdio` felett, amikor szüksége van az eszközökre.

Példa felhasználói kérések, amelyeket egy agent kezelhet:

- "Fordítsa le ezt a Markdown fájlt koreaira, és tartsa helyesnek a hivatkozásokat."
- "Fordítsa le ezt a Markdown fájlt koreaira az agent által segített MCP munkafolyamattal, a saját modelljét használva a lefordított darabokhoz."
- "Fordítsa le ezt a jegyzetfüzetet koreaira, őrizze meg a kódcellákat, és használja a Co-op Translator MCP-t a jegyzetfüzet rekonstruálásához."
- "Fordítsa le ennek a képnek a szövegét japánra, és mentse el az eredményt."
- "Próbafuttasson egy tároló-fordítást spanyolra, és mondja el, mi változna."
- "Ellenőrizze, hogy a koreai fordítás kimenete naprakész-e."

Markdown és jegyzetfüzetek esetén az MCP két módban működhet:

| Mód | Használja, amikor | Fő eszközök |
| --- | --- | --- |
| Agent által segített | Az MCP host agent a saját modelljével fordítson darabokat, a Co-op Translator LLM szolgáltatói hitelesítő adatok nélkül. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Szolgáltató által támogatott | A Co-op Translator közvetlenül hívja az Azure OpenAI-t, az OpenAI-t vagy az Anthropic-ot. | `translate_markdown_content`, `translate_notebook_content` |

MCP szolgáltató által támogatott Markdown eszközhívás formátuma:

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

MCP kép eszközhívás formátuma:

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

A tároló fordítása alapértelmezés szerint próbafuttatás (dry-run) az MCP-n keresztül:

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

- Természetes nyelvű fordítási munkafolyamatokat szeretne egy agentben vagy szerkesztőben.
- Markdown vagy jegyzetfüzet fordítást szeretne, ahol a host agent modell fordítja az előkészített darabokat.
- Azt szeretné, hogy az agent a kiválasztott tartalmat fordítsa le az egész tároló helyett.
- Jóváhagyási lépést szeretne a tároló-szintű írások előtt.
- Egy olyan felületet szeretne, amely a Markdown, jegyzetfüzet, kép, felülvizsgálat és útvonal-átírás eszközöket kínálja.

## Hogyan illeszkednek egymáshoz

Az CLI a legjobb alapértelmezett választás emberek számára, akik tárolókat fordítanak. A Python API akkor a legjobb, ha az ön kódja irányítja a munkafolyamatot. Az MCP szerver akkor a legjobb, ha egy agent vagy szerkesztő birtokolja a munkafolyamatot.

Mindhárom út ugyanazt a nyilvános Co-op Translator API-t használja, így elkezdheti a CLI-vel, később automatizálhat Python-nal, és ugyanazokat a képességeket teheti elérhetővé MCP kliens számára, amikor agent-vezérelt munkafolyamatokra van szüksége.