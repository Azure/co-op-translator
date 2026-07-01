# Configuração do Azure AI

Use este guia quando quiser configurar o Azure OpenAI para tradução de texto e o Azure AI Vision para extração de texto de imagens.

## Pré-requisitos

- Uma assinatura do Azure.
- Permissão para criar ou usar recursos do Azure AI e implantações de modelos.
- Um projeto no Azure AI Foundry ou acesso equivalente aos recursos Azure OpenAI e Azure AI Vision.

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
5. Registre o endpoint, nome da implantação, nome do modelo, chave da API e versão da API.

!!! note
    A versão da API do Azure OpenAI é separada da versão do modelo exibida no Azure AI Foundry. Escolha uma versão de API compatível para sua implantação.

## Configurar o Azure AI Vision

A tradução de imagens usa o Azure AI Vision para extrair texto das imagens de origem antes que o texto seja traduzido.

No seu projeto Azure AI, encontre a chave e o endpoint do Azure AI Services.

![Encontre as informações do serviço Azure AI](../../assets/find-azure-ai-info.png)

Recorde:

- Endpoint do Azure AI Service
- Chave da API do Azure AI Service

## Variáveis de ambiente

Adicione as credenciais ao seu `.env` file ou aos segredos do CI.

```bash
# Azure AI Vision, necessário para tradução de imagens
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, necessário para tradução de texto
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator também oferece suporte a conjuntos opcionais de credenciais de fallback. Duplique um conjunto completo de provedores com sufixos como `_1` ou `_2`; todas as variáveis em um conjunto de fallback devem compartilhar o mesmo sufixo.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Próximos passos

- Retorne para [Configuração](configuration.md) para configurar variáveis de ambiente locais ou do CI.
- Use [Referência da CLI](cli.md) para comandos de tradução.
- Use [GitHub Actions](github-actions.md) para automatizar pull requests de tradução.