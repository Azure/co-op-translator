# MCP सर्वर

Co-op Translator एजेंट्स, एडिटर्स, और MCP-संगत क्लाइंट्स के लिए एक Model Context Protocol सर्वर शामिल करता है।

डिफ़ॉल्ट लोकल सेटअप के लिए, उपयोगकर्ता अलग सर्वर मैन्युअली चलाकर नहीं रखते। वे अपने MCP क्लाइंट को कॉन्फ़िगर करते हैं, और जब क्लाइंट को Co-op Translator टूल्स की आवश्यकता होती है तो क्लाइंट `co-op-translator-mcp` को स्वतः `stdio` के माध्यम से शुरू कर देता है।

यदि आप CLI, Python API, और MCP के बीच निर्णय ले रहे हैं, तो [Choose Your Workflow](workflows.md) से शुरू करें।

जब किसी एजेंट या एडिटर को Co-op Translator को सीधे कॉल करना चाहिए तब MCP का उपयोग करें:

| उपयोगकर्ता लक्ष्य | MCP टूल्स |
| --- | --- |
| एक Markdown दस्तावेज़, नोटबुक, या छवि का अनुवाद करें | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| होस्ट एजेंट मॉडल के साथ Markdown या नोटबुक सामग्री का अनुवाद करें | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| आउटपुट पथ चुनने के बाद अनुवादित Markdown या नोटबुक लिंक पुन: लिखें | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI की तरह पूरे रिपॉजिटरी का अनुवाद करें | `run_translation`, `translate_project` |
| LLM क्रेडेंशियल्स के बिना अनुवादित आउटपुट की समीक्षा करें | `run_review` |
| क्षमताओं और परिवेश की स्थिति का निरीक्षण करें | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP सर्वर उसी सार्वजनिक Python API को रैप करता है जिसका दस्तावेज [Python API](api.md) में है। Provider-backed टूल्स वही कॉन्फ़िगर किए गए प्रोवाइडर्स उपयोग करते हैं जो CLI और Python API उपयोग करते हैं। Agent-assisted टूल्स MCP होस्ट एजेंट के लिए अनुवाद करने हेतु chunks तैयार करते हैं, फिर अंतिम Markdown या नोटबुक को पुनर्निर्माण करने के लिए Co-op Translator का उपयोग करते हैं।

## चरण 1: Co-op Translator स्थापित और कॉन्फ़िगर करें

अपने MCP क्लाइंट द्वारा उपयोग किए जाने वाले Python वातावरण में Co-op Translator स्थापित करें:

```bash
pip install co-op-translator
```

लोकल डेवलपमेंट के लिए, इस रिपॉजिटरी से पैकेज को editable मोड में इंस्टॉल करें:

```bash
pip install -e .
```

अपना MCP क्लाइंट जो अनुवाद मोड उपयोग करेगा चुनें:

| मोड | इसका उपयोग करें | क्रेडेंशियल्स |
| --- | --- | --- |
| Provider-backed | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, या `run_translation` कॉल करता है। | Markdown और नोटबुक अनुवाद के लिए Azure OpenAI या OpenAI की आवश्यकता होती है। इमेज अनुवाद के लिए अतिरिक्त रूप से Azure AI Vision की आवश्यकता है। |
| Agent-assisted | MCP होस्ट एजेंट उन chunks का अनुवाद करता है जो `start_markdown_agent_translation` या `start_notebook_agent_translation` द्वारा लौटाए जाते हैं। | Markdown या नोटबुक chunks के लिए Co-op Translator LLM प्रोवाइडर क्रेडेंशियल्स आवश्यक नहीं हैं। इमेज अनुवाद अभी agent-assisted मोड द्वारा कवर नहीं किया गया है। |

