<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T03:49:55+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "hu"
}
-->
# A Co-op Translator GitHub Action használata (Szervezeti útmutató)

**Célközönség:** Ez az útmutató **Microsoft belső felhasználóknak** vagy olyan csapatoknak szól, akik hozzáférnek a Co-op Translator előre elkészített GitHub App hitelesítő adataihoz, vagy saját egyedi GitHub Appot tudnak létrehozni.

Automatizáld a dokumentáció fordítását a Co-op Translator GitHub Action segítségével. Ez az útmutató lépésről lépésre bemutatja, hogyan állítsd be az actiont, hogy automatikusan létrehozzon pull requesteket a frissített fordításokkal, amikor a forrás Markdown fájlok vagy képek módosulnak.

> [!IMPORTANT]
> 
> **A megfelelő útmutató kiválasztása:**
>
> Ez az útmutató a **GitHub App ID és Private Key** használatát mutatja be. Általában ezt a "Szervezeti útmutató" módszert akkor kell választanod, ha: **`GITHUB_TOKEN` jogosultságok korlátozottak:** A szervezeted vagy a repository beállításai korlátozzák az alapértelmezett `GITHUB_TOKEN` által biztosított jogosultságokat. Ha például a `GITHUB_TOKEN` nem kapja meg a szükséges `write` jogosultságokat (mint a `contents: write` vagy `pull-requests: write`), akkor a [Publikus beállítási útmutatóban](./github-actions-guide-public.md) leírt workflow nem fog működni jogosultság hiánya miatt. Egy dedikált GitHub App használata, amelynek jogosultságai kifejezetten meg vannak adva, megkerüli ezt a korlátozást.
>
> **Ha rád nem vonatkozik a fenti korlátozás:**
>
> Ha a standard `GITHUB_TOKEN` elegendő jogosultsággal rendelkezik a repositorydban (tehát nincs szervezeti korlátozás), akkor használd inkább a **[Publikus beállítási útmutatót GITHUB_TOKEN-nel](./github-actions-guide-public.md)**. A publikus útmutató nem igényel App ID vagy Private Key beszerzését, csak a standard `GITHUB_TOKEN`-t és a repository jogosultságait használja.

## Előfeltételek

Mielőtt beállítanád a GitHub Actiont, győződj meg róla, hogy rendelkezel a szükséges AI szolgáltatás hitelesítő adataival.

**1. Szükséges: AI nyelvi modell hitelesítő adatok**
Legalább egy támogatott nyelvi modellhez szükséged lesz hitelesítő adatokra:

- **Azure OpenAI**: Szükséges Endpoint, API Key, Modell/Deployment nevek, API verzió.
- **OpenAI**: Szükséges API Key, (Opcionális: Org ID, Base URL, Modell ID).
- Részletek: [Támogatott modellek és szolgáltatások](../../../../README.md).
- Beállítási útmutató: [Azure OpenAI beállítása](../set-up-resources/set-up-azure-openai.md).

**2. Opcionális: Computer Vision hitelesítő adatok (képek fordításához)**

- Csak akkor szükséges, ha képeken lévő szöveget is fordítani szeretnél.
- **Azure Computer Vision**: Szükséges Endpoint és Subscription Key.
- Ha nem adod meg, az action [csak Markdown módban](../markdown-only-mode.md) fut.
- Beállítási útmutató: [Azure Computer Vision beállítása](../set-up-resources/set-up-azure-computer-vision.md).

## Beállítás és konfiguráció

Kövesd az alábbi lépéseket a Co-op Translator GitHub Action beállításához a repositorydban:

### 1. lépés: GitHub App hitelesítés telepítése és konfigurálása

A workflow GitHub App hitelesítést használ, hogy biztonságosan tudjon műveleteket végezni a repositorydban (pl. pull requesteket létrehozni). Válassz egy lehetőséget:

#### **A opció: Előre elkészített Co-op Translator GitHub App telepítése (Microsoft belső használatra)**

1. Nyisd meg a [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) oldalát.

1. Kattints az **Install** gombra, majd válaszd ki azt a fiókot vagy szervezetet, ahol a cél repository található.

    <img src="../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.hu.png" alt="Install app">

1. Válaszd az **Only select repositories** lehetőséget, majd jelöld ki a cél repositoryt (pl. `PhiCookBook`). Kattints az **Install** gombra. Előfordulhat, hogy hitelesítened kell magad.

    <img src="../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.hu.png" alt="Install authorize">

1. **App hitelesítő adatok beszerzése (belső folyamat szükséges):** Ahhoz, hogy a workflow az app nevében tudjon hitelesíteni, két információra lesz szükséged, amit a Co-op Translator csapat biztosít:
  - **App ID:** A Co-op Translator app egyedi azonosítója. Az App ID: `1164076`.
  - **Private Key:** Meg kell szerezned a `.pem` privát kulcsfájl **teljes tartalmát** a karbantartótól. **Ezt a kulcsot kezeld jelszóként, és tartsd biztonságban!**

1. Folytasd a 2. lépéssel.

#### **B opció: Saját egyedi GitHub App használata**

- Ha szeretnéd, létrehozhatsz és konfigurálhatsz saját GitHub Appot is. Biztosítsd, hogy olvasási és írási jogosultsága legyen a Contents és Pull requests-hez. Szükséged lesz az App ID-ra és a generált Private Key-re.

