# Python API

స్థిరమైన పబ్లిక్ Python API ను `co_op_translator.api` నుండి ఎక్స్‌పోర్ట్ చేస్తారు. అత్యధిక ఇంటిగ్రేషన్లు ఈ వర్క్‌ఫ్లోలలో ఒకదాన్ని ఉపయోగిస్తాయి:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| వ్యక్తిగత ఫైళ్లను లేదా పత్రాలను అనువదించండి | మీ అప్లికేషన్ మూల కంటెంట్‌ను చదివి, అనువాదానికి Co-op Translator‌ను పిలుస్తుంది మరియు ఫలితాన్ని ఎక్కడ సేకరించాలో నిర్ణయిస్తుంది. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| హోస్ట్-ఏజెంట్ అనువాదానికి కాంటెంట్ సిద్ధం చేయండి | మీ MCP హోస్ట్ లేదా అప్లికేషన్ మోడల్ చెంక్‌లను అనువదిస్తుంది, Co-op Translator చెంకింగ్ మరియు పునర్నిర్మాణాన్ని నిర్వహిస్తుంది. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| మొత్తం రిపోజిటరీని అనువదించండి | మీరు Python API CLI లాగా ప్రవర్తించి డిస్కవరీ, అవుట్‌పుట్ పాత్‌లు, మెటాడేటా, క్లీనప్ మరియు రాతల నిర్వహణను నిర్వహించాలని కోరుకుంటున్నారు. | `run_translation` |

`core`, `config`, `review`, మరియు `utils` లోని చాలా లోతైన మాడ్యూల్‌లు ఈ API ఎంట్రీ పాయింట్లతో ఉపయోగించే అమలు వివరాలు.

MCP క్లయింట్లు [MCP Server](mcp.md) ద్వారా అదే పబ్లిక్ API ను ఉపయోగిస్తాయి. Python ని నేరుగా పిలవడానికి ఈ పేజీని ఉపయోగించండి, మరియు Co-op Translator ని ఏజెంట్ లేదా ఎడిటర్‌కు ప్రవేశపెటిస్తున్నప్పుడు MCP గైడ్‌ని ఉపయోగించండి. CLI, Python API, మరియు MCP మధ్య నిర్ణయం తీసుకునే పరిస్థితిలో, [Choose Your Workflow](workflows.md) తో ప్రారంభించండి.

## మొదటిసారి API ప్రవాహం

Python కోడ్ నుండి Co-op Translator ని పిలుస్తే ఇక్కడి నుండి ప్రారంభించండి:

1. మీరు కేవలం హోస్ట్-ఏజెంట్ అనువాదానికి Markdown లేదా notebook ఖండాలు మాత్రమే సిద్ధం చేయకపోతే, [Configuration](configuration.md) లో వివరిసినట్లుగా ఒక LLM ప్రొవైడర్‌ను కాన్ఫిగర్ చేయండి.
2. మీ అప్లికేషన్ ఫైల్ I/O ను నిర్వహిస్తుందా అనే విషయం నిర్ణయించుకోండి.
3. మీ అప్లికేషన్ వ్యక్తిగత ఫైళ్లను చదివి రాస్తే కంటెంట్ APIలు ఉపయోగించండి.
4. Co-op Translator ఒక రిపోజిటరీని CLI లాగా ప్రాసెస్ చేయాలనుకుంటే `run_translation` ను ఉపయోగించండి.
5. ఆటోమేషన్‌లో నిర్ణయాత్మక తనిఖీలకు అవశ్యకమైతే అనువాదం తర్వాత `run_review` ను ఉపయోగించండి.

