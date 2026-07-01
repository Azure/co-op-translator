# Python API

സ്ഥിരമായ പൊതു Python API `co_op_translator.api`-ൽ നിന്നാണ് എക്സ്പോർട്ട് ചെയ്യപ്പെട്ടിരിക്കുന്നത്. കൂടുതൽ ഇന്റഗ്രേഷനുകൾ ഈ വേർക്ക്ഫ്ലോകളിലൊന്നായി ഉപയോഗിക്കുന്നു:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | നിങ്ങളുടെ അപ്ലിക്കേഷൻ സോഴ്‌സ് ഉള്ളടക്കം വായിച്ച്, തർജ്ജമയ്ക്ക് Co-op Translator വിളിക്കുകയും ഫലം എവിടെയാണ് സേവ് ചെയ്യണമെന്ന് തീരുമാനിക്കുകയും ചെയ്യുന്നത്. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | നിങ്ങളുടെ MCP ഹോസ്റ്റ് അല്ലെങ്കിൽ അപ്ലിക്കേഷൻ മോഡൽ chunk കളെ തർജ്ജമ ചെയ്യും, Co-op Translator chunk ചെയ്യലും പുനർനിർമ്മാണവും കൈകാര്യം ചെയ്യും. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Python API CLI പോലെ പ്രവർത്തിച്ച് കണ്ടെത്തൽ, ഔട്ട്പുട്ട് പാതകൾ, മെറ്റാഡേറ്റ, ക്ലീൻഅപ്പ്, എഴുത്ത് എന്നിവ കൈകാര്യം ചെയ്യണമെന്ന് നിങ്ങൾക്ക് ആവശ്യമുണ്ടെങ്കിൽ. | `run_translation` |

`core`, `config`, `review`, மற்றும் `utils` എന്നിങ്ങനെ ഉള്ളതിലെ താഴത്തെ നിലയിലെ മൊഡ്യൂളുകൾ ഈ API എൻട്രി പോയിന്റുകൾ ഉപയോഗിക്കുന്ന യ имп്ലിമെന്റേഷൻ വിശദാംശങ്ങളാണ്.

MCP ക്ലയന്റുകൾ [MCP Server](mcp.md) വഴി അതേ പൊതു API ഉപയോഗിക്കുന്നു. Python നേരിട്ട് വിളിക്കുമ്പോൾ ഈ പേജ് ഉപയോഗിക്കുക, Co-op Translator ഒരു ഏജന്റിനോ എഡിറ്ററിനോ പുറത്ത് വെക്കുമ്പോൾ MCP ഗൈഡ് ഉപയോഗിക്കുക. CLI, Python API, MCP എന്നിവയിൽ തിരഞ്ഞെടുക്കാൻ പോകുന്നവർക്ക് [Choose Your Workflow](workflows.md) മുതലാക്കി തുടങ്ങുക.

## First-Time API Flow

Python കോഡിൽ നിന്ന് Co-op Translator വിളിക്കുകയാണെങ്കിൽ ഇവിടെ നിന്ന് തുടങ്ങുക:

1. [Configuration](configuration.md)-ൽ വിശദീകരിച്ചിരിക്കുന്നതുപോലെ ഒരു LLM പ്രൊവൈഡർ കോൺഫിഗർ ചെയ്യുക, അല്ലെങ്കിൽ നിങ്ങൾ മർക്ക്ഡൗൺ അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് chunk കളെ മാത്രം host-agent നു തയ്യാറാക്കുകയാണെങ്കിൽ ഇത് ഒഴിവാക്കാം.
2. നിങ്ങളുടെ അപ്ലിക്കേഷൻ ഫയൽ I/O കൈകാര്യം ചെയ്യണമോ എന്ന് തീരുമാനിക്കുക.
3. ഒരു ഫയൽ വായിച്ച് എഴുതി ചെയ്യുന്നെങ്കിൽ content APIs ഉപയോഗിക്കുക.
4. CLI പോലെയാണ് repository പ്രോസസ് ചെയ്യുന്നത് ആഗ്രഹിക്കുമ്പോൾ `run_translation` ഉപയോഗിക്കുക.
5. ഓട്ടോമേഷൻ തത്സമയ പരിശോധനകൾക്ക് `run_review` ഉപയോഗിക്കുക.

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

