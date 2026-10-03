# MCP सर्व्हर

Co-op Translator मध्ये एजंट्स, संपादक आणि MCP-सुसंगत क्लायंटसाठी Model Context Protocol सर्व्हर समाविष्ट आहे.

डिफॉल्ट स्थानिक सेटअपसाठी, वापरकर्ते स्वतंत्र सर्व्हर हस्तचाळवणीने सुरू ठेवत नाहीत. ते त्यांचा MCP क्लायंट कॉन्फिगर करतात, आणि क्लायंटला Co-op Translator उपकरणे लागल्यावर तो `stdio` वर `co-op-translator-mcp` आपोआप सुरू करतो.

जर तुम्ही CLI, Python API आणि MCP यांच्यामध्ये निर्णय घेत असाल, तर [तुमचा कार्यप्रवाह निवडा](workflows.md) पासून सुरू करा.

जेव्हा एखाद्या एजंट किंवा एडिटरने Co-op Translator ला थेट कॉल करायला हवे तेव्हा MCP वापरा:

| वापरकर्त्याचा उद्देश | MCP टूल्स |
| --- | --- |
| एक Markdown दस्तऐवज, नोटबुक किंवा प्रतिमा भाषांतरित करा | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| होस्ट एजंट मॉडेल वापरून Markdown किंवा नोटबुक सामग्री भाषांतरित करा | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| आउटपुट पथ निवडल्यानंतर अनुवादित Markdown किंवा नोटबुकच्या दुव्यांचे पुनर्लेखन करा | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI प्रमाणे पूर्ण रेपॉझिटरी भाषांतरित करा | `run_translation`, `translate_project` |
| LLM क्रेडेन्शियल्स न देता अनुवादित आउटपुटचा आढावा घ्या | `run_review` |
| क्षमता आणि वातावरणाची स्थिती तपासा | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP सर्व्हर त्याच सार्वजनिक Python API ला व्रॅप करते जे [Python API](api.md) मध्ये दस्तऐवजीकृत आहे. Provider-backed टूल्स CLI आणि Python API सारखेच कॉन्फिगर केलेले providers वापरतात. Agent-assisted टूल्स MCP होस्ट एजंटसाठी भाषांतर करण्यासाठी chunks तयार करतात, नंतर अंतिम Markdown किंवा नोटबुक पुन्हा तयार करण्यासाठी Co-op Translator वापरतात.

## टप्पा 1: Co-op Translator स्थापित करा आणि कॉन्फिगर करा

तुमच्या MCP क्लायंटने वापरणार्‍या Python वातावरणात Co-op Translator स्थापित करा:

```bash
pip install co-op-translator
```

या रेपॉझिटरीमधून स्थानिक विकासासाठी, पॅकेज editable मोडमध्ये स्थापित करा:

```bash
pip install -e .
```

तुमचा MCP क्लायंट कोणता अनुवाद मोड वापरेल ते निवडा:

| मोड | हे कोणासाठी वापरा | क्रेडेन्शियल्स |
| --- | --- | --- |
| Provider-backed | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, किंवा `run_translation` कॉल करते. | भाषांतरासाठी Azure OpenAI, OpenAI किंवा Anthropic आवश्यक आहे. प्रतिमा भाषांतरासाठी Azure AI Vision देखील आवश्यक आहे. |
| Agent-assisted | MCP होस्ट एजंट `start_markdown_agent_translation` किंवा `start_notebook_agent_translation` द्वारे परत केलेले chunks भाषांतरित करतो. | Markdown किंवा नोटबुक chunks साठी Co-op Translator LLM provider क्रेडेन्शियल्स आवश्यक नाहीत. प्रतिमा भाषांतर अजून agent-assisted मोडमध्ये समाविष्ट नाही. |

जर तुम्ही Codex किंवा Claude Code सारख्या एजंटच्या आत Markdown किंवा नोटबुक भाषांतराने सुरू करत असाल, तर agent-assisted मोडपासून प्रारंभ करा. Provider-backed मोड वापरा जेव्हा तुम्हाला Co-op Translator स्वतः तुमचे कॉन्फिगर केलेले providers कॉल करावे, जेव्हा तुम्ही प्रतिमा भाषांतरित करत असता, किंवा जेव्हा तुम्ही CLI सारखे रेपॉझिटरी-स्तरीय भाषांतर चालवत आहात.

