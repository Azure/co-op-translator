# Python API

സ്ഥിരമായ പൊതു Python API `co_op_translator.api`-നിന്നാണ് എക്സ്പോർട്ട് ചെയ്യപ്പെടുന്നത്. പല ഇന്റഗ്രേഷനുകളും ഇവയിൽ ഒന്നിലുള്ള പ്രവാഹരീതി ഉപയോഗിക്കുന്നു:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | നിങ്ങളുടെ ആപ്ലിക്കേഷൻ സോഴ്‌സ് ഉള്ളടക്കം വായിച്ച്, തർജ്ജമയ്‌ക്കായി Co-op Translator വിളിച്ച് ഫലം എവിടെ സേവ് ചെയ്യണമെന്നത് നിർണ്ണയിക്കുന്നപ്പോൾ. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| ഹോസ്റ്റ്-ഏജന്റ് തർജ്ജമയ്ക്ക് ഉള്ളടക്കം തയ്യാറാക്കുക | നിങ്ങളുടെ MCP ഹോസ്റ്റ് അല്ലെങ്കിൽ ആപ്ലിക്കേഷൻ മോഡൽ ചങ്കുകൾ തർജ്ജമ ചെയ്യും, Co-op Translator ചങ്കുചെയ്യലും പുനഃസംരചനയും കൈകാര്യം ചെയ്യും. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Python API CLI പോലെയായും കണ്ടെത്തൽ, ഔട്ട്‌പുട്ട് പാതകൾ, മെടാഡേറ്റാ, ക്ലീനപ്പ്, എഴുത്ത് തുടങ്ങിയവ കൈകാര്യം ചെയ്യാൻ നിങ്ങൾ ആഗ്രഹിക്കുമ്പോൾ. | `run_translation` |

`core`, `config`, `review`, `utils` എന്നിവയുടെ കീഴിലുള്ള ബഹുതാംശ ലൊവേർ-ലെവൽ മോഡ്യൂളുകൾ ഈ API എൻട്രിപോയിൻറുകൾ ഉപയോഗിക്കുന്ന നടപ്പിലാക്കലുകളുടെ വിശദാംശങ്ങളാണ്.

MCP ക്ലയന്റുകൾ [MCP Server](mcp.md) മുഖാന്തിരം ഒരേ പൊതു API ഉപയോഗിക്കുന്നു. Python നേരിട്ട് വിളിക്കുമ്പോൾ ഈ പേജ് ഉപയോഗിക്കുക, Co-op Translator ഒരു ഏജന്റിനോ എഡിറ്ററിനോ തുറന്നുകൊടുക്കുമ്പോൾ MCP ഗൈഡ് ഉപയോഗിക്കുക. CLI, Python API, MCP എന്നിവയിലെ തിരഞ്ഞെടുപ്പ് ചെയ്യാനുണ്ടെങ്കില്‍ [Choose Your Workflow](workflows.md) നിന്ന് തുടങ്ങുക.

## ആദ്യമായുള്ള API പ്രവാഹം

Python കോഡിൽ നിന്ന് Co-op Translator വിളിക്കുന്നതിനാണ് ഇവിടെ നിന്ന് തുടങ്ങുക:

1. [Configuration](configuration.md)ൽ വിവരിച്ചിരിക്കുന്ന പോലെ ഒരു LLM പ്രൊവൈഡർ കോൺഫിഗർ ചെയ്യുക, ഹോസ്റ്റ്-എജന്റ് തർജ്ജമയ്ക്ക് Markdown അല്ലെങ്കിൽ നോട്ട്‌ബുക്ക് ചങ്കുകൾ മാത്രം തയ്യാറാക്കുകയാണെങ്കിൽ ഇത് ആവശ്യമില്ല.
2. നിങ്ങളുടെ ആപ്ലിക്കേഷൻ ഫയൽ I/O കൈകാര്യം ചെയ്യുന്നുണ്ടോ എന്നത് തീരുമാനിക്കുക.
3. നിങ്ങളുടെ ആപ്ലിക്കേഷൻ വ്യക്തിഗത ഫയലുകൾ വായിച്ചു എഴുതുന്നുണ്ടെങ്കിൽ ഉള്ളടക്ക APIകൾ ഉപയോഗിക്കുക.
4. Co-op Translator ഒരു റെപ്പോസ്‌റ്ററി CLI പോലെയായി പ്രോസസ് ചെയ്യേണ്ടതുണ്ടെങ്കിൽ `run_translation` ഉപയോഗിക്കുക.
5. ഓട്ടോമേഷനിൽ നിർണ്ണായക പരിശോധനകൾ ആവശ്യമായിരിക്കുകയാണെങ്കിൽ തർജ്ജമയ്ക്ക് ശേഷം `run_review` ഉപയോഗിക്കുക.

