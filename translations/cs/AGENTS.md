<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:32:51+00:00",
  "source_file": "AGENTS.md",
  "language_code": "cs"
}
-->
## Přehled projektu

Co‑op Translator je nástroj v Pythonu pro příkazovou řádku a workflow pro GitHub Actions, který překládá Markdown soubory, Jupyter notebooky a text z obrázků do více jazyků. Výstupy organizuje do jazykově specifických složek a udržuje překlady synchronizované se zdrojovým obsahem. Projekt je strukturován jako knihovna spravovaná pomocí Poetry s CLI vstupními body.

### Přehled architektury

- CLI vstupní body (`translate`, `migrate-links`, `evaluate`) spouští jednotné CLI, které zajišťuje překlad, migraci odkazů a vyhodnocovací toky.
- Načítání konfigurace čte `.env` a automaticky detekuje poskytovatele LLM (Azure OpenAI nebo OpenAI) a případně poskytovatele pro zpracování obrazu (Azure AI Service) pro extrakci textu z obrázků.
- Jádro překladu zpracovává Markdown a notebooky; pipeline pro zpracování obrazu extrahuje text z obrázků při použití `-img`.
- Výstupy jsou organizovány do `translations/<lang>/` pro text a `translated_images/` pro obrázky, přičemž je zachována původní struktura.

### Klíčové technologie a frameworky

- Python 3.10–3.12, Poetry pro balíčkování
- CLI: `click`
- LLM/AI SDK: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP a data: `httpx`, `pydantic`
- Práce s obrázky: `pillow`, `opencv-python`, `matplotlib`
- Nástroje: `pytest`, `black`, `ruff`

## Příkazy pro nastavení

### Předpoklady

- Python 3.10–3.12
- Azure předplatné (volitelné, pro služby Azure AI)
- Přístup k internetu pro LLM/Vision API (např. Azure OpenAI/OpenAI, Azure AI Vision)

### Varianta A: Poetry (doporučeno)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Varianta B: pip/venv

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

## Použití pro koncové uživatele

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
- Výchozí entrypoint je `translate`. Pro migraci odkazů použijte `--entrypoint migrate-links`.
- Ujistěte se, že balíček GHCR má viditelnost Public pro anonymní stahování.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Konfigurace prostředí

Vytvořte soubor `.env` v kořenovém adresáři repozitáře a zadejte přihlašovací údaje/endpointy pro zvolený jazykový model a (volitelně) službu pro zpracování obrazu. Pro nastavení konkrétního poskytovatele viz `getting_started/set-up-azure-ai.md`.

### Požadované proměnné prostředí

Musí být nakonfigurován alespoň jeden poskytovatel LLM. Pro překlad obrázků je nutné také nastavit Azure AI Service.

- Azure OpenAI (překlad textu):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativa pro překlad textu):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (volitelné)
  - `OPENAI_CHAT_MODEL_ID` (povinné při použití OpenAI)
  - `OPENAI_BASE_URL` (volitelné; výchozí je `https://api.openai.com/v1`)

