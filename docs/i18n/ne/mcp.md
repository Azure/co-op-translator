# MCP सर्भर

Co-op Translator मा एजेन्टहरू, सम्पादकहरू, र MCP-संग मिल्ने क्लाइन्टहरूका लागि Model Context Protocol सर्भर समावेश छ।

डिफल्ट स्थानीय सेटअपको लागि, प्रयोगकर्ताहरूले छुट्टै सर्भर हातैले चलाएर राख्दैनन्। तिनीहरूले आफ्नो MCP क्लाइन्ट कन्फिगर गर्छन्, र क्लाइन्टले Co-op Translator उपकरणहरू चाहिँदा `co-op-translator-mcp` लाई `stdio` मार्फत स्वचालित रूपमा सुरु गर्छ।

यदि तपाईं CLI, Python API, र MCP बीच निर्णय गर्दै हुनुहुन्छ भने [आफ्नो कार्यप्रवाह छनौट गर्नुहोस्](workflows.md) बाट सुरु गर्नुहोस्।

जब एजेन्ट वा सम्पादकले Co-op Translator लाई सिधै कल गर्नुपर्छ तब MCP प्रयोग गर्नुहोस्:

| प्रयोगकर्ताको लक्ष्य | MCP उपकरणहरू |
| --- | --- |
| एक Markdown दस्तावेज, नोटबुक, वा छवि अनुवाद गर्नुहोस् | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| होस्ट एजेन्ट मोडेलसँग Markdown वा नोटबुक सामग्री अनुवाद गर्नुहोस् | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| आउटपुट पथ छानेपछि अनुवादित Markdown वा नोटबुक लिङ्कहरू पुनर्लेखन गर्नुहोस् | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI जस्तै पूर्ण रिपोजिटरी अनुवाद गर्नुहोस् | `run_translation`, `translate_project` |
| LLM क्रेडेन्सियल्स बिना अनुवादित आउटपुट समीक्षा गर्नुहोस् | `run_review` |
| क्षमताहरू र वातावरणको स्थिति निरीक्षण गर्नुहोस् | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP सर्भरले [Python API](api.md) मा डकुमेन्ट गरिएको उस्तै सार्वजनिक Python API लाई र्‍याप गर्छ। प्रदायक-समर्थित उपकरणहरूले CLI र Python API जसरी कन्फिगर गरिएका प्रदायकहरू प्रयोग गर्छन्। एजेन्ट-समर्थित उपकरणहरूले MCP होस्ट एजेन्टले अनुवाद गर्नका लागि chunks तयार गर्छन्, त्यसपछि Co-op Translator लाई प्रयोग गरेर अन्तिम Markdown वा नोटबुक पुनर्निर्माण गर्छन्।

## चरण 1: Co-op Translator इन्स्टल र कन्फिगर गर्नुहोस्

आफ्नो MCP क्लाइन्टले प्रयोग गर्ने Python वातावरणमा Co-op Translator इन्स्टल गर्नुहोस्:

```bash
pip install co-op-translator
```

यो रिपोजिटरीबाट स्थानीय विकासका लागि प्याकेजलाई editable मोडमा इन्स्टल गर्नुहोस्:

```bash
pip install -e .
```

तपाईंको MCP क्लाइन्टले प्रयोग गर्ने अनुवाद मोड चयन गर्नुहोस्:

| मोड | यसलाई प्रयोग गर्नुहोस् | क्रेडेन्सियल्स |
| --- | --- | --- |
| प्रदायक-समर्थित | Co-op Translator ले `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, वा `run_translation` कल गर्छ। | अनुवादका लागि Azure OpenAI, OpenAI, वा Anthropic आवश्यक हुन्छ। छवि अनुवादका लागि Azure AI Vision पनि आवश्यक छ। |
| एजेन्ट-सहायित | MCP होस्ट एजेन्टले `start_markdown_agent_translation` वा `start_notebook_agent_translation` बाट फर्किएका chunks अनुवाद गर्छ। | Markdown वा नोटबुक chunks का लागि Co-op Translator LLM प्रदायक क्रेडेन्सियल्स आवश्यक पर्दैन। छवि अनुवाद हाल एजेन्ट-सहायित मोडले समेटेको छैन। |

यदि तपाईं Codex वा Claude Code जस्ता एजेन्ट भित्र Markdown वा नोटबुक अनुवादबाट सुरु गर्दै हुनुहुन्छ भने एजेन्ट-सहायित मोडबाट सुरु गर्नुहोस्। जब तपाईं चाहनुहुन्छ Co-op Translator आफैले तपाईंले कन्फिगर गरेका प्रदायकहरूलाई कल गरोस्, छविहरू अनुवाद गर्नु परोस्, वा CLI जस्तै रिपोजिटरी-स्तर अनुवाद चलाउनु परोस् तब प्रदायक-समर्थित मोड प्रयोग गर्नुहोस्।

प्रदायक-समर्थित वर्कफ्लोजका लागि एउटा प्रदायक कन्फिगर गर्नुहोस्:

```bash
# एज़्योर ओपनएआई
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# वा ओपनएआई
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# वा एन्थ्रोपिक
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

