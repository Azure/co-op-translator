# Konfiguraatio

Co-op Translator vaatii yhden kielimallitarjoajan. Kuvien kääntäminen vaatii lisäksi Azure AI Visionin.

Konfiguraatio luetaan ympäristömuuttujista. Paikallisissa projekteissa laita ne projektin juureen tiedostoon `.env`.

For Azure resource setup, see [Azure AI Setup](azure-ai-setup.md).

## Paikallinen ajonaikainen asennus

Käytä virtuaaliympäristöä ennen CLI:n ajamista paikallisesti. Co-op Translator tukee Python 3.10–3.12.

Tavalliseen CLI-käyttöön asenna julkaistu paketti virtuaaliympäristöön:

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

For repository development, install dependencies from the project root instead:

```bash
poetry install
poetry run translate --help
```

Kun CLI on käytettävissä, määritä yksi kielimallitarjoaja tiedostossa `.env`.

## Tarjoajan valinta

Työkalu tunnistaa tarjoajat automaattisesti tässä järjestyksessä:

1. Azure OpenAI
2. OpenAI

Jos kumpaakaan tarjoajaa ei ole konfiguroitu, `translate`, `evaluate`, `migrate-links` ja `run_translation` epäonnistuvat konfiguraatiotarkistuksissa. `co-op-review` ja `run_review` ovat deterministisiä ylläpitotarkistuksia eivätkä vaadi tarjoajatunnuksia.

## Azure OpenAI

Käytä Azure OpenAIta, kun mallisi on otettu käyttöön Azure AI Foundryssa tai Azure OpenAI Service -palvelussa.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Yhteyden tarkistus käyttää endpointia, API-avainta, API-versiota ja deploymentin nimeä ennen käännöksen aloittamista.

## OpenAI

Käytä OpenAI:ta kutsuttaessa OpenAI-APIa suoraan.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # valinnainen
OPENAI_BASE_URL="..."        # valinnainen
```

`OPENAI_CHAT_MODEL_ID` vaaditaan, koska kääntäjä tarvitsee eksplisiittisen chat-mallin API-kutsuja varten.

## Azure AI Vision

Kuvien kääntäminen vaatii Azure AI Visionin, jotta työkalu voi poimia tekstiä kuvista ennen niiden kääntämistä.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Jos kuvien kääntäminen on valittu `-img`:llä, `images=True`:llä tai ilman sisältötyypin suodatinta, työkalu validoi Vision-konfiguraation ennen käännöksen alkamista.

## Useita tunnussarjoja

Konfiguraatiokerros tukee useita tunnussarjoja lisäämällä muuttujien perään saman indeksin:

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

Jokaisen sarjan on oltava täydellinen. Terveystarkistus valitsee toimivan sarjan ennen kuin käännös jatkuu.

## Komentojen vaatimukset

| Komento tai API | LLM vaaditaan | Vision vaaditaan | Huomautukset |
| --- | --- | --- | --- |
| `translate -md` | Kyllä | Ei | Kääntää vain Markdownia. |
| `translate -nb` | Kyllä | Ei | Kääntää vain muistikirjoja. |
| `translate -img` | Kyllä | Kyllä | Kääntää vain kuvia. |
| `translate` ilman tyyppilippuja | Kyllä | Kyllä | Oletustila sisältää Markdownin, muistikirjat ja kuvat. |
| `evaluate` | Kyllä | Ei | Käyttää LLM-arviointia, ellei `--fast` ole valittu. |
| `migrate-links` | Kyllä | Ei | Suorittaa linkkien migraation, mutta suorittaa silti jaetut konfiguraatiotarkastukset. |
| `co-op-review` | Ei | Ei | Suorittaa deterministisiä tarkistuksia käännösrakenteesta, ajantasaisuudesta, Markdownista, muistikirjoista ja paikallisista linkeistä. |
| `run_translation(markdown=True)` | Kyllä | Ei | Ohjelmallinen Markdown-käännös. |
| `run_translation(images=True)` | Kyllä | Kyllä | Ohjelmallinen kuvien käännös. |
| `run_review(...)` | Ei | Ei | Ohjelmallinen deterministinen tarkastus. |

## Tulostuskansiot

Oletustekstinkäännöksen tulostus:

```text
translations/<language-code>/<source-relative-path>
```

Oletuskäännettyjen kuvien tulostus:

```text
translated_images/<language-code>/<source-relative-path>
```

Python-API voi yliajaa nämä hakemistot käyttämällä `translations_dir` ja `image_dir`.