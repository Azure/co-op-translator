<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:33:13+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sk"
}
-->
## Prehľad projektu

Co‑op Translator je nástroj v Pythone pre príkazový riadok a workflow pre GitHub Actions, ktorý prekladá Markdown súbory, Jupyter notebooky a text z obrázkov do viacerých jazykov. Výstupy organizuje do jazykovo špecifických priečinkov a udržiava preklady synchronizované so zdrojovým obsahom. Projekt je štruktúrovaný ako knižnica spravovaná cez Poetry s CLI vstupnými bodmi.

### Prehľad architektúry

- CLI vstupné body (`translate`, `migrate-links`, `evaluate`) spúšťajú jednotné CLI, ktoré rozdeľuje úlohy na preklad, migráciu odkazov a vyhodnocovanie.
- Loader konfigurácie načítava `.env` a automaticky detekuje poskytovateľa LLM (Azure OpenAI alebo OpenAI) a, ak je to požadované, poskytovateľa pre vision (Azure AI Service) na extrakciu textu z obrázkov.
- Prekladové jadro spracováva Markdown a notebooky; vision pipeline extrahuje text z obrázkov pri použití `-img`.
- Výstupy sú organizované do `translations/<lang>/` pre text a `translated_images/` pre obrázky, pričom sa zachováva pôvodná štruktúra.

### Kľúčové technológie a frameworky

- Python 3.10–3.12, Poetry na balenie
- CLI: `click`
- LLM/AI SDK: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP a dáta: `httpx`, `pydantic`
- Práca s obrázkami: `pillow`, `opencv-python`, `matplotlib`
- Nástroje: `pytest`, `black`, `ruff`

## Príkazy na nastavenie

### Predpoklady

- Python 3.10–3.12
- Azure subscription (voliteľné, pre Azure AI služby)
- Prístup na internet pre LLM/Vision API (napr. Azure OpenAI/OpenAI, Azure AI Vision)

### Možnosť A: Poetry (odporúčané)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Možnosť B: pip/venv

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

## Použitie pre koncových používateľov

### Docker (publikovaný image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Poznámky:
- Predvolený entrypoint je `translate`. Pre migráciu odkazov použite `--entrypoint migrate-links`.
- Uistite sa, že balík GHCR je nastavený ako Public pre anonymné sťahovanie.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Konfigurácia prostredia

Vytvorte súbor `.env` v koreňovom adresári repozitára a zadajte prihlasovacie údaje/endpointy pre zvolený jazykový model a (voliteľne) vision službu. Pre nastavenie špecifické pre poskytovateľa pozrite `getting_started/set-up-azure-ai.md`.

### Požadované premenné prostredia

Aspoň jeden poskytovateľ LLM musí byť nastavený. Pre preklad obrázkov je potrebné nastaviť aj Azure AI Service.

- Azure OpenAI (preklad textu):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternatíva pre preklad textu):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (voliteľné)
  - `OPENAI_CHAT_MODEL_ID` (povinné pri použití OpenAI)
  - `OPENAI_BASE_URL` (voliteľné; predvolene `https://api.openai.com/v1`)