प्रदायक-समर्थित छवि अनुवादका लागि थप आवश्यक:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    एजेण्ट-सहायता मोड हाल Markdown र नोटबुक Markdown सेलहरू समेट्छ। छवि अनुवाद अझै पनि प्रदायक-समर्थित इमेज पाइपलाइन प्रयोग गर्छ र OCR तथा लेआउट-सचेत रेंडरिङका लागि Azure AI Vision आवश्यक पर्छ।

## चरण 2: आफ्नो MCP क्लाइन्ट कन्फिगर गर्नुहोस्

सामान्य स्थानीय `stdio` सेटअपका लागि, Co-op Translator लाई आफ्नो MCP क्लाइन्ट कन्फिगरेसनमा थप्नुहोस्। क्लाइन्टले प्रक्रिया स्वचालित रूपमा सुरु र बन्द गर्नेछ।

इन्स्टल गरिएको प्याकेज कन्फिगरेसन:

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

Windows मा सोर्स चेकआउट कन्फिगरेसन:

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

macOS वा Linux मा सोर्स चेकआउट कन्फिगरेसन:

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

MCP क्लाइन्ट कन्फिगरेसन परिवर्तन गरेपछि, क्लाइन्टलाई पुन: सुरु वा रीलोड गर्नुहोस् ताकि यसले नयाँ सर्भर पत्ता लगाउन सकोस।

## चरण 3: क्लाइन्टमा सर्भर प्रमाणित गर्नुहोस्

उपलब्ध उपकरणहरू सूचीबद्ध गर्न MCP क्लाइन्टलाई भन्नुहोस्, वा पहिले एउटा पढ्न मात्र सहायक कल गर्नुहोस्:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

सुरुमा गर्ने उपयोगी जाँचहरू:

| उपकरण | के जाँच गर्ने |
| --- | --- |
| `get_api_overview` | सर्भर पहुँचयोग्य छ भनी पुष्टि गर्छ र उपलब्ध वर्कफ्लोज देखाउँछ। |
| `list_supported_languages` | प्याकेज गरिएको भाषा डाटा लोड गर्न सकिन्छ भनी पुष्टि गर्छ। |
| `get_configuration_status` | गोप्य मानहरू देखाए बिना LLM र Vision प्रदायकको उपलब्धता पुष्टि गर्छ। |

## चरण 4: एक कार्यप्रवाह छान्नुहोस्

### व्यक्तिगत फाइल वा दस्तावेज अनुवाद गर्नुहोस्

MCP क्लाइन्टसँग पहिले नै दस्तावेज सामग्री वा छवि पथ भएमा र Co-op Translator ले कन्फिगर गरिएको अनुवाद प्रदायकहरूलाई कल गर्नुपर्ने अवस्थामा प्रदायक-समर्थित सामग्री उपकरणहरू प्रयोग गर्नुहोस्।

Markdown का लागि:

1. `document`, `language_code`, र ऐच्छिक रूपमा `source_path` सँग `translate_markdown_content` कल गर्नुहोस्।
2. यदि अनुवादित नतिजा Co-op Translator आउटपुट लेआउटकामा लेखिने छ भने, `rewrite_markdown_paths` कल गर्नुहोस्।
3. क्लाइन्टलाई अन्तिम `content` लेख्न वा फर्काउन दिनुहोस्।

नोटबुकहरूको लागि:

1. नोटबुक JSON र `language_code` सँग `translate_notebook_content` कल गर्नुहोस्।
2. अनुवादित नोटबुक लिङ्कहरू लक्ष्य पथका लागि समायोजन आवश्यक भए `rewrite_notebook_paths` कल गर्नुहोस्।
3. अन्तिम नोटबुक JSON लेख्नुहोस् वा फर्काउनुहोस्।

छविहरूका लागि:

1. `image_path`, `language_code`, र ऐच्छिक `root_dir` वा `fast_mode` सँग `translate_image_content` कल गर्नुहोस्।
2. फर्काइएको `data_base64` र `mime_type` पढ्नुहोस्।
3. यदि `output_path` दिइएको छ भने, अनुवादित छवि सो पथमा पनि बचत हुन्छ।

