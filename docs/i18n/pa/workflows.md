# ਆਪਣਾ ਵਰਕਫਲੋ ਚੁਣੋ

Co-op Translator ਤਿੰਨ ਤਰੀਕਿਆਂ ਨਾਲ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ: CLI, Python API, ਅਤੇ MCP ਸਰਵਰ। ਇਹਨਾਂ ਕੋਲ ਇੱਕੋ ਜਿਹੀਆਂ ਅਨੁਵਾਦ ਸਮਰੱਥਾਵਾਂ ਹਨ, ਪਰ ਹਰ ਇੱਕ ਵੱਖਰੇ ਵਰਕਫਲੋ ਲਈ موزੂ ਹੈ।

ਇਹ ਪੰਨਾ ਵਰਤੋਂ ਜਦੋਂ ਤੁਸੀਂ ਇਹ ਫੈਸਲਾ ਕਰ ਰਹੇ ਹੋ ਕਿ ਕਿੱਥੋਂ ਸ਼ੁਰੂ ਕਰਨਾ ਹੈ।

## ਤੁਰੰਤ ਫੈਸਲਾ

| If you want to... | Use | Start here |
| --- | --- | --- |
| ਟਰਮੀਨਲ ਤੋਂ ਇੱਕ ਰਿਪੋਜ਼ਿਟਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰੋ ਜਾਂ ਸਮੀਖਿਆ ਕਰੋ | CLI | [CLI ਰੈਫਰੇਂਸ](cli.md) |
| Python ਸਕ੍ਰਿਪਟ, ਸਰਵਿਸ, ਨੋਟਬੁੱਕ, ਜਾਂ CI ਜੌਬ ਵਿੱਚ ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਕਰੋ | Python API | [Python API](api.md) |
| ਇੱਕ ਏਜੰਟ, ਐਡੀਟਰ, ਜਾਂ MCP-ਕੰਪੈਟਿਬਲ ਕਲਾਇੰਟ ਨੂੰ ਤੁਹਾਡੇ ਲਈ ਸਮੱਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰਨ ਦਿਓ | MCP Server | [MCP Server](mcp.md) |
| ਇੱਕ Markdown ਦਸਤਾਵੇਜ਼, ਨੋਟਬੁੱਕ, ਜਾਂ ਤਸਵੀਰ ਜਿਸਨੂੰ ਤੁਹਾਡੀ ਐਪ ਪਹਿਲਾਂ ਹੀ ਲੋਡ ਕਰ ਚੁੱਕੀ ਹੈ, ਦਾ ਅਨੁਵਾਦ ਕਰੋ | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| ਪੂਰੀ ਰਿਪੋਜ਼ਿਟਰੀ ਨੂੰ ਮਿਆਰੀ ਆਉਟਪੁੱਟ ਫੋਲਡਰਾਂ ਅਤੇ ਮੈਟਾ ਡੇਟਾ ਨਾਲ ਅਨੁਵਾਦ ਕਰੋ | CLI or `run_translation` | [CLI ਰੈਫਰੇਂਸ](cli.md) or [Python API](api.md) |

## CLI ਵਰਤੋਂ ਕਰੋ ਜਦੋਂ

ਉਸ ਵੇਲੇ CLI ਚੁਣੋ ਜਦੋਂ ਕੋਈ ਵਿਅਕਤੀ ਜਾਂ CI ਨੌਕਰੀ ਸ਼ੈੱਲ ਤੋਂ ਰਿਪੋਜ਼ਿਟਰੀ ਦਾ ਅਨੁਵਾਦ ਚਲਾ ਰਹੀ ਹੋਵੇ।

CLI ਸਭ ਤੋਂ ਸਿੱਧਾ ਰਸਤਾ ਹੈ ਜਦੋਂ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ Co-op Translator ਪ੍ਰੋਜੈਕਟ ਫਾਇਲਾਂ ਦੀ ਖੋਜ ਕਰੇ, ਅਨੁਵਾਦਿਤ ਆਉਟਪੁੱਟ ਬਣਾਏ, ਪ੍ਰੋਜੈਕਟ ਲੇਆਉਟ ਨੂੰ ਕਾਇਮ ਰੱਖੇ, ਮੈਟਾ ਡੇਟਾ ਅਪਡੇਟ ਕਰੇ, ਅਤੇ ਸਮੀਖਿਆ ਕਮਾਂਡ ਚਲਾਏ।

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

ਉਪਯੋਗ ਲਈ ਢੁਕਵਾਂ:

- ਤੁਸੀਂ ਆਪਣੇ ਟਰਮੀਨਲ ਤੋਂ ਇੱਕ ਰਿਪੋਜ਼ਿਟਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰ ਰਹੇ ਹੋ।
- ਤੁਸੀਂ CI ਜਾਂ ਰਿਲੀਜ਼ ਵਰਕਫਲੋਜ਼ ਲਈ ਇੱਕ ਦੁਹਰਾਊ ਕਮਾਂਡ ਚਾਹੁੰਦੇ ਹੋ।
- ਤੁਸੀਂ ਨਿਰਮਿਤ ਪ੍ਰੋਜੈਕਟ ਖੋਜ, ਆਉਟਪੁੱਟ ਪਾਥ, ਮੈਟਾ ਡੇਟਾ, ਸਾਫ਼-ਸਫ਼ਾਈ, ਅਤੇ ਸਮੀਖਿਆ ਚਾਹੁੰਦੇ ਹੋ।
- ਤੁਸੀਂ ਪਾਇਥਨ ਕੋਡ ਲਿਖਣ ਦੀ ਥਾਂ ਕਮਾਂਡ ਇੰਟਰਫੇਸ ਨੂੰ ਤਰਜੀਹ ਦਿੰਦੇ ਹੋ।

## Python API ਵਰਤੋਂ ਕਰੋ ਜਦੋਂ

ਉਸ ਵੇਲੇ Python API ਚੁਣੋ ਜਦੋਂ ਤੁਹਾਡਾ ਆਪਣਾ ਕੋਡ ਵਰਕਫਲੋ ਨੂੰ ਕੰਟਰੋਲ ਕਰੇ।

API ਐਪਲੀਕੇਸ਼ਨਾਂ, ਆਟੋਮੇਸ਼ਨ ਸਕ੍ਰਿਪਟਾਂ, ਨੋਟਬੁੱਕਾਂ, ਸਰਵਿਸز, ਅਤੇ کسਟਮ ਪਾਇਪਲਾਈਨਾਂ ਲਈ ਲਾਭਦਾਇਕ ਹੈ। ਇਹ ਤੁਹਾਨੂੰ ਵਿਅਕਤੀਗਤ ਫਾਇਲਾਂ ਲਈ ਨੀਚਲੇ-ਸਤਰ ਦੀ ਸਮੱਗਰੀ ਅਨੁਵਾਦ API ਕਾਲ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਜਾਂ CLI ਦੁਆਰਾ ਵਰਤਿਆ ਜਾਣ ਵਾਲੇ ਇੱਕੋ ਜਿਹੇ ਰਿਪੋਜ਼ਿਟਰੀ-ਸਤਹ ਦੇ ਆਰਕੇਸ्ट्रੇਸ਼ਨ ਨੂੰ ਚਲਾਉਣ ਦਿੰਦਾ ਹੈ।

ਇੱਕ Markdown ਦਸਤਾਵੇਜ਼ ਅਨੁਵਾਦ ਕਰੋ ਅਤੇ ਫੈਸਲਾ ਕਰੋ ਕਿ ਇਸਨੂੰ ਕਿੱਥੇ ਸੇਵ ਕਰਨਾ ਹੈ:

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

Python ਤੋਂ ਰਿਪੋਜ਼ਿਟਰੀ ਅਨੁਵਾਦ ਚਲਾਉਣਾ:

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

ਉਪਯੋਗ ਲਈ ਢੁਕਵਾਂ:

- ਤੁਹਾਡੀ ਐਪਲੀਕੇਸ਼ਨ ਪਹਿਲਾਂ ਹੀ ਫਾਇਲਾਂ, ਬਫਰ, ਨੋਟਬੁੱਕ, ਜਾਂ ਤਸਵੀਰ ਬਾਈਟਸ ਪੜ੍ਹਦੀ ਹੈ।
- ਤੁਹਾਨੂੰ کسਟਮ ਵੈਰਿਫਿਕੇਸ਼ਨ, ਸਟੋਰੇਜ, ਲੋਗਿੰਗ, ਰੀਟ੍ਰਾਈ, ਜਾਂ ਮਨਜ਼ੂਰੀ ਵਹਿਣ ਦੀ ਲੋੜ ਹੈ।
- ਤੁਸੀਂ ਇੱਕ ਦਸਤਾਵੇਜ਼, ਨੋਟਬੁੱਕ, ਜਾਂ ਤਸਵੀਰ ਦਾ ਅਨੁਵਾਦ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਬਿਨਾਂ ਪੂਰੀ ਰਿਪੋਜ਼ਿਟਰੀ ਪ੍ਰੋਸੈਸ ਕੀਤੇ।
- ਤੁਸੀਂ ਰਿਪੋਜ਼ਿਟਰੀ ਅਨੁਵਾਦ ਚਾਹੁੰਦੇ ਹੋ, ਪਰ ਸ਼ੈੱਲ ਕਮਾਂਡ ਦੀ ਥਾਂ Python ਆਟੋਮੇਸ਼ਨ ਤੋਂ।

