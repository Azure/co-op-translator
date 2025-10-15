<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:33:34+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ro"
}
-->
# AGENTS.md

## Prezentare generală a proiectului

Co‑op Translator este un instrument Python pentru linia de comandă și un workflow GitHub Actions care traduce fișiere Markdown, notebook-uri Jupyter și text din imagini în mai multe limbi. Organizează rezultatele în foldere specifice fiecărei limbi și menține traducerile sincronizate cu conținutul sursă. Proiectul este structurat ca o bibliotecă gestionată cu Poetry, având puncte de intrare CLI.

### Prezentare generală a arhitecturii

- Punctele de intrare CLI (`translate`, `migrate-links`, `evaluate`) apelează o interfață unificată care direcționează către fluxurile de traducere, migrare de linkuri și evaluare.
- Loader-ul de configurare citește `.env` și detectează automat furnizorul LLM (Azure OpenAI sau OpenAI) și, dacă este solicitat, furnizorul de viziune (Azure AI Service) pentru extragerea textului din imagini.
- Nucleul de traducere gestionează fișiere Markdown și notebook-uri; pipeline-ul de viziune extrage textul din imagini când se folosește `-img`.
- Rezultatele sunt organizate în `translations/<lang>/` pentru text și `translated_images/` pentru imagini, păstrând structura originală.

### Tehnologii și framework-uri principale

- Python 3.10–3.12, Poetry pentru gestionarea pachetelor
- CLI: `click`
- SDK-uri LLM/AI: Azure OpenAI, OpenAI
- Viziune: Azure AI Service (Computer Vision)
- HTTP și date: `httpx`, `pydantic`
- Procesare imagini: `pillow`, `opencv-python`, `matplotlib`
- Unelte: `pytest`, `black`, `ruff`

## Comenzi de instalare

### Cerințe preliminare

- Python 3.10–3.12
- Abonament Azure (opțional, pentru serviciile Azure AI)
- Acces la internet pentru API-urile LLM/Vision (de exemplu, Azure OpenAI/OpenAI, Azure AI Vision)

### Opțiunea A: Poetry (recomandat)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Opțiunea B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## Utilizare pentru utilizatorul final

### Docker (imagine publicată)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Note:
- Punctul de intrare implicit este `translate`. Poți suprascrie cu `--entrypoint migrate-links` pentru migrarea linkurilor.
- Asigură-te că pachetul GHCR are vizibilitate Public pentru pull-uri anonime.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Configurarea mediului

Creează un fișier `.env` la rădăcina depozitului și furnizează credențiale/endpoint-uri pentru modelul lingvistic ales și (opțional) pentru serviciul de viziune. Pentru configurare specifică furnizorului, vezi `getting_started/set-up-azure-ai.md`.

### Variabile de mediu necesare

Trebuie configurat cel puțin un furnizor LLM. Pentru traducerea imaginilor, trebuie configurat și Azure AI Service.

- Azure OpenAI (traducere text):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativă pentru traducere text):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (opțional)
  - `OPENAI_CHAT_MODEL_ID` (necesar când folosești OpenAI)
  - `OPENAI_BASE_URL` (opțional; implicit `https://api.openai.com/v1`)

