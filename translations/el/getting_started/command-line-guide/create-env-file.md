<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:26:50+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "el"
}
-->
# Δημιουργήστε το αρχείο *.env* στον ριζικό φάκελο

Σε αυτό το σεμινάριο, θα σας καθοδηγήσουμε στη ρύθμιση των μεταβλητών περιβάλλοντος για τις υπηρεσίες Azure χρησιμοποιώντας ένα αρχείο *.env*. Οι μεταβλητές περιβάλλοντος σας επιτρέπουν να διαχειρίζεστε με ασφάλεια ευαίσθητα διαπιστευτήρια, όπως κλειδιά API, χωρίς να τα ενσωματώνετε απευθείας στον κώδικά σας.

> [!IMPORTANT]
> - Απαιτείται να ρυθμιστεί μόνο μία υπηρεσία μοντέλου γλώσσας (Azure OpenAI ή OpenAI). Συμπληρώστε τις μεταβλητές περιβάλλοντος για την υπηρεσία που προτιμάτε. Εάν οριστούν μεταβλητές περιβάλλοντος για πολλαπλά μοντέλα γλώσσας, ο μεταφραστής συνεργασίας θα επιλέξει μία βάσει προτεραιότητας.
> - Εάν δεν οριστούν μεταβλητές περιβάλλοντος για το Computer Vision, ο μεταφραστής θα μεταβεί αυτόματα σε [λειτουργία μόνο Markdown](./markdown-only-mode.md).

> [!NOTE]
> Αυτός ο οδηγός εστιάζει κυρίως στις υπηρεσίες Azure, αλλά μπορείτε να επιλέξετε οποιοδήποτε υποστηριζόμενο μοντέλο γλώσσας από τη [λίστα υποστηριζόμενων μοντέλων και υπηρεσιών](../README.md#-supported-models-and-services).

## Δημιουργία του αρχείου *.env*

Στον ριζικό φάκελο του έργου σας, δημιουργήστε ένα αρχείο με όνομα *.env*. Σε αυτό το αρχείο θα αποθηκεύσετε όλες τις μεταβλητές περιβάλλοντος σε απλή μορφή.

> [!WARNING]
> Μην προσθέτετε το αρχείο *.env* σε συστήματα ελέγχου έκδοσης όπως το Git. Προσθέστε το *.env* στο αρχείο .gitignore για να αποφύγετε τυχαίες προσθήκες.

1. Μεταβείτε στον ριζικό φάκελο του έργου σας.

1. Δημιουργήστε ένα αρχείο *.env* στον ριζικό φάκελο του έργου σας.

1. Ανοίξτε το αρχείο *.env* και επικολλήστε το ακόλουθο πρότυπο:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> Εάν θέλετε να βρείτε τα κλειδιά API και τα endpoints σας, μπορείτε να ανατρέξετε στο [set-up-azure-ai.md](../set-up-azure-ai.md).

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στην αρχική του γλώσσα πρέπει να θεωρείται η επίσημη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.