Provider-backed वर्कफ्लोसाठी एक provider कॉन्फिगर करा:

```bash
# अॅझ्यूर ओपनएआय
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# किंवा ओपनएआय
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# किंवा अँथ्रोपिक
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Provider-backed प्रतिमा भाषांतरासाठी अतिरिक्तपणे आवश्यक:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted मोड सध्या Markdown आणि नोटबुकमधील Markdown सेल्स कव्हर करतो. प्रतिमा भाषांतर अद्याप provider-backed प्रतिमा पाइपलाइन वापरते आणि OCR आणि लेआउट-आधारित रेंडरिंगसाठी Azure AI Vision आवश्यक आहे.

## टप्पा 2: तुमचा MCP क्लायंट कॉन्फिगर करा

सामान्य स्थानिक `stdio` सेटअपसाठी, Co-op Translator तुमच्या MCP क्लायंट कॉन्फिगरेशनमध्ये जोडा. क्लायंट हा प्रोसेस आपोआप सुरू आणि थांबवेल.

स्थापित पॅकेज कॉन्फिगरेशन:

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

Windows वर स्रोत चेकआउट कॉन्फिगरेशन:

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

macOS किंवा Linux वर स्रोत चेकआउट कॉन्फिगरेशन:

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

MCP क्लायंट कॉन्फिगरेशन बदलल्यानंतर, क्लायंटला नवीन सर्व्हर शोधता यावा म्हणून क्लायंट रीस्टार्ट किंवा री-लोड करा.

## टप्पा 3: क्लायंटमध्ये सर्व्हरची पडताळणी करा

उपलब्ध टूल्सची यादी करण्यासाठी MCP क्लायंटला विचारा, किंवा आधी वाचण्यालायक हेल्पर्सपैकी एक कॉल करा:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

उपयुक्त प्रथम तपासण्या:

| टूल | काय तपासावे |
| --- | --- |
| `get_api_overview` | सर्व्हर पोहोचण्यायोग्य आहे याची पुष्टी करतो आणि उपलब्ध वर्कफ्लो दाखवतो. |
| `list_supported_languages` | पॅकेज केलेला भाषा डेटा लोड होऊ शकतो याची पुष्टी करतो. |
| `get_configuration_status` | गुप्त मूल्ये उघड न करता LLM आणि Vision provider उपलब्धता पुष्टी करतो. |

## टप्पा 4: एक वर्कफ्लो निवडा

### वैयक्तिक फाईल्स किंवा दस्तऐवज भाषांतरित करा

जेव्हा MCP क्लायंटकडे आधीच दस्तऐवज सामग्री किंवा प्रतिमा पाथ असतो आणि Co-op Translator ने कॉन्फिगर केलेल्या translation providers कॉल करायचे असतील तेव्हा provider-backed content टूल्स वापरा.

Markdown साठी:

1. `document`, `language_code`, आणि ऐच्छिकपणे `source_path` सह `translate_markdown_content` कॉल करा.
2. जर अनुवादित निकाल Co-op Translator आउटपुट लेआउटमध्ये लिहिला जाणार असेल, तर `rewrite_markdown_paths` कॉल करा.
3. क्लायंटला अंतिम `content` लिहू द्या किंवा परत करा.

नोटबुकसाठी:

1. नोटबुक JSON आणि `language_code` सह `translate_notebook_content` कॉल करा.
2. जर अनुवादित नोटबुक दुव्यांना लक्ष्य पथानुसार समायोजित करणे आवश्यक असेल तर `rewrite_notebook_paths` कॉल करा.
3. अंतिम नोटबुक JSON लिहा किंवा परत करा.

प्रतिमांसाठी:

1. `image_path`, `language_code`, आणि ऐच्छिक `root_dir` किंवा `fast_mode` सह `translate_image_content` कॉल करा.
2. परत आलेले `data_base64` आणि `mime_type` वाचा.
3. जर `output_path` दिलेले असेल तर, अनुवादित प्रतिमा त्या पथावरही जतन केली जाते.

कंटेंट टूल्स प्रोजेक्ट डिस्कवरी, मेटाडेटा अपडेट्स, डिस्क्लेमर्स किंवा स्वयंचलित पाथ पुनर्लेखन करत नाहीत. जर तुम्हाला होस्ट एजंटने Co-op Translator LLM provider क्रेडेन्शियल्स शिवाय Markdown किंवा नोटबुक chunks भाषांतर करावे असेल तर खालील agent-assisted वर्कफ्लो वापरा.

### होस्ट एजंट मॉडेलसह भाषांतर करा

जेव्हा तुम्हाला Co-op Translator साठी LLM provider कॉन्फिगर न करता MCP होस्ट एजंट, उदा. एक कोडिंग सहाय्यक, अनुवादित मजकूर तयार करावा असे वाटते तेव्हा agent-assisted टूल्स वापरा.

चॅट-आधारित MCP क्लायंटमध्ये, सामान्यतः तुम्हाला टूल JSON स्वतः लिहिण्याची गरज नाही. एजंटला agent-assisted वर्कफ्लो वापरायला विचारा:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

नोटबुकसाठी, तीच पद्धत वापरा:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

जर तुमचा MCP क्लायंट सर्व्हर प्रॉम्प्टस समर्थन करतो, तर क्लायंटला तीच वर्कफ्लो सूचना लोड करण्यासाठी `agent_assisted_markdown_translation_prompt` वापरा.

Markdown साठी:

1. `document`, `language_code`, आणि ऐच्छिकपणे `source_path` सह `start_markdown_agent_translation` कॉल करा.
2. परत आलेल्या प्रत्येक chunk चे `prompt` अनुसरून होस्ट एजंटमध्ये भाषांतर करा.
3. मूळ `job` आणि `chunk_id` आणि `translated_text` वापरून अनुवादित chunks सह `finish_markdown_agent_translation` कॉल करा.
4. जर सामग्री अनुवादित लक्ष्य पथावर लिहिली जाणार असेल तर `rewrite_markdown_paths` कॉल करा.

नोटबुकसाठी:

1. नोटबुक JSON आणि `language_code` सह `start_notebook_agent_translation` कॉल करा.
2. परत आलेल्या प्रत्येक chunk होस्ट एजंटमध्ये भाषांतर करा.
3. मूळ `job` आणि अनुवादित chunks सह `finish_notebook_agent_translation` कॉल करा.
4. जर अनुवादित नोटबुक दुव्यांना लक्ष्य-पथ समायोजनाची गरज असेल तर `rewrite_notebook_paths` कॉल करा.

Agent-assisted टूल्स Co-op Translator मधून कॉन्फिगर केलेल्या LLM provider ला कॉल करत नाहीत. परत आलेल्या chunks चे भाषांतर करण्याचे जबाबदारी होस्ट एजंटवर आहे. Co-op Translator Markdown chunking, placeholder संरक्षण, frontmatter पुनर्निर्मिती, नोटबुक सेल बदल आणि अनुवादानंतरचे सामान्यीकरण हाताळतो.

### संपूर्ण रेपॉझिटरीचे भाषांतर करा

जेव्हा वापरकर्ता Co-op Translator ला `translate` CLI प्रमाणे वागावे असे इच्छितो तेव्हा `run_translation` वापरा.

रेपॉझिटरी भाषांतराचे डीफॉल्ट `dry_run=true` असते जेणेकरून एजंट फाईल बदलापूर्वी परिमाण तपासू शकेल:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

`run_translation` च्या निकालात आवृत्त-आधारित (versioned) `events` अ‍ॅरे समाविष्ट असतो
`co-op.translation.event.v1` प्रगती इव्हेंट्स. MCP क्लायंट्सना खालील
फील्ड्स जसे `type`, `stage_key`, `completed`, `total`, आणि `current_path` वापरावीत,
कॅप्चर केलेला कन्सोल मजकूर पार्स करण्याऐवजी. `json_events_path` पास केल्यास हे
इव्हेंट्स NDJSON फाइलमध्येही लिहिले जातील.

लेखनास परवानगी देण्यासाठी, कॉल करणाऱ्याने दोन्ही `dry_run=false` आणि `confirm_write=true` सेट केले पाहिजेत:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` हे `run_translation` साठी सुसंगतता उपनाम (compatibility alias) म्हणून उपलब्ध केले आहे.

