# GitHub Actions

Použijte GitHub Actions, když chcete, aby repozitář automaticky přeložil změněnou dokumentaci a otevřel pull request s vygenerovanými výstupy.

Začněte se standardním nastavením `GITHUB_TOKEN`, včetně repozitářů organizací, kde to politika umožňuje. Viz [Nastavení GitHub App](#github-app-setup), když vaše organizace vyžaduje identitu App nebo potřebujete automatické spuštění downstream workflow.

**Lidské úpravy:** tyto workflowy znovu překládají změněné zdrojové soubory celé a mohou přepsat formulace upravené v jejich překladech. Zkontrolujte každý PR před sloučením. Zachování úrovně bloků Markdown pro přijaté úpravy vyžaduje vlastní integraci s [poskytovatelem stavu překladu Python API](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Váš první PR s překladem README

Začněte s jedním kořenovým `README.md` a jedním cílovým jazykem. Toto workflow překládá pouze Markdown, takže Azure AI Vision není vyžadována.

1. Zkopírujte [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([zobrazit šablonu na GitHubu](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) do `.github/workflows/translate-readme.yml` v repozitáři, který chcete překládat, a uložte jej do výchozí větve tohoto repozitáře. Šablona používá root Action `Azure/co-op-translator@main`, která instaluje CLI ze stejného referenčního zdroje. Pro opakovatelné běhy zalockujte prověřený commit.
2. Otevřete **Actions > Translate README > Run workflow**, vyberte jazyk a ponechte zaškrtnuté **Preview only**. Zkontrolujte odhad tokenů ve fázi náhledu. Náhled nevolá poskytovatele modelu, nepíše překlady ani nevytváří PR.
3. Přidejte tajné klíče pro jednoho [poskytovatele textu](#prerequisites) a povolte **Povolit GitHub Actions vytvářet a schvalovat pull requesty** v **Nastavení > Akce > Obecné**. Šablona požaduje `contents: write` a `pull-requests: write` pro svůj job; nemusíte měnit výchozí oprávnění pro každý workflow. Pokud politika organizace tato oprávnění nebo toto nastavení blokuje, požádejte správce o schválenou [GitHub App](#github-app-setup).
4. Spusťte workflow znovu s odškrtnutým **Preview only**. Vytvoří náhled, přeloží, spustí `co-op-review --readme-only` a vytvoří nebo aktualizuje PR s překladem pouze poté, co překlad a kontrola úspěšně proběhnou. Souhrn workflow obsahuje odkaz na PR.
5. Zkontrolujte znění a změny souborů v PR a poté sloučte, až budete připraveni. Workflow neslučuje automaticky.

PR obsahuje pouze `translations/<language>/README.md` a jeho soubor s metadaty jazyka. Zdrojové README zůstává nezměněné a odkazy na jiné dokumenty stále ukazují na zdrojové dokumenty. Tělo PR uvádí změněné soubory a výsledky strukturované kontroly. Pokud překlad nebo kontrola selže, prohlédněte souhrn workflow a logy selhaného kroku; žádný PR není vytvořen. Pokud nejsou žádné změny, nový PR není potřeba.

**Poznámka k organizaci a CI:** GitHub App je volitelná, není požadavkem vlastnictví organizace. S `GITHUB_TOKEN` vyžadují workflow pro pull-requesty otevírání, aktualizaci nebo znovuotevření PR uživatele s právy zápisu, aby vybral **Approve workflows to run**. Push workflowy nejsou tímto tokenem spouštěny. Pro bezobslužné downstream CI viz [Nastavení GitHub App](#github-app-setup) a GitHub's [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Předpoklady

Před vytvořením workflow nakonfigurujte tajné klíče AI služeb, které váš běh překladu potřebuje.

Textový překlad vyžaduje jednoho poskytovatele jazykového modelu:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus volitelné `OPENAI_ORG_ID` a `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus volitelné `ANTHROPIC_BASE_URL`

Překlad obrázků navíc vyžaduje Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Viz [Konfigurace](configuration.md) a [Nastavení Azure AI](azure-ai-setup.md) pro podrobnosti lokální konfigurace.

## Standardní nastavení

Po vyzkoušení README workflow použijte toto nastavení k překladu Markdown souborů v repozitáři do několika jazyků. Spouští kontrolu Markdown před otevřením PR a nevyžaduje Azure AI Vision.

### Krok 1: Přidejte tajné klíče repozitáře

V cílovém repozitáři otevřete **Settings** > **Secrets and variables** > **Actions**, a poté přidejte tajné klíče poskytovatele, které bude workflow používat.

![Vybrat tajné klíče Actions](../../assets/github-actions/select-setting-action.png)

### Krok 2: Povolit oprávnění workflow

Otevřete **Settings** > **Actions** > **General**.

Pod **Workflow permissions**:

1. Povolte **Povolit GitHub Actions vytvářet a schvalovat pull requesty**.
2. Uložte nastavení.

Následující job explicitně požaduje `contents: write` a `pull-requests: write`. Nechte výchozí oprávnění workflow repozitáře beze změny. Pokud politika organizace blokuje vytváření PR, požádejte správce o schválenou [GitHub App](#github-app-setup).

### Krok 3: Přidejte workflow

Vytvořte `.github/workflows/co-op-translator.yml`:

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

Změňte `TARGET_LANGUAGES` na jazyky, které váš projekt potřebuje. Kontrola používá Python API pouze ke kontrole Markdown, což odpovídá kroku překladu. Chyba při překladu nebo kontrole zastaví job před vytvořením PR. Workflow PR neslučuje automaticky. Pro velké repozitáře přidejte filtr `paths:` pod `on.push`, aby se workflow spouštěl pouze při změnách dokumentace.

### Volitelné: notebooky a obrázky

Pro notebooky přidejte `-nb` ke příkazu překladu a nastavte `notebook=True` v kroku kontroly. Pro text na obrázcích nakonfigurujte dvě [tajné klíče Azure AI Vision](#prerequisites), předávejte je v `env` kroku překladu, přidejte `-img` do příkazu a přidejte `translated_images/` do `add-paths` kroku PR. Překlady obrázků zkontrolujte vizuálně; deterministická kontrola necertifikuje text na obrázcích ani lingvistickou přesnost.

## Nastavení GitHub App

Použijte schválenou GitHub App, když vaše organizace vyžaduje identitu App, nebo když generovaný PR potřebuje spustit downstream CI bez kroku schválení `GITHUB_TOKEN`. App neobejde politiku organizace; správci stále kontrolují její instalaci a oprávnění.

### Krok 1: Vytvoření nebo instalace GitHub App

Použijte existující App poskytnutou organizací, pokud je dostupná, nebo vytvořte App s přístupem pro čtení/zápis k **Contents** a **Pull requests**. Nainstalujte ji do cílového repozitáře se všemi požadovanými schváleními organizace.

Poznamenejte si:

- App ID
- Obsah privátního klíče

Uložte je jako tajné klíče repozitáře:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Krok 2: Vygenerujte token App

Přidejte tento krok bezprostředně před existující krok pull requestu. Pro README šablonu použijte stejnou podmínku úspěchu, aby náhledy a neúspěšné překlady nežádaly o token App:

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

Poté změňte pouze vstup `token` v existujícím kroku pull requestu na `${{ steps.generate_token.outputs.token }}`. Nechte jeho podmínku úspěchu, větev, tělo PR a `add-paths` beze změny. Token je ve výchozím nastavení ohraničen na aktuální repozitář. Při přizpůsobení standardního nastavení místo README šablony vynechte výše uvedené `if`: tohle workflow používá výchozí podmínku úspěchu, takže vytvoření tokenu a vytvoření PR proběhnou pouze poté, co překlad a kontrola uspějí.

Viz oficiální [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) pro instalaci a oprávnění tokenu.

## Omezení runnerů

Runnery hostované GitHubem mají maximální dobu trvání jobu. Velké repozitáře nebo mnoho cílových jazyků může tento limit překročit.

Pro velké překladové zátěže:

- Překládejte méně jazyků na běh.
- Použijte obsahové příznaky jako `-md`, `-nb` nebo `-img`.
- Použijte self-hosted runner, pokud velikost repozitáře nebo latence modelu dělá hostované runnery nespolehlivé.

## Kontrola v CI

Použijte `co-op-review`, když by měl pull request ověřit vygenerované překlady bez volání poskytovatelů LLM nebo Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` je beta deterministický příkaz pro kontrolu. Jeho kontroly a výstupní schéma se mohou vyvíjet, ale je navržen tak, aby byl bezpečný pro CI, protože nezapisuje soubory ani nevolá poskytovatele modelů.