| Goal | API to start with |
| --- | --- |
| ఒక Markdown స్ట్రింగ్ లేదా ఫైల్‌ను అనువదించండి | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| హోస్ట్ ఏజెంట్‌ను Markdown లేదా నోట్‌బుక్ భాగాలను అనువదించనివ్వండి | `start_markdown_agent_translation` లేదా `start_notebook_agent_translation` |
| ఔట్‌పుట్ మార్గాన్ని ఎంచుకున్న తర్వాత అనువదించిన లింకులను తిరిగి రాయండి | `rewrite_markdown_paths` లేదా `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## సన్నివేశం 1: వ్యక్తిగత ఫైళ్ళను లేదా పత్రాలను అనువదించండి

మీకు ఇప్పటికే ఫైల్, ఎడిటర్ బఫర్, notebook పేలోడ్, MCP అభ్యర్థన, లేదా కస్టమ్ పైప్‌లైన్ ఇన్‌పుట్ ఉన్నప్పుడు మీ కోడ్ ఫైల్ I/O ను నిర్వహిస్తుంటే ఈ వర్క్‌ఫ్లో ఉపయోగించండి:

1. మూల విషయాన్ని చదవండి.
2. ఒక కంటెంట్ అనువాద API ను పిలవండి.
3. అనువదించిన విషయం ప్రాజెక్ట్ అనువాద ఫోల్డర్‌లో రాయబడాల్సినట్లయితే, ఐచ్ఛికంగా మార్గం రీవ్రైటింగ్ API ను పిలవండి.
4. ఫలితాన్ని మీ అప్లికేషన్ నుండి సేవ్ చేయండి లేదా రిటర్న్ చేయండి.

కంటెంట్ అనువాద APIలు ప్రాజెక్ట్ గుర్తింపు (discovery) ను నడపవు, మెటాడేటా రాయవు, డిస్క్లెయిమర్లను జతపరచవు, మరియు లింకులను ఆటోమేటిగానే రీవ్రైట్ చేయవు.

### Markdown ఫైల్

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

అనువదించిన Markdown Co-op Translator ప్రాజెక్ట్ లేఆউట్‌లో నిలవకపోతే, `rewrite_markdown_paths` ను స్కిప్ చేసి అనువదించిన స్ట్రింగ్‌ను నేరుగా సేవ్ చేయండి.

### Notebook ఫైల్

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

`translate_notebook_content` Markdown సెల్‌లను అనువదిస్తుంది మరియు non-Markdown సెల్‌లను పరిరక్షిస్తుంది. మార్గ రీవ్రైటింగ్ కేవలం Markdown సెల్‌లకు మాత్రమే వర్తిస్తుంది.

### చిత్ర ఫైల్

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

`translate_image_content` మూల చిత్రాన్ని చదివి ఒక రెండర్డ్ `PIL.Image.Image` ను రిటర్న్ చేస్తుంది. ఇది అనువదించిన చిత్రం మెటాడేటాను రాయదు.

## సన్నివేశం 2: మొత్తం రిపోజిటరీని అనువదించండి

Python API `translate` CLI లాగా పనిచేయాలని కోరుకుంటే ఈ వర్క్‌ఫ్లో ఉపయోగించండి. `run_translation` మద్దతు పొందే ఫైళ్లను కనుగొంటుంది, ఎంపిక చేసిన కంటెంట్ రకాల్ని అనువదిస్తుంది, మార్గాలను రీవ్రైట్ చేస్తుంది, అవుట్‌పుట్ ఫైళ్లను రాస్తుంది, మెటాడేటాను అప్డేట్ చేస్తుంది, మరియు శుభికరణ వంటి అనువాద నిర్వహణ పనులు చేస్తుంది.

`run_translation` ప్రాజెక్ట్ ఆర్చిస్ట్రేషన్ ప్రవేశ బిందువుగా ప్రాముఖ్యంగా సూచించబడింది. `translate_project` అదే ప్రవర్తనతో అనుకూలత అలియాస్‌గా ఎక్స్‌పోర్ట్ చేయబడింది.

ప్రస్తుత రిపోజిటరీలోని Markdown ఫైళ్లను కొరియన్ మరియు జపనీస్ భాషలలోకి అనువదించండి:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

నిర్దిష్ట ప్రాజెక్ట్ రూట్ నుండి మాత్రమే నోట్‌బుక్స్‌ను అనువదించండి:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ఫైళ్లను రాయకుండా అనువాద పరిమాణాన్ని ముందుగా చూడండి:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ఒక ఇంటిగ్రేషన్ కోసం నిర్మిత పురోగతి ఈవెంట్స్‌ను రికార్డ్ చేయండి:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # మీ జాబ్-ఈవెంట్ పట్టికలో పేలోడ్‌ను నిల్వ చేయండి లేదా దాన్ని మీ UIకి స్ట్రీమ్ చేయండి.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

ఈవెంట్లు వెర్షన్ చేయబడిన స్కీమా `co-op.translation.event.v1` ను ఉపయోగిస్తాయి. ఇంటిగ్రేషన్లు
`type` మరియు `stage_key` వంటి స్థిర ఫీల్డ్‌లపై ఆధారపడాలి, మానవ-సామ్ముఖ్యపు
కన్సోల్ పాఠ్యం లేదా `stage_label` పై కాకుండా.

ఒకే కాల్‌లో బహుళ కంటెంట్ రూట్స్‌ను అనువదించండి:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

అనువాదాలను స్పష్టమైన అవుట్‌పుట్ గుంపులలో రాయండి:

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

ప్రతి భాషలో అంతర్గత ఉపడైరెక్టరీ ఉండాల్సినప్పుడు ప్రతి-భాష ప్లేస్‌హోల్డర్‌ను ఉపయోగించండి:

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

ఒకటి కూడా `markdown`, `notebook`, లేదా `images` సెట్ చేయబడకపోతే, API అన్ని మద్దతు పొందిన రకాలను అనువదిస్తుంది: Markdown, నోట్‌బుక్స్, మరియు చిత్రాలు.

### అనుమోదించిన మానవ సవరింపులను అనువాద స్థితి ప్రదాతతో సంరక్షించండి

డిఫాల్ట్‌గా, Co-op Translator దాని ప్రస్తుతం ఉన్న ఫైల్-స్థాయి ప్రవర్తనను కొనసాగిస్తుంది:
Markdown మూలం పాతదైతే, మొత్తం అనువదించిన ఫైల్ మళ్లీ సృష్టించబడుతుంది. హోస్ట్
ఇంటిగ్రేషన్లు ఐచ్ఛికంగా `TranslationStateProvider` ను అందించవచ్చు, తద్వారా మార్పు కాకపోయిన మూల బ్లాక్‌లలో మానవ
సవరింపులను నిల్వ చేయవచ్చు.

ప్రొవైడర్ చివరి ఆమోదించబడ్డ మూల/లక్ష్య జంటను అందిస్తుంది మరియు ప్రతి కొత్త
అభ్యర్థిని రికార్డ్ చేస్తుంది. ఆమోదం ఇంటిగ్రేషన్ యొక్క బాధ్యతగా ఉంటుంది—ఉదాహరణకి,
అనువాద పుల్ రిక్వెస్ట్ విలీనం అయిన తర్వాత:

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

చెల్లుబాటు అయ్యే, అనుమోదించిన బేస్‌లైన్ ఉన్న Markdown ఫైళ్లకు, Co-op Translator సరిపోల్చుతుంది
పై-స్థాయి Markdown బ్లాక్‌లు. మార్చబడని మూల బ్లాక్‌లు ప్రస్తుత అనువదించిన
బ్లాక్‌లు, వ్యక్తులచే చేసిన సవరణలను కూడా కలిపి; మార్చబడిన లేదా జోడించబడిన మూల బ్లాక్‌లు పంపబడతాయి
అనువాదానికి; తొలగించిన మూల బ్లాక్‌లు తొలగించబడతాయి. సరిపోలింపు అనిశ్చితమైతే,
లక్ష్య నిర్మాణం మారిపోయినట్లయితే, బ్లాక్ అనువాదం చెల్లనిది అయితే, లేదా బేస్‌లైన్ అందుబాటులో లేకపోతే
అందుబాటులో లేకపోతే, Co-op Translator సురక్షితంగా ప్రస్తుత పూర్తి-ఫైల్
అనువాద మార్గానికి వెనక్కి వెళ్తుంది.

ఈ API డాక్యుమెంట్ అనువాద స్థితిని నిల్వ చేస్తుంది, డాక్యుమెంట్-దాటి పదబంధం లేదా
సెగ్మెంట్ అనువాద మెమొరీని కాదు. ఇది ప్రస్తుతం Markdown ప్రాజెక్ట్
అనువాదానికి వర్తిస్తుంది. Notebook మరియు image ప్రవర్తన మారలేదు. `update=True`
ఇప్పటికీ పూర్తి పునరుత్పత్తిని అభ్యర్థిస్తుంది.

ఒకటి లేదా ఎక్కువ ఫైళ్లు అనువదించలేకపోతే, `run_translation` ఒక
`RuntimeError` ను ప్రాజెక్ట్ वర్క్‌ఫ్లో ముగిసిన తర్వాత ఎక్కిస్తుంది, కానీ
లేదా లేకపోయిన అవుట్పుట్ ఉన్న విజయవంతమైన రన్ గా నివేదించదు. ఇంటిగ్రేషన్లు దీన్ని విఫలమైన
పని గా పరిగణించి ముందున్న ఆమోదించిన అనువాద స్థితిని నిలుపుకోవాలి.

## అనువదించిన అవుట్‌పుట్‌ను సమీక్షించండి

`run_review` LLM లేదా Vision క్రెడెన్షియల్స్ లేకుండా నిర్ణయాత్మక అనువాద తనిఖీలను నడిపిస్తుంది.

!!! note "బీటా"
    `run_review` అనేది బీటా నిర్దారిత రివ్యూ API. ఇది మోడల్ ప్రొవైడర్లను కాల్ చేయదు లేదా ఫైళ్లను రాయదు, కానీ తనిఖీలు మరియు ఇష్యూ స్కీమాలు మారవచ్చు.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README-only అనువాదం తర్వాత, సమీక్ష కోసం అదే పరిధిని ఉపయోగించండి:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` ప్రతి కాన్ఫిగర్ చేసిన సోర్స్ రూట్ కింద కేవలం `README.md`ని మాత్రమే సమీక్ష చేస్తుంది,
