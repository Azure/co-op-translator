# MCP ਸਰਵਰ

Co-op Translator ਵਿੱਚ ਏਜੰਟਾਂ, ਐਡੀਟਰਾਂ, ਅਤੇ MCP-ਅਨੁਕੂਲ ਕਲਾਇੰਟਾਂ ਲਈ ਇੱਕ Model Context Protocol ਸਰਵਰ ਸ਼ਾਮِل ਹੈ।

ਡਿਫੌਲਟ ਲੋਕਲ ਸੈਟਅੱਪ ਲਈ, ਯੂਜ਼ਰ ਵਖ-ਵਖ ਸਰਵਰ ਹੱਥੋਂ ਨਹੀਂ ਚਲਾਉਂਦੇ। ਉਹ ਆਪਣੇ MCP ਕਲਾਇੰਟ ਨੂੰ ਸੰਰਚਿਤ ਕਰਦੇ ਹਨ, ਅਤੇ ਜਦੋਂ Co-op Translator ਟੂਲ ਦੀ ਲੋੜ ਪੈਂਦੀ ਹੈ ਤਾਂ ਕਲਾਇੰਟ `co-op-translator-mcp` ਨੂੰ `stdio` ਰਾਹੀਂ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ।

ਜੇ ਤੁਸੀਂ CLI, Python API, ਅਤੇ MCP ਵਿਚੋਂ ਚੋਣ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ [Choose Your Workflow](workflows.md) ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ।

ਜਦੋਂ ਕੋਈ ਏਜੰਟ ਜਾਂ ਐਡੀਟਰ Co-op Translator ਨੂੰ ਸਿੱਧਾ ਕਾਲ ਕਰਨਾ ਚਾਹੁੰਦਾ ਹੋਵੇ ਤਾਂ MCP ਵਰਤੋ:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP ਸਰਵਰ ਉਹੀ ਪਬਲਿਕ Python API ਰੈਪ ਕਰਦਾ ਹੈ ਜੋ [Python API](api.md) ਵਿੱਚ ਦਸਤਾਵੇਜ਼ ਕੀਤਾ ਗਿਆ ਹੈ। Provider-backed ਟੂਲ CLI ਅਤੇ Python API ਨਾਲ ਇੱਕੋ ਕਨਫਿਗਰ ਕੀਤੇ ਪ੍ਰੋਵਾਇਡਰ ਵਰਤਦੇ ਹਨ। ਏਜੰਟ-ਸਹਾਇਤ ਟੂਲ MCP ਹੋਸਟ ਏਜੰਟ ਲਈ chunks ਤਿਆਰ ਕਰਦੇ ਹਨ ਜੋ ਅਨੁਵਾਦ ਲਈ ਵਾਪਸ ਭੇਜੇ ਜਾਂਦੇ ਹਨ, ਫਿਰ Co-op Translator ਆਖਰੀ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਨੂੰ ਮੁੜ-ਬਨਾਉਂਦਾ ਹੈ।

## ਕਦਮ 1: Install and Configure Co-op Translator

ਉਸ Python ਵਾਤਾਵਰਣ ਵਿੱਚ Co-op Translator ਇੰਸਟਾਲ ਕਰੋ ਜੋ ਤੁਹਾਡੇ MCP ਕਲਾਇੰਟ ਦੁਆਰਾ ਵਰਤਿਆ ਜਾਵੇਗਾ:

```bash
pip install co-op-translator
```

ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਤੋਂ ਲੋਕਲ ਵਿਕਾਸ ਲਈ, ਪੈਕੇਜ ਨੂੰ editable ਮੋਡ ਵਿੱਚ ਇੰਸਟਾਲ ਕਰੋ:

```bash
pip install -e .
```

ਉਸ ਅਨੁਵਾਦ ਮੋਡ ਦੀ ਚੋਣ ਕਰੋ ਜੋ ਤੁਹਾਡਾ MCP ਕਲਾਇੰਟ ਵਰਤੇਗਾ:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown ਅਤੇ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਲਈ Azure OpenAI ਜਾਂ OpenAI ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ ਵੀ Azure AI Vision ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | Markdown ਜਾਂ ਨੋਟਬੁੱਕ chunks ਲਈ Co-op Translator LLM ਪ੍ਰੋਵਾਈਡਰ ਕ੍ਰੈਡੇੰਸ਼ਲ ਦੀ ਲੋੜ ਨਹੀਂ। Agent-assisted ਮੋਡ ਹਾਲੇ ਤੱਕ ਚਿੱਤਰ ਅਨੁਵਾਦ ਨੂੰ ਕਵਰ ਨਹੀਂ ਕਰਦਾ। |

