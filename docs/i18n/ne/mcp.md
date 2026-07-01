# MCP Server

Co-op Translator मा एजेन्टहरू, सम्पादकहरू, र MCP-संगत क्लाइन्टहरूको लागि Model Context Protocol सर्भर समावेश छ।

पूर्वनिर्धारित स्थानीय सेटअपको लागि, प्रयोगकर्ताहरूले पृथक सर्भर म्यानुअली चलाइरहनु पर्दैन। तिनीहरूले आफ्नो MCP क्लाइन्ट कन्फिगर गर्दछन्, र क्लाइन्टले Co-op Translator उपकरणहरू आवश्यक पर्दा `co-op-translator-mcp` लाई स्वचालित रूपमा `stdio` मार्फत सुरु गर्छ।

CLI, Python API, र MCP बीच छान्दै हुनुहुन्छ भने, [Choose Your Workflow](workflows.md) बाट सुरु गर्नुहोस्।

जब एजेन्ट वा सम्पादकले Co-op Translator लाई प्रत्यक्ष कल गर्नुपर्छ तब MCP प्रयोग गर्नुहोस्:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP सर्भरले [Python API](api.md) मा दस्तावेज गरिएको समान सार्वजनिक Python API लाई र्याप गर्छ। Provider-backed उपकरणहरूले CLI र Python API जस्तै कन्फिगर गरिएका प्रदायकहरू प्रयोग गर्छन्। एजेन्ट-सहायताप्राप्त उपकरणहरूले MCP होस्ट एजेन्टलाई अनुवाद गर्नका लागि खण्डहरू तयार गर्छन्, त्यसपछि Co-op Translator लाई अन्तिम Markdown वा नोटबुक पुनर्निर्माण गर्न प्रयोग गर्छन्।

## Step 1: Install and Configure Co-op Translator

तपाईंको MCP क्लाइन्टले प्रयोग गर्ने Python वातावरणमा Co-op Translator स्थापना गर्नुहोस्:

```bash
pip install co-op-translator
```

यस रिपोजिटरीबाट स्थानीय विकासको लागि, प्याकेजलाई editable मोडमा स्थापना गर्नुहोस्:

```bash
pip install -e .
```