यदि आप Codex या Claude Code जैसे एजेंट के अंदर Markdown या नोटबुक अनुवाद से शुरू कर रहे हैं, तो agent-assisted मोड से शुरू करें। Provider-backed मोड का उपयोग तब करें जब आप चाहें कि Co-op Translator स्वयं आपके कॉन्फ़िगर किए गए प्रोवाइडर्स को कॉल करे, जब आप छवियों का अनुवाद कर रहे हों, या जब आप CLI की तरह रिपॉजिटरी-स्तर का अनुवाद चला रहे हों।

केवल provider-backed वर्कफ़्लोज़ के लिए प्रोवाइडर क्रेडेंशियल्स कॉन्फ़िगर करें:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed इमेज अनुवाद के लिए अतिरिक्त रूप से आवश्यक है:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted मोड वर्तमान में Markdown और नोटबुक Markdown सेल्स को कवर करता है। इमेज अनुवाद अभी भी provider-backed इमेज पाइपलाइन का उपयोग करता है और OCR और लेआउट-संज्ञेय रेंडरिंग के लिए Azure AI Vision की आवश्यकता होती है।

## चरण 2: अपने MCP क्लाइंट को कॉन्फ़िगर करें

सामान्य लोकल `stdio` सेटअप के लिए, Co-op Translator को अपने MCP क्लाइंट कॉन्फ़िगरेशन में जोड़ें। क्लाइंट प्रक्रिया को स्वतः शुरू और बंद कर देगा।

इंस्टॉल किए गए पैकेज कॉन्फ़िगरेशन:

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

Windows पर सोर्स चेकआउट कॉन्फ़िगरेशन:

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

macOS या Linux पर सोर्स चेकआउट कॉन्फ़िगरेशन:

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

MCP क्लाइंट कॉन्फ़िगरेशन बदलने के बाद, नया सर्वर खोजने के लिए क्लाइंट को रीस्टार्ट या रीलोड करें।

## चरण 3: क्लाइंट में सर्वर सत्यापित करें

उपलब्ध टूल्स की सूची प्राप्त करने के लिए MCP क्लाइंट से पूछें, या पहले किसी एक read-only हेल्पर को कॉल करें:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

प्रारंभिक उपयोगी जाँचें:

| टूल | जांचने के लिए क्या है |
| --- | --- |
| `get_api_overview` | पुष्टि करता है कि सर्वर पहुँच योग्य है और उपलब्ध वर्कफ़्लोज़ दिखाता है। |
| `list_supported_languages` | पुष्टि करता है कि पैकेज्ड भाषा डेटा लोड किया जा सकता है। |
| `get_configuration_status` | पुष्टि करता है कि LLM और Vision प्रोवाइडर उपलब्ध हैं बिना गुप्त मान दिखाए। |

## चरण 4: एक वर्कफ़्लो चुनें

### व्यक्तिगत फ़ाइलें या दस्तावेज़ अनुवाद करें

जब MCP क्लाइंट के पास पहले से दस्तावेज़ सामग्री या इमेज पाथ हो और Co-op Translator को कॉन्फ़िगर किए गए अनुवाद प्रोवाइडर्स को कॉल करना चाहिए, तो provider-backed कंटेंट टूल्स का उपयोग करें।

Markdown के लिए:

1. `document`, `language_code`, और वैकल्पिक रूप से `source_path` के साथ `translate_markdown_content` कॉल करें।
2. यदि अनुवादित परिणाम Co-op Translator आउटपुट लेआउट में लिखा जाएगा, तो `rewrite_markdown_paths` कॉल करें।
3. क्लाइंट को अंतिम `content` लिखने या वापस करने दें।

नोटबुक्स के लिए:

1. नोटबुक JSON और `language_code` के साथ `translate_notebook_content` कॉल करें।
2. यदि अनुवादित नोटबुक लिंक को लक्ष्य पाथ के लिए समायोजित करने की आवश्यकता हो तो `rewrite_notebook_paths` कॉल करें।
3. अंतिम नोटबुक JSON लिखें या वापस करें।

इमेजेस के लिए:

1. `image_path`, `language_code`, और वैकल्पिक `root_dir` या `fast_mode` के साथ `translate_image_content` कॉल करें।
2. लौटाए गए `data_base64` और `mime_type` को पढ़ें।
3. यदि `output_path` प्रदान किया गया है, तो अनुवादित छवि उस पाथ पर भी सहेजी जाती है।

कंटेंट टूल्स प्रोजेक्ट डिस्कवरी, मेटाडेटा अपडेट्स, डिस्क्लेमर, या स्वचालित पाथ पुन:लेखन नहीं करते। यदि आप चाहें कि होस्ट एजेंट Co-op Translator LLM प्रोवाइडर क्रेडेंशियल्स के बिना Markdown या नोटबुक chunks का अनुवाद करे, तो नीचे agent-assisted वर्कफ़्लो का उपयोग करें।

### होस्ट एजेंट मॉडल के साथ अनुवाद

जब आप चाहें कि MCP होस्ट एजेंट, जैसे कोडिंग असिस्टेंट, अनुवादित पाठ उत्पन्न करे बजाए इसके कि आप Co-op Translator के लिए Azure OpenAI या OpenAI कॉन्फ़िगर करें, तब agent-assisted टूल्स का उपयोग करें।

एक चैट-आधारित MCP क्लाइंट में, आमतौर पर आपको टूल JSON स्वयं लिखने की आवश्यकता नहीं होती। एजेंट से agent-assisted वर्कफ़्लो का उपयोग करने के लिए कहें:

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

यदि आपका MCP क्लाइंट सर्वर प्रॉम्प्ट्स का समर्थन करता है, तो क्लाइंट को उसी वर्कफ़्लो निर्देश लोड कराने के लिए `agent_assisted_markdown_translation_prompt` का उपयोग करें।

Markdown के लिए:

1. `document`, `language_code`, और वैकल्पिक रूप से `source_path` के साथ `start_markdown_agent_translation` कॉल करें।
2. होस्ट एजेंट में लौटाए गए प्रत्येक chunk का `prompt` का पालन करके अनुवाद करें।
3. मूल `job` और `chunk_id` तथा `translated_text` का उपयोग करके अनुवादित chunks के साथ `finish_markdown_agent_translation` कॉल करें।
4. यदि सामग्री अनुवादित लक्ष्य पाथ में लिखी जाएगी, तो `rewrite_markdown_paths` कॉल करें।

नोटबुक्स के लिए:

1. नोटबुक JSON और `language_code` के साथ `start_notebook_agent_translation` कॉल करें।
2. होस्ट एजेंट में लौटाए गए प्रत्येक chunk का अनुवाद करें।
3. मूल `job` और अनुवादित chunks के साथ `finish_notebook_agent_translation` कॉल करें।
4. अनुवादित नोटबुक लिंक को लक्ष्य-पाथ समायोजन की आवश्यकता हो तो `rewrite_notebook_paths` कॉल करें।

Agent-assisted टूल्स Co-op Translator से Azure OpenAI या OpenAI को कॉल नहीं करते। लौटाए गए chunks का अनुवाद करने की जिम्मेदारी होस्ट एजेंट की होती है। Co-op Translator Markdown chunking, placeholder संरक्षण, frontmatter पुनर्निर्माण, नोटबुक सेल प्रतिस्थापन, और पोस्ट-ट्रांसलेशन सामान्यीकरण को संभालता है।

### पूरे रिपॉजिटरी का अनुवाद करें

जब उपयोगकर्ता चाहता है कि Co-op Translator CLI की तरह व्यवहार करे तो `run_translation` का उपयोग करें।

रिपॉजिटरी अनुवाद का डिफ़ॉल्ट `dry_run=true` होता है ताकि एजेंट स्कोप का निरीक्षण कर सके इससे पहले कि फ़ाइलें बदली जाएँ:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

