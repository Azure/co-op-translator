# Servidor MCP

Co-op Translator inclui um servidor Model Context Protocol para agentes, editores e clientes compatíveis com MCP.

Para a configuração local padrão, os utilizadores não mantêm um servidor separado em execução manualmente. Eles configuram o seu cliente MCP, e o cliente inicia `co-op-translator-mcp` automaticamente sobre `stdio` quando precisa das ferramentas Co-op Translator.

Se estiver a decidir entre CLI, Python API e MCP, comece com [Escolha o Seu Fluxo de Trabalho](workflows.md).

Use MCP quando um agente ou editor deve chamar o Co-op Translator diretamente:

| User goal | MCP tools |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

O servidor MCP envolve a mesma API pública Python documentada em [Python API](api.md). As ferramentas suportadas por providers usam os mesmos providers configurados que a CLI e a Python API. As ferramentas assistidas por agente preparam segmentos para o agente host MCP traduzir e depois usam o Co-op Translator para reconstruir o Markdown ou o notebook final.

## Passo 1: Instalar e Configurar o Co-op Translator

Instale o Co-op Translator no ambiente Python que o seu cliente MCP irá usar:

```bash
pip install co-op-translator
```

Para desenvolvimento local a partir deste repositório, instale o pacote em modo editável:

```bash
pip install -e .
```

Escolha o modo de tradução que o seu cliente MCP irá usar:

| Mode | Use this for | Credentials |
| --- | --- | --- |
| Provider-backed | Co-op Translator calls `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, or `run_translation`. | Markdown and notebook translation require Azure OpenAI or OpenAI. Image translation also requires Azure AI Vision. |
| Agent-assisted | The MCP host agent translates chunks returned by `start_markdown_agent_translation` or `start_notebook_agent_translation`. | No Co-op Translator LLM provider credentials are required for Markdown or notebook chunks. Image translation is not covered by agent-assisted mode yet. |

Se está a começar com tradução de Markdown ou notebooks dentro de um agente como Codex ou Claude Code, comece em modo assistido por agente. Use o modo suportado por providers quando quiser que o próprio Co-op Translator chame os seus providers configurados, quando estiver a traduzir imagens, ou quando estiver a executar tradução ao nível do repositório como a CLI.

Configure credenciais de providers apenas para fluxos de trabalho suportados por providers:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

A tradução de imagens suportada por providers adicionalmente necessita:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Passo 2: Configurar o Seu Cliente MCP

Para a configuração normal local `stdio`, adicione o Co-op Translator à configuração do seu cliente MCP. O cliente irá iniciar e terminar o processo automaticamente.

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

Configuração a partir do checkout do código-fonte no Windows:

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

Configuração a partir do checkout do código-fonte no macOS ou Linux:

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

Após alterar a configuração do cliente MCP, reinicie ou recarregue o cliente para que possa descobrir o novo servidor.

## Passo 3: Verificar o Servidor no Cliente

Peça ao cliente MCP para listar as ferramentas disponíveis, ou chame um dos auxiliares somente leitura primeiro:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Verificações úteis iniciais:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Confirms the server is reachable and shows available workflows. |
| `list_supported_languages` | Confirms packaged language data can be loaded. |
| `get_configuration_status` | Confirms LLM and Vision provider availability without exposing secret values. |

## Passo 4: Escolher um Fluxo de Trabalho

### Traduzir Ficheiros ou Documentos Individuais

Use as ferramentas de conteúdo suportadas por providers quando o cliente MCP já tem o conteúdo do documento ou um caminho de imagem e o Co-op Translator deve chamar os providers de tradução configurados.

Para Markdown:

1. Chame `translate_markdown_content` com `document`, `language_code` e opcionalmente `source_path`.
2. Se o resultado traduzido for escrito num layout de output do Co-op Translator, chame `rewrite_markdown_paths`.
3. Deixe o cliente escrever ou retornar o `content` final.

Para notebooks:

1. Chame `translate_notebook_content` com o JSON do notebook e `language_code`.
2. Chame `rewrite_notebook_paths` se os links do notebook traduzido precisarem de ser ajustados para um caminho de destino.
3. Escreva ou retorne o JSON final do notebook.

Para imagens:

1. Chame `translate_image_content` com `image_path`, `language_code` e opcional `root_dir` ou `fast_mode`.
2. Leia o `data_base64` e o `mime_type` retornados.
3. Se `output_path` for fornecido, a imagem traduzida também será guardada nesse caminho.

As ferramentas de conteúdo não realizam descoberta de projeto, atualizações de metadados, avisos legais, ou reescrita automática de caminhos. Se quiser que o agente host traduza segmentos de Markdown ou notebook sem credenciais de provider LLM do Co-op Translator, use o fluxo assistido por agente abaixo.

### Traduzir com o Modelo do Agente Host

Use as ferramentas assistidas por agente quando quiser que o agente host MCP, tal como um assistente de programação, produza o texto traduzido em vez de configurar Azure OpenAI ou OpenAI para o Co-op Translator.

Num cliente MCP baseado em chat, normalmente não é necessário escrever o JSON da ferramenta você mesmo. Peça ao agente para usar o fluxo assistido por agente:

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

Se o seu cliente MCP suportar server prompts, use `agent_assisted_markdown_translation_prompt` para fazer o cliente carregar as mesmas instruções de fluxo de trabalho.

Para Markdown:

1. Chame `start_markdown_agent_translation` com `document`, `language_code`, e opcionalmente `source_path`.
2. Traduza cada segmento retornado no agente host seguindo o `prompt` do segmento.
3. Chame `finish_markdown_agent_translation` com o `job` original e segmentos traduzidos usando `chunk_id` e `translated_text`.
4. Se o conteúdo for escrito para um caminho alvo traduzido, chame `rewrite_markdown_paths`.

Para notebooks:

1. Chame `start_notebook_agent_translation` com o JSON do notebook e `language_code`.
2. Traduza cada segmento retornado no agente host.
3. Chame `finish_notebook_agent_translation` com o `job` original e segmentos traduzidos.
4. Chame `rewrite_notebook_paths` se os links do notebook traduzido precisarem de ajuste de caminho de destino.

As ferramentas assistidas por agente não chamam Azure OpenAI ou OpenAI a partir do Co-op Translator. O agente host é responsável por traduzir os segmentos retornados. O Co-op Translator lida com chunking de Markdown, preservação de espaços reservados, reconstrução de frontmatter, substituição de células de notebook e normalização pós-tradução.

### Traduzir um Repositório Inteiro

Use `run_translation` quando o utilizador quiser que o Co-op Translator se comporte como a CLI `translate`.

A tradução de repositório tem por defeito `dry_run=true` para que um agente possa inspecionar o âmbito antes de alterações aos ficheiros:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Para permitir escritas, o chamador deve definir ambos `dry_run=false` e `confirm_write=true`:

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

### Rever Output Traduzido

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

O resultado inclui output de texto capturado e um resumo estruturado da revisão quando disponível.

## Execuções Manuais do Servidor

As execuções manuais são principalmente para depuração ou para transportes que se comportam como servidores de longa duração.

Debug do servidor stdio por defeito:

```bash
co-op-translator-mcp
```

Executar a partir de um checkout do código-fonte:

```bash
python -m co_op_translator.mcp.server
```

Executar um servidor HTTP ou SSE de longa duração:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Para integrações locais com editores e agentes, prefira a configuração `stdio` gerida pelo cliente no Passo 2.

## Ferramentas

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

## Recursos

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

## Exemplos de Copiar-Colar

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

## Resolução de Problemas

| Problem | What to try |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Notas de Segurança

- MCP tool calls are model-controlled by the host application, so repository translation is dry-run by default.
- Full repository translation can create, update, or remove many files. Require explicit user approval before setting `confirm_write=true`.
- The configuration status tool never returns API keys, endpoints, or other secret values.
- Image translation returns base64 image data. Large images can produce large tool responses.
- Agent-assisted tools return source chunks and prompts to the MCP host. Use them only with content the user is comfortable sending to that host agent model.