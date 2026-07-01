# Pasirinkite savo darbo eigą

Co-op Translator galima naudoti trimis būdais: CLI, Python API ir MCP serveriu. Visi jie turi tas pačias vertimo galimybes, tačiau kiekvienas tinka kitokiai darbo eigai.

Naudokite šį puslapį, kai nusprendžiate, nuo ko pradėti.

## Greitas sprendimas

| Jei norite... | Naudoti | Pradėkite čia |
| --- | --- | --- |
| Išversti arba peržiūrėti saugyklą iš terminalo | CLI | [CLI nuoroda](cli.md) |
| Pridėti vertimą į Python skriptą, paslaugą, užrašų knygą arba CI užduotį | Python API | [Python API](api.md) |
| Leisti agentui, redaktoriui arba su MCP suderinamam klientui išversti turinį už jus | MCP Server | [MCP serveris](mcp.md) |
| Išversti vieną Markdown dokumentą, užrašų knygą arba paveikslėlį, kurį jūsų programa jau įkėlė | Python API arba MCP Server | [Python API](api.md) arba [MCP serveris](mcp.md) |
| Išversti visą saugyklą su standartiniais išvesties aplankais ir metaduomenimis | CLI arba `run_translation` | [CLI nuoroda](cli.md) arba [Python API](api.md) |

## Naudokite CLI, kai

Rinkitės CLI, kai žmogus arba CI užduotis atlieka saugyklos vertimą iš terminalo.

CLI yra tiesiausias kelias, kai norite, kad Co-op Translator aptiktų projekto failus, sukurtų išverstus rezultatus, išsaugotų projekto išdėstymą, atnaujintų metaduomenis ir paleistų peržiūros komandas.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Tinka:

- Verčiate saugyklą naudodami terminalą.
- Norite pakartojamos komandos CI arba leidimo darbo eigoms.
- Norite įdiegto projekto aptikimo, išvesties kelių, metaduomenų, švarinimo ir peržiūros.
- Teikiate pirmenybę komandiniam sąsajai, o ne Python kodui rašyti.

## Naudokite Python API, kai

Rinkitės Python API, kai jūsų kodas turi valdyti darbo eigą.

API yra naudinga programoms, automatizavimo skriptams, užrašų knygoms, paslaugoms ir pasirinktinėms eilėms. Ji leidžia kviesti žemo lygio turinio vertimo API atskiroms byloms arba paleisti tą patį saugyklos lygio orkestravimą, kurį naudoja CLI.

Išverskite vieną Markdown dokumentą ir nuspręskite, kur jį išsaugoti:

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

Paleiskite saugyklos vertimą iš Python:

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

Tinka:

- Jūsų programa jau skaito failus, buferius, užrašų knygas arba vaizdo baitus.
- Jums reikia pasirinktinės validacijos, saugojimo, žurnavimo, pakartojimų arba patvirtinimo srautų.
- Norite išversti vieną dokumentą, užrašų knygą arba vaizdą neapdorodami visos saugyklos.
- Norite saugyklos vertimo, bet per Python automatizavimą, o ne per shell komandą.

## Naudokite MCP serverį, kai

Rinkitės MCP serverį, kai agentas, redaktorius arba su MCP suderinamas klientas turėtų kviesti Co-op Translator įrankius.

Įprastame vietiniame nustatyme vartotojas rankiniu būdu nelaiko serverio veikiančio. MCP klientas paleidžia `co-op-translator-mcp` per `stdio`, kai jam reikalingi įrankiai.

Pavyzdiniai vartotojo užklausos, kurias galėtų tvarkyti agentas:

- "Išverskite šį Markdown failą į korėjiečių kalbą ir užtikrinkite, kad nuorodos būtų teisingos."
- "Išverskite šį Markdown failą į korėjiečių kalbą naudodami agento asistuojamą MCP darbo eigą, savo modeliui taikant išverstoms dalims."
- "Išverskite šią užrašų knygą į korėjiečių kalbą, išsaugokite kodo langelius ir naudokite Co-op Translator MCP užrašų knygos atkūrimui."
- "Išverskite šio paveikslėlio tekstą į japonų kalbą ir išsaugokite rezultatą."
- "Atlikite bandomąjį saugyklos vertimą į ispanų kalbą ir pasakykite, kas pasikeistų."
- "Peržiūrėkite, ar korėjiečių vertimo rezultatai yra atnaujinti."

Markdown ir užrašų knygoms MCP gali veikti dviem režimais:

| Režimas | Naudokite kai | Pagrindiniai įrankiai |
| --- | --- | --- |
| Agentui padedant | MCP šeimininko agentas turėtų versti gabalus naudodamas savo modelį, be Co-op Translator LLM teikėjo kredencialų. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Teikėjo palaikomas | Co-op Translator turėtų kviesti Azure OpenAI arba OpenAI tiesiogiai. | `translate_markdown_content`, `translate_notebook_content` |

MCP teikėjo palaikomas Markdown įrankio iškvietimo forma:

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

MCP vaizdo įrankio iškvietimo forma:

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

Per MCP saugyklos vertimas pagal numatytuosius nustatymus vykdomas bandomuoju režimu:

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

Tinka:

- Norite natūralių kalbų vertimo darbo eigų agento ar redaktoriaus viduje.
- Norite Markdown arba užrašų knygos vertimo, kai šeimininko agento modelis išverčia paruoštus gabalus.
- Norite, kad agentas išverstų pasirinktą turinį, o ne visą saugyklą.
- Norite patvirtinimo žingsnio prieš rašant į visą saugyklą.
- Norite vienos sąsajos, kuri suteikia prieigą prie Markdown, užrašų knygos, vaizdų, peržiūros ir kelių perrašymo įrankių.

## Kaip jie dera tarpusavyje

CLI yra geriausias numatytasis pasirinkimas žmonėms, verčiantiems saugyklas. Python API geriausia, kai jūsų kodas valdo darbo eigą. MCP serveris geriausias, kai agentas arba redaktorius valdo darbo eigą.

Visos trys galimybės naudoja tą patį viešą Co-op Translator API, todėl galite pradėti nuo CLI, vėliau automatizuoti su Python ir, prireikus, suteikti tas pačias galimybes MCP klientams agentų valdomoms darbo eigoms.