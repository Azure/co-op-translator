# Servidor MCP

Co-op Translator inclui um servidor Model Context Protocol para agentes, editores e clientes compatíveis com MCP.

Para a configuração local por omissão, os utilizadores não mantêm um servidor separado em execução manualmente. Configuram o seu cliente MCP, e o cliente inicia `co-op-translator-mcp` automaticamente sobre `stdio` quando precisa das ferramentas do Co-op Translator.

Se estiver a decidir entre CLI, Python API e MCP, comece com [Choose Your Workflow](workflows.md).

Use MCP quando um agente ou editor deverá chamar o Co-op Translator diretamente:

| User goal | MCP tools |
| --- | --- |
| Traduzir um documento Markdown, um notebook ou uma imagem | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Traduzir conteúdo Markdown ou de notebooks com o modelo do agente anfitrião | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Reescrever links traduzidos de Markdown ou de notebooks após escolher o caminho de saída | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Traduzir um repositório completo, tal como a CLI | `run_translation`, `translate_project` |
| Rever a saída traduzida sem credenciais de LLM | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

O servidor MCP expõe a mesma API pública em Python documentada em [API Python](api.md). As ferramentas suportadas por provedores usam os mesmos provedores configurados que a CLI e a API Python. As ferramentas assistidas por agente preparam blocos para o agente anfitrião MCP traduzir e depois usam o Co-op Translator para reconstruir o Markdown ou notebook final.

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
| Suportado por um fornecedor | O Co-op Translator chama `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, ou `run_translation`. | A tradução requer Azure OpenAI, OpenAI ou Anthropic. A tradução de imagens também requer Azure AI Vision. |
| Assistido por agente | O agente anfitrião MCP traduz os blocos devolvidos por `start_markdown_agent_translation` ou `start_notebook_agent_translation`. | Não são necessárias credenciais de provider de LLM do Co-op Translator para blocos de Markdown ou de notebook. A tradução de imagens ainda não é suportada pelo modo assistido por agente. |

Se está a começar com tradução de Markdown ou de notebooks dentro de um agente como o Codex ou o Claude Code, comece com o modo assistido por agente. Utilize o modo suportado por provedores quando quiser que o próprio Co-op Translator contacte os provedores que configurou, quando estiver a traduzir imagens, ou quando estiver a executar tradução a nível de repositório, como a CLI.

Configure um fornecedor para fluxos de trabalho suportados pelo fornecedor:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Ou OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Ou Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

A tradução de imagens suportada por fornecedor necessita também de:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    O modo assistido por agente abrange atualmente Markdown e células Markdown de notebooks. A tradução de imagens continua a utilizar o pipeline de imagens suportado por provedores e requer o Azure AI Vision para OCR e renderização sensível ao layout.

## Passo 2: Configurar o seu cliente MCP

Para a configuração local normal `stdio`, adicione o Co-op Translator à configuração do seu cliente MCP. O cliente iniciará e terminará o processo automaticamente.

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

Configuração do checkout do código-fonte no macOS ou Linux:

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

Depois de alterar a configuração do cliente MCP, reinicie ou recarregue o cliente para que este possa descobrir o novo servidor.

## Passo 3: Verificar o servidor no cliente

Peça ao cliente MCP para listar as ferramentas disponíveis, ou chame primeiro um dos auxiliares apenas de leitura:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Useful first checks:

| Tool | What to check |
| --- | --- |
| `get_api_overview` | Confirma que o servidor é acessível e mostra os fluxos de trabalho disponíveis. |
| `list_supported_languages` | Confirma que os dados de idioma empacotados podem ser carregados. |
| `get_configuration_status` | Confirma a disponibilidade do fornecedor LLM e Vision sem expor valores secretos. |

## Passo 4: Escolher um fluxo de trabalho

### Traduzir Ficheiros ou Documentos Individuais

Utilize ferramentas de conteúdo suportadas por fornecedores quando o cliente MCP já tiver o conteúdo do documento ou um caminho de imagem e o Co-op Translator deve chamar os fornecedores de tradução configurados.

For Markdown:

1. Call `translate_markdown_content` with `document`, `language_code`, and optionally `source_path`.
2. Se o resultado traduzido for escrito num layout de saída do Co-op Translator, chame `rewrite_markdown_paths`.
3. Deixe o cliente escrever ou devolver o `content` final.

For notebooks:

1. Call `translate_notebook_content` with notebook JSON and `language_code`.
2. Chame `rewrite_notebook_paths` se os links do notebook traduzido precisarem de ser ajustados para um caminho de destino.
3. Escreva ou devolva o JSON final do notebook.

For images:

1. Call `translate_image_content` with `image_path`, `language_code`, and optional `root_dir` or `fast_mode`.
2. Read the returned `data_base64` and `mime_type`.
3. Se `output_path` for fornecido, a imagem traduzida também é guardada nesse caminho.

As ferramentas de conteúdo não executam descoberta de projetos, atualizações de metadados, avisos legais, ou reescrita automática de caminhos. Se pretende que o agente anfitrião traduza fragmentos de Markdown ou notebooks sem credenciais de fornecedor LLM do Co-op Translator, utilize o fluxo de trabalho assistido por agente abaixo.

### Traduzir com o Modelo do Agente Anfitrião

Utilize ferramentas assistidas por agente quando desejar que o agente anfitrião MCP, como um assistente de programação, gere o texto traduzido em vez de configurar um fornecedor LLM para o Co-op Translator.

Num cliente MCP baseado em chat, normalmente não precisa de escrever o JSON da ferramenta sozinho. Peça ao agente para usar o fluxo de trabalho assistido por agente:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Para notebooks, utilize o mesmo padrão:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Se o seu cliente MCP suportar prompts do servidor, use `agent_assisted_markdown_translation_prompt` para que o cliente carregue as mesmas instruções do fluxo de trabalho.

For Markdown:

1. Call `start_markdown_agent_translation` with `document`, `language_code`, and optionally `source_path`.
2. Traduza cada fragmento retornado no agente anfitrião seguindo o fragmento `prompt`.
3. Call `finish_markdown_agent_translation` with the original `job` and translated chunks using `chunk_id` and `translated_text`.
4. Se o conteúdo for escrito para um caminho de destino traduzido, chame `rewrite_markdown_paths`.

For notebooks:

1. Call `start_notebook_agent_translation` with notebook JSON and `language_code`.
2. Traduza cada fragmento devolvido no agente anfitrião.
3. Call `finish_notebook_agent_translation` with the original `job` and translated chunks.
4. Chame `rewrite_notebook_paths` se os links traduzidos do notebook precisarem de ajuste do caminho de destino.

As ferramentas assistidas por agente não chamam o fornecedor de LLM configurado a partir do Co-op Translator. O agente anfitrião é responsável por traduzir os fragmentos retornados. O Co-op Translator lida com o fragmentamento de Markdown, preservação de espaços reservados, reconstrução do frontmatter, substituição de células de notebooks e normalização pós-tradução.

### Traduzir um Repositório Inteiro

Use `run_translation` quando o utilizador quiser que o Co-op Translator se comporte como a CLI `translate`.

A tradução do repositório tem como predefinição `dry_run=true` para que um agente possa inspecionar o âmbito antes das alterações aos ficheiros:

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

### Rever a Saída Traduzida

Use `run_review` para verificações determinísticas que não exigem credenciais LLM ou Vision:

!!! note "Beta"
    O MCP expõe a API beta `run_review`. É segura para fluxos de trabalho de revisão apenas de leitura, mas as verificações de revisão e os esquemas de problemas podem evoluir.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

O resultado inclui o texto capturado e um resumo de revisão estruturado quando disponível.

## Execuções manuais do servidor

As execuções manuais destinam-se principalmente à depuração ou a transportes que se comportam como servidores de longa duração.

Debug the default stdio server:

```bash
co-op-translator-mcp
```

Run from a source checkout:

```bash
python -m co_op_translator.mcp.server
```

Execute um servidor HTTP ou SSE de longa duração:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Para integrações locais com editores e agentes, prefira a configuração gerida pelo cliente `stdio` no Passo 2.

## Tools

| Tool | Purpose | Writes files |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Traduzir células Markdown no JSON do notebook. | Não |
| `translate_image_content` | Traduzir texto numa imagem e devolver dados de imagem em base64. | Opcional, apenas quando `output_path` é fornecido |
| `start_markdown_agent_translation` | Preparar fragmentos Markdown para o agente anfitrião traduzir sem credenciais LLM do Co-op Translator. | Não |
| `finish_markdown_agent_translation` | Reconstruir Markdown a partir de fragmentos traduzidos pelo agente anfitrião. | Não |
| `start_notebook_agent_translation` | Preparar fragmentos de células Markdown de um notebook para o agente anfitrião traduzir. | Não |
| `finish_notebook_agent_translation` | Reconstruir JSON do notebook a partir de fragmentos traduzidos pelo agente anfitrião. | Não |
| `rewrite_markdown_paths` | Reescrever o corpo Markdown e os caminhos de frontmatter para um destino traduzido. | Não |
| `rewrite_notebook_paths` | Reescrever caminhos dentro de células Markdown do notebook. | Não |
| `run_translation` | Executar a tradução ao nível do projeto, como a CLI. | Sim quando `dry_run=false` e `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Reportar os fornecedores LLM e Vision configurados sem expor segredos. | Não |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Descrever fluxos de trabalho e ferramentas MCP disponíveis. | Não |

