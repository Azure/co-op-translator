# Python API

Stabilni javni Python vmesnik (API) je izvezen iz `co_op_translator.api`. Večina integracij uporablja enega od teh potekov:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Prevedi posamezne datoteke ali dokumente | Vaša aplikacija prebere izvorno vsebino, pokliče Co-op Translator za prevod in odloči, kam shraniti rezultat. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Pripravi vsebino za prevod s strani gostiteljskega agenta | Vaš MCP gostitelj ali model aplikacije bo prevedel koščke, medtem ko Co-op Translator poskrbi za razdelitev in rekonstrukcijo. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Prevedi celoten repozitorij | Želite, da se Python API obnaša kot CLI in obvladuje odkrivanje, izhodne poti, metapodatke, čiščenje in pisanja. | `run_translation` |

Večina nižjenivojskih modulov pod `core`, `config`, `review` in `utils` je implementacijske podrobnosti, ki jih uporabljajo ti vstopni API-ji.

MCP odjemalci uporabljajo isti javni API preko [MCP Server](mcp.md). Uporabite to stran, ko kličete Python neposredno, in MCP vodnik, ko izpostavljate Co-op Translator agentu ali urejevalniku. Če se odločate med CLI, Python API in MCP, začnite z [Izberite svoj potek dela](workflows.md).

## Prvi potek uporabe API-ja

Začnite tukaj, če kličete Co-op Translator iz Pythona:

1. Konfigurirajte ponudnika LLM tako, kot je opisano v [Configuration](configuration.md), razen če pripravljate samo Markdown ali notebook koščke za prevod s strani gostiteljskega agenta.
2. Odločite, ali vaša aplikacija upravlja z datotečnim I/O.
3. Uporabite vsebinske API-je, ko vaša aplikacija bere in zapisuje posamezne datoteke.
4. Uporabite `run_translation`, ko naj Co-op Translator obdela repozitorij podobno kot CLI.
5. Uporabite `run_review` po prevajanju, če potrebujete deterministične kontrole v avtomatizaciji.

| Goal | API to start with |
| --- | --- |
| Prevedi en Markdown niz ali datoteko | `translate_markdown_content` |
| Prevedi en notebook payload | `translate_notebook_content` |
| Prevedi eno sliko | `translate_image_content` |
| Dovolite gostiteljskemu agentu, da prevede Markdown ali notebook koščke | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Prepišite prevedene povezave po izbiri izhodne poti | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Prevedi celoten repozitorij | `run_translation` |
| Preglej prevedeno izhodno vsebino | `run_review` |

## Scenarij 1: Prevedi posamezne datoteke ali dokumente

Uporabite ta potek, ko že imate datoteko, vsebnik urejevalnika, notebook payload, MCP zahtevo ali lasten vhod za cevovod (pipeline). Vaša koda upravlja datotečni I/O:

1. Preberite izvorno vsebino.
2. Pokličite API za prevajanje vsebine.
3. Po želji pokličite API za prepisovanje poti, če bo prevedena vsebina zapisana v mapo projekta za prevode.
4. Shrani ali vrni rezultat iz vaše aplikacije.

Vsebinski API-ji za prevajanje ne izvajajo odkrivanja projekta, ne zapisujejo metapodatkov, ne dodajajo obvestil in samodejno ne prepisujejo povezav.

### Datoteka Markdown

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

Če prevedeni Markdown ne bo v Co-op Translator postavitvi projekta, preskočite `rewrite_markdown_paths` in shranite prevedeni niz neposredno.

### Datoteka zvezka

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

`translate_notebook_content` prevede Markdown celice in ohranja ne-Markdown celice. Prepisovanje poti se uporablja samo za Markdown celice.

### Datoteka slike

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

`translate_image_content` prebere izvorno sliko in vrne renderirano `PIL.Image.Image`. Ne zapisuje prevedenih metapodatkov slike.

## Scenarij 2: Prevedi celoten repozitorij

Uporabite ta potek, ko želite, da se Python API obnaša kot `translate` CLI. `run_translation` odkrije podprte datoteke, prevede izbrane vrste vsebin, prepiše poti, zapiše izhodne datoteke, posodobi metapodatke in izvede vzdrževalna opravila prevajanja, kot je čiščenje.

`run_translation` je prednostna vstopna točka za orkestracijo projektov. `translate_project` je izvezen kot združljivostni vzdevek z enakim vedenjem.

Prevedite Markdown datoteke v trenutnem repozitoriju v korejščino in japonščino:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Prevedite samo notebooke iz določene korenske mape projekta:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Predogled obsega prevajanja brez zapisovanja datotek:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Zabeležite strukturirane dogodke napredka za integracijo:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Shrani vsebino v svojo tabelo dogodkov opravila ali jo pretoči v uporabniški vmesnik.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Dogodki uporabljajo verzionirano shemo `co-op.translation.event.v1`. Integracije bi morale
se opirati na stabilna polja, kot sta `type` in `stage_key`, ne na uporabniku namenjeno
konzolno besedilo ali `stage_label`.

Prevedite več korenin vsebine v enem klicu:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Zapišite prevode v eksplicitne izhodne skupine:

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

Uporabite označbo (placeholder) na jezik, kadar naj vsak jezik vsebuje gnezdeno podmapo:

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

Če nobena od možnosti `markdown`, `notebook` ali `images` ni nastavljena, API prevede vse podprte vrste: Markdown, notebooke in slike.

### Ohrani sprejete ročne spremembe z zagotavljalcem stanja prevoda

Privzeto Co-op Translator ohranja svoje obstoječe vedenje na ravni datotek: ko je
izvorni Markdown zastarel, se celotna prevedena datoteka znova ustvari. Gostovane
integracije lahko opcijsko posredujejo `TranslationStateProvider`, da ohranijo ročne
ureditve v izvornih blokih, ki se niso spremenili.

Ponudnik zagotovi zadnji sprejeti par izvor/cilj in zabeleži vsak nov
kandidat. Sprejem ostaja odgovornost integracije—na primer,
po združitvi pull requesta za prevod:

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

Za Markdown datoteke s veljavno sprejeto osnovo, Co-op Translator poravna
vrhnje nivojske Markdown bloke. Nespremenjeni izvorni bloki ponovno uporabijo trenutne prevedene
bloke, vključno z ročnimi popravki; spremenjeni ali dodani izvorni bloki se pošljejo
v prevod; izbrisani izvorni bloki so odstranjeni. Če je poravnava dvoumna,
se je struktura cilja spremenila, je prevod bloka neveljaven ali ni na voljo nobene osnove,
se Co-op Translator varno vrne na obstoječi postopek prevajanja celotne datoteke.



segmentne prevodne pomnilnike. Trenutno velja za prevajanje Markdown projektov.
Vedenje za notebooke in slike ostaja nespremenjeno. Posredovanje `update=True`
še vedno zahteva popolno regeneracijo.

Če eno ali več datotek ni mogoče prevesti, `run_translation` sproži
`RuntimeError` po zaključku poteka dela projekta namesto poročanja o
uspešnem izvajanju z manjkajočim izhodom. Integracije bi morale to obravnavati kot neuspešno
nalogo in obdržati prejšnje sprejeto stanje prevoda.

## Pregled prevedenega izhoda

`run_review` izvaja deterministične kontrole prevoda brez LLM ali Vision poverilnic.

