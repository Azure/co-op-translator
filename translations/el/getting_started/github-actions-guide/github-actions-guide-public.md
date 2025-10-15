<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T03:15:09+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "el"
}
-->
# Χρήση του Co-op Translator GitHub Action (Δημόσια Ρύθμιση)

**Απευθύνεται σε:** Αυτός ο οδηγός προορίζεται για χρήστες σε δημόσια ή ιδιωτικά αποθετήρια όπου τα τυπικά δικαιώματα GitHub Actions είναι επαρκή. Χρησιμοποιεί το ενσωματωμένο `GITHUB_TOKEN`.

Αυτοματοποιήστε τη μετάφραση της τεκμηρίωσης του αποθετηρίου σας εύκολα με το Co-op Translator GitHub Action. Ο οδηγός αυτός σας καθοδηγεί στη ρύθμιση της ενέργειας ώστε να δημιουργεί αυτόματα pull requests με ενημερωμένες μεταφράσεις κάθε φορά που αλλάζουν τα αρχεία Markdown ή οι εικόνες πηγής σας.

> [!IMPORTANT]
>
> **Επιλογή σωστού οδηγού:**
>
> Αυτός ο οδηγός περιγράφει τη **πιο απλή ρύθμιση με χρήση του τυπικού `GITHUB_TOKEN`**. Αυτή είναι η προτεινόμενη μέθοδος για τους περισσότερους χρήστες, καθώς δεν απαιτεί διαχείριση ευαίσθητων Private Keys για GitHub App.
>

## Προαπαιτούμενα

Πριν ρυθμίσετε το GitHub Action, βεβαιωθείτε ότι έχετε έτοιμα τα απαραίτητα διαπιστευτήρια για την υπηρεσία AI.

**1. Απαραίτητο: Διαπιστευτήρια AI Language Model**
Χρειάζεστε διαπιστευτήρια για τουλάχιστον ένα υποστηριζόμενο Language Model:

- **Azure OpenAI**: Απαιτεί Endpoint, API Key, Model/Deployment Names, API Version.
- **OpenAI**: Απαιτεί API Key, (Προαιρετικά: Org ID, Base URL, Model ID).
- Δείτε [Υποστηριζόμενα Μοντέλα και Υπηρεσίες](../../../../README.md) για λεπτομέρειες.

**2. Προαιρετικό: Διαπιστευτήρια AI Vision (για Μετάφραση Εικόνων)**

- Απαιτούνται μόνο αν θέλετε να μεταφράσετε κείμενο μέσα σε εικόνες.
- **Azure AI Vision**: Απαιτεί Endpoint και Subscription Key.
- Αν δεν δοθούν, η ενέργεια λειτουργεί σε [λειτουργία μόνο Markdown](../markdown-only-mode.md).

## Ρύθμιση και Παραμετροποίηση

Ακολουθήστε τα παρακάτω βήματα για να ρυθμίσετε το Co-op Translator GitHub Action στο αποθετήριό σας χρησιμοποιώντας το τυπικό `GITHUB_TOKEN`.

### Βήμα 1: Κατανόηση Αυθεντικοποίησης (Χρήση `GITHUB_TOKEN`)

Αυτό το workflow χρησιμοποιεί το ενσωματωμένο `GITHUB_TOKEN` που παρέχει το GitHub Actions. Το token αυτό δίνει αυτόματα δικαιώματα στο workflow να αλληλεπιδρά με το αποθετήριό σας, σύμφωνα με τις ρυθμίσεις που θα ορίσετε στο **Βήμα 3**.

### Βήμα 2: Ρύθμιση Μυστικών του Αποθετηρίου

Χρειάζεται μόνο να προσθέσετε τα **διαπιστευτήρια της υπηρεσίας AI** ως κρυπτογραφημένα μυστικά στις ρυθμίσεις του αποθετηρίου σας.

1.  Μεταβείτε στο αποθετήριο σας στο GitHub.
2.  Επιλέξτε **Settings** > **Secrets and variables** > **Actions**.
3.  Στην ενότητα **Repository secrets**, κάντε κλικ στο **New repository secret** για κάθε απαραίτητο μυστικό υπηρεσίας AI που αναφέρεται παρακάτω.

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.el.png" alt="Επιλογή ρύθμισης action"> *(Αναφορά εικόνας: Δείχνει πού προσθέτετε τα μυστικά)*

**Απαραίτητα Μυστικά Υπηρεσίας AI (Προσθέστε ΟΛΑ όσα ισχύουν σύμφωνα με τα Προαπαιτούμενα):**

