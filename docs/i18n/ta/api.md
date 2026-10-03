# Python API

நிலையான பொது Python API `co_op_translator.api` இருந்து ஏற்றுமதி செய்யப்படுகிறது. பெரும்பாலான ஒருங்கிணைப்புகள் பின்வரும் பணிமுறைகளில் ஒன்றைப் பயன்படுத்துகின்றன:

| நிலை | எப்போது பயன்படுத்தவேண்டும் | முக்கிய API-கள் |
| --- | --- | --- |
| Translate individual files or documents | உங்கள் பயன்பாடு மூல உள்ளடக்கத்தை படிக்கிறது, மொழிபெயர்ப்புக்கு Co-op Translator-ஐ அழைக்கிறது, மற்றும் முடிவை எங்கு சேமிக்க வேண்டும் என்பதை தீர்மானிக்கிறது. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| ஹோஸ்ட்-ஏஜென்ட் மொழிபெயர்ப்பிற்கு உள்ளடக்கத்தை தயாரிக்க | உங்கள் MCP ஹோஸ்ட் அல்லது பயன்பாட்டு மாதிரி துண்டுகளை மொழிபெயர்க்கும், Co-op Translator துண்டாக்கம் மற்றும் மீண்டும் கட்டமைப்பை கையாள்கிறது. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | நீங்கள் Python API CLI போல செயல்பட்டு, கண்டறிதல், வெளியீட்டு பாதைகள், மெட்டாடேட்டா, சுத்திகரிப்பு, மற்றும் கோப்புகள் எழுதுதல் ஆகியவை கையாள வேண்டும். | `run_translation` |

`core`, `config`, `review`, மற்றும் `utils` கீழ் உள்ள பெரும்பாலான கீழ்நிலைக் தொகுதிகள் இந்த API நுழைவு புள்ளிகள் பயன்படுத்தும் செயல்படுத்தல் விவரங்களே.

MCP கிளையண்டுகள் [MCP சேவையகம்](mcp.md) மூலம் அதே பொது API-ஐப் பயன்படுத்துகின்றன. Python-ஐ நேரடியாக அழைக்கும் போது இந்த பக்கத்தைப் பயன்படுத்தவும், Co-op Translator-ஐ ஏஜென்ட் அல்லது எடிட்டருக்கு வெளிப்படுத்தும்போது MCP வழிகாட்டியைப் பயன்படுத்தவும். CLI, Python API, மற்றும் MCP இடையில் தீர்மானிக்கிறீர்களானா என்றால், [உங்கள் வேலைவழியைத் தேர்ந்தெடுக்கவும்](workflows.md) என்றதிலிருந்து தொடங்கவும்.

## முதன்முறை API ஓட்டம்

Python கோட்நூலிலிருந்து Co-op Translator-ஐ அழைக்கிறீர்களானால் இங்கே இருந்து தொடங்கவும்:

1. [Configuration](configuration.md) இல் விவரிக்கப்பட்டபடி ஒரு LLM வழங்குநரை அமைக்கவும் — நீங்கள் ஹோஸ்ட்-ஏஜென்ட் மொழிபெயர்ப்பிற்கு மட்டும் Markdown அல்லது நோட்புக் துண்டுக்களை தயாரித்து கொண்டிருக்கிறீர்கள் என்றால் இது தேவையில்லை.
2. உங்கள் பயன்பாடு கோப்பு I/O-ஐ சொந்தமாக கையாளுகிறதா என்பதை தீர்மானிக்கவும்.
3. உங்கள் பயன்பாடு தனி கோப்புகளைப் படித்து எழுதும்போது உள்ளடக்க API-களைப் பயன்படுத்தவும்.
4. Co-op Translator CLI போல ஒரு ரெப்பொசிட்டரியை செயலாக்க வேண்டும் என்றால் `run_translation`-ஐப் பயன்படுத்தவும்.
5. தானாக செயல்படுத்தலில் நிரந்தரமான சோதனைகள் தேவைப்பட்டால் மொழிபெயர்ப்புக்குப் பிறகு `run_review`-ஐப் பயன்படுத்தவும்.

| Goal | API to start with |
| --- | --- |
| ஒரு Markdown ஸ்ட்ரிங் அல்லது கோப்பை மொழிபெயர்க்கவும் | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| ஹோஸ்ட்-ஏஜென்டு Markdown அல்லது நோட்புக் துண்டுகளை மொழிபெயர்க்க அனுமதிக்கவும் | `start_markdown_agent_translation` அல்லது `start_notebook_agent_translation` |
| வெளியீட்டு பாதையை தேர்ந்தெடுத்த பிறகு மொழிபெயர்க்கப்பட்ட இணைப்புகளை மறுசீரமைக்கவும் | `rewrite_markdown_paths` அல்லது `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## நிலை 1: தனி கோப்புகள் அல்லது ஆவணங்களை மொழிபெயர்த்தல்

உங்கள் கையில already ஒரு கோப்பு, எடிட்டர் பஃபர், நோட்புக் தரவு, MCP கோரிக்கை, அல்லது தனிப்பயன் பைப்லைன் உள்ளீடு இருந்தால் இந்த வேலைநடத்தைப் பயன்படுத்தவும். கோப்பு I/O-வை உங்கள் குறியீடு நிர்வகிக்கும்:

1. Read the source content.
2. Call a content translation API.
3. மொழிபெயர்க்கப்பட்ட உள்ளடக்கம் ஒரு திட்டப் மொழிபெயர்ப்பு அடைவிற்கு எழுதப்படவிருந்தால் விருப்பத்துக்கு படி பாதை மறுஸ்திருத்த API-ஐ அழைக்கவும்.
4. உங்கள் பயன்பாட்டில் இருந்து முடிவை சேமிக்கவும் அல்லது திருப்பி வழங்கவும்.

உள்ளடக்க மொழிபெயர்ப்பு API-கள் திட்ட கண்டறிதலையும் இயக்காது, மெட்டாடேட்டாவை எழுதாது, பொறுப்புரிமைக் குறிப்பு சேர்க்காது, மற்றும் இணைப்புகளை தானாக மறுசீரமைக்காது.

### Markdown கோப்பு

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

மொழிபெயரிக்கப்பட்ட Markdown Co-op Translator திட்ட அமைப்பில் இருக்கும் இல்லையெனில், `rewrite_markdown_paths`-ஐத் தவிர்த்து மொழிபெயர்க்கப்பட்ட சரத்தை நேரடியாக சேமிக்கவும்.

### நோட்புக் கோப்பு

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

`translate_notebook_content` Markdown செல்களை மொழிபெயர்க்கிறது மற்றும் Markdown அல்லாத செல்களை பாதுகாக்கிறது. பாதை மறுஸ்திருத்தம் மட்டுமே Markdown செல்களுக்கு பொருந்தும்.

### படக் கோப்பு

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

`translate_image_content` மூல படத்தை வாசித்து உருவாக்கப்பட்ட `PIL.Image.Image` ஐ திருப்பி வழங்குகிறது. இது மொழிபெயர்க்கப்பட்ட பட மெட்டாடேட்டாவை எழுதாது.

## நிலை 2: ஒரு முழு ரெப்பொசிட்டரியை மொழிபெயர்த்தல்

Python API-ஐ `translate` CLI போன்ற வழியில் செயல்படச் செய்ய வேண்டும் என்றால் இந்த வேலைநடத்தைப் பயன்படுத்தவும். `run_translation` ஆதரிக்கப்படுகிற கோப்புகளை கண்டறிந்து, தேர்ந்தெடுக்கப்பட்ட உள்ளடக்க வகைகளை மொழிபெயர்த்து, பாதைகளைக் மறுதேர்மானித்து, வெளியீடு கோப்புகளை எழுதியும், மெட்டாடேட்டாவை புதுப்பித்தும், சுத்திகரிப்பு போன்ற மொழிபெயர்ப்பு பராமரிப்பு பணிகளைச் செய்கிறது.

`run_translation` என்பது முன்னுரிமையான திட்ட ஒழுங்கமைப்பு நுழைவு புள்ளியாகும். `translate_project` அதே நடத்தை கொண்ட இணக்கப்பெயராக ஏற்றுமதி செய்யப்பட்டிருக்கிறது.

தற்போதைய ரெப்போசிட்டரியில் உள்ள Markdown கோப்புகளை கொரிய மற்றும் ஜப்பானிய மொழிகளில் மொழிபெயர்க்கவும்:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

ஒரு குறிப்பிட்ட திட்ட ரூட்-இல் இருந்து மட்டுமே நோட்புக் கோப்புகளை மொழிபெயர்க்க:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

கோப்புகளை எழுதாமலேயே மொழிபெயர்ப்பு அளவை முன்னோட்டமாகக் காண்க:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

ஒரு ஒருங்கிணைப்பிற்கான கட்டமைவாய்ந்த முன்னேற்ற நிகழ்வுகளை பதிவு செய்க:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # தகவல் தொகுதியை உங்கள் வேலை-நிகழ்வு அட்டவணையில் சேமிக்கவும் அல்லது அதை உங்கள் பயனர் இடைமுகத்திற்கு ஸ்ட்ரீம் செய்யவும்.


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

ஒரே அழைப்பில் பல உள்ளடக்க மூலங்களை மொழிபெயர்க்க:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

மொழிபெயர்ப்புகளை தெளிவான வெளியீட்டு குழுக்களில் எழுதுக:

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

ஒவ்வொரு மொழிக்காக உள்-அடைவை கொண்டிருக்க வேண்டும் என்றால் மொழி-வாரியான placeholder ஒன்றைப் பயன்படுத்தவும்:

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

`markdown`, `notebook`, அல்லது `images` எதுவுமும் அமைக்கப்படவில்லை என்றால், API அனைத்து ஆதரிக்கப்பட்ட வகைகளையும் மொழிபெயர்க்கும்: Markdown, நோட்புக் கோப்புகள், மற்றும் படங்கள்.

### TranslationStateProvider உடன் ஏற்றுக்கொள்ளப்பட்ட மனித திருத்தங்களை பாதுகாக்குதல்

இயல்பாக, Co-op Translator அதன் தற்போதைய கோப்பு-அடிப்படையின்மான நடத்தையை பேணுகிறது:
Markdown மூலங்கள் பழையதாக இருந்தால், முழு மொழிபெயர்க்கப்பட்ட கோப்பும் மீண்டும் உருவாக்கப்படுகிறது. ஹோஸ்ட்
ஒருங்கைப்புகள் விருப்பத்தின்படி `TranslationStateProvider`-ஐ வழங்கி மாற்றமில்லாத
மூல தொகுதிகளில் மனிதரால் செய்யப்பட்ட திருத்தங்களை பாதுகாக்கலாம்.

சேவை வழங்குநர் கடைசியாக ஏற்கப்பட்ட மூல/இலக்கு ஜோடியை வழங்கி ஒவ்வொரு புதிய பரிந்துரையையும் பதிவுசெய்கிறது.
ஏற்றுக்கொள்வது ஒருங்கிணைப்பின் பொறுப்பாகவே இருக்கும் — உதாரணத்திற்கு,
ஒரு மொழிபெயர்ப்பு pull request இணைக்கப்பட்டபின்:

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

ஏற்றுக்கொள்ளப்பட்ட செல்லுபடியான அடிப்படை (baseline) கொண்ட Markdown கோப்புகளுக்கு, Co-op Translator மேற்பார்வை Markdown தொகுதிகளை ஒத்திசைக்கிறது
மேல்நிலை Markdown தொகுதிகள். மாற்றமில்லாத மூல தொகுதிகள் தற்போதைய மொழிபெயர்க்கப்பட்ட
தொகுதிகள், மனிதர்களால் செய்யப்பட்ட திருத்தங்களையும் 포함செய்து, மீண்டும் பயன்படுத்தப்படுகின்றன; மாற்றப்பட்ட அல்லது சேர்க்கப்பட்ட மூல தொகுதிகள் மொழிபெயர்க்க
அனுப்பப்படுகின்றன; நீக்கப்பட்ட மூல தொகுதிகள் அகற்றப்படுகின்றன. ஒத்திசைவு தெளிவற்றதாயின்,
இலக்கு கட்டமைப்பு மாறியிருந்தால், ஒரு தொகுதி மொழிபெயர்ப்பு செல்லுபடியற்றதாக இருந்தால், அல்லது ஏதேனම් அடிப்படை கிடைக்கவில்லையென்றால்,
Co-op Translator பாதுகாப்பாக உள்ளமுள்ள முழு-கோப்பு மொழிபெயர்ப்பு பாதைக்கு திரும்பும்.
மொழிபெயர்ப்பு பாதை.

இந்த API ஆவண மொழிபெயர்ப்பு நிலையை சேமிக்கிறது, ஆவணங்களுக்கிடையிலான சொற்றொடர் அல்லது
பகுதி மொழிபெயர்ப்பு நினைவகத்தை அல்ல. இது தற்போது Markdown திட்ட மொழிபெயர்ப்பிற்கு பொருந்தும்.
மொழிபெயர்ப்பு. நோட்புக் மற்றும் பட நடத்தை மாற்றமற்றதாகவே உள்ளது. `update=True`
இன்னும் முழு மறுசீரமைப்பை கோருகிறது.

ஒரு அல்லது பல கோப்புகளை மொழிபெயர்க்க முடியாவிட்டால், `run_translation`
`RuntimeError`-ஐ திட்ட பணிநடவடிக்கை முடிந்தவுடன் எழுப்பும், இல்லாத வெளியீடு இருந்தபோதும் வெற்றிகரமான ஓட்டத்தை தெரிவிக்காமல்.
ஒருங்கிணைப்புகள் இதை தோல்வியான வேலையாக கருத வேண்டும் மற்றும்
முந்தைய ஏற்கப்பட்ட மொழிபெயர்ப்பு நிலையைப் பேணிக்கொள்ள வேண்டும்.

## மொழிபெயர்க்கப்பட்ட வெளியீட்டை மதிப்பாய்வு

`run_review` LLM அல்லது Vision அங்கீகாரங்கள் இல்லாமல் தீர்மானமான மொழிபெயர்ப்பு சோதனைகளை இயக்குகிறது.

!!! note "பீட்டா"
    `run_review` ஒரு பீட்டா தீர்மானமான மதிப்பாய்வு API ஆகும். இது மாடல் வழங்குநர்களை அழைக்காது அல்லது கோப்புகளை எழுதாது, ஆனால் சரிபார்ப்புகள் மற்றும் issue ஸ்கீமாக்கள் மாறக்கூடும்.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README மட்டமான மொழிபெயர்ப்புக்குப் பிறகு, மதிப்பாய்விற்கு அதே பரப்பினை பயன்படுத்தவும்:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` reviews only `README.md` under each configured source root,