ਜੇ ਤੁਸੀਂ Codex ਜਾਂ Claude Code ਵਰਗੇ ਏਜੰਟ ਦੇ ਅੰਦਰ Markdown ਜਾਂ ਨੋਟਬੁੱਕ ਅਨੁਵਾਦ ਨਾਲ ਸ਼ੁਰੂ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ agent-assisted ਮੋਡ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ। ਜਦੋਂ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ Co-op Translator ਆਪ ਹੀ ਤੁਹਾਡੇ ਕਨਫਿਗਰ ਕੀਤੇ ਪ੍ਰੋਵਾਈਡਰਾਂ ਨੂੰ ਕਾਲ ਕਰੇ, ਜਾਂ ਜਦੋਂ ਤੁਸੀਂ ਚਿੱਤਰ ਅਨੁਵਾਦ ਕਰ ਰਹੇ ਹੋ, ਜਾਂ ਜਦੋਂ ਤੁਸੀਂ CLI ਵਰਗਾ ਰਿਪੋਜ਼ਟਰੀ-ਸਤਹੀ ਅਨੁਵਾਦ ਚਲਾ ਰਹੇ ਹੋ ਤਾਂ provider-backed ਮੋਡ ਵਰਤੋ।

ਕੇਵਲ provider-backed ਵਰਕਫਲੋ ਲਈ ਪ੍ਰੋਵਾਈਡਰ ਕ੍ਰੈਡੇੰਸ਼ਲ ਸੰਰਚਿਤ ਕਰੋ:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Provider-backed ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ ਵਾਧੂ ਤੌਰ 'ਤੇ ਲੋੜ ਹੈ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## ਕਦਮ 2: Configure Your MCP Client

ਸਧਾਰਣ ਲੋਕਲ `stdio` ਸੈਟਅੱਪ ਲਈ, Co-op Translator ਨੂੰ ਆਪਣੇ MCP ਕਲਾਇੰਟ কਾਂਫਿਗਰੇਸ਼ਨ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰੋ। ਕਲਾਇੰਟ ਪ੍ਰੋਸੈਸ ਨੂੰ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਸ਼ੁਰੂ ਅਤੇ ਬੰਦ ਕਰੇਗਾ।

Installed package configuration:

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

Source checkout configuration on Windows:

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

Source checkout configuration on macOS or Linux:

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

MCP ਕਲਾਇੰਟ ਦੀ ਸੰਰਚਨਾ ਬਦਲਣ ਤੋਂ ਬਾਅਦ, ਕਲਾਇੰਟ ਨੂੰ ਰੀਸਟਾਰਟ ਜਾਂ ਰੀਲੋਡ ਕਰੋ ਤਾਂ ਜੋ ਉਹ ਨਵੇਂ ਸਰਵਰ ਨੂੰ ਖੋਜ ਸਕੇ।

## ਕਦਮ 3: Verify the Server in the Client

MCP ਕਲਾਇੰਟ ਨੂੰ ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਪੁੱਛੋ, ਜਾਂ ਪਹਿਲਾਂ ਪੜ੍ਹਨ-ਕੇਵਲ ਹੈਲਪਰਾ ਨੂੰ ਕਾਲ ਕਰੋ:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

ਲਾਭਕਾਰੀ ਪਹਿਲੀਆਂ ਜਾਂਚਾਂ:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ ਕਿ ਸਰਵਰ ਪਹੁੰਚਯੋਗ ਹੈ ਅਤੇ ਉਪਲਬਧ ਵਰਕਫਲੋ ਦਿਖਾਉਂਦਾ ਹੈ। |
| `list_supported_languages` | ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ ਕਿ ਪੈਕੇਜ ਕੀਤੀ ਭਾਸ਼ਾ ਡੇਟਾ ਲੋਡ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। |
| `get_configuration_status` | ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ ਕਿ LLM ਅਤੇ Vision ਪ੍ਰੋਵਾਇਡਰ ਉਪਲਬਧ ਹਨ ਬਿਨਾਂ ਗੁਪਤ ਮੁੱਲ ਖੁਲਾਸਾ ਕੀਤੇ। |

