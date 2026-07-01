# Διαμόρφωση

Το Co-op Translator απαιτεί έναν πάροχο μοντέλου γλώσσας. Η μετάφραση εικόνων επιπλέον απαιτεί το Azure AI Vision.

Η διαμόρφωση διαβάζεται από μεταβλητές περιβάλλοντος. Για τοπικά έργα, τοποθετήστε τις σε ένα αρχείο `.env` στη ρίζα του έργου.

Για τη ρύθμιση πόρων Azure, δείτε το [Ρύθμιση Azure AI](azure-ai-setup.md).

## Τοπική ρύθμιση χρόνου εκτέλεσης

Χρησιμοποιήστε ένα εικονικό περιβάλλον πριν εκτελέσετε το CLI τοπικά. Το Co-op Translator υποστηρίζει Python 3.10 έως 3.12.

Για τη συνήθη χρήση του CLI, εγκαταστήστε το δημοσιευμένο πακέτο μέσα σε ένα εικονικό περιβάλλον:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Για ανάπτυξη του αποθετηρίου, εγκαταστήστε τις εξαρτήσεις από τη ρίζα του έργου αντί αυτού:

```bash
poetry install
poetry run translate --help
```

Αφού το CLI είναι διαθέσιμο, διαμορφώστε έναν πάροχο μοντέλου γλώσσας στο `.env`.

## Επιλογή παρόχου

Το εργαλείο ανιχνεύει αυτόματα τους παρόχους με αυτή τη σειρά:

1. Azure OpenAI
2. OpenAI

Εάν κανένας από τους παρόχους δεν έχει διαμορφωθεί, οι `translate`, `evaluate`, `migrate-links` και `run_translation` αποτυγχάνουν κατά τους ελέγχους διαμόρφωσης. Τα `co-op-review` και `run_review` είναι ντετερμινιστικοί έλεγχοι συντήρησης και δεν απαιτούν διαπιστευτήρια παρόχου.

## Azure OpenAI

Χρησιμοποιήστε το Azure OpenAI όταν το μοντέλο σας είναι αναπτυγμένο στο Azure AI Foundry ή στο Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Ο έλεγχος συνδεσιμότητας χρησιμοποιεί το endpoint, το API key, την API version και το deployment name πριν ξεκινήσει η μετάφραση.

## OpenAI

Χρησιμοποιήστε το OpenAI όταν καλείτε απευθείας το OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # προαιρετικό
OPENAI_BASE_URL="..."        # προαιρετικό
```

`OPENAI_CHAT_MODEL_ID` απαιτείται επειδή ο μεταφραστής χρειάζεται ένα ρητό chat model για κλήσεις API.

## Azure AI Vision

Η μετάφραση εικόνων απαιτεί το Azure AI Vision ώστε το εργαλείο να μπορεί να εξάγει κείμενο από εικόνες πριν το μεταφράσει.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Εάν η μετάφραση εικόνων επιλεγεί με `-img`, `images=True`, ή χωρίς φίλτρο τύπου περιεχομένου, το εργαλείο επικυρώνει τη διαμόρφωση του Vision πριν ξεκινήσει η μετάφραση.

## Πολλαπλά σύνολα διαπιστευτηρίων

Το επίπεδο διαμόρφωσης υποστηρίζει πολλαπλά σύνολα διαπιστευτηρίων προσθέτοντας επίθημα στις μεταβλητές με τον ίδιο δείκτη:

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

Κάθε σύνολο πρέπει να είναι πλήρες. Ο έλεγχος υγείας επιλέγει ένα λειτουργικό σύνολο πριν προχωρήσει η μετάφραση.

## Απαιτήσεις εντολών

| Εντολή ή API | Απαιτείται LLM | Απαιτείται Vision | Σημειώσεις |
| --- | --- | --- | --- |
| `translate -md` | Ναι | Όχι | Μεταφράζει μόνο Markdown. |
| `translate -nb` | Ναι | Όχι | Μεταφράζει μόνο σημειωματάρια. |
| `translate -img` | Ναι | Ναι | Μεταφράζει μόνο εικόνες. |
| `translate` with no type flags | Ναι | Ναι | Η προεπιλεγμένη λειτουργία περιλαμβάνει Markdown, σημειωματάρια και εικόνες. |
| `evaluate` | Ναι | Όχι | Χρησιμοποιεί αξιολόγηση LLM εκτός εάν επιλεγεί το `--fast`. |
| `migrate-links` | Ναι | Όχι | Εκτελεί μετανάστευση συνδέσμων, αλλά εξακολουθεί να εκτελεί τους κοινούς ελέγχους διαμόρφωσης. |
| `co-op-review` | Όχι | Όχι | Διενεργεί ντετερμινιστικούς ελέγχους για τη δομή μετάφρασης, την επικαιρότητα, το Markdown, τα σημειωματάρια και τους τοπικούς συνδέσμους. |
| `run_translation(markdown=True)` | Ναι | Όχι | Προγραμματική μετάφραση Markdown. |
| `run_translation(images=True)` | Ναι | Ναι | Προγραμματική μετάφραση εικόνων. |
| `run_review(...)` | Όχι | Όχι | Προγραμματική ντετερμινιστική ανασκόπηση. |

## Κατάλογοι εξόδου

Προεπιλεγμένη έξοδος μετάφρασης κειμένου:

```text
translations/<language-code>/<source-relative-path>
```

Προεπιλεγμένη έξοδος μεταφρασμένων εικόνων:

```text
translated_images/<language-code>/<source-relative-path>
```

Το Python API μπορεί να παρακάμψει αυτούς τους καταλόγους με τα `translations_dir` και `image_dir`.