# API ya Python

API ya umma thabiti ya Python imetolewa kutoka `co_op_translator.api`. Mwingiliano wengi hutumia mojawapo ya mtiririko huu:

| Senario | Tumia hili wakati | API Kuu |
| --- | --- | --- |
| Tafsiri faili au nyaraka binafsi | Programu yako inasoma maudhui ya chanzo, inaita Co-op Translator kwa ajili ya tafsiri, na inaamua wapi kuhifadhi matokeo. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Tayarisha maudhui kwa tafsiri ya wakala mwenyeji | Mwenyeji wako wa MCP au modeli ya programu itatafsiri vipande, wakati Co-op Translator inashughulikia kugawa vipande na ujenzi upya. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Tafsiri hazina yote | Unataka API ya Python iwe kama CLI na kushughulikia ugunduzi, njia za pato, metadata, usafi, na uandishi. | `run_translation` |

Moduli nyingi za ngazi ya chini chini ya `core`, `config`, `review`, na `utils` ni maelezo ya utekelezaji yanayotumiwa na pointi hizi za kuingia za API.

Wateja wa MCP hutumia API ya umma sawa kupitia [MCP Server](mcp.md). Tumia ukurasa huu unapoita Python moja kwa moja, na mwongozo wa MCP unapokuwa unamtambulisha Co-op Translator kwa wakala au mhariri. Ikiwa unaamua kati ya CLI, API ya Python, na MCP, anza na [Chagua Mtiririko Wako](workflows.md).

## Mtiririko wa API kwa Mara ya Kwanza

Anza hapa ikiwa unaita Co-op Translator kutoka kwa msimbo wa Python:

1. Sanidi mtoa huduma wa LLM kama ilivyoelezwa katika [Configuration](configuration.md), isipokuwa tu unapokuwa unatayarisha vipande vya Markdown au daftari kwa tafsiri ya wakala mwenyeji.
2. Amua kama programu yako itasimamia I/O ya faili.
3. Tumia API za maudhui wakati programu yako inasoma na kuandika faili binafsi.
4. Tumia `run_translation` wakati Co-op Translator inapaswa kushughulikia hazina kama CLI.
5. Tumia `run_review` baada ya tafsiri ikiwa unahitaji ukaguzi thabiti kwa otomatiki.

| Lengo | API ya kuanzia nayo |
| --- | --- |
| Tafsiri kamba au faili moja ya Markdown | `translate_markdown_content` |
| Tafsiri maudhui ya daftari moja | `translate_notebook_content` |
| Tafsiri picha moja | `translate_image_content` |
| Wawezeshe wakala mwenyeji kutafsiri vipande vya Markdown au daftari | `start_markdown_agent_translation` au `start_notebook_agent_translation` |
| Andika upya viungo vilivyotafsiriwa baada ya kuchagua njia ya pato | `rewrite_markdown_paths` au `rewrite_notebook_paths` |
| Tafsiri hazina yote | `run_translation` |
| Kagua matokeo yaliyotafsiriwa | `run_review` |

## Senario 1: Tafsiri Faili au Nyaraka Binafsi

Tumia mtiririko huu wakati tayari una faili, buffer ya mhariri, maudhui ya daftari, ombi la MCP, au pembejeo za pipeline maalum. Msimbo wako unasimamia I/O ya faili:

1. Soma maudhui ya chanzo.
2. Ita API ya tafsiri ya maudhui.
3. Hiari: ita API ya uandishi upya wa njia ikiwa maudhui yaliyotafsiriwa yataandikwa ndani ya folda ya tafsiri ya mradi.
4. Hifadhi au rudisha matokeo kutoka kwa programu yako.

API za tafsiri za maudhui hazifanyi ugunduzi wa mradi, hazandiki metadata, haziongezi taarifa za kutengwa, na hazibadilisha viungo kiotomatiki.

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

Ikiwa Markdown iliyotafsiriwa haitakuwa ndani ya muundo wa mradi wa Co-op Translator, ruka `rewrite_markdown_paths` na hifadhi kamba iliyotafsiriwa moja kwa moja.

### Faili la Daftari

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

`translate_notebook_content` inatafsiri seli za Markdown na inahifadhi seli zisizo za Markdown. Uandishi upya wa njia unatekelezwa kwa seli za Markdown pekee.

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

`translate_image_content` inasoma picha ya chanzo na inarudisha `PIL.Image.Image` iliyotengenezwa. Haandiki metadata ya picha iliyotafsiriwa.

