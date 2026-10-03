# Python API

API សាធារណៈ Python ដែលមានស្ថិរភាព ត្រូវបាននាំចេញពី `co_op_translator.api`. ការរួមបញ្ចូលភាគច្រើនប្រើមួយក្នុងចំណោមដំណើរការទាំងនេះ:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| បកប្រែឯកសារ ឬឯកសារផ្សេងៗ | កម្មវិធីរបស់អ្នកអានមាតិកាដើម ហៅ Co-op Translator សម្រាប់បកប្រែ ហើយសម្រេចថាត្រូវរក្សាទុកលទ្ធផលនៅឯណា។ | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| រៀបចំមាតិកាសម្រាប់ការបកប្រែដោយ host-agent | MCP host របស់អ្នក ឬម៉ូដែលកម្មវិធីនឹងបកប្រែចំណែកខណៈពេល Co-op Translator ទទួលខុសត្រូវក្នុងការបំបែក និងស្តារឡើងវិញ។ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| បកប្រែ repository ទាំងមូល | អ្នកចង់ឲ្យ Python API មានអាកប្បកិរិយាដូច CLI ហើយ​គ្រប់គ្រងការរកឃើញ, ទីតាំងលទ្ធផល, មេតាដាតា, ការសម្អាត និងការសរសេរ។ | `run_translation` |

ម៉ូឌុលកម្រិតទាបភាគច្រើនក្រោម `core`, `config`, `review`, និង `utils` គឺជាព័ត៌មានលម្អិតនៃការអនុវត្តដែលត្រូវបានប្រើដោយចំណុចចូល API ទាំងនេះ។

អ្នកភាគី MCP ប្រើ API សាធារណៈដូចគ្នាតាមរយៈ [MCP Server](mcp.md)។ ប្រើទំព័រនេះពេលហៅ Python ដោយផ្ទាល់ ហើយប្រើមគ្គុទ្ទេសក៍ MCP ពេលបង្ហាញ Co-op Translator ទៅភ្នាក់ងារ ឬកម្មវិធីកែសម្រួល។ ប្រសិនបើអ្នកកំពុងសម្រេចចិត្តរវាង CLI, Python API, និង MCP ចាប់ផ្តើមជាមួយ [Choose Your Workflow](workflows.md)។

## ដំណើរការ API សម្រាប់លើកដំបូង

ចាប់ផ្ដើមនៅទីនេះ ប្រសិនបើអ្នកកំពុងហៅ Co-op Translator ពីកូដ Python៖

1. កំណត់រចនាសម្ព័ន្ធអ្នកផ្គត)L LLM ដោយដូចដែលបានពិពណ៌នា​នៅក្នុង [Configuration](configuration.md), លើកលែងតែអ្នកកំពុងតែរៀបចំផ្នែក Markdown ឬ notebook សម្រាប់ការបកប្រែដោយ host-agent។
2. សម្រេចថាតើកម្មវិធីរបស់អ្នកទទួលបន្ទុកការបញ្ចូល/ចេញឯកសារ (file I/O) ឬអត់.
3. ប្រើ content APIs ពេលកម្មវិធីរបស់អ្នកអាន និងសរសេរ ឯកសារតែមួយៗ។
4. ប្រើ `run_translation` ពេល Co-op Translator ត្រូវដំណើរការ repository ដូចជា CLI។
5. ប្រើ `run_review` បន្ទាប់ពីការបកប្រែ ប្រសិនបើអ្នកត្រូវការការត្រួតពិនិត្យដែលអាចកំណត់បាននៅក្នុងស្វ័យប្រវត្តិកម្ម។

