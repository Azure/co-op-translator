# Python API

Stabilni javni Python API izvezen je iz `co_op_translator.api`. Većina integracija koristi jedan od ovih tijekova rada:

| Scenarij | Koristite kada | Glavni API-ji |
| --- | --- | --- |
| Prevedite pojedinačne datoteke ili dokumente | Vaša aplikacija čita izvorni sadržaj, poziva Co-op Translator za prijevod i odlučuje gdje spremiti rezultat. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Pripremite sadržaj za prijevod host-agenta | Vaš MCP host ili model aplikacije će prevoditi fragmente, dok Co-op Translator upravlja razbijanjem na fragmente i njihovom rekonstrukcijom. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Prevedite cijeli repozitorij | Želite da se Python API ponaša kao CLI i obrađuje pronalaženje, izlazne putove, metapodatke, čišćenje i pisanje. | `run_translation` |

Većina nižerazinskih modula pod `core`, `config`, `review` i `utils` su implementacijski detalji koje koriste ove ulazne točke API-ja.

MCP klijenti koriste isti javni API preko [MCP poslužitelja](mcp.md). Koristite ovu stranicu kada pozivate Python izravno, a MCP vodič kada izlažete Co-op Translator agentu ili uređivaču. Ako odlučujete između CLI-ja, Python API-ja i MCP-a, započnite s [Odaberite svoj tijek rada](workflows.md).

## Prvi tijek rada s API-jem

Počnite ovdje ako pozivate Co-op Translator iz Python koda:

1. Konfigurirajte davatelja LLM-a kako je opisano u [Konfiguracija](configuration.md), osim ako samo pripremate Markdown ili dijelove bilježnice za prijevod host-agenta.
2. Odlučite hoće li vaša aplikacija upravljati ulazno-izlazom datoteka.
3. Koristite API-je za sadržaj kad vaša aplikacija čita i zapisuje pojedinačne datoteke.
4. Koristite `run_translation` kada Co-op Translator treba obraditi repozitorij poput CLI-ja.
5. Koristite `run_review` nakon prijevoda ako trebate determinističke provjere u automatizaciji.

| Cilj | API za početak |
| --- | --- |
| Prevedite jedan Markdown niz ili datoteku | `translate_markdown_content` |
| Prevedite jedan sadržaj bilježnice | `translate_notebook_content` |
| Prevedite jednu sliku | `translate_image_content` |
| Dopustite host-agentu da prevodi Markdown ili fragmente bilježnice | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Prepišite prevedene poveznice nakon odabira izlazne putanje | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Prevedite cijeli repozitorij | `run_translation` |
| Pregledajte prevedeni izlaz | `run_review` |

## Scenarij 1: Prevođenje pojedinačnih datoteka ili dokumenata

Koristite ovaj tijek rada kada već imate datoteku, međuspremnik urednika, sadržaj bilježnice, MCP zahtjev ili prilagođeni ulaz cjevovoda. Vaš kod upravlja ulazno-izlaznim operacijama datoteka:

1. Pročitajte izvorni sadržaj.
2. Pozovite API za prijevod sadržaja.
3. Po potrebi pozovite API za prepisivanje putanja ako će prevedeni sadržaj biti zapisan u mapu prijevoda projekta.
4. Spremite ili vratite rezultat iz vaše aplikacije.

API-ji za prijevod sadržaja ne pokreću otkrivanje projekata, ne zapisuju metapodatke, ne dodaju odricanja i ne prepisuju poveznice automatski.

### Markdown datoteka

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

Ako prevedeni Markdown neće biti u rasporedu projekta Co-op Translatora, preskočite `rewrite_markdown_paths` i spremite prevedeni niz izravno.

### Datoteka bilježnice

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

`translate_notebook_content` prevodi Markdown ćelije i zadržava ne-Markdown ćelije. Prepisivanje putanja primjenjuje se samo na Markdown ćelije.

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

