# Configuração

O Co-op Translator requer um fornecedor de modelo de linguagem. A tradução de imagens requer, adicionalmente, o Azure AI Vision.

A configuração é lida a partir de variáveis de ambiente. Para projetos locais, coloque-as num ficheiro `.env` na raiz do projeto.

Para configurar recursos do Azure, veja [Configuração do Azure AI](azure-ai-setup.md).

## Configuração do ambiente local

Use um ambiente virtual antes de executar a CLI localmente. O Co-op Translator suporta Python 3.11 a 3.14.

Para uso normal da CLI, instale o pacote publicado dentro de um ambiente virtual:

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

Para desenvolvimento do repositório, instale as dependências a partir da raiz do projeto em vez disso:

```bash
poetry install
poetry run translate --help
```

Depois de a CLI estar disponível, configure um fornecedor de modelo de linguagem no `.env`.

## Seleção do fornecedor

A ferramenta deteta automaticamente os fornecedores nesta ordem:

1. Azure OpenAI
2. OpenAI
3. Anthropic

A tradução requer credenciais do fornecedor, exceto para pré-visualizações como `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` e `run_review` são operações de manutenção determinísticas e não requerem credenciais do fornecedor.

## Back-end do cliente de modelo

A partir do Co-op Translator 0.22.0, o Azure OpenAI, OpenAI e Anthropic usam o Microsoft Agent Framework por defeito. Não é necessária qualquer configuração de back-end para uso normal.

O Semantic Kernel permanece disponível temporariamente para compatibilidade. Para o selecionar explicitamente, defina:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

A utilização do Semantic Kernel gera um aviso de descontinuação. Está previsto que o pacote mova o Semantic Kernel para uma dependência opcional na versão 0.23.0 e remova a integração na 0.24.0, sujeito aos resultados de compatibilidade e ao feedback dos utilizadores. Anthropic requer `agent-framework`; selecionar explicitamente `semantic-kernel` com Anthropic falha com um erro de configuração. Valores inválidos falham durante a inicialização do tradutor suportado pelo fornecedor em vez de retroceder silenciosamente. Siga o processo de implementação e reporte bloqueadores em [issue do GitHub #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Use o Azure OpenAI quando o seu modelo estiver implementado no Azure AI Foundry ou no Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

A verificação de conectividade utiliza o endpoint, a chave da API, a versão da API e o nome da implantação antes de a tradução começar.

## OpenAI

Use o OpenAI ao chamar a API do OpenAI diretamente.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` é obrigatório porque o tradutor necessita de um modelo de chat explícito para chamadas à API.

Deixe `OPENAI_ORG_ID` e `OPENAI_BASE_URL` por definir para a configuração por defeito. Acrescente um ID de organização apenas se a sua conta necessitar de um, ou uma URL base apenas quando estiver a usar um endpoint personalizado. Não copie valores de espaço reservado para definições opcionais.

## Anthropic Claude

Use Anthropic ao chamar a API Claude diretamente. Crie uma [Chave de API Anthropic](https://platform.claude.com/docs/en/get-started) e escolha um [ID de modelo Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) suportado.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` e `ANTHROPIC_MODEL` são obrigatórios. Não precisa de definir `CO_OP_TRANSLATOR_MODEL_CLIENT`; o Agent Framework é o back-end por defeito.

Deixe `ANTHROPIC_BASE_URL` por definir para a API Anthropic. Defina-a apenas quando usar um endpoint personalizado.

`ANTHROPIC_MAX_TOKENS` tem o valor por defeito `8192`, o que deixa espaço para scripts com densidade de tokens elevada, como Meitei Mayek. Diminua-o se o seu modelo ou endpoint compatível com Anthropic limitar a saída abaixo desse valor.

## Azure AI Vision

A tradução de imagens requer o Azure AI Vision para que a ferramenta possa extrair texto das imagens antes de o modelo de linguagem configurado o traduzir. Anthropic pode traduzir o texto extraído tal como o Azure OpenAI ou o OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Se a tradução de imagens for selecionada com `-img`, `images=True`, ou sem filtro de tipo de conteúdo, a ferramenta valida a configuração do Vision antes de a tradução começar.

## Vários conjuntos de credenciais

A camada de configuração suporta múltiplos conjuntos de credenciais ao sufixar variáveis com o mesmo índice:

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

Cada conjunto deve estar completo. A verificação de estado seleciona um conjunto funcional antes de a tradução prosseguir.

OpenAI e Anthropic suportam a mesma convenção de sufixos. Mantenha cada variável num conjunto de credenciais com o mesmo sufixo, incluindo valores opcionais como `OPENAI_BASE_URL_1` ou `ANTHROPIC_BASE_URL_1`.

## Requisitos de comandos

| Comando ou API | Requer LLM | Requer Vision | Notas |
| --- | --- | --- | --- |
| `translate -md` | Sim | Não | Traduz apenas Markdown. |
| `translate -nb` | Sim | Não | Traduz apenas notebooks. |
| `translate -img` | Sim | Sim | Traduz apenas imagens. |
| `translate` sem flags de tipo | Sim | Sim | O modo por defeito inclui Markdown, notebooks e imagens. |
| `evaluate` | Sim | Não | Usa avaliação por LLM a menos que `--fast` esteja selecionado. |
| `migrate-links` | Não | Não | Executa migração local de links sem chamadas ao fornecedor. |
| `co-op-review` | Não | Não | Executa verificações determinísticas de estrutura de tradução, atualidade, Markdown, notebooks e links locais. |
| `run_translation(markdown=True)` | Sim | Não | Tradução programática de Markdown. |
| `run_translation(images=True)` | Sim | Sim | Tradução programática de imagens. |
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

A API Python pode substituir estes diretórios com `translations_dir` e `image_dir`.