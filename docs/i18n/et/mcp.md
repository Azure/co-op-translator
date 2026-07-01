# MCP-server

Co-op Translator sisaldab Model Context Protocoli serverit agentidele, redaktoritele ja MCP-ühilduvatele klientidele.

Tavapärase kohaliku seadistuse puhul ei pea kasutajad eraldi serverit käsitsi jooksutama. Nad konfigureerivad oma MCP-kliendi ning klient käivitab `co-op-translator-mcp` automaatselt üle `stdio`, kui on vaja Co-op Translator tööriistu.

Kui otsustate CLI, Python API ja MCP vahel, alustage [Vali oma töövoog](workflows.md).

Kasutage MCP-d siis, kui agent või redaktor peaks kutsuma Co-op Translator otse:

| Kasutaja eesmärk | MCP-tööriistad |
| --- | --- |
| Tõlgi üks Markdowni dokument, märkmik või pilt | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Tõlgi Markdowni või märkmiku sisu host-agendi mudeliga | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Ümberkirjuta tõlgitud Markdowni või märkmiku lingid pärast väljundi tee valimist | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Tõlgi terve repositoorium nagu CLI | `run_translation`, `translate_project` |
| Vaadake üle tõlgitud väljund ilma LLM-õigusteta | `run_review` |
| Kontrolli võimekust ja keskkonna staatust | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP-server kapseldab samu avalikke Python API-sid, mis on dokumenteeritud [Pythoni API](api.md). Provider-toega tööriistad kasutavad samu konfigureeritud providereid nagu CLI ja Python API. Agent-assisteeritud tööriistad ette valmistavad tükkideks jagatud sisud MCP host-agendile tõlkimiseks ja seejärel kasutavad Co-op Translatorit lõpliku Markdowni või märkmiku rekonstrueerimiseks.

## Samm 1: Paigalda ja seadista Co-op Translator

Paigalda Co-op Translator Pythonikeskkonda, mida sinu MCP-kliendi seadistus kasutab:

```bash
pip install co-op-translator
```

Kohalikuks arenduseks sellest repositooriumist paigalda pakett muudetavas režiimis:

```bash
pip install -e .
```

Vali tõlkimise režiim, mida sinu MCP-kliient kasutab:

| Režiim | Kasuta seda jaoks | Volitused |
| --- | --- | --- |
| Provider-toega | Co-op Translator kutsub `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` või `run_translation`. | Markdowni ja märkmiku tõlkimiseks on vaja Azure OpenAI või OpenAI võtmeid. Pildi tõlkimiseks on lisaks vaja Azure AI Visioni. |
| Agent-assisteeritud | MCP host-agent tõlgib tükkidena tagastatud sisu, mis saadi `start_markdown_agent_translation` või `start_notebook_agent_translation` abil. | Markdowni või märkmiku tükkide jaoks ei ole Co-op Translator LLM-provideri volitusi vaja. Pildi tõlkimine ei kuulu veel agent-assisteeritud režiimi alla. |

Kui alustate Markdowni või märkmiku tõlkimisega agendi sees nagu Codex või Claude Code, alustage agent-assisteeritud režiimiga. Kasutage provider-toega režiimi, kui soovite, et Co-op Translator ise kutsuks teie konfigureeritud providereid, kui tõlgite pilte või kui jooksutate repositooriumi tasemel tõlget nagu CLI.

Konfigureerige provideri volitused ainult provider-toega töövoogude jaoks:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-toega pilditõlkimine vajab lisaks:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisteeritud režiim katab hetkel Markdowni ja märkmiku Markdowni lahtrid. Pilditõlkimine kasutab jätkuvalt provider-toega pilditoru ja nõuab OCR-iks ning paigutustundlikuks renderduseks Azure AI Visioni.

## Samm 2: Konfigureeri oma MCP-kliient

