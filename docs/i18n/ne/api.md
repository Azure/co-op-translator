# Python API

स्थिर सार्वजनिक Python API `co_op_translator.api` बाट निर्यात गरिएको छ। धेरै एकीकरणहरूले यी मध्ये एक प्रवाहहरू प्रयोग गर्दछन्:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | तपाईंको एप्लिकेसन स्रोत सामग्री पढ्छ, अनुवादका लागि Co-op Translator लाई बोलाउँछ, र परिणाम कहाँ बचत गर्ने निर्णय गर्छ। | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | तपाईंको MCP होस्ट वा एप्लिकेसन मोडेलले च्यांकहरू अनुवाद गर्नेछ, जबकि Co-op Translator ले चंकिनिङ र पुनर्निर्माण ह्यान्डल गर्छ। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | तपाईं चाहनुहुन्छ कि Python API CLI जस्तो व्यवहार गरोस् र खोजी, आउटपुट पाथहरू, मेटाडाटा, क्लीनअप, र लेखनहरू ह्यान्डल गरोस्। | `run_translation` |

धेरै निचला-स्तर मोड्युलहरू `core`, `config`, `review`, र `utils` अन्तर्गत यी API प्रविष्टि बिन्दुहरूले प्रयोग गर्ने इम्प्लिमेन्टेशन विवरणहरू हुन्।

MCP क्लाइन्टहरूले [MCP Server](mcp.md) मार्फत एउटै सार्वजनिक API प्रयोग गर्दछन्। जब तपाईं सिधै Python बोलाउनुहुन्छ यो पृष्ठ प्रयोग गर्नुहोस्, र एजेन्ट वा सम्पादकलाई Co-op Translator एक्स्पोज गर्दा MCP गाइड प्रयोग गर्नुहोस्। यदि तपाईं CLI, Python API, र MCP बीच निर्णय गर्दै हुनुहुन्छ भने, [Choose Your Workflow](workflows.md) बाट सुरु गर्नुहोस्।

## First-Time API Flow

यहाँबाट सुरु गर्नुहोस् यदि तपाईं Python 코드बाट Co-op Translator कल गर्दै हुनुहुन्छ भने:

1. [Configuration](configuration.md) मा वर्णन गरिएको अनुसार LLM प्रदायक कन्फिगर गर्नुहोस्, जबसम्म तपाईं केवल Markdown वा नोटबुक चंक्सहरु होस्ट-एजेन्ट अनुवादका लागि तयार गर्दै हुनुहुन्न।
2. निर्णय गर्नुहोस् कि तपाईंको एप्लिकेसनले फाइल I/O व्यवस्थापन गर्छ कि गर्दैन।
3. जब तपाईंको एप्लिकेसनले व्यक्तिगत फाइलहरू पढ्छ र लेख्छ तब सामग्री API हरू प्रयोग गर्नुहोस्।
4. Co-op Translator ले CLI जस्तो रिपोजिटरी प्रोसेस गर्नुपर्छ भने `run_translation` प्रयोग गर्नुहोस्।
5. यदि तपाईंलाई स्वतःकरणमा निर्धारणयोग्य जाँचहरू चाहिन्छ भने अनुवादपछि `run_review` प्रयोग गर्नुहोस्।

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

यो कार्यप्रवाह तब प्रयोग गर्नुहोस् जब तपाइंसँग पहिले नै फाइल, सम्पादक बफर, नोटबुक पेलोड, MCP अनुरोध, वा कस्टम पाइपलाइन इनपुट छ। तपाईंको कोड फाइल I/O को मालिक छ:

1. स्रोत सामग्री पढ्नुहोस्।
2. सामग्री अनुवाद API कल गर्नुहोस्।
3. विकल्पगत रूपमा पाथ राइटराइटिङ API कल गर्नुहोस् यदि अनुवादित सामग्री परियोजना अनुवाद फोल्डरमा लेखिनेछ भने।
4. तपाईंको एप्लिकेसनबाट परिणाम बचत वा फर्काउनुहोस्।

सामग्री अनुवाद API हरू प्रोजेक्ट डिस्कभरी चलाउँदैनन्, मेटाडाटा लेख्दैनन्, डिस्क्लेमरहरू थप्दैनन्, र स्वतः लिंकहरू राइटराइट गर्दैनन्।

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

