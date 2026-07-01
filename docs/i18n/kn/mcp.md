# MCP ಸರ್ವರ್

Co-op Translator मध्ये ಏಜೆಂಟ್‌ಗಳು, ಸಂಪಾದಕರು ಮತ್ತು MCP-ಸಮಾನ ಕ್ಲೈಯಿಂಟ್‌ಗಳಿಗಾಗಿ Model Context Protocol ಸರ್ವರ್ ಸೇರಿದೆ.

ಡೀಫಾಲ್ಟ್ ಸ್ಥಳೀಯ ಸಂರಚನೆಗಾಗಿ, ಬಳಕೆದಾರರು ಒಂದೇ ವಿಭಿನ್ನ ಸರ್ವರ್ ಅನ್ನು ಕೈಯಿಂದ ಓಡಿಸುವ ಅಗತ್ಯವಿಲ್ಲ. ಅವೆರವರು ತಮ್ಮ MCP ಕ್ಲೈಯಿಂಟ್ನ್ನು ಸಂರಚಿಸುತ್ತಾರೆ, ಮತ್ತು ಕ್ಲೈಯಿಂಟ್ ಅವಶ್ಯಕತೆ ಇರುವಾಗ Co-op Translator સાધನಗಳಿಗೆ `stdio` ಮೂಲಕ ಸ್ವಯಂಚಾಲಿತವಾಗಿ `co-op-translator-mcp` ಅನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ.

ನೀವು CLI, Python API, ಮತ್ತು MCP ನಡುವೆ ಆಯ್ಕೆ ಮಾಡುತ್ತಿರುವಲ್ಲಿ, [Choose Your Workflow](workflows.md) ನಿಂದ ಪ್ರಾರಂಭಿಸಿ.

MCP ಅನ್ನು ಬಳಸಿರಿ جڏهن ಏಜೆಂಟ್ ಅಥವಾ ಸಂಪಾದಕ ನೇರವಾಗಿ Co-op Translator ಅನ್ನು ಕರೆದಿರಬೇಕು:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP ಸರ್ವರ್ [Python API](api.md) ನಲ್ಲಿ ದಾಖಲಿಸಿರುವ ಅದೇ ಪಬ್ಲಿಕ್ Python API ಅನ್ನು ಲೆಪಿಸುತ್ತದೆ. ಪ್ರೊವೈಡರ್-ನಿರ್ಧರಿತ ಸಾಧನಗಳು CLI ಮತ್ತು Python API ಗೆ ಕೊಂಡಿರುವ ಅದೇ ಸಂರಚಿಸಲಾದ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಬಳಸುತ್ತವೆ. ಏಜೆಂಟ್-ಸಹಾಯಕ ಸಾಧನಗಳು MCP ಹೋಸ್ಟ್ ಏಜೆಂಟ್‌ಗೆ ಅನುವಾದಿಸಲು ಚಂಕ್‌ಗಳನ್ನು ತಯಾರಿಸುತ್ತವೆ, ನಂತರ Co-op Translator ಅನ್ನು ಬಳಸಿಕೊಂಡು ಅಂತಿಮ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಅನ್ನು ಪುನರ್ನಿರ್ಮಾಣ ಮಾಡುತ್ತವೆ.

## Step 1: Install and Configure Co-op Translator

ನಿಮ್ಮ MCP ಕ್ಲೈಯಿಂಟ್ ಬಳಸಲಿರುವ Python ಪರಿಸರದಲ್ಲಿ Co-op Translator ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ:

```bash
pip install co-op-translator
```

ಈ ಸಂಗ್ರಹಣೆಯಿಂದ ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಗಾಗಿ, ಪ್ಯಾಕೇಜ್ ಅನ್ನು editable ಮೋಡ್‌ನಲ್ಲಿ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ:

```bash
pip install -e .
```

ನಿಮ್ಮ MCP ಕ್ಲೈಯಿಂಟ್ ಬಳಸಲಿರುವ ಅನುವಾದ ಮೋಡ್ ಆಯ್ಕೆಮಾಡಿ:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

