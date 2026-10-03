# अपना वर्कफ़्लो चुनें

Co-op Translator का उपयोग तीन तरीकों से किया जा सकता है: CLI, Python API, और MCP Server। ये एक ही अनुवाद क्षमताएँ साझा करते हैं, लेकिन प्रत्येक अलग वर्कफ़्लो के अनुरूप है।

जब आप यह तय कर रहे हों कि कहाँ से शुरू करें तो इस पृष्ठ का उपयोग करें।

**यदि आप अनुवादों को मैन्युअली संपादित करते हैं:** डिफ़ॉल्ट CLI और Actions वर्कफ़्लो संशोधित स्रोत फ़ाइलों को पूरी तरह से पुन:अनुवाद करते हैं, इसलिए उन फ़ाइलों में आपका शब्द-रूप ओवरराइट हो सकता है। अपडेट स्वीकार करने से पहले diff की समीक्षा करें। स्वीकृत संपादनों के लिए Markdown ब्लॉक-स्तर संरक्षण के लिए, वैकल्पिक [Python API अनुवाद स्थिति प्रदाता](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) का प्रयोग करें।

## त्वरित निर्णय

| यदि आप चाहते हैं... | प्रयोग करें | यहाँ से शुरू करें |
| --- | --- | --- |
| टर्मिनल से किसी रिपॉज़िटरी का अनुवाद या समीक्षा करें | CLI | [CLI संदर्भ](cli.md) |
| एक Python स्क्रिप्ट, सर्विस, नोटबुक, या CI जॉब में अनुवाद जोड़ें | Python API | [Python API](api.md) |
| एक एजेंट, एडिटर, या MCP-संगत क्लाइंट को आपके लिए सामग्री का अनुवाद करने दें | MCP Server | [MCP Server](mcp.md) |
| एक Markdown दस्तावेज़, नोटबुक, या छवि का अनुवाद करें जिसे आपकी ऐप पहले से लोड कर चुकी है | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| मानक आउटपुट फ़ोल्डर्स और मेटाडेटा के साथ पूरी रिपॉज़िटरी का अनुवाद करें | CLI या `run_translation` | [CLI संदर्भ](cli.md) या [Python API](api.md) |

## CLI का उपयोग तब करें जब

CLI चुनें जब कोई व्यक्ति या CI जॉब शेल से रिपॉज़िटरी अनुवाद चला रहा हो।

CLI सबसे सीधा रास्ता है जब आप चाहते हैं कि Co-op Translator प्रोजेक्ट फ़ाइलों का पता लगाए, अनूदित आउटपुट बनाए, प्रोजेक्ट लेआउट को सुरक्षित रखे, मेटाडेटा अपडेट करे, और समीक्षा आदेश चलाए।

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

