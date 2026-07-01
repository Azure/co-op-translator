# Python API

Το σταθερό δημόσιο Python API εξάγεται από `co_op_translator.api`. Οι περισσότερες ενσωματώσεις χρησιμοποιούν μία από αυτές τις ροές εργασίας:

| Σενάριο | Χρησιμοποιήστε αυτό όταν | Κύρια APIs |
| --- | --- | --- |
| Μετάφραση μεμονωμένων αρχείων ή εγγράφων | Η εφαρμογή σας διαβάζει το αρχικό περιεχόμενο, καλεί το Co-op Translator για μετάφραση και αποφασίζει πού θα αποθηκεύσει το αποτέλεσμα. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Προετοιμασία περιεχομένου για μετάφραση από host-agent | Ο MCP host ή το μοντέλο της εφαρμογής σας θα μεταφράσει κομμάτια, ενώ το Co-op Translator χειρίζεται το κομμάτιασμα και την ανασυγκρότηση. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Μετάφραση ολόκληρου repository | Θέλετε το Python API να συμπεριφέρεται όπως το CLI και να χειρίζεται την ανακάλυψη, μονοπάτια εξόδου, μεταδεδομένα, καθαρισμό και εγγραφές. | `run_translation` |

Τα περισσότερα χαμηλού επιπέδου modules κάτω από `core`, `config`, `review`, και `utils` είναι λεπτομέρειες υλοποίησης που χρησιμοποιούνται από αυτά τα σημεία εισόδου του API.

Οι πελάτες MCP χρησιμοποιούν το ίδιο δημόσιο API μέσω του [MCP Server](mcp.md). Χρησιμοποιήστε αυτή τη σελίδα όταν καλείτε Python απευθείας, και τον οδηγό MCP όταν εκθέτετε το Co-op Translator σε έναν agent ή επεξεργαστή. Αν αποφασίζετε ανάμεσα σε CLI, Python API και MCP, ξεκινήστε με το [Choose Your Workflow](workflows.md).

## First-Time API Flow

Ξεκινήστε εδώ εάν καλείτε το Co-op Translator από κώδικα Python:

1. Διαμορφώστε έναν πάροχο LLM όπως περιγράφεται στο [Configuration](configuration.md), εκτός αν μόνο προετοιμάζετε κομμάτια Markdown ή notebook για μετάφραση από host-agent.
2. Αποφασίστε αν η εφαρμογή σας αναλαμβάνει το I/O των αρχείων.
3. Χρησιμοποιήστε τα content APIs όταν η εφαρμογή σας διαβάζει και γράφει μεμονωμένα αρχεία.
4. Χρησιμοποιήστε `run_translation` όταν το Co-op Translator πρέπει να επεξεργαστεί ένα repository όπως το CLI.
5. Χρησιμοποιήστε `run_review` μετά τη μετάφραση αν χρειάζεστε ντετερμινιστικούς ελέγχους στην αυτοματοποίηση.

| Στόχος | API για να ξεκινήσετε |
| --- | --- |
| Μετάφραση μιας Markdown συμβολοσειράς ή αρχείου | `translate_markdown_content` |
| Μετάφραση ενός notebook payload | `translate_notebook_content` |
| Μετάφραση μιας εικόνας | `translate_image_content` |
| Να επιτρέψετε σε host agent να μεταφράσει κομμάτια Markdown ή notebook | `start_markdown_agent_translation` ή `start_notebook_agent_translation` |
| Επανεγγραφή μεταφρασμένων συνδέσμων μετά την επιλογή μονοπατιού εξόδου | `rewrite_markdown_paths` ή `rewrite_notebook_paths` |
| Μετάφραση ενός πλήρους repository | `run_translation` |
| Εξέταση/έλεγχος μεταφρασμένου αποτελέσματος | `run_review` |

## Scenario 1: Translate Individual Files or Documents

Χρησιμοποιήστε αυτή τη ροή όταν έχετε ήδη ένα αρχείο, buffer επεξεργαστή, notebook payload, αίτημα MCP ή προσαρμοσμένη είσοδο pipeline. Ο κώδικάς σας αναλαμβάνει το I/O αρχείων:

1. Διαβάστε το αρχικό περιεχόμενο.
2. Καλέστε ένα API μετάφρασης περιεχομένου.
3. Προαιρετικά καλέστε ένα API επανεγγραφής μονοπατιού αν το μεταφρασμένο περιεχόμενο θα γραφτεί σε φάκελο μετάφρασης του project.
4. Αποθηκεύστε ή επιστρέψτε το αποτέλεσμα από την εφαρμογή σας.

Τα APIs μετάφρασης περιεχομένου δεν τρέχουν ανακάλυψη project, δεν γράφουν μεταδεδομένα, δεν προσθέτουν αποποιήσεις ευθυνών και δεν επανεγγράφουν συνδέσμους αυτόματα.

### Markdown File

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

Εάν το μεταφρασμένο Markdown δεν θα βρίσκεται σε layout project του Co-op Translator, παραλείψτε το `rewrite_markdown_paths` και αποθηκεύστε την μεταφρασμένη συμβολοσειρά απευθείας.

### Notebook File

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

Το `translate_notebook_content` μεταφράζει τα Markdown cells και διατηρεί τα μη-Markdown cells. Η επανεγγραφή μονοπατιών εφαρμόζεται μόνο σε Markdown cells.

### Image File

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

Το `translate_image_content` διαβάζει την αρχική εικόνα και επιστρέφει ένα αποδοσμένο `PIL.Image.Image`. Δεν γράφει μεταδεδομένα μεταφρασμένης εικόνας.

## Scenario 2: Translate an Entire Repository

Χρησιμοποιήστε αυτή τη ροή όταν θέλετε το Python API να συμπεριφέρεται όπως το `translate` CLI. Το `run_translation` ανακαλύπτει υποστηριζόμενα αρχεία, μεταφράζει επιλεγμένους τύπους περιεχομένου, επανεγγράφει μονοπάτια, γράφει αρχεία εξόδου, ενημερώνει μεταδεδομένα και εκτελεί εργασίες συντήρησης μετάφρασης όπως καθαρισμό.

Το `run_translation` είναι το προτιμώμενο σημείο εισόδου ορχήστρωσης project. Το `translate_project` εξάγεται ως συμβατό alias με την ίδια συμπεριφορά.

Μεταφράστε αρχεία Markdown στο τρέχον repository στα κορεάτικα και ιαπωνικά:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Μεταφράστε μόνο notebooks από συγκεκριμένο root project:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Προεπισκόπηση όγκου μετάφρασης χωρίς εγγραφή αρχείων:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Μεταφράστε πολλαπλές ρίζες περιεχομένου σε μία κλήση:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Γράψτε μεταφράσεις σε ρητά output groups:

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

Χρησιμοποιήστε ένα placeholder ανά γλώσσα όταν κάθε γλώσσα πρέπει να περιέχει έναν εμφωλευμένο υποφάκελο:

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

Εάν κανένα από τα `markdown`, `notebook`, ή `images` δεν είναι ενεργοποιημένο, το API μεταφράζει όλους τους υποστηριζόμενους τύπους: Markdown, notebooks και images.

## Review Translated Output

Το `run_review` εκτελεί ντετερμινιστικούς ελέγχους μετάφρασης χωρίς πιστοποιητικά LLM ή Vision.

!!! note "Beta"
    Το `run_review` είναι ένα beta ντετερμινιστικό API ελέγχου. Δεν καλεί παρόχους μοντέλων ούτε γράφει αρχεία, αλλά τα σχήματα ελέγχων και ζητημάτων ενδέχεται να εξελιχθούν.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Εξετάστε μόνο αρχεία που άλλαξαν σε σχέση με ένα base ref και εκτυπώστε έξοδο με μορφή συμβατή με GitHub:

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

## Copy-Paste API Examples

Μεταφράστε περιεχόμενο Markdown χωρίς εγγραφές αρχείων:

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

Μεταφράστε και επανεγγράψτε συνδέσμους Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Μεταφράστε ένα repository από Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Μεταφράστε πολλαπλές ρίζες:

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

Διατηρήστε όρους λεξιλογίου (glossary):

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

## Public Entry Points

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Content Translation APIs