`translate_image_content` čita izvornu sliku i vraća renderiranu `PIL.Image.Image`. Ne zapisuje metapodatke prevedene slike.

## Scenarij 2: Prevođenje cijelog repozitorija

Koristite ovaj tijek rada kada želite da se Python API ponaša kao `translate` CLI. `run_translation` pronalazi podržane datoteke, prevodi odabrane vrste sadržaja, prepisuje putanje, zapisuje izlazne datoteke, ažurira metapodatke i obavlja zadatke održavanja prijevoda poput čišćenja.

`run_translation` je preporučena ulazna točka za orkestraciju projekta. `translate_project` je izvezen kao alias radi kompatibilnosti s istim ponašanjem.

Prevedite Markdown datoteke u trenutnom repozitoriju na korejski i japanski:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Prevedite samo bilježnice iz određenog korijena projekta:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Pregledajte obujam prijevoda bez pisanja datoteka:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Evidentirajte strukturirane događaje napretka za integraciju:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Pohranite payload u tablicu događaja zadatka ili ga streamajte u svoje korisničko sučelje.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Događaji koriste verzioniranu shemu `co-op.translation.event.v1`. Integracije bi trebale
se oslanjati na stabilna polja kao što su `type` i `stage_key`, a ne na tekst namijenjen korisnicima
konzole ili `stage_label`.

Prevedite više korijena sadržaja jednim pozivom:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Zapišite prijevode u eksplicitne izlazne grupe:

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

Koristite zamjenski znak po jeziku kada svaki jezik treba sadržavati ugniježđeni poddirektorij:

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

Ako nijedan od `markdown`, `notebook` ili `images` nije postavljen, API prevodi sve podržane vrste: Markdown, bilježnice i slike.

### Sačuvajte prihvaćene ljudske izmjene pomoću pružatelja stanja prijevoda

Po zadanoj postavci, Co-op Translator zadržava svoje postojeće ponašanje na razini datoteke: kada
izvorni Markdown zastari, cijela prevedena datoteka se ponovno generira. Hostirane
integracije mogu opcionalno proslijediti `TranslationStateProvider` kako bi zadržale ljudske
izmjene u izvornih blokovima koji se nisu promijenili.

Pružatelj osigurava zadnji prihvaćeni par izvor/cilj i bilježi svaki novi
kandidat. Prihvaćanje ostaje odgovornost integracije—na primjer,
nakon što je pull request prijevoda spojen:

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

Za Markdown datoteke s valjanom prihvaćenom osnovom, Co-op Translator usklađuje
vršne Markdown blokove. Nepromijenjeni izvorni blokovi ponovno koriste trenutne prevedene
blokove, uključujući izmjene koje su napravili ljudi; promijenjeni ili dodani izvorni blokovi se šalju
na prijevod; izbrisani izvorni blokovi se uklanjaju. Ako je usklađivanje dvoumno,
ciljna struktura se promijenila, prijevod bloka je nevažeći, ili nema osnovne linije
dostupne, Co-op Translator sigurno vraća na postojeći cijelo-datotečni
put prijevoda.

Ovaj API pohranjuje stanje prijevoda dokumenta, a ne među-dokumentnu memoriju fraza ili
segmenta prijevoda. Trenutno se primjenjuje na prijevod Markdown projekata.
Ponašanje bilježnica i slika je nepromijenjeno. Prosljeđivanje `update=True`
još uvijek zahtijeva potpunu regeneraciju.

Ako jedna ili više datoteka ne mogu biti prevedene, `run_translation` baca
`RuntimeError` nakon što tijek rada projekta završi umjesto da prijavi
uspješan tijek s nedostajućim izlazom. Integracije bi to trebale smatrati neuspjelim
zadatkom i zadržati prethodno prihvaćeno stanje prijevoda.

## Pregled prevedenog izlaza

