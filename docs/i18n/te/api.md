# Python API

స ثابتమైన పబ్లిక్ Python API `co_op_translator.api` నుండి ఎక్స్పోర్ట్ చేయబడింది. ఎక్కువ ఇంటిగ్రేషన్లు ఈ వర్క్ఫ్లోలలో ఒకటిని ఉపయోగిస్తాయి:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | మీ అప్లికేషన్ మూల కంటెంట్ చదివి, అనువాదానికి Co-op Translator‌ను పిలిచే సమయంలో మరియు ఫలితాన్ని ఎక్కడ సేవ్ చేయాలో నిర్ణయించుకునే సమయంలో. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | మీ MCP హోస్ట్ లేదా అప్లికేషన్ మోడల్ భాగాలుగా అనువాదం చేస్తుంది, Co-op Translator చెంకింగ్ మరియు పునర్విన్యాసాన్ని నిర్వహిస్తుంది. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | మీరు Python API CLI వంటిగా ప‌నిచేయి మరియు డిస్కవరీ, అవుట్‌పుట్ పాథ్లు, మెటాడేటా, క్లీన్‌అప్ మరియు రాయడం నిర్వహించాలనుకుంటే. | `run_translation` |

`core`, `config`, `review`, మరియు `utils` కిందని күп దిగువ-స్థాయి మాడ్యూల్స్ ఈ API ప్రవేశ బిందూళ్ ద్వారా ఉపయోగించే అమలు వివరాలుగా ఉండును.

MCP కస్టమర్లు [MCP Server](mcp.md) ద్వారా అదే పబ్లిక్ API ను ఉపయోగిస్తారు. Python కేరాఫోన్ పేజీని నేరుగా పిలిచేటప్పుడు ఈ పేజీని ఉపయోగించండి, మరియు Co-op Translator‌ను ఏజెంట్ లేదా ఎడిటర్‌కు ప్రదర్శిస్తేప్పుడు MCP గైడ్‌ను ఉపయోగించండి. CLI, Python API, మరియు MCP మధ్య నిర్ణయించుకుంటున్నట్లయితే, [Choose Your Workflow](workflows.md) తో ప్రారంభించండి.

## First-Time API Flow

Python కోడ్ నుండి Co-op Translator ను పిలుస్తున్నట్లయితే ఇక్కడ ప్రారంభించండి:

1. [Configuration](configuration.md)లో వివరించబడినట్లుగా ఒక LLM ప్రొవైడర్‌ను కాన్ఫిగర్ చేయండి, లేకపోతే మీరు Markdown లేదా నోట్‌బుక్ చెంక్స్ మాత్రమే హోస్ట్-ఏజెంట్ అనువాదానికి సిద్ధం చేస్తున్నట్లయితే ఇది అవసరం లేదు.
2. మీ అప్లికేషన్ ఫైల్ I/O ను నిర్వహిస్తుందా కాదా నిర్ణయించుకోండి.
3. మీ అప్లికేషన్ వ్యక్తిగత ఫైళ్లను చదవడం మరియు రాయడం చేస్తే content APIs ఉపయోగించండి.
4. Co-op Translator CLI వలా ఒక రెపోని ప్రాసెస్ చేయాలి అనుకుంటే `run_translation` ఉపయోగించండి.
5. ఆటోమేషన్‌లో నిర్దిష్ట పరికలనలను అవసరమైతే అనువాదం తర్వాత `run_review` ఉపయోగించండి.

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

ఈ వర్క్ఫ్లోను ఉపయోగించండి మీరు ఇప్పటికే ఒక ఫైల్, ఎడిటర్ బఫర్, నోట్‌బుక్ పేలోడ్, MCP రిక్వెస్ట్, లేదా కస్టమ్ పైప్‌లైన్ ఇన్పుట్ కలిగి ఉన్నప్పుడు. మీ కోడ్ ఫైల్ I/O ని నిర్వహిస్తుంది:

1. మూల కంటెంట్‌ను చదవండి.
2. కంటెంట్ అనువాద API ని పిలవండి.
3. అనువాదిత కంటెంట్ ప్రాజెక్ట్ ట్రాన్స్‌లేషన్ ఫోల్డర్‌లో రాయబడే ఉద్దేశ్యమైతే కావలసినట్లయితే పాథ్ రిరైటింగ్ API పిలవండి.
4. మీ అప్లికేషన్ నుండి ఫలితాన్ని సేవ్ లేదా రిటర్న్ చేయండి.

కంటెంట్ అనువాద APIలు ప్రాజెక్ట్ డిస్కవరీను నడపవు, మెటాడేటాను రాయవు, డిస్క్లెయిమర్లు జోడించవు, మరియు లింక్‌లను స్వయంచాలకంగా రిరైట్ చేయవు.

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

అనువదించిన Markdown ఒక Co-op Translator ప్రాజెక్ట్ లేఅవుట్లో ఉండకపోతే, `rewrite_markdown_paths` ను ఉంచకుంటే అనువదించిన స్ట్రింగ్‌ను నేరుగా సేవ్ చేయండి.

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

`translate_notebook_content` Markdown సెల్స్‌ను అనువదించి non-Markdown సెల్స్‌ను నిలుపుకుంటుంది. పాథ్ రిరైటు మాత్రమే Markdown సెల్స్‌కు వర్తిస్తుంది.

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

`translate_image_content` మూల చిత్రం చదివి ఒక రేండర్డ్ `PIL.Image.Image` ను రిటర్న్ చేస్తుంది. ఇది అనువదించిన చిత్ర మెటాడేటాను రాయదు.

## Scenario 2: Translate an Entire Repository

ఈ వర్క్ఫ్లోను ఉపయోగించండి మీరు Python API ని `translate` CLI వంటిగా పని చేస్తుందని కోరుకుంటే. `run_translation` సపోర్ట్ చేసిన ఫైళ్లను కనుగొంటుంది, ఎంపిక చేయబడిన కంటెంట్ టైల్స్‌ను అనువదిస్తుంది, పాథ్‌లను రిరైట్ చేస్తుంది, అవుట్‌పుట్ ఫైళ్లను రాస్తుంది, మెటాడేటాను నవీకరిస్తుంది, మరియు క్లీన్‌ప్ వంటి అనువాద నిర్వహణ పనులను నిర్వహిస్తుంది.

`run_translation` ప్రాజెక్ట్ ఒర్కస్ట్రేషన్ ప్రవేశ బిందువు కోసం మెరుగ్గా సిఫార్సు చేయబడుతుంది. `translate_project` అదే ప్రవర్తనతో అనుకూలత అలియాస్‌గా ఎక్స్‌పోర్ట్ చేయబడింది.

ప్రాథమిక రిపోజిటరీలో Markdown ఫైళ్లను కొరియన్ మరియు జపనీస్‌లో అనువదించండి:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

కేవలం ఒక నిర్దిష్ట ప్రాజెక్ట్ రూట్ నుండి నోట్‌బుక్స్ మాత్రమే అనువదించండి:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ఫైళ్లు రాయకుండా అనువాద పరిమాణాన్ని ప్రివ్యూ చేయండి:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ఒక కాల్‌లో బహుళ కంటెంట్ రూట్స్‌ను అనువదించండి:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

అనువాదాలను స్పష్టమైన అవుట్‌పుట్ గ్రూపుల్లో రాయండి:

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

ప్రతి భాషలో ఒక nested ఉపదర్శిలో ఉండాలనుకుంటే ప్రతి-భాష ప్లేస్‌హోల్డర్ ఉపయోగించండి:

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

