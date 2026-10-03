# MCP ಸರ್ವರ್

Co-op Translator ನಲ್ಲಿ ಏಜೆಂಟ್‌ಗಳು, ಸಂಪಾದಕರು ಮತ್ತು MCP-ಅನುಕೂಲ ಕ್ಲೈಂಟ್‌ಗಳಿಗೆ ಒಂದು Model Context Protocol ಸರ್ವರ್ ಅಳವಡಿಸಲಾಗಿದೆ.

ಡೀಫಾಲ್ಟ್ ಸ್ಥಳೀಯ ಸೆಟ್ಅಪ್‌‌ಗಾಗಿ, ಬಳಕೆದಾರರು ವಿಭಿನ್ನ ಸರ್ವರ್ ಅನ್ನು ಕೈಯಿಂದ ಓಡಿಸುವ ಅಗತ್ಯವಿಲ್ಲ. ಅವರು ತಮ್ಮ MCP ಕ್ಲೈಂಟ್ ಅನ್ನು ಸಂರಚಿಸುತ್ತಾರೆ, ಮತ್ತು ಕ್ಲೈಂಟ್ Co-op Translator ಉಪಕರಣಗಳನ್ನು ಬೇಕಾದಾಗ `stdio` ಮೂಲಕ ಸ್ವಯಂಚಾಲಿತವಾಗಿ `co-op-translator-mcp` ಅನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ.

CLI, Python API ಮತ್ತು MCP ನಡುವಿನ ನಿರ್ಧಾರ ತೆಗೆದುಕೊಳ್ಳುತ್ತಿದ್ದರೆ, [ನಿಮ್ಮ ಕೆಲಸಪ್ರವಾಹವನ್ನು ಆಯ್ಕೆಮಾಡಿ](workflows.md) ರಿಂದ ಪ್ರಾರಂಭಿಸಿ.

ಏಜೆಂಟ್ ಅಥವಾ ಸಂಪಾದಕ Co-op Translator ಅನ್ನು ನೇರವಾಗಿ ಕರೆಮಾಡಬೇಕಾದಾಗ MCP ಅನ್ನು ಬಳಸಿ:

| ಬಳಕೆದಾರರ ಉದ್ದೇಶ | MCP ಸಾಧನಗಳು |
| --- | --- |
| ಒಂದು Markdown ಡಾಕ್ಯುಮೆಂಟ್, ನೋಟ್ಬುಕ್ ಅಥವಾ ಚಿತ್ರವನ್ನು ಅನುವಾದಿಸಿ | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಮಾದರಿಯೊಂದಿಗೆ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ವಿಷಯವನ್ನು ಅನುವಾದಿಸಿ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| ಔಟ್‌ಪುಟ್ ಪಥ ಆಯ್ಕೆ ಮಾಡಿದ ನಂತರ ಅನುವಾದಿತ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಲಿಂಕ್‌ಗಳನ್ನು ಮರುಬರೆಯಿರಿ | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI ಹೋಲಿನ ಪೂರ್ಣ ರೆಪೊಸಿಟರಿಯನ್ನು ಅನುವಾದಿಸಿ | `run_translation`, `translate_project` |
| LLM ಪ್ರಮಾಣಪತ್ರಗಳಿಲ್ಲದೆ ಅನುವಾದಿತ ಔಟ್‌ಪುಟ್ ಪರಿಶೀಲನೆ ಮಾಡಿ | `run_review` |
| ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಪರಿಸರ ಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP ಸರ್ವರ್ [Python API](api.md)ದಲ್ಲಿ ದಾಖಲೆಗೊಳ್ಳುವ ಅದೇ ಸಾರ್ವಜನಿಕ Python API ಅನ್ನು ಅವಲಂಬಿಸುತ್ತದೆ. ಪ್ರೊವೈಡರ್-ಆಧಾರಿತ ಉಪಕರಣಗಳು CLI ಮತ್ತು Python API ಜೊತೆ ಸಂರಚಿಸಲಾಗಿರುವ ಅದೇ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಬಳಸುತ್ತವೆ. ಏಜೆಂಟ್-ಸಹಕಾರಿ ಉಪಕರಣಗಳು MCP ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಅನುವಾದಿಸಲು ಚಂಕ್‌ಗಳನ್ನು ಸಿದ್ಧಪಡಿಸುತ್ತವೆ ಮತ್ತು ನಂತರ Co-op Translator ಅನ್ನು ಬಳಸಿಕೊಂಡು ಅಂತಿಮ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಅನ್ನು ಪುನರ್-ನಿರ್ಮಾಣ ಮಾಡುತ್ತವೆ.

## ಹಂತ 1: Co-op Translator ಅನ್ನು ಸ್ಥಾಪಿಸಿ ಮತ್ತು ಸಂರಚಿಸಿ

ನಿಮ್ಮ MCP ಕ್ಲೈಂಟ್ ಬಳಸುವ Python ಪರಿಸರದಲ್ಲಿ Co-op Translator ಅನ್ನು ಸ್ಥಾಪಿಸಿ:

```bash
pip install co-op-translator
```