| Όνομα Μυστικού                         | Περιγραφή                               | Πηγή Τιμής                     |
| :------------------------------------- | :-------------------------------------- | :----------------------------- |
| `AZURE_AI_SERVICE_API_KEY`             | Κλειδί για Azure AI Service (Computer Vision)  | Το Azure AI Foundry σας               |
| `AZURE_AI_SERVICE_ENDPOINT`            | Endpoint για Azure AI Service (Computer Vision) | Το Azure AI Foundry σας               |
| `AZURE_OPENAI_API_KEY`                 | Κλειδί για Azure OpenAI service              | Το Azure AI Foundry σας               |
| `AZURE_OPENAI_ENDPOINT`                | Endpoint για Azure OpenAI service         | Το Azure AI Foundry σας               |
| `AZURE_OPENAI_MODEL_NAME`              | Όνομα μοντέλου Azure OpenAI              | Το Azure AI Foundry σας               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`    | Όνομα deployment Azure OpenAI            | Το Azure AI Foundry σας               |
| `AZURE_OPENAI_API_VERSION`             | Έκδοση API για Azure OpenAI              | Το Azure AI Foundry σας               |
| `OPENAI_API_KEY`                       | API Key για OpenAI                        | Η πλατφόρμα OpenAI σας              |
| `OPENAI_ORG_ID`                        | OpenAI Organization ID (Προαιρετικό)         | Η πλατφόρμα OpenAI σας              |
| `OPENAI_CHAT_MODEL_ID`                 | Συγκεκριμένο OpenAI model ID (Προαιρετικό)       | Η πλατφόρμα OpenAI σας              |
| `OPENAI_BASE_URL`                      | Custom OpenAI API Base URL (Προαιρετικό)     | Η πλατφόρμα OpenAI σας              |

### Βήμα 3: Ρύθμιση Δικαιωμάτων Workflow

Το GitHub Action χρειάζεται δικαιώματα μέσω του `GITHUB_TOKEN` για να κάνει checkout τον κώδικα και να δημιουργεί pull requests.

1.  Στο αποθετήριό σας, πηγαίνετε στο **Settings** > **Actions** > **General**.
2.  Κάντε scroll στην ενότητα **Workflow permissions**.
3.  Επιλέξτε **Read and write permissions**. Αυτό δίνει στο `GITHUB_TOKEN` τα απαραίτητα δικαιώματα `contents: write` και `pull-requests: write` για το workflow.
4.  Βεβαιωθείτε ότι το checkbox για **Allow GitHub Actions to create and approve pull requests** είναι **επιλεγμένο**.
5.  Πατήστε **Save**.

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.el.png" alt="Ρύθμιση δικαιωμάτων">

### Βήμα 4: Δημιουργία Αρχείου Workflow

Τέλος, δημιουργήστε το YAML αρχείο που ορίζει το αυτοματοποιημένο workflow με χρήση του `GITHUB_TOKEN`.

1.  Στον root φάκελο του αποθετηρίου σας, δημιουργήστε τον φάκελο `.github/workflows/` αν δεν υπάρχει ήδη.
2.  Μέσα στο `.github/workflows/`, δημιουργήστε ένα αρχείο με όνομα `co-op-translator.yml`.
3.  Επικολλήστε το παρακάτω περιεχόμενο στο `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **Προσαρμόστε το Workflow:**
  - **[!IMPORTANT] Γλώσσες-στόχοι:** Στο βήμα `Run Co-op Translator`, **ΠΡΕΠΕΙ να ελέγξετε και να τροποποιήσετε τη λίστα των κωδικών γλωσσών** μέσα στην εντολή `translate -l "..." -y` ώστε να ταιριάζει με τις ανάγκες του project σας. Η παράδειγμα λίστα (`ar de es...`) πρέπει να αντικατασταθεί ή να προσαρμοστεί.
  - **Trigger (`on:`):** Το τρέχον trigger εκτελείται σε κάθε push στο `main`. Για μεγάλα αποθετήρια, σκεφτείτε να προσθέσετε ένα φίλτρο `paths:` (δείτε το σχολιασμένο παράδειγμα στο YAML) ώστε το workflow να τρέχει μόνο όταν αλλάζουν σχετικά αρχεία (π.χ. τεκμηρίωση πηγής), εξοικονομώντας χρόνο εκτέλεσης.
  - **Λεπτομέρειες PR:** Προσαρμόστε το `commit-message`, `title`, `body`, το όνομα του `branch` και τα `labels` στο βήμα `Create Pull Request` αν χρειάζεται.

## Εκτέλεση του Workflow

> [!WARNING]  
> **Χρονικό Όριο Εκτέλεσης GitHub-hosted Runner:**  
> Τα GitHub-hosted runners όπως το `ubuntu-latest` έχουν **μέγιστο όριο εκτέλεσης 6 ώρες**.  
> Για μεγάλα αποθετήρια τεκμηρίωσης, αν η διαδικασία μετάφρασης ξεπεράσει τις 6 ώρες, το workflow θα τερματιστεί αυτόματα.  
> Για να το αποφύγετε:  
> - Χρησιμοποιήστε **self-hosted runner** (χωρίς χρονικό όριο)  
> - Μειώστε τον αριθμό των γλωσσών-στόχων ανά εκτέλεση

Μόλις το αρχείο `co-op-translator.yml` συγχωνευτεί στο κύριο branch σας (ή στο branch που ορίζεται στο trigger `on:`), το workflow θα εκτελείται αυτόματα κάθε φορά που γίνονται αλλαγές σε αυτό το branch (και ταιριάζουν με το φίλτρο `paths`, αν έχει ρυθμιστεί).

---

**Αποποίηση Ευθύνης**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρότι καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.