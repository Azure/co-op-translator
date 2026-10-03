# API για Python

Το σταθερό δημόσιο API για Python εξάγεται από `co_op_translator.api`. Οι περισσότερες ενσωματώσεις χρησιμοποιούν μία από αυτές τις ροές εργασίας:

| Σενάριο | Χρησιμοποιήστε αυτό όταν | Κύρια APIs |
| --- | --- | --- |
| Μεταφράστε μεμονωμένα αρχεία ή έγγραφα | Η εφαρμογή σας διαβάζει το περιεχόμενο πηγής, καλεί το Co-op Translator για μετάφραση και αποφασίζει πού θα αποθηκεύσει το αποτέλεσμα. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Προετοιμασία περιεχομένου για μετάφραση από host-agent | Ο host MCP ή το μοντέλο εφαρμογής σας θα μεταφράσει τα κομμάτια, ενώ το Co-op Translator χειρίζεται το χωρισμό σε κομμάτια και την ανασύνθεση. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Μεταφράστε ολόκληρο αποθετήριο | Θέλετε το Python API να συμπεριφέρεται όπως το CLI και να αναλαμβάνει ανίχνευση, διαδρομές εξόδου, μεταδεδομένα, καθαρισμό και εγγραφές. | `run_translation` |

Τα περισσότερα χαμηλού επιπέδου modules υπό `core`, `config`, `review`, και `utils` είναι λεπτομέρειες υλοποίησης που χρησιμοποιούνται από αυτά τα σημεία εισόδου του API.

Οι πελάτες MCP χρησιμοποιούν το ίδιο δημόσιο API μέσω του [MCP Server](mcp.md). Χρησιμοποιήστε αυτή τη σελίδα όταν καλείτε Python απευθείας, και τον οδηγό MCP όταν εκθέτετε το Co-op Translator σε έναν agent ή επεξεργαστή. Εάν αποφασίζετε μεταξύ CLI, Python API, και MCP, ξεκινήστε με [Choose Your Workflow](workflows.md).

## Ροή API για πρώτη φορά

Ξεκινήστε εδώ αν καλείτε το Co-op Translator από κώδικα Python:

1. Διαμορφώστε έναν πάροχο LLM όπως περιγράφεται στο [Configuration](configuration.md), εκτός αν απλώς προετοιμάζετε κομμάτια Markdown ή notebook για μετάφραση από host-agent.
2. Αποφασίστε αν η εφαρμογή σας αναλαμβάνει τις λειτουργίες εισόδου/εξόδου αρχείων.
3. Χρησιμοποιήστε τα API περιεχομένου όταν η εφαρμογή σας διαβάζει και γράφει μεμονωμένα αρχεία.
4. Χρησιμοποιήστε `run_translation` όταν το Co-op Translator πρέπει να επεξεργαστεί ένα αποθετήριο όπως το CLI.
5. Χρησιμοποιήστε `run_review` μετά τη μετάφραση εάν χρειάζεστε ντετερμινιστικούς ελέγχους σε αυτοματισμό.

| Στόχος | API για να ξεκινήσετε |
| --- | --- |
| Μεταφράστε μια συμβολοσειρά ή αρχείο Markdown | `translate_markdown_content` |
| Μεταφράστε ένα περιεχόμενο notebook | `translate_notebook_content` |
| Μεταφράστε μία εικόνα | `translate_image_content` |
| Αφήστε έναν host agent να μεταφράσει κομμάτια Markdown ή notebook | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Επαναγράψτε μεταφρασμένους συνδέσμους μετά την επιλογή διαδρομής εξόδου | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Μεταφράστε ένα πλήρες αποθετήριο | `run_translation` |
| Επανεξέταση μεταφρασμένου αποτελέσματος | `run_review` |

## Σενάριο 1: Μεταφράστε μεμονωμένα αρχεία ή έγγραφα

Χρησιμοποιήστε αυτή τη ροή εργασίας όταν έχετε ήδη ένα αρχείο, buffer επεξεργαστή, payload notebook, αίτημα MCP, ή προσαρμοσμένη ροή εισόδου. Ο κώδικάς σας αναλαμβάνει τις λειτουργίες εισόδου/εξόδου αρχείων:

