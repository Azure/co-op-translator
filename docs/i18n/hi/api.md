# Python API

स्थिर सार्वजनिक Python API `co_op_translator.api` से निर्यात किया जाता है। अधिकांश एकीकरण इन कार्यप्रवाहों में से एक का उपयोग करते हैं:

| परिदृश्य | कब उपयोग करें | मुख्य API |
| --- | --- | --- |
| व्यक्तिगत फ़ाइलें या दस्तावेज़ अनुवादित करें | आपका एप्लिकेशन स्रोत सामग्री पढ़ता है, अनुवाद के लिए Co-op Translator को कॉल करता है, और परिणाम कहाँ सहेजना है यह तय करता है। | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| होस्ट-एजेंट अनुवाद के लिए सामग्री तैयार करें | आपका MCP होस्ट या एप्लिकेशन मॉडल चंक्स का अनुवाद करेगा, जबकि Co-op Translator चंक्स बनाना और पुनर्निर्माण संभालेगा। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| एक संपूर्ण रिपॉज़िटरी अनुवादित करें | आप चाहते हैं कि Python API CLI की तरह व्यवहार करे और डिस्कवरी, आउटपुट पथ, मेटाडेटा, क्लीनअप और लेखन संभाले। | `run_translation` |

`core`, `config`, `review`, और `utils` के अंतर्गत अधिकांश निचले-स्तर मॉड्यूल इन API एंट्री पॉइंट्स द्वारा उपयोग किए जाने वाले कार्यान्वयन विवरण हैं।

MCP क्लाइंट्स [MCP सर्वर](mcp.md) के माध्यम से वही सार्वजनिक API उपयोग करते हैं। सीधे Python कॉल करने पर इस पृष्ठ का उपयोग करें, और Co-op Translator को किसी एजेंट या संपादक के लिए एक्सपोज़ करते समय MCP गाइड का उपयोग करें। यदि आप CLI, Python API, और MCP के बीच निर्णय ले रहे हैं, तो [अपना कार्यप्रवाह चुनें](workflows.md) से शुरू करें।

## पहली बार API फ्लो

यदि आप Python कोड से Co-op Translator को कॉल कर रहे हैं तो यहाँ से शुरू करें:

1. एक LLM प्रदाता को [कॉन्फ़िगरेशन](configuration.md) में वर्णित के अनुसार कॉन्फ़िगर करें, जब तक कि आप केवल होस्ट-एजेंट अनुवाद के लिए Markdown या नोटबुक चंक्स ही तैयार नहीं कर रहे हों।
2. निर्णय लें कि क्या आपकी एप्लिकेशन फ़ाइल I/O संभालती है।
3. जब आपका एप्लिकेशन व्यक्तिगत फ़ाइलें पढ़ता और लिखता है तो कंटेंट API का उपयोग करें।
4. जब Co-op Translator को CLI की तरह किसी रिपॉज़िटरी को प्रोसेस करना चाहिए तब `run_translation` का उपयोग करें।
5. यदि ऑटोमेशन में आपको निर्धारक जाँचों की आवश्यकता है तो अनुवाद के बाद `run_review` का उपयोग करें।

| लक्ष्य | शुरू करने के लिए API |
| --- | --- |
| एक Markdown स्ट्रिंग या फ़ाइल अनुवादित करें | `translate_markdown_content` |
| एक नोटबुक पेलोड अनुवादित करें | `translate_notebook_content` |
| एक छवि अनुवादित करें | `translate_image_content` |
| होस्ट एजेंट को Markdown या नोटबुक चंक्स का अनुवाद करने दें | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| आउटपुट पथ चुनने के बाद अनुवादित लिंक पुनर्लेखित करें | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| एक पूरी रिपॉज़िटरी अनुवादित करें | `run_translation` |
| अनुवादित आउटपुट की समीक्षा करें | `run_review` |

## परिदृश्य 1: व्यक्तिगत फ़ाइलें या दस्तावेज़ अनुवादित करें

