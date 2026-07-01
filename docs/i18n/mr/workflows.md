# तुमचा कार्यप्रवाह निवडा

Co-op Translator तीन पद्धतींनी वापरला जाऊ शकतो: CLI, Python API, आणि MCP सर्व्हर. त्यांच्या अनुवाद क्षमतांमध्ये साम्य आहे, परंतु प्रत्येक वेगळ्या कार्यप्रवाहाला जुळते.

हे पृष्ठ वापरा जेव्हा तुम्ही कुठून सुरू करायचे हे ठरवत असता.

## त्वरित निर्णय

| तुम्हाला हवे असल्यास... | वापर | येथे सुरू करा |
| --- | --- | --- |
| टर्मिनलमधून रेपॉझिटरीचे अनुवाद किंवा पुनरावलोकन करायचे असतील | CLI | [CLI संदर्भ](cli.md) |
| Python स्क्रिप्ट, सेवा, नोटबुक, किंवा CI जॉबमध्ये अनुवाद जोडा | Python API | [Python API](api.md) |
| एजंट, एडिटर, किंवा MCP-सुसंगत क्लायंटला तुमच्यासाठी सामग्री अनुवादित करु द्यायचे असले | MCP सर्व्हर | [MCP Server](mcp.md) |
| तुमच्या अ‍ॅपने आधीच लोड केलेला एक Markdown दस्तऐवज, नोटबुक किंवा प्रतिमा अनुवादित करायची असले | Python API किंवा MCP सर्व्हर | [Python API](api.md) किंवा [MCP Server](mcp.md) |
| मानक आउटपुट फोल्डर्स आणि मेटाडेटा असलेली पूर्ण रेपॉझिटरी अनुवादित करायची असले | CLI किंवा `run_translation` | [CLI संदर्भ](cli.md) किंवा [Python API](api.md) |

## CLI वापरा जेव्हा

जेव्हा एखादी व्यक्ती किंवा CI जॉब शेलमधून रेपॉझिटरी अनुवाद चालवत असेल तेव्हा CLI निवडा.

CLI हा सर्वात थेट मार्ग आहे जेव्हा तुम्हाला Co-op Translator कडून प्रोजेक्ट फाइल्स शोधावयाच्या असतील, अनुवादित आउटपुट तयार करायचे असतील, प्रोजेक्ट लेआउट जतन करायचा असेल, मेटाडेटा अपडेट करायचे असेल, आणि पुनरावलोकन कमांड्स चालवायच्या असतील.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

योग्य परिस्थिती:

- तुम्ही टर्मिनलमधून रेपॉझिटरी अनुवादित करत आहात.
- CI किंवा रिलीज वर्कफ्लोकरिता तुम्हाला पुन्हा चालवता येणारा कमांड हवा आहे.
- तुम्हाला अंगभूत प्रोजेक्ट शोध, आउटपुट पाथ, मेटाडेटा, क्लीनअप, आणि पुनरावलोकन हवे आहेत.
- Python कोड लिहिण्यापेक्षा तुम्हाला कमांड इंटरफेस प्राधान्य आहे.

## Python API वापरा जेव्हा

जेव्हा तुमच्या स्वतःच्या कोडने कार्यप्रवाह नियंत्रित करायचा असेल तेव्हा Python API निवडा.

API अनुप्रयोगांसाठी, ऑटोमेशन स्क्रिप्टसाठी, नोटबुकसाठी, सेवांसाठी आणि सानुकूल पाइपलाइन्ससाठी उपयुक्त आहे. हे तुम्हाला वैयक्तिक फाइलसाठी लो-लेव्हल कंटेंट अनुवाद API कॉल करण्याची परवानगी देते, किंवा CLI द्वारा वापरले जाणारे तेच रेपॉझिटरी-लेव्हल ऑर्केस्ट्रेशन चालवू देते.

एक Markdown दस्तऐवज अनुवादित करा आणि तो कुठे जतन करायचा ते ठरवा:

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

योग्य परिस्थिती:

- तुमची अ‍ॅप आधीच फाइल्स, बफर, नोटबुक किंवा इमेज बाइट्स वाचते.
- तुम्हाला सानुकूल व्हॅलिडेशन, स्टोरेज, लॉगिंग, पुनर्नियत्न किंवा मंजुरी प्रवाहांची गरज आहे.
- पूर्ण रेपॉझिटरी प्रक्रिया न करता एक दस्तऐवज, नोटबुक किंवा प्रतिमा अनुवादित करायची आहे.
- तुम्हाला रेपॉझिटरी अनुवाद हवा आहे, परंतु शेल कमांडऐवजी Python ऑटोमेशनमधून.

