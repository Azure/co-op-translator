# Konfiguraatio

Co-op Translator vaatii yhden kielimallin tarjoajan. Kuvien käännös edellyttää lisäksi Azure AI Visionia.

Konfiguraatio luetaan ympäristömuuttujista. Paikallisissa projekteissa sijoita ne projektin juureen tiedostoon `.env`.

Azure-resurssien määritystä varten katso [Azure AI -asennus](azure-ai-setup.md).

## Paikallinen suoritusaikaympäristön asennus

Käytä virtuaaliympäristöä ennen CLI:n suorittamista paikallisesti. Co-op Translator tukee Python 3.11–3.14.

Tavallista CLI-käyttöä varten asenna julkaistu paketti virtuaaliympäristöön:

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

### Repositorion kehitys

Repositorion kehitystä varten asenna riippuvuudet projektin juuresta sen sijaan:

```bash
poetry install
poetry run translate --help
```

Kun CLI on saatavilla, määritä yksi kielimallin tarjoaja tiedostossa `.env`.

## Tarjoajan valinta

Työkalu tunnistaa tarjoajat automaattisesti tässä järjestyksessä:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Käännös vaatii tarjoajan tunnistetiedot, lukuun ottamatta esikatseluja kuten `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, ja `run_review` ovat deterministisiä ylläpitotoimintoja eivätkä vaadi tarjoajan tunnistetietoja.

## Mallin asiakas-backend

Co-op Translator 0.22.0:sta alkaen Azure OpenAI, OpenAI ja Anthropic käyttävät oletuksena Microsoft Agent Frameworkia. Normaalissa käytössä backend-asetusta ei tarvita.

Semantic Kernel on toistaiseksi saatavilla yhteensopivuussyistä. Valitaksesi sen nimenomaisesti, aseta:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernelin käyttäminen aiheuttaa vanhentumisvaroituksen. Paketin on tarkoitus siirtää Semantic Kernel valinnaiseksi riippuvuudeksi versiossa 0.23.0 ja poistaa integraatio versiossa 0.24.0, riippuen yhteensopivuustuloksista ja käyttäjäpalautteesta. Anthropic vaatii `agent-framework`; `semantic-kernel` -valinnan nimenomainen käyttö Anthropicin kanssa epäonnistuu konfiguraatiovirheeseen. Virheelliset arvot epäonnistuvat tarjoajaa käyttävän kääntäjän alustuksessa sen sijaan, että ne hiljaisesti palauttaisivat oletukseen. Seuraa käyttöönottoa ja raportoi estävät tekijät [GitHub-issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Käytä Azure OpenAI:ta, kun mallisi on otettu käyttöön Azure AI Foundryssa tai Azure OpenAI -palvelussa.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Yhteyden tarkistus käyttää endpoint-osoitetta, API-avainta, API-versiota ja käyttöönoton nimeä ennen käännöksen aloittamista.

## OpenAI

Käytä OpenAI:ta, kun kutsut OpenAI-APIa suoraan.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` vaaditaan, koska kääntäjä tarvitsee selkeän chat-mallin API-kutsuja varten.

Jätä `OPENAI_ORG_ID` ja `OPENAI_BASE_URL` määrittämättä oletusasetusta varten. Lisää organisaatio-ID vain, jos tilisi sitä tarvitsee, tai base URL vain, kun käytät mukautettua päätepistettä. Älä kopioi paikkamerkkien arvoja valinnaisiin asetuksiin.

## Anthropic Claude

Käytä Anthropicia, kun kutsut Claude-APIa suoraan. Luo [Anthropic API -avain](https://platform.claude.com/docs/en/get-started) ja valitse tuettu [Claude-mallin ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` ja `ANTHROPIC_MODEL` ovat pakollisia. Sinun ei tarvitse asettaa `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework on oletustaustana.

Jätä `ANTHROPIC_BASE_URL` määrittämättä Anthropicin API:lle. Aseta se vain, kun käytät mukautettua päätepistettä.

`ANTHROPIC_MAX_TOKENS` oletusarvo on `8192`, mikä jättää tilaa tokenirikkaalle skriptikäytölle kuten Meitei Mayekille. Laske arvoa, jos mallisi tai Anthropic-yhteensopiva päätepiste rajoittaa tuottoa alle tämän.

## Azure AI Vision

Kuvien käännös vaatii Azure AI Visionin, jotta työkalu voi poimia tekstiä kuvista ennen, kuin asetettu kielimalli kääntää sen. Anthropic voi kääntää poimitun tekstin aivan kuten Azure OpenAI tai OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Jos kuvien käännös on valittu optioilla `-img`, `images=True` tai ilman sisältötyypin suodatinta, työkalu validoi Vision-konfiguraation ennen käännöksen aloittamista.

## Useita tunnistetietosarjoja

Konfiguraatiokerros tukee useita tunnistetietosarjoja lisäämällä samoja indeksejä muuttujien loppuun:

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

Jokaisen sarjan on oltava täydellinen. Terveystarkistus valitsee toimivan sarjan ennen käännöksen jatkumista.

OpenAI ja Anthropic tukevat samaa sufiksikonventiota. Pidä jokainen muuttuja tunnistetietosarjassa samalla sufiksilla, mukaan lukien valinnaiset arvot kuten `OPENAI_BASE_URL_1` tai `ANTHROPIC_BASE_URL_1`.

## Komentojen vaatimukset

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | Kyllä | Ei | Kääntää vain Markdownin. |
| `translate -nb` | Kyllä | Ei | Kääntää vain notebookit. |
| `translate -img` | Kyllä | Kyllä | Kääntää vain kuvat. |
| `translate` with no type flags | Kyllä | Kyllä | Oletustila sisältää Markdownin, notebookit ja kuvat. |
| `evaluate` | Kyllä | Ei | Käyttää LLM-arviointia, ellei valita `--fast`. |
| `migrate-links` | Ei | Ei | Suorittaa paikallisen linkkien migraation ilman tarjoajakutsuja. |
| `co-op-review` | Ei | Ei | Suorittaa deterministiset tarkistukset käännösrakenteesta, tuoreudesta, Markdownista, notebookeista ja paikallisista linkeistä. |
| `run_translation(markdown=True)` | Kyllä | Ei | Ohjelmallinen Markdown-käännös. |
| `run_translation(images=True)` | Kyllä | Kyllä | Ohjelmallinen kuvakäännös. |
| `run_review(...)` | Ei | Ei | Ohjelmallinen deterministinen tarkistus. |

## Tulostushakemistot

Oletustekstikäännöksen ulostulo:

```text
translations/<language-code>/<source-relative-path>
```

Default translated image output:

```text
translated_images/<language-code>/<source-relative-path>
```

Python-rajapinta voi ohittaa nämä hakemistot käyttämällä `translations_dir` ja `image_dir`.