നിങ്ങൾക്ക് ഇതിനകം ഒരു ഫയൽ, എഡിറ്റർ ബഫർ, നോട്ട്‌ബുക്ക് പേ‌ലോഡ്, MCP റിക്വസ്റ്റ്, അല്ലെങ്കിൽ കസ്റ്റം പൈപ്പ്ലൈൻ ഇൻപുട്ട് ഉണ്ടെങ്കിൽ ഈ വേർക്ക്ഫ്ലോ ഉപയോഗിക്കുക. നിങ്ങളുടെ കോഡ് ഫയൽ I/O ന് ഉത്തരവാദിയാണ്:

1. സോഴ്‌സ് ഉള്ളടക്കം വായിക്കുക.
2. ഒരു content translation API വിളിക്കുക.
3. തർജ്ജമ ചെയ്ത ഉള്ളടക്കം ഒരു പ്രോജക്ട് തർജ്ജമ ഫോളഡറിൽ എഴുതാൻ പോകുന്നു എങ്കിൽ ഐച്ഛികമായും path rewriting API വിളിക്കുക.
4. നിങ്ങളുടെ അപ്ലിക്കേഷനിൽ നിന്ന് ഫലം സേവ് ചെയ്യുക അല്ലെങ്കിൽ റിട്ടേൺ ചെയ്യുക.

എല്ലാ content translation APIs-കളും പ്രോജക്ട് കണ്ടെത്തൽ നടത്തുകയില്ല, മെറ്റാഡേറ്റ എഴുതുകയില്ല, ഡിസ്ക്ലെയിമറുകൾ ചേർക്കുകയില്ല, ലിങ്കുകൾ ഓട്ടോമാറ്റിക്കായി പുനഃരചെയ്യുകയില്ല.

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

തർജ്ജമ ചെയ്ത Markdown Co-op Translator പ്രോജക്ട് ലേഔട്ടിൽ ഇല്ലാതെ സ്റ്റോറുചെയ്യുകയാണെങ്കിൽ, `rewrite_markdown_paths` ഒഴിവാക്കി തർജ്ജമ ചെയ്ത സ്ട്രിംഗ് നേരിട്ടു സേവ് ചെയ്യുക.

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

`translate_notebook_content` Markdown സെല്ലുകൾ തർജ്ജമ ചെയ്യുകയും നോൺ-Markdown സെല്ലുകൾ നിലനിർത്തുകയും ചെയ്യുന്നു. പാത പുനരാഖ്യാനം Markdown സെല്ലുകൾക്ക് മാത്രമേ ബാധകമാവൂ.

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

`translate_image_content` സോഴ്‌സ് ഇമേജ് വായിച്ച് ഒരു റെൻഡർ ചെയ്ത `PIL.Image.Image` റിട്ടേൺ ചെയ്യുന്നു. ഇത് തർജ്ജമ ചെയ്ത ഇമേജ് മെറ്റാഡേറ്റ സംരക്ഷിക്കില്ല.

## Scenario 2: Translate an Entire Repository

Python API CLI-യുടെ പോലെ പ്രവർത്തിക്കണമെന്ന് നിങ്ങൾക്കുണ്ടെങ്കിൽ ഈ വേർക്ക്ഫ്ലോ ഉപയോഗിക്കുക. `run_translation` പിന്തുണയുള്ള ഫയലുകൾ കണ്ടെത്തുകയും, തെരഞ്ഞെടുത്ത ഉള്ളടക്കം തരം തർജ്ജമ ചെയ്യുകയും, പാതകൾ പുനരാഖ്യാനം ചെയ്യുകയും, ഔട്ട്പുട്ട് ഫയലുകൾ എഴുതുകയും, മെറ്റാഡേറ്റ അപ්ඩേറ്റ് ചെയ്യുകയും, ക്ലീൻഅപ്പ് പോലുള്ള തർജ്ജമ പരിപാലന പ്രവർത്തനങ്ങൾ നടത്തുകയും ചെയ്യും.

`run_translation` പ്രൊജക്ട് ഓർക്കസ്ട്രേഷൻ എൻട്രി പോയിന്റ് ആയി അഭിലഷിതമാണ്. സമാന പെരുമാറ്റമുള്ള ഒരു പരാമ്യം-തൽക്കാലം അലൈസ് ആയി `translate_project` എക്സ്പോർട്ട് ചെയ്തിരിക്കുന്നു.