ನೀವು Codex ಅಥವಾ Claude Code ಮುಂತಾದ ಏಜೆಂಟ್ ಒಳಗಡೆ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಅನುವಾದದಿಂದ ಪ್ರಾರಂಭಿಸುತ್ತಿದ್ದರೆ, agent-assisted ಮೋಡ್‌ನಿಂದ ಪ್ರಾರಂಭಿಸಿ. Co-op Translator ತನ್ನ ಜೊತೆಗೆ ನಿಮ್ಮ ಸಂರಚಿಸಲಾದ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಕರೆದುಕೊಳ್ಳಬೇಕಾದಾಗ, ಚಿತ್ರಗಳನ್ನು ಅನುವಾದಿಸುವಾಗ, ಅಥವಾ CLI ನ ಹಾಗೆ ಸಂಗ್ರಹಣಾ ಮಟ್ಟದ ಅನುವಾದ ನಡೆಸುವಾಗ provider-backed ಮೋಡ್ ಅನ್ನು ಬಳಸಿ.

ಪ್ರೊವೈಡರ್-ನಿರ್ಧರಿತ ವರ್ಕ್‌ಫ್ಲೋಗಳಿಗಾಗಿ ಮಾತ್ರ ಪ್ರೊವೈಡರ್ ಕ್ರೆಡೆನ್ಶಿಯಲ್ಸ್ ಅನ್ನು ಸಂರಚಿಸಿ:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

ಪ್ರೊವೈಡರ್-ನಿರ್ಧರಿತ ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ ಕೆಳಕಂಡವುಗಳು ಹೆಚ್ಚಾಗಿ ಅಗತ್ಯವಿದೆ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Step 2: Configure Your MCP Client

ಸಾಮಾನ್ಯ ಸ್ಥಳೀಯ `stdio` ಸಂರಚನೆಗಾಗಿ, ನಿಮ್ಮ MCP ಕ್ಲೈಯಿಂಟ್ ಕಾನ್ಫಿಗ್‌ಗೆ Co-op Translator ಅನ್ನು ಸೇರಿಸಿ. ಕ್ಲೈಯಿಂಟ್ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪ್ರಾರಂಭ ಮತ್ತು ನಿಲ್ಲಿಸುತ್ತದೆ.

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

MCP ಕ್ಲೈಯಿಂಟ್ ಸಂರಚನೆಯನ್ನು ಬದಲಿಸಿದ ನಂತರ, ಹೊಸ ಸರ್ವರ್ ಕಂಡುಹಿಡಿಯಲು ಕ್ಲೈಯಿಂಟ್ ಅನ್ನು ಮರುಪ್ರಾರಂಭ ಅಥವಾ ರೀಲೋಡ್ ಮಾಡಿ.

## Step 3: Verify the Server in the Client

ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪ್ರತ್ಯೇಕಿಸಲು ಅಥವಾ ಮೊದಲಿಗೆ ಓದು ಮಾತ್ರ ಸಹಾಯಕರನ್ನು ಕರೆದೊಯ್ಯಲು MCP ಕ್ಲೈಯಿಂಟ್‌ಗೆ ಕೇಳಿ:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

ಉಪಯುಕ್ತ ಪ್ರಾಥಮಿಕ ಪರೀಕ್ಷೆಗಳು:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Confirms the server is reachable and shows available workflows. |
| `list_supported_languages` | Confirms packaged language data can be loaded. |
| `get_configuration_status` | Confirms LLM and Vision provider availability without exposing secret values. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

MCP ಕ್ಲೈಯಿಂಟ್ ಈಗಾಗಲೇ ಡೋಕ್ಯುಮೆಂಟ್ ವಿಷಯ ಅಥವಾ ಚಿತ್ರ ಮಾರ್ಗವನ್ನು ಹೊಂದಿದ್ದರೆ ಮತ್ತು Co-op Translator ಸಂರಚಿಸಲಾದ ಅನುವಾದ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಕರೆದುಕೊಳ್ಳಬೇಕು ಎಂದಾದರೆ provider-backed content tools ಅನ್ನು ಬಳಸಿರಿ.

Markdown ಗೆ:

1. `document`, `language_code`, ಮತ್ತು ಐಚ್ಛಿಕವಾಗಿ `source_path` ಒದಗಿಸಿ `translate_markdown_content` ಅನ್ನು ಕರೆ ಮಾಡಿ.
2. ಅನುವದಿತ ಫಲಿತಾಂಶವನ್ನು Co-op Translator ಔಟ್‌ಪುಟ್ ಲೇಔಟ್‌ಗೆ ಬರೆಯಬೇಕಾದರೆ, `rewrite_markdown_paths` ಅನ್ನು ಕರೆ ಮಾಡಿ.
3. ಕ್ಲೈಯಿಂಟ್ ಅಂತಿಮ `content` ಅನ್ನು ಬರೆಯಲಿ ಅಥವಾ ಹಿಂತಿರುಗಿಸಲಿ.

ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ:

