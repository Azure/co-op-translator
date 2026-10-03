# GitHub Actions

Használjon GitHub Actions-t, ha szeretné, hogy egy tároló automatikusan lefordítsa a megváltozott dokumentációt, és létrehozzon egy pull requestet a generált eredményekkel.

Kezdje az alapértelmezett `GITHUB_TOKEN` beállítással, beleértve az olyan szervezeti adattárakat is, ahol a házirend engedélyezi azt. Lásd a [GitHub App beállítása](#github-app-setup)-t, ha a szervezet App-azonosságot követel meg, vagy automatikus downstream munkafolyamat-futtatásokra van szükség.

**Emberi szerkesztések:** ezek a munkafolyamatok teljes egészében újrafordítják a megváltozott forrásfájlokat, és felülírhatják a fordításaikban végrehajtott megfogalmazás-módosításokat. Minden PR-t ellenőrizzen összeolvadás előtt. Az elfogadott módosítások Markdown blokk-szintű megőrzése egyedi integrációt igényel a [Python API fordítási állapot-szolgáltató](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)-val.

## Az első README fordítási PR

Kezdje egy gyökér `README.md` fájllal és egy célnyelvvel. Ez a munkafolyamat csak Markdown-t fordít, így az Azure AI Vision nem szükséges.

1. Másolja a [translate-readme.yml](../../assets/workflows/translate-readme.yml) fájlt ([sablon megtekintése a GitHub-on](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) a `.github/workflows/translate-readme.yml` helyre abba a tárolóba, amelyet le szeretne fordítani, és commitolja azt a tároló alapértelmezett ágába. A sablon a gyökér Action-t használja az `Azure/co-op-translator@main`-ből, amely ugyanarról a forrás-ref-ről telepíti a CLI-t. A reprodukálható futtatásokhoz rögzítsen egy ellenőrzött commitot.
2. Nyissa meg az **Actions > Translate README > Run workflow** menüpontot, válasszon nyelvet, és hagyja bejelölve a **Preview only** opciót. Ellenőrizze a tokenbecslést az előnézet lépésben. Az előnézet nem hív modell-szolgáltatókat, nem ír fordításokat, és nem hoz létre PR-t.
3. Adja hozzá egy [szöveg szolgáltató](#prerequisites) titkait, és engedélyezze az **Engedélyezze, hogy a GitHub Actions létrehozhasson és jóváhagyhasson pull requesteket** opciót a **Beállítások > Műveletek > Általános** alatt. A sablon kéri a `contents: write` és `pull-requests: write` jogosultságokat a feladatához; nem szükséges megváltoztatni az alapértelmezett jogosultságokat minden munkafolyamathoz. Ha a szervezeti házirend blokkolja ezeket a jogosultságokat vagy ezt a beállítást, kérdezze meg az adminisztrátort egy jóváhagyott [GitHub-alkalmazás](#github-app-setup) ügyében.
4. Futtassa újra a munkafolyamatot úgy, hogy a **Preview only** nincs bejelölve. Ez előnézetet készít, lefordít, lefuttatja a `co-op-review --readme-only` parancsot, és csak akkor hozza létre vagy frissíti a fordítási PR-t, ha a fordítás és az ellenőrzés sikeres. A munkafolyamat összefoglalója linket ad a PR-hez.
5. Ellenőrizze a PR-ben a megfogalmazást és a fájlváltozásokat, majd egyesítse, ha készen áll. A munkafolyamat nem egyesít automatikusan.

A PR csak a `translations/<language>/README.md` fájlt és annak nyelvi metadatafájlját tartalmazza. A forrás README változatlan marad, és a kapcsolódó dokumentumokra mutató linkek továbbra is a forrásdokumentumokra mutatnak. A PR szövege felsorolja a megváltozott fájlokat és a strukturális ellenőrzés eredményeit. Ha a fordítás vagy az ellenőrzés meghiúsul, vizsgálja meg a munkafolyamat összefoglalóját és a sikertelen lépés naplóit; PR nem jön létre. Ha nincs változás, nincs szükség új PR-re.

**Szervezeti és CI megjegyzés:** A GitHub App opcionális, nem követelmény a szervezeti tulajdonhoz. A `GITHUB_TOKEN` használatával a pull-request munkafolyamatok PR megnyitásához, frissítéséhez vagy újbóli megnyitásához olyan felhasználót igényelnek, akinek írási jogosultsága van az **Approve workflows to run** kiválasztásához. A push munkafolyamatokat ez a token nem indítja el. Az felügyelet nélküli downstream CI-hez lásd a [GitHub App beállítása](#github-app-setup) részt és a GitHub [munkafolyamat-indítási szabályait](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Előfeltételek

A munkafolyamat létrehozása előtt konfigurálja azokat az AI szolgáltatás titkokat, amelyekre a fordítási futtatásának szüksége lesz.

A szövegfordításhoz egy nyelvi modell szolgáltató szükséges:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

A képfordításhoz emellett szükség van az Azure AI Vision-re:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Lásd a [Konfiguráció](configuration.md) és az [Azure AI beállítása](azure-ai-setup.md) részeket a helyi konfiguráció részleteiért.

## Alapértelmezett beállítás

Miután kipróbálta a README munkafolyamatot, használja ezt a beállítást egy tároló Markdown fájljainak több nyelvre történő lefordításához. A PR megnyitása előtt lefuttat egy Markdown-ellenőrzést, és nem igényli az Azure AI Vision-t.

### 1. lépés: A tároló titkainak hozzáadása

A cél tárolóban nyissa meg a **Settings** > **Secrets and variables** > **Actions** részt, majd adja hozzá azokat a szolgáltatói titkokat, amelyeket a munkafolyamata használni fog.

![Actions titkok kiválasztása](../../assets/github-actions/select-setting-action.png)

### 2. lépés: A munkafolyamat jogosultságainak engedélyezése

Nyissa meg a **Settings** > **Actions** > **General** részt.

A **Workflow permissions** alatt:

1. Kapcsolja be a **Engedélyezze, hogy a GitHub Actions létrehozhasson és jóváhagyhasson pull requesteket** opciót.
2. Mentse a beállítást.

Az alábbi feladat kifejezetten kéri a `contents: write` és `pull-requests: write` jogosultságokat. Hagyja változatlanul a tároló alapértelmezett munkafolyamat-jogosultságait. Ha a szervezeti házirend blokkolja a PR létrehozását, kérdezze meg az adminisztrátort egy jóváhagyott [GitHub-alkalmazás](#github-app-setup) ügyében.

### 3. lépés: Adja hozzá a munkafolyamatot

Hozza létre a `.github/workflows/co-op-translator.yml` fájlt:

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

Állítsa be a `TARGET_LANGUAGES` értékét a projektjéhez szükséges nyelvekre. Az ellenőrzés a Python API-t használja, és csak a Markdown-t vizsgálja, így illeszkedik a fordítási lépéshez. Egy fordítási vagy ellenőrzési hiba megállítja a feladatot a PR létrehozása előtt. A munkafolyamat nem egyesíti automatikusan a PR-t. Nagy tárolók esetén adjon hozzá egy `paths:` szűrőt az `on.push` alá, hogy a munkafolyamat csak a dokumentáció változásakor fusson.

### Opcionális: notebookok és képek

Jegyzetfüzetekhez adja hozzá a fordítási parancshoz a `-nb` jelzőt, és állítsa a review lépésben a `notebook=True` értéket. Kép szöveg esetén konfigurálja a két [Azure AI Vision titkot](#prerequisites), adja át azokat a fordítási lépés `env`-jében, adja hozzá a parancshoz a `-img` jelzőt, és a PR lépés `add-paths` mezőjéhez vegye fel a `translated_images/` mappát. A lefordított képeket vizuálisan ellenőrizze; a determinisztikus ellenőrzés nem garantálja a képszöveg vagy a nyelvi pontosság helyességét.

## GitHub App beállítása

Használjon jóváhagyott GitHub-alkalmazást, ha a szervezete App-azonosságot követel meg, vagy ha a generált PR-nek a `GITHUB_TOKEN` jóváhagyási lépése nélküli downstream CI-t kell kiváltania. Egy App nem kerüli meg a szervezeti házirendet; az adminisztrátorok továbbra is szabályozzák annak telepítését és jogosultságait.

### 1. lépés: GitHub-alkalmazás létrehozása vagy telepítése

Használjon meglévő, szervezet által biztosított App-ot, ha elérhető, vagy hozzon létre egyet olvasási/írási hozzáféréssel a **Contents** és **Pull requests** engedélyekhez. Telepítse azt a cél tárolóra a szükséges szervezeti jóváhagyással.

Rögzítse:

- App azonosító
- A privát kulcs tartalma

Tárolja őket tárolói titkokként:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### 2. lépés: App token generálása

Adja hozzá ezt a lépést közvetlenül a meglévő pull request lépés elé. A README sablon esetén használja ugyanazt a sikerfeltételt, hogy az előnézetek és a sikertelen fordítások ne kérjenek App tokent:

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

Ezután csak a meglévő pull request lépés `token` bemenetét módosítsa `${{ steps.generate_token.outputs.token }}`-re. Tartsa változatlanul a sikerfeltételét, az ágat, a PR törzsét és az `add-paths` beállítást. A token alapértelmezés szerint az aktuális tárolóra van korlátozva. Amikor a standard beállítást adaptálja a README sablon helyett, hagyja el a fenti `if` feltételt: az a munkafolyamat az alapértelmezett sikerfeltételt használja, így a token létrehozása és a PR létrehozása csak a fordítás és ellenőrzés sikeressége után fut.

Tekintse meg a hivatalos [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) telepítési és token-jogosultsági információiért.

## Runner-korlátok

A GitHub által hosztolt futtatókra maximális munkafutásidő vonatkozik. Nagy tárolók vagy sok célnyelv esetén ez a korlát könnyen túlléphető.

Nagy fordítási terhelések esetén:

- Futtatásonként fordítson kevesebb nyelvet.
- Használjon tartalomjelzőket, például `-md`, `-nb` vagy `-img`.
- Használjon self-hosted futtatót, ha a tároló mérete vagy a modell késleltetése miatt a hosztolt futtatók megbízhatatlanok.

## Ellenőrzés CI-ben

Használja a `co-op-review`-t, amikor egy pull requestnek érvényesítenie kell a generált fordításokat anélkül, hogy LLM- vagy Vision-szolgáltatókat hívna.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

A `co-op-review` egy béta, determinisztikus ellenőrző parancs. Ellenőrzései és kimeneti sémája fejlődhet, de CI-re tervezve biztonságos, mivel nem ír fájlokat és nem hív modell-szolgáltatókat.