# Konfigurácia

Co-op Translator vyžaduje jedného poskytovateľa jazykového modelu. Preklad obrázkov navyše vyžaduje Azure AI Vision.

Konfigurácia sa načítava z premenných prostredia. Pre lokálne projekty umiestnite ich do súboru `.env` v koreňovom adresári projektu.

Pre nastavenie zdrojov Azure pozrite [Azure AI Setup](azure-ai-setup.md).

## Lokálne nastavenie runtime

Použite virtuálne prostredie pred spustením CLI lokálne. Co-op Translator podporuje Python 3.10 až 3.12.

Pre bežné používanie CLI nainštalujte zverejnený balík do virtuálneho prostredia:

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

Pre vývoj v repozitári namiesto toho nainštalujte závislosti z koreňového adresára projektu:

```bash
poetry install
poetry run translate --help
```

Po sprístupnení CLI nakonfigurujte v `.env` jedného poskytovateľa jazykového modelu.

## Výber poskytovateľa

Nástroj automaticky detekuje poskytovateľov v tomto poradí:

1. Azure OpenAI
2. OpenAI

Ak nie je nakonfigurovaný žiadny z poskytovateľov, `translate`, `evaluate`, `migrate-links` a `run_translation` zlyhajú počas kontrol konfigurácie. `co-op-review` a `run_review` sú deterministické údržbové kontroly a nevyžadujú poverenia poskytovateľa.

## Azure OpenAI

Použite Azure OpenAI, keď je váš model nasadený v Azure AI Foundry alebo v Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Kontrola konektivity používa endpoint, API kľúč, verziu API a názov nasadenia pred začiatkom prekladu.

## OpenAI

Použite OpenAI pri priamom volaní OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # voliteľné
OPENAI_BASE_URL="..."        # voliteľné
```

`OPENAI_CHAT_MODEL_ID` je povinný, pretože prekladač potrebuje explicitný chatovací model pre volania API.

## Azure AI Vision

Preklad obrázkov vyžaduje Azure AI Vision, aby nástroj mohol extrahovať text z obrázkov pred ich prekladom.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ak je preklad obrázkov vybraný pomocou `-img`, `images=True` alebo bez filtra typu obsahu, nástroj overí konfiguráciu Vision pred začiatkom prekladu.

## Viacero sád poverení

Vrstva konfigurácie podporuje viacero sád poverení pridaním rovnakého indexu na koniec premenných:

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

Každá sada musí byť úplná. Kontrola zdravotného stavu vyberie funkčnú sadu pred pokračovaním prekladu.

## Požiadavky príkazov

| Príkaz alebo API | Vyžaduje LLM | Vyžaduje Vision | Poznámky |
| --- | --- | --- | --- |
| `translate -md` | Áno | Nie | Prekladá len Markdown. |
| `translate -nb` | Áno | Nie | Prekladá len notebooky. |
| `translate -img` | Áno | Áno | Prekladá len obrázky. |
| `translate` with no type flags | Áno | Áno | Predvolený režim zahŕňa Markdown, notebooky a obrázky. |
| `evaluate` | Áno | Nie | Používa hodnotenie LLM, pokiaľ nie je zvolená voľba `--fast`. |
| `migrate-links` | Áno | Nie | Vykonáva migráciu odkazov, ale stále spúšťa spoločné kontroly konfigurácie. |
| `co-op-review` | Nie | Nie | Vykonáva deterministické kontroly štruktúry prekladu, aktuálnosti, Markdownu, notebookov a lokálnych odkazov. |
| `run_translation(markdown=True)` | Áno | Nie | Programatický preklad Markdownu. |
| `run_translation(images=True)` | Áno | Áno | Programatický preklad obrázkov. |
| `run_review(...)` | Nie | Nie | Programatické deterministické preskúmanie. |

## Výstupné adresáre

Predvolený výstup pre textový preklad:

```text
translations/<language-code>/<source-relative-path>
```

Predvolený výstup pre preložené obrázky:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API môže tieto adresáre prepísať pomocou `translations_dir` a `image_dir`.