<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:15:10+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "es"
}
-->
# Configurar Azure OpenAI para traducción de idiomas

## Crear un recurso de Azure OpenAI en Azure AI Foundry

Para configurar Azure OpenAI en Azure AI Foundry, sigue estos pasos:

### Crear un Hub

1. Inicia sesión en el [portal de Azure AI Foundry](https://ai.azure.com): Asegúrate de estar conectado con tu cuenta de Azure.

2. Navega al Centro de Gestión: Desde la página principal, selecciona "Management Center" en el menú lateral izquierdo.

3. Crear un nuevo Hub: Haz clic en "+ New hub" e ingresa los detalles necesarios como Suscripción, Grupo de Recursos y Nombre del Hub. Recomendamos desplegar el hub en East US, ya que esta región soporta modelos de Cognitive vision y GPT.

4. Revisar y Crear: Revisa los detalles y haz clic en "Create" para configurar tu hub.

### Crear un Proyecto

1. Ir a la página principal: Si no estás allí, selecciona "Azure AI Foundry" en la parte superior izquierda para ir a la página principal.

2. Crear un Proyecto: Haz clic en "+ Create project" e ingresa un nombre para tu proyecto.

3. Seleccionar un Hub: Si tienes varios hubs, selecciona el que deseas usar. Si quieres crear un hub nuevo, puedes hacerlo en este paso.

4. Configurar el Proyecto: Sigue las indicaciones para configurar tu proyecto según tus necesidades.

5. Crear el Proyecto: Haz clic en "Create" para finalizar la configuración.

### Desplegar un Modelo y Endpoint para modelo OpenAI

1. Inicia sesión en el [portal de Azure AI Foundry](https://ai.azure.com): Asegúrate de estar conectado con la suscripción de Azure que contiene tu recurso de Azure OpenAI Service.

2. Navega a Models and Endpount: Desde la página principal de Azure AI Foundry, encuentra el recuadro que dice " y selecciona "Let's go." o Model and Endpoints en el menú lateral izquierdo.

3. Si aún no tienes un modelo GPT desplegado, selecciona deploy model: elige un modelo GPT; recomendamos GPT-4o, GPT-4o-mini u o3-mini.

4. Accede a tus recursos: Deberías ver tus recursos existentes de Azure OpenAI Service. Si tienes varios recursos, usa el selector para elegir con cuál quieres trabajar.

Para instrucciones más detalladas, puedes consultar la documentación oficial de Azure AI Foundry.

[How to Create a project](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[How to Create resources](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[How to use OpenAI Model in AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[OpenAI Services in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.