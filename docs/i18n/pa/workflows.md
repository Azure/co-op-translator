# ਆਪਣਾ ਵਰਕਫਲੋ ਚੁਣੋ

Co-op Translator ਨੂੰ ਤਿੰਨ ਢੰਗਾਂ ਨਾਲ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ: CLI, Python API, ਅਤੇ MCP ਸਰਵਰ. ਇਹ ਸਭ ਇਕੋ ਜਿਹੀਆਂ ਅਨੁਵਾਦ ਸਮਰੱਥਾਵਾਂ ਸਾਂਝਾ ਕਰਦੇ ਹਨ, ਪਰ ਹਰ ਇਕ ਵੱਖਰਾ ਵਰਕਫਲੋ ਲਈ موزون ਹੈ.

ਜਦੋਂ ਤੁਸੀਂ ਇਹ ਫੈਸਲਾ ਕਰ ਰਹੇ ਹੋ ਕਿ ਕਿੱਥੋਂ ਸ਼ੁਰੂ ਕਰਨਾ ਹੈ, ਤਾਂ ਇਸ ਪੰਨੇ ਦੀ ਵਰਤੋਂ ਕਰੋ।

**ਜੇ ਤੁਸੀਂ ਅਨੁਵਾਦ ਹੱਥੋਂ ਸੋਧਦੇ ਹੋ:** ਡਿਫੌਲਟ CLI ਅਤੇ Actions ਵਰਕਫਲੋ ਬਦਲੇ ਹੋਏ ਸਰੋਤ ਫਾਇਲਾਂ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਮੁੜਅਨੁਵਾਦ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ ਉਹ ਫਾਇਲਾਂ ਵਿੱਚ ਤੁਹਾਡੇ ਲਫ਼ਜ਼ ਓਵਰਰਾਈਟ ਹੋ ਸਕਦੇ ਹਨ। ਅਪਡੇਟ ਨੂੰ ਸਵੀਕਾਰ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ diff ਦੀ ਸਮੀਖਿਆ ਕਰੋ। Markdown ਬਲਾਕ-ਪੱਧਰੀ ਸਵੀਕ੍ਰਿਤ ਸੋਧਾਂ ਦੀ ਸੰਰੱਖਣਾ ਲਈ, ਵਿਕਲਪੀ [Python API ਅਨੁਵਾਦ ਸਥਿਤੀ ਪ੍ਰਦਾਤਾ](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) ਦੀ ਵਰਤੋਂ ਕਰੋ।

## ਤੁਰੰਤ ਫੈਸਲਾ

| ਜੇ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ... | ਵਰਤੋਂ | ਇਥੋਂ ਸ਼ੁਰੂ ਕਰੋ |
| --- | --- | --- |
| ਟਰਮੀਨਲ ਤੋਂ ਇੱਕ ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਅਨੁਵਾਦ ਜਾਂ ਸਮੀਖਿਆ ਕਰੋ | CLI | [CLI ਰੈਫਰੰਸ](cli.md) |
| Python ਸਕ੍ਰਿਪਟ, ਸਰਵਿਸ, ਨੋਟਬੁੱਕ, ਜਾਂ CI ਨੌਕਰੀ ਵਿੱਚ ਅਨੁਵਾਦ ਜੋੜੋ | Python API | [Python API](api.md) |
| ਕਿਸੇ ਏਜੰਟ, ਸੰਪਾਦਕ, ਜਾਂ MCP-ਸਮਰਥਿਤ ਕਲਾਇੰਟ ਨੂੰ ਤੁਹਾਡੇ ਲਈ ਸਮੱਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰਨ ਦਿਓ | MCP Server | [MCP Server](mcp.md) |
| ਇੱਕ Markdown ਦਸਤਾਵੇਜ਼, ਨੋਟਬੁੱਕ, ਜਾਂ ਚਿੱਤਰ ਅਨੁਵਾਦ ਕਰੋ ਜੋ ਤੁਹਾਡੀ ਐਪ ਪਹਿਲਾਂ ਲੋਡ ਕਰ ਚੁੱਕੀ ਹੈ | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| ਪੂਰੇ ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਅਨੁਵਾਦ ਸਧਾਰਨ ਆਉਟਪੁੱਟ ਫੋਲਡਰਾਂ ਅਤੇ ਮੈਟਾਡੇਟਾ ਨਾਲ ਕਰੋ | CLI or `run_translation` | [CLI ਰੈਫਰੰਸ](cli.md) or [Python API](api.md) |