കറന്റ് റിപോസിറ്ററിയിലെ Markdown ഫയലുകൾ കൊറിയൻ અને ജപ്പാനീസ് ആയി തർജ്ജമ ചെയ്യുക:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ഒരു പ്രത്യേക പ്രോജക്ട് റൂട്ട്-ൽ നിന്നുള്ള നോട്ട്‌ബുക്കുകൾ മാത്രം തർജ്ജമ ചെയ്യുക:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ഫയൽ എഴുതാതെ തർജ്ജമ വോള്യം മുൻകൂട്ടി കാണിക്കുക:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ഒരേ കോൾ-ൽ متعدد കൺറെന്റ് റൂട്ടുകൾ തർജ്ജമ ചെയ്യുക:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

തർജ്മകൾ വ്യക്തമായ ഔട്ട്പുട്ട് ഗ്രൂപ്പുകളിലേക്ക് എഴുതുക:

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

പ്രത്യക്ഷത്തിൽ ഓരോ ഭാഷയ്ക്കും ഒരു nested സബ് ഡയറക്ടറി വേണമെങ്കിൽ ഓരോ ഭാഷയ്ക്കും ഒരു placeholder ഉപയോഗിക്കുക:

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

`markdown`, `notebook`, അല്ലെങ്കിൽ `images`-ൽ ഒന്നും സജ്ജമാക്കിയിട്ടില്ലെങ്കിൽ, API എല്ലാ പിന്തുണയുള്ള തരം തർജ്ജമ ചെയ്യും: Markdown, നോട്ട്‌ബുക്കുകൾ, ഇമേജ്‌സ്.

## Review Translated Output

`run_review` LLM അല്ലെങ്കിൽ Vision ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ നിർണായക തർജ്ജമ പരിശോധനകൾ നടത്തുന്നു.

!!! note "Beta"
    `run_review` ഒരു ബീറ്റാ നിർണായക റിവ്യൂ API ആണ്. ഇത് മോഡൽ പ്രൊവൈഡറുകൾ വിളിക്കുകയില്ല അല്ലെങ്കിൽ ഫയലുകൾ എഴുതുകയില്ല, എന്നാൽ ചെക്കുകളും ഇഷ്യൂ സ്കീമകളും എ evolucion ആയി മാറാം.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

ബേസ് റിഫിനോട്_changed ഉള്ള ഫയലുകൾ മാത്രം റിവ്യൂ ചെയ്യുകയും GitHub-ഫ്ലേവർഡ് ഔട്ട്പുട്ട് പ്രിന്റ് ചെയ്യുകയും ചെയ്യുക:

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

ഫയൽ എഴുതാതെ Markdown ഉള്ളടക്കം തർജ്ജമ ചെയ്യുക:

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

Markdown ലിങ്കുകൾ തർജ്ജമ ചെയ്ത് പുനരാഖ്യാനം ചെയ്യുക:

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

Python-യിൽ നിന്നു ഒരു റിപോസിറ്ററി തർജ്ജമ ചെയ്യുക:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

பல റൂട്ടുകൾ തർജ്മ ചെയ്യുക:

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

ഗ്ലോസറി പദങ്ങൾ സംരക്ഷിക്കുക:

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

