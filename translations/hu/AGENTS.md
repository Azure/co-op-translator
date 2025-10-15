<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:32:29+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hu"
}
-->
## Projekt áttekintés

A Co‑op Translator egy Python parancssori eszköz és GitHub Actions workflow, amely Markdown fájlokat, Jupyter notebookokat és képeken lévő szöveget fordít több nyelvre. Az eredményeket nyelv-specifikus mappákba rendezi, és folyamatosan szinkronban tartja a fordításokat az eredeti tartalommal. A projekt egy Poetry-vel kezelt könyvtárként van felépítve, CLI belépési pontokkal.

### Architektúra áttekintése

- A CLI belépési pontok (`translate`, `migrate-links`, `evaluate`) egy egységes CLI-t hívnak meg, amely a fordítási, link migrációs és értékelési folyamatokat indítja.
- A konfiguráció betöltője beolvassa a `.env` fájlt, automatikusan felismeri az LLM szolgáltatót (Azure OpenAI vagy OpenAI), és igény esetén a képfeldolgozó szolgáltatót (Azure AI Service) is, ha képszöveg kinyerés szükséges.
- A fordítási mag kezeli a Markdown-t és a notebookokat; a képfeldolgozó folyamat szöveget nyer ki a képekből, ha a `-img` opciót használjuk.
- Az eredmények a `translations/<lang>/` mappába kerülnek szöveg esetén, és a `translated_images/` mappába képek esetén, az eredeti struktúra megtartásával.

### Főbb technológiák és keretrendszerek

- Python 3.10–3.12, Poetry csomagkezeléshez
- CLI: `click`
- LLM/AI SDK-k: Azure OpenAI, OpenAI
- Képfeldolgozás: Azure AI Service (Computer Vision)
- HTTP és adatkezelés: `httpx`, `pydantic`
- Képfeldolgozás: `pillow`, `opencv-python`, `matplotlib`
- Eszközök: `pytest`, `black`, `ruff`

## Telepítési parancsok

### Előfeltételek

- Python 3.10–3.12
- Azure előfizetés (opcionális, Azure AI szolgáltatásokhoz)
- Internetkapcsolat LLM/Képfeldolgozó API-khoz (pl. Azure OpenAI/OpenAI, Azure AI Vision)

### A opció: Poetry (ajánlott)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### B opció: pip/venv

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

## Végfelhasználói használat

### Docker (publikált image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Megjegyzések:
- Az alapértelmezett belépési pont a `translate`. Link migrációhoz használja a `--entrypoint migrate-links` opciót.
- Győződjön meg róla, hogy a GHCR csomag láthatósága Publikus, hogy névtelen letöltés lehetséges legyen.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Környezeti konfiguráció

Hozzon létre egy `.env` fájlt a repozitórium gyökerében, és adja meg a választott nyelvi modellhez és (opcionálisan) képfeldolgozó szolgáltatáshoz szükséges hitelesítő adatokat/végpontokat. Szolgáltató-specifikus beállításokhoz lásd: `getting_started/set-up-azure-ai.md`.

### Szükséges környezeti változók

Legalább egy LLM szolgáltatót konfigurálni kell. Képek fordításához az Azure AI Service-t is be kell állítani.

- Azure OpenAI (szövegfordítás):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternatív szövegfordítás):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (opcionális)
  - `OPENAI_CHAT_MODEL_ID` (kötelező, ha OpenAI szolgáltatót használ)
  - `OPENAI_BASE_URL` (opcionális; alapértelmezett: `https://api.openai.com/v1`)

