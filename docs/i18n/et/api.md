# Pythoni API

Püsiv avalik Pythoni API on eksporditud moodulist `co_op_translator.api`. Enamik integratsioone kasutab üht järgmistest töövoogudest:

| Stsenaarium | Kasutada, kui | Põhilised API-d |
| --- | --- | --- |
| Tõlgi üksikuid faile või dokumente | Teie rakendus loeb lähte sisu, kutsub Co-op Translatori tõlkimiseks ja otsustab, kuhu tulemuse salvestada. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Valmista sisu host-agendi tõlkimiseks | Teie MCP host või rakenduse mudel tõlgib tükke, samal ajal kui Co-op Translator tegeleb tükkide jagamise ja taasühendamisega. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Tõlgi kogu hoidla | Soovite, et Pythoni API käituks nagu CLI ning haldaks failide leidmist, väljundite teid, metaandmeid, puhastust ja kirjutamisi. | `run_translation` |

Enamik `core`, `config`, `review` ja `utils` alam-mooduleid on nende API sisenemispunktide rakenduslikud üksikasjad.

MCP kliendid kasutavad sama avalikku API-d läbi [MCP Server](mcp.md). Kasutage seda lehte, kui kutsute Pythoni otse, ja MCP juhendit, kui avaldate Co-op Translatori agendile või redaktorile. Kui otsustate CLI, Pythoni API ja MCP vahel, alustage [Vali oma töövoog](workflows.md).

## Esmane API töövoog

Alustage siit, kui kutsute Co-op Translatorit Pythoni koodist:

1. Konfigureerige LLM-pakkuja nagu kirjeldatud lehel [Configuration](configuration.md), välja arvatud juhul, kui valmistate ainult Markdowni või notebooki tükke host-agendi tõlkimiseks.
2. Otsustage, kas teie rakendus haldab failide sisend-/väljundit.
3. Kasutage sisu API-sid, kui teie rakendus loeb ja kirjutab üksikuid faile.
4. Kasutage `run_translation`, kui Co-op Translator peaks töötlema hoidlat nagu CLI.
5. Kasutage `run_review` pärast tõlget, kui vajate automatiseerimisel deterministlikke kontrolle.

| Eesmärk | Alguseks sobiv API |
| --- | --- |
| Tõlgi üks Markdowni string või fail | `translate_markdown_content` |
| Tõlgi ühe notebooki sisu | `translate_notebook_content` |
| Tõlgi üks pilt | `translate_image_content` |
| Laske host-agendil tõlkida Markdowni või notebooki tükke | `start_markdown_agent_translation` või `start_notebook_agent_translation` |
| Ümberkirjutada tõlgitud lingid pärast väljundtee valimist | `rewrite_markdown_paths` või `rewrite_notebook_paths` |
| Tõlgi kogu hoidla | `run_translation` |
| Kontrolli tõlgitud väljundit | `run_review` |

## Stsenaarium 1: Tõlgi üksikuid faile või dokumente

Kasutage seda töövoogu, kui teil on juba fail, redaktori puhver, notebooki sisu, MCP päring või kohandatud torujuhtme sisend. Teie kood haldab failide sisend-/väljundit:

1. Lugege lähte sisu.
2. Kutsuge sisu tõlke-API-d.
3. Vajadusel kutsuge tee ümberkirjutamise API, kui tõlgitud sisu kirjutatakse projekti tõlkekausta.
4. Salvestage või tagastage tulemus oma rakendusest.

Sisu tõlke-API-d ei käivita projekti avastamist, ei kirjuta metaandmeid, ei lisa vastutusklausleid ega kirjuta linke automaatselt ümber.

### Markdown-fail

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

Kui tõlgitud Markdown ei asu Co-op Translatori projekti paigutuses, jätke `rewrite_markdown_paths` vahele ja salvestage tõlgitud tekst otse.

### Notebook-fail

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

`translate_notebook_content` tõlgib Markdowni lahtrid ja säilitab mitte-Markdowni lahtrid. Teede ümberkirjutamist rakendatakse ainult Markdowni lahtritele.

