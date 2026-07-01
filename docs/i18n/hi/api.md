# Python API

स्थिर सार्वजनिक Python API `co_op_translator.api` से निर्यात की गई है। अधिकांश एकीकरण इन कार्यप्रवाहों में से एक का उपयोग करते हैं:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | आपका एप्लिकेशन स्रोत सामग्री पढ़ता है, अनुवाद के लिए Co-op Translator को कॉल करता है, और परिणाम कहाँ सहेजा जाएगा यह तय करता है। | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | आपका MCP होस्ट या एप्लिकेशन मॉडल चंक्स का अनुवाद करेगा, जबकि Co-op Translator चंकिंग और पुनर्निर्माण संभालता है। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | आप चाहते हैं कि Python API CLI की तरह व्यवहार करे और डिस्कवरी, आउटपुट पाथ, मेटाडेटा, क्लीनअप, और लिखने का प्रबंधन करे। | `run_translation` |

इन API एंट्री पोइंट्स द्वारा उपयोग किए जाने वाले `core`, `config`, `review`, और `utils` के अंतर्गत अधिकांश निचले-स्तर मॉड्यूल लागूकरण विवरण हैं।

MCP क्लाइंट उसी सार्वजनिक API का उपयोग [MCP Server](mcp.md) के माध्यम से करते हैं। सीधे Python से कॉल करते समय इस पृष्ठ का उपयोग करें, और Co-op Translator को किसी एजेंट या संपादक के लिए एक्सपोज़ करते समय MCP गाइड का उपयोग करें। यदि आप CLI, Python API, और MCP के बीच निर्णय ले रहे हैं, तो [Choose Your Workflow](workflows.md) से शुरू करें।

## First-Time API Flow

यदि आप Python कोड से Co-op Translator को कॉल कर रहे हैं तो यहाँ से शुरू करें:

1. [Configuration](configuration.md) में बताई गई तरह एक LLM प्रदाता कॉन्फ़िगर करें, जब तक कि आप केवल Markdown या नोटबुक चंक्स को होस्ट-एजेंट अनुवाद के लिए तैयार नहीं कर रहे हों।
2. तय करें कि आपकी एप्लिकेशन फाइल I/O की जिम्मेदारी संभालेगी या नहीं।
3. जब आपकी एप्लिकेशन व्यक्तिगत फ़ाइलें पढ़ती और लिखती है तो content APIs का उपयोग करें।
4. जब आप चाहते हैं कि Co-op Translator CLI की तरह किसी रिपोज़िटरी को प्रोसेस करे तो `run_translation` का उपयोग करें।
5. यदि आपको ऑटोमेशन में निश्चित जाँच की आवश्यकता है तो अनुवाद के बाद `run_review` का उपयोग करें।

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

इस वर्कफ़्लो का उपयोग तब करें जब आपके पास पहले से ही कोई फ़ाइल, एडिटर बफ़र, नोटबुक पेलोड, MCP रिक्वेस्ट, या कस्टम पाइपलाइन इनपुट हो। आपकी कोड फाइल I/O की जिम्मेदारी संभालेगी:

1. स्रोत सामग्री पढ़ें।
2. किसी content translation API को कॉल करें।
3. यदि अनुवादित सामग्री किसी प्रोजेक्ट ट्रांसलेशन फ़ोल्डर में लिखी जाएगी तो वैकल्पिक रूप से path rewriting API को कॉल करें।
4. परिणाम को अपनी एप्लिकेशन में सहेजें या वापस करें।

content translation APIs परियोजना डिस्कवरी नहीं चलाते, मेटाडेटा नहीं लिखते, डिसक्लेमर जोड़ते नहीं हैं, और लिंक स्वतः री-राइट नहीं करते।

### Markdown File

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

### Notebook File

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

`translate_notebook_content` Markdown सेल्स का अनुवाद करता है और non-Markdown सेल्स को संरक्षित रखता है। पाथ री-राइटिंग केवल Markdown सेल्स पर लागू होती है।

### Image File

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

`translate_image_content` स्रोत छवि पढ़ता है और एक रेंडर किया हुआ `PIL.Image.Image` लौटाता है। यह अनुवादित इमेज मेटाडेटा नहीं लिखता।

## Scenario 2: Translate an Entire Repository

इस वर्कफ़्लो का उपयोग तब करें जब आप चाहते हैं कि Python API `translate` CLI की तरह व्यवहार करे। `run_translation` समर्थित फ़ाइलों का पता लगाता है, चयनित सामग्री प्रकारों का अनुवाद करता है, पाथ री-राइट करता है, आउटपुट फ़ाइलें लिखता है, मेटाडेटा अपडेट करता है, और क्लीनअप जैसे अनुवाद रखरखाव कार्य करता है।

`run_translation` पसंदीदा प्रोजेक्ट ऑर्केस्ट्रेशन एंट्री पॉइंट है। `translate_project` समान व्यवहार के साथ एक कंपैटिबिलिटी उपनाम के रूप में एक्सपोर्ट किया गया है।

Markdown फ़ाइलों को वर्तमान रिपॉज़िटरी में Korean और Japanese में अनुवाद करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

एक विशिष्ट प्रोजेक्ट रूट से केवल नोटबुक्स का अनुवाद करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

फ़ाइल लिखे बिना अनुवाद मात्रा का पूर्वावलोकन करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

एक ही कॉल में कई कंटेंट रूट्स का अनुवाद करें:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

ट्रांसलेशन्स को स्पष्ट आउटपुट समूहों में लिखें:

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

जब हर भाषा में एक नेस्टेड सबडायरेक्टरी होनी चाहिए तो प्रति-भाषा प्लेसहोल्डर का उपयोग करें:

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

यदि `markdown`, `notebook`, या `images` में से कोई भी सेट नहीं है, तो API सभी समर्थित प्रकारों का अनुवाद करता है: Markdown, नोटबुक, और इमेजेज़।

## Review Translated Output

`run_review` LLM या Vision क्रेडेंशियल्स के बिना निर्धारित अनुवाद जाँचें चलाता है।

!!! note "Beta"
    `run_review` एक बीटा निर्धारित समीक्षा API है। यह मॉडल प्रदाताओं को कॉल नहीं करता और फ़ाइलें नहीं लिखता, लेकिन चेक और इशू स्कीमा विकसित हो सकते हैं।

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

केवल एक बेस रेफ के खिलाफ बदली गई फ़ाइलों की समीक्षा करें और GitHub-फ़्लेवर्ड आउटपुट प्रिंट करें:

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

## Copy-Paste API Examples

Markdown सामग्री का अनुवाद करें बिना फाइल लिखे:

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

Markdown लिंक का अनुवाद और री-राइट करें:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

एकाधिक रूट्स का अनुवाद करें:

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

ग्लोसरी शब्दों को संरक्षित रखें:

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

## Public Entry Points

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Content Translation APIs

Content translation APIs उन इंटीग्रेशन के लिए अभिप्रेत हैं जिनके पास पहले से ही मेमोरी में सामग्री होती है, जैसे कि एक एडिटर एक्सटेंशन, MCP टूल, नोटबुक प्रोसेसर, या कस्टम पाइपलाइन।

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. केवल Markdown सामग्री का अनुवाद करता है। यह लिंक री-राइट नहीं करता, मेटाडेटा नहीं लिखता, और डिसक्लेमर नहीं जोड़ता। |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown सेल्स का अनुवाद करता है और non-Markdown सेल्स को संरक्षित रखता है। यह लिंक री-राइट नहीं करता, मेटाडेटा नहीं लिखता, और डिसक्लेमर नहीं जोड़ता। |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. इमेज टेक्स्ट निकालता और अनुवाद करता है, फिर एक रेंडर की हुई इमेज लौटाता है। यह अनुवादित इमेज मेटाडेटा सहेजता नहीं है। |

`translate_markdown_content` और `translate_notebook_content` उनके विकल्पों के माध्यम से एक वैकल्पिक `source_path` स्वीकार करते हैं। पाथ अनुवादक को संदर्भ के रूप में पास किया जाता है; कॉलर अनुवाद के बाद किसी भी प्रोजेक्ट-विशिष्ट पाथ री-राइटिंग के लिए जिम्मेदार रहते हैं।

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

उसी विकल्पों को शब्दकोशों के रूप में भी पास किया जा सकता है:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted APIs Co-op Translator से Azure OpenAI या OpenAI को कॉल नहीं करते। वे होस्ट-एजेंट द्वारा अनुवाद के लिए Markdown या नोटबुक चंक्स तैयार करते हैं, फिर अनुवादित चंक्स से अंतिम सामग्री का पुनर्निर्माण करते हैं।

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | चंक्स, प्रॉम्प्ट्स, और पुनर्निर्माण स्थिति के साथ एक self-contained Markdown जॉब लौटाएं। |
| `finish_markdown_agent_translation` | एक जॉब और होस्ट-एजेंट द्वारा अनुवादित चंक्स से Markdown पुनर्निर्माण करें। |
| `start_notebook_agent_translation` | होस्ट-एजेंट अनुवाद के लिए Markdown-सेल चंक्स के साथ एक नोटबुक जॉब लौटाएं। |
| `finish_notebook_agent_translation` | कोड सेल्स, आउटपुट, और मेटाडेटा को संरक्षित रखते हुए नोटबुक JSON पुनर्निर्माण करें। |

यह वर्कफ़्लो मुख्य रूप से MCP होस्ट्स के लिए अभिप्रेत है। यदि आपको Co-op Translator द्वारा प्रदाता कॉल्स का प्रबंधन करने वाले प्रोडक्शन रिपोज़िटरी अनुवाद की आवश्यकता है, तो `translate_markdown_content`, `translate_notebook_content`, या `run_translation` का उपयोग करें।

## Path Rewriting APIs

Path rewriting APIs कोई अनुवाद नहीं करते। वे स्रोत पाथ, अनुवादित लक्ष्य पाथ, और प्रोजेक्ट लेआउट ज्ञात होने के बाद लिंक और frontmatter पाथ्स को अपडेट करते हैं।

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | अनुवादित लक्ष्य के लिए Markdown लिंक और समर्थित frontmatter पाथ फ़ील्ड्स को री-राइट करता है। |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | प्रत्येक Markdown सेल पर Markdown पाथ री-राइटिंग लागू करता है और non-Markdown सेल्स को अपरिवर्तित छोड़ता है। |