## Resources

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | Visão geral em JSON dos fluxos de trabalho e ferramentas. |
| `co-op://supported-languages` | Lista em JSON dos códigos de idiomas suportados. |
| `co-op://configuration` | Resumo em JSON da disponibilidade de fornecedores sem segredos. |

## Prompts

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | Orientar um cliente MCP na tradução de conteúdo e, opcionalmente, na reescrita de caminhos. |
| `agent_assisted_markdown_translation_prompt` | Orientar um cliente MCP na tradução de Markdown pelo agente anfitrião sem credenciais do fornecedor LLM do Co-op Translator. |
| `translate_repository_prompt` | Orientar um cliente MCP na tradução de um repositório, começando por uma execução experimental (dry-run). |

## Exemplos de copiar e colar

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

Traduzir Markdown com o modelo do agente anfitrião:

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

Depois de o agente anfitrião traduzir cada fragmento retornado, finalize o trabalho com o objeto completo `job` retornado por `start_markdown_agent_translation`:

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
| O cliente MCP não consegue encontrar `co-op-translator-mcp`. | Utilize o caminho absoluto do executável Python e a configuração de checkout de origem `["-m", "co_op_translator.mcp.server"]`. |
| O servidor está listado mas a tradução falha. | Chame `get_configuration_status` e confirme que um fornecedor de LLM está disponível. |
| Pretende tradução de Markdown ou de notebooks sem credenciais de fornecedor. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` ou os equivalentes para notebooks para que o agente anfitrião traduza os fragmentos. |
| A tradução da imagem falha. | Confirme que as variáveis do Azure AI Vision estão definidas e chame `get_configuration_status`. |
| A tradução do repositório não escreve ficheiros. | Defina `dry_run=false` e `confirm_write=true` apenas após aprovação explícita do utilizador. |
| As alterações na configuração do cliente não aparecem. | Reinicie ou recarregue o cliente MCP. |

## Notas de segurança

- As chamadas de ferramentas MCP são controladas pelo modelo da aplicação anfitriã, pelo que a tradução do repositório é, por predefinição, uma execução experimental (dry-run).
- A tradução completa do repositório pode criar, atualizar ou remover muitos ficheiros. Requer aprovação explícita do utilizador antes de definir `confirm_write=true`.
- A ferramenta de estado de configuração nunca devolve chaves de API, endpoints ou outros valores secretos.
- A tradução da imagem devolve dados de imagem em base64. Imagens grandes podem gerar respostas de ferramenta de grande dimensão.
- As ferramentas assistidas por agente devolvem fragmentos de origem e prompts para o host MCP. Use-as apenas com conteúdo que o utilizador esteja confortável em enviar para esse modelo de agente do host.
