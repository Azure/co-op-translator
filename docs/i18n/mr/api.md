# Python API

स्थिर सार्वजनिक Python API `co_op_translator.api` मध्ये निर्यात केले जाते. बहुतेक समाकलन हे खालील कार्यप्रवाहांपैकी एक वापरतात:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | आपल्या अनुप्रयोगाने स्त्रोत सामग्री वाचली आहे, Co-op Translator ला अनुवादासाठी कॉल करतो, आणि निकाल कुठे जतन करायचा हे ठरवते. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | आपला MCP होस्ट किंवा अनुप्रयोग मॉडेल चंक अनुवादेल, तर Co-op Translator चंकिंग आणि पुन्हा संकलन हाताळेल. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | आपण Python API ला CLI सारखे वागवू इच्छिता आणि शोध, आउटपुट पाथ, मेटाडेटा, क्लीनअप आणि लेखन हाताळू इच्छिता. | `run_translation` |

`core`, `config`, `review`, आणि `utils` अंतर्गत बहुतेक लोअर-लेव्हल मॉड्युल हे अंमलबजावणी तपशील आहेत जे या API एन्ट्री पॉइंट्सद्वारे वापरले जातात.

MCP क्लायंटसाठी सार्वजनिक API [MCP Server](mcp.md) द्वारे उपलब्ध आहे. Python थेट कॉल करताना हा पृष्ठ वापरा, आणि Co-op Translator एका एजंट किंवा संपादकाला उघडताना MCP मार्गदर्शक वापरा. CLI, Python API, आणि MCP यांच्यात निर्णय घेत असाल तर [Choose Your Workflow](workflows.md) पासून प्रारंभ करा.

## First-Time API Flow

आपण Python कोडवरून Co-op Translator कॉल करत असाल तर येथे प्रारंभ करा:

1. [Configuration](configuration.md) मध्ये वर्णन केल्याप्रमाणे LLM प्रदायक कॉन्फिगर करा, जोपर्यंत आपण फक्त Markdown किंवा नोटबुक चंक्स होस्ट-एजंट ट्रान्सलेशनसाठी तयार करत नाही तोपर्यंत.
2. ठरवा की आपल्या अनुप्रयोगाकडे फाइल I/O आहे की नाही.
3. जेव्हा आपल्या अनुप्रयोगाने स्वतंत्र फाइल्स वाचल्या किंवा लिहिल्या तर कंटेंट API वापरा.
4. जेव्हा Co-op Translator ला CLI प्रमाणे रिपॉझिटरी प्रोसेस करायची असेल तेव्हा `run_translation` वापरा.
5. जर आपल्याला ऑटोमेशनमध्ये निर्दिष्ट तपासणी आवश्यक असेल तर अनुवादानंतर `run_review` वापरा.

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

हा कार्यप्रवाह वापरा जेव्हा आपल्याकडे आधीच फाइल, संपादक बफर, नोटबुक पेलोड, MCP रिक्वेस्ट, किंवा कस्टम पाइपलाइन इनपुट असेल. आपला कोड फाइल I/O ची मालकी घेतो:

1. स्त्रोत सामग्री वाचा.
2. कंटेंट ट्रान्सलेशन API कॉल करा.
3. जर अनुवादित सामग्री प्रोजेक्ट ट्रान्सलेशनल फोल्डरमध्ये लिहिली जाणार असेल तर वैकल्पिकपणे पाथ रीराइटिंग API कॉल करा.
4. आपल्या अनुप्रयोगातून निकाल जतन करा किंवा परत करा.

कंटेंट ट्रान्सलेशन API प्रोजेक्ट डिस्कवरी चालवत नाहीत, मेटाडेटा लिहीत नाहीत, डिस्क्लेमर जोडत नाहीत, आणि लिंक स्वयंचलितपणे रिराइट करत नाहीत.

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

जर अनुवादित Markdown Co-op Translator प्रोजेक्ट लेआउटमध्ये नसेल तर `rewrite_markdown_paths` वगळा आणि अनुवादित स्ट्रिंग थेट जतन करा.

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

