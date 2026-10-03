# Python API

Стабилан јавни Python API се експортује из `co_op_translator.api`. Већина интеграција користи један од следећих токова рада:

| Сценарио | Користите ово када | Главни API-ји |
| --- | --- | --- |
| Превођење појединачних датотека или докумената | Ваша апликација чита изворни садржај, позива Co-op Translator за превођење и одлучује где да сачува резултат. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Припрема садржаја за превођење од стране host-агента | Ваш MCP host или модел апликације ће преводити делове, док Co-op Translator обавља делење на делове и реконструкцију. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Превођење целог репозиторијума | Желите да Python API ради као CLI и да обавља откривање, излазне путеве, метаподатке, чишћење и записивање. | `run_translation` |

Већина нижих модула унутар `core`, `config`, `review` и `utils` су детаљи имплементације које користе ове улазне тачке API-ја.

MCP клијенти користе исти јавни API преко [MCP Server](mcp.md). Користите ову страницу када позивате Python директно, а MCP водич када изложите Co-op Translator агенту или уређивачу. Ако бираете између CLI, Python API и MCP, почните са [Choose Your Workflow](workflows.md).

## Почетни ток API-ја

Почните овде ако позивате Co-op Translator из Python кода:

1. Конфигуришите LLM провајдера како је описано у [Configuration](configuration.md), осим ако само припремате Markdown или notebook делове за превођење од стране host-агента.
2. Одлучите да ли ваша апликација контролише I/O за фајлове.
3. Користите content API-је када ваша апликација чита и записује појединачне датотеке.
4. Користите `run_translation` када Co-op Translator треба да обради репозиторијум као CLI.
5. Користите `run_review` након превођења ако вам требају детерминистичке провере у аутоматизацији.

| Циљ | API за почетак |
| --- | --- |
| Преведите један Markdown низ или датотеку | `translate_markdown_content` |
| Преведите један notebook садржај | `translate_notebook_content` |
| Преведите једну слику | `translate_image_content` |
| Дозволите host агенту да преводи Markdown или notebook делове | `start_markdown_agent_translation` или `start_notebook_agent_translation` |
| Препишите преведене линкове након избора излазног пута | `rewrite_markdown_paths` или `rewrite_notebook_paths` |
| Преведите читав репозиторијум | `run_translation` |
| Прегледајте преведени излаз | `run_review` |

## Сценарио 1: Превођење појединачних датотека или докумената

Користите овај ток рада када већ имате датотеку, бафер у уређивачу, notebook садржај, MCP захтев или прилагођени улаз у цевоводу. Ваш код управља фајл I/O:

1. Прочитајте изворни садржај.
2. Позовите API за превођење садржаја.
3. По потреби позовите API за преписивање пута ако ће преведени садржај бити запамћен у фолдеру пројектног превођења.
4. Сачувајте или вратите резултат из ваше апликације.

API-ји за превођење садржаја не извршавају откривање пројекта, не записују метаподатке, не додају одрицања од одговорности и не преписују линкове аутоматски.

### Markdown датотека

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

Ако преведени Markdown неће бити унутар тренутне структуре пројекта Co-op Translator, прескочите `rewrite_markdown_paths` и сачувајте преведени низ директно.

### Notebook датотека

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

`translate_notebook_content` преводи Markdown ћелије и задржава не-Markdown ћелије. Преписивање путања се примењује само на Markdown ћелије.

### Слика

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

`translate_image_content` чита изворну слику и враћа render-овани `PIL.Image.Image`. Не записује метаподатке преведене слике.

## Сценарио 2: Превођење целог репозиторијума

Користите овај ток рада када желите да Python API ради као `translate` CLI. `run_translation` открива подржане фајлове, преводи изабране типове садржаја, преписује путеве, записује излазне фајлове, ажурира метаподатке и обавља одржавање превођења као што је чишћење.

`run_translation` је превасходна улазна тачка за оркестрацију пројекта. `translate_project` се извозе као алијас за компатибилност са истим понашањем.