### Pildifail

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

`translate_image_content` loeb lähtepildi ja tagastab renderdatud `PIL.Image.Image`. See ei kirjuta tõlgitud pildi metaandmeid.

## Stsenaarium 2: Tõlgi kogu hoidla

Kasutage seda töövoogu, kui soovite, et Pythoni API käituks nagu `translate` CLI. `run_translation` avastab toetatud failid, tõlgib valitud sisutüübid, ümberkirjutab teid, kirjutab väljundfaile, uuendab metaandmeid ja teostab tõlke hooldustöid nagu puhastus.

`run_translation` on eelistatud projekti orkestreerimise sisenemispunkt. `translate_project` on eksportitud ühilduvusaliasena sama käitumisega.

Tõlkige Markdown-failid praegusest hoidlast korea ja jaapani keelde:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Tõlgi ainult notebooke ühest kindlast projekti juurkataloogist:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Eelvaade tõlke mahule ilma failide kirjutamiseta:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Salvestage struktureeritud edenemise sündmused integratsiooni jaoks:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Salvesta sisu oma töö-sündmuste tabelisse või voogedasta see oma kasutajaliidesesse.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Sündmused kasutavad versioonitud skeemi `co-op.translation.event.v1`. Integratsioonid peaksid
tugineda stabiilsetele väljadele nagu `type` ja `stage_key`, mitte
konsoolitekstile ega `stage_label`.

Tõlkige mitu sisu juurkausta ühes kutses:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Kirjutage tõlked selgesse väljundgruppi:

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

Kasutage per-keele kohatäidet, kui igal keelel peaks olema pesastatud alamkataloog:

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

Kui ükski `markdown`, `notebook` või `images` pole seatud, tõlgib API kõik toetatud tüübid: Markdown, notebookid ja pildid.

### Säilitage aktsepteeritud inimeste muudatused tõlkeoleku pakkujaga

Vaikimisi hoiab Co-op Translator oma olemasolevat failitaseme käitumist: kui
Markdowni lähte sisu on aegunud, genereeritakse kogu tõlgitud fail uuesti. Hostitud
integratsioonid võivad valikuliselt edastada `TranslationStateProvider`-i, et säilitada inimeste
muudatusi lähteplokkides, mis pole muutunud.

Pakkuja esitab viimase aktsepteeritud lähte/siht paari ja salvestab iga uue
kandidaadi. Aktsepteerimine jääb integratsiooni vastutuseks—näiteks,
pärast tõlke pull requesti integreerimist:

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

Markdowni failide puhul, millel on kehtiv aktsepteeritud baasjoon, joondab Co-op Translator
tipp-taseme Markdown blokke. Muutumata lähteplokid taaskasutavad praeguseid tõlgitud
blokke, sh inimeste tehtud muudatusi; muudetud või lisatud lähteplokid saadetakse
tõlkimiseks; kustutatud lähteplokid eemaldatakse. Kui joondus on ebaselge,
sihtstruktuur muutus, bloki tõlge on kehtetu või baasjoont pole
saadaval, langeb Co-op Translator turvaliselt tagasi olemasolevale kogu faili
tõlke teele.

See API salvestab dokumendi tõlkeolekut, mitte dokumentidevahelist fraasi või
segmentide tõlkemälu. See kehtib hetkel Markdowni projekti
tõlkimisele. Notebooki ja pildi käitumine on muutumatu. `update=True`
edastamine taotleb siiski täielikku uuesti genereerimist.

Kui ühte või enamat faili ei õnnestu tõlkida, viskab `run_translation`
`RuntimeError` pärast projekti töövoo lõppu, selle asemel et teatada
õnnestunud jooksust, kus väljund puudub. Integratsioonid peaksid seda käsitlema kui ebaõnnestunud
tööülesannet ning säilitama eelmise aktsepteeritud tõlkeoleku.

## Tõlgitud väljundi ülevaatus

`run_review` käivitab deterministlikud tõlke kontrollid ilma LLMi või Visioni tõenditeta.

