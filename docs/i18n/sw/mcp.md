# Seva ya MCP

Co-op Translator inajumuisha seva ya Model Context Protocol kwa maajenti, wahariri, na wateja wanaoendana na MCP.

Kwa usanidi wa kawaida wa eneo-lokal, watumiaji hawaiendeshi seva tofauti kwa mkono. Wanakonfigura mteja wao wa MCP, na mteja huanzisha `co-op-translator-mcp` kiotomatiki kupitia `stdio` wakati unahitaji zana za Co-op Translator.

Ikiwa unasonga kati ya CLI, Python API, na MCP, anza na [Chagua Mtiririko Wako](workflows.md).

Tumia MCP wakati ajenti au mhariri anapaswa kumuita Co-op Translator moja kwa moja:

| Lengo la mtumiaji | Zana za MCP |
| --- | --- |
| Tafsiri hati moja ya Markdown, daftari, au picha | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Tafsiri yaliyomo ya Markdown au daftari kwa kutumia modeli ya ajenti mwenyeji | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rekebisha viungo vya Markdown au daftari yaliyotafsiriwa baada ya kuchagua njia ya pato | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Tafsiri hazina nzima kama CLI | `run_translation`, `translate_project` |
| Kagua pato lililotafsiriwa bila sifa za LLM | `run_review` |
| Chunguza uwezo na hali ya mazingira | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Seva ya MCP inafunika API ya Python ya umma inayofaa iliyoelezewa katika [API ya Python](api.md). Zana zinazotumia watoaji zinafanya kazi na watoaji waliosanidiwa sawa na CLI na API ya Python. Zana zilizosindikizwa na ajenti zinaandaa vipande kwa ajenti mwenyeji wa MCP kutafsiri, kisha zinatumia Co-op Translator kujenga upya Markdown au daftari la mwisho.

## Hatua 1: Sakinisha na Sanidi Co-op Translator

Sakinisha Co-op Translator katika mazingira ya Python ambayo mteja wako wa MCP atatumia:

```bash
pip install co-op-translator
```

Kwa maendeleo ya eneo-lokal kutoka kwenye hifadhidata hii, sakinisha kifurushi katika modi ya kuhariri:

```bash
pip install -e .
```

Chagua modi ya kutafsiri ambayo mteja wako wa MCP atatumia:

| Modi | Tumia kwa | Cheti |
| --- | --- | --- |
| Inayotegemea mtoa huduma | Co-op Translator inaita `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, au `run_translation`. | Kutafsiri kunahitaji Azure OpenAI, OpenAI, au Anthropic. Kutafsiri picha pia kunahitaji Azure AI Vision. |
| Inayosaidiwa na ajenti | Ajenti mwenyeji wa MCP anatafsiri vipande vilivyorejeshwa na `start_markdown_agent_translation` au `start_notebook_agent_translation`. | Hakuna sifa za mtoa LLM za Co-op Translator zinahitajika kwa vipande vya Markdown au daftari. Kutafsiri picha bado hakujajumuishwa katika modi inayosaidiwa na ajenti. |

Ikiwa unaanza na kutafsiri Markdown au daftari ndani ya ajenti kama Codex au Claude Code, anza kwa modi inayosaidiwa na ajenti. Tumia modi inayotegemea mtoa huduma unapotaka Co-op Translator yenyewe iite watoaji ulioweka, unapokutafsiri picha, au unapotekeleza tafsiri ya kiwango cha hazina kama CLI.

Sanidi mtoa huduma mmoja kwa ajili ya milinganyo inayotegemea mtoa huduma:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Au OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Au Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Kutafsiri picha kwa njia inayotegemea mtoa huduma pia kunahitaji:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Modi inayosaidiwa na ajenti kwa sasa inahusisha Markdown na seli za Markdown za daftari. Kutafsiri picha bado kunatumia mtiririko wa picha unaotegemea mtoa huduma na kunahitaji Azure AI Vision kwa OCR na uchoraji unaojua mpangilio.

## Hatua 2: Sanidi Mteja Wako wa MCP

Kwa usanidi wa kawaida wa eneo-lokal `stdio`, ongeza Co-op Translator kwenye usanidi wa mteja wako wa MCP. Mteja ataanzisha na kusimamisha mchakato kiotomatiki.

Usanidi wa kifurushi kilichosakinishwa:

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

Usanidi wa checkout ya chanzo kwenye Windows:

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

Usanidi wa checkout ya chanzo kwenye macOS au Linux:

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

Baada ya kubadilisha usanidi wa mteja wa MCP, anzisha upya au upakia upya mteja ili uweze kugundua seva mpya.

## Hatua 3: Thibitisha Seva katika Mteja

Muulize mteja wa MCP upangue zana zinazopatikana, au itumie moja ya wasaidizi wa kusoma pekee kwa mara ya kwanza:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Ukaguzi muhimu wa awali:

| Zana | Kitu cha kukagua |
| --- | --- |
| `get_api_overview` | Inathibitisha seva inapatikana na inaonyesha mitiririko ya kazi inayopatikana. |
| `list_supported_languages` | Inathibitisha data za lugha zilizopakiwa zinaweza kupakiwa. |
| `get_configuration_status` | Inathibitisha upatikanaji wa mtoa LLM na Vision bila kufichua thamani za siri. |

## Hatua 4: Chagua Mtiririko wa Kazi

### Tafsiri Faili au Nyaraka Mmoja-Mmoja

Tumia zana za yaliyomo zinazotegemea mtoa huduma wakati mteja wa MCP tayari ana yaliyomo ya hati au njia ya picha na Co-op Translator inapaswa kuita watoaji uliowekwa.

Kwa Markdown:

1. Piga simu `translate_markdown_content` kwa `document`, `language_code`, na kwa hiari `source_path`.
2. Ikiwa matokeo yaliyotafsiriwa yataandikwa katika muundo wa pato la Co-op Translator, piga simu `rewrite_markdown_paths`.
3. Acha mteja aandike au arudishe `content` ya mwisho.

Kwa daftari:

1. Piga simu `translate_notebook_content` na JSON ya daftari na `language_code`.
2. Piga simu `rewrite_notebook_paths` ikiwa viungo vya daftari yaliyotafsiriwa vinahitaji kurekebishwa kwa njia lengwa.
3. Andika au rudi JSON ya daftari ya mwisho.

Kwa picha:

1. Piga simu `translate_image_content` kwa `image_path`, `language_code`, na kwa hiari `root_dir` au `fast_mode`.
2. Soma `data_base64` na `mime_type` vilivyorejeshwa.
3. Ikiwa `output_path` imetolewa, picha iliyotafsiriwa pia inawekwa kwenye njia hiyo.

Zana za yaliyomo hazitekelezi ugunduzi wa mradi, masasisho ya metadata, viwango vya kujitenga, au uandishi wa njia kiotomatiki. Ikiwa unataka ajenti mwenyeji atafsiri vipande vya Markdown au daftari bila sifa za mtoa LLM za Co-op Translator, tumia mtiririko unaosaidiwa na ajenti hapa chini.

### Tafsiri kwa Modeli ya Ajenti Mwenyeji

Tumia zana zinazosaidiwa na ajenti unapotaka ajenti mwenyeji wa MCP, kama msaidizi wa kuweka msimbo, kutoa maandishi yaliyotafsiri badala ya kusanidi mtoa huduma wa LLM kwa Co-op Translator.

Katika mteja wa MCP unaotegemea chat, kawaida hauhitaji kuandika JSON ya zana wewe mwenyewe. Muombe ajenti atumie mtiririko unaosaidiwa na ajenti:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Kwa daftari, tumia mtindo ule ule:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Ikiwa mteja wako wa MCP unaunga mkono wasukumo za seva, tumia `agent_assisted_markdown_translation_prompt` ili mteja apakue maagizo ya mtiririko huo huo.

Kwa Markdown:

1. Piga simu `start_markdown_agent_translation` kwa `document`, `language_code`, na kwa hiari `source_path`.
2. Tafsiri kila kipande kilichorejeshwa kwenye ajenti mwenyeji kwa kufuata `prompt` ya kipande.
3. Piga simu `finish_markdown_agent_translation` na `job` asili na vipande vilivyotafsiriwa ukitumia `chunk_id` na `translated_text`.
4. Ikiwa yaliyomo yataandikwa kwenye njia lengwa iliyotafsiriwa, piga simu `rewrite_markdown_paths`.

Kwa daftari:

1. Piga simu `start_notebook_agent_translation` na JSON ya daftari na `language_code`.
2. Tafsiri kila kipande kilichorejeshwa kwenye ajenti mwenyeji.
3. Piga simu `finish_notebook_agent_translation` kwa `job` asili na vipande vilivyotafsiriwa.
4. Piga simu `rewrite_notebook_paths` ikiwa viungo vya daftari yaliyotafsiriwa vinahitaji kurekebishwa kwa njia lengwa.

Zana zinazosaidiwa na ajenti hazipigi simu kwa mtoa LLM uliowezeshwa kutoka Co-op Translator. Ajenti mwenyeji ndiye anayehusika kutafsiri vipande vilivyorejeshwa. Co-op Translator inashughulikia kugawanya Markdown, kuhifadhi viti vinavyobaki (placeholders), ujenzi wa frontmatter, uingizaji wa seli za daftari, na kawaida baada ya kutafsiri.

### Tafsiri Hazina Yote ya Mradi

Tumia `run_translation` wakati mtumiaji anataka Co-op Translator ifanye kazi kama CLI ya `translate`.

Tafsiri ya hazina inakuwa kwa chaguo `dry_run=true` ili ajenti aweze kukagua wigo kabla ya mabadiliko ya faili:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Matokeo ya `run_translation` yanajumuisha safu ya `events` yenye matukio ya maendeleo yaliyobadilishwa toleo
`co-op.translation.event.v1`. Wateja wa MCP wanapaswa kutumia nyanja kama
`type`, `stage_key`, `completed`, `total`, na `current_path` badala ya
kuchambua maandishi yaliyorekodiwa kwenye konsoli. Pitisha `json_events_path` pia kuandika matukio hayo
kwenye faili ya NDJSON.

Ili kuruhusu uandikaji, mwito lazima weke `dry_run=false` na pia `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` imefunuliwa kama jina la ulinganifu kwa `run_translation`.

### Kagua Matokeo Yaliyotafsiriwa

Tumia `run_review` kwa ukaguzi wa deterministic ambao hauhitaji sifa za LLM au Vision:

!!! note "Beta"
    MCP inafungua API ya beta `run_review`. Ni salama kwa mitiririko ya ukaguzi wa kusoma pekee, lakini ukaguzi na miundo ya masuala yanaweza kubadilika.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Matokeo yanajumuisha matokeo ya maandishi yaliyorekodiwa na muhtasari uliopangwa wa ukaguzi inapopatikana.

## Uendeshaji wa Seva Kwa Mikono

Uendeshaji kwa mikono kwa kawaida ni kwa ajili ya kutatua mdudu au kwa usafirishaji unaofanya kazi kama seva zinazoendelea kwa muda mrefu.

Gundua mdudu kwa seva ya stdio ya msingi:

```bash
co-op-translator-mcp
```

Endesha kutoka kwenye checkout ya chanzo:

```bash
python -m co_op_translator.mcp.server
```

Endesha seva ya HTTP au SSE yenye maisha marefu:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Kwa ujumuishaji wa mhariri na ajenti wa eneo-lokal, pendelea usanidi wa `stdio` unaosimamiwa na mteja katika Hatua 2.

## Zana

| Zana | Madhumuni | Inaandika faili |
| --- | --- | --- |
| `translate_markdown_content` | Tafsiri maandishi ya Markdown. | Hapana |
| `translate_notebook_content` | Tafsiri seli za Markdown katika JSON ya daftari. | Hapana |
| `translate_image_content` | Tafsiri maandishi katika picha moja na rudisha data ya picha kwa base64. | Hiari, tu wakati `output_path` imetolewa |
| `start_markdown_agent_translation` | Andaa vipande vya Markdown kwa ajenti mwenyeji kutafsiri bila sifa za mtoa LLM za Co-op Translator. | Hapana |
| `finish_markdown_agent_translation` | Jenga tena Markdown kutoka kwa vipande vilivyotafsiriwa na ajenti mwenyeji. | Hapana |
| `start_notebook_agent_translation` | Andaa vipande vya seli za Markdown za daftari kwa ajenti mwenyeji kutafsiri. | Hapana |
| `finish_notebook_agent_translation` | Jenga tena JSON ya daftari kutoka kwa vipande vilivyotafsiriwa na ajenti mwenyeji. | Hapana |
| `rewrite_markdown_paths` | Rekebisha mwili wa Markdown na njia za frontmatter kwa lengo lililotafsiriwa. | Hapana |
| `rewrite_notebook_paths` | Rekebisha njia ndani ya seli za Markdown za daftari. | Hapana |
| `run_translation` | Endesha tafsiri ya mradi kama CLI. | Ndiyo wakati `dry_run=false` na `confirm_write=true` |
| `translate_project` | Jina la ulinganifu kwa `run_translation`. | Ndiyo wakati `dry_run=false` na `confirm_write=true` |
| `run_review` | Endesha ukaguzi wa deterministic. | Hapana |
| `get_configuration_status` | Ripoti watoaji wa LLM na Vision waliowekwa bila kufichua siri. | Hapana |
| `list_supported_languages` | Orodha ya misimbo ya lugha lengwa zinazotumika. | Hapana |
| `get_api_overview` | Elezea mitiririko ya MCP inayopatikana na zana. | Hapana |

## Rasilimali

| Resource URI | Madhumuni |
| --- | --- |
| `co-op://api` | Muhtasari wa JSON wa mitiririko ya kazi na zana. |
| `co-op://supported-languages` | Orodha ya JSON ya misimbo ya lugha zinazotumika. |
| `co-op://configuration` | Muhtasari wa upatikanaji wa mtoa huduma kwa JSON bila siri. |