including custom `groups` and output directories. Other documents and nested
READMEs are excluded. A missing source README raises `ValueError`; failed
translation checks raise `RuntimeError`.

మూల రిఫ్‌తో పోల్చి మార్చబడిన ఫైళ్లను మాత్రమే సమీక్షించండి మరియు GitHub-శైలి అవుట్‌పుట్‌ను ప్రింట్ చేయండి:

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

## కాపీ-పేస్ట్ API ఉదాహరణలు

ఫైల్ రాయకుండా Markdown కంటెంట్‌ని అనువదించండి:

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

Translate and rewrite Markdown links:

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

Translate a repository from Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Translate multiple roots:

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

Preserve glossary terms:

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

## సార్వజనిక ఎంట్రీ పాయింట్లు

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

## కంటెంట్ అనువాద APIలు

కంటెంట్ అనువాద APIలు ఇప్పటికే మెమరీలో కంటెంట్ ఉన్న ఇంటిగ్రేషన్ల కోసం ఉద్దేశించబడ్డవి, ఉదాహరణకు ఎడిటర్ ఎక్స్‌టెన్షన్, MCP టూల్, నోట్‌బుక్ ప్రాసెసర్, లేదా కస్టమ్ పైప్‌లైన్.

| ఫంక్షన్ | ఇన్‌పుట్ | అవుట్‌పుట్ | ఫైల్ I/O | గమనికలు |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. కేవలం Markdown కంటెంట్‌ను అనువదిస్తుంది. ఇది లింకులను తిరిగి రాయదు, మెటాడేటాను రాయదు, లేదా డిస్క్లైమర్లను జత చేయదు. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown సెల్స్‌ను అనువదించి, మార్క్‌డౌన్ కాని సెల్స్‌ను పరిరక్షిస్తుంది. ఇది లింకులను తిరిగి రాయదు, మెటాడేటాను రాయదు, లేదా డిస్క్లైమర్లను జత చేయదు. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. ఇమేజ్‌లోని టెక్స్ట్‌ను తీసుకుని అనువదించి, ఆ తర్వాత రేండర్ చేసిన ఇమేజ్‌ని తిరిగి ఇస్తుంది. ఇది అనువదించిన ఇమేజ్ మెటాడేటాను సేవ్ చేయదు. |

