# MCP-palvelin

Co-op Translator sisältää Model Context Protocol -palvelimen agenteille, editorseille ja MCP-yhteensopiville asiakkaille.

Oletuspaikallisessa asennuksessa käyttäjät eivät pidä erillistä palvelinta käynnissä käsin. He määrittävät MCP-asiakkaansa, ja asiakas käynnistää `co-op-translator-mcp` automaattisesti yli `stdio`n, kun se tarvitsee Co-op Translator -työkaluja.

Jos valitset CLI:n, Python-API:n ja MCP:n välillä, aloita [Valitse työnkulku](workflows.md).

Käytä MCP:tä, kun agentin tai editorin pitäisi kutsua Co-op Translatoria suoraan:

| Käyttäjän tavoite | MCP-työkalut |
| --- | --- |
| Käännä yksi Markdown-asiakirja, muistikirja tai kuva | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Käännä Markdown- tai muistikirjasisältöä isäntäagentin mallilla | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Uudelleenkirjoita käännettyjen Markdown- tai muistikirjalinkkien polut valitun kohdepolun jälkeen | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Käännä koko repositorio kuten CLI | `run_translation`, `translate_project` |
| Tarkista käännetty tulos ilman LLM-tunnuksia | `run_review` |
| Tarkastele ominaisuuksia ja ympäristön tilaa | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP-palvelin käärii saman julkisen Python-API:n, joka on dokumentoitu [Python API](api.md). Tarjoajapohjaiset työkalut käyttävät samoja konfiguroituja tarjoajia kuin CLI ja Python-API. Agenttiavusteiset työkalut valmistelevat lohkot MCP-isäntäagentin käännettäviksi ja käyttävät sitten Co-op Translatoria lopullisen Markdownin tai muistikirjan rekonstruointiin.

## Vaihe 1: Asenna ja konfiguroi Co-op Translator

Asenna Co-op Translator Python-ympäristöön, jota MCP-asiakas käyttää:

```bash
pip install co-op-translator
```

Paikallista kehitystä varten tästä repositoriosta asenna paketti muokattavaan tilaan:

```bash
pip install -e .
```

Valitse käännöstila, jota MCP-asiakkaasi käyttää:

| Tila | Käytä tähän | Tunnukset |
| --- | --- | --- |
| Tarjoajapohjainen | Co-op Translator kutsuu `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` tai `run_translation`. | Käännös vaatii Azure OpenAI:n, OpenAI:n tai Anthropicin. Kuvien käännös vaatii myös Azure AI Visionin. |
| Agenttiavusteinen | MCP-isäntäagentti kääntää lohkot, jotka palautetaan `start_markdown_agent_translation` tai `start_notebook_agent_translation`. | Co-op Translatorin LLM-tarjoajatunnuksia ei tarvita Markdown- tai muistikirjalohtkoille. Kuvien käännös ei ole vielä tuettu agenttiavusteisessa tilassa. |

Jos aloitat Markdown- tai muistikirjakäännöksillä agentin sisällä, kuten Codexilla tai Claude Codella, aloita agenttiavusteisella tilalla. Käytä tarjoajapohjaista tilaa, kun haluat Co-op Translatorin itse kutsuvan konfiguroidut tarjoajasi, kun käännät kuvia tai kun suoritat repositorion tason käännöstä kuten CLI.

Konfiguroi yksi tarjoaja tarjoajapohjaisia työnkulkuja varten:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Tai OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Tai Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Tarjoajapohjainen kuvien käännös tarvitsee lisäksi:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agenttiavusteinen tila kattaa tällä hetkellä Markdownin ja muistikirjan Markdown-solut. Kuvien käännös käyttää edelleen tarjoajapohjaista kuva-putkea ja vaatii Azure AI Visionin OCR:ää ja asettelutietoista renderöintiä.

## Vaihe 2: Konfiguroi MCP-asiakkaasi

Normaalissa paikallisessa `stdio`-asetuksessa lisää Co-op Translator MCP-asiakkaasi konfiguraatioon. Asiakas käynnistää ja pysäyttää prosessin automaattisesti.

Asennetun paketin konfiguraatio:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Lähdekoodin checkout -konfiguraatio Windowsissa:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Lähdekoodin checkout -konfiguraatio macOS:lle tai Linuxille:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