`markdown`, `notebook`, లేదా `images` లో ఏదీ సెట్ చేయబడకపోతే, API అన్ని సపోర్ట్ చేసిన రకాలన్నీ అనువదిస్తుంది: Markdown, notebooks, మరియు images.

## Review Translated Output

`run_review` LLM లేదా Vision క్రెడెన్షియల్స్ లేకుండా నిర్దిష్ట అనువాద పరీక్షలను నడిపిస్తుంది.

!!! note "Beta"
    `run_review` ఒక బీటా నిర్దిష్ట రివ్యూ API. ఇది మోడల్ ప్రొవైడర్లను పిలవదు లేదా ఫైళ్లను రాయదు, కాని చెక్‌లు మరియు ఇష్యూ స్కీమాలు మారవచ్చు.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

బేస్ రిఫ్‌పై మార్చబడిన ఫైళ్లను మాత్రమే రివ్యూ చేయండి మరియు GitHub-రూపింతః ఔట్‌పుట్ ముద్రించండి:

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

ఫైల్ రాయకుండానే Markdown కంటెంట్‌ను అనువదించండి:

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

Markdown లింక్‌లను అనువదించి రిరైట్ చేయండి:

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

Python నుండి ఒక రిపోజిటరీను అనువదించండి:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

బహుళ రూట్స్‌ను అనువదించండి:

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

గ్లోసరీ పదాలను పరిమితి చేయండి:

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

కంటెంట్ అనువాద APIలు ఇన్-మెమరీలో ఇప్పటికే కంటెంట్ ఉన్న ఇంటిగ్రేషన్ల కోసం ఉద్దేశించబడ్డాయి, ఉదాహరణకు ఒక ఎడిటర్ ఎక్స్‌టెన్షన్, MCP టూల్, నోట్‌బుక్ ప్రాసెసర్, లేదా కస్టమ్ పైప్‌లైన్.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Markdown కంటెంట్‌ను మాత్రమే అనువదిస్తుంది. ఇది లింక్‌లను రిరైట్ చేయదు, మెటాడేటాను రాయదు, లేదా డిస్క్లెయిమర్లు జోడించదు. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown సెల్స్‌ను అనువదించి non-Markdown సెల్స్‌ను నిలిపి ఉంచుతుంది. ఇది లింక్‌లను రిరైట్ చేయదు, మెటాడేటాను రాయదు, లేదా డిస్క్లెయిమర్లు జోడించదు. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. చిత్రం నుండి టెక్స్ట్‌ను ఎక్స్‌ทรాక్ట్ చేసి అనువదించి, తర్వాత ఒక రేండర్డ్ చిత్రం రిటర్న్ చేస్తుంది. ఇది అనువదించిన చిత్రం మెటాడేటాను సేవ్ చేయదు. |

`translate_markdown_content` మరియు `translate_notebook_content` ఐచ్ఛిక `source_path` ను వారి ఆప్షన్స్ ద్వారా అంగీకరిస్తాయి. పాథ్ అనువాదకునికి కాన్టెక్స్ట్‌గా పాస్ చేయబడుతుంది; అనువాదం తర్వాత ప్రాజెక్ట్-స్పెసిఫిక్ పాథ్ రిరైటింగ్ కోసం కాలర్లే బాధ్యత వహిస్తారు.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

