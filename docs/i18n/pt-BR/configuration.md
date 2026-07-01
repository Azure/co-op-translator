# Configuração

Co-op Translator requer um provedor de modelo de linguagem. A tradução de imagens requer adicionalmente o Azure AI Vision.

A configuração é lida a partir de variáveis de ambiente. Para projetos locais, coloque-as em um arquivo `.env` na raiz do projeto.

Para configurar recursos do Azure, consulte [Configuração do Azure AI](azure-ai-setup.md).

## Configuração do ambiente local

Use um ambiente virtual antes de executar a CLI localmente. O Co-op Translator suporta Python 3.10 até 3.12.

Para uso normal da CLI, instale o pacote publicado dentro de um ambiente virtual:

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

Depois que a CLI estiver disponível, configure um provedor de modelo de linguagem no arquivo `.env`.

## Seleção de provedor

A ferramenta detecta automaticamente os provedores nesta ordem:

1. Azure OpenAI
2. OpenAI

Se nenhum provedor estiver configurado, `translate`, `evaluate`, `migrate-links` e `run_translation` falharão durante as verificações de configuração. `co-op-review` e `run_review` são verificações de manutenção determinísticas e não exigem credenciais de provedor.

## Azure OpenAI

Use o Azure OpenAI quando seu modelo estiver implantado no Azure AI Foundry ou no Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

A verificação de conectividade usa o endpoint, a chave de API, a versão da API e o nome da implantação antes do início da tradução.

## OpenAI

Use o OpenAI ao chamar a API do OpenAI diretamente.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # opcional
OPENAI_BASE_URL="..."        # opcional
```

O `OPENAI_CHAT_MODEL_ID` é obrigatório porque o tradutor precisa de um modelo de chat explícito para chamadas de API.

## Azure AI Vision

A tradução de imagens requer o Azure AI Vision para que a ferramenta possa extrair texto das imagens antes de traduzi-lo.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Se a tradução de imagens for selecionada com `-img`, `images=True`, ou sem filtro de tipo de conteúdo, a ferramenta valida a configuração do Vision antes do início da tradução.

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

Cada conjunto deve estar completo. A verificação de integridade seleciona um conjunto funcional antes que a tradução prossiga.

## Requisitos de comandos

| Comando ou API | LLM necessário | Vision necessário | Observações |
| --- | --- | --- | --- |
| `translate -md` | Sim | Não | Traduz apenas Markdown. |
| `translate -nb` | Sim | Não | Traduz apenas notebooks. |
| `translate -img` | Sim | Sim | Traduz apenas imagens. |
| `translate` with no type flags | Sim | Sim | O modo padrão inclui Markdown, notebooks e imagens. |
| `evaluate` | Sim | Não | Usa avaliação por LLM, a menos que `--fast` seja selecionado. |
| `migrate-links` | Sim | Não | Executa migração de links, mas ainda realiza verificações de configuração compartilhadas. |
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

A API Python pode sobrescrever esses diretórios com `translations_dir` e `image_dir`.