Tavalise kohaliku `stdio` seadistuse jaoks lisa Co-op Translator oma MCP-kliendi konfiguratsiooni. Klient käivitab ja lõpetab protsessi automaatselt.

Paigaldatud paketi konfiguratsioon:

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

Allikapuu konfiguratsioon Windowsis:

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

Allikapuu konfiguratsioon macOS-is või Linuxis:

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

Pärast MCP-kliendi konfiguratsiooni muutmist taaskäivitage või laadige klient uuesti, et see leiaks uue serveri.

## Samm 3: Veenduge, et server on kliendis nähtav

Paluge MCP-kliendil loetleda saadaval olevad tööriistad või kutsuda üks reast loetavatest ainult-lugemis abiabiinidest:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Kasulikud esimesed kontrollid:

| Tööriist | Mida kontrollida |
| --- | --- |
| `get_api_overview` | Kinnitus, et server on saavutatav ja näitab saadaval olevaid töövooge. |
| `list_supported_languages` | Kinnitus, et pakitud keeleandmeid saab laadida. |
| `get_configuration_status` | Kinnitus LLM- ja Vision-providerite olemasolust ilma saladusi avaldamata. |

## Samm 4: Vali töövoog

### Tõlgi üksikfaile või -dokumente

Kasuta provider-toega sisutööriistu, kui MCP-kliendil on juba dokumenti sisu või pilditee ja Co-op Translator peaks kutsuma konfigureeritud tõlkeproviderid.

Markdowni jaoks:

1. Kutsu `translate_markdown_content` koos `document`, `language_code` ja valikuliselt `source_path` parameetritega.
2. Kui tõlgitud tulemus kirjutatakse Co-op Translator väljundpaigutusse, kutsu `rewrite_markdown_paths`.
3. Lase kliendil kirjutada või tagastada lõplik `content`.

Märkmike jaoks:

1. Kutsu `translate_notebook_content` märkmiku JSON-iga ja `language_code`-ga.
2. Kutsu `rewrite_notebook_paths`, kui tõlgitud märkmiku lingid vajavad sihttee jaoks kohandamist.
3. Kirjuta või tagasta lõplik märkmiku JSON.

Piltide jaoks:

1. Kutsu `translate_image_content` koos `image_path`, `language_code` ja valikulise `root_dir` või `fast_mode` parameetriga.
2. Loe tagastatud `data_base64` ja `mime_type`.
3. Kui `output_path` on antud, salvestatakse tõlgitud pilt ka sellesse teele.

Sisutööriistad ei soorita projekti avastust, metaandmete värskendusi, vastutusi ega automaatset tee ümberkirjutamist. Kui soovite, et host-agent tõlgiks Markdowni või märkmiku tükkidena ilma Co-op Translator LLM-provideri volitusteta, kasutage allpool olevat agent-assisteeritud töövoogu.

### Tõlgi host-agendi mudeliga

Kasuta agent-assisteeritud tööriistu, kui soovite, et MCP host-agent, näiteks kodeerimisassistent, genereeriks tõlgitud teksti asemel Co-op Translatori jaoks Azure OpenAI või OpenAI seadistamist.

Vestluspõhises MCP-kliendis ei pea tavaliselt tööriista JSON-i ise kirjutama. Paluge agendil kasutada agent-assisteeritud töövoogu:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Märkmike puhul kasutage sama mustrit:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Kui teie MCP-kliendi toetab serveri prompt'e, kasutage `agent_assisted_markdown_translation_prompt`, et klient laadiks samad töövoo juhised.

Markdowni jaoks:

1. Kutsu `start_markdown_agent_translation` koos `document`, `language_code` ja valikuliselt `source_path`.
2. Tõlkige host-agendis iga tagastatud tükk, järgides tükile kuuluvaid `prompt`.
3. Kutsu `finish_markdown_agent_translation` koos originaalse `job` ja tõlgitud tükkidega, kasutades `chunk_id` ja `translated_text`.
4. Kui sisu kirjutatakse tõlgitud sihtteele, kutsu `rewrite_markdown_paths`.