అనే క్రియల‌ను డిక్షనరీస్‌గా కూడా పాస్ చేయవచ్చు:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted APIలు Co-op Translator నుండి Azure OpenAI లేదా OpenAI ను పిలవవు. ఇవి Markdown లేదా నోట్‌బుక్ చెంక్స్‌ను హోస్ట్ ఏజెంట్ అనువదించడానికి సిద్ధం చేస్తాయి, తర్వాత అనువదించిన చెంక్స్ నుంచి తుది కంటెంట్‌ను పునర్‌నిర్మాణం చేస్తాయి.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | చెంక్స్, ప్రాంప్ట్‌లు, మరియు పునర్నిర్మాణ స్థితి ఉన్న సుస్థిర Markdown జాబ్ ని రిటర్న్ చేయండి. |
| `finish_markdown_agent_translation` | ఒక జాబ్ మరియు హోస్ట్-ఏజెంట్ అనువదించిన చెంక్స్ నుండి Markdown ను పునర్నిర్మాణం చేయండి. |
| `start_notebook_agent_translation` | హోస్ట్-ఏజెంట్ అనువాదానికి Markdown-సెల్ చెంక్స్ ఉన్న ఒక నోట్‌బుక్ జాబ్ ను రిటర్న్ చేయండి. |
| `finish_notebook_agent_translation` | కోడ్ సెల్స్, అవుట్‌పుట్స్, మరియు మెటాడేటాను నిలిపి ఉంచుతూ నోట్‌బుక్ JSON ను పునర్నిర్మాణం చేయండి. |

ఈ వర్క్ఫ్లో ప్రాథమికంగా MCP హోస్ట్‌ల కోసం ఉద్దేశించబడింది. మీరు ప్రొడక్షన్ రిపోజిటరీ అనువాదం కావాల్సిన సమయంలో Co-op Translator ప్రొవైడర్ కాల్‌లను నిర్వహించేది కావాలి అంటే `translate_markdown_content`, `translate_notebook_content`, లేదా `run_translation` ఉపయోగించండి.

## Path Rewriting APIs

పాథ్ రిరైటింగ్ APIలు అనువాదం చేయవు. ఇవి కాలర్లు మూల పాథ్, అనువదించిన లక్ష్య పాథ్, మరియు ప్రాజెక్ట్ లేఅవుట్ తెలుసుకున్న తర్వాత లింక్‌లు మరియు ఫ్రంట్‌మేటర్ పాథ్‌లను అప్‌డేట్ చేస్తాయి.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | అనువదించిన లక్ష్యానికి Markdown లింక్‌లు మరియు సపోర్ట్ చేసిన frontmatter పాథ్ ఫీల్డ్స్‌ను రిరైట్ చేస్తుంది. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | ప్రతి Markdown సెల్‌కు Markdown పాథ్ రిరైటింగ్‌ను వర్తింపజేస్తుంది మరియు non-Markdown సెల్స్‌ను మార్చదు. |