- Azure AI Service képszöveg kinyeréshez (kötelező, ha `-img` opciót használ):
  - `AZURE_AI_SERVICE_API_KEY` (preferált) vagy régi `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Példa `.env` részlet:

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

Megjegyzések:

- Az eszköz automatikusan felismeri az elérhető LLM szolgáltatót; konfigurálja az Azure OpenAI-t vagy az OpenAI-t.
- Képek fordításához szükséges a `AZURE_AI_SERVICE_API_KEY` és a `AZURE_AI_SERVICE_ENDPOINT`.
- A CLI egyértelmű hibát jelez, ha hiányoznak a szükséges változók.

## Fejlesztési munkafolyamat

- A forráskód a `src/co_op_translator` mappában található; a tesztek a `tests/` mappában.
- Fő CLI-k (belépési pontokon keresztül telepítve):

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

További használati dokumentáció: `getting_started/`.

## Tesztelési útmutató

A teszteket a repozitórium gyökeréből futtassa. Néhány teszthez API hitelesítő adatok szükségesek; ezeket szükség esetén hagyja ki.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Opcionális lefedettség (ehhez `coverage` szükséges):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Kódstílus irányelvek

- Formázó: Black (`pyproject.toml`-ban konfigurálva, sorhossz 88)
- Linter: Ruff (`pyproject.toml`-ban konfigurálva, sorhossz 120)
- Típusellenőrzés: mypy (konfiguráció elérhető; telepítés esetén engedélyezze)

Parancsok:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

A Python forrásokat a `src/` mappában, a teszteket a `tests/` mappában szervezze, és részesítse előnyben az explicit importokat a csomag névterén belül (`co_op_translator.*`).

## Build és kiadás

A buildelt fájlok a `dist/` mappába kerülnek.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatizálás GitHub Actions-szel támogatott; lásd:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Konténer image (GHCR)

- Hivatalos image: `ghcr.io/azure/co-op-translator:<tag>`
- Tag-ek: `latest` (main ágon), szemantikus tag-ek mint `vX.Y.Z`, és egy `sha` tag
- Multi-arch: `linux/amd64, linux/arm64` támogatott Buildx-szel
- Dockerfile minta: függőségek wheeljeinek buildelése builderben (`build-essential` és `python3-dev`), majd telepítés helyi wheelhouse-ból runtime-ban (`pip install --no-index --find-links=/wheels`)
- Munkafolyamat: `.github/workflows/docker-publish.yml` buildeli és feltölti a GHCR-re

## Biztonsági szempontok

- API kulcsokat és végpontokat tartsa `.env`-ben vagy CI titkos tárolójában; soha ne commitolja a titkokat.
- Képek fordításához Azure AI Vision kulcsok/végpontok szükségesek; ellenkező esetben hagyja ki a `-img` opciót.
- Nagy fordítási mennyiségek futtatásakor ellenőrizze a szolgáltatói kvótákat/limitációkat.

## Pull Request irányelvek

### Beküldés előtt

1. **Tesztelje a módosításokat:**
   - Futtassa végig az érintett notebookokat
   - Ellenőrizze, hogy minden cella hibamentesen fut
   - Győződjön meg róla, hogy a kimenetek megfelelőek

2. **Dokumentáció frissítése:**
   - Frissítse a `README.md`-t, ha új fogalmat ad hozzá
   - Adjon megjegyzéseket a notebookokban az összetett kódhoz
   - Biztosítsa, hogy a markdown cellák magyarázzák a célokat

3. **Fájlmódosítások:**
   - Kerülje a `.env` fájlok commitolását (használjon `.env.example`-t)
   - Ne commitolja a `venv/` vagy `__pycache__/` könyvtárakat
   - Tartsa meg a notebook kimeneteket, ha azok szemléltetnek fogalmakat
   - Távolítsa el az ideiglenes fájlokat és backup notebookokat (`*-backup.ipynb`)

4. **Stílus és formázás:**
   - Kövesse a stílus- és formázási irányelveket
   - Futtassa a `poetry run black .` és `poetry run ruff check .` parancsokat a stílus- és formázási hibák ellenőrzéséhez

5. **Teszt és CLI súgó frissítése:**
   - Adjon hozzá vagy frissítsen teszteket, ha viselkedést módosít
   - Tartsa a CLI súgót összhangban a változásokkal


### Commit üzenet és merge stratégia

Squash and Merge az alapértelmezett. A végső squash commit üzenet formátuma:

```bash
<type>: <description> (#<PR number>)
```

Engedélyezett típusok:
- `Docs` — dokumentáció frissítések
- `Build` — build rendszer, függőségek, konfiguráció/CI
- `Core` — alapvető funkcionalitás és funkciók (pl. `src/co_op_translator/core`)

Példák:
- `Docs: Telepítési útmutató frissítése érthetőségért (#50)`
- `Core: Képfeldolgozás fejlesztése (#60)`

Megjegyzések:
- A PR címek gyakran automatikusan kapnak előtagot címkék alapján; ellenőrizze, hogy a generált előtag helyes-e.

### PR cím formátuma

Használjon világos, tömör címeket. Részesítse előnyben ugyanazt a szerkezetet, mint a végső squash commit:
- `Docs: Telepítési útmutató frissítése érthetőségért`
- `Core: Képfeldolgozás fejlesztése`

## Hibakeresés és problémamegoldás

- Gyakori problémák és megoldások: `getting_started/troubleshooting.md`
- Támogatott nyelvek és megjegyzések (betűtípusok/ismert hibák): `getting_started/supported-languages.md`
- Notebookokban lévő link problémák esetén futtassa újra: `migrate-links -l "all" -y`

## Megjegyzések ügynököknek

- Használja a Poetry-t a reprodukálható környezetekhez; ellenkező esetben a `requirements.txt`-t.
- CI-ben CLI-k futtatásakor adja meg a szükséges titkokat környezeti változókkal vagy `.env` injektálással.
- Monorepo felhasználók számára ez a repo önálló csomagként működik; nincs szükség alcsomag koordinációra.

- Multi-arch útmutató: tartsa meg a `linux/arm64` támogatást, ha ARM felhasználók (Apple Silicon/ARM szerverek) célcsoport; ellenkező esetben a `linux/amd64` is elegendő egyszerűség kedvéért.
- Konténer használatot preferáló felhasználóknak mutasson a Docker Gyorsindításra a `README.md`-ben; tartalmazza a Bash és PowerShell változatokat is a különböző idézőjelek miatt.

---

**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvű változata tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.