`run_review` izvodi determinističke provjere prijevoda bez LLM ili Vision vjerodajnica.

!!! note "Beta"
    `run_review` je beta deterministički API za pregled. Ne poziva pružatelje modela niti zapisuje datoteke, ali provjere i sheme problema se mogu mijenjati.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Nakon prijevoda samo README-a, upotrijebite isti opseg za pregled:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` pregleda samo `README.md` unutar svakog konfiguriranog izvornog korijena,
uključujući prilagođene `groups` i izlazne mape. Ostali dokumenti i ugniježđeni
README-ovi su isključeni. Nedostajući izvorni README podiže `ValueError`; neuspjele
provjere prijevoda podižu `RuntimeError`.

Pregledaj samo datoteke promijenjene u odnosu na osnovni ref i ispiši izlaz u GitHub formatu:

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

## Primjeri API-ja za kopiranje i lijepljenje

Prevedi Markdown sadržaj bez zapisivanja datoteka:

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

Prevedi i prepiši Markdown poveznice:

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

Prevedi repozitorij iz Pythona:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Prevedi više korijena:

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

Sačuvaj termine iz glosara:

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

## Javne ulazne točke

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

## API-ji za prijevod sadržaja

API-ji za prijevod sadržaja namijenjeni su integracijama koje već imaju sadržaj u memoriji, kao što su proširenje uređivača, MCP alat, procesor bilježnica ili prilagođeni tijek obrade.

| Funkcija | Ulaz | Izlaz | Rad s datotekama | Napomene |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Asinkrono. Prevodi samo Markdown sadržaj. Ne prepisuje poveznice, ne zapisuje metapodatke niti ne dodaje izjave o odricanju odgovornosti. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Asinkrono. Prevodi Markdown ćelije i čuva ne-Markdown ćelije. Ne prepisuje poveznice, ne zapisuje metapodatke niti ne dodaje izjave o odricanju odgovornosti. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Čita samo izvornu sliku | Sinkrono. Izdvaja i prevodi tekst sa slike, zatim vraća renderiranu sliku. Ne sprema metapodatke prevedene slike. |

`translate_markdown_content` i `translate_notebook_content` prihvaćaju opcionalni `source_path` kroz svoje opcije. Putanja se prosljeđuje kao kontekst prevoditelju; pozivatelji i dalje snose odgovornost za bilo kakvo prepisivanje putanja specifično za projekt nakon prijevoda.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Iste opcije mogu se proslijediti kao rječnici:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API-ji za prijevod uz pomoć agenta

API-ji uz pomoć agenta ne pozivaju konfiguriranog pružatelja LLM iz Co-op Translatora. Oni pripremaju Markdown ili dijelove bilježnice za prevođenje od strane host-agenta, a zatim rekonstruiraju konačni sadržaj iz prevedenih dijelova.

| Funkcija | Svrha |
| --- | --- |
| `start_markdown_agent_translation` | Vraća samostalan Markdown zadatak s dijelovima, promptovima i stanjem za rekonstrukciju. |
| `finish_markdown_agent_translation` | Rekonstruira Markdown iz zadatka i dijelova koje je preveo host-agent. |
| `start_notebook_agent_translation` | Vraća zadatak za bilježnicu s dijelovima Markdown-ćelija za prevođenje od strane host-agenta. |
| `finish_notebook_agent_translation` | Rekonstruira notebook JSON uz očuvanje kodnih ćelija, izlaza i metapodataka. |

Ovaj tijek rada je uglavnom namijenjen MCP hostovima. Ako trebate produkcijski prijevod repozitorija pri kojem Co-op Translator upravlja pozivima pružatelja, koristite `translate_markdown_content`, `translate_notebook_content` ili `run_translation`.

## API-ji za prepisivanje putanja

API-ji za prepisivanje putanja ne obavljaju prijevod. Oni ažuriraju poveznice i putanje u frontmatteru nakon što pozivatelji znaju izvornu putanju, prevedenu ciljnu putanju i izgled projekta.

| Funkcija | Opseg | Napomene |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown tijelo i frontmatter | Prepisuje Markdown poveznice i podržana polja putanja u frontmatteru za prevedenu ciljnu lokaciju. |
| `rewrite_notebook_paths` | Markdown ćelije u notebook JSON-u | Primjenjuje prepisivanje Markdown putanja na svaku Markdown ćeliju i ostavlja ne-Markdown ćelije nepromijenjenima. |

Argument `policy` može biti rječnik s ovim poljima:

| Polje | Obavezno | Svrha |
| --- | --- | --- |
| `language_code` | Da | Kod ciljnog jezika, poput `"ko"` ili `"pt-BR"`. |
| `root_dir` | Ne | Korijen izvornog projekta. Zadano je `"."`. |
| `translations_dir` | Ne | Direktorij za izlaz prevedenog teksta. Zadano je `translations` unutar `root_dir`. |
| `translated_images_dir` | Ne | Direktorij izlaza prevedenih slika. Zadano je `translated_images` unutar `root_dir`. |
| `translation_types` | Ne | Omogućeni tipovi prijevoda. Zadano su Markdown, bilježnice i slike. |
| `lang_subdir` | Ne | Opcionalni poddirektorij ispod svake mape jezika. |

## Parametri prijevoda projekta

| Parametar | Tip | Zadano | Svrha |
| --- | --- | --- | --- |
| `language_codes` | `str` | Obavezno | Kodovi ciljanih jezika odvojeni razmakom, na primjer `"ko ja fr"`, ili `"all"`. Alias kodovi se normaliziraju u kanonske BCP 47 vrijednosti. |
| `root_dir` | `str` | `"."` | Korijen projekta za jedinstveni cilj prijevoda. Ignorira se kada su zadani `root_dirs` ili `groups`. |
| `update` | `bool` | `False` | Izbriši i ponovno stvori postojeće prijevode za odabrane jezike. |
| `images` | `bool` | `False` | Uključi prijevod slika. Zahtijeva konfiguraciju Azure AI Vision. |
| `markdown` | `bool` | `False` | Uključi prijevod Markdowna. |
| `notebook` | `bool` | `False` | Uključi prijevod Jupyter bilježnica. |
| `debug` | `bool` | `False` | Omogući debug zapisivanje (logiranje). |
| `save_logs` | `bool` | `False` | Spremi log datoteke razine DEBUG pod glavnim direktorijem `logs/`. |
| `yes` | `bool` | `True` | Automatski potvrdi upite za programsko i CI korištenje. |
| `add_disclaimer` | `bool` | `False` | Dodaj odricanja o strojnom prevođenju u prevedeni Markdown i bilježnice. |
| `translations_dir` | `str \| None` | `None` | Prilagođeni direktorij izlaza za prijevod teksta. Relativne putanje se rješavaju u odnosu na svaki korijen. |
| `image_dir` | `str \| None` | `None` | Prilagođeni direktorij izlaza za prevedene slike. Relativne putanje se rješavaju u odnosu na svaki korijen. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Više korijenskih direktorija koji dijele iste postavke izlaza. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Izričiti parovi `(root_dir, translations_dir)`. Imaju prednost nad `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL spremišta koji se koristi pri prikazu uputa tablice jezika u README-u. |
| `glossaries` | `Iterable[str] \| None` | `None` | Pojmovi iz rječnika koje treba sačuvati tijekom prevođenja. Duplikati i prazni pojmovi se normaliziraju. |
| `dry_run` | `bool` | `False` | Procijeni opseg prijevoda i pregledaj ponašanje migracije bez zapisivanja datoteka. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Opcionalni adapter za perzistenciju prihvaćene osnovne verzije i kandidata za inkrementalne ažuriranja Markdowna. Izostavljanje zadržava postojeće ponašanje za cijele datoteke. |

## Parametri pregleda

`run_review` namjerno odražava potpis `run_translation` gdje je moguće tako da automatizacija može prebacivati između tijekova rada prijevoda i pregleda s minimalnim grananjem.

| Parametar | Tip | Zadano | Svrha |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Ciljne mape jezika za pregled. Prihvaćaju se nizovi razdvojeni razmakom i iterabilni tipovi. `"all"` pregleda svaki otkriveni jezik prijevoda. |
| `root_dir` | `str` | `"."` | Korijen projekta za jedan cilj pregleda. Ignorira se kada su zadani `root_dirs` ili `groups`. |
| `markdown` | `bool` | `False` | Uključi izvorne Markdown i MDX datoteke. |
| `notebook` | `bool` | `False` | Uključi izvorne Jupyter bilježnice. |
| `images` | `bool` | `False` | Rezervirano radi usklađenosti s opcijama prijevoda. Reference veza na slike provjeravaju se iz Markdowna. |
| `translations_dir` | `str \| None` | `None` | Prilagođeni direktorij izlaza za prijevod teksta. Relativne putanje se rješavaju u odnosu na svaki korijen. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Više korijenskih direktorija koji dijele iste postavke izlaza. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Izričiti parovi `(root_dir, translations_dir)`. Imaju prednost nad `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref koji se koristi za ograničavanje pregleda na promijenjene izvorne datoteke. |
| `readme_only` | `bool` | `False` | Pregledava samo `README.md` pod svakim izvornim korijenom. Nedostajući izvorni README izaziva `ValueError`. |
| `output_format` | `str` | `"text"` | Format izlaza pregleda. Podržane vrijednosti su `"text"` i `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Tretiraj upozorenja kao neuspjehe uz pogreške. |
| `debug` | `bool` | `False` | Omogući debug zapisivanje (logging). |
| `save_logs` | `bool` | `False` | Spremi DEBUG razine log datoteke u korijenski direktorij `logs/`. |

