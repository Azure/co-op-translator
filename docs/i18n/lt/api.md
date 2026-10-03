# Python API

Stabili viešoji Python API eksportuojama iš `co_op_translator.api`. Dauguma integracijų naudoja vieną iš šių darbo eigų:

| Scenarijus | Naudokite, kai | Pagrindinės API |
| --- | --- | --- |
| Versti atskirus failus arba dokumentus | Jūsų programa perskaito šaltinio turinį, iškviečia Co-op Translator vertimui ir nusprendžia, kur išsaugoti rezultatą. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Paruošti turinį host-agento vertimui | Jūsų MCP host'as arba programos modelis verčia fragmentus, o Co-op Translator rūpinasi fragmentavimu ir rekonstrukcija. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Versti visą repozitoriją | Norite, kad Python API elgtųsi kaip CLI ir atliktų aptikimą, išvesties kelių nustatymą, metaduomenų atnaujinimą, švarinimą ir įrašymus. | `run_translation` |

Dauguma žemesnio lygio modulių `core`, `config`, `review` ir `utils` yra įgyvendinimo detalės, naudojamos šiems API įėjimo taškams.

MCP klientai naudoja tą pačią viešą API per [MCP Server](mcp.md). Naudokite šį puslapį, kai kviečiate Python tiesiogiai, o MCP vadovą — kai eksponuojate Co-op Translator agentui arba redaktoriui. Jei renkatės tarp CLI, Python API ir MCP, pradėkite nuo [Pasirinkite savo darbo eigą](workflows.md).

## Pradinė API eiga

Pradėkite čia, jei kviečiate Co-op Translator iš Python kodo:

1. Konfigūruokite LLM tiekėją kaip aprašyta [Konfigūracija](configuration.md), nebent ruošiate tik Markdown ar užrašų knygelės fragmentus host-agento vertimui.
2. Nuspręskite, ar jūsų programa valdo failų I/O.
3. Naudokite turinio API, kai jūsų programa skaito ir rašo atskirus failus.
4. Naudokite `run_translation`, kai Co-op Translator turėtų apdoroti repozitoriją kaip CLI.
5. Naudokite `run_review` po vertimo, jei automatizacijoje reikia deterministinių patikrinimų.

| Tikslas | API, nuo kurio pradėti |
| --- | --- |
| Išversti vieną Markdown eilutę arba failą | `translate_markdown_content` |
| Išversti vienos užrašų knygelės turinį | `translate_notebook_content` |
| Išversti vieną vaizdą | `translate_image_content` |
| Leisti hosto agentui išversti Markdown arba notebook fragmentus | `start_markdown_agent_translation` arba `start_notebook_agent_translation` |
| Perrašyti išverstus nuorodus po išvesties kelio pasirinkimo | `rewrite_markdown_paths` arba `rewrite_notebook_paths` |
| Išversti visą repozitoriją | `run_translation` |
| Peržiūrėti išverstą išvestį | `run_review` |

## Scenarijus 1: Versti atskirus failus arba dokumentus

Naudokite šią darbo eigą, kai jau turite failą, redaktoriaus buferį, notebook turinį, MCP užklausą arba pasirinktą vamzdyno įvestį. Jūsų kodas valdo failų I/O:

1. Perskaitykite šaltinio turinį.
2. Iškvieskite turinio vertimo API.
3. Pasirinktinai iškvieskite kelio perrašymo API, jei išverstas turinys bus įrašytas į projekto vertimų aplanką.
4. Išsaugokite arba grąžinkite rezultatą iš savo programos.

Turinio vertimo API neatlieka projekto aptikimo, neįrašo metaduomenų, neprideda atsakomybės prierašų ir automatiškai neperrašo nuorodų.

### Markdown failas

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Jei išverstas Markdown nebus talpinamas Co-op Translator projekto struktūroje, praleiskite `rewrite_markdown_paths` ir išsaugokite išverstą eilutę tiesiogiai.

### Notebook failas

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` verčia Markdown langelius ir išsaugo ne-Markdown langelius. Kelio perrašymas taikomas tik Markdown langeliams.

### Vaizdo failas

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` perskaito šaltinio vaizdą ir grąžina renderintą `PIL.Image.Image`. Ji neįrašo išversto vaizdo metaduomenų.