सामग्री उपकरणहरूले प्रोजेक्ट डिस्कभरी, मेटाडाटा अपडेटहरू, डिस्क्लेमरहरू, वा स्वचालित पाथ पुनर्लेखन गर्दैनन्। यदि तपाईं चाहनुहुन्छ होस्ट एजेन्टले Co-op Translator LLM प्रदायक क्रेडेन्सियल्स बिना Markdown वा नोटबुक chunks अनुवाद गरोस् भने, तलको एजेन्ट-सहायित वर्कफ्लो प्रयोग गर्नुहोस्।

### होस्ट एजेन्ट मोडेलसँग अनुवाद गर्नुहोस्

जब तपाईं चाहनुहुन्छ MCP होस्ट एजेन्ट—जस्तै कोडिङ सहायक—ले अनुवादित टेक्स्ट उत्पादन गरोस् र Co-op Translator का लागि LLM प्रदायक कन्फिगर नगरियोस् तब एजेन्ट-सहायित उपकरणहरू प्रयोग गर्नुहोस्।

च्याट-आधारित MCP क्लाइन्टमा, सामान्यतया तपाईंले आफैंले टुल JSON लेख्न आवश्यक पर्दैन। एजेन्टलाई एजेन्ट-सहायित वर्कफ्लो प्रयोग गर्न भन्नुहोस्:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

नोटबुकका लागि पनि उही ढाँचा प्रयोग गर्नुहोस्:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

यदि तपाईंको MCP क्लाइन्टले सर्भर प्रम्प्टहरू समर्थन गर्छ भने, क्लाइन्टले उस्तै वर्कफ्लो निर्देशनहरू लोड गर्न `agent_assisted_markdown_translation_prompt` प्रयोग गर्नुहोस्।

Markdown का लागि:

1. `document`, `language_code`, र ऐच्छिक रूपमा `source_path` सँग `start_markdown_agent_translation` कल गर्नुहोस्।
2. प्रत्येक फर्काइएको खण्डलाई होस्ट एजेन्टमा खण्डको `prompt` अनुसार अनुवाद गर्नुहोस्।
3. मूल `job` र अनुवादित खण्डहरू `chunk_id` र `translated_text` प्रयोग गरेर `finish_markdown_agent_translation` कल गर्नुहोस्।
4. यदि सामग्री अनुवादित लक्ष्य पथमा लेखिने छ भने, `rewrite_markdown_paths` कल गर्नुहोस्।

नोटबुकहरूका लागि:

1. नोटबुक JSON र `language_code` सँग `start_notebook_agent_translation` कल गर्नुहोस्।
2. प्रत्येक फर्काइएको खण्ड होस्ट एजेन्टमा अनुवाद गर्नुहोस्।
3. मूल `job` र अनुवादित खण्डहरूसहित `finish_notebook_agent_translation` कल गर्नुहोस्।
4. अनुवादित नोटबुक लिङ्कहरू लक्ष्य-पथ समायोजन आवश्यक परे `rewrite_notebook_paths` कल गर्नुहोस्।

एजेन्ट-सहायित उपकरणहरूले Co-op Translator बाट कन्फिगर गरिएको LLM प्रदायकलाई कल गर्दैनन्। फर्काइएको खण्डहरू अनुवाद गर्ने जिम्मेवारी होस्ट एजेन्टको हुन्छ। Co-op Translator ले Markdown खण्डकरण, प्लेसहोल्डर संरक्षण, frontmatter पुनर्निर्माण, नोटबुक सेल प्रतिस्थापन, र अनुवादपछि सामान्यीकरण ह्यान्डल गर्छ।

### सम्पूर्ण रिपोजिटरी अनुवाद गर्नुहोस्

प्रयोगकर्ताले Co-op Translator लाई `translate` CLI जस्तै व्यवहार गराउन चाहँदा `run_translation` प्रयोग गर्नुहोस्।

रिपोजिटरी अनुवाद डिफल्ट रूपमा `dry_run=true` मा रहन्छ ताकि एजेन्टले फाइल परिवर्तनहरू गर्नु अघि दायरालाई जाँच्न सकोस्:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

The `run_translation` result includes an `events` array with versioned
`co-op.translation.event.v1` progress events. MCP clients should use fields such
as `type`, `stage_key`, `completed`, `total`, and `current_path` instead of
parsing captured console text. Pass `json_events_path` to also write those events
to an NDJSON file.

