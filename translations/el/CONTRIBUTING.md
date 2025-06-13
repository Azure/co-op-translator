<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:34:51+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "el"
}
-->
# Συμβολή στο Co-op Translator

Αυτό το έργο καλωσορίζει συνεισφορές και προτάσεις. Οι περισσότερες συνεισφορές απαιτούν να συμφωνήσετε με μια  
Συμφωνία Άδειας Συμβολής (CLA) που δηλώνει ότι έχετε το δικαίωμα και πράγματι παραχωρείτε σε εμάς  
τα δικαιώματα χρήσης της συνεισφοράς σας. Για λεπτομέρειες, επισκεφθείτε το https://cla.opensource.microsoft.com.

Όταν υποβάλλετε ένα pull request, ένας bot CLA θα καθορίσει αυτόματα αν χρειάζεται να παρέχετε  
μια CLA και θα προσθέσει τα κατάλληλα στοιχεία στο PR (π.χ. έλεγχο κατάστασης, σχόλιο). Απλώς ακολουθήστε τις οδηγίες  
που παρέχει ο bot. Θα χρειαστεί να το κάνετε μόνο μία φορά για όλα τα repos που χρησιμοποιούν την CLA μας.

## Ρύθμιση περιβάλλοντος ανάπτυξης

Για να ρυθμίσετε το περιβάλλον ανάπτυξης για αυτό το έργο, προτείνουμε τη χρήση του Poetry για τη διαχείριση εξαρτήσεων. Χρησιμοποιούμε `pyproject.toml` για τη διαχείριση των εξαρτήσεων του έργου, και επομένως, για να εγκαταστήσετε τις εξαρτήσεις, θα πρέπει να χρησιμοποιήσετε το Poetry.

### Δημιουργία εικονικού περιβάλλοντος

#### Χρήση pip

```bash
python -m venv .venv
```

#### Χρήση Poetry

```bash
poetry init
```

### Ενεργοποίηση του εικονικού περιβάλλοντος

#### Για pip και Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Χρήση Poetry

```bash
poetry shell
```

### Εγκατάσταση του πακέτου και των απαιτούμενων πακέτων

#### Χρήση Poetry (από pyproject.toml)

```bash
poetry install
```

### Χειροκίνητος έλεγχος

Πριν υποβάλετε ένα PR, είναι σημαντικό να δοκιμάσετε τη λειτουργία μετάφρασης με πραγματική τεκμηρίωση:

1. Δημιουργήστε έναν φάκελο δοκιμών στον ριζικό κατάλογο:
    ```bash
    mkdir test_docs
    ```

2. Αντιγράψτε κάποια αρχεία markdown και εικόνες που θέλετε να μεταφράσετε στον φάκελο δοκιμών. Για παράδειγμα:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Εγκαταστήστε το πακέτο τοπικά:
    ```bash
    pip install -e .
    ```