## MCP सर्व्हर वापरा जेव्हा

जेव्हा एजंट, एडिटर, किंवा MCP-सुसंगत क्लायंट Co-op Translator टूल्स कॉल करायला हवा तेव्हा MCP सर्व्हर निवडा.

नॉर्मल लोकल सेटअपमध्ये, वापरकर्ता मॅन्युअली सर्व्हर चालू ठेवत नाही. जेव्हा MCP क्लायंटला टूल्सची गरज असते तेव्हा ते `co-op-translator-mcp` ला `stdio` वरून सुरू करते.

उदाहरणार्थ वापरकर्त्याच्या विनंत्या ज्यांना एजंट हाताळू शकेल:

- "हा Markdown फाइल कोरियनमध्ये अनुवादित करा आणि दुवे बरोबर ठेवा."
- "एजंट-सहाय्यक MCP वर्कफ्लो वापरून हा Markdown फाइल कोरियनमध्ये अनुवादित करा, अनुवादित भागांसाठी तुमचा स्वतःचा मॉडेल वापरा."
- "हा नोटबुक कोरियनमध्ये अनुवादित करा, कोड सेल्स जतन करा, आणि नोटबुक पुन्हा तयार करण्यासाठी Co-op Translator MCP वापरा."
- "या प्रतिमेमधील मजकूर जपानीमध्ये अनुवादित करा आणि परिणाम जतन करा."
- "रेपॉझिटरीचा अनुवाद स्पॅनिशमध्ये ड्राय-रन करा आणि मला सांगा काय बदल होईल."
- "कोरियन अनुवाद आउटपुट अद्ययावत आहे की नाही ते पुनरावलोकन करा."

Markdown आणि नोटबुकसाठी, MCP दोन मोडमध्ये काम करू शकते:

| मोड | कधी वापरावे | मुख्य टूल्स |
| --- | --- | --- |
| Agent-assisted | MCP होस्ट एजंटने त्याच्या स्वतःच्या मॉडेलने चंक अनुवाद करावेत, Co-op Translator LLM प्रदाता क्रेडेन्शियल्स न वापरता. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator ने Azure OpenAI किंवा OpenAI थेट कॉल केले पाहिजे. | `translate_markdown_content`, `translate_notebook_content` |

MCP प्रदाता-आधारित Markdown टूल कॉलचे स्वरुप:

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

MCP प्रतिमा टूल कॉलचे स्वरुप:

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

MCP द्वारे रेपॉझिटरी अनुवाद डीफॉल्टने ड्राय-रन केला जातो:

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

- तुम्हाला एजंट किंवा एडिटरमध्ये नैसर्गिक-भाषा अनुवाद वर्कफ्लो हवे आहेत.
- तुम्हाला असा Markdown किंवा नोटबुक अनुवाद हवा आहे ज्यात होस्ट एजंट मॉडेल तयार केलेले चंक्स अनुवादित करते.
- पूर्ण रेपॉझिटरीऐवजी निवडलेली सामग्री एजंटने अनुवादित करावी असे तुम्हाला पाहिजे.
- रेपॉझिटरी-व्यापी लेखनापूर्वी मंजुरी टप्पा हवा आहे.
- तुम्हाला एकच इंटरफेस हवे जे Markdown, नोटबुक, प्रतिमा, पुनरावलोकन आणि पाथ-रीरायटिंग टूल्स प्रदर्शित करतो.

## ते कसे एकत्र बसतात

रेपॉझिटरी अनुवाद करणाऱ्या माणसांसाठी CLI हा सर्वोत्तम डीफॉल्ट आहे. जेव्हा तुमचा कोड कार्यप्रवाहाचा मालक असतो तेव्हा Python API सर्वोत्तम आहे. जेव्हा एजंट किंवा एडिटर कार्यप्रवाहाचा मालक असतो तेव्हा MCP सर्व्हर सर्वोत्तम आहे.

या तीनही मार्गांचा वापर एकाच सार्वजनिक Co-op Translator API करतात, त्यामुळे तुम्ही CLI ने सुरू करू शकता, नंतर Python ने ऑटोमेशन करू शकता, आणि जेव्हा तुम्हाला एजंट-चालित वर्कफ्लोची गरज असेल तेव्हा तेच क्षमता MCP क्लायंटसाठी उघडू शकता.