### अनुवादित आउटपुटचे पुनरावलोकन

`run_review` वापरा त्या निर्णायक तपासणीसाठी ज्यात LLM किंवा Vision क्रेडेन्शियल्सची आवश्यकता नसते:

!!! note "Beta"
    MCP बीटा `run_review` API उघडते. हे केवळ-वाचन पुनरावलोकन वर्कफ्लोजसाठी सुरक्षित आहे, परंतु पुनरावलोकन तपासण्या आणि समस्या schemas यांमध्ये बदल होऊ शकतात.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

निकालात कॅप्चर केलेले मजकूर आउटपुट आणि उपलब्ध असल्यास संरचित पुनरावलोकन सारांश समाविष्ट असतो.

## मॅन्युअल सर्व्हर चालवा

मॅन्युअल रन मुख्यतः डीबगिंगसाठी किंवा अशा ट्रान्सपोर्टसाठी आहेत जे दीर्घकाल चालणाऱ्या सर्व्हर्सप्रमाणे वागतात.

डीबग करा डिफॉल्ट stdio सर्व्हर:

```bash
co-op-translator-mcp
```

स्रोत चेकआउटमधून चालवा:

```bash
python -m co_op_translator.mcp.server
```

दीर्घकालीन HTTP किंवा SSE सर्व्हर चालवा:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