1. Διαβάστε το περιεχόμενο πηγής.
2. Καλέστε ένα API μετάφρασης περιεχομένου.
3. Προαιρετικά καλέστε ένα API επαναγραφής διαδρομών εάν το μεταφρασμένο περιεχόμενο θα γραφτεί σε έναν φάκελο μετάφρασης έργου.
4. Αποθηκεύστε ή επιστρέψτε το αποτέλεσμα από την εφαρμογή σας.

Τα API μετάφρασης περιεχομένου δεν εκτελούν ανίχνευση έργου, δεν γράφουν μεταδεδομένα, δεν προσθέτουν αποποιήσεις ευθυνών, και δεν επαναγράφουν συνδέσμους αυτόματα.

### Αρχείο Markdown

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

Εάν το μεταφρασμένο Markdown δεν θα βρίσκεται σε διάταξη έργου Co-op Translator, παραλείψτε το `rewrite_markdown_paths` και αποθηκεύστε τη μεταφρασμένη συμβολοσειρά απευθείας.

### Αρχείο Notebook

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

`translate_notebook_content` μεταφράζει κελιά Markdown και διατηρεί τα μη-Markdown κελιά. Η επαναγραφή διαδρομών εφαρμόζεται μόνο σε κελιά Markdown.

### Αρχείο Εικόνας

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

`translate_image_content` διαβάζει την πηγή της εικόνας και επιστρέφει ένα αποδομένο `PIL.Image.Image`. Δεν γράφει μεταδεδομένα μεταφρασμένης εικόνας.

## Σενάριο 2: Μεταφράστε ολόκληρο αποθετήριο

Χρησιμοποιήστε αυτή τη ροή εργασίας όταν θέλετε το Python API να λειτουργεί σαν το `translate` CLI. Το `run_translation` εντοπίζει υποστηριζόμενα αρχεία, μεταφράζει επιλεγμένους τύπους περιεχομένου, επαναγράφει διαδρομές, γράφει αρχεία εξόδου, ενημερώνει μεταδεδομένα και εκτελεί εργασίες συντήρησης μετάφρασης όπως καθαρισμό.

Το `run_translation` είναι το προτιμώμενο σημείο εισόδου ορχήστρωσης έργου. Το `translate_project` εξάγεται ως alias συμβατότητας με την ίδια συμπεριφορά.

Μεταφράστε αρχεία Markdown στο τρέχον αποθετήριο σε Κορεάτικα και Ιαπωνικά:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Μεταφράστε μόνο notebooks από μια συγκεκριμένη ρίζα έργου:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Προεπισκόπηση όγκου μετάφρασης χωρίς να γράψετε αρχεία:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Καταγράψτε δομημένα γεγονότα προόδου για μια ενσωμάτωση:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Αποθηκεύστε το περιεχόμενο (payload) στον πίνακα γεγονότων εργασίας ή μεταδώστε το στη διεπαφή χρήστη σας.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Τα γεγονότα χρησιμοποιούν το εκδομένο σχήμα `co-op.translation.event.v1`. Οι ενσωματώσεις θα πρέπει
να εξαρτώνται από σταθερά πεδία όπως `type` και `stage_key`, όχι από ανθρώπινα προσανατολισμένο
κείμενο κονσόλας ή `stage_label`.

Μεταφράστε πολλαπλές ρίζες περιεχομένου με μία κλήση:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Γράψτε μεταφράσεις σε ρητές ομάδες εξόδου:

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

Εάν κανένα από `markdown`, `notebook` ή `images` δεν έχει οριστεί, το API μεταφράζει όλους τους υποστηριζόμενους τύπους: Markdown, notebooks, και εικόνες.

### Διατηρήστε αποδεκτές ανθρώπινες επεξεργασίες με έναν provider κατάστασης μετάφρασης