## Scenarijus 2: Versti visą repozitoriją

Naudokite šią darbo eigą, kai norite, kad Python API elgtųsi kaip `translate` CLI. `run_translation` aptinka palaikomus failus, išverčia pasirinktus turinio tipus, perrašo kelius, įrašo išvesties failus, atnaujina metaduomenis ir atlieka vertimo priežiūros užduotis, tokias kaip švarinimas.

`run_translation` yra pageidaujamas projekto orkestravimo įėjimo taškas. `translate_project` eksportuojamas kaip suderinamumo aliasas su tokiu pačiu elgesiu.

Išverskite Markdown failus esamoje repozitorijoje į korėjiečių ir japonų kalbas:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Versti tik užrašų knygeles iš nurodyto projekto šaknies:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Peržiūrėti vertimo apimtį neįrašant failų:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Įrašyti struktūruotus pažangos įvykius integracijai:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Išsaugokite payload savo job-event lentelėje arba srautu perduokite jį į vartotojo sąsają.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Įvykiai naudoja versijuotą schemą `co-op.translation.event.v1`. Integracijos turėtų
pasikliauti stabiliais laukais, tokiais kaip `type` ir `stage_key`, o ne žmogui skirtu
konsolės tekstu ar `stage_label`.

Išversti kelis turinio šaknius vienu kvietimu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Įrašyti vertimus į aiškiai nurodytas išvesties grupes:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Naudokite kalbai skirtą vietos rezervavimo žymeklį, kai kiekviena kalba turėtų turėti įdėtą poaplankį:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

Jei `markdown`, `notebook` arba `images` nėra nustatyti, API išverčia visus palaikomus tipus: Markdown, užrašų knygeles ir vaizdus.

### Išsaugoti priimtus žmonių redagavimus naudojant vertimo būsenos tiekėją

Pagal numatytuosius nustatymus Co-op Translator išlaiko esamą elgesį failo lygiu: kai
Markdown šaltinis yra pasenęs, visas išverstas failas regeneruojamas. Priglobtos
integracijos gali pasirinktinai perduoti `TranslationStateProvider`, kad išsaugotų žmonių
redagavimus šaltinio blokuose, kurie nepasikeitė.

Tiekėjas pateikia paskutinę priimtą šaltinio/tikslo porą ir įrašo kiekvieną naują
kandidatai. Priėmimas lieka integracijos atsakomybė – pavyzdžiui,
po to, kai vertimo pull request'as yra sujungtas:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

Markdown failams, turintiems galiojančią priimtą bazinę versiją, Co-op Translator sulygina
aukščiausio lygio Markdown blokus. Nepakeisti šaltinio blokai pakartotinai naudoja esamus išverstus
blokus, įskaitant žmonių atliktus redagavimus; pakeisti arba pridėti šaltinio blokai siunčiami
vertimui; ištrinti šaltinio blokai pašalinami. Jei derinimas neaiškus,
tikslinė struktūra pasikeitė, bloko vertimas yra neteisingas arba nėra bazinės versijos,
Co-op Translator saugiai grįžta prie esamo pilno failo
vertimo kelio.

Ši API saugo dokumento vertimo būseną, o ne tarp-dokumentinę frazių ar
segmentų vertimo atmintį. Šiuo metu taikoma Markdown projekto
vertimui. Užrašų knygelių ir vaizdų elgsena nepakinta. Perdavimas `update=True`
vis tiek prašo visiškos regeneracijos.

Jei vienas ar daugiau failų negali būti išversti, `run_translation` meta
`RuntimeError` po to, kai projekto darbo eiga baigiasi, vietoje to, kad praneštų apie
sėkmingą vykdymą su trūkstama išvestimi. Integracijos turėtų traktuoti tai kaip nepavykusį
užduotį ir išlaikyti ankstesnę priimtą vertimo būseną.

## Peržiūrėti išverstą išvestį

`run_review` atlieka deterministinius vertimo patikrinimus be LLM ar Vision kredencialų.