यदि अनुवादित Markdown Co-op Translator परियोजना लेआउटमा बस्ने छैन भने, `rewrite_markdown_paths` स्किप गर्नुहोस् र अनुवादित स्ट्रिङ सिधै बचत गर्नुहोस्।

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

`translate_notebook_content` ले Markdown सेलहरू अनुवाद गर्छ र गैर-Markdown सेलहरू संरक्षण गर्छ। पाथ राइटराइटिङ केवल Markdown सेलहरूमा लागू हुन्छ।

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

`translate_image_content` स्रोत इमेज पढ्छ र रेंडर्ड `PIL.Image.Image` फिर्ता गर्छ। यसले अनुवादित इमेज मेटाडाटा लेख्दैन।

## Scenario 2: Translate an Entire Repository

यो कार्यप्रवाह तब प्रयोग गर्नुहोस् जब तपाईं चाहनुहुन्छ कि Python API `translate` CLI जस्तो व्यवहार गरोस्। `run_translation` ले समर्थित फाइलहरू खोज्छ, चयनित सामग्री प्रकारहरू अनुवाद गर्छ, पाथहरू राइटराइट गर्छ, आउटपुट फाइलहरू लेख्छ, मेटाडाटा अद्यावधिक गर्छ, र क्लीनअप जस्ता अनुवाद मर्मतकार्यहरू प्रदर्शन गर्छ।

`run_translation` परियोजना ऑर्केस्ट्रेसनको प्राथमिक प्रविष्टि बिन्दु हो। `translate_project` समान व्यवहार भएको कम्प्याटिबिलिटी अलायसको रूपमा निर्यात गरिएको छ।

वर्तमान रिपोजिटरीका Markdown फाइलहरू कोरियन र जापानीमा अनुवाद गर्नुहोस्:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

एक विशिष्ट परियोजना रुटबाट केवल नोटबुकहरू अनुवाद गर्नुहोस्:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

फाइलहरू लेख्दै बिना अनुवाद मात्रा पूर्वावलोकन गर्नुहोस्:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

एकै कलमा बहु सामग्री रुटहरू अनुवाद गर्नुहोस्:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

स्पष्ट आउटपुट समूहहरूमा अनुवादहरू लेख्नुहोस्:

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

प्रत्येक भाषाले नेस्टेड सबडाइरेक्टरी समावेश गर्नुपर्ने हुँदा प्रति-भाषा प्लेसहोल्डर प्रयोग गर्नुहोस्:

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

यदि `markdown`, `notebook`, वा `images` मध्ये कुनै पनि सेट गरिएको छैन भने, API ले सबै समर्थित प्रकारहरू अनुवाद गर्छ: Markdown, नोटबुक, र इमेजहरू।

## Review Translated Output

`run_review` ले LLM वा Vision प्रमाणपत्र बिना निर्धारणयोग्य अनुवाद जाँचहरू चलाउँछ।

!!! note "बेटा"
    `run_review` एक बेटा निर्धारणयोग्य समीक्षा API हो। यसले मोडल प्रदायकहरूलाई कल गर्दैन वा फाइलहरू लेख्दैन, तर जाँचहरू र इश्यू स्किमाहरू परिवर्तन हुन सक्छन्।

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

केवल बेस रेफ विरुद्ध परिवर्तन भएका फाइलहरू मात्र समीक्षा गर्नुहोस् र GitHub-फ्लेवर्ड आउटपुट मुद्रण गर्नुहोस्:

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

फाइल लेख्न बिना Markdown सामग्री अनुवाद गर्नुहोस्:

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

Markdown लिङ्कहरू अनुवाद गरेर राइटराइट गर्नुहोस्:

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

Python बाट रिपोजिटरी अनुवाद गर्नुहोस्:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

एकाधिक रुटहरू अनुवाद गर्नुहोस्:

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

Glossary शब्दहरू राख्नुहोस्:

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