!!! note "Beeta"
    `run_review` on beeta-faasis deterministlik ülevaatus-API. See ei kutsu mudelipakkujaid ega kirjuta faile, kuid kontrollid ja probleemiskeemid võivad muutuda.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Pärast ainult README tõlget kasutage ülevaatuseks sama ulatust:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` kontrollib ainult iga konfigureeritud lähtejuure all olevat `README.md`-i,
sh kohandatud `groups`-e ja väljundkatalooge. Teised dokumendid ja pesastatud
README-d on välistatud. Puuduv lähte-README tekitab `ValueError`; ebaõnnestunud
tõlke kontrollide ebaõnnestumine viskab `RuntimeError`.

Kontrollige ainult faile, mis muutusid võrreldes baasrefiga, ja trükkige GitHub-stiilis väljund:

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

## Kopeeri-kleebi API näited

Tõlkige Markdowni sisu ilma failikirjutusteta:

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

Tõlkige ja kirjutage Markdowni lingid ümber:

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

Tõlkige hoidla Pythoni abil:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Tõlgi mitu juurkausta:

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

Säilitage sõnastiku terminid:

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

## Avalikud sisenemispunktid

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

## Sisu tõlke-API-d

Sisu tõlke-API-d on mõeldud integratsioonidele, millel on sisu juba mälus, näiteks redaktori laiendus, MCP tööriist, notebooki protsessor või kohandatud torujuhtme komponent.

| Funktsioon | Sisend | Väljund | Faili sisend-/väljund | Märkused |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Asünkroonne. Tõlgib ainult Markdowni sisu. See ei kirjuta linke ümber, ei kirjuta metaandmeid ega lisa vastutusklausleid. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Asünkroonne. Tõlgib Markdowni lahtrid ja säilitab mitte-Markdowni lahtrid. See ei kirjuta linke ümber, ei kirjuta metaandmeid ega lisa vastutusklausleid. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Ekstraheerib ja tõlgib pilditeksti, seejärel tagastab renderdatud pildi. See ei salvesta tõlgitud pildi metaandmeid. |

`translate_markdown_content` ja `translate_notebook_content` aktsepteerivad valikulist `source_path` oma valikute kaudu. See tee antakse tõlkijale kontekstina; kutsujad vastutavad endiselt kõigi projekti-spetsiifiliste teede ümberkirjutamise eest pärast tõlget.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Samad valikud saab edastada sõnastikena:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agendi abiga tõlke-API-d

Agendiabiga API-d ei kutsu Co-op Translatorist konfigureeritud LLM-pakkujat. Need valmistavad ette Markdowni või notebooki tükke, mida host-agent tõlgib, ja seejärel rekonstrueerivad lõpliku sisu tõlgitud tükkidest.

| Funktsioon | Eesmärk |
| --- | --- |
| `start_markdown_agent_translation` | Tagastab iseseisva Markdowni tööülesande koos tükkide, promptide ja rekonstruktsiooni olekuga. |
| `finish_markdown_agent_translation` | Rekonstrueerib Markdowni tööülesannest ja host-agendi tõlgitud tükkidest. |
| `start_notebook_agent_translation` | Tagastab notebooki tööülesande koos Markdowni lahtritükkidega host-agendi tõlkimiseks. |
| `finish_notebook_agent_translation` | Rekonstrueerib notebooki JSON-i säilitades koodilahtrid, väljundid ja metaandmed. |

See töövoog on peamiselt mõeldud MCP hostidele. Kui vajate tootmises hoidla tõlget, kus Co-op Translator haldab pakkuja kutsed, kasutage `translate_markdown_content`, `translate_notebook_content` või `run_translation`.

## Tee ümberkirjutamise API-d

Tee ümberkirjutamise API-d ei tee tõlget. Need uuendavad linke ja frontmatter'i teid pärast seda, kui kutsujad teavad lähte teed, tõlgitud sihtteed ja projekti paigutust.

| Funktsioon | Ulatus | Märkused |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Ümberkirjutab Markdowni lingid ja toetatud frontmatteri tee väljad tõlgitud sihtkoha jaoks. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Rakendab Markdowni teede ümberkirjutamist iga Markdowni lahtri jaoks ja jätab mitte-Markdowni lahtrid muutumatuks. |

Argument `policy` võib olla sõnastik järgmiste väljadega:

| Väli | Nõutud | Eesmärk |
| --- | --- | --- |
| `language_code` | Jah | Sihtkeele kood, näiteks `"ko"` või `"pt-BR"`. |
| `root_dir` | Ei | Allika projekti juur. Vaikimisi `"."`. |
| `translations_dir` | Ei | Teksttõlke väljundkataloog. Vaikimisi `translations` `root_dir` all. |
| `translated_images_dir` | Ei | Tõlgitud piltide väljundkataloog. Vaikimisi `translated_images` `root_dir` all. |
| `translation_types` | Ei | Lubatud tõlketüübid. Vaikimisi Markdown, notebookid ja pildid. |
| `lang_subdir` | Ei | Valikuline alamkataloog iga keelekausta all. |

## Projekti tõlke parameetrid

| Parameeter | Tüüp | Vaikeväärtus | Eesmärk |
| --- | --- | --- | --- |
| `language_codes` | `str` | Nõutud | Vahemärgiga eraldatud sihtkeelte koodid, nagu `"ko ja fr"`, või `"all"`. Aliaskoodid normaliseeritakse kanonilisteks BCP 47 väärtusteks. |
| `root_dir` | `str` | `"."` | Projekti juur ühe tõlkesihendi jaoks. Ignoreeritakse, kui on antud `root_dirs` või `groups`. |
| `update` | `bool` | `False` | Kustutab ja loob uuesti olemasolevad tõlked valitud keeltele. |
| `images` | `bool` | `False` | Kaasa piltide tõlkimine. Nõuab Azure AI Visioni konfiguratsiooni. |
| `markdown` | `bool` | `False` | Kaasa Markdowni tõlge. |
| `notebook` | `bool` | `False` | Kaasa Jupyteri notebooki tõlge. |
| `debug` | `bool` | `False` | Luba silumislogimine. |
| `save_logs` | `bool` | `False` | Salvesta DEBUG-taseme logifailid juurkausta `logs/` alla. |
| `yes` | `bool` | `True` | Automaatselt kinnitab viipasid programmeerliku ja CI-kasutuse jaoks. |
| `add_disclaimer` | `bool` | `False` | Lisa masintõlke lahtiütlusi tõlgitud Markdowni ja märkmike juurde. |
| `translations_dir` | `str \| None` | `None` | Kohandatud tekstitõlke väljundkataloog. Suhtelised teed lahendatakse iga juurkataloogi suhtes. |
| `image_dir` | `str \| None` | `None` | Kohandatud tõlgitud piltide väljundkataloog. Suhtelised teed lahendatakse iga juurkataloogi suhtes. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mitmed juurkataloogid, mis jagavad samu väljundseadeid. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Otsesed `(root_dir, translations_dir)` paarid. Neil on eelis `root_dirs` ees. |
| `repo_url` | `str \| None` | `None` | Repositooriumi URL, mida kasutatakse README keele tabeli juhendi renderdamisel. |
| `glossaries` | `Iterable[str] \| None` | `None` | Sõnastiku terminid, mida tõlkimise käigus säilitatakse. Duplikaadid ja tühjad terminid normaliseeritakse. |
| `dry_run` | `bool` | `False` | Hinda tõlke mahtu ja eelvaata migratsiooni käitumist ilma faile kirjutamata. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Valikuline aktsepteeritud-baasiline ja kandidaadi püsivusadapter inkrementaalsete Markdowni uuenduste jaoks. Selle välja jätmine säilitab olemasoleva kogu-faili käitumise. |

## Ülevaatamise parameetrid

`run_review` peegeldab tahtlikult `run_translation` signatuuri, kus võimalik, nii et automatiseerimine saab minimaalse tingimusloogikaga vahetada tõlke- ja ülevaatusvoogude vahel.

| Parameeter | Tüüp | Vaikimisi | Eesmärk |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Ülevaatamiseks sihtkeele kaustad. Aktsepteeritakse tühikuga eraldatud stringe ja iteratiive. `"all"` ülevaatab kõik leitud tõlkekeeli. |
| `root_dir` | `str` | `"."` | Projekti juur ühe ülevaatuse sihtmärgi jaoks. Ignoreeritakse, kui on määratud `root_dirs` või `groups`. |
| `markdown` | `bool` | `False` | Sisaldab Markdowni ja MDX-i lähtefaile. |
| `notebook` | `bool` | `False` | Sisaldab Jupyteri märkmike lähtefaile. |
| `images` | `bool` | `False` | Reserveeritud pariteedi huvides tõlkevalikutega. Pildi viiteid kontrollitakse Markdownist. |
| `translations_dir` | `str \| None` | `None` | Kohandatud tekstitõlke väljundkataloog. Suhtelised teed lahendatakse iga juurkataloogi suhtes. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mitmed juurkataloogid, mis jagavad samu väljundseadeid. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Otsesed `(root_dir, translations_dir)` paarid. Neil on eelis `root_dirs` ees. |
| `changed_from` | `str \| None` | `None` | Git ref, mida kasutatakse ülevaatuse piiramiseks muudetud lähtefailidele. |
| `readme_only` | `bool` | `False` | Ülevaatab ainult iga lähtejuure all olevat `README.md`-i. Puuduv lähte-README tekitab `ValueError`. |
| `output_format` | `str` | `"text"` | Ülevaatuse väljundi vorming. Toetatud väärtused on `"text"` ja `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Käsitle hoiatusi vigade kõrval ka ebaõnnestumistena. |
| `debug` | `bool` | `False` | Luba silumise logimine. |
| `save_logs` | `bool` | `False` | Salvesta DEBUG-taseme logifailid juurkataloogi `logs/` alla. |

