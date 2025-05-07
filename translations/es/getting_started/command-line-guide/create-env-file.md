<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:54:11+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "es"
}
-->
# Crear el archivo *.env* en el directorio raíz

En este tutorial, te guiaremos para configurar tus variables de entorno para los servicios de Azure usando un archivo *.env*. Las variables de entorno te permiten gestionar de forma segura credenciales sensibles, como claves API, sin tener que codificarlas directamente en tu base de código.

> [!IMPORTANT]
> - Solo es necesario configurar un servicio de modelo de lenguaje (Azure OpenAI o OpenAI). Completa las variables de entorno para el servicio que prefieras. Si se configuran variables para varios modelos de lenguaje, el traductor co-op seleccionará uno según la prioridad.
> - Si no se configuran las variables de entorno para Computer Vision, el traductor cambiará automáticamente al [modo solo Markdown](./markdown-only-mode.md).

> [!NOTE]
> Esta guía se centra principalmente en los servicios de Azure, pero puedes elegir cualquier modelo de lenguaje compatible de la [lista de modelos y servicios compatibles](../README.md#-supported-models-and-services).

## Crear el archivo *.env*

En el directorio raíz de tu proyecto, crea un archivo llamado *.env*. Este archivo almacenará todas tus variables de entorno en un formato sencillo.

> [!WARNING]
> No cometas tu archivo *.env* en sistemas de control de versiones como Git. Agrega *.env* a tu archivo .gitignore para evitar commits accidentales.

1. Navega al directorio raíz de tu proyecto.

1. Crea un archivo *.env* en el directorio raíz de tu proyecto.

    ![Crear archivo *.env*.](../../../../imgs/create-env.png)

1. Abre el archivo *.env* y pega la siguiente plantilla:

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_AIServices_api_key"
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

## Reúne tus credenciales de Azure

Necesitarás las siguientes credenciales de Azure para configurar el entorno:

Puedes obtener todos los detalles desde la página de resumen del proyecto dentro de [AI Foundry](https://ai.azure.com/build/overview)

![Resumen Foundry](../../../../imgs/foundry-overview.png)


### Para Azure AI Service:

    - Azure Subscription Key: Tu clave API de Azure AI Services, que te permite acceder a los servicios de Azure AI.
    - Azure AI Service Endpoint: La URL del endpoint para tu servicio específico de Azure AI.

### Para Azure OpenAI Service:

    - Azure OpenAI API Key: La clave API para acceder a los servicios de Azure OpenAI.
    - Azure OpenAI Endpoint: La URL del endpoint para tu servicio de Azure OpenAI.


1. Copia y pega tu clave y Endpoint de AI Services en el archivo *.env*.
2. Copia y pega tu clave API y Endpoint de Azure OpenAI en el archivo *.env*.

### Detalles del modelo

Selecciona Modelo y Endpoints desde el menú lateral izquierdo

![Modelos Foundry](../../../../imgs/gpt-models.png)

Ahora debes seleccionar el modelo que deseas utilizar para obtener los detalles del modelo

![Detalles del modelo](../../../../imgs/model-deployment-name.png)

Para el archivo .env necesitamos los siguientes datos

    - Azure OpenAI Model Name: El nombre del modelo con el que interactuarás.
    - Azure OpenAI Name: El nombre de tu despliegue para los modelos de Azure OpenAI.
    - Azure OpenAI API Version: La versión de la API de Azure OpenAI que estás usando, que se encuentra al final de la cadena URL.

Para obtener estos detalles selecciona el despliegue del modelo

![Información del modelo Foundry](../../../../imgs/foundry-model-info.png)

### Añadir variables de entorno de Azure

3. Copia y pega tu **Name** de Azure OpenAI y la **Version** del modelo en el archivo *.env*.
4. Guarda el archivo *.env*.
5. Ahora, puedes acceder a estas variables de entorno para usar **Co-op Translator** con tus servicios de Azure.

**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.