जब आपके पास पहले से ही एक फ़ाइल, एडिटर बफर, नोटबुक पेलोड, MCP अनुरोध, या कस्टम पाइपलाइन इनपुट मौजूद हो तो इस वर्कफ़्लो का उपयोग करें। आपका कोड फ़ाइल I/O का मालिक है:

1. स्रोत सामग्री पढ़ें।
2. किसी कंटेंट अनुवाद API को कॉल करें।
3. वैकल्पिक रूप से पथ पुनर्लेखन API को कॉल करें यदि अनुवादित सामग्री को किसी प्रोजेक्ट ट्रांसलेशन फ़ोल्डर में लिखा जाएगा।
4. अपने एप्लिकेशन से परिणाम सहेजें या लौटाएँ।

कंटेंट अनुवाद API प्रोजेक्ट डिस्कवरी नहीं चलाते, मेटाडेटा नहीं लिखते, डिस्क्लेमर नहीं जोड़ते, और स्वतः लिंक पुनर्लेखन नहीं करते।

### Markdown फ़ाइल

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

यदि अनुवादित Markdown Co-op Translator प्रोजेक्ट लेआउट में नहीं रहेगा, तो `rewrite_markdown_paths` छोड़ दें और अनुवादित स्ट्रिंग को सीधे सहेजें।

### नोटबुक फ़ाइल

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` Markdown सेल्स का अनुवाद करता है और नॉन-Markdown सेल्स को संरक्षित रखता है। पथ पुनर्लेखन केवल Markdown सेल्स पर लागू होता है।

### इमेज फ़ाइल

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` स्रोत इमेज को पढ़ता है और एक रेंडर्ड `PIL.Image.Image` लौटाता है। यह अनुवादित इमेज मेटाडेटा नहीं लिखता।

## परिदृश्य 2: एक संपूर्ण रिपॉज़िटरी अनुवादित करें

जब आप चाहते हैं कि Python API `translate` CLI की तरह व्यवहार करे तब इस वर्कफ़्लो का उपयोग करें। `run_translation` समर्थित फ़ाइलों को खोजता है, चुनी गई सामग्री प्रकारों का अनुवाद करता है, पथों को पुनर्लेखित करता है, आउटपुट फ़ाइलें लिखता है, मेटाडेटा अपडेट करता है, और क्लीनअप जैसे अनुवाद रखरखाव कार्य करता है।

`run_translation` पसंदीदा प्रोजेक्ट ऑर्केस्ट्रेशन एंट्री पॉइंट है। `translate_project` समान व्यवहार के साथ कम्पैटिबिलिटी उपनाम के रूप में एक्सपोर्ट किया गया है।

वर्तमान रिपॉज़िटरी में Markdown फ़ाइलों को कोरियाई और जापानी में अनुवादित करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

विशिष्ट प्रोजेक्ट रूट से केवल नोटबुक्स अनुवादित करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

फ़ाइलें लिखे बिना अनुवाद वॉल्यूम का पूर्वावलोकन करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

एक इंटीग्रेशन के लिए संरचित प्रगति इवेंट रिकॉर्ड करें:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # पेलोड को अपनी job-event तालिका में संग्रहीत करें या इसे अपने UI पर स्ट्रीम करें।


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

इवेंट्स संस्करणित स्कीमा `co-op.translation.event.v1` का उपयोग करते हैं। इंटीग्रेशन को
ऐसे स्थिर फ़ील्ड्स पर निर्भर होना चाहिए जैसे `type` और `stage_key`, न कि मानव-समक्ष
कंसोल टेक्स्ट या `stage_label` पर।

एक ही कॉल में कई कंटेंट रूट्स का अनुवाद करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

स्पष्ट आउटपुट समूहों में अनुवादों को लिखें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

जब प्रत्येक भाषा में एक नेस्टेड उप-निर्देशिका होनी चाहिए तो प्रति-भाषा प्लेसहोल्डर का उपयोग करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

