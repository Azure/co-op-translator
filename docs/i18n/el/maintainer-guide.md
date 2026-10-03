# Οδηγός Συντηρητή

Αυτή η σελίδα συνοψίζει πώς το API, το CLI και ο ιστότοπος τεκμηρίωσης συνδέονται μεταξύ τους.

## Όριο δημόσιου API

Το σταθερό Python API εξάγεται από:

```python
co_op_translator.api
```

Το δημόσιο API οργανώνεται σε βοηθήματα μετάφρασης περιεχομένου, βοηθήματα επαναγραφής διαδρομών, ορχήστρωση έργου, και ανασκόπηση:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` είναι το όριο επίμονης αποθήκευσης για τις φιλοξενούμενες ενσωματώσεις.
Πρέπει να κρατά τους παραγόμενους υποψηφίους ξεχωριστά από τις αποδεκτές βασικές γραμμές ώστε μια
μη συγχωνευμένη μετάφραση να μην γίνει η πηγή της αλήθειας.

Κατά την προσθήκη νέων δημόσιων API, ενημερώστε:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- σχετικά τεστ του API στο `tests/co_op_translator/`, όπως `test_api.py` ή `test_review_api.py`

Αποφύγετε την τεκμηρίωση των κατώτερων `core` modules ως σταθερό API, εκτός αν το έργο προτίθεται να τα υποστηρίξει άμεσα.

## Σημεία εισόδου CLI

Το πακέτο ορίζει αυτά τα σενάρια Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` δρομολογεί ανά όνομα σεναρίου:

- `translate` καλεί `co_op_translator.cli.translate.translate_command`
- `evaluate` καλεί `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` καλεί `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` καλεί `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` παρακάμπτει το `__main__.py` και καλεί απευθείας `co_op_translator.mcp.server:main`.

Κατά την προσθήκη ή αλλαγή των επιλογών CLI, ενημερώστε:

- την αντίστοιχη εντολή `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- τα τεστ που σχετίζονται με το CLI, εάν η συμπεριφορά αλλάξει

## MCP server

Ο διακομιστής MCP υλοποιείται σε:

```python
co_op_translator.mcp.server
```

Ο διακομιστής εσκεμμένα περιβάλλει το δημόσιο Python API αντί να καλεί τα κατώτερου επιπέδου `core` modules. Διατηρήστε αυτό το όριο ανέπαφο ώστε οι πελάτες MCP, οι καλούντες Python και το CLI να μοιράζονται την ίδια συμπεριφορά.

Κατά την προσθήκη ή αλλαγή εργαλείων MCP, ενημερώστε:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` αν αλλάξει η επιφάνεια του δημόσιου API

Τα εργαλεία μετάφρασης του αποθετηρίου μπορούν να κληθούν από μοντέλο μέσω MCP και μπορούν να γράψουν πολλά αρχεία. Κρατήστε το `dry_run=True` ως προεπιλογή και απαιτήστε `confirm_write=True` πριν από μετάφραση έργου χωρίς dry run.

## Ροή μετάφρασης

Η υψηλού επιπέδου ροή μετάφρασης έργου είναι:

1. Αναλύστε τα ορίσματα CLI ή τις παραμέτρους του API.
2. Επικυρώστε τη διαμόρφωση LLM με `LLMConfig`.
3. Επικυρώστε το Azure AI Vision όταν έχει επιλεγεί μετάφραση εικόνων.
4. Κανονικοποιήστε τους κωδικούς γλωσσών.
5. Εντοπίστε παλιές (legacy) ψευδωνυμίες φακέλων γλώσσας.
6. Εκτιμήστε τον όγκο μετάφρασης.
7. Ενημερώστε τις ενότητες γλώσσας/μαθήματος στο README όταν είναι εφαρμόσιμο.
8. Αναθέστε τη μετάφραση έργου σε `ProjectTranslator`.
9. Το `ProjectTranslator` αναθέτει την επεξεργασία αρχείων στο `TranslationManager`.

`TranslationManager` είναι αποτελούμενο από mixins εστιασμένους σε τύπους αρχείων:

- `ProjectMarkdownTranslationMixin` χειρίζεται την ανάγνωση αρχείων Markdown, τη μετάφραση περιεχομένου, την επαναγραφή διαδρομών, τα μεταδεδομένα, τις αποποιήσεις και τις εγγραφές.
- `ProjectNotebookTranslationMixin` χειρίζεται την ανάγνωση αρχείων notebook, τη μετάφραση κελιών Markdown, την επαναγραφή διαδρομών, τα μεταδεδομένα, τις αποποιήσεις και τις εγγραφές.
- `ProjectImageTranslationMixin` χειρίζεται την ανίχνευση εικόνων, την εξαγωγή/μετάφραση κειμένου, την απόδοση και εγγραφή εικόνων, και τα μεταδεδομένα.

