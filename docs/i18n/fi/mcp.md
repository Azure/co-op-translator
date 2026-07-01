# MCP-palvelin

Co-op Translator sisältää Model Context Protocol -palvelimen agenteille, editoreille ja MCP-yhteensopiville asiakkaille.

Oletusarvoisessa paikallisessa asennuksessa käyttäjien ei tarvitse pitää erillistä palvelinta käynnissä käsin. He konfiguroivat MCP-asiakkaansa, ja asiakas käynnistää `co-op-translator-mcp` automaattisesti `stdio`-yhteyden yli, kun se tarvitsee Co-op Translator -työkaluja.

Jos valitset CLI:n, Python-API:n ja MCP:n välillä, aloita [Valitse työnkulku](workflows.md).

Käytä MCP:tä, kun agentin tai editorin tulisi kutsua Co-op Translatoria suoraan:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP-palvelin käärii saman julkisen Python-API:n, joka on dokumentoitu [Python API](api.md). Toimittajapohjaiset työkalut käyttävät samoja konfiguroituja tarjoajia kuin CLI ja Python-API. Agentin avustamat työkalut valmistelevat paloiksi jaetut osiot MCP-isäntäagentille käännettäväksi, ja käyttävät sitten Co-op Translatoria lopullisen Markdownin tai muistikirjan rekonstruointiin.

## Vaihe 1: Asenna ja määritä Co-op Translator

Asenna Co-op Translator Python-ympäristöön, jota MCP-asiakkaasi käyttää:

```bash
pip install co-op-translator
```

Paikallista kehitystä varten tästä repositoriosta asenna paketti muokattavassa tilassa:

```bash
pip install -e .
```

Valitse käännöstila, jota MCP-asiakkaasi käyttää:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

Jos aloitat Markdown- tai muistikirjakäännöksillä agentin, kuten Codexin tai Claude Coden, sisällä, aloita agentin avustamasta tilasta. Käytä toimittajapohjaista tilaa, kun haluat Co-op Translatorin itse kutsuvan konfiguroituja tarjoajia, kun käännät kuvia, tai kun ajat repotason käännöstä kuten CLI.

Konfiguroi tarjoajien tunnistetiedot vain toimittajapohjaisiin työnkulkuihin:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Toimittajapohjainen kuvakäännös tarvitsee lisäksi:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Vaihe 2: Määritä MCP-asiakkaasi

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

Lähdekoodin checkout -konfiguraatio macOSissa tai Linuxissa:

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

Muutettuasi MCP-asiakkaan konfiguraatiota, käynnistä tai lataa asiakas uudelleen, jotta se voi löytää uuden palvelimen.

## Vaihe 3: Varmista palvelin asiakkaassa

Pyydä MCP-asiakasta listaamaan käytettävissä olevat työkalut, tai kutsu ensin jotain luku -aputoimintoa:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Hyödyllisiä ensimmäisiä tarkistuksia:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Confirms the server is reachable and shows available workflows. |
| `list_supported_languages` | Confirms packaged language data can be loaded. |
| `get_configuration_status` | Confirms LLM and Vision provider availability without exposing secret values. |

## Vaihe 4: Valitse työnkulku

### Käännä yksittäisiä tiedostoja tai dokumentteja

Käytä toimittajapohjaisia sisältötyökaluja, kun MCP-asiakkaalla on jo dokumentin sisältö tai kuva polkuineen ja Co-op Translatorin tulisi kutsua konfiguroituja kääntäjäpalveluja.

Markdownille:

1. Kutsu `translate_markdown_content` parametrien `document`, `language_code` ja tarvittaessa `source_path` kanssa.
2. Jos käännetty tulos kirjoitetaan Co-op Translatorin tulostusasetteluun, kutsu `rewrite_markdown_paths`.
3. Anna asiakkaan kirjoittaa tai palauttaa lopullinen `content`.

Muistikirjoille:

1. Kutsu `translate_notebook_content` muistikirjan JSONilla ja `language_code`-parametrilla.
2. Kutsu `rewrite_notebook_paths`, jos käännettyjen muistikirjalinkkien polkuja täytyy säätää kohdepolkua varten.
3. Kirjoita tai palauta lopullinen muistikirja-JSON.

Kuville:

1. Kutsu `translate_image_content` parametrien `image_path`, `language_code` ja valinnaisesti `root_dir` tai `fast_mode` kanssa.
2. Lue palautettu `data_base64` ja `mime_type`.
3. Jos `output_path` on annettu, käännetty kuva tallennetaan myös siihen polkuun.

Sisältötyökalut eivät suorita projektin löytöä, metatietojen päivityksiä, vastuuvapauslausekkeita tai automaattista polun uudelleenkirjoitusta. Jos haluat isäntäagentin kääntävän Markdown- tai muistikirjajohtoiset palat ilman Co-op Translatorin LLM-tarjoajatunnuksia, käytä alla olevaa agentin avustamaa työnkulkua.

### Käännä isäntäagentin mallilla

Käytä agentin avustamia työkaluja, kun haluat MCP-isäntäagentin, kuten koodausavustajan, tuottavan käännetyn tekstin sen sijaan, että konfiguroisit Azure OpenAI:n tai OpenAI:n Co-op Translatorille.