लेख्न अनुमति दिन प्रयोगकर्ताले दुबै `dry_run=false` र `confirm_write=true` सेट गर्नुपर्छ:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` लाई `run_translation` को कम्प्याटिबिलिटी उपनामको रूपमा एक्स्पोज गरिएको छ।

### अनुवादित आउटपुट समीक्षा गर्नुहोस्

LLM वा Vision क्रीडेन्सियल्स आवश्यक नपर्ने निश्चित जाँचहरूका लागि `run_review` प्रयोग गर्नुहोस्:

!!! note "Beta"
    MCP ले बेटा `run_review` API सार्वजनिक गरेको छ। यो पढ्न मात्रका समीक्षा कार्यप्रवाहहरूका लागि सुरक्षित छ, तर समीक्षा जाँचहरू र इश्यू स्किमाहरू परिवर्तन हुन सक्छन्।

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

नतिजाले क्याप्चर गरिएको टेक्स्ट आउटपुट र उपलब्ध हुँदा संरचित समीक्षा सारांश समावेश गर्छ।

## म्यानुअल सर्भर रनहरू

म्यानुअल रनहरू मुख्य रूपमा डिबगिङका लागि वा लामो चल्ने सर्भरहरु जस्तै व्यवहार गर्ने ट्रान्सपोर्टहरूको लागि हुन्छन्।

डिफल्ट stdio सर्भर डिबग गर्नुहोस्:

```bash
co-op-translator-mcp
```

सोर्स चेकआउटबाट चलाउनुहोस्:

```bash
python -m co_op_translator.mcp.server
```

लामो समय चल्ने HTTP वा SSE सर्भर चलाउनुहोस्:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

स्थानीय सम्पादक र एजेन्ट समाकलनका लागि, चरण 2 मा क्लाइन्ट-व्यवस्थित `stdio` कन्फिगरेसन प्राथमिकता दिनुहोस्।

## उपकरणहरू

| उपकरण | उद्देश्य | फाइलहरू लेख्छ |
| --- | --- | --- |
| `translate_markdown_content` | Markdown स्ट्रिङ अनुवाद गर्नुहोस्। | होइन |
| `translate_notebook_content` | नोटबुक JSON मा Markdown सेलहरू अनुवाद गर्नुहोस्। | होइन |
| `translate_image_content` | एक छविमा भएको टेक्स्ट अनुवाद गरी base64 छवि डाटा फर्काउनुहोस्। | ऐच्छिक, केवल जब `output_path` प्रदान गरिएको छ |
| `start_markdown_agent_translation` | Co-op Translator LLM क्रेडेन्सियल्स बिना होस्ट एजेन्टले अनुवाद गर्न Markdown खण्डहरू तयार गर्नुहोस्। | होइन |
| `finish_markdown_agent_translation` | होस्ट-एजेन्ट द्वारा अनुवादित खण्डहरूबाट Markdown पुनर्निर्माण गर्नुहोस्। | होइन |
| `start_notebook_agent_translation` | होस्ट एजेन्टले अनुवाद गर्न नोटबुक Markdown-सेल खण्डहरू तयार गर्नुहोस्। | होइन |
| `finish_notebook_agent_translation` | होस्ट-एजेन्ट अनुवादित खण्डहरूबाट नोटबुक JSON पुनर्निर्माण गर्नुहोस्। | होइन |
| `rewrite_markdown_paths` | अनुवादित लक्ष्यका लागि Markdown बडी र frontmatter पथहरू पुनर्लेखन गर्नुहोस्। | होइन |
| `rewrite_notebook_paths` | नोटबुक Markdown सेलभित्र पथहरू पुनर्लेखन गर्नुहोस्। | होइन |
| `run_translation` | CLI जस्तै प्रोजेक्ट-स्तर अनुवाद चलाउनुहोस्। | हो जब `dry_run=false` र `confirm_write=true` |
| `translate_project` | `run_translation` को कम्प्याटिबिलिटी उपनाम। | हो जब `dry_run=false` र `confirm_write=true` |
| `run_review` | निश्चित (deterministic) समीक्षा जाँचहरू चलाउनुहोस्। | होइन |
| `get_configuration_status` | गोप्यहरू नखूलिकन कन्फिगर गरिएका LLM र Vision प्रदायकहरूको रिपोर्ट गर्नुहोस्। | होइन |
| `list_supported_languages` | समर्थित लक्ष्य भाषा कोडहरूको सूची दिनुहोस्। | होइन |
| `get_api_overview` | उपलब्ध MCP वर्कफ्लोज र उपकरणहरूको वर्णन गर्नुहोस्। | होइन |

## स्रोतहरू

| स्रोत URI | उद्देश्य |
| --- | --- |
| `co-op://api` | वर्कफ्लोज र उपकरणहरूको JSON ओभरभ्यु। |
| `co-op://supported-languages` | समर्थित भाषा कोडहरूको JSON सूची। |
| `co-op://configuration` | गोप्यहरू बिना प्रदायक उपलब्धताको JSON सारांश। |