Kui ükski `markdown`, `notebook` ega `images` pole seatud, siis API ülevaatab Markdowni, märkmikud ja pildi viited, kus see on asjakohane. Ülevaatus ei kutsu LLM-teenuse pakkujat ega nõua API-võtmeid.

## Konfiguratsiooni nõuded

Pakkuja-põhised tõlke-API-d nõuavad enne tõlkimist pakkuja konfiguratsiooni:

- Markdowni ja märkmiku tõlkimine nõuab LLM-teenuse pakkujat. Konfigureerige Azure OpenAI, OpenAI või Anthropic.
- Pildi tõlkimine nõuab LLM-teenuse pakkuja kõrval Azure AI Visioni.
- `run_translation` kontrollib kerget ühenduvust enne projekti tõlke alustamist.
- Agenti abiga `start_*_agent_translation` ja `finish_*_agent_translation` API-d ei kutsu Co-op Translator'i LLM-teenuse pakkujaid. Hostrakendus või MCP-agent tõlgib ettevalmistatud lõigud.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` ja `run_review` on deterministlikud ning ei vaja pakkuja mandaate.

Nõutavad Azure OpenAI muutujad:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Nõutavad OpenAI muutujad:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Nõutavad Anthropic muutujad:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` ja `ANTHROPIC_MAX_TOKENS` on valikulised. Alates Co-op Translator versioonist 0.22.0 on Microsoft Agent Framework vaikimisi mudeli klient kõigi pakkujate jaoks. Semantic Kernel'i saab ajutiselt valida `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` abil, kuid selle valimine annab deprekeerimishoiaku; vt [konfiguratsiooni](configuration.md#model-client-backend) et tutvuda etapilise eemaldamise plaaniga.

Pildi tõlkimiseks vajalikud Azure AI Vision muutujad:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` on deterministlik ja ei vaja LLM- ega Azure AI Vision konfiguratsiooni.