1. ನೋಟ್ಬುಕ್ JSON ಮತ್ತು `language_code` ನೊಂದಿಗೆ `translate_notebook_content` ಅನ್ನು ಕರೆ ಮಾಡಿ.
2. ಅನುವಾದಿತ ನೋಟ್ಬುಕ್ ಲಿಂಕ್‌ಗಳು ಗುರಿ ಪಥಕ್ಕೆ ಹೊಂದಿಸಲು `rewrite_notebook_paths` ಅನ್ನು ಕರೆ ಮಾಡಿ.
3. ಅಂತಿಮ ನೋಟ್ಬುಕ್ JSON ಅನ್ನು ಬರೆಯಿರಿ ಅಥವಾ ಹಿಂತಿರುಗಿಸಿ.

ಚಿತ್ರಗಳಿಗೆ:

1. `image_path`, `language_code`, ಮತ್ತು ಐಚ್ಛಿಕವಾಗಿ `root_dir` ಅಥವಾ `fast_mode` ಒದಗಿಸಿ `translate_image_content` ಅನ್ನು ಕರೆ ಮಾಡಿ.
2. ಹಿಂತಿರುಗಿಸಲಾದ `data_base64` ಮತ್ತು `mime_type` ಅನ್ನು ಓದಿ.
3. `output_path` ಒದಗಿಸಲಾಗಿದ್ದರೆ, ಅನುವದಿತ ಚಿತ್ರವು ಆ ಪಥಕ್ಕೂ ಉಳಿಸಿಬಿಡಲಾಗಿದೆ.

ಕಂಟೆಂಟ್ ಸಾಧನಗಳು ಪ್ರಾಜೆಕ್ಟ್ ಕಂಡುಹಿಡಿತ, ಮೆಟಾಡೇಟಾ تازهಗೊಳಿಸುವಿಕೆ, ಡಿಸ್ಕ್ಲೇಮರ್‌ಗಳು, ಅಥವಾ ಸ್ವಯಂಚಾಲಿತ ಪಥ ಪುನರ್‌ಲೇಖನೆಯನ್ನು ನಿರ್ವಹಿಸುವುದಿಲ್ಲ. ನೀವು MCP ಹೋಸ್ಟ್ ಏಜೆಂಟ್ Co-op Translator LLM ಪ್ರೊವೈಡರ್ ಕ್ರೆಡೆನ್ಶಿಯಲ್ಸ್ ಇಲ್ಲದೆ Markdown ಅಥವಾ ನೋಟ್ಬುಕ್ ಚಂಕ್‌ಗಳನ್ನು ಅನುವದಿಸಲು ಬಯಸಿದರೆ, ಕೆಳಗಿನ agent-assisted ವರ್ಕ್‌ಫ್ಲೋ ಬಳಸಿ.

### Translate with the Host Agent Model

Co-op Translator ಗೆ Azure OpenAI ಅಥವಾ OpenAI ಕಾನ್ಫಿಗರ್ ಮಾಡದೆ, MCP ಹೋಸ್ಟ್ ಏಜೆಂಟ್ (ಉದಾಹರಣೆಗೆ ಕೋಡಿಂಗ್ ಸಹಾಯಕ) ಅನುವದಿತ ಪಠ್ಯವನ್ನು ಉತ್ಪಾದಿಸಬೇಕು ಎಂದಾದರೆ agent-assisted ಸಾಧನಗಳನ್ನು ಬಳಸಿ.

ಚಾಟ್ ಆಧಾರಿತ MCP ಕ್ಲೈಯಿಂಟ್‌ನಲ್ಲಿ, ಸಾಮಾನ್ಯವಾಗಿ ನೀವು ಸ್ವತಃ ಟೂಲ್ JSON ಬರೆಯಬೇಕಾಗಿಲ್ಲ. ಏಜೆಂಟ್ ಅನ್ನು agent-assisted ವರ್ಕ್‌ಫ್ಲೋ ಬಳಸಲು ಕೇಳಿ:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ hetzelfde ಮಾದರಿಯನ್ನು ಬಳಸಿ:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

ನಿಮ್ಮ MCP ಕ್ಲೈಯಿಂಟ್ ಸರ್ವರ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬೆಂಬಲಿಸಿದರೆ, `agent_assisted_markdown_translation_prompt` ಅನ್ನು ಬಳಸಿಕೊಂಡು ಕ್ಲೈಯಿಂಟ್ ಅದೇ ವರ್ಕ್‌ಫ್ಲೋ ಸೂಚನೆಗಳನ್ನು ಲೋಡ್ ಮಾಡಿಸಿಕೊಳ್ಳಿ.

Markdown ಗೆ:

1. `document`, `language_code`, ಮತ್ತು ಐಚ್ಛಿಕವಾಗಿ `source_path` ಒದಗಿಸಿ `start_markdown_agent_translation` ಅನ್ನು ಕರೆ ಮಾಡಿ.
2. ಹಿಂತಿರುಗಿಸಿದ ಪ್ರತಿ ಚಂಕ್ ಅನ್ನು ಹೋಸ್ಟ್ ಏಜೆಂಟ್‌ನಲ್ಲಿ ಚಂಕ್ `prompt` ಅನ್ನು ಅನುಸರಿಸಿ ಅನುವದಿಸಿ.
3. ಮೂಲ `job` ಮತ್ತು `chunk_id` ಮತ್ತು `translated_text` ಬಳಸಿ ಅನುವದಿತ ಚಂಕ್‌ಗಳೊಂದಿಗೆ `finish_markdown_agent_translation` ಅನ್ನು ಕರೆ ಮಾಡಿ.
4. ವಿಷಯವು ಅನುವದಿತ ಗುರಿ ಪಥಕ್ಕೆ ಬರೆಯಲಾದರೆ, `rewrite_markdown_paths` ಅನ್ನು ಕರೆ ಮಾಡಿ.

ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ:

1. ನೋಟ್ಬುಕ್ JSON ಮತ್ತು `language_code` ನೊಂದಿಗೆ `start_notebook_agent_translation` ಅನ್ನು ಕರೆ ಮಾಡಿ.
2. ಹಿಂತಿರುಗಿಸಿದ ಪ್ರತಿ ಚಂಕ್ ಅನ್ನು ಹೋಸ್ಟ್ ಏಜೆಂಟ್‌ನಲ್ಲಿ ಅನುವದಿಸಿ.
3. ಮೂಲ `job` ಮತ್ತು ಅನುವದಿತ ಚಂಕ್‌ಗಳೊಂದಿಗೆ `finish_notebook_agent_translation` ಅನ್ನು ಕರೆ ಮಾಡಿ.
4. ಅನುವದಿತ ನೋಟ್ಬುಕ್ ಲಿಂಕ್‌ಗಳು ಗುರಿ-ಪಥ ಹೊಂದಿಕೆಯಿಂದ ಬದಲಾಗಬೇಕಾದರೆ `rewrite_notebook_paths` ಅನ್ನು ಕರೆ ಮಾಡಿ.

Agent-assisted ಸಾಧನಗಳು Co-op Translator ರಿಂದ Azure OpenAI ಅಥವಾ OpenAI ಅನ್ನು ಕರೆ ಮಾಡುವುದಿಲ್ಲ. ಹೋಸ್ಟ್ ಏಜೆಂಟ್ ಹಿಂತಿರುಗಿಸಿದ ಚಂಕ್‌ಗಳನ್ನು ಅನುವದಿಸುವುದಕ್ಕಾಗಿ ಜವಾಬ್ದಾರಿಯಿದೆ. Co-op Translator Markdown ಚಂಕಿಂಗ್, placeholder ಸಂರಕ್ಷಣೆ, frontmatter ಪುನರ್ನಿರ್ಮಾಣ, ನೋಟ್ಬುಕ್ ಸೆಲ್ ಬದಲಾವಣೆ, ಮತ್ತು ಅನುವಾದದ ನಂತರ ಸಾಮಾನ್ಯೀಕರಣವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.

### Translate an Entire Repository

ಬಳಕೆದಾರರು Co-op Translator ಅನ್ನು `translate` CLI ನಂತೆ ಕೆಲಸ ಮಾಡುವಂತೆ ಬಯಸಿದರೆ `run_translation` ಬಳಸಿ.

