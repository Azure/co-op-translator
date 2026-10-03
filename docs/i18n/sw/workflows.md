# Chagua Mtiririko Wako wa Kazi

Co-op Translator inaweza kutumika kwa njia tatu: CLI, Python API, na seva ya MCP. Zinashiriki uwezo uleule wa kutafsiri, lakini kila moja inafaa mtiririko tofauti wa kazi.

Tumia ukurasa huu unapokuwa unajiamua wapi kuanza.

**Ikiwa unabadilisha tafsiri kwa mkono:** mtiririko wa chaguo-msingi wa CLI na Actions hurefanya tafsiri tena faili za chanzo zilizobadilika kwa ukamilifu, hivyo maneno yako katika faili hizo yanaweza kufutwa. Kagua tofauti (diff) kabla ya kukubali sasisho. Kwa kuhifadhi ngazi-ya-kizuizi ya blok wa Markdown kwa marekebisho yaliyokubaliwa, tumia mupeanaji wa hali ya tafsiri wa [Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Uamuzi wa Haraka

| Ikiwa unataka... | Tumia | Anza hapa |
| --- | --- | --- |
| Kutafsiri au kukagua repository kutoka terminali | CLI | [Marejeleo ya CLI](cli.md) |
| Ongeza tafsiri kwenye script ya Python, huduma, notebook, au kazi ya CI | Python API | [Python API](api.md) |
| Mruhusu wakala, mhariri, au mteja anayeendana na MCP kutafsiri maudhui kwa niaba yako | MCP Server | [MCP Server](mcp.md) |
| Tafsiri hati moja ya Markdown, notebook, au picha ambayo programu yako tayari imeipakia | Python API au MCP Server | [Python API](api.md) au [MCP Server](mcp.md) |
| Tafsiri repository nzima na folda za kutolea-tumizi za kawaida na metadata | CLI au `run_translation` | [Marejeleo ya CLI](cli.md) au [Python API](api.md) |

## Tumia CLI wakati

Chagua CLI wakati mtu au kazi ya CI inaendesha tafsiri ya repository kutoka kwenye shell.

CLI ni njia ya moja kwa moja zaidi wakati unataka Co-op Translator kugundua faili za mradi, kuunda matokeo yaliyotafsiriwa, kuhifadhi mpangilio wa mradi, kusasisha metadata, na kuendesha amri za ukaguzi.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Mfano huu unatafsiri Markdown na notebooks. Ongeza `-img` tu baada ya kusanidi [Azure AI Vision](configuration.md#azure-ai-vision). Kwa run ya kwanza inayolenga Markdown pekee, fuata [Tafsiri yako ya kwanza](first-translation.md).

Inafaa kwa:

- Unatafsiri repository kutoka terminali yako.
- Unataka amri inayoweza kurudiwa kwa michakato ya CI au utoaji.
- Unataka kugundua mradi, njia za matokeo, metadata, usafishaji, na ukaguzi vilivyojengwa ndani.
- Unapendelea kiolesura cha amri badala ya kuandika msimbo wa Python.

## Tumia Python API wakati

Chagua Python API wakati msimbo wako unapaswa kudhibiti mtiririko wa kazi.

API ni muhimu kwa programu, script za uendeshaji wa otomatiki, notebooks, huduma, na mifumo maalum. Inakuwezesha kuita API za ngazi ya chini za kutafsiri maudhui kwa faili binafsi, au kuendesha utaratibu sawa wa kiwango cha repository unaotumika na CLI.

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

Endesha tafsiri ya repository kutoka Python:

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

Inafaa kwa:

- Programu yako tayari inasoma faili, buffers, notebooks, au baiti za picha.
- Unahitaji uthibitishaji maalum, uhifadhi, uandishi wa kumbukumbu (logging), jaribio tena, au taratibu za kuidhinisha.
- Unataka kutafsiri hati moja, notebook, au picha bila kushughulikia repository nzima.
- Unataka tafsiri ya repository, lakini kupitia uendeshaji wa Python badala ya amri ya shell.

## Tumia Server ya MCP wakati

Chagua seva ya MCP wakati wakala, mhariri, au mteja anayefaa na MCP anapaswa kuita zana za Co-op Translator.

Katika usanidi wa kawaida wa eneo-kazi, mtumiaji hajawahi kuendelea kuendesha seva kwa mkono. Mteja wa MCP huanza `co-op-translator-mcp` juu ya `stdio` anapohitaji zana.

Mifano ya ombi la mtumiaji ambalo wakala anaweza kushughulikia:

- "Tafsiri faili hii ya Markdown kwa Kikorea na uhakikishe viunganisho viko sahihi."
- "Tafsiri faili hii ya Markdown kwa Kikorea kupitia mtiririko wa MCP unaosaidiwa na wakala, ukitumia mfano wako kwa vipande vilivyotafsiriwa."
- "Tafsiri notebook hii kwa Kikorea, hifadhi seli za msimbo, na tumia Co-op Translator MCP kujenga tena notebook."
- "Tafsiri maandishi katika picha hii kwa Kijapani na hifadhi matokeo."
- "Fanya mtihani (dry-run) wa tafsiri ya repository kwa Kihispania na niambie ni mabadiliko gani yangetokea."
- "Kagua kama matokeo ya tafsiri ya Kikorea yapo sawa na yaliyosasishwa."

Kwa Markdown na notebooks, MCP inaweza kufanya kazi kwa njia mbili:

| Hali | Tumia wakati | Zana kuu |
| --- | --- | --- |
| Inayosaidiwa na wakala | Wakala mwenyeji wa MCP anapaswa kutafsiri vipande kwa kutumia mfano wake mwenyewe, bila vigezo vya mtoa huduma wa LLM wa Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Inaungwa mkono na mtoa huduma | Co-op Translator inapaswa kuita Azure OpenAI, OpenAI, au Anthropic moja kwa moja. | `translate_markdown_content`, `translate_notebook_content` |

Muundo wa wito wa zana ya Markdown ya MCP inayoungwa mkono na mtoa huduma:

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

Muundo wa wito wa zana ya picha ya MCP:

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

Tafsiri ya repository kwa kawaida hufanywa kama jaribio (dry-run) kupitia MCP:

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

- Unataka mitiririko ya tafsiri kwa lugha asilia ndani ya wakala au mhariri.
- Unataka tafsiri ya Markdown au notebook ambapo modeli ya wakala mwenyeji inatafsiri vipande vilivyotayarishwa.
- Unataka wakala atafsiri maudhui yaliyochaguliwa badala ya repository nzima.
- Unataka hatua ya idhini kabla ya kuandika kwa repository nzima.
- Unataka kiolesura kimoja kinachofunguka zana za Markdown, notebook, picha, ukaguzi, na uandishi upya wa njia.

## Jinsi Zinavyofanya Kazi Pamoja

CLI ni chaguo bora kwa watu wanaotafsiri repositories. Python API ni bora wakati msimbo wako unamiliki mtiririko wa kazi. Seva ya MCP ni bora wakati wakala au mhariri anamiliki mtiririko wa kazi.

Njia zote tatu zinatumia API ya umma ya Co-op Translator, hivyo unaweza kuanza na CLI, kuendeshanisha kwa Python baadaye, na kutoa uwezo uleule kwa wateja wa MCP wakati unahitaji mitiririko inayosukumwa na wakala.