Content translation APIs എഡിറ്റര്‍ എക്സ്റ്റൻഷൻ, MCP ടൂൾ, നോട്ട്‌ബുക്ക് പ്രോസസ്സർ, അല്ലെങ്കിൽ കസ്റ്റം പൈപ്പ്ലൈൻ പോലുള്ള memory-യിൽ ഉള്ള ഉള്ളടക്കം ഇതിനകം ഉണ്ടായിരിക്കുന്ന ഇന്റഗ്രേഷനുകൾക്ക് ഉദ്ദേശിച്ചവയാണ്.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Markdown ഉള്ളടക്കമാണ് മാത്രം തർജ്ജമ ചെയ്യുന്നത്. ലിങ്കുകൾ പുനരാഖ്യാനം ചെയ്യുകയില്ല, മെറ്റാഡേറ്റ എഴുതുകയില്ല, അല്ലെങ്കിൽ ഡിസ്ക്ലെയിമറുകൾ ചേർക്കുകയില്ല. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown സെല്ലുകൾ തർജ്ജമ ചെയ്യുകയും നോൺ-Markdown സെല്ലുകൾ സംരക്ഷിക്കുകയും ചെയ്യുന്നു. ലിങ്കുകൾ പുനരാഖ്യാനം ചെയ്യുകയില്ല, മെറ്റാഡേറ്റ എഴുതുകയില്ല, അല്ലെങ്കിൽ ഡിസ്ക്ലെയിമറുകൾ ചേർക്കുകയില്ല. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. ഇമേജ് ടെക്സ്റ്റ് എക്സ്ട്രാക്റ്റ് ചെയ്ത് തർജ്ജമ ചെയ്‍തു, പിന്നീട് ഒരു റെൻഡർ ചെയ്ത ഇമേജ് റിട്ടേൺ ചെയ്യുന്നു. ഇത് തർജ്ജമ ചെയ്ത ഇമേജ് മെറ്റാഡേറ്റ സേവ് ചെയ്യുകയില്ല. |

`translate_markdown_content`യും `translate_notebook_content`ും ഓൺഷണൽ `source_path` ഓപ്ഷനിലൂടെ സ്വീകരിക്കുന്നു. പാത ട്രാൻസ്ലേറ്ററിനായി കോൺടെക്സ്റ്റായി പാസ്സ് ചെയ്യപ്പെടുന്നു; callers പ്രോജക്ട്-നിർദ്ദിഷ്ട പാത പുനരാഖ്യാനം തർജ്ജമക്കു ശേഷം നിർവഹിക്കേണ്ടത് തുടരാം.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

അധികം ഓപ്ഷനുകൾ ഡിക്ഷണറിയുകൾ ആയി പാസ്സ് ചെയ്യാം:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Agent-assisted APIs Co-op Translator-ൽ നിന്ന് Azure OpenAI അല്ലെങ്കിൽ OpenAI വിളിക്കുകയില്ല. അവ Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് chunkകള്‍ host agent-ന് തർജ്ജമ ചെയ്യാൻ തയ്യാറാക്കി, തുടർന്ന് തർജ്ജമ ചെയ്ത chunk കളിൽ നിന്നു ഫൈനൽ ഉള്ളടക്കം പുനർനിർമ്മിക്കുകയാണു ചെയ്യുന്നത്.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | chunks, prompts, reconstruction state എന്നിവയോടെയുള്ള സ്വയം-അനൗദ്യോഗിക Markdown ജോബ് റിട്ടേൺ ചെയ്യുക. |
| `finish_markdown_agent_translation` | ഒരു ജോബിൽ നിന്നും host-agent തർജ്ജമ ചെയ്ത chunk കളിൽ നിന്നു Markdown പുനർനിർമ്മിക്കുക. |
| `start_notebook_agent_translation` | host-agent തർജ്ജമ ചെയ്യാനുള്ള Markdown-സെൽ chunkകളോടുള്ള ഒരു നോട്ട്‌ബുക്ക് ജോബ് റിട്ടേൺ ചെയ്യുക. |
| `finish_notebook_agent_translation` | കോഡ് സെല്ലുകൾ, ഔട്ട്പുട്ടുകൾ, മെറ്റാഡേറ്റ എന്നിവ സംരക്ഷിച്ച് നോട്ട്‌ബുക്ക് JSON പുനർനിർമ്മിക്കുക. |

ഈ വേർക്ക്ഫ്ലോ MCP ഹോസ്റ്റുകൾക്കുവേണ്ടിയാണ് പ്രധാനമായും ഉദ്ദേശിച്ചിരിക്കുന്നത്. Co-op Translator പ്രൊവൈഡർ കോളുകൾ മാനേജുചെയ്യുന്ന പ്രൊഡക്ഷൻ റിപോസിറ്ററി തർജ്ജമ വേണമെങ്കിൽ `translate_markdown_content`, `translate_notebook_content`, അല്ലെങ്കിൽ `run_translation` ഉപയോഗിക്കുക.

## Path Rewriting APIs

