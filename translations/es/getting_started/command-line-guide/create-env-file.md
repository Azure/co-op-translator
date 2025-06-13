<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T12:38:29+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "es"
}
-->
# Crear el archivo *.env* en el directorio raíz

En este tutorial, te guiaremos para configurar tus variables de entorno para los servicios de Azure usando un archivo *.env*. Las variables de entorno te permiten gestionar de forma segura credenciales sensibles, como claves API, sin tener que codificarlas directamente en tu base de código.

> [!IMPORTANT]
> - Solo es necesario configurar un servicio de modelo de lenguaje (Azure OpenAI o OpenAI). Completa las variables de entorno para el servicio que prefieras. Si se configuran variables de entorno para varios modelos de lenguaje, el traductor cooperativo seleccionará uno según la prioridad.
> - Si no se configuran las variables de entorno de Computer Vision, el traductor cambiará automáticamente al [modo solo Markdown](./markdown-only-mode.md).

> [!NOTE]
> Esta guía se centra principalmente en los servicios de Azure, pero puedes elegir cualquier modelo de lenguaje compatible de la [lista de modelos y servicios compatibles](../README.md#-supported-models-and-services).

## Crear el archivo *.env*

En el directorio raíz de tu proyecto, crea un archivo llamado *.env*. Este archivo almacenará todas tus variables de entorno en un formato sencillo.

> [!WARNING]
> No hagas commit de tu archivo *.env* en sistemas de control de versiones como Git. Agrega *.env* a tu archivo .gitignore para evitar commits accidentales.

1. Navega al directorio raíz de tu proyecto.

1. Crea un archivo *.env* en el directorio raíz de tu proyecto.

1. Abre el archivo *.env* y pega la siguiente plantilla:

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
> Si quieres encontrar tus claves API y endpoints, puedes consultar [set-up-azure-ai.md](../set-up-azure-ai.md).

**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.