!!! note "Beta"
    `run_review` je beta deterministični API za pregledovanje. Ne kliče ponudnikov modelov ali zapisuje datotek, vendar se lahko preverjanja in sheme težav spreminjajo.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Po prevodu, ki je omejen na README, uporabite isti obseg za pregled:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` pregleda samo `README.md` v vsaki konfigurirani izvorni korenski mapi,
vključno s prilagojenimi `groups` in izhodnimi mapami. Drugi dokumenti in gnezdene
README datoteke so izključene. Manjkajoče izvorno README sproži `ValueError`; neuspešna
preverjanja prevoda povzročijo `RuntimeError`.

Preglejte samo datoteke, spremenjene glede na osnovno referenco in izpišite izhod v GitHub slogu:

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

## Primeri API-jev za kopiranje in lepljenje

Prevedite vsebino Markdown brez zapisovanja datotek:

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

Prevedite in prepišite povezave v Markdownu:

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

Prevedite repozitorij z Pythona:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Prevedite več korenskih map:

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

Ohranite izraze slovarja:

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

## Javne vstopne točke

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

## API-ji za prevajanje vsebine

API-ji za prevajanje vsebine so namenjeni integracijam, ki že imajo vsebino v pomnilniku, na primer razširitvi urejevalnika, orodju MCP, procesorju zvezkov ali prilagojenemu cevovodu.

| Funkcija | Vhod | Izhod | Datotečni I/O | Opombe |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Ne | Asinhrono. Prevede samo vsebino Markdown. Ne prepisuje povezav, ne zapisuje metapodatkov in ne dodaja izjav o omejitvah. |
| `translate_notebook_content` | Notebook JSON `str` ali `dict` | Notebook JSON `str` | Ne | Asinhrono. Prevede Markdown celice in ohranja ne-Markdown celice. Ne prepisuje povezav, ne zapisuje metapodatkov in ne dodaja izjav o omejitvah. |
| `translate_image_content` | Pot do slike | `PIL.Image.Image` | Prebere samo izvorno sliko | Sinhrono. Izvleče in prevede besedilo slike, nato vrne upodobljeno sliko. Ne shrani metapodatkov prevedene slike. |

`translate_markdown_content` in `translate_notebook_content` sprejmeta izbirno `source_path` skozi svoje možnosti. Pot se posreduje kot kontekst prevajalcu; klicatelji ostanejo odgovorni za morebitno projektno-specifično prepisovanje poti po prevodu.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Enake možnosti je mogoče posredovati kot slovarji:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API-ji za prevajanje z agentno pomočjo

API-ji z agentno pomočjo ne kličejo konfiguriranega ponudnika LLM v Co-op Translatorju. Pripravijo kose Markdowna ali zvezka za gostiteljskega agenta, da jih prevede, nato pa rekonstruirajo končno vsebino iz prevedenih kosov.

| Funkcija | Namen |
| --- | --- |
| `start_markdown_agent_translation` | Vrne samostojno Markdown opravilo s kosi, pozivi in stanjem rekonstrukcije. |
| `finish_markdown_agent_translation` | Rekonstruira Markdown iz opravila in kosov, prevedenih s strani gostiteljskega agenta. |
| `start_notebook_agent_translation` | Vrne opravilo zvezka s kosi Markdown celic za prevod s strani gostiteljskega agenta. |
| `finish_notebook_agent_translation` | Rekonstruira JSON zvezka ob ohranitvi kodnih celic, izhodov in metapodatkov. |

Ta potek dela je predvsem namenjen gostiteljem MCP. Če potrebujete prevod repozitorija v produkciji, pri katerem Co-op Translator upravlja klice ponudnikov, uporabite `translate_markdown_content`, `translate_notebook_content` ali `run_translation`.

## API-ji za prepisovanje poti

API-ji za prepisovanje poti ne izvajajo prevodov. Posodabljajo povezave in poti v frontmatterju potem, ko klicatelji poznajo izvorno pot, prevedeno ciljno pot in postavitev projekta.

| Funkcija | Obseg | Opombe |
| --- | --- | --- |
| `rewrite_markdown_paths` | Telo Markdowna in frontmatter | Prepiše povezave v Markdownu in podprta polja poti v frontmatterju za prevedeno ciljno mesto. |
| `rewrite_notebook_paths` | Markdown celice v JSON zvezka | Uporablja prepisovanje poti v Markdownu za vsako Markdown celico in pusti ne-Markdown celice nespremenjene. |

Argument `policy` je lahko slovar z naslednjimi polji:

| Polje | Obvezno | Namen |
| --- | --- | --- |
| `language_code` | Da | Koda ciljanega jezika, na primer `"ko"` ali `"pt-BR"`. |
| `root_dir` | Ne | Izvorna korenska mapa projekta. Privzeto `"."`. |
| `translations_dir` | Ne | Izhodna mapa za prevedeno besedilo. Privzeto `translations` pod `root_dir`. |
| `translated_images_dir` | Ne | Izhodna mapa za prevedene slike. Privzeto `translated_images` pod `root_dir`. |
| `translation_types` | Ne | Omogočeni tipi prevajanja. Privzeto Markdown, zvezki in slike. |
| `lang_subdir` | Ne | Izbirna podmapa v vsaki mapi jezika. |

## Parametri prevajanja projekta

| Parameter | Tip | Privzeto | Namen |
| --- | --- | --- | --- |
| `language_codes` | `str` | Obvezno | Ciljne jezikovne kode ločene s presledki, na primer `"ko ja fr"` ali `"all"`. Nadomestne kode se normalizirajo v kanonične vrednosti BCP 47. |
| `root_dir` | `str` | `"."` | Korenska mapa projekta za en prevodni cilj. Prezrto, ko so podani `root_dirs` ali `groups`. |
| `update` | `bool` | `False` | Izbriše in znova ustvari obstoječe prevode za izbrane jezike. |
| `images` | `bool` | `False` | Vključi prevajanje slik. Zahteva konfiguracijo Azure AI Vision. |
| `markdown` | `bool` | `False` | Vključi prevajanje Markdowna. |
| `notebook` | `bool` | `False` | Vključi prevajanje Jupyter zvezkov. |
| `debug` | `bool` | `False` | Omogoči debug beleženje. |
| `save_logs` | `bool` | `False` | Shrani datoteke dnevnika ravni DEBUG v korenski imenik `logs/`. |
| `yes` | `bool` | `True` | Samodejno potrdi pozive za programatično rabo in CI. |
| `add_disclaimer` | `bool` | `False` | Dodaj izjave o strojnih prevodih v prevedene Markdown datoteke in zvezke. |
| `translations_dir` | `str \| None` | `None` | Po meri določena izhodna mapa za prevedeno besedilo. Relativne poti se razrešijo glede na vsako korensko mapo. |
| `image_dir` | `str \| None` | `None` | Po meri določena izhodna mapa za prevedene slike. Relativne poti se razrešijo glede na vsako korensko mapo. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Več korenskih map, ki delijo iste izhodne nastavitve. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Izrecni pari `(root_dir, translations_dir)`. Ima prednost pred `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL repozitorija, uporabljen pri upodabljanju navodil za tabelo jezikov v README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Izrazi slovarja, ki naj ostanejo ohranjeni med prevodom. Podvojeni in prazni vnosi se normalizirajo. |
| `dry_run` | `bool` | `False` | Oceni obseg prevajanja in prikaže predogled migracijskega vedenja brez zapisovanja datotek. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Izbiren adapter za trajno shranjevanje accepted-baseline in candidate stanj za inkrementalne posodobitve Markdowna. Če ga izpustite, se ohrani obstoječe vedenje obdelave celotnih datotek. |