| Goal | API to start with |
| --- | --- |
| បកប្រែខ្សែអក្សរ Markdown ឬឯកសារមួយ | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| អនុញ្ញាតឲ្យភ្នាក់ងារម្ចាស់ម៉ាស៊ីន (host agent) បកប្រែផ្នែក Markdown ឬកញ្ចប់ notebook | `start_markdown_agent_translation` ឬ `start_notebook_agent_translation` |
| សរសេរឡើងវិញតំណភ្ជាប់ដែលបានបកប្រែក្រោយពីជ្រើសផ្លូវចេញ | `rewrite_markdown_paths` ឬ `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## សេណារីយ៉ូ 1: បកប្រែឯកសារតែម្នាក់ៗ ឬឯកសារ

ប្រើវិធីសាស្រ្តនេះពេលដែលអ្នកមានឯកសារ, editor buffer, notebook payload, សំណើ MCP, ឬការបញ្ចូល pipeline ផ្ទាល់ខ្លួន។ កូដរបស់អ្នកទទួលខុសត្រូវចំពោះ I/O ឯកសារ៖

1. Read the source content.
2. Call a content translation API.
3. ជាជម្រើស អាចហៅ API សម្រាប់រែរៀបផ្លូវ (path rewriting) ប្រសិនបើមាតិកាបកប្រែត្រូវបានសរសេរចូលទៅក្នុងថតបកប្រែរបស់គម្រោង។
4. រក្សាទុក ឬត្រឡប់លទ្ធផលពីកម្មវិធីរបស់អ្នក.

Content translation APIs មិនចូលរួមក្នុងការរកឃើញគម្រោង មិនសរសេរមេតាដាតា មិនបន្ថែមសេចក្តីពន្យល់ (disclaimers) និងមិនរៀបចំតំណភ្ជាប់ឡើងវិញដោយស្វ័យប្រវត្តិ។

### ឯកសារ Markdown

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

ប្រសិនបើ Markdown ដែលបានបកប្រែ មិនទាក់ទងនឹងផ្នែកផែនការគម្រោង Co-op Translator សូមលែងហៅ `rewrite_markdown_paths` ហើយរក្សាទុកស្រង់អក្សរដែលបានបកប្រែដោយផ្ទាល់។

### ឯកសារ Notebook

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

`translate_notebook_content` បកប្រែកោសិកា Markdown និងរក្សាកោសិកាផ្សេងៗដែលមិនមែន Markdown. ការសរសេរឡើងវិញផ្លូវត្រូវអនុវត្តតែកំពុងចំពោះកោសិកា Markdown.

### ឯកសាររូបភាព

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

`translate_image_content` អានរូបភាពប្រភព និងត្រឡប់ជា `PIL.Image.Image` ដែលបានបញ្ចេញ. វាមិនសរសេរមេតាដាតារូបភាពដែលបានបកប្រែ.

## សេណារីយ៉ូ 2: បកប្រែឃ្លាំងទាំងមូល

ប្រើវិធីសាស្រ្តនេះពេលអ្នកចង់ឲ្យ Python API បំពេញដូច CLI `translate`។ `run_translation` ស្វែងរកឯកសារដែលគាំទ្រ បកប្រែប្រភេទមាតិកាដែលបានជ្រើស រៀបចំផ្លូវ(path) សរសេរ​ឯកសារចេញ បន្ទាន់សម័យមេតាដាតា និងអនុវត្តភារកិច្ចថែទាំបកប្រែ ដូចជា ការ​សម្អាត។

`run_translation` គឺជាចំណុចចូលដែលពេញចិត្តសម្រាប់រៀបចំគម្រោង។ `translate_project` ត្រូវបាននាំចេញជាឈ្មោះជំនួសសម្រាប់ភាពផ្គូផ្គងដែលមានអាកប្បកម្មដូចគ្នា។

បកប្រែឯកសារ Markdown ក្នុង repository បច្ចុប្បន្នទៅជាភាសាកូរ៉េ និងជប៉ុន៖

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

បកប្រែតែសៀវភៅកំណត់ត្រា (notebooks) ពីឫសគម្រោងជាក់លាក់:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ពិនិត្យមើលបរិមាណការបកប្រែដោយ​មិន​សរសេរ​ឯកសារ៖

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

កត់ត្រាព្រឹត្តិការណ៍វឌ្ឍនភាពដែលមានទ្រង់ទ្រាយសម្រាប់ការរួមបញ្ចូល៖

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # ផ្ទុកទិន្នន័យទៅក្នុងតារាងព្រឹត្តិការណ៍ការងាររបស់អ្នក ឬផ្សាយវាទៅ UI របស់អ្នក។


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Events use the versioned schema `co-op.translation.event.v1`. Integrations should
depend on stable fields such as `type` and `stage_key`, not on human-facing
console text or `stage_label`.

បកប្រែឫសមាតិកាច្រើនក្នុងការហៅ​មួយ:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

សរសេរការបកប្រែក្នុងក្រុមលទ្ធផលដែលកំណត់ជាក់លាក់:

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

ប្រើកន្លែងទុកពាក្យសម្រាប់រៀងរាល់ភាសា ពេលដែលរាល់ភាសាត្រូវមានថតរង nested subdirectory៖

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

ប្រសិនបើមួយណាមួយក្នុងចំណោម `markdown`, `notebook`, ឬ `images` មិនត្រូវបានកំណត់ទេ API នឹងបកប្រែប្រភេទទាំងអស់ដែលគាំទ្រ៖ Markdown, notebooks, និងរូបភាព។

### រក្សាទុកការកែដោយមនុស្សដែលទទួលយកជាមួយអ្នកផ្ដល់ស្ថានភាពបកប្រែ

ដោយលំនាំដើម Co-op Translator រក្សាទុកអាកប្បកិរិយារបស់វាកម្រិតឯកសារ៖ នៅពេលដែល
ប្រភព Markdown មិនទាន់ទាន់សម័យ (stale), ឯកសារបកប្រែទាំងមូល នឹងត្រូវបានបង្កើតឡើងវិញ។ ការរួមបញ្ចូលដែលផ្ទុក
អាចជាជម្រើសផ្ញើ `TranslationStateProvider` ដើម្បីរក្សា
ការកែសម្រួលដោយមនុស្សនៅក្នុងប្លុកប្រភពដែលមិនបានផ្លាស់ប្ដូរទេ។

អ្នកផ្ដល់នេះផ្គត់ផ្គង់គูប្រភព/គោលដៅចុងក្រោយដែលបានទទួលយក និងកត់ត្រាបេក្ខជនថ្មីៗ។
ការយល់ព្រមនៅតែជាទំនួលខុសត្រូវរបស់ការរួមបញ្ចូល—ឧទាហរណ៍,
បន្ទាប់ពីសំណើ 'pull request' សម្រាប់ការបកប្រែត្រូវបានបញ្ចូល:

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

សម្រាប់ឯកសារ Markdown ដែលមានគម្រប់មូលដ្ឋាន (accepted baseline) ត្រឹមត្រូវ Co-op Translator នឹងសម្របសម្រួល
ប្លុក Markdown កម្រិតខ្ពស់។ ប្លុកប្រភពដែលមិនបានផ្លាស់ប្តូរនឹងប្រើវិញប្លុកដែលបានបកប្រែបច្ចុប្បន្ន
ប្លុក ដោយរួមមានការកែប្រែដែលធ្វើដោយមនុស្ស; ប្លុកប្រភពដែលបានផ្លាស់ប្តូរ ឬបានបន្ថែមនឹងត្រូវផ្ញើ
សម្រាប់ការបកប្រែ; ប្លុកប្រភពដែលបានលុបត្រូវបានដកចេញ។ ប្រសិនបើការសម្របសម្រួលមិនច្បាស់,
រចនាសម្ព័ន្ធគោលដៅបានផ្លាស់ប្ដូរ, ការបកប្រែប្លុកមួយមិនត្រឹមត្រូវ, ឬគ្មានគម្រប់មូលដ្ឋាន
ទេ Co-op Translator នឹងត្រឡប់ទៅលទ្ធវិធីបកប្រែឯកសារ​ទាំងមូល​ដែលមានស្រាប់ដោយសុវត្ថិភាព
ផ្លូវបកប្រែ។

API នេះផ្ទុកស្ថានភាពការបកប្រែឯកសារ មិនមែនជា​មេម៉ូរីបកប្រែសម្រាប់ឃ្លា ឬផ្នែកពីឯកសារផ្សេងៗទេ។
វាបច្ចុប្បន្នអនុវត្តចំពោះការបកប្រែគម្រោង Markdown
បកប្រែ។ ការប្រព្រឹត្តិរបស់ Notebook និងរូបភាពមិនបានផ្លាស់ប្ដូរ។ ការបញ្ជូន `update=True`
នៅតែស្នើសុំការបង្កើតឡើងវិញទាំងស្រុង។

ប្រសិនបើឯកសារមួយឬច្រើនមិនអាចបកប្រែបាន `run_translation` នឹងលើក
`RuntimeError` បន្ទាប់ពីដំណើរការ​គម្រោងបញ្ចប់ ផ្ទុយពីការរាយការណ៍ថា
ដំណើរការជោគជ័យដែលមានលទ្ធផលខ្វះ។ ការរួមបញ្ចូលគួររាប់នេះថាជាការងារបរាជ័យ
ហើយរក្សាស្ថានភាពបកប្រែដែលបានទទួលយកមុន។

## ពិនិត្យលទ្ធផលដែលបានបកប្រែ

`run_review` បំពេញការត្រួតពិនិត្យការបកប្រែដែលកំណត់ដោយមិនត្រូវការសក្ខីបត្រ LLM ឬ Vision។

!!! note "Beta"
    `run_review` គឺជា API ពិនិត្យប្រភេទ beta ដែលផ្តល់ការត្រួតពិនិត្យដែលអាចកំណត់បាន។ វាមិនហៅអ្នកផ្តល់ម៉ូដែល ឬសរសេរឯកសារ ទេ ប៉ុន្តែការត្រួតពិនិត្យ និងរាងស.schemas បញ្ហាអាចអភិវឌ្ឍបាន។

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

បន្ទាប់ពីការ​បកប្រែ README តែតែមួយ សូមប្រើដែនកំណត់ដូចគ្នាសម្រាប់ការពិនិត្យ៖

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` reviews only `README.md` under each configured source root,
including custom `groups` and output directories. Other documents and nested
READMEs are excluded. A missing source README raises `ValueError`; failed
translation checks raise `RuntimeError`.

