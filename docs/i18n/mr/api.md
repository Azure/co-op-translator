# Python API

स्थिर सार्वजनिक Python API `co_op_translator.api` मधून निर्यात केले जाते. बहुतेक एकत्रीकरणे या कार्यप्रवाहांपैकी एक वापरतात:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| वैयक्तिक फायली किंवा दस्तऐवज अनुवादित करा | आपले अनुप्रयोग स्त्रोत सामग्री वाचते, अनुवादासाठी Co-op Translator ला कॉल करते, आणि निकाल कुठे जतन करायचा ते ठरवते. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| होस्ट-एजंट अनुवादासाठी सामग्री तयार करा | आपला MCP होस्ट किंवा अनुप्रयोग मॉडेल भाग अनुवादेल, तर Co-op Translator भागांमध्ये विभागणे आणि पुनर्निर्माण हाताळतो. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| संपूर्ण रेपॉझिटरी अनुवादित करा | आपण Python API ला CLI प्रमाणे वागावे आणि शोधणे, आउटपुट मार्ग, मेटाडेटा, स्वच्छता, आणि लेखन हाताळावे अशी अपेक्षा करता. | `run_translation` |

`core`, `config`, `review`, आणि `utils` अंतर्गत बहुतेक कमी-स्तरीय मॉड्यूल्स या API प्रवेशबिंदूंनी वापरल्या जाणाऱ्या अंमलबजावणी तपशील आहेत.

MCP क्लायंट्स त्याच सार्वजनिक API चा वापर [MCP सर्व्हर](mcp.md) च्या माध्यमातून करतात. Python थेट कॉल करताना ही पृष्ठ वापरा, आणि Co-op Translator एजंट किंवा संपादकास उघडताना MCP मार्गदर्शक वापरा. जर तुम्ही CLI, Python API, आणि MCP यामध्ये निर्णय घेत असाल, तर [आपला कार्यप्रवाह निवडा](workflows.md) पासून सुरू करा.

## प्रथमच API प्रवाह

जर तुम्ही Python कोडमधून Co-op Translator कॉल करत असाल तर येथे प्रारंभ करा:

1. [कॉन्फिगरेशन](configuration.md) मध्ये वर्णन केल्याप्रमाणे एक LLM प्रदाता कॉन्फिगर करा, जोपर्यंत तुम्ही फक्त Markdown किंवा नोटबुक भाग होस्ट-एजंट अनुवादासाठी तयार करत नाही.
2. ठरवा की तुमच्या अनुप्रयोगाचे फाइल I/O नियंत्रणात आहे का.
3. जेव्हा तुमचे अनुप्रयोग वैयक्तिक फायली वाचते आणि लिहिते तेव्हा content APIs वापरा.
4. Co-op Translator ने CLI प्रमाणे रेपॉझिटरी प्रक्रिया करायची असल्यास `run_translation` वापरा.
5. ऑटोमेशनमध्ये निर्धारक तपासण्यांची आवश्यकता असल्यास अनुवादनानंतर `run_review` वापरा.

| Goal | API to start with |
| --- | --- |
| एक Markdown स्ट्रिंग किंवा फाइल अनुवादित करा | `translate_markdown_content` |
| एक नोटबुक पेलोड अनुवादित करा | `translate_notebook_content` |
| एक प्रतिमा अनुवादित करा | `translate_image_content` |
| होस्ट एजंटला Markdown किंवा नोटबुक भाग अनुवाद करू द्या | `start_markdown_agent_translation` किंवा `start_notebook_agent_translation` |
| आउटपुट पथ निवडल्यानंतर अनुवादित दुवे पुनर्लेखन करा | `rewrite_markdown_paths` किंवा `rewrite_notebook_paths` |
| संपूर्ण रेपॉझिटरी अनुवादित करा | `run_translation` |
| अनुवादित आउटपुटचे पुनरावलोकन करा | `run_review` |

## परिस्थिती 1: वैयक्तिक फायली किंवा दस्तऐवज अनुवादित करा

हा कार्यप्रवाह वापरा जेव्हा तुमच्याकडे आधीच फाइल, संपादक बफर, नोटबुक पेलोड, MCP विनंती, किंवा सानुकूल पाइपलाइन इनपुट आहे. तुमच्या कोडकडे फाइल I/O ची जबाबदारी आहे:

1. स्रोत सामग्री वाचा.
2. कंटेंट अनुवाद API कॉल करा.
3. पर्यायीरीत्या पथ पुनर्लेखन API कॉल करा जर अनुवादित सामग्री प्रोजेक्ट अनुवाद फोल्डरमध्ये लिहिली जाणार असेल.
4. निकाल जतन करा किंवा तुमच्या अनुप्रयोगातून परत करा.

कंटेंट अनुवाद API प्रोजेक्ट शोध चालवतात नाहीत, मेटाडेटा लिहितात नाहीत, अस्वीकरण जोडत नाहीत, आणि दुवे स्वयंचलितपणे पुनर्लेखन करत नाहीत.

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

जर अनुवादित Markdown Co-op Translator प्रोजेक्ट लेआउटमध्ये ठेवला जाणार नसेल, तर `rewrite_markdown_paths` वगळा आणि अनुवादित स्ट्रिंग थेट जतन करा.

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

`translate_notebook_content` Markdown सेल्स अनुवादित करते आणि नॉन-Markdown सेल्स जतन करते. पथ पुनर्लेखन फक्त Markdown सेल्सवर लागू होते.

### प्रतिमा फाइल

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

`translate_image_content` स्त्रोत प्रतिमा वाचते आणि रेंडर केलेली `PIL.Image.Image` परत करते. हे अनुवादित प्रतिमा मेटाडेटा लिहिते नाही.

## परिस्थिती 2: संपूर्ण रेपॉझिटरी अनुवादित करा

हा कार्यप्रवाह वापरा जेव्हा तुम्हाला Python API `translate` CLI सारखे वागावे असे वाटते. `run_translation` समर्थित फायली शोधतो, निवडलेले कंटेंट प्रकार अनुवादित करतो, पथ पुनर्लेखन करतो, आउटपुट फायली लिहितो, मेटाडेटा अद्यतनित करतो, आणि क्लीनअप सारखी अनुवाद देखभाल कामे पार पाडतो.

`run_translation` हा प्रोजेक्ट ऑर्केस्ट्रेशनसाठी पसंतीचा प्रवेशबिंदू आहे. `translate_project` तेच वर्तन असलेला अनुकूलतेचा उपनाम म्हणून निर्यात केला आहे.

सध्याच्या रेपॉझिटरीतील Markdown फायली कोरियन आणि जपानीमध्ये अनुवादित करा:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

विशिष्ट प्रोजेक्ट रूटमधून फक्त नोटबुक्स अनुवादित करा:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

फायली न लिहिता अनुवादनाची मात्रा पूर्वावलोकन करा:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

एकत्रीकरणासाठी संरचित प्रगती इव्हेंट्स रेकॉर्ड करा:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # पेलोड आपल्या job-event टेबलमध्ये साठवा किंवा ते आपल्या UI कडे स्ट्रीम करा.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

इव्हेंट्स आवृत्तीसहित स्कीमा `co-op.translation.event.v1` वापरतात. एकत्रीकरणांनी
`type` आणि `stage_key` सारख्या स्थिर फील्ड्सवर अवलंबून असावे, कन्सोलवर दाखवणाऱ्या
मजकूर किंवा `stage_label` वर नव्हे.

एक कॉलमध्ये अनेक कंटेंट रूट्स अनुवादित करा:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

अनुवाद स्पष्ट आउटपुट गटांमध्ये लिहा:

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

जेव्हा प्रत्येक भाषेमध्ये एक नेस्टेड सबडिरेक्टरी असावी तेव्हा प्रति-भाषा प्लेसहोल्डर वापरा:

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

जर `markdown`, `notebook`, किंवा `images` पैकी कोणतीही सेट केलेली नसेल, तर API सर्व समर्थित प्रकार अनुवादित करते: Markdown, नोटबुक्स, आणि प्रतिमा.

### अनुवाद स्थिती प्रदात्याद्वारे मान्य केलेले मानवी संपादन जतन करा

