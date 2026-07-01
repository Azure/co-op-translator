# Ρύθμιση Azure AI

Χρησιμοποιήστε αυτόν τον οδηγό όταν θέλετε να διαμορφώσετε το Azure OpenAI για μετάφραση κειμένου και το Azure AI Vision για εξαγωγή κειμένου από εικόνες.

## Προαπαιτούμενα

- Συνδρομή Azure.
- Δικαιώματα για δημιουργία ή χρήση πόρων Azure AI και αναπτύξεων μοντέλων.
- Ένα έργο στο Azure AI Foundry ή ισοδύναμη πρόσβαση σε πόρους Azure OpenAI και Azure AI Vision.

## Δημιουργία έργου Azure AI

1. Ανοίξτε το [Azure AI Foundry](https://ai.azure.com).
2. Δημιουργήστε ή επιλέξτε ένα έργο.
3. Δημιουργήστε ή επιλέξτε ένα AI hub για το έργο.
4. Ανοίξτε την επισκόπηση του έργου μετά τη δημιουργία.

## Ανάπτυξη μοντέλου Azure OpenAI

1. Στο έργο, ανοίξτε τα **Μοντέλα + endpoints**.
2. Επιλέξτε **Ανάπτυξη μοντέλου**.
3. Επιλέξτε ένα μοντέλο GPT όπως το `gpt-4o`.
4. Αναπτύξτε το μοντέλο.
5. Καταγράψτε το endpoint, το όνομα ανάπτυξης, το όνομα μοντέλου, το κλειδί API και την έκδοση API.

!!! note
    Η έκδοση του Azure OpenAI API είναι ξεχωριστή από την έκδοση του μοντέλου που εμφανίζεται στο Azure AI Foundry. Επιλέξτε μια υποστηριζόμενη έκδοση API για την ανάπτυξή σας.

## Διαμόρφωση Azure AI Vision

Η μετάφραση εικόνων χρησιμοποιεί το Azure AI Vision για εξαγωγή κειμένου από τις αρχικές εικόνες πριν μεταφραστεί το κείμενο.

Στο έργο Azure AI σας, βρείτε το κλειδί και το endpoint της υπηρεσίας Azure AI.

![Βρείτε πληροφορίες για την υπηρεσία Azure AI](../../assets/find-azure-ai-info.png)

Καταγράψτε:

- Endpoint υπηρεσίας Azure AI
- Κλειδί API υπηρεσίας Azure AI

## Μεταβλητές περιβάλλοντος

Προσθέστε τα διαπιστευτήρια στο αρχείο σας `.env` ή στα μυστικά του CI.

```bash
# Azure AI Vision, απαιτείται για τη μετάφραση εικόνων
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, απαιτείται για τη μετάφραση κειμένου
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Το Co-op Translator υποστηρίζει επίσης προαιρετικά εφεδρικά σύνολα διαπιστευτηρίων. Αντιγράψτε ένα πλήρες σύνολο παρόχου με κατάληξη όπως `_1` ή `_2`; όλες οι μεταβλητές σε ένα εφεδρικό σύνολο πρέπει να έχουν την ίδια κατάληξη.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Επόμενα βήματα

- Επιστρέψτε στη [Διαμόρφωση](configuration.md) για να ρυθμίσετε τοπικές ή CI μεταβλητές περιβάλλοντος.
- Χρησιμοποιήστε την [Αναφορά CLI](cli.md) για εντολές μετάφρασης.
- Χρησιμοποιήστε τα [GitHub Actions](github-actions.md) για αυτοματοποίηση των pull requests μετάφρασης.