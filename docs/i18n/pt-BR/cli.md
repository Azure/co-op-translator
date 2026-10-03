# Referência da CLI

O Co-op Translator instala estes pontos de entrada de linha de comando:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Os comandos `translate`, `evaluate`, `migrate-links` e `co-op-review` são despachados através de `co_op_translator.__main__`, que seleciona a implementação do comando com base no nome do script invocado. O servidor MCP usa `co_op_translator.mcp.server` diretamente.

Se você está decidindo entre CLI, API Python e MCP, comece com [Escolha Seu Fluxo de Trabalho](workflows.md).

## Saída do Console

Terminais interativos usam a formatação Rich para o cabeçalho do comando, progresso e resumos. A saída em CI e a saída não interativa automaticamente retornam para texto simples.

Defina `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` para forçar saída simples, ou `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` para forçar saída Rich. Defina `CO_OP_TRANSLATOR_NO_PROGRESS=1` para manter resumos enquanto suprime barras de progresso ao vivo.

Use `translate --json-events progress.ndjson` quando outro sistema precisar
progresso legível por máquina. A CLI continua a renderizar saída voltada a humanos, enquanto
o arquivo NDJSON recebe eventos versionados `co-op.translation.event.v1` com
campos estáveis como `type`, `stage_key`, `completed`, `total`, e
`current_path`.

## Fluxo inicial da CLI

Comece aqui se você estiver usando o Co-op Translator a partir de um terminal:

1. Configure um provedor de LLM conforme descrito em [Configuração](configuration.md).
2. Escolha o tipo de conteúdo que você deseja traduzir.
3. Execute primeiro um comando focado, como tradução apenas de Markdown.
4. Use `--dry-run` before large repository changes.
5. Use `co-op-review` após a tradução para verificar a estrutura e a atualidade.

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expor ferramentas para um cliente MCP | Configure o [MCP Server](mcp.md) em vez de executar comandos da CLI diretamente. |

## translate

Traduza arquivos Markdown, notebooks e texto de imagens para um ou mais idiomas de destino.

```bash
translate -l "ko ja fr"
```

### Exemplos comuns

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

Atualize traduções existentes excluindo-as e recriando-as:

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

Write structured progress events:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Sim | Códigos de idioma separados por espaço, como `"es fr de"` ou `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-u`, `--update` | Não | Excluir traduções existentes para os idiomas selecionados e recriá-las. |
| `-img`, `--images` | No | Translate only image files. |
| `-md`, `--markdown` | No | Translate only Markdown files. |
| `-nb`, `--notebook` | No | Translate only Jupyter notebook files. |
| `-d`, `--debug` | Não | Habilitar logs de depuração no console. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `--json-events` | Não | Gravar eventos de progresso de tradução legíveis por máquina como NDJSON. |
| `-x`, `--fix` | Não | Retraduzir arquivos Markdown com baixa confiança com base em resultados de avaliações anteriores. |
| `-c`, `--min-confidence` | No | Confidence threshold for `--fix`. Defaults to `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Não | Adicionar ou suprimir avisos de tradução automática. Padrão: ativado na CLI. |
| `-f`, `--fast` | No | Deprecated fast image mode. |
| `-y`, `--yes` | Não | Confirmar automaticamente os prompts, útil em CI. |
| `--repo-url` | Não | URL do repositório usado no aviso de sparse-checkout da tabela de idiomas do README. |
| `--migrate-language-folders` | Não | Renomear pastas de alias legadas, como `cn` ou `tw`, para pastas canônicas BCP 47. |
| `--dry-run` | Não | Visualizar a migração de pastas de idioma e estimativas de tradução sem gravar arquivos. |

Se nenhuma flag de tipo for fornecida, `translate` processa Markdown, notebooks e imagens. A tradução de imagens requer configuração do Azure AI Vision.

## evaluate

Avaliar a qualidade do Markdown traduzido para um idioma.

!!! warning "Experimental"
    `evaluate` é experimental. Ele pode usar verificações de qualidade baseadas em regras e em LLMs, grava resultados de avaliação nos metadados de tradução, e seu modelo de pontuação e comportamento de metadados podem mudar.

```bash
evaluate -l "ko"
```

### Exemplos comuns

Use um limite de baixa confiança mais rigoroso:

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

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Single language code to evaluate. Alias codes are normalized. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `-c`, `--min-confidence` | Não | Limiar usado ao listar traduções de baixa confiança. Padrão para `0.7`. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Rule-based evaluation only. |
| `-D`, `--deep` | No | LLM-based evaluation only. |

Por padrão, `evaluate` usa tanto avaliação baseada em regras quanto baseada em LLM. Os resultados são gravados nos metadados de tradução e resumidos no console.

## co-op-review

Execute verificações determinísticas de manutenção de tradução sem credenciais de API.

!!! note "Beta"
    `co-op-review` é um comando de revisão determinístico em beta. Ele não chama provedores de modelo nem grava arquivos, mas suas verificações e o esquema de saída de problemas podem evoluir.

```bash
co-op-review -l "ko"
```

### Exemplos comuns

Revisar traduções em coreano e japonês a partir do diretório atual:

```bash
co-op-review -l "ko ja"
```

Review a specific project root:

```bash
co-op-review -l "fr" -r ./my-course
```

Revisar apenas o README após uma tradução somente do README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignora outros documentos e READMEs aninhados. Ele falha se a raiz
`README.md` estiver ausente. Combinado com `--changed-from`, ele revisa apenas o README
quando esse arquivo de origem for alterado. A tradução apenas do README deixa o README de origem
inalterado, incluindo quaisquer marcadores de seção compartilhada.

Revisar apenas os arquivos de origem alterados em relação a uma referência base:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Gerar saída em Markdown no estilo GitHub para resumos de CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Não | Código de idioma a ser revisado. Pode ser passado várias vezes ou como um valor separado por espaços. Padrão: todas as línguas de tradução descobertas. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--changed-from` | Não | Referência Git usada para limitar a revisão aos arquivos de origem alterados. |
| `--readme-only` | No | Review only the root `README.md` translation. |
| `--format` | No | Output format: `text` or `github`. Defaults to `text`. |

`co-op-review` atualmente verifica arquivos traduzidos ausentes, metadados de tradução faltantes ou obsoletos, integridade do frontmatter do Markdown e de cercas de código, JSON de notebook traduzido inválido e destinos de links locais de Markdown ou imagens ausentes. Links ausentes são avisos por padrão; problemas estruturais e de atualidade fazem o comando falhar.

## co-op-translator-mcp

Execute o servidor Co-op Translator MCP para agentes, editores e clientes compatíveis com MCP.

```bash
co-op-translator-mcp
```

O transporte padrão é `stdio`. Veja o guia [MCP Server](mcp.md) para configuração do cliente, ferramentas, recursos e notas de segurança.

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | MCP transport: `stdio`, `streamable-http`, or `sse`. Defaults to `stdio`. |

## migrate-links

Reprocesse arquivos Markdown traduzidos e atualize os links dos notebooks para que apontem para notebooks traduzidos quando disponíveis.

```bash
migrate-links -l "ko ja"
```

### Exemplos comuns

Preview link updates:

```bash
migrate-links -l "ko" --dry-run
```

Processar todos os idiomas suportados sem confirmação:

```bash
migrate-links -l "all" -y
```

Reescreva links apenas quando existirem notebooks traduzidos:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Space-separated language codes, or `"all"`. |
| `-r`, `--root-dir` | No | Project root. Defaults to the current directory. |
| `--image-dir` | No | Diretório de imagens traduzidas relativo à raiz. Padrão: `translated_images`. |
| `--dry-run` | No | Mostrar arquivos que seriam alterados sem gravar as atualizações. |
| `--fallback-to-original`, `--no-fallback-to-original` | Não | Usar links originais dos notebooks quando notebooks traduzidos estiverem ausentes. Habilitado por padrão. |
| `-d`, `--debug` | No | Enable debug logging. |
| `-s`, `--save-logs` | No | Save DEBUG-level logs under `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Confirmar automaticamente as solicitações ao processar todos os idiomas. |

## Environment

Quando um comando requer credenciais de provedor, configure um destes conjuntos de provedor. `translate --dry-run` e `co-op-review` não exigem credenciais de provedor:

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

A tradução de imagens também requer Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Layout de saída

Text translations are written under:

```text
translations/<language-code>/<original-path>
```

A saída de imagens traduzidas é gravada em:

```text
translated_images/<language-code>/<original-path>
```

For example, translating `README.md` and `docs/setup.md` into Korean produces:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Exemplos de CLI para copiar e colar

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

Pré-visualizar tradução de Markdown sem gravar arquivos:

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