ಈ ರೆಪೊಸಿಟೋರಿಯಿಂದ ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಗಾಗಿ, ಪ್ಯಾಕೇಜ್ ಅನ್ನು ಸಂಪಾದನಾಶೀಲ (editable) ಮೋಡ್‌ನಲ್ಲಿ ಸ್ಥಾಪಿಸಿ:

```bash
pip install -e .
```

ನಿಮ್ಮ MCP ಕ್ಲೈಂಟ್ ಬಳಸುವ ಅನುವಾದ ಮೋಡ್ ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ:

| ಮೋಡ್ | ಇದಕ್ಕಾಗಿ ಬಳಸಿರಿ | ಪ್ರಮಾಣಪತ್ರಗಳು |
| --- | --- | --- |
| ಪ್ರೊವೈಡರ್-ಆಧಾರಿತ | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ಅಥವಾ `run_translation` ಅನ್ನು ಕರೆಮಾಡುತ್ತದೆ. | ಅನುವಾದಕ್ಕೆ Azure OpenAI, OpenAI, ಅಥವಾ Anthropic ಅಗತ್ಯವಿದೆ. ಚಿತ್ರ ಅನುವಾದಕ್ಕೆ Azure AI Vision ಕೂಡ ಬೇಕು. |
| ಏಜೆಂಟ್-ಸಹಕಾರಿ | MCP ಹೋಸ್ಟ್ ಏಜೆಂಟ್ `start_markdown_agent_translation` ಅಥವಾ `start_notebook_agent_translation` ಮುಖಾಂತರ ಮರಳಿಸಿದ ಚಂಕ್‌ಗಳನ್ನು ಅನುವಾದಿಸುತ್ತದೆ. | Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಚಂಕ್ಗಳಿಗೆ Co-op Translator LLM ಪ್ರೊವೈಡರ್ ಪ್ರಮಾಣಪತ್ರಗಳ ಅಗತ್ಯವಿಲ್ಲ. ಚಿತ್ರ ಅನುವಾದ ಇನ್ನೂ ಏಜೆಂಟ್-ಸಹಕಾರಿ ಮೋಡ್‌ನಲ್ಲಿ ಒಳಗೊಂಡಿಲ್ಲ. |

Codex ಅಥವಾ Claude Code ರೀತಿಯ ಏಜೆಂಟ್ ಒಳಗೆ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಅನುವಾದದಿಂದ ಪ್ರಾರಂಭಿಸುತ್ತಿದ್ದರೆ, ಏಜೆಂಟ್-ಸಹಕಾರಿ ಮೋಡ್‌ರಿಂದ ಪ್ರಾರಂಭಿಸಿ. Co-op Translator ತಾನೇ ನಿಮ್ಮ ಸಂರಚಿತ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಕರೆಮಾಡಬೇಕಾದರೆ, ಚಿತ್ರಗಳನ್ನು ಅನುವಾದಿಸುತ್ತಿದ್ದರೆ, ಅಥವಾ CLI ಹೋಲಿದಂತೆ ರೆಪೊಸಿಟರಿ-ಮಟ್ಟದ ಅನುವಾದ ನಡೆಸಬೇಕಿದ್ದರೆ ಪ್ರೊವೈಡರ್-ಆಧಾರಿತ ಮೋಡ್ ಬಳಸಿರಿ.

ಪ್ರೊವೈಡರ್-ಆಧಾರಿತ ವರ್ಕ್‌ಫ್ಲೋಗಳಿಗಾಗಿ ಒಂದು ಪ್ರೊವೈಡರ್ ಅನ್ನು ಸಂರಚಿಸಿ:

```bash
# ಏಜ್ಯೂರ್ ಓಪನ್‌ಏಐ
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# ಅಥವಾ ಓಪನ್‌ಏಐ
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# ಅಥವಾ ಅನ್ತ್ರೋಪಿಕ್
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

ಪ್ರೊವೈಡರ್-ಆಧಾರಿತ ಚಿತ್ರ ಅನುವಾದಕ್ಕೆ ಹೆಚ್ಚುವರಿಯಾಗಿ ಬೇಕಾಗುವುದು:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    ಏಜೆಂಟ್-ಸಹಕಾರಿ ಮೋಡ್ ಪ್ರಸ್ತುತ Markdown ಮತ್ತು ನೋಟ್ಬುಕ್ Markdown ಸೆಲ್‌ಗಳನ್ನು ಒಳಗೊಂಡಿದೆ. ಚಿತ್ರ ಅನುವಾದ ಇನ್ನೂ ಪ್ರೊವೈಡರ್-ಆಧಾರಿತ ಚಿತ್ರ ಪೈಪ್‌ಲೈನನ್ನು ಬಳಸುತ್ತದೆ ಮತ್ತು OCR ಮತ್ತು ಲೇಔಟ್-ಅಗ್ನೋಸ್ಸಿಂಗ್ ರೆಂಡರಿಂಗ್‌ಗೆ Azure AI Vision ಅಗತ್ಯವಿದೆ.

## ಹಂತ 2: ನಿಮ್ಮ MCP ಕ್ಲೈಂಟ್ ಅನ್ನು ಸಂರಚಿಸಿ

ಸಾಮಾನ್ಯ ಸ್ಥಳೀಯ `stdio` ಸೆಟ್ಅಪ್‌ಗಾಗಿ, Co-op Translator ಅನ್ನು ನಿಮ್ಮ MCP ಕ್ಲೈಂಟ್ ಸಂರಚನೆಯಲ್ಲಿ ಸೇರಿಸಿ. ಕ್ಲೈಂಟ್ ಆ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ನಿಲ್ಲಿಸುತ್ತದೆ.

ಸ್ಥಾಪಿಸಲಾದ ಪ್ಯಾಕೇಜ್ ಸಂರಚನೆ:

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

Windows ನಲ್ಲಿ ಮೂಲ checkout ಸಂರಚನೆ:

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

macOS ಅಥವಾ Linux ನಲ್ಲಿ ಮೂಲ checkout ಸಂರಚನೆ:

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

MCP ಕ್ಲೈಂಟ್ ಸಂರಚನೆಯನ್ನು ಬದಲಿಸಿದ ನಂತರ, ಹೊಸ ಸರ್ವರ್ ಅನ್ನು ಕಂಡುಹಿಡಿಯಲು ಕ್ಲೈಂಟ್ ಅನ್ನು ಮರುಪ್ರಾರಂಭ ಅಥವಾ ಮರುಲೋಡ್ ಮಾಡಿ.

## ಹಂತ 3: ಕ್ಲೈಂಟ್‌ನಲ್ಲಿ ಸರ್ವರ್ ಅನ್ನು ಪರಿಶೀಲಿಸಿ

ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಲು MCP ಕ್ಲೈಂಟ್ ಅನ್ನು ಕೇಳಿ, ಅಥವಾ ಮೊದಲು ಓದು-ಮಾತ್ರ ಸಹಾಯಕಗಳಲ್ಲಿ ಒಂದನ್ನು ಕರೆಮಾಡಿ:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

ಪ್ರಯೋಜನಕಾರಿ ಪ್ರಾಥಮಿಕ ಪರಿಶೀಲನೆಗಳು:

| ಉಪಕರಣ | ಎನ್ನು ಪರಿಶೀಲಿಸಬೇಕು |
| --- | --- |
| `get_api_overview` | ಸರ್ವರ್ ತಲುಪಬಹುದೆಂದು ದೃಢಪಡಿಸುತ್ತದೆ ಮತ್ತು ಲಭ್ಯವಿರುವ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ತೋರಿಸುತ್ತದೆ. |
| `list_supported_languages` | ಪ್ಯಾಕೇಜ್ ಮಾಡಲಾದ ಭಾಷಾ ಡೇಟಾವನ್ನು ಲೋಡ್ ಮಾಡಬಹುದೆಂದು ದೃಢಪಡಿಸುತ್ತದೆ. |
| `get_configuration_status` | ರಹಸ್ಯ ಮೌಲ್ಯಗಳನ್ನು ಬಹಿರಂಗಪಡಿಸದೆ LLM ಮತ್ತು Vision ಪ್ರೊವೈಡರ್ ಲಭ್ಯತೆಯನ್ನು ದೃಢಪಡಿಸುತ್ತದೆ. |

## ಹಂತ 4: ಒಂದು ವರ್ಕ್ಫ್ಲೋ ಆಯ್ಕೆ ಮಾಡಿ

### ವೈಯಕ್ತಿಕ ಫೈಲ್‌ಗಳು ಅಥವಾ ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಅನುವಾದಿಸು

MCP ಕ್ಲೈಂಟ್‌ಗೆ ಈಗಾಗಲೇ ಡಾಕ್ಯುಮೆಂಟ್ ವಿಷಯ ಅಥವಾ ಚಿತ್ರ ಪಥ ಇದ್ದು, Co-op Translator ಸಂರಚಿತ ಅನುವಾದ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಕರೆಮಾಡಬೇಕಾದಾಗ ಪ್ರೊವೈಡರ್-ಆಧಾರಿತ ವಿಷಯ ಉಪಕರಣಗಳನ್ನು ಬಳಸಿ.

Markdown ಗಾಗಿ:

1. `document`, `language_code`, ಮತ್ತು ಆಯ್ಕೆಯಾಗಿ `source_path` ಜೊತೆಗೆ `translate_markdown_content` ಅನ್ನು ಕರೆಮಾಡಿ.
2. ಅನುವಾದಿತ ಫಲಿತಾಂಶವನ್ನು Co-op Translator ಔಟ್‌ಪುಟ್ বিন್ಯಾಸಕ್ಕೆ ಬರೆಯಬೇಕಾದರೆ, `rewrite_markdown_paths` ಅನ್ನು ಕರೆಮಾಡಿ.
3. ಕ್ಲೈಂಟ್‌ಗೆ ಅಂತಿಮ `content` ಅನ್ನು ಬರೆಯಲು ಅಥವಾ ಮರಳಿಸಲು ಬಿಡಿ.

ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ:

1. ನೋಟ್ಬುಕ್ JSON ಮತ್ತು `language_code` ಜೊತೆ `translate_notebook_content` ಅನ್ನು ಕರೆಮಾಡಿ.
2. ಅನುವಾದಿತ ನೋಟ್ಬುಕ್ ಲಿಂಕ್‌ಗಳನ್ನು ಗುರಿ ಪಥಕ್ಕೆ ಸರಿಹೊಂದಿಸಬೇಕಾದರೆ `rewrite_notebook_paths` ಅನ್ನು ಕರೆಮಾಡಿ.
3. ಅಂತಿಮ ನೋಟ್ಬುಕ್ JSON ಅನ್ನು ಬರೆಯಿರಿ ಅಥವಾ ಮರಳಿ ನೀಡಿ.

ಚಿತ್ರಗಳಿಗಾಗಿ:

1. `image_path`, `language_code`, ಮತ್ತು ಆಯ್ಕೆಯಾಗಿ `root_dir` ಅಥವಾ `fast_mode` ಜೊತೆ `translate_image_content` ಅನ್ನು ಕರೆಮಾಡಿ.
2. ಮರಳಿಸಲಾದ `data_base64` ಮತ್ತು `mime_type` ಅನ್ನು ಓದಿ.
3. `output_path` ನೀಡಲ್ಪಟ್ಟಿದ್ದರೆ, ಅನುವಾದಿತ ಚಿತ್ರವನ್ನು ಆ ಪಥದಲ್ಲಿಯೂ ಸಂರಕ್ಷಿಸಲಾಗುತ್ತದೆ.

ವಿಷಯ ಉಪಕರಣಗಳು ಪ್ರಾಜೆಕ್ಟ್ ಕಂಡುಹೊರತುವುದು, ಮೆಟಾಡೇಟಾ ನವೀಕರಣಗಳು, ದಿಸ್ಕ್ಲೇಮರ್‍ಗಳು ಅಥವಾ ಸ್ವಯಂಚಾಲಿತ ಪಥ ಮರುಬರೆಯುವಿಕೆಯನ್ನು ನಿರ್ವಹಿಸುವುದಿಲ್ಲ. Co-op Translator LLM ಪ್ರೊವೈಡರ್ ಪ್ರಮಾಣಪತ್ರಗಳಿಲ್ಲದೆ ಹೋಸ್ಟ್ ಏಜೆಂಟ್ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಚಂಕ್‌ಗಳನ್ನು ಅನುವಾದಿಸಬೇಕಾದರೆ, ಕೆಳಗಿನ ಏಜೆಂಟ್-ಸಹಕಾರಿ ವರ್ಕ್ಫ್ಲೋವನ್ನು ಬಳಸಿ.

### ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಮಾದರಿಯೊಂದಿಗೆ ಅನುವಾದಿಸು

Co-op Translator ಗಾಗಿ LLM ಪ್ರೊವೈಡರ್ ಅನ್ನು ಸಂರಚಿಸುವ ಬದಲು MCP ಹೋಸ್ಟ್ ಏಜೆಂಟ್ (ಉದಾಹರಣೆಗೆ ಕೋಡಿಂಗ್ ಸಹಾಯಕ) ಅನುವಾದಿತ ಪಠ್ಯವನ್ನು ಉತ್ಪಾದಿಸುವಂತೆ ಬೇಕಾದರೆ ಏಜೆಂಟ್-ಸಹಕಾರಿ ಉಪಕರಣಗಳನ್ನು ಬಳಸಿ.

ಚಾಟ್ ಆಧಾರಿತ MCP ಕ್ಲೈಂಟ್‌ನಲ್ಲಿ, ಸಾಮಾನ್ಯವಾಗಿ ನೀವು ಟೂಲ್ JSON ಅನ್ನು ನಿಮ್ಮಿಂದಲೇ ಬರೆಯಬೇಕಾಗುವುದಿಲ್ಲ. ಏಜೆಂಟ್‌ಗೆ ಏಜೆಂಟ್-ಸಹಕಾರಿ ವರ್ಕ್ಫ್ಲೋ ಬಳಸಲು ಹೇಳಿ:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ, ಇದೇ ಮಾದರಿಯನ್ನು ಬಳಸಿ:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

ನಿಮ್ಮ MCP ಕ್ಲೈಂಟ್ ಸರ್ವರ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬೆಂಬಲಿಸಿದರೆ, ಅದೇ ವರ್ಕ್‌ಫ್ಲೋ ಸೂಚನೆಗಳನ್ನು ಲೋಡ್ ಮಾಡಲು `agent_assisted_markdown_translation_prompt` ಅನ್ನು ಬಳಸಿ.

Markdown ಗಾಗಿ:

1. `document`, `language_code`, ಮತ್ತು ಆಯ್ಕೆಯಾಗಿ `source_path` ಜೊತೆ `start_markdown_agent_translation` ಅನ್ನು ಕರೆಮಾಡಿ.
2. ಪ್ರತಿ ಮರಳಿಸಲಾದ ಚಂಕ್‌ನ `prompt` ಅನ್ನು ಅನುಸರಿಸಿ ಹೋಸ್ಟ್ ಏಜೆಂಟ್‌ನಲ್ಲಿ ಅವುಗಳನ್ನು ಅನುವಾದಿಸಿ.
3. ಮೂಲ `job` ಮತ್ತು `chunk_id`, `translated_text` ಬಳಸಿಕೊಂಡು ಅನುವಾದಿತ ಚಂಕ್‌ಗಳೊಂದಿಗೆ `finish_markdown_agent_translation` ಅನ್ನು ಕರೆ ಮಾಡಿ.
4. ವಿಷಯವನ್ನು ಅನುವಾದಿತ ಗುರಿ ಪಥಕ್ಕೆ ಬರೆಯಬೇಕಾದರೆ, `rewrite_markdown_paths` ಅನ್ನು ಕರೆಮಾಡಿ.

ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ:

1. ನೋಟ್ಬುಕ್ JSON ಮತ್ತು `language_code` ಜೊತೆ `start_notebook_agent_translation` ಅನ್ನು ಕರೆಮಾಡಿ.
2. ಹೋಸ್ಟ್ ಏಜೆಂಟ್‌ನಲ್ಲಿ ಮರಳಲಾದ ಪ್ರತಿ ಚಂಕ್ ಅನ್ನು ಅನುವಾದಿಸಿ.
3. ಮೂಲ `job` ಮತ್ತು ಅನುವಾದಿತ ಚಂಕ್‌ಗಳೊಂದಿಗೆ `finish_notebook_agent_translation` ಅನ್ನು ಕರೆಮಾಡಿ.
4. ಅನುವಾದಿತ ನೋಟ್ಬುಕ್ ಲಿಂಕ್‌ಗಳು ಗುರಿ-ಪಥ ಸರಿಹೊಂದಿಕೆಗೆ ಅಗತ್ಯವಿದ್ದರೆ `rewrite_notebook_paths` ಅನ್ನು ಕರೆಮಾಡಿ.

ಏಜೆಂಟ್-ಸಹಕಾರಿ ಉಪಕರಣಗಳು Co-op Translator ನಿಂದ ಸಂರಚಿತ LLM ಪ್ರೊವೈಡರ್ ಅನ್ನು ಕರೆಯುವುದಿಲ್ಲ. ಮರಳಿಸಲಿದ್ದ ಚಂಕ್‌ಗಳನ್ನು ಅನುವಾದಿಸುವ ಜವಾಬ್ದಾರಿ ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಮೇಲೆ ಇರುತ್ತದೆ. Co-op Translator Markdown ಚಂಕಿಂಗ್, ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್ ಸಂರಕ್ಷಣೆ, ಫ್ರಂಟ್‌ಮ್ಯಾಟರ್ ಪುನರ್-ನಿರ್ಮಾಣ, ನೋಟ್ಬುಕ್ ಸೆಲ್ ಬದಲಾವಣೆ ಮತ್ತು ಅನುವಾದದ ನಂತರದ ಸಮಾನುಕರಣವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.

### ಸಂಪೂರ್ಣ ರೆಪೊಸಿಟೋರಿಯನ್ನು ಅನುವಾದಿಸಿ

ಬಳಕೆದಾರನು Co-op Translator ಅನ್ನು `translate` CLI ರೀತಿಯಲ್ಲಿ ವರ್ತಿಸಬೇಕೆಂದು ಬಯಸಿದಾಗ `run_translation` ಅನ್ನು ಬಳಸಿ.

ರೆಪೊಸಿಟರಿ ಅನುವಾದವು ಡೀಫಾಲ್ಟ್ ಆಗಿ `dry_run=true` ಆಗಿರುತ್ತದೆ, ಇದರಿಂದ ಏಜೆಂಟ್ ಫೈಲ್ ಬದಲಾವಣೆಗಳ ಮುನ್ನ ವ್ಯಾಪ್ತಿಯನ್ನು ಪರಿಶೀಲಿಸಬಹುದು:

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

ಬರೆಯಲು ಅನುಮತಿ ನೀಡಲು, ಕರೆಮಾಡುವವನು ಎರಡೂ `dry_run=false` ಮತ್ತು `confirm_write=true` ಅನ್ನು ಸೆಟ್ ಮಾಡಬೇಕು:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ಅನ್ನು `run_translation` ಗೆ ಹೊಂದಿಕಾಸಾಧಕ ಬದಲಿ ಹೆಸರು ಆಗಿ ಒದಗಿಸಲಾಗಿದೆ.

### ಅನುವಾದಿತ ಔಟ್‌ಪುಟ್ ಪರಿಶೀಲಿಸಿ

LLM ಅಥವಾ Vision ಪ್ರಮಾಣಪತ್ರಗಳಿಲ್ಲದ ನಿರ್ಣಾಯಕ ಪರಿಶೀಲನೆಗಳಿಗೆ `run_review` ಅನ್ನು ಬಳಸಿ:

!!! note "Beta"
    MCP Beta `run_review` API ಅನ್ನು ಅನಾವರಣ ಮಾಡುತ್ತದೆ. ಇದು ಓದು-ಮಾತ್ರ ರಿವ್ಯೂ ವರ್ಕ್‌ಫ್ಲೋಗಳಿಗೆ ಸುರಕ್ಷಿತವಾಗಿದೆ, ಆದರೆ ರಿವ್ಯೂ ಪರಿಶೀಲನೆಗಳು ಮತ್ತು ಸಮಸ್ಯೆ ಸ್ಕೀಮಾಗಳು ಬದಲಾಗಬಹುದು.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

ಫಲಿತಾಂಶದಲ್ಲಿ ಹಿಡಿದಿಟ್ಟುಕೊಂಡ ಪಠ್ಯ ಔಟ್‌ಪುಟ್ ಮತ್ತು ಲಭ್ಯವಿದ್ದಲ್ಲಿ ಸಂರಚಿತ ರಿವ್ಯೂ ಸಾರಾಂಶವೂ ಒಳಗೊಳ್ಳುತ್ತದೆ.

## ಕೈಯಿಂದ ಸರ್ವರ್ ಚಾಲನೆಗಳು

ಕೈಯಿಂದ ನಡೆಸುವ ಚಾಲನೆಗಳು ಮುಖ್ಯವಾಗಿ ಡಿಬಗ್ಗಿಂಗ್‌ಗಾಗಿ ಅಥವಾ ದೀರ್ಘಾವಧಿ ಸರ್ವರ್‍ಗಳಂತೆ ವರ್ತಿಸುವ ಟ್ರಾನ್ಸ್ಪೋರ್ಟ್‌ಗಳಿಗಾಗಿ ಇರುತ್ತವೆ.

ಡೀಫಾಲ್ಟ್ stdio ಸರ್ವರ್ ಅನ್ನು ಡಿಬಗ್ ಮಾಡಿ:

```bash
co-op-translator-mcp
```

ಮೂಲ checkout ನಿಂದ ರನ್ ಮಾಡಿ:

```bash
python -m co_op_translator.mcp.server
```

ದೀರ್ಘಕಾಲದ HTTP ಅಥವಾ SSE ಸರ್ವರ್ ಅನ್ನು ರನ್ ಮಾಡಿ:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

ಸ್ಥಳೀಯ ಸಂಪಾದಕ ಮತ್ತು ಏಜೆಂಟ್ ಇಂಟégrೇಶನ್‌ಗಳಿಗಾಗಿ, ಹಂತ 2 ರಲ್ಲಿ ಕ್ಲೈಂಟ್-ನಿರ್ವಹಿತ `stdio` ಸಂರಚನೆಯನ್ನು ಆದ್ಯತೆ ನೀಡಿ.

## ಉಪಕರಣಗಳು

| ಉಪಕರಣ | ಉದ್ದೇಶ | ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯುತ್ತದೆಯೇ |
| --- | --- | --- |
| `translate_markdown_content` | Markdown ಸ್ಟ್ರಿಂಗ್ ಅನ್ನು ಅನುವಾದಿಸಿ. | ಇಲ್ಲ |
| `translate_notebook_content` | ನೋಟ್ಬುಕ್ JSON ನಲ್ಲಿ Markdown ಸೆಲ್‍ಗಳನ್ನು ಅನುವಾದಿಸಿ. | ಇಲ್ಲ |
| `translate_image_content` | ಒಂದು ಚಿತ್ರದಲ್ಲಿನ ಪಠ್ಯವನ್ನು ಅನುವಾದಿಸಿ ಮತ್ತು base64 ಚಿತ್ರ ಡೇಟಾವನ್ನು ಮರಳಿಸಿ. | ಐಚ್ಛಿಕ, ಕೇವಲ `output_path` ನೀಡಿದಾಗ ಮಾತ್ರ |
| `start_markdown_agent_translation` | Co-op Translator LLM ಪ್ರಮಾಣಪತ್ರಗಳಿಲ್ಲದೆ ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಅನುವಾದಿಸಲು Markdown ಚಂಕ್‌ಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಿ. | ಇಲ್ಲ |
| `finish_markdown_agent_translation` | ಹೋಸ್ಟ್-ಏಜೆಂಟ್ ಅನುವಾದಿತ ಚಂಕ್‌ಗಳಿಂದ Markdown ಅನ್ನು ಪುನರ್-ನಿರ್ಮಾಣ ಮಾಡಿ. | ಇಲ್ಲ |
| `start_notebook_agent_translation` | ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಅನುವಾದಿಸಲು ನೋಟ್ಬುಕ್ Markdown-ಸೆಲ್ ಚಂಕ್‌ಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಿ. | ಇಲ್ಲ |
| `finish_notebook_agent_translation` | ಹೋಸ್ಟ್-ಏಜೆಂಟ್ ಅನುವಾದಿತ ಚಂಕ್‌ಗಳಿಂದ ನೋಟ್ಬುಕ್ JSON ಅನ್ನು ಪುನರ್-ನಿರ್ಮಾಣ ಮಾಡಿ. | ಇಲ್ಲ |
| `rewrite_markdown_paths` | ಅನುವಾದಿತ ಗುರಿಗಾಗಿ Markdown ದೇಹ ಮತ್ತು ಫ್ರಂಟ್‌ಮ್ಯಾಟರ್ ಪಥಗಳನ್ನು ಮರುಬರೆಯಿರಿ. | ಇಲ್ಲ |
| `rewrite_notebook_paths` | ನೋಟ್ಬುಕ್ Markdown ಸೆಲ್‌ಗಳ ಒಳಗಿನ ಪಥಗಳನ್ನು ಮರುಬರೆಯಿರಿ. | ಇಲ್ಲ |
| `run_translation` | CLI ಹೋಲಿನಂತೆ ಪ್ರಾಜೆಕ್ಟ್-ಮಟ್ಟದ ಅನುವಾದವನ್ನು ಚಾಲನೆ ಮಾಡಿ. | ಹೌದು (`dry_run=false` ಮತ್ತು `confirm_write=true` ಆಗಿರುವಾಗ) |
| `translate_project` | `run_translation` ಗೆ ಹೊಂದಿಕಾಸಾಧಕ ಬದಲಿ ಹೆಸರು. | ಹೌದು (`dry_run=false` ಮತ್ತು `confirm_write=true` ಆಗಿರುವಾಗ) |
| `run_review` | ನಿರ್ಣಾಯಕ ರಿವ್ಯೂ ಪರಿಶೀಲನೆಗಳನ್ನು ಚಾಲನೆ ಮಾಡಿ. | ಇಲ್ಲ |
| `get_configuration_status` | ರಹಸ್ಯಗಳನ್ನು ಬಹಿರಂಗಪಡಿಸದೆ ಸಂರಚಿತ LLM ಮತ್ತು Vision ಪ್ರೊವೈಡರ್‌ಗಳ ವರದಿ ನೀಡಿ. | ಇಲ್ಲ |
| `list_supported_languages` | ಬೆಂಬಲಿತ ಗುರಿ ಭಾಷಾ ಕೋಡ್‌ಗಳ ಪಟ್ಟಿಯನ್ನು ನೀಡುತ್ತದೆ. | ಇಲ್ಲ |
| `get_api_overview` | ಲಭ್ಯವಿರುವ MCP ವರ್ಕ್‌ಫ್ಲೋ ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ವಿವರಿಸಿ. | ಇಲ್ಲ |

## ಸಂಪನ್ಮೂಲಗಳು

| ಸಂಪನ್ಮೂಲ URI | ಉದ್ದೇಶ |
| --- | --- |
| `co-op://api` | ವರ್ಕ್‌ಫ್ಲೋ ಮತ್ತು ಉಪಕರಣಗಳ JSON ಅವಲೋಕನ. |
| `co-op://supported-languages` | ಬೆಂಬಲಿತ ಭಾಷಾ ಕೋಡ್‌ಗಳ JSON ಪಟ್ಟಿ. |
| `co-op://configuration` | ರಹಸ್ಯಗಳಿಲ್ಲದ ಪ್ರೊವೈಡರ್ ಲಭ್ಯತೆಯ ಸಾರಾಂಶ JSON. |

