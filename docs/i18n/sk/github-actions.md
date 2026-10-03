# GitHub Actions

Použite GitHub Actions, keď chcete, aby repozitár automaticky prekladal zmenenú dokumentáciu a otvoril pull request s vygenerovanými výsledkami.

Začnite s bežným nastavením `GITHUB_TOKEN`, vrátane repozitárov organizácie, kde to politika umožňuje. Pozrite si [Nastavenie GitHub App](#github-app-setup), ak vaša organizácia vyžaduje identitu App alebo potrebujete automatické spúšťanie downstream workflowov.

**Ručné úpravy:** tieto workflowy znovu prekladajú zmenené zdrojové súbory v celku a môžu prepísať znenie upravené v ich prekladoch. Pred zlúčením skontrolujte každý PR. Zachovanie úprav na úrovni blokov Markdown si vyžaduje vlastnú integráciu s [poskytovateľom stavu prekladu Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Váš prvý PR pre preklad README

Začnite s jedným koreňovým súborom `README.md` a jedným cieľovým jazykom. Tento workflow prekladá iba Markdown, takže Azure AI Vision nie je potrebné.

1. Skopírujte [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([zobraziť šablónu na GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) do `.github/workflows/translate-readme.yml` v repozitári, ktorý chcete prekladať, a commitnite ho do predvoleného branchu toho repozitára. Šablóna používa root Action v `Azure/co-op-translator@main`, ktorá inštaluje CLI z rovnakého source ref. Pripnite skontrolovaný commit pre reprodukovateľné spustenia.
2. Otvorte **Actions > Translate README > Run workflow**, vyberte jazyk a nechajte zaškrtnutú možnosť **Preview only**. Skontrolujte odhad tokenov v kroku náhľadu. Náhľad nevolá poskytovateľov modelov, nezapisuje preklady ani nevytvára PR.
3. Pridajte tajomstvá pre jedného [poskytovateľa textu](#prerequisites) a povolte **GitHub Actions vytvárať a schvaľovať pull requesty** v **Nastavenia > Akcie > Všeobecné**. Šablóna si pre svoju úlohu vyžaduje `contents: write` a `pull-requests: write`; nemusíte meniť predvolené povolenia pre každý workflow. Ak politika organizácie tieto povolenia alebo toto nastavenie blokuje, požiadajte správcu o schválenú [GitHub App](#github-app-setup).
4. Spustite workflow znova s nezaškrtnutou možnosťou **Preview only**. Vykoná náhľad, preklad, spustí `co-op-review --readme-only` a vytvorí alebo aktualizuje PR s prekladom len potom, čo preklad a kontrola uspejú. Súhrn workflowu obsahuje odkaz na PR.
5. Skontrolujte znenie a zmeny súborov v PR, potom ho zlúčte, keď budete pripravení. Workflow nezlúči automaticky.

PR obsahuje len `translations/<language>/README.md` a jeho súbor s metadátami jazyka. Zdrojový README zostáva nezmenený a odkazy na ďalšie dokumenty naďalej smerujú na zdrojové dokumenty. Telo PR uvádza zmenené súbory a výsledky štrukturálnej kontroly. Ak preklad alebo kontrola zlyhajú, preštudujte súhrn workflowu a logy neúspešných krokov; PR sa nevytvorí. Ak nie sú žiadne zmeny, nový PR nie je potrebný.

**Poznámka k organizácii a CI:** GitHub App je voliteľná, nie požiadavka vlastníctva organizácie. S `GITHUB_TOKEN` vyžadujú workflowy pull-requestu pre otvorenie, aktualizáciu alebo znovuotvorenie PR používateľa s právom zápisu, ktorý vyberie **Approve workflows to run**. Push workflowy sa týmto tokenom nespúšťajú. Pre automatizované downstream CI pozrite [Nastavenie GitHub App](#github-app-setup) a GitHubove [pravidlá spúšťania workflowov](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Požiadavky

Pred vytvorením workflowu nakonfigurujte tajomstvá služby AI, ktoré potrebuje váš beh prekladu.

Preklad textu vyžaduje jedného poskytovateľa jazykového modelu:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Preklad obrázkov navyše vyžaduje Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Pozrite si [Konfiguráciu](configuration.md) a [Nastavenie Azure AI](azure-ai-setup.md) pre detaily lokálnej konfigurácie.

## Štandardné nastavenie

Po vyskúšaní README workflowu použite toto nastavenie na preklad Markdown súborov repozitára do viacerých jazykov. Spustí Markdown kontrolu pred otvorením PR a nevyžaduje Azure AI Vision.

### Krok 1: Pridajte tajomstvá repozitára

V cieľovom repozitári otvorte **Settings** > **Secrets and variables** > **Actions**, potom pridajte tajomstvá poskytovateľa, ktoré bude workflow používať.

![Vyberte tajomstvá Actions](../../assets/github-actions/select-setting-action.png)

### Krok 2: Povoliť povolenia workflowu

Otvorte **Settings** > **Actions** > **General**.

Pod **Workflow permissions**:

1. Povoľte **GitHub Actions vytvárať a schvaľovať pull requesty**.
2. Uložte nastavenie.

Nižšie uvedená úloha výslovne žiada o `contents: write` a `pull-requests: write`. Nechajte predvolené povolenia workflowu repozitára nezmenené. Ak politika organizácie blokuje vytváranie PR, opýtajte sa správcu na schválenú [GitHub App](#github-app-setup).

### Krok 3: Pridajte workflow

Vytvorte `.github/workflows/co-op-translator.yml`:

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

Zmeňte `TARGET_LANGUAGES` na jazyky, ktoré váš projekt potrebuje. Kontrola používa Python API na kontrolu len Markdownu, čo zodpovedá kroku prekladu. Chyba pri preklade alebo kontrole zastaví úlohu pred vytvorením PR. Workflow PR automaticky nezlúči. Pre veľké repozitáre pridajte filter `paths:` pod `on.push`, aby sa workflow spúšťal len pri zmenách dokumentácie.

### Voliteľné: notebooky a obrázky

Pre notebooky pridajte `-nb` k prekladovému príkazu a nastavte `notebook=True` v kroku kontroly. Pre text z obrázkov nakonfigurujte dve [tajomstvá Azure AI Vision](#prerequisites), odovzdajte ich v `env` kroku prekladu, pridajte `-img` k príkazu a pridajte `translated_images/` do kroku PR `add-paths`. Prekontrolujte preložené obrázky vizuálne; deterministická kontrola neoveruje text na obrázkoch ani jazykovú presnosť.

## Nastavenie GitHub App

Použite schválenú GitHub App, keď vaša organizácia vyžaduje identitu App alebo keď vygenerovaný PR potrebuje spustiť downstream CI bez kroku schválenia `GITHUB_TOKEN`. App neobchádza politiku organizácie; správcovia stále kontrolujú jej inštaláciu a povolenia.

### Krok 1: Vytvorte alebo nainštalujte GitHub App

Použite existujúcu App poskytnutú organizáciou, ak je k dispozícii, alebo vytvorte jednu s právami na čítanie/zápis do **Contents** a **Pull requests**. Nainštalujte ju na cieľový repozitár s potrebným schválením organizácie.

Zaznamenajte:

- App ID
- Obsah privátneho kľúča

Uložte ich ako tajomstvá repozitára:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Krok 2: Vygenerujte token App

Pridajte tento krok priamo pred existujúci krok pull requestu. Pre README šablónu použite rovnakú podmienku úspechu, aby náhľady a neúspešné preklady nežiadali token App:

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

Potom zmente iba vstup `token` v existujúcom kroku pull requestu na `${{ steps.generate_token.outputs.token }}`. Nechajte jeho podmienku úspechu, vetvu, telo PR a `add-paths` nezmenené. Token je podľa predvoleného nastavenia obmedzený na aktuálny repozitár. Pri prispôsobovaní štandardného nastavenia namiesto README šablóny vynechajte vyššie uvedené `if`: ten workflow používa predvolenú podmienku úspechu, takže vytvorenie tokenu a vytvorenie PR sa spustia len po úspešnom preklade a kontrole.

Pozrite si oficiálnu [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) pre inštaláciu a povolenia tokenu.

## Obmedzenia runnera

Runnery hosťované GitHubom majú maximálnu dobu trvania úlohy. Veľké repozitáre alebo veľa cieľových jazykov môžu tento limit prekročiť.

Pre veľké prekladové záťaže:

- Prekladajte menej jazykov na jedno spustenie.
- Použite argumenty obsahu ako `-md`, `-nb` alebo `-img`.
- Použite self-hosted runner, keď veľkosť repozitára alebo latencia modelu spôsobuje, že hosťované runnery sú nespolehlivé.

## Kontrola v CI

Použite `co-op-review`, keď by mal pull request overiť vygenerované preklady bez volania poskytovateľov LLM alebo Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` je beta deterministický príkaz kontroly. Jeho kontroly a výstupné schéma sa môžu vyvíjať, ale je navrhnutý tak, aby bol bezpečný pre CI, pretože nezapisuje súbory ani nevolá poskytovateľov modelov.