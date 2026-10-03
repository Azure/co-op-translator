# Configuração

O Co-op Translator requer um provedor de modelo de linguagem. A tradução de imagens requer adicionalmente o Azure AI Vision.

A configuração é lida a partir de variáveis de ambiente. Para projetos locais, coloque-as em um arquivo `.env` na raiz do projeto.

Para configuração de recursos do Azure, veja [Configuração do Azure AI](azure-ai-setup.md).

## Configuração do ambiente local

Use um ambiente virtual antes de executar o CLI localmente. O Co-op Translator suporta Python 3.11 a 3.14.

Para uso normal do CLI, instale o pacote publicado dentro de um ambiente virtual:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Desenvolvimento do repositório

Para desenvolvimento do repositório, instale as dependências a partir da raiz do projeto:

```bash
poetry install
poetry run translate --help
```

Depois que o CLI estiver disponível, configure um provedor de modelo de linguagem no `.env`.

## Seleção de provedor

A ferramenta detecta provedores automaticamente nesta ordem:

1. Azure OpenAI
2. OpenAI
3. Anthropic

A tradução requer credenciais do provedor, exceto para visualizações, como `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` e `run_review` são operações de manutenção determinísticas e não requerem credenciais do provedor.

## Backend do cliente de modelo

A partir do Co-op Translator 0.22.0, Azure OpenAI, OpenAI e Anthropic usam o Microsoft Agent Framework por padrão. Nenhuma configuração de backend é necessária para uso normal.

O Semantic Kernel permanece disponível temporariamente para compatibilidade. Para selecioná-lo explicitamente, defina:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

O uso do Semantic Kernel gera um aviso de descontinuação. Está planejado que o pacote mova o Semantic Kernel para uma dependência opcional na versão 0.23.0 e remova a integração na 0.24.0, sujeito aos resultados de compatibilidade e ao feedback dos usuários. Anthropic requer `agent-framework`; selecionar explicitamente `semantic-kernel` com Anthropic falha com um erro de configuração. Valores inválidos falham durante a inicialização do tradutor com suporte de provedor em vez de recorrer silenciosamente a outro valor. Acompanhe o lançamento e reporte bloqueadores em [GitHub issue #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Use Azure OpenAI quando seu modelo estiver implantado no Azure AI Foundry ou no Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

A verificação de conectividade usa o endpoint, a chave de API, a versão da API e o nome da implantação antes do início da tradução.

## OpenAI

Use OpenAI ao chamar a API da OpenAI diretamente.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` é obrigatório porque o tradutor precisa de um modelo de chat explícito para chamadas de API.

Deixe `OPENAI_ORG_ID` e `OPENAI_BASE_URL` sem valor para a configuração padrão. Adicione um ID de organização somente se sua conta precisar, ou um URL base somente quando usar um endpoint personalizado. Não copie valores de espaço reservado para configurações opcionais.

## Anthropic Claude

Use Anthropic ao chamar diretamente a API Claude. Crie uma [chave de API Anthropic](https://platform.claude.com/docs/en/get-started) e escolha um [ID de modelo Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) suportado.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` e `ANTHROPIC_MODEL` são obrigatórios. Você não precisa definir `CO_OP_TRANSLATOR_MODEL_CLIENT`; o Agent Framework é o backend padrão.

Deixe `ANTHROPIC_BASE_URL` sem valor para a API Anthropic. Defina-o apenas ao usar um endpoint personalizado.

`ANTHROPIC_MAX_TOKENS` tem como padrão `8192`, o que deixa espaço para scripts densos em tokens, como Meitei Mayek. Reduza-o se seu modelo ou endpoint compatível com Anthropic limitar a saída abaixo disso.

## Azure AI Vision

A tradução de imagens requer o Azure AI Vision para que a ferramenta possa extrair texto das imagens antes que o modelo de linguagem configurado o traduza. A Anthropic pode traduzir o texto extraído assim como o Azure OpenAI ou o OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Se a tradução de imagens for selecionada com `-img`, `images=True` ou sem filtro de tipo de conteúdo, a ferramenta valida a configuração do Vision antes do início da tradução.

## Múltiplos conjuntos de credenciais

A camada de configuração suporta múltiplos conjuntos de credenciais sufixando variáveis com o mesmo índice:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Cada conjunto deve ser completo. A verificação de integridade seleciona um conjunto funcional antes de a tradução prosseguir.

OpenAI e Anthropic suportam a mesma convenção de sufixos. Mantenha todas as variáveis em um conjunto de credenciais com o mesmo sufixo, incluindo valores opcionais como `OPENAI_BASE_URL_1` ou `ANTHROPIC_BASE_URL_1`.

## Requisitos de comando

| Comando ou API | LLM necessário | Vision necessário | Observações |
| --- | --- | --- | --- |
| `translate -md` | Sim | Não | Tradução apenas de Markdown. |
| `translate -nb` | Sim | Não | Tradução apenas de notebooks. |
| `translate -img` | Sim | Sim | Tradução apenas de imagens. |
| `translate` sem flags de tipo | Sim | Sim | O modo padrão inclui Markdown, notebooks e imagens. |
| `evaluate` | Sim | Não | Usa avaliação por LLM a menos que `--fast` seja selecionado. |
| `migrate-links` | Não | Não | Realiza migração local de links sem chamadas ao provedor. |
| `co-op-review` | Não | Não | Executa verificações determinísticas de estrutura de tradução, atualidade, Markdown, notebooks e links locais. |
| `run_translation(markdown=True)` | Sim | Não | Tradução de Markdown programática. |
| `run_translation(images=True)` | Sim | Sim | Tradução de imagens programática. |
| `run_review(...)` | Não | Não | Revisão determinística programática. |

## Diretórios de saída

Saída padrão de tradução de texto:

```text
translations/<language-code>/<source-relative-path>
```

Saída padrão de imagens traduzidas:

```text
translated_images/<language-code>/<source-relative-path>
```

A API Python pode sobrescrever esses diretórios com `translations_dir` e `image_dir`.