including custom `groups` and output directories. Other documents and nested
READMEs are excluded. A missing source README raises `ValueError`; failed
translation checks raise `RuntimeError`.

base ref-க்கெதிராக மாற்றப்பட்ட கோப்புகளை மட்டும் மதிப்பாய்வு செய்து GitHub-வடிவிலான வெளியீட்டை அச்சிடவும்:

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

## காப்பி-பேஸ்ட் API எடுத்துக்காட்டுகள்

கோப்புகளை எழுதாமலே Markdown உள்ளடக்கத்தை மொழிபெயர்க்க:

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

## பொது நுழைவு புள்ளிகள்

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

## உள்ளடக்கம் மொழிபெயர்ப்பு API-கள்

உள்ளடக்கம் மொழிபெயர்ப்பு APIகள், ஏற்கனவே உள்ளடக்கத்தை நினைவில் வைத்திருக்கும் ஒருங்கிணைப்புகளுக்காக முகாம்படுத்தப்பட்டவை, உதாரணமாக ஒரு எடிட்டர் விரிவாக்கம், MCP கருவி, நோட்புக் செயலி, அல்லது தனிப்பயன் பைப்ப்லைன்.

| செயல்பாடு | உள்ளீடு | வெளியீடு | கோப்பு I/O | குறிப்புகள் |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | இல்லை | அசிங்க். Markdown உள்ளடக்கத்தை மட்டும் மொழிபெயர்க்கிறது. இது இணைப்புகளை மறுஸ்திருத்தாது, மெட்டாடேட்டாவை எழுதாது, அல்லது மறுக்கல் குறிப்புகளை இணைக்காது. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | இல்லை | அசிங்க். Markdown செல்களை மொழிபெயர்க்கிறது மற்றும் Markdown அல்லாத செல்களை பாதுகாக்கிறது. இது இணைப்புகளை மறுஸ்திருத்தாது, மெட்டாடேட்டாவை எழுதாது, அல்லது மறுக்கல் குறிப்புகளை இணைக்காது. |
| `translate_image_content` | Image path | `PIL.Image.Image` | மூல படத்தை மட்டுமே வாசிக்கிறது | ஒத்திசைவு. படம் உரையை பிரித்து மொழிபெயர்த்து, பின்னர் உருவாக்கப்பட்ட படத்தை திருப்பி வழங்குகிறது. இது மொழிபெயர்க்கப்பட்ட படம் மெட்டாடேட்டாவை சேமிக்காது. |