यदि `markdown`, `notebook`, या `images` में से कोई भी सेट नहीं है, तो API सभी समर्थित प्रकारों का अनुवाद करता है: Markdown, नोटबुक, और इमेज।

### स्वीकृत मानव संपादन को TranslationStateProvider के साथ संरक्षित करें

डिफ़ॉल्ट रूप से, Co-op Translator अपनी मौजूदा फ़айл-स्तर व्यवहार बनाए रखता है: जब एक
Markdown स्रोत पुराना हो जाता है, तो पूरी अनुवादित फ़ाइल पुनः उत्पन्न की जाती है। होस्टेड
इंटीग्रेशन वैकल्पिक रूप से `TranslationStateProvider` पास कर सकते हैं ताकि मानव
स्रोत ब्लॉकों में किए गए संपादन जिन्हें बदला नहीं गया है संरक्षित रहें।

प्रदाता अंतिम स्वीकृत स्रोत/लक्ष्य युग्म प्रदान करता है और प्रत्येक नए
उम्मीदवार को रिकॉर्ड करता है। स्वीकृति इंटीग्रेशन की जिम्मेदारी बनी रहती है—उदाहरण के लिए,
जब अनुवाद पुल अनुरोध मर्ज हो जाए:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

वैध स्वीकृत बेसलाइन वाले Markdown फ़ाइलों के लिए, Co-op Translator
शीर्ष-स्तरीय Markdown ब्लॉकों को संरेखित करता है। अपरिवर्तित स्रोत ब्लॉक्स वर्तमान अनुवादित
ब्लॉक्स का पुन: उपयोग करते हैं, जिनमें लोगों द्वारा किए गए संपादन शामिल हैं; बदले गए या जोड़े गए स्रोत ब्लॉक्स अनुवाद के लिए भेजे जाते हैं
; हटाए गए स्रोत ब्लॉक्स हटा दिए जाते हैं। यदि संरेखण अस्पष्ट है,
लक्ष्य संरचना बदल गई है, किसी ब्लॉक का अनुवाद अमान्य है, या कोई बेसलाइन उपलब्ध नहीं है,
तो Co-op Translator सुरक्षित रूप से मौजूदा पूर्ण-फ़ाइल
अनुवाद पथ पर वापस चला जाता है।

यह API दस्तावेज़ अनुवाद स्थिति संग्रहीत करती है, न कि दस्तावेज़ों के पार वाक्यांश या
सेगमेंट अनुवाद मेमोरी। यह वर्तमान में Markdown प्रोजेक्ट अनुवाद पर लागू होती है।
नोटबुक और इमेज व्यवहार अपरिवर्तित रहता है। `update=True` पास करने से
फिर भी पूर्ण पुनरुत्पादन का अनुरोध होता है।

यदि एक या अधिक फाइलों का अनुवाद नहीं किया जा सकता, तो `run_translation` एक
`RuntimeError` फ़ेंकता है परियोजना वर्कफ़्लो समाप्त होने के बाद, बजाय यह रिपोर्ट करने के
कि सफल रन हुआ लेकिन आउटपुट गायब है। इंटीग्रेशन को इसे एक असफल
जॉब मानना चाहिए और पूर्व स्वीकृत अनुवाद स्थिति बनाए रखनी चाहिए।

## अनुवादित आउटपुट की समीक्षा करें

`run_review` LLM या Vision क्रेडेंशियल्स के बिना निर्धारक अनुवाद जाँचें चलाता है।