Path rewriting APIs എവരും തർജ്ജമ ചെയ്തിട്ടില്ല. അവ callers സോഴ്‌സ് പാത, തർജ്മിച്ച ടാർഗറ്റ് പാത, പ്രോജക്ട് ലേഔട്ട് എന്നിവ അറിയുമ്പോൾ ലിങ്കുകളും frontmatter പാതകളും അപ്ഡേറ്റ് ചെയ്യുന്നു.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | ഒരു തർജ്മിച്ച ടാർഗറ്റിനായി Markdown ലിങ്കുകളും പിന്തുണയുള്ള frontmatter പാത ഫീൽഡുകളും പുനരാഖ്യാനം ചെയ്യുന്നു. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | ഓരോ Markdown സെല്ലിനും Markdown path rewriting പ്രയോഗിക്കുന്നു, നോൺ-Markdown സെല്ലുകൾ മാറ്റം ഇല്ലാതെയാണ്. |

`policy` argument ഒരു ഡിക്ഷണറിയായിരിക്കാമെന്ന് ഈ ഫീൽഡുകൾ അടങ്ങിയിരിക്കാം:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | ലക്ഷ്യ ഭാഷ കോഡ്, ഉദാഹരണത്തിന് `"ko"` അല്ലെങ്കിൽ `"pt-BR"` പോലുള്ളത്. |
| `root_dir` | No | സോഴ്‌സ് പ്രോജക്ട് റൂട്ട്. ഡീഫോൾട്ട് `"."`. |
| `translations_dir` | No | ടെക്സ്റ്റ് തർജ്ജമ ഔട്ട്പുട്ട് ഡയറക്ടറി. ഡീഫോൾട്ട് `root_dir` നുയുടെ കീഴിൽ `translations`. |
| `translated_images_dir` | No | തർജ്ജമ ചെയ്ത ഇമേജ് ഔട്ട്പുട്ട് ഡയറക്ടറി. ഡീഫോൾട്ട് `root_dir` നുയ്റെ കീഴിൽ `translated_images`. |
| `translation_types` | No | സജീവമാക്കിയ തർജ്ജമ തരം. ഡീഫോൾട്ട് Markdown, നോട്ട്‌ബുക്കുകൾ, ഇമേജ്‌സ്. |
| `lang_subdir` | No | ഓരോ ഭാഷാ ഫോളഡറിന്റെയും കീഴിൽ ഐച്ഛിക സബ് ഡയറക്ടറി. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | സ്പേസ്-വിൽ വേർതിരിച്ച ലക്ഷ്യ ഭാഷ കോഡുകൾ, ഉദാഹരണത്തിന് `"ko ja fr"`, അല്ലെങ്കിൽ `"all"`. അലിയാസ് കോഡുകൾ canonical BCP 47 മൂല്യങ്ങളാക്കി നോർമലൈസ് ചെയ്യപ്പെടും. |
| `root_dir` | `str` | `"."` | ഒറ്റ തർജ്ജമ ലക്ഷ്യത്തിനുള്ള പ്രോജക്ട് റൂട്ട്. `root_dirs` അല്ലെങ്കിൽ `groups` നൽകുന്നാർ حين രോഗിക്കും. |
| `update` | `bool` | `False` | തിരഞ്ഞെടുക്കപ്പെട്ട ഭാഷകൾക്കായി നിലവിലുള്ള തർജ്മകൾ ഡിലീറ്റ് ചെയ്ത് പുനഃസൃഷ്ടിക്കുക. |
| `images` | `bool` | `False` | ഇമേജ് തർജ്ജമ ഉൾപ്പെടുത്തുക. Azure AI Vision കോൺഫിഗറേഷൻ ആവശ്യമായിരിക്കും. |
| `markdown` | `bool` | `False` | Markdown തർജ്ജമ ഉൾപ്പെടുത്തുക. |
| `notebook` | `bool` | `False` | Jupyter നോട്ട്‌ബുക്ക് തർജ്ജമ ഉൾപ്പെടുത്തുക. |
| `debug` | `bool` | `False` | ഡീബഗ് ലോഗിംഗ് സജീവമാക്കുക. |
| `save_logs` | `bool` | `False` | റൂട്ട് `logs/` ഡയറക്ടറിയിൽ DEBUG-ലെവൽ ലോഗ് ഫയലുകൾ സേവ് ചെയ്യുക. |
| `yes` | `bool` | `True` | പ്രോഗ്രാമാറ്റിക് மற்றும் CI ഉപയോഗത്തിന് ഓട്ടോ-കോൺഫർമേഷൻ. |
| `add_disclaimer` | `bool` | `False` | തർജ്ജമ ചെയ്ത Markdown மற்றும் നോട്ട്‌ബുക്കുകളിൽ മെഷീൻ തർജ്ജമ ഡിസ്ക്ലെയ്മര്‍ ചേർക്കുക. |
| `translations_dir` | `str \| None` | `None` | കസ്റ്റം ടെക്സ്റ്റ് തർജ്ജമ ഔട്ട്പുട്ട് ഡയറക്ടറി. റിലേറ്റീവ് പാതകൾ ഓരോ റൂട്ടിനോടും എതിരായി റിസോൾവ് ചെയ്യും. |
| `image_dir` | `str \| None` | `None` | കസ്റ്റം തർജ്ജമ ചെയ്ത ഇമേജ് ഔട്ട്പുട്ട് ഡയറക്ടറി. റിലേറ്റീവ് പാതകൾ ഓരോ റൂട്ടിനോടും എതിരായി റിസോൾവ് ചെയ്യും. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ഒരേ ഔട്ട്പുട്ട് സെറ്റിങ്ങുകൾ പങ്കിടുന്ന متعدد റൂട്ടുകൾ. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | വ്യക്തമായ `(root_dir, translations_dir)` ജോഡികൾ. `root_dirs`-ക്കുണ്ടായിരിക്കുമ്പോൾ ഇവ മുൻഗണനയുള്ളവയാണ്. |
| `repo_url` | `str \| None` | `None` | README ഭാഷ ടേബിൾ മാർഗനിർദ്ദേശം റെൻഡർ ചെയ്യുമ്പോൾ ഉപയോഗിക്കുന്ന റിപോസിറ്ററി URL. |
| `glossaries` | `Iterable[str] \| None` | `None` | തർജ്മ ചെയ്യുമ്പോൾ സംരക്ഷിക്കേണ്ട ഗ്ലോസറി പദങ്ങൾ. ഡുപ്ലിക്കേറ്റുകളും ശൂന്യ പദങ്ങളും നോർമലൈസ് ചെയ്യപ്പെടും. |
| `dry_run` | `bool` | `False` | ഫയലുകൾ എഴുതാതെ തർജ്മ വോള്യം വിലയിരുത്തുകയും മൈഗ്രേഷൻ പെരുമാറ്റം മുൻവീക്ഷണം ചെയ്യുകയും ചെയ്യുക. |