| Goal | API to start with |
| --- | --- |
| ഒരു Markdown സ്ട്രിംഗ് അല്ലെങ്കിൽ ഫയൽ തർജ്ജമിക്കുക | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| ഒരു ഹോസ്റ്റ്-ഏജന്റ് Markdown അല്ലെങ്കിൽ നോട്ട്ബുക്ക് ചങ്കുകൾ തർജ്ജമ ചെയ്യട്ടെ | `start_markdown_agent_translation` അല്ലെങ്കിൽ `start_notebook_agent_translation` |
| ഔട്ട്പുട്ട് പാത തിരഞ്ഞെടുക്കുന്നതിന് ശേഷം പരിഭാഷപ്പെടുത്തിയ ലിങ്കുകൾ പുനഃരചിക്കുക | `rewrite_markdown_paths` അല്ലെങ്കിൽ `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## സന്ദർഭം 1: വ്യക്തിഗത ഫയലുകൾ അല്ലെങ്കിൽ ഡോക്യുമെന്റുകൾ വിവർത്തനം ചെയ്യുക

നിങ്ങളുടെ কাছে ഇതിനകം ഒരു ഫയൽ, എഡിറ്റർ ബഫർ, നോട്ട്‌ബുക്ക് പേയ്ലോഡ്, MCP അഭ്യർ‍ത്ഥന, അല്ലെങ്കിൽ കസ്റ്റം പൈപ്പ്‌ലൈനിന്റെ ഇൻപുട്ട് ഉണ്ടെങ്കിൽ ഈ പ്രവാഹരീതി ഉപയോഗിക്കുക. നിങ്ങളുടെ കോഡാണ് ഫയൽ I/O കൈകാര്യം ചെയ്യുന്നത്:

1. സോഴ്‌സ് ഉള്ളടക്കം വായിക്കുക.
2. ഒരു ഉള്ളടക്ക തർജ്ജമ API വിളിക്കുക.
3. തർജ്ജമിച്ച ഉള്ളടക്കം പ്രോജക്ട് ട്രാൻസ്ലേഷൻ ഫോളഡറിൽ എഴുതാനാണ് പോകുന്നത് എങ്കിൽ, ആവശ്യമായപ്പോൾ പാത്ത് പുനഃരചന API വിളിക്കുക.
4. ഫലം നിങ്ങളുടെ അപേക്ഷയിൽ സേവ് ചെയ്യുക അല്ലെങ്കിൽ റിട്ടേൺ ചെയ്യുക.

ഉള്ളടക്ക തർജ്ജമ APIകൾ പ്രോജക്റ്റ് കണ്ടെത്തൽ നടത്തുകയില്ല, മെടാഡേറ്റാ എഴുതുകയില്ല, അസ്സർടിംചെയ്യൽ കുറിപ്പുകൾ ചേർക്കുകയില്ല, ലിങ്കുകൾ സ്വയമേ പുനഃരചെയ്യുകയില്ല.

### Markdown ഫയൽ

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

തർജ്ജമിച്ച Markdown Co-op Translator പ്രോജക്റ്റ് ലേഔട്ടിൽ താമസിക്കുകയില്ലങ്കിൽ, `rewrite_markdown_paths` ഒഴിവാക്കി തർജ്ജമിച്ച സ്ട്രിംഗ് നേരിട്ട് സേവ് ചെയ്യുക.

### നോട്ട്ബുക്ക് ഫയൽ

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

`translate_notebook_content` Markdown സെല്ലുകൾ തർജ്ജമ ചെയ്യുകയും Markdown അല്ലാത്ത സെല്ലുകൾ സംരക്ഷിക്കുകയും ചെയ്യുന്നു. പാത പുനഃരചന Markdown സെല്ലുകൾക്ക് മാത്രമേ ബാധകമാകൂ.

### ചിത്രം ഫയൽ

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

`translate_image_content` സോഴ്‌സ് ചിത്രം വായിച്ച് ഒരു റെൻഡർ ചെയ്ത `PIL.Image.Image` റിട്ടേൺ ചെയ്യുന്നു. ഇത് തർജ്ജമിച്ച ചിത്രത്തിന്റെ മെടാഡേറ്റാ എഴുതുകയില്ല.

## സന്ദർഭം 2: ഒരു മുഴുവൻ റിപ്പോസിറ്ററി വിവർത്തനം ചെയ്യുക

Python API `translate` CLI പോലെയായി പെരുമാറണമെന്നാൽ ഈ പ്രവാഹരീതി ഉപയോഗിക്കുക. `run_translation` പിന്തുണയുള്ള ഫയലുകൾ കണ്ടെത്തുന്നു, തിരഞ്ഞെടുക്കപ്പെട്ട ഉള്ളടക്ക തരം തർജ്ജമ ചെയ്യുന്നു, പാതകൾ പുനഃരചിക്കുന്നു, ഔട്ട്‌പുട്ട് ഫയലുകൾ എഴുതുന്നു, മെടാഡേറ്റാ അപ്‌ഡേറ്റ് ചെയ്യുന്നു, ക്ലീനപ്പ് പോലുള്ള പരിപാലനാ কাজങ്ങൾ നിർവഹിക്കുന്നു.

`run_translation` പ്രോജക്ട് ഓർക്കസ്ട്രേഷൻ ആരംഭബിന്ദുവിനെക്കുറിച്ച് മുൻഗണന ലഭിച്ച എന്റ്രിപോയിന്റാണ്. അതേ പെരുമാറ്റത്തോടെ `translate_project` ഒരു compatibility alias ആയി എക്സ്പോർട്ട് ചെയ്യപ്പെട്ടിരിക്കുന്നു.

നിലവിലുള്ള റിപോസിറ്ററിയിലുള്ള Markdown ഫയലുകൾ കൊറിയനും ജാപ്പനീസിനും വിവർത്തനം ചെയ്യുക:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ഒരു പ്രത്യേക പ്രോജക്ട് റൂട്ടിൽ നിന്നുള്ള നോട്ട്ബുക്കുകൾ മാത്രം തർജ്ജമിക്കുക:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ഫയലുകൾ എഴുതാതെ പരിഭാഷയുടെ വോള്യം മുൻകൂട്ടി കാണിക്കുക:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ഒരു ഇന്റഗ്രേഷന үчүн ഘടനാബദ്ധമായ പുരോഗതി ഇവന്റുകൾ രേഖപ്പെടുത്തുക:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # പേലോഡ് നിങ്ങളുടെ ജോബ്-ഇവന്റ് പട്ടികയിൽ സൂക്ഷിക്കുക അല്ലെങ്കിൽ അത് നിങ്ങളുടെ UI-യിലേക്ക് സ്ട്രീം ചെയ്യുക


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

ഒരു കോൾ-ൽ متعدد ഉള്ളടക്കം റൂട്ടുകൾ തർജ്ജമിക്കുക:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

പരിഭാഷകൾ നിശ്ചിത ഔട്ട്പുട്ട് ഗ്രൂപ്പുകളിൽ എഴുതുക:

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

ഓരോ ഭാഷയ്ക്കും ഒരു അടിയിലേക്ക് സബ്‌ഡയറക്ടറി ഉണ്ടാകണം എന്ന സാഹചര്യം ഉണ്ടെങ്കിൽ ഭാഷാനുസരിച്ചുള്ള പ്ലേസ്ഹോൾഡർ ഉപയോഗിക്കുക:

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

`markdown`, `notebook`, അല്ലെങ്കിൽ `images` ഏതെങ്കിലും സജ്ജമാക്കിയിട്ടില്ലെങ്കിലെങ്കില്‍, API എല്ലാ പിന്തുണയുള്ള ടൈപ്പുകളും തർജ്ജമ ചെയ്യുന്നു: Markdown, നോട്ട്ബുക്കുകൾ, மற்றும் ചിത്രങ്ങൾ.

### സ്വീകരിക്കപ്പെട്ട മനുഷ്യ എഡിറ്റുകൾ വിവർത്തന സ്റ്റേറ്റ് പ്രൊവൈഡറോടെ സംരക്ഷിക്കുക

എൻറെ ഡീഫോൾട്ട് നിലയിൽ, Co-op Translator നിലവിലുള്ള ഫയൽ-നില പെരുമാറ്റം നിലനിർത്തുന്നു: ഒരു
Markdown സോഴ്‌സ് പഴകിയിരിക്കുന്ന പക്ഷം, മുഴുവൻ തർജ്ജമ ചെയ്ത ഫയൽ വീണ്ടും ജനറേറ്റ് ചെയ്യപ്പെടും. ഹോസ്റ്റുചെയ്‌ത
ഇന്റഗ്രേഷനുകൾ ഐച്ഛികമായി `TranslationStateProvider` സമർപ്പിക്കാവുന്നതാണ്
മാറ്റമില്ലാത്ത സോഴ്‌സ് ബ്ലോക്കുകളിലുള്ള മാനവൻ നടത്തിയ തിരുത്തലുകൾ സംരക്ഷിക്കാൻ.

പ്രൊവൈഡറും അവസാനമായി അംഗീകരിച്ച source/target ജോഡിയെ നൽകുകയും ഓരോ പുതിയ പ്രതീക്ഷാർത്ഥിയെയും രേഖപ്പെടുത്തുകയും ചെയ്യുന്നു.
അംഗീകാരം ഇന്റഗ്രേഷനിന്റെ ഉത്തരവാദിത്യമായി തുടരുന്നു — ഉദാഹരണത്തിന്,
ഒരു വിവർത്തന pull request മർജ് ചെയ്തശേഷം:

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

സാധുവായ അംഗീകൃത ബേസ്‌ലൈനുള്ള Markdown ഫയലുകൾക്കായി, Co-op Translator മുകളിൽ നിലവിലുള്ള Markdown ബ്ലോക്കുകൾ പൊതു പാര്യത്തിലെത്തിക്കുന്നു.
മാറ്റമില്ലാത്ത source ബ്ലോക്കുകൾ നിലവിലുള്ള വിവർത്തിക്കപ്പെട്ട ബ്ലോക്കുകൾ വീണ്ടും ഉപയോഗിക്കും, മനുഷ്യർ നടത്തിയ തിരുത്തലുകളും ഉൾപ്പെടെ; മാറ്റപ്പെടുകയോ ചേർക്കപ്പെടുകയോ ചെയ്ത source ബ്ലോക്കുകൾ വിവർത്തനത്തിനായി അയയ്ക്കപ്പെടും; ഒഴിവാക്കിയ source ബ്ലോക്കുകൾ നീക്കം ചെയ്യപ്പെടും.

ക്രമീകരണം अस्पष्टമായാൽ, ലക്ഷ്യ ഘടന മാറ്റപ്പെട്ടാൽ, ഒരു ബ്ലോക്ക് വിവർത്തനം അസാധുവായിരുന്നാൽ, അല്ലെങ്കിൽ ബേസ്‌ലൈനൊന്നും ലഭ്യമല്ലെങ്കിൽ, Co-op Translator സുരക്ഷിതമായി നിലവിലുള്ള മുഴുവൻ ഫയൽ വിവർത്തന മാര്‍ഗത്തിലേക്ക് fallback ചെയ്യും.

ഈ API രൂപങ്ങൾ ഡോക്യമെന്റ് വിവർത്തന സ്റ്റേറ്റ് സംഭരിക്കും; ഡോക്യുമെന്റുകൾക്കിടയിലെ വാചകങ്ങളോ സെഗ്‌മെന്റുകളോ ഉള്ള ട്രാൻസ്ലേഷൻ മെമ്മറിയെ അല്ല.
ഇത് നിലവിൽ Markdown പ്രൊജക്ട് വിവർത്തനത്തിന് ബാധകമാണ്.
Notebook-നും ഇമേജ് പെരുമാറ്റത്തിനും മാറ്റമില്ല.
`update=True` നൽകുന്നതിലൂടെ ഇപ്പോഴും പൂർണ പുനർസൃഷ്ടി ആവശ്യപ്പെടപ്പെടുന്നു.

ഒരു അല്ലെങ്കിൽ അതിലധികം ഫയലുകൾ വിവർത്തനം ചെയ്യാൻ കഴിയാതെപോയാൽ, പ്രോജക്ട് വര്‍ക്ക്‌ഫ്ലോ പൂർത്തിയായതിനു ശേഷം `run_translation` ഒരു `RuntimeError` ഉയർത്തും, കുറവുള്ള ഔട്ട്‌പുട്ടോടെ വിജയകരമായ റൺ റിപ്പോര്ട്ട് ചെയ്യുന്നതിന് പകരം.
ഇന്റഗ്രേഷനുകൾ ഇതിനെ പരാജയപ്പെട്ട ജോബായി പരിഗണിച്ച് മുൻപ് അംഗീകരിച്ച വിവർത്തന നില നിലനിർത്തേണ്ടതാണ്.

## വിവർത്തനം ചെയ്ത ഫലങ്ങൾ അവലോകനം ചെയ്യുക

`run_review` LLM അല്ലെങ്കിൽ Vision ക്രെഡൻഷ്യലുകൾ ഇല്ലാതെ നിർവചിതമായ വിവർത്തനപരിശോധനകൾ നടത്തും.

!!! note "Beta"
    `run_review` ഒരു ബീറ്റാ-നിശ്ചിത റിവ്യൂ API ആണ്. ഇത് മോഡൽ പ്രൊവൈഡർമാരെ വിളിക്കുകയോ ഫയലുകൾ എഴുതുകയോ ചെയ്യാറില്ല, പക്ഷേ ചെക്കുകളും ഇഷ്യൂ സ്കീമങ്ങളും പരിണമിക്കാനിടയുണ്ട്.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README മാത്രം തർജ്ജമയ്ക്ക് ശേഷം, റിവ്യൂക്കായി അതേ സ്കോപ്പ് ഉപയോഗിക്കുക:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` ഓരോ കോൺഫിഗർ ചെയ്ത സോഴ്സ് റൂട്ടിന്റെയും കീഴിലുള്ള `README.md` മാത്രമേ അവലോകനം ചെയ്യൂ,
