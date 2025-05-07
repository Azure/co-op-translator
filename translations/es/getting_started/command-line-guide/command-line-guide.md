<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:52:14+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "es"
}
-->
# Cómo usar la interfaz de línea de comandos (CLI) de Co-op Translator

## Requisitos previos

- **Python 3.10 o superior**: Necesario para ejecutar Co-op Translator.
- **Recurso de Modelo de Lenguaje**:  
  - **Azure OpenAI** u otros LLMs. Más detalles en [modelos y servicios soportados](../../../../README.md).
- **Recurso de Visión por Computadora** (opcional):  
  - Para traducción de imágenes. Si no está disponible, el traductor funcionará en [modo solo Markdown](../markdown-only-mode.md).  
  - **Azure Computer Vision**

### Configuración inicial

Antes de comenzar, asegúrate de configurar los siguientes recursos:

- [Configurar Azure OpenAI](../set-up-resources/set-up-azure-openai.md)
- [Configurar Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md) (opcional)

## Tabla de contenidos

1. [Crear un archivo '.env' en el directorio raíz](./create-env-file.md)  
   - Incluye las claves necesarias para el servicio del modelo de lenguaje elegido.  
   - Si se omiten las claves de Azure Computer Vision o se especifica `-md`, el traductor funcionará en modo solo Markdown.  
3. [Instalar el paquete Co-op translator](./install-package.md)  
4. [Traducir tu proyecto usando Co-op Translator](./translator-your-project.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.