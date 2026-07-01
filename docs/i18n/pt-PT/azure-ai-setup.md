# Configuração do Azure AI

Use este guia quando quiser configurar o Azure OpenAI para tradução de texto e o Azure AI Vision para extração de texto de imagens.

## Pré-requisitos

- Uma subscrição do Azure.
- Permissão para criar ou usar recursos Azure AI e implantações de modelos.
- Um projeto no Azure AI Foundry ou acesso equivalente a recursos Azure OpenAI e Azure AI Vision.

## Criar um projeto Azure AI

1. Abra [Azure AI Foundry](https://ai.azure.com).
2. Crie ou selecione um projeto.
3. Crie ou selecione um hub de IA para o projeto.
4. Abra a visão geral do projeto após a criação.

## Implantar um modelo Azure OpenAI

1. No projeto, abra **Modelos + endpoints**.
2. Selecione **Implantar modelo**.
3. Escolha um modelo GPT, como `gpt-4o`.
4. Implemente o modelo.
5. Anote o endpoint, o nome da implantação, o nome do modelo, a chave da API e a versão da API.

!!! note
    A versão da API do Azure OpenAI é separada da versão do modelo exibida no Azure AI Foundry. Escolha uma versão da API suportada para a sua implantação.

## Configurar o Azure AI Vision

A tradução de imagens utiliza o Azure AI Vision para extrair texto das imagens de origem antes de o texto ser traduzido.

No seu projeto Azure AI, encontre a chave e o endpoint do Azure AI Services.

![Encontrar informações do serviço Azure AI](../../assets/find-azure-ai-info.png)

Registe:

- Endpoint do Azure AI Service
- Chave da API do Azure AI Service

## Variáveis de ambiente

Adicione as credenciais ao seu ficheiro `.env` ou aos segredos do CI.

```bash
# Azure AI Vision, necessário para a tradução de imagens
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, necessário para a tradução de texto
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator também suporta conjuntos de credenciais de reserva opcionais. Duplique um conjunto completo do fornecedor com sufixos tais como `_1` ou `_2`; todas as variáveis num conjunto de reserva devem partilhar o mesmo sufixo.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Próximos passos

- Volte a [Configuração](configuration.md) para configurar as variáveis de ambiente locais ou do CI.
- Use [Referência da CLI](cli.md) para comandos de tradução.
- Use [GitHub Actions](github-actions.md) para automatizar pull requests de tradução.