## Käitumise märkused

- Sisutõlke API-d hoiavad tõlke eraldi projekti teede ümberkirjutusest. Kutsuge otseselt `rewrite_markdown_paths` või `rewrite_notebook_paths`, kui tõlgitud sisu jaoks tuleb sihtkoha suhtelised lingid kohandada.
- Projekti orkestreerimise API-d lisavad projekti käitumise sisu tõlkimise ümber, sealhulgas failide leidmine, kirjutamine, teede ümberkirjutamine, metaandmed, puhastus ja valikulised lahtiütlused.
- `run_translation` kuvab edenemise ja hinnangute kokkuvõtted läbi sama Rich-põhise raportööri, mida kasutab CLI. Mitteinteraktiivne väljund kasutab lihtteksti.
- `dry_run=True` arvutab hinnanguid, kasutades virtuaalseid README uuendusi, kuid ei kirjuta README-d ega tõlkefaile.
- `groups` töödeldakse järjekorras. Üks kokkuvõtlik hinnang prinditakse enne töö algust.
- Kui on valitud pildi tõlkimine, siis puuduv Visioni konfiguratsioon viskab vea enne tõlkimise alustamist.
- Olemasolevad alias-põhised keelekaustad tuvastatakse ja neid saab jooksu käigus migreerida kanoniliste keelekaustade nimedeks.
- `run_review` ebaõnnestub kadunud tõlgitud failide, puuduvate või aegunud tõlke-metaandmete, valesti vormistatud Markdowni frontmatteri/koodiaedikute ning vigase tõlgitud märkmiku JSON-i korral.
- `run_review` teatab vaikimisi puuduvatest kohalikest Markdowni ja pildi viite sihtmärkidest hoiatustena.

