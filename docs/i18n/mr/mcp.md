# MCP सर्व्हर

Co-op Translator मध्ये एजंट्स, संपादक आणि MCP-सुसंगत क्लायंटसाठी Model Context Protocol सर्व्हर समाविष्ट आहे.

डिफॉल्ट लोकल सेटअपसाठी, वापरकर्ते स्वतंत्र सर्व्हर स्वतः हाताने चालवू शकत नाहीत. ते त्यांचा MCP क्लायंट कॉन्फिगर करतात, आणि क्लायंटला Co-op Translator साधनांची गरज असताना तो `stdio` वर आपोआप `co-op-translator-mcp` सुरू करतो.

जर आपण CLI, Python API आणि MCP यांपैकी निवड करत असाल, तर [आपला कार्यप्रवाह निवडा](workflows.md) पासून सुरू करा.

जेव्हा एखाद्या एजंट किंवा संपादकाने Co-op Translator ला थेट कॉल करणे आवश्यक असेल तेव्हा MCP वापरा:

| वापरकर्त्याचा उद्देश | MCP साधने |
| --- | --- |
| एक Markdown दस्तऐवज, नोटबुक, किंवा प्रतिमा अनुवादित करा | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| होस्ट एजंट मॉडेलसह Markdown किंवा नोटबुक सामग्री अनुवादित करा | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| आउटपुट पथ निवडल्यानंतर अनुवादित Markdown किंवा नोटबुक लिंक्स पुनर्लेखन करा | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI प्रमाणे पूर्ण रेपॉझिटरी अनुवादित करा | `run_translation`, `translate_project` |
| LLM क्रेडेन्शियल्स नसतानाही अनुवादित आउटपुट रीव्ह्यू करा | `run_review` |
| क्षमता आणि वातावरण स्थिती तपासा | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP सर्व्हर त्याच सार्वजनिक Python API ला व्रॅप करतो जे [Python API](api.md) मध्ये दस्तऐवजीकृत आहे. प्रोव्हायडर-आधारित साधने CLI आणि Python API प्रमाणेच कॉन्फिगर केलेले प्रोव्हायडर्स वापरतात. एजंट-सहाय्यक साधने MCP होस्ट एजंटसाठी अनुवाद करण्यासाठी चंक्स तयार करतात, आणि नंतर अंतिम Markdown किंवा नोटबुक पुनर्निर्माण करण्यासाठी Co-op Translator वापरतात.

## टप्पा 1: Co-op Translator इन्स्टॉल आणि कॉन्फिगर करा

आपल्या MCP क्लायंटने वापरणाऱ्या Python वातावरणात Co-op Translator इन्स्टॉल करा:

```bash
pip install co-op-translator
```

या रेपॉझिटरीहून लोकल विकासासाठी, पॅकेज editable मोडमध्ये इन्स्टॉल करा:

```bash
pip install -e .
```

आपल्या MCP क्लायंटने कोणता अनुवाद मोड वापरायचा हे निवडा:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, किंवा `run_translation` कॉल करतो. | Markdown आणि नोटबुक अनुवादासाठी Azure OpenAI किंवा OpenAI आवश्यक आहेत. प्रतिमा अनुवादासाठी Azure AI Vision देखील आवश्यक आहे. |
| Agent-assisted | MCP होस्ट एजंट `start_markdown_agent_translation` किंवा `start_notebook_agent_translation` ने परत केलेले चंक्स अनुवादित करतो. | Markdown किंवा नोटबुक चंक्ससाठी Co-op Translator LLM प्रोव्हायडर क्रेडेन्शियल्स आवश्यक नाहीत. प्रतिमा अनुवाद अद्याप एजंट-सहाय्यक मोडने कव्हर केलेले नाही. |

जर आपण Codex किंवा Claude Code सारख्या एजंटमध्ये Markdown किंवा नोटबुक अनुवाद सुरू करत असाल, तर एजंट-सहाय्यक मोडने प्रारंभ करा. जेव्हा आपण हवे असत तेव्हा Co-op Translator स्वतः कॉन्फिगर केलेल्या प्रोव्हायडर्सना कॉल करावा अशी इच्छा असेल, प्रतिमा अनुवाद करत असाल, किंवा CLI प्रमाणे रेपॉझिटरी-स्तरीय अनुवाद चालवत असाल तेव्हा प्रोव्हायडर-आधारित मोड वापरा.