Преведите Markdown датотеке у текућем репозиторијуму на корејски и јапански:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Преведите само notebook-ове из специфичног корена пројекта:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Прегледајте обим превођења без писања датотека:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Забележите структурисане догађаје напретка за интеграцију:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Сачувајте податке у вашој табели догађаја задатка или их стримујте у ваш кориснички интерфејс.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Догађаји користе верзионисани шему `co-op.translation.event.v1`. Интеграције би требало да
се ослањају на стабилна поља као што су `type` и `stage_key`, а не на кориснички видљив
текст конзоле или `stage_label`.

Преведите више корена садржаја у једном позиву:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Сачувајте преводе у експлицитне излазне групе:

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

Користите плейсхолдер по језику када сваки језик треба да садржи угнежђени поддиректоријум:

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

Ако ни једно од `markdown`, `notebook` или `images` није подешено, API преводи све подржане типове: Markdown, notebooks и images.

### Чување прихваћених људских измена помоћу провајдера стања превођења

По подразумеваној вредности, Co-op Translator задржава постојеће понашање на нивоу фајлова: када
изворни Markdown застарева, цео преведени фајл се поново генерише. Hosted
интеграције могу опционално проследити `TranslationStateProvider` да би сачувале људске
измене у изворним блоковима који се нису променили.

Провајдер обезбеђује последњи прихваћени пар извор/циљ и евидентира сваки нови
кандидат. Прихватање остаје одговорност интеграције — на пример,
након што се pull request за превод споји:

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

За Markdown датотеке са валидном прихваћеном базом, Co-op Translator поравнава
врхунске Markdown блокове. Неизмењени изворни блокови поново користе тренутне преведене
блокове, укључујући измене које су направили људи; измењени или додати изворни блокови се шаљу
на превод; избрисани изворни блокови се уклањају. Ако је поравнање нејасно,
циљна структура се променила, превод блока је неважећи или не постоји база,
Co-op Translator сигурно пада на постојећи пут потпуне фајл превођења.


меморију сегментног превођења. Тренутно се примењује на Markdown пројектно
превођење. Понашање за notebook и слике остаје непромењено. Прослеђивање `update=True`
и даље захтева пуну регенерацију.


`RuntimeError` након што се пројектни ток рада заврши уместо да пријави
успешан покрет са недостајућим излазом. Интеграције би ово требало да третиарају као неуспели
посао и задрже претходно прихваћено стање превода.


## Преглед преведеног садржаја

`run_review` извршава детерминистичке провере превођења без LLM или Vision акредитива.