!!! note "Beta"
    `run_review` yra beta deterministinis peržiūros API. Jis nekviečia modelių tiekėjų ar neįrašo failų, tačiau patikrinimai ir problemų schemos gali keistis.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Po tik README vertimo naudokite tą patį peržiūros mastą:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` peržiūri tik `README.md` kiekvienoje sukonfigūruotoje šaltinio šaknyje,
įskaitant pasirinktinius `groups` ir išvesties katalogus. Kiti dokumentai ir įdėti
README failai yra neįtraukti. Trūkstamas šaltinio README sukelia `ValueError`; nepavykę
vertimo patikrinimai meta `RuntimeError`.

Peržiūrėkite tik failus, pakeistus lyginant su baziniu ref, ir atspausdinkite GitHub formato išvestį:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Kopijuokite-ir-klijuokite API pavyzdžiai

Išversti Markdown turinį neįrašant failų:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Išversti ir perrašyti Markdown nuorodas:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Išversti repozitoriją iš Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Išversti kelias šaknis:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Išsaugoti žodyno terminus:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Viešieji įėjimo taškai

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Turinio vertimo API

Turinio vertimo API skirtos integracijoms, kurios jau turi turinį atmintyje, pavyzdžiui redaktoriaus priedui, MCP įrankiui, notebook apdorojimo modulį ar pasirinktinei vamzdyno daliai.

| Funkcija | Įvestis | Išvestis | Failų I/O | Pastabos |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Ne | Asinchroninė. Išverčia tik Markdown turinį. Ji neperrašo nuorodų, neįrašo metaduomenų ir neprideda atsakomybės prierašų. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Ne | Asinchroninė. Išverčia Markdown langelius ir išsaugo ne-Markdown langelius. Ji neperrašo nuorodų, neįrašo metaduomenų ir neprideda atsakomybės prierašų. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Skaito tik šaltinio vaizdą | Sinchroninė. Ištraukia ir išverčia vaizdo tekstą, tada grąžina renderintą vaizdą. Ji neįrašo išversto vaizdo metaduomenų. |

`translate_markdown_content` ir `translate_notebook_content` priima pasirenkamą `source_path` per jų parinktis. Kelias perduodamas kaip kontekstas vertėjui; kvietėjai lieka atsakingi už bet kokį projekto specifinį kelio perrašymą po vertimo.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Tos pačios parinktys gali būti perduotos kaip žodynai:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agentų padedamos vertimo API

Agentų padedamos API nekviečia sukonfigūruoto LLM tiekėjo iš Co-op Translator. Jos paruošia Markdown arba notebook fragmentus hosto agentui išversti, tada rekonstruoja galutinį turinį iš išverstų fragmentų.

| Funkcija | Paskirtis |
| --- | --- |
| `start_markdown_agent_translation` | Grąžina savarankišką Markdown užduotį su fragmentais, užklausomis ir rekonstrukcijos būsena. |
| `finish_markdown_agent_translation` | Rekonstruoti Markdown iš užduoties ir hosto agento išverstų fragmentų. |
| `start_notebook_agent_translation` | Grąžina notebook užduotį su Markdown langelių fragmentais hosto agento vertimui. |
| `finish_notebook_agent_translation` | Rekonstruoti notebook JSON išsaugant kodo langelius, rezultatus ir metaduomenis. |

Ši darbo eiga skirta daugiausia MCP hostams. Jei jums reikia produkcinio repozitorijos vertimo, kai Co-op Translator valdo tiekėjų kvietimus, naudokite `translate_markdown_content`, `translate_notebook_content` arba `run_translation`.

## Kelio perrašymo API

Kelio perrašymo API neatlieka vertimo. Jos atnaujina nuorodas ir frontmatter kelius, kai kvietėjai žino šaltinio kelią, išverstą tikslinį kelią ir projekto išdėstymą.

| Funkcija | Aprėptis | Pastabos |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown turinys ir frontmatter | Perrašo Markdown nuorodas ir palaikomus frontmatter kelio laukus išverstam tikslui. |
| `rewrite_notebook_paths` | Markdown langeliai notebook JSON'e | Taiko Markdown kelio perrašymą kiekvienam Markdown langeliui ir palieka ne-Markdown langelius nepakitusius. |

`policy` argumentas gali būti žodynas su šiais laukais:

| Laukas | Reikalinga | Paskirtis |
| --- | --- | --- |
| `language_code` | Taip | Tikslinės kalbos kodas, pavyzdžiui `"ko"` arba `"pt-BR"`. |
| `root_dir` | Ne | Šaltinio projekto šakninis katalogas. Pagal numatytuosius: `"."`. |
| `translations_dir` | Ne | Teksto vertimų išvesties katalogas. Pagal nutylėjimą `translations` po `root_dir`. |
| `translated_images_dir` | Ne | Išverstų vaizdų išvesties katalogas. Pagal nutylėjimą `translated_images` po `root_dir`. |
| `translation_types` | Ne | Įjungti vertimo tipai. Pagal nutylėjimą Markdown, užrašų knygelės ir vaizdai. |
| `lang_subdir` | Ne | Pasirenkamas poskatalogas kiekviename kalbos aplanke. |

## Projekto vertimo parametrai

| Parametras | Tipas | Numatytoji reikšmė | Paskirtis |
| --- | --- | --- | --- |
| `language_codes` | `str` | Privaloma | Tarpais atskirti tikslinių kalbų kodai, pavyzdžiui `"ko ja fr"`, arba `"all"`. Alias kodai normalizuojami į kanonines BCP 47 reikšmes. |
| `root_dir` | `str` | `"."` | Projekto šakninis katalogas vienam vertimo tikslui. Ignoruojamas, kai pateikiami `root_dirs` arba `groups`. |
| `update` | `bool` | `False` | Ištrina ir iš naujo sukuria esamus vertimus pasirinktomis kalbomis. |
| `images` | `bool` | `False` | Įtraukti vaizdų vertimą. Reikalauja Azure AI Vision konfigūracijos. |
| `markdown` | `bool` | `False` | Įtraukti Markdown vertimą. |
| `notebook` | `bool` | `False` | Įtraukti Jupyter užrašų knygelės vertimą. |
| `debug` | `bool` | `False` | Įjungti derinimo žurnalavimą. |
| `save_logs` | `bool` | `False` | Išsaugoti DEBUG lygio žurnalo failus pagrindiniame `logs/` kataloge. |
| `yes` | `bool` | `True` | Automatiškai patvirtinti raginimus programiniam naudojimui ir CI. |
| `add_disclaimer` | `bool` | `False` | Pridėti mašininio vertimo atsakomybės apribojimus prie išverstų Markdown ir užrašų knygelių. |
| `translations_dir` | `str \| None` | `None` | Specialus teksto vertimo išvesties katalogas. Santykiniai keliai sprendžiami pagal kiekvieną šaknį. |
| `image_dir` | `str \| None` | `None` | Specialus išverstų vaizdų išvesties katalogas. Santykiniai keliai sprendžiami pagal kiekvieną šaknį. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Kelios šaknys, kurios dalijasi tais pačiais išvesties nustatymais. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Aiškūs `(root_dir, translations_dir)` porų rinkiniai. Teikiama pirmenybė prieš `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Saugyklos URL naudojamas pateikiant README kalbų lentelės instrukcijas. |
| `glossaries` | `Iterable[str] \| None` | `None` | Žodyno terminai, kuriuos reikia išsaugoti vertimo metu. Pasikartojimai ir tušti terminai normalizuojami. |
| `dry_run` | `bool` | `False` | Įvertinti vertimo apimtį ir peržiūrėti migracijos elgesį neišrašant failų. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Pasirenkamas priimto bazinio ir kandidato išsaugojimo adapteris inkrementiniams Markdown atnaujinimams. Jo nepateikimas išlaiko esamą viso failo elgesį. |