Κατά προεπιλογή, το Co-op Translator διατηρεί την υπάρχουσα συμπεριφορά σε επίπεδο αρχείου: όταν ένα
πηγαίο Markdown είναι παρωχημένο, ολόκληρο το μεταφρασμένο αρχείο αναδημιουργείται. Οι φιλοξενούμενες
ενσωματώσεις μπορούν προαιρετικά να περάσουν έναν `TranslationStateProvider` για να διατηρήσουν ανθρώπινες
επεξεργασίες σε μπλοκ πηγής που δεν έχουν αλλάξει.

Ο provider παρέχει το τελευταίο αποδεκτό ζεύγος πηγής/στόχου και καταγράφει κάθε νέο
υποψήφιο. Η αποδοχή παραμένει ευθύνη της ενσωμάτωσης—για παράδειγμα,
μετά τη συγχώνευση ενός pull request μετάφρασης:

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

Για αρχεία Markdown με έγκυρη αποδεκτή βάση, το Co-op Translator ευθυγραμμίζει
τα κορυφαία επίπεδα μπλοκ Markdown. Τα αμετάβλητα μπλοκ πηγής επαναχρησιμοποιούν τα τρέχοντα μεταφρασμένα
μπλοκ, συμπεριλαμβανομένων επεξεργασιών που έγιναν από ανθρώπους; τα αλλαγμένα ή προστιθέμενα μπλοκ πηγής αποστέλλονται
για μετάφραση; τα διαγραμμένα μπλοκ πηγής αφαιρούνται. Εάν η ευθυγράμμιση είναι ασαφής,
η δομή στόχου άλλαξε, μια μετάφραση μπλοκ είναι άκυρη, ή δεν υπάρχει βάση
διαθέσιμη, το Co-op Translator επιστρέφει με ασφάλεια στην υπάρχουσα πλήρους-αρχείου
διαδρομή μετάφρασης.

Αυτό το API αποθηκεύει κατάσταση μετάφρασης εγγράφου, όχι μια δια-εγγράφων μνήμη φράσεων ή
μνήμη μετάφρασης τμημάτων. Επί του παρόντος εφαρμόζεται στη μετάφραση έργου Markdown.
Η συμπεριφορά για notebook και εικόνες παραμένει αμετάβλητη. Η παράδοση `update=True`
ακόμη ζητά πλήρη αναδημιουργία.

Εάν ένα ή περισσότερα αρχεία δεν μπορούν να μεταφραστούν, το `run_translation` εγείρει ένα
`RuntimeError` μετά το τέλος της ροής εργασίας έργου αντί να αναφέρει ένα
επιτυχημένο τρέξιμο με ελλιπή έξοδο. Οι ενσωματώσεις θα πρέπει να το θεωρούν ως αποτυχημένη
εργασία και να διατηρήσουν την προηγούμενη αποδεκτή κατάσταση μετάφρασης.

## Επανεξέταση μεταφρασμένου αποτελέσματος

`run_review` εκτελεί ντετερμινιστικούς ελέγχους μετάφρασης χωρίς διαπιστευτήρια LLM ή Vision.