കസ്റ്റം `groups`-ഉം ഔട്ട്പുട്ട് ഡയറക്ടറികളും ഉൾപ്പെടുന്നു. മറ്റ് ഡോക്യുമെന്റുകളും നെസ്റ്റുചെയ്യപ്പെട്ട README ഫയലുകളും ഒഴിവാക്കിയിരിക്കും.
ഒരു നഷ്ടമായ സോഴ്സ് README `ValueError` ഉയർത്തും; പരാജയപ്പെട്ട തർജ്ജമാ പരിശോധനകൾ `RuntimeError` ഉയർത്തും.


ഒരു ബേസ് റഫറൻസിന്റെ എതിരെ മാറ്റം വന്ന ഫയലുകൾ മാത്രം റിവ്യൂ ചെയ്യുക, കൂടാതെ GitHub-ഫ്ലേവേർഡ് ഔട്ട്പുട്ട് പ്രിന്റ് ചെയ്യുക:

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

## കോപി-പേസ്റ്റ് API ഉദാഹരണങ്ങൾ

ഫയൽ എഴുതലുകൾ ഇല്ലാതെ Markdown ഉള്ളടക്കം തർജ്ജമ ചെയ്യുക:

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

Markdown ലിങ്കുകൾ തർജ്ജമ ചെയ്ത് പുനഃലിഖിക്കുക:

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