## Peržiūros parametrai

`run_review` specialiai atitinka `run_translation` parašo struktūrą, kai tik įmanoma, kad automatikai būtų lengviau perjungti vertimo ir peržiūros darbo srautus su minimaliu šakų skaičiumi.

| Parametras | Tipas | Numatytasis | Paskirtis |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Tikslinės kalbų aplankai peržiūrai. Priimami tarpu atskirti stringai ir iteruojami objektai. `"all"` peržiūri visas aptiktas vertimo kalbas. |
| `root_dir` | `str` | `"."` | Projekto šaknis vienam peržiūros tikslui. Ignoruojama kai pateikti `root_dirs` arba `groups`. |
| `markdown` | `bool` | `False` | Įtraukti Markdown ir MDX šaltinio failus. |
| `notebook` | `bool` | `False` | Įtraukti Jupyter užrašų knygelių šaltinio failus. |
| `images` | `bool` | `False` | Skirta suderinamumui su vertimo parinktimis. Nuorodų į vaizdus atitikmenys tikrinami iš Markdown. |
| `translations_dir` | `str \| None` | `None` | Specialus teksto vertimo išvesties katalogas. Santykiniai keliai sprendžiami pagal kiekvieną šaknį. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Kelios šaknys, kurios dalijasi tais pačiais išvesties nustatymais. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Aiškūs `(root_dir, translations_dir)` porų rinkiniai. Teikiama pirmenybė prieš `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref naudojama apriboti peržiūrą tik pakeistiems šaltinio failams. |
| `readme_only` | `bool` | `False` | Peržiūrėti tik `README.md` kiekvienoje šaltinio šaknyje. Trūkstantis šaltinio README sukelia `ValueError`. |
| `output_format` | `str` | `"text"` | Peržiūros išvesties formatas. Palaikomos reikšmės: `"text"` ir `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Vertinti įspėjimus kaip klaidas, be jau esančių klaidų. |
| `debug` | `bool` | `False` | Įjungti derinimo (debug) žurnalavimą. |
| `save_logs` | `bool` | `False` | Išsaugoti DEBUG lygio žurnalų failus po pagrindiniu `logs/` katalogu. |

