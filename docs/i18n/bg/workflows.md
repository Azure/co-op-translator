# Изберете своя работен процес

Co-op Translator може да се използва по три начина: CLI, Python API и MCP server. Те споделят същите възможности за превод, но всеки от тях пасва на различен работен процес.

Използвайте тази страница, когато решавате откъде да започнете.

**Ако редактирате преводите ръчно:** по подразбиране CLI и Actions работните потоци превеждат променените изходни файлове изцяло, така че вашите формулировки в тези файлове могат да бъдат презаписани. Прегледайте diff-а преди да приемете актуализация. За запазване на блоковете в Markdown при приети редакции използвайте опционалния [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Бързо решение

| Ако искате да... | Използвайте | Започнете тук |
| --- | --- | --- |
| Превеждате или преглеждате репозитория от терминал | CLI | [Референция за CLI](cli.md) |
| Добавите превод в Python скрипт, услуга, тетрадка или CI задача | Python API | [Python API](api.md) |
| Позволите на агент, редактор или MCP-съвместим клиент да преведе съдържанието вместо вас | MCP Server | [MCP Server](mcp.md) |
| Преведете един Markdown документ, тетрадка или изображение, което вашето приложение вече е заредило | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Преведете цялото хранилище с стандартни папки за изход и метаданни | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Използвайте CLI, когато

Изберете CLI, когато човек или CI задача стартира превода на репозитория от терминал.

CLI е най-прекия път, когато искате Co-op Translator да открие файловете на проекта, да създаде преведени резултати, да запази разположението на проекта, да актуализира метаданни и да изпълни команди за преглед.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Този пример превежда Markdown и бележници. Добавете `-img` само след конфигуриране на [Azure AI Vision](configuration.md#azure-ai-vision). За първо изпълнение само с Markdown, следвайте [Вашия първи превод](first-translation.md).

Подходящо за:

- Превеждате репозитория от терминала си.
- Искате повторяема команда за CI или release работни процеси.
- Искате вградена откриваемост на проекта, изходни пътища, метаданни, почистване и преглед.
- Предпочитате интерфейс чрез команди вместо писане на Python код.

## Използвайте Python API, когато

Изберете Python API, когато вашият код трябва да контролира работния процес.

API е полезен за приложения, автоматизационни скриптове, тетрадки, услуги и персонализирани конвейери. Той ви позволява да извиквате нискониво APIs за превод на съдържание за отделни файлове или да изпълните същата оркестрация на ниво репозитория, използвана от CLI.

Преведете един Markdown документ и решете къде да го запишете:

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

Изпълнете превод на репозитория от Python:

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

Подходящо за:

- Вашето приложение вече чете файлове, буфери, тетрадки или байтове на изображения.
- Имате нужда от персонализирана валидация, съхранение, логване, повторни опити или потоци за одобрение.
- Искате да преведете един документ, тетрадка или изображение без да обработвате цялото хранилище.
- Искате превод на репозитория, но чрез Python автоматизация вместо чрез команда в shell.

## Използвайте MCP Server, когато

Изберете MCP server, когато агент, редактор или MCP-съвместим клиент трябва да извика инструментите на Co-op Translator.

В нормалната локална конфигурация потребителят не поддържа ръчно сървър в работно състояние. MCP клиентът стартира `co-op-translator-mcp` през `stdio`, когато се нуждае от инструментите.

Примерни потребителски заявки, които агентът може да обработи:

- "Преведи този Markdown файл на корейски и запази връзките коректни."
- "Преведи този Markdown файл на корейски с помощта на MCP workflow с асистиращ агент, като използваш собствен модел за преведените парчета."
- "Преведи тази тетрадка на корейски, запази кодовите клетки и използвай Co-op Translator MCP за реконструкция на тетрадката."
- "Преведи текста в това изображение на японски и запази резултата."
- "Направи пробно (dry-run) превеждане на репозитория на испански и ми кажи какво би се променило."
- "Прегледай дали корейският превод е актуален."

За Markdown и тетрадки, MCP може да работи в два режима:

| Режим | Използвайте когато | Основни инструменти |
| --- | --- | --- |
| С агентска помощ | Хост агентът на MCP трябва да превежда парчета със собствения си модел, без креденшъли за доставчик на LLM на Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| С подкрепа от доставчик | Co-op Translator трябва да вика Azure OpenAI, OpenAI или Anthropic директно. | `translate_markdown_content`, `translate_notebook_content` |

Формат на извикване на Markdown инструмента при MCP, подкрепен от доставчик:

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

Формат на извикване на изображителния инструмент на MCP:

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

Преводът на репозитория е по подразбиране в режим dry-run чрез MCP:

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

Подходящо за:

- Искате естественоезикови преводни работни потоци вътре в агент или редактор.
- Искате превод на Markdown или тетрадки, където моделът на хост агента превежда подготвените парчета.
- Искате агентът да превежда избрано съдържание вместо цялото хранилище.
- Искате стъпка за одобрение преди записване в цялото хранилище.
- Искате един интерфейс, който предоставя инструменти за Markdown, тетрадки, изображения, преглед и пренаписване на пътища.

## Как се вписват заедно

CLI е най-добрият избор по подразбиране за хора, които превеждат репозитории. Python API е най-подходящ, когато вашият код управлява работния процес. MCP server е най-подходящ, когато агент или редактор управлява работния процес.

Всички три пътя използват един и същи публичен Co-op Translator API, така че можете да започнете с CLI, да автоматизирате с Python по-късно и да изложите същите възможности на MCP клиенти, когато имате нужда от работни потоци, управлявани от агенти.