ពិនិត្យតែឯកសារដែលបានផ្លាស់ប្តូរទៅប្រកួតជាមួយ base ref ហើយបោះពុម្ពលទ្ធផលទម្រង់ GitHub៖

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

## ឧទាហរណ៍ API សម្រាប់ចម្លង និង បិទ

បកប្រែមាតិកា Markdown ដោយមិនសរសេរ​ឯកសារ:

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

## ចំណុចចូលសាធារណៈ

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

## API សម្រាប់បកប្រែ​មាតិកា

Content translation APIs ត្រូវបានដាក់ឲ្យសាកសមសម្រាប់ការរួមបញ្ចូលដែលមានមាតិកានៅក្នុងភេទ memory មុនរួច ដូចជា ការពង្រីក editor, ឧបករណ៍ MCP, ព្រីសេសស័រ notebook, ឬ pipeline ម៉ាស៊ីនផ្ទាល់ខ្លួន។

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. បកប្រែ​មាតិកា Markdown តែប៉ុណ្ណោះ។ វាមិនរៀបចំ​តំណភ្ជាប់ឡើងវិញ មិនសរសេរ metadata និងមិនបន្ថែមសេចក្តីពន្យល់ (disclaimers)។ |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. បកប្រែ Markdown cells និងរក្សាប្រភេទកោសិកាដែលមិនមែន Markdown។ វាមិនរៀបចំតំណភ្ជាប់ឡើងវិញ មិនសរសេរ metadata និងមិនបន្ថែមសេចក្តីពន្យល់ (disclaimers)។ |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. ដកអក្សរពីរូបភាព និងបកប្រែវា បន្ទាប់មកត្រឡប់​រូបភាពដែលបានបញ្ចាំងវិញ។ វាមិនរក្សា metadata រូបភាពដែលបានបកប្រែ។ |

