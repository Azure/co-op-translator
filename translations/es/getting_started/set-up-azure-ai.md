<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:18:43+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "es"
}
-->
# Configurar Azure AI para Co-op Translator (Azure OpenAI y Azure AI Vision)

Esta guía te lleva paso a paso para configurar Azure OpenAI para la traducción de idiomas y Azure Computer Vision para el análisis de contenido de imágenes (que luego se puede usar para traducción basada en imágenes) dentro de Azure AI Foundry.

**Requisitos previos:**
- Una cuenta de Azure con una suscripción activa.
- Permisos suficientes para crear recursos y despliegues en tu suscripción de Azure.

## Crear un Proyecto de Azure AI

Comenzarás creando un Proyecto de Azure AI, que actúa como un lugar central para gestionar tus recursos de IA.

1. Navega a [https://ai.azure.com](https://ai.azure.com) e inicia sesión con tu cuenta de Azure.

1. Selecciona **+Crear** para crear un nuevo proyecto.

1. Realiza las siguientes tareas:
   - Ingresa un **Nombre del proyecto** (por ejemplo, `CoopTranslator-Project`).
   - Selecciona el **Centro de IA** (por ejemplo, `CoopTranslator-Hub`) (Crea uno nuevo si es necesario).

1. Haz clic en "**Revisar y crear**" para configurar tu proyecto. Serás dirigido a la página de resumen de tu proyecto.

## Configurar Azure OpenAI para Traducción de Idiomas

Dentro de tu proyecto, desplegarás un modelo de Azure OpenAI que servirá como backend para la traducción de texto.

### Navegar a Tu Proyecto

Si aún no estás ahí, abre tu proyecto recién creado (por ejemplo, `CoopTranslator-Project`) en Azure AI Foundry.

### Desplegar un Modelo OpenAI

1. En el menú izquierdo de tu proyecto, bajo "Mis activos", selecciona "**Modelos + puntos de conexión**".

1. Selecciona **+ Desplegar modelo**.

1. Selecciona **Desplegar Modelo Base**.

1. Se te mostrará una lista de modelos disponibles. Filtra o busca un modelo GPT adecuado. Recomendamos `gpt-4o`.

1. Selecciona el modelo deseado y haz clic en **Confirmar**.

1. Selecciona **Desplegar**.

### Configuración de Azure OpenAI

Una vez desplegado, puedes seleccionar el despliegue desde la página de "**Modelos + puntos de conexión**" para encontrar su **URL del endpoint REST**, **Clave**, **Nombre del despliegue**, **Nombre del modelo** y **Versión de API**. Estos datos serán necesarios para integrar el modelo de traducción en tu aplicación.

## Configurar Azure Computer Vision para Traducción de Imágenes

Para habilitar la traducción de texto dentro de imágenes, necesitas obtener la Clave API y el Endpoint del Servicio Azure AI.

1. Navega a tu Proyecto de Azure AI (por ejemplo, `CoopTranslator-Project`). Asegúrate de estar en la página de resumen del proyecto.

### Configuración del Servicio Azure AI

Encuentra la Clave API y el Endpoint desde el Servicio Azure AI.

1. Navega a tu Proyecto de Azure AI (por ejemplo, `CoopTranslator-Project`). Asegúrate de estar en la página de resumen del proyecto.

1. Encuentra la **Clave API** y el **Endpoint** en la pestaña del Servicio Azure AI.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Esta conexión hace que las capacidades del recurso vinculado de Servicios Azure AI (incluido el análisis de imágenes) estén disponibles para tu proyecto en AI Foundry. Luego puedes usar esta conexión en tus notebooks o aplicaciones para extraer texto de imágenes, que posteriormente puede enviarse al modelo Azure OpenAI para traducción.

## Consolidando Tus Credenciales

Para este punto, deberías haber recopilado lo siguiente:

**Para Azure OpenAI (Traducción de Texto):**
- Endpoint de Azure OpenAI
- Clave API de Azure OpenAI
- Nombre del Modelo Azure OpenAI (por ejemplo, `gpt-4o`)
- Nombre del Despliegue Azure OpenAI (por ejemplo, `cooptranslator-gpt4o`)
- Versión de API de Azure OpenAI

**Para Servicios Azure AI (Extracción de Texto de Imágenes vía Vision):**
- Endpoint del Servicio Azure AI
- Clave API del Servicio Azure AI

### Ejemplo: Configuración de Variables de Entorno (Vista previa)

Más adelante, al construir tu aplicación, probablemente la configures usando estas credenciales recopiladas. Por ejemplo, podrías establecerlas como variables de entorno así:

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

### Lecturas adicionales

- [Cómo crear un proyecto en Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Cómo crear recursos Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Cómo desplegar modelos OpenAI en Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que pueda surgir del uso de esta traducción.