ಸಂಗ್ರಹಣಾ ಅನುವಾದವು ಡೀಫಾಲ್ಟ್ గా `dry_run=true` ಆಗಿದೆ ಹೀಗಾಗಿ ಏಜೆಂಟ್ ಫೈಲ್ ಬದಲಾವಣೆಯ ಮುಂಚೆ ವ್ಯಾಪ್ತಿಯನ್ನು ಪರಿಶೀಲಿಸಬಹುದು:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

ಬರೆಯಲು ಅನುಮತಿ ನೀಡಲು, ಕರೆದವರು `dry_run=false` ಮತ್ತು `confirm_write=true` ಎರಡನ್ನು ಹೊಂದಿಸಬೇಕು:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` ಅನ್ನು `run_translation` ಗೆ ಹೊಂದಾಣಿಕೆಯ ಅಲಿಯಾಸ್ ಆಗಿ ಪ್ರಸ್ತುತಪಡಿಸಲಾಗಿದೆ.

### Review Translated Output

LLM ಅಥವಾ Vision ಕ್ರೆಡೆನ್ಶಿಯಲ್ಸ್ ಅನ್ನು ಅಗತ್ಯವಿಲ್ಲದೆ ನಿರ್ಧಾರಾತ್ಮಕ ಪರಿಶೀಲನೆಗಳಿಗೆ `run_review` ಬಳಸಿ:

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

ಫಲಿತಾಂಶವು ಕ್ಯಾಪ್ಚರ್ ಮಾಡಿದ ಪಠ್ಯ ಔಟ್‌ಪುಟ್ ಮತ್ತು ಲಭ್ಯವಿದ್ದಲ್ಲಿ ರಚನೆಯಾದ ಪರಿಶೀಲನೆ ಸಂಗ್ರಹವನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ.

## Manual Server Runs

ಮ್ಯಾನುಯಲ್ ರನ್‌ಗಳು ಮುಖ್ಯವಾಗಿ ಡಿಬಗಿಂಗ್ ಅಥವಾ ದೀರ್ಘಕಾಲಿಕ ಸರ್ವರ್ ರೂಪದಲ್ಲಿ ನಡೆದುಕೊಳ್ಳುವ ಟ್ರಾನ್ಸ್‌ಪೋರ್ಟ್‌ಗಳುಗಾಗಿ.

ಡೀಫಾಲ್ಟ್ stdio ಸರ್ವರ್ ಅನ್ನು ಡೀಬಗ್ ಮಾಡಿ:

```bash
co-op-translator-mcp
```

ಸೋರ್ಸ್ ಚೆಕ್ಔಟ್‌ನಿಂದ ಚಾಲನೆ ಮಾಡಿರಿ:

```bash
python -m co_op_translator.mcp.server
```

ದೀರ್ಘಕಾಲಿಕ HTTP ಅಥವಾ SSE ಸರ್ವರ್ ಓಡಿಸಿರಿ:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

ಸ್ಥಾನೀಯ ಸಂಪಾದಕ ಮತ್ತು ಏಜೆಂಟ್ ಏಕ್ಸ್ಟೈಗ್ರೇಷನ್‌ಗಳಿಗಾಗಿ, ದಯವಿಟ್ಟು Step 2 ನಲ್ಲಿರುವ ಕ್ಲೈಯಿಂಟ್-ನಿರ್ವಹಿತ `stdio` ಸಂರಚನೆವನ್ನು ಪ್ರಾಧಾನ್ಯ ನೀಡಿ.

## Tools

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

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Copy-Paste Examples

Translate Markdown content:

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

Rewrite translated Markdown links:

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

Translate Markdown with the host agent model:

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

After the host agent translates each returned chunk, finish the job with the complete `job` object returned by `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

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

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Safety Notes

- MCP tool calls are model-controlled by the host application, so repository translation is dry-run by default.
- Full repository translation can create, update, or remove many files. Require explicit user approval before setting `confirm_write=true`.
- The configuration status tool never returns API keys, endpoints, or other secret values.
- Image translation returns base64 image data. Large images can produce large tool responses.
- Agent-assisted tools return source chunks and prompts to the MCP host. Use them only with content the user is comfortable sending to that host agent model.