`translate_markdown_content` និង `translate_notebook_content` អាចទទួលយក `source_path` ជាជម្រើសតាមរយៈជម្រើសរបស់ពួកវា។ ផ្លូវនេះត្រូវបានផ្ញើជាបរិបទទៅកាន់អ្នកបកប្រែ; អ្នកហៅនៅតែទទួលខុសត្រូវចំពោះការកែប្ដូរផ្លូវពិសេសសម្រាប់គម្រោងបន្ទាប់ពីការបកប្រែ។

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

ជម្រើសដូចគ្នានេះអាចផ្ញើជា dictionaries បាន:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API បកប្រែដោយជំនួយពីភ្នាក់ងារ

Agent-assisted APIs មិនហៅអ្នកផ្គត)L LLM ដែលបានកំណត់ពី Co-op Translator ទេ។ ពួកវា រៀបចំផ្នែក Markdown ឬ notebook សម្រាប់ host agent ដើម្បីបកប្រែ ហើយបន្ទាប់មកស្ដារមាតិកាចុងក្រោយពីផ្នែកដែលបានបកប្រែ។

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | ត្រឡប់ការងារ Markdown ដោយខ្លួនឯងដែលមានចំណែក (chunks), បញ្ជាសំណើ (prompts), និងស្ថានភាពស្ដារឡើងវិញ (reconstruction state). |
| `finish_markdown_agent_translation` | ស្ដារឡើងវិញ Markdown ពីការងារ និងចំណែកដែលបានបកប្រែដោយម៉ាស៊ីនផ្ទុក និងភ្នាក់ងារ។ |
| `start_notebook_agent_translation` | ត្រឡប់ការងារ notebook មួយដែលមានចំណែក Markdown-cell សម្រាប់ការបកប្រែដោយម៉ាស៊ីនផ្ទុក និងភ្នាក់ងារ។ |
| `finish_notebook_agent_translation` | ស្ដារឡើងវិញ JSON របស់ notebook ខណៈដែលរក្សា កូដសែល, លទ្ធផល, និងព័ត៍មានម៉េតាដាតា។ |

វិធីសាស្រ្តនេះភាគច្រើនមានគោលដៅសម្រាប់ MCP hosts។ ប្រសិនបើអ្នកចង់ការបកប្រែ repository លំដាប់ផលិតកម្ម ជាមួយ Co-op Translator គ្រប់គ្រងការហៅ provider សូមប្រើ `translate_markdown_content`, `translate_notebook_content`, ឬ `run_translation`។

