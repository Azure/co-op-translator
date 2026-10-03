# तपाइँको वर्कफ्लो चयन गर्नुहोस्

Co-op Translator लाई तीन तरिकाले प्रयोग गर्न सकिन्छ: CLI, Python API, र MCP सर्भर। तिनीहरू समान अनुवाद क्षमताहरू साझा गर्छन्, तर प्रत्येक अलग वर्कफ्लोमा अनुकूल हुन्छ।

कहाँबाट सुरु गर्ने निर्णय गर्दा यो पृष्ठ प्रयोग गर्नुहोस्।

**यदि तपाईं अनुवादहरू हातबाट सम्पादन गर्नुभयो भने:** डिफ़ल्ट CLI र Actions वर्कफ्लोहरूले परिवर्तन भएका स्रोत फाइलहरूलाई पूर्ण रूपमा पुनःअनुवाद गर्छन्, त्यसैले ती फाइलहरूमा गरेको तपाईंको शब्दांकन ओभरराइट हुन सक्छ। अपडेट स्वीकार गर्नु अघि diff समीक्षा गर्नुहोस्। स्वीकृत सम्पादनहरूको Markdown ब्लक-स्तर संरक्षणका लागि, वैकल्पिक [Python API अनुवाद अवस्था प्रदायक](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) प्रयोग गर्नुहोस्।

## छिटो निर्णय

| यदि तपाईं चाहनुहुन्छ... | प्रयोग गर्नुहोस् | यहाँबाट सुरु गर्नुहोस् |
| --- | --- | --- |
| टर्मिनलबाट रिपोजिटरी अनुवाद वा समीक्षा गर्नुहोस् | CLI | [CLI सन्दर्भ](cli.md) |
| Python स्क्रिप्ट, सेवा, नोटबुक, वा CI काममा अनुवाद थप्नुहोस् | Python API | [Python API](api.md) |
| एजेन्ट, सम्पादक, वा MCP-समर्थित क्लाइन्टलाई तपाईंको लागि सामग्री अनुवाद गर्न दिनुहोस् | MCP Server | [MCP Server](mcp.md) |
| तपाईंको अनुप्रयोगले पहिले नै लोड गरेको एउटा Markdown दस्तावेज, नोटबुक, वा छवि अनुवाद गर्नुहोस् | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| मानक आउटपुट फोल्डरहरू र मेटाडाटा सहित सम्पूर्ण रिपोजिटरी अनुवाद गर्नुहोस् | CLI or `run_translation` | [CLI सन्दर्भ](cli.md) or [Python API](api.md) |

## CLI प्रयोग गर्नुहोस् जब

जब व्यक्ति वा CI जॉब शेलबाट रिपोजिटरी अनुवाद चलाइरहेको छ तब CLI छनौट गर्नुहोस्।

जब तपाइँ Co-op Translator लाई प्रोजेक्ट फाइलहरू पत्ता लगाउन, अनुवादित आउटपुटहरू सिर्जना गर्न, प्रोजेक्ट लेआउट कायम राख्न, मेटाडाटा अद्यावधिक गर्न, र समीक्षा कमाण्डहरू चलाउन चाहनुहुन्छ भने CLI सबैभन्दा प्रत्यक्ष बाटो हो।

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