Τα κατώτερου επιπέδου API περιεχομένου παραλείπουν τη ροή εργασίας του έργου:

1. `translate_markdown_content` και `translate_notebook_content` μεταφράζουν μόνο περιεχόμενο στη μνήμη.
2. `translate_image_content` μεταφράζει κείμενο σε μια μεμονωμένη εικόνα και επιστρέφει ένα αποδομένο αντικείμενο εικόνας.
3. `rewrite_markdown_paths` και `rewrite_notebook_paths` είναι ρητά βοηθήματα μετα-επεξεργασίας. Δεν κάνουν μετάφραση ούτε εγγραφές έργου.

## Ροή αναθεώρησης

Η ντετερμινιστική ροή ανασκόπησης είναι:

1. Αναλύστε τα ορίσματα CLI ή τις παραμέτρους του API.
2. Κανονικοποιήστε τους ζητούμενους κωδικούς γλωσσών.
3. Δημιουργήστε έναν ή περισσότερους στόχους ανασκόπησης από `root_dir`, `root_dirs`, ή `groups`.
4. Προαιρετικά περιορίστε τα αρχεία προέλευσης με `--changed-from`.
5. Εκτελέστε ντετερμινιστικούς ελέγχους για δομή, φρεσκάδα μετάφρασης, ακεραιότητα Markdown και τοπικές διαδρομές συνδέσμων/εικόνων.
6. Εκτυπώστε είτε απλό κείμενο είτε Markdown συμβατό με GitHub.
7. Εξέλθετε με αποτυχία όταν εντοπίζονται σφάλματα ανασκόπησης.

Η ροή ανασκόπησης δεν απαιτεί κλειδιά API και παραμένει διαθέσιμη για τοπικούς ελέγχους ή προαιρετικό CI καταναλωτή. Αυτό το αποθετήριο δεν εκτελεί `co-op-review` αυτόματα σε κάθε pull request.

## Ιστότοπος τεκμηρίωσης

Ο ιστότοπος τεκμηρίωσης ρυθμίζεται από:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Ο κατάλογος `docs/` είναι η κανονική πηγή τεκμηρίωσης. Μην προσθέτετε νέους οδηγούς τελικού χρήστη εκτός αυτού του καταλόγου εκτός εάν το έργο εισάγει σκόπιμα άλλη δημοσιευμένη επιφάνεια τεκμηρίωσης.

Δημιουργία τοπικά:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Προεπισκόπηση τοπικά:

```bash
python -m mkdocs serve
```

Ο παραγόμενος ιστότοπος γράφεται στο `site/`, το οποίο αγνοείται από το git.

## Ροή εργασίας GitHub Pages

`.github/workflows/docs.yml` χτίζει τον ιστότοπο στις pull requests και τον αναπτύσσει σε pushes στο `main`.

Η ροή εργασίας εγκαθιστά:

```bash
pip install -r requirements-docs.txt
```

Η ροή εργασίας τεκμηρίωσης εγκαθιστά μόνο την αλυσίδα εργαλείων τεκμηρίωσης. Το `mkdocs.yml` δείχνει το `mkdocstrings` στο `src/` ώστε οι σελίδες του δημόσιου API να μπορούν να αποδοθούν από το δέντρο πηγαίου κώδικα χωρίς την εγκατάσταση του πλήρους συνόλου εξαρτήσεων χρόνου εκτέλεσης. Εάν μελλοντική τεκμηρίωση API απαιτήσει εισαγωγή προαιρετικών παρόχων χρόνου εκτέλεσης κατά τη διάρκεια της κατασκευής, ενημερώστε τόσο το `.github/workflows/docs.yml` όσο και αυτόν τον οδηγό μαζί.

## Πρότυπο ποιότητας τεκμηρίωσης

Πριν συγχωνεύσετε αλλαγές τεκμηρίωσης, εκτελέστε:

```bash
python -m mkdocs build --strict
git diff --check
```

Χρησιμοποιήστε αυστηρές κατασκευές ώστε σπασμένοι σύνδεσμοι, μη έγκυρες εγγραφές πλοήγησης και προβλήματα απόδοσης API να αποτυγχάνουν νωρίς.