## Review Parameters

`run_review` സാധ്യമായിടത്തോളം `run_translation` സിഗ്നേച്ചറിനെ അനുകരിക്കുന്നു ताकि ഓട്ടോമേഷൻ കുറഞ്ഞ ബ്രാഞ്ചിംഗോടെ തർജ്മയും റിവ്യൂ വേർക്ക്ഫ്ലോയിലുമുള്ള ഇടപെടൽ സ്വിച്ച് ചെയ്യാവൂ.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | റിവ്യൂ ചെയ്യേണ്ട ലക്ഷ്യ ഭാഷാ ഫോൾഡറുകൾ. സ്പേസ്-വിച്ഛേദിച്ച സ്ട്രിംഗുകളും iterable-ുകളും സ്വീകരിക്കുന്നു. `"all"` കണ്ടെത്തിയ എല്ലാ തർജ്മാ ഭാഷകളും റിവ്യൂ ചെയ്യും. |
| `root_dir` | `str` | `"."` | ഒറ്റ റിവ്യൂ ലക്ഷ്യത്തിനുള്ള പ്രോജക്ട് റൂട്ട്. `root_dirs` അല്ലെങ്കിൽ `groups` നൽകിയാൽ ഇത് ഉപേക്ഷിക്കപ്പെടും. |
| `markdown` | `bool` | `False` | Markdown અને MDX സോഴ്‌സ് ഫയലുകൾ ഉൾപ്പെടുത്തുക. |
| `notebook` | `bool` | `False` | Jupyter നോട്ട്‌ബുക്ക് സോഴ്‌സ് ഫയലുകൾ ഉൾപ്പെടുത്തുക. |
| `images` | `bool` | `False` | തർജ്മ ഓപ്ഷനുകളോടുള്ള സമത്വത്തിന് വേണ്ടി 예약് ചെയ്തിരിക്കുന്നത്. Markdown-ൽ നിന്നുള്ള ഇമേജ് ലിങ്ക് റഫറൻസുകൾ പരിശോധിക്കപ്പെടും. |
| `translations_dir` | `str \| None` | `None` | കസ്റ്റം ടെക്സ്റ്റ് ട്രാൻസ്ലേഷൻ ഔട്ട്‌പുട്ട് ഡയറക്ടറി. സാപേക്ഷ പാതകൾ ഓരോ റൂട്ടിനെയും അടിസ്ഥാനമാക്കി തീർക്കപ്പെടും. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ഒരേ ഔട്ട്‌പുട്ട് ക്രമീകരണങ്ങൾ പങ്കുവെക്കുന്ന ഒന്നിലധികം റൂട്ടുകൾ. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | സ്‌പഷ്ടമായ `(root_dir, translations_dir)` ജോഡികൾ. `root_dirs`ന് മുകളിൽ മുൻഗണന നൽകുന്നു. |
| `changed_from` | `str \| None` | `None` | പരിശോധന മാറ്റപ്പെട്ട സോഴ്‌സ് ഫയലുകളിൽ മാത്രം പരിമിതപ്പെടുത്താൻ ഉപയോഗിക്കുന്ന Git റഫറൻസ്. |
| `output_format` | `str` | `"text"` | റിവ്യൂ ഔട്ട്‌പുട്ട് ഫോർമാറ്റ്. പിന്തുണയ്ക്കുന്ന മൂല്യങ്ങൾ `"text"`യും `"github"`ഉം ആണ്. |
| `fail_on_warnings` | `bool` | `False` | എററുകളോടൊപ്പം മുന്നറിയിപ്പുകളെയും പരാജയങ്ങളായി കണക്കാക്കുക. |
| `debug` | `bool` | `False` | ഡീബഗ് ലോഗിങ് സജ്ജമാക്കുക. |
| `save_logs` | `bool` | `False` | റൂട്ടിലുള്ള `logs/` ഡയറക്ടറിയിൽ DEBUG-തല ലോഗ് ഫയലുകൾ സേവ് ചെയ്യുക. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## കോൺഫിഗറേഷൻ ആവശ്യകതകൾ

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

