# MCP सर्वर

Co-op Translator में एजेंटों, संपादकों, और MCP-अनुकूल क्लाइंट्स के लिए एक Model Context Protocol सर्वर शामिल है।

डिफ़ॉल्ट लोकल सेटअप के लिए, उपयोगकर्ता अलग से कोई सर्वर मैन्युअल रूप से चलाए बिना रखते हैं। वे अपने MCP क्लाइंट को कॉन्फ़िगर करते हैं, और जब उन्हें Co-op Translator टूल्स की आवश्यकता होती है तो क्लाइंट स्वतः `co-op-translator-mcp` को `stdio` के माध्यम से शुरू कर देता है।

यदि आप CLI, Python API, और MCP के बीच निर्णय कर रहे हैं, तो [अपना वर्कफ़्लो चुनें](workflows.md) से शुरू करें।

जब किसी एजेंट या संपादक को Co-op Translator को सीधे कॉल करना चाहिए तब MCP का उपयोग करें:

| उपयोगकर्ता लक्ष्य | MCP उपकरण |
| --- | --- |
| एक Markdown दस्तावेज़, नोटबुक, या छवि का अनुवाद करें | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| होस्ट एजेंट मॉडल के साथ Markdown या नोटबुक सामग्री का अनुवाद करें | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| आउटपुट पथ चुनने के बाद अनूदित Markdown या नोटबुक लिंक फिर से लिखें | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI की तरह पूरे रिपॉज़िटरी का अनुवाद करें | `run_translation`, `translate_project` |
| LLM क्रेडेंशियल्स के बिना अनूदित आउटपुट की समीक्षा करें | `run_review` |
| क्षमताओं और पर्यावरण स्थिति का निरीक्षण करें | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP सर्वर उसी सार्वजनिक Python API को रैप करता है जैसा [Python API](api.md) में दस्तावेजीकृत है। प्रदाता-समर्थित टूल CLI और Python API के समान कॉन्फ़िगर किए गए प्रदाताओं का उपयोग करते हैं। एजेंट-सहायता टूल MCP होस्ट एजेंट के लिए अनुवाद करने के लिए चंक्स तैयार करते हैं, और फिर अंतिम Markdown या नोटबुक पुनर्निर्माण करने के लिए Co-op Translator का उपयोग करते हैं।

## चरण 1: Co-op Translator इंस्टॉल और कॉन्फ़िगर करें

अपने MCP क्लाइंट द्वारा इस्तेमाल किए जाने वाले Python वातावरण में Co-op Translator इंस्टॉल करें:

```bash
pip install co-op-translator
```

इस रिपॉज़िटरी से लोकल विकास के लिए, पैकेज को एडिटेबल मोड में इंस्टॉल करें:

```bash
pip install -e .
```

अपना MCP क्लाइंट जो अनुवाद मोड उपयोग करेगा उसे चुनें:

| मोड | इसका उपयोग किसके लिए करें | क्रेडेंशियल्स |
| --- | --- | --- |
| प्रदाता-समर्थित | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, या `run_translation` को कॉल करता है। | अनुवाद के लिए Azure OpenAI, OpenAI, या Anthropic की आवश्यकता होती है। छवि अनुवाद के लिए Azure AI Vision भी आवश्यक है। |
| एजेंट-सहायता | MCP होस्ट एजेंट उन चंक्स का अनुवाद करता है जो `start_markdown_agent_translation` या `start_notebook_agent_translation` द्वारा लौटाए जाते हैं। | Markdown या नोटबुक चंक्स के लिए Co-op Translator LLM प्रदाता क्रेडेंशियल्स की आवश्यकता नहीं है। छवि अनुवाद अभी एजेंट-सहायता मोड में शामिल नहीं है। |

यदि आप Codex या Claude Code जैसे किसी एजेंट के अंदर Markdown या नोटबुक अनुवाद से शुरू कर रहे हैं, तो एजेंट-सहायता मोड से शुरू करें। जब आप चाहते हैं कि Co-op Translator स्वयं आपके कॉन्फ़िगर किए गए प्रदाताओं को कॉल करे, जब आप छवियों का अनुवाद कर रहे हों, या जब आप CLI की तरह रिपॉज़िटरी-स्तरीय अनुवाद चला रहे हों तो प्रदाता-समर्थित मोड का उपयोग करें।

