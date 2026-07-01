# Configuração

O Co-op Translator requer um fornecedor de modelo de linguagem. A tradução de imagens requer, adicionalmente, o Azure AI Vision.

A configuração é lida a partir de variáveis de ambiente. Para projetos locais, coloque-as num ficheiro `.env` na raiz do projeto.

Para a configuração de recursos Azure, consulte [Configuração do Azure AI](azure-ai-setup.md).

## Configuração do ambiente local

Use um ambiente virtual antes de executar a CLI localmente. O Co-op Translator suporta Python 3.10 a 3.12.

Para utilização normal da CLI, instale o pacote publicado dentro de um ambiente virtual:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

For repository development, install dependencies from the project root instead:

```bash
poetry install
poetry run translate --help
```

After the CLI is available, configure one language model provider in `.env`.

## Seleção de provedor

A ferramenta detecta automaticamente os fornecedores por esta ordem:

1. Azure OpenAI
2. OpenAI

Se nenhum fornecedor estiver configurado, `translate`, `evaluate`, `migrate-links`, e `run_translation` falham durante as verificações de configuração. `co-op-review` e `run_review` são verificações de manutenção determinísticas e não requerem credenciais de fornecedor.

## Azure OpenAI

Use Azure OpenAI quando o seu modelo estiver implementado no Azure AI Foundry ou no Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

A verificação de conectividade usa o endpoint, a chave da API, a versão da API, e o nome da implementação antes de a tradução começar.

## OpenAI

Use OpenAI quando estiver a chamar diretamente a API da OpenAI.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # opcional
OPENAI_BASE_URL="..."        # opcional
```

`OPENAI_CHAT_MODEL_ID` é obrigatório porque o tradutor precisa de um modelo de chat explícito para chamadas à API.

## Azure AI Vision

A tradução de imagens requer o Azure AI Vision para que a ferramenta possa extrair texto das imagens antes de as traduzir.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Se a tradução de imagens for selecionada com `-img`, `images=True`, ou sem filtro de content-type, a ferramenta valida a configuração do Vision antes de iniciar a tradução.

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

Cada conjunto deve estar completo. A verificação de saúde selecciona um conjunto funcional antes de a tradução prosseguir.

## Requisitos dos comandos

| Comando ou API | Requer LLM | Requer Vision | Notas |
| --- | --- | --- | --- |
| `translate -md` | Sim | Não | Traduz apenas Markdown. |
| `translate -nb` | Sim | Não | Traduz apenas notebooks. |
| `translate -img` | Sim | Sim | Traduz apenas imagens. |
| `translate` with no type flags | Sim | Sim | O modo por defeito inclui Markdown, notebooks, e imagens. |
| `evaluate` | Sim | Não | Usa avaliação LLM a menos que `--fast` seja selecionado. |
| `migrate-links` | Sim | Não | Executa migração de links, mas ainda executa verificações de configuração partilhadas. |
| `co-op-review` | Não | Não | Executa verificações determinísticas de estrutura de tradução, actualidade, Markdown, notebooks, e links locais. |
| `run_translation(markdown=True)` | Sim | Não | Tradução programática de Markdown. |
| `run_translation(images=True)` | Sim | Sim | Tradução programática de imagens. |
| `run_review(...)` | Não | Não | Revisão determinística programática. |

## Diretórios de saída

Saída de tradução de texto por defeito:

```text
translations/<language-code>/<source-relative-path>
```

Saída de imagens traduzidas por defeito:

```text
translated_images/<language-code>/<source-relative-path>
```

A API Python pode sobrescrever estes diretórios com `translations_dir` e `image_dir`.