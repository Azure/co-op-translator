# Οδηγός Συντηρητή

Αυτή η σελίδα συνοψίζει πώς είναι διασυνδεδεμένα το API, το CLI και ο ιστότοπος τεκμηρίωσης.

## Δημόσιο όριο API

Το σταθερό Python API εξάγεται από:

```python
co_op_translator.api
```

Η δημόσια API οργανώνεται σε βοηθητικά εργαλεία μετάφρασης περιεχομένου, βοηθητικά εργαλεία επανεγγραφής διαδρομών, ενορχήστρωση έργου και ανασκόπηση:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

Όταν προσθέτετε νέες δημόσιες διεπαφές API, ενημερώστε:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- relevant API tests under `tests/co_op_translator/`, such as `test_api.py` or `test_review_api.py`

Αποφύγετε τη τεκμηρίωση χαμηλότερου επιπέδου μονάδων `core` ως σταθερή διεπαφή API εκτός εάν το έργο σκοπεύει να τις υποστηρίξει άμεσα.

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

`src/co_op_translator/__main__.py` αναθέτει ανάλογα με το όνομα του script:

- `translate` καλεί `co_op_translator.cli.translate.translate_command`
- `evaluate` καλεί `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` καλεί `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` καλεί `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` παρακάμπτει το `__main__.py` και καλεί το `co_op_translator.mcp.server:main` απευθείας.

Όταν προσθέτετε ή αλλάζετε επιλογές CLI, ενημερώστε:

- the relevant `src/co_op_translator/cli/*.py` command
- `docs/cli.md`
- Δοκιμές που σχετίζονται με το CLI, αν αλλάξει η συμπεριφορά

## Διακομιστής MCP

Ο διακομιστής MCP υλοποιείται σε:

```python
co_op_translator.mcp.server
```

Ο διακομιστής σκόπιμα τυλίγει τη δημόσια Python API αντί να καλεί χαμηλότερου επιπέδου μονάδες `core`. Διατηρήστε αυτό το όριο άθικτο ώστε οι πελάτες MCP, οι καλούντες Python και το CLI να μοιράζονται την ίδια συμπεριφορά.

