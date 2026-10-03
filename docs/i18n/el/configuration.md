# Διαμόρφωση

Το Co-op Translator απαιτεί έναν παροχέα γλωσσικού μοντέλου. Η μετάφραση εικόνων απαιτεί επιπλέον το Azure AI Vision.

Η διαμόρφωση διαβάζεται από μεταβλητές περιβάλλοντος. Για τοπικά έργα, τοποθετήστε τες σε ένα αρχείο `.env` στη ρίζα του έργου.

Για την ρύθμιση πόρων Azure, δείτε [Azure AI Setup](azure-ai-setup.md).

## Τοπική ρύθμιση χρόνου εκτέλεσης

Χρησιμοποιήστε ένα virtual environment πριν τρέξετε το CLI τοπικά. Το Co-op Translator υποστηρίζει Python 3.11 έως 3.14.

Για τις κανονικές χρήσεις του CLI, εγκαταστήστε το δημοσιευμένο πακέτο μέσα σε ένα virtual environment:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Ανάπτυξη αποθετηρίου

Για ανάπτυξη του αποθετηρίου, εγκαταστήστε τις εξαρτήσεις από τη ρίζα του έργου αντίθετα:

```bash
poetry install
poetry run translate --help
```

Αφού το CLI είναι διαθέσιμο, ρυθμίστε έναν παροχέα γλωσσικού μοντέλου στο `.env`.

## Επιλογή παρόχου

Το εργαλείο ανιχνεύει αυτόματα παρόχους με αυτή τη σειρά:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Η μετάφραση απαιτεί διαπιστευτήρια παρόχου, εκτός από προεπισκοπήσεις όπως `translate -l "ko" -md --dry-run`. Οι `migrate-links`, `co-op-review` και `run_review` είναι ντετερμινιστικές λειτουργίες συντήρησης και δεν απαιτούν διαπιστευτήρια παρόχου.

## Backend πελάτη μοντέλου

Ξεκινώντας με το Co-op Translator 0.22.0, το Azure OpenAI, το OpenAI και το Anthropic χρησιμοποιούν από προεπιλογή το Microsoft Agent Framework. Δεν απαιτείται ρύθμιση backend για κανονική χρήση.