डिफॉल्टनुसार, Co-op Translator त्याचे विद्यमान फाइल-स्तरीय वर्तन ठेवतो: जेव्हा एक
Markdown स्रोत जुनं झाले आहे, संपूर्ण अनुवादित फाइल पुन्हा तयार केली जाते. होस्टेड
एकत्रीकरणे पर्यायीरीत्या `TranslationStateProvider` पास करू शकतात जेणेकरून मानवी
संपादने बदलले नसलेल्या स्रोत ब्लॉक्समध्ये जतन केली जाऊ शकतील.

प्रदाता शेवटचा स्वीकारलेला स्रोत/लक्ष्य जोडी पुरवतो आणि प्रत्येक नवीन
उमेदवार नोंदवतो. स्वीकारणी ही एकत्रीकरणाची जबाबदारी राहते—उदाहरणार्थ,
अनुवाद पुल विनंती मर्ज केल्यानंतर:

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

वैध स्वीकारलेले बेसलाइन असलेल्या Markdown फाइलसाठी, Co-op Translator टॉप-लव्हल Markdown ब्लॉक्सचे संरेखन करते.
न बदललेले स्रोत ब्लॉक्स सध्याचे अनुवादित ब्लॉक्स पुन्हा वापरतात, ज्यात लोकांनी केलेली संपादने समाविष्ट आहेत;
बदललेले किंवा नवीन जोडलेले स्रोत ब्लॉक्स अनुवादासाठी पाठवले जातात;
हटवलेल्या स्रोत ब्लॉक्स काढले जातात. जर संरेखन अस्पष्ट असेल,
लक्षित संरचना बदलली असेल, ब्लॉक अनुवाद अवैध आहे, किंवा कोणतीही बेसलाइन
उपलब्ध नसेल, तर Co-op Translator सुरक्षितपणे विद्यमान पूर्ण-फाइल
अनुवाद पद्धतीकडे परत येतो.

हे API दस्तऐवज अनुवाद स्थिती साठवते, दस्तऐवज-आंतर वाक्यांश किंवा
सेगमेंट अनुवाद स्मृती नाही. सध्या हे Markdown प्रोजेक्ट अनुवादनावर लागू होते.
नोटबुक आणि प्रतिमा वर्तन अपरिवर्तित आहे. `update=True` पास केल्याने
अजूनही संपूर्ण पुन्हा निर्माण विनंती होते.

जर एक किंवा अधिक फायली अनुवादित केल्या जाऊ शकत नसतील, तर `run_translation` एक
`RuntimeError` उभारतो प्रोजेक्ट कार्यप्रवाह संपल्यानंतर, गहाळ आउटपुटसह यशस्वी रन अहवाल देण्याऐवजी.
एकत्रीकरणांनी याला अयशस्वी जॉब म्हणून वागवले पाहिजे आणि
मागील स्वीकारलेली अनुवाद स्थिती राखून ठेवावी.

## अनुवादित आउटपुट पुनरावलोकन

`run_review` LLM किंवा Vision प्रमाणपत्रांशिवाय निर्धारक अनुवाद तपासणी चालविते.

!!! note "Beta"
    `run_review` एक बीटा निर्धारक पुनरावलोकन API आहे. हे मॉडेल प्रदात्यांना कॉल करत नाही किंवा फायली लिहित नाही, परंतु तपासण्या आणि इश्यू स्कीमा विकसित होऊ शकतात.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

