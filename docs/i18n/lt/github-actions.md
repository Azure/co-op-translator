# GitHub Actions

Naudokite GitHub Actions, kai norite, kad saugykla automatiškai išverstų pakeistą dokumentaciją ir atidarytų pull request su sugeneruotais rezultatais.

Pradėkite nuo įprasto `GITHUB_TOKEN` nustatymo, įskaitant ir organizacijos saugykloms, kai politika tai leidžia. Žr. [GitHub App nustatymas](#github-app-setup) kai jūsų organizacija reikalauja App tapatybės arba kai reikia automatinių tolimesnių darbo srautų vykdymų.

**Žmogiški redagavimai:** šie darbo srautai pilnai išverčia pakeistus šaltinio failus iš naujo ir gali perrašyti jų vertimuose atliktus žodžius. Peržiūrėkite kiekvieną PR prieš sujungiant. Priimtų redagavimų Markdown blokų lygmens išsaugojimui reikalinga pasirinktinė integracija su [Python API vertimo būsenos teikėju](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Jūsų pirmasis README vertimo PR

Pradėkite nuo vieno šakninio `README.md` ir vienos tikslinės kalbos. Šis darbo srautas verčia tik Markdown, todėl Azure AI Vision nėra reikalingas.

1. Kopijuokite [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([peržiūrėkite šabloną GitHub'e](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) į `.github/workflows/translate-readme.yml` saugykloje, kurią norite versti, ir patvirtinkite tai į tos saugyklos numatytąją šaką. Šablonas naudoja pagrindinį Action `Azure/co-op-translator@main`, kuris įdiegia CLI iš to paties šaltinio ref. Užfiksuokite peržiūrėtą commit'ą reproducuojamiems vykdymams.
2. Atidarykite **Actions > Translate README > Run workflow**, pasirinkite kalbą ir palikite pažymėtą **Preview only**. Peržiūros žingsnyje peržiūrėkite token įvertinimą. Peržiūra nepaleidžia modelių teikėjų, neįrašo vertimų ir nesukuria PR.
3. Pridėkite paslaptis vienam [teksto teikėjui](#prerequisites), ir įjunkite **Leisti GitHub Actions kurti ir patvirtinti pull užklausas** skiltyje **Nustatymai > Veiksmai > Bendrieji**. Šablonas prašo `contents: write` ir `pull-requests: write` savo darbui; jums nereikia keisti numatytųjų leidimų kiekvienam darbo srautui. Jei organizacijos politika blokuoja šiuos leidimus arba šį nustatymą, kreipkitės į administratorių dėl patvirtinto [GitHub App](#github-app-setup).
4. Paleiskite darbo srautą dar kartą, nepažymėję **Preview only**. Jis peržiūri, išverčia, paleidžia `co-op-review --readme-only` ir sukuria arba atnaujina vertimo PR tik po to, kai vertimas ir peržiūra sėkmingai užbaigti. Darbo srauto santrauka pateikia nuorodą į PR.
5. Peržiūrėkite PR žodyną ir failų pakeitimus, tada sujunkite, kai būsite pasiruošę. Darbo srautas nesujungia automatiškai.

PR sudaro tik `translations/<language>/README.md` ir jo kalbos metaduomenų failas. Šaltinio README lieka nepakitęs, o nuorodos į kitus dokumentus toliau nukreipia į šaltinio dokumentus. PR aprašyme nurodyti pakeisti failai ir struktūrinės peržiūros rezultatai. Jei vertimas arba peržiūra nepavyksta, patikrinkite darbo srauto santrauką ir nepavykusių žingsnių žurnalus; PR nėra sukuriamas. Jei pakeitimų nėra, naujo PR nereikia.

**Organizacijos ir CI pastaba:** GitHub App yra neprivalomas, jis nėra organizacijos nuosavybės reikalavimas. Su `GITHUB_TOKEN`, pull-request darbo srautams atidaryti, atnaujinti ar vėl atidaryti PR reikia, kad vartotojas su rašymo teisėmis pasirinktų **Approve workflows to run**. Push tipo darbo srautai nėra suaktyvinami šiuo tokenu. Dėl neprižiūrimo tolimesnio CI žr. [GitHub App nustatymas](#github-app-setup) ir GitHub [darbo srautų suaktyvinimo taisykles](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Prieš pradedant

Prieš kuriant darbo srautą, sukonfigūruokite AI paslaugos paslaptis, kurių reikės vertimo vykdymui.

Teksto vertimui reikalingas vienas kalbos modelių teikėjas:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, taip pat neprivalomi `OPENAI_ORG_ID` ir `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, taip pat neprivalomas `ANTHROPIC_BASE_URL`

Vaizdų vertimui papildomai reikalingas Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Žr. [Konfigūracija](configuration.md) ir [Azure AI nustatymas](azure-ai-setup.md) dėl vietinės konfigūracijos detalių.

## Standartinė sąranka

Išbandę README darbo srautą, naudokite šią sąranką, kad išverstumėte saugyklos Markdown failus į kelias kalbas. Ji atlieka Markdown peržiūrą prieš atidarant PR ir nereikalauja Azure AI Vision.

### 1 žingsnis: Pridėti saugyklos paslaptis

Tikslinėje saugykloje atidarykite **Settings** > **Secrets and variables** > **Actions**, tada pridėkite teikėjo paslaptis, kurias naudos jūsų darbo srautas.

![Pasirinkite Actions paslaptis](../../assets/github-actions/select-setting-action.png)

### 2 žingsnis: Įgalinti darbo srauto leidimus

Atidarykite **Settings** > **Actions** > **General**.

Skiltyje **Workflow permissions**:

1. Įjunkite **Leisti GitHub Actions kurti ir patvirtinti pull užklausas**.
2. Išsaugokite nustatymą.

Žemiau pateikta užduotis aiškiai prašo `contents: write` ir `pull-requests: write`. Laikykite saugyklos numatytuosius darbo srauto leidimus nepakitus. Jei organizacijos politika blokuoja PR kūrimą, kreipkitės į administratorių dėl patvirtinto [GitHub App](#github-app-setup).

### 3 žingsnis: Pridėti darbo srautą

Sukurkite `.github/workflows/co-op-translator.yml`:

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

Pakeiskite `TARGET_LANGUAGES` į kalbas, kurių reikia jūsų projektui. Peržiūra naudoja Python API tik Markdown tikrinimui, atitinkant vertimo žingsnį. Vertimo arba peržiūros klaida sustabdo užduotį prieš PR kūrimą. Darbo srautas nesujungia PR automatiškai. Didelėms saugykloms pridėkite `paths:` filtrą po `on.push`, kad darbo srautas vyktų tik tuomet, kai keičiasi dokumentacija.

### Pasirenkama: notebook'ai ir vaizdai

Notebook'ams pridėkite `-nb` prie vertimo komandos ir nustatykite `notebook=True` peržiūros žingsnyje. Vaizdų tekstui sukonfigūruokite dvi [Azure AI Vision paslaptis](#prerequisites), perduokite jas vertimo žingsnio `env`, pridėkite `-img` prie komandos ir į PR žingsnio `add-paths` įtraukite `translated_images/`. Peržiūrėkite išverstus vaizdus vizualiai; deterministinė peržiūra negarantuoja vaizdų teksto ar lingvistinio tikslumo.

## GitHub App nustatymas

Naudokite patvirtintą GitHub App, kai jūsų organizacija reikalauja App tapatybės arba kai sugeneruotas PR turi sukelti tolimesnį CI be `GITHUB_TOKEN` patvirtinimo žingsnio. App nepereinėja organizacijos politikos; administratoriai vis dar kontroliuoja jo įdiegimą ir leidimus.

### 1 žingsnis: Sukurkite arba įdiekite GitHub App

Naudokite esamą organizacijos suteiktą App, jei yra, arba sukurkite vieną su skaitymo/rašymo prieiga prie **Contents** ir **Pull requests**. Įdiekite jį tikslinei saugyklai su bet kokiu reikalingu organizacijos patvirtinimu.

Užsirašykite:

- App ID
- Privataus rakto turinį

Išsaugokite juos kaip saugyklos paslaptis:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### 2 žingsnis: Sugeneruoti App tokeną

Pridėkite šį žingsnį iškart prieš esamą pull request žingsnį. README šablonui naudokite tą pačią sėkmės sąlygą, kad peržiūros ir nepavykę vertimai neprašytų App tokeno:

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

Tada pakeiskite tik esamo pull request žingsnio `token` įvestį į `${{ steps.generate_token.outputs.token }}`. Išlaikykite jo sėkmės sąlygą, šaką, PR turinį ir `add-paths` nepakitus. Pagal numatytuosius nustatymus tokenas yra ribojamas iki einamosios saugyklos. Kai pritaikote standartinę sąranką vietoje README šablono, praleiskite aukščiau esantį `if`: tas darbo srautas naudoja numatytąją sėkmės sąlygą, todėl tokeno kūrimas ir PR kūrimas vykdomi tik po to, kai vertimas ir peržiūra pavyksta.

Dėl diegimo ir tokeno leidimų žr. oficialų [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2).

## Runner apribojimai

GitHub talpinami runneriai turi maksimalų užduoties trukmės limitą. Didelės saugyklos arba daug tikslinių kalbų gali viršyti tą ribą.

Didesnėms vertimo apkrovoms:

- Versti mažiau kalbų per vykdymą.
- Naudokite turinio žymes (flags) kaip `-md`, `-nb`, arba `-img`.
- Naudokite savarankiškai talpinamą runnerį, kai saugyklos dydis arba modelio delsimas daro talpinamus runnerius nepatikimais.

## Peržiūra CI

Naudokite `co-op-review`, kai pull request turėtų patvirtinti sugeneruotus vertimus be LLM arba Vision teikėjų kvietimo.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` yra beta deterministinis peržiūros komanda. Jos patikros ir išvesties schema gali keistis, bet ji sukurta saugiai naudoti CI, nes ji neįrašo failų ir nekviečia modelių teikėjų.