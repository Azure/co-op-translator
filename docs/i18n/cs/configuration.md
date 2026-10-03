# Konfigurace

Co-op Translator vyžaduje jednoho poskytovatele modelu jazyka. Překlad obrázků navíc vyžaduje Azure AI Vision.

Konfigurace se načítá z proměnných prostředí. Pro lokální projekty je umístěte do souboru `.env` v kořeni projektu.

Pro nastavení prostředků Azure viz [Nastavení Azure AI](azure-ai-setup.md).

## Lokální nastavení runtime

Před spuštěním CLI lokálně použijte virtuální prostředí. Co-op Translator podporuje Python 3.11 až 3.14.

Pro běžné použití CLI nainstalujte publikovaný balíček do virtuálního prostředí:

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

### Vývoj v repozitáři

Pro vývoj repozitáře místo toho nainstalujte závislosti z kořene projektu:

```bash
poetry install
poetry run translate --help
```

Poté, co je CLI dostupné, nastavte v `.env` jednoho poskytovatele modelu jazyka.

## Výběr poskytovatele

Nástroj automaticky rozpoznává poskytovatele v tomto pořadí:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Překlad vyžaduje přihlašovací údaje poskytovatele, s výjimkou náhledů, například `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` a `run_review` jsou deterministické údržbové operace a nevyžadují přihlašovací údaje poskytovatele.

## Backend klienta modelu

Od verze Co-op Translator 0.22.0 používají Azure OpenAI, OpenAI a Anthropic ve výchozím nastavení Microsoft Agent Framework. Pro běžné použití není třeba nastavovat backend.

Semantic Kernel zůstává dočasně dostupný pro kompatibilitu. Pro jeho explicitní výběr nastavte:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Používání Semantic Kernel vyvolává varování o zastarání. Plánuje se přesunout Semantic Kernel do volitelné závislosti v 0.23.0 a odstranit integraci v 0.24.0, v závislosti na výsledcích kompatibility a zpětné vazbě uživatelů. Anthropic vyžaduje `agent-framework`; explicitní výběr `semantic-kernel` s Anthropic selže s konfigurační chybou. Neplatné hodnoty selhávají při inicializaci překladače závislého na poskytovateli místo toho, aby tiše přešly na záložní možnost. Sledujte nasazování a nahlaste blokátory v [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Používejte Azure OpenAI, když je váš model nasazen v Azure AI Foundry nebo Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Kontrola konektivity používá koncový bod, API klíč, verzi API a název nasazení před zahájením překladu.

## OpenAI

Používejte OpenAI při přímém volání rozhraní OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` je povinné, protože překladač potřebuje explicitní chatovací model pro volání API.

Nechte `OPENAI_ORG_ID` a `OPENAI_BASE_URL` nezadané pro výchozí nastavení. Přidejte ID organizace jen pokud ho váš účet vyžaduje, nebo základní URL jen při použití vlastního koncového bodu. Nekopírujte zástupné hodnoty pro volitelná nastavení.

## Anthropic Claude

Používejte Anthropic při přímém volání Claude API. Vytvořte [klíč API Anthropic](https://platform.claude.com/docs/en/get-started) a vyberte podporované [ID modelu Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` a `ANTHROPIC_MODEL` jsou povinné. Není třeba nastavovat `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework je výchozí backend.

Nechte `ANTHROPIC_BASE_URL` nezadané pro Anthropic API. Nastavte ho pouze při použití vlastního koncového bodu.

`ANTHROPIC_MAX_TOKENS` má výchozí hodnotu `8192`, což ponechává místo pro tokenově náročné skripty jako Meitei Mayek. Snižte jej, pokud váš model nebo endpoint kompatibilní s Anthropic omezuje výstup pod tuto hodnotu.

## Azure AI Vision

Překlad obrázků vyžaduje Azure AI Vision, aby nástroj mohl z obrázků nejprve extrahovat text, který následně přeloží nakonfigurovaný jazykový model. Anthropic může extrahovaný text překládat stejně jako Azure OpenAI nebo OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Pokud je překlad obrázků zvolen pomocí `-img`, `images=True` nebo není filtrován typ obsahu, nástroj před zahájením překladu ověří konfiguraci Vision.

## Více sad přihlašovacích údajů

Vrstva konfigurace podporuje více sad přihlašovacích údajů připojením stejného indexu jako přípony k proměnným:

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

OpenAI a Anthropic podporují stejnou konvenci přípon. Udržujte každou proměnnou v sadě přihlašovacích údajů se stejnou příponou, včetně volitelných hodnot jako `OPENAI_BASE_URL_1` nebo `ANTHROPIC_BASE_URL_1`.

## Požadavky příkazů

| Příkaz nebo API | Požadováno LLM | Požadováno Vision | Poznámky |
| --- | --- | --- | --- |
| `translate -md` | Ano | Ne | Překládá pouze Markdown. |
| `translate -nb` | Ano | Ne | Překládá pouze notebooky. |
| `translate -img` | Ano | Ano | Překládá pouze obrázky. |
| `translate` bez typových přepínačů | Ano | Ano | Výchozí režim zahrnuje Markdown, notebooky a obrázky. |
| `evaluate` | Ano | Ne | Používá hodnocení LLM, pokud není zvolen přepínač `--fast`. |
| `migrate-links` | Ne | Ne | Provádí lokální migraci odkazů bez volání poskytovatele. |
| `co-op-review` | Ne | Ne | Provádí deterministické kontroly struktury překladu, aktuálnosti, Markdownu, notebooků a lokálních odkazů. |
| `run_translation(markdown=True)` | Ano | Ne | Programatický překlad Markdownu. |
| `run_translation(images=True)` | Ano | Ano | Programatický překlad obrázků. |
| `run_review(...)` | Ne | Ne | Programatické deterministické přezkoumání. |

## Výstupní adresáře

Výchozí výstup pro překlad textu:

```text
translations/<language-code>/<source-relative-path>
```

Výchozí výstup přeložených obrázků:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API může tyto adresáře přepsat pomocí `translations_dir` a `image_dir`.