Python-ൽ നിന്ന് ഒരു റിപ്പോസിറ്ററി തർജ്ജമിക്കുക:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

മൾട്ടിപ്പിൾ റൂട്ടുകൾ തർജ്ജമിക്കുക:

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

## പൊതു പ്രവേശന പോയിന്റുകൾ

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

## ഉള്ളടക്കം പരിഭാഷ APIകൾ

ഉള്ളടക്കം തർജ്ജമ API-കൾ, എഡിറ്റർ എക്സ്റ്റൻഷൻ, MCP ടൂൾ, നോട്ട്ബുക്ക് പ്രോസസ്സർ, അല്ലെങ്കിൽ കസ്റ്റം പൈപ്പ്‌ലൈൻ പോലുള്ള മുമ്പേ മെമ്മറിയിലുള്ള ഉള്ളടക്കം കൈകാര്യം ചെയ്യുന്ന സംയോജനംগুলിന് ഉദ്ദേശിച്ചവയാണ്.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Markdown ഉള്ളടക്കം മാത്രം തർജ്ജമ ചെയ്യുന്നു. ഇത് ലിങ്കുകൾ പുനരാഖ്യാനം ചെയ്യുകയോ, മെറ്റാഡേറ്റാ എഴുതുകയോ, ഡിസ്‌ക്ലെയിമറുകൾ ചേർക്കുകയോ ചെയ്യില്ല. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown സെലുകൾ തർജ്ജമ ചെയ്യുന്നു ಮತ್ತು non-Markdown സെലുകൾ നിലനിർത്തുന്നു. ഇത് ലിങ്കുകൾ പുനരാഖ്യാനം ചെയ്യുകയോ, മെറ്റാഡേറ്റാ എഴുതുകയോ, ഡിസ്‌ക്ലെയിമറുകൾ ചേർക്കുകയോ ചെയ്യില്ല. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. ചിത്രം ഉള്ളടക്കത്തിൽ നിന്നുള്ള ടെക്സ്റ്റ് പുറത്തെടുക്കുകയും അതർജ്ജമ ചെയ്ത് റെൻഡർ ചെയ്ത ചിത്രം റിട്ടേൺ ചെയ്യുകയും ചെയ്യുന്നു. ഇത് തർജ്ജമ ചെയ്ത ചിത്ര മെടാഡേറ്റാ സേവ് ചെയ്യാറില്ല. |

`translate_markdown_content` and `translate_notebook_content` അവരുടെ ഓപ്ഷനുകൾ വഴി ഐച്ഛികമായ `source_path` സ്വീകരിക്കാം. പാത്ത് ട്രാൻസ്ലേറ്ററിന് കോൺടെക്സ്റ്റായി പാസായിരിക്കും; കോൾ ചെയ്യുന്നവർ തർജ്ജമക്ക് ശേഷം പ്രോജക്ട്-നിർദ്ദിഷ്ട പാത്ത് പുനരാഖ്യാനം ചെയ്യുന്നതിന് ബാധ്യസ്ഥരാണ്.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

അതേ ഓപ്ഷനുകൾ നിഘണ്ടുക്കളായി നൽകി നൽകാവുന്നതാണ്:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## ഏജന്റ്-സഹായിത പരിഭാഷ APIകൾ

ഏജന്റ്-സഹായിത API-കൾ Co-op Translator-ൽ കോൺഫിഗർ ചെയ്ത LLM പ്രൊവൈഡറെ വിളിക്കാറില്ല. അവ ഹോസ്റ്റ് ഏജന്റ് തർജ്ജമ ചെയ്യാൻ Markdown അല്ലെങ്കിൽ നോട്ട്ബുക്ക് ചങ്കുകൾ തയ്യാറാക്കുകയും, പിന്നീട് തർജ്ജമിച്ച ചങ്കുകളിൽ നിന്ന് അന്തിമ ഉള്ളടക്കം പുനർനിർമിക്കുകയും ചെയ്യുന്നു.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | ഒരു സ്വയം സമഗ്രമായ Markdown ജോബ് ചങ്കുകളോടും പ്രോംപ്റ്റുകളോടും പുനർനിർമാണ സ്റ്റേറ്റിനോടും ചേർന്ന് റിട്ടേൺ ചെയ്യുന്നു. |
| `finish_markdown_agent_translation` | ജോബ് และ ഹോസ്റ്റ്-ഏജന്റ് തർജ്ജമിച്ച ചങ്കുകൾ ഉപയോഗിച്ച് Markdown പുനർനിർമിക്കുന്നു. |
| `start_notebook_agent_translation` | ഹോസ്റ്റ്-ഏജന്റിന് വേണ്ടി Markdown-സെൽ ചങ്കുകളുള്ള ഒരു നോട്ട്ബുക്ക് ജോബ് റിട്ടേൺ ചെയ്യുന്നു. |
| `finish_notebook_agent_translation` | കോഡ് സെൽസ്, ഔട്ട്പുട്ടുകൾ, മേട്ടാഡേറ്റ എന്നിവ നിലനിർത്തിയും നോട്ട്ബുക്ക് JSON പുനർനിർമിക്കുന്നു. |

ഈ വർക്ഫ്ലോ MCP ഹോസ്റ്റുകൾക്കായാണ് പ്രധാനമായും ഉദ്ദേശിച്ചിരിക്കുന്നത്. Co-op Translator പ്രൊവൈഡർ കോളുകൾ കൈകാര്യം ചെയ്ത് പ്രൊഡക്ഷൻ റിപ്പോസിറ്ററി തർജ്ജമണം വേണമെങ്കിൽ `translate_markdown_content`, `translate_notebook_content`, അല്ലെങ്കിൽ `run_translation` ഉപയോഗിക്കൂ.

## പാത പുനർലേഖന APIകൾ

