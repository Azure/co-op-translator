# Konfiguracija

Co-op Translator zahteva enega ponudnika jezikovnega modela. Prevajanje slik dodatno zahteva Azure AI Vision.

Konfiguracija se bere iz okoljskih spremenljivk. Za lokalne projekte jih postavite v datoteko `.env` v korenu projekta.

Za nastavitev Azure virov glejte [Nastavitev Azure AI](azure-ai-setup.md).

## Lokalna nastavitev zagona

Pred lokalnim zagonom ukazne vrstice uporabite virtualno okolje. Co-op Translator podpira Python 3.11 do 3.14.

Za običajno uporabo ukazne vrstice namestite objavljen paket znotraj virtualnega okolja:

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

### Razvoj repozitorija

Za razvoj repozitorija namestite odvisnosti iz korena projekta:

```bash
poetry install
poetry run translate --help
```

Ko je ukazna vrstica na voljo, konfigurirajte enega ponudnika jezikovnega modela v `.env`.

## Izbira ponudnika

Orodje samodejno zazna ponudnike v tem vrstnem redu:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Prevajanje zahteva poverilnice ponudnika, razen za predoglede, kot je `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` in `run_review` so deterministične vzdrževalne operacije in ne zahtevajo poverilnic ponudnika.

## Backend odjemalca modela

Od različice Co-op Translator 0.22.0 dalje Azure OpenAI, OpenAI in Anthropic privzeto uporabljajo Microsoft Agent Framework. Za običajno uporabo ni potrebna nobena nastavitev backenda.

Semantic Kernel ostaja začasno na voljo za združljivost. Če ga želite izbrati eksplicitno, nastavite:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Uporaba Semantic Kernel sproži opozorilo o zastaranju. Paket namerava premakniti Semantic Kernel v opcijsko odvisnost v 0.23.0 in odstraniti integracijo v 0.24.0, odvisno od rezultatov združljivosti in povratnih informacij uporabnikov. Anthropic zahteva `agent-framework`; eksplicitna izbira `semantic-kernel` z Anthropic povzroči napako pri konfiguraciji. Neveljavne vrednosti povzročijo napako med inicializacijo prevajalnika, ki temelji na ponudniku, namesto da bi tiho prešle na privzeto. Spremljajte uvajanje in poročajte o blokadah v [GitHub težavi #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Uporabite Azure OpenAI, ko je vaš model nameščen v Azure AI Foundry ali Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Preverjanje povezljivosti uporablja končno točko, API ključ, različico API in ime namestitve pred začetkom prevajanja.

## OpenAI

Uporabite OpenAI, ko neposredno kličete OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` je zahtevan, ker prevajalnik potrebuje eksplicitni klepetni model za API klice.

Pustite `OPENAI_ORG_ID` in `OPENAI_BASE_URL` prazni za privzeto nastavitev. Dodajte ID organizacije samo, če ga vaš račun potrebuje, ali osnovni URL le, ko uporabljate prilagojeno končno točko. Ne kopirajte nadomestnih vrednosti za opcijske nastavitve.

## Anthropic Claude

Uporabite Anthropic, ko neposredno kličete Claude API. Ustvarite [Anthropic API ključ](https://platform.claude.com/docs/en/get-started) in izberite podprt [ID modela Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` in `ANTHROPIC_MODEL` sta zahtevana. Ni vam treba nastaviti `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework je privzeti backend.

Pustite `ANTHROPIC_BASE_URL` nespremenjen za Anthropic API. Nastavite ga le, ko uporabljate prilagojeno končno točko.

`ANTHROPIC_MAX_TOKENS` privzeto znaša `8192`, kar pusti prostor za jezikovne skripte z veliko tokeni, kot je Meitei Mayek. Znižajte ga, če vaš model ali Anthropic-kompatibilna končna točka omejuje izhod pod to vrednost.

## Azure AI Vision

Prevajanje slik zahteva Azure AI Vision, da lahko orodje izvleče besedilo iz slik pred tem, ko ga prevaja konfigurirani jezikovni model. Anthropic lahko prevede izvlečeno besedilo enako kot Azure OpenAI ali OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Če je prevajanje slik izbrano z `-img`, `images=True`, ali brez filtra vrste vsebine, orodje preveri konfiguracijo Vision pred začetkom prevajanja.

## Več nizov poverilnic

Plast konfiguracije podpira več nizov poverilnic s priponami spremenljivk z istim indeksom:

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

Vsak niz mora biti popoln. Preverjanje stanja izbere delujoč niz pred nadaljevanjem prevajanja.

OpenAI in Anthropic podpirata isto konvencijo pripon. Ohranjajte vsako spremenljivko v nizu poverilnic na isti priponi, vključno z opcijskimi vrednostmi, kot sta `OPENAI_BASE_URL_1` ali `ANTHROPIC_BASE_URL_1`.

## Zahteve za ukaze

| Ukaz ali API | Potreben LLM | Potrebna Vision | Opombe |
| --- | --- | --- | --- |
| `translate -md` | Da | Ne | Prevede samo Markdown. |
| `translate -nb` | Da | Ne | Prevede samo zvezke (notebooks). |
| `translate -img` | Da | Da | Prevede samo slike. |
| `translate` brez zastavic vrste | Da | Da | Privzeti način vključuje Markdown, zvezke (notebooks) in slike. |
| `evaluate` | Da | Ne | Uporablja ocenjevanje z LLM, razen če je izbrana možnost `--fast`. |
| `migrate-links` | Ne | Ne | Izvaja lokalno migracijo povezav brez klicev ponudnika. |
| `co-op-review` | Ne | Ne | Izvede deterministične preglede strukture prevajanja, svežine, Markdowna, zvezkov in lokalnih povezav. |
| `run_translation(markdown=True)` | Da | Ne | Programsko prevajanje Markdowna. |
| `run_translation(images=True)` | Da | Da | Programsko prevajanje slik. |
| `run_review(...)` | Ne | Ne | Programski deterministični pregled. |

## Izhodne mape

Privzeti izhod besedilnega prevajanja:

```text
translations/<language-code>/<source-relative-path>
```

Privzeti izhod prevedenih slik:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API lahko prepiše te mape z `translations_dir` in `image_dir`.