स्थानिक एडिटर आणि एजंट एकीकरणांसाठी, टप्पा 2 मधील क्लायंट-व्यवस्थापित `stdio` कॉन्फिगरेशन प्राधान्य द्या.

## टूल्स

| टूल | उद्देश | फाईल्स लिहिते |
| --- | --- | --- |
| `translate_markdown_content` | Markdown स्ट्रिंगचे भाषांतर करा. | नाही |
| `translate_notebook_content` | नोटबुक JSON मधील Markdown सेल्सचे भाषांतर करा. | नाही |
| `translate_image_content` | एका प्रतिमेतील मजकूर भाषांतर करा आणि base64 प्रतिमा डेटा परत करा. | ऐच्छिक, फक्त जेव्हा `output_path` प्रदान केले आहे |
| `start_markdown_agent_translation` | Co-op Translator LLM क्रेडेन्शियल्स न वापरता होस्ट एजंटसाठी Markdown chunks तयार करा. | नाही |
| `finish_markdown_agent_translation` | होस्ट-एजंटने अनुवादित केलेल्या chunks मधून Markdown पुनर्निर्मित करा. | नाही |
| `start_notebook_agent_translation` | होस्ट एजंटसाठी नोटबुकमधील Markdown-सेल chunks तयार करा. | नाही |
| `finish_notebook_agent_translation` | होस्ट-एजंटने अनुवादित केलेल्या chunks मधून नोटबुक JSON पुनर्निर्मित करा. | नाही |
| `rewrite_markdown_paths` | अनुवादित लक्ष्यासाठी Markdown बॉडी आणि frontmatter पथ पुनर्लेखन करा. | नाही |
| `rewrite_notebook_paths` | नोटबुक Markdown सेल्समधील पथ पुनर्लेखन करा. | नाही |
| `run_translation` | CLI प्रमाणे प्रोजेक्ट-स्तरीय भाषांतर चालवा. | हो, जेव्हा `dry_run=false` आणि `confirm_write=true` असेल |
| `translate_project` | `run_translation` साठी सुसंगतता उपनाम. | हो, जेव्हा `dry_run=false` आणि `confirm_write=true` असेल |
| `run_review` | निर्णायक पुनरावलोकन तपासण्या चला. | नाही |
| `get_configuration_status` | गुप्त न उघडता कॉन्फिगर केलेले LLM आणि Vision providers रिपोर्ट करा. | नाही |
| `list_supported_languages` | समर्थित लक्ष्य भाषा कोड्सची यादी करा. | नाही |
| `get_api_overview` | उपलब्ध MCP वर्कफ्लो आणि टूल्सचे वर्णन करा. | नाही |

## संसाधने

