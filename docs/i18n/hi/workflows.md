# अपना वर्कफ़्लो चुनें

Co-op Translator को तीन तरीकों से उपयोग किया जा सकता है: CLI, Python API, और MCP सर्वर। इनकी अनुवाद क्षमताएँ समान हैं, लेकिन हर एक अलग वर्कफ़्लो के लिए उपयुक्त है।

शुरू करने का निर्णय करते समय इस पृष्ठ का उपयोग करें।

## त्वरित निर्णय

| यदि आप चाहते हैं कि... | उपयोग करें | यहाँ शुरू करें |
| --- | --- | --- |
| एक टर्मिनल से रिपॉज़िटरी का अनुवाद या समीक्षा करें | CLI | [CLI संदर्भ](cli.md) |
| एक Python स्क्रिप्ट, सेवा, नोटबुक, या CI जॉब में अनुवाद जोड़ें | Python API | [Python API](api.md) |
| किसी एजेंट, संपादक, या MCP-संगत क्लाइंट को आपके लिए सामग्री अनुवाद करने दें | MCP Server | [MCP सर्वर](mcp.md) |
| एक Markdown दस्तावेज़, नोटबुक, या इमेज अनुवाद करें जो आपकी ऐप पहले ही लोड कर चुकी है | Python API या MCP Server | [Python API](api.md) या [MCP सर्वर](mcp.md) |
| मानक आउटपुट फ़ोल्डर्स और मेटाडेटा के साथ पूरी रिपॉज़िटरी का अनुवाद करें | CLI या `run_translation` | [CLI संदर्भ](cli.md) या [Python API](api.md) |

## CLI का उपयोग तब करें जब

CLI चुनें जब कोई व्यक्ति या CI जॉब शेल से रिपॉज़िटरी अनुवाद चला रहा हो।

CLI सबसे प्रत्यक्ष मार्ग है जब आप चाहते हैं कि Co-op Translator प्रोजेक्ट फ़ाइलों का पता लगाए, अनूदित आउटपुट बनाए, प्रोजेक्ट लेआउट संरक्षित रखे, मेटाडेटा अपडेट करे, और समीक्षा कमांड चलाए।

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

उपयुक्त स्थितियाँ:

- आप अपनी टर्मिनल से एक रिपॉज़िटरी का अनुवाद कर रहे हैं।
- आप CI या रिलीज़ वर्कफ़्लो के लिए एक दोहराने योग्य कमांड चाहते हैं।
- आप इन-बिल्ट प्रोजेक्ट डिस्कवरी, आउटपुट पाथ, मेटाडेटा, क्लीनअप, और समीक्षा चाहते हैं।
- आप Python कोड लिखने के बजाय कमांड इंटरफ़ेस पसंद करते हैं।

## Python API का उपयोग कब करें

Python API चुनें जब आपका अपना कोड वर्कफ़्लो को नियंत्रित करना चाहिए।

API वही काम एप्लिकेशन, ऑटोमेशन स्क्रिप्ट, नोटबुक, सेवाएँ, और कस्टम पाइपलाइनों के लिए उपयोगी बनाती है। यह आपको व्यक्तिगत फाइलों के लिए लो-लेवल कंटेंट अनुवाद APIs कॉल करने या CLI द्वारा उपयोग किए जाने वाले समान रिपॉज़िटरी-लेवल ऑर्केस्ट्रेशन चलाने देती है।

एक Markdown दस्तावेज़ का अनुवाद करें और यह तय करें कि उसे कहाँ सहेजना है:

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

उपयुक्त स्थितियाँ:

- आपकी एप्लिकेशन पहले से फाइलें, बफ़र्स, नोटबुक, या इमेज बाइट्स पढ़ती है।
- आपको कस्टम वैलिडेशन, स्टोरेज, लॉगिंग, रिट्राइज, या अप्रूवल फ्लो चाहिए।
- आप एक दस्तावेज़, नोटबुक, या इमेज का अनुवाद करना चाहते हैं बिना पूरी रिपॉज़िटरी को प्रोसेस किए।
- आप रिपॉज़िटरी अनुवाद चाहते हैं, लेकिन शेल कमांड के बजाय Python ऑटोमेशन से।