फक्त README अनुवादनानंतर, पुनरावलोकनासाठी तितकाच व्याप्ती वापरा:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` फक्त प्रत्येक कॉन्फिगर केलेल्या स्रोत रूटखालील `README.md` चे पुनरावलोकन करते,
सानुकूल `groups` आणि आउटपुट निर्देशिका समाविष्ट करून. इतर दस्तऐवज आणि नेस्टेड
README वगळले जातात. स्त्रोत README नसल्यास `ValueError` उभरतो; अयशस्वी
अनुवाद तपासण्या `RuntimeError` उचलतात.

फक्त बेस रेफच्या विरुद्ध बदललेल्या फायलींचे पुनरावलोकन करा आणि GitHub-शैलीचे आउटपुट प्रिंट करा:

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

## कॉपी-पेस्ट API उदाहरणे

फायली न लिहिता Markdown सामग्री अनुवादित करा:

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

Markdown दुवे अनुवादित करा आणि पुनर्लेखन करा:

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

Python मधून रेपॉझिटरी अनुवादित करा:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

अनेक रूट्स अनुवादित करा:

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

शब्दसूची संज्ञा जतन करा:

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

## सार्वजनिक प्रवेश बिंदू

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

## कंटेंट अनुवाद APIs

कंटेंट अनुवाद API त्या एकत्रीकरणांसाठी आहेत ज्यांकडे आधीपासून मेमरीमध्ये सामग्री आहे, जसे की संपादक विस्तार, MCP टूल, नोटबुक प्रोसेसर, किंवा सानुकूल पाइपलाइन.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | नाही | असिंक. फक्त Markdown सामग्री अनुवादित करते. हे दुवे पुनर्लेखन करत नाही, मेटाडेटा लिहित नाही, किंवा अस्वीकरण जोडत नाही. |
| `translate_notebook_content` | Notebook JSON `str` किंवा `dict` | Notebook JSON `str` | नाही | असिंक. Markdown सेल्स अनुवादित करते आणि नॉन-Markdown सेल्स जतन करते. हे दुवे पुनर्लेखन करत नाही, मेटाडेटा लिहित नाही, किंवा अस्वीकरण जोडत नाही. |
| `translate_image_content` | प्रतिमा मार्ग | `PIL.Image.Image` | फक्त स्रोत प्रतिमा वाचते | सिंक्रोनस. प्रतिमेतील मजकूर काढून अनुवादित करतो, आणि नंतर रेंडर केलेली प्रतिमा परत करतो. हे अनुवादित प्रतिमा मेटाडेटा जतन करत नाही. |

`translate_markdown_content` आणि `translate_notebook_content` त्यांच्या पर्यायांद्वारे एक ऐच्छिक `source_path` स्वीकारतात. मार्ग भाषांतरकाला संदर्भ म्हणून दिला जातो; कॉल करणारे अनुवादानंतर कोणतेही प्रोजेक्ट-विशिष्ट पथ पुनर्लेखन करण्यासाठी जबाबदार राहतात.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

हेच पर्याय शब्दकोश (dictionaries) म्हणून पास केले जाऊ शकतात:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## एजंट-सहाय्यक अनुवाद API

एजंट-सहाय्यक API Co-op Translator मधून कॉन्फिगर केलेल्या LLM प्रदात्याला कॉल करत नाहीत. ते होस्ट एजंटसाठी Markdown किंवा नोटबुक भाग तयार करतात, नंतर अनुवादित भागांमधून अंतिम सामग्री पुन्हा तयार करतात.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | चंक्स, प्रॉम्प्ट्स, आणि पुनर्निर्माण स्थितीसह स्व-समाविष्ट Markdown जॉब परत करा. |
| `finish_markdown_agent_translation` | जॉब आणि होस्ट-एजंटने अनुवादित चंक्स वापरून Markdown पुनर्निर्माण करा. |
| `start_notebook_agent_translation` | होस्ट-एजंट अनुवादासाठी Markdown-सेल चंक्ससह नोटबुक जॉब परत करा. |
| `finish_notebook_agent_translation` | कोड सेल्स, आउटपुट आणि मेटाडेटा जपून ठेवताना नोटबुक JSON पुनर्निर्माण करा. |

हा कार्यप्रवाह मुख्यतः MCP होस्टसाठी आहे. जर तुम्हाला उत्पादन रेपॉझिटरी अनुवाद हवा असेल आणि Co-op Translator प्रदाता कॉल्स व्यवस्थापित करेल असे हवे, तर `translate_markdown_content`, `translate_notebook_content`, किंवा `run_translation` वापरा.

## पथ पुनर्लेखन API

पथ पुनर्लेखन API कोणताही अनुवाद करत नाहीत. कॉल करणाऱ्याला स्रोत पथ, अनुवादित लक्ष्य पथ, आणि प्रोजेक्ट लेआउट माहित झाल्यानंतर ते दुवे आणि फ्रंटमॅटर पथ अद्यतनित करतात.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body आणि फ्रंटमॅटर | अनुवादित लक्ष्यासाठी Markdown दुवे आणि समर्थित फ्रंटमॅटर पथ फील्ड्स पुनर्लेखन करते. |
| `rewrite_notebook_paths` | नोटबुक JSON मधील Markdown सेल्स | प्रत्येक Markdown सेलवर Markdown पथ पुनर्लेखन लागू करते आणि नॉन-Markdown सेल्स अपरिवर्तित ठेवते. |

`policy` आर्ग्युमेंट हे खालील फील्ड्स असलेल्या शब्दकोश असू शकते:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | होय | लक्ष्य भाषा कोड, जसे की `"ko"` किंवा `"pt-BR"`. |
| `root_dir` | नाही | स्रोत प्रोजेक्ट रूट. डीफॉल्ट `"."`. |
| `translations_dir` | नाही | टेक्स्ट अनुवाद आउटपुट निर्देशिका. डीफॉल्ट `root_dir` अंतर्गत `translations`. |
| `translated_images_dir` | नाही | अनुवादित प्रतिमा आउटपुट निर्देशिका. डीफॉल्ट `root_dir` अंतर्गत `translated_images`. |
| `translation_types` | नाही | सक्षम केलेले अनुवाद प्रकार. डीफॉल्ट म्हणजे Markdown, नोटबुक, आणि प्रतिमा. |
| `lang_subdir` | नाही | प्रत्येक भाषा फोल्डरखाली ऐच्छिक उपनिर्देशिका. |

## प्रोजेक्ट अनुवाद पॅरामीटर्स

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | आवश्यक | स्पेस-वेगळे लक्ष्य भाषा कोड जसे `"ko ja fr"`, किंवा `"all"`. उपनाम कोड्स मानक BCP 47 मूल्यांमध्ये सामान्यीकृत केले जातात. |
| `root_dir` | `str` | `"."` | एकल अनुवाद लक्ष्यासाठी प्रोजेक्ट रूट. `root_dirs` किंवा `groups` दिले असताना उपेक्षित. |
| `update` | `bool` | `False` | निवडलेल्या भाषांसाठी विद्यमान अनुवाद हटवा आणि पुन्हा तयार करा. |
| `images` | `bool` | `False` | प्रतिमा अनुवाद समाविष्ट करा. यासाठी Azure AI Vision कॉन्फिगरेशन आवश्यक आहे. |
| `markdown` | `bool` | `False` | Markdown अनुवाद समाविष्ट करा. |
| `notebook` | `bool` | `False` | Jupyter नोटबुक अनुवाद समाविष्ट करा. |
| `debug` | `bool` | `False` | डिबग लॉगिंग सक्षम करा. |
| `save_logs` | `bool` | `False` | रूट `logs/` निर्देशिकेत DEBUG-स्तराच्या लॉग फाइल्स जतन करा. |
| `yes` | `bool` | `True` | प्रोग्रामॅटिक आणि CI वापरासाठी प्रॉम्प्ट्स स्वयंचलितपणे पुष्टी करा. |
| `add_disclaimer` | `bool` | `False` | अनुवादित Markdown आणि नोटबुकमध्ये मशीन अनुवादाचे अस्वीकरण जोडा. |
| `translations_dir` | `str \| None` | `None` | सानुकूल मजकूर अनुवाद आउटपुट निर्देशिका. सापेक्ष मार्ग प्रत्येक मूळ निर्देशिकेच्या संदर्भात निराकरण केले जातील. |
| `image_dir` | `str \| None` | `None` | सानुकूल अनुवादित प्रतिमा आउटपुट निर्देशिका. सापेक्ष मार्ग प्रत्येक मूळ निर्देशिकेच्या संदर्भात निराकरण केले जातील. |
| `root_dirs` | `Iterable[str] \| None` | `None` | समान आउटपुट सेटिंग्ज सामायिक करणाऱ्या अनेक मूळ निर्देशिका. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | स्पष्ट `(root_dir, translations_dir)` जोड्या. `root_dirs` वर प्राधान्य घ्यावे. |
| `repo_url` | `str \| None` | `None` | README मध्ये भाषा सारणी मार्गदर्शन रेंडर करताना वापरला जाणारा रेपॉझिटरी URL. |
| `glossaries` | `Iterable[str] \| None` | `None` | अनुवादादरम्यान जतन करण्यासाठी शब्दसंग्रहातील शब्द. प्रतिकृती आणि रिकामे शब्द सामान्यीकृत केले जातात. |
| `dry_run` | `bool` | `False` | फायली लिहित न करता अनुवादाच्या प्रमाणाचा अंदाज व स्थलांतराचे पूर्वावलोकन करा. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | क्रमिक Markdown अद्यतनांसाठी ऐच्छिक स्वीकारलेले-बेसलाइन आणि उमेदवार टिकवणी अ‍ॅडॅप्टर. ते वगळल्यास विद्यमान पूर्ण-फाइल वर्तन कायम राहते. |

## पुनरावलोकन पॅरामीटर्स

`run_review` उद्देशाने शक्य तितक्या ठिकाणी `run_translation` च्या सिग्नेचरचे प्रतिबिंब करते जेणेकरून ऑटोमेशन अनुवाद आणि पुनरावलोकन वर्कफ्लो दरम्यान कमीतकमी शाखा बदलांसह स्विच करू शकेल.

| पॅरामीटर | प्रकार | डीफॉल्ट | उद्देश |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | पुनरावलोकन करण्यासाठी लक्ष्य भाषा फोल्डर्स. स्पेस-वेगळ्या स्ट्रिंग्स आणि iterable स्वीकारले जातात. `"all"` सगळ्या आढळलेल्या भाषांचे पुनरावलोकन करते. |
| `root_dir` | `str` | `"."` | एकल पुनरावलोकन लक्ष्यासाठी प्रकल्प मूळ. `root_dirs` किंवा `groups` पुरवले असतील तर हे दुर्लक्षित केले जाते. |
| `markdown` | `bool` | `False` | Markdown आणि MDX स्रोत फाइल्स समाविष्ट करा. |
| `notebook` | `bool` | `False` | Jupyter नोटबुक स्रोत फाइल्स समाविष्ट करा. |
| `images` | `bool` | `False` | अनुवाद पर्यायांसह सुसंगतीसाठी राखीव. प्रतिमांवरील लिंक संदर्भ Markdown मधून तपासले जातात. |
| `translations_dir` | `str \| None` | `None` | सानुकूल मजकूर अनुवाद आउटपुट निर्देशिका. सापेक्ष मार्ग प्रत्येक मूळ निर्देशिकेच्या संदर्भात निराकरण केले जातील. |
| `root_dirs` | `Iterable[str] \| None` | `None` | समान आउटपुट सेटिंग्ज सामायिक करणाऱ्या अनेक मूळ निर्देशिका. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | स्पष्ट `(root_dir, translations_dir)` जोड्या. `root_dirs` वर प्राधान्य घ्यावे. |
| `changed_from` | `str \| None` | `None` | पुनरावलोकन फक्त बदललेल्या स्रोत फाइल्सपुरते मर्यादित करण्यासाठी वापरले जाणारे Git ref. |
| `readme_only` | `bool` | `False` | प्रत्येक स्रोत मूळाखालील फक्त `README.md` चे पुनरावलोकन करा. स्रोत README अनुपस्थित असल्यास `ValueError` उभारले जाते. |
| `output_format` | `str` | `"text"` | पुनरावलोकन आउटपुट स्वरूप. समर्थित मूल्ये `"text"` आणि `"github"` आहेत. |
| `fail_on_warnings` | `bool` | `False` | चेतावण्या त्रुटींसह अपयश म्हणून वागविल्या जातात. |
| `debug` | `bool` | `False` | डिबग लॉगिंग सक्षम करा. |
| `save_logs` | `bool` | `False` | रूट `logs/` निर्देशिकेखाली DEBUG-स्तरीय लॉग फाइल्स जतन करा. |

जर `markdown`, `notebook`, किंवा `images` पैकी कोणतेही सेट केलेले नसेल तर API Markdown, नोटबुक आणि लागू असल्यास प्रतिमा लिंक संदर्भ पुनरावलोकन करते. पुनरावलोकन LLM प्रदात्याला कॉल करत नाही आणि API कींची आवश्यकता नाही.

## कॉन्फिगरेशन आवश्यकता

प्रदाता-आधारित अनुवाद API ला अनुवाद करण्यापूर्वी प्रदाता कॉन्फिगरेशनची आवश्यकता असते:

- Markdown आणि नोटबुक अनुवादासाठी LLM प्रदात्याची आवश्यकता आहे. Azure OpenAI, OpenAI, किंवा Anthropic कॉन्फिगर करा.
- प्रतिमा अनुवादासाठी LLM प्रदात्यासोबत Azure AI Vision आवश्यक आहे.
- `run_translation` प्रकल्प अनुवाद सुरू होण्यापूर्वी हलके कनेक्टिव्हिटी तपासणी चालवते.
- एजंट-सहाय्यक `start_*_agent_translation` आणि `finish_*_agent_translation` APIs Co-op Translator LLM प्रदात्यांना कॉल करत नाहीत. होस्ट अनुप्रयोग किंवा MCP एजंट तयार केलेले चंक्स अनुवादित करतो.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, आणि `run_review` निश्चित आहेत आणि प्रदाता क्रेडेन्शियल्सची आवश्यकता नाही.

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

`ANTHROPIC_BASE_URL` आणि `ANTHROPIC_MAX_TOKENS` ऐच्छिक आहेत. Co-op Translator 0.22.0 पासून सर्व प्रदात्यांसाठी Microsoft Agent Framework हा डीफॉल्ट मॉडेल क्लायंट आहे. Semantic Kernel अजूनही तात्पुरते `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` ने निवडता येते, परंतु असे केल्यास एक अप्रचलिततेची चेतावणी दिली जाते; टप्प्याटप्प्याने काढून टाकण्याच्या योजनेसाठी [configuration](configuration.md#model-client-backend) पहा.

प्रतिमा अनुवादासाठी आवश्यक Azure AI Vision वेरिएबल्स:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` निश्चित आहे आणि LLM किंवा Azure AI Vision कॉन्फिगरेशनची आवश्यकता नाही.

