<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:15:36+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "br"
}
-->
# Configurar Azure OpenAI para tradução de idiomas

## Criar um recurso Azure OpenAI no Azure AI Foundry

Para configurar o Azure OpenAI no Azure AI Foundry, siga estes passos:

### Criando um Hub

1. Faça login no [portal Azure AI Foundry](https://ai.azure.com): Certifique-se de estar logado com sua conta Azure.

2. Navegue até o Centro de Gerenciamento: Na página inicial, selecione "Management Center" no menu à esquerda.

3. Crie um Novo Hub: Clique em "+ New hub" e preencha os detalhes necessários como Subscription, Resource Group e Hub Name. Recomendamos implantar o hub na região East US, pois essa região suporta modelos Cognitive vision e GPT.

4. Revise e Crie: Revise as informações e clique em "Create" para configurar seu hub.

### Criando um Projeto

1. Vá para a Página Inicial: Se ainda não estiver lá, selecione "Azure AI Foundry" no canto superior esquerdo da página para acessar a página inicial.

2. Crie um Projeto: Clique em "+ Create project" e insira um nome para seu projeto.

3. Selecione um Hub: Se você tiver vários hubs, escolha o que deseja usar. Se quiser criar um novo hub, pode fazer isso nesta etapa.

4. Configure o Projeto: Siga as instruções para configurar seu projeto conforme suas necessidades.

5. Crie o Projeto: Clique em "Create" para finalizar a configuração.

### Implantando um Modelo e Endpoint para o modelo OpenAI

1. Faça login no [portal Azure AI Foundry](https://ai.azure.com): Certifique-se de estar logado com a assinatura Azure que possui seu recurso Azure OpenAI Service.

2. Navegue até Models and Endpoints: Na página inicial do Azure AI Foundry, encontre o bloco que diz " and select "Let's go." ou vá em Model and Endpoints no menu à esquerda.

3. Se ainda não tiver um modelo GPT implantado, selecione deploy model: escolha um modelo GPT, recomendamos GPT-4o, GPT-4o-mini ou o3-mini.

4. Acesse seus recursos: Você verá seus recursos Azure OpenAI Service existentes. Se tiver vários recursos, use o seletor para escolher qual deseja utilizar.

Para instruções mais detalhadas, consulte a documentação oficial do Azure AI Foundry.

[How to Create a project](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[How to Create resources](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[How to use OpenAI Model in AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[OpenAI Services in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.