प्रदाता-समर्थित वर्कफ़्लो के लिए एक प्रदाता कॉन्फ़िगर करें:

```bash
# एज़्योर ओपनएआई
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# या ओपनएआई
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# या एंथ्रोपिक
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

प्रदाता-समर्थित छवि अनुवाद के लिए अतिरिक्त रूप से आवश्यक है:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    एजेंट-सहायता मोड वर्तमान में Markdown और नोटबुक के Markdown सेल को शामिल करता है। छवि अनुवाद अभी भी प्रदाता-समर्थित इमेज पाइपलाइन का उपयोग करता है और OCR व लेआउट-आधारित रेंडरिंग के लिए Azure AI Vision की आवश्यकता होती है।

## चरण 2: अपने MCP क्लाइंट को कॉन्फ़िगर करें

सामान्य लोकल `stdio` सेटअप के लिए, अपने MCP क्लाइंट कॉन्फ़िगरेशन में Co-op Translator जोड़ें। क्लाइंट प्रक्रिया को स्वचालित रूप से शुरू और बंद कर देगा।

इंस्टॉल किए गए पैकेज का कॉन्फ़िगरेशन:

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

Windows पर स्रोत चेकआउट कॉन्फ़िगरेशन:

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

macOS या Linux पर स्रोत चेकआउट कॉन्फ़िगरेशन:

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

MCP क्लाइंट कॉन्फ़िगरेशन बदलने के बाद, क्लाइंट को नई सर्वर खोजने के लिए पुनरारंभ या रीलोड करें।

## चरण 3: क्लाइंट में सर्वर का सत्यापन करें

उपलब्ध टूल सूचीबद्ध करने के लिए MCP क्लाइंट से पूछें, या पहले किसी एक read-only हेल्पर को कॉल करें:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

पहली उपयोगी जाँचें:

| टूल | क्या जाँचें |
| --- | --- |
| `get_api_overview` | सुनिश्चित करता है कि सर्वर पहुँचा जा सकता है और उपलब्ध वर्कफ़्लो दिखाता है। |
| `list_supported_languages` | सुनिश्चित करता है कि पैकेज्ड भाषा डेटा लोड किया जा सकता है। |
| `get_configuration_status` | LLM और Vision प्रदाता की उपलब्धता की पुष्टि करता है बिना किसी गुप्त मान को प्रकट किए। |

## चरण 4: एक वर्कफ़्लो चुनें

### व्यक्तिगत फ़ाइलें या दस्तावेज़ अनुवादित करें

जब MCP क्लाइंट के पास पहले से दस्तावेज़ सामग्री या छवि पथ हो और Co-op Translator को कॉन्फ़िगर किए गए अनुवाद प्रदाताओं को कॉल करना चाहिए, तो प्रदाता-समर्थित कंटेंट टूल्स का उपयोग करें।

Markdown के लिए:

1. `document`, `language_code`, और वैकल्पिक रूप से `source_path` के साथ `translate_markdown_content` को कॉल करें।
2. यदि अनूदित परिणाम को Co-op Translator आउटपुट लेआउट में लिखा जाएगा, तो `rewrite_markdown_paths` को कॉल करें।
3. क्लाइंट को अंतिम `content` लिखने या लौटाने दें।

नोटबुक के लिए:

1. नोटबुक JSON और `language_code` के साथ `translate_notebook_content` को कॉल करें।
2. यदि अनूदित नोटबुक लिंक को लक्षित पथ के लिए समायोजित करने की आवश्यकता हो तो `rewrite_notebook_paths` को कॉल करें।
3. अंतिम नोटबुक JSON लिखें या लौटाएँ।

छवियों के लिए:

1. `image_path`, `language_code`, और वैकल्पिक `root_dir` या `fast_mode` के साथ `translate_image_content` को कॉल करें।
2. लौटाए गए `data_base64` और `mime_type` को पढ़ें।
3. यदि `output_path` प्रदान किया गया है, तो अनूदित छवि उस पथ पर भी सहेजी जाएगी।

कंटेंट टूल्स प्रोजेक्ट डिसकवरी, मेटाडेटा अपडेट्स, डिस्क्लेमर्स, या स्वचालित पाथ रीराइटिंग नहीं करते। यदि आप चाहते हैं कि होस्ट एजेंट Co-op Translator LLM प्रदाता क्रेडेंशियल्स के बिना Markdown या नोटबुक चंक्स का अनुवाद करे, तो नीचे दिए गए एजेंट-сहायता वर्कफ़्लो का उपयोग करें।

### होस्ट एजेंट मॉडल के साथ अनुवाद करें

जब आप चाहें कि MCP होस्ट एजेंट (जैसे कोडिंग असिस्टेंट) अनूदित टेक्स्ट उत्पन्न करे बजाय इसके कि Co-op Translator के लिए LLM प्रदाता कॉन्फ़िगर करें, तब एजेंट-सहायता टूल्स का उपयोग करें।

एक चैट-आधारित MCP क्लाइंट में, सामान्यतः आपको स्वयं टूल JSON लिखने की ज़रूरत नहीं होती। एजेंट से अनुरोध करें कि वह एजेंट-सहायता वर्कफ़्लो का उपयोग करे:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

नोटबुक्स के लिए, वही पैटर्न उपयोग करें:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

यदि आपका MCP क्लाइंट सर्वर प्रॉम्प्ट्स का समर्थन करता है, तो वही वर्कफ़्लो निर्देश लोड करने के लिए क्लाइंट को `agent_assisted_markdown_translation_prompt` का उपयोग करें।

Markdown के लिए:

1. `document`, `language_code`, और वैकल्पिक रूप से `source_path` के साथ `start_markdown_agent_translation` को कॉल करें।
2. हर लौटाए गए चंक का होस्ट एजेंट में चंक `prompt` का पालन करके अनुवाद करें।
3. मूल `job` और अनूदित चंक्स को `chunk_id` और `translated_text` का उपयोग करके `finish_markdown_agent_translation` के साथ कॉल करें।
4. यदि सामग्री को अनूदित लक्ष्य पथ पर लिखा जाएगा, तो `rewrite_markdown_paths` को कॉल करें।

नोटबुक्स के लिए:

1. नोटबुक JSON और `language_code` के साथ `start_notebook_agent_translation` को कॉल करें।
2. प्रत्येक लौटाए गए चंक का होस्ट एजेंट में अनुवाद करें।
3. मूल `job` और अनुवादित खंडों के साथ `finish_notebook_agent_translation` को कॉल करें।
4. यदि अनुवादित नोटबुक लिंक को लक्ष्य-पथ समायोजन की आवश्यकता हो तो `rewrite_notebook_paths` को कॉल करें।

Agent-assisted tools Co-op Translator से कॉन्फ़िगर किए गए LLM प्रोवाइडर को कॉल नहीं करते। होस्ट एजेंट लौटाए गए खंडों का अनुवाद करने के लिए जिम्मेदार है। Co-op Translator Markdown का खंडन, प्लेसहोल्डर संरक्षण, फ्रंटमैटर पुनर्निर्माण, नोटबुक सेल प्रतिस्थापन, और अनुवाद के बाद सामान्यीकरण संभालता है।

### पूरे रिपॉजिटरी का अनुवाद करें

उपयोग करें `run_translation` जब उपयोगकर्ता चाहता है कि Co-op Translator `translate` CLI की तरह व्यवहार करे।

रिपॉजिटरी अनुवाद डिफ़ॉल्ट रूप से `dry_run=true` होता है ताकि एजेंट फ़ाइल परिवर्तनों से पहले सीमा का निरीक्षण कर सके:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` परिणाम में संस्करण-संबंधित `events` एरे शामिल होता है
`co-op.translation.event.v1` प्रगति इवेंट्स। MCP क्लाइंट्स को निम्न फ़ील्ड्स का उपयोग करना चाहिए जैसे
`type`, `stage_key`, `completed`, `total`, और `current_path` के बजाय
पकड़े गए कंसोल टेक्स्ट को पार्स करने के बजाय। उन इवेंट्स को भी लिखने के लिए `json_events_path` पास करें
एक NDJSON फ़ाइल में।

