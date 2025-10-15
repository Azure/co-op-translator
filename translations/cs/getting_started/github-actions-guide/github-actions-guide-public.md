<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "527ca4d0a8d3f51087ec3317279e36ee",
  "translation_date": "2025-10-15T03:53:21+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "cs"
}
-->
# Použití Co-op Translator GitHub Action (Veřejné nastavení)

**Cílová skupina:** Tento průvodce je určen pro uživatele ve většině veřejných nebo soukromých repozitářů, kde jsou dostačující standardní oprávnění GitHub Actions. Využívá vestavěný `GITHUB_TOKEN`.

Automatizujte překlad dokumentace vašeho repozitáře snadno pomocí Co-op Translator GitHub Action. Tento průvodce vás provede nastavením akce, která automaticky vytváří pull requesty s aktualizovanými překlady pokaždé, když se změní vaše zdrojové Markdown soubory nebo obrázky.

> [!IMPORTANT]
>
> **Výběr správného průvodce:**
>
> Tento průvodce popisuje **jednodušší nastavení pomocí standardního `GITHUB_TOKEN`**. Toto je doporučená metoda pro většinu uživatelů, protože nevyžaduje správu citlivých privátních klíčů GitHub App.
>

## Předpoklady

Než začnete konfigurovat GitHub Action, ujistěte se, že máte připravené potřebné přihlašovací údaje k AI službě.

**1. Povinné: Přihlašovací údaje k AI jazykovému modelu**
Potřebujete přihlašovací údaje alespoň k jednomu podporovanému jazykovému modelu:

- **Azure OpenAI**: Vyžaduje Endpoint, API klíč, názvy modelu/deploymentu, verzi API.
- **OpenAI**: Vyžaduje API klíč, (volitelně: Org ID, Base URL, Model ID).
- Podrobnosti najdete v [Podporované modely a služby](../../../../README.md).

**2. Volitelné: Přihlašovací údaje k AI Vision (pro překlad textu v obrázcích)**

- Vyžadováno pouze pokud potřebujete překládat text v obrázcích.
- **Azure AI Vision**: Vyžaduje Endpoint a Subscription Key.
- Pokud není zadáno, akce se spustí v [pouze Markdown režimu](../markdown-only-mode.md).

## Nastavení a konfigurace

Postupujte podle těchto kroků pro nastavení Co-op Translator GitHub Action ve vašem repozitáři pomocí standardního `GITHUB_TOKEN`.

### Krok 1: Pochopení autentizace (Použití `GITHUB_TOKEN`)

Tento workflow používá vestavěný `GITHUB_TOKEN`, který poskytuje GitHub Actions. Tento token automaticky uděluje workflowu oprávnění k interakci s vaším repozitářem na základě nastavení z **Kroku 3**.

### Krok 2: Nastavení tajných údajů v repozitáři

Stačí přidat **přihlašovací údaje k AI službě** jako šifrovaná tajemství v nastavení vašeho repozitáře.

1.  Přejděte do cílového GitHub repozitáře.
2.  Otevřete **Settings** > **Secrets and variables** > **Actions**.
3.  V sekci **Repository secrets** klikněte na **New repository secret** pro každé požadované tajemství AI služby uvedené níže.

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.cs.png" alt="Vyberte nastavení akce"> *(Obrázek: Ukazuje, kde přidat tajemství)*

**Požadovaná tajemství AI služby (Přidejte VŠECHNA, která odpovídají vašim předpokladům):**

