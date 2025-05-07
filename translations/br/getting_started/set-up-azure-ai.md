<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:19:17+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "br"
}
-->
# Configurar Azure AI para Co-op Translator (Azure OpenAI & Azure AI Vision)

Este guia orienta você na configuração do Azure OpenAI para tradução de idiomas e do Azure Computer Vision para análise de conteúdo de imagens (que pode ser usado para tradução baseada em imagem) dentro do Azure AI Foundry.

**Pré-requisitos:**
- Uma conta Azure com uma assinatura ativa.
- Permissões suficientes para criar recursos e implantações na sua assinatura Azure.

## Criar um Projeto Azure AI

Você começará criando um Projeto Azure AI, que funciona como um local central para gerenciar seus recursos de IA.

1. Acesse [https://ai.azure.com](https://ai.azure.com) e faça login com sua conta Azure.

1. Selecione **+Create** para criar um novo projeto.

1. Realize as seguintes tarefas:
   - Informe um **Nome do projeto** (ex.: `CoopTranslator-Project`).
   - Selecione o **AI hub** (ex.: `CoopTranslator-Hub`) (Crie um novo, se necessário).

1. Clique em "**Review and Create**" para configurar seu projeto. Você será direcionado para a página de visão geral do projeto.

## Configurar Azure OpenAI para Tradução de Idiomas

Dentro do seu projeto, você implantará um modelo Azure OpenAI para servir como backend para tradução de texto.

### Navegar até seu Projeto

Se ainda não estiver, abra seu projeto recém-criado (ex.: `CoopTranslator-Project`) no Azure AI Foundry.

### Implantar um Modelo OpenAI

1. No menu à esquerda do seu projeto, em "My assets", selecione "**Models + endpoints**".

1. Selecione **+ Deploy model**.

1. Escolha **Deploy Base Model**.

1. Será exibida uma lista de modelos disponíveis. Filtre ou pesquise por um modelo GPT adequado. Recomendamos `gpt-4o`.

1. Selecione o modelo desejado e clique em **Confirm**.

1. Clique em **Deploy**.

### Configuração do Azure OpenAI

Após a implantação, você pode selecionar a implantação na página "**Models + endpoints**" para encontrar a **URL do endpoint REST**, **Chave**, **Nome da implantação**, **Nome do modelo** e **Versão da API**. Essas informações serão necessárias para integrar o modelo de tradução à sua aplicação.

## Configurar Azure Computer Vision para Tradução de Imagens

Para habilitar a tradução de texto dentro de imagens, é necessário obter a Chave da API e o Endpoint do Azure AI Service.

1. Acesse seu Projeto Azure AI (ex.: `CoopTranslator-Project`). Certifique-se de estar na página de visão geral do projeto.

### Configuração do Azure AI Service

Encontre a Chave da API e o Endpoint no Azure AI Service.

1. Acesse seu Projeto Azure AI (ex.: `CoopTranslator-Project`). Certifique-se de estar na página de visão geral do projeto.

1. Localize a **API Key** e o **Endpoint** na aba do Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Essa conexão torna as capacidades do recurso vinculado do Azure AI Services (incluindo análise de imagens) disponíveis para seu projeto AI Foundry. Você poderá usar essa conexão em seus notebooks ou aplicações para extrair texto de imagens, que pode ser enviado posteriormente ao modelo Azure OpenAI para tradução.

## Consolidando suas Credenciais

Até aqui, você deve ter coletado o seguinte:

**Para Azure OpenAI (Tradução de Texto):**
- Endpoint Azure OpenAI
- Chave da API Azure OpenAI
- Nome do Modelo Azure OpenAI (ex.: `gpt-4o`)
- Nome da Implantação Azure OpenAI (ex.: `cooptranslator-gpt4o`)
- Versão da API Azure OpenAI

**Para Azure AI Services (Extração de Texto de Imagens via Vision):**
- Endpoint Azure AI Service
- Chave da API Azure AI Service

### Exemplo: Configuração de Variáveis de Ambiente (Preview)

Mais adiante, ao construir sua aplicação, provavelmente irá configurá-la usando essas credenciais coletadas. Por exemplo, pode defini-las como variáveis de ambiente da seguinte forma:

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-02-01
```

---

### Leituras Complementares

- [Como criar um projeto no Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Como criar recursos Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Como implantar modelos OpenAI no Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.