## MCP ਸਰਵਰ ਵਰਤੋਂ ਕਰੋ ਜਦੋਂ

ਉਸ ਵੇਲੇ MCP ਸਰਵਰ ਚੁਣੋ ਜਦੋਂ ਕੋਈ ਏਜੰਟ, ਐਡੀਟਰ, ਜਾਂ MCP-ਕੰਪੈਟਿਬਲ ਕਲਾਇੰਟ Co-op Translator ਟੂਲਸ ਨੂੰ ਕਾਲ ਕਰੇ।

ਆਮ ਲੋਕਲ ਸੈਟਅਪ ਵਿੱਚ, ਯੂਜ਼ਰ ਮੈਨੂਅਲੀ ਤੌਰ 'ਤੇ ਸਰਵਰ ਚਲਾਉਂਦਾ ਨਹੀਂ ਹੈ। MCP ਕਲਾਇੰਟ ਜਦੋਂ ਟੂਲਸ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ ਤਾਂ `co-op-translator-mcp` ਨੂੰ `stdio` 'ਤੇ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ।

ਉਦਾਹਰਣ ਵਰਗੀ ਯੂਜ਼ਰ ਬੇਨਤੀਆਂ ਜੋ ਇੱਕ ਏਜੰਟ ਸੰਭਾਲ ਸਕਦਾ ਹੈ:

- "ਇਸ Markdown ਫਾਈਲ ਦਾ ਕੋਰੀਆਈ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ ਅਤੇ ਲਿੰਕਾਂ ਸਹੀ ਰੱਖੋ।"
- "ਅਜਿਹੀ Markdown ਫਾਈਲ ਨੂੰ ਏਜੰਟ-ਸਹਾਇਤ MCP ਵਰਕਫਲੋ ਨਾਲ ਕੋਰੀਆਈ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ, ਅਤੇ ਅਨੁਵਾਦਿਤ ਚੰਕਾਂ ਲਈ ਆਪਣਾ ਮਾਡਲ ਵਰਤੋਂ।"
- "ਇਸ ਨੋਟਬੁੱਕ ਨੂੰ ਕੋਰੀਆਈ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ, ਕੋਡ ਸੈੱਲਜ਼ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖੋ, ਅਤੇ ਨੋਟਬੁੱਕ ਨੂੰ ਦੁਬਾਰਾ ਬਣਾਉਣ ਲਈ Co-op Translator MCP ਵਰਤੋਂ।"
- "ਇਸ ਤਸਵੀਰ ਵਿੱਚ ਲਿਖੇ ਟੈਕਸਟ ਦਾ ਜਪਾਨੀ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ ਅਤੇ ਨਤੀਜਾ ਸੇਵ ਕਰੋ।"
- "ਰਿਪੋਜ਼ਿਟਰੀ ਅਨੁਵਾਦ ਦਾ ਡраи-ਰਨ ਕਰੋ ਸਪੇਨੀ ਵਿੱਚ ਅਤੇ ਮੈਨੂੰ ਦੱਸੋ ਕਿ ਕੀ ਬਦਲੇਗਾ।"
- "ਸਮੀਖਿਆ ਕਰੋ ਕਿ ਕੋਰੀਆਈ ਅਨੁਵਾਦ ਆਉਟਪੁੱਟ ਅਪ-ਟੂ-ਡੇਟ ਹੈ ਜਾਂ ਨਹੀਂ।"

Markdown ਅਤੇ ਨੋਟਬੁੱਕ ਲਈ, MCP ਦੋ ਮੋਡਾਂ ਵਿੱਚ ਕੰਮ ਕਰ ਸਕਦਾ ਹੈ:

| Mode | Use when | Main tools |
| --- | --- | --- |
| Agent-assisted | ਜਦੋਂ MCP ਹੋਸਟ ਏਜੰਟ अपने ਮਾਡਲ ਨਾਲ ਚੰਕਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੇ, ਬਿਨਾਂ Co-op Translator LLM ਪ੍ਰੋਵਾਇਡਰ ਕਰੈਡੈਂਸ਼ਲ ਦੇ। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | ਜਦੋਂ Co-op Translator ਸਿੱਧਾ Azure OpenAI ਜਾਂ OpenAI ਨੂੰ ਕਾਲ ਕਰੇ। | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown ਟੂਲ ਕਾਲ ਆਕਾਰ:

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

MCP ਇਮੇਜ ਟੂਲ ਕਾਲ ਆਕਾਰ:

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

MCP ਰਾਹੀਂ ਰਿਪੋਜ਼ਿਟਰੀ ਅਨੁਵਾਦ ਮੂਲ ਰੂਪ ਵਿੱਚ ਡਰਾਈ-ਰਨ ਹੁੰਦਾ ਹੈ:

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

ਉਪਯੋਗ ਲਈ ਢੁਕਵਾਂ:

- ਤੁਸੀਂ ਏਜੰਟ ਜਾਂ ਐਡੀਟਰ ਦੇ ਅੰਦਰ ਕੁਦਰਤੀ-ਭਾਸ਼ਾ ਅਨੁਵਾਦ ਵਰਕਫਲੋਜ਼ ਚਾਹੁੰਦੇ ਹੋ।
- ਤੁਸੀਂ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਚਾਹੁੰਦੇ ਹੋ ਜਿੱਥੇ ਹੋਸਟ ਏਜੰਟ ਮਾਡਲ ਤਿਆਰ ਕੀਤੇ ਚੰਕਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੇ।
- ਤੁਸੀਂ ਏਜੰਟ ਨੂੰ ਚੁਣੀ ਹੋਈ ਸਮੱਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰਵਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ ਬਜਾਏ ਪੂਰੀ ਰਿਪੋਜ਼ਿਟਰੀ ਦੇ।
- ਤੁਸੀਂ ਰਿਪੋਜ਼ਿਟਰੀ-ਵਿਆਪੀ ਲਿਖਾਈ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਮਨਜ਼ੂਰੀ ਕਦਮ ਚਾਹੁੰਦੇ ਹੋ।
- ਤੁਸੀਂ ਇੱਕ ਇੰਟਰਫੇਸ ਚਾਹੁੰਦੇ ਹੋ ਜੋ Markdown, ਨੋਟਬੁੱਕ, ਤਸਵੀਰ, ਸਮੀਖਿਆ, ਅਤੇ ਪاتھ-ਰਿ-ਰਾਈਟਿੰਗ ਟੂਲਜ਼ ਨੂੰ ਐਕਸਪੋਜ਼ ਕਰੇ।

## ਇਹ ਇਕੱਠੇ ਕਿਵੇਂ ਫਿੱਟ ਹੁੰਦੇ ਹਨ

CLI ਮਨੁੱਖਾਂ ਲਈ ਰਿਪੋਜ਼ਿਟਰੀਆਂ ਦਾ ਅਨੁਵਾਦ ਕਰਨ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਡਿਫੌਲਟ ਹੈ। Python API ਸਭ ਤੋਂ ਵਧੀਆ ਹੈ ਜਦੋਂ ਤੁਹਾਡਾ ਕੋਡ ਵਰਕਫਲੋ ਦਾ ਮਾਲਕ ਹੋਵੇ। MCP ਸਰਵਰ ਸਭ ਤੋਂ ਵਧੀਆ ਹੈ ਜਦੋਂ ਇੱਕ ਏਜੰਟ ਜਾਂ ਐਡੀਟਰ ਵਰਕਫਲੋ ਦਾ ਮਾਲਕ ਹੋਵੇ।

ਇਹ ਤਿੰਨੋ ਰਾਹ ਇਕੋ ਜਿਹੇ ਪਬਲਿਕ Co-op Translator API ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ ਤੁਸੀਂ CLI ਨਾਲ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ, ਬਾਅਦ ਵਿੱਚ Python ਨਾਲ ਆਟੋਮੇਟ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਜਦੋਂ ਤਾਹਾਨੂੰ ਏਜੰਟ-ਚਲਿਤ ਵਰਕਫਲੋਜ਼ ਦੀ ਲੋੜ ਹੋਵੇ ਤਾਂ MCP ਕਲਾਇੰਟਾਂ ਨੂੰ ਇਹੋ ਜਿਹੀਆਂ ਸਮਰੱਥਾਵਾਂ ਪ੍ਰਦਾਨ ਕਰ ਸਕਦੇ ਹੋ।