4. Εκτελέστε το Co-op Translator στα αρχεία δοκιμών σας:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Ελέγξτε τα μεταφρασμένα αρχεία στο `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Συμπληρώστε τις μεταβλητές περιβάλλοντος όπως υποδεικνύεται.

> [!TIP]
>
> ### Επιπλέον επιλογές περιβάλλοντος ανάπτυξης
>
> Εκτός από την εκτέλεση του έργου τοπικά, μπορείτε επίσης να χρησιμοποιήσετε GitHub Codespaces ή VS Code Dev Containers για εναλλακτική ρύθμιση περιβάλλοντος ανάπτυξης.
>
> #### GitHub Codespaces
>
> Μπορείτε να τρέξετε αυτά τα δείγματα εικονικά χρησιμοποιώντας το GitHub Codespaces χωρίς επιπλέον ρυθμίσεις ή εγκαταστάσεις.
>
> Το κουμπί θα ανοίξει μια web-based έκδοση του VS Code στον browser σας:
>
> 1. Ανοίξτε το πρότυπο (μπορεί να χρειαστούν μερικά λεπτά):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Τοπική εκτέλεση με VS Code Dev Containers
>
> ⚠️ Αυτή η επιλογή λειτουργεί μόνο αν το Docker Desktop έχει τουλάχιστον 16 GB RAM διαθέσιμα. Αν έχετε λιγότερα από 16 GB RAM, μπορείτε να δοκιμάσετε την επιλογή [GitHub Codespaces](../..) ή να την [ρυθμίσετε τοπικά](../..).
>
> Μια σχετική επιλογή είναι τα VS Code Dev Containers, που ανοίγουν το έργο στο τοπικό VS Code χρησιμοποιώντας την [επέκταση Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Ξεκινήστε το Docker Desktop (εγκαταστήστε το αν δεν είναι ήδη εγκατεστημένο)
> 2. Ανοίξτε το έργο:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Στυλ Κώδικα

Χρησιμοποιούμε το [Black](https://github.com/psf/black) ως formatter κώδικα Python για να διατηρήσουμε συνεπή στυλ κώδικα σε όλο το έργο. Το Black είναι ένας αμείλικτος formatter που αναμορφώνει αυτόματα τον κώδικα Python ώστε να ακολουθεί το στυλ του Black.

#### Ρυθμίσεις

Η ρύθμιση του Black καθορίζεται στο `pyproject.toml` μας:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Εγκατάσταση Black

Μπορείτε να εγκαταστήσετε το Black είτε με Poetry (προτεινόμενο) είτε με pip:

##### Χρήση Poetry

Το Black εγκαθίσταται αυτόματα όταν ρυθμίζετε το περιβάλλον ανάπτυξης:
```bash
poetry install
```

##### Χρήση pip

Αν χρησιμοποιείτε pip, μπορείτε να εγκαταστήσετε το Black απευθείας:
```bash
pip install black
```

#### Χρήση Black

##### Με Poetry

1. Μορφοποιήστε όλα τα αρχεία Python στο έργο:
    ```bash
    poetry run black .
    ```

2. Μορφοποιήστε ένα συγκεκριμένο αρχείο ή φάκελο:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Με pip

1. Μορφοποιήστε όλα τα αρχεία Python στο έργο:
    ```bash
    black .
    ```

2. Μορφοποιήστε ένα συγκεκριμένο αρχείο ή φάκελο:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Συνιστούμε να ρυθμίσετε τον επεξεργαστή σας ώστε να μορφοποιεί αυτόματα τον κώδικα με το Black κατά την αποθήκευση. Οι περισσότεροι σύγχρονοι επεξεργαστές υποστηρίζουν αυτό μέσω επεκτάσεων ή plugins.

## Εκτέλεση Co-op Translator

Για να τρέξετε το Co-op Translator χρησιμοποιώντας το Poetry στο περιβάλλον σας, ακολουθήστε τα εξής βήματα:

1. Μεταβείτε στον φάκελο όπου θέλετε να εκτελέσετε δοκιμές μετάφρασης ή δημιουργήστε έναν προσωρινό φάκελο για δοκιμές.

2. Εκτελέστε την παρακάτω εντολή. Η παράμετρος `-l ko` with the language code you wish to translate into. The `-d` σημαίνει λειτουργία αποσφαλμάτωσης.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Βεβαιωθείτε ότι το περιβάλλον Poetry είναι ενεργοποιημένο (poetry shell) πριν τρέξετε την εντολή.

## Συντηρητές

### Μήνυμα commit και στρατηγική συγχώνευσης

Για να διασφαλίσουμε τη συνέπεια και την καθαρότητα στο ιστορικό commit του έργου μας, ακολουθούμε ένα συγκεκριμένο format μηνύματος commit **για το τελικό μήνυμα commit** όταν χρησιμοποιούμε τη στρατηγική **Squash and Merge**.

Όταν ένα pull request (PR) συγχωνεύεται, τα επιμέρους commits συμπιέζονται σε ένα ενιαίο commit. Το τελικό μήνυμα commit πρέπει να ακολουθεί το παρακάτω format για να διατηρείται ένα καθαρό και συνεπές ιστορικό.

#### Format μηνύματος commit (για squash and merge)

Χρησιμοποιούμε το ακόλουθο format για τα μηνύματα commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Καθορίζει την κατηγορία του commit. Χρησιμοποιούμε τους εξής τύπους:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Ενημέρωση οδηγιών εγκατάστασης για μεγαλύτερη σαφήνεια (#50)`
- `Core: Βελτίωση χειρισμού μετάφρασης εικόνων (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `διόρθωση ορθογραφικού λάθους`
- `ενημέρωση README`
- `προσαρμογή μορφοποίησης`

They should be squashed into:
`Docs: Βελτίωση σαφήνειας και μορφοποίησης τεκμηρίωσης (#65)`

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η επίσημη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.