सामग्री अनुवाद API हरू ती एकीकरणहरूका लागि लक्षित छन् जससँग पहिले नै मेमोरीमा सामग्री हुन्छ, जस्तै सम्पादक एक्सटेन्सन, MCP उपकरण, नोटबुक प्रोसेसर, वा कस्टम पाइपलाइन।

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. केवल Markdown सामग्री अनुवाद गर्छ। यसले लिंकहरू राइटराइट गर्दैन, मेटाडाटा लेख्दैन, वा डिस्क्लेमरहरू थप्दैन। |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown सेलहरू अनुवाद गर्छ र गैर-Markdown सेलहरू संरक्षण गर्छ। यसले लिंकहरू राइटराइट गर्दैन, मेटाडाटा लेख्दैन, वा डिस्क्लेमरहरू थप्दैन। |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. इमेज टेक्स्ट निकालेपछि अनुवाद गरेर रेंडर्ड इमेज फिर्ता गर्छ। यसले अनुवादित इमेज मेटाडाटा बचत गर्दैन। |

`translate_markdown_content` र `translate_notebook_content` ले वैकल्पिक `source_path` आफ्नो विकल्पमार्गबाट स्वीकार गर्छन्। पाथ अनुवादकलाई सन्दर्भको रूपमा पास गरिन्छ; कल गर्नेहरूले अनुवादपछि कुनै परियोजना-विशेष पाथ राइटराइटिङको जिम्मेवारी बाँकी राख्छन्।

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

उही विकल्पहरू डिक्शनरीहरूका रूपमा पनि पठाउन सकिन्छ:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

एजेन्ट-असिस्टेड API हरू Co-op Translator बाट Azure OpenAI वा OpenAI कल गर्दैनन्। तिनीहरूले होस्ट एजेन्टलाई अनुवादका लागि Markdown वा नोटबुक चंक्सहरू तयार पार्छन्, त्यसपछि अनुवादित चंक्सहरूबाट अन्तिम सामग्री पुनर्निर्माण गर्छन्।

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | चंक्स, प्रॉम्प्टहरू, र पुनर्निर्माण अवस्था सहित स्व-निहित Markdown काम फिर्ता गर्छ। |
| `finish_markdown_agent_translation` | एउटा जॉब र होस्ट-एजेन्टले अनुवाद गरेका चंक्सबाट Markdown पुनर्निर्माण गर्छ। |
| `start_notebook_agent_translation` | होस्ट-एजेन्ट अनुवादका लागि Markdown-सेल चंक्ससहित नोटबुक जॉब फिर्ता गर्छ। |
| `finish_notebook_agent_translation` | कोड सेलहरू, आउटपुटहरू, र मेटाडाटा संरक्षण गर्दै नोटबुक JSON पुनर्निर्माण गर्छ। |

यो कार्यप्रवाह मुख्य रूपमा MCP होस्टहरूको लागि लक्षित छ। यदि तपाईंलाई उत्पादन रिपोजिटरी अनुवाद चाहिन्छ जहाँ Co-op Translator प्रदायक कॉलहरू व्यवस्थापन गर्छ, भने `translate_markdown_content`, `translate_notebook_content`, वा `run_translation` प्रयोग गर्नुहोस्।

## Path Rewriting APIs

पाथ राइटराइटिङ API हरूले कुनै अनुवाद गर्दैनन्। तिनीहरूले कल गर्नेहरूले स्रोत पाथ, अनुवादित लक्ष्य पाथ, र परियोजना लेआउट थाहा पाएपछि लिंकहरू र फ्रन्टम्याटर पाथहरू अपडेट गर्छन्।

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | अनुवादित लक्ष्यका लागि Markdown लिङ्कहरू र समर्थित फ्रन्टम्याटर पाथ फिल्डहरू राइटराइट गर्छ। |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | प्रत्येक Markdown सेलमा Markdown पाथ राइटराइटिङ लागू गर्छ र गैर-Markdown सेलहरू अपरिवर्तित छोड्छ। |