## ಪ್ರಾಂಪ್ಟ್‌ಗಳು

| ಪ್ರಾಂಪ್ಟ್ | ಉದ್ದೇಶ |
| --- | --- |
| `translate_markdown_document_prompt` | ವಿಷಯ ಅನುವಾದ ಮತ್ತು ಐಚ್ಛಿಕ ಪಥ ಮರುಬರೆಯುವಿಕೆಯ ಮೂಲಕ MCP ಕ್ಲೈಂಟ್‌ಗೆ ಮಾರ್ಗದರ್ಶನ ಮಾಡಿ. |
| `agent_assisted_markdown_translation_prompt` | Co-op Translator LLM ಪ್ರೊವೈಡರ್ ಪ್ರಮಾಣಪತ್ರಗಳಿಲ್ಲದೆ ಹೋಸ್ಟ್-ಏಜೆಂಟ್ Markdown ಅನುವಾದದ ಮೂಲಕ MCP ಕ್ಲೈಂಟ್‌ಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡಿ. |
| `translate_repository_prompt` | ಮೊದಲು dry-run ನಡೆಸುವ ರೆपೊಸಿಟರಿ ಅನುವಾದದ ಮೂಲಕ MCP ಕ್ಲೈಂಟ್‌ಗೆ ಮಾರ್ಗದರ್ಶನ ಮಾಡಿ. |