## Senario 2: Tafsiri Hazina Yote

Tumia mtiririko huu unapotaka API ya Python ifanye kazi kama CLI `translate`. `run_translation` hugundua faili zinazoungwa mkono, inatafsiri aina zilizochaguliwa za maudhui, inaandika upya njia, inaandika faili za pato, inaupdate metadata, na inafanya kazi za matengenezo ya tafsiri kama usafi.

`run_translation` ni njia iliyopendekezwa ya kuanzisha uratibu wa mradi. `translate_project` imetolewa kama jina la urafiki lenye tabia ile ile.

Tafsiri faili za Markdown katika hazina iliyopo kuwa Kikorea na Kijapani:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Tafsiri vitabu vya daftari pekee kutoka mzizi maalum wa mradi:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Angalia kiwango cha tafsiri bila kuandika faili:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Weka kumbukumbu za matukio ya maendeleo yaliyo muundo kwa ajili ya muingiliano:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Hifadhi yaliyomo (payload) katika jedwali lako la matukio za kazi au uyatume kwa mtiririko kwenye kiolesura chako cha mtumiaji.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Matukio yanatumia skema yenye toleo `co-op.translation.event.v1`. Mwingiliano yanapaswa
kutegemea nyanja thabiti kama `type` na `stage_key`, si kwenye maandishi yanayoonekana kwa watu
kwenye konsole au `stage_label`.

Tafsiri mzizi nyingi za maudhui kwa wito mmoja:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Weka tafsiri katika makundi ya pato yaliyoelezeka:

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

Tumia kibadilishi cha kila lugha wakati kila lugha inapaswa kuwa na saraka ndogo ndani:

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

Ikiwa hakuna kati ya `markdown`, `notebook`, au `images` zimewekwa, API inatafsiri aina zote zinazoungwa mkono: Markdown, daftari, na picha.

### Hifadhi mabadiliko yaliyoruhusiwa na binadamu kwa kutumia mtoa hali ya tafsiri

Kwa chaguo-msingi, Co-op Translator huendelea na tabia yake ya sasa kwa ngazi ya faili: wakati
chanzo cha Markdown kinapokuwa kimepitwa na wakati, faili yote iliyotafsiriwa inatengenezwa upya. Ushirikiano unaoendeshwa na mwenyeji
unaweza kwa hiari kupitisha `TranslationStateProvider` ili kuhifadhi mabadiliko ya wanadamu
katika vibloku vya chanzo ambavyo havijabadilika.

Mtoa huduma hutoa jozi ya mwisho ya chanzo/lengo iliyokubaliwa na kurekodi kila
mgombea. Kukubaliwa kunabaki kuwa jukumu la muingiliano—kwa mfano,
baada ya ombi la kuvuta (pull request) la tafsiri kuchanganywa:

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

Kwa faili za Markdown zenye msingi uliokubaliwa halali, Co-op Translator huoanisha
vibloku vya juu vya Markdown. Vibloku vya chanzo ambavyo havijabadilika vinatumia tena vibloku vilivyotafsiriwa vya sasa,
vikiwemo marekebisho yaliyofanywa na watu; vibloku vya chanzo vilivyobadilika au vilivyongezwa vinatumwa
kwa tafsiri; vibloku vya chanzo vilivyofutwa vimoondolewa. Ikiwa ulinganifu hauko wazi,
muundo wa lengo umebadilika, tafsiri ya kibao ni batili, au hakuna msingi
upatikane, Co-op Translator kwa usalama hurudi kwenye
njia ya sasa ya tafsiri ya faili nzima.

API hii inahifadhi hali ya tafsiri ya hati, si kumbukumbu ya sentensi au
'translation memory' ya segmenti. Hivi sasa inatumika kwa mradi wa Markdown
tafsiri. Tabia za daftari na picha hazijabadilika. Kupitisha `update=True`
bado huita utafsiri kwa njia ya uzalishaji kamili.

Ikiwa faili moja au zaidi haiwezi kutafsiriwa, `run_translation` inaleta
`RuntimeError` baada ya mtiririko wa mradi kumalizika badala ya kuripoti
kazi iliyofanikiwa lakini pamoja na pato lilikosekana. Mwingiliano yanapaswa kuitendea kama kazi iliyoshindwa
na kuhifadhi hali ya tafsiri iliyokubaliwa ya awali.

## Kagua Matokeo Yaliyotafsiriwa