`policy` तर्कले यी फिल्डहरू भएका डिक्शनरी हुन सक्छ:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | लक्ष्य भाषा कोड, जस्तै `"ko"` वा `"pt-BR"`। |
| `root_dir` | No | स्रोत परियोजना रुट। पूर्वनिर्धारित `"."` हो। |
| `translations_dir` | No | पाठ अनुवाद आउटपुट डाइरेक्टरी। पूर्वनिर्धारित `translations` `root_dir` भित्र। |
| `translated_images_dir` | No | अनुवादित इमेज आउटपुट डाइरेक्टरी। पूर्वनिर्धारित `translated_images` `root_dir` भित्र। |
| `translation_types` | No | सक्षम अनुवाद प्रकारहरू। पूर्वनिर्धारित Markdown, नोटबुक, र इमेजहरू। |
| `lang_subdir` | No | प्रत्येक भाषा फोल्डर भित्र वैकल्पिक सबडाइरेक्टरी। |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | स्पेस-सेपरेट गरिएको लक्ष्य भाषा कोडहरू, जस्तै `"ko ja fr"`, वा `"all"`। अलायस कोडहरू BCP 47 मानकमा सामान्यीकृत गरिन्छ। |
| `root_dir` | `str` | `"."` | एकल अनुवाद लक्ष्यको लागि परियोजना रुट। `root_dirs` वा `groups` आपूर्ति गर्दा यो अनदेखा गरिन्छ। |
| `update` | `bool` | `False` | चयन गरिएका भाषाहरूका लागि अवस्थित अनुवादहरू मेटाएर पुनः सिर्जना गर्नुहोस्। |
| `images` | `bool` | `False` | इमेज अनुवाद समावेश गर्नुहोस्। Azure AI Vision कन्फिगरेसन आवश्यक छ। |
| `markdown` | `bool` | `False` | Markdown अनुवाद समावेश गर्नुहोस्। |
| `notebook` | `bool` | `False` | Jupyter नोटबुक अनुवाद समावेश गर्नुहोस्। |
| `debug` | `bool` | `False` | डीबग लगिङ सक्षम पार्नुहोस्। |
| `save_logs` | `bool` | `False` | रुट `logs/` डाइरेक्टरी अन्तर्गत DEBUG-स्तर लग फाइलहरू बचत गर्नुहोस्। |
| `yes` | `bool` | `True` | प्रोग्राम्याटिक र CI प्रयोगका लागि अटो-कन्फर्म प्रम्प्टहरू। |
| `add_disclaimer` | `bool` | `False` | अनुवादित Markdown र नोटबुकहरूमा मेशिन अनुवाद डिस्क्लेमरहरू थप्नुहोस्। |
| `translations_dir` | `str \| None` | `None` | कस्टम पाठ अनुवाद आउटपुट डाइरेक्टरी। सापेक्ष पाथहरू प्रत्येक रुटको सन्दर्भमा हल हुन्छन्। |
| `image_dir` | `str \| None` | `None` | कस्टम अनुवादित इमेज आउटपुट डाइरेक्टरी। सापेक्ष पाथहरू प्रत्येक रुटको सन्दर्भमा हल हुन्छन्। |
| `root_dirs` | `Iterable[str] \| None` | `None` | एउटै आउटपुट सेटिङ्स साझा गर्ने बहु रुटहरू। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | स्पष्ट `(root_dir, translations_dir)` जोडीहरू। `root_dirs` भन्दा प्राथमिकता दिइन्छ। |
| `repo_url` | `str \| None` | `None` | README भाषा तालिका मार्गदर्शन रेंडर गर्दा प्रयोग हुने रिपोजिटरी URL। |
| `glossaries` | `Iterable[str] \| None` | `None` | अनुवादको क्रममा संरक्षण गर्नुपर्ने शब्दसंग्रह शब्दहरू। नक्कलहरू र खाली शब्दहरू सामान्यीकृत गरिन्छ। |
| `dry_run` | `bool` | `False` | फाइलहरू लेख्नु बिना अनुवाद मात्रा अनुमान र माइग्रेसन व्यवहार पूर्वावलोकन गर्नुहोस्। |

## Review Parameters

