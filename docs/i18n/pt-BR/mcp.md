# Servidor MCP

O Co-op Translator inclui um servidor Model Context Protocol para agentes, editores e clientes compatíveis com MCP.

Para a configuração local padrão, os usuários não precisam manter um servidor separado em execução manualmente. Eles configuram seu cliente MCP, e o cliente inicia `co-op-translator-mcp` automaticamente sobre `stdio` quando precisar das ferramentas do Co-op Translator.

Se você está decidindo entre CLI, API Python e MCP, comece por [Escolha Seu Fluxo de Trabalho](workflows.md).

Use MCP quando um agente ou editor deve chamar o Co-op Translator diretamente:

| Objetivo do usuário | Ferramentas MCP |
| --- | --- |
| Traduzir um documento Markdown, notebook ou imagem | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Traduzir conteúdo Markdown ou de notebook com o modelo agente host | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Reescrever links traduzidos de Markdown ou notebook após escolher o caminho de saída | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Traduzir um repositório inteiro como a CLI | `run_translation`, `translate_project` |
| Revisar a saída traduzida sem credenciais LLM | `run_review` |
| Inspecionar capacidades e status do ambiente | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

O servidor MCP envolve a mesma API pública em Python documentada em [API em Python](api.md). Ferramentas com suporte de provedor usam os mesmos provedores configurados que a CLI e a API Python. Ferramentas assistidas por agente preparam chunks para o agente host MCP traduzir e, em seguida, usam o Co-op Translator para reconstruir o Markdown ou notebook final.

## Etapa 1: Instale e Configure o Co-op Translator

Instale o Co-op Translator no ambiente Python que seu cliente MCP irá usar:

```bash
pip install co-op-translator
```

Para desenvolvimento local a partir deste repositório, instale o pacote no modo editável:

```bash
pip install -e .
```

Escolha o modo de tradução que seu cliente MCP irá usar:

| Modo | Use para | Credenciais |
| --- | --- | --- |
| Provider-backed | O Co-op Translator chama `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` ou `run_translation`. | A tradução requer Azure OpenAI, OpenAI ou Anthropic. Tradução de imagens também requer Azure AI Vision. |
| Agent-assisted | O agente host MCP traduz chunks retornados por `start_markdown_agent_translation` ou `start_notebook_agent_translation`. | Não são necessárias credenciais de provedor LLM do Co-op Translator para chunks de Markdown ou notebook. A tradução de imagens ainda não é coberta pelo modo assistido por agente. |

Se você está começando com tradução de Markdown ou notebook dentro de um agente como Codex ou Claude Code, comece com o modo assistido por agente. Use o modo provider-backed quando quiser que o próprio Co-op Translator chame seus provedores configurados, quando estiver traduzindo imagens ou quando estiver executando tradução em nível de repositório como a CLI.

Configure um provedor para fluxos de trabalho provider-backed:

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

A tradução de imagens com suporte de provedor adicionalmente precisa de:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    O modo assistido por agente atualmente cobre Markdown e células Markdown de notebook. A tradução de imagens ainda usa o pipeline de imagem com suporte de provedor e requer Azure AI Vision para OCR e renderização com consciência de layout.

## Etapa 2: Configure Seu Cliente MCP

Para a configuração normal local `stdio`, adicione o Co-op Translator à configuração do seu cliente MCP. O cliente iniciará e encerrará o processo automaticamente.

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

Configuração de checkout de origem no Windows:

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

Configuração de checkout de origem no macOS ou Linux:

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

## Etapa 3: Verifique o Servidor no Cliente

Peça ao cliente MCP para listar as ferramentas disponíveis ou chame um dos auxiliares somente leitura primeiro:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Verificações iniciais úteis:

| Ferramenta | O que verificar |
| --- | --- |
| `get_api_overview` | Confirma que o servidor está acessível e mostra fluxos de trabalho disponíveis. |
| `list_supported_languages` | Confirma que os dados de idiomas empacotados podem ser carregados. |
| `get_configuration_status` | Confirma disponibilidade de provedores LLM e Vision sem expor valores secretos. |

## Etapa 4: Escolha um Fluxo de Trabalho

### Traduzir Arquivos ou Documentos Individuais

Use as ferramentas de conteúdo provider-backed quando o cliente MCP já tiver o conteúdo do documento ou o caminho da imagem e o Co-op Translator deve chamar os provedores de tradução configurados.

Para Markdown:

1. Chame `translate_markdown_content` com `document`, `language_code` e opcionalmente `source_path`.
2. Se o resultado traduzido for gravado em um layout de saída do Co-op Translator, chame `rewrite_markdown_paths`.
3. Deixe o cliente gravar ou retornar o `content` final.

Para notebooks:

1. Chame `translate_notebook_content` com o JSON do notebook e `language_code`.
2. Chame `rewrite_notebook_paths` se os links do notebook traduzido precisarem ser ajustados para um caminho de destino.
3. Grave ou retorne o JSON final do notebook.

Para imagens:

1. Chame `translate_image_content` com `image_path`, `language_code` e opcionalmente `root_dir` ou `fast_mode`.
2. Leia o `data_base64` e `mime_type` retornados.
3. Se `output_path` for fornecido, a imagem traduzida também é salva nesse caminho.

As ferramentas de conteúdo não realizam descoberta de projeto, atualizações de metadados, avisos ou reescritas automáticas de caminho. Se você quiser que o agente host traduza chunks de Markdown ou notebook sem credenciais de provedor LLM do Co-op Translator, use o fluxo assistido por agente abaixo.

### Traduzir com o Modelo Agente Host

Use as ferramentas assistidas por agente quando quiser que o agente host MCP, como um assistente de codificação, produza o texto traduzido em vez de configurar um provedor LLM para o Co-op Translator.

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

Se seu cliente MCP suportar prompts de servidor, use `agent_assisted_markdown_translation_prompt` para que o cliente carregue as mesmas instruções do fluxo de trabalho.

Para Markdown:

1. Chame `start_markdown_agent_translation` com `document`, `language_code` e opcionalmente `source_path`.
2. Traduza cada chunk retornado no agente host seguindo o `prompt` do chunk.
3. Chame `finish_markdown_agent_translation` com o `job` original e os chunks traduzidos usando `chunk_id` e `translated_text`.
4. Se o conteúdo for gravado em um caminho de destino traduzido, chame `rewrite_markdown_paths`.

Para notebooks:

1. Chame `start_notebook_agent_translation` com o JSON do notebook e `language_code`.
2. Traduza cada chunk retornado no agente host.
3. Chame `finish_notebook_agent_translation` com o `job` original e os chunks traduzidos.
4. Chame `rewrite_notebook_paths` se os links do notebook traduzido precisarem de ajuste para o caminho de destino.

As ferramentas assistidas por agente não chamam o provedor LLM configurado do Co-op Translator. O agente host é responsável por traduzir os chunks retornados. O Co-op Translator lida com chunking de Markdown, preservação de placeholders, reconstrução de frontmatter, substituição de células de notebook e normalização pós-tradução.

### Traduzir um Repositório Inteiro

Use `run_translation` quando o usuário quiser que o Co-op Translator se comporte como a CLI `translate`.

A tradução de repositório padrão é `dry_run=true` para que um agente possa inspecionar o escopo antes de alterações nos arquivos:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

O resultado de `run_translation` inclui um array `events` com eventos de progresso versionados
`co-op.translation.event.v1`. Clientes MCP devem usar campos como
`type`, `stage_key`, `completed`, `total` e `current_path` em vez de
analisar texto capturado do console. Passe `json_events_path` para também gravar esses eventos
em um arquivo NDJSON.

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

### Revisar Saída Traduzida

Use `run_review` para verificações determinísticas que não exigem credenciais LLM ou Vision:

!!! note "Beta"
    O MCP expõe a API beta `run_review`. É segura para fluxos de trabalho de revisão somente leitura, mas as verificações de revisão e os esquemas de problemas podem evoluir.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

O resultado inclui saída de texto capturada e um resumo de revisão estruturado quando disponível.

## Execuções Manuais do Servidor

Execuções manuais são principalmente para depuração ou para transportes que se comportam como servidores de longa duração.

Depure o servidor stdio padrão:

```bash
co-op-translator-mcp
```

Execute a partir de um checkout de origem:

```bash
python -m co_op_translator.mcp.server
```

Execute um servidor HTTP ou SSE de longa duração:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Para integrações locais de editor e agente, prefira a configuração `stdio` gerenciada pelo cliente na Etapa 2.

## Ferramentas