## പെരുമാറ്റ കുറിപ്പുകൾ

- Content translation APIs keep translation separate from project path rewriting. Call `rewrite_markdown_paths` or `rewrite_notebook_paths` explicitly when translated content needs project-relative links adjusted for a target location.
- Project orchestration APIs add project behavior around content translation, including file discovery, writes, path rewriting, metadata, cleanup, and optional disclaimers.
- `run_translation` prints progress and estimate summaries through Click, matching the CLI user experience.
- `dry_run=True` computes estimates using virtual README updates, but does not write the README or translation files.
- `groups` are processed sequentially. A single aggregate estimate is printed before work begins.
- When image translation is selected, missing Vision configuration raises an error before translation starts.
- Existing alias-based language folders are detected and can be migrated to canonical language folder names as part of the run.
- `run_review` fails on missing translated files, missing or stale translation metadata, malformed Markdown frontmatter/code fences, and invalid translated notebook JSON.
- `run_review` reports missing local Markdown and image link targets as warnings by default.

## ആന്തരിക കോൾ പാത

The API delegates to the same core implementation used by the CLI:

പരിഭാഷ:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Focused project translation mixins for Markdown, notebooks, and images.
8. Markdown, notebook, text, and image translators under `co_op_translator.core`.

റിവ്യൂ:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