`run_review` जानाजानी `run_translation` को सिग्नेचरलाई जहाँ सम्भव मिलाउँछ ताकि स्वतःकरणले न्यूनतम ब्रान्चिङका साथ अनुवाद र समीक्षा कार्यप्रवाहहरू बीच स्विच गर्न सकोस्।

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | समीक्षा गर्न लक्षित भाषा फोल्डरहरू। स्पेस-सेपरेटेड स्ट्रिङहरू र इटेरेबलहरू स्वीकार गरिन्छ। `"all"` ले पत्ता लागेको प्रत्येक अनुवाद भाषा समीक्षा गर्छ। |
| `root_dir` | `str` | `"."` | एकल समीक्षा लक्ष्यको लागि परियोजना रुट। `root_dirs` वा `groups` आपूर्ति हुँदा यो अनदेखा गरिन्छ। |
| `markdown` | `bool` | `False` | Markdown र MDX स्रोत फाइलहरू समावेश गर्नुहोस्। |
| `notebook` | `bool` | `False` | Jupyter नोटबुक स्रोत फाइलहरू समावेश गर्नुहोस्। |
| `images` | `bool` | `False` | अनुवाद विकल्पहरूसँग समता कायम राख्न आरक्षित। Markdown बाट इमेज रिफरेन्सहरू जाँच गरिन्छ। |
| `translations_dir` | `str \| None` | `None` | अनुकूलित टेक्स्ट अनुवाद आउटपुट डाइरेक्टरी। सापेक्ष पथहरू प्रत्येक root विरुद्ध समाधान गरिन्छ। |
| `root_dirs` | `Iterable[str] \| None` | `None` | एकै आउटपुट सेटिङ साझा गर्ने एकाधिक roots। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs। `root_dirs` माथि प्राथमिकता लिन्छ। |
| `changed_from` | `str \| None` | `None` | समीक्षा परिवर्तन भएका स्रोत फाइलहरूमा सीमित गर्न प्रयोग गरिने Git ref। |
| `output_format` | `str` | `"text"` | समीक्षा आउटपुट ढाँचा। समर्थन गरिएका मानहरू `"text"` र `"github"` हुन्। |
| `fail_on_warnings` | `bool` | `False` | त्रुटिहरूको अतिरिक्त चेतावनीहरूलाई असफलता मानिन्छ। |
| `debug` | `bool` | `False` | डिबग लगिङ सक्षम गर्नुहोस्। |
| `save_logs` | `bool` | `False` | रुट `logs/` डाइरेक्टरी अन्तर्गत DEBUG-स्तरका लग फाइलहरू सुरक्षित गर्नुहोस्। |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## कन्फिगरेशन आवश्यकताहरू

प्रदायक-समर्थित अनुवाद API हरूले अनुवाद गर्नु अघि प्रदायक कन्फिगरेसन आवश्यक पर्छ:

- Markdown र नोटबुक अनुवादका लागि LLM प्रदायक आवश्यक हुन्छ। Azure OpenAI वा OpenAI मध्ये कुनै एक कन्फिगर गर्नुहोस्।
- इमेज अनुवादका लागि LLM प्रदायकको साथै Azure AI Vision आवश्यक हुन्छ।
- `run_translation` प्रोजेक्ट अनुवाद सुरु हुनुअघि हल्का कनेक्टिभिटी जाँचहरू चलाउँछ।
- एजेन्ट-सहायता प्राप्त `start_*_agent_translation` र `finish_*_agent_translation` API हरूले Co-op Translator LLM प्रदायकहरूलाई कल गर्दैनन्। होस्ट एप्लिकेसन वा MCP एजेन्टले तयार गरिएका चंकहरू अनुवाद गर्छ।
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, र `run_review` निर्धारणक्षम छन् र प्रदायक प्रमाणपत्रहरू आवश्यक पर्दैन।

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

`run_review` निर्धारणक्षम छ र Azure OpenAI, OpenAI, वा Azure AI Vision कन्फिगरेसन आवश्यक पर्दैन।

## व्यवहार नोटहरू