## Parametri pregleda

`run_review` namensko zrcali podpis `run_translation`, kjer je mogoče, tako da lahko avtomatizacija preklaplja med prevajalskimi in preglednimi poteki z minimalnim razvejanjem.

| Parameter | Tip | Privzeto | Namen |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Ciljne mape jezikov za pregled. Sprejemajo se nizi, ločeni s presledki, in iterabilni tipi. `"all"` pregleda vse odkrite jezike prevodov. |
| `root_dir` | `str` | `"."` | Korenska mapa projekta za en cilj pregleda. Ignorirano, ko so podani `root_dirs` ali `groups`. |
| `markdown` | `bool` | `False` | Vključi izvorne datoteke Markdown in MDX. |
| `notebook` | `bool` | `False` | Vključi izvorne datoteke Jupyter zvezkov. |
| `images` | `bool` | `False` | Rezervirano za skladnost z možnostmi prevajanja. Sklici na slike se preverjajo v Markdown datotekah. |
| `translations_dir` | `str \| None` | `None` | Po meri določena izhodna mapa za prevedeno besedilo. Relativne poti se razrešijo glede na vsako korensko mapo. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Več korenskih map, ki delijo enake izhodne nastavitve. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Izrecni pari `(root_dir, translations_dir)`. Ima prednost pred `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git referenca, uporabljena za omejitev pregleda na spremenjene izvorne datoteke. |
| `readme_only` | `bool` | `False` | Preglej samo `README.md` v vsaki izvorni korenski mapi. Manjkajoči izvorni README sproži `ValueError`. |
| `output_format` | `str` | `"text"` | Format izhoda pregleda. Podprte vrednosti so `"text"` in `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Obravnavaj opozorila kot neuspehe poleg napak. |
| `debug` | `bool` | `False` | Omogoči debug zapisovanje dnevnika. |
| `save_logs` | `bool` | `False` | Shrani dnevniške datoteke na ravni DEBUG v korensko mapo `logs/`. |

Če nobena izmed možnosti `markdown`, `notebook` ali `images` ni nastavljena, API pregleda Markdown, zvezke in sklice na slike, kjer je primerno. Pregled ne kliče ponudnika LLM in ne zahteva API ključev.

## Zahteve konfiguracije

Prevajalski API-ji, ki temeljijo na ponudnikih, zahtevajo konfiguracijo ponudnika pred prevajanjem:

- Prevodi Markdowna in zvezkov zahtevajo ponudnika LLM. Konfigurirajte Azure OpenAI, OpenAI ali Anthropic.
- Prevajanje slik poleg ponudnika LLM zahteva Azure AI Vision.
- `run_translation` izvede lahke preglede povezljivosti, preden se začne prevajanje projekta.
- API-ji z asistenco agenta `start_*_agent_translation` in `finish_*_agent_translation` ne kličejo Co-op Translator LLM ponudnikov. Gostiteljska aplikacija ali MCP agent prevede pripravljene koščke.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` in `run_review` so deterministični in ne zahtevajo poverilnic ponudnika.

Zahtevane spremenljivke za Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Zahtevane spremenljivke za OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Zahtevane spremenljivke za Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` in `ANTHROPIC_MAX_TOKENS` sta izbirni. Microsoft Agent Framework je privzeti modelni odjemalec za vse ponudnike od različice Co-op Translator 0.22.0 naprej. Semantic Kernel je še vedno mogoče začasno izbrati z `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, vendar to sproži opozorilo o odstranitvi; glejte [configuration](configuration.md#model-client-backend) za načrt postopne odstranitve.

Zahtevane spremenljivke Azure AI Vision za prevajanje slik:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` je determinističen in ne zahteva konfiguracije LLM ali Azure AI Vision.

