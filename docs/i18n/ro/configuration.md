# Configurare

Co-op Translator necesită un singur furnizor de model lingvistic. Traducerea imaginilor necesită în plus Azure AI Vision.

Configurarea se citește din variabilele de mediu. Pentru proiecte locale, plasați-le într-un fișier `.env` la rădăcina proiectului.

Pentru configurarea resurselor Azure, vedeți [Configurare Azure AI](azure-ai-setup.md).

## Configurare locală a mediului de rulare

Folosiți un mediu virtual înainte de a rula CLI-ul local. Co-op Translator acceptă Python 3.10 până la 3.12.

Pentru utilizarea normală a CLI-ului, instalați pachetul publicat într-un mediu virtual:

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

Pentru dezvoltarea în repository, instalați dependențele din rădăcina proiectului în schimb:

```bash
poetry install
poetry run translate --help
```

După ce CLI-ul este disponibil, configurați un furnizor de model lingvistic în `.env`.

## Selectarea furnizorului

Instrumentul detectează automat furnizorii în această ordine:

1. Azure OpenAI
2. OpenAI

Dacă niciunul dintre furnizori nu este configurat, `translate`, `evaluate`, `migrate-links`, și `run_translation` eșuează în timpul verificărilor de configurare. `co-op-review` și `run_review` sunt verificări deterministe de întreținere și nu necesită acreditări de la furnizor.

## Azure OpenAI

Folosiți Azure OpenAI atunci când modelul dvs. este implementat în Azure AI Foundry sau Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Verificarea conectivității folosește endpoint-ul, cheia API, versiunea API și numele deployment-ului înainte de a începe traducerea.

## OpenAI

Folosiți OpenAI atunci când apelați API-ul OpenAI direct.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # opțional
OPENAI_BASE_URL="..."        # opțional
```

`OPENAI_CHAT_MODEL_ID` este necesar deoarece translatorul are nevoie de un model de chat explicit pentru apeluri API.

## Azure AI Vision

Traducerea imaginilor necesită Azure AI Vision astfel încât instrumentul să poată extrage textul din imagini înainte de a-l traduce.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Dacă traducerea imaginilor este selectată cu `-img`, `images=True`, sau fără filtru de tip de conținut, instrumentul validează configurația Vision înainte de începerea traducerii.

## Seturi multiple de acreditări

Stratul de configurare acceptă seturi multiple de acreditări prin sufixarea variabilelor cu același index:

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

Fiecare set trebuie să fie complet. Verificarea stării selectează un set funcțional înainte de continuarea traducerii.

## Cerințe ale comenzilor

| Comandă sau API | LLM necesar | Vision necesar | Note |
| --- | --- | --- | --- |
| `translate -md` | Da | Nu | Traduce doar Markdown. |
| `translate -nb` | Da | Nu | Traduce doar notebook-uri. |
| `translate -img` | Da | Da | Traduce doar imagini. |
| `translate` with no type flags | Da | Da | Modul implicit include Markdown, notebook-uri și imagini. |
| `evaluate` | Da | Nu | Folosește evaluarea LLM cu excepția cazului în care este selectat `--fast`. |
| `migrate-links` | Da | Nu | Efectuează migrarea linkurilor, dar tot rulează verificările comune de configurare. |
| `co-op-review` | Nu | Nu | Rulează verificări deterministe pentru structura traducerii, prospețimea conținutului, Markdown, notebook-uri și linkuri locale. |
| `run_translation(markdown=True)` | Da | Nu | Traducere Markdown programatică. |
| `run_translation(images=True)` | Da | Da | Traducere programatică a imaginilor. |
| `run_review(...)` | Nu | Nu | Revizuire deterministă programatică. |

## Directoare de ieșire

Ieșirea implicită pentru traducerea textului:

```text
translations/<language-code>/<source-relative-path>
```

Ieșirea implicită pentru imaginile traduse:

```text
translated_images/<language-code>/<source-relative-path>
```

API-ul Python poate suprascrie aceste directoare cu `translations_dir` și `image_dir`.