പാത്ത് പുനഃരാഖ്യാനം API-കൾ തർജ്ജമ ചെയ്യാറില്ല. കോൾ yapanവർ സോഴ്സ് പാത്ത്, തർജ്ജമ ചെയ്ത ടാർഗെറ്റ് പാത്ത്, പ്രോജക്ട് ലേയൗട്ട് എന്നിവ അറിഞ്ഞതായി കഴിഞ്ഞു എങ്കിൽ അവ ലിങ്കുകളും ഫ്രണ്ട്‌മെറ്റർ പാത്തുകളും അപ്‌ഡേറ്റ് ചെയ്യുന്നു.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | തർജ്ജമ ചെയ്ത ലക്ഷ്യത്തിനായി Markdown ലിങ്കുകളും പിന്തുണയ്ക്കപ്പെട്ട frontmatter പാത ഫീൽഡുകളും വീണ്ടും എഴുതുന്നു. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | ഓരോ Markdown സെലിനും Markdown പാത പുനരാഖ്യാനം പ്രയോഗിക്കുകയും non-Markdown സെല്ലുകൾ മാറ്റമില്ലാതെ വെക്കും. |

`policy` ഓർഗുമെന്റ് താഴെ കാണുന്ന ഫീൽഡുകളുള്ള ഒരു ഡിക്ഷണറിയായിരിക്കാം:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | ലക്ഷ്യ ভাষാ കോഡ്, ഉദാഹരണത്തിന് `"ko"` അല്ലെങ്കിൽ `"pt-BR"`. |
| `root_dir` | No | സോഴ്സ് പ്രോജക്ട് റൂട്ട്. ഡീഫോള്ട് `"."`. |
| `translations_dir` | No | ടെക്സ്റ്റ് തർജ്ജമാ ഔട്ട്പുട്ട് ഡയറക്ടറി. ഡീഫോള്ട് `translations`, `root_dir`-ന്റേതടിയിൽ. |
| `translated_images_dir` | No | തർജ്ജമ ചെയ്ത ചിത്രം ഔട്ട്പുട്ട് ഡയറക്ടറി. ഡീഫോള്ട് `translated_images`, `root_dir`-ന്റേതടിയിൽ. |
| `translation_types` | No | സജ്ജീകരിച്ച തർജ്ജമ തരം(കൾ). ഡീഫോള്ട് Markdown, notebooks, images. |
| `lang_subdir` | No | ഓരോ ഭാഷാ ഫോള്ഡറിന്റെയും കീഴിൽ ഐച്ഛിക ഉപഡയറക്ടറി. |

## പ്രോജക്ട് വിവർത്തന പാരാമീറ്ററുകൾ

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | സ്പേസ്-വച്ച് വേർതിരിച്ച ലക്ഷ്യ ഭാഷാ കോഡുകൾ, ഉദാഹരണത്തിന് `"ko ja fr"`, അല്ലെങ്കിൽ `"all"`. അലിയാസ് കോഡുകൾ സാധാരണ BCP 47 മൂല്യങ്ങളാക്കി സ്വഭാവീകരിക്കപ്പെടുന്നു. |
| `root_dir` | `str` | `"."` | സിംഗിൾ തർജ്ജമാ ലക്ഷ്യത്തിനുള്ള പ്രോജക്ട് റൂട്ട്. `root_dirs` അല്ലെങ്കിൽ `groups` നൽകിയാൽ ഇത് അവഗണിക്കുന്നു. |
| `update` | `bool` | `False` | തിരഞ്ഞെടുക്കപ്പെട്ട ഭാഷകൾക്കുള്ള നിലവിലുള്ള തർജ്ജമകൾ നീക്കം ചെയ്ത് വീണ്ടും സൃഷ്ടിക്കും. |
| `images` | `bool` | `False` | ചിത്ര തർജ്ജമ ഉൾപ്പെടുത്തുക. Azure AI Vision ക്രമീകരണം ആവശ്യമാണ്. |
| `markdown` | `bool` | `False` | Markdown തർജ്ജമ ഉൾപ്പെടുത്തുക. |
| `notebook` | `bool` | `False` | Jupyter നോട്ട്ബുക്ക് തർജ്ജമ ഉൾപ്പെടുത്തുക. |
| `debug` | `bool` | `False` | ഡീബഗ് ലോഗിംഗ് സജീവമാക്കുക. |
| `save_logs` | `bool` | `False` | റൂട്ട് `logs/` ഡയറക്ടറിയിലേയ്ക്ക് DEBUG-തലത്തിലുള്ള ലോഗ് ഫയലുകൾ സേവ് ചെയ്യുക. |
| `yes` | `bool` | `True` | പ്രോഗ്രാമാറ്റിക് ആവശ്യങ്ങൾക്കുമായി மற்றும் CI ഉപയോഗത്തിനായി പ്രോംപ്റ്റുകൾ സ്വയം സ്ഥിരീകരിക്കുക. |
| `add_disclaimer` | `bool` | `False` | വിവർത്തനം ചെയ്ത Markdown-കളിലും നോട്ട്‌ബുക്കുകളിലും മെഷീൻ വിവർത്തന ഡിസ്‌ക്ലെയിമറുകൾ ചേർക്കുക. |
| `translations_dir` | `str \| None` | `None` | കസ്റ്റം ടെക്സ്റ്റ് വിവർത്തന ഔട്ട്‌പുട്ട് ഡയറക്ടറി. റെലേറ്റീവ് പാതകൾ ഓരോ റൂട്ടിനെയും അടിസ്ഥാനമാക്കി പരിഹരിക്കപ്പെടുന്നു. |
| `image_dir` | `str \| None` | `None` | കസ്റ്റം വിവർത്തനപ്പെടുത്തിയ ഇമേജ് ഔട്ട്‌പുട്ട് ഡയറക്ടറി. റെലേറ്റീവ് പാതകൾ ഓരോ റൂട്ടിനെയും അടിസ്ഥാനമാക്കി പരിഹരിക്കപ്പെടുന്നു. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ഒരേ ഔട്ട്‌പുട്ട് ക്രമീകരണങ്ങൾ പങ്കിടുന്ന പല റൂട്ടുകളും. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | സൂചിപ്പിച്ച `(root_dir, translations_dir)` ജോഡികൾ. `root_dirs`-നേക്കാളാണ് മുൻഗണന. |
| `repo_url` | `str \| None` | `None` | README ഭാഷാ പട്ടിക മാർഗനിർദ്ദേശം റെൻഡർ ചെയ്യുമ്പോൾ ഉപയോഗിക്കുന്ന Repository URL. |
| `glossaries` | `Iterable[str] \| None` | `None` | വിവർത്തനത്തിനിടെ സംരക്ഷിക്കേണ്ട ഗ്ലോസറി പദങ്ങൾ. പ്രതികൾക്കും ശൂന്യ പദങ്ങൾക്കും നോർമലൈസേഷൻ പ്രശ്‌നങ്ങൾ പരിഹരിക്കുന്നു. |
| `dry_run` | `bool` | `False` | ഫയലുകൾ എഴുതാതെ വിവർത്തന വോളിയവും മൈഗ്രേഷൻ പെരുമാറ്റത്തിനുള്ള മുൻകൂർ ദൃശ്യവൽക്കരണവും കണക്കുകൂട്ടുക. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | ഇൻക്രമെന്റൽ Markdown അപ്‌ഡേറ്റുകൾക്കായുള്ള ഓപ്ഷണൽ accepted-baseline तथा candidate സ്ഥിരത അഡാപ്റ്റർ. ഇത് ഒഴിവാക്കിയാൽ നിലവിലുള്ള മുഴുവൻ-ഫയൽ പെരുമാറ്റം നിലനിർത്തപ്പെടും. |

