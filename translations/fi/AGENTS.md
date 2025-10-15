<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:29:22+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fi"
}
-->
## Projektin yleiskatsaus

Co‑op Translator on Python-komentorivityökalu ja GitHub Actions -työnkulku, joka kääntää Markdown-tiedostoja, Jupyter-muistikirjoja ja kuvien tekstiä useille kielille. Se järjestää tulokset kielikohtaisiin kansioihin ja pitää käännökset synkronoituna lähdesisällön kanssa. Projekti on rakennettu Poetry-hallittuna kirjastona, jossa on CLI-päätepisteet.

### Arkkitehtuurin yleiskuvaus

- CLI-päätepisteet (`translate`, `migrate-links`, `evaluate`) kutsuvat yhtenäistä CLI:tä, joka ohjaa käännös-, linkkien siirto- ja arviointiprosesseihin.
- Konfiguraation lataaja lukee `.env`-tiedoston ja tunnistaa automaattisesti LLM-palveluntarjoajan (Azure OpenAI tai OpenAI) sekä tarvittaessa vision-palvelun (Azure AI Service) kuvatekstin tunnistukseen.
- Käännösydin käsittelee Markdownia ja muistikirjoja; vision-putki poimii tekstiä kuvista, kun käytetään `-img`-valitsinta.
- Tulokset järjestetään kansioihin `translations/<lang>/` tekstille ja `translated_images/` kuville, alkuperäisen rakenteen säilyttäen.

### Keskeiset teknologiat ja kehykset

- Python 3.10–3.12, Poetry paketointiin
- CLI: `click`
- LLM/AI SDK:t: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP ja data: `httpx`, `pydantic`
- Kuvankäsittely: `pillow`, `opencv-python`, `matplotlib`
- Työkalut: `pytest`, `black`, `ruff`

## Asennuskomennot

### Esivaatimukset

- Python 3.10–3.12
- Azure-tilaus (valinnainen, Azure AI -palveluille)
- Internet-yhteys LLM/Vision API:lle (esim. Azure OpenAI/OpenAI, Azure AI Vision)

### Vaihtoehto A: Poetry (suositeltu)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Vaihtoehto B: pip/venv

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

## Käyttöohjeet loppukäyttäjälle

### Docker (julkaistu kuva)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Huomioita:
- Oletuspäätepiste on `translate`. Korvaa `--entrypoint migrate-links` linkkien siirtoa varten.
- Varmista, että GHCR-paketin näkyvyys on Julkinen anonyymeille latauksille.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Ympäristön konfigurointi

Luo `.env`-tiedosto projektin juureen ja lisää tunnukset/päätepisteet valitsemallesi kielimallille ja (tarvittaessa) vision-palvelulle. Palveluntarjoajakohtaiset ohjeet löytyvät tiedostosta `getting_started/set-up-azure-ai.md`.

### Vaaditut ympäristömuuttujat

Vähintään yksi LLM-palveluntarjoaja tulee olla konfiguroitu. Kuvakäännöksiin vaaditaan myös Azure AI Service.

- Azure OpenAI (tekstin käännös):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (vaihtoehtoinen tekstin käännös):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (valinnainen)
  - `OPENAI_CHAT_MODEL_ID` (vaaditaan OpenAI-palveluntarjoajalla)
  - `OPENAI_BASE_URL` (valinnainen; oletus `https://api.openai.com/v1`)