`policy` आर्गुमेंट एक शब्दकोश हो सकता है जिसमें ये फील्ड्स हों:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | लक्ष्य भाषा कोड, जैसे `"ko"` या `"pt-BR"`। |
| `root_dir` | No | स्रोत प्रोजेक्ट रूट। डिफ़ॉल्ट `"."` है। |
| `translations_dir` | No | टेक्स्ट अनुवाद आउटपुट डायरेक्टरी। डिफ़ॉल्ट `root_dir` के अंतर्गत `translations` है। |
| `translated_images_dir` | No | अनुवादित इमेज आउटपुट डायरेक्टरी। डिफ़ॉल्ट `root_dir` के अंतर्गत `translated_images` है। |
| `translation_types` | No | सक्षम अनुवाद प्रकार। डिफ़ॉल्ट Markdown, नोटबुक, और इमेजेज़ हैं। |
| `lang_subdir` | No | प्रत्येक भाषा फ़ोल्डर के अंतर्गत वैकल्पिक सबडायरेक्टरी। |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | स्पेस से पृथक लक्ष्य भाषा कोड, जैसे `"ko ja fr"`, या `"all"`। उपनाम कोड्स canonical BCP 47 मानों में सामान्यीकृत होते हैं। |
| `root_dir` | `str` | `"."` | एकल अनुवाद लक्ष्य के लिए प्रोजेक्ट रूट। जब `root_dirs` या `groups` सप्लाई किए जाते हैं तब अनदेखा किया जाता है। |
| `update` | `bool` | `False` | चयनित भाषाओं के लिए मौजूदा ट्रांसलेशन्स को हटा कर पुन: बनाएं। |
| `images` | `bool` | `False` | इमेज अनुवाद शामिल करें। इसके लिए Azure AI Vision कॉन्फ़िगरेशन की आवश्यकता है। |
| `markdown` | `bool` | `False` | Markdown अनुवाद शामिल करें। |
| `notebook` | `bool` | `False` | Jupyter नोटबुक अनुवाद शामिल करें। |
| `debug` | `bool` | `False` | डिबग लॉगिंग सक्रिय करें। |
| `save_logs` | `bool` | `False` | रूट `logs/` डायरेक्टरी के अंतर्गत DEBUG-स्तर लॉग फ़ाइलें सहेजें। |
| `yes` | `bool` | `True` | प्रोग्रामेटिक और CI उपयोग के लिए प्रॉम्प्ट्स को स्वचालित रूप से कन्फर्म करें। |
| `add_disclaimer` | `bool` | `False` | अनुवादित Markdown और नोटबुक में मशीन अनुवाद डिसक्लेमर जोड़ें। |
| `translations_dir` | `str \| None` | `None` | कस्टम टेक्स्ट अनुवाद आउटपुट डायरेक्टरी। सापेक्ष पाथ्स प्रत्येक रूट के खिलाफ हल होते हैं। |
| `image_dir` | `str \| None` | `None` | कस्टम अनुवादित इमेज आउटपुट डायरेक्टरी। सापेक्ष पाथ्स प्रत्येक रूट के खिलाफ हल होते हैं। |
| `root_dirs` | `Iterable[str] \| None` | `None` | कई रूट्स जो समान आउटपुट सेटिंग्स साझा करते हैं। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | स्पष्ट `(root_dir, translations_dir)` जोड़े। यह `root_dirs` पर प्राथमिकता लेता है। |
| `repo_url` | `str \| None` | `None` | README भाषा तालिका गाइडेंस रेंडर करने के समय प्रयुक्त रिपॉज़िटरी URL। |
| `glossaries` | `Iterable[str] \| None` | `None` | अनुवाद के दौरान संरक्षित किए जाने वाले ग्लोसरी शब्द। डुप्लिकेट और खाली शब्द सामान्यीकृत होते हैं। |
| `dry_run` | `bool` | `False` | फ़ाइल लिखे बिना अनुवाद मात्रा का अनुमान और माइग्रेशन व्यवहार का पूर्वावलोकन। |

## Review Parameters

`run_review` जानबूझकर जहाँ संभव हो `run_translation` सिग्नेचर को मिरर करता है ताकि ऑटोमेशन न्यूनतम ब्रांचिंग के साथ अनुवाद और समीक्षा वर्कफ़्लो के बीच स्विच कर सके।

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | समीक्षा के लिए लक्ष्य भाषा फ़ोल्डर्स। स्पेस से पृथक स्ट्रिंग्स और इटरेबल स्वीकार किए जाते हैं। `"all"` हर खोजी गई अनुवाद भाषा की समीक्षा करता है। |
| `root_dir` | `str` | `"."` | एकल समीक्षा लक्ष्य के लिए प्रोजेक्ट रूट। जब `root_dirs` या `groups` सप्लाई किए जाते हैं तब अनदेखा किया जाता है। |
| `markdown` | `bool` | `False` | Markdown और MDX स्रोत फ़ाइलें शामिल करें। |
| `notebook` | `bool` | `False` | Jupyter नोटबुक स्रोत फ़ाइलें शामिल करें। |
| `images` | `bool` | `False` | अनुवाद विकल्पों के साथ समरूपता के लिए आरक्षित। Markdown से इमेज के लिंक रेफरेंसेज़ की जाँच की जाती है। |
| `translations_dir` | `str \| None` | `None` | कस्टम टेक्स्ट अनुवाद आउटपुट निर्देशिका। सापेक्ष पथ प्रत्येक मूल निर्देशिका के अनुरूप सुलझाए जाते हैं। |
| `root_dirs` | `Iterable[str] \| None` | `None` | एक ही आउटपुट सेटिंग्स साझा करने वाले कई रूट। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | स्पष्ट `(root_dir, translations_dir)` युग्म। यह `root_dirs` पर प्राथमिकता देता है। |
| `changed_from` | `str \| None` | `None` | Git ref जिसका उपयोग केवल बदले हुए स्रोत फ़ाइलों के रिव्यू को सीमित करने के लिए किया जाता है। |
| `output_format` | `str` | `"text"` | रिव्यू आउटपुट फॉर्मैट। समर्थित मान `"text"` और `"github"` हैं। |
| `fail_on_warnings` | `bool` | `False` | चेतावनियों को त्रुटियों के साथ-साथ विफलताओं के रूप में माना जाए। |
| `debug` | `bool` | `False` | डिबग लॉगिंग सक्षम करें। |
| `save_logs` | `bool` | `False` | मूल `logs/` निर्देशिका के अंतर्गत DEBUG-स्तर की लॉग फ़ाइलें सहेजें। |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## कॉन्फ़िगरेशन आवश्यकताएँ

