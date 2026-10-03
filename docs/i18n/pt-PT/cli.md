# Referência da CLI

O Co-op Translator instala estes pontos de entrada de linha de comando:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Os comandos `translate`, `evaluate`, `migrate-links` e `co-op-review` são encaminhados através de `co_op_translator.__main__`, que selecciona a implementação do comando com base no nome do script invocado. O servidor MCP usa `co_op_translator.mcp.server` directamente.

Se estiver a decidir entre a CLI, a API Python e o MCP, comece por [Escolha o seu fluxo de trabalho](workflows.md).

## Saída da consola

Os terminais interativos utilizam a formatação Rich para o cabeçalho do comando, progresso e sumários. As saídas em CI e não interactivas passam automaticamente para texto simples.

Defina `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` para forçar saída em texto simples, ou `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` para forçar saída Rich. Defina `CO_OP_TRANSLATOR_NO_PROGRESS=1` para manter os sumários enquanto suprime as barras de progresso em directo.

Use `translate --json-events progress.ndjson` quando outro sistema necessitar de progresso legível por máquina. A CLI continua a apresentar saída para utilizadores humanos, enquanto o ficheiro NDJSON recebe eventos versionados `co-op.translation.event.v1` com campos estáveis como `type`, `stage_key`, `completed`, `total` e `current_path`.





## Fluxo inicial da CLI

Comece aqui se estiver a utilizar o Co-op Translator a partir de um terminal:

1. Configure um fornecedor LLM conforme descrito em [Configuração](configuration.md).
2. Escolha o tipo de conteúdo que pretende traduzir.
3. Execute primeiro um comando focado, como a tradução apenas de Markdown.
4. Use `--dry-run` antes de alterações grandes no repositório.
5. Utilize `co-op-review` após a tradução para verificar a estrutura e a actualidade.

| Objetivo | Comando para começar |
| --- | --- |
| Traduzir documentos Markdown | `translate -l "ko" -md` |
| Traduzir notebooks | `translate -l "ko" -nb` |
| Traduzir texto de imagens | `translate -l "ko" -img` |
| Pré-visualizar o trabalho sem escrever ficheiros | `translate -l "ko" -md --dry-run` |
| Rever traduções existentes | `co-op-review -l "ko"` |
| Actualizar ligações de notebooks e Markdown | `migrate-links -l "ko" --dry-run` |
| Expor ferramentas a um cliente MCP | Configure o [Servidor MCP](mcp.md) em vez de executar comandos da CLI directamente. |

## translate

Traduzir ficheiros Markdown, notebooks e texto de imagens para uma ou mais línguas de destino.

```bash
translate -l "ko ja fr"
```

### Exemplos comuns

Traduzir apenas Markdown:

```bash
translate -l "de" -md
```

Traduzir apenas notebooks:

```bash
translate -l "zh-CN" -nb
```

Traduzir Markdown e imagens:

```bash
translate -l "pt-BR" -md -img
```

Actualizar traduções existentes eliminando-as e recriando-as:

```bash
translate -l "ko" -u
```

Executar sem prompts interativos:

```bash
translate -l "ko ja" -md -y
```

Guardar registos:

```bash
translate -l "ko" -s
```

Escrever eventos de progresso estruturados:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Opções

