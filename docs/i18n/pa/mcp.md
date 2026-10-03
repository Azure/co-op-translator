# MCP ਸਰਵਰ

Co-op Translator ਵਿੱਚ ਏਜੰਟਾਂ, ਸੰਪਾਦਕਾਂ ਅਤੇ MCP-ਅਨੁਕੂਲ ਕਲਾਇੰਟਾਂ ਲਈ ਇੱਕ Model Context Protocol ਸਰਵਰ ਸ਼ਾਮਿਲ ਹੈ.

ਡਿਫਾਲਟ ਲੋਕਲ ਸੈਟਅਪ ਲਈ, ਯੂਜ਼ਰਾਂ ਨੂੰ ਹੱਥੋਂ ਵੱਖਰਾ ਸਰਵਰ ਚਲਾਈ ਰੱਖਣ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ। ਉਹ ਆਪਣੇ MCP ਕਲਾਇੰਟ ਨੂੰ ਸੰਰਚਿਤ ਕਰਦੇ ਹਨ, ਅਤੇ ਜਦੋਂ Co-op Translator ਟੂਲਾਂ ਦੀ ਲੋੜ ਪੈਂਦੀ ਹੈ ਤਾਂ ਕਲਾਇੰਟ `co-op-translator-mcp` ਨੂੰ ਆਪਣੇ ਆਪ `stdio` ਰਾਹੀਂ ਸ਼ੁਰੂ ਕਰ ਦਿੰਦਾ ਹੈ।

ਜੇ ਤੁਸੀਂ CLI, Python API, ਅਤੇ MCP ਦੇ ਵਿਚਕਾਰ ਫ਼ੈਸਲਾ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ [ਆਪਣਾ ਵਰਕਫਲੋ ਚੁਣੋ](workflows.md) ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ।

MCP ਦੀ ਵਰਤੋਂ ਕਰੋ ਜਦੋਂ ਕੋਈ ਏਜੰਟ ਜਾਂ ਐਡੀਟਰ Co-op Translator ਨੂੰ ਸਿੱਧਾ ਕਾਲ ਕਰੇ:

| ਯੂਜ਼ਰ ਦਾ ਟੀਚਾ | MCP ਟੂਲ |
| --- | --- |
| ਇੱਕ Markdown ਦਸਤਾਵੇਜ਼, ਨੋਟਬੁੱਕ, ਜਾਂ ਚਿੱਤਰ ਦਾ ਅਨੁਵਾਦ ਕਰੋ | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| ਹੋਸਟ ਏਜੰਟ ਮਾਡਲ ਨਾਲ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਸਮੱਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰੋ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ਆਊਟਪੁਟ ਪਾਥ ਚੁਣਨ ਤੋਂ ਬਾਅਦ ਅਨੁਵਾਦ ਕੀਤੇ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਲਿੰਕਾਂ ਨੂੰ ਮੁੜ ਲਿਖੋ | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI ਵਾਂਗ ਪੂਰੇ ਰਿਪੋਜਟਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰੋ | `run_translation`, `translate_project` |
| LLM ਕ੍ਰੈਡੈਂਸ਼ਲਾਂ ਬਿਨਾਂ ਅਨੁਵਾਦਿਤ ਆਉਟਪੁਟ ਦੀ ਸਮੀਖਿਆ ਕਰੋ | `run_review` |
| ਸਮਰੱਥਾਵਾਂ ਅਤੇ ਵਾਤਾਵਰਣ ਦੀ ਸਥਿਤੀ ਦੀ ਜਾਂਚ ਕਰੋ | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP ਸਰਵਰ ਉਹੀ ਜਨਤਕ Python API ਲਪੇਟਦਾ ਹੈ ਜੋ [Python API](api.md) ਵਿੱਚ ਦਸਤਾਵੇਜ਼ਬੱਧ ਹੈ। Provider-backed ਟੂਲ CLI ਅਤੇ Python API ਨਾਲੋਂ ਹੀ ਸੰਰਚਿਤ ਪ੍ਰੋਵਾਈਡਰਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ। Agent-assisted ਟੂਲ MCP ਹੋਸਟ ਏਜੰਟ ਲਈ chunks ਤਿਆਰ ਕਰਦੇ ਹਨ ਤ ώστε ਉਹ ਅਨੁਵਾਦ ਕਰ ਸਕੇ, ਫਿਰ Co-op Translator ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਖਰੀ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਨੂੰ ਦੁਬਾਰਾ ਤਿਆਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

## ਕਦਮ 1: Co-op Translator ਨੂੰ ਇੰਸਟਾਲ ਅਤੇ ਸੰਰਚਿਤ ਕਰੋ

ਉਸ Python ਮਾਹੌਲ ਵਿੱਚ Co-op Translator ਇੰਸਟਾਲ ਕਰੋ ਜੋ ਤੁਹਾਡਾ MCP ਕਲਾਇੰਟ ਵਰਤੇਗਾ:

