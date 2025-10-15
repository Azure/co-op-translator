<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T05:02:14+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "et"
}
-->
# Co-op Translator GitHub Actioni kasutamine (Organisatsiooni juhend)

**Sihtgrupp:** See juhend on mõeldud **Microsofti sisekasutajatele** või **meeskondadele, kellel on juurdepääs vajalikele volitustele eelkonfigureeritud Co-op Translator GitHub Appi jaoks** või kes saavad luua omaenda kohandatud GitHub Appi.

Automatiseeri oma repo dokumentatsiooni tõlkimine lihtsalt Co-op Translator GitHub Actioni abil. See juhend aitab sul seadistada actioni nii, et iga kord, kui sinu lähte-Markdown-failid või pildid muutuvad, luuakse automaatselt tõlgetega pull requestid.

> [!IMPORTANT]
> 
> **Õige juhendi valimine:**
>
> See juhend kirjeldab seadistamist **GitHub App ID ja Private Key** abil. Tavaliselt vajad seda "Organisatsiooni juhendi" meetodit, kui: **`GITHUB_TOKEN` õigused on piiratud:** Sinu organisatsiooni või repo seadistused piiravad vaikimisi antud õigusi, mis on seotud tavapärase `GITHUB_TOKEN`-iga. Eriti, kui `GITHUB_TOKEN`-il ei ole vajalikke `write` õigusi (näiteks `contents: write` või `pull-requests: write`), siis [Avaliku juhendi](./github-actions-guide-public.md) workflow ebaõnnestub õiguste puudumise tõttu. Eraldi GitHub Appi kasutamine, millel on selgelt määratud õigused, lahendab selle piirangu.
>
> **Kui eelnev ei kehti sinu kohta:**
>
> Kui tavapärasel `GITHUB_TOKEN`-il on sinu repos piisavad õigused (ehk sind ei piira organisatsiooni reeglid), kasuta **[Avalikku juhendit GITHUB_TOKEN-iga](./github-actions-guide-public.md)**. Avalik juhend ei nõua App ID või Private Key hankimist ega haldamist, vaid tugineb ainult tavapärasele `GITHUB_TOKEN`-ile ja repo õigustele.

## Eeltingimused

Enne GitHub Actioni seadistamist veendu, et sul on vajalikud AI teenuse volitused olemas.

**1. Vajalik: AI keelemudeli volitused**
Sul on vaja volitusi vähemalt ühele toetatud keelemudelile:

- **Azure OpenAI**: Vajab Endpointi, API Keyd, mudeli/deploymenti nimesid, API versiooni.
- **OpenAI**: Vajab API Keyd, (valikuline: Org ID, Base URL, Model ID).
- Vaata [Toetatud mudelid ja teenused](../../../../README.md) detailideks.
- Seadistusjuhend: [Azure OpenAI seadistamine](../set-up-resources/set-up-azure-openai.md).

**2. Valikuline: Computer Vision volitused (piltide tõlkimiseks)**

- Vajalik ainult siis, kui soovid tõlkida pildivahelist teksti.
- **Azure Computer Vision**: Vajab Endpointi ja Subscription Keyd.
- Kui neid ei ole, töötab action [ainult Markdowni režiimis](../markdown-only-mode.md).
- Seadistusjuhend: [Azure Computer Vision seadistamine](../set-up-resources/set-up-azure-computer-vision.md).

## Seadistamine ja konfigureerimine

Järgi neid samme, et seadistada Co-op Translator GitHub Action oma repos:

### Samm 1: GitHub Appi autentimise paigaldamine ja seadistamine

Workflow kasutab GitHub Appi autentimist, et turvaliselt suhelda sinu repoga (nt pull requestide loomiseks) sinu nimel. Vali üks variant:

#### **Variant A: Paigalda eelkonfigureeritud Co-op Translator GitHub App (Microsofti sisekasutajatele)**