## ਕਦਮ 4: Choose a Workflow

### ਵਿਅਕਤੀਗਤ ਫਾਈਲਾਂ ਜਾਂ ਦਸਤਾਵੇਜ਼ ਅਨੁਵਾਦ ਕਰੋ

ਜਦੋਂ MCP ਕਲਾਇੰਟ ਕੋਲ ਦਸਤਾਵੇਜ਼ ਸਮੱਗਰੀ ਜਾਂ ਚਿੱਤਰ ਪਾਥ ਹੁੰਦਾ ਹੈ ਅਤੇ Co-op Translator ਨੂੰ ਕਨਫਿਗਰ ਕੀਤੇ ਪ੍ਰੋਵਾਈਡਰਾਂ ਨੂੰ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਤਾਂ provider-backed content ਟੂਲ ਵਰਤੋਂ ਕਰੋ।

Markdown ਲਈ:

1. `document`, `language_code`, ਅਤੇ ਵਿਕਲਪਿਕ ਤੌਰ 'ਤੇ `source_path` ਦੇ ਨਾਲ `translate_markdown_content` ਕਾਲ ਕਰੋ।
2. ਜੇ ਅਨੁਵਾਦ ਕੀਤਾ ਨਤੀਜਾ Co-op Translator ਆਊਟਪੁੱਟ ਲੇਆਉਟ ਵਿੱਚ ਲਿਖਿਆ ਜਾਣਾ ਹੈ, ਤਾਂ `rewrite_markdown_paths` ਕਾਲ ਕਰੋ।
3. ਕਲਾਇੰਟ ਨੂੰ ਆਖਰੀ `content` ਲਿਖਣ ਜਾਂ ਵਾਪਸ ਕਰਨ ਦਿਓ।

ਨੋਟਬੁੱਕ ਲਈ:

1. ਨੋਟਬੁੱਕ JSON ਅਤੇ `language_code` ਨਾਲ `translate_notebook_content` ਕਾਲ ਕਰੋ।
2. ਜੇ ਅਨੁਵਾਦ ਕੀਤੇ ਨੋਟਬੁੱਕ ਲਿੰਕਾਂ ਨੂੰ ਟਾਰਗੇਟ ਪਾਥ ਲਈ ਅਨੁਕੂਲ ਕਰਨ ਦੀ ਲੋੜ ਹੋਏ ਤਾਂ `rewrite_notebook_paths` ਕਾਲ ਕਰੋ।
3. ਆਖਰੀ ਨੋਟਬੁੱਕ JSON ਲਿਖੋ ਜਾਂ ਵਾਪਸ ਕਰੋ।

ਚਿੱਤਰਾਂ ਲਈ:

1. `image_path`, `language_code`, ਅਤੇ ਵਿਕਲਪਿਕ `root_dir` ਜਾਂ `fast_mode` ਦੇ ਨਾਲ `translate_image_content` ਕਾਲ ਕਰੋ।
2. ਵਾਪਸ ਆਏ `data_base64` ਅਤੇ `mime_type` ਨੂੰ ਪੜ੍ਹੋ।
3. ਜੇ `output_path` ਦਿੱਤਾ ਗਿਆ ਹੈ ਤਾਂ ਅਨੁਵਾਦ ਕੀਤਾ ਚਿੱਤਰ ਉਸ ਪਾਥ 'ਤੇ ਵੀ ਸੇਵ ਕੀਤਾ ਜਾਵੇਗਾ।

ਇਨ ਸਮੱਗਰੀ ਟੂਲਾਂ ਵਿੱਚ ਪ੍ਰੋਜੈਕਟ ਖੋਜ, ਮੈਟਾਡੇਟਾ ਅਪਡੇਟ, ਡਿਸਕਲੇਮਰ, ਜਾਂ ਆਟੋਮੈਟਿਕ ਪਾਥ ਮੁੜ-ਲਿਖਾਈ ਸ਼ਾਮِل ਨਹੀਂ ਹੁੰਦੀ। ਜੇ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ ਹੋਸਟ ਏਜੰਟ Co-op Translator LLM ਪ੍ਰੋਵਾਈਡਰ ਕ੍ਰੈਡੇੰਸ਼ਲਾਂ ਦੇ ਬਿਨਾਂ Markdown ਜਾਂ ਨੋਟਬੁੱਕ chunks ਦਾ ਅਨੁਵਾਦ ਕਰੇ, ਤਾਂ ਹੇਠਾਂ ਦਿੱਤਾ agent-assisted ਵਰਕਫਲੋ ਵਰਤੋਂ।

