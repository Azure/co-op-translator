# CLI Reference

Co-op Translator instala estes pontos de entrada de linha de comando:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

O servidor MCP usa `co_op_translator.mcp.server` diretamente.

Se você está decidindo entre CLI, API Python e MCP, comece por [Escolha seu fluxo de trabalho](workflows.md).

## First-Time CLI Flow

Comece aqui se você estiver usando o Co-op Translator a partir de um terminal:

1. Configure um provedor de LLM conforme descrito em [Configuration](configuration.md).
2. Escolha o tipo de conteúdo que deseja traduzir.
3. Execute um comando focado primeiro, como tradução somente de Markdown.
4. Use `--dry-run` antes de grandes alterações no repositório.
5. Use `co-op-review` após a tradução para verificar estrutura e atualidade.

| Objetivo | Comando para começar |
| --- | --- |
| Traduzir documentos Markdown | `translate -l "ko" -md` |
| Traduzir notebooks | `translate -l "ko" -nb` |
| Traduzir texto em imagens | `translate -l "ko" -img` |
| Visualizar trabalho sem gravar arquivos | `translate -l "ko" -md --dry-run` |
| Revisar traduções existentes | `co-op-review -l "ko"` |
| Atualizar links de notebook e Markdown | `migrate-links -l "ko" --dry-run` |
| Expor ferramentas para um cliente MCP | Configure o [Servidor MCP](mcp.md) em vez de executar comandos da CLI diretamente. |

## translate

Translate Markdown files, notebooks, and image text into one or more target languages.

```bash
translate -l "ko ja fr"
```

### Common examples

Translate only Markdown:

```bash
translate -l "de" -md
```

Translate only notebooks:

```bash
translate -l "zh-CN" -nb
```

Translate Markdown and images:

```bash
translate -l "pt-BR" -md -img
```

Update existing translations by deleting and recreating them:

```bash
translate -l "ko" -u
```

Run without interactive prompts:

```bash
translate -l "ko ja" -md -y
```

Save logs:

```bash
translate -l "ko" -s
```

### Options

