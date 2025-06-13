<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:26:06+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "pt"
}
-->
# Criar o ficheiro *.env* na diretoria raiz

Neste tutorial, vamos guiá-lo na configuração das suas variáveis de ambiente para os serviços Azure usando um ficheiro *.env*. As variáveis de ambiente permitem gerir de forma segura credenciais sensíveis, como chaves de API, sem as incluir diretamente no seu código.

> [!IMPORTANT]
> - Só precisa configurar um serviço de modelo de linguagem (Azure OpenAI ou OpenAI). Preencha as variáveis de ambiente para o serviço que preferir. Se forem definidas variáveis para vários modelos de linguagem, o tradutor colaborativo selecionará um com base na prioridade.
> - Se as variáveis de ambiente do Computer Vision não estiverem definidas, o tradutor irá automaticamente mudar para o [modo apenas Markdown](./markdown-only-mode.md).

> [!NOTE]
> Este guia foca-se principalmente nos serviços Azure, mas pode escolher qualquer modelo de linguagem suportado da [lista de modelos e serviços suportados](../README.md#-supported-models-and-services).

## Criar o ficheiro *.env*

Na diretoria raiz do seu projeto, crie um ficheiro chamado *.env*. Este ficheiro irá armazenar todas as suas variáveis de ambiente num formato simples.

> [!WARNING]
> Não faça commit do seu ficheiro *.env* em sistemas de controlo de versão como o Git. Adicione *.env* ao seu ficheiro .gitignore para evitar commits acidentais.

1. Navegue até à diretoria raiz do seu projeto.

1. Crie um ficheiro *.env* na diretoria raiz do seu projeto.

1. Abra o ficheiro *.env* e cole o seguinte modelo:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> Se quiser encontrar as suas chaves de API e endpoints, pode consultar [set-up-azure-ai.md](../set-up-azure-ai.md).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.