## ನಕಲಿಸಿ-ಅಂಟಿಸಿ ಉದಾಹರಣೆಗಳು

Markdown ವಿಷಯವನ್ನು ಅನುವಾದಿಸು:

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

ಅನುವಾದಿತ Markdown ಲಿಂಕ್‌ಗಳನ್ನು ಮರುಬರೆಯಿರಿ:

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

ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಮಾದರಿಯಿಂದ Markdown ಅನ್ನು ಅನುವಾದಿಸು:

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

ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಪ್ರತಿಯೊಂದು ಮರಳಿಸಿದ ಚಂಕ್ ಅನ್ನು ಅನುವಾದಿಸಿದ ನಂತರ, `start_markdown_agent_translation` ಮೂಲಕ ಮರಳಿಸಿದ ಸಂಪೂರ್ಣ `job` ಆಬ್ಜೆಕ್ಟ್‌ನೊಂದಿಗೆ ಕೆಲಸವನ್ನು ಮುಗಿಸಿ:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

ರೆಪೊಸಿಟರಿ ಅನುವಾದದ ಮುನ್ಸೂಚನೆ:

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

## ತೊಂದರೆ ಪರಿಹಾರ

| ಸಮಸ್ಯೆ | ಪ್ರಯತ್ನಿಸಬೇಕಾದುದು |
| --- | --- |
| MCP ಕ್ಲೈಂಟ್ `co-op-translator-mcp` ಅನ್ನು ಕಂಡುಕೊಳ್ಳುತ್ತಿಲ್ಲ. | ನಿಖರ (absolute) Python ಕಾರ್ಯನಿರ್ವಹಣಾ ಪಥ ಮತ್ತು `["-m", "co_op_translator.mcp.server"]` source checkout ಸಂರಚನೆಯನ್ನು ಬಳಸಿ. |
| ಸರ್ವರ್ ಪಟ್ಟಿ ಆಗಿದೆ ಆದರೆ ಅನುವಾದ ವಿಫಲವಾಗಿದೆ. | `get_configuration_status` ಅನ್ನು ಕರೆಮಾಡಿ ಮತ್ತು LLM ಪ್ರೊವೈಡರ್ ಲಭ್ಯವಿದೆಯೆಂದು ದೃಢಪಡಿಸಿ. |
| ನೀವು ಪ್ರೊವೈಡರ್ ಪ್ರಮಾಣಪತ್ರಗಳಿಲ್ಲದೆ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಅನುವಾದಬಯಸುತ್ತೀರಿ. | ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಚಂಕ್‌ಗಳನ್ನು ಅನುವಾದಿಸಲಿ ಎಂದು `start_markdown_agent_translation` / `finish_markdown_agent_translation` ಅಥವಾ ನೋಟ್ಬುಕ್ ಸಮಾನವಾದಗಳನ್ನು ಬಳಸಿ. |
| ಚಿತ್ರ ಅನುವಾದ ವಿಫಲವಾಗಿದೆ. | Azure AI Vision ವ್ಯಾರಿಯಬಲ್‌ಗಳು ಸೆಟ್ ಆಗಿವೆ ಎಂದು ದೃಢಪಡಿಸಿ ಮತ್ತು `get_configuration_status` ಅನ್ನು ಕರೆಮಾಡಿ. |
| ರೆಪೊಸಿಟರಿ ಅನುವಾದ ಫೈಲ್‌ಗಳನ್ನು ಬರೆಯುತ್ತಿಲ್ಲ. | ಸ್ಪಷ್ಟ ಬಳಕೆದಾರ ಅನುಮೋದನೆಯ ನಂತರ ಮಾತ್ರ `dry_run=false` ಮತ್ತು `confirm_write=true` ಅನ್ನು ಸೆಟ್ ಮಾಡಿ. |
| ಕ್ಲೈಂಟ್ ಕಾನ್ಫಿಗ್‌ನಲ್ಲಿ ಬದಲಾವಣೆಗಳು ಕಾಣಿಸದೆ ಇದ್ದರೆ. | MCP ಕ್ಲೈಂಟ್ ಅನ್ನು ಮರುಪ್ರಾರಂಭ ಅಥವಾ ಮರುಲೋಡ್ ಮಾಡಿ. |