| Opção | Obrigatório | Descrição |
| --- | --- | --- |
| `-l`, `--language-codes` | Sim | Códigos de idioma separados por espaço, como `"es fr de"`, ou `"all"`. |
| `-r`, `--root-dir` | Não | Raiz do projeto. Padrão para o diretório atual. |
| `-u`, `--update` | Não | Exclui traduções existentes para os idiomas selecionados e as recria. |
| `-img`, `--images` | Não | Traduz apenas arquivos de imagem. |
| `-md`, `--markdown` | Não | Traduz apenas arquivos Markdown. |
| `-nb`, `--notebook` | Não | Traduz apenas arquivos de notebook Jupyter. |
| `-d`, `--debug` | Não | Habilita logging de depuração no console. |
| `-s`, `--save-logs` | Não | Salva logs em nível DEBUG em `<root-dir>/logs/`. |
| `-x`, `--fix` | Não | Retraduz arquivos Markdown de baixa confiança com base em resultados de avaliação anteriores. |
| `-c`, `--min-confidence` | Não | Limite de confiança para `--fix`. Padrão é `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Não | Adiciona ou suprime avisos de tradução automática. Habilitado por padrão na CLI. |
| `-f`, `--fast` | Não | Modo rápido de imagem obsoleto. |
| `-y`, `--yes` | Não | Confirma automaticamente prompts, útil em CI. |
| `--repo-url` | Não | URL do repositório usado no aviso de sparse-checkout da tabela de idiomas do README. |
| `--migrate-language-folders` | Não | Renomeia pastas de alias legadas, como `cn` ou `tw`, para pastas canônicas BCP 47. |
| `--dry-run` | Não | Visualiza a migração de pastas de idioma e estimativas de tradução sem gravar arquivos. |

If no type flag is provided, `translate` processes Markdown, notebooks, and images. Image translation requires Azure AI Vision configuration.

## evaluate

Evaluate translated Markdown quality for one language.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Common examples

Use a stricter low-confidence threshold:

```bash
evaluate -l "es" -c 0.8
```

Run rule-based checks only:

```bash
evaluate -l "fr" -f
```

Run LLM-based checks only:

```bash
evaluate -l "ja" -D
```

### Options

| Opção | Obrigatório | Descrição |
| --- | --- | --- |
| `-l`, `--language-code` | Sim | Código de idioma único a ser avaliado. Códigos alias são normalizados. |
| `-r`, `--root-dir` | Não | Raiz do projeto. Padrão para o diretório atual. |
| `-c`, `--min-confidence` | Não | Limite usado ao listar traduções de baixa confiança. Padrão é `0.7`. |
| `-d`, `--debug` | Não | Habilita logging de depuração. |
| `-s`, `--save-logs` | Não | Salva logs em nível DEBUG em `<root-dir>/logs/`. |
| `-f`, `--fast` | Não | Apenas avaliação baseada em regras. |
| `-D`, `--deep` | Não | Apenas avaliação baseada em LLM. |

Por padrão, `evaluate` usa tanto avaliação baseada em regras quanto baseada em LLM. Os resultados são gravados nos metadados de tradução e resumidos no console.

## co-op-review

Run deterministic translation maintenance checks without API credentials.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Common examples

Review Korean and Japanese translations from the current directory:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Review only source files changed against a base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Print GitHub-flavored Markdown output for CI summaries:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Opção | Obrigatório | Descrição |
| --- | --- | --- |
| `-l`, `--language-code` | Não | Código de idioma para revisar. Pode ser passado múltiplas vezes ou como um valor separado por espaços. Padrão para todos os idiomas de tradução descobertos. |
| `-r`, `--root-dir` | Não | Raiz do projeto. Padrão para o diretório atual. |
| `--changed-from` | Não | Ref Git usado para limitar a revisão a arquivos de origem alterados. |
| `--format` | Não | Formato de saída: `text` ou `github`. Padrão é `text`. |

`co-op-review` atualmente verifica arquivos traduzidos ausentes, metadados de tradução ausentes ou desatualizados, integridade de frontmatter e cercas de código em Markdown, JSON de notebooks traduzidos inválido e alvos locais de links Markdown ou de imagem ausentes. Links faltantes são avisos por padrão; problemas de estrutura e atualidade fazem o comando falhar.

## co-op-translator-mcp

Run the Co-op Translator MCP server for agents, editors, and MCP-compatible clients.

```bash
co-op-translator-mcp
```

The default transport is `stdio`. See the [MCP Server](mcp.md) guide for client configuration, tools, resources, and safety notes.

### Options

| Opção | Obrigatório | Descrição |
| --- | --- | --- |
| `--transport` | Não | Transporte MCP: `stdio`, `streamable-http`, ou `sse`. Padrão é `stdio`. |

## migrate-links

Reprocess translated Markdown files and update notebook links so they point to translated notebooks when available.

```bash
migrate-links -l "ko ja"
```

### Common examples

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

Process all supported languages without confirmation:

```bash
migrate-links -l "all" -y
```

Only rewrite links when translated notebooks exist:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Opção | Obrigatório | Descrição |
| --- | --- | --- |
| `-l`, `--language-codes` | Sim | Códigos de idioma separados por espaço, ou `"all"`. |
| `-r`, `--root-dir` | Não | Raiz do projeto. Padrão para o diretório atual. |
| `--image-dir` | Não | Diretório de imagens traduzidas relativo à raiz. Padrão é `translated_images`. |
| `--dry-run` | Não | Mostra arquivos que seriam alterados sem escrever atualizações. |
| `--fallback-to-original`, `--no-fallback-to-original` | Não | Usa links de notebook originais quando notebooks traduzidos estiverem ausentes. Habilitado por padrão. |
| `-d`, `--debug` | Não | Habilita logging de depuração. |
| `-s`, `--save-logs` | Não | Salva logs em nível DEBUG em `<root-dir>/logs/`. |
| `-y`, `--yes` | Não | Confirma automaticamente prompts ao processar todos os idiomas. |

## Environment

All commands require one configured LLM provider:

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
```

Image translation additionally requires Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

Translated image output is written under:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

Translate Markdown into three languages:

```bash
translate -l "ko ja fr" -md
```

Translate notebooks only:

```bash
translate -l "zh-CN" -nb
```

Translate images only:

```bash
translate -l "pt-BR" -img
```

Preview Markdown translation without writing files:

```bash
translate -l "de es" -md --dry-run
```

Repair low-confidence Markdown translations:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Run CI-friendly Markdown translation:

```bash
translate -l "ko ja" -md -y -s
```

Review translated output:

```bash
co-op-review -l "ko ja"
```

Preview link migration:

```bash
migrate-links -l "ko" --dry-run
```