### ਹੋਸਟ ਏਜੰਟ ਮਾਡਲ ਨਾਲ ਅਨੁਵਾਦ ਕਰੋ

Agent-assisted ਟੂਲਾਂ ਵਰਤੋਂ ਜਦੋਂ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਕਿ MCP ਹੋਸਟ ਏਜੰਟ (ਉਦਾਹਰਣ ਲਈ ਕੋਡਿੰਗ ਸਹਾਇਕ) ਅਨੁਵਾਦ ਕਰੇ ਬਜਾਏ ਇਸਦੇ ਕਿ ਤੁਸੀਂ Co-op Translator ਲਈ Azure OpenAI ਜਾਂ OpenAI ਸੰਰਚਿਤ ਕਰੋ।

ਇੱਕ ਚੈਟ-ਆਧਾਰਿਤ MCP ਕਲਾਇੰਟ ਵਿੱਚ, ਆਮ ਤੌਰ 'ਤੇ ਤੁਹਾਨੂੰ ਖੁਦ ਟੂਲ JSON ਲਿਖਣ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ। ਏਜੰਟ ਨੂੰ agent-assisted ਵਰਕਫਲੋ ਵਰਤਣ ਲਈ ਕਹੋ:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

ਨੋਟਬੁੱਕਾਂ ਲਈ, ਇਸੇ ਪੈਟਰਨ ਦਾ ਉਪਯੋਗ ਕਰੋ:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

ਜੇ ਤੁਹਾਡਾ MCP ਕਲਾਇੰਟ ਸਰਵਰ ਪ੍ਰਾਂਪਟ ਨੂੰ ਸਪੋਰਟ ਕਰਦਾ ਹੈ, ਤਾਂ ਇੱਕੋ ਵਰਕਫਲੋ ਨਿਰਦੇਸ਼ ਲੋਡ ਕਰਨ ਲਈ `agent_assisted_markdown_translation_prompt` ਵਰਤੋ।

Markdown ਲਈ:

1. `document`, `language_code`, ਅਤੇ ਵਿਕਲਪਿਕ `source_path` ਦੇ ਨਾਲ `start_markdown_agent_translation` ਕਾਲ ਕਰੋ।
2. ਹੋਸਟ ਏਜੰਟ ਵਿੱਚ ਹਰ ਵਾਪਸ ਕੀਤੇ chunk ਨੂੰ chunk `prompt` ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਅਨੁਵਾਦ ਕਰੋ।
3. ਮੂਲ `job` ਅਤੇ `chunk_id` ਅਤੇ `translated_text` ਵਰਤ ਕੇ ਅਨੁਵਾਦ ਕੀਤੇ chunk ਭੇਜ ਕੇ `finish_markdown_agent_translation` ਕਾਲ ਕਰੋ।
4. ਜੇ ਸਮੱਗਰੀ ਨੂੰ ਕਿਸੇ ਅਨੁਵਾਦਿਤ ਟਾਰਗੇਟ ਪਾਥ 'ਤੇ ਲਿਖਿਆ ਜਾਣਾ ਹੈ ਤਾਂ `rewrite_markdown_paths` ਕਾਲ ਕਰੋ।

ਨੋਟਬੁੱਕ ਲਈ:

1. ਨੋਟਬੁੱਕ JSON ਅਤੇ `language_code` ਦੇ ਨਾਲ `start_notebook_agent_translation` ਕਾਲ ਕਰੋ।
2. ਹੋਸਟ ਏਜੰਟ ਵਿੱਚ ਹਰ ਵਾਪਸ ਕੀਤੇ chunk ਦਾ ਅਨੁਵਾਦ ਕਰੋ।
3. ਮੂਲ `job` ਅਤੇ ਅਨੁਵਾਦ ਕੀਤੇ chunks ਨਾਲ `finish_notebook_agent_translation` ਕਾਲ ਕਰੋ।
4. ਜੇ ਅਨੁਵਾਦ ਕੀਤੇ ਨੋਟਬੁੱਕ ਲਿੰਕ ਟਾਰਗੇਟ-ਪਾਥ ਲਈ ਅਨੁਕੂਲ ਕਰਨ ਦੀ ਲੋੜ ਹੋਏ ਤਾਂ `rewrite_notebook_paths` ਕਾਲ ਕਰੋ।