| Ferramenta | Propósito | Grava arquivos |
| --- | --- | --- |
| `translate_markdown_content` | Traduz uma string Markdown. | Não |
| `translate_notebook_content` | Traduz células Markdown no JSON do notebook. | Não |
| `translate_image_content` | Traduz texto em uma imagem e retorna dados de imagem em base64. | Opcional, somente quando `output_path` for fornecido |
| `start_markdown_agent_translation` | Prepara chunks de Markdown para o agente host traduzir sem credenciais LLM do Co-op Translator. | Não |
| `finish_markdown_agent_translation` | Reconstrói o Markdown a partir de chunks traduzidos pelo agente host. | Não |
| `start_notebook_agent_translation` | Prepara chunks de células Markdown do notebook para o agente host traduzir. | Não |
| `finish_notebook_agent_translation` | Reconstrói o JSON do notebook a partir de chunks traduzidos pelo agente host. | Não |
| `rewrite_markdown_paths` | Reescreve o corpo e os caminhos de frontmatter do Markdown para um destino traduzido. | Não |
| `rewrite_notebook_paths` | Reescreve caminhos dentro de células Markdown do notebook. | Não |
| `run_translation` | Executa tradução em nível de projeto como a CLI. | Sim quando `dry_run=false` e `confirm_write=true` |
| `translate_project` | Alias de compatibilidade para `run_translation`. | Sim quando `dry_run=false` e `confirm_write=true` |
| `run_review` | Executa verificações de revisão determinísticas. | Não |
| `get_configuration_status` | Relata provedores LLM e Vision configurados sem expor segredos. | Não |
| `list_supported_languages` | Lista códigos de idioma alvo suportados. | Não |
| `get_api_overview` | Descreve fluxos de trabalho e ferramentas MCP disponíveis. | Não |

## Recursos

| URI de Recurso | Propósito |
| --- | --- |
| `co-op://api` | Visão geral JSON de fluxos de trabalho e ferramentas. |
| `co-op://supported-languages` | Lista JSON de códigos de idiomas suportados. |
| `co-op://configuration` | Resumo JSON de disponibilidade de provedores sem segredos. |

## Prompts

| Prompt | Propósito |
| --- | --- |
| `translate_markdown_document_prompt` | Orienta um cliente MCP através da tradução de conteúdo mais reescrita opcional de caminhos. |
| `agent_assisted_markdown_translation_prompt` | Orienta um cliente MCP através da tradução de Markdown pelo agente host sem credenciais de provedor LLM do Co-op Translator. |
| `translate_repository_prompt` | Orienta um cliente MCP através da tradução do repositório com dry-run primeiro. |

## Exemplos de Copiar-Colar

Traduzir conteúdo Markdown:

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

Reescrever links de Markdown traduzidos:

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

Traduzir Markdown com o modelo agente host:

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

Após o agente host traduzir cada chunk retornado, finalize o job com o objeto `job` completo retornado por `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Visualizar a tradução do repositório:

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

## Solução de Problemas

| Problema | O que tentar |
| --- | --- |
| O cliente MCP não consegue encontrar `co-op-translator-mcp`. | Use o caminho absoluto do executável Python e a configuração de checkout de origem `["-m", "co_op_translator.mcp.server"]`. |
| O servidor está listado mas a tradução falha. | Chame `get_configuration_status` e confirme que um provedor LLM está disponível. |
| Você quer tradução de Markdown ou notebook sem credenciais de provedor. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` ou os equivalentes para notebook para que o agente host traduza os chunks. |
| A tradução de imagem falha. | Confirme que as variáveis do Azure AI Vision estão definidas e chame `get_configuration_status`. |
| A tradução de repositório não grava arquivos. | Defina `dry_run=false` e `confirm_write=true` somente após aprovação explícita do usuário. |
| Alterações na configuração do cliente não aparecem. | Reinicie ou recarregue o cliente MCP. |

## Notas de Segurança

- As chamadas de ferramenta MCP são controladas pelo modelo da aplicação host, portanto a tradução de repositório é dry-run por padrão.
- A tradução completa de repositório pode criar, atualizar ou remover muitos arquivos. Exija aprovação explícita do usuário antes de definir `confirm_write=true`.
- A ferramenta de status de configuração nunca retorna chaves de API, endpoints ou outros valores secretos.
- A tradução de imagens retorna dados de imagem em base64. Imagens grandes podem produzir respostas de ferramenta volumosas.
- As ferramentas assistidas por agente retornam chunks de origem e prompts para o host MCP. Use-as apenas com conteúdo que o usuário esteja confortável em enviar para esse modelo agente host.