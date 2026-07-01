# तपाईंको कार्यप्रवाह छनौट गर्नुहोस्

Co-op Translator लाई तीन तरिकाले प्रयोग गर्न सकिन्छ: CLI, Python API, र MCP सर्भर। तीहरूमा अनुवाद क्षमताहरू एउटै छन्, तर प्रत्येकले फरक कार्यप्रवाहका लागि उपयुक्त हुन्छ।

कहाँबाट सुरु गर्ने निर्णय गर्दा यो पृष्ठ प्रयोग गर्नुहोस्।

## छिटो निर्णय

| यदि तपाईं ... चाहनुहुन्छ | प्रयोग | यहाँबाट सुरु गर्नुहोस् |
| --- | --- | --- |
| टर्मिनलबाट रिपोजिटरी अनुवाद वा समीक्षा गर्नुहोस् | CLI | [CLI सन्दर्भ](cli.md) |
| Python स्क्रिप्ट, सेवा, नोटबुक, वा CI काममा अनुवाद थप्नुहोस् | Python API | [Python API](api.md) |
| एजेन्ट, सम्पादक, वा MCP-अनुकूल क्लाइन्टलाई तपाईंको लागि सामग्री अनुवाद गर्न दिनुहोस् | MCP Server | [MCP सर्भर](mcp.md) |
| तपाईंको एपले पहिले नै लोड गरेको कुनै Markdown दस्तावेज, नोटबुक, वा छवि अनुवाद गर्नुहोस् | Python API वा MCP Server | [Python API](api.md) वा [MCP Server](mcp.md) |
| मानक आउटपुट फोल्डर र मेटाडेटासहित सम्पूर्ण रिपोजिटरी अनुवाद गर्नुहोस् | CLI वा `run_translation` | [CLI सन्दर्भ](cli.md) वा [Python API](api.md) |

## CLI प्रयोग गर्नुहोस् जब

CLI रोज्नुहोस् जब कुनै व्यक्ति वा CI काम शेलबाट रिपोजिटरी अनुवाद सञ्चालन गर्दैछ।

CLI सबभन्दा प्रत्यक्ष मार्ग हो जब तपाईं Co-op Translator लाई प्रोजेक्ट फाइलहरू पत्ता लगाउन, अनुवादित आउटपुटहरू सिर्जना गर्न, प्रोजेक्ट लेआउट Preserve गर्न, मेटाडेटा अपडेट गर्न, र समीक्षा कमान्डहरू चलाउन चाहनुहुन्छ।

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

उपयुक्त अवस्थामा:

- तपाईं टर्मिनलबाट रिपोजिटरी अनुवाद गर्दै हुनुहुन्छ।
- तपाईं CI वा रिलिज कार्यप्रवाहका लागि दोहोर्याउन मिल्ने कमान्ड चाहनुहुन्छ।
- तपाईंले बिल्ट-इन प्रोजेक्ट खोज, आउटपुट पाथहरू, मेटाडेटा, क्लिनअप, र समीक्षा चाहानुहुन्छ।
- तपाईं Python कोड लेख्नुभन्दा कमान्ड इन्टरफेसलाई प्राथमिकता दिनुहुन्छ।

## Python API प्रयोग गर्नुहोस् जब

तपाईंको आफ्नै कोडले कार्यप्रवाह नियन्त्रण गर्नु पर्ने भए Python API रोज्नुहोस्।

API एप्लिकेसनहरू, अटोमेसन स्क्रिप्टहरू, नोटबुकहरू, सेवाहरू, र कस्टम पाइपलाइनहरूको लागि उपयोगी हुन्छ। यसले व्यक्तिगत फाइलहरूको लागि तल्लो-स्तर कन्टेन्ट अनुवाद API हरू कल गर्न वा CLI द्वारा प्रयोग गरिने त्यही रिपोजिटरी-स्तर सञ्चालन चलाउन अनुमति दिन्छ।

एउटा Markdown दस्तावेज अनुवाद गर्नुहोस् र यसलाई कहाँ बचत गर्ने निर्णय गर्नुहोस्:

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
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

उपयुक्त अवस्थामा:

- तपाईंको एपले पहिले नै फाइलहरू, बफरहरू, नोटबुकहरू, वा छवि बाइटहरू पढ्छ।
- तपाईंलाई अनुकूलित मान्यकरण, भण्डारण, लगिङ, पुन:प्रयास, वा स्वीकृति फ्लोहरू आवश्यक छन्।
- पूर्ण रिपोजिटरी प्रोसेस नगरी एउटा दस्तावेज, नोटबुक, वा छवि अनुवाद गर्न चाहनुहुन्छ।
- तपाईं रिपोजिटरी अनुवाद चाहनुहुन्छ, तर शेल कमान्डको सट्टा Python अटोमेसनबाट।