- Azure AI Service kuvatekstin tunnistukseen (vaaditaan kun käytetään `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (suositeltu) tai vanha `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Esimerkki `.env`-pätkä:

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

Huomioita:

- Työkalu tunnistaa automaattisesti käytettävissä olevan LLM-palveluntarjoajan; konfiguroi joko Azure OpenAI tai OpenAI.
- Kuvakäännös vaatii sekä `AZURE_AI_SERVICE_API_KEY` että `AZURE_AI_SERVICE_ENDPOINT`.
- CLI antaa selkeän virheen, jos vaadittuja muuttujia puuttuu.

## Kehitystyön kulku

- Lähdekoodi sijaitsee kansiossa `src/co_op_translator`; testit kansiossa `tests/`.
- Pääasialliset CLI:t (asennettu päätepisteiden kautta):

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

Lisäkäyttöohjeet löytyvät kansiosta `getting_started/`.

## Testausohjeet

Aja testit projektin juuresta. Osa testeistä saattaa vaatia API-tunnuksia; ohita ne tarvittaessa.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Valinnainen kattavuus (vaatii `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Koodityylin ohjeet

- Muotoilija: Black (`pyproject.toml`-tiedostossa, rivin pituus 88)
- Linter: Ruff (`pyproject.toml`-tiedostossa, rivin pituus 120)
- Tyyppitarkistukset: mypy (konfiguraatio löytyy; ota käyttöön jos asennettu)

Komennot:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Järjestä Python-lähteet kansioon `src/`, testit kansioon `tests/`, ja suosi eksplisiittisiä importteja paketin nimenavaruudessa (`co_op_translator.*`).

## Rakennus ja julkaisu

Rakennusartifaktit julkaistaan kansioon `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automaatio GitHub Actionsin kautta on tuettu; katso:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Konttikuva (GHCR)

- Virallinen kuva: `ghcr.io/azure/co-op-translator:<tag>`
- Tagit: `latest` (päähaara), semanttiset tagit kuten `vX.Y.Z`, sekä `sha`-tagi
- Multi-arch: `linux/amd64, linux/arm64` tuettu Buildx:llä
- Dockerfile-malli: rakenna riippuvuuksien wheelit builderissa (`build-essential` ja `python3-dev`) ja asenna ajossa paikallisesta wheelhouse:sta (`pip install --no-index --find-links=/wheels`)
- Työnkulku: `.github/workflows/docker-publish.yml` rakentaa ja pushaa GHCR:ään

## Tietoturvaohjeet

- Säilytä API-avaimet ja päätepisteet `.env`-tiedostossa tai CI:n salaisuuksissa; älä koskaan tallenna tunnuksia versionhallintaan.
- Kuvakäännöksiin vaaditaan Azure AI Vision -avaimet/päätepisteet; muuten jätä `-img` pois.
- Tarkista palveluntarjoajan kiintiöt/rajoitukset suuria käännöseriä ajaessa.

## Pull Request -ohjeet

### Ennen lähettämistä

1. **Testaa muutoksesi:**
   - Aja muokatut muistikirjat kokonaan
   - Varmista, että kaikki solut suorittuvat virheittä
   - Tarkista, että tulosteet ovat asianmukaisia

2. **Dokumentaatiopäivitykset:**
   - Päivitä `README.md`, jos lisäät uusia käsitteitä
   - Lisää kommentteja muistikirjoihin monimutkaiselle koodille
   - Varmista, että markdown-solut selittävät tarkoituksen

3. **Tiedostomuutokset:**
   - Vältä `.env`-tiedostojen tallentamista (käytä `.env.example`)
   - Älä tallenna `venv/`- tai `__pycache__/`-hakemistoja
   - Säilytä muistikirjojen tulosteet, kun ne havainnollistavat käsitteitä
   - Poista väliaikaiset tiedostot ja varmuuskopiot (`*-backup.ipynb`)

4. **Tyyli ja muotoilu:**
   - Noudata tyyli- ja muotoiluohjeita
   - Aja `poetry run black .` ja `poetry run ruff check .` tarkistaaksesi tyyli- ja muotoiluvirheet

5. **Lisää/päivitä testit ja CLI-ohjeet:**
   - Lisää tai päivitä testejä, kun muutat toiminnallisuutta
   - Pidä CLI-ohjeet ajan tasalla muutosten kanssa


### Commit-viestin ja yhdistämisen käytäntö

Käytämme oletuksena Squash and Merge -menetelmää. Lopullisen squash commit -viestin tulee noudattaa muotoa:

```bash
<type>: <description> (#<PR number>)
```

Sallitut tyypit:
- `Docs` — dokumentaatiopäivitykset
- `Build` — rakennusjärjestelmä, riippuvuudet, konfiguraatio/CI
- `Core` — ydintoiminnallisuus ja ominaisuudet (esim. `src/co_op_translator/core`)

Esimerkkejä:
- `Docs: Päivitä asennusohjeet selkeyden vuoksi (#50)`
- `Core: Paranna kuvakäännöksen käsittelyä (#60)`

Huomioita:
- PR-otsikot saavat usein automaattisen prefiksin labelien perusteella; tarkista, että generoitunut prefiksi on oikea.

### PR-otsikon muoto

Käytä selkeitä, ytimekkäitä otsikoita. Suosi samaa rakennetta kuin lopullisessa squash commitissa:
- `Docs: Päivitä asennusohjeet selkeyden vuoksi`
- `Core: Paranna kuvakäännöksen käsittelyä`

## Vianmääritys ja ongelmatilanteet

- Yleiset ongelmat ja ratkaisut: `getting_started/troubleshooting.md`
- Tuetut kielet ja huomiot (fontit/tunnetut ongelmat): `getting_started/supported-languages.md`
- Muistikirjojen linkkiongelmissa aja uudelleen: `migrate-links -l "all" -y`

## Agenttien huomioita

- Suosi Poetrya toistettavien ympäristöjen luomiseen; muuten käytä `requirements.txt`.
- Kun ajat CLI:tä CI:ssä, anna tarvittavat salaisuudet ympäristömuuttujina tai `.env`-injektiona.
- Monorepo-käyttäjille tämä repo toimii itsenäisenä pakettina; alapakettien koordinointia ei tarvita.

- Multi-arch-ohje: pidä `linux/arm64` mukana, jos ARM-käyttäjät (Apple Silicon/ARM-palvelimet) ovat kohderyhmänä; muuten pelkkä `linux/amd64` riittää yksinkertaisuuden vuoksi.
- Ohjaa käyttäjät Dockerin pika-aloitukseen `README.md`:ssä, jos he suosivat konttikäyttöä; sisällytä Bash- ja PowerShell-versiot lainausmerkkien eroavaisuuksien vuoksi.

---

**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkintavirheistä.