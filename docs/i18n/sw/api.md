# API ya Python

API ya umma ya Python imethibitishwa inatolewa kutoka `co_op_translator.api`. Mwingiliano nyingi hutumia moja ya mitiririko ifuatayo:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Moduli nyingi za ngazi ya chini chini ya `core`, `config`, `review`, na `utils` ni maelezo ya utekelezaji yanayotumika na hizi sehemu za kuingia za API.

Wateja wa MCP wanatumia API ya umma kupitia [MCP Server](mcp.md). Tumia ukurasa huu unapochukua Python moja kwa moja, na mwongozo wa MCP unapofungua Co-op Translator kwa wakala au mhariri. Ikiwa unaamua kati ya CLI, API ya Python, na MCP, anza na [Choose Your Workflow](workflows.md).

## Mtiririko wa API kwa Mara ya Kwanza

Anza hapa ikiwa unaita Co-op Translator kutoka kwa msimbo wa Python:

1. Sanidi mtoa LLM kama ilivyoelezwa katika [Configuration](configuration.md), isipokuwa unapangilia tu vipande vya Markdown au notibuki kwa tafsiri ya mwenyeji-wakala.
2. Amua ikiwa programu yako inamiliki I/O ya faili.
3. Tumia API za maudhui wakati programu yako inasoma na kuandika faili binafsi.
4. Tumia `run_translation` wakati Co-op Translator inapaswa kuchakata hifadhi kama CLI.
5. Tumia `run_review` baada ya tafsiri ikiwa unahitaji ukaguzi wa deterministic katika automatisering.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Senario 1: Tafsiri Faili au Nyaraka Binafsi

Tumia mtiririko huu wakati tayari una faili, buffer ya mhariri, payload ya notibuki, ombi la MCP, au pembejeo ya pipeline maalum. Msimbo wako unamiliki I/O ya faili:

1. Soma maudhui ya chanzo.
2. Ita API ya tafsiri ya maudhui.
3. Hiari: ita API ya kuandika upya njia ikiwa maudhui yaliyotafsiriwa yataandikwa kwenye folda ya tafsiri ya mradi.
4. Hifadhi au rudisha matokeo kutoka kwa programu yako.

API za tafsiri za maudhui hazifanyi ugunduzi wa mradi, hazandika metadata, haziongezi maandishi ya onyo, na hazibadilishi viungo kiotomatiki.

### Faili la Markdown

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

Ikiwa Markdown iliyotafsiriwa haitakuwa ndani ya mpangilio wa mradi wa Co-op Translator, skip `rewrite_markdown_paths` na hifadhi kamba iliyotafsiriwa moja kwa moja.

### Faili la Notebook

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

`translate_notebook_content` hutafsiri seli za Markdown na huhifadhi seli zisizo za Markdown. Kuandika upya njia kunatumika kwa seli za Markdown pekee.

### Faili la Picha

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

`translate_image_content` husoma picha ya chanzo na kurudisha `PIL.Image.Image` iliyochorwa. Haidai kuandika metadata ya picha iliyotafsiriwa.

## Senario 2: Tafsiri Hifadhi Nzima ya Mradi

Tumia mtiririko huu wakati unataka API ya Python ifanye kazi kama CLI ya `translate`. `run_translation` hugundua faili zinazotambuliwa, hutafsiri aina za maudhui zilizochaguliwa, huandika upya njia, huandika faili za matokeo, huweka metadata, na hufanya kazi za matengenezo ya tafsiri kama kusafisha.

`run_translation` ni nukta inayopendekezwa ya kuandaa miradi. `translate_project` hutolewa kama jina la urudufu lenye tabia ile ile.

Tafsiri faili za Markdown katika hifadhi ya sasa kuwa Kikorea na Kijapani:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Tafsiri notibuki pekee kutoka mzizi maalum wa mradi:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Angalia kiasi cha tafsiri bila kuandika faili:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Tafsiri mizizi mingi ya maudhui kwa wito mmoja:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Andika tafsiri ndani ya makundi maalum ya matokeo:

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

Tumia nafasi ya kujaza kwa kila lugha wakati kila lugha inapaswa kuwa na saraka ndogo iliyojengwa ndani:

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