## റിവ്യൂ പാരാമീറ്ററുകൾ

`run_review` സാധ്യമായിടത്തോളം `run_translation`-ന്റെ സിഗ്നേച്ചറിനെ അനുകരിക്കുന്നു, അതുകൊണ്ടാണ് ഓട്ടോമേഷൻത്തിന് വിവർത്തനവും റിവ്യൂ പ്രവർത്തനങ്ങളിലേക്കുള്ള മാറ്റം കുറഞ്ഞ ശാഖീകരണത്തോടെ സാധ്യമാകുന്നത്.

| പാരാമീറ്റർ | തരം | ഡീഫോൾട്ട് | ഉദ്ദേശ്യം |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | പരിശോധിക്കാനുളള ലക്ഷ്യ ഭാഷാ ഫോൾഡറുകൾ. സ്പേസ്-വിഭജിത സ്ട്രിംഗ്‍കളും Iterable-കളും സ്വീകരിക്കപ്പെടുന്നു. `"all"` കണ്ടെത്തിയ എല്ലാ വിവർത്തനഭാഷകളും പരിശോധിക്കും. |
| `root_dir` | `str` | `"."` | ഒരൊറ്റ റിവ്യൂ ലക്ഷ്യത്തിനുള്ള പ്രോജക്ട് റൂട്ടും. `root_dirs` അല്ലെങ്കിൽ `groups` നൽകിയുള്ളപ്പോൾ ഇത് അവഗണിക്കപ്പെടും. |
| `markdown` | `bool` | `False` | Markdown കൺറന്റ് എന്നിവയും MDX സോഴ്‌സ് ഫയലുകളും ഉൾപ്പെടുത്തുക. |
| `notebook` | `bool` | `False` | Jupyter നോട്ട്‌ബുക്ക് സോഴ്‌സ് ഫയലുകൾ ഉൾപ്പെടുത്തുക. |
| `images` | `bool` | `False` | വിവർത്തന ഓപ്ഷനുകളുമായുള്ള സമതുല്യതയ്ക്കായി സംരക്ഷിച്ചിട്ടുള്ളത്. ഇമേജ് ലിങ്ക് റഫറൻസുകൾ Markdown-ൽ നിന്ന് പരിശോധിക്കപ്പെടുന്നു. |
| `translations_dir` | `str \| None` | `None` | കസ്റ്റം ടെക്സ്റ്റ് വിവർത്തന ഔട്ട്‌പുട്ട് ഡയറക്ടറി. റെലേറ്റീവ് പാതകൾ ഓരോ റൂട്ടിനെയും അടിസ്ഥാനമാക്കി പരിഹരിക്കപ്പെടുന്നു. |
| `root_dirs` | `Iterable[str] \| None` | `None` | ഒരേ ഔട്ട്‌പുട്ട് ക്രമീകരണങ്ങൾ പങ്കിടുന്ന പല റൂട്ടുകളും. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | സൂചിപ്പിച്ച `(root_dir, translations_dir)` ജോഡികൾ. `root_dirs`-നേക്കാളാണ് മുൻഗണന. |
| `changed_from` | `str \| None` | `None` | മാറ്റം വന്ന സോഴ്‌സ് ഫയലുകൾക്ക് മാത്രം റിവ്യൂ പരിധി ഏറൂചെയ്യാൻ ഉപയോഗിക്കുന്ന Git ref. |
| `readme_only` | `bool` | `False` | ഓരോ സോഴ്‌സ് റൂട്ടിന്റെയും കീഴിലെ `README.md` മാത്രം പരിശോധിക്കുക. ഒരു സോഴ്‌സ് README സാന്നിദ്ധ്യമില്ലെങ്കിൽ `ValueError` ഉയരും. |
| `output_format` | `str` | `"text"` | റിവ്യൂ ഔട്ട്‌പുട്ട് ഫോർമാറ്റ്. പിന്തുണയ്ക്കുന്ന മൂല്യങ്ങൾ `"text"` અને `"github"` ആണ്. |
| `fail_on_warnings` | `bool` | `False` | മുന്നറിയിപ്പുകളെ പിഴവുകളോടൊപ്പം പരാജയങ്ങളായി പരിഗണിക്കുക. |
| `debug` | `bool` | `False` | ഡീബഗ് ലോഗിംഗ് സജീവമാക്കുക. |
| `save_logs` | `bool` | `False` | റൂട്ട് `logs/` ഡയറക്ടറിയിലേക്ക് DEBUG നിലയിലെ ലോഗ് ഫയലുകൾ സംരക്ഷിക്കുക. |

`markdown`, `notebook`, അല്ലെങ്കിൽ `images` യിൽ ഒന്നും സജ്ജമാക്കിയില്ലെങ്കിൽ, API ആവശ്യമായ സ്ഥാനങ്ങളിൽ Markdown, നോട്ട്‌ബുക്കുകൾ, അതേസമയം ഇമേജ് ലിങ്ക് റഫറൻസുകൾ പരിശോധിക്കും. റിവ്യൂ LLM പ്രൊവൈഡറെ വിളിക്കുകയില്ല ಮತ್ತು API കീയുകൾ ആവശ്യമില്ല.

## കോൺഫിഗറേഷൻ ആവശ്യകതകൾ

പ്രൊവൈഡർ പിന്തുണയുള്ള വിവർത്തന API-കൾ വിവർത്തനം തുടങ്ങുന്നതിന് മുമ്പ് പ്രൊവൈഡർ കോൺഫിഗറേഷൻ ആവശ്യമാണ്:

- Markdownയും നോട്ട്‌ബുക്ക് വിവർത്തനത്തിനും LLM പ്രൊവൈഡർ ആവശ്യമാണ്. Azure OpenAI, OpenAI, അല്ലെങ്കിൽ Anthropic കോൺഫിഗർ ചെയ്യുക.
- ഇമേജ് വിവർത്തനത്തിന് LLM പ്രൊവൈഡറോടൊപ്പം Azure AI Vision ആവശ്യമാണ്.
- `run_translation` പ്രോജക്ട് വിവർത്തനം തുടങ്ങുന്നതിന് മുമ്പ് ലഘു കണക്ടിവിറ്റി പരിശോധനകൾ നടത്തും.
- ഏജന്റ് സഹായിച്ച `start_*_agent_translation` மற்றும் `finish_*_agent_translation` API-കൾ Co-op Translator LLM പ്രൊവൈഡറുകളെ വിളിക്കാറില്ല. ഹോസ്റ്റായ ആപ്ലിക്കേഷൻ അല്ലെങ്കിൽ MCP ഏജന്റ് തയ്യാറാക്കിയ ചങ്കുകൾ വിവർത്തനം ചെയ്യുന്നു.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, এবং `run_review` നിർണായകമാണ് കൂടാതെ പ്രൊവൈഡർ ക്രെഡൻഷ്യലുകൾ ആവശ്യപ്പെടില്ല.

ആവശ്യമുള്ള Azure OpenAI വേരിയബിളുകൾ:

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