!!! note "Beta"
    `run_review` је бета детерминистичан API за ревизију. Не позива провајдере модела нити уписује датотеке, али шеме провера и проблема могу еволуирати.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Након превода који обухвата само README, користите исти опсег за ревизију:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` ревидира само `README.md` под сваким конфигурисаним кореном извора,
укључујући прилагођене `groups` и директоријуме за излаз. Остали документи и угнеждени
README фајлови су искључени. Недостајући изворни README избацује `ValueError`; неуспешне
провере превода изазивају `RuntimeError`.

Ревидирајте само фајлове који су промењени у односу на базну референцу и испишите GitHub-стилски излаз:

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

## Примери API-ја за копирање и лепљење

Преведите Markdown садржај без уписа у фајлове:

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

Преведите и препишите Markdown линкове:

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

Преведите репозиторијум помоћу Pythona:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Преведите више корена:

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

Сачувајте термине из глосара:

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

## Јавне тачке уласка

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

## API-ји за превод садржаја

API-ји за превођење садржаја су намењени интеграцијама које већ имају садржај у меморији, као што су екстензија уређивача, MCP алат, процесор нотебука или прилагођени ток обраде.

| Функција | Улаз | Излаз | Рад са фајловима | Напомене |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Не | Асинхроно. Преводи само Markdown садржај. Не преписује линкове, не уписује метаподатке и не додаје дисклејмере. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Не | Асинхроно. Преводи Markdown ћелије и задржава не-Markdown ћелије. Не преписује линкове, не уписује метаподатке и не додаје дисклејмере. |
| `translate_image_content` | Путања до слике | `PIL.Image.Image` | Чита само изворну слику | Синхроно. Извлачи и преводи текст са слике, затим враћа рендеровану слику. Не чува метаподатке преведене слике. |

`translate_markdown_content` и `translate_notebook_content` прихватају опциони `source_path` кроз њихове опције. Путања се прослеђује као контекст преводиоцу; позиваоци и даље остају одговорни за било које специфично за пројекат преписивање путања након превода.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Исте опције се могу проследити као речници:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API-ји за превођење уз помоћ агента

API-ји уз помоћ агента не позивају конфигурисаног LLM провајдера из Co-op Translator-а. Они припремају Markdown или делове нотебука за хост агента да их преведе, а затим реконструишу коначни садржај из преведених делова.

| Функција | Намена |
| --- | --- |
| `start_markdown_agent_translation` | Враћа самосталан Markdown посао са деловима, промптима и стањем за реконструкцију. |
| `finish_markdown_agent_translation` | Реконструише Markdown из посла и делова преведених од стране хост-агента. |
| `start_notebook_agent_translation` | Враћа нотебук посао са деловима Markdown-ћелија за превођење од стране хост-агента. |
| `finish_notebook_agent_translation` | Реконструише notebook JSON уз очување ћелија са кодом, излаза и метаподатака. |

Овај радни ток је углавном намењен MCP хостовима. Ако вам треба продукционо превођење репозиторијума са Co-op Translator-ом који управља позивима провајдера, користите `translate_markdown_content`, `translate_notebook_content` или `run_translation`.

## API-ји за преписивање путања

API-ји за преписивање путања не изводе превод. Они ажурирају линкове и путање у frontmatter-у након што позиваоци знају изворну путању, преведену циљну путању и распоред пројекта.

| Функција | Опсег | Напомене |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown тело и frontmatter | Преписује Markdown линкове и подржана поља путања у frontmatter-у за преведени циљ. |
| `rewrite_notebook_paths` | Markdown ћелије у notebook JSON | Примењује преписивање Markdown путања на сваку Markdown ћелију и оставља не-Markdown ћелије непромењеним. |

Аргумент `policy` може бити речник са овим пољима:

| Поље | Обавезно | Намена |
| --- | --- | --- |
| `language_code` | Да | Код циљног језика, као што је `"ko"` или `"pt-BR"`. |
| `root_dir` | Не | Корен извора пројекта. Подразумевано `"."`. |
| `translations_dir` | Не | Директоријум за излаз текстуалног превода. Подразумевано `translations` под `root_dir`. |
| `translated_images_dir` | Не | Директоријум за излаз преведених слика. Подразумевано `translated_images` под `root_dir`. |
| `translation_types` | Не | Омогућени типови превођења. Подразумевано Markdown, нотебуци и слике. |
| `lang_subdir` | Не | Опциона поддиректорија у оквиру сваке фасцикле језика. |

## Параметри превођења пројекта

| Параметар | Тип | Подразумевано | Намена |
| --- | --- | --- | --- |
| `language_codes` | `str` | Обавезно | Циљни кодови језика одвојени размаком, као на пример `"ko ja fr"`, или `"all"`. Alias кодови се нормализују на канонске BCP 47 вредности. |
| `root_dir` | `str` | `"."` | Корен пројекта за један циљ превођења. Игнорише се када су `root_dirs` или `groups` обезбеђени. |
| `update` | `bool` | `False` | Обриши и поново креира постојеће преводе за изабране језике. |
| `images` | `bool` | `False` | Укључи превођење слика. Захтева конфигурацију Azure AI Vision. |
| `markdown` | `bool` | `False` | Укључи превођење Markdown-а. |
| `notebook` | `bool` | `False` | Укључи превођење Jupyter notebook-а. |
| `debug` | `bool` | `False` | Омогући debug логовање. |
| `save_logs` | `bool` | `False` | Сачувај лог фајлове нивоа DEBUG у коренском директоријуму `logs/`. |
| `yes` | `bool` | `True` | Аутоматски потврђује упите за програмску и CI употребу. |
| `add_disclaimer` | `bool` | `False` | Додаје одрицања одговорности о машинском преводу у преведени Markdown и бележнице. |
| `translations_dir` | `str \| None` | `None` | Прилагођени директоријум за излазне преводе текста. Релативне путање се решавају у односу на сваки корен. |
| `image_dir` | `str \| None` | `None` | Прилагођени директоријум за излаз преведених слика. Релативне путање се решавају у односу на сваки корен. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Више коренских директоријума који деле иста подешавања за излаз. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Експлицитни парови `(root_dir, translations_dir)`. Имају предност над `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL репозиторијума који се користи при приказу упутства табеле језика у README-у. |
| `glossaries` | `Iterable[str] \| None` | `None` | Појмови из глосара које треба сачувати током превођења. Дупликати и празни појмови се нормализују. |
| `dry_run` | `bool` | `False` | Процењује обим превођења и прегледа понашање миграције без уписивања фајлова. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Опциони адаптер за перзистенцију прихваћене базне верзије и кандидата за инкрементална ажурирања Markdown-а. Изостављање задржава постојеће понашање које обрађује целе фајлове. |

## Параметри прегледа

`run_review` намерно одражава сигнатуру `run_translation` где је то могуће тако да аутоматизација може да пребаци између радних токова превођења и прегледа уз минимално гранање.

| Параметар | Тип | Подразумевано | Намена |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Циљне фасцикле језика за преглед. Прихватају се низови раздвојени размаком и итерабли. `"all"` прегледа све откривене језике превода. |
| `root_dir` | `str` | `"."` | Корен пројекта за један циљ прегледа. Игнорише се када се доставе `root_dirs` или `groups`. |
| `markdown` | `bool` | `False` | Укључује Markdown и MDX изворне фајлове. |
| `notebook` | `bool` | `False` | Укључује Jupyter notebook изворне фајлове. |
| `images` | `bool` | `False` | Резервисано ради паритета са опцијама превођења. Референце веза ка сликама се проверавају из Markdown-а. |
| `translations_dir` | `str \| None` | `None` | Прилагођени директоријум за излазне преводе текста. Релативне путање се решавају у односу на сваки корен. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Више коренских директоријума који деле иста подешавања за излаз. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Експлицитни парови `(root_dir, translations_dir)`. Имају предност над `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Git референца која се користи да ограничи преглед на изменјене изворне фајлове. |
| `readme_only` | `bool` | `False` | Прегледава само `README.md` у оквиру сваког изворног корена. Недостајући изворни README изазива `ValueError`. |
| `output_format` | `str` | `"text"` | Формат излаза прегледа. Подржане вредности су `"text"` и `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Сматра упозорења као неуспехе поред грешака. |
| `debug` | `bool` | `False` | Омогућава дебаг логовање. |
| `save_logs` | `bool` | `False` | Сачува DEBUG-ниво лог фајлове у коренском директоријуму `logs/`. |

Ако ниједна од `markdown`, `notebook` или `images` није подешена, API прегледа Markdown, бележнице и референце веза ка сликама где је применљиво. Преглед не позива LLM провајдера и не захтева API кључеве.

## Захтеви за конфигурацију

API-ји за превод који се ослањају на провајдере захтевају конфигурацију провајдера пре превођења:

- Превођење Markdown-а и бележница захтева LLM провајдера. Конфигуришите Azure OpenAI, OpenAI или Anthropic.
- Превођење слика захтева Azure AI Vision поред LLM провајдера.
- `run_translation` изводи лагане провере повезаности пре него што превођење пројекта започне.
- API-ји помоћу агента `start_*_agent_translation` и `finish_*_agent_translation` не позивају Co-op Translator LLM провајдере. Домаћинска апликација или MCP агент преводи припремљене делове.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` и `run_review` су детерминистички и не захтевају акредитиве провајдера.

Потребне Azure OpenAI променљиве:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Потребне OpenAI променљиве:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Потребне Anthropic променљиве:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` и `ANTHROPIC_MAX_TOKENS` су опционалне. Microsoft Agent Framework је подразумевани клијент модела за све провајдере почевши од Co-op Translator 0.22.0. Semantic Kernel се и даље може привремено изабрати помоћу `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, али то емитује упозорење о депрекацији; погледајте [конфигурацију](configuration.md#model-client-backend) за план постепеног уклањања.

Потребне Azure AI Vision променљиве за превођење слика:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` је детерминистички и не захтева конфигурацију LLM-а или Azure AI Vision.

