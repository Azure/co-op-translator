<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T05:01:18+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "lt"
}
-->
# Co-op Translator GitHub Action naudojimas (organizacijos vadovas)

**Tikslinė auditorija:** Šis vadovas skirtas **Microsoft vidiniams naudotojams** arba **komandoms, turinčioms prieigą prie iš anksto paruoštos Co-op Translator GitHub programėlės kredencialų** arba galinčioms susikurti savo GitHub programėlę.

Automatiškai išverskite savo repozitorijos dokumentaciją naudodami Co-op Translator GitHub Action. Šiame vadove rasite instrukcijas, kaip sukonfigūruoti veiksmą, kad automatiškai būtų kuriami pull request'ai su atnaujintais vertimais, kai tik pasikeičia jūsų Markdown failai ar paveikslėliai.

> [!IMPORTANT]
> 
> **Pasirinkite tinkamą vadovą:**
>
> Šiame vadove aprašyta konfigūracija naudojant **GitHub App ID ir privatų raktą**. Šis „organizacijos vadovo“ metodas paprastai reikalingas, jei: **`GITHUB_TOKEN` leidimai yra apriboti:** Jūsų organizacijos ar repozitorijos nustatymai riboja standartinio `GITHUB_TOKEN` suteikiamus leidimus. Jei `GITHUB_TOKEN` neturi reikiamų `write` leidimų (pvz., `contents: write` ar `pull-requests: write`), [viešojo vadovo](./github-actions-guide-public.md) darbo eiga nepavyks dėl nepakankamų leidimų. Naudojant specialią GitHub programėlę su aiškiai suteiktais leidimais, šis apribojimas apeinamas.
>
> **Jei aukščiau aprašyta situacija jums netaikoma:**
>
> Jei standartinis `GITHUB_TOKEN` turi pakankamai leidimų jūsų repozitorijoje (t. y. jūsų neblokuoja organizaciniai apribojimai), naudokite **[viešąjį vadovą su GITHUB_TOKEN](./github-actions-guide-public.md)**. Viešajam vadovui nereikia gauti ar valdyti App ID ar privačių raktų – pakanka standartinio `GITHUB_TOKEN` ir repozitorijos leidimų.

## Prieš pradedant

Prieš konfigūruodami GitHub Action, įsitikinkite, kad turite reikiamus AI paslaugų kredencialus.

**1. Privaloma: AI kalbos modelio kredencialai**
Reikalingi bent vienos palaikomos kalbos modelio kredencialai:

- **Azure OpenAI**: Reikalingas Endpoint, API Key, Model/Deployment pavadinimai, API versija.
- **OpenAI**: Reikalingas API Key, (pasirinktinai: Org ID, Base URL, Model ID).
- Daugiau informacijos rasite [Palaikomi modeliai ir paslaugos](../../../../README.md).
- Konfigūravimo vadovas: [Azure OpenAI konfigūravimas](../set-up-resources/set-up-azure-openai.md).

**2. Pasirinktinai: Kompiuterinės regos kredencialai (vaizdų vertimui)**

- Reikalinga tik jei norite versti tekstą paveikslėliuose.
- **Azure Computer Vision**: Reikalingas Endpoint ir Subscription Key.
- Jei nepateiksite, veiksmas veiks [tik su Markdown](../markdown-only-mode.md).
- Konfigūravimo vadovas: [Azure Computer Vision konfigūravimas](../set-up-resources/set-up-azure-computer-vision.md).

## Konfigūravimas

Vadovaukitės šiais žingsniais, kad sukonfigūruotumėte Co-op Translator GitHub Action savo repozitorijoje:

### 1 žingsnis: Įdiekite ir sukonfigūruokite GitHub App autentifikaciją

Darbo eiga naudoja GitHub App autentifikaciją, kad saugiai galėtų veikti jūsų repozitorijoje (pvz., kurti pull request'us) jūsų vardu. Pasirinkite vieną variantą:

#### **A variantas: Įdiekite iš anksto paruoštą Co-op Translator GitHub programėlę (Microsoft vidiniam naudojimui)**

1. Eikite į [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) puslapį.

1. Pasirinkite **Install** ir pasirinkite paskyrą ar organizaciją, kurioje yra jūsų repozitorija.

    ![Install app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.lt.png)

1. Pasirinkite **Only select repositories** ir pažymėkite savo repozitoriją (pvz., `PhiCookBook`). Spauskite **Install**. Gali tekti patvirtinti tapatybę.

    ![Install authorize](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.lt.png)

1. **Gaukite programėlės kredencialus (vidinis procesas):** Kad darbo eiga galėtų autentifikuotis kaip programėlė, jums reikės dviejų duomenų, kuriuos suteikia Co-op Translator komanda:
  - **App ID:** Unikalus Co-op Translator programėlės identifikatorius. App ID yra: `1164076`.
  - **Privatus raktas:** Turite gauti **visą** `.pem` privataus rakto failo turinį iš atsakingo asmens. **Laikykite šį raktą saugiai, kaip slaptažodį.**

1. Pereikite prie 2 žingsnio.

#### **B variantas: Naudokite savo GitHub programėlę**

- Jei norite, galite susikurti ir sukonfigūruoti savo GitHub programėlę. Įsitikinkite, kad ji turi Read & write prieigą prie Contents ir Pull requests. Jums reikės jos App ID ir sugeneruoto privataus rakto.

### 2 žingsnis: Konfigūruokite repozitorijos paslaptis

Turite pridėti GitHub programėlės kredencialus ir AI paslaugų kredencialus kaip užšifruotas paslaptis repozitorijos nustatymuose.

1. Eikite į savo repozitoriją (pvz., `PhiCookBook`).

1. Eikite į **Settings** > **Secrets and variables** > **Actions**.

1. Skiltyje **Repository secrets** spauskite **New repository secret** kiekvienai žemiau nurodytai paslapčiai.

   ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.lt.png)