Τα APIs μετάφρασης περιεχομένου προορίζονται για ενσωματώσεις που ήδη έχουν περιεχόμενο σε μνήμη, όπως επέκταση επεξεργαστή, εργαλείο MCP, επεξεργαστής notebook ή προσαρμοσμένο pipeline.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Μεταφράζει μόνο περιεχόμενο Markdown. Δεν επανεγγράφει συνδέσμους, δεν γράφει μεταδεδομένα, ούτε προσθέτει αποποιήσεις ευθυνών. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Μεταφράζει Markdown cells και διατηρεί τα μη-Markdown cells. Δεν επανεγγράφει συνδέσμους, δεν γράφει μεταδεδομένα, ούτε προσθέτει αποποιήσεις ευθυνών. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Εξάγει και μεταφράζει το κείμενο της εικόνας, και στη συνέχεια επιστρέφει μία αποδοσμένη εικόνα. Δεν αποθηκεύει μεταδεδομένα μεταφρασμένης εικόνας. |

Τα `translate_markdown_content` και `translate_notebook_content` δέχονται ένα προαιρετικό `source_path` μέσω των options τους. Το μονοπάτι περνιέται ως context στον μεταφραστή· οι καλούντες παραμένουν υπεύθυνοι για οποιαδήποτε project-συγκεκριμένη επανεγγραφή μονοπατιών μετά τη μετάφραση.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Οι ίδιες επιλογές μπορούν να περαστούν ως dictionaries:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Τα agent-assisted APIs δεν καλούν Azure OpenAI ή OpenAI από το Co-op Translator. Προετοιμάζουν κομμάτια Markdown ή notebook για να τα μεταφράσει ένας host agent και στη συνέχεια ανασυνθέτουν το τελικό περιεχόμενο από τα μεταφρασμένα κομμάτια.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Επιστρέφει μια αυτοτελή εργασία Markdown με κομμάτια, prompts και κατάσταση ανασυγκρότησης. |
| `finish_markdown_agent_translation` | Ανασυνθέτει το Markdown από μια εργασία και τα μεταφρασμένα κομμάτια του host-agent. |
| `start_notebook_agent_translation` | Επιστρέφει μια εργασία notebook με κομμάτια από Markdown cells για μετάφραση από host-agent. |
| `finish_notebook_agent_translation` | Ανασυνθέτει το notebook JSON διατηρώντας code cells, outputs και μεταδεδομένα. |

Αυτή η ροή εργασίας προορίζεται κυρίως για hosts MCP. Αν χρειάζεστε μετάφραση repository σε production με το Co-op Translator να διαχειρίζεται τις κλήσεις σε παρόχους, χρησιμοποιήστε `translate_markdown_content`, `translate_notebook_content`, ή `run_translation`.

## Path Rewriting APIs

Τα APIs επανεγγραφής μονοπατιών δεν εκτελούν καμία μετάφραση. Ενημερώνουν συνδέσμους και πεδία frontmatter αφού οι καλούντες γνωρίζουν το μονοπάτι πηγής, το μεταφρασμένο μονοπάτι προορισμού και το layout του project.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Επανεγγράφει συνδέσμους Markdown και υποστηριζόμενα πεδία μονοπατιών frontmatter για έναν μεταφρασμένο προορισμό. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Εφαρμόζει την επανεγγραφή μονοπατιών Markdown σε κάθε Markdown cell και αφήνει τα μη-Markdown cells αμετάβλητα. |