Jei nei `markdown`, nei `notebook`, nei `images` nėra nustatyti, API peržiūri Markdown, užrašus ir vaizdų nuorodų atitikmenis, kur tai taikoma. Peržiūrai nereikia LLM paslaugų teikėjo ir API raktų.

## Konfigūracijos reikalavimai

Vertimo API, priklausomos nuo paslaugų teikėjų, reikalauja paslaugų teikėjo konfigūracijos prieš verčiant:

- Markdown ir užrašų knygelių vertimui reikalingas LLM paslaugų teikėjas. Konfigūruokite Azure OpenAI, OpenAI arba Anthropic.
- Vaizdų vertimui, be LLM paslaugų teikėjo, reikia ir Azure AI Vision.
- `run_translation` paleidžia lengvus jungties tikrinimus prieš pradedant projekto vertimą.
- Agentų pagalbinės `start_*_agent_translation` ir `finish_*_agent_translation` API nekviečia Co-op Translator LLM paslaugų teikėjų. Paruoštus fragmentus verčia host aplikacija arba MCP agentas.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` ir `run_review` yra deterministiniai ir nereikalauja paslaugų teikėjų kredencialų.

Būtini Azure OpenAI kintamieji:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Būtini OpenAI kintamieji:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Būtini Anthropic kintamieji:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` ir `ANTHROPIC_MAX_TOKENS` yra neprivalomi. Microsoft Agent Framework yra numatytasis modelio klientas visiems teikėjams pradedant su Co-op Translator 0.22.0. Semantic Kernel vis tiek galima laikinai pasirinkti naudojant `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, tačiau tai išmes pasenimo įspėjimą; žr. [konfigūracija](configuration.md#model-client-backend) dėl etapinio pašalinimo plano.

Būtini Azure AI Vision kintamieji vaizdų vertimui:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` yra deterministinis ir nereikalauja LLM ar Azure AI Vision konfigūracijos.

## Elgesio pastabos