`policy` ఆర్గ్యుమెంట్ ఈ ఫీల్డ్స్ ఉన్న డిక్షనరీ కావచ్చు:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | లక్ష్య భాషా కోడ్, ఉదా. `"ko"` లేదా `"pt-BR"`. |
| `root_dir` | No | మూల ప్రాజెక్ట్ రూట్. డిఫాల్ట్ `"."`. |
| `translations_dir` | No | టెక్స్ట్ అనువాద అవుట్‌పుట్ డైరెక్టరీ. డిఫాల్ట్ `translations` under `root_dir`. |
| `translated_images_dir` | No | అనువదించిన చిత్రాల అవుట్‌పుట్ డైరెక్టరీ. డిఫాల్ట్ `translated_images` under `root_dir`. |
| `translation_types` | No | ఎనేబుల్ చేసిన అనువాద రకాలు. డిఫాల్ట్ Markdown, notebooks, మరియు images. |
| `lang_subdir` | No | ప్రతి భాష ఫోల్డర్ లోని ఐచ్ఛిక ఉపడైరెక్టరీ. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | స్పేస్-విచ్ఛిన్నమైన లక్ష్య భాషా కోడ్లు, ఉదా `"ko ja fr"`, లేదా `"all"`. అలియాస్ కోడ్లు సాధారణీకరించి canonical BCP 47 విలువలకు మార్చబడతాయి. |
| `root_dir` | `str` | `"."` | ఒక్క లక్ష్యానికి ప్రాజెక్ట్ రూట్. `root_dirs` లేదా `groups` సరఫరా చేయబడినప్పుడు ఇగ్నోర్ చేయబడుతుంది. |
| `update` | `bool` | `False` | ఎంపిక చేసిన భాషల కోసం ఉన్న అనువాదాలను డిలీట్ చేసి మళ్లీ సృష్టిస్తుంది. |
| `images` | `bool` | `False` | చిత్రం అనువాదాన్ని కలిపి. ఇది Azure AI Vision కాన్ఫిగరేషన్ అవసరం. |
| `markdown` | `bool` | `False` | Markdown అనువాదాన్ని కలపండి. |
| `notebook` | `bool` | `False` | Jupyter నోట్‌బుక్ అనువాదాన్ని కలపండి. |
| `debug` | `bool` | `False` | డీబగ్ లాగింగ్‌ను ఎనేబుల్ చేయండి. |
| `save_logs` | `bool` | `False` | రూట్ `logs/` డైరక్టరీ క్రింద DEBUG-స్థాయి లాగ్ ఫైళ్లు సేవ్ చేయండి. |
| `yes` | `bool` | `True` | ప్రోగ్రామాటిక్ మరియు CI ఉపయోగానికి ప్రాంప్ట్స్ ఆటో-కన్ఫర్మ్ చేయండి. |
| `add_disclaimer` | `bool` | `False` | అనువదించిన Markdown మరియు నోట్‌బుక్స్‌కు మెషిన్ అనువాద డిస్క్లెయిమర్‌లు జోడించండి. |
| `translations_dir` | `str \| None` | `None` | కస్టమ్ టెక్స్ట్ అనువాద అవుట్‌పుట్ డైరెక్టరీ. రిలేటివ్ పాథ్స్ ప్రతి రూట్ ప‌రంగా రిసాల్వ్ అవుతాయి. |
| `image_dir` | `str \| None` | `None` | కస్టమ్ అనువదించిన చిత్రం అవుట్‌పుట్ డైరెక్టరీ. రిలేటివ్ పాథ్స్ ప్రతి రూట్ ప‌రంగా రిసాల్వ్ అవుతాయి. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ఒకే అవుట్‌పుట్ సెట్టింగ్స్‌ను పంచుకునే బహుళ రూట్స్. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | స్పష్టమైన `(root_dir, translations_dir)` జోడులు. `root_dirs` కంటే ప్రాధాన్యత కలిగి ఉంటుంది. |
| `repo_url` | `str \| None` | `None` | README భాష పట్టిక మార్గదర్శకాన్ని రేండర్ చేయడానికి ఉపయోగించే రిపోజిటరీ URL. |
| `glossaries` | `Iterable[str] \| None` | `None` | అనువాద సమయంలో సంరక్షించవలసిన గ్లోసరీ పదాలు. డూప్లికేట్స్ మరియు ఖాళీ పదాలు సాధారణీకరించబడతాయి. |
| `dry_run` | `bool` | `False` | ఫైళ్లు రాస్తుండకుండానే అనువాద పరిమాణాన్ని అంచనా వేయండి మరియు మైగ్రేషన్ ప్రవర్తనను ప్రివ్యూ చేయండి. |

## Review Parameters