The following classes are useful for maintainers, but are not exported as the package-level stable API.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | പ്രോജക്ട് നിലവാരത്തിലുള്ള പരിഭാഷ, ഡയറക്ടറി മാനേജ്മെന്റ്, ഓരോ ഭാഷയ്ക്കുള്ള മെറ്റാഡേറ്റാ സാധാരണീകരണം, Markdown, notebook, image ട്രാൻസ്ലേറ്റർമാർക്കുള്ള ഡെലിഗേഷൻ എന്നിവ ഏകാഞ്ഞുചേർക്കുന്നു. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, നോട്ട്‌ബുക്കുകൾ, ഇമേജുകൾ, സ്റ്റെയിൽ കണ്ടെത്തൽ, ട്രാൻസ്ലേഷൻ മെറ്റാഡേറ്റാ അപ്‌ഡേറ്റുകൾ എന്നിവയ്ക്കായുള്ള അസിങ്ക് ഫയൽ പ്രോസസിംഗ് പ്രവർത്തനങ്ങൾ നടത്തുന്നു. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ഫയൽ വായനകൾ, ഉള്ളടക്ക പരിഭാഷ, പാത പുനർലിഖനം, മെറ്റാഡേറ്റാ, വ്യത്യാസ പ്രഖ്യാപനങ്ങൾ, ഫയൽ എഴുതൽ എന്നിവ ഏകോപിപ്പിക്കുന്നു. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | നോട്ട്‌ബുക്ക് ഫയൽ വായനകൾ, Markdown സെൽ പരിഭാഷ, പാത പുനർലിഖനം, മെറ്റാഡേറ്റാ, വ്യത്യാസ പ്രഖ്യാപനങ്ങൾ, ഫയൽ എഴുതൽ എന്നിവ ഏകോപിപ്പിക്കുന്നു. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | സോഴ്‌സ് ഇമേജ് കണ്ടെത്തൽ, ഇമേജ് പരിഭാഷ, ഔട്ട്‌പുട്ട് പാതകൾ, മെറ്റാഡേറ്റാ, ഫയൽ എഴുതൽ എന്നിവ ഏകോപിപ്പിക്കുന്നു. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | പരിഭാഷപ്പെടുത്തിയ Markdown ജോഡികൾ കണ്ടെത്തുന്നു, പരിഭാഷ ഗുണനിലവാരം വിലയിരുത്തുന്നു, കൂടിയ വിശ്വാസമില്ലാത്ത റിപെയർ പ്രവൃത്തികൾക്കായുള്ള വിശ്വാസ മെറ്റാഡേറ്റാ വായിക്കുന്നു. |
| `ReviewRunner` | `co_op_translator.review.runner` | സോഴ്‌സ് ഫയലുകൾ, ലക്ഷ്യ ഭാഷകൾ, ക്രമീകരിച്ച ട്രാൻസ്ലേഷൻ റൂട്ടുകൾ എന്നിവയിലുടനീളമുള്ള നിർണായക റിവ്യൂ ചെക്കുകൾ ഏകോപിപ്പിക്കുന്നു. |
| `ReviewTarget` | `co_op_translator.review.targets` | ഒരു സോഴ്‌സ് റൂട്ടും ആ റൂട്ടിനുള്ള ട്രാൻസ്ലേഷൻ ഔട്ട്‌പുട്ട് ഡയറക്ടറിയും വിവരിക്കുന്നു. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | പാരമ്പര്യ ആലിയാസ് ഭാഷ ഫോൾഡറുകൾ കണ്ടെത്തുകയും കാനോൺിക്കൽ BCP 47 ഫോൾഡർ മാറൽ പദ്ധതികൾ തയ്യാറാക്കുകയും ചെയ്യുന്നു. |
| `Config` | `co_op_translator.config.base_config` | `.env` ഫയലുകൾ ലോഡ് ചെയ്യുകയും ആവശ്യമായ LLMയും ഐച്ഛിക Vision പ്രൊവൈഡറുകളും കോൺഫിഗർ ചെയ്‌തിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുകയും ചെയ്യുന്നു. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI അല്ലെങ്കിൽ OpenAI സ്വയം തിരിച്ചറിഞ്ഞ് ആവശ്യമായ എൻവയോൺമെന്റ് വേരിയബിളുകൾ പരിശോദിക്കുകയും പ്രൊവൈഡർ കണക്റ്റിവിറ്റി ചെക്കുകൾ നടത്തുകയും ചെയ്യുന്നു. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | ഇമേജ് പരിഭാഷയ്ക്കായി Azure AI Vision കോൺഫിഗറേഷൻ കണ്ടെത്തുകയും കണക്റ്റിവിറ്റി ചെക്കുകൾ നടത്തുകയും ചെയ്യുന്നു. |