## API សម្រាប់សរសេរ​ផ្លូវឡើងវិញ

Path rewriting APIs មិនអនុវត្តការបកប្រែទេ។ ពួកវា ថត​បំលែងតំណភ្ជាប់ និងផ្លូវ frontmatter បន្ទាប់ពីអ្នកហៅដឹងពី path ប្រភព path គោលដៅដែលបានបកប្រែ និងលំនាំគម្រោង។

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | បន្សំផ្លាស់ប្ដូរ តំណភ្ជាប់ Markdown និងវាលផ្លូវ frontmatter ដែលគាំទ្រសម្រាប់គោលដៅដែលបានបកប្រែ។ |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | អនុវត្តការរៀបចំផ្លូវ Markdown ទៅលើកោសិកា Markdown មួយៗ និងទុកឱ្យកោសិកាដែលមិនមែន Markdown មិនផ្លាស់ប្ដូរ។ |

អាគុយម៉ង់ `policy` អាច​ជា dictionary ដែលមាន​វាល​ទាំងនេះ៖

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | ទេ | ប្រភេទការបកប្រែដែលបានបើក។ លំនាំដើមជា Markdown, notebooks, និង images. |
| `lang_subdir` | ទេ | ថតរងជាជម្រើសនៅក្រោមថតរាល់ភាសា។ |