- Azure AI Service pro extrakci textu z obrázků (povinné při použití `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (preferováno) nebo starší `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Ukázka úryvku `.env`:

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

- Nástroj automaticky detekuje dostupného poskytovatele LLM; nakonfigurujte buď Azure OpenAI, nebo OpenAI.
- Překlad obrázků vyžaduje jak `AZURE_AI_SERVICE_API_KEY`, tak `AZURE_AI_SERVICE_ENDPOINT`.
- CLI vypíše jasnou chybu, pokud chybí požadované proměnné.

## Vývojový workflow

- Zdrojový kód je ve složce `src/co_op_translator`; testy ve složce `tests/`.
- Hlavní CLI (instalované přes entry points):

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

Další dokumentaci k použití najdete v `getting_started/`.

## Pokyny k testování

Testy spouštějte z kořenového adresáře repozitáře. Některé testy mohou vyžadovat API klíče; tyto testy lze přeskočit.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Volitelné měření pokrytí (vyžaduje `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Pokyny ke stylu kódu

- Formátování: Black (nastaveno v `pyproject.toml`, délka řádku 88)
- Linter: Ruff (nastaveno v `pyproject.toml`, délka řádku 120)
- Kontrola typů: mypy (konfigurace přítomna; povolte, pokud je nainstalováno)

Příkazy:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organizujte Python zdroje do `src/`, testy do `tests/` a preferujte explicitní importy v rámci balíčku (`co_op_translator.*`).

## Build a nasazení

Build artefakty jsou publikovány do `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automatizace pomocí GitHub Actions je podporována; viz:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Kontejnerový image (GHCR)

- Oficiální image: `ghcr.io/azure/co-op-translator:<tag>`
- Tagy: `latest` (na main), sémantické tagy jako `vX.Y.Z` a tag `sha`
- Multi-arch: `linux/amd64, linux/arm64` podporováno přes Buildx
- Vzor Dockerfile: build závislostí ve builderu (s `build-essential` a `python3-dev`) a instalace z lokálního wheelhouse v runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` buildí a pushuje do GHCR

## Bezpečnostní doporučení

- Uchovávejte API klíče a endpointy v `.env` nebo v úložišti tajných údajů CI; nikdy neukládejte tajné údaje do repozitáře.
- Pro překlad obrázků jsou vyžadovány klíče/endpointy Azure AI Vision; jinak vynechte `-img`.
- Při větších dávkách překladů ověřte limity/kvóty poskytovatele.

## Pokyny pro Pull Requesty

### Před odesláním

1. **Otestujte své změny:**
   - Spusťte všechny upravené notebooky celé
   - Ověřte, že všechny buňky proběhnou bez chyb
   - Zkontrolujte, že výstupy dávají smysl

2. **Aktualizace dokumentace:**
   - Aktualizujte `README.md` při přidání nových konceptů
   - Přidejte komentáře do notebooků ke složitějším částem kódu
   - Ujistěte se, že markdown buňky vysvětlují účel

3. **Změny souborů:**
   - Nezavazujte `.env` soubory (použijte `.env.example`)
   - Nezavazujte složky `venv/` nebo `__pycache__/`
   - Zachovejte výstupy v notebooku, pokud demonstrují koncepty
   - Odstraňte dočasné soubory a záložní notebooky (`*-backup.ipynb`)

4. **Styl a formátování:**
   - Dodržujte pokyny ke stylu a formátování
   - Spusťte `poetry run black .` a `poetry run ruff check .` pro kontrolu stylu a formátování

5. **Přidejte/aktualizujte testy a nápovědu CLI:**
   - Přidejte nebo aktualizujte testy při změně chování
   - Udržujte nápovědu CLI v souladu se změnami


### Formát zprávy commitu a strategie sloučení

Používáme Squash and Merge jako výchozí. Finální squash commit zpráva by měla mít formát:

```bash
<type>: <description> (#<PR number>)
```

Povolené typy:
- `Docs` — aktualizace dokumentace
- `Build` — build systém, závislosti, konfigurace/CI
- `Core` — základní funkcionalita a vlastnosti (např. `src/co_op_translator/core`)

Příklady:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Poznámky:
- Tituly PR jsou často automaticky předvyplněny podle štítků; ověřte, že generovaný prefix je správný.

### Formát názvu PR

Používejte jasné, výstižné názvy. Preferujte stejnou strukturu jako finální squash commit:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Ladění a řešení problémů

- Běžné problémy a jejich řešení: `getting_started/troubleshooting.md`
- Podporované jazyky a poznámky (včetně fontů/známých problémů): `getting_started/supported-languages.md`
- Pro problémy s odkazy v noteboocích spusťte znovu: `migrate-links -l "all" -y`

## Poznámky pro agenty

- Preferujte Poetry pro reprodukovatelné prostředí; jinak použijte `requirements.txt`.
- Při spouštění CLI v CI poskytujte potřebné tajné údaje přes proměnné prostředí nebo injekci `.env`.
- Pro monorepo spotřebitele tento repozitář funguje jako samostatný balíček; není nutná koordinace sub‑balíčků.

- Multi-arch doporučení: zachovejte `linux/arm64`, pokud cílíte na ARM uživatele (Apple Silicon/ARM servery); jinak pro jednoduchost stačí pouze `linux/amd64`.
- Uživatelům, kteří preferují kontejnery, doporučte Docker Quick Start v `README.md`; uveďte varianty pro Bash i PowerShell kvůli rozdílům v uvozovkách.

---

**Prohlášení**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.