प्रोव्हायडर-आधारित वर्कफ्लो साठी फक्त प्रोव्हायडर क्रेडेन्शियल्स कॉन्फिगर करा:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

प्रोव्हायडर-आधारित प्रतिमा अनुवादासाठी अतिरिक्तपणे आवश्यक आहे:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    एजंट-सहाय्यक मोड सध्या Markdown आणि नोटबुकच्या Markdown सेल्सवर कव्हर करतो. प्रतिमा अनुवाद अद्याप प्रोव्हायडर-आधारित इमेज पाइपलाइन वापरतो आणि OCR व लेआउट-अवेअर रेंडरिंगसाठी Azure AI Vision आवश्यक आहे.

## टप्पा 2: आपला MCP क्लायंट कॉन्फिगर करा

सामान्य स्थानिक `stdio` सेटअपसाठी, आपल्या MCP क्लायंट कॉन्फिगरेशनमध्ये Co-op Translator जोडा. क्लायंट प्रोसेस आपोआप सुरू आणि थांबवेल.

इन्स्टॉल केलेल्या पॅकेजसाठी कॉन्फिगरेशन:

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

Windows वर सोर्स चेकआउट कॉन्फिगरेशन:

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

macOS किंवा Linux वर सोर्स चेकआउट कॉन्फिगरेशन:

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

MCP क्लायंट कॉन्फिगरेशन बदलल्यानंतर, नवीन सर्व्हर शोधण्यासाठी क्लायंट रीस्टार्ट किंवा रीलोड करा.

## टप्पा 3: क्लायंटमध्ये सर्व्हर सत्यापित करा

MCP क्लायंटला उपलब्ध टूल्सची यादी विचारून किंवा प्रथम वाच-केवल हेल्पर्सपैकी कोणतीही एक कॉल करून तपासा:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

सुरुवातीस उपयुक्त तपासणी:

| Tool | काय तपासायचे |
| --- | --- |
| `get_api_overview` | सर्व्हर पोहोचण्याजोगा आहे का हे पुष्टी करतो आणि उपलब्ध वर्कफ्लो दाखवतो. |
| `list_supported_languages` | पॅकेज केलेली भाषा डेटा लोड होऊ शकते का हे पुष्टी करतो. |
| `get_configuration_status` | गुप्त मूल्ये उघड न करता LLM आणि Vision प्रोव्हायडर उपलब्धता पुष्टी करतो. |

## टप्पा 4: कामाचा प्रवाह निवडा

### स्वतंत्र फाइल्स किंवा दस्तऐवज अनुवादित करा

जर MCP क्लायंटकडे आधीपासून दस्तऐवज सामग्री किंवा प्रतिमा पथ असेल आणि Co-op Translator कॉन्फिगर केलेल्या अनुवाद प्रोव्हायडर्सना कॉल करणे अपेक्षित असेल तर प्रोव्हायडर-आधारित सामग्री साधने वापरा.

Markdown साठी:

1. `document`, `language_code`, आणि ऐच्छिक `source_path` सह `translate_markdown_content` कॉल करा.
2. अनुवादित निकाल Co-op Translator आउटपुट लेआउटमध्ये लिहिला जाईल असेल तर `rewrite_markdown_paths` कॉल करा.
3. क्लायंटला अंतिम `content` लिहायला किंवा परत करायला द्या.

नोटबुकसाठी:

1. नोटबुक JSON आणि `language_code` सह `translate_notebook_content` कॉल करा.
2. अनुवादित नोटबुक लिंक्स लक्ष्य पथानुसार समायोजित करायच्या असतील तर `rewrite_notebook_paths` कॉल करा.
3. अंतिम नोटबुक JSON लिहा किंवा परत करा.

प्रतिमांसाठी:

1. `image_path`, `language_code`, आणि ऐच्छिक `root_dir` किंवा `fast_mode` सह `translate_image_content` कॉल करा.
2. परत केलेले `data_base64` आणि `mime_type` वाचा.
3. `output_path` प्रदान केल्यास, अनुवादित प्रतिमाही त्या पथावर जतन केली जाते.