## Maelekezo

| Chocheo | Madhumuni |
| --- | --- |
| `translate_markdown_document_prompt` | Waambie mteja wa MCP kupitia tafsiri ya yaliyomo pamoja na uandishi wa njia kwa hiari. |
| `agent_assisted_markdown_translation_prompt` | Waambie mteja wa MCP kupitia tafsiri ya Markdown kwa ajenti mwenyeji bila sifa za mtoa LLM za Co-op Translator. |
| `translate_repository_prompt` | Waambie mteja wa MCP kupitia tafsiri ya hazina kwa kuanza na run kavu (dry-run-first). |

## Mifano za Nakili-na-Bandika

Tafsiri yaliyomo ya Markdown:

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

Rekebisha viungo vya Markdown vilivyotafsiriwa:

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

Tafsiri Markdown kwa kutumia modeli ya ajenti mwenyeji:

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

Baada ya ajenti mwenyeji kutafsiri kila kipande kilichorejeshwa, malizia kazi kwa kitu kamili cha `job` kilichorejeshwa na `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Onyesha awali tafsiri ya hazina:

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

## Utatuzi wa Matatizo

| Tatizo | Kitu cha kujaribu |
| --- | --- |
| Mteja wa MCP hauwezi kupata `co-op-translator-mcp`. | Tumia njia kamili ya utekelezaji wa Python na usanidi wa checkout ya chanzo `["-m", "co_op_translator.mcp.server"]`. |
| Seva imeorodheshwa lakini tafsiri inashindwa. | Piga simu `get_configuration_status` na thibitisha mtoa LLM anapatikana. |
| Unataka tafsiri ya Markdown au daftari bila sifa za mtoa huduma. | Tumia `start_markdown_agent_translation` / `finish_markdown_agent_translation` au sawa kwa daftari ili ajenti mwenyeji atafsiri vipande. |
| Kutafsiri picha kunashindwa. | Thibitisha vigezo vya Azure AI Vision vimewekwa na piga simu `get_configuration_status`. |
| Tafsiri ya hazina haisomi faili. | Weka `dry_run=false` na `confirm_write=true` tu baada ya idhini ya wazi ya mtumiaji. |
| Mabadiliko ya usanidi wa mteja hayaonekani. | Anzisha upya au upakia upya mteja wa MCP. |

## Vidokezo vya Usalama

- Miito ya zana za MCP zinadhibitiwa na programu mwenyeji, kwa hivyo tafsiri ya hazina kwa chaguo ni run kavu kwa msingi.
- Tafsiri kamili ya hazina inaweza kuunda, kusasisha, au kuondoa faili nyingi. Hitaji idhini wazi ya mtumiaji kabla ya kuweka `confirm_write=true`.
- Zana ya hali ya usanidi haitarudishi kamwe API keys, endpoints, au thamani nyinginezo za siri.
- Kutafsiri picha kunarudisha data ya picha kwa base64. Picha kubwa zinaweza kutoa majibu makubwa ya zana.
- Zana zinazosaidiwa na ajenti hurudisha vipande vya asili na wasukumo kwa mwenyeji wa MCP. Zitumiwe tu kwa yaliyomo ambayo mtumiaji anafurahia kuyatuma kwa mfano huyo wa ajenti mwenyeji.