यो उदाहरणले Markdown र नोटबुकहरू अनुवाद गर्छ। `-img` केवल [Azure AI Vision](configuration.md#azure-ai-vision) कन्फिगर गरेपछि मात्र थप्नुहोस्। Markdown-मैत्री पहिलो रनका लागि, [तपाईंको पहिलो अनुवाद](first-translation.md) अनुसरण गर्नुहोस्।

उपयुक्त प्रयोगहरू:

- तपाईं टर्मिनलबाट रिपोजिटरी अनुवाद गर्दै हुनुहुन्छ।
- तपाईं CI वा रिलीज वर्कफ्लोका लागि पुन:चल्ने कमाण्ड चाहनुहुन्छ।
- तपाइँले बिल्ट-इन प्रोजेक्ट पत्ता लगाउने सुविधा, आउटपुट पथहरू, मेटाडाटा, क्लिनअप, र समीक्षा चाहनुहुन्छ।
- तपाईं Python कोड लेख्नुभन्दा कमाण्ड इन्टरफेसलाई रुचाउनुहुन्छ।

## Python API प्रयोग गर्नुहोस् जब

जब तपाईंको आफ्नै कोडले वर्कफ्लोलाई नियन्त्रण गर्नु पर्छ तब Python API छान्नुहोस्।

API अनुप्रयोगहरू, अटोमेसन स्क्रिप्टहरू, नोटबुकहरू, सेवाहरू, र अनुकूल पाइपलाइनहरूका लागि उपयोगी छ। यसले तपाईँलाई व्यक्तिगत फाइलहरूका लागि लो-लेभल सामग्री अनुवाद API हरू कल गर्न वा CLI द्वारा प्रयोग गरिने एउटै रिपोजिटरी-स्तरीय ओरकेस्ट्रेशन चलाउन अनुमति दिन्छ।

एउटा Markdown दस्तावेज अनुवाद गरी यसलाई कहाँ बचत गर्ने निर्णय गर्नुहोस्:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Python बाट रिपोजिटरी अनुवाद चलाउनुहोस्:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

उपयुक्त प्रयोगहरू:

- तपाईंको अनुप्रयोग पहिले देखि नै फाइलहरू, बफरहरू, नोटबुकहरू, वा इमेज बाइटहरू पढ्छ।
- तपाईंलाई कस्टम भ्यालिडेसन, स्टोरेज, लगिङ, पुन:प्रयास, वा अनुमोदन प्रवाहहरूको आवश्यकता छ।
- तपाईंले सम्पूर्ण रिपोजिटरी प्रोसेस नगरी एउटा दस्तावेज, नोटबुक, वा छवि अनुवाद गर्न चाहनुहुन्छ।
- तपाईं रिपोजिटरी अनुवाद चाहनुहुन्छ, तर शेल कमाण्डको सट्टा Python अटोमेसनबाट।

## MCP सर्भर प्रयोग गर्नुहोस् जब

जब एजेन्ट, सम्पादक, वा MCP-समर्थित क्लाइन्टले Co-op Translator उपकरणहरू कल गर्नुपर्छ तब MCP सर्भर छान्नुहोस्।

सामान्य स्थानीय सेटअपमा, प्रयोगकर्ताले म्यानुअली सर्भर चलाइराख्दैन। MCP क्लाइन्टले आवश्यकता परेमा `stdio` मार्फत `co-op-translator-mcp` सुरु गर्छ।

एजेन्टले सम्हाल्न सक्ने प्रयोगकर्ता अनुरोधका उदाहरणहरू:

- "यो Markdown फाइललाई कोरियनमा अनुवाद गर्नुहोस् र लिंकहरू सहि राख्नुहोस्।"
- "एजेन्ट-सहयोगी MCP वर्कफ्लो प्रयोग गरी यस Markdown फाइललाई कोरियनमा अनुवाद गर्नुहोस्, अनुवाद गरिएका खन्डहरूको लागि तपाईंको आफ्नै मोडेल प्रयोग गर्दै।"
- "यो नोटबुकलाई कोरियनमा अनुवाद गर्नुहोस्, कोड सेलहरू कायम राख्नुहोस्, र नोटबुक पुनर्निर्माण गर्न Co-op Translator MCP प्रयोग गर्नुहोस्।"
- "यस छविको पाठलाई जापानीमा अनुवाद गरी परिणाम सुरक्षित गर्नुहोस्।"
- "रिपोजिटरी अनुवादलाई स्पेनीमा ड्राइ-रन गर्नुहोस् र के बदलिन्थ्यो बताउनुहोस्।"
- "कोरियन अनुवाद आउटपुट अद्यावधिक छ कि छैन समीक्षा गर्नुहोस्।"

Markdown र नोटबुकहरूको लागि, MCP दुई मोडहरूमा काम गर्न सक्छ:

| मोड | कहिले प्रयोग गर्ने | मुख्य उपकरणहरू |
| --- | --- | --- |
| Agent-assisted | MCP होस्ट एजेन्टले आफ्नै मोडेल प्रयोग गरी खन्डहरू अनुवाद गर्नुपर्छ, Co-op Translator LLM प्रदायक क्रेडेन्शियल्स बिना। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator ले Azure OpenAI, OpenAI, वा Anthropic सिधै कल गर्नुपर्छ। | `translate_markdown_content`, `translate_notebook_content` |

MCP प्रदायक-समर्थित Markdown उपकरण कल आकार:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP इमेज उपकरण कल आकार:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

रिपोजिटरी अनुवाद MCP मार्फत डिफल्ट रूपमा ड्राइ-रन हुन्छ:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

उपयुक्त प्रयोगहरू:

- तपाईं एजेन्ट वा सम्पादक भित्र प्राकृतिक-भाषा अनुवाद वर्कफ्लोहरू चाहनुहुन्छ।
- तपाईं Markdown वा नोटबुक अनुवाद चाहनुहुन्छ जहाँ होस्ट एजेन्ट मोडेलले तयारी गरिएका खन्डहरू अनुवाद गर्छ।
- तपाईं चाहनुहुन्छ एजेन्टले सम्पूर्ण रिपोजिटरीको सट्टा चयन गरिएको सामग्री अनुवाद गरोस्।
- तपाईं रिपोजिटरीव्यापी लेखन अघि अनुमोदन चरण चाहनुहुन्छ।
- तपाईं यस्तो एक इन्टरफेस चाहनुहुन्छ जसले Markdown, नोटबुक, इमेज, समीक्षा, र पथ-пुनर्लेखन उपकरणहरू प्रस्तुत गर्छ।

## तिनीहरू कसरी एक आपसमा मेल खान्छन्

रिपोजिटरी अनुवाद गर्ने मानिसहरूका लागि CLI सबैभन्दा उपयुक्त डिफल्ट हो। तपाईंको कोडले वर्कफ्लोको मालिक हुँदा Python API सबैभन्दा राम्रो हुन्छ। एजेन्ट वा सम्पादकले वर्कफ्लोको मालिक हुँदा MCP सर्भर सबैभन्दा उपयुक्त हुन्छ।

यी तीनै मार्गहरूले एउटै सार्वजनिक Co-op Translator API प्रयोग गर्छन्, त्यसैले तपाईं CLI बाट सुरु गर्न सक्नुहुन्छ, पछि Python मार्फत अटोमेट गर्न सक्नुहुन्छ, र एजेन्ट-संचालित वर्कफ्लोहरू चाहिएको बेला ती समान क्षमताहरू MCP क्लाइन्टहरूलाई प्रस्तुत गर्न सक्नुहुन्छ।