लिखने की अनुमति देने के लिए, कॉलर को दोनों `dry_run=false` और `confirm_write=true` सेट करने होंगे:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` को `run_translation` के लिए संगतता उपनाम के रूप में एक्सपोज़ किया गया है।

### अनुवादित आउटपुट की समीक्षा करें

बिना LLM या Vision क्रेडेंशियल्स के पढ़ने-केवल जांचों के लिए `run_review` का उपयोग करें:

!!! note "Beta"
    MCP बीटा `run_review` API एक्सपोज़ करता है। यह रीड-ओनली समीक्षा वर्कफ़्लोज़ के लिए सुरक्षित है, लेकिन समीक्षा जांचें और समस्या स्कीमाएँ बदल सकती हैं।

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

परिणाम में कैप्चर किया गया टेक्स्ट आउटपुट और जब उपलब्ध हो तो एक संरचित समीक्षा सारांश शामिल होता है।

## मैनुअल सर्वर रन

मैनुअल रन मुख्यतः डीबगिंग या ऐसे ट्रांसपोर्ट्स के लिए होते हैं जो लॉन्ग-रनिंग सर्वर जैसी व्यवहार करते हैं।

डिफ़ॉल्ट stdio सर्वर को डीबग करें:

```bash
co-op-translator-mcp
```

सोर्स चेकआउट से चलाएँ:

```bash
python -m co_op_translator.mcp.server
```

लॉन्ग-लाइव्ड HTTP या SSE सर्वर चलाएँ:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

लोकल एडिटर और एजेंट इंटीग्रेशन्स के लिए, चरण 2 में क्लाइंट-मैनेज्ड `stdio` कॉन्फ़िगरेशन को प्राथमिकता दें।

## टूल्स

| टूल | प्रयोजन | फ़ाइलें लिखता है |
| --- | --- | --- |
| `translate_markdown_content` | एक Markdown स्ट्रिंग का अनुवाद करें। | नहीं |
| `translate_notebook_content` | नोटबुक JSON में Markdown सेल्स का अनुवाद करें। | नहीं |
| `translate_image_content` | एक छवि में टेक्स्ट का अनुवाद करें और base64 इमेज डेटा वापस करें। | वैकल्पिक, केवल जब `output_path` प्रदान किया गया हो |
| `start_markdown_agent_translation` | Co-op Translator LLM क्रेडेंशियल्स के बिना होस्ट एजेंट के अनुवाद के लिए Markdown chunks तैयार करें। | नहीं |
| `finish_markdown_agent_translation` | होस्ट-एजेंट द्वारा अनुवादित chunks से Markdown पुनर्निर्माण करें। | नहीं |
| `start_notebook_agent_translation` | होस्ट एजेंट के अनुवाद के लिए नोटबुक Markdown-सेल chunks तैयार करें। | नहीं |
| `finish_notebook_agent_translation` | होस्ट-एजेंट द्वारा अनुवादित chunks से नोटबुक JSON पुनर्निर्माण करें। | नहीं |
| `rewrite_markdown_paths` | अनुवादित लक्ष्य के लिए Markdown बॉडी और frontmatter पाथ्स को पुन:लिखें। | नहीं |
| `rewrite_notebook_paths` | नोटबुक Markdown सेल्स के अंदर पाथ्स को पुन:लिखें। | नहीं |
| `run_translation` | CLI की तरह प्रोजेक्ट-लेवल अनुवाद चलाएं। | हाँ जब `dry_run=false` और `confirm_write=true` |
| `translate_project` | `run_translation` के लिए संगतता उपनाम। | हाँ जब `dry_run=false` और `confirm_write=true` |
| `run_review` | निर्धार्यवादी समीक्षा जांचें चलाएँ। | नहीं |
| `get_configuration_status` | गुप्त मान दिखाए बिना कॉन्फ़िगर किए गए LLM और Vision प्रोवाइडर्स की रिपोर्ट करें। | नहीं |
| `list_supported_languages` | समर्थित लक्ष्य भाषा कोड सूचीबद्ध करें। | नहीं |
| `get_api_overview` | उपलब्ध MCP वर्कफ़्लोज़ और टूल्स का वर्णन करें। | नहीं |

## संसाधन

| Resource URI | प्रयोजन |
| --- | --- |
| `co-op://api` | वर्कफ़्लोज़ और टूल्स का JSON ओवरव्यू। |
| `co-op://supported-languages` | समर्थित भाषा कोड्स की JSON सूची। |
| `co-op://configuration` | बिना गुप्तों के प्रोवाइडर उपलब्धता सारांश का JSON। |

