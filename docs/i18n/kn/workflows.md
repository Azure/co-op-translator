# ನಿಮ್ಮ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಆಯ್ಕೆಮಾಡಿ

Co-op Translator ಅನ್ನು ಮೂರು ರೀತಿಗಳಲ್ಲಿ ಬಳಸಬಹುದು: CLI, Python API, ಮತ್ತು MCP ಸರ್ವರ್. ಅವುಗಳೆಲ್ಲವೂ ಅದೇ ಅನುವಾದ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತವೆ, ಆದರೆ ಪ್ರತಿ ಒಂದು ವಿಭಿನ್ನ ಕಾರ್ಯಪ್ರವಾಹಕ್ಕೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.

ಯಾವ ಸ್ಥಳದಿಂದ ಆರಂಭಿಸಬೇಕೆಂದು ನಿರ್ಧರಿಸುತ್ತಿರುವಾಗ ಈ ಪುಟವನ್ನು ಉಪಯೋಗಿಸಿ.

## ತ್ವರಿತ ನಿರ್ಧಾರ

| ನೀವು ಬಯಸಿದ್ದರೆ... | ಬಳಸುವುದು | ಇಲ್ಲಿ ಪ್ರಾರಂಭಿಸಿ |
| --- | --- | --- |
| ಟರ್ಮಿನಲ್‌ನಿಂದ ರೆಪೊಸಿಟರಿಯನ್ನು ಅನುವದಿಸಲು ಅಥವಾ ಪರಿಶೀಲಿಸಲು | CLI | [CLI ಉಲ್ಲೇಖ](cli.md) |
| Python ಸ್ಕ್ರಿಪ್ಟ್, ಸೇವೆ, ನೋಟ್‌ಬುಕ್, ಅಥವಾ CI ಕೆಲಸಕ್ಕೆ ಅನುವಾದ ಸೇರಿಸಲು | Python API | [Python API](api.md) |
| ಏಜೆಂಟ್, ಎಡಿಟರ್, ಅಥವಾ MCP-ಸಾಮ್ಯ 클ೈಂಟ್ ನಿಮಗಾಗಿ ವಿಷಯವನ್ನು ಅನುವಾದಿಸಲಿ | MCP ಸರ್ವರ್ | [MCP Server](mcp.md) |
| ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಈಗಾಗಲೇ ಲೋಡ್ ಮಾಡಿದ ಒಂದು Markdown ಡಾಕ್ಯುಮೆಂಟ್, ನೋಟ್‌ಬುಕ್, ಅಥವಾ ಚಿತ್ರ ಅನ್ನು ಅನುವಾದಿಸಲು | Python API ಅಥವಾ MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| ಸಾಮಾನ್ಯ ಔಟ್‌ಪುಟ್ ಫೋಲ್ಡರ್‌ಗಳು ಮತ್ತು ಮೆಟಾಡೇಟಾ ಹೊಂದಿರುವ ಸಂಪೂರ್ಣ ರೆಪೊಸಿಟರಿಯನ್ನು ಅನುವಾದಿಸಲು | CLI ಅಥವಾ `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## CLI ಅನ್ನು ಬಳಸಬೇಕಾದಾಗ

ಯಾರಾದರೂ ಅಥವಾ CI ಕೆಲಸವು ಶೆಲ್ಲಿನಿಂದ ರೆಪೊಸಿಟರಿ ಅನುವಾದವನ್ನು ನಡಿಸುತ್ತದೆ ಎಂದಾದರೆ CLI ಆಯ್ಕೆಮಾಡಿ.

Co-op Translator ಪ್ರಾಜೆಕ್ಟ್ ಫೈಲ್‌ಗಳನ್ನು ಕಂಡುಹಿಡಿಯೋ, ಅನುವಾದಿತ ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸೋ, ಪ್ರಾಜೆಕ್ಟ್ ವಿನ್ಯಾಸವನ್ನು ಕಾಪಾಡೋ, ಮೆಟಾಡೇಟಾ ನವೀಕರಿಸೋ ಮತ್ತು ವಿಮರ್ಶಾ ಆಜ್ಞೆಗಳನ್ನು ನಡವಾಡೋ ಬಯಸಿದಾಗ CLI ಅತ್ಯಂತ ನೇರ ಮಾರ್ಗವಾಗಿದೆ.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

ಉತ್ತಮ ಹೊಂದಾಣಿಕೆಗಳು:

- ನೀವು ಟರ್ಮಿನಲ್‌ನಿಂದ ರೆಪೊಸಿಟರಿಯನ್ನು ಅನುವಾದಿಸುತ್ತಿದ್ದೀರಿ.
- CI ಅಥವಾ ರಿಲೀಸ್ ಕಾರ್ಯಪ್ರವಾಹಗಳಿಗಾಗಿ ಪುನರಾವರ್ತಿಸಬಹುದಾದ ಆಜ್ಞೆಯು ಬೇಕು.
- ನಿಮಗೆ ನಿರ್ಮಿತ ಪ್ರಾಜೆಕ್ಟ್ ಕಂಡುಹಿಡಿತ, ಔಟ್‌ಪುಟ್ ಮಾರ್ಗಗಳು, ಮೆಟಾಡೇಟಾ, ಸ್ವಚ್ಛತೆ ಮತ್ತು ವಿಮರ್ಶೆ ಬೇಕಾಗಿದೆ.
- Python ಕೋಡ್ ಬರೆಯುವುದಕ್ಕೆ ಬದಲು ಆಜ್ಞಾ ಇಂಟರ್ಫೇಸ್ ಇಷ್ಟವಿದ್ದರೆ.

## Python API ಅನ್ನು ಬಳಸಬೇಕಾದಾಗ

ನಿಮ್ಮ ಸ್ವಂತ ಕೋಡ್ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ನಿಯಂತ್ರಿಸಬೇಕು ಎಂದಾದರೆ Python API ಆಯ್ಕೆಮಾಡಿ.

API ಅಪ್ಲಿಕೇಶನ್‌ಗಳು, automation ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು, ನೋಟ್‌ಬುಕ್‌ಗಳು, ಸೇವೆಗಳು ಮತ್ತು ಕಸ್ಟಮ್ ಪೈಪ್‌ಲೈನ್‌ಗಳಿಗಾಗಿ ಉಪಯುಕ್ತವಾಗಿದೆ. ಇದು ನಿಮಗೆ ವೈಯಕ್ತಿಕ ಫೈಲ್‌ಗಳಿಗಾಗಿ ತಳಸ್ಥರ ವಿಷಯ ಅನುವಾದ APIಗಳನ್ನು ಕರೆಯಲು ಅಥವಾ CLI ಬಳಸುವ ಇದೇ ರೆಪೊಸಿಟರಿ-ಮಟ್ಟದ ಕ್ರಮವನ್ನೇ Python ನಿಂದ ನಡೆಸಲು ಅನುಮತಿಸುತ್ತದೆ.

ಒಂದು Markdown ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಅನುವಾದಿಸಿ ಮತ್ತು ಅದನ್ನು ಎಲ್ಲಿ ಉಳಿಸಬೇಕೆಂದು ನಿರ್ಧರಿಸಿ:

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

Python ನಿಂದ ರೆಪೊಸಿಟರಿ ಅನುವಾದವನ್ನು ನಡಿಸಿ:

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

ಉತ್ತಮ ಹೊಂದಾಣಿಕೆಗಳು:

- ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಈಗಾಗಲೇ ಫೈಲ್‌ಗಳು, ಬಫರ್‌ಗಳು, ನೋಟ್‌ಬುಕ್‌ಗಳು ಅಥವಾ ಇಮೇಜ್ ಬೈಟ್‌ಗಳನ್ನು ಓದುತ್ತದೆ.
- ನಿಮಗೆ ಕಸ್ಟಮ್ ಮಾನ್ಯತೆ, ಸಂಗ್ರಹ, ಲಾಗಿಂಗ್, ಪುನರಾಯತ್ನಗಳು, ಅಥವಾ ಅನುಮೋದನೆ ಪ್ರಕ್ರಿಯೆಗಳನ್ನು ಬೇಕಾಗಿರುತ್ತದೆ.
- ಸಂಪೂರ್ಣ ರೆಪೊಸಿಟರಿಯನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸದೆ ಒಂದು ಡಾಕ್ಯುಮೆಂಟ್, ನೋಟ್‌ಬುಕ್, ಅಥವಾ ಇಮೇಜ್ ಅನ್ನು ಅನುವಾದಿಸಬೇಕಿದ್ದರೆ.
- ನೀವು ರೆಪೊಸಿಟರಿ ಅನುವಾದವನ್ನು ಬಯಸುತ್ತೀರಿ, ಆದರೆ ಶೆಲ್ ಆಜ್ಞೆಯ ಬದಲು Python ಆಟೋಮೇಶನ್‌ನಿಂದ.

## MCP ಸರ್ವರ್ ಅನ್ನು ಬಳಸಬೇಕಾದಾಗ

ಏಜೆಂಟ್, ಎಡಿಟರ್ ಅಥವಾ MCP-ಸಾಮ್ಯ 클ೈಂಟ್ Co-op Translator ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡಬೇಕಾದಾಗ MCP ಸರ್ವರ್ ಆಯ್ಕೆಮಾಡಿ.

ಸಾಮಾನ್ಯ ಸ್ಥಳೀಯ ಸೆಟಪ್‌ನಲ್ಲಿ, ಬಳಕೆದಾರನು ಕೈಯಿಂದ ಸರ್ವರ್ ಅನ್ನು ರನ್ ಮಾಡಲ್ಲ. MCP ಕ್ಲೈಂಟ್ ಸಾಧನಗಳ ಅಗತ್ಯವಿದ್ದಾಗ `stdio` ಮೂಲಕ `co-op-translator-mcp` ಅನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ.

ಏಜೆಂಟ್ ನಿರ್ವಹಿಸಬಹುದಾದ ಉದಾಹರಣೆಯ ಬಳಕೆದಾರ ವಿನಂತಿಗಳು:

- "ಈ Markdown ಫೈಲ್ ಅನ್ನು ಕೊರಿಯನ್‌ಗೆ ಅನುವಾದಿಸಿ ಮತ್ತು ಲಿಂಕ್‌ಗಳನ್ನು ಸರಿಯಾಗೆಯೇ ಉಳಿಸಿ."
- "ಏಜೆಂಟ್ ಸಹಾಯಿತ MCP ಕಾರ್ಯಪ್ರವಾಹದೊಂದಿಗೆ ಈ Markdown ಫೈಲ್ ಅನ್ನು ಕೊರಿಯನ್‌ಗೆ ಅನುವಾದಿಸಿ, ಅನುವಾದಿತ ಭಾಗಗಳಿಗೆ ನಿಮ್ಮ ಸ್ವಂತ ಮಾದರಿಯನ್ನು ಬಳಸಿ."
- "ಈ ನೋಟ್‌ಬುಕ್ ಅನ್ನು ಕೊರಿಯನ್‌ಗೆ ಅನುವಾದಿಸಿ, ಕೋಡ್ ಸೆಲ್‌ಗಳನ್ನು ಉಳಿಸಿಡಿ, ಮತ್ತು ನೋಟ್‌ಬುಕ್ ಅನ್ನು ಪುನರ್ ರಚಿಸಲು Co-op Translator MCP ಅನ್ನು ಬಳಸಿ."
- "ಈ ಚಿತ್ರದಲ್ಲಿರುವ ಪಠ್ಯವನ್ನು ಜಪಾನಿ ಭಾಷೆಗೆ ಅನುವಾದಿಸಿ ಮತ್ತು ಫಲಿತಾಂಶವನ್ನು ಸಂರಕ್ಷಿಸಿ."
- "ರೆಪೊಸಿಟರಿ ಅನುವಾದವನ್ನು ಸ್ಪ್ಯಾನಿಷ್‌ಗೆ ಡ್ರೈ-ರನ್ ಮಾಡಿ ಮತ್ತು ಏನಿದು ಬದಲಾಗುತ್ತದೆಯೆಂದು ನನಗೆ ತಿಳಿಸಿ."
- "ಕೊರಿಯನ್ ಅನುವಾದ ಔಟ್‌ಪುಟ್ ನವೀಕರಿಸಲಾಗಿದೆ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸಿ."

Markdown ಮತ್ತು ನೋಟ್‌ಬುಕ್‌ಗಳಿಗಾಗಿ, MCP ಎರಡು ಮೋಡ್‌ಗಳಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸಬಹುದು:

| ಮೋಡ್ | ಯಾವಾಗ ಬಳಕೆಮಾಡುವುದು | ಮುಖ್ಯ ಸಾಧನಗಳು |
| --- | --- | --- |
| ಏಜೆಂಟ್-ಸಹಾಯಿತ | MCP ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ತನ್ನ ಸ್ವಂತ ಮಾದರಿಯನ್ನು ಬಳಸಿ ಭಾಗಗಳನ್ನು ಅನುವಾದಿಸಬೇಕು, Co-op Translator LLM ಪ್ರೊವೈಡರ್ ಕ್ರೆಡೆಂಶಿಯಲ್ಸ್ ಇಲ್ಲದೆ. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ಪ್ರೊವೈಡರ್-ಬೆಕ್‌ಡ್ | Co-op Translator ನೇರವಾಗಿ Azure OpenAI ಅಥವಾ OpenAI ಅನ್ನು ಕರೆ ಮಾಡಬೇಕು. | `translate_markdown_content`, `translate_notebook_content` |

MCP ಪ್ರೊವೈಡರ್-ಬೆಕ್‌ಡ್ Markdown ಸಾಧನ ಕರೆ ರೂಪ:

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

MCP ಇಮೇಜ್ ಸಾಧನ ಕರೆ ರೂಪ:

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

ರೆಪೊಸಿಟರಿ ಅನುವಾದವು MCP ಮೂಲಕ ಡೀಫಾಲ್ಟ್ ಆಗಿ ಡ್ರೈ-ರನ್ ಆಗಿದೆ:

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

ಉತ್ತಮ ಹೊಂದಾಣಿಕೆಗಳು:

- ಏಜೆಂಟ್ ಅಥವಾ ಎಡಿಟರ್ ಒಳಗೆ ನೈಸರ್ಗಿಕ-ಭಾಷಾ ಅನುವಾದ ಕಾರ್ಯಪ್ರವಾಹ ಬೇಕಾದಾಗ.
- ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಮಾದರಿ ತಯಾರಿಸಿದ ಭಾಗಗಳನ್ನು ಅನುವಾದಿಸುವ Markdown ಅಥವಾ ನೋಟ್‌ಬುಕ್ ಅನುವಾದ ಬೇಕಿದ್ದಲ್ಲಿ.
- ಸಂಪೂರ್ಣ ರೆಪೊಸಿಟರಿಯ ಬದಲಾಗಿ ಆಯ್ಕೆಯಾದ ವಿಷಯವನ್ನು ಏಜೆಂಟ್ ಅನುವಾದಿಸಬೇಕು ಎಂದು ಬಯಸಿದರೆ.
- ರೆಪೊಸಿಟರಿ-ವ್ಯಾಪ್ತಿ ಬರೆದಾಗ mbere ಅನುಮೋದನೆ ಹಂತ ಬೇಕಾದರೆ.
- Markdown, ನೋಟ್‌ಬುಕ್, ಚಿತ್ರ, ವಿಮರ್ಶೆ ಮತ್ತು ಮಾರ್ಗ-ಮರುಬರಹ ಸಾಧನಗಳನ್ನು ಒಟ್ಟಿಗೆ ಒದಗಿಸುವ ಒಂದು ಇಂಟರ್ಫೇಸ್ ಬೇಕಾದರೆ.

## ಅವುಗಳು ಒಟ್ಟಿಗೆ ಹೇಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತವೆ

CLI ಮಾನವರು ರೆಪೊಸಿಟರಿಗಳನ್ನು ಅನುವಾದಿಸುವಾಗ ಉತ್ತಮ ಡಿಫಾಲ್ಟ್ ಆಗಿದೆ. ನಿಮ್ಮ ಕೋಡ್ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಹೊಂದಿದಾಗ Python API ಉತ್ತಮವಾಗಿದೆ. ಏಜೆಂಟ್ ಅಥವಾ ಎಡಿಟರ್ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ನಿಯಂತ್ರಿಸಿದಾಗ MCP ಸರ್ವರ್ ಉತ್ತಮವಾಗಿದೆ.

ಈ ಮೂರು ಮಾರ್ಗಗಳು ಒಂದೇ सार्वजनिक Co-op Translator API ಅನ್ನು ಬಳಸುತ್ತವೆ, ಆದ್ದರಿಂದ ನೀವು CLI ನಿಂದ ಪ್ರಾರಂಭಿಸಿ, ನಂತರ Python ಮೂಲಕ ಆಟೋಮೇಟ್ ಮಾಡಿ, ಮತ್ತು ಏಜೆಂಟ್ ಚಾಲಿತ ಕಾರ್ಯಪ್ರವಾಹಗಳ ಅಗತ್ಯವಿದ್ದಾಗ MCP ಕ್ಲೈಂಟ್‌ಗಳಿಗೆ ಅದೇ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಒದಗಿಸಬಹುದು.