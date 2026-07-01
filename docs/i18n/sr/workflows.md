# Изаберите свој радни ток

Co-op Translator се може користити на три начина: CLI, Python API и MCP сервер. Делe исте могућности превода, али сваки од њих одговара другом радном току.

Користите ову страницу када одлучујете одакле да почнете.

## Брза одлука

| Ако желите да... | Користите | Почните овде |
| --- | --- | --- |
| Преведете или прегледате репозиторијум из терминала | CLI | [CLI референца](cli.md) |
| Додате превод у Python скрипт, сервис, notebook или CI посао | Python API | [Python API](api.md) |
| Дозволите агенту, уређивачу или клијенту компатибилном са MCP да преведе садржај за вас | MCP сервер | [MCP сервер](mcp.md) |
| Преведете један Markdown документ, нотебук или слику коју ваша апликација већ учитала | Python API или MCP сервер | [Python API](api.md) или [MCP сервер](mcp.md) |
| Преведете цео репозиторијум са стандардним излазним фасциклама и метаподацима | CLI или `run_translation` | [CLI референца](cli.md) или [Python API](api.md) |

## Користите CLI када

Изаберите CLI када особа или CI посао покреће превођење репозиторијума из командне линије.

CLI је најдиректнији пут када желите да Co-op Translator открије датотеке пројекта, креира преведене излазне податке, сачува распоред пројекта, ажурира метаподатке и покрене наредбе за преглед.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Погодно за:

- Преводите репозиторијум из вашег терминала.
- Желите понављачку команду за CI или токове рада за издавање.
- Желите уграђено откривање пројекта, излазне путање, метаподатке, чишћење и преглед.
- Пон preferирате командни интерфејс уместо писања Python кода.

## Користите Python API када

Изаберите Python API када ваш код треба да контролише радни ток.

API је користан за апликације, аутоматизационе скрипте, notebooks, сервисе и прилагођене цевоводе. Овом вам омогућава да позовете ниско-нивне API-је за превођење садржаја за појединачне датотеке, или да покренете исту оркестрацију на нивоу репозиторијума коју користи CLI.

Преведите један Markdown документ и одлучите где ћете га сачувати:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


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
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Покрените превођење репозиторијума из Pythona:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Погодно за:

- Ваша апликација већ чита датотеке, бафере, нотебуке или бајтове слике.
- Потребна вам је прилагођена валидација, складиштење, евиденција, поновни покушаји или токови одобравања.
- Желите да преведете један документ, нотебук или слику без обраде целог репозиторијума.
- Желите превођење репозиторијума, али из Python аутоматизације уместо наредбе у шелу.

## Користите MCP сервер када

Изаберите MCP сервер када агент, уређивач или клијент компатибилан са MCP треба да позове алате Co-op Translator-а.

У нормалном локалном подешавању, корисник не одржава сервер ручно. MCP клијент покреће `co-op-translator-mcp` преко `stdio` када му затребају алати.

Примери захтева које би агент могао обрадити:

- "Преведи овај Markdown фајл на корејски и задржи исправне линкове."
- "Преведи овај Markdown фајл на корејски уз MCP радни ток помоћу агента, користећи ваш модел за преведене делове."
- "Преведи овај нотебук на корејски, сачувај ћелије кода и користи Co-op Translator MCP да реконструише нотебук."
- "Преведи текст на овој слици на јапански и сачува резултат."
- "Изврши пробни превод репозиторијума на шпански и реци ми шта би се променило."
- "Проверите да ли је излаз корејског превода ажуран."

За Markdown и нотебуке, MCP може да ради у два режима:

| Режим | Користите када | Главни алати |
| --- | --- | --- |
| Агент-помогнут | MCP домаћин агент треба да преведе делове користећи свој модел, без Co-op Translator акредитива провајдера LLM. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Подржано од провајдера | Co-op Translator треба директно да позове Azure OpenAI или OpenAI. | `translate_markdown_content`, `translate_notebook_content` |

Облик позива алата за MCP provider-backed Markdown:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

Облик позива алата за MCP слике:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

Превођење репозиторијума преко MCP је подразумевано у пробном режиму:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Погодно за:

- Желите природнојезичке токове рада за превођење унутар агента или уређивача.
- Желите превођење Markdown-а или нотебука где домаћин агентски модел преводи припремљене делове.
- Желите да агент преведе одабрани садржај уместо целог репозиторијума.
- Желите корак одобрења пре писања по целом репозиторијуму.
- Желите један интерфејс који излаже алате за Markdown, нотебук, слике, преглед и преписивање путања.

## Како се међусобно уклапају

CLI је најбољи подразумевани избор за људе који преводе репозиторијуме. Python API је најбољи када ваш код управља радним током. MCP сервер је најбољи када агент или уређивач управља радним током.

Сва три пута користе исти јавни Co-op Translator API, тако да можете почети са CLI-јем, аутоматизовати касније помоћу Pythona и изложити исте могућности MCP клијентима када затребају радни токови покретани агентима.