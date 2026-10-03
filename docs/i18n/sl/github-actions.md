# GitHub Actions

Uporabite GitHub Actions, kadar želite, da repozitorij samodejno prevede spremenjeno dokumentacijo in odpre pull request z ustvarjenimi izhodi.

Začnite z običajno nastavitvijo `GITHUB_TOKEN`, tudi za repozitorije organizacij, kjer politika to dovoljuje. Oglejte si [Nastavitev GitHub aplikacije](#github-app-setup), če vaša organizacija zahteva identiteto aplikacije ali potrebujete samodejne zagon downstream delovnih tokov.

**Ročne spremembe:** ti delovni tokovi ponovno v celoti prevedejo spremenjene izvorne datoteke in lahko prepišejo besedilo, ki so ga ročno uredili v prevodih. Pred združitvijo preglejte vsak PR. Ohranjanje sprememb na ravni Markdown blokov zahteva prilagojeno integracijo s [ponudnikom stanja prevoda Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Vaš prvi PR za prevod README

Začnite z eno korensko datoteko `README.md` in enim ciljnim jezikom. Ta delovni tok prevaja samo Markdown, zato Azure AI Vision ni potreben.

1. Kopirajte [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([ogled predloge na GitHubu](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) v `.github/workflows/translate-readme.yml` v repozitorij, ki ga želite prevesti, in ga commitajte v privzeto vejo tega repozitorija. Predloga uporablja glavno Action v `Azure/co-op-translator@main`, ki namesti CLI iz istega vira. Za ponovljive izvedbe pripnite pregledan commit.
2. Odprite **Actions > Translate README > Run workflow**, izberite jezik in pustite označeno **Preview only**. Preglejte oceno tokenov v koraku predogleda. Predogled ne kliče ponudnikov modelov, ne zapisuje prevodov in ne ustvari PR.
3. Dodajte skrivnosti za en [ponudnik besedila](#prerequisites), in omogočite **Dovoli GitHub Actions ustvarjanje in odobritev pull requestov** v **Nastavitve > Dejanja > Splošno**. Predloga zahteva `contents: write` in `pull-requests: write` za svoje delo; ni treba spreminjati privzetih dovoljenj za vsak delovni tok. Če politika organizacije blokira ta dovoljenja ali to nastavitev, vprašajte skrbnika za odobreno [aplikacijo GitHub](#github-app-setup).
4. Zaženite delovni tok znova s preklicano označitvijo **Preview only**. Izvede predogled, prevede, zažene `co-op-review --readme-only`, in ustvari ali posodobi prevodni PR šele po uspešni prevodu in pregledu. Povzetek delovnega toka se poveže na PR.
5. Preglejte besedilo in spremembe datotek v PR, nato združite, ko ste pripravljeni. Delovni tok ne združi samodejno.

PR vsebuje samo `translations/<language>/README.md` in njegovo datoteko z metapodatki jezika. Izvorni README ostane nespremenjen, povezave na druge dokumente pa še vedno kažejo na izvorne dokumente. V telo PR so navedene spremenjene datoteke in rezultati strukturnega pregleda. Če prevod ali pregled ne uspe, preglejte povzetek delovnega toka in dnevnike neuspelih korakov; PR ni ustvarjen. Če ni sprememb, nov PR ni potreben.

**Opomba za organizacije in CI:** GitHub App je izbiren, ni zahteva lastništva organizacije. Z `GITHUB_TOKEN` delovni tokovi za pull requeste za odpiranje, posodabljanje ali ponovno odpiranje PR zahtevajo uporabnika z dostopom za pisanje, da izbere **Approve workflows to run**. Push delovni tokovi niso sproženi s tem tokenom. Za brezpotrben downstream CI glejte [Nastavitev GitHub aplikacije](#github-app-setup) in GitHubova [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Predpogoji

Pred ustvarjanjem delovnega toka konfigurirajte skrivnosti AI storitve, ki jih potrebuje vaš prevod.

Za prevod besedila je potreben en ponudnik jezikovnega modela:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Za prevod slik dodatno zahteva Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Oglejte si [Konfiguracija](configuration.md) in [Nastavitev Azure AI](azure-ai-setup.md) za podrobnosti lokalne konfiguracije.

## Standardna nastavitev

Po preizkusu delovnega toka za README uporabite to nastavitev za prevajanje Markdown datotek repozitorija v več jezikov. Izvede pregled Markdowna pred odpiranjem PR in ne zahteva Azure AI Vision.

### Korak 1: Dodajte skrivnosti repozitorija

V ciljnem repozitoriju odprite **Settings** > **Secrets and variables** > **Actions**, nato dodajte skrivnosti ponudnika, ki jih bo uporabil vaš delovni tok.

![Izberite skrivnosti Actions](../../assets/github-actions/select-setting-action.png)

### Korak 2: Omogočite dovoljenja delovnega toka

Odprite **Settings** > **Actions** > **General**.

Pod **Workflow permissions**:

1. Omogočite **Dovoli GitHub Actions, da ustvarja in odobri pull requeste**.
2. Shranite nastavitev.

Spodnje delo izrecno zahteva `contents: write` in `pull-requests: write`. Privzetih dovoljenj delovnega toka repozitorija ne spreminjajte. Če politika organizacije blokira ustvarjanje PR, vprašajte skrbnika glede odobrene [GitHub App](#github-app-setup).

### Korak 3: Dodajte delovni tok

Ustvarite `.github/workflows/co-op-translator.yml`:

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

Spremenite `TARGET_LANGUAGES` v jezike, ki jih potrebuje vaš projekt. Pregled uporablja Python API za preverjanje samo Markdowna, kar ustreza koraku prevajanja. Napaka pri prevodu ali pregledu ustavi delo pred ustvarjanjem PR. Delovni tok PR ne združi samodejno. Za velike repozitorije dodajte filter `paths:` pod `on.push`, da delovni tok teče le, ko se spremeni dokumentacija.

### Izbirno: zvezki in slike

Za zvezke dodajte `-nb` k prevodnemu ukazu in nastavite `notebook=True` v koraku pregleda. Za besedilo na slikah konfigurirajte dve [skrivnosti Azure AI Vision](#prerequisites), prenesite jih v `env` prevodnega koraka, dodajte `-img` k ukazu in dodajte `translated_images/` v koraku PR `add-paths`. Preglejte prevedene slike vizualno; deterministični pregled ne potrjuje besedila na slikah ali jezikovne natančnosti.

## Nastavitev GitHub aplikacije

Uporabite odobreno GitHub aplikacijo, kadar vaša organizacija zahteva identiteto aplikacije, ali kadar ustvarjeni PR potrebuje sprožitev downstream CI brez koraka odobritve `GITHUB_TOKEN`. Aplikacija ne zaobide politike organizacije; skrbniki še vedno nadzorujejo njeno namestitev in dovoljenja.

### Korak 1: Ustvarite ali namestite GitHub aplikacijo

Uporabite obstoječo aplikacijo, ki jo zagotavlja organizacija, če je na voljo, ali ustvarite novo z dostopom za branje/pisanje do **Contents** in **Pull requests**. Namestite jo na ciljni repozitorij z morebitno potrebno odobritvijo organizacije.

Record:

- App ID
- Vsebina zasebnega ključa

Shrani jih kot skrivnosti repozitorija:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Korak 2: Generirajte žeton aplikacije

Dodajte ta korak takoj pred obstoječim korakom pull requesta. Za predlogo README uporabite isto pogoj uspeha, tako da predogledi in neuspešni prevodi ne zahtevajo žetona aplikacije:

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

Nato spremenite samo obstoječi `token` vhod koraka pull requesta na `${{ steps.generate_token.outputs.token }}`. Ohranite njegovo pogoj uspeha, vejo, telo PR in `add-paths` nespremenjene. Žeton je privzeto omejen na trenutni repozitorij. Pri prilagajanju standardne nastavitve namesto predloge README izpustite zgornji `if`: ta delovni tok uporablja privzeti pogoj uspeha, zato ustvarjanje žetona in ustvarjanje PR tečeta šele po uspešnem prevodu in pregledu.

Oglejte si uradni [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) za namestitev in dovoljenja žetona.

## Omejitve runnerjev

GitHub-hostani runnerji imajo največno trajanje opravila. Veliki repozitoriji ali veliko ciljnih jezikov lahko presegajo to omejitev.

Za velike prevodne obremenitve:

- Prevedite manj jezikov na zagon.
- Uporabite zastavice vsebine, kot so `-md`, `-nb` ali `-img`.
- Uporabite self-hosted runner, kadar velikost repozitorija ali zakasnitev modela naredi hostane runnerje nezanesljive.

## Pregled v CI

Uporabite `co-op-review`, kadar naj pull request preveri ustvarjene prevode, ne da bi klical LLM ali Vision ponudnike.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` je beta determinističen ukaz za pregled. Njegove preverbe in shema izhodov se lahko razvijajo, vendar je zasnovan kot varen za CI, ker ne zapisuje datotek ali kliče ponudnikov modelov.