| Opção | Obrigatório | Descrição |
| --- | --- | --- |
| `-l`, `--language-codes` | Sim | Códigos de línguas separados por espaços, tais como `"es fr de"`, ou `"all"`. |
| `-r`, `--root-dir` | Não | Raiz do projecto. Por omissão, o directório actual. |
| `-u`, `--update` | Não | Eliminar traduções existentes para as línguas seleccionadas e recriá-las. |
| `-img`, `--images` | Não | Traduzir apenas ficheiros de imagem. |
| `-md`, `--markdown` | Não | Traduzir apenas ficheiros Markdown. |
| `-nb`, `--notebook` | Não | Traduzir apenas ficheiros Jupyter notebook. |
| `-d`, `--debug` | Não | Activar registo de depuração na consola. |
| `-s`, `--save-logs` | Não | Guardar logs ao nível DEBUG em `<root-dir>/logs/`. |
| `--json-events` | Não | Escrever eventos de progresso de tradução legíveis por máquina como NDJSON. |
| `-x`, `--fix` | Não | Retraduzir ficheiros Markdown de baixa confiança com base em resultados de avaliação anteriores. |
| `-c`, `--min-confidence` | Não | Limiar de confiança para `--fix`. Por omissão `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Não | Adicionar ou suprimir avisos de tradução automática. Por omissão está activado na CLI. |
| `-f`, `--fast` | Não | Modo rápido de imagem obsoleto. |
| `-y`, `--yes` | Não | Confirmar automaticamente prompts, útil em CI. |
| `--repo-url` | Não | URL do repositório usado no aviso de sparse-checkout da tabela de línguas do README. |
| `--migrate-language-folders` | Não | Renomear pastas de alias legadas, tais como `cn` ou `tw`, para pastas canónicas BCP 47. |
| `--dry-run` | Não | Pré-visualizar a migração de pastas de idioma e estimativas de tradução sem escrever ficheiros. |

Se nenhuma flag de tipo for fornecida, `translate` processa Markdown, notebooks e imagens. A tradução de imagens requer configuração do Azure AI Vision.

## evaluate

Avaliar a qualidade das traduções Markdown para uma língua.

!!! warning "Experimental"
    O `evaluate` é experimental. Pode usar verificações de qualidade baseadas em regras e em LLM, escreve os resultados da avaliação nos metadados de tradução, e o seu modelo de pontuação e comportamento de metadados podem mudar.

```bash
evaluate -l "ko"
```

### Exemplos comuns

Utilize um limiar de baixa confiança mais rigoroso:

```bash
evaluate -l "es" -c 0.8
```

Executar apenas verificações baseadas em regras:

```bash
evaluate -l "fr" -f
```

Executar apenas verificações baseadas em LLM:

```bash
evaluate -l "ja" -D
```

### Opções

| Opção | Obrigatório | Descrição |
| --- | --- | --- |
| `-l`, `--language-code` | Sim | Código de uma única língua a avaliar. Códigos de alias são normalizados. |
| `-r`, `--root-dir` | Não | Raiz do projecto. Por omissão, o directório actual. |
| `-c`, `--min-confidence` | Não | Limiar usado ao listar traduções de baixa confiança. Por omissão `0.7`. |
| `-d`, `--debug` | Não | Activar registo de depuração. |
| `-s`, `--save-logs` | Não | Guardar logs ao nível DEBUG em `<root-dir>/logs/`. |
| `-f`, `--fast` | Não | Apenas avaliação baseada em regras. |
| `-D`, `--deep` | Não | Apenas avaliação baseada em LLM. |

Por omissão, o `evaluate` usa ambos os métodos, baseado em regras e em LLM. Os resultados são escritos nos metadados de tradução e resumidos na consola.

## co-op-review

Execute verificações determinísticas de manutenção de traduções sem credenciais de API.

!!! note "Beta"
    O `co-op-review` é um comando beta de revisão determinística. Não chama fornecedores de modelos nem escreve ficheiros, mas as suas verificações e o esquema de saída de problemas podem evoluir.

```bash
co-op-review -l "ko"
```

### Exemplos comuns

Rever traduções em coreano e japonês a partir do directório actual:

```bash
co-op-review -l "ko ja"
```

Rever uma raiz de projecto específica:

```bash
co-op-review -l "fr" -r ./my-course
```

Rever apenas o README após uma tradução apenas do README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignora outros documentos e READMEs aninhados. Falha se o `README.md` da raiz estiver em falta. Em combinação com `--changed-from`, revê apenas o README quando esse ficheiro fonte mudou. A tradução apenas do README deixa o README fonte inalterado, incluindo quaisquer marcadores de secção partilhada.




Rever apenas ficheiros fonte alterados em relação a uma referência base:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Imprimir saída Markdown no formato GitHub para sumários de CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opções

| Opção | Obrigatório | Descrição |
| --- | --- | --- |
| `-l`, `--language-code` | Não | Código da língua a rever. Pode ser passado várias vezes ou como um valor separado por espaços. Por omissão inclui todas as línguas de tradução descobertas. |
| `-r`, `--root-dir` | Não | Raiz do projecto. Por omissão, o directório actual. |
| `--changed-from` | Não | Ref Git usado para limitar a revisão aos ficheiros fonte alterados. |
| `--readme-only` | Não | Rever apenas a tradução do `README.md` da raiz. |
| `--format` | Não | Formato de saída: `text` ou `github`. Por omissão `text`. |

O `co-op-review` verifica actualmente ficheiros traduzidos em falta, metadados de tradução em falta ou desactualizados, integridade do frontmatter do Markdown e dos blocos de código, JSON de notebook traduzido inválido, e destinos locais de ligações Markdown ou imagens em falta. Ligações em falta são avisos por omissão; problemas de estrutura e actualidade fazem o comando falhar.

## co-op-translator-mcp

Execute o servidor MCP do Co-op Translator para agentes, editores e clientes compatíveis com MCP.

```bash
co-op-translator-mcp
```

O transporte por omissão é `stdio`. Veja o guia [Servidor MCP](mcp.md) para configuração do cliente, ferramentas, recursos e notas de segurança.

### Opções

| Opção | Obrigatório | Descrição |
| --- | --- | --- |
| `--transport` | Não | Transporte MCP: `stdio`, `streamable-http`, ou `sse`. Por omissão `stdio`. |

## migrate-links

Reprocessar ficheiros Markdown traduzidos e actualizar ligações de notebooks de forma a apontarem para notebooks traduzidos quando disponíveis.

```bash
migrate-links -l "ko ja"
```

### Exemplos comuns

Pré-visualizar actualizações de ligações:

```bash
migrate-links -l "ko" --dry-run
```

Processar todas as línguas suportadas sem confirmação:

```bash
migrate-links -l "all" -y
```

Reescrever ligações apenas quando existirem notebooks traduzidos:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opções

| Opção | Obrigatório | Descrição |
| --- | --- | --- |
| `-l`, `--language-codes` | Sim | Códigos de línguas separados por espaços, ou `"all"`. |
| `-r`, `--root-dir` | Não | Raiz do projecto. Por omissão, o directório actual. |
| `--image-dir` | Não | Directório de imagens traduzidas relativo à raiz. Por omissão `translated_images`. |
| `--dry-run` | Não | Mostrar ficheiros que seriam alterados sem escrever actualizações. |
| `--fallback-to-original`, `--no-fallback-to-original` | Não | Utilizar ligações originais de notebook quando os notebooks traduzidos estiverem em falta. Activado por omissão. |
| `-d`, `--debug` | Não | Activar registo de depuração. |
| `-s`, `--save-logs` | Não | Guardar logs ao nível DEBUG em `<root-dir>/logs/`. |
| `-y`, `--yes` | Não | Confirmar automaticamente prompts ao processar todas as línguas. |

## Environment

Quando um comando necessita de credenciais de fornecedor, configure um destes conjuntos de fornecedores. `translate --dry-run` e `co-op-review` não requerem credenciais de fornecedor:

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

A tradução de imagens requer adicionalmente o Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Estrutura de saída

As traduções de texto são escritas em:

```text
translations/<language-code>/<original-path>
```

A saída de imagens traduzidas é escrita em:

```text
translated_images/<language-code>/<original-path>
```

Por exemplo, traduzir `README.md` e `docs/setup.md` para coreano produz:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Exemplos de CLI para copiar e colar

Traduzir Markdown para três línguas:

```bash
translate -l "ko ja fr" -md
```

Traduzir apenas notebooks:

```bash
translate -l "zh-CN" -nb
```

Traduzir apenas imagens:

```bash
translate -l "pt-BR" -img
```

Pré-visualizar tradução de Markdown sem escrever ficheiros:

```bash
translate -l "de es" -md --dry-run
```

Corrigir traduções Markdown de baixa confiança:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Executar tradução de Markdown compatível com CI:

```bash
translate -l "ko ja" -md -y -s
```

Rever saída traduzida:

```bash
co-op-review -l "ko ja"
```

Pré-visualizar migração de ligações:

```bash
migrate-links -l "ko" --dry-run
```