`translate_markdown_content` மற்றும் `translate_notebook_content` அவர்களது விருப்பங்களின் மூலம் ஒரு விருப்பமான `source_path`-ஐ ஏற்கக் கொள்ளும். பாதை மொழிபெயர்ப்பாளருக்கு ச-context-ஆக அனுப்பப்படுகிறது; மொழிபெயர்ப்புக்குப் பிறகு திட்ட-சார்ந்த எந்தவொரு பாதை மறுஎழுத்துக்கும் அழைப்பாளரே பொறுப்பவர்களாக இருப்பார்கள்.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

அதே விருப்பங்களை அகராதிகளாக (dictionaries) அனுப்பலாம்:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## ஏஜென்ட்-ஆதரித்த மொழிபெயர்ப்பு API-கள்

ஏஜென்ட்-உதவியுடன் APIகள் Co-op Translator உடன் கட்டமைக்கப்பட்ட LLM வழங்குநரை அழைக்கமாட்டند. அவை ஹோஸ்ட் ஏஜென்ட் மொழிபெயர்க்க Markdown அல்லது நோட்புக் துணுக்குகளை தயார் செய்து, பின்னர் மொழிபெயரிக்கப்பட்ட துணுக்குகளிலிருந்து இறுதி உள்ளடக்கத்தை மீளமைக்கின்றன.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | துணுக்குகள், prompts மற்றும் மீளமைக்கல் நிலை உடன் ஒரு சுய-கொண்ட Markdown பணியை திருப்பி அளிக்கிறது. |
| `finish_markdown_agent_translation` | ஒரு பணி மற்றும் ஹோஸ்ட்-ஏஜென்ட் மொழிபெயர்த்த துணுக்குகளிலிருந்து Markdown-ஐ மீளமைக்கிறது. |
| `start_notebook_agent_translation` | ஹோஸ்ட்-ஏஜென்ட் மொழிபெயர்ப்பிற்கு Markdown-செல் துணுக்குகளுடன் நோட்புக் பணியை திருப்பி அளிக்கிறது. |
| `finish_notebook_agent_translation` | குறியீட்டு செல்கள், வெளியீடுகள் மற்றும் மெட்டாடேட்டாவை பாதுகாத்து நோட்புக் JSON-ஐ மீளமைக்கிறது. |

