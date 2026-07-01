# Chagua Mchakato Wako

Co-op Translator inaweza kutumika kwa njia tatu: CLI, Python API, na seva ya MCP. Zinashiriki uwezo sawa wa kutafsiri, lakini kila moja inafaa kwa mchakato wa kazi tofauti.

Tumia ukurasa huu unapokuwa unaamua wapi kuanza.

## Uamuzi wa Haraka

| Ikiwa unataka... | Tumia | Anza hapa |
| --- | --- | --- |
| Kutafsiri au kukagua hazina kutoka terminali | CLI | [CLI Reference](cli.md) |
| Ongeza tafsiri kwenye script ya Python, huduma, daftari, au kazi ya CI | Python API | [Python API](api.md) |
| Acha wakala, mhariri, au mteja anayefaa na MCP atafsiri maudhui kwa niaba yako | MCP Server | [MCP Server](mcp.md) |
| Tafsiri hati moja ya Markdown, daftari, au picha ambayo programu yako tayari imeipakia | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Tafsiri hazina nzima na folda za pato za kawaida na metadata | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Tumia CLI wakati

Chagua CLI wakati mtu au kazi ya CI inaendesha utafsiri wa hazina kutoka shell.

CLI ndiyo njia ya moja kwa moja wakati unataka Co-op Translator kugundua mafaili ya mradi, kuunda matokeo yaliyotafsiriwa, kuhifadhi muundo wa mradi, kusasisha metadata, na kuendesha amri za ukaguzi.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Inafaa kwa:

- Unatafsiri hazina kutoka terminali yako.
- Unataka amri inayoweza kurudiwa kwa CI au mchakato za utoaji.
- Unataka ugunduzi wa mradi uliojengwa, njia za pato, metadata, usafishaji, na ukaguzi.
- Unapendelea kiolesura cha amri badala ya kuandika msimbo wa Python.

## Tumia Python API wakati

Chagua Python API wakati msimbo wako unapaswa kudhibiti mchakato wa kazi.

API ni muhimu kwa programu, script za otomatiki, daftari (notebooks), huduma, na mitiririko maalum. Inakuwezesha kuita API za utafsiri wa maudhui za ngazi ya chini kwa mafaili binafsi, au kuendesha uratibu wa ngazi ya hazina unaotumika na CLI.

Tafsiri hati moja ya Markdown na uamue wapi kuihifadhi:

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

Endesha utafsiri wa hazina kutoka Python:

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

Inafaa kwa:

- Programu yako tayari inasoma mafaili, buffer, daftari (notebooks), au baiti za picha.
- Unahitaji uthibitisho maalum, uhifadhi, udhibiti wa kumbukumbu (logging), jaribio la kurudia, au mitiririko ya idhini.
- Unataka kutafsiri hati moja, daftari, au picha bila kusindika hazina nzima.
- Unataka utafsiri wa hazina, lakini kutoka otomatiki ya Python badala ya amri ya shell.

## Tumia Seva ya MCP wakati

Chagua seva ya MCP wakati wakala, mhariri, au mteja anayefaa na MCP inapaswa kuita zana za Co-op Translator.

Katika usanidi wa kawaida wa ndani, mtumiaji haendi kwa mikono kuendelea kuendesha seva. Mteja wa MCP huanzisha `co-op-translator-mcp` kupitia `stdio` anapohitaji zana hizo.

Mifano ya maombi ya mtumiaji ambayo wakala anaweza kushughulikia:

- "Tafsiri faili hii ya Markdown kwa Kikorea na hakikisha viungo viko sahihi."
- "Tafsiri faili hii ya Markdown kwa Kikorea kwa mtiririko wa MCP unaosaidiwa na wakala, ukitumia mfano wako kwa vipande vilivyotafsiriwa."
- "Tafsiri daftari hili (notebook) kwa Kikorea, uhifadhi seli za msimbo, na tumia Co-op Translator MCP kujenga daftari upya."
- "Tafsiri maandishi katika picha hii kwa Kijapani na hifadhi matokeo."
- "Fanya jaribio (dry-run) la utafsiri wa hazina kwa Kihispania na niambie ni nini kingeweza kubadilika."
- "Kagua kama matokeo ya tafsiri ya Kikorea yako hadi tarehe."

Kwa Markdown na daftari (notebooks), MCP inaweza kufanya kazi kwa njia mbili:

| Hali | Tumia wakati | Zana kuu |
| --- | --- | --- |
| Iliyosaidiwa na wakala | Wakala mwenyeji wa MCP anapaswa kutafsiri vipande kwa mfano wake, bila vyeti vya mtoa huduma wa LLM wa Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Inayotegemea mtoa huduma | Co-op Translator inapaswa kuita Azure OpenAI au OpenAI moja kwa moja. | `translate_markdown_content`, `translate_notebook_content` |

Muundo wa mwito wa zana ya Markdown iliyotegemea mtoa huduma wa MCP:

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

Muundo wa mwito wa zana ya picha ya MCP:

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

Utafsiri wa hazina unafanywa jaribio (dry-run) kwa chaguo-msingi kupitia MCP:

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

Inafaa kwa:

- Unataka mitiririko ya utafsiri ya lugha ya asili ndani ya wakala au mhariri.
- Unataka utafsiri wa Markdown au daftari ambapo mfano wa wakala mwenyeji unatafsiri vipande vilivyotayarishwa.
- Unataka wakala atafsiri maudhui yaliyoteuliwa badala ya hazina nzima.
- Unataka hatua ya idhini kabla ya maandishi kwa hazina nzima.
- Unataka kiolesura kimoja kinachofichua zana za Markdown, daftari, picha, ukaguzi, na uandishi upya wa njia.

## Jinsi Zinavyofanya Kazi Pamoja

CLI ni chaguo bora kwa wanadamu wanaotafsiri hazina. Python API ni bora wakati msimbo wako unamiliki mchakato wa kazi. Seva ya MCP ni bora wakati wakala au mhariri anamiliki mchakato wa kazi.

Njia zote tatu zinatumia API ya umma ya Co-op Translator, hivyo unaweza kuanza na CLI, kuotomatisha kwa Python baadaye, na kufichua uwezo ule ule kwa wateja wa MCP unapohitaji mitiririko inayoendeshwa na wakala.