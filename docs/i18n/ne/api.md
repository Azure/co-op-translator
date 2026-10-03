# Python API

स्थिर सार्वजनिक Python API `co_op_translator.api` बाट निर्यात गरिएको छ। अधिकांश एकीकरणहरूले यी कार्यप्रवाह मध्ये एक प्रयोग गर्छन्:

| परिदृश्य | यो प्रयोग गर्नुहोस् जब | मुख्य API हरू |
| --- | --- | --- |
| व्यक्तिगत फाइलहरू वा दस्तावेजहरू अनुवाद गर्नुहोस् | तपाइँको अनुप्रयोग स्रोत सामग्री पढ्छ, Co-op Translator लाई अनुवादका लागि कल गर्छ, र परिणाम कहाँ सुरक्षित गर्ने निर्णय गर्छ। | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| होस्ट-एजेन्ट अनुवादका लागि सामग्री तयार गर्नुहोस् | तपाईंको MCP होस्ट वा अनुप्रयोग मोडेलले चंकहरू अनुवाद गर्नेछ, जबकि Co-op Translator ले चंकिङ र पुनर्निर्माण व्यवस्थापन गर्छ। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| पूरा रिपोजिटरी अनुवाद गर्नुहोस् | तपाईं चाहनुहुन्छ कि Python API ले CLI जस्तै व्यवहार गरोस् र डिस्कवरी, आउटपुट पथ, मेटाडाटा, सफाइ, र लेखनहरू व्यवस्थापन गरोस्। | `run_translation` |

अधिकांश तल्लो-स्तरका मोड्युलहरू `core`, `config`, `review`, र `utils` अन्तर्गत यी API प्रवेश पोइन्टहरूले प्रयोग गर्ने कार्यान्वयन विवरणहरू हुन्।

MCP क्लाइन्टहरूले [MCP Server](mcp.md) मार्फत उही सार्वजनिक API प्रयोग गर्छन्। Python प्रत्यक्ष रूपमा कल गर्दा यो पृष्ठ प्रयोग गर्नुहोस्, र Co-op Translator लाई एजेन्ट वा सम्पादकमा प्रदर्शन गर्दा MCP मार्गदर्शिका प्रयोग गर्नुहोस्। यदि तपाईं CLI, Python API, र MCP बीच निर्णय गर्दै हुनुहुन्छ भने, [आफ्नो कार्यप्रवाह छान्नुहोस्](workflows.md) बाट सुरु गर्नुहोस्।

## पहिलो पटक API फ्लो

यहाँबाट सुरु गर्नुहोस् यदि तपाईं Python कोडबाट Co-op Translator कल गर्दै हुनुहुन्छ:

1. [कन्फिगरेसन](configuration.md) मा वर्णन गरिएको अनुसार LLM प्रदायकलाई कन्फिगर गर्नुहोस्, जबसम्म तपाईं केवल होस्ट-एजेन्ट अनुवादका लागि Markdown वा नोटबुक चंकहरू तयार गरिरहनु भएको छैन।
2. तपाइँको अनुप्रयोगले फाइल I/O आफैं हाँक्छ कि होइन निर्णय गर्नुहोस्।
3. तपाइँको अनुप्रयोगले व्यक्तिगत फाइलहरु पढ्ने र लेख्ने बेला सामग्री API हरू प्रयोग गर्नुहोस्।
4. Co-op Translator ले CLI जस्तै रिपोजिटरी प्रोसेस गर्नु पर्ने बेला `run_translation` प्रयोग गर्नुहोस्।
5. यदि तपाइँलाई स्वचालनमा सुनिश्चित जाँचहरू चाहिन्छ भने अनुवादपछि `run_review` प्रयोग गर्नुहोस्।

| लक्ष्य | सुरु गर्नको लागि API |
| --- | --- |
| एक Markdown स्ट्रिङ वा फाइल अनुवाद गर्नुहोस् | `translate_markdown_content` |
| एक नोटबुक पेलोड अनुवाद गर्नुहोस् | `translate_notebook_content` |
| एक तस्बिर अनुवाद गर्नुहोस् | `translate_image_content` |
| होस्ट एजेन्टलाई Markdown वा नोटबुक चंकहरू अनुवाद गर्न दिनुहोस् | `start_markdown_agent_translation` वा `start_notebook_agent_translation` |
| आउटपुट पथ चयन गरेपछि अनुवादित लिङ्कहरू पुन:लेख्नुहोस् | `rewrite_markdown_paths` वा `rewrite_notebook_paths` |
| पूर्ण रिपोजिटरी अनुवाद गर्नुहोस् | `run_translation` |
| अनुवादित आउटपुट समीक्षा गर्नुहोस् | `run_review` |