## प्रम्प्टहरू

| प्रम्प्ट | उद्देश्य |
| --- | --- |
| `translate_markdown_document_prompt` | सामग्री अनुवाद र ऐच्छिक पाथ पुनर्लेखन सहित MCP क्लाइन्टलाई मार्गदर्शन गर्नुहोस्। |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM प्रदायक क्रेडेन्सियल्स बिना होस्ट-एजेन्ट Markdown अनुवादका लागि MCP क्लाइन्टलाई मार्गदर्शन गर्नुहोस्। |
| `translate_repository_prompt` | प्राथमिक रूपमा dry-run गर्ने रिपोजिटरी अनुवादमा MCP क्लाइन्टलाई मार्गदर्शन गर्नुहोस्। |

## कपी-पेस्ट उदाहरणहरू

Markdown सामग्री अनुवाद गर्नुहोस्:

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

अनुवादित Markdown लिङ्कहरू पुनर्लेखन गर्नुहोस्:

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

होस्ट एजेन्ट मोडेलसँग Markdown अनुवाद गर्नुहोस्:

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

होस्ट एजेन्टले प्रत्येक फर्काइएको खण्ड अनुवाद गरेपछि, `start_markdown_agent_translation` ले फर्काएको पूर्ण `job` वस्तु सहित जागिर पूरा गर्नुहोस्:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

रिपोजिटरी अनुवाद पूर्वावलोकन गर्नुहोस्:

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

## समस्या समाधान

| समस्या | के प्रयास गर्ने |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | पूर्ण Python executable पथ प्रयोग गर्नुहोस् र `["-m", "co_op_translator.mcp.server"]` source checkout कन्फिगरेसन प्रयोग गर्नुहोस्। |
| सर्भर सूचीबद्ध गरिएको छ तर अनुवाद असफल हुन्छ। | `get_configuration_status` कल गरेर LLM प्रदायक उपलब्ध छ कि छैन पुष्टि गर्नुहोस्। |
| तपाईं Markdown वा नोटबुक अनुवाद प्रदायक क्रेडेन्सियलहरू बिना चाहनुहुन्छ। | `start_markdown_agent_translation` / `finish_markdown_agent_translation` वा नोटबुकसम्बन्धी समकक्ष प्रयोग गर्नुहोस् ताकि होस्ट एजेन्टले खण्डहरू अनुवाद गरोस्। |
| Image translation fails. | Azure AI Vision भेरिएबलहरू सेट छन् कि छैनन् पुष्टि गर्नुहोस् र `get_configuration_status` कल गर्नुहोस्। |
| Repository अनुवादले फाइलहरू लेख्दैन। | स्पष्ट प्रयोगकर्ता अनुमोदन पछि मात्र `dry_run=false` र `confirm_write=true` सेट गर्नुहोस्। |
| क्लाइन्ट कन्फिगमा परिवर्तनहरू देखिँदैनन्। | MCP क्लाइन्टलाई पुन: सुरु वा रीलोड गर्नुहोस्। |

## सुरक्षा नोटहरू

- MCP उपकरण कलहरू होस्ट एप्लिकेसन द्वारा मोडेल-नियन्त्रित हुन्छन्, त्यसैले रिपोजिटरी अनुवाद डिफल्ट रूपमा dry-run हुन्छ।
- पूर्ण रिपोजिटरी अनुवादले धेरै फाइलहरू सिर्जना, अपडेट, वा हटाउन सक्छ। `confirm_write=true` सेट गर्नु अघि स्पष्ट प्रयोगकर्ता अनुमोदन आवश्यक पार्नुहोस्।
- कन्फिगरेशन स्थिति उपकरणले कहिल्यै API किज, endpoints, वा अन्य गोप्य मानहरू फिर्ता गर्दैन।
- छवि अनुवादले base64 छवि डाटा फर्काउँछ। ठूला छविहरूले ठूलो टुल प्रतिक्रिया उत्पन्न गर्न सक्छन्।
- एजेन्ट-सहायित उपकरणहरूले स्रोत खण्डहरू र प्रम्प्टहरू MCP होस्टलाई फिर्ता गर्छन्। तिनीहरूलाई मात्र त्यस्तो सामग्रीसहित प्रयोग गर्नुहोस् जुन प्रयोगकर्ता त्यस होस्ट एजेन्ट मोडेलमा पठाउन सहज छ।