## वर्तन नोट्स

- कंटेंट अनुवाद API प्रोजेक्ट पाथ पुनर्लेखनापासून अनुवाद वेगळे ठेवतात. अनुवादित कंटेंटसाठी प्रकल्प-सापेक्ष दुवे लक्ष्य स्थानानुसार समायोजित करण्याची गरज असल्यास `rewrite_markdown_paths` किंवा `rewrite_notebook_paths` स्पष्टपणे कॉल करा.
- प्रकल्प ऑर्केस्ट्रेशन API कंटेंट अनुवादाभोवती प्रकल्प वर्तन जोडतात, ज्यात फाइल शोध, लेखन, पाथ पुनर्लेखन, मेटाडेटा, स्वच्छता, आणि ऐच्छिक अस्वीकरण समाविष्ट आहेत.
- `run_translation` CLI द्वारे वापरल्या जाणाऱ्या त्याच Rich-बॅक्ड रिपोर्टरद्वारे प्रगती आणि अंदाज सारांश मुद्रित करते. नॉन-इंटरएक्टिव्ह आउटपुट सामान्य मजकूरकडे परत जाते.
- `dry_run=True` आभासी README अद्यतनांचा वापर करून अंदाज गणना करते, परंतु README किंवा अनुवाद फाइल्स लिहीत नाही.
- `groups` क्रमाने प्रक्रिया केल्या जातात. काम सुरू होण्यापूर्वी एक एकत्रित अंदाज मुद्रित केला जातो.
- जेव्हा प्रतिमा अनुवाद निवडले जाते, तेव्हा Vision कॉन्फिगरेशन अनुपस्थित असल्यास अनुवाद सुरू होण्यापूर्वी त्रुटी उद्भवते.
- विद्यमान उपनाम-आधारित भाषा फोल्डर्स ओळखले जातात आणि रनच्या भाग म्हणून कॅनॉनिकल भाषा फोल्डर नावे मध्ये स्थलांतर केले जाऊ शकते.
- `run_review` गहाळ अनुवादित फाईल्स, गहाळ किंवा जुने अनुवाद मेटाडेटा, चुकीचे Markdown फ्रंटमॅटर/कोड फेन्स, आणि अवैध अनुवादित नोटबुक JSON वर अयशस्वी होते.
- `run_review` स्थानिक Markdown आणि प्रतिमा लिंक लक्ष्य गहाळ असल्यास ते सामान्यतः चेतावणी म्हणून नोंदवते.