!!! note "बीटा"
    `run_review` एक बीटा निर्धारक समीक्षा API है। यह मॉडल प्रदाताओं को कॉल नहीं करता और न ही फ़ाइलें लिखता है, पर चेक और इशू स्कीमाएँ विकसित हो सकती हैं।

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README-केवल अनुवाद के बाद, समीक्षा के लिए वही स्कोप इस्तेमाल करें:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` केवल प्रत्येक कॉन्फ़िगर किए गए सोर्स रूट के अंतर्गत `README.md` की समीक्षा करता है,
including custom `groups` and output directories. Other documents and nested
READMEs are excluded. A missing source README raises `ValueError`; failed
translation checks raise `RuntimeError`.

केवल बेस रेफ़ के खिलाफ बदले गए फाइलों की समीक्षा करें और GitHub-flavored आउटपुट प्रिंट करें:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## कॉपी-पेस्ट API उदाहरण

फाइल लिखे बिना Markdown सामग्री का अनुवाद करें:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Markdown लिंक का अनुवाद और पुनर्लेखन करें:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Python से एक रिपॉज़िटरी का अनुवाद करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

कई रूट्स का अनुवाद करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

ग्लोसरी शब्दों को बनाए रखें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## सार्वजनिक एंट्री पॉइंट्स

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## सामग्री अनुवाद APIs

सामग्री अनुवाद APIs उन इंटीग्रेशन के लिए हैं जिनके पास पहले से ही स्मृति में सामग्री होती है, जैसे कि एक एडिटर एक्सटेंशन, MCP टूल, नोटबुक प्रोसेसर, या कस्टम पाइपलाइन।

| फ़ंक्शन | इनपुट | आउटपुट | फ़ाइल I/O | नोट्स |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. केवल Markdown सामग्री का अनुवाद करता है। यह लिंक पुनर्लेखन नहीं करता, मेटाडेटा नहीं लिखता, और अस्वीकरण नहीं जोड़ता। |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown सेल्स का अनुवाद करता है और non-Markdown सेल्स को संरक्षित रखता है। यह लिंक पुनर्लेखन नहीं करता, मेटाडेटा नहीं लिखता, और अस्वीकरण नहीं जोड़ता। |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. इमेज टेक्स्ट निकालता और अनुवाद करता है, फिर एक रेंडर की हुई इमेज लौटाता है। यह अनूदित इमेज मेटाडेटा सहेजता नहीं है। |

`translate_markdown_content` और `translate_notebook_content` अपने विकल्पों के माध्यम से वैकल्पिक `source_path` स्वीकार करते हैं। पाथ ट्रांसलेटर को संदर्भ के रूप में पास किया जाता है; कॉलर अनुवाद के बाद किसी भी प्रोजेक्ट-विशेष पथ पुनर्लेखन के लिए जिम्मेदार रहते हैं।

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

उसी विकल्पों को डिक्शनरी के रूप में पास किया जा सकता है:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## एजेंट-सहायित अनुवाद APIs

एजेंट-सहायित APIs Co-op Translator से कॉन्फ़िगर किए गए LLM प्रदाता को कॉल नहीं करतीं। ये एक होस्ट एजेंट द्वारा अनुवाद के लिए Markdown या नोटबुक चंक्स तैयार करती हैं, और फिर अनूदित चंक्स से अंतिम सामग्री का पुनर्निर्माण करती हैं।

| फ़ंक्शन | उद्देश्य |
| --- | --- |
| `start_markdown_agent_translation` | स्व-निहित Markdown जॉब हिस्सों, प्रांप्ट्स, और पुनर्निर्माण स्थिति के साथ लौटाता है। |
| `finish_markdown_agent_translation` | जॉब और होस्ट-एजेंट द्वारा अनुवादित हिस्सों से Markdown पुनर्निर्माण करता है। |
| `start_notebook_agent_translation` | होस्ट-एजेंट अनुवाद के लिए Markdown-सेल हिस्सों के साथ एक नोटबुक जॉब लौटाता है। |
| `finish_notebook_agent_translation` | कोड सेल्स, आउटपुट्स, और मेटाडेटा को संरक्षित रखते हुए नोटबुक JSON पुनर्निर्माण करता है। |

यह वर्कफ़्लो मुख्य रूप से MCP होस्ट्स के लिए है। यदि आपको प्रोडक्शन रिपॉज़िटरी अनुवाद चाहिए जिसमें Co-op Translator प्रदाता कॉल्स का प्रबंधन करे, तो `translate_markdown_content`, `translate_notebook_content`, या `run_translation` उपयोग करें।

## पाथ पुनर्लेखन APIs

पाथ पुनर्लेखन APIs कोई अनुवाद नहीं करतीं। वे लिंक और frontmatter पाथ्स को अपडेट करती हैं जब कॉलर्स को स्रोत पाथ, अनूदित लक्षित पाथ, और प्रोजेक्ट लेआउट ज्ञात हो।

| फ़ंक्शन | स्कोप | नोट्स |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown बॉडी और फ्रंटमैटर | अनुवादित लक्ष्य के लिए Markdown लिंक और समर्थित फ्रंटमैटर पथ फ़ील्ड्स को पुनर्लेखन करता है। |
| `rewrite_notebook_paths` | Notebook JSON में Markdown सेल्स | प्रत्येक Markdown सेल पर Markdown पथ पुनर्लेखन लागू करता है और गैर-Markdown सेल्स को अपरिवर्तित छोड़ता है। |

`policy` आर्गुमेंट इन फ़ील्ड्स के साथ एक डिक्शनरी हो सकता है:

| फ़ील्ड | आवश्यक | उद्देश्य |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | नहीं | सक्षम अनुवाद प्रकार। डिफ़ॉल्ट: Markdown, नोटबुक, और छवियाँ। |
| `lang_subdir` | नहीं | प्रत्येक भाषा फ़ोल्डर के भीतर वैकल्पिक उपनिर्देशिका। |

## प्रोजेक्ट अनुवाद पैरामीटर

| पैरामीटर | टाइप | डिफ़ॉल्ट | उद्देश्य |
| --- | --- | --- | --- |
| `language_codes` | `str` | आवश्यक | स्पेस-से पृथक लक्ष्य भाषा कोड, जैसे `"ko ja fr"` या `"all"`। उपनाम कोडों को मानक BCP 47 मानों में सामान्यीकृत किया जाता है। |
| `root_dir` | `str` | `"."` | एकल अनुवाद लक्ष्य के लिए प्रोजेक्ट रूट। जब `root_dirs` या `groups` प्रदान किए जाते हैं तो इसे अनदेखा किया जाता है। |
| `update` | `bool` | `False` | चयनित भाषाओं के लिए मौजूदा अनुवादों को हटाएं और पुनः बनाएं। |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | DEBUG-स्तर की लॉग फ़ाइलों को रूट `logs/` निर्देशिका के अंतर्गत सहेजें। |
| `yes` | `bool` | `True` | प्रोग्रामेटिक और CI उपयोग के लिए संकेतों को स्वचालित रूप से पुष्टि करें। |
| `add_disclaimer` | `bool` | `False` | अनुवादित Markdown और नोटबुक में मशीन-अनुवाद अस्वीकरण जोड़ें। |
| `translations_dir` | `str \| None` | `None` | कस्टम टेक्स्ट अनुवाद आउटपुट निर्देशिका। सापेक्ष पथ प्रत्येक रूट के सापेक्ष सुलझाए जाते हैं। |
| `image_dir` | `str \| None` | `None` | कस्टम अनुवादित इमेज आउटपुट निर्देशिका। सापेक्ष पथ प्रत्येक रूट के सापेक्ष सुलझाए जाते हैं। |
| `root_dirs` | `Iterable[str] \| None` | `None` | एकाधिक रूट जो समान आउटपुट सेटिंग्स साझा करते हैं। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. Takes precedence over `root_dirs`. |
| `repo_url` | `str \| None` | `None` | README भाषा तालिका मार्गदर्शन को रेंडर करते समय उपयोग किया जाने वाला रिपॉजिटरी URL। |
| `glossaries` | `Iterable[str] \| None` | `None` | अनुवाद के दौरान संरक्षित करने के लिए शब्दावली शब्द। डुप्लिकेट और खाली शब्द सामान्यीकृत किए जाते हैं। |
| `dry_run` | `bool` | `False` | फ़ाइलें लिखे बिना अनुवाद वॉल्यूम का अनुमान लगाएँ और माइग्रेशन व्यवहार का पूर्वावलोकन करें। |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | इन्क्रीमेंटल Markdown अपडेट्स के लिए वैकल्पिक accepted-baseline और candidate persistence एडेप्टर। इसे छोड़ने से मौजूदा पूर्ण-फ़ाइल व्यवहार संरक्षित रहता है। |

## समीक्षा पैरामीटर

`run_review` जहां संभव हो `run_translation` सिग्नेचर को जानबूझकर प्रतिबिंबित करता है ताकि ऑटोमेशन अनुवाद और समीक्षा वर्कफ़्लो के बीच न्यूनतम ब्रांचिंग के साथ स्विच कर सके।

| पैरामीटर | प्रकार | डिफ़ॉल्ट | उद्देश्य |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | समीक्षा के लिए लक्षित भाषा फ़ोल्डर्स। स्पेस-सेपरेटेड स्ट्रिंग्स और इटेरेबल स्वीकार किए जाते हैं। `"all"` हर खोजी गई अनुवाद भाषा की समीक्षा करता है। |
| `root_dir` | `str` | `"."` | एकल समीक्षा लक्ष्य के लिए प्रोजेक्ट रूट। जब `root_dirs` या `groups` प्रदान किए जाते हैं तो अनदेखा किया जाता है। |
| `markdown` | `bool` | `False` | Markdown और MDX सोर्स फाइलों को शामिल करें। |
| `notebook` | `bool` | `False` | Jupyter नोटबुक सोर्स फाइलों को शामिल करें। |
| `images` | `bool` | `False` | अनुवाद विकल्पों के साथ समतुल्य के लिए आरक्षित। इमेज के लिंक संदर्भ Markdown से जाँच किए जाते हैं। |
| `translations_dir` | `str \| None` | `None` | कस्टम टेक्स्ट अनुवाद आउटपुट निर्देशिका। सापेक्ष पथ प्रत्येक रूट के सापेक्ष सुलझाए जाते हैं। |
| `root_dirs` | `Iterable[str] \| None` | `None` | एकाधिक रूट जो समान आउटपुट सेटिंग्स साझा करते हैं। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. Takes precedence over `root_dirs`. |
| `changed_from` | `str \| None` | `None` | समीक्षा को बदले गए सोर्स फ़ाइलों तक सीमित करने के लिए उपयोग किया गया Git ref। |
| `readme_only` | `bool` | `False` | प्रत्येक स्रोत रूट के अंतर्गत केवल `README.md` की समीक्षा करें। एक लापता स्रोत README `ValueError` उठाता है। |
| `output_format` | `str` | `"text"` | समीक्षा आउटपुट फॉर्मैट। समर्थित मान `"text"` और `"github"` हैं। |
| `fail_on_warnings` | `bool` | `False` | चेतावनियों को त्रुटियों के साथ-साथ विफलताओं के रूप में मानें। |
| `debug` | `bool` | `False` | डेबग लॉगिंग सक्षम करें। |
| `save_logs` | `bool` | `False` | रूट `logs/` निर्देशिका के अंतर्गत DEBUG-लेवल लॉग फ़ाइलें सहेजें। |

यदि `markdown`, `notebook`, या `images` में से कोई भी सेट नहीं है, तो API जहाँ लागू हो Markdown, नोटबुक, और इमेज लिंक संदर्भों की समीक्षा करता है। समीक्षा किसी LLM प्रदाता को कॉल नहीं करती और API कुंजियाँ आवश्यक नहीं हैं।

## कॉन्फ़िगरेशन आवश्यकताएँ

प्रदाता-समर्थित अनुवाद API अनुवाद से पहले प्रदाता कॉन्फ़िगरेशन की आवश्यकता होती है:

- Markdown और नोटबुक अनुवाद के लिए एक LLM प्रदाता आवश्यक है। Azure OpenAI, OpenAI, या Anthropic को कॉन्फ़िगर करें।
- इमेज अनुवाद के लिए LLM प्रदाता के अलावा Azure AI Vision की आवश्यकता होती है।
- `run_translation` प्रोजेक्ट अनुवाद शुरू होने से पहले हल्के कनेक्टिविटी जाँच चलाता है।
- एजेंट-सहायता प्राप्त `start_*_agent_translation` और `finish_*_agent_translation` APIs Co-op Translator LLM प्रदाताओं को कॉल नहीं करते। होस्ट एप्लिकेशन या MCP एजेंट तैयार किए गए हिस्सों का अनुवाद करता है।
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, और `run_review` निर्धारित हैं और इन्हें प्रदाता क्रेडेंशियल्स की आवश्यकता नहीं होती।

आवश्यक Azure OpenAI वेरिएबल्स:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

आवश्यक OpenAI वेरिएबल्स:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

आवश्यक Anthropic वेरिएबल्स:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` and `ANTHROPIC_MAX_TOKENS` वैकल्पिक हैं। Co-op Translator 0.22.0 से शुरू करते हुए Microsoft Agent Framework सभी प्रदाताओं के लिए डिफ़ॉल्ट मॉडल क्लाइंट है। Semantic Kernel को अस्थायी रूप से `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` के साथ चुना जा सकता है, लेकिन ऐसा करने पर एक डिप्रिकेशन चेतावनी जारी होती है; चरणबद्ध हटाने की योजना के लिए [कॉन्फ़िगरेशन](configuration.md#model-client-backend) देखें।

इमेज अनुवाद के लिए आवश्यक Azure AI Vision वेरिएबल्स:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` निश्चित है और इसे LLM या Azure AI Vision कॉन्फ़िगरेशन की आवश्यकता नहीं है।

## व्यवहार नोट्स

- सामग्री अनुवाद API अनुवाद को प्रोजेक्ट पाथ रीराइटिंग से अलग रखता है। जब अनुवादित सामग्री के लिए प्रोजेक्ट-सापेक्ष लिंक को लक्षित स्थान के लिए समायोजित करने की आवश्यकता हो तो स्पष्ट रूप से `rewrite_markdown_paths` या `rewrite_notebook_paths` कॉल करें।
- प्रोजेक्ट ऑर्केस्ट्रेशन API सामग्री अनुवाद के चारों ओर प्रोजेक्ट व्यवहार जोड़ते हैं, जिनमें फ़ाइल खोज, लेखन, पाथ रीराइटिंग, मेटाडेटा, क्लीनअप, और वैकल्पिक अस्वीकरण शामिल हैं।
- `run_translation` CLI द्वारा उपयोग किए गए उसी Rich-समर्थित रिपोर्टर के माध्यम से प्रगति और अनुमान सारांश प्रिंट करता है। नॉन-इंटरैक्टिव आउटपुट साधारण टेक्स्ट पर वापस आ जाता है।
- `dry_run=True` आभासी README अपडेट्स का उपयोग करके अनुमान गणना करता है, लेकिन README या अनुवाद फ़ाइलें नहीं लिखता।
- `groups` क्रमिक रूप से संसाधित किए जाते हैं। कार्य शुरू होने से पहले एक समेकित अनुमान मुद्रित किया जाता है।
- जब इमेज अनुवाद चुना जाता है, तो Vision विन्यास का अभाव अनुवाद शुरू होने से पहले एक त्रुटि उठाता है।
- मौजूदा उपनाम-आधारित भाषा फ़ोल्डरों का पता लगाया जाता है और रन के हिस्से के रूप में उन्हें प्रामाणिक भाषा फ़ोल्डर नामों में माइग्रेट किया जा सकता है।
- `run_review` गायब अनुवादित फ़ाइलों, गायब या पुरानी अनुवाद मेटाडेटा, खराब रूप से निर्मित Markdown फ्रंटमैटर/कोड फ़ेन्स, और अमान्य अनुवादित नोटबुक JSON पर विफल होता है।
- `run_review` डिफ़ॉल्ट रूप से स्थानीय Markdown और इमेज लिंक लक्ष्यों के लापता होने को चेतावनी के रूप में रिपोर्ट करता है।

## आंतरिक कॉल पथ

API CLI द्वारा उपयोग की जाने वाली उसी कोर इम्प्लीमेंटेशन को सौंपता है:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, या `translate_image_content` इन-मेमोरी अनुवाद के लिए।
2. `co_op_translator.api.translation.rewrite_markdown_paths` या `rewrite_notebook_paths` स्पष्ट पाथ पोस्ट-प्रोसेसिंग के लिए।
3. `co_op_translator.api.translation.run_translation` पूर्ण प्रोजेक्ट ऑर्केस्ट्रेशन के लिए।
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, नोटबुक, और इमेज के लिए केंद्रित प्रोजेक्ट अनुवाद मिक्सिन।
8. `co_op_translator.core` के अंतर्गत Markdown, नोटबुक, टेक्स्ट, और इमेज ट्रांसलेटर्स।

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` के तहत निर्धार्य जाँचें

निम्नलिखित क्लास मेंटेनर्स के लिए उपयोगी हैं, लेकिन पैकेज-स्तरीय स्थिर API के रूप में एक्सपोर्ट नहीं किए जाते।

| क्लास | मॉड्यूल | जिम्मेदारी |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | प्रोजेक्ट-स्तरीय अनुवाद, निर्देशिका प्रबंधन, प्रति-भाषा मेटाडेटा सामान्यीकरण, और Markdown, नोटबुक, तथा इमेज ट्रांसलेटर्स को सौंपता है। |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, नोटबुक, इमेज, स्टेल डिटेक्शन, और अनुवाद मेटाडेटा अपडेट्स के लिए असिंक्रोनस फ़ाइल प्रोसेसिंग कार्य करता है। |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown फ़ाइल पढ़ना, सामग्री अनुवाद, पाथ रीराइटिंग, मेटाडेटा, अस्वीकरण, और लेखन का समन्वय करता है। |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | नोटबुक फ़ाइल पढ़ना, Markdown-सेल अनुवाद, पाथ रीराइटिंग, मेटाडेटा, अस्वीकरण, और लेखन का समन्वय करता है। |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | स्रोत इमेज खोज, इमेज अनुवाद, आउटपुट पथ, मेटाडेटा, और लेखन का समन्वय करता है। |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | अनुवादित Markdown जोड़े खोजता है, अनुवाद गुणवत्ता का मूल्यांकन करता है, और कम-विश्वास मरम्मत वर्कफ़्लो के लिए विश्वास मेटाडेटा पढ़ता है। |
| `ReviewRunner` | `co_op_translator.review.runner` | स्रोत फ़ाइलों, लक्ष्य भाषाओं, और कॉन्फ़िगर किए गए अनुवाद रूट्स के बीच निर्धार्य समीक्षा जाँचों का समन्वय करता है। |
| `ReviewTarget` | `co_op_translator.review.targets` | किसी स्रोत रूट और उस रूट के लिए समीक्षा किए गए अनुवाद आउटपुट निर्देशिका का वर्णन करता है। |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | लेगसी उपनाम भाषा फ़ोल्डर्स का पता लगाता है और कैननिकल BCP 47 फ़ोल्डर माइग्रेशन योजनाएँ तैयार करता है। |
| `Config` | `co_op_translator.config.base_config` | `.env` फ़ाइलें लोड करता है और जाँचता है कि आवश्यक LLM और वैकल्पिक Vision प्रदाता कॉन्फ़िगर हैं या नहीं। |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI, या Anthropic का ऑटो-डिटेक्ट करता है, आवश्यक पर्यावरण वेरिएबल्स को मान्य करता है, और प्रदाता कनेक्टिविटी चेक चलाता है। |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision कॉन्फ़िगरेशन का पता लगाता है और इमेज अनुवाद के लिए कनेक्टिविटी चेक चलाता है। |