Ikiwa hakuna `markdown`, `notebook`, au `images` iliyowekwa, API itatafsiri aina zote zinazotambulika: Markdown, notibuki, na picha.

## Kagua Matokeo ya Tafsiri

`run_review` hufanya ukaguzi wa tafsiri wa deterministic bila sifa za LLM au Vision.

!!! note "Beta"
    `run_review` ni API ya ukaguzi wa deterministic inayoko katika beta. Haipigi watoa modeli au kuandika faili, lakini ukaguzi na mifumo ya masuala yanaweza kubadilika.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Kagua faili zilizobadilika tu dhidi ya ref ya msingi na chapeza matokeo yenye ladha ya GitHub:

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

## Mifano ya API za Nakili-na-Kubandika

Tafsiri maudhui ya Markdown bila kuandika faili:

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

Tafsiri na andika upya viungo vya Markdown:

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

Tafsiri hifadhi kutoka Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Tafsiri mizizi mingi:

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

Hifadhi maneno ya leksikari:

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

## Sehemu za Kuingia za Umma

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

## API za Tafsiri za Maudhui

API za tafsiri za maudhui zimetengenezwa kwa mwingiliano ambao tayari wana maudhui kwa kumbukumbu, kama ugani wa mhariri, zana ya MCP, processor ya notibuki, au pipeline maalum.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Asinkroni. Hutafsiri maudhui ya Markdown pekee. Haiandiki upya viungo, haiandiki metadata, wala haiiongezi disclaimer. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Asinkroni. Hutafsiri seli za Markdown na huhifadhi seli zisizo za Markdown. Haiandiki upya viungo, haiandiki metadata, wala haiiongezi disclaimer. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Sinkroni. Hutokana na kutoa na kutafsiri maandishi ya picha, kisha inarudisha picha iliyopakwa. Haihifadhi metadata ya picha iliyotafsiriwa. |

`translate_markdown_content` na `translate_notebook_content` zinakubali `source_path` chaguo katika chaguzi zao. Njia inapitishwa kama muktadha kwa mtafsiri; wito wanabaki kuwajibika kwa uandishi maalum wa mradi baada ya tafsiri.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Chaguzi zile zile zinaweza kupitishwa kama kamusi:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API za Tafsiri Zinazosaidiwa na Wakala

API zinazosaidiwa na wakala hazipigi Azure OpenAI au OpenAI kutoka Co-op Translator. Zinaunda vipande vya Markdown au notibuki kwa wakala mwenyeji kutafsiri, kisha kujenga tena maudhui ya mwisho kutoka kwa vipande vilivyotafsiriwa.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

Mtiririko huu kwa kawaida umetumika kwa mwenyeji wa MCP. Ikiwa unahitaji tafsiri ya hifadhi kwa uzalishaji na Co-op Translator ikisimamia wito wa mtoa huduma, tumia `translate_markdown_content`, `translate_notebook_content`, au `run_translation`.

## API za Kuandika Upya Njia

API za kuandika upya njia hazitekelezi tafsiri. Zinaboresha viungo na njia za frontmatter baada ya wito kujua njia ya chanzo, njia ya lengo iliyotafsiriwa, na mpangilio wa mradi.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