`translate_markdown_content` మరియు `translate_notebook_content` వారి ఎంపికల ద్వారా ఐచ్ఛిక `source_path` ను స్వీకరిస్తాయి. పథాన్ని అనువాదకుడికి సందర్భం (context)గా పంపబడుతుంది; అనువాదం తర్వాత ప్రాజెక్టు-నిర్దిష్ట పథం పునఃరచనా బాధ్యత కాలర్లపైనే ఉంటుంది.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

అదే ఎంపికలను డిక్షనరీలాగా అందించవచ్చు:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## ఏజెంట్-సహాయంతో అనువాద APIలు

ఏజెంట్-సహాయిత APIలు Co-op Translator నుండి కాన్ఫిగర్ చేయబడిన LLM ప్రొవైడర్‌ను కాల్ చేయవు. వారు హోస్ట్ ఏజెంట్ అనువదించడానికి Markdown లేదా నోట్‌బుక్ ఛంక్‌లను సిద్ధం చేస్తారు, తరువాత అనువదించిన ఛంక్‌ల నుండి తుది కంటెంట్‌ను పునఃనిర్మాణం చేస్తారు.

| ఫంక్షన్ | ప్రయోజనం |
| --- | --- |
| `start_markdown_agent_translation` | చంక్‌లు, ప్రాంప్ట్‌లు మరియు పునఃనిర్మాణ స్థితితో స్వతంత్రంగా ఉండే Markdown జాబ్‌ను తిరిగి ఇస్తుంది. |
| `finish_markdown_agent_translation` | జాబ్ మరియు హోస్ట్-ఏజెంట్ అనువదించిన’ch’ ఛంక్‌ల నుండి Markdown‌ను పునఃనిర్మాణం చేస్తుంది. |
| `start_notebook_agent_translation` | హోస్ట్-ఏజెంట్ అనువాదానికి Markdown-సెల్ ఛంక్‌లతో కూడిన నోట్‌బుక్ జాబ్‌ను తిరిగి ఇస్తుంది. |
| `finish_notebook_agent_translation` | కోడ్ సెల్‌లు, అవుట్‌పुट్లు మరియు మెటాడేటాను conservaçãoగా (preserving) ఉంచి నోట్‌బుక్ JSON ను పునఃనిర్మాణం చేస్తుంది. |

ఈ వర్క్‌ఫ్లో ప్రధానంగా MCP హోస్ట్స్ కోసం ఉద్దేశించబడింది. Co-op Translator ప్రొవైడర్ కాల్స్ నిర్వహిస్తూ ప్రొడక్షన్ రిపోజిటరీ అనువాదం అవసరమైతే, `translate_markdown_content`, `translate_notebook_content`, లేదా `run_translation` ఉపయోగించండి.

## పాథ్ రీరైటింగ్ APIలు

పాత్ రీరైటింగ్ APIలు అనువాదం చేయవు. అవి కాల్ చేయేవారు మూల పాత్, అనువదించిన లక్ష్య పాత్, మరియు ప్రాజెక్ట్ లేఅవుట్ తెలుసుకున్న తర్వాత లింకులు మరియు ఫ్రంట్‌మాటర్ పాథ్‌లను నవీకరిస్తాయి.