## परिदृश्य 1: व्यक्तिगत फाइलहरू वा कागजातहरू अनुवाद गर्नुहोस्

जब तपाईंसँग पहिले नै फाइल, एडिटर बफर, नोटबुक पेलोड, MCP अनुरोध, वा कस्टम पाइपलाइन इनपुट छ भने यो कार्यप्रवाह प्रयोग गर्नुहोस्। तपाइँको कोडले फाइल I/O को नियन्त्रण गर्छ:

1. स्रोत सामग्री पढ्नुहोस्।
2. सामग्री अनुवाद API कल गर्नुहोस्।
3. वैकल्पिक रूपमा पथ पुन:लेखन API कल गर्नुहोस् यदि अनुवादित सामग्री प्रोजेक्ट अनुवाद फोल्डरमा लेखिनेछ भने।
4. तपाईंको अनुप्रयोगबाट नतिजा बचत वा फर्काउनुहोस्।

सामग्री अनुवाद API हरूले प्रोजेक्ट खोज चलाउँदैनन्, मेटाडाटा लेख्दैनन्, अस्वीकरणहरू थप्दैनन्, र लिङ्कहरू स्वत: पुन:लेख्दैनन्।

### Markdown फाइल

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

यदि अनुवादित Markdown Co-op Translator प्रोजेक्ट लेआउटमा नरहनेछ भने, `rewrite_markdown_paths` लाई छोड्नुहोस् र अनुवादित स्ट्रिङ सिधै सुरक्षित गर्नुहोस्।

### नोटबुक फाइल

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

`translate_notebook_content` ले Markdown कोषहरू अनुवाद गर्छ र गैर-Markdown कोषहरूलाई कायम राख्छ। पथ पुन:लेखन केवल Markdown कोषहरूमा लागू हुन्छ।

### छवि फाइल

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

`translate_image_content` ले स्रोत छवि पढ्छ र रेंडर गरिएको `PIL.Image.Image` फर्काउँछ। यसले अनुवादित छवि मेटाडाटा लेख्दैन।

## परिदृश्य 2: पूरा रिपोजिटरी अनुवाद गर्नुहोस्

जब तपाइँ चाहनुहुन्छ कि Python API `translate` CLI जस्तै व्यवहार गरोस् तब यो कार्यप्रवाह प्रयोग गर्नुहोस्। `run_translation` ले समर्थित फाइलहरू पत्ता लगाउँछ, चयन गरिएको सामग्री प्रकारहरू अनुवाद गर्छ, पथहरू पुन:लेखन गर्छ, आउटपुट फाइलहरू लेख्छ, मेटाडाटा अपडेट गर्छ, र सफाइ जस्ता अनुवाद मर्मत कार्यहरू गर्दछ।

`run_translation` प्राथमिक प्रोजेक्ट व्यवस्थापन प्रवेश बिन्दु हो। `translate_project` समान व्यवहार सहित एक कम्प्याटिबिलिटी उपनामका रूपमा निर्यात गरिएको छ।

वर्तमान रिपोजिटरीका Markdown फाइलहरूलाई कोरियन र जापानीमा अनुवाद गर्नुहोस्:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

विशिष्ट प्रोजेक्ट रुटबाट केवल नोटबुकहरू मात्र अनुवाद गर्नुहोस्:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

फाइलहरू लेख्नु बिना अनुवाद परिमाण पूर्वावलोकन गर्नुहोस्:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

एक एकीकरणका लागि संरचित प्रगति घटनाहरू रेकर्ड गर्नुहोस्:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # पेलोडलाई आफ्नो job-event तालिकामा भण्डारण गर्नुहोस् वा यसलाई आफ्नो UI तर्फ स्ट्रिम गर्नुहोस्।


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

घटनाहरूले संस्करणयुक्त स्किमा `co-op.translation.event.v1` प्रयोग गर्छन्। एकीकरणहरूले `type` र `stage_key` जस्ता स्थिर फिल्डहरूमा भर पर्नु पर्छ, मानव-समक्ष देखिने कन्सोल टेक्स्ट वा `stage_label` मा होइन।