இந்த வேலை 흐름ம் பெரும்பாலும் MCP ஹோஸ்டுகளுக்காக மட்டுமே நோக்கமாக உள்ளது. Co-op Translator வழங்குநர் அழைப்புகளை நிர்வகித்து உற்பத்தி ரெப்போசிடரி மொழிபெயர்ப்பு தேவையெனில், `translate_markdown_content`, `translate_notebook_content`, அல்லது `run_translation`-ஐ பயன்படுத்தவும்.

## பாதை மறுஎழுதல் API-கள்

பாதை மறுவழிச் சீரமைப்பு APIகள் மொழிபெயர்ப்பு செய்யாது. அவை மூல பாதை, மொழிபெயர்க்கப்பட்ட இலக்கு பாதை மற்றும் திட்ட அமைப்பு தெரிந்த பிறகு இணைப்புகள் மற்றும் frontmatter பாதைகளை புதுப்பிக்கின்றன.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown உள்ளடக்கம் மற்றும் frontmatter | மொழிபெயர்க்கப்பட்ட இலக்குக்காக Markdown இணைப்புகள் மற்றும் ஆதரிக்கப்படும் frontmatter பாதை புலங்களை மீண்டும் எழுதுகிறது. |
| `rewrite_notebook_paths` | Notebook JSON இல் Markdown செல்கள் | ஒவ்வொரு Markdown செல்லிலும் Markdown பாதை மறுஇழுத்துதலைப் பயன்படுத்துகிறது மற்றும் non-Markdown செல்களை மாற்றமில்லாமல் வைக்கும். |

`policy` என்ற argument கீழ்க்கண்ட புலங்களை கொண்ட ஒரு அகராதியாக இருக்கலாம்:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | இல்லை | செயல்படுத்தப்பட்ட மொழிபெயர்ப்பு வகைகள். இயல்பாக Markdown, நோட்புக்குகள் மற்றும் படங்கள். |
| `lang_subdir` | இல்லை | ஒவ்வொரு மொழி கோப்புறை கீழேயும் விருப்பமான உபகோப்பகம். |

## திட்ட மொழிபெயர்ப்பு அளவுருக்கள்

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | அவசியம் | இடவெளியால் பிரிக்கப்பட்ட இலக்கு மொழி குறியீடுகள், உதாரணமாக `"ko ja fr"`, அல்லது `"all"`. மாற்று குறியீடுகள் canonical BCP 47 மதிப்புகளுக்கு சாதாரணப்படுத்தப்படுகின்றன. |
| `root_dir` | `str` | `"."` | ஒரு தனி மொழிபெயர்ப்பு இலக்குக்கான திட்டத்தின் மூலக் கோப்புறை. `root_dirs` அல்லது `groups` வழங்கப்பட்டால் புறக்கணிக்கப்படும். |
| `update` | `bool` | `False` | தேர்ந்தெடுக்கப்பட்ட மொழிகளுக்காக உள்ள மொழிபெயர்ப்புகளை நீக்கி மீண்டும் உருவாக்குகிறது. |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | DEBUG-நிலை பதிவுக் கோப்புகளை ரூட் `logs/` கோப்புறையின் கீழ் சேமிக்கவும். |
| `yes` | `bool` | `True` | நிரலாக்க மற்றும் CI பயன்பாட்டிற்கு வரும் வைத்தல்களை தானாக உறுதிசெய்கிறது. |
| `add_disclaimer` | `bool` | `False` | மொழிபெயர்க்கப்பட்ட Markdown மற்றும் நோட்பூக்களில் மெஷின் மொழிபெயர்ப்பு குறித்த விளக்க குறிப்புகளைச் சேர்க்கவும். |
| `translations_dir` | `str \| None` | `None` | தனிப்பயன் உரை மொழிபெயர்ப்பு வெளியீட்டு கோப்புறை. சார்பு பாதைகள் ஒவ்வொரு மூலத்திற்கும் அடிப்படையில் தீர்மானிக்கப்படுகின்றன. |
| `image_dir` | `str \| None` | `None` | மொழிபெயர்க்கப்பட்ட படங்களுக்கான தனிப்பயன் வெளியீட்டு கோப்புறை. சார்பு பாதைகள் ஒவ்வொரு மூலத்திற்கும் அடிப்படையில் தீர்மானிக்கப்படுகின்றன. |
| `root_dirs` | `Iterable[str] \| None` | `None` | அதே வெளியீட்டு அமைப்புகளைப் பகிரும் பல மூல அடைவுகள். |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | தெளிவான `(root_dir, translations_dir)` ஜோடிகள். `root_dirs` விட முன்னுரிமை பெறும். |
| `repo_url` | `str \| None` | `None` | README மொழி அட்டவணை வழிகாட்டியை உருவாக்கும் போது பயன்படுத்தப்படும் ரெப்பொசிட்டரி URL. |
| `glossaries` | `Iterable[str] \| None` | `None` | மொழிபெயர்ப்பின் போது பாதுகாக்க வேண்டிய அகராதி வார்த்தைகள். நகல்களும் காலியான சொற்களும் சீரமைக்கப்படுகின்றன. |
| `dry_run` | `bool` | `False` | கோப்புகளை எழுதாமல் மொழிபெயர்வு பரிமாணத்தை மதிப்பிடவும் மற்றும் மைக்ரேஷன் நடத்தை முன்னோட்டமாக பார்க்கவும். |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | இங்குதான் ஏற்றுக்கொள்ளப்பட்ட-அடிப்படை மற்றும் வேட்பாளர் நிலைத்தன்மை வழங்கும் விருப்பமான அடாப்டர் (incremental Markdown புதுப்பிப்புகளுக்காக). இதனை விடுத்தால் முந்தைய முழு-கோப்பு நடத்தை பாதுகாக்கப்படும். |

