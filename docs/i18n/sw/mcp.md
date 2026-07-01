# MCP Server

Co-op Translator inajumuisha seva ya Model Context Protocol kwa maajenti, wahariri, na wateja wanaolingana na MCP.

Kwa usanidi wa eneo-mbali wa chaguo-msingi, watumiaji hawana kuendesha seva tofauti kwa mkono. Wanapanga mteja wao wa MCP, na mteja huanzisha `co-op-translator-mcp` moja kwa moja kupitia `stdio` wanapohitaji zana za Co-op Translator.

Ikiwa unatafakari kati ya CLI, Python API, na MCP, anza na [Choose Your Workflow](workflows.md).

Tumia MCP wakati maajenti au mhariri inapaswa kumwita Co-op Translator moja kwa moja:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Seva ya MCP inajifunika API ya umma ya Python iliyoandikwa katika [Python API](api.md). Zana zinazotegemea muuzaji hutumia muuzaji aliyosanidiwa kama CLI na Python API. Zana zinazosaidiwa na maajenti huandaa vipande kwa mjuu wa mwenyeji wa MCP kutafsiri, kisha hutumia Co-op Translator kujenga tena Markdown au daftari la mwisho.

## Step 1: Install and Configure Co-op Translator

Sakinisha Co-op Translator katika mazingira ya Python ambayo mteja wako wa MCP atatumia:

```bash
pip install co-op-translator
```

Kwa maendeleo ya eneo-mbali kutoka kwenye hifadhidata hii, sakinisha kifurushi katika modi ya kuhariri:

```bash
pip install -e .
```

