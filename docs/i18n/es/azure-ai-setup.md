# Configuración de Azure AI

Use this guide when you want to configure Azure OpenAI for text translation and Azure AI Vision for image text extraction.

## Requisitos previos

- Una suscripción de Azure.
- Permiso para crear o usar recursos de Azure AI y despliegues de modelos.
- Un proyecto en Azure AI Foundry o acceso equivalente a recursos de Azure OpenAI y Azure AI Vision.

## Crear un proyecto de Azure AI

1. Abra [Azure AI Foundry](https://ai.azure.com).
2. Cree o seleccione un proyecto.
3. Cree o seleccione un hub de IA para el proyecto.
4. Abra la vista general del proyecto después de crearlo.

## Desplegar un modelo de Azure OpenAI

1. En el proyecto, abra **Models + endpoints**.
2. Seleccione **Deploy model**.
3. Elija un modelo GPT como `gpt-4o`.
4. Despliegue el modelo.
5. Anote el endpoint, el nombre del despliegue, el nombre del modelo, la clave de API y la versión de la API.

!!! note
    La versión de la API de Azure OpenAI es independiente de la versión del modelo que se muestra en Azure AI Foundry. Elija una versión de API compatible para su despliegue.

## Configurar Azure AI Vision

La traducción de imágenes utiliza Azure AI Vision para extraer texto de las imágenes de origen antes de traducir el texto.

En su proyecto de Azure AI, encuentre la clave y el endpoint del servicio Azure AI Services.

![Encontrar información del servicio de Azure AI](../../assets/find-azure-ai-info.png)

Registre:

- Endpoint del servicio Azure AI
- Clave de API del servicio Azure AI

## Variables de entorno

Agregue las credenciales a su `.env` file or CI secrets.

```bash
# Azure AI Vision, necesario para la traducción de imágenes
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, necesario para la traducción de texto
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator también admite conjuntos de credenciales de reserva opcionales. Duplique un conjunto completo de proveedor con sufijos como `_1` o `_2`; todas las variables en un conjunto de reserva deben compartir el mismo sufijo.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Próximos pasos

- Vuelva a [Configuration](configuration.md) para configurar las variables de entorno locales o de CI.
- Use [CLI Reference](cli.md) para los comandos de traducción.
- Use [GitHub Actions](github-actions.md) para automatizar las solicitudes de extracción de traducción.