कंटेंट साधने प्रकल्प शोध, मेटाडेटा अद्यतने, डिस्क्लेमर्स, किंवा स्वयंचलित पथ पुनर्लेखन करीत नाहीत. जर आपण होस्ट एजंटला Co-op Translator LLM प्रोव्हायडर क्रेडेन्शियल्स शिवाय Markdown किंवा नोटबुक चंक्स अनुवादित करावेत असे इच्छित असाल, तर खालील एजंट-सहाय्यक वर्कफ्लो वापरा.

### होस्ट एजंट मॉडेलने अनुवाद करा

जर आपण Co-op Translator साठी Azure OpenAI किंवा OpenAI कॉन्फिगर न करता होस्ट एजंट (उदा. कोडिंग सहाय्यक) कडून अनुवादित मजकूर प्राप्त करू इच्छित असाल तर एजंट-सहाय्यक साधने वापरा.

चॅट-आधारित MCP क्लायंटमध्ये, सामान्यतः आपल्याला टूल JSON स्वतः लिहिण्याची गरज नाही. एजंटला एजंट-सहाय्यक वर्कफ्लो वापरण्यास सांगा:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

नोटबुकसाठी, त्याच नमुन्याचा वापर करा:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

जर आपला MCP क्लायंट सर्व्हर प्रॉम्प्ट्सना समर्थन देत असेल, तर क्लायंटला समान वर्कफ्लो सूचनां लोड करण्यासाठी `agent_assisted_markdown_translation_prompt` वापरा.

Markdown साठी:

1. `document`, `language_code`, आणि ऐच्छिक `source_path` सह `start_markdown_agent_translation` कॉल करा.
2. परत केलेल्या प्रत्येक चंकचे `prompt` अनुसरून होस्ट एजंटमध्ये अनुवाद करा.
3. मूळ `job` आणि `chunk_id` व `translated_text` वापरून अनुवादित चंक्ससह `finish_markdown_agent_translation` कॉल करा.
4. सामग्री अनुवादित लक्ष्य पथावर लिहिली जाणार असेल तर `rewrite_markdown_paths` कॉल करा.

नोटबुकसाठी:

1. नोटबुक JSON आणि `language_code` सह `start_notebook_agent_translation` कॉल करा.
2. परत केलेले प्रत्येक चंक होस्ट एजंटमध्ये अनुवाद करा.
3. मूळ `job` आणि अनुवादित चंक्ससह `finish_notebook_agent_translation` कॉल करा.
4. अनुवादित नोटबुक लिंक्सना लक्ष्य-पथ समायोजन आवश्यक असल्यास `rewrite_notebook_paths` कॉल करा.

एजंट-सहाय्यक साधने Co-op Translator मधून Azure OpenAI किंवा OpenAI ला कॉल करत नाहीत. परत केलेले चंक्स अनुवादित करण्याची जबाबदारी होस्ट एजंटची आहे. Co-op Translator Markdown चंकिंग, प्लेसहोल्डर जतन करणे, फ्रंटमॅटर पुनर्निर्माण, नोटबुक सेल रिप्लेसमेंट, आणि अनुवादानंतर सामान्यीकरण हाताळतो.

### संपूर्ण रेपॉझिटरी अनुवादित करा

जेव्हा वापरकर्ता Co-op Translator ला `translate` CLI प्रमाणे काम करावयाचे असेल तेव्हा `run_translation` वापरा.

रेपॉझिटरी अनुवाद डिफॉल्टने `dry_run=true` असतो जेणेकरून एजंट फायली बदलण्यापूर्वी स्कोप तपासू शकेल:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