Agent-assisted ਟੂਲ Co-op Translator ਵੱਲੋਂ Azure OpenAI ਜਾਂ OpenAI ਨੂੰ ਕਾਲ ਨਹੀਂ ਕਰਦੇ। ਵਾਪਸ ਕੀਤੇ chunks ਦਾ ਅਨੁਵਾਦ ਕਰਨ ਦੀ ਜਿੰਮੇਵਾਰੀ ਹੋਸਟ ਏਜੰਟ ਦੀ ਹੁੰਦੀ ਹੈ। Co-op Translator Markdown chunking, placeholder preservation, frontmatter reconstruction, notebook cell replacement, ਅਤੇ post-translation normalization ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ।

### ਪੂਰੇ ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਅਨੁਵਾਦ ਕਰੋ

ਜਦੋਂ ਯੂਜ਼ਰ ਚਾਹੁੰਦਾ ਹੈ ਕਿ Co-op Translator CLI ਵਾਂਗ ਵਰਤੇ ਜਾਵੇ ਤਾਂ `run_translation` ਵਰਤੋਂ।

ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ ਡਿਫੌਲਟ ਤੌਰ 'ਤੇ `dry_run=true` ਹੁੰਦਾ ਹੈ ਤਾਂ ਕਿ ਏਜੰਟ ਫਾਈਲਾਂ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਸਕੋਪ ਦੀ ਜਾਂਚ ਕਰ ਸਕੇ:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

ਲਿਖਤਾਂ ਦੀ ਆਗਿਆ ਦੇਣ ਲਈ, ਕਾਲ ਕਰਨ ਵਾਲੇ ਨੂੰ ਦੋਹਾਂ `dry_run=false` ਅਤੇ `confirm_write=true` ਸੈੱਟ ਕਰਨੇ ਪੈਣਗੇ:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ਨੂੰ `run_translation` ਲਈ ਇੱਕ ਕੁੰਪੈਟਬਿਲਿਟੀ aliaਸ ਵਜੋਂ ਐਕਸਪੋਜ਼ ਕੀਤਾ ਗਿਆ ਹੈ।

### ਅਨੁਵਾਦਿਤ ਨਤੀਜੇ ਦੀ ਸਮੀਖਿਆ

ਉਹ deterministic ਚੈੱਕਾਂ ਲਈ `run_review` ਵਰਤੋਂ ਜੋ LLM ਜਾਂ Vision ਕ੍ਰੈਡੇੰਸ਼ਲ ਦੀ ਲੋੜ ਨਹੀਂ ਰੱਖਦੇ:

!!! note "Beta"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

ਨਤੀਜਾ ਵਿੱਚ ਕੈਪਚਰ ਕੀਤਾ ਟੈਕਸਟ ਆਉਟਪੁੱਟ ਅਤੇ ਜਦੋਂ ਉਪਲਬਧ ਹੋਵੇ ਇੱਕ ਸਰਚਿਤ ਸਮੀਖਿਆ ਸੰਖੇਪ ਸ਼ਾਮِل ਹੁੰਦਾ ਹੈ।

## ਮੈਨੂਅਲ ਸਰਵਰ ਚਲਾਉਣ

ਮੈਨੂਅਲ ਚਲਾਏ ਜਾਣ ਵਾਲੇ ਸਰਵਰ ਜ਼ਿਆਦਾ ਤਰ ਡਬੱਗਿੰਗ ਲਈ ਜਾਂ ਉਨ੍ਹਾਂ ਟਰਾਂਸਪੋਰਟਾਂ ਲਈ ਹੁੰਦੇ ਹਨ ਜੋ ਲੰਬੇ ਸਮੇਂ ਚੱਲ ਰਹੇ ਸਰਵਰ ਵਾਂਗ ਵਰਤਦੇ ਹਨ।

ਡਿਫੌਲਟ stdio ਸਰਵਰ ਡੀਬੱਗ ਕਰੋ:

```bash
co-op-translator-mcp
```

Source checkout ਤੋਂ ਚਲਾਓ:

```bash
python -m co_op_translator.mcp.server
```