Chat-pohjaisessa MCP-asiakkaassa sinun ei yleensä tarvitse kirjoittaa työkalun JSONia itse. Pyydä agenttia käyttämään agentin avustamaa työnkulkua:

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

Jos MCP-asiakkaasi tukee palvelinkehotteita, käytä `agent_assisted_markdown_translation_prompt`-kehotetta, jotta asiakas lataa samat työnkulkuohjeet.

Markdownille:

1. Kutsu `start_markdown_agent_translation` parametrien `document`, `language_code` ja tarvittaessa `source_path` kanssa.
2. Käännä jokainen palautettu pala isäntäagentissa seuraamalla palan `prompt`-ohjeita.
3. Kutsu `finish_markdown_agent_translation` alkuperäisen `job`-objektin ja käännettyjen palojen kanssa käyttäen `chunk_id` ja `translated_text`.
4. Jos sisältö kirjoitetaan käännettyyn kohdepolkuun, kutsu `rewrite_markdown_paths`.

Muistikirjoille:

1. Kutsu `start_notebook_agent_translation` muistikirjan JSONilla ja `language_code`-parametrilla.
2. Käännä jokainen palautettu pala isäntäagentissa.
3. Kutsu `finish_notebook_agent_translation` alkuperäisen `job`-objektin ja käännettyjen palojen kanssa.
4. Kutsu `rewrite_notebook_paths`, jos käännettyjen muistikirjalinkkien polkuja täytyy säätää kohdepolkua varten.

Agentin avustamat työkalut eivät kutsu Azure OpenAI:ta tai OpenAI:a Co-op Translatorista. Isäntäagentti vastaa palautettujen palojen kääntämisestä. Co-op Translator hoitaa Markdownin paloittelun, paikkamerkkien säilyttämisen, frontmatterin rekonstruoinnin, muistikirjasolujen korvaamisen ja jälkikäännöksen normalisoinnin.

### Käännä koko arkisto

Käytä `run_translation`, kun käyttäjä haluaa Co-op Translatorin toimivan kuten `translate`-CLI.

Arkiston käännös oletusarvoisesti käyttää `dry_run=true`, jotta agentti voi tarkastella laajuutta ennen tiedostomuutoksia:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Sallitaaksesi kirjoitukset, kutsujan on asetettava sekä `dry_run=false` että `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` on altistettu yhteensopivuusalias `run_translation`ille.

### Tarkista käännetty tulos

Käytä `run_review` deterministisille tarkistuksille, jotka eivät vaadi LLM- tai Vision-tunnuksia:

!!! note "Beta"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Tulos sisältää kaapatun tekstitulosteen ja rakenteellisen tarkistusyhteenvedon, kun saatavilla.

## Manuaaliset palvelinajot

Manuaaliset ajot ovat pääasiassa virheenkorjausta tai siirtoja varten, jotka toimivat kuin pitkäkestoiset palvelimet.

Debuggaa oletusarvoinen stdio-palvelin:

```bash
co-op-translator-mcp
```

Aja lähdekoodin checkoutista:

```bash
python -m co_op_translator.mcp.server
```

Aja pitkäikäinen HTTP- tai SSE-palvelin:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Paikallisia editori- ja agentti-integraatioita varten suosittelemme vaiheessa 2 kuvattua asiakashallittua `stdio`-konfiguraatiota.

## Työkalut

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | No |
| `translate_image_content` | Translate text in one image and return base64 image data. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Prepare Markdown chunks for the host agent to translate without Co-op Translator LLM credentials. | No |
| `finish_markdown_agent_translation` | Reconstruct Markdown from host-agent translated chunks. | No |
| `start_notebook_agent_translation` | Prepare notebook Markdown-cell chunks for the host agent to translate. | No |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON from host-agent translated chunks. | No |
| `rewrite_markdown_paths` | Rewrite Markdown body and frontmatter paths for a translated target. | No |
| `rewrite_notebook_paths` | Rewrite paths inside notebook Markdown cells. | No |
| `run_translation` | Run project-level translation like the CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Report configured LLM and Vision providers without exposing secrets. | No |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Describe available MCP workflows and tools. | No |

## Resurssit

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Kehotukset

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Kopioi-liitä esimerkit

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
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

Kun isäntäagentti kääntää jokaisen palautetun palan, viimeistele työ kutsumalla `start_markdown_agent_translation`in palauttamalla täydellä `job`-objektilla:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Esikatsele arkiston käännöstä:

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

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Turvallisuusmuistiinpanot

- MCP-työkalukutsut ovat isäntäapplikaation mallin hallinnoimia, joten arkiston käännös on oletusarvoisesti dry-run.
- Täydellinen arkiston käännös voi luoda, päivittää tai poistaa monia tiedostoja. Vaadi nimenomainen käyttäjän hyväksyntä ennen `confirm_write=true` asettamista.
- Konfiguraation tilatyökalu ei koskaan palauta API-avaimia, päätepisteitä tai muita salaisia arvoja.
- Kuvakäännös palauttaa base64-kuvatietoja. Suuret kuvat voivat tuottaa suuria työkaluvastauksia.
- Agentin avustamat työkalut palauttavat lähdepalat ja kehotteet MCP-isännälle. Käytä niitä vain sisällön kanssa, jonka käyttäjä on valmis lähettämään kyseiselle isäntäagentin mallille.