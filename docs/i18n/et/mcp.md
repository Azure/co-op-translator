# MCP-server

Co-op Translator sisaldab Model Context Protocoli serverit agentidele, redaktoritele ja MCP-ühilduvatele klientidele.

Vaikimisi lokaalse seadistuse korral ei pea kasutajad eraldi serverit käsitsi käivitama. Nad konfigureerivad oma MCP-klienti, ning klient käivitab vajadusel Co-op Translatori tööriistude jaoks automaatselt `co-op-translator-mcp` kaudu `stdio`.

Kui valid CLI, Python API ja MCP vahel, alusta lehega [Vali töövoog](workflows.md).

Kasuta MCP-i, kui agent või redaktor peaks kutsuma Co-op Translatorit otse:

| Kasutaja eesmärk | MCP tööriistad |
| --- | --- |
| Tõlgi üks Markdown-dokument, märkmik või pilt | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Tõlgi Markdowni või märkmiku sisu hostagendi mudeli abil | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Ümberkirjuta tõlgitud Markdowni või märkmiku lingid pärast väljundteekonna valimist | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Tõlgi kogu repositoorium nagu CLI | `run_translation`, `translate_project` |
| Vaata üle tõlgitud väljund ilma LLM-i volitusteta | `run_review` |
| Kontrolli võimalusi ja keskkonna olekut | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP-server pakendab sama avalikku Pythoni API-d, mis on dokumenteeritud [Pythoni API](api.md). Pakkuja-toega tööriistad kasutavad samu konfigureeritud pakkujaid nagu CLI ja Python API. Agendi abistatud tööriistad valmistavad MCP hostagendile tõlkimiseks tükke, seejärel kasutavad Co-op Translatorit lõpliku Markdowni või märkmiku rekonstrueerimiseks.

## Samm 1: Paigalda ja konfigureeri Co-op Translator

Paigalda Co-op Translator Python-keskkonda, mida su MCP klient kasutab:

```bash
pip install co-op-translator
```

Lokaalse arenduse jaoks sellest repositooriumist paigalda pakett redigeeritavas režiimis:

```bash
pip install -e .
```

Vali tõlkimisrežiim, mida su MCP klient kasutab:

| Režiim | Kasuta seda | Volitused |
| --- | --- | --- |
| Pakkujapõhine | Co-op Translator kutsub `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` või `run_translation`. | Tõlkimiseks on vaja Azure OpenAI, OpenAI või Anthropic teenust. Piltide tõlkimiseks on vaja ka Azure AI Vision'i. |
| Agendi abiga | MCP hostagent tõlgib `start_markdown_agent_translation` või `start_notebook_agent_translation` tagastatud tükke. | Markdowni või märkmiku tükkide jaoks ei ole Co-op Translatori LLM-pakkuja volitusi vaja. Piltide tõlkimine ei ole agenti abiga režiimis veel toetatud. |

Kui alustad Markdowni või märkmiku tõlkimisega agendis nagu Codex või Claude Code, alusta agenti abiga režiimist. Kasuta pakkujapõhist režiimi, kui soovid, et Co-op Translator ise kutsuks konfigureeritud pakkujaid, kui tõlgid pilte või kui jooksutad repositooriumi tasandi tõlget nagu CLI.

Konfigureeri üks pakkuja pakkujapõhiste töövoogude jaoks:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Või OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Või Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Pakkujapõhine pildi tõlkimine vajab lisaks:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agendi abiga režiim katab praegu Markdowni ja märkmiku Markdown-rakke. Piltide tõlkimine kasutab endiselt pakkujapõhist pilditoru ning nõuab OCR-iks ja paigutustundlikuks renderdamiseks Azure AI Vision'i.

## Samm 2: Konfigureeri oma MCP klient

Tavalise lokaalse `stdio` seadistuse korral lisa Co-op Translator oma MCP kliendi konfiguratsiooni. Klient käivitab ja lõpetab protsessi automaatselt.

Installitud paketi konfiguratsioon:

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

