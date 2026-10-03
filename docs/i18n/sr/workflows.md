# Изаберите свој радни ток

Co-op Translator се може користити на три начина: CLI, Python API и MCP сервер. Сви деле исте могућности превођења, али сваки од њих одговара другачијем радном току.

Користите ову страницу када одлучујете где да почнете.

**Ако ручно уређујете преводе:** подразумевани CLI и Actions радни токови поново преводе измењене изворне датотеке у целини, тако да ваш избор речи у тим датотекама може бити преписан. Прегледајте diff пре него што прихватите ажурирање. За чување прилагођених измена на нивоу Markdown блокова користите опциони [провајдер стања превођења Python API-ја](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Брза одлука

| Ако желите... | Користите | Почните овде |
| --- | --- | --- |
| Превести или прегледати репозиторијум из терминала | CLI | [CLI референца](cli.md) |
| Додати превод у Python скрипт, сервис, ноутбук или CI задатак | Python API | [Python API](api.md) |
| Пустите агента, уређивач или MCP-компатибилан клијент да преведе садржај за вас | MCP Server | [MCP Server](mcp.md) |
| Превести један Markdown документ, ноутбук или слику коју је ваша апликација већ учитала | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Превести цео репозиторијум са стандардним фолдерима за излаз и метаподацима | CLI or `run_translation` | [CLI референца](cli.md) or [Python API](api.md) |

## Користите CLI када

Изаберите CLI када особа или CI задатак покреће превођење репозиторијума из shell-а.

CLI је најдиректнији пут када желите да Co-op Translator открије проектне датотеке, креира преведене излазне датотеке, сачува распоред пројекта, ажурира метаподатке и покрене команде за преглед.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Овај пример преводи Markdown и ноутбуке. Додајте `-img` само након конфигурисања [Azure AI Vision](configuration.md#azure-ai-vision). За први покрет само за Markdown, следите [Ваш први превод](first-translation.md).

Погодно за:

- Преводите репозиторијум из вашег терминала.
- Желите поновљиву команду за CI или релизне радне токове.
- Желите уграђено откривање пројекта, излазне путеве, метаподатке, чишћење и преглед.
- Предпочитате командни интерфејс уместо писања Python кода.

## Користите Python API када

Изаберите Python API када ваш код треба да контролише радни ток.

API је користан за апликације, аутоматизационе скрипте, ноутбуке, сервисе и прилагођене токове рада. Он вам омогућава да позивате ниско-нивне API-је за превођење садржаја за појединачне датотеке, или покренете исту оркестрацију на нивоу репозиторијума коју користи CLI.

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

Покрените превођење репозиторијума из Python-а:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Погодно за:

- Ваша апликација већ чита датотеке, бафере, ноутбуке или бајтове слика.
- Потребна вам је прилагођена валидација, складиштење, логовање, поновни покушаји или токови одобравања.
- Желите да преведете један документ, ноутбук или слику без обраде целог репозиторијума.
- Желите превођење репозиторијума, али преко Python аутоматизације уместо shell команде.

## Користите MCP сервер када

Изаберите MCP сервер када агент, уређивач или MCP-компатибилан клијент треба да позове алате Co-op Translator-а.

У нормалној локалној конфигурацији корисник не покреће сервер ручно. MCP клијент покреће `co-op-translator-mcp` преко `stdio` када му затребају алати.

Примери захтева корисника које агент може обрадити:

- "Преведи овај Markdown фајл на корејски и задржи исправне линкове."
- "Преведи овај Markdown фајл на корејски уз MCP радни ток помоћу агента, користећи свој модел за преведене делове."
- "Преведи овај ноутбук на корејски, сачувај код ћелија и користи Co-op Translator MCP за реконструкцију ноутбука."
- "Преведи текст на овој слици на јапански и сачувај резултат."
- "Изврши сухи покрет превођења репозиторијума на шпански и реци ми шта би се променило."
- "Проверити да ли је излаз корејског превода ажуран."

За Markdown и ноутбуке, MCP може радити у два режима:

| Режим | Користити када | Главни алати |
| --- | --- | --- |
| Уз помоћ агента | Домаћински MCP агент треба да преводи делове својим моделом, без креденцијала провајдера LLM-а Co-op Translator-а. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Подржан од провајдера | Co-op Translator треба директно да позове Azure OpenAI, OpenAI или Anthropic. | `translate_markdown_content`, `translate_notebook_content` |

Облик позива Markdown алата подржан од MCP провајдера:

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

MCP image tool call shape:

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

Превођење репозиторијума се по подразумеваној вредности извршава као пробно преко MCP-а:

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

- Желите токове превођења у природном језику унутар агента или уређивача.
- Желите превођење Markdown-а или ноутбука у којем модел домаћинског агента преводи припремљене делове.
- Желите да агент преведе одабран садржај уместо целог репозиторијума.
- Желите корак одобравања пре писања по целом репозиторијуму.
- Желите један интерфејс који пружа алате за Markdown, ноутбуке, слике, преглед и преписивање путева.

## Како се уклапају

CLI је најбољи подешен избор за људе који преводе репозиторијуме. Python API је најбољи када ваш код управља радним током. MCP сервер је најбољи када агент или уређивач управља радним током.

Сва три пута користе исти јавни Co-op Translator API, тако да можете почети са CLI-јем, касније аутоматизовати помоћу Python-а, и изложити исте могућности MCP клијентима када вам затребају радни токови које покрећу агенти.