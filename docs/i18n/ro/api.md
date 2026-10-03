# Python API

API-ul public stabil pentru Python este exportat din `co_op_translator.api`. Majoritatea integrărilor folosesc unul dintre aceste fluxuri de lucru:

| Scenariu | Când să folosești | API-uri principale |
| --- | --- | --- |
| Traduce fișiere sau documente individuale | Aplicația ta citește conținutul sursă, apelează Co-op Translator pentru traducere și decide unde să salveze rezultatul. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Pregătește conținut pentru traducerea de către agentul gazdă | Gazda MCP sau modelul aplicației tale va traduce fragmentele, în timp ce Co-op Translator se ocupă de fragmentare și reconstruire. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Traduce întregul repository | Vrei ca API-ul Python să se comporte ca CLI-ul și să gestioneze descoperirea, căile de ieșire, metadatele, curățarea și scrierile. | `run_translation` |

Majoritatea modulelor de nivel inferior din `core`, `config`, `review` și `utils` sunt detalii de implementare folosite de aceste puncte de intrare ale API-ului.

Clienții MCP folosesc același API public prin [MCP Server](mcp.md). Folosește această pagină când apelezi Python direct și ghidul MCP când expui Co-op Translator unui agent sau editor. Dacă decizi între CLI, API-ul Python și MCP, începe cu [Alege fluxul de lucru](workflows.md).

## Fluxul inițial al API-ului

Începeți aici dacă apelați Co-op Translator din cod Python:

1. Configurați un furnizor LLM așa cum este descris în [Configurare](configuration.md), cu excepția cazului în care pregătiți doar fragmente Markdown sau notebook pentru traducerea gazdă-agent.
2. Decideți dacă aplicația dvs. gestionează I/O pentru fișiere.
3. Folosiți API-urile de conținut când aplicația dvs. citește și scrie fișiere individuale.
4. Utilizați `run_translation` când Co-op Translator ar trebui să proceseze un repository la fel ca CLI-ul.
5. Utilizați `run_review` după traducere dacă aveți nevoie de verificări deterministe în automatizare.

| Obiectiv | API pentru început |
| --- | --- |
| Traduce un șir sau fișier Markdown | `translate_markdown_content` |
| Traduce un payload de notebook | `translate_notebook_content` |
| Traduce o imagine | `translate_image_content` |
| Permite unui agent gazdă să traducă fragmente Markdown sau de notebook | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rescrie linkurile traduse după ce alegi o cale de ieșire | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Traduce un repository complet | `run_translation` |
| Revizuiește rezultatul tradus | `run_review` |

## Scenariul 1: Traducerea fișierelor sau documentelor individuale

Utilizați acest flux de lucru când aveți deja un fișier, un buffer de editor, un payload de notebook, o cerere MCP sau un input pentru un pipeline personalizat. Codul dvs. deține operațiile de intrare/ieșire pe fișiere:

1. Read the source content.
2. Call a content translation API.
3. Apelați opțional un API de rescriere a căilor dacă conținutul tradus va fi scris într-un folder de traducere al proiectului.
4. Salvați sau returnați rezultatul din aplicația dvs.

API-urile de traducere a conținutului nu rulează descoperirea proiectului, nu scriu metadate, nu adaugă avertismente și nu rescriu link-urile automat.

### Fișier Markdown

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

Dacă Markdown-ul tradus nu va face parte din structura de proiect Co-op Translator, săriți `rewrite_markdown_paths` și salvați direct șirul tradus.

### Fișier Notebook

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

`translate_notebook_content` traduce celulele Markdown și păstrează celulele non-Markdown. Rescrierea căilor se aplică numai celulelor Markdown.

### Fișier Imagine

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

`translate_image_content` citește imaginea sursă și returnează un `PIL.Image.Image` redat. Nu scrie metadatele imaginii traduse.

## Scenariul 2: Traduceți întregul depozit

Utilizați acest flux de lucru când doriți ca API-ul Python să se comporte ca CLI-ul `translate`. `run_translation` detectează fișierele acceptate, traduce tipurile de conținut selectate, rescrie căile, scrie fișierele de ieșire, actualizează metadatele și efectuează sarcini de întreținere a traducerilor, cum ar fi curățarea.

`run_translation` este punctul de intrare preferat pentru orchestrarea proiectului. `translate_project` este exportat ca alias de compatibilitate cu același comportament.