Ako nijedan od `markdown`, `notebook` ili `images` nije postavljen, API pregledava Markdown, bilježnice i reference veza na slike gdje je primjenjivo. Pregled ne poziva LLM providera i ne zahtijeva API ključeve.

## Zahtjevi konfiguracije

API-ji za prijevod koji se oslanjaju na providere zahtijevaju konfiguraciju providera prije prevođenja:

- Prevođenje Markdowna i bilježnica zahtijeva LLM providera. Konfigurirajte Azure OpenAI, OpenAI ili Anthropic.
- Prevođenje slika zahtijeva Azure AI Vision uz LLM providera.
- `run_translation` izvodi lagane provjere povezanosti prije nego što započne prijevod projekta.
- Agentom podržani API-ji `start_*_agent_translation` i `finish_*_agent_translation` ne pozivaju Co-op Translator LLM providere. Host aplikacija ili MCP agent prevodi pripremljene dijelove.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` i `run_review` su deterministički i ne zahtijevaju vjerodajnice providera.

Obavezne Azure OpenAI varijable:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Obavezne OpenAI varijable:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Obavezne Anthropic varijable:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` i `ANTHROPIC_MAX_TOKENS` su opcionalni. Microsoft Agent Framework je zadani klijent modela za sve providere počevši s Co-op Translator 0.22.0. Semantic Kernel se još uvijek može privremeno odabrati s `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, ali to uzrokuje upozorenje o zastarijevanju; vidi [configuration](configuration.md#model-client-backend) za plan postupnog uklanjanja.

Obavezne Azure AI Vision varijable za prevođenje slika:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` je deterministički i ne zahtijeva konfiguraciju LLM-a ili Azure AI Vision.

## Napomene o ponašanju