```bash
pip install co-op-translator
```

ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਤੋਂ ਲੋਕਲ ਵਿਕਾਸ ਲਈ, ਪੈਕੇਜ ਨੂੰ ਐਡਿਟੇਬਲ ਮੋਡ ਵਿੱਚ ਇੰਸਟਾਲ ਕਰੋ:

```bash
pip install -e .
```

ਆਪਣੇ MCP ਕਲਾਇੰਟ ਵੱਲੋਂ ਵਰਤੇ ਜਾਣ ਵਾਲੇ ਅਨੁਵਾਦ ਮੋਡ ਨੂੰ ਚੁਣੋ:

| ਮੋਡ | ਇਸਦਾ ਉਪਯੋਗ | ਕ੍ਰੈਡੈਂਸ਼ਲ |
| --- | --- | --- |
| Provider-backed | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ਜਾਂ `run_translation` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ। | ਅਨੁਵਾਦ ਲਈ Azure OpenAI, OpenAI, ਜਾਂ Anthropic ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ ਵੀ Azure AI Vision ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। |
| Agent-assisted | MCP ਹੋਸਟ ਏਜੰਟ ਉਹ chunks ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ ਜੋ `start_markdown_agent_translation` ਜਾਂ `start_notebook_agent_translation` ਵਾਪਸ ਕਰਦੇ ਹਨ। | Markdown ਜਾਂ ਨੋਟਬੁੱਕ chunks ਲਈ Co-op Translator LLM ਪ੍ਰੋਵਾਈਡਰ ਕ੍ਰੈਡੈਂਸ਼ਲ ਦੀ ਲੋੜ ਨਹੀਂ। ਚਿੱਤਰ ਅਨੁਵਾਦ ਹਜੇ agent-assisted ਮੋਡ ਵੱਲੋਂ ਕਵਰ ਨਹੀਂ ਕੀਤਾ ਗਿਆ। |

ਜੇ ਤੁਸੀਂ Codex ਜਾਂ Claude Code ਵਰਗੇ ਏਜੰਟ ਦੇ ਅੰਦਰ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਨਾਲ ਸ਼ੁਰੂ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ agent-assisted ਮੋਡ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ। ਜਦੋਂ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ Co-op Translator ਖ਼ੁਦ ਤੁਹਾਡੇ ਸੰਰਚਿਤ ਪ੍ਰੋਵਾਈਡਰਾਂ ਨੂੰ ਕਾਲ ਕਰੇ, ਜਾਂ ਜਦੋਂ ਤੁਸੀਂ ਇਮੇਜਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰ ਰਹੇ ਹੋ, ਜਾਂ CLI ਵਰਗਾ ਪ੍ਰੋਜੈਕਟ-ਸਤਰ ਅਨੁਵਾਦ ਚਲਾ ਰਹੇ ਹੋ, ਤਾਂ provider-backed ਮੋਡ ਦੀ ਵਰਤੋਂ ਕਰੋ।

Provider-backed ਵਰਕਫਲੋ ਲਈ ਇੱਕ ਪ੍ਰੋਵਾਈਡਰ ਸੰਰਚਿਤ ਕਰੋ:

```bash
# ਏਜ਼ਯੂਰ ਓਪਨ ਏਆਈ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# ਜਾਂ ਓਪਨ ਏਆਈ
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# ਜਾਂ ਐਂਥਰੋਪਿਕ
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Provider-backed ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ ਹੋਰ ਲੋੜ ਹੈ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode ਇਸ ਸਮੇਂ Markdown ਅਤੇ ਨੋਟਬੁੱਕ ਦੇ Markdown ਸੈੱਲਾਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ। ਚਿੱਤਰ ਅਨੁਵਾਦ ਅਜੇ ਵੀ provider-backed image pipeline ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਅਤੇ OCR ਅਤੇ ਲੇਆਉਟ-ਸਚੇਤ ਰੈਂਡਰਿੰਗ ਲਈ Azure AI Vision ਦੀ ਲੋੜ ਹੁੰਦੀ ہے۔

## ਕਦਮ 2: ਆਪਣੇ MCP ਕਲਾਇੰਟ ਨੂੰ ਸੰਰਚਿਤ ਕਰੋ

ਸਧਾਰਨ ਲੋਕਲ `stdio` ਸੈਟਅਪ ਲਈ, Co-op Translator ਨੂੰ ਆਪਣੇ MCP ਕਲਾਇੰਟ ਕੰਫਿਗਰੇਸ਼ਨ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ। ਕਲਾਇੰਟ ਇਸ ਪ੍ਰੋਸੈਸ ਨੂੰ ਆਪਣੇ ਆਪ ਸ਼ੁਰੂ ਅਤੇ ਰੋਕੇਗਾ।

ਇੰਸਟਾਲ ਕੀਤੇ ਪੈਕੇਜ ਦੀ ਸੰਰਚਨਾ:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Windows 'ਤੇ ਸੋਰਸ ਚੈਕਆਉਟ ਸੰਰਚਨਾ:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

macOS ਜਾਂ Linux 'ਤੇ ਸੋਰਸ ਚੈਕਆਉਟ ਸੰਰਚਨਾ:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

MCP ਕਲਾਇੰਟ ਕੰਫਿਗਰੇਸ਼ਨ ਬਦਲਣ ਤੋਂ ਬਾਅਦ, ਕਲਾਇੰਟ ਨੂੰ ਰਿਸਟਾਰਟ ਜਾਂ ਰੀਲੋਡ ਕਰੋ ਤਾਂ ਜੋ ਇਹ ਨਵੇਂ ਸਰਵਰ ਨੂੰ ਖੋਜ ਸਕੇ।

## ਕਦਮ 3: ਕਲਾਇੰਟ ਵਿੱਚ ਸਰਵਰ ਦੀ ਪੜਤਾਲ ਕਰੋ

ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਲਈ MCP ਕਲਾਇੰਟ ਨੂੰ ਕਹੋ, ਜਾਂ ਪਹਿਲਾਂ ਇਕ read-only ਹੈਲਪਰ ਕਾਲ ਕਰੋ:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

ਸ਼ੁਰੂਆਤੀ ਲਾਭਦਾਇਕ ਜਾਂਚਾਂ:

| ਟੂਲ | ਕੀ ਜਾਂਚਣਾ ਹੈ |
| --- | --- |
| `get_api_overview` | ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ ਕਿ ਸਰਵਰ ਪਹੁੰਚਯੋਗ ਹੈ ਅਤੇ ਉਪਲਬਧ ਵਰਕਫਲੋ ਦਿਖਾਉਂਦਾ ਹੈ। |
| `list_supported_languages` | ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ ਕਿ ਪੈਕੇਜ ਕੀਤੇ ਭਾਸ਼ਾ ਡਾਟਾ ਨੂੰ ਲੋਡ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। |
| `get_configuration_status` | ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ ਕਿ LLM ਅਤੇ Vision ਪ੍ਰੋਵਾਈਡਰ ਉਪਲਬਧ ਹਨ ਬਿਨਾਂ ਗੁਪਤ ਮੁੱਲਾਂ ਨੂੰ ਪ੍ਰਗਟ ਕੀਤੇ। |

## ਕਦਮ 4: ਇੱਕ ਵਰਕਫਲੋ ਚੁਣੋ

### ਵੱਖ-ਵੱਖ ਫਾਇਲਾਂ ਜਾਂ ਦਸਤਾਵੇਜ਼ਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ

ਜਦ MCP ਕਲਾਇੰਟ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਦਸਤਾਵੇਜ਼ ਸਮੱਗਰੀ ਜਾਂ ਚਿੱਤਰ ਪਾਥ ਹੋਵੇ ਅਤੇ Co-op Translator ਨੂੰ ਸੰਰਚਿਤ ਪ੍ਰੋਵਾਈਡਰਾਂ ਨੂੰ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੋਵੇ, ਤਾਂ provider-backed ਸਮੱਗਰੀ ਟੂਲ ਵਰਤੋ।

Markdown ਲਈ:

1. `document`, `language_code`, ਅਤੇ ਵਿਕਲਪਕ `source_path` ਨਾਲ `translate_markdown_content` ਕਾਲ ਕਰੋ।
2. ਜੇ ਅਨੁਵਾਦਿਤ ਨਤੀਜਾ Co-op Translator ਆਊਟਪੁੱਟ ਲੇਆਉਟ ਵਿੱਚ ਲਿਖਿਆ ਜਾਣਾ ਹੈ, ਤਾਂ `rewrite_markdown_paths` ਕਾਲ ਕਰੋ।
3. ਕਲਾਇੰਟ ਨੂੰ ਆਖਰੀ `content` ਲਿਖਣ ਜਾਂ ਵਾਪਸ ਕਰਨ ਦਿਓ।

ਨੋਟਬੁੱਕ ਲਈ:

1. ਨੋਟਬੁੱਕ JSON ਅਤੇ `language_code` ਨਾਲ `translate_notebook_content` ਕਾਲ ਕਰੋ।
2. ਜੇ ਅਨੁਵਾਦਿਤ ਨੋਟਬੁੱਕ ਲਿੰਕਾਂ ਨੂੰ ਟਾਰਗੇਟ ਪਾਥ ਲਈ ਢਾਲਨਾ ਪੈਣਾ ਹੋਵੇ ਤਾਂ `rewrite_notebook_paths` ਕਾਲ ਕਰੋ।
3. ਆਖਰੀ ਨੋਟਬੁੱਕ JSON ਲਿਖੋ ਜਾਂ ਵਾਪਸ ਕਰੋ।

ਚਿੱਤਰਾਂ ਲਈ:

1. `image_path`, `language_code`, ਅਤੇ ਵਿਕਲਪਕ `root_dir` ਜਾਂ `fast_mode` ਨਾਲ `translate_image_content` ਕਾਲ ਕਰੋ।
2. ਵਾਪਸ ਆਏ `data_base64` ਅਤੇ `mime_type` ਨੂੰ ਪੜ੍ਹੋ।
3. ਜੇ `output_path` ਦਿੱਤਾ ਗਿਆ ਹੈ, ਤਾਂ ਅਨੁਵਾਦਿਤ ਚਿੱਤਰ ਉਸ ਪਾਥ 'ਤੇ ਵੀ ਸੇਵ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

ਸਮੱਗਰੀ ਟੂਲ ਪ੍ਰੋਜੈਕਟ ਦੀ ਖੋਜ, ਮੈਟਾ ਡਾਟਾ ਅੱਪਡੇਟ, ਡਿਸਕਲੈਮਰ, ਜਾਂ ਆਟੋਮੈਟਿਕ ਪਾਥ ਰੀਰਾਈਟ ਨਹੀਂ ਕਰਦੇ। ਜੇ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ ਹੋਸਟ ਏਜੰਟ Co-op Translator LLM ਪ੍ਰੋਵਾਈਡਰ ਕ੍ਰੈਡੈਂਸ਼ਲਾਂ ਬਿਨਾਂ Markdown ਜਾਂ ਨੋਟਬੁੱਕ chunks ਦਾ ਅਨੁਵਾਦ ਕਰੇ, ਤਾਂ ਹੇਠਾਂ ਦਿੱਤੇ agent-assisted ਵਰਕਫਲੋ ਦੀ ਵਰਤੋਂ ਕਰੋ।

### ਹੋਸਟ ਏਜੰਟ ਮਾਡਲ ਨਾਲ ਅਨੁਵਾਦ ਕਰੋ

ਜਦੋਂ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ MCP ਹੋਸਟ ਏਜੰਟ, ਜਿਵੇਂ ਕਿ ਇੱਕ ਕੋਡਿੰਗ ਸਹਾਇਕ, Co-op Translator ਲਈ LLM ਪ੍ਰੋਵਾਈਡਰ ਸੈਟ ਕਰਨ ਦੀ ਬਜਾਏ ਅਨੁਵਾਦ ਕੀਤਾ ਟੈਕਸਟ ਤਿਆਰ ਕਰੇ, ਤਾਂ agent-assisted ਟੂਲ ਵਰਤੋ।

ਇੱਕ ਚੈਟ-ਆਧਾਰਿਤ MCP ਕਲਾਇੰਟ ਵਿੱਚ, ਆਮ ਤੌਰ 'ਤੇ ਤੁਹਾਨੂੰ ਖੁਦ ਟੂਲ JSON ਲਿਖਣ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ। ਏਜੰਟ ਨੂੰ agent-assisted ਵਰਕਫਲੋ ਵਰਤਣ ਲਈ ਕਹੋ:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

ਨੋਟਬੁੱਕ ਲਈ, ਇੱਕੋ ਹੀ ਪੈਟਰਨ ਵਰਤੋਂ:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

ਜੇ ਤੁਹਾਡਾ MCP ਕਲਾਇੰਟ ਸਰਵਰ ਪ੍ਰੋਂਪਟਾਂ ਨੂੰ ਸਹਿਯੋਗ ਕਰਦਾ ਹੈ, ਤਾਂ `agent_assisted_markdown_translation_prompt` ਵਰਤ ਕੇ ਕਲਾਇੰਟ ਨੂੰ ਇਕੋ ਵਰਕਫਲੋ ਨਿਰਦੇਸ਼ ਲੋਡ ਕਰਨ ਲਈ ਕਹੋ।

Markdown ਲਈ:

1. `document`, `language_code`, ਅਤੇ ਵਿਕਲਪਕ `source_path` ਨਾਲ `start_markdown_agent_translation` ਕਾਲ ਕਰੋ।
2. ਹੋਸਟ ਏਜੰਟ ਵਿੱਚ chunk `prompt` ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹੋਏ ਹਰ ਵਾਪਸ ਆਏ chunk ਦਾ ਅਨੁਵਾਦ ਕਰੋ।
3. ਮੂਲ `job` ਅਤੇ ਅਨੁਵਾਦਿਤ chunks ਨੂੰ `chunk_id` ਅਤੇ `translated_text` ਦੀ ਵਰਤੋਂ ਕਰਕੇ `finish_markdown_agent_translation` ਨਾਲ ਪੂਰਾ ਕਰੋ।
4. ਜੇ ਸਮੱਗਰੀ ਨੂੰ ਅਨੁਵਾਦਿਤ ਟਾਰਗੇਟ ਪਾਥ 'ਤੇ ਲਿਖਿਆ ਜਾਣਾ ਹੈ, ਤਾਂ `rewrite_markdown_paths` ਕਾਲ ਕਰੋ।

ਨੋਟਬੁੱਕ ਲਈ:

1. ਨੋਟਬੁੱਕ JSON ਅਤੇ `language_code` ਨਾਲ `start_notebook_agent_translation` ਕਾਲ ਕਰੋ।
2. ਹੋਸਟ ਏਜੰਟ ਵਿੱਚ ਹਰ ਵਾਪਸ ਆਏ chunk ਦਾ ਅਨੁਵਾਦ ਕਰੋ।
3. ਮੂਲ `job` ਅਤੇ ਅਨੁਵਾਦਿਤ chunks ਦੇ ਨਾਲ `finish_notebook_agent_translation` ਕਾਲ ਕਰੋ।
4. ਜੇ ਅਨੁਵਾਦਿਤ ਨੋਟਬੁੱਕ ਲਿੰਕਾਂ ਨੂੰ ਟਾਰਗੇਟ-ਪਾਥ ਅਨੁਕੂਲਤਾ ਦੀ ਲੋੜ ਹੋਵੇ ਤਾਂ `rewrite_notebook_paths` ਕਾਲ ਕਰੋ।

Agent-assisted ਟੂਲ Co-op Translator ਤੋਂ ਸੰਰਚਿਤ LLM ਪ੍ਰੋਵਾਈਡਰ ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦੇ। ਵਾਪਸ ਕੀਤੇ chunks ਦਾ ਅਨੁਵਾਦ ਕਰਨ ਦੀ ਜ਼ਿੰਮੇਵਾਰੀ ਹੋਸਟ ਏਜੰਟ ਦੀ ਹੁੰਦੀ ਹੈ। Co-op Translator Markdown chunking, placeholder ਸੰਰਕਸ਼ਣ, frontmatter ਮੁੜ-ਨਿਰਮਾਣ, ਨੋਟਬੁੱਕ ਸੈੱਲ ਰੀਪਲੇਸਮੈਂਟ, ਅਤੇ ਅਨੁਵਾਦ-ਬਾਦ ਨਾਰਮਲਾਈਜ਼ੇਸ਼ਨ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ।

### ਪੂਰੇ ਰਿਪੋਜਟਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰੋ

ਜਦੋਂ ਯੂਜ਼ਰ ਚਾਹੁੰਦਾ ਹੈ ਕਿ Co-op Translator `translate` CLI ਦੀ ਤਰ੍ਹਾਂ ਵਰਤਿਆ ਜਾਵੇ, ਤਾਂ `run_translation` ਦੀ ਵਰਤੋਂ ਕਰੋ।

ਰਿਪੋਜਟਰੀ ਅਨੁਵਾਦ ਦਾ ਡਿਫਾਲਟ `dry_run=true` ਹੁੰਦਾ ਹੈ ਤਾਂ ਜੋ ਏਜੰਟ ਫਾਇਲਾਂ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਤੋਂ ਪਹਿਲਾਂ ਸਕੋਪ ਦੀ ਜਾਂਚ ਕਰ ਸਕੇ:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

The `run_translation` result includes an `events` array with versioned
`co-op.translation.event.v1` progress events. MCP clients should use fields such
as `type`, `stage_key`, `completed`, `total`, and `current_path` instead of
parsing captured console text. Pass `json_events_path` to also write those events
to an NDJSON file.

ਲਿਖਤਾਂ ਦੀ ਆਗਿਆ ਦੇਣ ਲਈ, ਕੌਲਰ ਨੇ ਦੋਵੇਂ `dry_run=false` ਅਤੇ `confirm_write=true` ਸੈੱਟ ਕਰਨੇ ਲਾਜ਼ਮੀ ਹਨ:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ਨੂੰ `run_translation` ਲਈ ਕਮਪੈਟੀਬਿਲਟੀ ਅਲਿਆਸ ਵਜੋਂ ਦਰਸਾਇਆ ਗਿਆ ਹੈ।

### ਅਨੁਵਾਦਿਤ ਆਉਟਪੁਟ ਦੀ ਸਮੀਖਿਆ ਕਰੋ

ਉਹ deterministic ਜਾਂਚਾਂ ਲਈ `run_review` ਦੀ ਵਰਤੋਂ ਕਰੋ ਜਿਹਨ ਲਈ LLM ਜਾਂ Vision ਕ੍ਰੈਡੈਂਸ਼ਲ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ:

!!! note "ਬੀਟਾ"
    MCP ਬੀਟਾ `run_review` API ਤੱਕ ਪਹੁੰਚ ਦਿੰਦਾ ਹੈ. ਇਹ ਪੜ੍ਹਨ-ਕੇਵਲ ਸਮੀਖਿਆ ਵਰਕਫਲੋਜ਼ ਲਈ ਸੁਰੱਖਿਅਤ ਹੈ, ਪਰ ਸਮੀਖਿਆ ਜਾਂਚਾਂ ਅਤੇ ਇਸ਼ੂ ਸਕੀਮਾਂ ਵਿਕਸਿਤ ਹੋ ਸਕਦੀਆਂ ਹਨ.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

ਨਤੀਜੇ ਵਿੱਚ ਜਦ ਉਪਲਬਧ ਹੋਵੇ ਤਾਂ ਕੈਪਚਰ ਕੀਤੇ ਟੈਕਸਟ ਆਉਟਪੁੱਟ ਅਤੇ ਇੱਕ ਸੰਰਚਿਤ ਰੀਵਿਊ ਸੰਖੇਪ ਸ਼ਾਮਿਲ ਹੁੰਦਾ ਹੈ।

## ਮੈਨੂਅਲ ਸਰਵਰ ਰਨ

ਮੈਨੂਅਲ ਰਨ ਮੁੱਖਤੌਰ 'ਤੇ ਡੀਬੱਗਿੰਗ ਲਈ ਜਾਂ ਉਹਨਾਂ ਟਰਾਂਸਪੋਰਟਾਂ ਲਈ ਹੁੰਦੇ ਹਨ ਜੋ ਲੰਬੇ ਸਮੇਂ ਚੱਲਣ ਵਾਲੇ ਸਰਵਰਾਂ ਵਾਂਗ ਵਰਤਦੇ ਹਨ।

ਡਿਫਾਲਟ stdio ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰੋ:

```bash
co-op-translator-mcp
```

ਸੋਰਸ ਚੈਕਆਉਟ ਤੋਂ ਚਲਾਓ:

```bash
python -m co_op_translator.mcp.server
```

ਲੰਬੇ ਸਮੇਂ ਚੱਲਣ ਵਾਲਾ HTTP ਜਾਂ SSE ਸਰਵਰ ਚਲਾਓ:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

ਲੋਕਲ ਐਡੀਟਰ ਅਤੇ ਏਜੰਟ ਇੰਟੇਗਰੇਸ਼ਨਾਂ ਲਈ, ਕਦਮ 2 ਵਿੱਚ ਦਿੱਤੀ client-managed `stdio` ਸੰਰਚਨਾ ਨੂੰ ਤਰਜੀਹ ਦਿਓ।

## ਟੂਲ

| ਟੂਲ | ਉਦੇਸ਼ | ਫਾਈਲਾਂ ਲਿਖਦਾ ਹੈ |
| --- | --- | --- |
| `translate_markdown_content` | ਇੱਕ Markdown ਸਟਰਿੰਗ ਦਾ ਅਨੁਵਾਦ ਕਰੋ। | ਨਹੀਂ |
| `translate_notebook_content` | ਨੋਟਬੁੱਕ JSON ਵਿੱਚ Markdown ਸੈੱਲਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ। | ਨਹੀਂ |
| `translate_image_content` | ਇੱਕ ਚਿੱਤਰ ਵਿੱਚਲੇ ਟੈਕਸਟ ਦਾ ਅਨੁਵਾਦ ਕਰੋ ਅਤੇ base64 ਚਿੱਤਰ ਡੇਟਾ ਵਾਪਸ ਕਰੋ। | ਵਿਕਲਪਕ, ਸਿਰਫ ਜਦੋਂ `output_path` ਦਿੱਤਾ ਗਿਆ ਹੋਵੇ |
| `start_markdown_agent_translation` | ਹੋਸਟ ਏਜੰਟ ਲਈ Markdown chunks ਤਿਆਰ ਕਰੋ ਬਿਨਾਂ Co-op Translator LLM ਕ੍ਰੈਡੈਂਸ਼ਲਾਂ। | ਨਹੀਂ |
| `finish_markdown_agent_translation` | ਹੋਸਟ-ਏਜੰਟ ਅਨੁਵਾਦਿਤ chunks ਤੋਂ Markdown ਨੂੰ ਮੁੜ-ਤਿਆਰ ਕਰੋ। | ਨਹੀਂ |
| `start_notebook_agent_translation` | ਹੋਸਟ ਏਜੰਟ ਲਈ ਨੋਟਬੁੱਕ Markdown-ਸੈੱਲ chunks ਤਿਆਰ ਕਰੋ। | ਨਹੀਂ |
| `finish_notebook_agent_translation` | ਹੋਸਟ-ਏਜੰਟ ਅਨੁਵਾਦਿਤ chunks ਤੋਂ ਨੋਟਬੁੱਕ JSON ਮੁੜ-ਤਿਆਰ ਕਰੋ। | ਨਹੀਂ |
| `rewrite_markdown_paths` | ਅਨੁਵਾਦਿਤ ਟਾਰਗੇਟ ਲਈ Markdown ਬਾਡੀ ਅਤੇ frontmatter ਪਾਥਾਂ ਨੂੰ ਮੁੜ-ਲਿਖੋ। | ਨਹੀਂ |
| `rewrite_notebook_paths` | ਨੋਟਬੁੱਕ Markdown ਸੈੱਲਾਂ ਦੇ ਅੰਦਰ ਪਾਥਾਂ ਨੂੰ ਮੁੜ-ਲਿਖੋ। | ਨਹੀਂ |
| `run_translation` | CLI ਵਾਂਗ ਪ੍ਰੋਜੈਕਟ-ਸਤਰ ਅਨੁਵਾਦ ਚਲਾਓ। | ਹਾਂ ਜਦ `dry_run=false` ਅਤੇ `confirm_write=true` |
| `translate_project` | `run_translation` ਲਈ compatibility alias। | ਹਾਂ ਜਦ `dry_run=false` ਅਤੇ `confirm_write=true` |
| `run_review` | deterministic ਰੀਵਿਊ ਜਾਂਚਾਂ ਚਲਾਓ। | ਨਹੀਂ |
| `get_configuration_status` | ਸੰਰਚਿਤ LLM ਅਤੇ Vision ਪ੍ਰੋਵਾਈਡਰਾਂ ਦੀ ਰਿਪੋਰਟ ਕਰੋ ਬਿਨਾਂ ਸੀਕ੍ਰੇਟ ਵੈਲਿਊਜ਼ ਨੂੰ ਪ੍ਰਗਟ ਕੀਤੇ। | ਨਹੀਂ |
| `list_supported_languages` | ਸਮਰਥਿਤ ਟਾਰਗੇਟ ਭਾਸ਼ਾ ਕੋਡਾਂ ਦੀ ਸੂਚੀ ਦਿਖਾਓ। | ਨਹੀਂ |
| `get_api_overview` | ਉਪਲਬਧ MCP ਵਰਕਫਲੋ ਅਤੇ ਟੂਲਾਂ ਦਾ ਵਰਣਨ ਕਰੋ। | ਨਹੀਂ |

## ਸਰੋਤ

| ਰਿਸੋਰਸ URI | ਉਦੇਸ਼ |
| --- | --- |
| `co-op://api` | ਵਰਕਫਲੋ ਅਤੇ ਟੂਲਾਂ ਦਾ JSON ਓਵਰਵਿਊ। |
| `co-op://supported-languages` | ਸਮਰਥਿਤ ਭਾਸ਼ਾ ਕੋਡਾਂ ਦੀ JSON ਸੂਚੀ। |
| `co-op://configuration` | ਸੀਕ੍ਰੇਟਾਂ ਦੇ ਬਿਨਾਂ ਪ੍ਰੋਵਾਈਡਰ ਉਪਲਬਧਤਾ ਦਾ JSON ਸਾਰਾਂਸ਼। |