!!! note "Beta"
    `run_review` είναι μια beta ντετερμινιστική API ανασκόπησης. Δεν καλεί παρόχους μοντέλων ούτε γράφει αρχεία, αλλά οι έλεγχοι και τα σχήματα ζητημάτων ενδέχεται να εξελιχθούν.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Μετά από μετάφραση μόνο README, χρησιμοποιήστε το ίδιο εύρος για την ανασκόπηση:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` ελέγχει μόνο το `README.md` κάτω από κάθε ρυθμισμένη ρίζα πηγής,
συμπεριλαμβανομένων των προσαρμοσμένων `groups` και καταλόγων εξόδου. Άλλα έγγραφα και εμφωλευμένα
README εξαιρούνται. Η έλλειψη αρχικού README εγείρει `ValueError`; αποτυχημένοι
έλεγχοι μετάφρασης εγείρουν `RuntimeError`.

Επανεξέταση μόνο αρχείων που άλλαξαν σε σχέση με μια βάση αναφοράς και εκτύπωση εξόδου με στυλ GitHub:

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

## Παραδείγματα API για Αντιγραφή-Επικόλληση

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

Μεταφράστε και επαναγράψτε συνδέσμους Markdown:

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

Μεταφράστε ένα αποθετήριο από Python:

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

Διατηρήστε όρους γλωσσαρίου:

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

## Δημόσια Σημεία Εισόδου

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

## API Μετάφρασης Περιεχομένου

Τα API μετάφρασης περιεχομένου προορίζονται για ενσωματώσεις που έχουν ήδη περιεχόμενο στη μνήμη, όπως επέκταση επεξεργαστή, εργαλείο MCP, επεξεργαστής notebook ή προσαρμοσμένη ροή.

| Συνάρτηση | Είσοδος | Έξοδος | I/O αρχείων | Σημειώσεις |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Όχι | Ασύγχρονο. Μεταφράζει μόνο περιεχόμενο Markdown. Δεν επαναγράφει συνδέσμους, δεν γράφει μεταδεδομένα, ούτε προσθέτει αποποιήσεις. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Όχι | Ασύγχρονο. Μεταφράζει κελιά Markdown και διατηρεί μη-Markdown κελιά. Δεν επαναγράφει συνδέσμους, δεν γράφει μεταδεδομένα, ούτε προσθέτει αποποιήσεις. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Διαβάζει μόνο την πηγή εικόνας | Συγχρονικό. Εξάγει και μεταφράζει το κείμενο της εικόνας, στη συνέχεια επιστρέφει μια αποδοσμένη εικόνα. Δεν αποθηκεύει μεταδεδομένα μεταφρασμένης εικόνας. |

`translate_markdown_content` και `translate_notebook_content` δέχονται προαιρετικό `source_path` μέσω των επιλογών τους. Η διαδρομή περνάει ως συμφραζόμενο στον μεταφραστή· οι καλούντες παραμένουν υπεύθυνοι για οποιαδήποτε έργου-ειδική επαναγραφή διαδρομών μετά τη μετάφραση.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Οι ίδιες επιλογές μπορούν να περαστούν ως λεξικά:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## APIs Μετάφρασης με Βοήθεια Agent

Τα API με βοήθεια agent δεν καλούν τον ρυθμισμένο πάροχο LLM από το Co-op Translator. Προετοιμάζουν κομμάτια Markdown ή notebook για να τα μεταφράσει ένας host agent, και στη συνέχεια ανασυνθέτουν το τελικό περιεχόμενο από τα μεταφρασμένα κομμάτια.

| Συνάρτηση | Σκοπός |
| --- | --- |
| `start_markdown_agent_translation` | Επιστρέφει μια αυτόνομη εργασία Markdown με κομμάτια, προτροπές, και κατάσταση ανασυγκρότησης. |
| `finish_markdown_agent_translation` | Ανασυνθέτει Markdown από μια εργασία και μεταφρασμένα κομμάτια host-agent. |
| `start_notebook_agent_translation` | Επιστρέφει μια εργασία notebook με κομμάτια κελιών Markdown για μετάφραση από host-agent. |
| `finish_notebook_agent_translation` | Ανασυνθέτει το JSON του notebook διατηρώντας κελιά κώδικα, εξόδους, και μεταδεδομένα. |

Αυτή η ροή εργασίας προορίζεται κυρίως για MCP hosts. Εάν χρειάζεστε μετάφραση αποθετηρίου σε παραγωγή με το Co-op Translator να διαχειρίζεται κλήσεις προς παρόχους, χρησιμοποιήστε `translate_markdown_content`, `translate_notebook_content`, ή `run_translation`.

## APIs Επαναγραφής Διαδρομών

Τα API επαναγραφής διαδρομών δεν εκτελούν μετάφραση. Ενημερώνουν συνδέσμους και διαδρομές στο frontmatter αφού οι καλούντες γνωρίζουν τη διαδρομή πηγής, τη μεταφρασμένη διαδρομή στόχου, και τη διάταξη έργου.

| Συνάρτηση | Εμβέλεια | Σημειώσεις |
| --- | --- | --- |
| `rewrite_markdown_paths` | Σώμα Markdown και frontmatter | Επαναγράφει συνδέσμους Markdown και υποστηριζόμενα πεδία διαδρομών στο frontmatter για έναν μεταφρασμένο στόχο. |
| `rewrite_notebook_paths` | Κελιά Markdown στο JSON του notebook | Εφαρμόζει επαναγραφή διαδρομών Markdown σε κάθε κελί Markdown και αφήνει τα μη-Markdown κελιά αμετάβλητα. |

Ο παράμετρος `policy` μπορεί να είναι ένα λεξικό με αυτά τα πεδία:

| Πεδίο | Υποχρεωτικό | Σκοπός |
| --- | --- | --- |
| `language_code` | Ναι | Κωδικός στόχου γλώσσας, όπως `"ko"` ή `"pt-BR"`. |
| `root_dir` | Όχι | Ρίζα έργου πηγής. Προεπιλογή `"."`. |
| `translations_dir` | Όχι | Κατάλογος εξόδου μεταφρασμένου κειμένου. Προεπιλογή `translations` κάτω από το `root_dir`. |
| `translated_images_dir` | Όχι | Κατάλογος εξόδου μεταφρασμένων εικόνων. Προεπιλογή `translated_images` κάτω από το `root_dir`. |
| `translation_types` | Όχι | Ενεργοί τύποι μετάφρασης. Προεπιλογή σε Markdown, notebooks, και εικόνες. |
| `lang_subdir` | Όχι | Προαιρετικός υποφάκελος κάτω από κάθε φάκελο γλώσσας. |

## Παράμετροι μετάφρασης έργου

| Παράμετρος | Τύπος | Προεπιλογή | Σκοπός |
| --- | --- | --- | --- |
| `language_codes` | `str` | Υποχρεωτικό | Κωδικοί στόχου γλωσσών χωρισμένοι με κενό, όπως `"ko ja fr"`, ή `"all"`. Οι ψευδωνυμικοί κωδικοί κανονικοποιούνται σε κανονικές τιμές BCP 47. |
| `root_dir` | `str` | `"."` | Ρίζα έργου για έναν μεμονωμένο στόχο μετάφρασης. Αγνοείται όταν παρέχονται `root_dirs` ή `groups`. |
| `update` | `bool` | `False` | Διαγράψτε και αναδημιουργήστε υπάρχουσες μεταφράσεις για τις επιλεγμένες γλώσσες. |
| `images` | `bool` | `False` | Συμπεριλάβετε μετάφραση εικόνων. Απαιτεί διαμόρφωση Azure AI Vision. |
| `markdown` | `bool` | `False` | Συμπεριλάβετε μετάφραση Markdown. |
| `notebook` | `bool` | `False` | Συμπεριλάβετε μετάφραση Jupyter notebook. |
| `debug` | `bool` | `False` | Ενεργοποιήστε καταγραφή αποσφαλμάτωσης. |
| `save_logs` | `bool` | `False` | Αποθηκεύστε αρχεία καταγραφής επιπέδου DEBUG κάτω από τον κατάλογο ρίζας `logs/`. |
| `yes` | `bool` | `True` | Αυτόματη επιβεβαίωση των προτροπών για προγραμματική χρήση και CI. |
| `add_disclaimer` | `bool` | `False` | Προσθέτει δηλώσεις αποποίησης μηχανικής μετάφρασης στα μεταφρασμένα Markdown και σημειωματάρια. |
| `translations_dir` | `str \| None` | `None` | Προσαρμοσμένος κατάλογος εξόδου μεταφρασμένου κειμένου. Οι σχετικές διαδρομές επιλύονται σε σχέση με κάθε ρίζα. |
| `image_dir` | `str \| None` | `None` | Προσαρμοσμένος κατάλογος εξόδου για μεταφρασμένες εικόνες. Οι σχετικές διαδρομές επιλύονται σε σχέση με κάθε ρίζα. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Πολλαπλές ρίζες που μοιράζονται τις ίδιες ρυθμίσεις εξόδου. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Ρητά ζεύγη `(root_dir, translations_dir)`. Έχουν προτεραιότητα έναντι του `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Το URL του αποθετηρίου που χρησιμοποιείται κατά την απόδοση οδηγιών πίνακα γλωσσών στο README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Όροι λεξιλογίου που διατηρούνται κατά τη μετάφραση. Οι διπλότυποι και κενές εγγραφές κανονικοποιούνται. |
| `dry_run` | `bool` | `False` | Εκτιμά τον όγκο μετάφρασης και προεπισκοπεί τη συμπεριφορά μετανάστευσης χωρίς εγγραφή αρχείων. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Προαιρετικός adapter διατήρησης αποδεκτού-βάσης και υποψηφίου για σταδιακές ενημερώσεις Markdown. Η παράλειψή του διατηρεί την υπάρχουσα συμπεριφορά πλήρους αρχείου. |