Chagua mode ya tafsiri ambayo mteja wako wa MCP atatumia:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator inaita `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, au `run_translation`. | Tafsiri ya Markdown na daftari la kumbukumbu inahitaji Azure OpenAI au OpenAI. Tafsiri ya picha pia inahitaji Azure AI Vision. |
| Agent-assisted | Mjuu mwenyeji wa MCP anatafsiri vipande vinavyorejeshwa na `start_markdown_agent_translation` au `start_notebook_agent_translation`. | Hakuna nyaraka za muuzaji za LLM za Co-op Translator zinahitajika kwa vipande vya Markdown au daftari la kumbukumbu. Tafsiri ya picha bado haijaunganika na mode ya msaada wa maajenti. |

Ikiwa unaanza na tafsiri ya Markdown au daftari la kumbukumbu ndani ya mjuu kama Codex au Claude Code, anza na mode ya msaada wa maajenti. Tumia mode ya provider-backed wakati ungependa Co-op Translator yenyewe iite muuzaji ulio sanidiwa, unapohitaji kutafsiri picha, au unapofanya tafsiri ya kiwango cha hifadhidata kama CLI.

Sanidi nyaraka za muuzaji kwa ajili ya workflows zinazotegemea muuzaji pekee:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Tafsiri ya picha inayotegemea muuzaji inahitaji pia:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Step 2: Configure Your MCP Client

Kwa usanidi wa kawaida wa eneo-mbali `stdio`, ongeza Co-op Translator kwenye usanidi wa mteja wako wa MCP. Mteja ataendesha na kuacha mchakato moja kwa moja.

Usanidi wa kifurushi kilichoinstaliwa:

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

Usanidi wa chanzo kilichopakuliwa kwenye Windows:

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

Usanidi wa chanzo kilichopakuliwa kwenye macOS au Linux:

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

Baada ya kubadilisha usanidi wa mteja wa MCP, anzisha tena au upakishe upya mteja ili uweze kugundua seva mpya.

## Step 3: Verify the Server in the Client

Waambie mteja wa MCP orodheshe zana zinazopatikana, au ita moja ya viongezi vya kusoma tu kwanza:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Vipimo vya awali vinavyofaa:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Inathibitisha kuwa seva inafikiwa na inaonyesha workflows zinazopatikana. |
| `list_supported_languages` | Inathibitisha kuwa data ya lugha iliyopakiwa inaweza kupakuliwa. |
| `get_configuration_status` | Inathibitisha upatikanaji wa muuzaji wa LLM na Vision bila kufichua thamani za siri. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

Tumia zana za yaliyomo zinazotegemea muuzaji wakati mteja wa MCP tayari ana yaliyomo ya nyaraka au njia ya picha na Co-op Translator inapaswa kuitwa na waajiri waliowekwa.

Kwa Markdown:

1. Ita `translate_markdown_content` na `document`, `language_code`, na hiari `source_path`.
2. Ikiwa matokeo yaliyotafsiriwa yataandikwa ndani ya mpangilio wa pato wa Co-op Translator, ita `rewrite_markdown_paths`.
3. Mteja aendelee kuandika au kurudisha `content` ya mwisho.

Kwa daftari la kumbukumbu:

1. Ita `translate_notebook_content` na JSON ya daftari la kumbukumbu na `language_code`.
2. Ita `rewrite_notebook_paths` ikiwa viungo vya daftari yaliyotafsiriwa vinahitaji kurekebishwa kwa njia ya lengo.
3. Andika au rudisha JSON ya daftari la kumbukumbu ya mwisho.

Kwa picha:

1. Ita `translate_image_content` na `image_path`, `language_code`, na hiari `root_dir` au `fast_mode`.
2. Soma `data_base64` na `mime_type` iliyorejeshwa.
3. Ikiwa `output_path` imetolewa, picha iliyotafsiriwa pia imehifadhiwa kwenye njia hiyo.

Zana za yaliyomo hazifanyi ugunduzi wa mradi, masasisho ya metadata, maonyo, au urekebishaji wa njia moja kwa moja. Ikiwa unataka mjuu mwenyeji atafsiri vipande vya Markdown au daftari bila nyaraka za muuzaji za LLM za Co-op Translator, tumia workflow inayosaidiwa na maajenti iliyo hapa chini.

### Translate with the Host Agent Model

Tumia zana zinazosaidiwa na maajenti wakati ungependa mjuu mwenyeji wa MCP, kama msaidizi wa kuandika msimbo, azalisha maandishi yaliyotafsiriwa badala ya kusanidi Azure OpenAI au OpenAI kwa Co-op Translator.

Katika mteja wa MCP unaotegemea mazungumzo, kawaida huna haja ya kuandika JSON ya zana yako mwenyewe. Muulize mjuu atumie workflow inayosaidiwa na maajenti:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Kwa daftari la kumbukumbu, tumia mfano ule ule:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ikiwa mteja wako wa MCP unaunga mkono maelekezo ya seva, tumia `agent_assisted_markdown_translation_prompt` ili mteja apakue maagizo ya workflow yale yale.

Kwa Markdown:

1. Ita `start_markdown_agent_translation` na `document`, `language_code`, na hiari `source_path`.
2. Tafsiri kila kipande kilichorejeshwa katika mjuu mwenyeji kwa kufuata `prompt` ya kipande.
3. Ita `finish_markdown_agent_translation` na `job` asilia na vipande vilivyotafsiriwa kwa kutumia `chunk_id` na `translated_text`.
4. Ikiwa yaliyomo yataandikwa kwenye njia ya lengo iliyotafsiriwa, ita `rewrite_markdown_paths`.

Kwa daftari la kumbukumbu:

1. Ita `start_notebook_agent_translation` na JSON ya daftari la kumbukumbu na `language_code`.
2. Tafsiri kila kipande kilichorejeshwa katika mjuu mwenyeji.
3. Ita `finish_notebook_agent_translation` na `job` asilia na vipande vilivyotafsiriwa.
4. Ita `rewrite_notebook_paths` ikiwa viungo vya daftari yaliyotafsiriwa vinahitaji kurekebishwa kwa njia ya lengo.

Zana zinazosaidiwa na maajenti hazitawita Azure OpenAI au OpenAI kutoka kwa Co-op Translator. Mjuu mwenyeji ndiye anayehusika kutafsiri vipande vilivyorejeshwa. Co-op Translator hushughulikia kugawanya Markdown, uhifadhi wa vichwa-vifupisho, ujenzi upya wa frontmatter, kubadilisha seli za daftari, na usawa baada ya tafsiri.

### Translate an Entire Repository

Tumia `run_translation` wakati mtumiaji anataka Co-op Translator ijitendee kama CLI `translate`.

Tafsiri ya hifadhidata ina chaguo-msingi `dry_run=true` ili mjuu aweze kukagua upeo kabla ya mabadiliko ya faili:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Ili kuruhusu kuandika, mpiga simu lazima aweke mbili `dry_run=false` na `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` imetolewa kama jina la utangamano kwa `run_translation`.

### Review Translated Output

Tumia `run_review` kwa ukaguzi thabiti ambao hauhitaji nyaraka za LLM au Vision:

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

Matokeo yanajumuisha matokeo ya maandishi yaliyorekodiwa na muhtasari wa ukaguzi uliopangwa wakati upo.

## Manual Server Runs

Mizunguko kwa mkono ni kwa kawaida kwa debugging au kwa usafirishaji unaotendeka kama seva zinazodumu.

Fanya debugging ya seva ya stdio ya chaguo-msingi:

```bash
co-op-translator-mcp
```

Endesha kutoka kwenye chanzo kilichopakuliwa:

```bash
python -m co_op_translator.mcp.server
```

Endesha seva ya HTTP au SSE inayodumu kwa muda mrefu:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Kwa ujumuishaji wa mhariri wa eneo-mbali na maajenti, pendelea usanidi wa `stdio` unaosimamiwa na mteja katika Hatua ya 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Tafsiri kamba (string) ya Markdown. | No |
| `translate_notebook_content` | Tafsiri seli za Markdown katika JSON ya daftari la kumbukumbu. | No |
| `translate_image_content` | Tafsiri maandishi kwenye picha moja na rudisha data ya picha base64. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Andaa vipande vya Markdown kwa mjuu mwenyeji kutafsiri bila nyaraka za LLM za Co-op Translator. | No |
| `finish_markdown_agent_translation` | Jenga tena Markdown kutoka kwa vipande vilivyotafsiriwa na mjuu-mshirika. | No |
| `start_notebook_agent_translation` | Andaa vipande vya seli za Markdown za daftari kwa mjuu mwenyeji kutafsiri. | No |
| `finish_notebook_agent_translation` | Jenga tena JSON ya daftari kutoka kwa vipande vilivyotafsiriwa na mjuu-mshirika. | No |
| `rewrite_markdown_paths` | Rekebisha mwili wa Markdown na njia za frontmatter kwa lengo lililotafsiriwa. | No |
| `rewrite_notebook_paths` | Rekebisha njia ndani ya seli za Markdown za daftari. | No |
| `run_translation` | Endesha tafsiri ya ngazi ya mradi kama CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Jina la utangamano kwa `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Endesha ukaguzi thabiti wa ukaguzi. | No |
| `get_configuration_status` | Ripoti muuzaji wa LLM na Vision waliowekwa bila kufichua siri. | No |
| `list_supported_languages` | Orodhesha msimbo wa lugha lengwa zinazoungwa mkono. | No |
| `get_api_overview` | Eleza workflows na zana za MCP zinazopatikana. | No |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | Muhtasari wa JSON wa workflows na zana. |
| `co-op://supported-languages` | Orodheshi ya JSON ya misimbo ya lugha zinazoungwa mkono. |
| `co-op://configuration` | Muhtasari wa upatikanaji wa muuzaji kwa JSON bila siri. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Waongoze mteja wa MCP kupitia tafsiri ya yaliyomo pamoja na urekebishaji wa njia hiari. |
| `agent_assisted_markdown_translation_prompt` | Waongoze mteja wa MCP kupitia tafsiri ya Markdown ya mjuu-mwenyeji bila nyaraka za LLM za Co-op Translator. |
| `translate_repository_prompt` | Waongoze mteja wa MCP kupitia tafsiri ya hifadhidata kwa kuanza kwa dry-run. |

