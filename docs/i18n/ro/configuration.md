# Configurare

Co-op Translator necesită un furnizor de model lingvistic. Traducerea imaginilor necesită, în plus, Azure AI Vision.

Configurația este citită din variabilele de mediu. Pentru proiecte locale, plasați-le într-un fișier `.env` în rădăcina proiectului.

Pentru configurarea resurselor Azure, vedeți [Configurare Azure AI](azure-ai-setup.md).

## Configurare locală a runtime-ului

Utilizați un mediu virtual înainte de a rula CLI-ul local. Co-op Translator acceptă Python 3.11 până la 3.14.

Pentru utilizare normală a CLI-ului, instalați pachetul publicat în interiorul unui mediu virtual:

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

### Dezvoltare în repository

Pentru dezvoltarea repository-ului, instalați dependențele din rădăcina proiectului în schimb:

```bash
poetry install
poetry run translate --help
```

După ce CLI-ul este disponibil, configurați un furnizor de model lingvistic în `.env`.

## Selectarea furnizorului

Instrumentul detectează automat furnizorii în această ordine:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Traducerea necesită acreditările furnizorului, cu excepția previzualizărilor precum `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` și `run_review` sunt operațiuni de mentenanță deterministe și nu necesită acreditări ale furnizorului.

## Backend pentru clientul modelului

Începând cu Co-op Translator 0.22.0, Azure OpenAI, OpenAI și Anthropic folosesc implicit Microsoft Agent Framework. Nu este necesară o setare a backend-ului pentru utilizarea normală.

Semantic Kernel rămâne disponibil temporar pentru compatibilitate. Pentru a-l selecta explicit, setați:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Utilizarea Semantic Kernel emite un avertisment de deprecizare. Se planifică mutarea Semantic Kernel ca o dependență opțională în 0.23.0 și eliminarea integrării în 0.24.0, în funcție de rezultatele compatibilității și feedback-ul utilizatorilor. Anthropic necesită `agent-framework`; selectarea explicită a `semantic-kernel` împreună cu Anthropic eșuează cu o eroare de configurare. Valorile invalide cauzează eșecul la inițializarea translatorului susținut de furnizor în loc să cadă silențios înapoi. Urmăriți implementarea și raportați blocajele în [problema GitHub #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Utilizați Azure OpenAI când modelul dvs. este implementat în Azure AI Foundry sau Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Verificarea conectivității folosește endpoint-ul, cheia API, versiunea API și numele deployment-ului înainte de a începe traducerea.

## OpenAI

Utilizați OpenAI când apelați direct API-ul OpenAI.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` este necesar deoarece translatorul are nevoie de un model de chat explicit pentru apelurile API.

Lăsați `OPENAI_ORG_ID` și `OPENAI_BASE_URL` necompletate pentru configurația implicită. Adăugați un ID de organizație doar dacă contul dvs. are nevoie de unul, sau un base URL doar când folosiți un endpoint personalizat. Nu copiați valorile placeholder pentru setările opționale.

## Anthropic Claude

Utilizați Anthropic când apelați direct API-ul Claude. Creați o [cheie API Anthropic](https://platform.claude.com/docs/en/get-started) și alegeți un [ID de model Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) compatibil.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` și `ANTHROPIC_MODEL` sunt necesare. Nu trebuie să setați `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework este backend-ul implicit.

Lăsați `ANTHROPIC_BASE_URL` necompletat pentru API-ul Anthropic. Setați-l doar când folosiți un endpoint personalizat.

`ANTHROPIC_MAX_TOKENS` are ca valoare implicită `8192`, ceea ce lasă spațiu pentru scripturi dense în tokeni, cum ar fi Meitei Mayek. Reduceți-l dacă modelul dvs. sau endpoint-ul compatibil Anthropic limitează ieșirea sub aceasta.

## Azure AI Vision

Traducerea imaginilor necesită Azure AI Vision astfel încât unealta să poată extrage textul din imagini înainte ca modelul lingvistic configurat să îl traducă. Anthropic poate traduce textul extras la fel ca Azure OpenAI sau OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Dacă traducerea imaginilor este selectată cu `-img`, `images=True` sau fără un filtru de tip de conținut, unealta validează configurația Vision înainte de a începe traducerea.

## Seturi multiple de acreditări

Stratul de configurare suportă seturi multiple de acreditări prin sufixarea variabilelor cu același index:

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

Fiecare set trebuie să fie complet. Verificarea stării selectează un set funcțional înainte ca traducerea să continue.

OpenAI și Anthropic acceptă aceeași convenție de sufix. Păstrați fiecare variabilă dintr-un set de acreditări pe același sufix, inclusiv valorile opționale precum `OPENAI_BASE_URL_1` sau `ANTHROPIC_BASE_URL_1`.

## Cerințe pentru comenzi

| Comandă sau API | LLM necesar | Vision necesar | Note |
| --- | --- | --- | --- |
| `translate -md` | Da | Nu | Traduce doar Markdown. |
| `translate -nb` | Da | Nu | Traduce doar notebook-uri. |
| `translate -img` | Da | Da | Traduce doar imagini. |
| `translate` with no type flags | Da | Da | Modul implicit include Markdown, notebook-uri și imagini. |
| `evaluate` | Da | Nu | Folosește evaluare LLM cu excepția cazului în care este selectat `--fast`. |
| `migrate-links` | Nu | Nu | Efectuează migrarea link-urilor local fără apeluri către furnizor. |
| `co-op-review` | Nu | Nu | Rulează verificări deterministe ale structurii traducerii, prospețimii, Markdown-ului, notebook-urilor și link-urilor locale. |
| `run_translation(markdown=True)` | Da | Nu | Traducere Markdown programatică. |
| `run_translation(images=True)` | Da | Da | Traducere de imagini programatică. |
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