Traduceți fișierele Markdown din depozitul curent în coreeană și japoneză:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Traduceți numai notebook-urile din rădăcina unui proiect specific:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Previzualizați volumul traducerii fără a scrie fișiere:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Înregistrați evenimente de progres structurate pentru o integrare:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Stochează payload-ul în tabelul job-event sau transmite-l către interfața ta UI.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Events use the versioned schema `co-op.translation.event.v1`. Integrations should
depend on stable fields such as `type` and `stage_key`, not on human-facing
console text or `stage_label`.

Traduceți mai multe rădăcini de conținut într-un singur apel:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Scrieți traducerile în grupuri de ieșire explicite:

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

Folosiți un marcator per limbă atunci când fiecare limbă ar trebui să conțină un subdirector încorporat:

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

Dacă niciuna dintre `markdown`, `notebook`, sau `images` nu este setată, API-ul traduce toate tipurile acceptate: Markdown, notebook-uri și imagini.

### Păstrați editările umane acceptate cu un furnizor de stare a traducerii

În mod implicit, Co-op Translator păstrează comportamentul său existent la nivel de fișier: când o
sursă Markdown este învechită, întregul fișier tradus este regenerat. Integrările găzduite
opțional pot transmite un `TranslationStateProvider` pentru a păstra
editările umane în blocurile sursă care nu s-au schimbat.

Furnizorul oferă ultima pereche sursă/țintă acceptată și înregistrează fiecare nou
candidat. Acceptarea rămâne responsabilitatea integrării—de exemplu,
după ce un pull request de traducere este îmbinat:

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

Pentru fișierele Markdown cu o bază de referință acceptată și validă, Co-op Translator aliniază
blocurile Markdown de nivel superior. Blocurile sursă neschimbate refolosesc blocurile traduse curente
existente, inclusiv modificările făcute de oameni; blocurile sursă modificate sau adăugate sunt trimise
pentru traducere; blocurile sursă șterse sunt eliminate. Dacă alinierea este ambiguă,
structura țintă s-a schimbat, traducerea unui bloc este invalidă sau nicio bază de referință
disponibilă, Co-op Translator revine în siguranță la calea existentă
de traducere a întregului fișier.

Această API stochează starea traducerii documentului, nu o memorie de traducere a frazelor sau
segmentelor între documente. Se aplică în prezent traducerii proiectului Markdown
. Comportamentul pentru notebook-uri și imagini rămâne neschimbat. Trimiterea lui `update=True`
încă solicită regenerarea completă.

Dacă unul sau mai multe fișiere nu pot fi traduse, `run_translation` declanșează un
`RuntimeError` după ce fluxul de lucru al proiectului se încheie în loc să raporteze o
execuție reușită cu ieșire lipsă. Integrările ar trebui să trateze acest lucru ca pe un job eșuat
și să păstreze starea anterioară de traducere acceptată.

## Revizuirea conținutului tradus

`run_review` execută verificări deterministe ale traducerii fără credențiale LLM sau Vision.

!!! note "Beta"
    `run_review` este o API beta de revizuire deterministă. Nu apelează furnizori de modele și nu scrie fișiere, dar regulile de verificare și schemele de issue pot evolua.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