## CLI ਦੀ ਵਰਤੋਂ ਕਰੋ ਜਦੋਂ

ਜਦੋਂ ਕੋਈ ਵਿਅਕਤੀ ਜਾਂ CI ਨੌਕਰੀ ਸ਼ੈਲ ਤੋਂ ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ ਚਲਾ ਰਹੀ ਹੋਵੇ ਤਾਂ CLI ਚੁਣੋ।

ਜਦੋਂ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ Co-op Translator ਪ੍ਰੋਜੈਕਟ ਫਾਇਲਾਂ ਖੋਜੇ, ਅਨੁਵਾਦਿਤ ਆਉਟਪੁੱਟ ਤਿਆਰ ਕਰੇ, ਪ੍ਰੋਜੈਕਟ ਲੇਆਉਟ ਸੰਭਾਲੇ, ਮੈਟਾਡੇਟਾ ਅਪਡੇਟ ਕਰੇ, ਅਤੇ ਸਮੀਖਿਆ ਕਮਾਂਡ ਚਲਾਏ, ਤਾਂ CLI ਸਭ ਤੋਂ ਸੀਧਾ ਰਸਤਾ ਹੈ।

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

ਇਹ ਉਦਾਹਰਨ Markdown ਅਤੇ ਨੋਟਬੁੱਕਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦੀ ਹੈ। `-img` ਨੂੰ ਸਿਰਫ਼ [Azure AI Vision](configuration.md#azure-ai-vision) ਨੂੰ ਕਨਫਿਗਰ ਕਰਨ ਤੋਂ ਬਾਅਦ ਸ਼ਾਮਲ ਕਰੋ। ਇੱਕ Markdown-ਕੇਵਲ ਪਹਿਲੀ ਚਲਾਉਣ ਲਈ, [ਤੁਹਾਡਾ ਪਹਿਲਾ ਅਨੁਵਾਦ](first-translation.md) ਦੀ ਪਾਲਣਾ ਕਰੋ।

ਚੰਗੇ ਉਪਯੋਗ:

- ਤੁਸੀਂ ਆਪਣੇ ਟਰਮੀਨਲ ਤੋਂ ਇੱਕ ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰ ਰਹੇ ਹੋ।
- ਤੁਸੀਂ CI ਜਾਂ ਰਿਲੀਜ਼ ਵਰਕਫਲੋਜ਼ ਲਈ ਦੁਹਰਾਅਯੋਗ ਕਮਾਂਡ ਚਾਹੁੰਦੇ ਹੋ।
- ਤੁਸੀਂ ਇਨਬਿਲਟ ਪ੍ਰੋਜੈਕਟ ਖੋਜ, ਆਉਟਪੁੱਟ ਪਾਥ, ਮੈਟਾਡੇਟਾ, ਸਫਾਈ, ਅਤੇ ਸਮੀਖਿਆ ਚਾਹੁੰਦੇ ਹੋ।
- Python ਕੋਡ ਲਿਖਣ ਦੀ ਥਾਂ ਤੁਸੀਂ ਕਮਾਂਡ ਇੰਟਰਫੇਸ ਨੂੰ ਤਰਜੀਹ ਦੇਂਦੇ ਹੋ।

## Python API ਦੀ ਵਰਤੋਂ ਕਰੋ ਜਦੋਂ

ਜਦੋਂ ਤੁਹਾਡਾ ਆਪਣਾ ਕੋਡ ਵਰਕਫਲੋ ਨੂੰ ਕੰਟਰੋਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੋਵੇ ਤਾਂ Python API ਚੁਣੋ।

API ਐਪਲੀਕੇਸ਼ਨ, ਆਟੋਮੇਸ਼ਨ ਸਕ੍ਰਿਪਟਾਂ, ਨੋਟਬੁੱਕ, ਸੇਵਾਵਾਂ, ਅਤੇ ਕਸਟਮ ਪਾਈਪਲਾਈਨਾਂ ਲਈ ਲਾਭਦਾਇਕ ਹੈ। ਇਹ ਤੁਹਾਨੂੰ ਵਿਅਕਤੀਗਤ ਫਾਇਲਾਂ ਲਈ ਨੀਵੀਂ ਪੱਧਰੀ ਸਮੱਗਰੀ ਅਨੁਵਾਦ API ਕਾਲ ਕਰਨ ਜਾਂ CLI ਦੁਆਰਾ ਵਰਤੀ ਜਾਂਦੀ ਇੱਕੋ ਹੀ ਰਿਪੋਜ਼ਟਰੀ-ਪੱਧਰੀ ਆਰਕੀਸਟ੍ਰੇਸ਼ਨ ਚਲਾਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ।

ਇੱਕ Markdown ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਕਰੋ ਅਤੇ ਫਿਰ ਇਹ ਫੈਸਲਾ ਕਰੋ ਕਿ ਕਿੱਥੇ ਸੇਵ ਕਰਨਾ ਹੈ:

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

Python ਤੋਂ ਇਕ ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ ਚਲਾਓ:

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

ਚੰਗੇ ਉਪਯੋਗ:

- ਤੁਹਾਡੀ ਐਪਲੀਕੇਸ਼ਨ ਪਹਿਲਾਂ ਹੀ ਫਾਇਲਾਂ, ਬਫਰ, ਨੋਟਬੁੱਕ, ਜਾਂ ਚਿੱਤਰ ਬਾਈਟ ਪੜ੍ਹਦੀ ਹੈ।
- ਤੁਹਾਨੂੰ ਕਸਟਮ ਵੈਲੀਡੇਸ਼ਨ, ਸਟੋਰੇਜ, ਲੌਗਿੰਗ, ਰੀਟ੍ਰਾਈਜ਼, ਜਾਂ ਮਨਜ਼ੂਰੀ ਫਲੋਜ਼ ਦੀ ਲੋੜ ਹੈ।
- ਤੁਸੀਂ ਪੂਰੀ ਰਿਪੋਜ਼ਟਰੀ ਪ੍ਰਕਿਰਿਆ ਕੀਤੇ ਬਿਨਾਂ ਇੱਕ ਦਸਤਾਵੇਜ਼, ਨੋਟਬੁੱਕ, ਜਾਂ ਚਿੱਤਰ ਦਾ ਅਨੁਵਾਦ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ।
- ਤੁਸੀਂ ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ ਚਾਹੁੰਦੇ ਹੋ, ਪਰ ਸ਼ੈਲ ਕਮਾਂਡ ਦੀ ਥਾਂ Python ਆਟੋਮੇਸ਼ਨ ਤੋਂ।

## MCP ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰੋ ਜਦੋਂ

ਜਦੋਂ ਇੱਕ ਏਜੰਟ, ਸੰਪਾਦਕ, ਜਾਂ MCP-ਸਮਰਥਿਤ ਕਲਾਇੰਟ ਨੂੰ Co-op Translator ਟੂਲ ਕਾਲ ਕਰਨੇ ਚਾਹੀਦੇ ਹਨ, ਤਦ MCP ਸਰਵਰ ਚੁਣੋ।

ਸਧਾਰਨ ਲੋਕਲ ਸੈਟਅੱਪ ਵਿੱਚ, ਯੂਜ਼ਰ ਹੱਥੋਂ ਸਰਵਰ ਨੂੰ ਚਲਾਉਂਦਾ ਨਹੀਂ ਰੱਖਦਾ। ਜਦੋਂ ਟੂਲਾਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ ਤਾਂ MCP ਕਲਾਇੰਟ `stdio` ਉਤੇ `co-op-translator-mcp` ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ।

ਉਦਾਹਰਨ ਵਜੋਂ ਯੂਜ਼ਰ ਦੀਆਂ ਉਹ ਬੇਨਤੀਆਂ ਜੋ ਏਜੰਟ ਸੰਭਾਲ ਸਕਦਾ ਹੈ:

- "ਇਸ Markdown ਫਾਇਲ ਦਾ ਕੋਰੀਅਨ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ ਅਤੇ ਲਿੰਕ ਸਹੀ ਰੱਖੋ।"
- "ਇਸ Markdown ਫਾਇਲ ਨੂੰ ਏਜੰਟ-ਸਹਾਇਤਾ MCP ਵਰਕਫਲੋ ਨਾਲ ਕੋਰੀਅਨ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ, ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਚੰਕਾਂ ਲਈ ਆਪਣੇ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ।"
- "ਇਸ ਨੋਟਬੁੱਕ ਨੂੰ ਕੋਰੀਅਨ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ, ਕੋਡ ਸੈੱਲਾਂ ਨੂੰ ਸੰਭਾਲੋ, ਅਤੇ ਨੋਟਬੁੱਕ ਨੂੰ ਦੁਬਾਰਾ ਬਣਾਉਣ ਲਈ Co-op Translator MCP ਦੀ ਵਰਤੋਂ ਕਰੋ।"
- "ਇਸ ਚਿੱਤਰ ਵਿੱਚ ਮੌਜੂਦ ਲਿਖਤ ਨੂੰ ਜਪਾਨੀ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ ਅਤੇ ਨਤੀਜੇ ਨੂੰ ਸੇਵ ਕਰੋ।"
- "ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ ਨੂੰ ਸਪੇਨੀ ਲਈ ਡ੍ਰਾਈ-ਰਨ ਕਰੋ ਅਤੇ ਦੱਸੋ ਕਿ ਕੀ ਬਦਲਵੇਗਾ।"
- "ਜਾਂਚੋ ਕਿ ਕੋਰੀਅਨ ਅਨੁਵਾਦ ਆਉਟਪੁੱਟ ਤਾਜ਼ਾ ਹੈ ਜਾਂ ਨਹੀਂ।"

Markdown ਅਤੇ ਨੋਟਬੁੱਕ ਲਈ, MCP ਦੋ ਢੰਗਾਂ ਵਿੱਚ ਕੰਮ ਕਰ ਸਕਦਾ ਹੈ:

| ਮੋਡ | ਵਰਤੋਂ ਜਦੋਂ | ਮੁੱਖ ਟੂਲ |
| --- | --- | --- |
| ਏਜੰਟ-ਸਹਾਇਤਾ | MCP ਹੋਸਟ ਏਜੰਟ ਨੂੰ ਆਪਣੇ ਮਾਡਲ ਨਾਲ ਚੰਕਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ, Co-op Translator LLM ਪ੍ਰਦਾਤਾ ਦੇ ਕ੍ਰੈਡੇਨਸ਼ੀਅਲਾਂ ਦੇ ਬਿਨਾਂ। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ਪ੍ਰਦਾਤਾ-ਅਧਾਰਿਤ | Co-op Translator ਨੂੰ Azure OpenAI, OpenAI, ਜਾਂ Anthropic ਨੂੰ ਸਿੱਧਾ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ। | `translate_markdown_content`, `translate_notebook_content` |

MCP ਪ੍ਰਦਾਤਾ-ਅਧਾਰਿਤ Markdown ਟੂਲ ਕਾਲ ਆਕਾਰ:

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

MCP ਚਿੱਤਰ ਟੂਲ ਕਾਲ ਆਕਾਰ:

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

ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ MCP ਰਾਹੀਂ ਡਿਫੌਲਟ ਤੌਰ 'ਤੇ ਡ੍ਰਾਈ-ਰਨ ਹੁੰਦਾ ਹੈ:

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

ਚੰਗੇ ਉਪਯੋਗ:

- ਤੁਸੀਂ ਇੱਕ ਏਜੰਟ ਜਾਂ ਸੰਪਾਦਕ ਦੇ ਅੰਦਰ ਕੁਦਰਤੀ-ਭਾਸ਼ਾ ਅਨੁਵਾਦ ਵਰਕਫਲੋ ਚਾਹੁੰਦੇ ਹੋ।
- ਤੁਸੀਂ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਚਾਹੁੰਦੇ ਹੋ ਜਿੱਥੇ ਹੋਸਟ ਏਜੰਟ ਮਾਡਲ ਤਿਆਰ ਕੀਤੇ ਚੰਕਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ।
- ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ ਏਜੰਟ ਪੂਰੇ ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਥਾਂ ਚੁਣੀ ਹੋਈ ਸਮੱਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰੇ।
- ਤੁਸੀਂ ਰਿਪੋਜ਼ਟਰੀ-ਵਿਆਪਕ ਲਿੱਖਣਾਂ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਮਨਜ਼ੂਰੀ ਕਦਮ ਚਾਹੁੰਦੇ ਹੋ।
- ਤੁਸੀਂ ਇੱਕ ਐਸਾ ਇੰਟਰਫੇਸ ਚਾਹੁੰਦੇ ਹੋ ਜੋ Markdown, ਨੋਟਬੁੱਕ, ਚਿੱਤਰ, ਸਮੀਖਿਆ, ਅਤੇ ਰਾਹ-ਪੁਨਰਲੇਖਣ ਟੂਲ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰੇ।

## ਇਹ ਇਕੱਠੇ ਕਿਵੇਂ ਮੇਲ ਖਾਂਦੇ ਹਨ

ਰਿਪੋਜ਼ਟਰੀਆਂ ਦਾ ਅਨੁਵਾਦ ਕਰਨ ਵਾਲੇ ਮਨੁੱਖਾਂ ਲਈ CLI ਸਭ ਤੋਂ ਵਧੀਆ ਡਿਫੌਲਟ ਹੈ। ਜਦੋਂ ਤੁਹਾਡੇ ਕੋਡ ਕੋਲ ਵਰਕਫਲੋ ਦੀ ਮਾਲਕੀ ਹੋਵੇ ਤਾਂ Python API ਸਭ ਤੋਂ ਵਧੀਆ ਹੈ। ਜਦੋਂ ਵਰਕਫਲੋ ਦੀ ਮਾਲਕੀ ਏਜੰਟ ਜਾਂ ਸੰਪਾਦਕ ਕੋਲ ਹੋਵੇ ਤਾਂ MCP ਸਰਵਰ ਸਭ ਤੋਂ ਵਧੀਆ ਹੈ।

ਤਿੰਨੋ ਰਾਹ ਇੱਕੋ ਜਿਹੀ ਪਬਲਿਕ Co-op Translator API ਵਰਤਦੇ ਹਨ, ਇਸ ਲਈ ਤੁਸੀਂ CLI ਨਾਲ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ, ਬਾਅਦ ਵਿੱਚ Python ਨਾਲ ਆਟੋਮੇਟ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਜਦੋਂ ਤੁਹਾਨੂੰ ਏਜੰਟ-ਚਲਾਏ ਜਾਣ ਵਾਲੇ ਵਰਕਫਲੋਜ਼ ਦੀ ਲੋੜ ਹੋਵੇ ਤਾਂ ਉਹੀ ਸਮਰੱਥਾਵਾਂ MCP ਕਲਾਇੰਟਾਂ ਨੂੰ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰ ਸਕਦੇ ਹੋ।