यह उदाहरण Markdown और नोटबुक का अनुवाद करता है। `-img` केवल [Azure AI Vision](configuration.md#azure-ai-vision) को कॉन्फ़िगर करने के बाद जोड़ें। Markdown-केवल पहले रन के लिए, [आपका पहला अनुवाद](first-translation.md) का पालन करें।

उपयुक्त स्थितियाँ:

- आप अपनी टर्मिनल से एक रिपॉज़िटरी का अनुवाद कर रहे हैं।
- आप CI या रिलीज़ वर्कफ़्लो के लिए एक पुनरावर्ती कमांड चाहते हैं।
- आप अंतर्निर्मित प्रोजेक्ट खोज, आउटपुट पथ, मेटाडेटा, साफ़-सफाई, और समीक्षा चाहते हैं।
- आप Python कोड लिखने की बजाय कमांड इंटरफ़ेस पसंद करते हैं।

## Python API का उपयोग तब करें जब

Python API चुनें जब आपका अपना कोड वर्कफ़्लो को नियंत्रित करना चाहिए।

API एप्लिकेशन्स, ऑटोमेशन स्क्रिप्ट, नोटबुक, सर्विसेज़, और कस्टम पाइपलाइनों के लिए उपयोगी है। यह आपको व्यक्तिगत फ़ाइलों के लिए लो-लेवल कंटेंट अनुवाद APIs कॉल करने देता है, या वही रिपॉज़िटरी-स्तरीय ऑर्केस्ट्रेशन चलाने देता है जो CLI उपयोग करता है।

एक Markdown दस्तावेज़ का अनुवाद करें और तय करें कि इसे कहाँ सेव करना है:

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

Python से रिपॉज़िटरी अनुवाद चलाएँ:

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

उपयुक्त स्थितियाँ:

- आपकी एप्लिकेशन पहले से फ़ाइलें, बफ़र्स, नोटबुक, या इमेज बाइट्स पढ़ती है।
- आपको कस्टम वैलिडेशन, स्टोरेज, लॉगिंग, रिट्राईज़, या अनुमोदन फ्लो की आवश्यकता है।
- आप बिना पूरी रिपॉज़िटरी प्रोसेस किए एक दस्तावेज़, नोटबुक, या छवि का अनुवाद करना चाहते हैं।
- आप रिपॉज़िटरी अनुवाद चाहते हैं, लेकिन शेल कमांड के बजाय Python ऑटोमेशन से।

## MCP Server का उपयोग तब करें जब

MCP server चुनें जब कोई एजेंट, एडिटर, या MCP-संगत क्लाइंट Co-op Translator टूल्स को कॉल करे।

सामान्य लोकल सेटअप में, उपयोगकर्ता मैन्युअली सर्वर चलाकर नहीं रखता। MCP क्लाइंट आवश्यक होने पर उपकरणों के लिए `co-op-translator-mcp` को `stdio` के माध्यम से शुरू करता है।

एजेंट द्वारा संभाले जाने योग्य उपयोगकर्ता अनुरोधों के उदाहरण:

- "इस Markdown फ़ाइल को कोरियाई में अनुवाद करें और लिंक सही रखें।"
- "एजेंट-सहायित MCP वर्कफ़्लो के साथ इस Markdown फ़ाइल का कोरियाई में अनुवाद करें, अनूदित खंडों के लिए अपने स्वयं के मॉडल का उपयोग करते हुए।"
- "इस नोटबुक को कोरियाई में अनूदित करें, कोड सेल्स को संरक्षित रखें, और नोटबुक को पुनर्निर्माण करने के लिए Co-op Translator MCP का उपयोग करें।"
- "इस छवि के टेक्स्ट को जापानी में अनुवाद करें और परिणाम सहेजें।"
- "रिपॉज़िटरी अनुवाद का ड्राइ-रन स्पेनिश में करें और बताइए क्या बदलेगा।"
- "जाँचें कि कोरियाई अनुवाद आउटपुट अद्यतित है या नहीं।"

Markdown और नोटबुक के लिए, MCP दो मोड में काम कर सकता है:

| मोड | कब उपयोग करें | मुख्य टूल्स |
| --- | --- | --- |
| Agent-assisted | MCP होस्ट एजेंट को अपने मॉडल के साथ खंडों का अनुवाद करना चाहिए, Co-op Translator LLM प्रदाता क्रेडेंशियल्स के बिना। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator को Azure OpenAI, OpenAI, या Anthropic को सीधे कॉल करना चाहिए। | `translate_markdown_content`, `translate_notebook_content` |

MCP प्रदाता-समर्थित Markdown टूल कॉल का स्वरूप:

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

MCP इमेज टूल कॉल का स्वरूप:

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

रिपॉज़िटरी अनुवाद डिफ़ॉल्ट रूप से MCP के माध्यम से ड्राइ-रन होता है:

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

उपयुक्त स्थितियाँ:

- आप एजेंट या एडिटर के भीतर प्राकृतिक-भाषा अनुवाद वर्कफ़्लो चाहते हैं।
- आप Markdown या नोटबुक अनुवाद चाहते हैं जहाँ होस्ट एजेंट मॉडल तैयार किए गए खंडों का अनुवाद करता है।
- आप चाहते हैं कि एजेंट संपूर्ण रिपॉज़िटरी की बजाय चयनित सामग्री का अनुवाद करे।
- आप रिपॉज़िटरी-भर लेखन से पहले एक अनुमोदन चरण चाहते हैं।
- आप एक ऐसा इंटरफ़ेस चाहते हैं जो Markdown, नोटबुक, छवि, समीक्षा, और पथ-पुनर्लेखन टूल्स प्रदर्शित करे।

## ये कैसे मेल खाते हैं

रिपॉज़िटरी का अनुवाद करने वाले मनुष्यों के लिए CLI सबसे अच्छा डिफ़ॉल्ट है। जब आपका कोड वर्कफ़्लो का मालिक हो तो Python API सबसे अच्छा है। जब एक एजेंट या एडिटर वर्कफ़्लो का मालिक हो तो MCP server सबसे अच्छा है।

तीनों मार्ग एक ही सार्वजनिक Co-op Translator API का उपयोग करते हैं, इसलिए आप CLI से शुरू कर सकते हैं, बाद में Python के साथ ऑटोमेट कर सकते हैं, और जब आपको एजेंट-चालित वर्कफ़्लो की आवश्यकता हो तो समान क्षमताएँ MCP क्लाइंट्स को प्रदान कर सकते हैं।