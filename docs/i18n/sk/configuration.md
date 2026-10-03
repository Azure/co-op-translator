# Konfigurácia

Co-op Translator vyžaduje jedného poskytovateľa jazykového modelu. Pre preklad obrázkov sa navyše vyžaduje Azure AI Vision.

Konfigurácia sa načítava z premenných prostredia. Pre lokálne projekty ich umiestnite do súboru `.env` v koreňovom adresári projektu.

Pre nastavenie zdrojov Azure pozrite [Nastavenie Azure AI](azure-ai-setup.md).

## Lokálne nastavenie runtime

Pred lokálnym spustením CLI používajte virtuálne prostredie. Co-op Translator podporuje Python 3.11 až 3.14.

Pre bežné používanie CLI nainštalujte publikovaný balík do virtuálneho prostredia:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Vývoj v repozitári

Pre vývoj v repozitári nainštalujte závislosti z koreňa projektu namiesto toho:

```bash
poetry install
poetry run translate --help
```

Keď je CLI dostupné, nakonfigurujte jedného poskytovateľa jazykového modelu v `.env`.

## Výber poskytovateľa

Nástroj automaticky rozpoznáva poskytovateľov v tomto poradí:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Preklad vyžaduje poverenia poskytovateľa, okrem náhľadov, ako je `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` a `run_review` sú deterministické údržbové operácie a nevyžadujú poverenia poskytovateľa.

## Backend klienta modelu

Od verzie Co-op Translator 0.22.0 používajú Azure OpenAI, OpenAI a Anthropic predvolene Microsoft Agent Framework. Pre bežné použitie nie je potrebné nastavovať backend.

Semantic Kernel zostáva dočasne dostupný pre kompatibilitu. Ak ho chcete vybrať explicitne, nastavte:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Používanie Semantic Kernel vyvolá varovanie o zastaraní. Plánuje sa presun Semantic Kernel do voliteľnej závislosti v 0.23.0 a odstránenie integrácie v 0.24.0, v závislosti od výsledkov kompatibility a spätnej väzby používateľov. Anthropic vyžaduje `agent-framework`; explicitné zvolenie `semantic-kernel` s Anthropic zlyhá s konfiguračnou chybou. Neplatné hodnoty zlyhajú počas inicializácie prekladača s podporou poskytovateľa namiesto tichého prepadu. Sledujte nasadzovanie a hláste blokátory v [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Použite Azure OpenAI, keď je váš model nasadený v Azure AI Foundry alebo Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Kontrola konektivity používa koncový bod, API kľúč, verziu API a názov nasadenia pred začiatkom prekladu.

## OpenAI

Použite OpenAI pri priamom volaní OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Premenná `OPENAI_CHAT_MODEL_ID` je povinná, pretože prekladač potrebuje explicitný chat model pre volania API.

Nechajte `OPENAI_ORG_ID` a `OPENAI_BASE_URL` nenastavené pre predvolené nastavenie. Pridajte ID organizácie len ak ho váš účet potrebuje, alebo base URL len pri používaní vlastného endpointu. Nekopírujte zástupné hodnoty pre voliteľné nastavenia.

## Anthropic Claude

Použite Anthropic pri priamom volaní Claude API. Vytvorte [kľúč Anthropic API](https://platform.claude.com/docs/en/get-started) a vyberte podporované [ID modelu Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Premenné `ANTHROPIC_API_KEY` a `ANTHROPIC_MODEL` sú povinné. Nemusíte nastavovať `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework je predvolený backend.

Nechajte `ANTHROPIC_BASE_URL` nenastavené pre Anthropic API. Nastavte ho iba pri používaní vlastného endpointu.

Hodnota `ANTHROPIC_MAX_TOKENS` má predvolenú hodnotu `8192`, čo ponecháva priestor pre skripty husté na tokeny, ako napríklad Meitei Mayek. Znížte ju, ak váš model alebo endpoint kompatibilný s Anthropic obmedzuje výstup pod túto hodnotu.

## Azure AI Vision

Preklad obrázkov vyžaduje Azure AI Vision, aby nástroj mohol extrahovať text z obrázkov predtým, než ho nakonfigurovaný jazykový model preloží. Anthropic môže preložiť extrahovaný text rovnako ako Azure OpenAI alebo OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Ak je preklad obrázkov zvolený pomocou `-img`, `images=True` alebo bez filtra typu obsahu, nástroj overí konfiguráciu Vision pred začiatkom prekladu.

## Viacero sád poverení

Konfiguračná vrstva podporuje viacero sád poverení pridaním prípony s rovnakým indexom k premenným:

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

Každá sada musí byť kompletná. Kontrola stavu vyberie fungujúcu sadu pred pokračovaním v preklade.

OpenAI a Anthropic podporujú rovnakú konvenciu prípon. Udržujte všetky premenné v sade poverení na tej istej príponke, vrátane voliteľných hodnôt, ako sú `OPENAI_BASE_URL_1` alebo `ANTHROPIC_BASE_URL_1`.

## Požiadavky na príkazy

| Príkaz alebo API | Vyžaduje sa LLM | Vyžaduje Vision | Poznámky |
| --- | --- | --- | --- |
| `translate -md` | Áno | Nie | Prekladá iba Markdown. |
| `translate -nb` | Áno | Nie | Prekladá iba notebooky. |
| `translate -img` | Áno | Áno | Prekladá iba obrázky. |
| `translate` bez typových príznakov | Áno | Áno | Predvolený režim zahŕňa Markdown, notebooky a obrázky. |
| `evaluate` | Áno | Nie | Používa hodnotenie LLM, pokiaľ nie je zvolený `--fast`. |
| `migrate-links` | Nie | Nie | Vykonáva lokálnu migráciu odkazov bez volaní poskytovateľa. |
| `co-op-review` | Nie | Nie | Spúšťa deterministické kontroly štruktúry prekladu, čerstvosti, Markdownu, notebookov a lokálnych odkazov. |
| `run_translation(markdown=True)` | Áno | Nie | Programatický preklad Markdownu. |
| `run_translation(images=True)` | Áno | Áno | Programatický preklad obrázkov. |
| `run_review(...)` | Nie | Nie | Programatická deterministická kontrola. |

## Výstupné adresáre

Predvolený výstup textového prekladu:

```text
translations/<language-code>/<source-relative-path>
```

Predvolený výstup pre preložené obrázky:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API môže prepísať tieto adresáre pomocou `translations_dir` a `image_dir`.