## जब MCP सर्वर का उपयोग करें

MCP सर्वर चुनें जब किसी एजेंट, संपादक, या MCP-संगत क्लाइंट को Co-op Translator टूल्स कॉल करने चाहिए।

सामान्य लोकल सेटअप में, उपयोगकर्ता मैन्युअली सर्वर नहीं चलाता। MCP क्लाइंट तब `co-op-translator-mcp` को `stdio` के माध्यम से शुरू करता है जब उसे टूल्स चाहिए होते हैं।

उदाहरण उपयोगकर्ता अनुरोध जिन्हें एक एजेंट संभाल सकता है:

- "इस Markdown फ़ाइल को कोरियाई में अनुवाद करें और लिंक सही रखें।"
- "इस Markdown फ़ाइल को एजेंट-सहायित MCP वर्कफ़्लो के साथ कोरियाई में अनुवाद करें, अनूदित चंक्स के लिए आपका अपना मॉडल उपयोग करते हुए।"
- "इस नोटबुक को कोरियाई में अनुवाद करें, कोड सेल्स को संरक्षित रखें, और नोटबुक को पुनर्निर्माण करने के लिए Co-op Translator MCP का उपयोग करें।"
- "इस इमेज के टेक्स्ट को जापानी में अनुवाद करें और परिणाम सहेजें।"
- "रिपॉज़िटरी अनुवाद का ड्राई-रन स्पेनिश में करें और बताइए क्या बदलेगा।"
- "समीक्षा करें कि कोरियाई अनुवाद आउटपुट अप-टू-डेट है या नहीं।"

Markdown और नोटबुक के लिए, MCP दो मोड में काम कर सकता है:

| Mode | किस समय उपयोग करें | मुख्य उपकरण |
| --- | --- | --- |
| Agent-assisted | MCP होस्ट एजेंट को उसके अपने मॉडल के साथ चंक्स का अनुवाद करना चाहिए, बिना Co-op Translator LLM प्रदाता क्रेडेंशियल्स के। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator सीधे Azure OpenAI या OpenAI को कॉल करे। | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown टूल कॉल का रूप:

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

MCP इमेज टूल कॉल का रूप:

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

रिपॉज़िटरी अनुवाद MCP के माध्यम से डिफ़ॉल्ट रूप से ड्राई-रन होता है:

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

- आप एजेंट या एडिटर के अंदर नेचुरल-लैंग्वेज अनुवाद वर्कफ़्लो चाहते हैं।
- आप Markdown या नोटबुक अनुवाद चाहते हैं जहाँ होस्ट एजेंट तैयार किए गए चंक्स का अनुवाद करे।
- आप चाहते हैं कि एजेंट पूरे रिपॉज़िटरी के बजाय चयनित सामग्री का अनुवाद करे।
- आप रिपॉज़िटरी-व्यापी लेखन से पहले एक अनुमोदन चरण चाहते हैं।
- आप एक ऐसा इंटरफ़ेस चाहते हैं जो Markdown, नोटबुक, इमेज, समीक्षा, और पाथ-रिराइटिंग टूल्स एक्सपोज़ करे।

## वे कैसे एक साथ मिलते हैं

CLI मानवों के लिए रिपॉज़िटरी अनुवाद करने का सबसे अच्छा डिफ़ॉल्ट है। Python API तब सबसे अच्छा है जब आपका कोड वर्कफ़्लो का मालिक हो। MCP सर्वर तब सबसे अच्छा है जब एक एजेंट या एडिटर वर्कफ़्लो का मालिक हो।

इन तीनों पथों में वही सार्वजनिक Co-op Translator API उपयोग होती है, इसलिए आप CLI के साथ शुरू कर सकते हैं, बाद में Python से ऑटोमेशन कर सकते हैं, और जब आपको एजेंट-ड्रिवन वर्कफ़्लो चाहिए तब वही क्षमताएँ MCP क्लाइंट्स के लिए एक्सपोज़ कर सकते हैं।