`run_review` inafanya ukaguzi thabiti wa tafsiri bila vigezo vya LLM au Vision.

!!! note "Beta"
    `run_review` ni API ya tathmini ya beta yenye utabiri. Haiitumi watoa modeli wala kuandika faili, lakini ukaguzi na skimu za masuala yanaweza kubadilika.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Baada ya tafsiri ya README pekee, tumia wigo huo huo kwa ajili ya ukaguzi:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` inakagua tu `README.md` chini ya kila mzizi wa chanzo uliowekwa,
ikijumuisha `groups` maalum na saraka za pato. Nyaraka nyingine na README zilizomo ndani
zimetengwa. Kukosa README ya chanzo kunachochea `ValueError`; ukaguzi wa tafsiri ulioshindikana
unaleta `RuntimeError`.

Kagua faili zilizo badilika tu dhidi ya rejea msingi na chapisha pato lenye mtindo wa GitHub:

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

## Mifano ya API za Nakili na Bandika

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

Tafsiri hazina kutoka Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Tafsiri mzizi nyingi:

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

Hifadhi maneno ya orodha ya istilahi:

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

## Pointi za Umma za Kuingia

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

## API za Tafsiri za Maudhui

API za tafsiri za maudhui zinalengwa kwa muingiliano ambao tayari wana maudhui ndani ya kumbukumbu, kama vile kipanuzi cha mhariri, zana ya MCP, processor ya daftari, au pipeline maalum.

| Kazi | Ingizo | Matokeo | I/O ya Faili | Maelezo |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Hapana | Asinkroni. Inatafsiri maudhui ya Markdown tu. Haiandiki viungo upya, haiandiki metadata, wala haiongezi taarifa za kutengwa. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Hapana | Asinkroni. Inatafsiri seli za Markdown na inahifadhi seli zisizo za Markdown. Haiandiki viungo upya, haiandiki metadata, wala haiongezi taarifa za kutengwa. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Inasoma picha ya chanzo tu | Sinkroni. Inatoa na kutafsiri maandishi ya picha, kisha inarudisha picha iliyochorwa. Haihifadhi metadata ya picha iliyotafsiriwa. |

`translate_markdown_content` na `translate_notebook_content` zinakubali chaguo la `source_path` kupitia chaguzi zao. Njia hiyo hupitishwa kama muktadha kwa mtafsiri; wito wanabaki kuwajibika kwa uandishi upya wa njia maalum za mradi baada ya tafsiri.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Chaguzi zile zile zinaweza kupitishwa kama kamusi (dictionary):

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API za Tafsiri Zilizosaidiwa na Wakala

API zilizosaidiwa na wakala hazifanyi wito kwa mtoa huduma wa LLM uliowekwa kutoka Co-op Translator. Zinatangaza vipande vya Markdown au daftari kwa wakala mwenyeji kutafsiri, kisha hujenga tena maudhui ya mwisho kutoka kwa vipande vilivyotafsiriwa.

| Kazi | Kusudi |
| --- | --- |
| `start_markdown_agent_translation` | Rudisha kazi ya Markdown yenye kujitegemea na vipande, mipangilio ya maelekezo, na hali ya ujenzi upya. |
| `finish_markdown_agent_translation` | Jenga tena Markdown kutoka kwa kazi na vipande vilivyotafsiriwa na wakala mwenyeji. |
| `start_notebook_agent_translation` | Rudisha kazi ya daftari yenye vipande vya seli za Markdown kwa tafsiri ya wakala mwenyeji. |
| `finish_notebook_agent_translation` | Jenga tena JSON ya daftari huku ukihifadhi seli za msimbo, matokeo, na metadata. |

Mtiririko huu umeundwa hasa kwa wenyeji wa MCP. Ikiwa unahitaji tafsiri ya hazina kwa uzalishaji ambapo Co-op Translator inasimamia wito kwa watoa huduma, tumia `translate_markdown_content`, `translate_notebook_content`, au `run_translation`.

## API za Uandishi Upya wa Njia

API za uandishi upya wa njia hazitekelezi tafsiri. Zinaboresha viungo na njia za frontmatter baada ya wito kujua njia ya chanzo, njia ya lengo iliyotafsiriwa, na mpangilio wa mradi.

| Kazi | Wigo | Maelezo |
| --- | --- | --- |
| `rewrite_markdown_paths` | Mwili wa Markdown na frontmatter | Inaandika upya viungo vya Markdown na mashamba ya frontmatter yanayounga mkono njia kwa lengo lililotafsiriwa. |
| `rewrite_notebook_paths` | Seli za Markdown katika JSON ya daftari | Inatekeleza uandishi upya wa njia za Markdown kwa kila seli ya Markdown na inaacha seli zisizo za Markdown bila kubadilika. |

Argumeni ya `policy` inaweza kuwa kamusi yenye mashamba haya:

| Sehemu | Inahitajika | Kusudi |
| --- | --- | --- |
| `language_code` | Ndiyo | Msimbo wa lugha ya lengo, kama `"ko"` au `"pt-BR"`. |
| `root_dir` | Hapana | Mzizi wa mradi wa chanzo. Default ni `"."`. |
| `translations_dir` | Hapana | Saraka ya pato ya tafsiri za maandishi. Default ni `translations` chini ya `root_dir`. |
| `translated_images_dir` | Hapana | Saraka ya pato ya picha zilizotafsiriwa. Default ni `translated_images` chini ya `root_dir`. |
| `translation_types` | Hapana | Aina za tafsiri zilizowezeshwa. Default ni Markdown, daftari, na picha. |
| `lang_subdir` | Hapana | Saraka ndogo ya hiari chini ya kila folda ya lugha. |

## Vigezo vya Tafsiri ya Mradi

| Vigezo | Aina | Chaguo-msingi | Kusudi |
| --- | --- | --- | --- |
| `language_codes` | `str` | Inahitajika | Misimbo ya lugha za lengo zilizotenganishwa kwa nafasi, kama `"ko ja fr"`, au `"all"`. Msimbo mbadala unalinganishwa na thamani za kimsingi za BCP 47. |
| `root_dir` | `str` | `"."` | Mzizi wa mradi kwa lengo moja la tafsiri. Haizingatiwi wakati `root_dirs` au `groups` zimetolewa. |
| `update` | `bool` | `False` | Futa na tengeneza upya tafsiri zilizopo kwa lugha zilizochaguliwa. |
| `images` | `bool` | `False` | Jumuisha tafsiri ya picha. Inahitaji usanidi wa Azure AI Vision. |
| `markdown` | `bool` | `False` | Jumuisha tafsiri ya Markdown. |
| `notebook` | `bool` | `False` | Jumuisha tafsiri ya daftari la Jupyter. |
| `debug` | `bool` | `False` | Washa uandishi wa kumbukumbu wa utatuzi (debug). |
| `save_logs` | `bool` | `False` | Hifadhi faili za kumbukumbu za ngazi ya DEBUG chini ya saraka ya mzizi `logs/`. |
| `yes` | `bool` | `True` | Thibitisha moja kwa moja viito kwa matumizi ya programu na CI. |
| `add_disclaimer` | `bool` | `False` | Ongeza viambatanisho vya tafsiri ya mashine kwenye Markdown na daftari zilizotafsiriwa. |
| `translations_dir` | `str \| None` | `None` | Saraka maalum ya pato la tafsiri ya maandishi. Njia za jamaa zinatatuliwa kwa kila mzizi. |
| `image_dir` | `str \| None` | `None` | Saraka maalum ya pato la picha zilizotafsiriwa. Njia za jamaa zinatatuliwa kwa kila mzizi. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mizizi mingi inayoshiriki mipangilio ileile ya pato. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pande zilizo wazi `(root_dir, translations_dir)`. Zinapata kipaumbele juu ya `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL ya hazina inayotumika wakati wa kuonyesha mwongozo wa jedwali la lugha kwenye README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Maneno ya orodha ya istilahi ya kuhifadhi wakati wa tafsiri. Nakala na maneno tupu zinapangwa kuwa sawa. |
| `dry_run` | `bool` | `False` | Kadiria kiasi cha tafsiri na hakiki tabia ya uhamishaji bila kuandika faili. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Kiambatisho cha hiari cha kuhifadhi msingi uliokubaliwa na wagombea kwa masasisho ya hatua kwa hatua ya Markdown. Kukosa kwake kunahifadhi tabia ya sasa ya faili kamili. |