După o traducere doar a README-ului, folosiți același scop pentru revizuire:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` revizuiește doar `README.md` din fiecare director rădăcină sursă configurat,
inclusiv `groups` personalizate și directoarele de ieșire. Alte documente și README-uri din subdirectoare
README-urile sunt excluse. Lipsa README-ului sursă aruncă `ValueError`; verificările de traducere eșuate
verificările de traducere eșuate ridică `RuntimeError`.

Revizuiți numai fișierele modificate față de o referință de bază și afișați ieșirea în stil GitHub:

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

## Exemple de API pentru copiere-lipire

Traduceți conținutul Markdown fără a scrie fișiere:

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

Traduceți și rescrieți link-urile Markdown:

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

Traduceți un repository din Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Traduceți mai multe rădăcini:

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

Păstrați termenii din glosar:

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

## Puncte de intrare publice

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

## API-uri pentru traducerea conținutului

API-urile de traducere a conținutului sunt destinate integrărilor care deja au conținut în memorie, cum ar fi o extensie de editor, un instrument MCP, un procesor de notebook-uri sau un pipeline personalizat.

| Funcție | Intrare | Ieșire | I/O fișiere | Note |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Nu | Asincron. Traduce doar conținutul Markdown. Nu rescrie link-urile, nu scrie metadate și nu adaugă declinări de responsabilitate. |
| `translate_notebook_content` | Notebook JSON `str` sau `dict` | Notebook JSON `str` | Nu | Asincron. Traduce celulele Markdown și păstrează celulele non-Markdown. Nu rescrie link-urile, nu scrie metadate și nu adaugă declinări de responsabilitate. |
| `translate_image_content` | Cale imagine | `PIL.Image.Image` | Citește doar imaginea sursă | Sincron. Extrage și traduce textul din imagine, apoi returnează o imagine redată. Nu salvează metadatele imaginii traduse. |

`translate_markdown_content` și `translate_notebook_content` acceptă un `source_path` opțional prin opțiunile lor. Calea este transmisă ca context traducătorului; apelanții rămân responsabili pentru orice rescriere de căi specifică proiectului după traducere.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Aceleași opțiuni pot fi transmise ca dicționare:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API-uri de traducere asistată de agent

API-urile asistate de agent nu apelează furnizorul LLM configurat din Co-op Translator. Ele pregătesc fragmente de Markdown sau notebook pentru ca un agent gazdă să le traducă, apoi reconstruiesc conținutul final din fragmentele traduse.

| Funcție | Scop |
| --- | --- |
| `start_markdown_agent_translation` | Returnează o sarcină Markdown autonomă cu fragmente, prompturi și stare de reconstrucție. |
| `finish_markdown_agent_translation` | Reconstruiește Markdown dintr-o sarcină și din fragmentele traduse de agentul gazdă. |
| `start_notebook_agent_translation` | Returnează o sarcină notebook cu fragmente din celulele Markdown pentru traducerea de către agentul gazdă. |
| `finish_notebook_agent_translation` | Reconstruiește JSON-ul notebook-ului păstrând celulele de cod, output-urile și metadatele. |

Acest flux de lucru este destinat în principal gazdelor MCP. Dacă aveți nevoie de traducerea unui repository în producție cu Co-op Translator gestionând apelurile către furnizori, folosiți `translate_markdown_content`, `translate_notebook_content` sau `run_translation`.

## API-uri pentru rescrierea căilor

API-urile de rescriere a căilor nu efectuează nicio traducere. Ele actualizează link-urile și căile din frontmatter după ce apelanții cunosc calea sursă, calea țintă tradusă și structura proiectului.

| Funcție | Domeniu | Note |
| --- | --- | --- |
| `rewrite_markdown_paths` | Corpul Markdown și frontmatter | Rescrie link-urile Markdown și câmpurile frontmatter de căi suportate pentru o țintă tradusă. |
| `rewrite_notebook_paths` | Celulele Markdown din JSON-ul notebook-ului | Aplică rescrierea căilor Markdown fiecărei celule Markdown și lasă neschimbate celulele non-Markdown. |

Argumentul `policy` poate fi un dicționar cu următoarele câmpuri:

| Câmp | Obligatoriu | Scop |
| --- | --- | --- |
| `language_code` | Da | Codul limbii țintă, cum ar fi `"ko"` sau `"pt-BR"`. |
| `root_dir` | Nu | Rădăcina proiectului sursă. Implicit este `"."`. |
| `translations_dir` | Nu | Directorul de ieșire pentru traducerile textului. Implicit este `translations` sub `root_dir`. |
| `translated_images_dir` | Nu | Directorul de ieșire pentru imaginile traduse. Implicit este `translated_images` sub `root_dir`. |
| `translation_types` | Nu | Tipurile de traducere activate. Implicit este Markdown, notebook-uri și imagini. |
| `lang_subdir` | Nu | Subdirector opțional sub fiecare folder de limbă. |

## Parametrii traducerii proiectului

| Parametru | Tip | Implicit | Scop |
| --- | --- | --- | --- |
| `language_codes` | `str` | Obligatoriu | Coduri de limbă țintă separate prin spațiu, cum ar fi `"ko ja fr"`, sau `"all"`. Codurile alias sunt normalizate la valorile canonice BCP 47. |
| `root_dir` | `str` | `"."` | Rădăcina proiectului pentru o singură țintă de traducere. Ignorat când sunt furnizate `root_dirs` sau `groups`. |
| `update` | `bool` | `False` | Șterge și recreează traducerile existente pentru limbile selectate. |
| `images` | `bool` | `False` | Include traducerea imaginilor. Necesită configurare Azure AI Vision. |
| `markdown` | `bool` | `False` | Include traducerea Markdown. |
| `notebook` | `bool` | `False` | Include traducerea notebook-urilor Jupyter. |
| `debug` | `bool` | `False` | Activează logarea de depanare. |
| `save_logs` | `bool` | `False` | Salvează fișiere jurnal la nivel DEBUG sub directorul `logs/` din rădăcină. |
| `yes` | `bool` | `True` | Confirmă automat prompturile pentru utilizare programatică și în CI. |
| `add_disclaimer` | `bool` | `False` | Adaugă mențiuni privind traducerea automată în Markdown-ul și notebook-urile traduse. |
| `translations_dir` | `str \| None` | `None` | Director personalizat pentru fișierele de ieșire ale traducerii textului. Căile relative se rezolvă în raport cu fiecare rădăcină. |
| `image_dir` | `str \| None` | `None` | Director personalizat pentru imaginile traduse. Căile relative se rezolvă în raport cu fiecare rădăcină. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mai multe rădăcini care împart aceleași setări de ieșire. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Perechi explicite `(root_dir, translations_dir)`. Au prioritate față de `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL-ul depozitului folosit la afișarea indicațiilor din tabelul de limbi din README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Termeni din glosar de păstrat în timpul traducerii. Duplicatele și termenii goi sunt normalizați. |
| `dry_run` | `bool` | `False` | Estimează volumul de traducere și previzualizează comportamentul de migrare fără a scrie fișiere. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Adaptor opțional de persistență pentru baza de referință acceptată și candidați pentru actualizări incrementale Markdown. Ometerea lui păstrează comportamentul existent de rescriere a fișierelor întregi. |