## ប៉ារ៉ាម៉ែត្រ​បកប្រែ​គម្រោង

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | ចាំបាច់ | កូដភាសាគោលដៅដែលបំបែកដោយចន្លោះ ដូចជា `"ko ja fr"` ឬ `"all"`។ កូដជំនួសត្រូវបានធម្មតាទៅតាមតម្លៃគោល BCP 47។ |
| `root_dir` | `str` | `"."` | ឫសគម្រោងសម្រាប់គោលដៅបកប្រែមួយ។ ត្រូវបានរំលងនៅពេលដែល `root_dirs` ឬ `groups` ត្រូវបានផ្គត់ផ្គង់។ |
| `update` | `bool` | `False` | លុប និងបង្កើតឡើងវិញការបកប្រែដែលមានស្រាប់សម្រាប់ភាសាទាំងដែលបានជ្រើស។ |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | រក្សា​ឯកសារ​កំណត់ហេតុ​កម្រិត DEBUG នៅក្រោមថតរុន `logs/`។ |
| `yes` | `bool` | `True` | បញ្ជាក់ដោយស្វ័យប្រវត្តិលើការទាមទារសម្រាប់ការប្រើប្រាស់ដោយកម្មវិធី និង CI។ |
| `add_disclaimer` | `bool` | `False` | បន្ថែមចំណាំថាជាបកប្រែដោយម៉ាស៊ីនទៅក្នុង Markdown និងសៀវភៅកំណត់ត្រាដែលបានបកប្រែ។ |
| `translations_dir` | `str \| None` | `None` | ថតលទ្ធផលសម្រាប់បកប្រែអត្ថបទ។ ផ្លូវទាក់ទងនឹងត្រូវដោះស្រាយទៅនឹង root រាល់មួយ។ |
| `image_dir` | `str \| None` | `None` | ថតលទ្ធផលសម្រាប់រូបភាពដែលបានបកប្រែ។ ផ្លូវទាក់ទងនឹងត្រូវដោះស្រាយទៅនឹង root រាល់មួយ។ |
| `root_dirs` | `Iterable[str] \| None` | `None` | Root ច្រើនដែលចែករំលែកការកំណត់លទ្ធផលដូចគ្នា។ |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | គូ `(root_dir, translations_dir)` បញ្ជាក់ដោយច្បាស់។ មានអាទិភាពលើ `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL នៃ repository ដែលប្រើពេលបង្ហាញការណែនាំតារាងភាសានៅ README។ |
| `glossaries` | `Iterable[str] \| None` | `None` | ពាក្យក្នុងនិយមន័យដែលត្រូវរក្សា​នៅពេលបកប្រែ។ ពាក្យដែលដូចគ្នា និងពាក្យទទេ នឹងត្រូវធម្មតា។ |
| `dry_run` | `bool` | `False` | ប៉ាន់ស្មានបរិមាណបកប្រែ និងមើលមុនអំពីអាកប្បកិរិយាការផ្លាស់ទីដោយមិនសរសេរ​ឯកសារ។ |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | ជាជម្រើសសម្រាប់ adapter សម្រាប់ accepted-baseline និង candidate persistence សម្រាប់ការអាប់ដេត Markdown ជាបន្តបន្ទាប់។ បើមិនបញ្ជាក់ទេ នឹងរក្សា​អត្តចរិតកំណត់ឯកសារពេញលេញ។ |

## ប៉ារ៉ាម៉ែត្រពិនិត្យ

`run_review` មានគោលបំណងស្រដៀងនឹង signature របស់ `run_translation` នៅកន្លែងដែលអាចធ្វើបាន ដូច្នេះ automation អាចប្ដូរវិញពី workflow បកប្រែទៅពិនិត្យដោយមាន branching តិចតួច។

| ប៉ារ៉ាម៉ែត្រ | ប្រភេទ | លំនាំដើម | គោលបំណង |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | ថតភាសាគោលដៅដែលត្រូវពិនិត្យ។ អត្ថលេខដែលចំរុះដោយចន្លោះ និង iterable ទាំងឡាយត្រូវបានទទួលយក។ `"all"` នឹងពិនិត្យភាសាបកប្រែទាំងអស់ដែលត្រូវបានរកឃើញ។ |
| `root_dir` | `str` | `"."` | Root នៃគម្រោងសម្រាប់គោលដៅពិនិត្យមួយ។ មិនបានយកចិត្តទុកដាក់នៅពេល `root_dirs` ឬ `groups` ត្រូវបានផ្ដល់។ |
| `markdown` | `bool` | `False` | រួមបញ្ចូលឯកសារ​ប្រភព Markdown និង MDX។ |
| `notebook` | `bool` | `False` | រួមបញ្ចូលឯកសារ​ប្រភព Jupyter notebook។ |
| `images` | `bool` | `False` | រក្សាទុកសម្រាប់ភាពស្រដៀងជាមួយជម្រើសបកប្រែ។ ឯកសារយោងតំណរទៅរូបភាពត្រូវបានពិនិត្យពីក្នុង Markdown។ |
| `translations_dir` | `str \| None` | `None` | ថតលទ្ធផលសម្រាប់បកប្រែអត្ថបទ។ ផ្លូវទាក់ទងនឹងត្រូវដោះស្រាយទៅនឹង root រាល់មួយ។ |
| `root_dirs` | `Iterable[str] \| None` | `None` | Root ច្រើនដែលចែករំលែកការកំណត់លទ្ធផលដូចគ្នា។ |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | គូ `(root_dir, translations_dir)` បញ្ជាក់ដោយច្បាស់។ មានអាទិភាពលើ `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref ដែលប្រើដើម្បីកំណត់ការពិនិត្យទៅលើឯកសារប្រភពដែលបានផ្លាស់ប្ដូរ។ |
| `readme_only` | `bool` | `False` | ពិនិត្យតែ `README.md` ខាងក្រោម root ប្រភពនីមួយៗ។ ប្រសិនបើ README ប្រភពអត់មាន នឹងធ្វើឲ្យកើត `ValueError`។ |
| `output_format` | `str` | `"text"` | ទ្រង់ទ្រាយលទ្ធផលសម្រាប់ពិនិត្យ។ តម្លៃដែលគាំទ្រមាន `"text"` និង `"github"`។ |
| `fail_on_warnings` | `bool` | `False` | ធ្វើឲ្យការព្រមានត្រូវបានគេចាត់ទុកជាការបរាជ័យ បន្ថែមលើកំហុស។ |
| `debug` | `bool` | `False` | បើកកំណត់ហេតុ debug។ |
| `save_logs` | `bool` | `False` | រក្សាទុកឯកសារកំណត់ហេតុ մակարդឹ DEBUG នៅក្រោមថត root `logs/`។ |

ប្រសិនបើ `markdown`, `notebook`, ឬ `images` មិនត្រូវបានកំណត់ API នឹងពិនិត្យ Markdown, notebooks, និង ឯកសារយោងតំណររូបភាពនៅកន្លែងដែលអាចប្រើបាន។ ការពិនិត្យមិនហៅអ្នកផ្គត់ផ្គង់ LLM ទេ ហើយមិនទាមទារកូនសោ API។

## តម្រូវការការកំណត់រចនាសម្ព័ន្ធ

API បកប្រែដែលផ្អែកលើ provider ត្រូវការការកំណត់ provider មុនពេលបកប្រែ៖