## अंतर्गत कॉल पथ

API CLI द्वारे वापरल्या जाणार्‍या त्याच कोर अंमलबजावणीकडे सौंपते:

अनुवाद:

1. मेमरीमध्ये अनुवादासाठी `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, किंवा `translate_image_content`.
2. स्पष्ट पाथ पोस्ट-प्रोसेसिंगसाठी `co_op_translator.api.translation.rewrite_markdown_paths` किंवा `rewrite_notebook_paths`.
3. पूर्ण प्रकल्प ऑर्केस्ट्रेशनसाठी `co_op_translator.api.translation.run_translation`.
4. `co_op_translator.config.Config`, `LLMConfig`, आणि `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, नोटबुक, आणि प्रतिमांसाठी लक्ष केंद्रित प्रकल्प अनुवाद मिक्सिन्स.
8. `co_op_translator.core` अंतर्गत Markdown, नोटबुक, टेक्स्ट, आणि प्रतिमा translators.

पुनरावलोकन:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` अंतर्गत निश्चित तपासण्या

खालील वर्ग मेंटेनर्ससाठी उपयुक्त आहेत, परंतु पॅकेज-स्तरीय स्थिर API म्हणून निर्यात केलेले नाहीत.

| वर्ग | मॉड्यूल | जबाबदारी |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | प्रकल्प-स्तरीय अनुवाद समन्वयित करते, निर्देशिका व्यवस्थापन, प्रति-भाषा मेटाडेटा सामान्यीकरण, आणि Markdown, नोटबुक, व प्रतिमा translators कडे प्रतिनिधीकरण. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, नोटबुक, प्रतिमा, जुन्या शोध, आणि अनुवाद मेटाडेटा अद्यतनांसाठी async फाइल प्रोसेसिंग कार्य करते. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown फाइल वाचन, कंटेंट अनुवाद, पाथ पुनर्लेखन, मेटाडेटा, अस्वीकरण, आणि लेखन यांचे ऑर्केस्ट्रेशन करते. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | नोटबुक फाइल वाचन, Markdown-सेल अनुवाद, पाथ पुनर्लेखन, मेटाडेटा, अस्वीकरण, आणि लेखन यांचे ऑर्केस्ट्रेशन करते. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | स्रोत प्रतिमा शोध, प्रतिमा अनुवाद, आउटपुट पाथ, मेटाडेटा, आणि लेखन यांचे ऑर्केस्ट्रेशन करते. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | अनुवादित Markdown जोड्या शोधते, अनुवाद गुणवत्ता मूल्यांकन करते, आणि कमी-विश्वास दुरुस्ती वर्कफ्लोसाठी विश्वास मेटाडेटा वाचते. |
| `ReviewRunner` | `co_op_translator.review.runner` | स्रोत फाइल्स, लक्ष्य भाषा, आणि कॉन्फिगर केलेल्या अनुवाद रूट्स दरम्यान निश्चित पुनरावलोकन तपासण्यांचे समन्वय करते. |
| `ReviewTarget` | `co_op_translator.review.targets` | एखाद्या स्रोत मूळ आणि त्या मूळासाठी पुनरावलोकन केलेल्या अनुवाद आउटपुट निर्देशिकेचे वर्णन करते. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | पुरातन उपनाम भाषा फोल्डर्स ओळखते आणि कॅनॉनिकल BCP 47 फोल्डर स्थलांतर योजना तयार करते. |
| `Config` | `co_op_translator.config.base_config` | `.env` फाइल्स लोड करते आणि आवश्यक LLM व ऐच्छिक Vision प्रदाते कॉन्फिगर केले आहेत का ते तपासते. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI, किंवा Anthropic स्वयंचलितपणे ओळखते, आवश्यक वातावरण वेरिएबल्स वैध करते, आणि प्रदाता कनेक्टिव्हिटी तपासण्या चालवते. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | प्रतिमा अनुवादासाठी Azure AI Vision कॉन्फिगरेशन ओळखते आणि कनेक्टिव्हिटी तपासण्या चालवते. |