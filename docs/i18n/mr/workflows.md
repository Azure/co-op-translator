# तुमचा कार्यप्रवाह निवडा

Co-op Translator तीन मार्गांनी वापरता येतो: CLI, Python API, आणि MCP सर्व्हर. त्यांची अनुवाद क्षमता समान आहे, परंतु प्रत्येक वेगळ्या कार्यप्रवाहासाठी योग्य आहे.

कोठून सुरू करायचे हे ठरवताना ह्या पृष्ठाचा वापर करा.

**If you edit translations by hand:** डीफॉल्ट CLI आणि Actions कार्यप्रवाह बदललेले स्रोत फाइल पूर्णपणे पुन्हा अनुवाद करतात, त्यामुळे त्या फाइलमधील तुमची शब्दरचना अधिलेखित होऊ शकते. अपडेट स्वीकारण्यापूर्वी diff तपासा. स्वीकारलेल्या संपादना Markdown ब्लॉक-स्तरीय संरक्षित ठेवण्यासाठी, ऐच्छिक [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) वापरा.

## त्वरित निर्णय

| जर तुम्हाला... | वापरा | येथे सुरू करा |
| --- | --- | --- |
| टर्मिनलमधून रेपॉझिटरीचे अनुवाद करा किंवा पुनरावलोकन करा | CLI | [CLI Reference](cli.md) |
| Python स्क्रिप्ट, सेवा, नोटबुक किंवा CI जॉब मध्ये अनुवाद जोडा | Python API | [Python API](api.md) |
| एजंट, एडिटर, किंवा MCP-सुसंगत क्लाएंट तुमच्यासाठी सामग्री अनुवाद करु शकतात | MCP Server | [MCP Server](mcp.md) |
| तुमच्या अ‍ॅपने आधीच लोड केलेला एक Markdown दस्तऐवज, नोटबुक किंवा प्रतिमा अनुवाद करा | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| सामान्य आउटपुट फोल्डर आणि मेटाडेटासह पूर्ण रेपॉझिटरी अनुवाद करा | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## CLI वापरा जेव्हा

CLI निवडा जेव्हा एखादी व्यक्ती किंवा CI जॉब शेलमधून रेपॉझिटरी अनुवाद चालवत आहे.

जेव्हा तुम्हाला Co-op Translator ला प्रोजेक्ट फाइल्स शोधून काढाव्यात, अनुवादित आउटपुट तयार करायचे असतील, प्रोजेक्ट लेआउट जपायचे असतील, मेटाडेटा अपडेट करायचे असतील, आणि पुनरावलोकन कमांड चालवायच्या असतील, तेव्हा CLI हा सर्वात थेट मार्ग आहे.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