## ਪ੍ਰੋਂਪਟ

| ਪ੍ਰੋਂਪਟ | ਉਦੇਸ਼ |
| --- | --- |
| `translate_markdown_document_prompt` | ਸਮੱਗਰੀ ਅਨੁਵਾਦ ਅਤੇ ਵਿਕਲਪਿਕ ਪਾਥ ਮੁੜ-ਲਿਖਣ ਵਿੱਚ MCP ਕਲਾਇੰਟ ਦੀ ਮਦਦ ਕਰਦਾ ਹੈ। |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM ਪ੍ਰੋਵਾਈਡਰ ਕ੍ਰੈਡੈਂਸ਼ਲਾਂ ਬਿਨਾਂ ਹੋਸਟ-ਏਜੰਟ Markdown ਅਨੁਵਾਦ ਵਿੱਚ MCP ਕਲਾਇੰਟ ਨੂੰ ਮਾਰਗਦਰਸ਼ਨ ਕਰਦਾ ਹੈ। |
| `translate_repository_prompt` | dry-run-ਪਹਿਲਾਂ ਰਿਪੋਜਟਰੀ ਅਨੁਵਾਦ ਲਈ MCP ਕਲਾਇੰਟ ਨੂੰ ਮਾਰਗਦਰਸ਼ਨ ਕਰਦਾ ਹੈ। |

