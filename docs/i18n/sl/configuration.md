# Konfiguracija

Co-op Translator zahteva enega ponudnika jezikovnega modela. Za prevod slik je poleg tega potreben Azure AI Vision.

Konfiguracija se bere iz okoljskih spremenljivk. Za lokalne projekte jih postavite v datoteko `.env` v korenu projekta.

Za nastavitev Azure virov glejte [Azure AI Setup](azure-ai-setup.md).

## Lokalna nastavitev za zagon

Uporabite virtualno okolje pred lokalnim zagonom CLI. Co-op Translator podpira Python 3.10 do 3.12.

Za normalno uporabo CLI namestite objavljen paket znotraj virtualnega okolja:

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

Za razvoj repozitorija namesto tega namestite odvisnosti iz korena projekta:

```bash
poetry install
poetry run translate --help
```

Ko je CLI na voljo, konfigurirajte enega ponudnika jezikovnega modela v `.env`.

## Izbira ponudnika

Orodje samodejno zazna ponudnike v tem vrstnem redu:

1. Azure OpenAI
2. OpenAI

Če nobeden od ponudnikov ni konfiguriran, `translate`, `evaluate`, `migrate-links` in `run_translation` ne uspejo med preverjanjem konfiguracije. `co-op-review` in `run_review` so deterministični vzdrževalni pregledi in ne zahtevajo poverilnic ponudnika.

## Azure OpenAI

Uporabite Azure OpenAI, kadar je vaš model nameščen v Azure AI Foundry ali Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Preverjanje povezave uporablja endpoint, API ključ, različico API-ja in ime razmestitve, preden se prevajanje začne.

## OpenAI

Uporabite OpenAI, kadar neposredno kličete OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # izbirno
OPENAI_BASE_URL="..."        # izbirno
```

`OPENAI_CHAT_MODEL_ID` je obvezen, ker prevajalnik za API klice potrebuje izrecen pogovorni model.

## Azure AI Vision

Prevod slik zahteva Azure AI Vision, da lahko orodje iz slik izvleče besedilo pred prevajanjem.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Če je prevod slik izbran z `-img`, `images=True` ali ni filtra vrste vsebine, orodje preveri konfiguracijo Vision pred začetkom prevajanja.

## Več naborov poverilnic

Plast konfiguracije podpira več naborov poverilnic z dodajanjem enakega indeksa kot pripone spremenljivkam:

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

Vsak nabor mora biti popoln. Preverjanje stanja izbere delujoči nabor, preden se prevajanje nadaljuje.

## Zahteve ukazov

| Ukaz ali API | Zahteva LLM | Zahteva Vision | Opombe |
| --- | --- | --- | --- |
| `translate -md` | Da | Ne | Prevaja samo Markdown. |
| `translate -nb` | Da | Ne | Prevaja samo zvezke. |
| `translate -img` | Da | Da | Prevaja samo slike. |
| `translate` with no type flags | Da | Da | Privzeti način vključuje Markdown, zvezke in slike. |
| `evaluate` | Da | Ne | Uporablja LLM ocenjevanje, razen če je izbran `--fast`. |
| `migrate-links` | Da | Ne | Izvaja migracijo povezav, vendar še vedno zažene skupne preglede konfiguracije. |
| `co-op-review` | Ne | Ne | Izvaja deterministične preglede strukture prevoda, svežine, Markdowna, zvezkov in lokalnih povezav. |
| `run_translation(markdown=True)` | Da | Ne | Programski prevod Markdowna. |
| `run_translation(images=True)` | Da | Da | Programski prevod slik. |
| `run_review(...)` | Ne | Ne | Programski deterministični pregled. |

## Izhodne mape

Privzeta izhodna mapa za besedilne prevode:

```text
translations/<language-code>/<source-relative-path>
```

Privzeta izhodna mapa za prevedene slike:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API lahko ta imenika prepiše z `translations_dir` in `image_dir`.