`run_review` ఉద్దేశ్యంగా `run_translation` సిగ్నేచర్‌ను అదే రీతిలో మిర్రర్ చేయడానికి రూపొందించబడింది ताकि ఆటోమేషన్ అనువాద మరియు రివ్యూ వర్క్‌ఫ్లోల మధ్య తక్కువ బ్రాంచింగ్‌తో మారోచ్చు.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | రివ్యూ చేయడానికి లక్ష్య భాష ఫోల్డర్లు. స్పేస్-విచ్ఛిన్న స్ట్రింగ్స్ మరియు ఇటరబుల్స్ స్వీకరించబడతాయి. `"all"` ప్రతి కనుగొన్న అనువాద భాషను రివ్యూ చేస్తుంది. |
| `root_dir` | `str` | `"."` | ఒక్క రివ్యూ లక్ష్యానికి ప్రాజెక్ట్ రూట్. `root_dirs` లేదా `groups` సరఫరా చేయబడినప్పుడు ఇగ్నోర్ చేయబడుతుంది. |
| `markdown` | `bool` | `False` | Markdown మరియు MDX సోర్స్ ఫైళ్లను కలపండి. |
| `notebook` | `bool` | `False` | Jupyter నోట్‌బుక్ సోర్స్ ఫైళ్లను కలపండి. |
| `images` | `bool` | `False` | అనువాద ఆప్షన్లతో సమానత్వం కోసం రిజర్వ్ చేయబడింది. చిత్రాలకు లింక్ సూచనలు Markdown నుండి తనిఖీ చేయబడతాయి. |
| `translations_dir` | `str \| None` | `None` | కస్టమ్ టెక్స్ట్ అనువాద అవుట్‌పుట్ డైరక్టరీ. రిలేటివ్ పాత్‌లు ప్రతి రూట్‌కు సంబంధించి పరిష్కరించబడతాయి. |
| `root_dirs` | `Iterable[str] \| None` | `None` | అదే అవుట్‌పుట్ సెట్టింగ్స్‌ను పంచుకునే బహుళ రూట్‌లు. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | స్పష్టమైన `(root_dir, translations_dir)` జంటలు. `root_dirs` పై ప్రాధాన్యం ఉంది. |
| `changed_from` | `str \| None` | `None` | మారిన సోర్స్ ఫైల్స్ వరకు రివ్యూ‌ను పరిమితం చేయడానికి వాడే Git ref. |
| `output_format` | `str` | `"text"` | రివ్యూ అవుట్‌పుట్ ఫార్మాట్. మద్దతు ఉన్న విలువలు `"text"` మరియు `"github"`. |
| `fail_on_warnings` | `bool` | `False` | హెచ్చరికలను కూడా తప్పిదాలుగా పరిగణించడం. |
| `debug` | `bool` | `False` | డీబగ్ లాగింగ్‌ను సడలించడం. |
| `save_logs` | `bool` | `False` | రూట్ `logs/` డైరక్టరీ క్రింద DEBUG-స్థాయి లాగ్ ఫైళ్లను సేవ్ చేయండి. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## కాన్ఫిగరేషన్ అవసరాలు

ప్రొవైడర్-ఆధారిత అనువాద API లు అనువదించే ముందు ప్రొవైడర్ కాన్ఫిగరేషన్‌ను కోరతాయి:

- Markdown మరియు notebook అనువాదానికి ఒక LLM ప్రొవైడర్ అవసరం. Azure OpenAI లేదా OpenAI లో ఏదైనా ఒకటిని కాన్ఫిగర్ చేయండి.
- ఇమేజ్ అనువాదానికి LLM ప్రొవైడర్‌తో పాటు Azure AI Vision అవసరం.
- `run_translation` ప్రాజెక్ట్ అనువాదం ప్రారంభమయ్యే ముందు లైట్‌వైట్ కనెక్టివిటీ తనిఖీలను నడుపుతుంది.
- ఏజెంట్-సహాయంతో ఉండే `start_*_agent_translation` మరియు `finish_*_agent_translation` APIs Co-op Translator LLM ప్రొవైడర్స్‌ను కాల్ చేయవు. హోస్ట్ అప్లికేషన్ లేదా MCP ఏజెంట్ తయారుచేసిన ఛంక్‌లను అనువదిస్తుంది.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, మరియు `run_review` నిర్ణాయకంగా పనిచేస్తాయి మరియు ప్రొవైడర్ క్రెడెన్షియల్స్ అవసరం ندارند.

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

`run_review` నిర్ణాయకంగా పనిచేస్తుంది మరియు Azure OpenAI, OpenAI, లేదా Azure AI Vision కాన్ఫిగరేషన్ అవసరం లేదు.