`translate_notebook_content` Markdown सेल अनुवाद करते आणि नॉन-Markdown सेल जतन करते. पाथ रीराइटिंग फक्त Markdown सेलवर लागू होते.

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

`translate_image_content` स्त्रोत प्रतिमा वाचते आणि रेंडर केलेली `PIL.Image.Image` परत करते. ते अनुवादित प्रतिमा मेटाडेटा लिहीत नाही.

## Scenario 2: Translate an Entire Repository

हा कार्यप्रवाह वापरा जेव्हा आपण Python API ला `translate` CLI प्रमाणे चालवू इच्छिता. `run_translation` समर्थित फाइल्स शोधते, निवडलेल्या सामग्री प्रकारांचे अनुवाद करते, पाथ रीराइट करते, आउटपुट फाइल्स लिहिते, मेटाडेटा अपडेट करते, आणि क्लीनअप सारखी ट्रान्सलेशन देखभाल कामे करते.

`run_translation` हा प्रोजेक्ट ऑर्केस्ट्रेशनसाठी पसंत केलेला एन्ट्री पॉइंट आहे. `translate_project` हे त्याच वर्तनासह सुसंगततेचा उपनाम म्हणून निर्यात केले जाते.

सध्याच्या रिपॉझिटरीतील Markdown फाइल्स कोरियन आणि जपानीमध्ये अनुवादित करा:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

विशिष्ट प्रोजेक्ट रूटमधून केवळ नोटबुक्स अनुवादित करा:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

फाइल्स लिहिल्याशिवाय अनुवादाचा अंदाज पहा:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

एकाच कॉलमध्ये एकाधिक कंटेंट रूट अनुवादित करा:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

अनुवाद निर्दिष्ट आउटपुट ग्रुपमध्ये लिहा:

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

प्रत्येक भाषेसाठी नेस्ट केलेली सबडायरेक्टरी असावी तेव्हा प्रति-भाषा प्लेसहोल्डर वापरा:

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

जर `markdown`, `notebook`, किंवा `images` पैकी कोणतेही सेट केलेले नसेल तर API सर्व समर्थन केलेले प्रकार अनुवादित करते: Markdown, नोटबुक, आणि प्रतिमा.

## Review Translated Output

`run_review` LLM किंवा Vision क्रेडेन्शियल्सशिवाय निश्चितनिष्ठ अनुवाद तपासणी चालवते.

!!! note "बीटा"
    `run_review` हा एक बीटा निश्चितनिष्ठ रिव्ह्यू API आहे. हे मॉडेल प्रदात्यांना कॉल करत नाही किंवा फाइल्स लिहीत नाही, परंतु तपासण्या आणि इश्यू स्कीमा विकसित होऊ शकतात.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

फक्त बेस रेफच्या विरुद्ध बदललेली फाइल्स रिव्ह्यू करा आणि GitHub-फ्लेवर्ड आउटपुट छापा:

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

फाइल लेखनांशिवाय Markdown सामग्री अनुवादित करा:

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

Markdown लिंक अनुवादित करा आणि रीराइट करा:

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

Python मधून रिपॉझिटरी अनुवादित करा:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

एकाधिक रूट अनुवादित करा:

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

ग्लोसरी शब्द जतन करा:

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

कंटेंट ट्रान्सलेशन API त्या समाकलनांसाठी करण्यात आल्या आहेत ज्यांच्याकडे आधीपासूनच मेमरीमध्ये सामग्री असते, जसे की संपादक विस्तार, MCP टूल, नोटबुक प्रोसेसर, किंवा कस्टम पाइपलाइन.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. फक्त Markdown सामग्रीचे अनुवाद करते. हे लिंक रीराइट करत नाही, मेटाडेटा लिहीत नाही, किंवा डिस्क्लेमर जोडत नाही. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown सेलांचे अनुवाद करते आणि नॉन-Markdown सेल जतन करते. हे लिंक रीराइट करत नाही, मेटाडेटा लिहीत नाही, किंवा डिस्क्लेमर जोडत नाही. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. प्रतिमेतील मजकूर काढते आणि अनुवाद करते, नंतर रेंडर केलेली प्रतिमा परत करते. हे अनुवादित प्रतिमा मेटाडेटा जतन करत नाही. |

`translate_markdown_content` आणि `translate_notebook_content` त्यांच्या ऑप्शन्सद्वारे वैकल्पिक `source_path` स्वीकारतात. पथ अनुवादकाला संदर्भ म्हणून पास केला जातो; अनुवादानंतर प्रोजेक्ट-विशिष्ट पाथ रीराइटिंगसाठी कॉलर्स जबाबदार राहतात.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

समान ऑप्शन्स डिक्शनरी म्हणूनही पास केले जाऊ शकतात:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

एजंट-सहाय्यक API Co-op Translator मधून Azure OpenAI किंवा OpenAI कॉल करत नाहीत. हे होस्ट एजंटला अनुवादासाठी Markdown किंवा नोटबुक चंक्स तयार करतात, नंतर अनुवादित चंक्समधून अंतिम सामग्री पुन्हा तयार करतात.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | चंक्स, प्रॉम्प्ट्स, आणि पुन्हा संकलन स्थितीसह स्वयंपूरक Markdown जॉब परत करा. |
| `finish_markdown_agent_translation` | जॉब आणि होस्ट-एजंटच्या अनुवादित चंक्समधून Markdown पुनर्निर्माण करा. |
| `start_notebook_agent_translation` | होस्ट-एजंट अनुवादासाठी Markdown-सेल चंक्ससह नोटबुक जॉब परत करा. |
| `finish_notebook_agent_translation` | कोड सेल्स, आउटपुट, आणि मेटाडेटा जपून नोटबुक JSON पुनर्निर्माण करा. |

हा कार्यप्रवाह मुख्यतः MCP होस्टसाठी उद्दिष्टित आहे. जर आपल्याला Co-op Translator हा प्रदाता कॉल्स व्यवस्थापित करत प्रॉडक्शन रिपॉझिटरी अनुवाद आवश्यक असेल तर `translate_markdown_content`, `translate_notebook_content`, किंवा `run_translation` वापरा.

## Path Rewriting APIs

पाथ रीराइटिंग API कोणताही अनुवाद करत नाहीत. ते लिंक आणि फ्रंटमॅटर पाथ अपडेट करतात जेव्हा कॉलर्सना स्त्रोत पथ, अनुवादित लक्ष्य पथ, आणि प्रोजेक्ट लेआउट माहिती असते.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | अनुवादित लक्ष्यासाठी Markdown लिंक आणि समर्थित फ्रंटमॅटर पाथ फील्ड रीराइट करते. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | प्रत्येक Markdown सेलवर Markdown पाथ रीराइटिंग लागू करते आणि नॉन-Markdown सेल्स अपरिवर्तित ठेवते. |

`policy` आर्ग्युमेंट खालील फील्डसह डिक्शनरी असू शकते:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | लक्ष्य भाषा कोड, उदा. `"ko"` किंवा `"pt-BR"`. |
| `root_dir` | No | स्त्रोत प्रोजेक्ट रूट. डीफॉल्ट `"."`. |
| `translations_dir` | No | टेक्स्ट अनुवाद आउटपुट डायरेक्टरी. डीफॉल्ट `root_dir` अंतर्गत `translations`. |
| `translated_images_dir` | No | अनुवादित प्रतिमा आउटपुट डायरेक्टरी. डीफॉल्ट `root_dir` अंतर्गत `translated_images`. |
| `translation_types` | No | सक्षम केलेले अनुवाद प्रकार. डीफॉल्ट Markdown, नोटबुक, आणि प्रतिमा. |
| `lang_subdir` | No | प्रत्येक भाषा फोल्डर अंतर्गत ऐच्छिक सबडायरेक्टरी. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | स्पेस-वेगळे लक्ष्य भाषा कोड, उदा. `"ko ja fr"`, किंवा `"all"`. उपनाम कोड canonical BCP 47 मूल्यांवर सामान्यीकरण केले जातात. |
| `root_dir` | `str` | `"."` | एका अनुवाद लक्ष्यासाठी प्रोजेक्ट रूट. जेव्हा `root_dirs` किंवा `groups` पुरवले जातात तेव्हा दुर्लक्षित केले जाते. |
| `update` | `bool` | `False` | निवडलेल्या भाषांसाठी अस्तित्वात असलेले अनुवाद हटवून पुन्हा तयार करा. |
| `images` | `bool` | `False` | प्रतिमा अनुवाद समाविष्ट करा. Azure AI Vision कॉन्फिगरेशन आवश्यक आहे. |
| `markdown` | `bool` | `False` | Markdown अनुवाद समाविष्ट करा. |
| `notebook` | `bool` | `False` | Jupyter नोटबुक अनुवाद समाविष्ट करा. |
| `debug` | `bool` | `False` | डीबग लॉगिंग सक्षम करा. |
| `save_logs` | `bool` | `False` | रूट `logs/` डायरेक्टरीखाली DEBUG-स्तर लॉग फाइल्स जतन करा. |
| `yes` | `bool` | `True` | प्रोग्रामॅटिक आणि CI वापरासाठी प्रॉम्प्ट ऑटो-कन्फर्म करा. |
| `add_disclaimer` | `bool` | `False` | अनुवादित Markdown आणि नोटबुकमध्ये मशीन अनुवाद डिस्क्लेमर जोडा. |
| `translations_dir` | `str \| None` | `None` | कस्टम टेक्स्ट अनुवाद आउटपुट डायरेक्टरी. सापेक्ष पाथ्स प्रत्येक रूटच्या विरोधात सोडवले जातात. |
| `image_dir` | `str \| None` | `None` | कस्टम अनुवादित प्रतिमा आउटपुट डायरेक्टरी. सापेक्ष पाथ्स प्रत्येक रूटच्या विरोधात सोडवले जातात. |
| `root_dirs` | `Iterable[str] \| None` | `None` | एकाच आउटपुट सेटिंग्ज शेअर करणार्या अनेक रूट्स. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | स्पष्ट `(root_dir, translations_dir)` जोडी. `root_dirs` पेक्षा प्राधान्य घेतो. |
| `repo_url` | `str \| None` | `None` | README भाषा टेबल मार्गदर्शन रेंडर करताना वापरण्यात येणारी रिपॉझिटरी URL. |
| `glossaries` | `Iterable[str] \| None` | `None` | अनुवादादरम्यान जतन करण्यासाठी ग्लोसरी शब्द. डुप्लिकेट आणि रिकामे शब्द सामान्यीकरण केले जातात. |
| `dry_run` | `bool` | `False` | फाइल्स न लिहिता अनुवादाचा अंदाज व माइग्रेशन वर्तणूक पूर्वावलोकन करा. |

## Review Parameters