लिखण्याची परवानगी देण्यासाठी, कॉल करणाऱ्याने दोन्ही `dry_run=false` आणि `confirm_write=true` सेट करणे आवश्यक आहे:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` हा `run_translation` साठी सुसंगत अलियास म्हणून एक्स्पोज केला गेला आहे.

### अनुवादित आउटपुट पुनरावलोकन करा

LLM किंवा Vision क्रेडेन्शियल्सची आवश्यकता नसलेल्या ठराविक तपासण्या (`deterministic checks`) साठी `run_review` वापरा:

!!! note "बीटा"
    MCP बीटा `run_review` API एक्स्पोज करतो. वाचन-केवळ पुनरावलोकन वर्कफ्लोसाठी ते सुरक्षित आहे, परंतु पुनरावलोकन तपासण्या आणि इश्यू स्कीम्स विकसित होऊ शकतात.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

निकालामध्ये कॅप्चर केलेले टेक्स्ट आउटपुट आणि उपलब्ध असेल तर संरचित पुनरावलोकन सारांश समाविष्ट आहे.

## मॅन्युअल सर्व्हर रन

मॅन्युअल रन मुख्यतः डीबगिंगसाठी किंवा दीर्घकाळ चालणाऱ्या सर्व्हरप्रमाणे वागणाऱ्या ट्रान्सपोर्टसाठी असतात.

डिफॉल्ट stdio सर्व्हर डीबग करा:

```bash
co-op-translator-mcp
```

सोर्स चेकआउटमधून चालवा:

```bash
python -m co_op_translator.mcp.server
```

दीर्घकालीन HTTP किंवा SSE सर्व्हर चालवा:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

लोकल संपादक आणि एजंट इंटिग्रेशनसाठी, टप्पा 2 मधील क्लायंट-व्यवस्थित `stdio` कॉन्फिगरेशन प्राधान्य द्या.

## साधने

| Tool | उद्देश | फाइल लिहिते |
| --- | --- | --- |
| `translate_markdown_content` | Markdown स्ट्रिंग अनुवादित करा. | नाही |
| `translate_notebook_content` | नोटबुक JSON मधील Markdown सेल्स अनुवादित करा. | नाही |
| `translate_image_content` | एका प्रतिमेतील मजकूर अनुवादित करा आणि base64 इमेज डेटा परत करा. | ऐच्छिक, केवळ जेव्हा `output_path` प्रदान केले असेल |
| `start_markdown_agent_translation` | होस्ट एजंटला Co-op Translator LLM प्रोव्हायडर क्रेडेन्शियल्स शिवाय अनुवादासाठी Markdown चंक्स तयार करा. | नाही |
| `finish_markdown_agent_translation` | होस्ट-एजंट अनुवादित चंक्समधून Markdown पुन्हा बनवा. | नाही |
| `start_notebook_agent_translation` | होस्ट एजंटसाठी नोटबुक Markdown-सेल चंक्स तयार करा. | नाही |
| `finish_notebook_agent_translation` | होस्ट-एजंट अनुवादित चंक्समधून नोटबुक JSON पुनर्निर्मित करा. | नाही |
| `rewrite_markdown_paths` | अनुवादित लक्ष्यासाठी Markdown बॉडी आणि फ्रंटमॅटर पाथ्स पुनर्लेखन करा. | नाही |
| `rewrite_notebook_paths` | नोटबुक Markdown सेल्समधील पाथ्स पुनर्लेखन करा. | नाही |
| `run_translation` | CLI प्रमाणे प्रोजेक्ट-स्तरीय अनुवाद चालवा. | होय जेव्हा `dry_run=false` आणि `confirm_write=true` |
| `translate_project` | `run_translation` साठी सुसंगत अलियास. | होय जेव्हा `dry_run=false` आणि `confirm_write=true` |
| `run_review` | ठराविक पुनरावलोकन तपासण्या चालवा. | नाही |
| `get_configuration_status` | गुप्त माहिती न उघडता कॉन्फिगर केलेले LLM आणि Vision प्रोव्हायडर्स रिपोर्ट करा. | नाही |
| `list_supported_languages` | समर्थित लक्ष्य भाषा कोडांची यादी करा. | नाही |
| `get_api_overview` | उपलब्ध MCP वर्कफ्लो आणि साधने वर्णन करा. | नाही |

## संसाधने

| Resource URI | उद्देश |
| --- | --- |
| `co-op://api` | वर्कफ्लो आणि साधनांची JSON ओव्हरव्ह्यू. |
| `co-op://supported-languages` | समर्थित भाषा कोडांची JSON यादी. |
| `co-op://configuration` | गुप्तांशांशिवाय प्रोव्हायडर उपलब्धतेचा JSON सारांश. |

