# Konfigurace

Co-op Translator vyžaduje jednoho poskytovatele jazykového modelu. Překlad obrázků navíc vyžaduje Azure AI Vision.

Konfigurace se načítá z proměnných prostředí. Pro lokální projekty umístěte proměnné do souboru `.env` v kořenovém adresáři projektu.

Pro nastavení Azure zdrojů viz [Nastavení Azure AI](azure-ai-setup.md).

## Lokální nastavení runtime

Před spuštěním CLI lokálně použijte virtuální prostředí. Co-op Translator podporuje Python 3.10 až 3.12.

Pro běžné používání CLI nainstalujte publikovaný balíček do virtuálního prostředí:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Pro vývoj v repozitáři nainstalujte závislosti z kořenového adresáře projektu:

```bash
poetry install
poetry run translate --help
```

Poté, co je CLI dostupné, nakonfigurujte v souboru `.env` jednoho poskytovatele jazykového modelu.

## Výběr poskytovatele

Nástroj automaticky detekuje poskytovatele v tomto pořadí:

1. Azure OpenAI
2. OpenAI

Pokud není nakonfigurován žádný z poskytovatelů, při kontrolách konfigurace selžou příkazy `translate`, `evaluate`, `migrate-links` a `run_translation`. `co-op-review` a `run_review` jsou deterministické údržbové kontroly a nevyžadují přihlašovací údaje poskytovatele.

## Azure OpenAI

Použijte Azure OpenAI, pokud je váš model nasazen v Azure AI Foundry nebo v Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Kontrola připojení používá endpoint, API klíč, verzi API a název nasazení před zahájením překladu.

## OpenAI

Použijte OpenAI, když voláte OpenAI API přímo.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # volitelný
OPENAI_BASE_URL="..."        # volitelný
```

`OPENAI_CHAT_MODEL_ID` je vyžadováno, protože překladač potřebuje explicitní chatovací model pro volání API.

## Azure AI Vision

Překlad obrázků vyžaduje Azure AI Vision, aby nástroj mohl před překladem z obrázků extrahovat text.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Pokud je překlad obrázků vybrán pomocí `-img`, `images=True` nebo pokud není použit filtr typu obsahu, nástroj před zahájením překladu ověří konfiguraci Vision.

## Více sad pověření

Vrstva konfigurace podporuje více sad pověření přidáním stejného indexu jako přípony k proměnným:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Každá sada musí být kompletní. Kontrola stavu vybere funkční sadu před pokračováním překladu.

## Požadavky příkazů

| Příkaz nebo API | LLM vyžadováno | Vision vyžadováno | Poznámky |
| --- | --- | --- | --- |
| `translate -md` | Ano | Ne | Překládá pouze Markdown. |
| `translate -nb` | Ano | Ne | Překládá pouze notebooky. |
| `translate -img` | Ano | Ano | Překládá pouze obrázky. |
| `translate` with no type flags | Ano | Ano | Výchozí režim zahrnuje Markdown, notebooky a obrázky. |
| `evaluate` | Ano | Ne | Používá hodnocení LLM, pokud není vybrán přepínač `--fast`. |
| `migrate-links` | Ano | Ne | Provádí migraci odkazů, ale stále spouští sdílené kontroly konfigurace. |
| `co-op-review` | Ne | Ne | Provádí deterministické kontroly struktury překladu, čerstvosti, Markdownu, notebooků a lokálních odkazů. |
| `run_translation(markdown=True)` | Ano | Ne | Programový překlad Markdownu. |
| `run_translation(images=True)` | Ano | Ano | Programový překlad obrázků. |
| `run_review(...)` | Ne | Ne | Programové deterministické přezkoumání. |

## Výstupní adresáře

Výchozí výstup překladu textu:

```text
translations/<language-code>/<source-relative-path>
```

Výchozí výstup přeložených obrázků:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API může tyto adresáře přepsat pomocí `translations_dir` a `image_dir`.