तपाईंको MCP क्लाइन्टले प्रयोग गर्ने अनुवाद मोड छान्नुहोस्:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator ले `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, वा `run_translation` कल गर्छ। | Markdown र नोटबुक अनुवादका लागि Azure OpenAI वा OpenAI आवश्यक छन्। इमेज अनुवादका लागि Azure AI Vision पनि आवश्यक हुन्छ। |
| Agent-assisted | MCP होस्ट एजेन्टले `start_markdown_agent_translation` वा `start_notebook_agent_translation` बाट फर्किएका खण्डहरू अनुवाद गर्छ। | Markdown वा नोटबुक खण्डहरूका लागि Co-op Translator LLM प्रदायक क्रेडेन्सियलहरू आवश्यक छैनन्। इमेज अनुवाद हालै एजेन्ट-सहायता मोडमा समावेश गरिएको छैन। |

Codex वा Claude Code जस्ता एजेन्टको भित्र Markdown वा नोटबुक अनुवादबाट सुरु गर्दै हुनुहुन्छ भने agent-assisted मोडबाट सुरु गर्नुहोस्। Co-op Translator आफैंले तपाईंका कन्फिगर गरिएका प्रदायकहरूलाई कल गर्नु पर्ने स्थिति, इमेज अनुवाद, वा CLI जस्तै रिपोजिटरी-स्तर अनुवाद गर्दा provider-backed मोड प्रयोग गर्नुहोस्।

Provider-backed कार्यप्रवाहहरूको लागि मात्र प्रदायक क्रेडेन्सियलहरू कन्फिगर गर्नुहोस्:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed इमेज अनुवादले अतिरिक्त रूपमा आवश्यक हुन्छ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Step 2: Configure Your MCP Client

सामान्य स्थानीय `stdio` सेटअपका लागि, Co-op Translator लाई आफ्नो MCP क्लाइन्ट कन्फिगरेसनमा थप्नुहोस्। क्लाइन्टले प्रोससलाई स्वतः सुरु र रोक्छ।

Installed package configuration:

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

Source checkout configuration on Windows:

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

Source checkout configuration on macOS or Linux:

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

MCP क्लाइन्ट कन्फिगरेसन परिवर्तन गरेपछि, क्लाइन्टले नयाँ सर्भर पत्ता लगाउन सकोस् भनेर क्लाइन्ट पुनः सुरु वा रीलोड गर्नुहोस्।

## Step 3: Verify the Server in the Client

MCP क्लाइन्टलाई उपलब्ध उपकरणहरूको सूची माग्नुहोस्, वा पहिले कुनै एउटा read-only सहायकहरू मध्ये एक कल गर्नुहोस्:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

उपयोगी पहिलो चेकहरू:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | सर्भर पहुँचयोग्य छ भनी पुष्टि गर्छ र उपलब्ध कार्यप्रवाहहरू देखाउँछ। |
| `list_supported_languages` | प्याकेज गरिएको भाषा डेटा लोड गर्न सकिन्छ भनी पुष्टि गर्छ। |
| `get_configuration_status` | LLM र Vision प्रदायक उपलब्धता जाँच्छ बिना गोप्य मानहरू प्रकट नगरीकन। |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

जब MCP क्लाइन्टसँग पहिले नै दस्तावेज सामग्री वा इमेज पाथ छ र Co-op Translator ले कन्फिगर गरिएका अनुवाद प्रदायकहरूलाई कल गर्नुपर्छ भने provider-backed content उपकरणहरू प्रयोग गर्नुहोस्।

Markdown को लागि:

1. `document`, `language_code`, र वैकल्पिक `source_path` सहित `translate_markdown_content` कल गर्नुहोस्।
2. यदि अनुवादित परिणाम Co-op Translator आउटपुट लेआउटमा लेखिनेछ भने, `rewrite_markdown_paths` कल गर्नुहोस्।
3. क्लाइन्टलाई अन्तिम `content` लेख्न वा फर्काउन दिनुहोस्।

नोटबुकका लागि:

1. नोटबुक JSON र `language_code` सहित `translate_notebook_content` कल गर्नुहोस्।
2. लक्षित पाथका लागि अनुवादित नोटबुक लिंकहरू समायोजन गर्न जरुरी भए `rewrite_notebook_paths` कल गर्नुहोस्।
3. अन्तिम नोटबुक JSON लेख्नुहोस् वा फर्काउनुहोस्।

इमेजका लागि:

1. `image_path`, `language_code`, र वैकल्पिक `root_dir` वा `fast_mode` सहित `translate_image_content` कल गर्नुहोस्।
2. फर्काइएको `data_base64` र `mime_type` पढ्नुहोस्।
3. यदि `output_path` प्रदान गरिएको छ भने, अनुवादित छवि त्यो पाथमा पनि सुरक्षित गरिन्छ।

यी सामग्री उपकरणहरूले प्रोजेक्ट डिस्कभरी, मेटाडाटा अपडेट, अस्वीकरण, वा स्वत: पाथ रिराइटिङ गर्दैनन्। यदि तपाईंले होस्ट एजेन्टलाई Co-op Translator LLM प्रदायक क्रेडेन्सियलहरू बिना Markdown वा नोटबुक खण्डहरू अनुवाद गर्न चाहनुहुन्छ भने तलको agent-assisted कार्यप्रवाह प्रयोग गर्नुहोस्।

### Translate with the Host Agent Model

जब तपाईं चाहनुहुन्छ कि MCP होस्ट एजेन्टले जस्तै कोडिङ सहायकले अनुवादित टेक्स्ट उत्पादन गरोस् र Co-op Translator का लागि Azure OpenAI वा OpenAI कन्फिगर नगरियोस् तब agent-assisted उपकरणहरू प्रयोग गर्नुहोस्।

च्याट-आधारित MCP क्लाइन्टमा, सामान्यतया तपाईंले टूल JSON आफैं लेख्न आवश्यक पर्दैन। एजेन्टलाई agent-assisted कार्यप्रवाह प्रयोग गर्न माग्नुहोस्:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

नोटबुकका लागि, उस्तै नमूना प्रयोग गर्नुहोस्:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

यदि तपाईंको MCP क्लाइन्ट सर्भर प्रोन्ट्स समर्थन गर्छ भने, क्लाइन्टलाई उस्तै कार्यप्रवाह निर्देशनहरू लोड गराउन `agent_assisted_markdown_translation_prompt` प्रयोग गर्नुहोस्।

Markdown का लागि:

1. `document`, `language_code`, र वैकल्पिक `source_path` सहित `start_markdown_agent_translation` कल गर्नुहोस्।
2. फर्किएका प्रत्येक खण्डलाई होस्ट एजेन्टमा खण्ड `prompt` पालना गर्दै अनुवाद गर्नुहोस्।
3. मूल `job` र `chunk_id` तथा `translated_text` प्रयोग गरी अनुवादित खण्डसहित `finish_markdown_agent_translation` कल गर्नुहोस्।
4. सामग्रीलाई अनुवादित लक्ष्य पाथमा लेखिनेछ भने `rewrite_markdown_paths` कल गर्नुहोस्।

नोटबुकका लागि:

1. नोटबुक JSON र `language_code` सहित `start_notebook_agent_translation` कल गर्नुहोस्।
2. फर्किएका प्रत्येक खण्डलाई होस्ट एजेन्टमा अनुवाद गर्नुहोस्।
3. मूल `job` र अनुवादित खण्डहरू सहित `finish_notebook_agent_translation` कल गर्नुहोस्।
4. अनुवादित नोटबुक लिंकहरू लक्ष्य-पाथ समायोजन चाहियो भने `rewrite_notebook_paths` कल गर्नुहोस्।

Agent-assisted उपकरणहरूले Co-op Translator बाट Azure OpenAI वा OpenAI कल गर्दैनन्। फर्काएका खण्डहरूको अनुवाद गर्ने जिम्मेवारी होस्ट एजेन्टको हुन्छ। Co-op Translator ले Markdown खण्डीकरण, प्लेसहोल्डर संरक्षण, फ्रन्टम्याटर पुनर्निर्माण, नोटबुक सेल प्रतिस्थापन, र पोष्ट-अनुवाद सामान्यीकरण ह्यान्डल गर्छ।

### Translate an Entire Repository

जब प्रयोगकर्ताले Co-op Translator लाई `translate` CLI जस्तै व्यवहार गर्न चाहन्छन् तब `run_translation` प्रयोग गर्नुहोस्।

रिपोजिटरी अनुवादको पूर्वनिर्धारित रूपमा `dry_run=true` हुन्छ ताकि एजेन्टले फाइल परिवर्तनहरू अघि दायरालाई निरीक्षण गर्न सकोस्:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

लेख्न अनुमति दिन, कलकर्ताले दुवै `dry_run=false` र `confirm_write=true` सेट गर्नुपर्छ:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` लाई `run_translation` को लागि कम्प्याटिबिलिटी अलायसको रूपमा एक्स्पोज गरिएको छ।