Muutettuasi MCP-asiakkaan konfiguraation, käynnistä tai lataa asiakas uudelleen, jotta se löytää uuden palvelimen.

## Vaihe 3: Varmista palvelin asiakkaassa

Pyydä MCP-asiakasta listaamaan käytettävissä olevat työkalut tai kutsu ensin jotakin vain-lukuista apuohjelmaa:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Hyödylliset ensitarkistukset:

| Työkalu | Tarkistettava asia |
| --- | --- |
| `get_api_overview` | Varmistaa, että palvelimeen saadaan yhteys ja näyttää käytettävissä olevat työnkulut. |
| `list_supported_languages` | Varmistaa, että pakatut kielitiedot voidaan ladata. |
| `get_configuration_status` | Varmistaa LLM- ja Vision-tarjoajien saatavuuden ilman salassa pidettävien arvojen paljastamista. |

## Vaihe 4: Valitse työnkulku

### Käännä yksittäisiä tiedostoja tai asiakirjoja

Käytä tarjoajapohjaisia sisältötyökaluja, kun MCP-asiakkaalla on jo asiakirjan sisältö tai kuvan polku ja Co-op Translatorin tulisi kutsua konfiguroituja kääntäjäpalveluita.

Markdownille:

1. Kutsu `translate_markdown_content` käyttäen `document`, `language_code` ja valinnaisesti `source_path`.
2. Jos käännetty tulos kirjoitetaan Co-op Translatorin tulostusasetteluun, kutsu `rewrite_markdown_paths`.
3. Anna asiakkaan kirjoittaa tai palauttaa lopullinen `content`.

Muistikirjoille:

1. Kutsu `translate_notebook_content` muistikirjan JSON:lla ja `language_code`.
2. Kutsu `rewrite_notebook_paths` jos käännettyjen muistikirjalinkkien polkuja täytyy säätää kohdepolulle.
3. Kirjoita tai palauta lopullinen muistikirjan JSON.

Kuville:

1. Kutsu `translate_image_content` käyttäen `image_path`, `language_code` ja valinnaisesti `root_dir` tai `fast_mode`.
2. Lue palautettu `data_base64` ja `mime_type`.
3. Jos `output_path` on annettu, käännetty kuva tallennetaan myös siihen polkuun.

Sisältötyökalut eivät suorita projektin etsintää, metatietojen päivityksiä, vastuuvapauslausekkeita tai automaattista polkujen uudelleenkirjoitusta. Jos haluat isäntäagentin kääntävän Markdown- tai muistikirjalohtkoja ilman Co-op Translatorin LLM-tarjoajan tunnuksia, käytä alla olevaa agenttiavusteista työnkulkua.

### Käännä isäntäagentin mallilla

Käytä agenttiavusteisia työkaluja, kun haluat MCP-isäntäagentin, kuten koodausavustajan, tuottavan käännetyn tekstin sen sijaan että konfiguroisit LLM-tarjoajan Co-op Translatorille.

Keskustelupohjaisessa MCP-asiakkaassa sinun ei yleensä tarvitse kirjoittaa työkalujen JSONia itse. Pyydä agenttia käyttämään agenttiavusteista työnkulkua:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Muistikirjoille käytä samaa kaavaa:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Jos MCP-asiakkaasi tukee palvelinpohjaisia kehotteita, käytä `agent_assisted_markdown_translation_prompt` jotta asiakas lataa samat työnkulkuohjeet.

Markdownille:

1. Kutsu `start_markdown_agent_translation` käyttäen `document`, `language_code` ja valinnaisesti `source_path`.
2. Käännä jokainen palautettu lohko isäntäagentissa noudattaen lohkon `prompt`-kehotteita.
3. Kutsu `finish_markdown_agent_translation` alkuperäisellä `job`-objektilla ja käännetyillä lohkoilla käyttäen `chunk_id` ja `translated_text`.
4. Jos sisältö kirjoitetaan käännettyyn kohdepolkuun, kutsu `rewrite_markdown_paths`.

Muistikirjoille:

1. Kutsu `start_notebook_agent_translation` muistikirjan JSONilla ja `language_code`.
2. Käännä jokainen palautettu lohko isäntäagentissa.
3. Kutsu `finish_notebook_agent_translation` alkuperäisellä `job`-objektilla ja käännetyillä lohkoilla.
4. Kutsu `rewrite_notebook_paths` jos käännettyjen muistikirjalinkkien kohdepolkuja täytyy säätää.

Agenttiavusteiset työkalut eivät kutsu Co-op Translatorin konfiguroitua LLM-tarjoajaa. Isäntäagentti vastaa palautettujen lohkojen kääntämisestä. Co-op Translator hoitaa Markdownin lohkomisen, paikkamerkkien säilyttämisen, frontmatterin rekonstruoinnin, muistikirjasolujen korvaamisen ja käännöksen jälkeisen normalisoinnin.

### Käännä koko repositorio

Käytä `run_translation` kun käyttäjä haluaa, että Co-op Translator käyttäytyy kuten `translate`-CLI.

Repositorion käännös on oletuksena `dry_run=true`, jotta agentti voi tarkistaa laajuuden ennen tiedostomuutoksia:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation`-tulos sisältää `events`-taulukon versionoiduilla
`co-op.translation.event.v1` -edistymistapahtumilla. MCP-asiakkaiden tulisi käyttää kenttiä kuten
`type`, `stage_key`, `completed`, `total` ja `current_path` sen sijaan, että
jäsennettäisiin kaapattua konsolitekstiä. Anna `json_events_path` myös kirjoittaaksesi nämä tapahtumat
NDJSON-tiedostoon.

Sallittaessa kirjoitukset, kutsujan on asetettava sekä `dry_run=false` että `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` on yhteensopivuusalias `run_translation`ille.

### Tarkista käännetty sisältö

Käytä `run_review`-toimintoa deterministisiin tarkistuksiin, jotka eivät vaadi LLM- tai Vision-tunnuksia:

!!! note "Beta"
    MCP tarjoaa beta-vaiheen `run_review`-API:n. Se on turvallinen vain-luku -tarkistustyönkuluille, mutta tarkistukset ja issue-skeemat saattavat kehittyä.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Tulos sisältää kaapatun tekstilähdön ja jäsennellyn tarkistusyhteenvedon, kun se on saatavilla.

## Manuaaliset palvelinajot

Manuaaliset ajot ovat pääasiassa virheenkorjausta tai siirtoja varten, jotka käyttäytyvät kuin pitkäkestoiset palvelimet.

Vianmääritys oletus-stdio-palvelimelle:

```bash
co-op-translator-mcp
```

Suorita lähdekooditarkastuksesta:

```bash
python -m co_op_translator.mcp.server
```

Suorita pitkäkestoinen HTTP- tai SSE-palvelin:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Paikallisissa editori- ja agenttaintegraatioissa suosittelemme asiakashallittua `stdio`-konfiguraatiota Vaiheessa 2.

## Työkalut

| Työkalu | Tarkoitus | Kirjoittaako tiedostoja |
| --- | --- | --- |
| `translate_markdown_content` | Käännä Markdown-merkkijono. | Ei |
| `translate_notebook_content` | Käännä Markdown-solut muistikirjan JSONista. | Ei |
| `translate_image_content` | Käännä tekstin yhdestä kuvasta ja palauta base64-kuvatiedot. | Valinnainen, vain kun `output_path` on annettu |
| `start_markdown_agent_translation` | Valmistelee Markdown-lohkot isäntäagentin käännettäviksi ilman Co-op Translatorin LLM-tarjoajan tunnuksia. | Ei |
| `finish_markdown_agent_translation` | Rekonstruoi Markdown isäntäagentin kääntämistä lohkoista. | Ei |
| `start_notebook_agent_translation` | Valmistelee muistikirjan Markdown-solulohkot isäntäagentin käännettäviksi. | Ei |
| `finish_notebook_agent_translation` | Rekonstruoi muistikirjan JSON isäntäagentin kääntämistä lohkoista. | Ei |
| `rewrite_markdown_paths` | Uudelleenkirjoittaa Markdown-runkoa ja frontmatter-polkuja käännetylle kohteelle. | Ei |
| `rewrite_notebook_paths` | Uudelleenkirjoittaa polkuja muistikirjan Markdown-soluissa. | Ei |
| `run_translation` | Suorita projektitason käännös kuten CLI. | Kyllä kun `dry_run=false` ja `confirm_write=true` |
| `translate_project` | Yhteensopivuusalias `run_translation`ille. | Kyllä kun `dry_run=false` ja `confirm_write=true` |
| `run_review` | Suorita deterministisiä tarkistusvaiheita. | Ei |
| `get_configuration_status` | Raportoi konfiguroidut LLM- ja Vision-tarjoajat paljastamatta salaisuuksia. | Ei |
| `list_supported_languages` | Listaa tuetut kohdekielikoodit. | Ei |
| `get_api_overview` | Kuvaa käytettävissä olevat MCP-työnkulut ja -työkalut. | Ei |

## Resurssit

| Resurssi-URI | Tarkoitus |
| --- | --- |
| `co-op://api` | JSON-yleiskatsaus työnkuluista ja työkaluista. |
| `co-op://supported-languages` | JSON-lista tuetuista kielikoodeista. |
| `co-op://configuration` | JSON-tarjoajasaatavuusyhteenveto ilman salaisuuksia. |

## Kehotteet

| Kehote | Tarkoitus |
| --- | --- |
| `translate_markdown_document_prompt` | Opastaa MCP-asiakasta sisällön käännössä sekä valinnaisessa polkujen uudelleenkirjoituksessa. |
| `agent_assisted_markdown_translation_prompt` | Opastaa MCP-asiakkaan isäntäagentin Markdown-käännöksessä ilman Co-op Translatorin LLM-tarjoajan tunnuksia. |
| `translate_repository_prompt` | Opastaa MCP-asiakasta repositorion käännössä, jossa ensin tehdään esikoeajo (dry-run). |

## Kopioi-liitä-esimerkit

Käännä Markdown-sisältö:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Uudelleenkirjoita käännetyt Markdown-linkit:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Käännä Markdown isäntäagentin mallilla:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Kun isäntäagentti kääntää jokaisen palautetun lohkon, viimeistele työ käyttämällä täydellistä `job`-objektia, jonka `start_markdown_agent_translation` palautti:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Esikatsele repositorion käännöstä:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Vianmääritys

| Ongelma | Mitä kokeilla |
| --- | --- |
| MCP-asiakas ei löydä `co-op-translator-mcp`. | Käytä absoluuttista Python-suoritettavan polkua ja `["-m", "co_op_translator.mcp.server"]` source checkout -konfiguraatiota. |
| Palvelin on listattu mutta käännös epäonnistuu. | Kutsu `get_configuration_status` ja vahvista, että LLM-tarjoaja on saatavilla. |
| Haluat Markdown- tai muistikirjakäännöksen ilman tarjoajatunnuksia. | Käytä `start_markdown_agent_translation` / `finish_markdown_agent_translation` tai muistikirjaekvivalenteja, jotta isäntäagentti kääntää lohkot. |
| Kuvien käännös epäonnistuu. | Varmista, että Azure AI Vision -muuttujat on asetettu ja kutsu `get_configuration_status`. |
| Repositorion käännös ei kirjoita tiedostoja. | Aseta `dry_run=false` ja `confirm_write=true` vain käyttäjän nimenomaisen hyväksynnän jälkeen. |
| Muutokset asiakkaan konfiguraatioon eivät näy. | Käynnistä tai lataa MCP-asiakas uudelleen. |

## Turvallisuusmuistiinpanot

- MCP-työkalukutsut ovat isäntäohjelman mallin ohjaamia, joten repositorion käännös on oletuksena dry-run.
- Koko repositorion käännös voi luoda, päivittää tai poistaa monia tiedostoja. Vaadi nimenomainen käyttäjän hyväksyntä ennen `confirm_write=true` asettamista.
- Konfiguraation tilan työkalu ei koskaan palauta API-avaimia, päätepisteitä tai muita salaisia arvoja.
- Kuvien käännös palauttaa base64-kuvatietoja. Suuret kuvat voivat tuottaa suuria työkaluvastauksia.
- Agenttiavusteiset työkalut palauttavat lähdelohtkoja ja kehotteita MCP-isännälle. Käytä niitä vain sisällön kanssa, jonka käyttäjä on valmis lähettämään tuolle isäntäagentin mallille.