`ANTHROPIC_BASE_URL` and `ANTHROPIC_MAX_TOKENS` ഓപ്ഷണലാണ്. Co-op Translator 0.22.0 മുതലുള്ള എല്ലാ പ്രൊവൈഡർമാർക്കും ഡീഫോൾട്ട് മോഡൽ ക്ലയന്റായി Microsoft Agent Framework നിലനിൽക്കുന്നു. Semantic Kernel താൽക്കാലികമായി `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` എന്നിലൂടെ തിരഞ്ഞെടുക്കാവുന്നതാണ്; എന്നാൽ അത് ഡിപ്പ്രീക്കേഷൻ മുന്നറിയിപ്പ് നൽകും; ഘട്ടബദ്ധമായി നീക്കം ചെയ്യാനുള്ള പദ്ധതി സംബന്ധിച്ച വിശദാംശങ്ങൾക്ക് [കോൺഫിഗറേഷൻ](configuration.md#model-client-backend) കാണുക.

ഇമേജ് വിവർത്തനത്തിന് ആവശ്യമായ Azure AI Vision വേരിയബിളുകൾ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` നിർണായകമാണ് և LLM അല്ലെങ്കിൽ Azure AI Vision കോൺഫിഗറേഷൻ ആവശ്യമില്ല.

## പ്രവർത്തന കുറിപ്പുകൾ

- Content translation API-കൾ വിവർത്തനത്തെ പ്രോജക്ട് പാത്ത് പുനഃരചനയിൽ നിന്ന് വേർതിരിച്ചുനിര്‍ത്തുന്നു. വിവർത്തനം ചെയ്ത ഉള്ളടക്കത്തിന് ലക്ഷ്യസ്ഥലത്തിനായുള്ള പ്രോജക്ട്-സാപേക്ഷ ലിങ്കുകൾ ക്രമീകരിക്കാൻ `rewrite_markdown_paths` അല്ലെങ്കിൽ `rewrite_notebook_paths` വ്യക്തമാകെ വിളിക്കുക.
- പ്രോജക്ട് ഓർക്കസ്ട്രേഷൻ API-കൾ ഫയൽ കണ്ടെത്തൽ, എഴുത്തുകൾ, പാത്ത് പുനഃരചന, മെറ്റാഡേറ്റ, ക്ലീൻഅപ്പ്, ഒപ്പം ഓപ്ഷണൽ ഡിസ്ക്ലെയിമറുകൾ ഉൾപ്പെടെ ഉള്ളടക്ക വിവർത്തനത്തിനുള്ള പ്രോജക്ട് പെരുമാറ്റം കൂട്ടിച്ചേർക്കുന്നു.
- `run_translation` CLI-യുമായി ഉപയോഗിക്കുന്നതേ Rich-ബാക്ക്ഡ് റിപ്പോർട്ടറിലൂടെ പുരോഗതിയും കണക്കുകൂട്ടലുകളുടെ സംഗ്രഹവും പ്രിന്റ് ചെയ്യുകയും ചെയ്യുന്നു. ഇന്ററാക്ടീവ് അല്ലാത്ത ഔട്ട്‌പുട്ടുകൾ സാധാരണ ടെക്സ്റ്റിലേക്ക് fallback ചെയ്യും.
- `dry_run=True` വെർച്വൽ README അപ്ഡേറ്റുകൾ ഉപയോഗിച്ച് കണക്കുകൂട്ടലുകൾ നിർവഹിക്കുന്നു, പക്ഷേ README അല്ലെങ്കിൽ വിവർത്തന ഫയലുകൾ എഴുതുകയില്ല.
- `groups` ക്രമാനുസൃതമായി پروസ്എസ് ചെയ്യപ്പെടുന്നു. ജോലി തുടങ്ങുന്നതിന് മുമ്പ് ഒരു ഏക സംയോജിത കണക്കുകൂട്ടൽ പ്രിന്റുചെയ്യപ്പെടും.
- ഇമേജ് വിവർത്തനം തിരഞ്ഞെടുക്കുകയാണെങ്കിൽ, Vision കോൺഫിഗറേഷൻ കാണപ്പെടാത്തപ്പോൾ വിവർത്തനം ആരംഭിക്കുന്നതിനു മുൻപ് പിശക് ഉയരും.
- നിലവിലുള്ള ആല്യാസ്-അധിഷ്ഠിത ഭാഷാ ഫോൾഡറുകൾ കണ്ടെത്തുകയും റൺ ഭാഗമായി canonical BCP 47 ഫോൾഡർ പേരുകളിലേക്ക് മൈഗ്രേറ്റ് ചെയ്യുന്നതിനുള്ള ഒരുക്കം നടത്തുകയും ചെയ്യാം.
- `run_review` കാണപ്പെടാത്ത വിവർത്തന ഫയലുകൾ, കാണാതോ പഴകിയ വിവർത്തന മെറ്റാഡേറ്റ, തെറ്റായി രൂപകൽപ്പന ചെയ്ത Markdown ഫ്രണ്ട്‌മാറ്റർ/കോഡ് ഫെൻസുകൾ, അസാധുവായ വിവർത്തനം ചെയ്ത നോട്ട്‌ബുക്ക് JSON എന്നിവയുടെ സാഹചര്യത്തിൽ പരാജയപ്പെടും.
- ഡീഫോൾട്ടായി `run_review` പ്രാദേശിക Markdown-യും ഇമേജ് ലിങ്ക് ലക്ഷ്യങ്ങളും കാണാതിരിക്കുന്നത് മുന്നറിയിപ്പുകളായി (warnings) റിപ്പോർട്ട് ചെയ്യും.

## ആന്തരിക കോൾ പാത

API CLI ഉപയോഗിക്കുന്നതേ കോർ ഇംപ്ലിമെൻറേഷനിലേക്ക് ഡെലഗേറ്റ് ചെയ്യുന്നു:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, നോട്ട്‌ബുക്കുകൾ, ഇമേജുകൾ എന്നിവയ്ക്കുള്ള കേന്ദ്രീകൃത പ്രോജക്ട് വിവർത്തന മിക്സിനുകൾ.
8. `co_op_translator.core`-ലുള്ള Markdown, നോട്ട്ബുക്ക്, ടെക്സ്റ്റ്, 및 ഇമേജ് ട്രാൻസ്ലേറ്ററുകൾ.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. നിർണായകമായ ചെക്കുകൾ `co_op_translator.review.checks`-ൽ.

താഴെപ്പറയുന്ന ക്ലാസുകൾ മാന്റെയ്നറുകൾക്ക് ഉപകാരപ്രദമാണ്, എന്നാൽ ഇവ പാക്കേജ്-നിലവാരത്തിലുള്ള സ്ഥിരമായ API ആയി എക്സ്പോർട്ട് ചെയ്തിട്ടില്ല.

| ക്ലാസ് | മൊഡ്യൂൾ | ഉത്തരവാദിത്തം |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | പ്രോജക്ട്-നിലവാര വിവർത്തനം, ഡയറക്ടറി മാനേജ്മെന്റ്, per-language മെറ്റാഡേറ്റ നോർമലൈസേഷൻ, കൂടാതെ Markdown, നോട്ട്‌ബുക്ക്, ഇമേജ് ട്രാൻസ്ലേറ്ററുകളിലേക്ക് ഡെലഗേഷൻ എന്നിവ ഏകോപിപ്പിക്കുന്നു. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, നോട്ട്‌ബുക്കുകൾ, ഇമേജുകൾ, സ്റ്റെയിൽ ഡിറ്റക്ഷൻ, വിവർത്തന മെറ്റാഡേറ്റ അപ്‌ഡേറ്റുകൾ എന്നിവയ്ക്കായി അസിങ്ക് ഫയൽ പ്രോസസ്സിംഗ് പ്രവർത്തനങ്ങൾ നിർവഹിക്കുന്നു. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ഫയൽ റീഡുകൾ, ഉള്ളടക്ക വിവർത്തനം, പാത്ത് പുനഃരചന, മെറ്റാഡേറ്റ, ഡിസ്‌ക്ലെയിമറുകൾ, എഴുത്തുകൾ എന്നിവ ഓർക്കസ്ട്രേറ്റ് ചെയ്യുന്നു. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | നോട്ട്‌ബുക്ക് ഫയൽ റീഡുകൾ, Markdown സെൽ വിവർത്തനം, പാത്ത് പുനഃരചന, മെറ്റാഡേറ്റ, ഡിസ്‌ക്ലെയിമറുകൾ, എഴുത്തുകൾ എന്നിവ ഓർക്കസ്ട്രേറ്റ് ചെയ്യുന്നു. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | സോഴ്സ് ഇമേജ് കണ്ടെത്തൽ, ഇമേജ് വിവർത്തനം, ഔട്ട്‌പുട്ട് പാതകൾ, മെറ്റാഡേറ്റ, എഴുത്തുകൾ എന്നിവ ഓർക്കസ്ട്രേറ്റ് ചെയ്യുന്നു. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | വിവർത്തനപ്പെട്ട Markdown ജോഡികൾ കണ്ടെത്തുന്നു, വിവർത്തന ഗുണനിലവാരം വിലയിരുത്തുന്നു, കുറഞ്ഞ ആത്മവിശ്വാസമുള്ള മറക്കൽ പ്രവാഹങ്ങൾക്ക് വേണ്ടി കൺഫിഡൻസ് മെറ്റാഡേറ്റ വായിക്കുന്നു. |
| `ReviewRunner` | `co_op_translator.review.runner` | സോഴ്‌സ് ഫയലുകൾ, ലക്ഷ്യ ഭാഷകൾ, കോൺഫിഗർ ചെയ്ത വിവർത്തന റൂട്ടുകൾ എന്നിവയ്ക്ക് മദ്ധ്യേ നിർണായക റിവ്യൂ ചെക്കുകൾ ഏകോപിപ്പിക്കുന്നു. |
| `ReviewTarget` | `co_op_translator.review.targets` | ഒരു സോേഴ്‌സ് റൂട്ട്, ആ റൂട്ടിന് പരിശോധിക്കപ്പെടുന്നത് എന്നതും ആ റൂട്ടിനുള്ള വിവർത്തന ഔട്ട്‌പുട്ട് ഡയറക്ടറിയും വിവരണം നൽകുന്നു. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | പൂർവ്വകാല ആല്യാസ് ഭാഷാ ഫോൾഡറുകൾ കണ്ടെത്തുകയും canonical BCP 47 ഫോൾഡറിലേക്ക് മൈഗ്രേഷൻ പദ്ധതികൾ തയ്യാറാക്കുകയും ചെയ്യുന്നു. |
| `Config` | `co_op_translator.config.base_config` | `.env` ഫയലുകൾ ലോഡ് ചെയ്യുകയും ആവശ്യമായ LLM-കളും ഓപ്ഷണൽ Vision പ്രൊവൈഡറുകളും കോൺഫിഗർ ചെയ്തിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുകയും ചെയ്യുന്നു. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI, അല്ലെങ്കിൽ Anthropic സ്വയം കണ്ടെത്തുകയും ആവശ്യവുമായ environment വേരിയബിളുകൾ സാധൂകരിക്കുകയും പ്രൊവൈഡർ കണക്റ്റിവിറ്റി ചെക്കുകൾ നടത്തുകയും ചെയ്യുന്നു. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision കോൺഫിഗറേഷൻ കണ്ടെത്തുകയും ഇമേജ് വിവർത്തനത്തിന് കണക്റ്റിവിറ്റി ചെക്കുകൾ നടത്തുകയും ചെയ്യുന്നു. |