एकै कलमा बहु सामग्री रुटहरू अनुवाद गर्नुहोस्:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

अनुवादहरूलाई स्पष्ट आउटपुट समूहहरूमा लेख्नुहोस्:

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

प्रत्येक भाषामा nested उप-निर्देशिका हुनुपर्ने बेला प्रति-भाषा प्लेसहोल्डर प्रयोग गर्नुहोस्:

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

यदि `markdown`, `notebook`, वा `images` मध्ये कुनै पनि सेट गरिएको छैन भने, API ले सबै समर्थित प्रकारहरू अनुवाद गर्छ: Markdown, नोटबुकहरू, र छविहरू।

### स्वीकृत मानव सम्पादनहरूलाई अनुवाद स्थिति प्रदायकसँग कायम राख्नुहोस्

स्वत: रूपमा, Co-op Translator यसको अवस्थित फाइल-स्तर व्यवहारलाई कायम राख्छ: जब
Markdown स्रोत पुरानो हुन्छ, सम्पूर्ण अनुवादित फाइल पुन: उत्पन्न गरिन्छ। होस्ट गरिएको
एकीकरणहरूले वैकल्पिक रूपमा मानवीय सम्पादनहरू सुरक्षित राख्न `TranslationStateProvider` पास गर्न सक्छन्
जसले परिवर्तन नभएका स्रोत ब्लकहरूमा गरेका सम्पादनहरूलाई कायम राख्छ।

प्रदायकले अन्तिम स्वीकृत स्रोत/लक्ष्य जोडी प्रदान गर्छ र प्रत्येक नयाँ
उम्मेदवार। स्वीकृतिको जिम्मेवारी एकीकरणको नै रहन्छ—उदाहरणका लागि,
अनुवाद पुल अनुरोध मर्ज भएपछि:

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

वैध स्वीकृत बेसलाइन भएको Markdown फाइलहरूका लागि, Co-op Translator ले समक्रमण गर्छ
शीर्ष-स्तर Markdown ब्लकहरू। अपरिवर्तित स्रोत ब्लकहरूले हालको अनुवादित
ब्लकहरू, जसमा व्यक्तिहरूद्वारा गरिएको सम्पादनहरू पनि समावेश छन्; परिवर्तन वा थप गरिएका स्रोत ब्लकहरू अनुवादका लागि पठाइन्छन्
अनुवादका लागि; मेटाइएका स्रोत ब्लकहरू हटाइन्छन्। यदि समक्रमण अस्पष्ट छ,
लक्ष्य संरचना परिवर्तन भएको छ, ब्लक अनुवाद अमान्य छ, वा कुनै बेसलाइन उपलब्ध छैन भने,
Co-op Translator सावधानीपूर्वक अवस्थित पूर्ण-फाइल
अनुवाद पथमा फर्किन्छ।

यो API दस्तावेज अनुवाद स्थिति भण्डारण गर्छ, क्रस-डकुमेन्ट वाक्यांश वा
सेग्मेन्ट अनुवाद मेमोरी होइन। यो हाल Markdown प्रोजेक्ट अनुवादमा लागू हुन्छ
। नोटबुक र छवि व्यवहार अपरिवर्तित छ। `update=True` पास गर्दा
अझै पूर्ण पुन:उत्पादनको अनुरोध हुन्छ।

यदि एक वा बढी फाइलहरू अनुवाद गर्न सकिंदैनन् भने, `run_translation` ले एक
`RuntimeError` फ्याँक्छ परियोजना कार्यप्रवाह समाप्त भएपछि,
खोइएको आउटपुट सहितको सफल रन रिपोर्ट गर्ने सट्टा। एकीकरणहरूले यसलाई असफल
कामको रूपमा हेर्नु पर्छ र पहिले स्वीकृत अनुवाद स्थिति राख्नुपर्छ।

## अनुवादित आउटपुटको समीक्षा

`run_review` ले LLM वा Vision प्रमाणपत्र बिना नियत अनुवाद जाँचहरू चलाउँछ।