## பரிசீலனை அளவுருக்கள்

`run_review` திட்டமிட்டவாறு `run_translation` கையொப்பத்துடன் சாத்தியமான அளவு வரை ஒத்திருக்கும், ஆகையால் ஆட்டோமேஷன் குறைந்த கிளை பிரிவுகளுடன் மொழிபெயர்ப்பு மற்றும் பரிசீலனை வேலைபாடுகளை மாறிக்கொள்ள முடியும்.

| அளவுரு | வகை | இயல்புநிலை | பயன் |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | பரிசீலிக்க வேண்டிய இலக்கு மொழி கோப்புறைகள். வெற்றிடத்தால் பிரிக்கப்பட்ட சரங்கள் மற்றும் Iterable வகைகள் ஏற்றுக் கொள்ளப்படுகின்றன. `"all"` கண்டறியப்பட்ட அனைத்து மொழிபெயர்ப்பு மொழிகளையும் பரிசீலிக்கும். |
| `root_dir` | `str` | `"."` | ஒரே பரிசீலனை இலக்குக்கான திட்டத்தின் மூல அடைவு. `root_dirs` அல்லது `groups` வழங்கப்பட்டால் இது புறக்கணிக்கப்படும். |
| `markdown` | `bool` | `False` | Markdown மற்றும் MDX மூலக் கோப்புகளைச் சேர்க்கவும். |
| `notebook` | `bool` | `False` | Jupyter நோட்புக் மூலக் கோப்புகளைச் சேர்க்கவும். |
| `images` | `bool` | `False` | மொழிபெயர்ப்பு விருப்பங்களுடன் ஒத்துழைவு செய்யுவதற்காக ஒதுக்கப்பட்டுள்ளது. படங்களுக்கான இணைப்பு குறிப்புகள் Markdown இல் இருந்து சரிபார்க்கப்படும். |
| `translations_dir` | `str \| None` | `None` | தனிப்பயன் உரை மொழிபெயர்ப்பு வெளியீட்டு கோப்புறை. சார்பு பாதைகள் ஒவ்வொரு மூலத்திற்கும் அடிப்படையில் தீர்மானிக்கப்படுகின்றன. |
| `root_dirs` | `Iterable[str] \| None` | `None` | அதே வெளியீட்டு அமைப்புகளைப் பகிரும் பல மூல அடைவுகள். |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | தெளிவான `(root_dir, translations_dir)` ஜோடிகள். `root_dirs` விட முன்னுரிமை பெறும். |
| `changed_from` | `str \| None` | `None` | மாற்றப்பட்ட மூலக் கோப்புகளுக்கு மட்டும் பரிசீலனையை வரையறுக்க பயன்படும் Git ref. |
| `readme_only` | `bool` | `False` | ஒவ்வொரு மூல அடைவின் கீழுள்ள `README.md` மட்டும் பரிசீலிக்கவும். மூல README இல்லையெனில் `ValueError` எழுக்கும். |
| `output_format` | `str` | `"text"` | பரிசீலனை வெளியீட்டு வடிவம். ஆதரிக்கப்படும் மதிப்புகள் `"text"` மற்றும் `"github"`. |
| `fail_on_warnings` | `bool` | `False` | எச்சரிக்கைகளை பிழைகளுக்கு கூடுதலாக தோல்விகளாகச் கருதும். |
| `debug` | `bool` | `False` | டீபக் பதிவு செயல்படுத்தவும். |
| `save_logs` | `bool` | `False` | DEBUG நிலை பதிவு கோப்புகளை மூல `logs/` அடைவுக்குள் சேமிக்கவும். |

`markdown`, `notebook`, அல்லது `images` எதுவும்தான் அமைக்கப்படாவிட்டால், API பொருத்தமான இடங்களில் Markdown, நோட்புக் மற்றும் பட இணைப்பு குறிப்புகளை பரிசீலிக்கும். பரிசீலனை LLM வழங்குநரை அழைக்காது மற்றும் API விசைகள் தேவையில்லை.

## கட்டமைப்பு தேவைகள்

வழங்குநர் ஆதரித மொழிபெயர்ப்பு APIகள் மொழிபெயர்ப்புக்கு முன்பு வழங்குநரின் கட்டமைப்பை தேவைப்படுத்துகின்றன:

- Markdown மற்றும் நோட்புக் மொழிபெயர்ப்பிற்கு LLM வழங்குநர் தேவை. Azure OpenAI, OpenAI, அல்லது Anthropic ஐ அமைக்கவும்.
- பட மொழிபெயர்ப்பிற்கு LLM வழங்குநருக்கு கூடுதலாக Azure AI Vision தேவை.
- `run_translation` திட்ட மொழிபெயர்ப்பு தொடங்குவதற்கு முன் இலகு இணைப்பு சரிபார்ப்புகளை இயக்குகிறது.
- முகவரியால் உதவியிக்கப்பட்ட `start_*_agent_translation` மற்றும் `finish_*_agent_translation` APIகள் Co-op Translator LLM வழங்குநர்களை அழைக்காது. ஹோஸ்ட் பயன்பாடு அல்லது MCP முகவர் தயாரிக்கப்பட்ட துண்டுகளை மொழிபெயர்க்கும்.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, மற்றும் `run_review` தீர்மானமானவை மற்றும் வழங்குநர் அங்கீகாரங்கள் தேவையில்லை.

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

`ANTHROPIC_BASE_URL` மற்றும் `ANTHROPIC_MAX_TOKENS` விருப்பமானவையாகும். Co-op Translator 0.22.0 இலிருந்து அனைத்து வழங்குநர்களுக்கும் Microsoft Agent Framework இயல்புநிலை மாடல் கிளையன்ட் ஆகும். Semantic Kernel-ஐ தற்காலிகமாக `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` மூலம் இன்னும் தேர்ந்தெடுக்கலாம், ஆனால் அதைச் செய்வதால் நீக்கப்படுவதைச் சார்ந்த ஒரு எச்சரிக்கை வெளியிடப்படும்; கட்டப்படுத்தப்பட்ட நீக்கத் திட்டத்தைப் பார்க்க [configuration](configuration.md#model-client-backend).

பட மொழிபெயர்ப்பிற்கு தேவையான Azure AI Vision மாறிகள்:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` தீர்மானமானது மற்றும் LLM அல்லது Azure AI Vision கட்டமைப்பை தேவையாக்காது.

## நடத்தை குறிப்புகள்

- உள்ளடக்க மொழிபெயர்ப்பு APIகள் மொழிபெயர்ப்பை திட்ட பாதை மீளமைப்பிலிருந்து தனியாக வைத்திருக்கின்றன. மொழிபெயர்க்கப்பட்ட உள்ளடக்கம் இலக்கு இடத்திற்கு திட்ட சார்ந்த இணைப்புகளை சரிசெய்ய வேண்டும் என்றால் `rewrite_markdown_paths` அல்லது `rewrite_notebook_paths` ஐ வெளிப்படையாக அழைக்கவும்.
- திட்ட ஒழுங்கமைப்பு APIகள் உள்ளடக்க மொழிபெயர்ப்பை சுற்றியும் திட்ட நடத்தை சேர்க்கின்றன, இதில் கோப்பு கண்டறிதல், எழுதுதல், பாதை மறுசீரமைப்பு, மெட்டா டேட்டா, சுத்தம் செய்யுதல் மற்றும் விருப்பமான மறுப்புரைகள் ஆகியவை சேரும்.
- `run_translation` CLI இல் பயன்படுத்தப்படும் அதே Rich-ஆதாரப்பட்ட ரிப்போர்டரைப் பயன்படுத்தி முன்னேற்றம் மற்றும் மதிப்பீட்டு சுருக்கங்களை அச்சிடுகிறது. இடைமுகமில்லா வெளியீடு சாதாரண உரையாகக் காட்டப்படும்.
- `dry_run=True` மெய்நிகர் README புதுப்பிப்புகளை பயன்படுத்தி மதிப்பீடுகளை கணக்கிடுகிறது, ஆனால் README அல்லது மொழிபெயர்ப்பு கோப்புகளை எழுதாது.
- `groups` வரிசையாக செயலாக்கப்படுகின்றன. வேலைத் தொடங்குவதற்கு முன் ஒரு ஒற்றை ஒருங்கிணைந்த மதிப்பீடு அச்சிடப்படும்.
- பட மொழிபெயர்ப்பு தேர்ந்தெடுக்கப்பட்டால், Vision கட்டமைப்பு காணப்படவில்லையெனில் மொழிபெயர்ப்பு தொடங்குவதற்கு முன் பிழை எழுப்பப்படும்.
- Existing alias-based language folders are detected and can be migrated to canonical BCP 47 language folder names as part of the run.
- `run_review` மொழிபெயர்க்கப்பட்ட கோப்புகள் காணப்படாமை, மொழிபெயர்ப்பு மெட்டா டேட்டா காணப்படாமை அல்லது பழையதாமை, தவறான வடிவமைக்கப்பட்ட Markdown frontmatter/code fences, மற்றும் செல்லாத மொழிபெயர்க்கப்பட்ட notebook JSON ஆகியவற்றில் தோல்வியடைவது.
- `run_review` இயல்பாக உள்ளூர் Markdown மற்றும் பட இணைப்பு இலக்குகள் காணப்படாமல் இருந்தால் அவற்றை எச்சரிக்கையாக அறிவிக்கின்றது.

## உள்ளக அழைப்பு பாதை

API அதே கோர் அமல்படுத்தலுக்கு ஒப்படைக்கிறது, இது CLI-இல் பயன்படுத்தப்படுகிறது:

Translation:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. மார்க்டவுன், நோட்புக்குகள் மற்றும் படங்களுக்கு கவனம் செலுத்தப்பட்ட திட்ட மொழிபெயர்ப்பு மிக்ஸின்கள்.
8. Markdown, நோட்புக், உரை மற்றும் பட மொழிபெயர்ப்பாளர்கள் `co_op_translator.core` இன் கீழ்.

Review:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` க்குக் கீழேயுள்ள தீர்மானமான சோதனைகள்

பின்வரும் வகுப்புகள் பராமரிப்பாளர்களுக்கு பயனுள்ளதாக இருக்கும், ஆனால் அவை தொகுப்பு-அடிப்படையிலான நிலையான API ஆக வெளியிடப்படவில்லை.

| வகுப்பு | மொடியூல் | பொறுப்பு |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | திட்ட நிலை மொழிபெயர்ப்பு, அடைவு நிர்வாகம், மொழி-ஒவ்வொன்றுக்கான மெட்டாடேட்டா சீரமைப்பு மற்றும் Markdown, notebook மற்றும் image மொழிபெயர்ப்பாளர்களுக்கு делெகேஷன் ஆகியவற்றை ஒருங்கிணைக்கிறது. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, notebooks, images, stale கண்டறிதல் மற்றும் மொழிபெயர்ப்பு மெட்டாடேட்டா புதுப்பிப்புகளுக்கான அசிங்க்ரோனஸ் கோப்பு செயலாக்க பணிகளை நடாத்தும். |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown கோப்பு வாசிப்புகள், உள்ளடக்கம் மொழிபெயர்ப்பு, பாதை மறுஅறிவித்தல், மெட்டாடேட்டா, மறுப்பு குறிப்புகள் மற்றும் எழுதுதல்களை ஒருங்கிணைக்கிறது. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | நோட்புக் கோப்பு வாசிப்புகள், Markdown-cell மொழிபெயர்ப்பு, பாதை மறுஅறிவித்தல், மெட்டாடேட்டா, மறுப்பு குறிப்புகள் மற்றும் எழுதுதலை ஒருங்கிணைக்கிறது. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | மூலப் படங்களின் கண்டறிதல், படம் மொழிபெயர்ப்பு, வெளியீட்டு பாதைகள், மெட்டாடேட்டா மற்றும் எழுதுதலை ஒருங்கிணைக்கிறது. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | மொழிபெயர்க்கப்பட்ட Markdown ஜோடிகளை கண்டுபிடிக்கிறது, மொழிபெயர்ப்பு தரத்தை மதிப்பீடு செய்கிறது மற்றும் குறைந்த நம்பகத்தன்மை திருத்த வேலைப்பாடுகளுக்காக நம்பிக்கை மெட்டாடேட்டாவை வாசிக்கிறது. |
| `ReviewRunner` | `co_op_translator.review.runner` | மூல கோப்புகள், இலக்கு மொழிகள் மற்றும் அமைக்கப்பட்ட மொழிபெயர்ப்பு மூலங்களுக்கு இடையில் தீர்மானமான பரிசீலனை சோதனைகளை ஒருங்கிணைக்கிறது. |
| `ReviewTarget` | `co_op_translator.review.targets` | ஒரு மூல அடைவு மற்றும் அதற்கான பரிசீலிக்கப்பட்ட மொழிபெயர்ப்பு வெளியீட்டு கோப்புறையை விளக்குகிறது. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | மரபு alias மொழி கோப்புறைகளை கண்டறிந்து canonical BCP 47 கோப்புறை இடமாற்றத் திட்டங்களை தயார் செய்கிறது. |
| `Config` | `co_op_translator.config.base_config` | `.env` கோப்புகளை ஏற்றுகிறது மற்றும் தேவையான LLM மற்றும் விருப்பமான Vision வழங்குநர்கள் கட்டமைக்கப்பட்டுள்ளனவா எனச் சரிபார்க்கிறது. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI, அல்லது Anthropic ஐ தானாக கண்டறிகிறது, தேவையான சுற்றுச்சூழல் மாறிலிகளை சரிபார்க்கிறது, மற்றும் வழங்குநர் இணைப்பு சோதனைகளை இயக்குகிறது. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision கட்டமைப்பைக் கண்டறிந்து பட மொழிபெயர்ப்பிற்கான இணைப்பு சோதனைகளை இயக்குகிறது. |