## MCP सर्भर प्रयोग गर्नुहोस् जब

एजेन्ट, सम्पादक, वा MCP-अनुकूल क्लाइन्टले Co-op Translator उपकरणहरू कल गर्नु पर्ने भए MCP सर्भर रोज्नुहोस्।

सामान्य स्थानीय सेटअपमा, प्रयोगकर्ताले म्यानुअली सर्भर चलाइराख्दैन। जब उपकरणहरूको आवश्यकता पर्छ MCP क्लाइन्टले `co-op-translator-mcp` लाई `stdio` मार्फत सुरु गर्दछ।

एजेन्टले सम्हाल्न सक्ने उदाहरण प्रयोगकर्ता अनुरोधहरू:

- "यो Markdown फाइललाई कोरियालीमा अनुवाद गर्नुहोस् र लिङ्कहरू सहि राख्नुहोस्।"
- "एजेन्ट-सहायता प्राप्त MCP कार्यप्रवाहको साथमा यो Markdown फाइललाई कोरियालीमा अनुवाद गर्नुहोस्, अनुवाद गरिएका खण्डका लागि आफ्नो मोडल प्रयोग गर्दै।"
- "यो नोटबुकलाई कोरियालीमा अनुवाद गर्नुहोस्, कोड सेलहरू कायम राख्नुहोस्, र नोटबुक पुनर्निर्माण गर्न Co-op Translator MCP प्रयोग गर्नुहोस्।"
- "यस छविमा भएको पाठलाई जापानीमा अनुवाद गर्नुहोस् र नतिजा बचत गर्नुहोस्।"
- "एक रिपोजिटरी अनुवादलाई स्पेनीमा ड्राइ-रन गर्नुहोस् र मलाई के बदलिन्थ्यो बताउनुहोस्।"
- "कोरियाली अनुवाद नतिजा अद्यावधिक छ कि छैन समीक्षा गर्नुहोस्।"

Markdown र नोटबुकहरूको लागि, MCP दुई मोडहरूमा काम गर्न सक्छ:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | The MCP host agent should translate chunks with its own model, without Co-op Translator LLM provider credentials. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator should call Azure OpenAI or OpenAI directly. | `translate_markdown_content`, `translate_notebook_content` |

MCP प्रदायक-समर्थित Markdown उपकरण कल ढाँचा:

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

MCP छवि उपकरण कल ढाँचा:

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

रिपोजिटरी अनुवाद MCP मार्फत डिफल्ट रूपमा ड्राइ-रन गरिन्छ:

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

उपयुक्त अवस्थामा:

- तपाईं एजेन्ट वा सम्पादक भित्र प्राकृतिक-भाषा अनुवाद कार्यप्रवाहहरू चाहनुहुन्छ।
- तपाईं Markdown वा नोटबुक अनुवाद चाहनुहुन्छ जहाँ होस्ट एजेन्ट मोडलले तयार गरिएका खण्डहरू अनुवाद गर्छ।
- पूरा रिपोजिटरीको सट्टा चयनित सामग्री एजेन्टले अनुवाद गरोस् भन्ने चाहनुहुन्छ।
- रिपोजिटरी-व्यापी लेखनहरू अघि स्वीकृति चरण चाहनुहुन्छ।
- तपाईं एक मात्र इन्टरफेस चाहनुहुन्छ जुन Markdown, नोटबुक, छवि, समीक्षा, र पाथ-पुनर्लेखन उपकरणहरू प्रकट गर्छ।

## यी कसरी सँगै मेल खान्छन्

CLI मानिसहरूले रिपोजिटरी अनुवाद गर्दा सबैभन्दा राम्रो डिफल्ट हो। Python API तब उत्तम हुन्छ जब तपाईंको कोडले कार्यप्रवाह नियन्त्रण गर्छ। MCP सर्भर तब उत्तम हुन्छ जब एजेन्ट वा सम्पादकले कार्यप्रवाह नियन्त्रण गर्छ।

यी तीनै मार्गहरूले उही सार्वजनिक Co-op Translator API प्रयोग गर्छन्, त्यसैले तपाईं CLI बाट सुरु गर्न सक्नुहुन्छ, पछि Python सँग अटोमेट गर्न सक्नुहुन्छ, र एजेन्ट-चालित कार्यप्रवाह चाहिंदा त्यही क्षमताहरू MCP क्लाइन्टहरूलाई प्रदर्शन गर्न सक्नुहुन्छ।