## प्रॉम्प्ट्स

| प्रॉम्प्ट | प्रयोजन |
| --- | --- |
| `translate_markdown_document_prompt` | कंटेंट अनुवाद और वैकल्पिक पाथ पुन:लेखन के लिए MCP क्लाइंट को मार्गदर्शन करें। |
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

अनुवादित Markdown लिंक पुन:लिखें:

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

होस्ट एजेंट मॉडल के साथ Markdown अनुवाद करें:

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

होस्ट एजेंट प्रत्येक लौटाए गए chunk का अनुवाद करने के बाद, `start_markdown_agent_translation` द्वारा लौटाए गए पूर्ण `job` ऑब्जेक्ट के साथ जॉब खत्म करें:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

रिपॉजिटरी अनुवाद का पूर्वावलोकन करें:

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
| MCP क्लाइंट `co-op-translator-mcp` नहीं ढूँढ पा रहा है। | absolute Python executable पाथ और `["-m", "co_op_translator.mcp.server"]` सोर्स चेकआउट कॉन्फ़िगरेशन का उपयोग करें। |
| सर्वर सूचीबद्ध है लेकिन अनुवाद विफल हो रहा है। | `get_configuration_status` कॉल करें और पुष्टि करें कि कोई LLM प्रोवाइडर उपलब्ध है। |
| आप Azure OpenAI/OpenAI कीज़ के बिना Markdown या नोटबुक अनुवाद चाहते हैं। | `start_markdown_agent_translation` / `finish_markdown_agent_translation` या नोटबुक समकक्षों का उपयोग करें ताकि होस्ट एजेंट chunks का अनुवाद कर सके। |
| इमेज अनुवाद विफल हो रहा है। | पुष्टि करें कि Azure AI Vision वेरिएबल्स सेट हैं और `get_configuration_status` कॉल करें। |
| रिपॉजिटरी अनुवाद फ़ाइलें नहीं लिखता। | केवल स्पष्ट उपयोगकर्ता अनुमोदन के बाद `dry_run=false` और `confirm_write=true` सेट करें। |
| क्लाइंट कॉन्फ़िग में किए गए परिवर्तन दिखाई नहीं देते। | MCP क्लाइंट को रीस्टार्ट या रीलोड करें। |

## सुरक्षा नोट्स

- MCP टूल कॉल्स होस्ट एप्लिकेशन द्वारा मॉडल-नियंत्रित होते हैं, इसलिए रिपॉजिटरी अनुवाद डिफ़ॉल्ट रूप से ड्राय-रन होता है।
- पूरा रिपॉजिटरी अनुवाद कई फाइलें बना, अपडेट, या हटाने कर सकता है। `confirm_write=true` सेट करने से पहले स्पष्ट उपयोगकर्ता अनुमोदन आवश्यक करें।
- कॉन्फ़िगरेशन स्टेटस टूल कभी भी API कीज़, endpoints, या अन्य गुप्त मान वापस नहीं करता।
- इमेज अनुवाद base64 इमेज डेटा लौटाता है। बड़ी छवियाँ बड़े टूल प्रतिक्रियाएं उत्पन्न कर सकती हैं।
- Agent-assisted टूल्स स्रोत chunks और prompts MCP होस्ट को लौटाते हैं। इन्हें केवल उस सामग्री के साथ उपयोग करें जो उपयोगकर्ता उस होस्ट एजेंट मॉडल को भेजने में सहज हो।