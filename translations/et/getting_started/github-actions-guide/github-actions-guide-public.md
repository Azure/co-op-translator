<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T05:03:23+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "et"
}
-->
# Co-op Translator GitHub Actioni kasutamine (avalik seadistus)

**Sihtgrupp:** See juhend on mõeldud kasutajatele, kes töötavad enamikes avalikes või privaatsetes repositooriumites, kus piisab GitHub Actionsi tavapärastest õigustest. Kasutatakse sisseehitatud `GITHUB_TOKEN`-it.

Automatiseeri oma repositooriumi dokumentatsiooni tõlkimine mugavalt Co-op Translator GitHub Actioni abil. See juhend aitab seadistada actioni nii, et iga kord, kui sinu lähte Markdown-failid või pildid muutuvad, luuakse automaatselt tõlgitud uuendustega pull request.

> [!IMPORTANT]
>
> **Õige juhendi valimine:**
>
> See juhend kirjeldab **lihtsamat seadistust, mis kasutab standardset `GITHUB_TOKEN`-it**. See on soovitatav enamikule kasutajatele, kuna ei nõua tundlike GitHub App Private Keyde haldamist.
>

## Eeltingimused

Enne GitHub Actioni seadistamist veendu, et sul on vajalikud AI-teenuse mandaadid olemas.

**1. Vajalik: AI keelemudeli mandaadid**
Sul on vaja vähemalt ühe toetatud keelemudeli mandaate:

- **Azure OpenAI**: Vajab Endpointi, API Keyd, mudeli/deploymendi nimesid, API versiooni.
- **OpenAI**: Vajab API Keyd, (valikuline: Org ID, Base URL, Model ID).
- Vaata [Toetatud mudelid ja teenused](../../../../README.md) täpsemalt.

**2. Valikuline: AI Vision mandaadid (piltide tõlkimiseks)**

- Vajalik ainult juhul, kui soovid tõlkida pildivahelist teksti.
- **Azure AI Vision**: Vajab Endpointi ja Subscription Keyd.
- Kui neid ei lisata, töötab action [ainult Markdowni režiimis](../markdown-only-mode.md).

## Seadistamine ja konfigureerimine

Järgi neid samme, et seadistada Co-op Translator GitHub Action oma repositooriumis, kasutades standardset `GITHUB_TOKEN`-it.

### Samm 1: Autentimise mõistmine (`GITHUB_TOKEN` kasutamine)

See workflow kasutab GitHub Actionsi poolt automaatselt loodavat `GITHUB_TOKEN`-it. See token annab workflowle õigused su repositooriumiga töötamiseks vastavalt **Sammus 3** määratud seadistustele.

### Samm 2: Repositooriumi saladuste seadistamine

Sul tuleb lisada ainult oma **AI-teenuse mandaadid** repositooriumi seadetes krüpteeritud saladustena.

1.  Ava oma siht-GitHubi repositoorium.
2.  Mine **Settings** > **Secrets and variables** > **Actions**.
3.  **Repository secrets** all klõpsa iga vajaliku AI-teenuse saladuse jaoks **New repository secret**.

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.et.png" alt="Vali seadistuse action" /> *(Pildiviide: Näitab, kuhu saladusi lisada)*

**Vajalikud AI-teenuse saladused (Lisa KÕIK, mis vastavad su eeldustele):**

| Saladuse nimi                         | Kirjeldus                               | Väärtuse allikas                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service'i võti (Computer Vision)  | Sinu Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service'i endpoint (Computer Vision) | Sinu Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI teenuse võti              | Sinu Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI teenuse endpoint         | Sinu Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Sinu Azure OpenAI mudeli nimi              | Sinu Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Sinu Azure OpenAI deploymendi nimi         | Sinu Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API versioon              | Sinu Azure AI Foundry               |
| `OPENAI_API_KEY`                    | OpenAI API võti                        | Sinu OpenAI platvorm              |
| `OPENAI_ORG_ID`                     | OpenAI organisatsiooni ID (valikuline)         | Sinu OpenAI platvorm              |
| `OPENAI_CHAT_MODEL_ID`              | Konkreetne OpenAI mudeli ID (valikuline)       | Sinu OpenAI platvorm              |
| `OPENAI_BASE_URL`                   | Kohandatud OpenAI API Base URL (valikuline)     | Sinu OpenAI platvorm              |

### Samm 3: Workflow õiguste seadistamine

GitHub Action vajab õigusi, mis antakse `GITHUB_TOKEN` kaudu, et koodi välja võtta ja pull requeste luua.

1.  Oma repositooriumis mine **Settings** > **Actions** > **General**.
2.  Kerige alla **Workflow permissions** sektsioonini.
3.  Vali **Read and write permissions**. See annab `GITHUB_TOKEN`-ile vajalikud `contents: write` ja `pull-requests: write` õigused selle workflow jaoks.
4.  Veendu, et **Allow GitHub Actions to create and approve pull requests** on **märgitud**.
5.  Vali **Save**.

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.et.png" alt="Õiguste seadistus" />

### Samm 4: Workflow faili loomine

Lõpuks loo YAML-fail, mis määratleb automatiseeritud workflow kasutades `GITHUB_TOKEN`-it.

1.  Oma repositooriumi juurkaustas loo vajadusel `.github/workflows/` kataloog.
2.  Kataloogis `.github/workflows/` loo fail nimega `co-op-translator.yml`.
3.  Kopeeri järgmine sisu faili `co-op-translator.yml`.

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
4.  **Kohanda workflowd:**
  - **[!IMPORTANT] Sihtkeeled:** `Run Co-op Translator` sammus pead **kindlasti üle vaatama ja muutma keelekoodide loendi** käsus `translate -l "..." -y`, et see vastaks su projekti vajadustele. Näidisloend (`ar de es...`) tuleb asendada või kohandada.
  - **Trigger (`on:`):** Praegune trigger käivitub iga kord, kui `main` harule tehakse push. Suurte repositooriumite puhul lisa kindlasti `paths:` filter (vt YAMLis kommenteeritud näidet), et workflow käivituks ainult siis, kui asjakohased failid (nt lähte-dokumentatsioon) muutuvad, säästes runneri minuteid.
  - **PR detailid:** Kohanda vajadusel `commit-message`, `title`, `body`, `branch` nime ja `labels` väärtusi `Create Pull Request` sammus.

## Workflow käivitamine

> [!WARNING]  
> **GitHubi hostitud runneri ajapiirang:**  
> GitHubi hostitud runneritel nagu `ubuntu-latest` on **maksimaalne tööaeg 6 tundi**.  
> Kui dokumentatsiooni tõlkimine võtab suure repositooriumi puhul kauem kui 6 tundi, katkestatakse workflow automaatselt.  
> Selle vältimiseks kaalu:  
> - **Isehostitud runneri** kasutamist (piirang puudub)  
> - Sihtkeelte arvu vähendamist ühe jooksu kohta

Kui `co-op-translator.yml` fail on liidetud su põhiharusse (või harusse, mis on määratud `on:` triggeris), käivitub workflow automaatselt iga kord, kui sellele harule tehakse muudatusi (ja vastab vajadusel `paths` filtrile).

---

**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokumenti selle algses keeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või tõlgendamisvigade eest.