Το Semantic Kernel παραμένει προσωρινά διαθέσιμο για συμβατότητα. Για να το επιλέξετε ρητά, ορίστε:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Η χρήση του Semantic Kernel προκαλεί προειδοποίηση απόσυρσης. Το πακέτο σχεδιάζεται να μεταφέρει το Semantic Kernel σε προαιρετική εξάρτηση στην έκδοση 0.23.0 και να αφαιρέσει την ενσωμάτωση στην 0.24.0, ανάλογα με τα αποτελέσματα συμβατότητας και τα σχόλια των χρηστών. Το Anthropic απαιτεί `agent-framework`; η ρητή επιλογή `semantic-kernel` με το Anthropic αποτυγχάνει με σφάλμα διαμόρφωσης. Μη έγκυρες τιμές αποτυγχάνουν κατά την αρχικοποίηση του μεταφραστή που υποστηρίζεται από τον πάροχο αντί να υποχωρούν σιωπηλά. Παρακολουθήστε την κυκλοφορία και αναφέρετε εμπόδια στο [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Χρησιμοποιήστε το Azure OpenAI όταν το μοντέλο σας έχει αναπτυχθεί στο Azure AI Foundry ή στην υπηρεσία Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Ο έλεγχος συνδεσιμότητας χρησιμοποιεί το endpoint, το κλειδί API, την έκδοση API και το όνομα ανάπτυξης πριν ξεκινήσει η μετάφραση.

## OpenAI

Χρησιμοποιήστε το OpenAI όταν καλείτε απευθείας το API της OpenAI.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Το `OPENAI_CHAT_MODEL_ID` είναι υποχρεωτικό επειδή ο μεταφραστής χρειάζεται ένα ρητό chat model για κλήσεις API.

Αφήστε τα `OPENAI_ORG_ID` και `OPENAI_BASE_URL` μη ρυθμισμένα για την προεπιλεγμένη ρύθμιση. Προσθέστε ένα ID οργανισμού μόνο αν ο λογαριασμός σας το απαιτεί, ή ένα base URL μόνο όταν χρησιμοποιείτε ένα προσαρμοσμένο endpoint. Μην αντιγράφετε προεπιλεγμένες τιμές κράτησης θέσης για προαιρετικές ρυθμίσεις.

## Anthropic Claude

Χρησιμοποιήστε το Anthropic όταν καλείτε απευθείας το API του Claude. Δημιουργήστε ένα [Anthropic API key](https://platform.claude.com/docs/en/get-started) και επιλέξτε ένα υποστηριζόμενο [Claude model ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Τα `ANTHROPIC_API_KEY` και `ANTHROPIC_MODEL` είναι υποχρεωτικά. Δεν χρειάζεται να ορίσετε το `CO_OP_TRANSLATOR_MODEL_CLIENT`; το Agent Framework είναι το προεπιλεγμένο backend.

Αφήστε το `ANTHROPIC_BASE_URL` μη ρυθμισμένο για το API του Anthropic. Ορίστε το μόνο όταν χρησιμοποιείτε προσαρμοσμένο endpoint.

Το `ANTHROPIC_MAX_TOKENS` έχει προεπιλογή `8192`, που αφήνει χώρο για σενάρια πλούσια σε tokens όπως το Meitei Mayek. Μειώστε το αν το μοντέλο σας ή το Anthropic-συμβατό endpoint περιορίζει την έξοδο κάτω από αυτό.

## Azure AI Vision

Η μετάφραση εικόνων απαιτεί το Azure AI Vision ώστε το εργαλείο να μπορεί να εξάγει κείμενο από εικόνες πριν το διαμορφωμένο γλωσσικό μοντέλο το μεταφράσει. Το Anthropic μπορεί να μεταφράσει το εξαγόμενο κείμενο όπως το Azure OpenAI ή το OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Αν η μετάφραση εικόνων επιλεγεί με `-img`, `images=True`, ή χωρίς φίλτρο τύπου περιεχομένου, το εργαλείο επικυρώνει τη ρύθμιση του Vision πριν ξεκινήσει η μετάφραση.

## Πολλαπλά σετ διαπιστευτηρίων

Το επίπεδο διαμόρφωσης υποστηρίζει πολλαπλά σετ διαπιστευτηρίων προσθέτοντας κατάληξη στις μεταβλητές με τον ίδιο δείκτη:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Κάθε σετ πρέπει να είναι πλήρες. Ο έλεγχος υγείας επιλέγει ένα λειτουργικό σετ πριν συνεχίσει η μετάφραση.

Το OpenAI και το Anthropic υποστηρίζουν την ίδια σύμβαση καταλήξεων. Κρατήστε κάθε μεταβλητή σε ένα σετ διαπιστευτηρίων στην ίδια κατάληξη, συμπεριλαμβανομένων προαιρετικών τιμών όπως `OPENAI_BASE_URL_1` ή `ANTHROPIC_BASE_URL_1`.

## Απαιτήσεις εντολών

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | Yes | No | Μεταφράζει μόνο Markdown. |
| `translate -nb` | Yes | No | Μεταφράζει μόνο notebooks. |
| `translate -img` | Yes | Yes | Μεταφράζει μόνο εικόνες. |
| `translate` with no type flags | Yes | Yes | Η προεπιλεγμένη λειτουργία περιλαμβάνει Markdown, notebooks και εικόνες. |
| `evaluate` | Yes | No | Χρησιμοποιεί αξιολόγηση LLM εκτός αν επιλεγεί `--fast`. |
| `migrate-links` | No | No | Εκτελεί τοπική μετανάστευση συνδέσμων χωρίς κλήσεις προς παρόχους. |
| `co-op-review` | No | No | Εκτελεί ντετερμινιστικούς ελέγχους δομής μετάφρασης, φρεσκάδας, Markdown, notebook και τοπικών συνδέσμων. |
| `run_translation(markdown=True)` | Yes | No | Προγραμματιστική μετάφραση Markdown. |
| `run_translation(images=True)` | Yes | Yes | Προγραμματιστική μετάφραση εικόνων. |
| `run_review(...)` | No | No | Προγραμματιστικός ντετερμινιστικός έλεγχος. |

## Φάκελοι εξόδου

Προεπιλεγμένη έξοδος μετάφρασης κειμένου:

```text
translations/<language-code>/<source-relative-path>
```

Προεπιλεγμένη έξοδος μεταφρασμένης εικόνας:

```text
translated_images/<language-code>/<source-relative-path>
```

Το Python API μπορεί να παρακάμψει αυτούς τους φακέλους με τα `translations_dir` και `image_dir`.