Allika koopia konfiguratsioon Windowsis:

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

Allika koopia konfiguratsioon macOS-is või Linuxis:

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

Pärast MCP kliendi konfiguratsiooni muutmist taaskäivita või laadi klient uuesti, et see leiaks uue serveri.

## Samm 3: Kinnita server kliendis

Palu MCP kliendil loetleda saadaolevad tööriistad või kutsu esmalt üks lugemiseks mõeldud abivahenditest:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Kasulikud esmased kontrollid:

| Tööriist | Mida kontrollida |
| --- | --- |
| `get_api_overview` | Kinnitab, et server on ühenduv ja näitab saadaolevaid töövooge. |
| `list_supported_languages` | Kinnitab, et pakitud keeleandmeid saab laadida. |
| `get_configuration_status` | Kinnitab LLM-i ja Vision-pakkujate kättesaadavuse ilma salajasi väärtusi avaldamata. |

## Samm 4: Vali töövoog

### Tõlgi üksikuid faile või dokumente

Kasuta pakkujapõhiseid sisutööriistu, kui MCP klientil on juba dokumendi sisu või pildi tee ning Co-op Translator peaks kutsuma konfigureeritud tõlke pakkujaid.

Markdowni jaoks:

1. Kutsu `translate_markdown_content` koos `document`, `language_code` ja valikulise `source_path`-iga.
2. Kui tõlgitud tulemus kirjutatakse Co-op Translatori väljundpaigutusse, kutsu `rewrite_markdown_paths`.
3. Lase kliendil kirjutada või tagastada lõplik `content`.

Märkmike jaoks:

1. Kutsu `translate_notebook_content` koos märkmiku JSON-i ja `language_code`'iga.
2. Kutsu `rewrite_notebook_paths`, kui tõlgitud märkmiku lingid vajavad kohandumist sihtteele.
3. Kirjuta või tagasta lõplik märkmiku JSON.

Piltide jaoks:

1. Kutsu `translate_image_content` koos `image_path`, `language_code` ja valikuliste `root_dir` või `fast_mode` parameetritega.
2. Loe tagastatud `data_base64` ja `mime_type`.
3. Kui `output_path` on antud, salvestatakse tõlgitud pilt ka sellesse teele.

Sisutööriistad ei tee projekti avastamist, metaandmete uuendusi, vastutustõendeid ega automaatset teede ümberkirjutamist. Kui soovid, et hostagent tõlgiks Markdowni või märkmiku tükke ilma Co-op Translatori LLM-pakkuja volitusteta, kasuta allolevat agenti abistatud töövoogu.

### Tõlgi hostagendi mudeliga

Kasuta agenti abistatud tööriistu, kui soovid, et MCP hostagent, näiteks kodeerimisassistent, toodaks tõlgitud teksti, selle asemel et konfigureerida Co-op Translatorile LLM-pakkujat.

Vestluspõhises MCP kliendis ei pea tavaliselt tööriista JSON-i ise kirjutama. Palu agendil kasutada agenti abistatud töövoogu:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Märkmike puhul kasuta sama mustrit:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Kui su MCP klient toetab serveripõhiseid prompt'e, kasuta `agent_assisted_markdown_translation_prompt`, et klient laadiks samad töövoo juhised.

Markdowni puhul:

1. Kutsu `start_markdown_agent_translation` koos `document`, `language_code` ja valikulise `source_path`-iga.
2. Tõlgi iga tagastatud tükk hostagendis, järgides tüki `prompt`i.
3. Kutsu `finish_markdown_agent_translation` originaalse `job`-i ja tõlgitud tükkidega, kasutades `chunk_id` ja `translated_text`.
4. Kui sisu kirjutatakse tõlgitud sihtteele, kutsu `rewrite_markdown_paths`.

Märkmike puhul:

1. Kutsu `start_notebook_agent_translation` koos märkmiku JSON-i ja `language_code`'iga.
2. Tõlgi iga tagastatud tükk hostagendis.
3. Kutsu `finish_notebook_agent_translation` originaalse `job`-i ja tõlgitud tükkidega.
4. Kutsu `rewrite_notebook_paths`, kui tõlgitud märkmiku lingid vajavad sihttee kohandamist.

Agendi abiga tööriistad ei kutsu Co-op Translatorist konfigureeritud LLM-pakkujat. Hostagent vastutab tagastatud tükkide tõlkimise eest. Co-op Translator tegeleb Markdowni tükeldamise, kohatäidete säilitamise, frontmatteri rekonstrueerimise, märkmiku lahtrite asendamise ja tõlkejärgse normaliseerimisega.

### Tõlgi kogu repositoorium

Kasuta `run_translation`, kui kasutaja soovib, et Co-op Translator käituks nagu `translate` CLI.

Repositooriumi tõlkimine on vaikimisi `dry_run=true`, et agent saaks enne failimuudatusi ulatust kontrollida:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Funktsiooni `run_translation` tulemus sisaldab `events` massiivi versioonitud
`co-op.translation.event.v1` edenemisüritustega. MCP kliendid peaksid kasutama väljasid nagu
`type`, `stage_key`, `completed`, `total`, ja `current_path` asemel
konsoolteksti parsima. Anna `json_events_path`, et kirjutada need sündmused
NDJSON-faili.

Kirjutamiste lubamiseks peab kutsuja seadma nii `dry_run=false` kui `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` on esitatud ühilduvusaliasena `run_translation`-ile.

### Vaata üle tõlgitud väljund

Kasuta `run_review` deterministlikeks kontrollideks, mis ei nõua LLM- ega Vision-volitusi:

!!! note "Beta"
    MCP avaldab beetaversioonis `run_review` API. See on lugemiseks mõeldud ülevaatamise töövoogude jaoks turvaline, kuid ülevaatamise kontrollid ja probleemiskeemid võivad areneda.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Tulemus sisaldab salvestatud teksti väljundit ja struktureeritud ülevaate kokkuvõtet, kui see on saadaval.

## Käsitsi serveri käivitused

Käsitsi käivitused on peamiselt silumiseks või transpordiks, mis käituvad nagu pikaajalised serverid.

Silumise jaoks vaikimisi `stdio` server:

```bash
co-op-translator-mcp
```

Käivita allika koopiast:

```bash
python -m co_op_translator.mcp.server
```

Käivita pikaajaline HTTP- või SSE-server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Lokaalsete redaktori- ja agendi integratsioonide puhul eelistage samm 2-s klienti haldavat `stdio` konfiguratsiooni.

## Tööriistad

| Tööriist | Eesmärk | Kas kirjutab faile |
| --- | --- | --- |
| `translate_markdown_content` | Tõlgib Markdowni stringi. | Ei |
| `translate_notebook_content` | Tõlgib märkmiku JSON-i Markdown-lahtrid. | Ei |
| `translate_image_content` | Tõlgib teksti ühes pildis ja tagastab base64-pildiandmeid. | Valikuline, ainult kui `output_path` on antud |
| `start_markdown_agent_translation` | Valmistab Markdowni tükid hostagendi tõlkimiseks ilma Co-op Translator LLM volitusteta. | Ei |
| `finish_markdown_agent_translation` | Rekonstrueerib Markdowni hostagendi tõlgitud tükkidest. | Ei |
| `start_notebook_agent_translation` | Valmistab märkmiku Markdown-lahtrite tükid hostagendi tõlkimiseks. | Ei |
| `finish_notebook_agent_translation` | Rekonstrueerib märkmiku JSON-i hostagendi tõlgitud tükkidest. | Ei |
| `rewrite_markdown_paths` | Ümberkirjutab Markdowni keha ja frontmatteri teed tõlgitud sihtkoha jaoks. | Ei |
| `rewrite_notebook_paths` | Ümberkirjutab teed märkmiku Markdown-lahtrites. | Ei |
| `run_translation` | Käivita projekti tasandi tõlkimine nagu CLI. | Jah, kui `dry_run=false` ja `confirm_write=true` |
| `translate_project` | Ühilduvusalias `run_translation`-ile. | Jah, kui `dry_run=false` ja `confirm_write=true` |
| `run_review` | Käivita deterministlikud ülevaatekontrollid. | Ei |
| `get_configuration_status` | Teata konfigureeritud LLM- ja Vision-pakkujatest ilma salajasi väärtusi avaldamata. | Ei |
| `list_supported_languages` | Loetle toetatud sihtkeele koodid. | Ei |
| `get_api_overview` | Kirjeldab saadaolevaid MCP töövooge ja tööriistu. | Ei |