## Παράμετροι Ανασκόπησης

`run_review` σκόπιμα αντικατοπτρίζει τη σύνταξη του `run_translation` όπου είναι δυνατόν, ώστε οι αυτοματισμοί να μπορούν να εναλλάσσονται μεταξύ των ροών εργασίας μετάφρασης και ανασκόπησης με ελάχιστους κλάδους.

| Παράμετρος | Τύπος | Προεπιλογή | Σκοπός |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Φάκελοι γλωσσών στόχων προς ανασκόπηση. Γίνονται δεκτά διαστήματα-χωρισμένα strings και iterable. Το `"all"` ανασκοπεί κάθε ανιχνευμένη γλώσσα μετάφρασης. |
| `root_dir` | `str` | `"."` | Ρίζα έργου για έναν μεμονωμένο στόχο ανασκόπησης. Αγνοείται όταν παρέχονται `root_dirs` ή `groups`. |
| `markdown` | `bool` | `False` | Συμπερίληψη αρχείων πηγής Markdown και MDX. |
| `notebook` | `bool` | `False` | Συμπερίληψη αρχείων πηγής Jupyter notebook. |
| `images` | `bool` | `False` | Κρατημένο για αντιστοιχία με τις επιλογές μετάφρασης. Οι αναφορές συνδέσμων προς εικόνες ελέγχονται από το Markdown. |
| `translations_dir` | `str \| None` | `None` | Προσαρμοσμένος κατάλογος εξόδου μεταφρασμένου κειμένου. Οι σχετικές διαδρομές επιλύονται σε σχέση με κάθε ρίζα. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Πολλαπλές ρίζες που μοιράζονται τις ίδιες ρυθμίσεις εξόδου. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Ρητά ζεύγη `(root_dir, translations_dir)`. Έχουν προτεραιότητα έναντι του `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Αναφορά Git που χρησιμοποιείται για τον περιορισμό της ανασκόπησης σε τροποποιημένα αρχεία πηγής. |
| `readme_only` | `bool` | `False` | Ανασκόπηση μόνο του `README.md` κάτω από κάθε ρίζα πηγής. Η απουσία του README πηγής προκαλεί `ValueError`. |
| `output_format` | `str` | `"text"` | Μορφή εξόδου ανασκόπησης. Οι υποστηριζόμενες τιμές είναι `"text"` και `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Θεωρεί τις προειδοποιήσεις ως αποτυχίες, επιπλέον των σφαλμάτων. |
| `debug` | `bool` | `False` | Ενεργοποίηση καταγραφής εντοπισμού σφαλμάτων. |
| `save_logs` | `bool` | `False` | Αποθήκευση αρχείων καταγραφής επιπέδου DEBUG υπό τον ρίζα κατάλογο `logs/`. |