Όταν προσθέτετε ή αλλάζετε εργαλεία MCP, ενημερώστε:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` if the public API surface changes

Τα εργαλεία μετάφρασης αποθετηρίου είναι καλούμενα από μοντέλο μέσω MCP και μπορούν να γράψουν πολλά αρχεία. Διατηρήστε το `dry_run=True` ως προεπιλογή και απαιτήστε `confirm_write=True` πριν από μετάφραση έργου χωρίς dry run.

## Ροή μετάφρασης

Η υψηλού επιπέδου ροή μετάφρασης έργου είναι:

1. Αναλύστε τα ορίσματα του CLI ή τις παραμέτρους του API.
2. Επικυρώστε τη ρύθμιση του LLM με `LLMConfig`.
3. Επικυρώστε το Azure AI Vision όταν επιλεγεί μετάφραση εικόνας.
4. Κανονικοποιήστε τους κωδικούς γλώσσας.
5. Εντοπίστε παλιούς ψευδωνύμους φακέλων γλώσσας.
6. Εκτιμήστε τον όγκο μετάφρασης.
7. Ενημερώστε τις ενότητες γλώσσας/μαθήματος του README όταν ισχύει.
8. Αναθέστε τη μετάφραση του έργου σε `ProjectTranslator`.
9. `ProjectTranslator` αναθέτει την επεξεργασία αρχείων στον `TranslationManager`.

`TranslationManager` αποτελείται από επικεντρωμένα mixins ανά τύπο αρχείου:

- Το `ProjectMarkdownTranslationMixin` χειρίζεται την ανάγνωση αρχείων Markdown, τη μετάφραση περιεχομένου, την επανεγγραφή διαδρομών, τα μεταδεδομένα, τις αποποιήσεις και τις εγγραφές.
- Το `ProjectNotebookTranslationMixin` χειρίζεται την ανάγνωση αρχείων notebook, τη μετάφραση κελιών Markdown, την επανεγγραφή διαδρομών, τα μεταδεδομένα, τις αποποιήσεις και τις εγγραφές.
- Το `ProjectImageTranslationMixin` χειρίζεται την ανίχνευση εικόνων, την εξαγωγή/μετάφραση κειμένου, τις εγγραφές αποδομένων εικόνων και τα μεταδεδομένα.

Οι χαμηλότερου επιπέδου διεπαφές περιεχομένου παρακάμπτουν τη ροή εργασίας του έργου:

1. `translate_markdown_content` και `translate_notebook_content` μεταφράζουν μόνο περιεχόμενο στη μνήμη.
2. `translate_image_content` μεταφράζει κείμενο σε μια εικόνα και επιστρέφει ένα αντικείμενο αποδοθείσας εικόνας.
3. `rewrite_markdown_paths` και `rewrite_notebook_paths` είναι ρητοί βοηθοί μεταεπεξεργασίας. Δεν εκτελούν μετάφραση ούτε εγγραφές έργου.

## Ροή ανασκόπησης

Η ντετερμινιστική ροή ανασκόπησης είναι:

1. Αναλύστε τα ορίσματα του CLI ή τις παραμέτρους του API.
2. Κανονικοποιήστε τους ζητούμενους κωδικούς γλώσσας.
3. Δημιουργήστε έναν ή περισσότερους στόχους ανασκόπησης από `root_dir`, `root_dirs` ή `groups`.
4. Προαιρετικά περιορίστε τα αρχεία προέλευσης με `--changed-from`.
5. Εκτελέστε ντετερμινιστικούς ελέγχους για δομή, φρεσκάδα μετάφρασης, ακεραιότητα Markdown και τοπικές διαδρομές συνδέσμων/εικόνων.
6. Εκτυπώστε είτε κείμενο είτε Markdown με μορφή GitHub.
7. Τερματίστε με αποτυχία όταν βρεθούν σφάλματα ανασκόπησης.

Η ροή ανασκόπησης δεν απαιτεί κλειδιά API και θα πρέπει να παραμείνει κατάλληλη για CI σε pull requests. Η ροή εργασίας pull request γράφει μια περίληψη ελέγχου σε κάθε εκτέλεση και δημοσιεύει σχόλιο PR μόνο όταν το `co-op-review` αποτύχει.

## Ιστότοπος τεκμηρίωσης

Ο ιστότοπος τεκμηρίωσης ρυθμίζεται από:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Ο κατάλογος `docs/` είναι η κανονική πηγή τεκμηρίωσης. Μην προσθέτετε νέους οδηγούς τελικών χρηστών έξω από αυτόν τον κατάλογο εκτός αν το έργο εισάγει σκόπιμα μια άλλη δημοσιευμένη επιφάνεια τεκμηρίωσης.

Κατασκευή τοπικά:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Προεπισκόπηση τοπικά:

```bash
python -m mkdocs serve
```

Ο παραγόμενος ιστότοπος γράφεται στον κατάλογο `site/`, ο οποίος αγνοείται από το git.

## Ροή εργασίας GitHub Pages

Το `.github/workflows/docs.yml` χτίζει τον ιστότοπο σε pull requests και τον αναπτύσσει σε pushes προς το `main`.

Η ροή εργασίας εγκαθιστά:

```bash
pip install -r requirements-docs.txt
```

Η ροή τεκμηρίωσης εγκαθιστά μόνο την αλυσίδα εργαλείων τεκμηρίωσης. Το `mkdocs.yml` δείχνει το `mkdocstrings` στο `src/` ώστε οι σελίδες της δημόσιας API να μπορούν να αποδοθούν από το δέντρο πηγαίου κώδικα χωρίς την εγκατάσταση του πλήρους συνόλου εξαρτήσεων χρόνου εκτέλεσης. Εάν μελλοντικά τα docs API απαιτήσουν την εισαγωγή προαιρετικών παρόχων χρόνου εκτέλεσης κατά τη διάρκεια της κατασκευής, ενημερώστε τόσο το `.github/workflows/docs.yml` όσο και αυτόν τον οδηγό μαζί.

## Πρότυπο ποιότητας τεκμηρίωσης

Πριν συγχωνεύσετε αλλαγές στην τεκμηρίωση, εκτελέστε:

```bash
python -m mkdocs build --strict
git diff --check
```

Χρησιμοποιήστε αυστηρές builds ώστε οι σπασμένοι σύνδεσμοι, οι μη έγκυρες εγγραφές πλοήγησης και τα προβλήματα απεικόνισης της τεκμηρίωσης API να αποτυγχάνουν νωρίς.