1. Mine [Co-op Translator GitHub Appi](https://github.com/apps/co-op-translator) lehele.

1. Vali **Install** ja vali konto või organisatsioon, kus sinu sihtrepo asub.

    <img src="../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.et.png" alt="Install app">

1. Vali **Only select repositories** ja märgi oma sihtrepo (nt `PhiCookBook`). Vajuta **Install**. Võid olla palutud autentida.

    <img src="../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.et.png" alt="Install authorize">

1. **Hangi Appi volitused (vajalik sisemine protsess):** Et workflow saaks autentida appina, vajad kahte infot, mille annab Co-op Translatori tiim:
  - **App ID:** Co-op Translatori appi unikaalne identifikaator. App ID on: `1164076`.
  - **Private Key:** Pead hankima **kogu `.pem` privaatvõtme faili sisu** haldaja kontaktilt. **Hoia seda võtit nagu parooli ja ära jaga seda.**

1. Jätka Sammuga 2.

#### **Variant B: Kasuta omaenda kohandatud GitHub Appi**

- Soovi korral võid luua ja seadistada oma GitHub Appi. Veendu, et sellel oleks lugemis- ja kirjutamisõigus Contentsile ja Pull requestidele. Sul on vaja selle App ID-d ja genereeritud Private Keyd.

### Samm 2: Repo saladuste seadistamine

Pead lisama GitHub Appi volitused ja AI teenuse volitused krüpteeritud saladustena oma repo seadetes.

1. Mine oma sihtrepo (nt `PhiCookBook`) lehele.

1. Vali **Settings** > **Secrets and variables** > **Actions**.

1. **Repository secrets** all vajuta **New repository secret** iga alloleva saladuse jaoks.

   <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.et.png" alt="Select setting action">

**Vajalikud saladused (GitHub Appi autentimiseks):**

| Saladuse nimi        | Kirjeldus                                         | Väärtuse allikas                                 |
| :------------------- | :------------------------------------------------ | :----------------------------------------------- |
| `GH_APP_ID`          | GitHub Appi ID (Samm 1-st).                       | GitHub Appi seaded                              |
| `GH_APP_PRIVATE_KEY` | **Kogu allalaaditud `.pem` faili sisu.**          | `.pem` fail (Samm 1-st)                         |

**AI teenuse saladused (Lisa KÕIK, mis vastavad sinu eeldustele):**

| Saladuse nimi                        | Kirjeldus                                 | Väärtuse allikas                 |
| :----------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`           | Azure AI Service'i võti (Computer Vision) | Azure AI Foundry                 |
| `AZURE_AI_SERVICE_ENDPOINT`          | Azure AI Service'i endpoint (Computer Vision) | Azure AI Foundry             |
| `AZURE_OPENAI_API_KEY`               | Azure OpenAI teenuse võti                 | Azure AI Foundry                 |
| `AZURE_OPENAI_ENDPOINT`              | Azure OpenAI teenuse endpoint             | Azure AI Foundry                 |
| `AZURE_OPENAI_MODEL_NAME`            | Sinu Azure OpenAI mudeli nimi             | Azure AI Foundry                 |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`  | Sinu Azure OpenAI deploymenti nimi        | Azure AI Foundry                 |
| `AZURE_OPENAI_API_VERSION`           | Azure OpenAI API versioon                 | Azure AI Foundry                 |
| `OPENAI_API_KEY`                     | OpenAI API võti                           | OpenAI Platform                  |
| `OPENAI_ORG_ID`                      | OpenAI organisatsiooni ID                  | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`               | Konkreetne OpenAI mudeli ID                | OpenAI Platform                  |
| `OPENAI_BASE_URL`                    | Kohandatud OpenAI API Base URL             | OpenAI Platform                  |

<img src="../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.et.png" alt="Enter environment variable name">

### Samm 3: Workflow faili loomine

Lõpuks loo YAML-fail, mis määrab automaatse workflow.

1. Repo juurkaustas loo `.github/workflows/` kaust, kui seda veel pole.

1. Kausta `.github/workflows/` sees loo fail nimega `co-op-translator.yml`.

1. Kopeeri järgmine sisu faili co-op-translator.yml.

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

4.  **Workflow kohandamine:**
  - **[!IMPORTANT] Sihtkeeled:** `Run Co-op Translator` sammus **PEAD üle vaatama ja muutma keelekoodide loendi** käsus `translate -l "..." -y`, et see vastaks sinu projekti vajadustele. Näidisloend (`ar de es...`) tuleb asendada või kohandada.
  - **Trigger (`on:`):** Praegune trigger käivitub iga pushi korral `main` harule. Suurte repode puhul lisa `paths:` filter (vt YAMLis kommenteeritud näidet), et workflow käivituks ainult siis, kui asjakohased failid (nt lähte-dokumentatsioon) muutuvad, säästes runneri minuteid.
  - **PR detailid:** Soovi korral kohanda `commit-message`, `title`, `body`, `branch` nime ja `labels` väärtusi `Create Pull Request` sammus.

## Volituste haldus ja uuendamine

- **Turvalisus:** Hoia tundlikud volitused (API võtmed, privaatvõtmed) alati GitHub Actionsi saladustena. Ära kunagi lisa neid workflow faili või repo koodi.
- **[!IMPORTANT] Võtmete uuendamine (Microsofti sisekasutajad):** Pane tähele, et Azure OpenAI võti võib Microsofti sees olla kohustusliku uuendamisega (nt iga 5 kuu tagant). Uuenda vastavad GitHubi saladused (`AZURE_OPENAI_...` võtmed) **enne nende aegumist**, et workflow ei katkeks.

## Workflow käivitamine

> [!WARNING]  
> **GitHubi hostitud runneri ajalimiit:**  
> GitHubi hostitud runneritel nagu `ubuntu-latest` on **maksimaalne käitusaeg 6 tundi**.  
> Kui dokumentatsiooni repo on suur ja tõlkimine võtab üle 6 tunni, katkestatakse workflow automaatselt.  
> Selle vältimiseks:  
> - Kasuta **isehostitud runnerit** (ilma ajalimiidita)  
> - Vähenda korraga tõlgitavate sihtkeelte arvu

Kui `co-op-translator.yml` fail on liidetud sinu main harusse (või harusse, mis on määratud `on:` triggeris), käivitub workflow automaatselt iga kord, kui sellele harule tehakse muudatusi (ja vastab `paths` filtrile, kui see on seadistatud).

Kui tõlked on loodud või uuendatud, loob action automaatselt Pull Requesti muudatustega, mis on valmis sinu ülevaatamiseks ja liitmiseks.

---

**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokumenti selle algses keeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgendamise eest.