Hoja `policy` inaweza kuwa kamusi yenye mashamba haya:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Defaults to Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## Vigezo vya Tafsiri ya Mradi

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Space-separated target language codes, such as `"ko ja fr"`, or `"all"`. Alias codes are normalized to canonical BCP 47 values. |
| `root_dir` | `str` | `"."` | Project root for a single translation target. Ignored when `root_dirs` or `groups` are supplied. |
| `update` | `bool` | `False` | Delete and recreate existing translations for the selected languages. |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files under the root `logs/` directory. |
| `yes` | `bool` | `True` | Auto-confirm prompts for programmatic and CI usage. |
| `add_disclaimer` | `bool` | `False` | Add machine translation disclaimers to translated Markdown and notebooks. |
| `translations_dir` | `str \| None` | `None` | Custom text translation output directory. Relative paths resolve against each root. |
| `image_dir` | `str \| None` | `None` | Custom translated image output directory. Relative paths resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Multiple roots that share the same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. Takes precedence over `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository URL used when rendering README language table guidance. |
| `glossaries` | `Iterable[str] \| None` | `None` | Glossary terms to preserve during translation. Duplicates and blank terms are normalized. |
| `dry_run` | `bool` | `False` | Estimate translation volume and preview migration behavior without writing files. |

## Vigezo vya Ukaguzi

`run_review` kwa makusudi inalingana na saini ya `run_translation` pale inapowezekana ili automatisering iweze kubadilisha kati ya mitiririko ya tafsiri na ukaguzi kwa kupungua kwa mageuzi.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Saraka ya pato ya tafsiri ya maandishi kwa desturi. Njia za relative hutatuliwa kwa kila mzizi. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mizizi mingi inayoshiriki mipangilio sawa ya pato. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Jozi wazi za `(root_dir, translations_dir)`. Inachukua kipaumbele kuliko `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git ref inayotumika kupunguza uhakiki kwa faili za chanzo zilizobadilika. |
| `output_format` | `str` | `"text"` | Aina ya pato la uhakiki. Thamani zinazotumika ni `"text"` na `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Chukulia maonyo kama kushindwa pamoja na makosa. |
| `debug` | `bool` | `False` | Washa ufuatiliaji/ulezaji wa debug. |
| `save_logs` | `bool` | `False` | Hifadhi faili za log za ngazi ya DEBUG chini ya saraka ya mzizi `logs/`. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Mahitaji ya Usanidi

Provider-backed translation APIs require provider configuration before translating:

- Markdown and notebook translation require an LLM provider. Configure either Azure OpenAI or OpenAI.
- Image translation requires Azure AI Vision in addition to the LLM provider.
- `run_translation` runs lightweight connectivity checks before project translation begins.
- Agent-assisted `start_*_agent_translation` and `finish_*_agent_translation` APIs do not call Co-op Translator LLM providers. The host application or MCP agent translates the prepared chunks.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, and `run_review` are deterministic and do not require provider credentials.

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

`run_review` is deterministic and does not require Azure OpenAI, OpenAI, or Azure AI Vision configuration.

## Vidokezo vya Tabia

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## Njia ya Mwito ya Ndani

The API delegates to the same core implementation used by the CLI:

Tafsiri:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

Uhakiki:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Inaendesha tafsiri ya ngazi ya mradi, usimamizi wa saraka, urekebishaji wa metadata kwa kila lugha, na kupitisha kazi kwa watafsiri wa Markdown, daftari, na picha. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Hufanya kazi za usindikaji faili zisizo za sinkrono kwa Markdown, daftari, picha, kugundua zilizo za zamani, na masasisho ya metadata ya tafsiri. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Inaoratibu kusoma faili za Markdown, tafsiri ya maudhui, kurekebisha njia, metadata, matangazo ya hiari, na uandishi. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Inaoratibu kusoma faili za daftari, tafsiri ya seli za Markdown, kurekebisha njia, metadata, matangazo ya hiari, na uandishi. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Inaoratibu ugunduzi wa picha za chanzo, tafsiri ya picha, njia za pato, metadata, na uandishi. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Inatafuta jozi za Markdown zilizotafsiriwa, hupima ubora wa tafsiri, na husoma metadata ya uaminifu kwa workflows za ukarabati wa uaminifu mdogo. |
| `ReviewRunner` | `co_op_translator.review.runner` | Inaweka uratibu wa ukaguzi wa deterministiki kwa faili za chanzo, lugha lengwa, na mizizi ya tafsiri iliyosanidiwa. |
| `ReviewTarget` | `co_op_translator.review.targets` | Inaelezea mzizi wa chanzo na saraka ya pato ya tafsiri inayokaguliwa kwa mzizi huo. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Inagundua saraka za lugha za alias za zamani na kuandaa mipango ya uhamishaji wa saraka za lugha za BCP 47 za kawaida. |
| `Config` | `co_op_translator.config.base_config` | Inapakia faili za `.env` na kukagua ikiwa wasambazaji waliotakiwa wa LLM na wanaoweza kuchaguliwa wa Vision wamewekwa. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Inagundua moja kwa moja Azure OpenAI au OpenAI, inathibitisha vigezo muhimu vya mazingira, na inaendesha ukaguzi wa unganisho wa msambazaji. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Inagundua usanidi wa Azure AI Vision na inaendesha ukaguzi wa unganisho kwa tafsiri za picha. |