`run_review` शक्य असल्यास `run_translation` सिग्नेचरचे जाणिवपूर्वक अनुकरण करते जेणेकरून ऑटोमेशन अनुवाद आणि रिव्ह्यू कार्यप्रवाहांमध्ये कमी शाखीकरणाने स्विच करु शकेल.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | रिव्ह्यूसाठी लक्ष्य भाषा फोल्डर्स. स्पेस-वेगळ्या स्ट्रिंग्स आणि इटेरेबल स्वीकारल्या जातात. `"all"` हे प्रत्येक शोधलेल्या अनुवाद भाषा रिव्ह्यू करते. |
| `root_dir` | `str` | `"."` | एका रिव्ह्यू लक्ष्यासाठी प्रोजेक्ट रूट. जेव्हा `root_dirs` किंवा `groups` पुरवले जातात तेव्हा दुर्लक्षित केले जाते. |
| `markdown` | `bool` | `False` | Markdown आणि MDX स्त्रोत फाइल्स समाविष्ट करा. |
| `notebook` | `bool` | `False` | Jupyter नोटबुक स्त्रोत फाइल्स समाविष्ट करा. |
| `images` | `bool` | `False` | अनुवाद पर्यायांसह साम्य राखण्यासाठी राखीव. Markdown मधून प्रतिमांवरील लिंक संदर्भ तपासले जातात. |
| `translations_dir` | `str \| None` | `None` | कस्टम मजकूर अनुवाद आउटपुट निर्देशिका. सापेक्ष मार्ग प्रत्येक root च्या संदर्भात सोडवले जातात. |
| `root_dirs` | `Iterable[str] \| None` | `None` | समान आउटपुट सेटिंग्ज सामायिक करणारे अनेक root. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` जोड्या. `root_dirs` पेक्षा प्राधान्य मिळते. |
| `changed_from` | `str \| None` | `None` | रिव्ह्यूला बदललेल्या स्रोत फाइल्सपुरते मर्यादित करण्यासाठी वापरलेला Git ref. |
| `output_format` | `str` | `"text"` | रिव्ह्यू आउटपुट फॉरमॅट. समर्थित मूल्ये "text" आणि "github" आहेत. |
| `fail_on_warnings` | `bool` | `False` | इशाऱ्यांना त्रुटींसह अपयश म्हणून वागवा. |
| `debug` | `bool` | `False` | डीबग लॉगिंग सक्षम करा. |
| `save_logs` | `bool` | `False` | रूट `logs/` निर्देशिकेअंतर्गत DEBUG-स्तरीय लॉग फायली जतन करा. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## कॉन्फिगरेशन आवश्यकता

प्रदाते-आधारित अनुवाद API ला अनुवाद करण्यापूर्वी प्रदाता कॉन्फिगरेशन आवश्यक आहे:

- Markdown आणि notebook अनुवादासाठी LLM प्रदाता आवश्यक आहे. Azure OpenAI किंवा OpenAI पैकी कोणताही कॉन्फिगर करा.
- Image अनुवादासाठी LLM प्रदात्याशिवाय Azure AI Vision आवश्यक आहे.
- `run_translation` प्रोजेक्ट अनुवाद सुरू होण्यापूर्वी हलके कनेक्टिव्हिटी तपास चालवते.
- एजंट-सहाय्यक `start_*_agent_translation` आणि `finish_*_agent_translation` API Co-op Translator LLM प्रदात्यांना कॉल करत नाहीत. होस्ट अनुप्रयोग किंवा MCP एजंट तयार केलेले चंक्स अनुवादित करतो.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, आणि `run_review` निर्धारिक आहेत आणि प्रदाता क्रेडेन्शियल्सची आवश्यकता नाही.

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

`run_review` निर्धारिक आहे आणि Azure OpenAI, OpenAI, किंवा Azure AI Vision कॉन्फिगरेशनची आवश्यकता नाही.

## वर्तन नोंदी

- Content translation APIs अनुवाद प्रोजेक्ट पाथ री-रायटिंगपासून वेगळे ठेवतात. जेव्हा अनुवादित सामग्रीसाठी प्रोजेक्ट-सापेक्ष लिंक लक्ष्य स्थानानुसार समायोजित करायच्या असतील तेव्हा स्पष्टपणे `rewrite_markdown_paths` किंवा `rewrite_notebook_paths` कॉल करा.
- प्रोजेक्ट ऑर्केस्ट्रेशन API सामग्री अनुवादाभोवती प्रोजेक्ट वर्तन जोडतात, ज्यात फाइल शोध, लेखन, पाथ री-रायटिंग, मेटाडेटा, क्लीनअप, आणि ऐच्छिक अस्वीकरणे यांचा समावेश आहे.
- `run_translation` Click मार्गे प्रगती आणि अंदाज सारांश छापते, CLI वापरकर्ता अनुभवाशी जुळणारे.
- `dry_run=True` आभासी README अद्यतनांचा वापर करून अंदाज गणना करते, परंतु README किंवा अनुवाद फायली लिहीत नाही.
- `groups` अनुक्रमे प्रक्रिया केल्या जातात. काम सुरू होण्यापूर्वी एक एकूण एकत्रित अंदाज छापला जातो.
- जेव्हा image अनुवाद निवडला जातो, तेव्हा Vision कॉन्फिगरेशन गायब असल्यास अनुवाद सुरू होण्यापूर्वी त्रुटी निर्माण होते.
- मौजूदा alias-आधारित भाषा फोल्डर्स ओळखले जातात आणि रनच्या भाग म्हणून त्यांना canonical भाषा फोल्डर नावांमध्ये स्थलांतरित केले जाऊ शकते.
- `run_review` गहाळ अनुवादित फायली, गहाळ किंवा कालबाह्य अनुवाद मेटाडेटा, चुकीचे Markdown frontmatter/code fences, आणि अवैध अनुवादित नोटबुक JSON वर अयशस्वी होते.
- `run_review` डीफॉल्टनुसार गहाळ स्थानिक Markdown आणि image link लक्ष्ये इशाऱ्यांप्रमाणे नोंदवते.

## अंतर्गत कॉल पथ

API CLI द्वारे वापरल्या जाणाऱ्या त्याच कोअर अंमलबजावणीकडे सौंपते:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| क्लास | मॉड्यूल | जबाबदारी |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | प्रोजेक्ट-स्तरीय अनुवाद समन्वयित करतो, निर्देशिका व्यवस्थापन, प्रति-भाषा मेटाडेटा सामान्यीकरण, आणि Markdown, notebook, आणि image translators कडे कार्ये सोपवतो. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, notebooks, images, stale detection, आणि अनुवाद मेटाडेटा अपडेटसाठी असिंक्रोन फाइल प्रक्रिया कार्य पार पाडतो. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown फाइल वाचन, सामग्री अनुवाद, पाथ री-रायटिंग, मेटाडेटा, अस्वीकरणे, आणि लेखनाची समन्वय करतो. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | नोटबुक फाइल वाचन, Markdown-सेल अनुवाद, पाथ री-रायटिंग, मेटाडेटा, अस्वीकरणे, आणि लेखनाची समन्वय करतो. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | स्रोत इमेज शोध, इमेज अनुवाद, आउटपुट पाथ्स, मेटाडेटा, आणि लेखनाचे समन्वय करतो. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | अनुवादित Markdown जोड्या शोधतो, अनुवाद गुणवत्ता मूल्यांकन करतो, आणि कमी-विश्वास दुरुस्ती वर्कफ्लोसाठी विश्वास मेटाडेटा वाचतो. |
| `ReviewRunner` | `co_op_translator.review.runner` | स्रोत फाइल्स, लक्ष्य भाषा, आणि कॉन्फिगर केलेल्या अनुवाद root वर निर्धारिक रिव्ह्यू तपासण्यांचे समन्वय करतो. |
| `ReviewTarget` | `co_op_translator.review.targets` | एका स्रोत root आणि त्या root साठी पुनरावलोकन केलेली अनुवाद आउटपुट निर्देशिका यांचे वर्णन करतो. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | लेगेसी alias भाषा फोल्डर्स ओळखतो आणि canonical BCP 47 फोल्डर स्थलांतर योजना तयार करतो. |
| `Config` | `co_op_translator.config.base_config` | `.env` फाइल्स लोड करतो आणि आवश्यक LLM आणि ऐच्छिक Vision प्रदाते कॉन्फिगर आहेत का ते तपासतो. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI किंवा OpenAI आपोआप ओळखतो, आवश्यक पर्यावरणीय चल वैध करतो, आणि प्रदाता कनेक्टिव्हिटी तपासणी चालवतो. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision कॉन्फिगरेशन शोधतो आणि image अनुवादासाठी कनेक्टिव्हिटी तपासणी चालवतो. |