Το όρισμα `policy` μπορεί να είναι ένα dictionary με αυτά τα πεδία:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Κωδικός γλώσσας προορισμού, όπως `"ko"` ή `"pt-BR"`. |
| `root_dir` | No | Ρίζα του project προέλευσης. Προεπιλογή `"."`. |
| `translations_dir` | No | Κατάλογος εξόδου για μεταφράσεις κειμένου. Προεπιλογή `translations` κάτω από το `root_dir`. |
| `translated_images_dir` | No | Κατάλογος εξόδου για μεταφρασμένες εικόνες. Προεπιλογή `translated_images` κάτω από το `root_dir`. |
| `translation_types` | No | Ενεργοποιημένοι τύποι μετάφρασης. Προεπιλογή: Markdown, notebooks και images. |
| `lang_subdir` | No | Προαιρετικός υποφάκελος κάτω από κάθε φάκελο γλώσσας. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Κωδικοί γλωσσών-στόχων διαχωρισμένοι με κενό, όπως `"ko ja fr"`, ή `"all"`. Οι alias κωδικοί κανονικοποιούνται σε κανονικές τιμές BCP 47. |
| `root_dir` | `str` | `"."` | Ρίζα project για έναν μεμονωμένο στόχο μετάφρασης. Αγνοείται όταν παρέχονται `root_dirs` ή `groups`. |
| `update` | `bool` | `False` | Διαγραφή και επανδημιουργία υπαρχουσών μεταφράσεων για τις επιλεγμένες γλώσσες. |
| `images` | `bool` | `False` | Συμπερίληψη μετάφρασης εικόνων. Απαιτεί διαμόρφωση Azure AI Vision. |
| `markdown` | `bool` | `False` | Συμπερίληψη μετάφρασης Markdown. |
| `notebook` | `bool` | `False` | Συμπερίληψη μετάφρασης Jupyter notebook. |
| `debug` | `bool` | `False` | Ενεργοποίηση debug logging. |
| `save_logs` | `bool` | `False` | Αποθήκευση αρχείων καταγραφής επιπέδου DEBUG κάτω από τον root κατάλογο `logs/`. |
| `yes` | `bool` | `True` | Αυτόματη επιβεβαίωση prompts για προγραμματιστική χρήση και CI. |
| `add_disclaimer` | `bool` | `False` | Προσθήκη αποποίησης ευθυνών μηχανικής μετάφρασης σε μεταφρασμένα Markdown και notebooks. |
| `translations_dir` | `str \| None` | `None` | Προσαρμοσμένος κατάλογος εξόδου μεταφράσεων κειμένου. Σχετικές διαδρομές επιλύονται ως προς κάθε root. |
| `image_dir` | `str \| None` | `None` | Προσαρμοσμένος κατάλογος εξόδου μεταφρασμένων εικόνων. Σχετικές διαδρομές επιλύονται ως προς κάθε root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Πολλαπλές ρίζες που μοιράζονται τις ίδιες ρυθμίσεις εξόδου. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Ρητά ζεύγη `(root_dir, translations_dir)`. Έχουν προτεραιότητα πάνω από τα `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL του repository που χρησιμοποιείται κατά την απόδοση οδηγίας πίνακα γλωσσών στο README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Όροι λεξιλογίου που θα διατηρηθούν κατά τη μετάφραση. Τα διπλότυπα και τα κενά στοιχεία κανονικοποιούνται. |
| `dry_run` | `bool` | `False` | Εκτίμηση όγκου μετάφρασης και προεπισκόπηση συμπεριφοράς μετανάστευσης χωρίς εγγραφή αρχείων. |

## Review Parameters

Το `run_review` σκόπιμα καθρεφτίζει την υπογραφή του `run_translation` όπου είναι δυνατό ώστε η αυτοματοποίηση να μπορεί να εναλλάσσεται μεταξύ ροών μετάφρασης και ελέγχου με ελάχιστη λογική διακλάδωσης.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Φάκελοι γλωσσών-στόχων προς εξέταση. Γίνονται αποδεκτές συμβολοσειρές χωρισμένες με κενό και iterable. Το `"all"` ελέγχει κάθε ανακαλυφθείσα γλώσσα μετάφρασης. |
| `root_dir` | `str` | `"."` | Ρίζα project για έναν μεμονωμένο στόχο ελέγχου. Αγνοείται όταν παρέχονται `root_dirs` ή `groups`. |
| `markdown` | `bool` | `False` | Συμπερίληψη αρχείων πηγής Markdown και MDX. |
| `notebook` | `bool` | `False` | Συμπερίληψη αρχείων πηγής Jupyter notebook. |
| `images` | `bool` | `False` | Κρατημένο για ισοτιμία με τις επιλογές μετάφρασης. Ελέγχονται οι αναφορές συνδέσμων σε εικόνες από Markdown. |
| `translations_dir` | `str \| None` | `None` | Προσαρμοσμένος κατάλογος εξόδου για μεταφράσεις κειμένου. Οι σχετικές διαδρομές επιλύονται σε σχέση με κάθε root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Πολλαπλές ρίζες που μοιράζονται τις ίδιες ρυθμίσεις εξόδου. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Ρητά `(root_dir, translations_dir)` ζεύγη. Έχουν προτεραιότητα έναντι του `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Αναφορά Git που χρησιμοποιείται για να περιορίσει την ανασκόπηση στα τροποποιημένα αρχεία πηγαίου κώδικα. |
| `output_format` | `str` | `"text"` | Μορφή εξόδου ανασκόπησης. Υποστηριζόμενες τιμές είναι `"text"` και `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Θεωρεί τις προειδοποιήσεις ως αποτυχίες επιπλέον των σφαλμάτων. |
| `debug` | `bool` | `False` | Ενεργοποιεί την καταγραφή αποσφαλμάτωσης. |
| `save_logs` | `bool` | `False` | Αποθηκεύει αρχεία καταγραφής σε επίπεδο DEBUG στον root κατάλογο `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Απαιτήσεις Διαμόρφωσης