## Vigezo vya Ukaguzi

`run_review` kwa makusudi inaiga saini ya `run_translation` inapowezekana ili otomatiki iweze kubadilisha kati ya taratibu za tafsiri na ukaguzi kwa mabadiliko madogo.

| Kigezo | Aina | Chaguo-msingi | Kusudi |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Folda za lugha lengwa za kukagua. Sehemu zilizoachwa kwa nafasi na orodha zinakubaliwa. `"all"` inakagua kila lugha ya tafsiri iliyogunduliwa. |
| `root_dir` | `str` | `"."` | Mzizi wa mradi kwa lengo moja la ukaguzi. Hupuuzwa wakati `root_dirs` au `groups` zitatolewa. |
| `markdown` | `bool` | `False` | Jumuisha faili za chanzo za Markdown na MDX. |
| `notebook` | `bool` | `False` | Jumuisha faili za chanzo za daftari za Jupyter. |
| `images` | `bool` | `False` | Imehifadhiwa ili kufanana na chaguzi za tafsiri. Marejeleo ya viunga vya picha yanakaguliwa kutoka Markdown. |
| `translations_dir` | `str \| None` | `None` | Saraka maalum ya pato la tafsiri ya maandishi. Njia za jamaa zinatatuliwa kwa kila mzizi. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Mizizi mingi inayoshiriki mipangilio ileile ya pato. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pande zilizo wazi `(root_dir, translations_dir)`. Zinapata kipaumbele juu ya `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Rejeo la Git linalotumika kuzuia ukaguzi kwa faili za chanzo zilizobadilishwa. |
| `readme_only` | `bool` | `False` | Kagua tu `README.md` chini ya kila mzizi wa chanzo. Kukosa README wa chanzo kunaleta `ValueError`. |
| `output_format` | `str` | `"text"` | Muundo wa pato la ukaguzi. Maadili yanayounga mkono ni `"text"` na `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Chukulia onyo kama kushindwa pamoja na makosa. |
| `debug` | `bool` | `False` | Washa uandishi wa kumbukumbu za debug. |
| `save_logs` | `bool` | `False` | Hifadhi faili za kumbukumbu za kiwango cha DEBUG chini ya saraka ya mzizi `logs/`. |

