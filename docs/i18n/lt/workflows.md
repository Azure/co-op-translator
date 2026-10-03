# Pasirinkite savo darbo eigą

Co-op Translator galima naudoti trimis būdais: CLI, Python API ir MCP serveriu. Jie dalijasi tomis pačiomis vertimo galimybėmis, tačiau kiekvienas tinkamas kitokiam darbo eigai.

Naudokite šį puslapį, kai nusprendžiate, nuo ko pradėti.

**Jei redaguojate vertimus rankiniu būdu:** numatytosios CLI ir Actions darbo eigos iš naujo išverčia pakeistus šaltinio failus pilnai, todėl jūsų suformuluotas turinys tuose failuose gali būti perrašytas. Peržiūrėkite diff prieš priimdami atnaujinimą. Norėdami išsaugoti Markdown blokų lygmens priimtų pataisų struktūrą, naudokite pasirinktinį [Python API vertimo būsenos teikėją](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Greitas sprendimas

| Jei norite... | Naudokite | Pradėkite čia |
| --- | --- | --- |
| Išversti arba peržiūrėti repozitoriją iš terminalo | CLI | [CLI Reference](cli.md) |
| Pridėti vertimą į Python scenarijų, paslaugą, užrašų knygutę arba CI užduotį | Python API | [Python API](api.md) |
| Leisti agentui, redaktoriui arba MCP suderinamam klientui versti turinį už jus | MCP Server | [MCP Server](mcp.md) |
| Išversti vieną Markdown dokumentą, užrašų knygutę arba paveikslėlį, kuriuos jūsų programa jau užkėlė | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Išversti visą repozitoriją su standartiniais išvesties katalogais ir metaduomenimis | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Naudokite CLI, kai

Rinkitės CLI, kai žmogus arba CI užduotis valdo repozitorijos vertimą iš komandinės eilutės.

CLI yra tiesiausias kelias, kai norite, kad Co-op Translator atrastų projekto failus, sukurtų išverstą išvestį, išsaugotų projekto struktūrą, atnaujintų metaduomenis ir paleistų peržiūros komandas.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Šis pavyzdys verčia Markdown ir užrašų knygutes. Pridėkite `-img` tik po to, kai sukonfigūruosite [Azure AI Vision](configuration.md#azure-ai-vision). Jei pirmą kartą verčiate tik Markdown, vadovaukitės [Jūsų pirmasis vertimas](first-translation.md).

Tinka:

- Verčiate repozitoriją iš savo terminalo.
- Norite pakartojamo comando CI ar išleidimo darbo eigoms.
- Norite įmontuoto projekto aptikimo, išvesties kelių, metaduomenų, išvalymo ir peržiūros.
- Teikiate pirmenybę komandinei sąsajai už Python kodo rašymą.

## Naudokite Python API, kai

Rinkitės Python API, kai jūsų kodas turi valdyti darbo eigą.

API yra naudinga programoms, automatizavimo scenarijams, užrašų knygutėms, paslaugoms ir pasirinktiniams srautams. Ji leidžia kviesti žemo lygio turinio vertimo API atskiriems failams arba vykdyti tą pačią repozitorijos lygmens orkestraciją, kurią naudoja CLI.

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

Vykdykite repozitorijos vertimą iš Python:

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

Tinka:

- Jūsų programa jau skaito failus, buferius, užrašų knygutes arba paveikslėlių baitus.
- Reikia pasirinktinių validacijų, saugojimo, žurnalaudavimo, bandymų pakartojimo ar patvirtinimo srautų.
- Norite išversti vieną dokumentą, užrašų knygutę arba paveikslėlį be visos repozitorijos apdorojimo.
- Norite repozitorijos vertimo, bet iš Python automatizacijos vietoje komandinės eilutės komandos.

## Naudokite MCP serverį, kai

Rinkitės MCP serverį, kai agentas, redaktorius arba MCP suderinamas klientas turėtų kviesti Co-op Translator įrankius.

Įprastame vietiniame nustatyme vartotojas rankiniu būdu nepaleidžia serverio. MCP klientas paleidžia `co-op-translator-mcp` per `stdio`, kai jam reikia įrankių.

Pavyzdiniai vartotojo prašymai, kuriuos agentas galėtų apdoroti:

- "Išverskite šį Markdown failą į korėjiečių kalbą ir palikite nuorodas taisyklingas."
- "Išverskite šį Markdown failą į korėjiečių kalbą naudodami agento padedamą MCP darbo eigą ir savo modelį verčiamoms dalims."
- "Išverskite šį užrašų knygutę į korėjiečių kalbą, išsaugokite kodo langelius ir naudokite Co-op Translator MCP, kad atstatytumėte užrašų knygutę."
- "Išverskite teksto turinį šioje nuotraukoje į japonų kalbą ir išsaugokite rezultatą."
- "Atlikite sausąjį (dry-run) repozitorijos vertimą į ispanų kalbą ir pasakykite, kas pasikeistų."
- "Peržiūrėkite, ar korėjiečių vertimas yra atnaujintas."

Markdown ir užrašų knygutėms MCP gali veikti dviem režimais:

| Režimas | Kada naudoti | Pagrindiniai įrankiai |
| --- | --- | --- |
| Su agento pagalba | Kai MCP šeimininko agentas turi išversti dalis naudodamas savo modelį, be Co-op Translator LLM teikėjo kredencialų. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Teikėjo palaikomas | Co-op Translator turėtų kviesti Azure OpenAI, OpenAI, arba Anthropic tiesiogiai. | `translate_markdown_content`, `translate_notebook_content` |

MCP teikėjo palaikomas Markdown įrankio kvietimo forma:

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

MCP paveikslėlių įrankio kvietimo forma:

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

Per MCP repozitorijos vertimas pagal numatytuosius nustatymus yra sausasis režimas (dry-run):

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

- Norite natūralios kalbos vertimo darbo eigos agente ar redaktoriuje.
- Norite Markdown arba užrašų knygutės vertimo, kai šeimininko agento modelis verčia paruoštas dalis.
- Norite, kad agentas išverstų pasirinktinį turinį, o ne visą repozitoriją.
- Norite patvirtinimo žingsnio prieš rašymą visoje repozitorijoje.
- Norite vienos sąsajos, kuri atvertų Markdown, užrašų knygutės, paveikslėlių, peržiūros ir kelių perrašymo įrankius.

## Kaip jie dera tarpusavyje

CLI yra geriausias numatytasis pasirinkimas žmonėms verčiantiems repozitorijas. Python API geriausiai tinka, kai jūsų kodas valdo darbo eigą. MCP serveris geriausias, kai darbo eigą valdo agentas arba redaktorius.

Visos trys galimybės naudoja tą pačią viešą Co-op Translator API, todėl galite pradėti nuo CLI, vėliau automatizuoti su Python ir pristatyti tas pačias galimybes MCP klientams, kai prireiks agentų valdomų darbo eigų.