## ప్రవర్తనా గమనికలు

- కంటెంట్ అనువాద API లు అనువాదాన్ని ప్రాజెక్ట్ పాత్ రీరైటింగ్ నుండి వేరుగా ఉంచతాయి. అనువదించిన కంటెంట్‌కు ప్రాజెక్ట్-ఆధారిత లింకులను లక్ష్య స్థలానికి సరిపడ도록 సర్దుబాటు చేయాల్సినప్పుడు స్పష్టంగా `rewrite_markdown_paths` లేదా `rewrite_notebook_paths` ను పిలవండి.
- ప్రాజెక్ట్ ఆర్కెస్ట్రేషన్ API లు కంటెంట్ అనువాదం చుట్టూ ప్రాజెక్ట్ వ్యహారాన్ని జోడిస్తాయి, ఇందులో ఫైల్ అన్వేషణ, రాయడం, పాత్ రైరైటింగ్, మెటాడేటా, క్లీన్అప్, మరియు ఐచ్ఛిక డిస్క్లేమర్లను కలిగి ఉంటాయి.
- `run_translation` ప్రోగ్రెస్ మరియు అంచనా సంగ్రహాలను Click ద్వారా ప్రింట్ చేస్తుంది, CLI యూజర్ అనుభవానికి తగ్గట్టుగా.
- `dry_run=True` వర్చువల్ README అప్డేట్స్ ఉపయోగించి అంచనాలను గణిస్తుంది, కానీ README లేదా అనువాద ఫైళ్లను రాయదు.
- `groups` వరుసగా ప్రాసెస్ చేయబడతాయి. పని మొదలవడానికి ముందు ఒక ఏకైక సమ్మేళిత అంచనాను ప్రింట్ చేస్తారు.
- ఇమేజ్ అనువాదం ఎంపికచేసినప్పుడు, Vision కాన్ఫిగరేషన్ లేకపోతే అనువాదం ప్రారంభమయ్యే ముందు తప్పు (error) వ్యక్తమవుతుంది.
- ఉన్న అలియాస్-ఆధారిత భాషా ఫోల్డర్‌లు గుర్తించబడతాయి మరియు రన్ భాగంగా వారికి క్యానానికల్ భాషా ఫోల్డర్ పేర్లకు మైగ్రేట్ చేయవచ్చు.
- `run_review` అనువదించిన ఫైళ్లు లేనప్పుడు, అనువాద మెటాడేటా లేపబడిన లేదా పాతగా ఉన్నప్పుడు, చెడ్డగా ఏర్పడిన Markdown frontmatter/code fences ఉన్నప్పుడు, మరియు సరైనవిగా లేని అనువదించిన notebook JSON ఉన్నప్పుడు విఫలం అవుతుంది.
- `run_review` స్థానిక Markdown మరియు ఇమేజ్ లింక్ లక్ష్యాలు లేకపోతె వాటిని డిఫాల్ట్‌గా హెచ్చరికలుగా రిపోర్ట్ చేస్తుంది.

## అంతర్గత కాల్ పాథ్