### 2. lépés: Repository titkos adatok konfigurálása

A GitHub App hitelesítő adatokat és az AI szolgáltatás hitelesítő adatokat titkosított secretsként kell hozzáadnod a repository beállításaihoz.

1. Nyisd meg a cél GitHub repositoryt (pl. `PhiCookBook`).

1. Menj a **Settings** > **Secrets and variables** > **Actions** menüponthoz.

1. A **Repository secrets** alatt kattints a **New repository secret** gombra minden egyes titkos adatnál az alábbiak közül.

   <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.hu.png" alt="Select setting action">

**Szükséges titkos adatok (GitHub App hitelesítéshez):**

| Secret Name          | Leírás                                      | Forrás                                     |
| :------------------- | :------------------------------------------ | :------------------------------------------ |
| `GH_APP_ID`          | A GitHub App azonosítója (1. lépésből).     | GitHub App beállítások                      |
| `GH_APP_PRIVATE_KEY` | A letöltött `.pem` fájl **teljes tartalma** | `.pem` fájl (1. lépésből)                   |

**AI szolgáltatás titkos adatok (Add meg az összeset, ami releváns):**

| Secret Name                         | Leírás                               | Forrás                     |
| :---------------------------------- | :----------------------------------- | :------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service kulcs (Computer Vision)  | Azure AI Foundry           |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service endpoint (Computer Vision) | Azure AI Foundry           |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI szolgáltatás kulcsa      | Azure AI Foundry           |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI szolgáltatás endpointja  | Azure AI Foundry           |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI modell neve              | Azure AI Foundry           |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI deployment neve          | Azure AI Foundry           |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API verziója             | Azure AI Foundry           |
| `OPENAI_API_KEY`                    | OpenAI API kulcs                      | OpenAI Platform            |
| `OPENAI_ORG_ID`                     | OpenAI szervezet azonosítója          | OpenAI Platform            |
| `OPENAI_CHAT_MODEL_ID`              | OpenAI modell azonosítója             | OpenAI Platform            |
| `OPENAI_BASE_URL`                   | Egyedi OpenAI API Base URL            | OpenAI Platform            |

<img src="../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.hu.png" alt="Enter environment variable name">

### 3. lépés: Workflow fájl létrehozása

Végül hozd létre a YAML fájlt, amely definiálja az automatizált workflow-t.

1. A repository gyökérkönyvtárában hozd létre a `.github/workflows/` könyvtárat, ha még nem létezik.

1. A `.github/workflows/` mappában hozz létre egy `co-op-translator.yml` nevű fájlt.

1. Illeszd be az alábbi tartalmat a co-op-translator.yml fájlba.

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

4.  **Workflow testreszabása:**
  - **[!IMPORTANT] Cél nyelvek:** A `Run Co-op Translator` lépésben **FELTÉTLENÜL ellenőrizd és módosítsd a nyelvi kódok listáját** a `translate -l "..." -y` parancsban, hogy megfeleljen a projekted igényeinek. Az itt szereplő példa (`ar de es...`) csak minta, cseréld le vagy egészítsd ki.
  - **Trigger (`on:`):** Jelenleg minden `main` branchre történő push esetén fut le. Nagy repositoryknál érdemes `paths:` szűrőt beállítani (lásd a YAML-ban a kommentelt példát), hogy csak releváns fájlok (pl. forrás dokumentáció) módosításakor fusson, így spórolhatsz a runner percekkel.
  - **PR részletek:** Szükség esetén testreszabhatod a `commit-message`, `title`, `body`, `branch` nevét és a `labels`-t a `Create Pull Request` lépésben.

## Hitelesítő adatok kezelése és megújítása

- **Biztonság:** Az érzékeny hitelesítő adatokat (API kulcsok, privát kulcsok) mindig GitHub Actions titkos adatként tárold. Soha ne tedd ki őket a workflow fájlban vagy a repository kódban.
- **[!IMPORTANT] Kulcs megújítás (Microsoft belső felhasználók):** Az Azure OpenAI kulcsot a Microsofton belül előfordulhat, hogy kötelezően meg kell újítani (pl. 5 havonta). Frissítsd a megfelelő GitHub titkos adatokat (`AZURE_OPENAI_...` kulcsok) **lejárat előtt**, hogy elkerüld a workflow hibákat.

## A workflow futtatása

> [!WARNING]  
> **GitHub-hosted Runner időkorlát:**  
> A GitHub által biztosított futtatók, mint az `ubuntu-latest`, **maximum 6 óráig** futtathatók.  
> Nagy dokumentációs repositoryknál, ha a fordítási folyamat 6 óránál tovább tart, a workflow automatikusan megszakad.  
> Ennek elkerülésére:  
> - Használj **saját futtatót** (nincs időkorlát)  
> - Csökkentsd a futtatott nyelvek számát egy-egy futásnál

Ha a `co-op-translator.yml` fájlt beolvasztod a main branchbe (vagy abba a branchbe, amit a `on:` triggerben megadtál), a workflow automatikusan lefut, amikor változásokat pusholsz abba a branchbe (és megfelel a `paths` szűrőnek, ha beállítottad).

Ha új vagy frissített fordítások készülnek, az action automatikusan létrehoz egy Pull Requestet a változtatásokkal, amit át tudsz nézni és be tudsz olvasztani.

---

**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.