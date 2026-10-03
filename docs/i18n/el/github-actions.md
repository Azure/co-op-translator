# GitHub Actions

Χρησιμοποιήστε το GitHub Actions όταν θέλετε ένα αποθετήριο να μεταφράζει αυτόματα την αλλαγμένη τεκμηρίωση και να ανοίγει ένα pull request με τα παραγόμενα αποτελέσματα.

Ξεκινήστε με τη βασική ρύθμιση `GITHUB_TOKEN`, ακόμα και για αποθετήρια οργανώσεων όπου η πολιτική το επιτρέπει. Δείτε [GitHub App Setup](#github-app-setup) όταν η οργάνωσή σας απαιτεί ταυτότητα App ή χρειάζεστε αυτόματες εκτελέσεις downstream workflows.

**Επεξεργασίες από ανθρώπους:** αυτές οι ροές εργασίας επαναμεταφράζουν πλήρως τα τροποποιημένα αρχεία πηγής και μπορούν να αντικαταστήσουν διατυπώσεις που έχουν επεξεργαστεί στις μεταφράσεις τους. Ελέγξτε κάθε PR πριν το συγχωνεύσετε. Η διατήρηση σε επίπεδο μπλοκ του Markdown για αποδεκτές επεξεργασίες απαιτεί προσαρμοσμένη ολοκλήρωση με τον [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Το πρώτο σας PR μετάφρασης του README

Ξεκινήστε με ένα αρχικό `README.md` και μία γλώσσα προορισμού. Αυτή η ροή εργασίας μεταφράζει μόνο Markdown, οπότε το Azure AI Vision δεν απαιτείται.

1. Αντιγράψτε το [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([δείτε το πρότυπο στο GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) στο `.github/workflows/translate-readme.yml` στο αποθετήριο που θέλετε να μεταφράσετε, και κάντε commit στο προεπιλεγμένο branch του αποθετηρίου. Το πρότυπο χρησιμοποιεί το root Action `Azure/co-op-translator@main`, το οποίο εγκαθιστά το CLI από την ίδια αναφορά πηγής. Κλειδώστε (pin) ένα ελεγμένο commit για αναπαραγώγιμες εκτελέσεις.
2. Ανοίξτε το **Actions > Translate README > Run workflow**, επιλέξτε μια γλώσσα και αφήστε το **Preview only** επιλεγμένο. Ελέγξτε την εκτίμηση tokens στο βήμα προεπισκόπησης. Η προεπισκόπηση δεν καλεί παρόχους μοντέλων, δεν γράφει μεταφράσεις και δεν δημιουργεί ένα PR.
3. Προσθέστε τα μυστικά για έναν [πάροχο κειμένου](#prerequisites), και ενεργοποιήστε το **Επιτρέψτε στο GitHub Actions να δημιουργεί και να εγκρίνει pull requests** κάτω από **Ρυθμίσεις > Actions > Γενικά**. Το πρότυπο ζητά `contents: write` και `pull-requests: write` για τη δουλειά του· δεν χρειάζεται να αλλάξετε τα προεπιλεγμένα δικαιώματα για κάθε workflow. Εάν η πολιτική της οργάνωσης μπλοκάρει αυτά τα δικαιώματα ή αυτή τη ρύθμιση, ρωτήστε έναν διαχειριστή για ένα εγκεκριμένο [GitHub App](#github-app-setup).
4. Εκτελέστε ξανά τη ροή εργασίας με το **Preview only** αποεπιλεγμένο. Κάνει προεπισκόπηση, μεταφράζει, τρέχει `co-op-review --readme-only`, και δημιουργεί ή ενημερώνει ένα PR μόνο αφού η μετάφραση και η αναθεώρηση ολοκληρωθούν με επιτυχία. Η περίληψη της ροής εργασίας συνδέεται με το PR.
5. Ελέγξτε τη διατύπωση και τις αλλαγές στα αρχεία στο PR, και στη συνέχεια συγχωνεύστε όταν είστε έτοιμοι. Η ροή εργασίας δεν συγχωνεύει αυτόματα.

Το PR περιέχει μόνο το `translations/<language>/README.md` και το αρχείο μεταδεδομένων γλώσσας του. Το αρχικό README παραμένει αμετάβλητο, και οι σύνδεσμοι σε άλλα έγγραφα εξακολουθούν να δείχνουν τα πρωτότυπα έγγραφα. Το σώμα του PR απαριθμεί τα αλλαγμένα αρχεία και τα αποτελέσματα της δομικής αναθεώρησης. Εάν η μετάφραση ή η αναθεώρηση αποτύχει, ελέγξτε την περίληψη της ροής εργασίας και τα logs του βήματος που απέτυχε· δεν δημιουργείται PR. Εάν δεν υπάρχουν αλλαγές, δεν απαιτείται νέο PR.

**Σημείωση για οργανώσεις και CI:** Ένα GitHub App είναι προαιρετικό, όχι απαίτηση ιδιοκτησίας οργανισμού. Με το `GITHUB_TOKEN`, οι ροές εργασίας pull request για άνοιγμα, ενημέρωση ή επαναφορά PR απαιτούν έναν χρήστη με δικαιώματα εγγραφής να επιλέξει **Approve workflows to run**. Οι push workflows δεν ενεργοποιούνται από αυτό το token. Για μη επανδρωμένο downstream CI, δείτε το [GitHub App Setup](#github-app-setup) και τους [κανόνες ενεργοποίησης ροών εργασίας](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) της GitHub.

## Prerequisites

Πριν δημιουργήσετε τη ροή εργασίας, διαμορφώστε τα secrets των υπηρεσιών AI που απαιτεί το τρέξιμο μετάφρασης.

Η μετάφραση κειμένου απαιτεί έναν παροχέα μοντέλου γλώσσας:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Η μετάφραση εικόνων επιπλέον απαιτεί το Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Δείτε [Configuration](configuration.md) και [Azure AI Setup](azure-ai-setup.md) για λεπτομέρειες τοπικής διαμόρφωσης.

## Βασική ρύθμιση

Αφού δοκιμάσετε τη ροή εργασίας για το README, χρησιμοποιήστε αυτή τη ρύθμιση για να μεταφράσετε τα αρχεία Markdown ενός αποθετηρίου σε πολλές γλώσσες. Εκτελεί μια αναθεώρηση Markdown πριν ανοίξει PR και δεν απαιτεί Azure AI Vision.

### Βήμα 1: Προσθήκη μυστικών αποθετηρίου

Στο αποθετήριο-στόχο, ανοίξτε **Settings** > **Secrets and variables** > **Actions**, στη συνέχεια προσθέστε τα provider secrets που θα χρησιμοποιήσει η ροή εργασίας σας.

![Επιλογή secrets για Actions](../../assets/github-actions/select-setting-action.png)

### Βήμα 2: Ενεργοποίηση δικαιωμάτων ροής εργασίας

Ανοίξτε **Settings** > **Actions** > **General**.

Under **Workflow permissions**:

1. Ενεργοποιήστε το **Επιτρέψτε στο GitHub Actions να δημιουργεί και να εγκρίνει pull requests**.
2. Αποθηκεύστε τη ρύθμιση.

Η δουλειά παρακάτω ζητά ρητά `contents: write` και `pull-requests: write`. Κρατήστε τα προεπιλεγμένα δικαιώματα workflow του αποθετηρίου αμετάβλητα. Εάν η πολιτική της οργάνωσης μπλοκάρει τη δημιουργία PR, ρωτήστε έναν διαχειριστή για ένα εγκεκριμένο [GitHub App](#github-app-setup).

### Βήμα 3: Προσθέστε τη ροή εργασίας

Δημιουργήστε το `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

Αλλάξτε το `TARGET_LANGUAGES` στις γλώσσες που χρειάζεται το έργο σας. Η αναθεώρηση χρησιμοποιεί την Python API για να ελέγξει μόνο Markdown, σε αντιστοιχία με το βήμα μετάφρασης. Σφάλμα στη μετάφραση ή στην αναθεώρηση σταματά τη δουλειά πριν τη δημιουργία PR. Η ροή εργασίας δεν συγχωνεύει το PR αυτόματα. Για μεγάλα αποθετήρια, προσθέστε ένα φίλτρο `paths:` κάτω από `on.push` ώστε η ροή εργασίας να τρέχει μόνο όταν αλλάζει η τεκμηρίωση.

### Προαιρετικό: σημειωματάρια και εικόνες

Για notebooks, προσθέστε `-nb` στην εντολή μετάφρασης και ορίστε `notebook=True` στο βήμα αναθεώρησης. Για κείμενο σε εικόνες, διαμορφώστε τα δύο [Azure AI Vision secrets](#prerequisites), περάστε τα στο `env` του βήματος μετάφρασης, προσθέστε `-img` στην εντολή και προσθέστε το `translated_images/` στο `add-paths` του βήματος PR. Ελέγξτε τις μεταφρασμένες εικόνες οπτικά· η ντετερμινιστική αναθεώρηση δεν πιστοποιεί το κείμενο της εικόνας ή τη γλωσσική ακρίβεια.

## Ρύθμιση εφαρμογής GitHub

Χρησιμοποιήστε ένα εγκεκριμένο GitHub App όταν η οργάνωσή σας απαιτεί ταυτότητα App, ή όταν το παραγόμενο PR χρειάζεται να ενεργοποιήσει downstream CI χωρίς το βήμα έγκρισης `GITHUB_TOKEN`. Ένα App δεν παρακάμπτει την πολιτική της οργάνωσης· οι διαχειριστές εξακολουθούν να ελέγχουν την εγκατάσταση και τα δικαιώματά του.

### Βήμα 1: Δημιουργήστε ή Εγκαταστήστε μια εφαρμογή GitHub

Χρησιμοποιήστε ένα υπάρχον App που παρέχεται από την οργάνωση όταν είναι διαθέσιμο, ή δημιουργήστε ένα με δικαιώματα ανάγνωσης/εγγραφής για **Contents** και **Pull requests**. Εγκαταστήστε το στο αποθετήριο-στόχο με οποιαδήποτε απαιτούμενη έγκριση από την οργάνωση.

Record:

- App ID
- Περιεχόμενα ιδιωτικού κλειδιού

Store them as repository secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Βήμα 2: Δημιουργήστε ένα token εφαρμογής

Προσθέστε αυτό το βήμα αμέσως πριν από το υπάρχον βήμα pull request. Για το πρότυπο README, χρησιμοποιήστε την ίδια συνθήκη επιτυχίας ώστε οι προεπισκοπήσεις και οι αποτυχημένες μεταφράσεις να μην ζητούν App token:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

Στη συνέχεια αλλάξτε μόνο την είσοδο `token` του υπάρχοντος βήματος pull request σε `${{ steps.generate_token.outputs.token }}`. Διατηρήστε αμετάβλητες τη συνθήκη επιτυχίας, το branch, το σώμα του PR και τα `add-paths`. Το token έχει προεπιλεγμένα εύρος στο τρέχον αποθετήριο. Όταν προσαρμόζετε τη βασική ρύθμιση αντί για το πρότυπο README, παραλείψτε το `if` παραπάνω: εκείνη η ροή εργασίας χρησιμοποιεί την προεπιλεγμένη συνθήκη επιτυχίας, οπότε η δημιουργία token και η δημιουργία PR εκτελούνται μόνο αφού η μετάφραση και η αναθεώρηση ολοκληρωθούν με επιτυχία.

Δείτε το επίσημο [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) για εγκατάσταση και δικαιώματα token.

## Όρια εκτελεστών

Οι GitHub-hosted runners έχουν μέγιστη διάρκεια εργασίας. Μεγάλα αποθετήρια ή πολλές γλώσσες προορισμού μπορεί να υπερβούν αυτό το όριο.

Για μεγάλους φόρτους μετάφρασης:

- Μεταφράστε λιγότερες γλώσσες ανά εκτέλεση.
- Χρησιμοποιήστε flags περιεχομένου όπως `-md`, `-nb`, ή `-img`.
- Χρησιμοποιήστε έναν self-hosted runner όταν το μέγεθος του αποθετηρίου ή η καθυστέρηση του μοντέλου κάνουν τους hosted runners μη αξιόπιστους.

## Ανασκόπηση στο CI

Χρησιμοποιήστε το `co-op-review` όταν ένα pull request πρέπει να επικυρώσει τις παραχθείσες μεταφράσεις χωρίς να καλεί παρόχους LLM ή Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` είναι μια beta εντολή ντετερμινιστικής αναθεώρησης. Οι έλεγχοι της και το σχήμα εξόδου της μπορεί να εξελιχθούν, αλλά έχει σχεδιαστεί ώστε να είναι ασφαλής για CI επειδή δεν γράφει αρχεία ούτε καλεί παρόχους μοντέλων.