हे उदाहरण Markdown आणि नोटबुकचे भाषांतर करते. फक्त [Azure AI Vision](configuration.md#azure-ai-vision) कॉन्फिगर केल्यावरच `-img` जोडा. केवळ Markdown साठी प्रथम रनसाठी, [तुमचा पहिला अनुवाद](first-translation.md) अनुसरा.

योग्य परिस्थिती:

- तुम्ही तुमच्या टर्मिनलमधून रेपॉझिटरी अनुवाद करत आहात.
- तुम्हाला CI किंवा रिलीज कार्यप्रवाहांसाठी पुन्हा वापरता येण्याजोगी कमांड हवी आहे.
- तुम्हाला अंगभूत प्रोजेक्ट शोध, आउटपुट पाथ, मेटाडेटा, साफसफाई आणि पुनरावलोकन हवे आहेत.
- Python कोड लिहिण्यापेक्षा तुम्हाला कमांड इंटरफेस प्राधान्य आहे.

## Python API वापरा जेव्हा

Python API निवडा जेव्हा तुमच्या स्वतःच्या कोडने कार्यप्रवाह नियंत्रित करावा.

API अनुप्रयोगांसाठी, ऑटोमेशन स्क्रिप्ट्स, नोटबुक्स, सेवांसाठी आणि कस्टम पाईपलाइन्ससाठी उपयुक्त आहे. हे तुम्हाला वैयक्तिक फाइलसाठी कमी-स्तरीय कंटेंट अनुवाद API कॉल करण्याची परवानगी देते, किंवा CLI द्वारे वापरल्या जाणाऱ्या त्याच रेपॉझिटरी-स्तरीय ऑर्केस्ट्रेशन चालवू देते.

एक Markdown दस्तऐवज अनुवाद करा आणि ते कुठे जतन करायचे ठरवा:

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

Python मधून रेपॉझिटरी अनुवाद चालवा:

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

योग्य परिस्थिती:

- तुमचे अ‍ॅप आधीच फाइल्स, बफर्स, नोटबुक्स किंवा इमेज बाइट्स वाचते.
- तुम्हाला कस्टम व्हॅलिडेशन, स्टोरेज, लॉगिंग, रीट्राईज किंवा अनुमोदन प्रवाहांची गरज आहे.
- तुम्हाला संपूर्ण रेपॉझिटरी प्रक्रिया न करता एक दस्तऐवज, नोटबुक किंवा प्रतिमा अनुवादायची आहे.
- तुम्हाला रेपॉझिटरी अनुवाद हवा आहे, पण शेल कमांडऐवजी Python ऑटोमेशनमधून.

## MCP Server वापरा जेव्हा

MCP सर्व्हर निवडा जेव्हा एखादा एजंट, एडिटर, किंवा MCP-सुसंगत क्लाएंट Co-op Translator टूल्स कॉल करेल.

साध्या लोकल सेटअपमध्ये, वापरकर्ता मॅन्युअली सर्व्हर चालू ठेवत नाही. जेव्हा टूल्सची आवश्यकता असते तेव्हा MCP क्लाएंट `stdio` वर `co-op-translator-mcp` सुरू करतो.

एजंट खालील प्रकारच्या वापरकर्ता विनंत्या हाताळू शकतो:

- "हा Markdown फाइल कोरियनमध्ये अनुवाद करा आणि दुवे योग्य राखा."
- "हा Markdown फाइल एजंट-सहाय्यक MCP कार्यप्रवाहाने कोरियनमध्ये अनुवाद करा, अनुवादित भागांसाठी तुमचे स्वतःचे मॉडेल वापरून."
- "हा नोटबुक कोरियनमध्ये अनुवाद करा, कोड सेल जतन करा, आणि नोटबुक पुन्हा तयार करण्यासाठी Co-op Translator MCP वापरा."
- "या प्रतिमेतील मजकूर जपानीत अनुवाद करा आणि परिणाम जतन करा."
- "रेपॉझिटरी अनुवाद स्पॅनिशमध्ये ड्राय-रन करा आणि काय बदल होईल ते सांगा."
- "कोरियन अनुवाद आउटपुट अद्ययावत आहे का ते पुनरावलोकन करा."

Markdown आणि नोटबुकसाठी, MCP दोन मोडमध्ये काम करू शकतो:

| मोड | वापरा जेव्हा | मुख्य साधने |
| --- | --- | --- |
| Agent-assisted | MCP होस्ट एजंटने आपल्या स्वतःच्या मॉडेलने चंक्स अनुवाद करावेत, Co-op Translator LLM प्रदाता क्रेडेन्शियल्सशिवाय. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator ने थेट Azure OpenAI, OpenAI, किंवा Anthropic कॉल करावे. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown टूल कॉल स्वरूप:

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

MCP इमेज टूल कॉल स्वरूप:

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

रेपॉझिटरी अनुवाद डीफॉल्टनुसार MCP द्वारे ड्राय-रन केला जातो:

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

योग्य परिस्थिती:

- तुम्हाला एजंट किंवा एडिटरमध्ये नैसर्गिक-भाषेतील अनुवाद कार्यप्रवाह हवा आहे.
- तुम्हाला Markdown किंवा नोटबुक अनुवाद हवा आहे ज्यात होस्ट एजंट मॉडेल तयार केलेले चंक अनुवाद करते.
- तुम्हाला संपूर्ण रेपॉझिटरीऐवजी एजंटने निवडलेला सामग्री अनुवाद करावी असे आहे.
- रेपॉझिटरी-व्यापी लेखन करण्यापूर्वी तुम्हाला अनुमोदन पाऊल हवे आहे.
- तुम्हाला एकच इंटरफेस हवे आहे जे Markdown, नोटबुक, प्रतिमा, पुनरावलोकन आणि पथ-पुनर्लेखन साधने उपलब्ध करून देते.

## ते एकत्र कसे बसतात

रेपॉझिटरी अनुवादणाऱ्या मानवांसाठी CLI हा सर्वोत्तम डीफॉल्ट आहे. जेव्हा तुमच्या कोडने कार्यप्रवाह नियंत्रित करायचा असेल तेव्हा Python API सर्वोत्तम आहे. जेव्हा एजंट किंवा एडिटर कार्यप्रवाहाचे मालक असेल तेव्हा MCP सर्व्हर सर्वोत्तम आहे.

या तीनही मार्गांनी एकाच सार्वजनिक Co-op Translator API चा वापर केला जातो, त्यामुळे तुम्ही CLI ने सुरुवात करू शकता, नंतर Python ने ऑटोमेट करू शकता, आणि जेव्हा एजंट-चालित कार्यप्रवाहांची गरज असेल तेव्हा त्याच क्षमता MCP क्लाएंटसाठी उघडू शकता.