लेखन की अनुमति देने के लिए, कॉल करने वाले को दोनों `dry_run=false` और `confirm_write=true` सेट करने चाहिए:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` को `run_translation` के लिए संगत एलियास के रूप में उपलब्ध कराया गया है।

### अनुवादित आउटपुट की समीक्षा

ऐसे निर्णायक चेक्स के लिए `run_review` का उपयोग करें जिन्हें LLM या Vision क्रेडेंशियल की आवश्यकता नहीं होती:

!!! note "Beta"
    MCP beta `run_review` API को एक्सपोज़ करता है। यह केवल-रीड समीक्षा वर्कफ़्लोज़ के लिए सुरक्षित है, लेकिन समीक्षा चेक्स और इश्यू स्कीमाएं विकसित हो सकती हैं।

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

परिणाम में कब्ज़ा किया गया टेक्स्ट आउटपुट और उपलब्ध होने पर एक संरचित समीक्षा सारांश शामिल होता है।

## मैनुअल सर्वर रन

मैनुअल रन मुख्य रूप से डिबगिंग के लिए या उन ट्रांसपोर्ट्स के लिए होते हैं जो लंबे समय तक चलने वाले सर्वरों की तरह व्यवहार करते हैं।

डिफ़ॉल्ट stdio सर्वर को डिबग करें:

```bash
co-op-translator-mcp
```

स्रोत चेकआउट से चलाएँ:

```bash
python -m co_op_translator.mcp.server
```

लंबे समय तक चलने वाला HTTP या SSE सर्वर चलाएँ:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

स्थानीय संपादक और एजेंट इंटीग्रेशन के लिए, चरण 2 में क्लाइंट-प्रबंधित `stdio` कॉन्फ़िगरेशन को प्राथमिकता दें।

## टूल्स

| टूल | उद्देश्य | फ़ाइलें लिखता है |
| --- | --- | --- |
| `translate_markdown_content` | एक Markdown स्ट्रिंग का अनुवाद करें। | नहीं |
| `translate_notebook_content` | नोटबुक JSON में Markdown सेल्स का अनुवाद करें। | नहीं |
| `translate_image_content` | एक इमेज में टेक्स्ट का अनुवाद करें और base64 इमेज डेटा लौटा दें। | वैकल्पिक, केवल जब `output_path` प्रदान किया गया हो |
| `start_markdown_agent_translation` | होस्ट एजेंट के लिए Markdown खंड तैयार करें ताकि वे Co-op Translator LLM क्रेडेंशियल्स के बिना अनुवाद कर सकें। | नहीं |
| `finish_markdown_agent_translation` | होस्ट-एजेंट द्वारा अनुवादित खंडों से Markdown को पुनर्निर्मित करें। | नहीं |
| `start_notebook_agent_translation` | होस्ट एजेंट के अनुवाद के लिए नोटबुक Markdown-सेल खंड तैयार करें। | नहीं |
| `finish_notebook_agent_translation` | होस्ट-एजेंट द्वारा अनुवादित खंडों से नोटबुक JSON को पुनर्निर्मित करें। | नहीं |
| `rewrite_markdown_paths` | अनूदित लक्ष्य के लिए Markdown बॉडी और फ्रंटमैटर पथों को पुनर्लेखन करें। | नहीं |
| `rewrite_notebook_paths` | नोटबुक Markdown सेल्स के अंदर पथों को पुनर्लेखन करें। | नहीं |
| `run_translation` | CLI की तरह प्रोजेक्ट-स्तरीय अनुवाद चलाएँ। | हाँ जब `dry_run=false` और `confirm_write=true` |
| `translate_project` | `run_translation` के लिए संगत एलियास। | हाँ जब `dry_run=false` और `confirm_write=true` |
| `run_review` | निर्णायक समीक्षा चेक्स चलाएँ। | नहीं |
| `get_configuration_status` | सीक्रेट्स को उजागर किए बिना कॉन्फ़िगर किए गए LLM और Vision प्रोवाइडर्स की रिपोर्ट करें। | नहीं |
| `list_supported_languages` | समर्थित लक्ष्य भाषा कोडों की सूची दें। | नहीं |
| `get_api_overview` | उपलब्ध MCP वर्कफ़्लोज़ और टूल्स का वर्णन करें। | नहीं |

## संसाधन

| संसाधन URI | उद्देश्य |
| --- | --- |
| `co-op://api` | वर्कफ़्लोज़ और टूल्स का JSON ओवरव्यू। |
| `co-op://supported-languages` | समर्थित भाषा कोडों की JSON सूची। |
| `co-op://configuration` | सीक्रेट्स के बिना प्रोवाइडर उपलब्धता का JSON सारांश। |