प्रदाता-समर्थित अनुवाद API को अनुवाद करने से पहले प्रदाता कॉन्फ़िगरेशन की आवश्यकता होती है:

- Markdown और notebook अनुवाद के लिए एक LLM प्रदाता आवश्यक है। Azure OpenAI या OpenAI में से किसी एक को कॉन्फ़िगर करें।
- Image अनुवाद के लिए LLM प्रदाता के अलावा Azure AI Vision भी आवश्यक है।
- `run_translation` प्रोजेक्ट अनुवाद शुरू होने से पहले हल्की कनेक्टिविटी जांचें चलाता है।
- Agent-सहायता प्राप्त `start_*_agent_translation` और `finish_*_agent_translation` APIs Co-op Translator LLM प्रदाताओं को कॉल नहीं करते। होस्ट एप्लिकेशन या MCP एजेंट तैयार किए गए चंक्स का अनुवाद करता है।
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, और `run_review` निश्चित हैं और इन्हें प्रदाता क्रेडेंशियल्स की आवश्यकता नहीं होती।

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` निर्धारित है और इसे Azure OpenAI, OpenAI, या Azure AI Vision कॉन्फ़िगरेशन की आवश्यकता नहीं है।

## व्यवहार नोट्स

- कंटेंट अनुवाद APIs अनुवाद को प्रोजेक्ट पथ पुनर्लेखन से अलग रखते हैं। जब अनूदित सामग्री के प्रोजेक्ट-सापेक्ष लिंक को लक्ष्य स्थान के लिए समायोजित करने की आवश्यकता हो, तब स्पष्ट रूप से `rewrite_markdown_paths` या `rewrite_notebook_paths` को कॉल करें।
- प्रोजेक्ट ऑर्केस्ट्रेशन APIs कंटेंट अनुवाद के इर्द-गिर्द प्रोजेक्ट व्यवहार जोड़ते हैं, जिनमें फ़ाइल खोज, लेखन, पथ पुनर्लेखन, मेटाडेटा, क्लीनअप, और वैकल्पिक अस्वीकरण शामिल हैं।
- `run_translation` Click के माध्यम से प्रगति और अनुमान सारांश प्रिंट करता है, जो CLI उपयोगकर्ता अनुभव से मेल खाता है।
- `dry_run=True` वर्चुअल README अपडेट्स का उपयोग करके अनुमान निकालता है, पर README या अनुवाद फ़ाइलें नहीं लिखता।
- `groups` को क्रमवार संसाधित किया जाता है। कार्य शुरू होने से पहले एक एकल समग्र अनुमान प्रिंट होता है।
- जब image अनुवाद चुना जाता है, तो Vision कॉन्फ़िगरेशन की कमी अनुवाद शुरू होने से पहले त्रुटि उठाती है।
- मौजूदा alias-आधारित भाषा फ़ोल्डरों का पता लगाया जाता है और इन्हें मानक BCP 47 फ़ोल्डर नामों में माइग्रेट किया जा सकता है।
- `run_review` अनुपस्थित अनूदित फ़ाइलों, अनुपस्थित या स्टेल अनुवाद मेटाडेटा, बिगड़ा हुआ Markdown frontmatter/code फेन्स, और अवैध अनूदित notebook JSON पर फेल होता है।
- `run_review` डिफ़ॉल्ट रूप से स्थानीय Markdown और image लिंक लक्ष्यों के लापता होने को चेतावनियों के रूप में रिपोर्ट करता है।

## आंतरिक कॉल पथ

API उसी कोर इम्प्लीमेंटेशन को डेलीगेट करती है जिसे CLI उपयोग करता है:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` इन-मेमोरी अनुवाद के लिए।  
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` स्पष्ट पथ पोस्ट-प्रोसेसिंग के लिए।  
3. `co_op_translator.api.translation.run_translation` पूर्ण प्रोजेक्ट ऑर्केस्ट्रेशन के लिए।  
4. `co_op_translator.config.Config`, `LLMConfig`, और `VisionConfig`.  
5. `co_op_translator.core.project.ProjectTranslator`.  
6. `co_op_translator.core.project.TranslationManager`.  
7. फोकस्ड प्रोजेक्ट अनुवाद मिक्सिन्स Markdown, notebooks, और images के लिए।  
8. `co_op_translator.core` के अंतर्गत Markdown, notebook, text, और image अनुवादक।  

Review:

1. `co_op_translator.api.review.run_review`  
2. `co_op_translator.review.targets.build_review_targets`  
3. `co_op_translator.review.runner.ReviewRunner`  
4. निर्धारक जांचें `co_op_translator.review.checks` के तहत

निम्नलिखित क्लासें रखरखावकर्ताओं के लिए उपयोगी हैं, लेकिन पैकेज-लेवल स्थिर API के रूप में एक्सपोर्ट नहीं की जातीं।

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | प्रोजेक्ट-स्तर के अनुवाद, निर्देशिका प्रबंधन, प्रति-भाषा मेटाडेटा सामान्यीकरण, और Markdown, notebook, और image अनुवादकों को सौंपने का समन्वय करता है। |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, notebooks, images, stale detection, और translation मेटाडेटा अपडेट्स के लिए async फ़ाइल प्रोसेसिंग कार्य करता है। |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown फ़ाइल पढ़ने, सामग्री अनुवाद, पथ पुनर्लेखन, मेटाडेटा, अस्वीकरण, और लेखन का समन्वय करता है। |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | notebook फ़ाइल पढ़ने, Markdown-सेल अनुवाद, पथ पुनर्लेखन, मेटाडेटा, अस्वीकरण, और लेखन का समन्वय करता है। |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | स्रोत इमेज की खोज, इमेज अनुवाद, आउटपुट पथ, मेटाडेटा, और लेखन का समन्वय करता है। |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | अनूदित Markdown जोड़े खोजता है, अनुवाद गुणवत्ता का मूल्यांकन करता है, और कम-विश्वास मरम्मत वर्कफ़्लोज़ के लिए भरोसा मेटाडेटा पढ़ता है। |
| `ReviewRunner` | `co_op_translator.review.runner` | स्रोत फ़ाइलों, लक्षित भाषाओं, और कॉन्फ़िगर किए गए अनुवाद रूट्स में निर्धारक रिव्यू जांचों का समन्वय करता है। |
| `ReviewTarget` | `co_op_translator.review.targets` | किसी स्रोत रूट और उस रूट के लिए समीक्षा किए जाने वाले अनुवाद आउटपुट निर्देशिका का वर्णन करता है। |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | पुरानी alias भाषा फ़ोल्डरों का पता लगाता है और मानक BCP 47 फ़ोल्डर माइग्रेशन योजनाएँ तैयार करता है। |
| `Config` | `co_op_translator.config.base_config` | `.env` फ़ाइलें लोड करता है और जाँचता है कि आवश्यक LLM और वैकल्पिक Vision प्रदाता कॉन्फ़िगर हैं या नहीं। |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | स्वचालित रूप से Azure OpenAI या OpenAI का पता लगाता है, आवश्यक एनवायरनमेंट वेरिएबल्स को सत्यापित करता है, और प्रदाता कनेक्टिविटी जांच चलाता है। |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision कॉन्फ़िगरेशन का पता लगाता है और इमेज अनुवाद के लिए कनेक्टिविटी जांच चलाता है। |