## ਕਾਪੀ-ਪੇਸਟ ਉਦਾਹਰਨਾਂ

Markdown ਸਮੱਗਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰੋ:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

ਅਨੁਵਾਦਿਤ Markdown ਲਿੰਕ ਮੁੜ-ਲਿਖੋ:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

ਹੋਸਟ ਏਜੰਟ ਮਾਡਲ ਨਾਲ Markdown ਦਾ ਅਨੁਵਾਦ ਕਰੋ:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

ਜਦੋਂ ਹੋਸਟ ਏਜੰਟ ਹਰ ਵਾਪਸ ਆਏ chunk ਦਾ ਅਨੁਵਾਦ ਕਰ ਲੈਂਦਾ ਹੈ, ਤਾਂ `start_markdown_agent_translation` ਵੱਲੋਂ ਵਾਪਸ ਕੀਤੇ ਪੂਰੇ `job` ਆਬਜੈਕਟ ਨਾਲ ਕੰਮ ਨੂੰ ਪੂਰਾ ਕਰੋ:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

ਰਿਪੋਜਟਰੀ ਅਨੁਵਾਦ ਦਾ ਪ੍ਰੀਵਿਊ:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## ਸਮੱਸਿਆ-ਨਿਵਾਰਨ

| ਸਮੱਸਿਆ | ਕੀ ਕੋਸ਼ਿਸ਼ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ |
| --- | --- |
| MCP ਕਲਾਇੰਟ `co-op-translator-mcp` ਨਹੀਂ ਲੱਭ ਸਕਦਾ. | ਪੂਰਾ Python executable ਪਾਥ ਵਰਤੋ ਅਤੇ `["-m", "co_op_translator.mcp.server"]` ਸੋਰਸ ਚੈਕਆਉਟ ਸੰਰਚਨਾ ਦਾ ਪ੍ਰਯੋਗ ਕਰੋ। |
| ਸਰਵਰ ਲਿਸਟ ਕੀਤਾ ਗਿਆ ਹੈ ਪਰ ਅਨੁਵਾਦ ਫੇਲ ਹੋ ਰਿਹਾ ਹੈ। | `get_configuration_status` ਕਾਲ ਕਰੋ ਅਤੇ ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ ਇੱਕ LLM ਪ੍ਰੋਵਾਈਡਰ ਉਪਲਬਧ ਹੈ। |
| ਤੁਸੀਂ_PROVIDER ਕ੍ਰੈਡੈਂਸ਼ਲ ਬਿਨਾਂ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਚਾਹੁੰਦੇ ਹੋ। | `start_markdown_agent_translation` / `finish_markdown_agent_translation` ਜਾਂ ਨੋਟਬੁੱਕ ਸਮਕक्ष ਵਰਤੋਂ ਤਾਂ ਜੋ ਹੋਸਟ ਏਜੰਟ chunks ਦਾ ਅਨੁਵਾਦ ਕਰੇ। |
| ਚਿੱਤਰ ਅਨੁਵਾਦ ਫੇਲ ਹੋ ਰਿਹਾ ਹੈ। | ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ Azure AI Vision ਵੈਰੀਏਬਲ ਸੈਟ ਹਨ ਅਤੇ `get_configuration_status` ਕਾਲ ਕਰੋ। |
| ਰਿਪੋਜਟਰੀ ਅਨੁਵਾਦ ਫਾਈਲਾਂ ਨਹੀਂ ਲਿਖਦਾ। | ਸਿਰਫ਼ ਸਪਸ਼ਟ ਯੂਜ਼ਰ ਮਨਜ਼ੂਰੀ ਦੇ ਬਾਅਦ `dry_run=false` ਅਤੇ `confirm_write=true` ਸੈੱਟ ਕਰੋ। |
| ਕਲਾਇੰਟ ਕੰਫਿਗ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਪ੍ਰਗਟ ਨਹੀਂ ਹੁੰਦੀਆਂ। | MCP ਕਲਾਇੰਟ ਨੂੰ ਰਿਸਟਾਰਟ ਜਾਂ ਰੀਲੋਡ ਕਰੋ। |