Provider-backed translation APIs require provider configuration before translating:

- Markdown and notebook translation require an LLM provider. Configure either Azure OpenAI or OpenAI.
- Image translation requires Azure AI Vision in addition to the LLM provider.
- `run_translation` runs lightweight connectivity checks before project translation begins.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` are deterministic and do not require provider credentials.

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` is deterministic and does not require Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## Σημειώσεις Συμπεριφοράς

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Εσωτερική Διαδρομή Κλήσεων

The API delegates to the same core implementation used by the CLI:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Συντονίζει τη μετάφραση σε επίπεδο έργου, τη διαχείριση καταλόγων, τη νορμοποίηση μεταδεδομένων ανά γλώσσα και την ανάθεση σε μεταφραστές Markdown, notebook και εικόνας. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Εκτελεί την ασύγχρονη επεξεργασία αρχείων για Markdown, notebooks, εικόνες, ανίχνευση παλαιότητας και ενημερώσεις μεταδεδομένων μετάφρασης. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Ορχηστρώνει την ανάγνωση αρχείων Markdown, τη μετάφραση περιεχομένου, την επανεγγραφή διαδρομών, τα μεταδεδομένα, τις αποποιήσεις και τις εγγραφές. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Ορχηστρώνει την ανάγνωση αρχείων notebook, τη μετάφραση κελιών Markdown, την επανεγγραφή διαδρομών, τα μεταδεδομένα, τις αποποιήσεις και τις εγγραφές. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Ορχηστρώνει την ανακάλυψη αρχικών εικόνων, τη μετάφραση εικόνων, τις διαδρομές εξόδου, τα μεταδεδομένα και τις εγγραφές. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Εντοπίζει ζεύγη μεταφρασμένων Markdown, αξιολογεί την ποιότητα μετάφρασης και διαβάζει μεταδεδομένα εμπιστοσύνης για ροές εργασίας επιδιόρθωσης χαμηλής εμπιστοσύνης. |
| `ReviewRunner` | `co_op_translator.review.runner` | Συντονίζει ντετερμινιστικούς ελέγχους ανασκόπησης σε αρχεία πηγής, γλώσσες-στόχους και διαμορφωμένες ρίζες μετάφρασης. |
| `ReviewTarget` | `co_op_translator.review.targets` | Περιγράφει μια ρίζα πηγής και τον κατάλογο εξόδου μετάφρασης που ανασκοπείται για εκείνη τη ρίζα. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Ανιχνεύει παλιούς φακέλους γλωσσών με ψευδώνυμα και προετοιμάζει σχέδια μετανάστευσης σε κανονικές ονομασίες φακέλων BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Φορτώνει αρχεία `.env` και ελέγχει εάν οι απαιτούμενοι πάροχοι LLM και οι προαιρετικοί Vision έχουν διαμορφωθεί. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Αυτό-εντοπίζει Azure OpenAI ή OpenAI, επικυρώνει τις απαιτούμενες μεταβλητές περιβάλλοντος και εκτελεί ελέγχους συνδεσιμότητας παρόχου. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Ανιχνεύει τη διαμόρφωση Azure AI Vision και εκτελεί ελέγχους συνδεσιμότητας για τη μετάφραση εικόνων. |