## Напомене о понашању

- API-ји за превод садржаја држе превођење одвојеним од преписивања путања пројекта. Позовите `rewrite_markdown_paths` или `rewrite_notebook_paths` експлицитно када преведени садржај треба да има пројектно-релативне линкове прилагођене за циљну локацију.
- API-ји за оркестрацију пројекта додају понашање око превођења садржаја, укључујући откривање фајлова, уписе, преписивање путања, метаподатке, чишћење и опционална одрицања.
- `run_translation` исписује сумарне информације о напретку и проценама преко истог Rich-подржаног извештача који користи CLI. Неинтерактивни излаз пада на обичан текст.
- `dry_run=True` израчунава процене користећи виртуелне ажурирања README-а, али не уписује README или фајлове превода.
- `groups` се обрађују секвенцијално. Једна агрегатна процена се исписује пре почетка рада.
- Када је изабрано превођење слика, недостатак Vision конфигурације изазива грешку пре почетка превођења.
- Постојеће алијас-базиране фасцикле језика се детектују и могу бити мигриране у канонске називе фасцикли језика као део покретања.
- `run_review` не успева у случају недостајућих преведених фајлова, недостајућих или застарелих метаподатака превода, неправилног Markdown frontmatter-а/кодних блокова и невалидног преведеног notebook JSON-а.
- `run_review` по подразумеваној вредности пријављује недостајуће локалне Markdown и циљеве веза ка сликама као упозорења.

## Унутрашњи позивни пут

API делегира истој основној имплементацији коју користи CLI:

Превођење:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` for in-memory translation.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` for explicit path post-processing.
3. `co_op_translator.api.translation.run_translation` for full project orchestration.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Миксини за пројектно фокусирано превођење за Markdown, бележнице и слике.
8. Преводиоци за Markdown, бележнице, текст и слике под `co_op_translator.core`.

Преглед:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Детерминистичке провере под `co_op_translator.review.checks`

Следеће класе су корисне за одржаваоце, али нису експортиране као стабилан API на ниво пакета.

| Класа | Модул | Одговорност |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Координише превођење на нивоу пројекта, управља директоријумима, нормализује метаподатке по језику и делегира превођење преводиоцима за Markdown, бележнице и слике. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Извршава асинхрони посао обраде фајлова за Markdown, бележнице, слике, детекцију застарелих и ажурирања метаподатака превода. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Оркестрира читање Markdown фајлова, превођење садржаја, преписивање путања, метаподатке, одрицања и уписе. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Оркестрира читање бележница, превођење Markdown ћелија, преписивање путања, метаподатке, одрицања и уписе. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Оркестрира откривање изворних слика, превођење слика, излазне путање, метаподатке и уписе. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Проналази парове преведеног Markdown-а, процењује квалитет превода и чита метаподатке о поверењу за радне токове поправке ниског поверења. |
| `ReviewRunner` | `co_op_translator.review.runner` | Координише детерминистичке провере прегледа преко изворних фајлова, циљних језика и конфигурисаних корена превода. |
| `ReviewTarget` | `co_op_translator.review.targets` | Описује изворни корен и директоријум излаза превода који се прегледа за тај корен. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Детектује наслеђене алијас фасцикле језика и припрема планове миграције у канонске BCP 47 фасцикле. |
| `Config` | `co_op_translator.config.base_config` | Учитава `.env` фајлове и проверава да ли су потребни LLM и опциони Vision провајдери конфигурисани. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Аутоматски детектује Azure OpenAI, OpenAI или Anthropic, врши валидацију потребних променљивих окружења и покреће провере повезаности провајдера. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Детектује конфигурацију Azure AI Vision-а и покреће провере повезаности за превођење слика. |