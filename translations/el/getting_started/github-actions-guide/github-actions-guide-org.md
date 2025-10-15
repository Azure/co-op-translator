<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:14:39+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "el"
}
-->
# Χρήση του Co-op Translator GitHub Action (Οδηγός για Οργανισμούς)

**Απευθύνεται σε:** Αυτός ο οδηγός προορίζεται για **εσωτερικούς χρήστες της Microsoft** ή **ομάδες που έχουν πρόσβαση στα απαραίτητα διαπιστευτήρια για την προεγκατεστημένη εφαρμογή Co-op Translator GitHub App** ή μπορούν να δημιουργήσουν τη δική τους προσαρμοσμένη GitHub App.

Αυτοματοποιήστε τη μετάφραση της τεκμηρίωσης του αποθετηρίου σας εύκολα με το Co-op Translator GitHub Action. Αυτός ο οδηγός σας καθοδηγεί στη ρύθμιση της ενέργειας ώστε να δημιουργεί αυτόματα pull requests με ενημερωμένες μεταφράσεις κάθε φορά που αλλάζουν τα αρχεία Markdown ή οι εικόνες πηγής σας.

> [!IMPORTANT]
> 
> **Επιλογή του σωστού οδηγού:**
>
> Αυτός ο οδηγός περιγράφει τη ρύθμιση χρησιμοποιώντας **GitHub App ID και Private Key**. Συνήθως χρειάζεστε αυτή τη μέθοδο "Οδηγός για Οργανισμούς" αν: **`GITHUB_TOKEN` Περιορισμένα Δικαιώματα:** Οι ρυθμίσεις του οργανισμού ή του αποθετηρίου σας περιορίζουν τα προεπιλεγμένα δικαιώματα που παρέχονται στο τυπικό `GITHUB_TOKEN`. Συγκεκριμένα, αν το `GITHUB_TOKEN` δεν επιτρέπεται να έχει τα απαραίτητα δικαιώματα `write` (όπως `contents: write` ή `pull-requests: write`), το workflow στον [Δημόσιο Οδηγό Ρύθμισης](./github-actions-guide-public.md) θα αποτύχει λόγω ανεπαρκών δικαιωμάτων. Η χρήση μιας ειδικής GitHub App με ρητά παραχωρημένα δικαιώματα παρακάμπτει αυτόν τον περιορισμό.
>
> **Αν τα παραπάνω δεν ισχύουν για εσάς:**
>
> Αν το τυπικό `GITHUB_TOKEN` έχει επαρκή δικαιώματα στο αποθετήριό σας (δηλαδή δεν εμποδίζεστε από περιορισμούς του οργανισμού), παρακαλούμε χρησιμοποιήστε τον **[Δημόσιο Οδηγό Ρύθμισης με χρήση GITHUB_TOKEN](./github-actions-guide-public.md)**. Ο δημόσιος οδηγός δεν απαιτεί απόκτηση ή διαχείριση App IDs ή Private Keys και βασίζεται μόνο στο τυπικό `GITHUB_TOKEN` και τα δικαιώματα του αποθετηρίου.

## Προαπαιτούμενα

Πριν ρυθμίσετε το GitHub Action, βεβαιωθείτε ότι έχετε έτοιμα τα απαραίτητα διαπιστευτήρια για την υπηρεσία AI.

**1. Απαραίτητα: Διαπιστευτήρια AI Language Model**
Χρειάζεστε διαπιστευτήρια για τουλάχιστον ένα υποστηριζόμενο Language Model:

- **Azure OpenAI**: Απαιτεί Endpoint, API Key, Model/Deployment Names, API Version.
- **OpenAI**: Απαιτεί API Key, (Προαιρετικά: Org ID, Base URL, Model ID).
- Δείτε [Υποστηριζόμενα Μοντέλα και Υπηρεσίες](../../../../README.md) για λεπτομέρειες.
- Οδηγός Ρύθμισης: [Ρύθμιση Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Προαιρετικά: Διαπιστευτήρια Computer Vision (για Μετάφραση Εικόνων)**

- Απαιτούνται μόνο αν θέλετε να μεταφράσετε κείμενο μέσα σε εικόνες.
- **Azure Computer Vision**: Απαιτεί Endpoint και Subscription Key.
- Αν δεν δοθούν, η ενέργεια λειτουργεί σε [λειτουργία μόνο Markdown](../markdown-only-mode.md).
- Οδηγός Ρύθμισης: [Ρύθμιση Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Ρύθμιση και Διαμόρφωση

Ακολουθήστε τα παρακάτω βήματα για να ρυθμίσετε το Co-op Translator GitHub Action στο αποθετήριό σας:

### Βήμα 1: Εγκατάσταση και Ρύθμιση Επαλήθευσης GitHub App

Το workflow χρησιμοποιεί επαλήθευση GitHub App για να αλληλεπιδρά με ασφάλεια με το αποθετήριό σας (π.χ. δημιουργία pull requests) εκ μέρους σας. Επιλέξτε μία επιλογή:

#### **Επιλογή Α: Εγκατάσταση της Προεγκατεστημένης Co-op Translator GitHub App (για Εσωτερική Χρήση Microsoft)**

1. Μεταβείτε στη σελίδα [Co-op Translator GitHub App](https://github.com/apps/co-op-translator).

1. Επιλέξτε **Install** και διαλέξτε τον λογαριασμό ή τον οργανισμό όπου βρίσκεται το αποθετήριό σας.

    ![Εγκατάσταση εφαρμογής](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.el.png)

1. Επιλέξτε **Only select repositories** και διαλέξτε το αποθετήριό σας (π.χ. `PhiCookBook`). Κάντε κλικ στο **Install**. Ίσως σας ζητηθεί να επαληθεύσετε την ταυτότητά σας.

    ![Εξουσιοδότηση εγκατάστασης](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.el.png)

1. **Λήψη Διαπιστευτηρίων App (Απαιτείται Εσωτερική Διαδικασία):** Για να επιτρέψετε στο workflow να επαληθευτεί ως η εφαρμογή, χρειάζεστε δύο στοιχεία που παρέχονται από την ομάδα Co-op Translator:
  - **App ID:** Ο μοναδικός αναγνωριστικός αριθμός της εφαρμογής Co-op Translator. Το App ID είναι: `1164076`.
  - **Private Key:** Πρέπει να λάβετε το **πλήρες περιεχόμενο** του αρχείου private key `.pem` από τον υπεύθυνο επικοινωνίας. **Χειριστείτε αυτό το κλειδί όπως έναν κωδικό πρόσβασης και διατηρήστε το ασφαλές.**

1. Συνεχίστε στο Βήμα 2.

#### **Επιλογή Β: Χρησιμοποιήστε τη Δική σας Προσαρμοσμένη GitHub App**

- Αν προτιμάτε, μπορείτε να δημιουργήσετε και να ρυθμίσετε τη δική σας GitHub App. Βεβαιωθείτε ότι έχει Read & write πρόσβαση σε Contents και Pull requests. Θα χρειαστείτε το App ID και ένα παραγόμενο Private Key.

### Βήμα 2: Ρύθμιση Μυστικών του Αποθετηρίου

Πρέπει να προσθέσετε τα διαπιστευτήρια της GitHub App και της υπηρεσίας AI ως κρυπτογραφημένα secrets στις ρυθμίσεις του αποθετηρίου σας.

1. Μεταβείτε στο αποθετήριο στόχο στο GitHub (π.χ. `PhiCookBook`).

1. Πηγαίνετε στις **Settings** > **Secrets and variables** > **Actions**.

1. Κάτω από **Repository secrets**, κάντε κλικ στο **New repository secret** για κάθε secret που αναφέρεται παρακάτω.

   ![Επιλογή ρυθμίσεων actions](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.el.png)

**Απαραίτητα Secrets (για Επαλήθευση GitHub App):**

| Όνομα Secret         | Περιγραφή                                         | Πηγή Τιμής                                        |
| :------------------- | :----------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | Το App ID της GitHub App (από το Βήμα 1).        | Ρυθμίσεις GitHub App                             |
| `GH_APP_PRIVATE_KEY` | Το **πλήρες περιεχόμενο** του ληφθέντος αρχείου `.pem`. | Αρχείο `.pem` (από το Βήμα 1)                  |

**Secrets Υπηρεσίας AI (Προσθέστε ΟΛΑ όσα ισχύουν με βάση τα Προαπαιτούμενα):**

| Όνομα Secret                        | Περιγραφή                                 | Πηγή Τιμής                        |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Κλειδί για Azure AI Service (Computer Vision)  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint για Azure AI Service (Computer Vision) | Azure AI Foundry                     |
| `AZURE_OPENAI_API_KEY`              | Κλειδί για την υπηρεσία Azure OpenAI      | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint για την υπηρεσία Azure OpenAI    | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | Όνομα μοντέλου Azure OpenAI               | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Όνομα ανάπτυξης Azure OpenAI              | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | Έκδοση API για Azure OpenAI               | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | API Key για OpenAI                        | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID                    | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | Συγκεκριμένο OpenAI model ID              | OpenAI Platform                    |
| `OPENAI_BASE_URL`                   | Προσαρμοσμένο OpenAI API Base URL         | OpenAI Platform                    |

![Εισαγωγή ονόματος μεταβλητής περιβάλλοντος](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.el.png)

### Βήμα 3: Δημιουργία του Αρχείου Workflow

Τέλος, δημιουργήστε το αρχείο YAML που ορίζει το αυτοματοποιημένο workflow.

1. Στον ριζικό φάκελο του αποθετηρίου σας, δημιουργήστε τον φάκελο `.github/workflows/` αν δεν υπάρχει ήδη.

1. Μέσα στο `.github/workflows/`, δημιουργήστε ένα αρχείο με όνομα `co-op-translator.yml`.

1. Επικολλήστε το παρακάτω περιεχόμενο στο co-op-translator.yml.

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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

4.  **Εξατομίκευση του Workflow:**
  - **[!IMPORTANT] Γλώσσες Στόχοι:** Στο βήμα `Run Co-op Translator`, **ΠΡΕΠΕΙ να ελέγξετε και να τροποποιήσετε τη λίστα των κωδικών γλωσσών** μέσα στην εντολή `translate -l "..." -y` ώστε να ταιριάζει με τις ανάγκες του έργου σας. Η ενδεικτική λίστα (`ar de es...`) πρέπει να αντικατασταθεί ή να προσαρμοστεί.
  - **Trigger (`on:`):** Η τρέχουσα ρύθμιση ενεργοποιείται σε κάθε push στο `main`. Για μεγάλα αποθετήρια, σκεφτείτε να προσθέσετε ένα φίλτρο `paths:` (δείτε το σχολιασμένο παράδειγμα στο YAML) ώστε το workflow να τρέχει μόνο όταν αλλάζουν σχετικά αρχεία (π.χ. τεκμηρίωση πηγής), εξοικονομώντας χρόνο εκτέλεσης.
  - **Λεπτομέρειες PR:** Εξατομικεύστε το `commit-message`, `title`, `body`, το όνομα του `branch` και τα `labels` στο βήμα `Create Pull Request` αν χρειάζεται.

## Διαχείριση και Ανανέωση Διαπιστευτηρίων

- **Ασφάλεια:** Αποθηκεύετε πάντα ευαίσθητα διαπιστευτήρια (API keys, private keys) ως secrets του GitHub Actions. Μην τα εκθέτετε ποτέ στο αρχείο workflow ή στον κώδικα του αποθετηρίου σας.
- **[!IMPORTANT] Ανανέωση Κλειδιών (Εσωτερικοί Χρήστες Microsoft):** Έχετε υπόψη ότι το Azure OpenAI key που χρησιμοποιείται εντός Microsoft μπορεί να έχει υποχρεωτική πολιτική ανανέωσης (π.χ. κάθε 5 μήνες). Βεβαιωθείτε ότι ενημερώνετε τα αντίστοιχα secrets του GitHub (`AZURE_OPENAI_...` keys) **πριν λήξουν** για να αποφύγετε αποτυχίες του workflow.

## Εκτέλεση του Workflow

> [!WARNING]  
> **Χρονικό Όριο Εκτέλεσης GitHub-hosted Runner:**  
> Τα GitHub-hosted runners όπως το `ubuntu-latest` έχουν **μέγιστο χρονικό όριο εκτέλεσης 6 ωρών**.  
> Για μεγάλα αποθετήρια τεκμηρίωσης, αν η διαδικασία μετάφρασης ξεπεράσει τις 6 ώρες, το workflow θα τερματιστεί αυτόματα.  
> Για να το αποφύγετε, σκεφτείτε:  
> - Να χρησιμοποιήσετε **self-hosted runner** (χωρίς χρονικό όριο)  
> - Να μειώσετε τον αριθμό των γλωσσών στόχων ανά εκτέλεση

Μόλις το αρχείο `co-op-translator.yml` συγχωνευτεί στο κύριο branch σας (ή στο branch που ορίζεται στο trigger `on:`), το workflow θα εκτελείται αυτόματα κάθε φορά που γίνονται αλλαγές σε αυτό το branch (και ταιριάζουν με το φίλτρο `paths`, αν έχει ρυθμιστεί).

Αν παραχθούν ή ενημερωθούν μεταφράσεις, η ενέργεια θα δημιουργήσει αυτόματα ένα Pull Request με τις αλλαγές, έτοιμο για έλεγχο και συγχώνευση.

---

**Αποποίηση Ευθύνης**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρότι καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.