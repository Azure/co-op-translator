<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:26:15+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "br"
}
-->
# Crie o arquivo *.env* no diretório raiz

Neste tutorial, vamos orientá-lo a configurar suas variáveis de ambiente para os serviços Azure usando um arquivo *.env*. As variáveis de ambiente permitem gerenciar de forma segura credenciais sensíveis, como chaves de API, sem precisar inseri-las diretamente no seu código.

> [!IMPORTANT]
> - Apenas um serviço de modelo de linguagem (Azure OpenAI ou OpenAI) precisa ser configurado. Preencha as variáveis de ambiente para o serviço que você preferir. Se variáveis para múltiplos modelos de linguagem estiverem definidas, o tradutor cooperativo selecionará uma com base na prioridade.
> - Se as variáveis de ambiente do Computer Vision não estiverem definidas, o tradutor mudará automaticamente para o [modo somente Markdown](./markdown-only-mode.md).

> [!NOTE]
> Este guia foca principalmente nos serviços Azure, mas você pode escolher qualquer modelo de linguagem suportado na [lista de modelos e serviços suportados](../README.md#-supported-models-and-services).

## Crie o arquivo *.env*

No diretório raiz do seu projeto, crie um arquivo chamado *.env*. Esse arquivo armazenará todas as suas variáveis de ambiente em um formato simples.

> [!WARNING]
> Não faça commit do seu arquivo *.env* em sistemas de controle de versão como o Git. Adicione *.env* ao seu arquivo .gitignore para evitar commits acidentais.

1. Navegue até o diretório raiz do seu projeto.

1. Crie um arquivo *.env* no diretório raiz do seu projeto.

1. Abra o arquivo *.env* e cole o seguinte modelo:

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
> Se quiser encontrar suas chaves de API e endpoints, consulte [set-up-azure-ai.md](../set-up-azure-ai.md).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.