- ការបកប្រែ Markdown និង notebook ត្រូវការអ្នកផ្គត់ផ្គង់ LLM។ សូមកំណត់រចនាសម្ព័ន្ធ Azure OpenAI, OpenAI ឬ Anthropic។
- ការបកប្រែរូបភាពត្រូវការការកំណត់ Azure AI Vision បូកជាមួយអ្នកផ្គត់ផ្គង់ LLM។
- `run_translation` ប្រតិបត្តិការត្រួតពិនិត្យការតភ្ជាប់ទំហំស្រាល មុនការចាប់ផ្ដើមបកប្រែគម្រោង។
- API ជួយដោយភ្នាក់ងារ `start_*_agent_translation` និង `finish_*_agent_translation` មិនហៅអ្នកផ្គត់ផ្គង់ LLM របស់ Co-op Translator ទេ។ កម្មវិធីដៃគோឬភ្នាក់ងារ MCP នឹងបកប្រែចំណែកដែលបានរៀបចំ។
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, និង `run_review` មានលទ្ធផលកំណត់ និងមិនទាមទារ provider credentials។

អថេរ Azure OpenAI ត្រូវការៈ

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

អថេរ OpenAI ត្រូវការៈ

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

អថេរ Anthropic ត្រូវការៈ

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` និង `ANTHROPIC_MAX_TOKENS` គឺជាជម្រើស។ Microsoft Agent Framework ជា client ម៉ូឌែលលំនាំដើមសម្រាប់អ្នកផ្គត់ផ្គង់ទាំងអស់ ចាប់ពី Co-op Translator 0.22.0។ Semantic Kernel អាចត្រូវបានជ្រើសជាលក្ខណៈបណ្តោះអាសន្នជាមួយ `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, ប៉ុន្តែការធ្វើដូចនេះនឹងបញ្ចេញការព្រមានលុបចោល; សូមមើល [កំណត់រចនាសម្ព័ន្ធ](configuration.md#model-client-backend) សម្រាប់ផែនការលុបចេញជាជំហាន។

អថេរ Azure AI Vision ត្រូវការ​សម្រាប់ការបកប្រែរូបភាពៈ

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` មានលទ្ធផលកំណត់ និងមិនទាមទារការកំណត់រចនាសម្ព័ន្ធ LLM ឬ Azure AI Vision។

## កំណត់សម្គាល់អាកប្បកិរិយា

- API បកប្រែខ្លឹមសារ រក្សាការបកប្រែក្នុងវិលផ្សេងពីការកែផ្លូវគម្រោង។ សូមហៅ `rewrite_markdown_paths` ឬ `rewrite_notebook_paths` ឲ្យច្បាស់ ពេលខ្លឹមសារដែលបានបកប្រែ ត្រូវការកែសម្រួលតំណរទាក់ទងនឹងគម្រោងសម្រាប់ទីតាំងគោលដៅ។
- API សម្របសម្រួលគម្រោងបន្ថែមអាកប្បកិរិយាជុំវិញការបកប្រែខ្លឹមសារ រួមមាន ការរកឃើញឯកសារ, ការសរសេរ, ការកែផ្លូវ, មេតាដាតា, ការសំអាត, និងចំណាំជាជម្រើស។
- `run_translation` បោះពុម្ពវិវត្តន៍និងសង្ខេបការប៉ាន់ស្មាន តាមរយៈអ្នករាយការណ៍ដែលគាំទ្រ Rich ដូចដែល CLI ប្រើ។ លទ្ធផលដែលមិនមានអន្តរកម្ម នឹងវិលមកជាអត្ថបទសាមញ្ញ។
- `dry_run=True` គណនាការប៉ាន់ស្មានដោយប្រើការអាប់ដេត README និមិត្តរូប ប៉ុន្តែមិនសរសេរ README ឬឯកសារបកប្រែទេ។
- `groups` ត្រូវបានដំណើរការជាស៊េរី។ សេចក្តីប៉ាន់ស្មានសរុបតែមួយត្រូវបានបោះពុម្ពមុនពេលការងារ​ចាប់ផ្ដើម។
- នៅពេលជ្រើសបកប្រែរូបភាព ការខ្វះកំណត់រចនាសម្ព័ន្ធ Vision នឹងបង្កើនកំហុសមុនពេលការបកប្រែចាប់ផ្ដើម។
- ថតភាសាដែលមាន alias នៅស្រាប់ ត្រូវបានរកឃើញ ហើយអាចត្រូវបានផ្លាស់ទីទៅឈ្មោះថតភាសា canonical BCP 47 ជាផ្នែកនៃការប្រតិបត្តិ។
- `run_review` នឹងបរាជ័យនៅលើឯកសារបកប្រែដែលខ្វះ, មេតាដាតាបកប្រែដែលខ្វះឬចាស់, Markdown frontmatter/កូដ fences ដែលខូចទ្រង់ទ្រាយ, និង JSON នៃ notebook ត្រូវបានបកប្រែដែលមិនត្រឹមត្រូវ។
- `run_review` របាយការណ៍ពីគោលដៅ Markdown និងតំណររូបភាពក្នុងស្រុកដែលខ្វះជាព្រមានដោយលំនាំដើម។

## ផ្លូវហៅក្នុង

API ចាត់ទុកការទាញទៅកាន់អនុវត្តមូលដ្ឋានដូចគ្នាដដែលដែល CLI ប្រើ៖

ការបកប្រែ:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` សម្រាប់ការបកប្រែក្នុងអង្គចងចាំ។
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` សម្រាប់ការកែសម្រួលផ្លូវក្រោយដល់យ៉ាងច្បាស់។
3. `co_op_translator.api.translation.run_translation` សម្រាប់ការសម្របសម្រួលគម្រោងទាំងមូល។
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. មិចស៊ីនផ្តោតសម្រាប់ការបកប្រែក្នុងគម្រោង​សម្រាប់ Markdown, notebooks, និងរូបភាព។
8. កម្មវិធីបកប្រែ Markdown, notebook, text និង image នៅក្រោម `co_op_translator.core`។

ការពិនិត្យ:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. ការត្រួតពិនិត្យដែលមានលទ្ធផលកំណត់ (deterministic) នៅក្រោម `co_op_translator.review.checks`

ថ្នាក់ដូចខាងក្រោមមានប្រយោជន៍សម្រាប់អ្នកថែទាំ ប៉ុន្តែមិនត្រូវបាននាំចេញជាតំណ API កម្រិតស្ថិរភាពនៅលើកញ្ចប់។

| ថ្នាក់ | ម៉ូឌុល | កាតព្វកិច្ច |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | សម្របសម្រួលការបកប្រែក្នុងកម្រិតគម្រោង, ការគ្រប់គ្រងថត, ការធម្មតាមេតាដាតាក្នុងមួយភាសា, និង delegation ទៅអ្នកបកប្រែ Markdown, notebook, និងរូបភាព។ |
| `TranslationManager` | `co_op_translator.core.project.translation` | អនុវត្តការប្រតិបត្តិការដំណើរការឯកសារដោយ async សម្រាប់ Markdown, notebooks, រូបភាព, ការរកឃើញ stale, និងការអាប់ដេតមេតាដាតាបកប្រែ។ |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | រៀបចំការអានឯកសារ Markdown, បកប្រែខ្លឹមសារ, កែផ្លូវ, មេតាដាតា, ចំណាំ, និងការសរសេរ។ |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | រៀបចំការអានឯកសារ notebook, បកប្រែកោសិកា Markdown, កែផ្លូវ, មេតាដាតា, ចំណាំ និងការសរសេរ។ |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | រៀបចំការរកឃើញរូបភាពប្រភព, បកប្រែរូបភាព, ផ្លូវលទ្ធផល, មេតាដាតា, និងការសរសេរ។ |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | ស្វែងរកគូ Markdown ដែលបានបកប្រែ, វាយតម្លៃគុណភាពបកប្រែ, និងអានមេតាដាតាគុណភាពជំនឿសម្រាប់ workflow ជួសជុលក្នុងករណីទំនុកចិត្តទាប។ |
| `ReviewRunner` | `co_op_translator.review.runner` | សម្របសម្រួលការត្រួតពិនិត្យដែលមានលទ្ធផលកំណត់ តាមឯកសារប្រភព, ភាសាគោលដៅ, និង root បកប្រែដែលបានកំណត់។ |
| `ReviewTarget` | `co_op_translator.review.targets` | ពិពណ៌នាអំពី root ប្រភព និងថតលទ្ធផលបកប្រែដែលត្រូវបានពិនិត្យសម្រាប់ root នោះ។ |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | រកឃើញថតភាសា alias បុរាណ និង រៀបចំផែនការផ្ទេរទៅឈ្មោះថតភាសា canonical BCP 47។ |
| `Config` | `co_op_translator.config.base_config` | ផ្ទុក `.env` files និងពិនិត្យថាតើអ្នកផ្គត់ផ្គង់ LLM ដែលត្រូវការ និង Vision ជាជម្រើស ត្រូវបានកំណត់រួចឬទេ។ |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | រកឃើញដោយស្វ័យប្រវត្តិ Azure OpenAI, OpenAI, ឬ Anthropic, ពិនិត្យអថេរបរិស្ថិតដែលត្រូវការ, និងដំណើរការត្រួតពិនិត្យភាពភ្ជាប់របស់ provider។ |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | រកឃើញការកំណត់ Azure AI Vision និងដំណើរការត្រួតពិនិត្យភាពភ្ជាប់សម្រាប់ការបកប្រែរូបភាព។ |