### Review Translated Output

LLM वा Vision क्रेडेन्सियलहरू आवश्यक नपर्ने निर्धारित जाँचहरूको लागि `run_review` प्रयोग गर्नुहोस्:

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

परिणामले समातिएको टेक्स्ट आउटपुट र उपलब्ध हुँदा संरचित समीक्षा सारांश समावेश गर्दछ।

## Manual Server Runs

म्यानुअल रनहरू मुख्य रूपमा डिबगिङ वा दीर्घकालीन सर्भर जस्ता व्यवहार गर्ने ट्रान्सपोर्टका लागि हुन्।

पूर्वनिर्धारित stdio सर्भर डिबग गर्नुहोस्:

```bash
co-op-translator-mcp
```

Source checkout बाट चलाउनुहोस्:

```bash
python -m co_op_translator.mcp.server
```

दीर्घकालीन HTTP वा SSE सर्भर चलाउनुहोस्:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

स्थानीय सम्पादक र एजेन्ट एकीकरणहरूको लागि, Step 2 मा क्लाइन्ट-प्रबन्धित `stdio` कन्फिगरेसनलाई प्राथमिकता दिनुहोस्।

## Tools

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

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

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
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Safety Notes

- MCP tool calls are model-controlled by the host application, so repository translation is dry-run by default.
- Full repository translation can create, update, or remove many files. Require explicit user approval before setting `confirm_write=true`.
- The configuration status tool never returns API keys, endpoints, or other secret values.
- Image translation returns base64 image data. Large images can produce large tool responses.
- Agent-assisted tools return source chunks and prompts to the MCP host. Use them only with content the user is comfortable sending to that host agent model.