| ఫంక్షన్ | పరిధి | గమనికలు |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown శరీరం మరియు ఫ్రంట్‌మాటర్ | అనువదించిన లక్ష్యానికి Markdown లింకులను మరియు మద్దతు ఉన్న ఫ్రంట్‌మాటర్ పాథ్ ఫీల్డ్‌లను తిరిగి రాశిస్తుంది. |
| `rewrite_notebook_paths` | Notebook JSONలోని Markdown సెల్స్ | ప్రతి Markdown సెల్‌కు Markdown పాథ్ రీరైటింగ్‌ను వర్తింపచేస్తుంది మరియు non-Markdown సెల్‌లను మార్పు చేయకుండా ఉంచుతుంది. |

`policy` ఆర్గుమెంట్ ఈ కింది ఫీల్డ్స్ ఉన్న డిక్షనరీ కావచ్చు:

| ఫీల్డ్ | అవసరం | ఉద్దేశ్యం |
| --- | --- | --- |
| `language_code` | Yes | లక్ష్య భాష కోడ్, ఉదాహరణకు `"ko"` లేదా `"pt-BR"`. |
| `root_dir` | No | సోర్స్ ప్రాజెక్ట్ రూట్. డిఫాల్ట్ `"."`. |
| `translations_dir` | No | టెక్స్ట్ అనువాద అవుట్‌పుట్ డైరెక్టరీ. డిఫాల్ట్ `root_dir` కింద ఉన్న `translations`. |
| `translated_images_dir` | No | అనువదించిన ఇమేజ్ అవుట్‌పుట్ డైరెక్టరీ. డిఫాల్ట్ `root_dir` కింద ఉన్న `translated_images`. |
| `translation_types` | No | సక్రియమైన అనువాద రకాలు. డిఫాల్ట్‌గా Markdown, నోట్బుక్స్, మరియు ఇమేజిస్. |
| `lang_subdir` | No | ప్రతి భాష ఫోల్డర్ కింద ఐచ్ఛిక సబ్డైరెక్టరీ. |

## ప్రాజెక్ట్ అనువాద పారామితులు

| పరామీటర్ | రకం | డిఫాల్ట్ | ఉద్దేశ్యం |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | స్పేస్-విచ్ఛిన్న లక్ష్య భాష కోడ్స్, ఉదాహరణకు `"ko ja fr"`, లేదా `"all"`. అలియాస్ కోడ్స్ canonical BCP 47 విలువలకు నార్మలైజ్ చేయబడతాయి. |
| `root_dir` | `str` | `"."` | ఒకే అనువాద లక్ష్యానికి ప్రాజెక్ట్ రూట్. `root_dirs` లేదా `groups` ఇచ్చినప్పుడు ఇది పరిగణించబడదు. |
| `update` | `bool` | `False` | ఎంచుకున్న భాషల కోసం ఉన్న అనువాదాలను తొలగించి తిరిగి సృష్టిస్తుంది. |
| `images` | `bool` | `False` | ఇమేజ్ అనువాదాన్ని చేర్చండి. Azure AI Vision కాన్ఫిగరేషన్ అవసరం. |
| `markdown` | `bool` | `False` | Markdown అనువాదాన్ని చేర్చండి. |
| `notebook` | `bool` | `False` | Jupyter notebook అనువాదాన్ని చేర్చండి. |
| `debug` | `bool` | `False` | డీబగ్ లాగింగ్‌ను ప్రారంభించండి. |
| `save_logs` | `bool` | `False` | DEBUG-స్థాయిలో లాగ్ ఫైళ్ళను రూట్ `logs/` డైరెక్టరీ కింద సేవ్ చేయండి. |
| `yes` | `bool` | `True` | ప్రోగ్రామాటిక్ మరియు CI వినియోగానికి ప్రాంప్ట్‌లను ఆటో-నిర్ధారిస్తుంది. |
| `add_disclaimer` | `bool` | `False` | అనువదించిన Markdown మరియు నోట్‌బుక్లకు మెషిన్ అనువాద నిరాకరణలు జోడిస్తుంది. |
| `translations_dir` | `str \| None` | `None` | కస్టమ్ టెక్స్ట్ అనువాద అవుట్‌పుట్ డైరెక్టరీ. రిలేటివ్ మార్గాలు ప్రతి రూట్‌ను ఆధారంగా పరిష్కరించబడతాయి. |
| `image_dir` | `str \| None` | `None` | కస్టమ్ అనువదించిన ఇమేజ్ అవుట్‌పుట్ డైరెక్టరీ. రిలేటివ్ మార్గాలు ప్రతి రూట్‌ను ఆధారంగా పరిష్కరించబడతాయి. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ఒకే అవుట్‌పుట్ సెట్టింగ్స్‌ను పంచుకునే బహుళ రూట్‌లు. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | స్పష్టమైన `(root_dir, translations_dir)` జంటలు. ఇది `root_dirs` కంటే ప్రాధాన్యతను కలిగి ఉంటుంది. |
| `repo_url` | `str \| None` | `None` | README భాషా పట్టిక మార్గదర్శకతను రూపొందించే సమయంలో ఉపయోగించే Repository URL. |
| `glossaries` | `Iterable[str] \| None` | `None` | అనువాద సమయంలో పరిరక్షించవలసిన పరిభాష పదాలు. నకలు మరియు ఖాళీ పదాలు సాధారణీకరించబడతాయి. |
| `dry_run` | `bool` | `False` | ఫైళ్లను రాయకుండా అనువాద పరిమాణాన్ని అంచనా వేయడం మరియు మైగ్రేషన్ ప్రవర్తనను ముందుగా పరిశీలించడం. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | ఇంక్రిమెంటల్ Markdown అప్‌డేట్ల కోసం ఐచ్ఛికంగా అంగీకరించిన-బేస్‌లైన్ మరియు అభ్యర్థి నిలుపుదల అడాప్టర్. దీన్ని వదిలివేస్తే ఉన్న పూర్తి-ఫైల్ ప్రవర్తన అరినడుతుంది. |