Αν κανένα από τα `markdown`, `notebook`, ή `images` δεν είναι ρυθμισμένο, η API ανασκοπεί Markdown, σημειωματάρια και αναφορές συνδέσμων εικόνων όπου ισχύει. Η ανασκόπηση δεν καλεί πάροχο LLM και δεν απαιτεί κλειδιά API.

## Απαιτήσεις Διαμόρφωσης

Οι APIs μετάφρασης που υποστηρίζονται από παρόχους απαιτούν διαμόρφωση παρόχου πριν από τη μετάφραση:

- Η μετάφραση Markdown και σημειωματάριων απαιτεί πάροχο LLM. Διαμορφώστε Azure OpenAI, OpenAI ή Anthropic.
- Η μετάφραση εικόνων απαιτεί Azure AI Vision επιπλέον του παρόχου LLM.
- `run_translation` εκτελεί ελαφρούς ελέγχους συνδεσιμότητας πριν ξεκινήσει η μετάφραση του έργου.
- Οι APIs με υποβοήθηση agent `start_*_agent_translation` και `finish_*_agent_translation` δεν καλούν τους LLM παρόχους του Co-op Translator. Η κεντρική εφαρμογή ή ο πράκτορας MCP μεταφράζει τα προετοιμασμένα κομμάτια.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` και `run_review` είναι ντετερμινιστικά και δεν απαιτούν διαπιστευτήρια παρόχου.

Απαιτούμενες μεταβλητές Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Απαιτούμενες μεταβλητές OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Απαιτούμενες μεταβλητές Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` και `ANTHROPIC_MAX_TOKENS` είναι προαιρετικές. Το Microsoft Agent Framework είναι ο προεπιλεγμένος πελάτης μοντέλου για όλους τους παρόχους αρχίζοντας από το Co-op Translator 0.22.0. Μπορεί να επιλεγεί προσωρινά το Semantic Kernel με `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, αλλά κάτι τέτοιο παράγει προειδοποίηση απόσυρσης· δείτε τη [διαμόρφωση](configuration.md#model-client-backend) για το σχέδιο σταδιακής αφαίρεσης.

Απαιτούμενες μεταβλητές Azure AI Vision για μετάφραση εικόνων:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Το `run_review` είναι ντετερμινιστικό και δεν απαιτεί διαμόρφωση LLM ή Azure AI Vision.

## Σημειώσεις Συμπεριφοράς

- Οι APIs μετάφρασης περιεχομένου διατηρούν τη μετάφραση χωριστά από την επαναγραφή διαδρομών έργου. Καλέστε `rewrite_markdown_paths` ή `rewrite_notebook_paths` ρητά όταν το μεταφρασμένο περιεχόμενο χρειάζεται προσαρμογή των project-relative συνδέσμων για έναν στόχο τοποθεσίας.
- Οι APIs ορχήστρωσης έργου προσθέτουν συμπεριφορά έργου γύρω από τη μετάφραση περιεχομένου, συμπεριλαμβανομένης της ανακάλυψης αρχείων, εγγραφών, επαναγραφής διαδρομών, μεταδεδομένων, καθαρισμού και προαιρετικών δηλώσεων αποποίησης.
- Το `run_translation` εκτυπώνει προόδους και συνοπτικές εκτιμήσεις μέσω του ίδιου reporter με Rich που χρησιμοποιεί το CLI. Η μη-διαδραστική έξοδος επανέρχεται σε απλό κείμενο.
- Το `dry_run=True` υπολογίζει εκτιμήσεις χρησιμοποιώντας εικονικές ενημερώσεις README, αλλά δεν εγγράφει το README ή τα αρχεία μετάφρασης.
- Τα `groups` επεξεργάζονται σειριακά. Μια ενιαία συνολική εκτίμηση εκτυπώνεται πριν ξεκινήσει η εργασία.
- Όταν επιλέγεται η μετάφραση εικόνων, η απουσία διαμόρφωσης Vision προκαλεί σφάλμα πριν από την έναρξη της μετάφρασης.
- Εντοπίζονται υπάρχοντες φάκελοι γλωσσών βασισμένοι σε ψευδωνύμια και μπορούν να μετακινηθούν σε κανονικά ονόματα φακέλων BCP 47 ως μέρος της εκτέλεσης.
- Το `run_review` αποτυγχάνει σε περίπτωση απουσίας μεταφρασμένων αρχείων, απουσίας ή ξεπερασμένων μεταδεδομένων μετάφρασης, κακοσχηματισμένου frontmatter/κωδικών φρακτών Markdown και άκυρου μεταφρασμένου JSON σημειωματαρίου.
- Το `run_review` καταγράφει την απουσία τοπικών στόχων Markdown και συνδέσμων εικόνων ως προειδοποιήσεις από προεπιλογή.

## Εσωτερική Διαδρομή Κλήσεων

Η API αναθέτει στην ίδια βασική υλοποίηση που χρησιμοποιεί η CLI:

Μετάφραση:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` για μετάφραση εντός μνήμης.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` για ρητή μετα-επεξεργασία διαδρομών.
3. `co_op_translator.api.translation.run_translation` για πλήρη ορχήστρωση έργου.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Εστιασμένα mixins μετάφρασης έργου για Markdown, σημειωματάρια και εικόνες.
8. Μεταφραστές Markdown, notebook, κειμένου και εικόνας υπό το `co_op_translator.core`.

Ανασκόπηση:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Ντετερμινιστικοί έλεγχοι στο `co_op_translator.review.checks`

Οι παρακάτω κλάσεις είναι χρήσιμες για συντηρητές, αλλά δεν εξάγονται ως σταθερή API σε επίπεδο πακέτου.

| Κλάση | Μονάδα | Ευθύνη |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Συντονίζει τη μετάφραση σε επίπεδο έργου, τη διαχείριση καταλόγων, την κανονικοποίηση μεταδεδομένων ανά γλώσσα και την ανάθεση σε μεταφραστές Markdown, notebook και εικόνας. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Εκτελεί την ασύγχρονη επεξεργασία αρχείων για Markdown, notebook, εικόνες, ανίχνευση εκφυλισμού και ενημερώσεις μεταδεδομένων μετάφρασης. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Ορχηστρώνει την ανάγνωση αρχείων Markdown, τη μετάφραση περιεχομένου, την επαναγραφή διαδρομών, τα μεταδεδομένα, τις δηλώσεις αποποίησης και τις εγγραφές. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Ορχηστρώνει την ανάγνωση αρχείων σημειωματαρίου, τη μετάφραση κελιών Markdown, την επαναγραφή διαδρομών, τα μεταδεδομένα, τις δηλώσεις αποποίησης και τις εγγραφές. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Ορχηστρώνει την ανακάλυψη πηγών εικόνων, τη μετάφραση εικόνων, τους καταλόγους εξόδου, τα μεταδεδομένα και τις εγγραφές. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Εντοπίζει ζεύγη μεταφρασμένων Markdown, αξιολογεί την ποιότητα μετάφρασης και διαβάζει μεταδεδομένα εμπιστοσύνης για ροές εργασίας επισκευής χαμηλής εμπιστοσύνης. |
| `ReviewRunner` | `co_op_translator.review.runner` | Συντονίζει τους ντετερμινιστικούς ελέγχους ανασκόπησης σε αρχεία πηγής, γλώσσες στόχου και ρυθμισμένες ρίζες μετάφρασης. |
| `ReviewTarget` | `co_op_translator.review.targets` | Περιγράφει μια ρίζα πηγής και τον κατάλογο εξόδου μετάφρασης που ανασκοπείται για εκείνη τη ρίζα. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Εντοπίζει παλαιούς φακέλους γλωσσών με ψευδώνυμα και προετοιμάζει σχέδια μετανάστευσης σε κανονικούς φακέλους BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Φορτώνει αρχεία `.env` και ελέγχει αν οι απαιτούμενοι πάροχοι LLM και οι προαιρετικοί πάροχοι Vision είναι διαμορφωμένοι. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Αυτόματη ανίχνευση Azure OpenAI, OpenAI ή Anthropic, επικύρωση απαιτούμενων μεταβλητών περιβάλλοντος και εκτέλεση ελέγχων συνδεσιμότητας παρόχου. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Εντοπίζει τη διαμόρφωση Azure AI Vision και εκτελεί ελέγχους συνδεσιμότητας για μετάφραση εικόνων. |