## ಸುರಕ್ಷತಾ ಗಮನಿಕೆಗಳು

- MCP ಉಪಕರಣ ಕರೆಗಳು ಹೋಸ್ಟ್ ಅಪ್ಲಿಕೇಶನ್ ಮೂಲಕ ಮಾದರಿ ನಿಯಂತ್ರಿತವಾಗಿರುವುದರಿಂದ, ರೆಪೊಸಿಟರಿ ಅನುವಾದ ಡೀಫಾಲ್ಟ್ ಆಗಿ dry-run ಆಗಿರುತ್ತದೆ.
- ಸಂಪೂರ್ಣ ರೆಪೊಸಿಟರಿ ಅನುವಾದವು ಅನೇಕ ಫೈಲ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸಬಹುದು, ನವೀಕರಿಸಬಹುದು ಅಥವಾ ಅಳಿಸಬಹುದು. `confirm_write=true` ಅನ್ನು ಸೆಟ್ ಮಾಡುವ ಮೊದಲು ಸ್ಪಷ್ಟ ಬಳಕೆದಾರ ಅನುಮೋದನೆ ಅಗತ್ಯವಿದೆ.
- ಸಂರಚನಾ ಸ್ಥಿತಿ ಉಪಕರಣವು API ಕೀಗಳು, ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳು ಅಥವಾ ಇತರ ರಹಸ್ಯ ಮೌಲ್ಯಗಳನ್ನು ಎಂದಿಗೂ ಮರಳಿಸುವುದಿಲ್ಲ.
- ಚಿತ್ರ ಅನುವಾದವು base64 ಚಿತ್ರದ ಡೇಟಾ ಅನ್ನು ಮರಳಿಸುತ್ತದೆ. ದೊಡ್ಡ ಚಿತ್ರಗಳು ದೊಡ್ಡ ಉಪಕರಣ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಹುಟ್ಟಿಸಲು ಸಾಧ್ಯ.
- ಏಜೆಂಟ್-ಸಹಕಾರಿ ಉಪಕರಣಗಳು ಮೂಲ ಚಂಕ್‌ಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು MCP ಹೋಸ್ಟ್‌ಗೆ ಮರಳಿಸುತ್ತವೆ. ಬಳಕೆದಾರನು ಆ ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಮಾದರಿಗೆ ಕಳುಹಿಸಲು ಅನುಕೂಲವಾಗುವ ವಿಷಯಗಳೊಂದಿಗೆ ಮಾತ್ರ ಅವುಗಳನ್ನು ಬಳಸಿ.