API CLI ఉపయోగించే అదే కోర్ అమలు కు డెలిగేట్ చేస్తుంది:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` ఇన్-మెమరీ అనువాదం కోసం.
2. `co_op_translator.api.translation.rewrite_markdown_paths` లేదా `rewrite_notebook_paths` స్పష్టమైన పాత్ పోస్ట్-ప్రాసెసింగ్ కోసం.
3. `co_op_translator.api.translation.run_translation` పూర్తి ప్రాజెక్ట్ ఆర్కెస్ట్రేషన్ కోసం.
4. `co_op_translator.config.Config`, `LLMConfig`, మరియు `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, notebook మరియు ఇమేజ్‌ల కోసం ఫోకస్ చేసిన ప్రాజెక్ట్ అనువాద మిక్సిన్లు.
8. `co_op_translator.core` క్రింద Markdown, notebook, పాఠ్యం, మరియు ఇమేజ్ ట్రాన్స్‌లేటర్లు.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` కింద నిర్ణాయక తనిఖీలు

క్రింది క్లాసులు మెయింటైన్ చేసే వారికి ఉపయోగకరంగా ఉన్నా కూడా ప్యాకేజ్-స్థాయి స్థిర API గా ఎగుమతి చేయబడవు.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | ప్రాజెక్ట్-స్థాయి అనువాదం, డైరక్టరీ నిర్వహణ, ప్రతి-భాష మెటాడేటా సాధారణీకరణ, మరియు Markdown, notebook, మరియు ఇమేజ్ ట్రాన్స్‌లేటర్లకు డెలిగేషన్‌ను సమన్వయిస్తుంది. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, notebooks, images కోసం async ఫైల్ ప్రాసెసింగ్ పని, స్టేల్ డిటెక్షన్, మరియు అనువాద మెటాడేటా అప్డేట్లను నిర్వహిస్తుంది. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ఫైల్ రీడ్స్, కంటెంట్ అనువాదం, పాత్ రీరైటింగ్, మెటాడేటా, డిస్క్లేమర్లు, మరియు రైట్స్‌ను సమన్వయిస్తుంది. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | notebook ఫైల్ రీడ్స్, Markdown-సెల్ అనువాదం, పాత్ రీరైటింగ్, మెటాడేటా, డిస్క్లేమర్లు, మరియు రైట్స్‌ను సమన్వయిస్తుంది. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | సోర్స్ ఇమేజ్ అన్వేషణ, ఇమేజ్ అనువాదం, అవుట్‌పుట్ పాత్‌లు, మెటాడేటా, మరియు రైట్స్‌ను సమన్వయిస్తుంది. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | అనువదించిన Markdown జంటలను కనుగొంటుంది, అనువాద నాణ్యతను మూల్యాంకనం చేస్తుంది, మరియు తక్కువ నమ్మకత మరమ్మత్తు వర్క్‌ఫ్లోలకు నమ్మకత మెటాడేటాను చదవుతుంది. |
| `ReviewRunner` | `co_op_translator.review.runner` | సోర్స్ ఫైళ్ల, లక్ష్య భాషల, మరియు కాన్ఫిగర్ చేసిన అనువాద రూట్స్ అంతటా నిర్ణాయక రివ్యూ తనిఖీలను సమన్వయిస్తుంది. |
| `ReviewTarget` | `co_op_translator.review.targets` | ఒక సోర్స్ రూట్ మరియు ఆ రూట్ కోసం సమీక్షించే అనువాద అవుట్‌పుట్ డైరక్టరీని వర్ణిస్తుంది. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | పాత అలియాస్ భాషా ఫోల్డర్లను గుర్తించి క్యానానికల్ BCP 47 ఫోల్డర్ మైగ్రేషన్ ప్రణాళికలను సిద్ధం చేస్తుంది. |
| `Config` | `co_op_translator.config.base_config` | `.env` ఫైల్‌లను లోడ్ చేసి అవసరమయిన LLM మరియు ఐచ్ఛిక Vision ప్రొవైడర్లు కాన్ఫిగర్ అయి ఉన్నారా అని తనిఖీ చేస్తుంది. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI లేదా OpenAI ను ఆటో-డిటెక్ట్ చేసి, అవసరమైన ఎన్విరాన్‌మెంట్ వేరియబుల్స్ ను ధ్రువీకరించి, ప్రొవైడర్ కనెక్టివిటీ తనిఖీలు నడపుతుంది. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | ఇమేజ్ అనువాదానికి Azure AI Vision కాన్ఫిగరేషన్‌ను గుర్తించి కనెక్టివిటీ తనిఖీలు నడుపుతుంది. |