- Turinio vertimo API laiko vertimą atskirai nuo projekto kelių perrašymo. Iškvieskite `rewrite_markdown_paths` arba `rewrite_notebook_paths` aiškiai, kai išverstas turinys reikalauja, kad projekto reliatyvios nuorodos būtų sureguliuotos pagal tikslinę vietą.
- Projekto orkestravimo API prideda projekto elgseną aplink turinio vertimą, įskaitant failų aptikimą, rašymą, kelių perrašymą, metaduomenis, valymą ir pasirenkamus atsakomybės pranešimus.
- `run_translation` spausdina pažangos ir įvertinimo santraukas per tą pačią Rich pagrįstą ataskaitų teikėją, kurią naudoja CLI. Neinteraktyvi išvestis pereina prie paprasto teksto.
- `dry_run=True` apskaičiuoja įverčius naudodamas virtualius README atnaujinimus, tačiau neišrašo README ar vertimo failų.
- `groups` apdorojami sekvenciškai. Vienas apibendrintas įvertis išspausdinamas prieš pradedant darbą.
- Kai pasirenkamas vaizdų vertimas, trūkstama Vision konfigūracija sukelia klaidą prieš pradedant vertimą.
- Aptinkami esami alias pagrindu sukurti kalbų aplankai ir juos galima perkelti į kanoninius BCP 47 kalbų aplankų pavadinimus kaip dalį vykdymo.
- `run_review` nepavyksta dėl trūkstamų išverstų failų, trūkstamų arba pasenusių vertimo metaduomenų, netaisyklingos Markdown frontmatter / kodo tvoros arba negaliojančio išversto užrašo knygelės JSON.
- `run_review` pagal numatytuosius nustatymus praneša apie trūkstamus vietinius Markdown ir vaizdų nuorodų tikslus kaip įspėjimus.

## Vidinis kvietimų kelias

API deleguoja tam pačiam pagrindiniam įgyvendinimui, kurį naudoja CLI:

Vertimas:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Sutelkti projekto vertimo mišiniai Markdown, užrašams ir vaizdams.
8. Markdown, užrašų, teksto ir vaizdų vertėjai po `co_op_translator.core`.

Peržiūra:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministiniai tikrinimai po `co_op_translator.review.checks`

Toliau išvardytos klasės naudingos priežiūrėtojams, bet jos nėra eksponuojamos kaip paketo lygmens stabilus API.

| Klasė | Modulis | Atsakomybė |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinuoja projekto lygmens vertimą, katalogų valdymą, metaduomenų normalizavimą kiekvienai kalbai ir delegavimą Markdown, užrašų ir vaizdų vertėjams. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Atlieka asinchroninį failų apdorojimą Markdown, užrašų, vaizdų, pasenusio turinio aptikimo ir vertimo metaduomenų atnaujinimų srityse. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Organizuoja Markdown failų nuskaitymą, turinio vertimą, kelių perrašymą, metaduomenis, atsakomybės pranešimus ir įrašymus. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Organizuoja užrašų knygelių failų nuskaitymą, Markdown langelių vertimą, kelių perrašymą, metaduomenis, atsakomybės pranešimus ir įrašymus. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Organizuoja šaltinio vaizdų aptikimą, vaizdų vertimą, išvesties kelius, metaduomenis ir įrašymus. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Randa išverstus Markdown poras, vertina vertimo kokybę ir skaito pasitikėjimo metaduomenis žemos pasitikėjimo taisymo darbo eigoms. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinuoja deterministinius peržiūros tikrinimus tarp šaltinio failų, tikslinių kalbų ir sukonfigūruotų vertimo šaknų. |
| `ReviewTarget` | `co_op_translator.review.targets` | Aprašo šaltinio šaknį ir vertimo išvesties katalogą, peržiūrėtą ta šakimi. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Aptinka senovinius alias pagrindu sukurtus kalbų aplankus ir paruošia kanoninių BCP 47 aplankų migracijos planus. |
| `Config` | `co_op_translator.config.base_config` | Įkelia `.env` failus ir tikrina, ar reikalingi LLM ir pasirenkami Vision paslaugų teikėjai yra sukonfigūruoti. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automatiškai aptinka Azure OpenAI, OpenAI arba Anthropic, tikrina būtinus aplinkos kintamuosius ir vykdo paslaugų teikėjo jungties patikrinimus. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Aptinka Azure AI Vision konfigūraciją ir vykdo jungties patikrinimus vaizdų vertimui. |