## Parametri de revizuire

`run_review` oglindește intenționat semnătura `run_translation` acolo unde este posibil, astfel încât automatizarea să poată comuta între fluxurile de lucru de traducere și revizuire cu ramificare minimă.

| Parametru | Tip | Implicit | Scop |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Folderele limbilor țintă de revizuit. Sunt acceptate șiruri separate prin spațiu și iterabile. `"all"` revizuiește fiecare limbă de traducere descoperită. |
| `root_dir` | `str` | `"."` | Rădăcina proiectului pentru o singură țintă de revizuire. Este ignorată când `root_dirs` sau `groups` sunt furnizate. |
| `markdown` | `bool` | `False` | Include fișierele sursă Markdown și MDX. |
| `notebook` | `bool` | `False` | Include fișierele sursă Jupyter notebook. |
| `images` | `bool` | `False` | Rezervat pentru paritate cu opțiunile de traducere. Referințele către imagini sunt verificate din Markdown. |
| `translations_dir` | `str \| None` | `None` | Director personalizat pentru fișierele de ieșire ale traducerii textului. Căile relative se rezolvă în raport cu fiecare rădăcină. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mai multe rădăcini care împart aceleași setări de ieșire. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Perechi explicite `(root_dir, translations_dir)`. Au prioritate față de `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Referință Git folosită pentru a limita revizuirea la fișierele sursă modificate. |
| `readme_only` | `bool` | `False` | Revizuiește doar `README.md` din fiecare rădăcină sursă. Lipsa unui README sursă ridică `ValueError`. |
| `output_format` | `str` | `"text"` | Formatul de ieșire al revizuirii. Valorile acceptate sunt `"text"` și `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Tratează avertismentele ca eșecuri pe lângă erori. |
| `debug` | `bool` | `False` | Activează logarea de depanare. |
| `save_logs` | `bool` | `False` | Salvează fișiere jurnal la nivel DEBUG în directorul `logs/` din rădăcină. |

Dacă niciuna dintre `markdown`, `notebook` sau `images` nu este setată, API-ul revizuiește Markdown-ul, notebook-urile și referințele link către imagini acolo unde este cazul. Revizuirea nu apelează un furnizor LLM și nu necesită chei API.

## Cerințe de configurare

API-urile de traducere care depind de un furnizor necesită configurarea furnizorului înainte de traducere:

- Traducerea Markdown și a notebook-urilor necesită un furnizor LLM. Configurați Azure OpenAI, OpenAI sau Anthropic.
- Traducerea imaginilor necesită Azure AI Vision pe lângă furnizorul LLM.
- `run_translation` execută verificări de conectivitate ușoare înainte de începerea traducerii proiectului.
- API-urile asistate de agent `start_*_agent_translation` și `finish_*_agent_translation` nu apelează furnizorii LLM ai Co-op Translator. Aplicația gazdă sau agentul MCP traduce blocurile pregătite.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` și `run_review` sunt deterministe și nu necesită credențiale de la furnizor.

Variabile Azure OpenAI necesare:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Variabile OpenAI necesare:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Variabile Anthropic necesare:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` și `ANTHROPIC_MAX_TOKENS` sunt opționale. Microsoft Agent Framework este clientul de model implicit pentru toți furnizorii începând cu Co-op Translator 0.22.0. Semantic Kernel poate fi încă selectat temporar cu `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, dar aceasta generează un avertisment de depreciere; vezi [configurare](configuration.md#model-client-backend) pentru planul de eliminare etapizat.

Variabile Azure AI Vision necesare pentru traducerea imaginilor:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` este determinist și nu necesită configurare pentru LLM sau Azure AI Vision.

## Observații despre comportament

- API-urile de traducere a conținutului păstrează separarea dintre traducere și rescrierea căilor proiectului. Apelați `rewrite_markdown_paths` sau `rewrite_notebook_paths` explicit când conținutul tradus necesită ajustarea linkurilor relative la proiect pentru o locație țintă.
- API-urile de orchestrare a proiectului adaugă comportament la nivel de proiect pentru traducerea conținutului, inclusiv descoperirea fișierelor, scrieri, rescrierea căilor, metadata, curățare și declinări de responsabilitate opționale.
- `run_translation` afișează rezumate de progres și estimări prin același raportor bazat pe Rich folosit de CLI. Ieșirea non-interactivă revine la text simplu.
- `dry_run=True` calculează estimări folosind actualizări virtuale ale README-ului, dar nu scrie README-ul sau fișierele de traducere.
- `groups` sunt procesate secvențial. O singură estimare agregată este afișată înainte de începerea lucrului.
- Când este selectată traducerea imaginilor, lipsa configurării Vision generează o eroare înainte de începerea traducerii.
- Folderele de limbă existente bazate pe aliasuri sunt detectate și pot fi migrate la nume canonice de foldere de limbă ca parte a rulării.
- `run_review` eșuează la fișiere traduse lipsă, metadata de traducere lipsă sau învechită, frontmatter Markdown sau blocuri de cod formate incorect și JSON invalid pentru notebook-uri traduse.
- `run_review` raportează țintele locale Markdown și link-urile către imagini lipsă ca avertismente în mod implicit.

## Cale internă de apel

API-ul delegă către aceeași implementare de bază folosită de CLI:

Traducere:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixin-uri axate pe traducerea proiectului pentru Markdown, notebook-uri și imagini.
8. Traducători pentru Markdown, notebook, text și imagini sub `co_op_translator.core`.

Revizuire:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Verificări deterministe sub `co_op_translator.review.checks`

Următoarele clase sunt utile pentru întreținători, dar nu sunt exportate ca API stabil la nivel de pachet.

| Clasă | Modul | Responsabilitate |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordonează traducerea la nivel de proiect, gestionarea directoarelor, normalizarea metadata pe limbă și delegarea către traducători pentru Markdown, notebook și imagini. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Realizează lucrările asincrone de procesare a fișierelor pentru Markdown, notebook-uri, imagini, detectarea învechirii și actualizările metadata de traducere. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orchestrează citirea fișierelor Markdown, traducerea conținutului, rescrierea căilor, metadata, declinări de responsabilitate și scrieri. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orchestrează citirea fișierelor notebook, traducerea celulelor Markdown, rescrierea căilor, metadata, declinări de responsabilitate și scrieri. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orchestrează descoperirea imaginilor sursă, traducerea imaginilor, căile de ieșire, metadata și scrieri. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Găsește perechile Markdown traduse, evaluează calitatea traducerii și citește metadata privind încrederea pentru fluxuri de lucru de remediere cu încredere scăzută. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordonează verificări deterministe de revizuire pentru fișierele sursă, limbile țintă și rădăcinile de traducere configurate. |
| `ReviewTarget` | `co_op_translator.review.targets` | Descrie o rădăcină sursă și directorul de ieșire al traducerii revizuit pentru acea rădăcină. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detectează foldere de limbă vechi bazate pe aliasuri și pregătește planuri de migrare către foldere canonice BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Încarcă fișiere `.env` și verifică dacă furnizorii LLM necesari și opțional Vision sunt configurați. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Detectează automat Azure OpenAI, OpenAI sau Anthropic, validează variabilele de mediu necesare și execută verificări de conectivitate pentru furnizor. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detectează configurația Azure AI Vision și execută verificări de conectivitate pentru traducerea imaginilor. |