**Privalomos paslaptys (GitHub programėlės autentifikacijai):**

| Paslapties pavadinimas | Aprašymas | Vertės šaltinis |
| :------------------- | :----------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | GitHub programėlės App ID (iš 1 žingsnio).      | GitHub App nustatymai                              |
| `GH_APP_PRIVATE_KEY` | **Visas** atsisiųsto `.pem` failo turinys. | `.pem` failas (iš 1 žingsnio)                      |

**AI paslaugų paslaptys (pridėkite visas, kurios taikomos pagal jūsų poreikius):**

| Paslapties pavadinimas | Aprašymas | Vertės šaltinis |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service raktas (Computer Vision)  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service Endpoint (Computer Vision) | Azure AI Foundry                     |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI paslaugos raktas              | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI paslaugos Endpoint            | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI modelio pavadinimas           | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI diegimo pavadinimas           | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API versija                   | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | OpenAI API raktas                          | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | OpenAI organizacijos ID                    | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | Konkretus OpenAI modelio ID                | OpenAI Platform                    |
| `OPENAI_BASE_URL`                   | OpenAI API bazinis URL                     | OpenAI Platform                    |

![Enter environment variable name](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.lt.png)

### 3 žingsnis: Sukurkite darbo eigos failą

Galiausiai sukurkite YAML failą, apibrėžiantį automatizuotą darbo eigą.

1. Repozitorijos šakniniame kataloge sukurkite `.github/workflows/` katalogą, jei jo dar nėra.

1. Kataloge `.github/workflows/` sukurkite failą pavadinimu `co-op-translator.yml`.

1. Įklijuokite žemiau pateiktą turinį į co-op-translator.yml.

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

4.  **Priderinkite darbo eigą:**
  - **[!IMPORTANT] Tikslinės kalbos:** `Run Co-op Translator` žingsnyje **BŪTINAI peržiūrėkite ir pakeiskite kalbų kodų sąrašą** komandoje `translate -l "..." -y`, kad jis atitiktų jūsų projekto poreikius. Pavyzdinis sąrašas (`ar de es...`) turi būti pakeistas arba pakoreguotas.
  - **Trigger (`on:`):** Dabartinis trigger'is veikia kiekvieną kartą, kai įvyksta push į `main`. Didelėms repozitorijoms rekomenduojama pridėti `paths:` filtrą (žr. YAML komentaruose), kad darbo eiga būtų vykdoma tik pasikeitus aktualiems failams (pvz., dokumentacijai), taip taupant runner minutes.
  - **PR informacija:** Jei reikia, pritaikykite `commit-message`, `title`, `body`, `branch` pavadinimą ir `labels` žingsnyje `Create Pull Request`.

## Kredencialų valdymas ir atnaujinimas

- **Saugumas:** Visada saugokite jautrius kredencialus (API raktus, privačius raktus) kaip GitHub Actions paslaptis. Niekada jų neatskleiskite darbo eigos faile ar repozitorijos kode.
- **[!IMPORTANT] Rakto atnaujinimas (Microsoft vidiniams naudotojams):** Atkreipkite dėmesį, kad Azure OpenAI raktas, naudojamas Microsoft viduje, gali turėti privalomą atnaujinimo politiką (pvz., kas 5 mėnesius). Būtinai atnaujinkite atitinkamas GitHub paslaptis (`AZURE_OPENAI_...` raktus) **prieš jiems pasibaigiant**, kad išvengtumėte darbo eigos klaidų.

## Darbo eigos vykdymas

> [!WARNING]  
> **GitHub-hosted Runner laiko limitas:**  
> GitHub-hosted runner'iai, tokie kaip `ubuntu-latest`, turi **maksimalų vykdymo laiką – 6 valandas**.  
> Jei didelės dokumentacijos repozitorijos vertimo procesas užtruks ilgiau nei 6 valandas, darbo eiga bus automatiškai nutraukta.  
> Kad to išvengtumėte, apsvarstykite:  
> - Naudoti **self-hosted runner** (be laiko limito)  
> - Sumažinti tikslinių kalbų skaičių per vieną vykdymą

Kai `co-op-translator.yml` failas bus sujungtas į pagrindinę šaką (ar kitą šaką, nurodytą `on:` trigger'yje), darbo eiga automatiškai bus vykdoma kiekvieną kartą, kai į tą šaką bus įkelti pakeitimai (ir atitiks `paths` filtrą, jei jis sukonfigūruotas).

Jei bus sugeneruoti ar atnaujinti vertimai, veiksmas automatiškai sukurs Pull Request su pakeitimais, paruoštais jūsų peržiūrai ir sujungimui.

---

**Atsakomybės atsisakymas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretaciją, kylančią dėl šio vertimo naudojimo.