- सामग्री अनुवाद API हरूले अनुवादलाई प्रोजेक्ट पथ पुनर्लेखनबाट अलग राख्छन्। अनुवादित सामग्रीको प्रोजेक्ट-सापेक्ष लिंकहरू लक्षित स्थानका लागि समायोजन गर्न आवश्यक परेमा स्पष्ट रूपमा `rewrite_markdown_paths` वा `rewrite_notebook_paths` कल गर्नुहोस्।
- प्रोजेक्ट अर्पेष्ट्रेसन (orchestration) API हरूले सामग्री अनुवादको वरिपरि प्रोजेक्ट व्यवहार थप्छन्, जसमध्ये फाइल खोजी, लेखन, पथ पुनर्लेखन, मेटाडाटा, क्लिनअप, र वैकल्पिक अस्वीकरणहरू समावेश छन्।
- `run_translation` Click मार्फत प्रगति र अनुमान सारांशहरू प्रिन्ट गर्छ, CLI प्रयोगकर्ता अनुभवसँग मेल खाने।
- `dry_run=True` ले भर्चुअल README अद्यावधिकहरू प्रयोग गरेर अनुमानहरू गणना गर्छ, तर README वा अनुवाद फाइलहरू लेख्दैन।
- `groups` क्रमशः प्रक्रियागर्दै हुन्छन्। काम सुरु हुनअघि एकल समग्र अनुमान प्रिन्ट गरिन्छ।
- इमेज अनुवाद चयन गर्दा, Vision कन्फिगरेसन हराएमा अनुवाद सुरु हुनुअघि त्रुटि उब्जिन्छ।
- अवस्थित एलियस-आधारित भाषा फोल्डरहरू पत्ता लगाइन्छ र रनको भागको रूपमा क्यानोनिकल BCP 47 भाषा फोल्डर नामहरूमा माइग्रेट गर्न सकिन्छ।
- `run_review` ले हराएका अनूदित फाइलहरू, हराएको वा पुरानो अनुवाद मेटाडाटा, बिग्रिएको Markdown frontmatter/code fences, र अमान्य अनूदित नोटबुक JSON मा असफल हुन्छ।
- `run_review` ले स्थानीय Markdown र इमेज लिंक लक्ष्यहरू हराइरहेका छन् भने तिनीहरूलाई पूर्वनिर्धारित रूपमा चेतावनीहरूको रूपमा रिपोर्ट गर्छ।

## आन्तरिक कल पथ

API ले CLI द्वारा प्रयोग गरिएको उस्तै मूल इम्प्लिमेन्टेशनमा डेलिगेट गर्छ:

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

| कक्षा | मोड्युल | जिम्मेवारी |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | प्रोजेक्ट-स्तर अनुवाद, डाइरेक्टरी व्यवस्थापन, प्रति-भाषा मेटाडाटा सामान्यीकरण, र Markdown, नोटबुक, तथा इमेज अनुवादकहरूमा जिम्मेवारी सुम्प्ने काम समन्वय गर्छ। |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, नोटबुक, इमेज, पुरानो अवस्था पत्ता लगाउने (stale detection), र अनुवाद मेटाडाटा अपडेटहरूको लागि असिन्क फाइल प्रोसेसिङ काम गर्छ। |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown फाइल पढाइ, सामग्री अनुवाद, पथ पुनर्डेखन, मेटाडाटा, अस्वीकरणहरू, र लेखनहरू समन्वय गर्छ। |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | नोटबुक फाइल पढाइ, Markdown-सेल अनुवाद, पथ पुनर्लेखन, मेटाडाटा, अस्वीकरणहरू, र लेखनहरू समन्वय गर्छ। |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | स्रोत इमेज खोजी, इमेज अनुवाद, आउटपुट पथहरू, मेटाडाटा, र लेखन समन्वय गर्छ। |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | अनूदित Markdown जोडीहरू फेला पार्छ, अनुवाद गुणस्तर मूल्याङ्कन गर्छ, र कम-विश्वस्तता मर्मत कार्यप्रवाहहरूका लागि विश्वास मेटाडाटा पढ्छ। |
| `ReviewRunner` | `co_op_translator.review.runner` | स्रोत फाइलहरू, लक्ष्य भाषाहरू, र कन्फिगर गरिएका अनुवाद रुटहरूमा निर्धारणक्षम समीक्षा जाँचहरू समन्वय गर्छ। |
| `ReviewTarget` | `co_op_translator.review.targets` | एक स्रोत root र उक्त root का लागि समीक्षा गरिने अनुवाद आउटपुट डाइरेक्टरी वर्णन गर्छ। |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | पुराना alias भाषा फोल्डरहरू पत्ता लगाउँछ र क्यानोनिकल BCP 47 फोल्डर माइग्रेशन योजना तयार गर्छ। |
| `Config` | `co_op_translator.config.base_config` | `.env` फाइलहरू लोड गर्छ र आवश्यक LLM र वैकल्पिक Vision प्रदायकहरू कन्फिगर गरिएको छ कि छैन जाँच्छ। |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI वा OpenAI स्वचालित रूपमा पहिचान गर्छ, आवश्यक वातावरण भेरिएबलहरू प्रमाणित गर्छ, र प्रदायक कनेक्टिभिटी जाँचहरू चलाउँछ। |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision कन्फिगरेसन पत्ता लगाउँछ र इमेज अनुवादका लागि कनेक्टिभिटी जाँचहरू चलाउँछ। |