ਲੰਬੇ ਸਮੇਂ ਚੱਲਣ ਵਾਲਾ HTTP ਜਾਂ SSE ਸਰਵਰ ਚਲਾਓ:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

ਲੋਕਲ ਐਡੀਟਰ ਅਤੇ ਏਜੰਟ ਇੰਟੀਗਰੇਸ਼ਨਾਂ ਲਈ, ਕਦਮ 2 ਵਿੱਚ ਦਿੱਤੀ ਗਈ client-managed `stdio` ਸੰਰਚਨਾ ਨੂੰ ਵੱਧ ਤਰਜ਼ੀਹ ਦਿਓ।

## ਟੂਲ

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | No |
| `translate_image_content` | Translate text in one image and return base64 image data. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Prepare Markdown chunks for the host agent to translate without Co-op Translator LLM credentials. | No |
| `finish_markdown_agent_translation` | Reconstruct Markdown from host-agent translated chunks. | No |
| `start_notebook_agent_translation` | Prepare notebook Markdown-cell chunks for the host agent to translate. | No |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON from host-agent translated chunks. | No |
| `rewrite_markdown_paths` | Rewrite Markdown body and frontmatter paths for a translated target. | No |
| `rewrite_notebook_paths` | Rewrite paths inside notebook Markdown cells. | No |
| `run_translation` | Run project-level translation like the CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Report configured LLM and Vision providers without exposing secrets. | No |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Describe available MCP workflows and tools. | No |

## ਸਰੋਤਰੋ

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | ਵਰਕਫਲੋ ਅਤੇ ਟੂਲਾਂ ਦਾ JSON ਓਵਰਵਿਊ। |
| `co-op://supported-languages` | ਸਮਰਥਿਤ ਭਾਸ਼ਾ ਕੋਡਾਂ ਦੀ JSON ਸੂਚੀ। |
| `co-op://configuration` | ਗੁਪਤ ਮੁੱਲਾਂ ਦੇ ਬਿਨਾਂ ਪ੍ਰੋਵਾਇਡਰ ਉਪਲਬਧਤਾ ਦਾ JSON ਸੰਖੇਪ। |

## ਪ੍ਰਾਂਪਟ

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | ਇੱਕ MCP ਕਲਾਇੰਟ ਨੂੰ ਸਮੱਗਰੀ ਅਨੁਵਾਦ ਅਤੇ ਵਿਕਲਪਿਕ ਪਾਥ ਮੁੜ-ਲਿਖਾਈ ਰਾਹੀਂ ਮਾਰਗਦਰਸ਼ਨ ਦਿਓ। |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM ਪ੍ਰੋਵਾਈਡਰ ਕ੍ਰੈਡੇੰਸ਼ਲਾਂ ਦੇ ਬਿਨਾਂ ਹੋਸਟ-ਏਜੰਟ Markdown ਅਨੁਵਾਦ ਲਈ MCP ਕਲਾਇੰਟ ਨੂੰ ਮਾਰਗਦਰਸ਼ਨ ਦਿਓ। |
| `translate_repository_prompt` | ਡ੍ਰਾਈ-ਰਨ-ਫਰਸਟ ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ ਲਈ MCP ਕਲਾਇੰਟ ਨੂੰ ਮਾਰਗਦਰਸ਼ਨ ਦਿਓ। |

## ਕਾਪੀ-ਪੇਸਟ ਉਦਾਹਰਣ

Markdown ਸਮੱਗਰੀ ਅਨੁਵਾਦ ਕਰੋ:

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

ਅਨੁਵਾਦ ਕੀਤੇ Markdown ਲਿੰਕ ਮੁੜ-ਲਿਖੋ:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
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

ਹੋਸਟ ਏਜੰਟ ਮਾਡਲ ਨਾਲ Markdown ਅਨੁਵਾਦ:

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

ਹੋਸਟ ਏਜੰਟ ਹਰ ਵਾਪਸ ਕੀਤੇ chunk ਦਾ ਅਨੁਵਾਦ ਕਰਨ ਤੋਂ ਬਾਅਦ, `start_markdown_agent_translation` ਵੱਲੋਂ ਵਾਪਸ ਕੀਤੇ ਪੂਰੇ `job` ਆਬਜੈਕਟ ਨਾਲ ਨੌਕਰੀ ਨੂੰ ਖਤਮ ਕਰੋ:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ ਦੀ ਪ੍ਰੀਵਿਊ:

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