## Ressursid

| Resurssi URI | Eesmärk |
| --- | --- |
| `co-op://api` | Töövoogude ja tööriistade JSON-ülevaade. |
| `co-op://supported-languages` | Toetatud keelekoodide JSON-loend. |
| `co-op://configuration` | Pakkujate kättesaadavuse kokkuvõte JSON-vormingus ilma salajasteta. |

## Promptid

| Prompt | Eesmärk |
| --- | --- |
| `translate_markdown_document_prompt` | Suunab MCP klienti sisu tõlkimisel ja valikulisel teede ümberkirjutamisel. |
| `agent_assisted_markdown_translation_prompt` | Suunab MCP klienti hostagendi Markdowni tõlkimisel ilma Co-op Translatori LLM volitusteta. |
| `translate_repository_prompt` | Suunab MCP klienti repositooriumi tõlkimisel, alustades dry-run'ist. |

## Kopeeri-kleebi näited

Tõlgi Markdown sisu:

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

Ümberkirjuta tõlgitud Markdowni lingid:

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

Tõlgi Markdown hostagendi mudeliga:

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

Pärast seda, kui hostagent on tõlkinud iga tagastatud tüki, lõpeta töö täieliku `job` objektiga, mille tagastas `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Eelvaata repositooriumi tõlkimist:

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

## Tõrkeotsing

| Probleem | Mida proovida |
| --- | --- |
| MCP klient ei leia `co-op-translator-mcp`. | Kasuta absoluutset Python täitmisfaili teed ja `["-m", "co_op_translator.mcp.server"]` allika-koopiast konfiguratsiooni. |
| Server on loetletud, kuid tõlkimine ebaõnnestub. | Kutsu `get_configuration_status` ja veendu, et LLM pakkuja on saadaval. |
| Soovid Markdowni või märkmiku tõlkimist ilma pakkuja volitusteta. | Kasuta `start_markdown_agent_translation` / `finish_markdown_agent_translation` või märkmiku vastavaid funktsioone, et hostagent tõlgiks tükid. |
| Piltide tõlkimine ebaõnnestub. | Veendu, et Azure AI Vision muutujad on seadistatud ja kutsu `get_configuration_status`. |
| Repositooriumi tõlkimine ei kirjuta faile. | Sea `dry_run=false` ja `confirm_write=true` alles pärast selget kasutaja heakskiitu. |
| Muudatused kliendi konfiguratsioonis ei ilmu. | Taaskäivita või laadi MCP klient uuesti. |

## Turvanõuanded

- MCP-i tööriistakutsed on hostrakenduse mudeli kontrolli all, seetõttu on repositooriumi tõlkimine vaikimisi dry-run.
- Täielik repositooriumi tõlkimine võib luua, uuendada või eemaldada palju faile. Nõua enne `confirm_write=true` seadmist selget kasutaja heakskiitu.
- Konfiguratsiooni staatuse tööriist ei tagasta kunagi API-võtmeid, lõpp-punkte ega muid salajasi väärtusi.
- Pilditõlge tagastab base64-pildiandmeid. Suured pildid võivad tekitada suuri tööriista vastuseid.
- Agendi abiga tööriistad tagastavad allikatükid ja promptid MCP hostile. Kasuta neid ainult sisu puhul, mida kasutaja on valmis saatma sellele hostagendi mudelile.