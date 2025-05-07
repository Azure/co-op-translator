<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T14:04:01+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "es"
}
-->
# Cómo usar la interfaz de línea de comandos (CLI) de Co-op Translator

## Requisitos previos

- **Python 3.10 o superior**: Necesario para ejecutar Co-op Translator.  
- **Recurso de modelo de lenguaje**:  
  - **Azure OpenAI** u otros LLMs. Los detalles se encuentran en [modelos y servicios compatibles](../../../../README.md).  
- **Recurso de Visión por Computadora** (opcional):  
  - Para la traducción de imágenes. Si no está disponible, el traductor funcionará en [modo solo Markdown](../markdown-only-mode.md).  
  - **Azure Computer Vision**  

## Tabla de contenido

1. [Crear un archivo '.env' en el directorio raíz](./create-env-file.md)  
   - Incluye las claves necesarias para el servicio del modelo de lenguaje elegido.  
   - Si se omiten las claves de Azure Computer Vision o se especifica `-md`, el traductor operará en modo solo Markdown.  
1. [Instalar el paquete Co-op translator](./install-package.md)  
1. [Traducir tu proyecto usando Co-op Translator](./translator-your-project.md)

**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.