## Sisemine kutsete rada

API delegeerib samale põhiteostusele, mida kasutab CLI:

Tõlkimine:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` mälus tehtava tõlke jaoks.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` eksplitsiitseks teede järeltöötluseks.
3. `co_op_translator.api.translation.run_translation` täielikuks projekti orkestreerimiseks.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Fookustatud projekti tõlke mixinid Markdowni, märkmike ja piltide jaoks.
8. Markdowni, märkmiku, teksti ja pildi tõlkijad `co_op_translator.core` all.

Ülevaatus:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministlikud kontrollid asuvad `co_op_translator.review.checks` all

Järgnevad klassid on hooldajatele kasulikud, kuid neid ei ekspordi paketi-taseme stabiilse API osana.

| Klass | Moodul | Vastutus |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordineerib projekti tasemel tõlget, kataloogi haldust, keelepõhist metaandmete normaliseerimist ning delegeerimist Markdowni, märkmiku ja pildi tõlkijatele. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Teostab asünkroonset failitöötlust Markdowni, märkmike, piltide, aegunud oleku tuvastamise ja tõlke metaandmete värskenduste jaoks. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestreerib Markdowni failide lugemist, sisu tõlkimist, teede ümberkirjutamist, metaandmeid, lahtiütlusi ja kirjutamist. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestreerib märkmikufailide lugemist, Markdown-rakkude tõlget, teede ümberkirjutamist, metaandmeid, lahtiütlusi ja kirjutamist. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestreerib lähte-piltide leidmist, pildi tõlget, väljundteid, metaandmeid ja kirjutamist. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Leiab tõlgitud Markdowni paarid, hindab tõlke kvaliteeti ja loeb usaldusmetaandmeid madala usaldusega parandustöövoogude jaoks. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordineerib deterministlikke ülevaatuse kontrolle lähtefailide, sihtkeelte ja konfigureeritud tõlkejuurte vahel. |
| `ReviewTarget` | `co_op_translator.review.targets` | Kirjeldab lähtejuurt ja selle juure jaoks ülevaadatud tõlkete väljundkataloogi. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Tuvastab pärandalias-keelekaustad ja valmistab ette kanoniliste BCP 47 kaustade migreerimiskavad. |
| `Config` | `co_op_translator.config.base_config` | Laeb `.env` faile ja kontrollib, kas vajalikud LLM- ja valikulised Vision-teenuse pakkujad on konfigureeritud. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Tuvastab automaatselt Azure OpenAI, OpenAI või Anthropic, valideerib nõutud keskkonnamuutujad ja käivitab pakkuja ühenduvuse kontrollid. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Tuvastab Azure AI Vision konfiguratsiooni ja käivitab ühenduvuse kontrollid pildi tõlkimiseks. |