- Azure AI Service na extrakciu textu z obrázkov (povinné pri použití `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (preferované) alebo staršie `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Príklad úryvku `.env`:

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

Poznámky:

- Nástroj automaticky detekuje dostupného poskytovateľa LLM; nastavte buď Azure OpenAI alebo OpenAI.
- Preklad obrázkov vyžaduje oboje: `AZURE_AI_SERVICE_API_KEY` aj `AZURE_AI_SERVICE_ENDPOINT`.
- CLI zobrazí jasnú chybu, ak chýbajú požadované premenné.

## Vývojový workflow

- Zdrojový kód je v `src/co_op_translator`; testy v `tests/`.
- Hlavné CLI (inštalované cez entry points):

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

Ďalšie návody na použitie nájdete v `getting_started/`.

## Pokyny na testovanie

Testy spúšťajte z koreňa repozitára. Niektoré testy môžu vyžadovať API kľúče; tie preskočte, ak je to potrebné.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Voliteľné pokrytie (vyžaduje `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Pokyny pre štýl kódu

- Formátovanie: Black (nastavené v `pyproject.toml`, dĺžka riadku 88)
- Linter: Ruff (nastavené v `pyproject.toml`, dĺžka riadku 120)
- Kontrola typov: mypy (konfigurácia prítomná; zapnite, ak je nainštalované)

Príkazy:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organizujte Python zdroje pod `src/`, testy pod `tests/` a uprednostňujte explicitné importy v rámci balíka (`co_op_translator.*`).

## Build a nasadenie

Build artefakty sa publikujú do `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatizácia cez GitHub Actions je podporovaná; pozrite:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Kontajnerový image (GHCR)

- Oficiálny image: `ghcr.io/azure/co-op-translator:<tag>`
- Tagy: `latest` (na main), semantické tagy ako `vX.Y.Z` a tag `sha`
- Multi-arch: `linux/amd64, linux/arm64` podporované cez Buildx
- Dockerfile vzor: build závislostí vo builderi (s `build-essential` a `python3-dev`) a inštalácia z lokálneho wheelhouse v runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` buildí a pushuje do GHCR

## Bezpečnostné odporúčania

- API kľúče a endpointy uchovávajte v `.env` alebo v CI secrets store; nikdy nekomitujte tajomstvá.
- Pre preklad obrázkov sú potrebné Azure AI Vision kľúče/endpointy; inak vynechajte `-img`.
- Pri veľkých dávkach prekladov si overte kvóty/limity poskytovateľa.

## Pokyny pre Pull Requesty

### Pred odoslaním

1. **Otestujte svoje zmeny:**
   - Spustite upravené notebooky celé
   - Overte, že všetky bunky prebehnú bez chýb
   - Skontrolujte, že výstupy sú vhodné

2. **Aktualizácie dokumentácie:**
   - Aktualizujte `README.md` pri pridávaní nových konceptov
   - Pridajte komentáre do notebookov pri zložitejšom kóde
   - Uistite sa, že markdown bunky vysvetľujú účel

3. **Zmeny súborov:**
   - Nekomitujte `.env` súbory (použite `.env.example`)
   - Nekomitujte adresáre `venv/` ani `__pycache__/`
   - Zachovajte výstupy notebookov, ak demonštrujú koncepty
   - Odstráňte dočasné súbory a záložné notebooky (`*-backup.ipynb`)

4. **Štýl a formátovanie:**
   - Dodržujte pokyny pre štýl a formátovanie
   - Spustite `poetry run black .` a `poetry run ruff check .` na kontrolu štýlu a formátovania

5. **Pridajte/aktualizujte testy a CLI help:**
   - Pridajte alebo aktualizujte testy pri zmene správania
   - Udržujte CLI help v súlade so zmenami


### Formát commit message a stratégia merge

Používame Squash and Merge ako predvolené. Finálna squash commit message by mala nasledovať:

```bash
<type>: <description> (#<PR number>)
```

Povolené typy:
- `Docs` — aktualizácie dokumentácie
- `Build` — build systém, závislosti, konfigurácia/CI
- `Core` — hlavná funkcionalita a vlastnosti (napr. `src/co_op_translator/core`)

Príklady:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Poznámky:
- Tituly PR sú často automaticky prefikované podľa labelov; overte, že generovaný prefix je správny.

### Formát názvu PR

Používajte jasné, stručné názvy. Uprednostnite rovnakú štruktúru ako finálny squash commit:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Ladenie a riešenie problémov

- Bežné problémy a riešenia: `getting_started/troubleshooting.md`
- Podporované jazyky a poznámky (vrátane fontov/známych problémov): `getting_started/supported-languages.md`
- Pri problémoch s odkazmi v notebookoch spustite znova: `migrate-links -l "all" -y`

## Poznámky pre agentov

- Uprednostnite Poetry pre reprodukovateľné prostredia; inak použite `requirements.txt`.
- Pri spúšťaní CLI v CI poskytnite potrebné tajomstvá cez premenné prostredia alebo `.env` injekciu.
- Pre monorepo konzumentov tento repozitár funguje ako samostatný balík; nie je potrebná koordinácia sub‑balíkov.

- Multi-arch odporúčanie: zachovajte `linux/arm64`, ak sú cieľom ARM používatelia (Apple Silicon/ARM servery); inak je pre jednoduchosť postačujúce iba `linux/amd64`.
- Používateľov odkážte na Docker Quick Start v `README.md`, ak preferujú použitie kontajnera; zahrňte Bash aj PowerShell varianty kvôli rozdielom v úvodzovkách.

---

**Vyhlásenie o vylúčení zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj sa považuje pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.