| Resource URI | उद्देश |
| --- | --- |
| `co-op://api` | वर्कफ्लो आणि टूल्स यांचा JSON आढावा. |
| `co-op://supported-languages` | समर्थित भाषा कोड्सची JSON यादी. |
| `co-op://configuration` | गुप्ते उघड न करता provider उपलब्धतेचा JSON सारांश. |

## प्रॉम्प्ट्स

| प्रॉम्प्ट | उद्देश |
| --- | --- |
| `translate_markdown_document_prompt` | सामग्री भाषांतर आणि ऐच्छिक पथ पुनर्लेखनाद्वारे MCP क्लायंट मार्गदर्शन करा. |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM provider क्रेडेन्शियल्स न वापरता होस्ट-एजंट Markdown भाषांतराद्वारे MCP क्लायंट मार्गदर्शन करा. |
| `translate_repository_prompt` | प्रथम dry-run असलेल्या रेपॉझिटरी भाषांतराद्वारे MCP क्लायंट मार्गदर्शन करा. |

## कॉपी-पेस्ट उदाहरणे

Markdown सामग्री भाषांतरित करा:

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

अनुवादित Markdown दुव्यांचे पुनर्लेखन करा:

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

होस्ट एजंट मॉडेलसह Markdown भाषांतर करा:

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

होस्ट एजंटने परत केलेला प्रत्येक chunk अनुवादित केल्यानंतर, `start_markdown_agent_translation` ने परत केलेल्या पूर्ण `job` ऑब्जेक्टसह जॉब पूर्ण करा:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

रेपॉझिटरी भाषांतर पूर्वावलोकन करा:

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

| समस्या | काय प्रयत्न करावे |
| --- | --- |
| MCP क्लायंटला `co-op-translator-mcp` सापडत नाही. | absolute Python executable path वापरा आणि `["-m", "co_op_translator.mcp.server"]` स्रोत चेकआउट कॉन्फिगरेशन वापरा. |
| सर्व्हर सूचीबद्ध आहे परंतु भाषांतर अयशस्वी होते. | `get_configuration_status` कॉल करा आणि LLM provider उपलब्ध आहे की नाही याची पुष्टी करा. |
| तुम्हाला provider क्रेडेन्शियल्स न देता Markdown किंवा नोटबुक भाषांतर हवे आहे. | `start_markdown_agent_translation` / `finish_markdown_agent_translation` किंवा नोटबुक समतुल्य वापरा जेणेकरून होस्ट एजंट chunks चे भाषांतर करेल. |
| प्रतिमा भाषांतर अयशस्वी होते. | Azure AI Vision व्हेरिएबले सेट आहेत का ते पुष्टी करा आणि `get_configuration_status` कॉल करा. |
| रेपॉझिटरी भाषांतर फाइल्स लिहीत नाही. | `dry_run=false` आणि `confirm_write=true` केवळ स्पष्ट वापरकर्ता अनुमोदनानंतर सेट करा. |
| क्लायंट कॉन्फिगमध्ये बदल दिसत नाहीत. | MCP क्लायंट रीस्टार्ट किंवा री-लोड करा. |

## सुरक्षितता टिपा

- MCP टूल कॉल होस्ट अ‍ॅप्लिकेशनद्वारे मॉडेल-नियंत्रित असतात, त्यामुळे रेपॉझिटरी भाषांतर डीफॉल्टनुसार dry-run असते.
- पूर्ण रेपॉझिटरी भाषांतराने अनेक फाईल्स तयार, अपडेट किंवा हटवू शकतात. `confirm_write=true` सेट करण्यापूर्वी स्पष्ट वापरकर्ता मंजुरी मागा.
- कॉन्फिगरेशन स्टेटस टूल कधीही API कीज, endpoints किंवा इतर गुप्त मूल्ये परत करत नाही.
- प्रतिमा भाषांतर base64 प्रतिमा डेटा परत करते. मोठ्या प्रतिमांमुळे टूल प्रतिसाद मोठे होऊ शकतात.
- Agent-assisted टूल्स स्रोत chunks आणि प्रॉम्प्ट्स MCP होस्टकडे परत करतात. त्या होस्ट एजंट मॉडेलनडे पाठवायला वापरकर्ता ज्याच्या सामग्रीबद्दल आरामदायी आहे त्याच्यासहच वापरा.