## సమీక్ష పరామితులు

`run_review` యదార్థంగా `run_translation` సంతకాన్ని వీలైనంత వరకు అనుకరిస్తుంది, తద్వారా ఆటోమేషన్ కనీస బ్రాంచింగ్‌తో అనువాద మరియు సమీక్ష వర్క్‌ఫ్లోల మధ్య మార్పు చేసుకోవచ్చు.

| పరామితి | రకం | డిఫాల్ట్ | ప్రయోజనం |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | సమీక్షకు లక్ష్య భాషా ఫోల్డర్లు. స్పేస్-విభజಿತ స్ట్రింగ్‌లు మరియు iterableలు స్వీకరించబడతాయి. `"all"` కనుగొన్న ప్రతి అనువాద భాషను సమీక్షిస్తుంది. |
| `root_dir` | `str` | `"."` | ఒకదాని సమీక్ష లక్ష్యానికి ప్రాజెక్ట్ రూట్. `root_dirs` లేదా `groups` అందించినప్పుడు విస్మరించబడుతుంది. |
| `markdown` | `bool` | `False` | Markdown మరియు MDX మూల ఫైళ్లను చేర్చండి. |
| `notebook` | `bool` | `False` | Jupyter నోట్‌బుక్ మూల ఫైళ్లను చేర్చండి. |
| `images` | `bool` | `False` | అనువాద ఎంపికలతో సమానత్వం కోసం రిజర్వ్ చేయబడింది. చిత్రాలకు సంబంధించిన లింక్ సూచనలు Markdown నుండి తనిఖీ చేయబడతాయి. |
| `translations_dir` | `str \| None` | `None` | కస్టమ్ టెక్స్ట్ అనువాద అవుట్‌పుట్ డైరెక్టరీ. రిలేటివ్ మార్గాలు ప్రతి రూట్‌ను ఆధారంగా పరిష్కరించబడతాయి. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ఒకే అవుట్‌పుట్ సెట్టింగ్స్‌ను పంచుకునే బహుళ రూట్‌లు. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | స్పష్టమైన `(root_dir, translations_dir)` జంటలు. ఇది `root_dirs` కంటే ప్రాధాన్యతను కలిగి ఉంటుంది. |
| `changed_from` | `str \| None` | `None` | సమీక్షను మారిన సోర్స్ ఫైళ్లకు పరిమితం చేయడానికి ఉపయోగించే Git ref. |
| `readme_only` | `bool` | `False` | ప్రతి సోర్స్ రూట్ కింద ఉన్న `README.md` మాత్రమే సమీక్షించండి. మూల README లేకపోతే `ValueError` కలగజేస్తుంది. |
| `output_format` | `str` | `"text"` | సమీక్ష అవుట్పుట్ ఫార్మాట్. మద్దతు ఇచ్చే విలువలు `"text"` మరియు `"github"`. |
| `fail_on_warnings` | `bool` | `False` | హెచ్చరికలను తప్పులతో పాటు విఫలతలుగా కూడా పరిగణించు. |
| `debug` | `bool` | `False` | డీబగ్ లాగింగ్‌ను ప్రారంభించు. |
| `save_logs` | `bool` | `False` | DEBUG-స్థాయి లాగ్ ఫైళ్ళను root `logs/` డైరెక్టరీలో సేవ్ చేయండి. |

`markdown`, `notebook`, లేదా `images`లో ఏవైనా సెట్ చేయబడకపోతే, API అవసరమైన సందర్భాల్లో Markdown, నోట్బుక్స్, మరియు చిత్రం లింక్ సూచనలను సమీక్షిస్తుంది. సమీక్ష LLM ప్రొవైడర్‌ను పిలవదు మరియు API కీలు అవసరం కాదు.