## Copy-Paste Examples

Translate Markdown content:

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

Rewrite translated Markdown links:

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

Translate Markdown with the host agent model:

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

After the host agent translates each returned chunk, finish the job with the complete `job` object returned by `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

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

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Tumia njia kamili ya utekelezaji wa Python na usanidi wa chanzo `["-m", "co_op_translator.mcp.server"]`. |
| The server is listed but translation fails. | Ita `get_configuration_status` na thibitisha muuzaji wa LLM anapatikana. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Tumia `start_markdown_agent_translation` / `finish_markdown_agent_translation` au sawa kwa daftari ili mjuu mwenyeji atafsiri vipande. |
| Image translation fails. | Thibitisha vigezo vya Azure AI Vision vimewekwa na ita `get_configuration_status`. |
| Repository translation does not write files. | Weka `dry_run=false` na `confirm_write=true` tu baada ya idhini wazi ya mtumiaji. |
| Changes to client config do not appear. | Anzisha tena au pakia upya mteja wa MCP. |

## Safety Notes

- Miito ya zana za MCP inaendeshwa na modeli na programu mwenyeji, kwa hivyo tafsiri ya hifadhidata ni dry-run kwa chaguo-msingi.
- Tafsiri kamili ya hifadhidata inaweza kuunda, kusasisha, au kuondoa mafaili mengi. Ishauri idhini wazi ya mtumiaji kabla ya kuweka `confirm_write=true`.
- Zana ya hali ya usanidi haina kurudisha kamwe API keys, endpoints, au thamani nyingine za siri.
- Tafsiri ya picha inarudisha data ya picha base64. Picha kubwa zinaweza kuzalisha majibu makubwa ya zana.
- Zana zinazosaidiwa na maajenti hurudisha vipande vya chanzo na maagizo kwa mjuu mwenyeji wa MCP. Zitumiwe tu na yaliyomo ambayo mtumiaji yameridhika kuyatuma kwa model ya mjuu-mwenyeji.