Iwapo hakuna kati ya `markdown`, `notebook`, au `images` zilizowekwa, API inakagua Markdown, daftari, na marejeleo ya viunga vya picha pale inapotumika. Ukaguzi hauitami mtoa huduma wa LLM na hauhitaji vitambulisho vya API.

## Mahitaji ya Usanidi

API za tafsiri zinazotegemea mtoa huduma zinahitaji usanidi wa mtoa huduma kabla ya kutafsiri:

- Tafsiri ya Markdown na daftari inahitaji mtoa huduma wa LLM. Sanidi Azure OpenAI, OpenAI, au Anthropic.
- Tafsiri ya picha inahitaji Azure AI Vision pamoja na mtoa huduma wa LLM.
- `run_translation` inafanya ukaguzi mdogo wa muunganisho kabla ya kuanza tafsiri ya mradi.
- API zinazosaidiwa na wakala `start_*_agent_translation` na `finish_*_agent_translation` hazipigi simu kwa watoa LLM wa Co-op Translator. Programu mwenyeji au wakala wa MCP ndiye anatafsiri vipande vilivyotayarishwa.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, na `run_review` ni zisizobadilika na hazihitaji nyaraka za uthibitisho za mtoa huduma.

Mazingira yanayohitajika kwa Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Mazingira yanayohitajika kwa OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Mazingira yanayohitajika kwa Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` na `ANTHROPIC_MAX_TOKENS` ni za hiari. Microsoft Agent Framework ndio mteja wa modeli chaguo-msingi kwa watoa huduma wote kuanzia Co-op Translator 0.22.0. Semantic Kernel bado inaweza kuchaguliwa kwa muda kwa kutumia `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, lakini kufanya hivyo hutoa onyo la kutotumika tena; ona [usanidi](configuration.md#model-client-backend) kwa mpango wa kuondoa kwa hatua.

Mazingira yanayohitajika ya Azure AI Vision kwa tafsiri ya picha:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` ni zisizobadilika na haihitaji usanidi wa LLM au Azure AI Vision.

## Vidokezo vya Tabia

- API za tafsiri ya yaliyomo zinahifadhi tafsiri tofauti na kuandika upya njia za mradi. Piga simu `rewrite_markdown_paths` au `rewrite_notebook_paths` waziwazi wakati yaliyotafsiriwa yanahitaji marekebisho ya viungo vinavyohusiana na mradi kwa eneo lengwa.
- API za upangaji wa mradi huongeza tabia za mradi kuzunguka tafsiri ya yaliyomo, ikijumuisha ugunduzi wa faili, uandishi, kuandika upya njia, metadata, usafishaji, na viambatanisho vya hiari.
- `run_translation` inachapisha muendelezo na muhtasari wa makadirio kupitia mtoaji taarifa mmoja unaotegemea Rich unaotumika na CLI. Pato lisilo na mwingiliano linarudi kwenye maandishi ya kawaida.
- `dry_run=True` inahesabu makadirio kwa kutumia masasisho ya README ya kidigitali, lakini haiandiki README wala faili za tafsiri.
- `groups` zinaandaliwa kwa mfululizo. Makadirio ya jumla yanachapishwa kabla ya kazi kuanza.
- Wakati tafsiri ya picha imechaguliwa, kukosekana kwa usanidi wa Vision husababisha kosa kabla ya kuanza tafsiri.
- Saraka za lugha zilizopo zinazotegemea majina ya kibadilifu (alias) zinatambuliwa na zinaweza kuhamishwa kwenda majina ya saraka ya lugha ya kikanoni kama sehemu ya utekelezaji.
- `run_review` inashindwa kwa faili za tafsiri zilizokosekana, metadata ya tafsiri iliyokosekana au iliyokauka, frontmatter/funga za msimbo za Markdown zisizo sahihi, na JSON ya daftari iliyotafsiriwa isiyo halali.
- `run_review` huripoti malengo ya Markdown ya ndani na viungo vya picha vilivyokosekana kama onyo kwa chaguo-msingi.

## Njia ya Kuitwa Ndani

API inamkabidhi utekelezaji uleule wa msingi unaotumika na CLI:

Tafsiri:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` kwa tafsiri inayofanyika ndani ya kumbukumbu.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` kwa uchakataji wa wazi wa njia baada ya tafsiri.
3. `co_op_translator.api.translation.run_translation` kwa upangaji kamili wa mradi.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mchanganyiko maalum wa tafsiri ya mradi kwa Markdown, daftari, na picha.
8. Watafsiri wa Markdown, daftari, maandishi, na picha chini ya `co_op_translator.core`.

Ukaguzi:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Deterministic checks under `co_op_translator.review.checks`

Madarasa yafuatayo ni muhimu kwa watunzaji, lakini hayatoiwi kama API thabiti ya ngazi ya kifurushi.

| Darasa | Moduli | Majukumu |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Inaongoza tafsiri ya ngazi ya mradi, usimamizi wa saraka, ulinganifu wa metadata kwa kila lugha, na kugawa kazi kwa watafsiri wa Markdown, daftari, na picha. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Inatekeleza kazi za usindikaji wa faili kwa njia ya async kwa Markdown, daftari, picha, ugundaji wa yaliyokauka, na masasisho ya metadata ya tafsiri. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Inaongoza kusomwa kwa faili za Markdown, tafsiri ya yaliyomo, kuandika upya njia, metadata, viambatanisho, na kuandika faili. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Inaongoza kusomwa kwa faili za daftari, tafsiri ya seli za Markdown, kuandika upya njia, metadata, viambatanisho, na kuandika faili. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Inaongoza ugundaji wa picha za chanzo, tafsiri ya picha, njia za pato, metadata, na kuandika faili. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Inatafuta jozi za Markdown zilizotafsiriwa, inathibitisha ubora wa tafsiri, na inasoma metadata ya kujiamini kwa taratibu za ukarabati za matokeo yenye uaminifu mdogo. |
| `ReviewRunner` | `co_op_translator.review.runner` | Inaratibu ukaguzi unaotegemewa kwa faili za chanzo, lugha lengwa, na mizizi ya tafsiri iliyosanidiwa. |
| `ReviewTarget` | `co_op_translator.review.targets` | Inaeleza mzizi wa chanzo na saraka ya pato la tafsiri inayokaguliwa kwa mzizi huo. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Inatambua saraka za lugha za jadi zilizo na majina ya kibadilifu na kuandaa mipango ya uhamishaji kwenda majina ya saraka ya lugha ya BCP 47 ya kikanoni. |
| `Config` | `co_op_translator.config.base_config` | Inapakia faili za `.env` na inakagua kama watoa LLM waliotakiwa na wale wa Vision wa hiari wamesanidiwa. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Inatambua kwa kiotomatiki Azure OpenAI, OpenAI, au Anthropic, inathibitisha vigezo vinavyohitajika vya mazingira, na inafanya ukaguzi wa muunganisho wa mtoa huduma. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Inagundua usanidi wa Azure AI Vision na inafanya ukaguzi wa muunganisho kwa tafsiri ya picha. |