## ਸਮੱਸਿਆ-ਨਿਵਾਰਣ

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Absolute Python executable ਪਾਥ ਅਤੇ `["-m", "co_op_translator.mcp.server"]` source checkout ਸੰਰਚਨਾ ਵਰਤੋਂ। |
| The server is listed but translation fails. | `get_configuration_status` ਕਾਲ ਕਰੋ ਅਤੇ ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ ਕੋਈ LLM ਪ੍ਰੋਵਾਇਡਰ ਉਪਲਬਧ ਹੈ। |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | `start_markdown_agent_translation` / `finish_markdown_agent_translation` ਜਾਂ ਨੋਟਬੁੱਕ ਸਮਕੱਖ ਵਰਤੋਂ ਤਾਂ ਕਿ ਹੋਸਟ ਏਜੰਟ chunks ਦਾ ਅਨੁਵਾਦ ਕਰੇ। |
| Image translation fails. | ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ Azure AI Vision ਵੈਰੀਏਬਲ ਸੈਟ ਹਨ ਅਤੇ `get_configuration_status` ਕਾਲ ਕਰੋ। |
| Repository translation does not write files. | ਸਿਰਫ਼ ਉਪਯੋਗਕਰਤਾ ਦੀ ਸਪੱਸ਼ਟ ਮਨਜ਼ੂਰੀ ਤੋਂ ਬਾਅਦ `dry_run=false` ਅਤੇ `confirm_write=true` ਸੈੱਟ ਕਰੋ। |
| Changes to client config do not appear. | MCP ਕਲਾਇੰਟ ਨੂੰ ਰੀਸਟਾਰਟ ਜਾਂ ਰੀਲੋਡ ਕਰੋ। |

## ਸੁਰੱਖਿਆ ਨੋਟਸ

- MCP ਟੂਲ ਕਾਲਾਂ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਵੱਲੋਂ ਮਾਡਲ-ਨਿਯੰਤ੍ਰਿਤ ਹੁੰਦੀਆਂ ਹਨ, ਇਸ ਲਈ ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ ਡਿਫੌਲਟ ਰੂਪ ਵਿੱਚ dry-run ਹੁੰਦਾ ਹੈ।
- ਪੂਰਾ ਰਿਪੋਜ਼ਟਰੀ ਅਨੁਵਾਦ ਕਈ ਫਾਈਲਾਂ ਬਣਾਉਣ, ਅਪਡੇਟ ਕਰਨ, ਜਾਂ ਹਟਾਉਣ ਦਾ ਕਾਰਨ ਬਣ ਸਕਦਾ ਹੈ। `confirm_write=true` ਸੈੱਟ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਸਪੱਸ਼ਟ ਉਪਭੋਗਤਾ ਮਨਜ਼ੂਰੀ ਦੀ ਲੋੜ ਰੱਖੋ।
- `get_configuration_status` ਟੂਲ ਕਦੇ ਵੀ API ਕੀਜ਼, endpoints, ਜਾਂ ਹੋਰ ਗੁਪਤ ਮੁੱਲ ਵਾਪਸ ਨਹੀਂ ਕਰਦਾ।
- ਚਿੱਤਰ ਅਨੁਵਾਦ base64 ਚਿੱਤਰ ਡੇਟਾ ਵਾਪਸ ਕਰਦਾ ਹੈ। ਵੱਡੇ ਚਿੱਤਰ ਵੱਡੇ ਟੂਲ ਜਵਾਬ ਪੈਦਾ ਕਰ ਸਕਦੇ ਹਨ।
- Agent-assisted ਟੂਲ ਸੋਰਸ chunks ਅਤੇ ਪ੍ਰਾਂਪਟ MCP ਹੋਸਟ ਨੂੰ ਵਾਪਸ ਕਰਦੇ ਹਨ। ਇਨ੍ਹਾਂ ਨੂੰ ਸਿਰਫ਼ ਉਸ ਸਮੱਗਰੀ ਨਾਲ ਵਰਤੋ ਜਿਸ ਨੂੰ ਯੂਜ਼ਰ ਉਸ ਹੋਸਟ ਏਜੰਟ ਮਾਡਲ ਨੂੰ ਭੇਜਣ ਲਈ ਆਰਾਮਦਾਇਕ ਸਮਝਦਾ ਹੈ।