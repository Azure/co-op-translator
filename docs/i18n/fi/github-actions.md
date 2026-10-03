# GitHub Actions

Käytä GitHub Actionsia, kun haluat, että repositorio kääntää muuttuneen dokumentaation automaattisesti ja avaa pull requestin luoduilla tuloksilla.

Aloita käyttämällä vakiomaista `GITHUB_TOKEN`-asetusta, myös organisaation repositorioissa, jos käytäntö sen sallii. Katso [GitHub-sovelluksen asetukset](#github-app-setup), jos organisaatiosi vaatii sovellusidentiteetin tai tarvitset automaattisia alavirran työnkulkuajoja.

**Ihmiset tekemät muokkaukset:** nämä työnkulut kääntävät muutetut lähdetiedostot kokonaan uudelleen ja voivat ylikirjoittaa käännöksiin tehdyt muokkaukset. Tarkista jokainen PR ennen yhdistämistä. Markdownin lohko‑tason säilyttäminen hyväksytyille muokkauksille edellyttää mukautettua integraatiota [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Ensimmäinen README-käännös-PR

Aloita yhdellä juurena olevalla `README.md`-tiedostolla ja yhdellä kohdekielellä. Tämä työnkulku kääntää vain Markdownia, joten Azure AI Vision ei ole vaadittu.

1. Kopioi [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([katso mallipohjaa GitHubissa](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) kohtaan `.github/workflows/translate-readme.yml` repositorioon, jonka haluat kääntää, ja tee commit kyseisen repositorion oletushaaraan. Malli käyttää juuritoimintoa `Azure/co-op-translator@main`, joka asentaa CLI:n samasta lähdeviitteestä. Lukitse tarkistettu commit toistettavien ajojen varmistamiseksi.
2. Avaa **Actions > Translate README > Run workflow**, valitse kieli ja pidä **Preview only** valittuna. Tarkista token-arvio esikatseluvaiheessa. Esikatselu ei kutsu mallitoimittajia, kirjoita käännöksiä tai luo PR:ää.
3. Lisää salaisuudet yhdelle [tekstitoimittajalle](#prerequisites) ja ota käyttöön **Salli GitHub Actionsin luoda ja hyväksyä vetopyyntöjä** kohdassa **Asetukset > Toiminnot > Yleiset**. Malli pyytää työnsä käyttöoikeuksiksi `contents: write` ja `pull-requests: write`; sinun ei tarvitse muuttaa oletusoikeuksia jokaista työnkulkua varten. Jos organisaation käytäntö estää nämä oikeudet tai asetuksen, kysy ylläpitäjältä hyväksytystä [GitHub-sovelluksesta](#github-app-setup).
4. Suorita työnkulku uudelleen siten, että **Preview only** ei ole valittuna. Se esikatseltelee, kääntää, suorittaa `co-op-review --readme-only` ja luo tai päivittää käännös-PR:n vasta käännöksen ja tarkistuksen onnistuttua. Työnkulun yhteenveto sisältää linkin PR:ään.
5. Tarkista PR:ssä sanamuodot ja tiedostomuutokset, ja yhdistä kun olet valmis. Työnkulku ei yhdistä automaattisesti.

PR sisältää vain `translations/<language>/README.md`-tiedoston ja sen kielimetadata­tiedoston. Lähde-README pysyy muuttumattomana, ja linkit muihin dokumentteihin osoittavat edelleen lähdedokumentteihin. PR:n kuvauksessa luetellaan muuttuneet tiedostot ja rakenteellinen tarkistusraportti. Jos käännös tai tarkistus epäonnistuu, tarkastele työnkulun yhteenvetoa ja epäonnistuneen vaiheen lokit; PR:ää ei luoda. Jos muutoksia ei ole, uutta PR:ää ei tarvita.

**Organization and CI note:** GitHub-sovellus on valinnainen, ei vaatimus organisaation omistuksessa. `GITHUB_TOKEN`:lla pull request -työnkulut PR:n avaamiseen, päivittämiseen tai uudelleenavaamiseen vaativat käyttäjän, jolla on kirjoitusoikeudet, valitsemaan **Approve workflows to run**. Push-työnkulkut eivät käynnisty tällä tokenilla. Automaattista alavirran CI:tä varten katso [GitHub-sovelluksen asetukset](#github-app-setup) ja GitHubin [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Esivaatimukset

Ennen työnkulun luomista, määritä AI-palvelun salaisuudet, joita käännösajo tarvitsee.

Tekstikäännös vaatii yhden kielimallipalveluntarjoajan:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Kuvien kääntäminen vaatii lisäksi Azure AI Visionin:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Lisätietoja paikallisesta konfiguraatiosta: katso [Configuration](configuration.md) ja [Azure AI Setup](azure-ai-setup.md).

## Vakioasetukset

Kokeiltuasi README-työnkulkua, käytä tätä asetusta kääntääksesi repositorion Markdown-tiedostot usealle kielelle. Se suorittaa Markdown-tarkistuksen ennen PR:n avaamista eikä vaadi Azure AI Visionia.

### Vaihe 1: Lisää repositorion salaisuudet

Kohderepositoriossasi avaa **Settings** > **Secrets and variables** > **Actions**, ja lisää sitten työnkulun käyttämät palveluntarjoajan salaisuudet.

![Valitse Actions-salaisuudet](../../assets/github-actions/select-setting-action.png)

### Vaihe 2: Ota työnkulun käyttöoikeudet käyttöön

Avaa **Settings** > **Actions** > **General**.

Kohdassa **Workflow permissions**:

1. Ota käyttöön **Salli GitHub Actionsin luoda ja hyväksyä vetopyyntöjä**.
2. Tallenna asetus.

Alla oleva työ pyytää nimenomaisesti `contents: write` ja `pull-requests: write`. Pidä repositorion oletustyönkulkuoikeudet muuttumattomina. Jos organisaation käytäntö estää PR:n luomisen, kysy ylläpitäjältä hyväksytystä [GitHub-sovelluksesta](#github-app-setup).

### Vaihe 3: Lisää työnkulku

Luo `.github/workflows/co-op-translator.yml`:

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

Vaihda `TARGET_LANGUAGES` niihin kieliin, joita projektisi tarvitsee. Tarkistus käyttää Python API:a tarkistaakseen vain Markdownin, mikä vastaa käännösvaihetta. Käännös- tai tarkistusvirhe pysäyttää työn ennen PR:n luomista. Työnkulku ei yhdistä PR:ää automaattisesti. Suurille repositorioille lisää `paths:`-suodatin `on.push`-kohtaan, jotta työnkulku suoritetaan vain, kun dokumentaatio muuttuu.

### Valinnainen: muistikirjat ja kuvat

Muistikirjoille lisää käännöskomennon loppuun `-nb` ja aseta tarkistusvaiheessa `notebook=True`. Kuvatekstien kohdalla konfiguroi kaksi [Azure AI Vision -salaisuutta](#prerequisites), välitä ne käännösvaiheen `env`-muuttujassa, lisää komentoon `-img` ja lisää PR-vaiheen `add-paths`-kohtaan `translated_images/`. Tarkista käännetyt kuvat visuaalisesti; deterministinen tarkistus ei varmista kuvatekstien tai kieliasun oikeellisuutta.

## GitHub-sovelluksen asetukset

Käytä hyväksyttyä GitHub-sovellusta, kun organisaatiosi vaatii sovellusidentiteetin tai kun luodun PR:n tulee käynnistää alavirran CI ilman `GITHUB_TOKEN`-hyväksyntävaihetta. Sovellus ei kierrä organisaation käytäntöjä; ylläpitäjät hallitsevat edelleen sen asennusta ja käyttöoikeuksia.

### Vaihe 1: Luo tai asenna GitHub-sovellus

Käytä olemassa olevaa organisaation tarjoamaa sovellusta, jos saatavilla, tai luo sellainen, jolla on luku- ja kirjoitusoikeudet **Contents** ja **Pull requests**. Asenna se kohderepositorioon mahdollisen organisaation hyväksynnän mukaisesti.

Record:

- App ID
- Private key contents

Store them as repository secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Vaihe 2: Generoi sovellustoken

Lisää tämä vaihe välittömästi olemassa olevaa pull request -vaihetta edeltäväksi. README-mallin kohdalla käytä samaa onnistumisehtoa, jotta esikatselut ja epäonnistuneet käännökset eivät pyydä sovellustokenia:

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

Sitten muuta vain olemassa olevan pull request -vaiheen `token`-syöte muotoon `${{ steps.generate_token.outputs.token }}`. Pidä sen onnistumisehto, haara, PR-kuvaus ja `add-paths` muuttumattomina. Token on oletuksena rajattu nykyiseen repositorioon. Kun sovellat vakioasetusta README-mallin sijaan, jätä yllä oleva `if` pois: kyseinen työnkulku käyttää oletus-onnistumisehtoa, joten tokenin luonti ja PR:n luonti suoritetaan vasta käännöksen ja tarkistuksen onnistuttua.

Katso virallinen [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) asennusta ja tokenin käyttöoikeuksia varten.

## Runner-rajoitukset

GitHubin isännöimillä juoksijoilla on enimmäistyöaika. Suuret repositoriot tai monet kohdekielet voivat ylittää tämän rajan.

Suurille käännöstyömäärille:

- Käännä vähemmän kieliä kerralla.
- Käytä sisältölippuja kuten `-md`, `-nb` tai `-img`.
- Käytä itseisännöityä runneria, kun repositorion koko tai mallin latenssi tekee isännöidyistä runnereista epäluotettavia.

## Tarkistus CI:ssä

Käytä `co-op-review`-komentoa, kun pull requestin pitää validoida luodut käännökset ilman LLM- tai Vision-palveluntarjoajien kutsumista.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` on beta-vaiheen deterministinen tarkistuskomento. Sen tarkistukset ja tulosskeema saattavat kehittyä, mutta se on suunniteltu turvalliseksi CI:ssä, koska se ei kirjoita tiedostoja tai kutsu mallipalveluntarjoajia.