## प्रॉम्प्ट्स

| प्रॉम्प्ट | उद्देश्य |
| --- | --- |
| `translate_markdown_document_prompt` | सामग्री अनुवाद और वैकल्पिक पथ-पुनर्लेखन के माध्यम से MCP क्लाइंट का मार्गदर्शन करें। |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM प्रोवाइडर क्रेडेंशियल्स के बिना होस्ट-एजेंट Markdown अनुवाद के माध्यम से MCP क्लाइंट का मार्गदर्शन करें। |
| `translate_repository_prompt` | ड्राय-रन-प्रथम रिपॉजिटरी अनुवाद के माध्यम से MCP क्लाइंट का मार्गदर्शन करें। |

## कॉपी-पेस्ट उदाहरण

Markdown सामग्री का अनुवाद करें:

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

अनूदित Markdown लिंक पुनर्लेखन करें:

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

Host एजेंट मॉडल के साथ Markdown अनुवाद करें:

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

जब होस्ट एजेंट प्रत्येक लौटा हुआ खंड अनुवाद कर ले, तो `start_markdown_agent_translation` द्वारा लौटाए गए पूर्ण `job` ऑब्जेक्ट के साथ जॉब पूरा करें:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

रिपॉजिटरी अनुवाद का पूर्वावलोकन:

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

