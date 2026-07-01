# Valige oma töövoog

Co-op Translatori saab kasutada kolmel viisil: CLI, Python API ja MCP-server. Need jagavad samu tõlkevõimekusi, kuid igaüks sobib erineva töövoo jaoks.

Kasutage seda lehte, kui otsustate, kust alustada.

## Kiire otsus

| Kui soovite... | Kasutage | Alustage siit |
| --- | --- | --- |
| Tõlkida või üle vaadata repositooriumi terminalist | CLI | [CLI Reference](cli.md) |
| Lisada tõlge Python-skripti, teenusesse, märkmikku või CI-töösse | Python API | [Python API](api.md) |
| Lasta agendil, redaktoril või MCP-ühilduval kliendil sisu teie eest tõlkida | MCP Server | [MCP Server](mcp.md) |
| Tõlkida üks Markdown-dokument, märkmik või pilt, mille teie rakendus on juba laadinud | Python API või MCP-server | [Python API](api.md) or [MCP Server](mcp.md) |
| Tõlkida kogu repositoorium standardsete väljundkaustade ja metaandmetega | CLI või `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Kasutage CLI-d, kui

Valige CLI, kui inimene või CI-töö juhib repositooriumi tõlkimist käsurealt.

CLI on kõige sirgjoonelisem tee, kui soovite, et Co-op Translator avastaks projekti failid, looks tõlgitud väljundeid, säilitaks projekti ülesehituse, uuendaks metaandmeid ja käivitaks ülevaatamise käske.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Sobib hästi:

- Te tõlgite repositooriumi käsurealt.
- Soovite korduvkasutatavat käsku CI- või väljalasketöövoogude jaoks.
- Soovite sisseehitatud projekti avastamist, väljundite radu, metaandmeid, puhastamist ja ülevaatamist.
- Eelistate käsuliidest Python-koodi kirjutamisele.

## Kasutage Python API-d, kui

Valige Python API, kui teie kood peaks kontrollima töövoogu.

API on kasulik rakenduste, automatiseerimisskriptide, märkmike, teenuste ja kohandatud torujuhtmete jaoks. See võimaldab kutsuda madala taseme sisu tõlke API-sid üksikute failide jaoks või käivitada sama repositooriumi-taseme orkestreerimist, mida kasutab CLI.

Tõlkige üks Markdown-dokument ja otsustage, kuhu see salvestada:

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

Käivitage repositooriumi tõlkimine Pythonist:

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

Sobib hästi:

- Teie rakendus loeb juba faile, puhvreid, märkmikke või pildibaite.
- Vajate kohandatud valideerimist, salvestust, logimist, taaskatseid või kinnituse töövooge.
- Soovite tõlkida ühte dokumenti, märkmikku või pilti ilma kogu repositooriumi töötlemata.
- Soovite repositooriumi tõlkimist, kuid Python-automatiseerimise kaudu, mitte käsurealt.

## Kasutage MCP-serverit, kui

Valige MCP-server, kui agent, redaktor või MCP-ühilduv klient peaks kutsuma Co-op Translatori tööriistu.

Tavapärases lokaalses seadistuses kasutaja ei hoia serverit käsitsi töös. MCP klient käivitab `co-op-translator-mcp` üle `stdio`, kui tal on tööriistu vaja.

Näited kasutajapäringutest, mida agent võiks töödelda:

- "Tõlgi see Markdown-fail korea keelde ja säilita lingid korrektsed."
- "Tõlgi see Markdown-fail korea keelde agenti abistatud MCP-töövoos, kasutades oma mudelit tõlgitud osade jaoks."
- "Tõlgi see märkmik korea keelde, säilita koodirakud ja kasuta Co-op Translatori MCP-d, et rekonstrueerida märkmik."
- "Tõlgi selle pildi tekst jaapani keelde ja salvesta tulemus."
- "Tee repositooriumi tõlke proovkäik hispaania keelde ja ütle mulle, mis muutuks."
- "Kontrolli, kas korea keelde tõlgitud väljund on ajakohane."

Markdowni ja märkmike puhul saab MCP töötada kahes režiimis:

| Režiim | Kas kasutada, kui | Põhitööriistad |
| --- | --- | --- |
| Agendi abiga | MCP hostagent peaks tõlkima tükke oma mudeliga, ilma Co-op Translatori LLM-teenuse mandaatideta. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Teenusepakkuja-toetatud | Co-op Translator peaks kutsuma Azure OpenAI või OpenAI otse. | `translate_markdown_content`, `translate_notebook_content` |

MCP teenusepakkuja-toetatud Markdown-tööriista kutse vorm:

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

Repositooriumi tõlkimine on MCP kaudu vaikimisi proovkäivitusena:

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

- Soovite loomuliku keele tõlketöövooge agendi või redaktori sees.
- Soovite Markdowni või märkmiku tõlget, kus hostagenti mudel tõlgib ettevalmistatud tükke.
- Soovite, et agent tõlgiks valitud sisu, mitte kogu repositooriumi.
- Soovite kinnitusetappi enne kogu repositooriumi kirjutamisi.
- Soovite üht liidest, mis pakub Markdowni, märkmiku, pildi, ülevaatamise ja tee-ümberkirjutamise tööriistu.

## Kuidas need omavahel sobivad

CLI on parim vaikimisi valik inimestele, kes tõlgivad repositooriume. Python API sobib kõige paremini, kui teie kood haldab töövoogu. MCP-server on parim, kui agent või redaktor haldab töövoogu.

Kõik kolm võimalust kasutavad sama avalikku Co-op Translator API-d, nii et saate alustada CLI-ga, automatiseerida hiljem Pythoni abil ning pakkuda samu võimalusi MCP-klientidele, kui vajate agentide juhitavaid töövooge.