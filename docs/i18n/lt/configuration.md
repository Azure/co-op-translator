# Konfigūracija

Co-op Translator reikalauja vieno kalbos modelio tiekėjo. Vaizdų vertimui papildomai reikalinga Azure AI Vision.

Konfigūracija skaitoma iš aplinkos kintamųjų. Vietiniams projektams įdėkite juos į `.env` bylą projekto šakninėje direktorijoje.

Azure išteklių nustatymui žr. [Azure AI nustatymas](azure-ai-setup.md).

## Vietinio vykdymo nustatymas

Prieš paleisdami CLI vietoje naudokite virtualią aplinką. Co-op Translator palaiko Python 3.10–3.12.

For normal CLI usage, install the published package inside a virtual environment:

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

Vystant saugyklą, vietoje įdiekite priklausomybes iš projekto šaknies:

```bash
poetry install
poetry run translate --help
```

Kai CLI bus pasiekiamas, sukonfigūruokite vieną kalbos modelio tiekėją faile `.env`.

## Tiekėjo pasirinkimas

Įrankis automatiškai aptinka tiekėjus šia tvarka:

1. Azure OpenAI
2. OpenAI

Jei nė vienas tiekėjas nėra sukonfigūruotas, `translate`, `evaluate`, `migrate-links`, ir `run_translation` nepraeis konfigūracijos patikrinimų. `co-op-review` ir `run_review` yra deterministiniai priežiūros patikrinimai ir jiems nereikia tiekėjo prisijungimo duomenų.

## Azure OpenAI

Naudokite Azure OpenAI, kai jūsų modelis diegiamas Azure AI Foundry arba Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Ryšio patikrinimas naudoja endpointą, API raktą, API versiją ir diegimo pavadinimą prieš pradedant vertimą.

## OpenAI

Naudokite OpenAI, kai tiesiogiai kreipiatės į OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # neprivalomas
OPENAI_BASE_URL="..."        # neprivalomas
```

`OPENAI_CHAT_MODEL_ID` yra privalomas, nes vertėjui API kvietimams reikia konkretaus pokalbių modelio.

## Azure AI Vision

Vaizdų vertimui reikalinga Azure AI Vision, kad įrankis galėtų išgauti tekstą iš vaizdų prieš jį verčiant.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Jei vaizdų vertimas parinktas su `-img`, `images=True`, arba nėra nustatyto content-type filtro, įrankis patikrina Vision konfigūraciją prieš pradedant vertimą.

## Kelios kredencialų rinkiniai

Konfigūracijos sluoksnis palaiko kelis kredencialų rinkinius pridedant kintamiesiems tą patį indeksą kaip priesagą:

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

Kiekvienas rinkinys turi būti pilnas. Sveikatos patikra parenka veikantį rinkinį prieš tęsiant vertimą.

## Komandų reikalavimai

| Komanda arba API | Reikalingas LLM | Reikalinga Vision | Pastabos |
| --- | --- | --- | --- |
| `translate -md` | Taip | Ne | Verčia tik Markdown. |
| `translate -nb` | Taip | Ne | Verčia tik užrašų knygeles. |
| `translate -img` | Taip | Taip | Verčia tik vaizdus. |
| `translate` with no type flags | Taip | Taip | Numatytasis režimas apima Markdown, užrašų knygeles ir vaizdus. |
| `evaluate` | Taip | Ne | Naudoja LLM vertinimą, nebent pasirenkamas `--fast`. |
| `migrate-links` | Taip | Ne | Atlieka nuorodų migraciją, bet vis tiek vykdo bendrus konfigūracijos patikrinimus. |
| `co-op-review` | Ne | Ne | Atlieka deterministinius vertimo struktūros, šviežumo, Markdown, užrašų knygelių ir vietinių nuorodų patikrinimus. |
| `run_translation(markdown=True)` | Taip | Ne | Programinis Markdown vertimas. |
| `run_translation(images=True)` | Taip | Taip | Programinis vaizdų vertimas. |
| `run_review(...)` | Ne | Ne | Programinė deterministinė peržiūra. |

## Išvedimo katalogai

Numatytoji teksto vertimo išvestis:

```text
translations/<language-code>/<source-relative-path>
```

Numatytoji išverstų vaizdų išvestis:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API gali perrašyti šiuos katalogus naudodama `translations_dir` ir `image_dir`.