## Opombe o vedenju

- API-ji za prevajanje vsebin ločijo prevajanje od prepisovanja poti projekta. Kličite `rewrite_markdown_paths` ali `rewrite_notebook_paths` izrecno, ko je treba pri prevedeni vsebini prilagoditi povezave relativno na projekt za ciljno lokacijo.
- API-ji za orkestracijo projektov dodajo vedenje projekta okoli prevajanja vsebin, vključno z iskanjem datotek, pisanjem, prepisovanjem poti, metapodatki, čiščenjem in neobveznimi izjavami.
- `run_translation` izpiše povzetke napredka in ocen prek istega Rich-podprtih poročevalca, ki ga uporablja CLI. Neinteraktivni izhod preide na navaden tekst.
- `dry_run=True` izračuna ocene z uporabo virtualnih posodobitev README, vendar ne zapiše README ali prevodnih datotek.
- `groups` se obdelujejo zaporedno. Pred pričetkom dela se izpiše ena združena ocena.
- Ko je izbran prevod slik, bo manjkajoča Vision konfiguracija sprožila napako pred začetkom prevajanja.
- Obstoječe jezikovne mape, ki temeljijo na aliasih, se zaznajo in jih je mogoče kot del izvajanja migrirati v kanonična imena jezikovnih map.
- `run_review` ne uspe ob manjkajočih prevedenih datotekah, manjkajočih ali zastarelih prevodnih metapodatkih, nepravilnem Markdown frontmatterju/oznaki za kodo ter neveljavnem JSON-u prevedenega zvezka.
- `run_review` po privzetku poroča o manjkajočih lokalnih ciljih Markdowna in povezavah do slik kot opozorila.

## Notranja klicna pot

API delegira na isto osnovno implementacijo, ki jo uporablja CLI:

Prevajanje:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, ali `translate_image_content` za prevajanje v pomnilniku.
2. `co_op_translator.api.translation.rewrite_markdown_paths` ali `rewrite_notebook_paths` za izrecno post-obdelavo poti.
3. `co_op_translator.api.translation.run_translation` za polno orkestracijo projekta.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Osredotočeni mixini za prevajanje projektov za Markdown, zvezke in slike.
8. Prevajalci za Markdown, zvezke, besedilo in slike v `co_op_translator.core`.

Pregled:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministični pregledi pod `co_op_translator.review.checks`

Naslednji razredi so koristni za vzdrževalce, vendar niso izpostavljeni kot stabilen API na ravni paketa.

| Razred | Modul | Odgovornost |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinira prevajanje na ravni projekta, upravljanje imenikov, normalizacijo metapodatkov na jezik in delegiranje prevajalcem za Markdown, zvezke in slike. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Izvaja asinhrono obdelavo datotek za Markdown, zvezke, slike, zaznavanje zastarelosti in posodobitve prevodnih metapodatkov. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestrira branje Markdown datotek, prevajanje vsebine, prepisovanje poti, metapodatke, izjave in zapisovanje. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestrira branje zvezkov, prevajanje Markdown celic, prepisovanje poti, metapodatke, izjave in zapisovanje. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestrira odkrivanje izvornih slik, prevajanje slik, izhodne poti, metapodatke in zapisovanje. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Poišče pare prevedenih Markdown datotek, oceni kakovost prevoda in prebere metapodatke o zaupanju za delovne tokove popravil z nizkim zaupanjem. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinira deterministične preglede čez izvorne datoteke, ciljne jezike in konfigurirane prevodne korene. |
| `ReviewTarget` | `co_op_translator.review.targets` | Opisuje izvorno korensko mapo in izhodno mapo prevodov, ki se pregleda za to korenino. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Zazna stare jezikovne mape z aliasi in pripravi načrte za migracijo v kanonične BCP 47 mape. |
| `Config` | `co_op_translator.config.base_config` | Naloži `.env` datoteke in preveri, ali so zahtevani LLM in izbirni Vision ponudniki konfigurirani. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Samodejno zazna Azure OpenAI, OpenAI ali Anthropic, preveri zahtevane okoljske spremenljivke in izvede preglede povezljivosti ponudnikov. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Zazna konfiguracijo Azure AI Vision in izvede preglede povezljivosti za prevajanje slik. |