## समस्या निवारण

| समस्या | क्या आज़माएँ |
| --- | --- |
| MCP क्लाइंट `co-op-translator-mcp` नहीं ढूंढ पा रहा है। | पूर्ण Python executable पथ और `["-m", "co_op_translator.mcp.server"]` source checkout कॉन्फ़िगरेशन का उपयोग करें। |
| सर्वर सूचीबद्ध है लेकिन अनुवाद फेल हो रहा है। | `get_configuration_status` कॉल करें और पुष्टि करें कि एक LLM प्रोवाइडर उपलब्ध है। |
| आप provider क्रेडेंशियल्स के बिना Markdown या नोटबुक अनुवाद चाहते हैं। | `start_markdown_agent_translation` / `finish_markdown_agent_translation` या नोटबुक समकक्षों का उपयोग करें ताकि होस्ट एजेंट खंडों का अनुवाद कर सके। |
| इमेज अनुवाद असफल होता है। | पुष्टि करें कि Azure AI Vision वेरिएबल्स सेट हैं और `get_configuration_status` कॉल करें। |
| रिपॉजिटरी अनुवाद फ़ाइलें नहीं लिखता। | केवल स्पष्ट उपयोगकर्ता अनुमोदन के बाद `dry_run=false` और `confirm_write=true` सेट करें। |
| क्लाइंट कॉन्फ़िग में परिवर्तन दिखाई नहीं देते। | MCP क्लाइंट को रीस्टार्ट या रीलोड करें। |

## सुरक्षा नोट्स

- MCP टूल कॉल होस्ट एप्लिकेशन द्वारा मॉडल-नियंत्रित होते हैं, इसलिए रिपॉजिटरी अनुवाद डिफ़ॉल्ट रूप से dry-run होता है।
- पूरा रिपॉजिटरी अनुवाद कई फ़ाइलें बना, अपडेट या हटाव कर सकता है। `confirm_write=true` सेट करने से पहले स्पष्ट उपयोगकर्ता अनुमोदन आवश्यक करें।
- configuration status टूल कभी भी API keys, endpoints, या अन्य गुप्त मान वापस नहीं करता।
- इमेज अनुवाद base64 इमेज डेटा लौटाता है। बड़ी इमेजेस बड़े टूल प्रतिक्रियाएँ उत्पन्न कर सकती हैं।
- एजेंट-सहायता प्राप्त टूल स्रोत खंड और प्रॉम्प्ट्स MCP होस्ट को लौटाते हैं। इन्हें केवल उन सामग्रियों के साथ उपयोग करें जिन्हें उपयोगकर्ता उस होस्ट एजेंट मॉडल को भेजने में सहज है।