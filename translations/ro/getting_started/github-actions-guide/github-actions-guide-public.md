<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T03:59:01+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "ro"
}
-->
# Utilizarea acțiunii Co-op Translator pe GitHub (Configurare Publică)

**Public țintă:** Acest ghid se adresează utilizatorilor din majoritatea depozitelor publice sau private unde permisiunile standard GitHub Actions sunt suficiente. Folosește `GITHUB_TOKEN` integrat.

Automatizează traducerea documentației din depozitul tău cu ușurință folosind acțiunea Co-op Translator pe GitHub. Acest ghid te ajută să configurezi acțiunea astfel încât să creeze automat pull request-uri cu traduceri actualizate ori de câte ori se modifică fișierele tale Markdown sursă sau imaginile.

> [!IMPORTANT]
>
> **Alegerea ghidului potrivit:**
>
> Acest ghid descrie **configurarea simplă folosind `GITHUB_TOKEN` standard**. Este metoda recomandată pentru majoritatea utilizatorilor, deoarece nu necesită gestionarea unor chei private sensibile pentru aplicații GitHub.
>

## Cerințe preliminare

Înainte de a configura acțiunea GitHub, asigură-te că ai la dispoziție credențialele pentru serviciul AI.

**1. Obligatoriu: Credențiale pentru modelul AI de limbaj**
Ai nevoie de credențiale pentru cel puțin un model de limbaj suportat:

- **Azure OpenAI**: Necesită Endpoint, API Key, Nume Model/Deployment, Versiune API.
- **OpenAI**: Necesită API Key, (Opțional: Org ID, Base URL, Model ID).
- Vezi [Modele și servicii suportate](../../../../README.md) pentru detalii.

**2. Opțional: Credențiale AI Vision (pentru traducerea imaginilor)**

- Necesare doar dacă vrei să traduci text din imagini.
- **Azure AI Vision**: Necesită Endpoint și Subscription Key.
- Dacă nu sunt furnizate, acțiunea va funcționa în [mod doar Markdown](../markdown-only-mode.md).

## Configurare și setare

Urmează pașii de mai jos pentru a configura acțiunea Co-op Translator în depozitul tău folosind `GITHUB_TOKEN` standard.

### Pasul 1: Înțelege autentificarea (folosind `GITHUB_TOKEN`)

Acest workflow folosește `GITHUB_TOKEN` integrat, oferit de GitHub Actions. Acest token acordă automat permisiuni workflow-ului pentru a interacționa cu depozitul tău, conform setărilor din **Pasul 3**.

### Pasul 2: Configurează secretele depozitului

Trebuie doar să adaugi **credențialele serviciului AI** ca secrete criptate în setările depozitului.

1.  Accesează depozitul tău GitHub.
2.  Mergi la **Settings** > **Secrets and variables** > **Actions**.
3.  Sub **Repository secrets**, apasă **New repository secret** pentru fiecare secret AI necesar din lista de mai jos.

    ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ro.png) *(Referință imagine: Arată unde se adaugă secretele)*

**Secrete AI necesare (Adaugă TOATE care se aplică în funcție de cerințele tale):**

| Nume secret                         | Descriere                               | Sursa valorii                     |
| :---------------------------------- | :-------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Cheie pentru Azure AI Service (Computer Vision)  | Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint pentru Azure AI Service (Computer Vision) | Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Cheie pentru serviciul Azure OpenAI              | Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint pentru serviciul Azure OpenAI         | Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Numele modelului Azure OpenAI              | Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Numele deployment-ului Azure OpenAI         | Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Versiunea API pentru Azure OpenAI              | Azure AI Foundry               |
| `OPENAI_API_KEY`                    | Cheie API pentru OpenAI                        | Platforma OpenAI              |
| `OPENAI_ORG_ID`                     | ID organizație OpenAI (Opțional)         | Platforma OpenAI              |
| `OPENAI_CHAT_MODEL_ID`              | ID model OpenAI specific (Opțional)       | Platforma OpenAI              |
| `OPENAI_BASE_URL`                   | URL de bază personalizat pentru API OpenAI (Opțional)     | Platforma OpenAI              |

### Pasul 3: Configurează permisiunile workflow-ului

Acțiunea GitHub are nevoie de permisiuni acordate prin `GITHUB_TOKEN` pentru a face checkout la cod și a crea pull request-uri.

1.  În depozitul tău, mergi la **Settings** > **Actions** > **General**.
2.  Derulează până la secțiunea **Workflow permissions**.
3.  Selectează **Read and write permissions**. Aceasta acordă permisiunile `contents: write` și `pull-requests: write` necesare workflow-ului.
4.  Asigură-te că bifezi **Allow GitHub Actions to create and approve pull requests**.
5.  Apasă **Save**.

![Permission setting](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.ro.png)

### Pasul 4: Creează fișierul workflow

În final, creează fișierul YAML care definește workflow-ul automatizat folosind `GITHUB_TOKEN`.

1.  În directorul rădăcină al depozitului, creează folderul `.github/workflows/` dacă nu există deja.
2.  În `.github/workflows/`, creează fișierul `co-op-translator.yml`.
3.  Copiază conținutul de mai jos în `co-op-translator.yml`.

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
4.  **Personalizează workflow-ul:**
  - **[!IMPORTANT] Limbile țintă:** În pasul `Run Co-op Translator`, **TREBUIE să verifici și să modifici lista codurilor de limbă** din comanda `translate -l "..." -y` pentru a corespunde cerințelor proiectului tău. Lista exemplu (`ar de es...`) trebuie înlocuită sau ajustată.
  - **Trigger (`on:`):** Trigger-ul actual rulează la fiecare push pe `main`. Pentru depozite mari, ia în considerare adăugarea unui filtru `paths:` (vezi exemplul comentat din YAML) pentru a rula workflow-ul doar când se modifică fișiere relevante (ex: documentația sursă), economisind minutele runner-ului.
  - **Detalii PR:** Poți personaliza `commit-message`, `title`, `body`, numele `branch` și `labels` din pasul `Create Pull Request` dacă este necesar.

## Rularea workflow-ului

> [!WARNING]  
> **Limită de timp pentru runner-ul găzduit de GitHub:**  
> Runner-ele găzduite de GitHub, precum `ubuntu-latest`, au o **limită maximă de execuție de 6 ore**.  
> Pentru depozite mari de documentație, dacă procesul de traducere depășește 6 ore, workflow-ul va fi oprit automat.  
> Pentru a evita acest lucru, ia în considerare:  
> - Utilizarea unui **runner self-hosted** (fără limită de timp)  
> - Reducerea numărului de limbi țintă per rulare

După ce fișierul `co-op-translator.yml` este integrat în ramura principală (sau ramura specificată în trigger-ul `on:`), workflow-ul va rula automat ori de câte ori se fac modificări pe acea ramură (și se potrivește cu filtrul `paths`, dacă este configurat).

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.