- API-ji za prijevod sadržaja odvajaju prijevod od prepisivanja putanja projekta. Pozovite `rewrite_markdown_paths` ili `rewrite_notebook_paths` izričito kad prevedeni sadržaj treba prilagoditi veze relativne prema projektu za ciljnu lokaciju.
- API-ji za orkestraciju projekta dodaju ponašanje projekta oko prevođenja sadržaja, uključujući otkrivanje datoteka, pisanja, prepisivanje putanja, metapodatke, čišćenje i opcionalna odricanja.
- `run_translation` ispisuje sažetke napretka i procjene kroz istog Rich-backed reportera kojeg koristi CLI. Neinteraktivni izlaz se vraća na običan tekst.
- `dry_run=True` izračunava procjene koristeći virtualne nadopune README-a, ali ne zapisuje README ili datoteke prijevoda.
- `groups` se obrađuju sekvencijalno. Jedna agregirana procjena se ispisuje prije početka rada.
- Kad je odabran prijevod slika, nedostajuća Vision konfiguracija podiže grešku prije početka prijevoda.
- Postojeće jezične mape temeljene na aliasima se detektiraju i mogu se migrirati na kanonična imena mapa jezika kao dio izvođenja.
- `run_review` ne uspijeva kod nedostajućih prevedenih datoteka, nedostajućih ili zastarjelih metapodataka prijevoda, neispravnog Markdown frontmattera/zagrada za kod i nevažećeg prevedenog notebook JSON-a.
- `run_review` prijavljuje nedostajuće lokalne Markdown i ciljeve veza na slike kao upozorenja prema zadanim postavkama.

## Interni put poziva

API delegira na istu osnovnu implementaciju koju koristi CLI:

Prijevod:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Fokusirani prijevodni miksini za Markdown, bilježnice i slike.
8. Markdown, bilježnica, tekst i prevoditelji slika u okviru `co_op_translator.core`.

Pregled:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Determinističke provjere pod `co_op_translator.review.checks`

Sljedeće klase su korisne održavateljima, ali nisu izvezene kao stabilni API na razini paketa.

| Klasa | Modul | Odgovornost |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Koordinira prijevod na razini projekta, upravljanje direktorijima, normalizaciju metapodataka po jeziku i delegiranje Markdown, bilježnica i prevoditeljima slika. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Obavlja asinkroni rad obrade datoteka za Markdown, bilježnice, slike, otkrivanje zastarjelosti i ažuriranja metapodataka prijevoda. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orkestrira čitanje Markdown datoteka, prijevod sadržaja, prepisivanje putanja, metapodatke, odricanja i zapisivanje. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orkestrira čitanje datoteka bilježnica, prijevod Markdown-celija, prepisivanje putanja, metapodatke, odricanja i zapisivanje. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orkestrira otkrivanje izvora slika, prijevod slika, izlazne putanje, metapodatke i zapisivanje. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Pronalazi prevedene Markdown parove, ocjenjuje kvalitetu prijevoda i čita metapodatke o povjerenju za popravne tijekove niske pouzdanosti. |
| `ReviewRunner` | `co_op_translator.review.runner` | Koordinira determinističke provjere pregleda preko izvornih datoteka, ciljnih jezika i konfiguriranih korijenskih direktorija prijevoda. |
| `ReviewTarget` | `co_op_translator.review.targets` | Opisuje izvorni korijen i direktorij izlaza prijevoda koji se pregledava za taj korijen. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Otkriva naslijeđene alias jezične mape i priprema planove migracije na kanonične BCP 47 mape. |
| `Config` | `co_op_translator.config.base_config` | Učitava `.env` datoteke i provjerava jesu li obavezni LLM i opcionalni Vision provideri konfigurirani. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Automatski detektira Azure OpenAI, OpenAI ili Anthropic, provjerava potrebne varijable okoline i izvodi provjere povezivosti providera. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detektira Azure AI Vision konfiguraciju i izvodi provjere povezivosti za prevođenje slika. |