- Azure AI Service pentru extragerea textului din imagini (necesar când folosești `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (preferat) sau vechiul `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Exemplu de fragment `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Note:

- Instrumentul detectează automat furnizorul LLM disponibil; configurează fie Azure OpenAI, fie OpenAI.
- Traducerea imaginilor necesită atât `AZURE_AI_SERVICE_API_KEY`, cât și `AZURE_AI_SERVICE_ENDPOINT`.
- CLI-ul va afișa o eroare clară dacă lipsesc variabilele necesare.

## Flux de lucru pentru dezvoltare

- Codul sursă se află în `src/co_op_translator`; testele în `tests/`.
- CLI-urile principale (instalate prin entry points):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Vezi documentația suplimentară de utilizare în `getting_started/`.

## Instrucțiuni de testare

Rulează testele din rădăcina depozitului. Unele teste pot necesita credențiale API; sari peste ele dacă este cazul.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Acoperire opțională (necesită `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Ghid de stil pentru cod

- Formatter: Black (configurat în `pyproject.toml`, lungime linie 88)
- Linter: Ruff (configurat în `pyproject.toml`, lungime linie 120)
- Verificări de tip: mypy (configurație prezentă; activează dacă este instalat)

Comenzi:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organizează sursele Python sub `src/`, testele sub `tests/` și preferă importurile explicite în namespace-ul pachetului (`co_op_translator.*`).

## Build și publicare

Artefactele de build sunt publicate în `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatizarea prin GitHub Actions este suportată; vezi:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Imagine container (GHCR)

- Imagine oficială: `ghcr.io/azure/co-op-translator:<tag>`
- Tag-uri: `latest` (pe main), tag-uri semantice ca `vX.Y.Z` și un tag `sha`
- Multi-arch: `linux/amd64, linux/arm64` suportate prin Buildx
- Pattern Dockerfile: construiește wheel-urile de dependențe în builder (cu `build-essential` și `python3-dev`) și instalează din wheelhouse local în runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` construiește și publică pe GHCR

## Considerații de securitate

- Păstrează cheile API și endpoint-urile în `.env` sau în store-ul de secrete CI; nu le comite niciodată.
- Pentru traducerea imaginilor, sunt necesare chei/endpoint-uri Azure AI Vision; altfel omite `-img`.
- Verifică cotele/limitele furnizorului când rulezi loturi mari de traduceri.

## Ghid pentru Pull Request-uri

### Înainte de a trimite

1. **Testează modificările:**
   - Rulează complet notebook-urile afectate
   - Verifică să nu existe erori la execuția celulelor
   - Asigură-te că rezultatele sunt corecte

2. **Actualizări de documentație:**
   - Actualizează `README.md` dacă adaugi concepte noi
   - Adaugă comentarii în notebook-uri pentru cod complex
   - Asigură-te că celulele markdown explică scopul

3. **Modificări de fișiere:**
   - Evită să comiți fișiere `.env` (folosește `.env.example`)
   - Nu comite directoarele `venv/` sau `__pycache__/`
   - Păstrează output-urile notebook-urilor când demonstrează concepte
   - Șterge fișierele temporare și backup-urile de notebook-uri (`*-backup.ipynb`)

4. **Stil și formatare:**
   - Respectă ghidul de stil și formatare
   - Rulează `poetry run black .` și `poetry run ruff check .` pentru verificarea stilului și formatării

5. **Adaugă/actualizează teste și help CLI:**
   - Adaugă sau actualizează teste când schimbi comportamentul
   - Menține help-ul CLI consistent cu modificările


### Formatul mesajului de commit și strategia de merge

Folosim Squash and Merge ca implicit. Mesajul final de squash commit trebuie să urmeze:

```bash
<type>: <description> (#<PR number>)
```

Tipuri permise:
- `Docs` — actualizări de documentație
- `Build` — sistem de build, dependențe, configurare/CI
- `Core` — funcționalitate și caracteristici de bază (ex: `src/co_op_translator/core`)

Exemple:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Note:
- Titlurile PR sunt adesea prefixate automat pe baza label-urilor; verifică dacă prefixul generat este corect.

### Formatul titlului PR

Folosește titluri clare și concise. Preferă aceeași structură ca la commit-ul final squash:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging și depanare

- Probleme comune și soluții: `getting_started/troubleshooting.md`
- Limbi suportate și note (inclusiv fonturi/probleme cunoscute): `getting_started/supported-languages.md`
- Pentru probleme cu linkurile în notebook-uri, rulează din nou: `migrate-links -l "all" -y`

## Note pentru agenți

- Preferă Poetry pentru medii reproductibile; altfel folosește `requirements.txt`.
- Când rulezi CLI-uri în CI, furnizează secretele necesare prin variabile de mediu sau injectare `.env`.
- Pentru consumatorii din monorepo, acest repo funcționează ca pachet independent; nu este necesară coordonarea sub-pachetelor.

- Ghid multi-arch: păstrează `linux/arm64` când utilizatorii ARM (Apple Silicon/servere ARM) sunt vizați; altfel doar `linux/amd64` este acceptabil pentru simplitate.
- Indică utilizatorilor Docker Quick Start din `README.md` dacă preferă utilizarea containerului; include variante Bash și PowerShell din cauza diferențelor de citare.

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.