Märkmike jaoks:

1. Kutsu `start_notebook_agent_translation` märkmiku JSON-iga ja `language_code`-ga.
2. Tõlkige host-agendis iga tagastatud tükk.
3. Kutsu `finish_notebook_agent_translation` koos originaalse `job` ja tõlgitud tükkidega.
4. Kutsu `rewrite_notebook_paths`, kui tõlgitud märkmiku lingid vajavad sihttee kohandamist.

Agent-assisteeritud tööriistad ei kutsu Co-op Translatorist Azure OpenAI ega OpenAI teenuseid. Host-agent vastutab tagastatud tükkide tõlkimise eest. Co-op Translator tegeleb Markdowni tükkide tegemise, kohatäidete säilitamise, frontmatteri rekonstrueerimise, märkmiku lahtri asendamise ja post-tõlke normaliseerimisega.

### Tõlgi terve repositoorium

Kasutage `run_translation`, kui kasutaja soovib, et Co-op Translator töötaks nagu `translate` CLI.

Repositooriumi tõlge on vaikimisi `dry_run=true`, et agent saaks enne failimuudatusi ulatust üle vaadata:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Kirjutamiste lubamiseks peab kutsuja määrama nii `dry_run=false` kui `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` on avalikustatud kui ühilduvusalias `run_translation` jaoks.

### Vaadake üle tõlgitud väljund

Kasutage `run_review` deterministlikeks kontrollideks, mis ei vaja LLM- või Vision-volitusi:

!!! note "Beta"
    MCP eksponeerib beetafunktsioonina `run_review` API-d. See on ohutu ainult-lugemise ülevaatus töövoogude jaoks, kuid ülevaatuse kontrollid ja probleemiskeemid võivad areneda.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Tulemus sisaldab jäädvustatud tekstiväljundit ja struktureeritud ülevaate kokkuvõtet, kui see on saadaval.

## Käsitsi serveri käivitused

Käsitsi käivitused on peamiselt silumiseks või transpordikihile, mis käitub nagu pika elueaga server.

Silumaks vaikimisi stdio-serverit:

```bash
co-op-translator-mcp
```

Käivita allikast:

```bash
python -m co_op_translator.mcp.server
```

Käivita pika elueaga HTTP või SSE server:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Kohalike redaktori- ja agendi integratsioonide jaoks eelistage Samm 2 klient-haldatut `stdio` konfiguratsiooni.

## Tööriistad

| Tööriist | Otstarve | Kas kirjutab faile |
| --- | --- | --- |
| `translate_markdown_content` | Tõlgi Markdowni string. | Ei |
| `translate_notebook_content` | Tõlgi märkmiku Markdowni lahtrid JSON-is. | Ei |
| `translate_image_content` | Tõlgi teksti ühes pildis ja tagasta base64 pildidata. | Valikuline, ainult kui `output_path` on antud |
| `start_markdown_agent_translation` | Valmista Markdowni tükid host-agendi tõlkimiseks ilma Co-op Translator LLM-volitusteta. | Ei |
| `finish_markdown_agent_translation` | Rekonstrueri Markdown host-agendi tõlgitud tükkidest. | Ei |
| `start_notebook_agent_translation` | Valmista märkmiku Markdown-lahtri tükid host-agendi tõlkimiseks. | Ei |
| `finish_notebook_agent_translation` | Rekonstrueri märkmiku JSON host-agendi tõlgitud tükkide põhjal. | Ei |
| `rewrite_markdown_paths` | Ümberkirjuta Markdowni keha ja frontmatteri teed tõlgitud sihtkoha jaoks. | Ei |
| `rewrite_notebook_paths` | Ümberkirjuta teed märkmiku Markdown-lahtrites. | Ei |
| `run_translation` | Käivita projekti-tasemeline tõlge nagu CLI. | Jah, kui `dry_run=false` ja `confirm_write=true` |
| `translate_project` | Ühilduvusalias `run_translation` jaoks. | Jah, kui `dry_run=false` ja `confirm_write=true` |
| `run_review` | Käivita deterministlikke ülevaatuse kontrolle. | Ei |
| `get_configuration_status` | Teata konfigureeritud LLM- ja Vision-provideritest ilma saladusi avaldamata. | Ei |
| `list_supported_languages` | Loetle toetatud sihtkeelekoodid. | Ei |
| `get_api_overview` | Kirjelda saadavalolevaid MCP töövooge ja tööriistu. | Ei |