## प्रॉम्प्ट्स

| Prompt | उद्देश |
| --- | --- |
| `translate_markdown_document_prompt` | कंटेंट अनुवाद आणि ऐच्छिक पथ पुनर्लेखन मार्गदर्शन करण्यासाठी MCP क्लायंटचे मार्गदर्शन करा. |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM प्रोव्हायडर क्रेडेन्शियल्स नसतानाही होस्ट-एजंट Markdown अनुवादासाठी MCP क्लायंटचे मार्गदर्शन करा. |
| `translate_repository_prompt` | प्रथम dry-run करून रेपॉझिटरी अनुवादासाठी MCP क्लायंटचे मार्गदर्शन करा. |

## कॉपी-पेस्ट उदाहरणे

Markdown सामग्री अनुवादित करा:

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

अनुवादित Markdown लिंक्स पुनर्लेखन करा:

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

होस्ट एजंट मॉडेलनुसार Markdown अनुवाद करा:

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

होस्ट एजंटने परत केलेल्या प्रत्येक चंकचे अनुवाद केल्यानंतर, `start_markdown_agent_translation` ने परत केलेल्या पूर्ण `job` ऑब्जेक्टसह जॉब पूर्ण करा:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

रेपॉझिटरी अनुवाद प्रीव्ह्यू करा:

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

| समस्या | काय करायला हवे |
| --- | --- |
| MCP क्लायंट `co-op-translator-mcp` सापडवू शकत नाही. | पूर्ण Python एक्झिक्युटेबल पथ आणि `["-m", "co_op_translator.mcp.server"]` सोर्स चेकआउट कॉन्फिगरेशन वापरा. |
| सर्व्हर सूचीबद्ध आहे परंतु अनुवाद अयशस्वी होतो. | `get_configuration_status` कॉल करा आणि LLM प्रोव्हायडर उपलब्ध आहे का ते पुष्टी करा. |
| आपण Azure OpenAI/OpenAI कीशिवाय Markdown किंवा नोटबुक अनुवाद हवे आहे. | `start_markdown_agent_translation` / `finish_markdown_agent_translation` किंवा नोटबुक समतुल्य वापरा जेणेकरून होस्ट एजंट चंक्स अनुवादित करेल. |
| प्रतिमा अनुवाद अयशस्वी होतो. | Azure AI Vision व्हेरीएबल्स सेट केलेले आहेत का ते पुष्टी करा आणि `get_configuration_status` कॉल करा. |
| रेपॉझिटरी अनुवाद फाइल्स लिहित नाही. | वापरकर्त्याच्या स्पष्ट मंजुरीनंतरच `dry_run=false` आणि `confirm_write=true` सेट करा. |
| क्लायंट कॉन्फिगमध्ये बदल दिसत नाहीत. | MCP क्लायंट रीस्टार्ट किंवा रीलोड करा. |

## सुरक्षा टीपा

- MCP टूल कॉल्स होस्ट अनुप्रयोगाद्वारे मॉडेल-नियंत्रित असतात, त्यामुळे रेपॉझिटरी अनुवाद डीफॉल्टने dry-run असतो.
- पूर्ण रेपॉझिटरी अनुवाद अनेक फाईल्स तयार, अपडेट किंवा काढून टाकू शकतो. `confirm_write=true` सेट करण्यापूर्वी स्पष्ट वापरकर्ता मंजुरी आवश्यक आहे.
- कॉन्फिगरेशन स्थिती टूल कधीही API कीز, एंडपॉइंट्स किंवा इतर गुप्त मूल्ये परत करत नाही.
- प्रतिमा अनुवाद base64 इमेज डेटा परत करतो. मोठ्या प्रतिमा मोठे टूल प्रतिसाद उत्पन्न करू शकतात.
- एजंट-सहाय्यक साधने स्रोत चंक्स आणि प्रॉम्प्ट्स MCP होस्टकडे परत करतात. फक्त अशा सामग्रीसाठी त्यांचा वापर करा ज्याबद्दल वापरकर्ता त्या होस्ट एजंट मॉडेलकडे पाठवण्यास सभ्य आहे.