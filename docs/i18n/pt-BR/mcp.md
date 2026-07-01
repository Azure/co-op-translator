# MCP Server

Co-op Translator inclui um servidor Model Context Protocol para agentes, editores e clientes compatíveis com MCP.

Para a configuração local padrão, os usuários não precisam manter um servidor separado em execução manualmente. Eles configuram seu cliente MCP, e o cliente inicia `co-op-translator-mcp` automaticamente via `stdio` quando precisa das ferramentas do Co-op Translator.

Se você está decidindo entre CLI, API Python e MCP, comece por [Escolha Seu Fluxo de Trabalho](workflows.md).

Use MCP quando um agente ou editor deve chamar o Co-op Translator diretamente:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

O servidor MCP encapsula a mesma API pública em Python documentada em [Python API](api.md). As ferramentas que usam provedores configurados utilizam os mesmos provedores configurados que a CLI e a API Python. As ferramentas assistidas por agente preparam blocos para o agente host MCP traduzir e, em seguida, usam o Co-op Translator para reconstruir o Markdown ou notebook final.

## Step 1: Install and Configure Co-op Translator

Instale o Co-op Translator no ambiente Python que seu cliente MCP irá usar:

```bash
pip install co-op-translator
```

Para desenvolvimento local a partir deste repositório, instale o pacote em modo editável:

```bash
pip install -e .
```

Escolha o modo de tradução que seu cliente MCP irá usar:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

Se você está começando com tradução de Markdown ou notebooks dentro de um agente como Codex ou Claude Code, comece no modo assistido por agente. Use o modo provider-backed quando você quiser que o próprio Co-op Translator chame seus provedores configurados, quando estiver traduzindo imagens ou quando estiver executando tradução em nível de repositório como a CLI.

Configure credenciais de provedores apenas para fluxos de trabalho provider-backed:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

A tradução de imagem com provider-backed adicionalmente precisa de:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Step 2: Configure Your MCP Client

Para a configuração normal local via `stdio`, adicione o Co-op Translator à configuração do seu cliente MCP. O cliente irá iniciar e parar o processo automaticamente.

Configuração do pacote instalado:

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

Configuração do checkout da fonte no Windows:

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

Configuração do checkout da fonte no macOS ou Linux:

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

Após alterar a configuração do cliente MCP, reinicie ou recarregue o cliente para que ele possa descobrir o novo servidor.

## Step 3: Verify the Server in the Client

Peça ao cliente MCP para listar as ferramentas disponíveis, ou chame primeiro um dos auxiliares somente leitura:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Verificações iniciais úteis:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Confirma que o servidor está alcançável e mostra fluxos de trabalho disponíveis. |
| `list_supported_languages` | Confirma que os dados de idioma empacotados podem ser carregados. |
| `get_configuration_status` | Confirma a disponibilidade de provedores LLM e Vision sem expor valores secretos. |

## Step 4: Choose a Workflow

### Translate Individual Files or Documents

Use as ferramentas de conteúdo provider-backed quando o cliente MCP já possui o conteúdo do documento ou o caminho da imagem e o Co-op Translator deve chamar os provedores de tradução configurados.

Para Markdown:

1. Chame `translate_markdown_content` com `document`, `language_code` e opcionalmente `source_path`.
2. Se o resultado traduzido for escrito em um layout de saída do Co-op Translator, chame `rewrite_markdown_paths`.
3. Deixe o cliente gravar ou retornar o `content` final.

Para notebooks:

1. Chame `translate_notebook_content` com o JSON do notebook e `language_code`.
2. Chame `rewrite_notebook_paths` se os links do notebook traduzido precisarem ser ajustados para um caminho de destino.
3. Grave ou retorne o JSON final do notebook.

Para imagens:

1. Chame `translate_image_content` com `image_path`, `language_code` e opcionalmente `root_dir` ou `fast_mode`.
2. Leia o `data_base64` retornado e o `mime_type`.
3. Se `output_path` for fornecido, a imagem traduzida também é salva nesse caminho.

As ferramentas de conteúdo não realizam descoberta de projeto, atualizações de metadados, avisos legais ou reescrita automática de caminhos. Se você quiser que o agente host traduza blocos de Markdown ou notebook sem credenciais de provedor LLM do Co-op Translator, use o fluxo assistido por agente abaixo.

### Translate with the Host Agent Model

Use as ferramentas assistidas por agente quando você quiser que o agente host MCP, como um assistente de programação, produza o texto traduzido em vez de configurar Azure OpenAI ou OpenAI para o Co-op Translator.

Em um cliente MCP baseado em chat, normalmente você não precisa escrever o JSON da ferramenta manualmente. Peça ao agente para usar o fluxo assistido por agente:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Para notebooks, use o mesmo padrão:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Se seu cliente MCP suportar prompts de servidor, use `agent_assisted_markdown_translation_prompt` para fazer o cliente carregar as mesmas instruções do fluxo de trabalho.

Para Markdown:

1. Chame `start_markdown_agent_translation` com `document`, `language_code` e opcionalmente `source_path`.
2. Traduza cada bloco retornado no agente host seguindo o `prompt` do bloco.
3. Chame `finish_markdown_agent_translation` com o `job` original e os blocos traduzidos usando `chunk_id` e `translated_text`.
4. Se o conteúdo for escrito em um caminho de destino traduzido, chame `rewrite_markdown_paths`.

Para notebooks:

1. Chame `start_notebook_agent_translation` com o JSON do notebook e `language_code`.
2. Traduza cada bloco retornado no agente host.
3. Chame `finish_notebook_agent_translation` com o `job` original e os blocos traduzidos.
4. Chame `rewrite_notebook_paths` se os links do notebook traduzido precisarem de ajuste de caminho de destino.

As ferramentas assistidas por agente não chamam Azure OpenAI ou OpenAI a partir do Co-op Translator. O agente host é responsável por traduzir os blocos retornados. O Co-op Translator lida com fragmentação de Markdown, preservação de espaços reservados, reconstrução de frontmatter, substituição de células de notebook e normalização pós-tradução.

### Translate an Entire Repository

Use `run_translation` quando o usuário desejar que o Co-op Translator se comporte como a CLI `translate`.

A tradução de repositório tem `dry_run=true` por padrão para que um agente possa inspecionar o escopo antes das alterações de arquivos:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Para permitir gravações, o chamador deve definir tanto `dry_run=false` quanto `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` é exposto como um alias de compatibilidade para `run_translation`.

### Review Translated Output

Use `run_review` para verificações determinísticas que não requerem credenciais LLM ou Vision:

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

O resultado inclui a saída de texto capturada e um resumo de revisão estruturado quando disponível.

## Manual Server Runs

Execuções manuais são principalmente para depuração ou para transportes que se comportam como servidores de longa execução.

Debug o servidor stdio padrão:

```bash
co-op-translator-mcp
```

Execute a partir de um checkout da fonte:

```bash
python -m co_op_translator.mcp.server
```

Execute um servidor HTTP ou SSE de longa duração:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Para integrações locais de editores e agentes, prefira a configuração `stdio` gerenciada pelo cliente no Passo 2.

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