## ਸੁਰੱਖਿਆ ਨੋਟਸ

- MCP ਟੂਲ ਕਾਲਾਂ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਦੁਆਰਾ ਮਾਡਲ-ਨਿਯੰਤ੍ਰਿਤ ਹੁੰਦੀਆਂ ਹਨ, ਇਸ ਲਈ רਿਪੋਜਟਰੀ ਅਨੁਵਾਦ ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ dry-run ਹੁੰਦਾ ਹੈ।
- ਪੂਰਾ ਰਿਪੋਜਟਰੀ ਅਨੁਵਾਦ ਕਈ ਫਾਈਲਾਂ ਬਣਾਉਂਦਾ, ਅੱਪਡੇਟ ਜਾਂ ਹਟਾ ਸਕਦਾ ਹੈ। `confirm_write=true` ਸੈੱਟ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਸਪਸ਼ਟ ਯੂਜ਼ਰ ਮਨਜ਼ੂਰੀ ਲੋੜੀਦੀ ਹੈ।
- configuration status ਟੂਲ ਕਦੇ ਵੀ API keys, endpoints, ਜਾਂ ਹੋਰ ਗੁਪਤ ਮੁੱਲ ਨਹੀਂ ਵਾਪਸ ਕਰਦਾ।
- ਚਿੱਤਰ ਅਨੁਵਾਦ base64 ਚਿੱਤਰ ਡੇਟਾ ਵਾਪਸ ਕਰਦਾ ਹੈ। ਵੱਡੇ ਚਿੱਤਰ ਵੱਡੇ ਟੂਲ ਰਿਸਪਾਂਸ ਪੈਦਾ ਕਰ ਸਕਦੇ ਹਨ।
- Agent-assisted ਟੂਲ ਸਰੋਤ chunks ਅਤੇ ਪ੍ਰੋਂਪਟਸ MCP ਹੋਸਟ ਨੂੰ ਵਾਪਸ ਕਰਦੇ ਹਨ। ਉਨ੍ਹਾਂ ਦੀ ਵਰਤੋਂ ਸਿਰਫ ਉਸ ਸਮੱਗਰੀ ਲਈ ਕਰੋ ਜਿਸਨੂੰ ਯੂਜ਼ਰ ਉਸ ਹੋਸਟ ਏਜੰਟ ਮਾਡਲ ਨੂੰ ਭੇਜਣ ਵਿੱਚ ਆਰਾਮਦਾਇਕ ਮਹਿਸੂਸ ਕਰਦਾ ਹੈ।