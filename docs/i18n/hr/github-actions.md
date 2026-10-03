# GitHub Actions

Koristite GitHub Actions kada želite da repozitorij automatski prevede promijenjenu dokumentaciju i otvori pull request s generiranim rezultatima.

Započnite sa standardnim postavljanjem `GITHUB_TOKEN`, uključujući i repozitorije organizacije gdje politika to dopušta. Pogledajte [Postavljanje GitHub aplikacije](#github-app-setup) kada vaša organizacija zahtijeva identitet aplikacije ili trebate automatsko pokretanje daljnjih workflowa.

**Ljudske izmjene:** ovi workflowi ponovno prevode promijenjene izvorne datoteke u cijelosti i mogu prebrisati formulacije uređene u njihovim prijevodima. Pregledajte svaki PR prije spajanja. Očuvanje izmjena na razini blokova Markdowna zahtijeva prilagođenu integraciju s [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Vaš prvi PR za prijevod README-a

Počnite s jednim korijenskim `README.md` i jednim ciljnim jezikom. Ovaj workflow prevodi samo Markdown, pa Azure AI Vision nije potreban.

1. Kopirajte [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([pogledajte predložak na GitHubu](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) u `.github/workflows/translate-readme.yml` u repozitorij koji želite prevesti i izvršite commit na zadanu granu tog repozitorija. Predložak koristi root Action u `Azure/co-op-translator@main`, koja instalira CLI iz istog izvornog refa. Zaključajte pregledani commit za reproducibilne izvođenja.
2. Otvorite **Actions > Translate README > Run workflow**, odaberite jezik i ostavite označeno **Preview only**. Pregledajte procjenu tokena u koraku pregleda. Preview ne poziva pružatelje modela, ne zapisuje prijevode niti ne stvara PR.
3. Dodajte tajne za jednog [pružatelja teksta](#prerequisites), i omogućite **Dopustite GitHub Actions da kreira i odobrava pull requestove** pod **Settings > Actions > General**. Predložak zahtijeva `contents: write` i `pull-requests: write` za svoj posao; nije potrebno mijenjati zadane dozvole za svaki workflow. Ako politika organizacije blokira ove dozvole ili ovu postavku, obratite se administratoru u vezi odobrene [GitHub App](#github-app-setup).
4. Pokrenite workflow ponovno s isključenom opcijom **Preview only**. On vrši pregled, prevodi, pokreće `co-op-review --readme-only` i kreira ili ažurira PR za prijevod tek nakon što prijevod i pregled uspiju. Sažetak workflowa sadrži poveznicu na PR.
5. Pregledajte formulacije i promjene datoteka u PR-u, zatim spojite kad ste spremni. Workflow se ne spaja automatski.

PR sadrži samo `translations/<language>/README.md` i njegovu datoteku s meta-podacima o jeziku. Izvorni README ostaje nepromijenjen, a poveznice na druge dokumente i dalje upućuju na izvorne dokumente. Tijelo PR-a navodi promijenjene datoteke i rezultate strukturnog pregleda. Ako prijevod ili pregled zakaže, pregledajte sažetak workflowa i zapisnike neuspjelih koraka; PR se ne stvara. Ako nema promjena, novi PR nije potreban.

**Napomena za organizaciju i CI:** GitHub App je opcionalan, nije zahtjev vlasništva organizacije. S `GITHUB_TOKEN`, workflowi za pull request koji otvaraju, ažuriraju ili ponovno otvaraju PR zahtijevaju da korisnik s pravom pisanja odabere **Approve workflows to run**. Push workflowi se ne aktiviraju ovim tokenom. Za automatizirani downstream CI, pogledajte [Postavljanje GitHub aplikacije](#github-app-setup) i GitHubova [pravila pokretanja workflowa](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Preduvjeti

Prije nego što stvorite workflow, konfigurirajte tajne AI usluga koje su potrebne vašem procesu prijevoda.

Za prijevod teksta potreban je jedan pružatelj modela jezika:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, te neobavezno `OPENAI_ORG_ID` i `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, te neobavezno `ANTHROPIC_BASE_URL`

Za prijevod slika dodatno je potreban Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Pogledajte [Konfiguracija](configuration.md) i [Postavljanje Azure AI](azure-ai-setup.md) za detalje lokalne konfiguracije.

## Standardno postavljanje

Nakon isprobavanja README workflowa, upotrijebite ovo postavljanje za prijevod Markdown datoteka u repozitoriju na više jezika. Pokreće pregled Markdowna prije otvaranja PR-a i ne zahtijeva Azure AI Vision.

### Korak 1: Dodajte tajne repozitorija

U ciljanom repozitoriju otvorite **Settings** > **Secrets and variables** > **Actions**, zatim dodajte tajne pružatelja koje će vaš workflow koristiti.

![Odaberite tajne za Actions](../../assets/github-actions/select-setting-action.png)

### Korak 2: Omogućite dozvole workflowa

Otvorite **Settings** > **Actions** > **General**.

Pod **Workflow permissions**:

1. Omogućite **Dopustite GitHub Actions da kreira i odobrava pull requestove**.
2. Spremite postavku.

Radni zadatak u nastavku eksplicitno zahtijeva `contents: write` i `pull-requests: write`. Ostavite zadane dozvole workflowa repozitorija nepromijenjene. Ako politika organizacije blokira stvaranje PR-a, obratite se administratoru u vezi odobrene [GitHub App](#github-app-setup).

### Korak 3: Dodajte workflow

Stvorite `.github/workflows/co-op-translator.yml`:

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

Promijenite `TARGET_LANGUAGES` na jezike koje vaš projekt treba. Pregled koristi Python API za provjeru samo Markdowna, što odgovara koraku prijevoda. Pogreška pri prijevodu ili pregledu zaustavlja posao prije stvaranja PR-a. Workflow ne spaja PR automatski. Za velike repozitorije dodajte `paths:` filter pod `on.push` tako da workflow radi samo kada se promijeni dokumentacija.

### Opcionalno: bilježnice i slike

Za bilježnice (notebooks) dodajte `-nb` naredbi za prijevod i postavite `notebook=True` u koraku pregleda. Za tekst na slikama konfigurirajte dvije [Azure AI Vision tajne](#prerequisites), proslijedite ih u `env` koraka prijevoda, dodajte `-img` naredbi i dodajte `translated_images/` u PR koraka `add-paths`. Vizualno pregledajte prevedene slike; deterministički pregled ne potvrđuje točnost teksta na slikama niti jezičnu točnost.

## Postavljanje GitHub aplikacije

Koristite odobrenu GitHub App kada vaša organizacija zahtijeva identitet aplikacije ili kada generirani PR treba pokrenuti downstream CI bez koraka odobrenja `GITHUB_TOKEN`-om. Aplikacija ne zaobilazi politiku organizacije; administratori i dalje kontroliraju njezinu instalaciju i dozvole.

### Korak 1: Stvorite ili instalirajte GitHub aplikaciju

Upotrijebite postojeću aplikaciju koju pruža organizacija ako je dostupna, ili stvorite novu s pristupom za čitanje/pisanje na **Contents** i **Pull requests**. Instalirajte je u ciljani repozitorij uz potrebna odobrenja organizacije.

Zabilježite:

- ID aplikacije
- Sadržaj privatnog ključa

Spremite ih kao tajne repozitorija:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Korak 2: Generirajte token aplikacije

Dodajte ovaj korak odmah prije postojećeg koraka za pull request. Za README predložak koristite istu uvjet uspjeha kako bi pregledi i neuspjeli prijevodi ne tražili token aplikacije:

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

Zatim promijenite samo `token` unos u postojećem koraku za pull request na `${{ steps.generate_token.outputs.token }}`. Ostavite njegov uvjet uspjeha, granu, tijelo PR-a i `add-paths` nepromijenjenima. Token je po defaultu ograničen na trenutni repozitorij. Prilikom prilagodbe standardnog postavljanja umjesto README predloška, izostavite `if` gore: taj workflow koristi zadani uvjet uspjeha, pa stvaranje tokena i stvaranje PR-a pokreću se tek nakon što prijevod i pregled uspiju.

Pogledajte službeni [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) za instalaciju i dozvole tokena.

## Ograničenja runnera

GitHub-hostirani runneri imaju maksimalno trajanje poslova. Veliki repozitoriji ili mnogo ciljanih jezika mogu premašiti to ograničenje.

Za velike radne količine prijevoda:

- Prevedite manje jezika po pokretanju.
- Koristite sadržajne zastavice poput `-md`, `-nb` ili `-img`.
- Koristite self-hosted runner kada veličina repozitorija ili latencija modela čini hostirane runnere nepouzdanim.

## Pregled u CI

Koristite `co-op-review` kada PR treba validirati generirane prijevode bez pozivanja LLM ili Vision pružatelja.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` je beta deterministička naredba za pregled. Njegove provjere i izlazna shema mogu se razvijati, ali je dizajnirana da bude sigurna za CI jer ne zapisuje datoteke niti ne poziva pružatelje modela.