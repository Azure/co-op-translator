# Vali oma töövoog

Co-op Translatorit saab kasutada kolmel viisil: CLI, Python API ja MCP server. Neil kõigil on samad tõlkevõimekused, kuid igaüks sobib erineva töövoo jaoks.

Kasuta seda lehte, kui otsustad, kust alustada.

**Kui muudad tõlkeid käsitsi:** vaikimisi CLI ja Actions töövood tõlgivad muudetud lähtefaile täielikult uuesti, nii et sinu sõnastus neis failides võib saada üle kirjutatud. Vaata diffi enne, kui aktsepteerid uuenduse. Heaksatud muudatuste Markdowni plokkide tasemel säilitamiseks kasuta valikulist [Python API tõlkeoleku pakkujat](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Kiire otsus

| Kui tahad... | Kasuta | Alusta siit |
| --- | --- | --- |
| Tõlkida või üle vaadata hoidlat terminalist | CLI | [CLI viide](cli.md) |
| Lisada tõlget Python-skripti, teenuse, märkmiku või CI-töö hulka | Python API | [Python API](api.md) |
| Lasta agendil, redaktoril või MCP-ühilduval kliendil sinu eest sisu tõlkida | MCP Server | [MCP Server](mcp.md) |
| Tõlkida üks Markdowni dokument, märkmik või pilt, mille su rakendus juba laadis | Python API või MCP Server | [Python API](api.md) või [MCP Server](mcp.md) |
| Tõlkida kogu hoidla koos standardsete väljundkaustade ja metadataga | CLI või `run_translation` | [CLI viide](cli.md) või [Python API](api.md) |

## Kasuta CLI-d, kui

Vali CLI, kui inimene või CI-töö juhib hoidla tõlkimist käsurealt.

CLI on kõige otsem tee, kui soovid, et Co-op Translator avastaks projektifaile, tõlgiks need, säilitaks projekti paigutuse, uuendaks metaandmeid ja käivitaks ülevaatuse käske.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

See näide tõlgib Markdowni ja märkmikke. Lisa `-img` alles pärast [Azure AI Vision](configuration.md#azure-ai-vision) seadistamist. Kui tahad esmalt ainult Markdowni, järgi [Sinu esimene tõlge](first-translation.md).

Sobib hästi:

- Sa tõlgid hoidlat terminalist.
- Sa tahad korduvat käsku CI või väljalaske töövoogude jaoks.
- Sa tahad sisseehitatud projektide avastamist, väljundite teid, metaandmeid, puhastust ja ülevaatust.
- Sa eelistad käsurealiidest Python-koodi kirjutamise asemel.

## Kasuta Python API-d, kui

Vali Python API, kui sinu kood peaks juhtima töövoogu.

API on kasulik rakenduste, automatiseerimisskriptide, märkmike, teenuste ja kohandatud torustike jaoks. See võimaldab kutsuda madala taseme sisu tõlke API-sid individuaalsete failide jaoks või käivitada sama hoidla-tasemel orkestreerimist, mida kasutab CLI.

Tõlgi üks Markdowni dokument ja otsusta, kuhu see salvestada:

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

Käivita hoidla tõlkimine Pythoni kaudu:

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

Sobib hästi:

- Sinu rakendus loeb juba faile, puhvriandmeid, märkmikke või pildi baite.
- Sul on vaja kohandatud valideerimist, salvestust, logimist, kordusi või heakskiitvoolusid.
- Tahad tõlkida ühte dokumenti, märkmikku või pilti ilma kogu hoidlat töödelda.
- Tahad hoidla tõlget, aga Pythoni automatiseerimisest, mitte käsurealt.

## Kasuta MCP serverit, kui

Vali MCP server, kui agent, redaktor või MCP-ühilduv klient peaks kutsuma Co-op Translator tööriistu.

Tavapärases lokaalses seadistuses ei pea kasutaja serverit käsitsi jooksutama. MCP klient käivitab `co-op-translator-mcp` üle `stdio`, kui tööriistu on vaja.

Näited kasutaja päringutest, mida agent võiks käsitleda:

- "Tõlgi see Markdowni fail koreakeelseks ja hoia lingid õiged."
- "Tõlgi see Markdowni fail koreakeelseks agenti abistatud MCP töövooga, kasutades tõlgitud lõikude jaoks oma mudelit."
- "Tõlgi see märkmik koreakeelseks, säilita koodirakud ja kasuta Co-op Translator MCP-i märkmiku taastamiseks."
- "Tõlgi selle pildi tekst jaapanikeelseks ja salvesta tulemus."
- "Tee hoidla tõlke kuivkäik hispaania keelde ja ütle mulle, mis muutuks."
- "Ülevaata, kas koreakeelne tõlke väljund on ajakohane."

Markdowni ja märkmike puhul saab MCP töötada kahes režiimis:

| Režiim | Kasuta, kui | Põhivahendid |
| --- | --- | --- |
| Agent-assisted | Kui MCP host-agent peaks tõlkima lõike oma mudeliga, ilma Co-op Translator LLM pakkuja mandaatideta. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Kui Co-op Translator peaks otse kasutama Azure OpenAI, OpenAI või Anthropic teenuseid. | `translate_markdown_content`, `translate_notebook_content` |

MCP pakkujapoolt toetava Markdowni tööriista kutse vorm:

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

MCP pilditööriista kutse vorm:

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

Hoidla tõlkimine on MCP kaudu vaikimisi kuivkäik:

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

Sobib hästi:

- Tahad loomuliku keele tõlke töövooge agendi või redaktori sees.
- Tahad Markdowni või märkmiku tõlget, kus host-agent mudel tõlgib ettevalmistatud lõike.
- Tahad, et agent tõlgiks valitud sisu, mitte kogu hoidlat.
- Tahad heakskiitmisastet enne hoidlaüleste kirjutamiste sooritamist.
- Tahad üht liidest, mis pakub Markdowni, märkmiku, pildi, ülevaatuse ja tee-ümberkirjutamise tööriistu.

## Kuidas need sobituvad

CLI on parim vaikimisi valik inimestele, kes tõlgivad hoidlaid. Python API on parim, kui sinu kood juhib töövoogu. MCP server on parim, kui agent või redaktor juhib töövoogu.

Kõik kolm rada kasutavad sama avalikku Co-op Translator API-d, nii et võid alustada CLI-ga, hiljem automatiseerida Pythoniga ja pakkuda samu võimalusi MCP klientidele, kui vajad agentipõhiseid töövooge.