!!! note "बीटा"
    `run_review` एक बीटा निर्धारणात्मक समीक्षा API हो। यसले मोडेल प्रदायकहरूको कल गर्दैन वा फाइलहरू लेख्दैन, तर जाँचहरू र मुद्दा स्किमाहरू विकास हुन सक्छन्।

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README-केवल अनुवादपछि, समीक्षाको लागि उही दायरा प्रयोग गर्नुहोस्:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` केवल प्रत्येक कन्फिगर गरिएको स्रोत रुट अन्तर्गत `README.md` मात्र समीक्षा गर्छ, अनुकूलित `groups` र आउटपुट निर्देशिकाहरू सहित।
अन्य कागजात र नेस्टेड READMEs बहिष्कृत छन्।
स्रोत README हराएको खण्डमा `ValueError` उचारिन्छ; असफल अनुवाद जाँचहरूले `RuntimeError` उचार्छ।


केवल बेस रेफ विरुद्ध परिवर्तन भएका फाइलहरू समीक्षा गर्नुहोस् र GitHub-शैलीको आउटपुट छाप्नुहोस्:

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

## कपी-पेस्ट API उदाहरणहरू

फाइल लेखाइ बिना Markdown सामग्री अनुवाद गर्नुहोस्:

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

Markdown लिङ्कहरू अनुवाद गरी पुन:लेख गर्नुहोस्:

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

शब्दावली शब्दहरू संरक्षित राख्नुहोस्:

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

## सार्वजनिक प्रवेश बिन्दुहरू

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

## सामग्री अनुवाद APIहरू

सामग्री अनुवाद API हरू तिनीहरूको स्मरणमा पहिले नै सामग्री भएका इंटिग्रेशनहरूका लागि उद्देश्य राखिएका छन्, जस्तै सम्पादक एक्सटेन्सन, MCP टुल, नोटबुक प्रोसेसर, वा कस्टम पाइपलाइन।

| फंक्शन | इनपुट | आउटपुट | फाइल I/O | नोटहरू |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | एसिन्क। केवल Markdown सामग्री अनुवाद गर्छ। यसले लिंकहरू पुनःलेख्दैन, मेटाडाटा लेख्दैन, वा अस्वीकरणहरू थप्दैन। |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | एसिन्क। Markdown सेलहरू अनुवाद गर्छ र गैर-Markdown सेलहरू संरक्षण गर्छ। यसले लिंकहरू पुनःलेख्दैन, मेटाडाटा लेख्दैन, वा अस्वीकरणहरू थप्दैन। |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | समकालिक। छवि पाठ निकाल्छ र अनुवाद गर्छ, त्यसपछि रेंडर गरिएको छवि फर्काउँछ। यसले अनुवादित छवि मेटाडाटा बचत गर्दैन। |

`translate_markdown_content` र `translate_notebook_content` लाई तिनीहरूको विकल्पहरू मार्फत वैकल्पिक `source_path` स्वीकार्छ। पथ अनुवादकलाई सन्दर्भको रूपमा पठाइन्छ; कलरहरूले अनुवादपछि कुनै पनि परियोजना-विशिष्ट पथ पुन:लेखनको लागि जिम्मेवार रहन्छन्।

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

उही विकल्पहरू डिक्शनरीहरू (dictionaries) को रूपमा पठाउन सकिन्छ:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## एजेन्ट-सहायित अनुवाद APIहरू

एजेन्ट-सहायित API हरू Co-op Translator बाट कन्फिगर गरिएको LLM प्रदायकलाई कल गर्दैनन्। तिनीहरूले होस्ट एजेन्टले अनुवाद गर्नका लागि Markdown वा नोटबुक चंकहरू तयार गर्दछन्, त्यसपछि अनुवाद गरिएका चंकहरूबाट अन्तिम सामग्री पुनर्निर्माण गर्दछन्।

| फंक्शन | उद्देश्य |
| --- | --- |
| `start_markdown_agent_translation` | खण्डहरू, प्रम्प्टहरू, र पुनर्निर्माण अवस्था सहित आत्म-निहित Markdown जाग (job) फिर्ता गर्छ। |
| `finish_markdown_agent_translation` | एक जाग र होस्ट-एजेन्टद्वारा अनुवाद गरिएका चंकहरूबाट Markdown पुनर्निर्माण गर्छ। |
| `start_notebook_agent_translation` | होस्ट-एजेन्ट अनुवादका लागि Markdown-सेल चंकहरू सहित नोटबुक जाग फिर्ता गर्छ। |
| `finish_notebook_agent_translation` | कोड सेलहरू, आउटपुटहरू, र मेटाडाटा जोगाउँदै नोटबुक JSON पुनर्निर्माण गर्छ। |

यो कार्यप्रवाह मुख्यतया MCP होस्टहरूका लागि हो। यदि तपाई production रिपोजिटरी अनुवाद चाहनुहुन्छ र Co-op Translator प्रदायक कलहरू व्यवस्थापन गरिरहेको छ भने, `translate_markdown_content`, `translate_notebook_content`, वा `run_translation` प्रयोग गर्नुहोस्।

## पथ पुनर्लेखन APIहरू

पाथ पुन:लेखन API हरू कुनै अनुवाद गर्दैनन्। कल गर्नेहरूले स्रोत पाथ, अनुवादित लक्ष्य पाथ, र परियोजना लेआउट थाहा पाएपछि तिनीहरूले लिंकहरू र फ्रन्टम्याटर पाथहरू अद्यावधिक गर्छन्।

| फंक्शन | दायरा | नोटहरू |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | अनुवादित लक्ष्यका लागि Markdown लिङ्कहरू र समर्थित फ्रन्टम्याटर पाथ फिल्डहरू पुन:लेख्दछ। |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | प्रत्येक Markdown सेलमा Markdown पाथ पुन:लेखन लागू गर्छ र गैर-Markdown सेलहरूलाई नबदलिएको अवस्थामा छोड्छ। |

यो `policy` आर्गुमेन्ट यी फिल्डहरू सहितको डिक्शनरी हुन सक्छ:

| फिल्ड | आवश्यक | उद्देश्य |
| --- | --- | --- |
| `language_code` | Yes | लक्षित भाषा कोड, जस्तै `"ko"` वा `"pt-BR"`। |
| `root_dir` | No | स्रोत परियोजना रुट। पूर्वनिर्धारित `"."`। |
| `translations_dir` | No | टेक्स्ट अनुवाद आउटपुट निर्देशिका। पूर्वनिर्धारित `translations` जुन `root_dir` भित्र हुन्छ। |
| `translated_images_dir` | No | अनुवादित छवि आउटपुट निर्देशिका। पूर्वनिर्धारित `translated_images` जुन `root_dir` भित्र हुन्छ। |
| `translation_types` | No | सक्षम गरिएको अनुवाद प्रकारहरू। पूर्वनिर्धारित: Markdown, नोटबुकहरू, र छविहरू। |
| `lang_subdir` | No | प्रत्येक भाषा फोल्डरअन्तर्गत वैकल्पिक सबडाइरेक्टरी। |

## परियोजना अनुवाद प्यारामिटरहरू

| प्यारामिटर | प्रकार | पूर्वनिर्धारित | उद्देश्य |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | स्पेस-भएर छुट्याइएका लक्षित भाषा कोडहरू, जस्तै `"ko ja fr"` वा `"all"`। एलियास कोडहरू canonical BCP 47 मानहरूमा सामान्यीकृत गरिन्छ। |
| `root_dir` | `str` | `"."` | एकल अनुवाद लक्ष्यको लागि परियोजना रुट। `root_dirs` वा `groups` दिइएमा उपेक्षित। |
| `update` | `bool` | `False` | चयनित भाषाहरूका लागि अवस्थित अनुवादहरू मेटाएर पुनः सिर्जना गर्नुहोस्। |
| `images` | `bool` | `False` | छवि अनुवाद समावेश गर्नुहोस्। Azure AI Vision कन्फिगरेसन आवश्यक छ। |
| `markdown` | `bool` | `False` | Markdown अनुवाद समावेश गर्नुहोस्। |
| `notebook` | `bool` | `False` | Jupyter नोटबुक अनुवाद समावेश गर्नुहोस्। |
| `debug` | `bool` | `False` | डिबग लगिंग सक्षम गर्नुहोस्। |
| `save_logs` | `bool` | `False` | रुट `logs/` निर्देशिकामा DEBUG-स्तरका लग फाइलहरू बचत गर्नुहोस्। |
| `yes` | `bool` | `True` | प्रोग्रामिक र CI प्रयोगका लागि संकेतहरू स्वत: पुष्टि गर्नुहोस्। |
| `add_disclaimer` | `bool` | `False` | अनुवादित Markdown र नोटबुकहरूमा मेसिन अनुवाद अस्वीकरण थप्नुहोस्। |
| `translations_dir` | `str \| None` | `None` | कस्टम पाठ अनुवाद आउटपुट निर्देशिका। सापेक्ष पथहरू प्रत्येक रुटको सापेक्ष समाधान हुन्छन्। |
| `image_dir` | `str \| None` | `None` | कस्टम अनुवादित छवि आउटपुट निर्देशिका। सापेक्ष पथहरू प्रत्येक रुटको सापेक्ष समाधान हुन्छन्। |
| `root_dirs` | `Iterable[str] \| None` | `None` | एकै आउटपुट सेटिङ्स साझा गर्ने धेरै रुटहरू। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | स्पष्ट `(root_dir, translations_dir)` जोडीहरू। `root_dirs` भन्दा प्राथमिकता लिन्छ। |
| `repo_url` | `str \| None` | `None` | README भाषा तालिका मार्गनिर्देशन रेंडर गर्दा प्रयोग हुने रिपोजिटरी URL। |
| `glossaries` | `Iterable[str] \| None` | `None` | अनुवादको क्रममा संरक्षित गर्नका लागि ग्लोसरी शब्दहरू। नक्कल र खाली शब्दहरू सामान्यीकृत गरिन्छ। |
| `dry_run` | `bool` | `False` | फाइलहरू लेख्ने बिना अनुवादको परिमाण अनुमान र माइग्रेशन व्यवहारको पूर्वावलोकन गर्छ। |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | इन्क्रिमेन्टल Markdown अपडेटका लागि वैकल्पिक accepted-baseline र candidate persistence-अडाप्टर। यसलाई नसमाविष्ट गर्दा विद्यमान पूर्ण-फाइल व्यवहार कायम रहन्छ। |

## समीक्षा प्यारामिटर

`run_review` जानबुझेर जहाँ सम्भव `run_translation` सिग्नेचरलाई नक्कल गर्छ ताकि अटोमेशनले अनुवाद र समीक्षा वर्कफ्लोहरू बीच न्यूनतम शाखीकरणका साथ स्विच गर्न सकोस्।

| प्यारामिटर | प्रकार | पूर्वनिर्धारित | उद्देश्य |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | समीक्षा गर्न लक्षित भाषा फोल्डरहरू। स्पेस-सेपरेटेड स्ट्रिङहरू र इटरेबलहरू स्वीकार्य छन्। `"all"` ले पत्ता लागेको सबै अनुवाद भाषाहरू समीक्षा गर्छ। |
| `root_dir` | `str` | `"."` | एकल समीक्षा लक्ष्यको लागि प्रोजेक्ट रुट। `root_dirs` वा `groups` प्रदान हुँदा उपेक्षित हुन्छ। |
| `markdown` | `bool` | `False` | Markdown र MDX स्रोत फाइलहरू समावेश गर्नुहोस्। |
| `notebook` | `bool` | `False` | Jupyter नोटबुक स्रोत फाइलहरू समावेश गर्नुहोस्। |
| `images` | `bool` | `False` | अनुवाद विकल्पहरूसँग समानताका लागि आरक्षित। छवि लिंक सन्दर्भहरू Markdown बाट जाँच गरिन्छ। |
| `translations_dir` | `str \| None` | `None` | कस्टम पाठ अनुवाद आउटपुट निर्देशिका। सापेक्ष पथहरू प्रत्येक रुटको सापेक्ष समाधान हुन्छन्। |
| `root_dirs` | `Iterable[str] \| None` | `None` | एकै आउटपुट सेटिङ साझा गर्ने बहु रुटहरू। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | स्पष्ट `(root_dir, translations_dir)` जोडीहरू। `root_dirs` माथि प्राथमिकता राख्छ। |
| `changed_from` | `str \| None` | `None` | परिवर्तन भएका स्रोत फाइलहरूमा मात्र समीक्षा सिमित गर्न प्रयोग गरिने Git ref। |
| `readme_only` | `bool` | `False` | हरेक स्रोत रुट अन्तर्गत मात्र `README.md` समीक्षा गर्नुहोस्। स्रोत README हराएमा `ValueError` उठाउँछ। |
| `output_format` | `str` | `"text"` | समीक्षा आउटपुट ढाँचा। समर्थन गरिएका मानहरू `"text"` र `"github"` हुन्। |
| `fail_on_warnings` | `bool` | `False` | चेतावनीहरूलाई त्रुटिसँगै असफलता मान्ने। |
| `debug` | `bool` | `False` | डिबग लगिङ सक्षम पार्नुहोस्। |
| `save_logs` | `bool` | `False` | DEBUG-स्तरका लग फाइलहरू root `logs/` निर्देशिकामा सुरक्षित गर्नुहोस्। |

यदि `markdown`, `notebook`, वा `images` मध्ये कुनै पनि सेट गरिएको छैन भने, API ले जहाँ लागू हुन्छ Markdown, नोटबुकहरू, र छवि लिंक सन्दर्भहरू समीक्षा गर्छ। समीक्षा ले LLM प्रदायकलाई कल गर्दैन र API कुञ्जीहरू आवश्यक पर्दैन।

## कन्फिगरेसन आवश्यकताहरू

प्रदायक-समर्थित अनुवाद API हरूले अनुवाद गर्नुअघि प्रदायक कन्फिगरेसन आवश्यक पर्छ:

- Markdown र नोटबुक अनुवादका लागि LLM प्रदायक आवश्यक हुन्छ। Azure OpenAI, OpenAI, वा Anthropic कन्फिगर गर्नुहोस्।
- छवि अनुवादका लागि LLM प्रदायकसँगै Azure AI Vision आवश्यक हुन्छ।
- `run_translation` प्रोजेक्ट अनुवाद सुरु हुनु अघि हल्का कनेक्टिविटी जाँचहरू चलाउँछ।
- एजेन्ट-सहायक `start_*_agent_translation` र `finish_*_agent_translation` API हरूले Co-op Translator LLM प्रदायकहरूलाई कॉल गर्दैनन्। होस्ट अनुप्रयोग वा MCP एजेन्टले तयार पारिएका chunks अनुवाद गर्छ।
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, र `run_review` निर्धार्य छन् र प्रदायक प्रमाणपत्र आवश्यक पर्दैन।

Azure OpenAI का आवश्यक भेरिएबलहरू:

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

Required Anthropic variables:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` र `ANTHROPIC_MAX_TOKENS` वैकल्पिक हुन्। Microsoft Agent Framework Co-op Translator 0.22.0 देखि सबै प्रदायकहरूको लागि पूर्वनिर्धारित मोडेल क्लाइन्ट हो। Semantic Kernel लाई अस्थायी रूपमा `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` द्वारा अझै चयन गर्न सकिन्छ, तर त्यसले विलुप्तता चेतावनी देखाउँछ; चरणबद्ध हटाउने योजनाका लागि [कन्फिगरेसन](configuration.md#model-client-backend) हेर्नुहोस्।

छवि अनुवादका लागि आवश्यक Azure AI Vision भेरिएबलहरू:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` निर्धार्य छ र LLM वा Azure AI Vision कन्फिगरेसन आवश्यक पर्दैन।

## व्यवहार सम्बन्धी नोटहरू

- सामग्री अनुवाद API हरूले अनुवादलाई प्रोजेक्ट पथ पुन:लेखनबाट अलग राख्छन्। अनुवादित सामग्रीलाई लक्ष्य स्थानका लागि प्रोजेक्ट-आधारित लिंक्स समायोजन गर्न आवश्यक भएमा स्पष्ट रूपमा `rewrite_markdown_paths` वा `rewrite_notebook_paths` कल गर्नुहोस्।
- प्रोजेक्ट अोर्केष्ट्रेशन API हरूले सामग्री अनुवाद वरिपरि प्रोजेक्ट व्यवहार थप्छन्, जसमा फाइल खोज, लेखन, पथ पुन:लेखन, मेटाडाटा, क्लिनअप, र वैकल्पिक अस्वीकरणहरू समावेश छन्।
- `run_translation` ले CLI द्वारा प्रयोग गरिने उस्तै Rich-आधारित रिपोर्टर मार्फत प्रगति र अनुमान सारांशहरू मुद्रण गर्छ। गैर-इंटरऐक्टिभ आउटपुटले साधारण पाठमा फर्किन्छ।
- `dry_run=True` ले भर्चुअल README अद्यावधिकहरू प्रयोग गरी अनुमान गणना गर्छ, तर README वा अनुवाद फाइलहरू लेख्दैन।
- `groups` क्रमशः प्रक्रिया गरिन्छ। काम सुरु हुनुअघि एकल समेकित अनुमान मुद्रण गरिन्छ।
- छवि अनुवाद चयन गर्दा Vision कन्फिगरेसन हराएमा अनुवाद सुरु हुनु अघि त्रुटि उठ्छ।
- अवस्थित alias-आधारित भाषा फोल्डरहरू पहिचान गरिन्छन् र रनको भागका रूपमा क्यानोनिकल भाषा फोल्डर नामहरूमा माइग्रेट गर्न सकिन्छ।
- `run_review` ले हराइरहेका अनुवादित फाइलहरू, हराएको वा अव्यवस्थित अनुवाद मेटाडाटा, बिग्रिएको Markdown frontmatter/code fences, र अवैध अनुवादित नोटबुक JSON मा असफल हुन्छ।
- `run_review` ले डिफल्ट रूपमा हराइरहेका स्थानीय Markdown र छवि लिंक लक्ष्यहरूलाई चेतावनीको रूपमा रिपोर्ट गर्छ।

## आन्तरिक कल पथ

API ले CLI द्वारा प्रयोग गरिने उही कोर कार्यान्वयनलाई सुम्पन्छ:

अनुवाद:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` इन-मेमोरी अनुवादका लागि।
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` स्पष्ट पथ पोस्ट-प्रोसेसिङका लागि।
3. `co_op_translator.api.translation.run_translation` पूर्ण प्रोजेक्ट अोर्केष्ट्रेसनका लागि।
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, नोटबुकहरू, र छविहरूका लागि केन्द्रित प्रोजेक्ट अनुवाद मिक्सिनहरू।
8. Markdown, notebook, टेक्स्ट, र छवि अनुवादकहरू `co_op_translator.core` अन्तर्गत।

समीक्षा:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. नियत जाँचहरू `co_op_translator.review.checks` अन्तर्गत

तलका क्लासहरू अनुरक्षणकर्ताहरूका लागि उपयोगी छन्, तर प्याकेज-स्तर स्थिर API को रूपमा निर्यात गरिएको छैनन्।

| क्लास | मोड्युल | जिम्मेवारी |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | प्रोजेक्ट-स्तर अनुवाद, डाइरेक्टरी व्यवस्थापन, प्रति-भाषा मेटाडाटा सामान्यीकरण, र Markdown, नोटबुक, र छवि अनुवादकहरूमा प्रतिनिधित्व समन्वय गर्छ। |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, नोटबुक, छविहरू, स्टेल पत्ता लगाउने, र अनुवाद मेटाडाटा अपडेटहरूको लागि एसिन्क फाइल प्रोसेसिङ कार्य प्रदर्शन गर्छ। |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown फाइल पढाइहरू, सामग्री अनुवाद, पथ पुन:लेखन, मेटाडाटा, अस्वीकरणहरू, र लेखनहरू समन्वय गर्छ। |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | नोटबुक फाइल पढाइहरू, Markdown-सेल अनुवाद, पथ पुन:लेखन, मेटाडाटा, अस्वीकरणहरू, र लेखनहरू समन्वय गर्छ। |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | स्रोत छवि खोज, छवि अनुवाद, आउटपुट पाथहरू, मेटाडाटा, र लेखनहरू समन्वय गर्छ। |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | अनुवादित Markdown जोडीहरू फेला पार्छ, अनुवाद गुणस्तर मूल्याङ्कन गर्छ, र कम-विश्वसनीयता मरम्मत वर्कफ्लोहरूको लागि विश्वास मेटाडाटा पढ्छ। |
| `ReviewRunner` | `co_op_translator.review.runner` | स्रोत फाइलहरू, लक्ष्य भाषा, र कन्फिगर गरिएको अनुवाद रुटहरूमा निर्धार्य समीक्षा जाँचहरू समन्वय गर्छ। |
| `ReviewTarget` | `co_op_translator.review.targets` | एक स्रोत रुट र सो रुटका लागि समीक्षा गरिने अनुवाद आउटपुट निर्देशिकालाई वर्णन गर्छ। |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | पुराना alias भाषा फोल्डरहरू पत्ता लगाउँछ र क्यानोनिकल BCP 47 फोल्डर माइग्रेशन योजना तयार गर्छ। |
| `Config` | `co_op_translator.config.base_config` | `.env` फाइलहरू लोड गर्छ र आवश्यक LLM र वैकल्पिक Vision प्रदायकहरू कन्फिगर गरिएको छ कि छैन जाँच गर्छ। |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI, वा Anthropic लाई स्वत: पत्ता लगाउँछ, आवश्यक वातावरण भेरिएबलहरू मान्य गर्छ, र प्रदायक कनेक्टिविटी जाँचहरू चलाउँछ। |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision कन्फिगरेसन पत्ता लगाउँछ र छवि अनुवादका लागि कनेक्टिविटी जाँचहरू चलाउँछ। |