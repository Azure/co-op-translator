# Изберете вашия работен поток

Co-op Translator може да се използва по три начина: CLI, Python API и MCP сървър. Те споделят същите възможности за превод, но всеки един пасва на различен работен поток.

Използвайте тази страница, когато решавате откъде да започнете.

## Бързо решение

| Ако искате да... | Използвайте | Започнете тук |
| --- | --- | --- |
| Да преведете или прегледате хранилище от терминала | CLI | [CLI Reference](cli.md) |
| Да добавите превод в Python скрипт, услуга, бележник или CI задача | Python API | [Python API](api.md) |
| Да позволите на агент, редактор или MCP-съвместим клиент да преведе съдържание вместо вас | MCP Server | [MCP Server](mcp.md) |
| Да преведете един Markdown документ, бележник или изображение, което вашето приложение вече е заредило | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| Да преведете цялото хранилище със стандартни изходни папки и метаданни | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Използвайте CLI когато

Изберете CLI, когато човек или CI задача управлява превода на репозитория от терминала.

CLI е най-прекия път, когато искате Co-op Translator да открие файловете на проекта, да създаде преведени резултати, да запази структурата на проекта, да актуализира метаданните и да изпълни команди за преглед.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Подходящо за:

- Превеждате хранилище от терминала.
- Искате повтаряща се команда за CI или release работни процеси.
- Искате вградено откриване на проекти, изходни пътища, метаданни, почистване и преглед.
- Предпочитате команден интерфейс пред писане на Python код.

## Използвайте Python API когато

Изберете Python API, когато вашият код трябва да контролира работния поток.

API е полезен за приложения, автоматизационни скриптове, бележници, услуги и персонализирани пайплайни. Той ви позволява да извиквате ниско-ниво API-та за превод на съдържание за отделни файлове или да стартирате същата оркестрация на ниво репозитории, която използва CLI.

Преведете един Markdown документ и решете къде да го запазите:

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

Подходящо за:

- Вашето приложение вече чете файлове, буфери, бележници или байтове от изображения.
- Имaте нужда от персонализирана валидация, съхранение, логване, повторни опити или одобрителни потоци.
- Искате да преведете един документ, бележник или изображение без да обработвате цялото хранилище.
- Искате превод на хранилище, но чрез Python автоматизация вместо команден ред.

## Използвайте MCP Server когато

Изберете MCP сървъра, когато агент, редактор или MCP-съвместим клиент трябва да извиква инструментите на Co-op Translator.

В нормалната локална настройка потребителят не поддържа ръчно сървър в изпълнение. MCP клиентът стартира `co-op-translator-mcp` над `stdio`, когато се нуждае от инструментите.

Примери за потребителски заявки, които агентът може да обработи:

- "Преведи този Markdown файл на корейски и запази връзките правилни."
- "Преведи този Markdown файл на корейски с MCP работния поток, подпомогнат от агент, като използваш собствен модел за превод на фрагментите."
- "Преведи този бележник на корейски, запази клетките с код и използвай Co-op Translator MCP за реконструиране на бележника."
- "Преведи текста в това изображение на японски и запази резултата."
- "Направи пробно превеждане на хранилище на испански и ми кажи какво би се променило."
- "Провери дали изходът на корейския превод е актуален."

За Markdown и бележници, MCP може да работи в два режима:

| Режим | Използвайте когато | Основни инструменти |
| --- | --- | --- |
| С подпомагане от агент | Агентът-хост на MCP трябва да превежда фрагментите със собствен модел, без идентификационни данни за доставчик на LLM от Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Подкрепено от доставчик | Co-op Translator трябва да извика Azure OpenAI или OpenAI директно. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool call shape:

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

Преводът на репозитория чрез MCP по подразбиране се изпълнява като dry-run:

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

- Искате работни потоци за превод на естествен език в рамките на агент или редактор.
- Искате превод на Markdown или бележник, при който моделът на хоста-агент превежда подготвените фрагменти.
- Искате агентът да превежда избрано съдържание, вместо цялото хранилище.
- Искате стъпка за одобрение преди записване в целия репозитория.
- Искате един интерфейс, който предлага инструменти за Markdown, бележник, изображение, преглед и пренаписване на пътища.

## Как се вписват помежду си

CLI е най-добрият по подразбиране избор за хора, които превеждат хранилища. Python API е най-подходящ, когато вашият код контролира работния поток. MCP сървърът е най-добър, когато агент или редактор контролира работния поток.

Всички три пътя използват един и същ публичен Co-op Translator API, така че можете да започнете с CLI, да автоматизирате с Python по-късно и да изложите същите възможности на MCP клиенти, когато имате нужда от работни потоци, управлявани от агенти.