| Název tajemství                      | Popis                                         | Zdroj hodnoty                  |
| :----------------------------------- | :--------------------------------------------- | :----------------------------- |
| `AZURE_AI_SERVICE_API_KEY`           | Klíč pro Azure AI Service (Computer Vision)    | Vaše Azure AI Foundry          |
| `AZURE_AI_SERVICE_ENDPOINT`          | Endpoint pro Azure AI Service (Computer Vision)| Vaše Azure AI Foundry          |
| `AZURE_OPENAI_API_KEY`               | Klíč pro Azure OpenAI službu                   | Vaše Azure AI Foundry          |
| `AZURE_OPENAI_ENDPOINT`              | Endpoint pro Azure OpenAI službu               | Vaše Azure AI Foundry          |
| `AZURE_OPENAI_MODEL_NAME`            | Název vašeho Azure OpenAI modelu               | Vaše Azure AI Foundry          |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`  | Název vašeho Azure OpenAI deploymentu          | Vaše Azure AI Foundry          |
| `AZURE_OPENAI_API_VERSION`           | Verze API pro Azure OpenAI                     | Vaše Azure AI Foundry          |
| `OPENAI_API_KEY`                     | API klíč pro OpenAI                            | Vaše OpenAI Platform           |
| `OPENAI_ORG_ID`                      | OpenAI Organization ID (volitelné)             | Vaše OpenAI Platform           |
| `OPENAI_CHAT_MODEL_ID`               | Konkrétní OpenAI model ID (volitelné)          | Vaše OpenAI Platform           |
| `OPENAI_BASE_URL`                    | Vlastní OpenAI API Base URL (volitelné)        | Vaše OpenAI Platform           |

### Krok 3: Nastavení oprávnění workflowu

GitHub Action potřebuje oprávnění udělená přes `GITHUB_TOKEN` pro checkout kódu a vytváření pull requestů.

1.  V repozitáři otevřete **Settings** > **Actions** > **General**.
2.  Sjeďte dolů do sekce **Workflow permissions**.
3.  Vyberte **Read and write permissions**. Tím získá `GITHUB_TOKEN` potřebná oprávnění `contents: write` a `pull-requests: write` pro tento workflow.
4.  Ujistěte se, že je zaškrtnuto **Allow GitHub Actions to create and approve pull requests**.
5.  Klikněte na **Save**.

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.cs.png" alt="Nastavení oprávnění">

### Krok 4: Vytvoření workflow souboru

Nakonec vytvořte YAML soubor, který definuje automatizovaný workflow s použitím `GITHUB_TOKEN`.

1.  V kořenovém adresáři repozitáře vytvořte složku `.github/workflows/`, pokud neexistuje.
2.  Do `.github/workflows/` vytvořte soubor s názvem `co-op-translator.yml`.
3.  Vložte následující obsah do souboru `co-op-translator.yml`.

```yaml
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
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
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

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
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
4.  **Přizpůsobení workflowu:**
  - **[!IMPORTANT] Cílové jazyky:** Ve kroku `Run Co-op Translator` **MUSÍTE zkontrolovat a upravit seznam jazykových kódů** v příkazu `translate -l "..." -y` podle potřeb vašeho projektu. Ukázkový seznam (`ar de es...`) je třeba nahradit nebo upravit.
  - **Trigger (`on:`):** Aktuální trigger spouští workflow při každém pushi do `main`. U velkých repozitářů zvažte přidání filtru `paths:` (viz komentář v YAML), aby se workflow spouštěl pouze při změně relevantních souborů (např. zdrojové dokumentace), což šetří čas běhu.
  - **Detaily PR:** Přizpůsobte `commit-message`, `title`, `body`, název `branch` a `labels` ve kroku `Create Pull Request` podle potřeby.

## Spuštění workflowu

> [!WARNING]  
> **Časový limit pro GitHub-hostované běhy:**  
> GitHub-hostované běhy jako `ubuntu-latest` mají **maximální časový limit 6 hodin**.  
> U velkých dokumentačních repozitářů, pokud překlad přesáhne 6 hodin, workflow bude automaticky ukončen.  
> Abyste tomu předešli, zvažte:  
> - Použití **self-hosted runneru** (bez časového limitu)  
> - Snížení počtu cílových jazyků na jeden běh

Jakmile je soubor `co-op-translator.yml` sloučen do vaší hlavní větve (nebo větve uvedené v triggeru `on:`), workflow se automaticky spustí pokaždé, když do této větve provedete změny (a splníte případný filtr `paths`).

---

**Prohlášení**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neneseme odpovědnost za jakékoli nedorozumění nebo nesprávné výklady vzniklé v důsledku použití tohoto překladu.