## Ressursid

| Ressursi URI | Otstarve |
| --- | --- |
| `co-op://api` | JSON ülevaade töövoogudest ja tööriistadest. |
| `co-op://supported-languages` | JSON loend toetatud keelekoodidest. |
| `co-op://configuration` | JSON providerite saadavuse kokkuvõte ilma saladusteta. |

## Prompts

| Prompt | Otstarve |
| --- | --- |
| `translate_markdown_document_prompt` | Juhendab MCP-kliendi läbi sisutõlke ja valikulise tee ümberkirjutuse. |
| `agent_assisted_markdown_translation_prompt` | Juhendab MCP-kliendi läbi host-agendi Markdowni tõlke ilma Co-op Translator LLM-provideri volitusteta. |
| `translate_repository_prompt` | Juhendab MCP-kliendi läbi esmalt dry-run-põhise repositooriumi tõlke. |

## Kopeeri-kleebi näited

Tõlgi Markdowni sisu:

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

Tõlgi Markdowni host-agendi mudeliga:

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

Pärast seda, kui host-agent tõlgib iga tagastatud tüki, lõpeta töö `job` objektiga, mis tagastati `start_markdown_agent_translation` kutsest:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Eelvaade repositooriumi tõlkimisest:

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
| MCP-kliendil ei õnnestu leida `co-op-translator-mcp`. | Kasutage absoluutset Python-tõlgendi teed ja `["-m", "co_op_translator.mcp.server"]` allikapuu konfiguratsiooni. |
| Server on loetletud, kuid tõlkimine ebaõnnestub. | Kutsuge `get_configuration_status` ja kinnitage, et LLM-provider on saadaval. |
| Soovite Markdowni või märkmiku tõlget ilma Azure OpenAI/OpenAI võtmeteta. | Kasutage `start_markdown_agent_translation` / `finish_markdown_agent_translation` või vastavaid märkmiku kutsungeid, nii et host-agent tõlgib tükkidena. |
| Pilditõlkimine ebaõnnestub. | Kinnitage, et Azure AI Vision muutujad on seadistatud ja kutsuge `get_configuration_status`. |
| Repositooriumi tõlge ei kirjuta faile. | Määrake `dry_run=false` ja `confirm_write=true` alles pärast otsest kasutaja kinnitust. |
| Kliendi konfiguratsiooni muudatused ei ilmu. | Taaskäivitage või laadige MCP-kliient uuesti. |

## Turvalisuse märkused

- MCP tööriistakõned on host-rakenduse mudeli poolt juhitavad, seega on repositooriumi tõlge vaikimisi dry-run.
- Täielik repositooriumi tõlge võib luua, uuendada või eemaldada palju faile. Nõudke enne `confirm_write=true` seadistamist selget kasutaja kinnitust.
- Konfiguratsiooni staatuse tööriist ei tagasta kunagi API-võtmeid, lõppepunkti ega muid saladusi.
- Pilditõlkimine tagastab base64 pildiandmeid. Suured pildid võivad tekitada suuri tööriista vastuseid.
- Agent-assisteeritud tööriistad tagastavad algseadme tükid ja prompt'id MCP hostile. Kasutage neid ainult sisuga, mida kasutaja on nõus saatma sellele host-agendi mudelile.