## కన్ఫిగరేషన్ అవసరాలు

Provider-ఆధారిత అనువాద APIలు అనువదించే ముందు ప్రొవైడర్ కాన్ఫిగరేషన్ అవసరం:

- Markdown మరియు నోట్‌బుక్ అనువాదానికి LLM ప్రొవైడర్ అవసరం. Azure OpenAI, OpenAI, లేదా Anthropic ని కాన్ఫిగర్ చేయండి.
- ఇమేజ్ అనువాదానికి LLM ప్రొవైడర్‌కు అదనంగా Azure AI Vision అవసరం.
- `run_translation` ప్రాజెక్ట్ అనువాదం ప్రారంభమవడానికి ముందు తేలికపాటి కనెక్టివిటీ తనిఖీలు నిర్వహిస్తుంది.
- ఏజెంట్-సహాయంతో `start_*_agent_translation` మరియు `finish_*_agent_translation` APIలు Co-op Translator LLM providers ను కాల్ చేయవు. హోస్ట్ అప్లికేషన్ లేదా MCP ఏజెంట్ సిద్ధం చేసిన భాగాలను అనువదిస్తుంది.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, మరియు `run_review` నిర్దిష్టమైనవి మరియు ప్రొవైడర్ క్రెడెన్షియల్స్ అవసరం ఉండవు.

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

Required Anthropic variables:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` and `ANTHROPIC_MAX_TOKENS` ఐచ్చికంగా ఉంటాయి. Microsoft Agent Framework Co-op Translator 0.22.0 నుంచి ప్రారంభమై అన్ని ప్రొవైడర్లకు డిఫాల్ట్ మోడల్ క్లయింట్. Semantic Kernel ను తాత్కాలికంగా ఇంకా `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` ద్వారా ఎంచుకోవచ్చు, కానీ అలాగే చేయడం ఒక డిప్రికేషన్ హెచ్చరికను విడుదల చేస్తుంది; దశల వారీ తొలగింపు ప్రణాళిక కోసం [కాన్ఫిగరేషన్](configuration.md#model-client-backend) ను చూడండి.

చిత్రం అనువాదానికి అవసరమైన Azure AI Vision వేరియబల్స్:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` నిర్ధారితంగా పనిచేస్తుంది మరియు LLM లేదా Azure AI Vision కాన్ఫిగరేషన్ అవసరం లేదు.

## ప్రవర్తన గమనికలు

- కంటెంట్ అనువాద APIలు అనువాదాన్ని ప్రాజెక్ట్ మార్గాల పునఃరాయిటింగ్ నుండి వేరుగా ఉంచుతాయి. అనువదించిన కంటెంట్‌కు లక్ష్య స్థానం కోసం ప్రాజెక్ట్-సాపేక్ష లింకులను సర్దుబాటు చేయాల్సినప్పుడు స్పష్టంగా `rewrite_markdown_paths` లేదా `rewrite_notebook_paths` ను పిలవండి.
- ప్రాజెక్ట్ ఆర్కెస్ట్రేషన్ APIలు ఫైల్ కనుగొనడం, రాయడం, మార్గాల పునఃరాయిటింగ్, మెటాడేటా, శుభ్రపరచడం మరియు ఐచ్ఛిక డిస్క్లెయిమర్లు వంటి కంటెంట్ అనువాదానికి సంబంధించిన ప్రాజెక్ట్ ప్రవర్తనను జోడిస్తాయి.
- `run_translation` CLI ద్వారా ఉపయోగించే అదే Rich-ఆధారిత రిపోర్టర్ ద్వారా ప్రగతి మరియు అంచనా సారాంశాలను ప్రింట్ చేస్తుంది. ఇంటరాక్టివ్ కాని అవుట్పుట్ సాధారణ టెక్స్ట్‌కు తిరిగి వస్తుంది.
- `dry_run=True` వర్చువల్ README నవీకరణలను ఉపయోగించి అంచనాలు లెక్కిస్తుంది, కానీ README లేదా అనువాద ఫైళ్లను రాయదు.
- `groups` అనేవి వరుసగా ప్రాసెస్ చేయబడతాయి. పని ప్రారంభించే ముందు ఒకే ఒక్క సమగ్ర అంచనా ప్రింట్ చేయబడుతుంది.
- ఇమేజ్ అనువాదం ఎంచుకున్నప్పుడు, Vision కాన్ఫిగరేషన్ లేకుంటే అనువాదం ప్రారంభమయ్యే ముందు ఒక లోపం తలెత్తుతుంది.
- ఇప్పటికే ఉన్న అలియాస్-ఆధారిత భాషా ఫోల్డర్లు కనుగొనబడతాయి మరియు రన్ సమయంలో అవి ప్రామాణిక భాషా ఫోల్డర్ పేర్లకు మైగ్రేట్ చేయబడవచ్చు.
- `run_review` అనువాదిత ఫైళ్లు లేవనప్పుడు, అనువాద మెటాడేటా లేమి లేదా పాతదిగా ఉండడం, దోషపూరితమైన Markdown frontmatter/code fences ఉండటం, మరియు చెలామణీ కాని అనువాదిత notebook JSON ఉన్నపుడు విఫలమవుతుంది.
- `run_review` స్థానిక Markdown మరియు ఇమేజ్ లింక్ లక్ష్యాల కొరతలను డిఫాల్ట్‌గా హెచ్చరికలుగా నివేదిస్తుంది.

## అంతర్గత కాల్ మార్గం

API CLI ఉపయోగించే అదే కోర్ అమలుకు అప్పగిస్తుంది:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, నోట్‌బుక్స్, మరియు ఇమేజ్‌లకు ఫోకస్ చేయబడ్డ ప్రాజెక్ట్ అనువాద మిక్సిన్లు.
8. Markdown, నోట్‌బుక్, టెక్స్ట్, మరియు ఇమేజ్ అనువాదకులు `co_op_translator.core` కింద.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

క్రింది క్లాసులు మెయింటెనర్లకు ఉపయోగకరమైనవి, కానీ ప్యాకేజ్-స్థాయి స్థిరమైన APIగా ఎక్స్‌పోర్ట్ చేయబడవు.

| క్లాస్ | మాడ్యూల్ | బాధ్యత |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | ప్రాజెక్ట్-స్థాయి అనువాదం, డైరెక్టరీ నిర్వహణ, ప్రతి-భాష మెటాడేటా సాధారణీకరణ, మరియు Markdown, notebook, మరియు image అనువాదకులకు డెలిగేషన్‌ను సమన్వయిస్తుంది. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, notebooks, images, స్టేల్ గుర్తింపు, మరియు అనువాద మెటాడేటా నవీకరణల కోసం అసింక్ ఫైల్ ప్రాసెసింగ్ పనులను నిర్వహిస్తుంది. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ఫైల్ చదవడం, కంటెంట్ అనువాదం, పాథ్ రీరైటింగ్, మెటాడేటా, నిరాకరణలు, మరియు రైట్స్ ను ఒర్కెస్ట్రేట్ చేస్తుంది. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | నోట్‌బుక్ ఫైల్ చదవడం, Markdown-సెల్ అనువాదం, పాథ్ రీరైటింగ్, మెటాడేటా, నిరాకరణలు, మరియు రైట్స్ ను ఒర్కెస్ట్రేట్ చేస్తుంది. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | సోర్స్ ఇమేజ్ కనుగొనడం, చిత్రం అనువాదం, అవుట్‌పుట్ పాథ్లు, మెటాడేటా, మరియు రైట్స్ ను ఒర్కెస్ట్రేట్ చేస్తుంది. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | అనువదించిన Markdown జంటలను కనుగొని, అనువాద నాణ్యతను మదింపు చేయగలిగినదిగా పరీక్షించి, తక్కువ విశ్వాసం మరమ్మత్తు వర్క్‌ఫ్లోల కోసం విశ్వాస మెటాడేటాను చదువుతుంది. |
| `ReviewRunner` | `co_op_translator.review.runner` | మూల ఫైళ్లు, లక్ష్య భాషలు, మరియు కాన్ఫిగర్ చేసిన అనువాద రూట్‌లను ఆవిర్భవించే నిర్దిష్ట సమీక్ష తనిఖీలను సమన్వయిస్తుంది. |
| `ReviewTarget` | `co_op_translator.review.targets` | ఒక సోర్స్ రూట్ మరియు ఆ రూట్ కోసం సమీక్ష చేయబడే అనువాద అవుట్‌పుట్ డైరెక్టరీను వివరించుకుంటుంది. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | పాత అలియాస్ భాషా ఫోల్డర్లను గుర్తించి ప్రమాణీకృత BCP 47 ఫోల్డర్ మైగ్రేషన్ ప్లాన్‌లను సిద్ధం చేస్తుంది. |
| `Config` | `co_op_translator.config.base_config` | `.env` ఫైళ్లను లోడ్ చేసి అవసరమయిన LLM మరియు ఐచ్ఛిక Vision ప్రొవైడర్లు కాన్ఫిగర్ అయ్యాయో లేదో తనిఖీ చేస్తుంది. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI, లేదా Anthropic ను ఆటోడిటెక్ట్ చేసి, అవసరమైన ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌ను ధృవీకరించి, ప్రొవైడర్ కనెక్టివిటీ చెక్లను నడిపిస్తుంది. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision కాన్ఫిగరేషన్‌ను గుర్తించి చిత్ర అనువాదం కోసం కనెక్టివిటీ చెక్స్ నడుపుతుంది. |