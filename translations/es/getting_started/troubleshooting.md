<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:21:55+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "es"
}
-->
# Guía de Solución de Problemas del Traductor Microsoft Co-op


## Resumen
El Traductor Microsoft Co-Op es una herramienta poderosa para traducir documentos Markdown de manera fluida. Esta guía te ayudará a resolver problemas comunes que puedas encontrar al usar la herramienta.

## Problemas Comunes y Soluciones

### 1. Problema con la Etiqueta Markdown
**Problema:** El documento Markdown traducido incluye una etiqueta `markdown` al principio, lo que causa problemas de visualización.

**Solución:** Para solucionarlo, simplemente elimina la etiqueta `markdown` al inicio del archivo. Esto permitirá que el archivo Markdown se muestre correctamente.

**Pasos:**
1. Abre el archivo Markdown traducido (`.md`).
2. Localiza la etiqueta `markdown` al principio del documento.
3. Elimina la etiqueta `markdown`.
4. Guarda los cambios en el archivo.
5. Vuelve a abrir el archivo para asegurarte de que se visualice correctamente.

### 2. Problema con las URL de Imágenes Embebidas
**Problema:** Las URLs de las imágenes embebidas no coinciden con la configuración regional del idioma, lo que provoca imágenes incorrectas o que no se muestren.

**Solución:** Revisa la URL de las imágenes embebidas y asegúrate de que coincidan con la configuración regional del idioma. Todas las imágenes están ubicadas en la carpeta `translated_images` y cada imagen tiene una etiqueta de configuración regional en el nombre del archivo.

**Pasos:**
1. Abre el documento Markdown traducido.
2. Identifica las imágenes embebidas y sus URLs.
3. Verifica que la configuración regional en el nombre del archivo de imagen coincida con el idioma del documento.
4. Actualiza las URLs si es necesario.
5. Guarda los cambios y vuelve a abrir el documento para confirmar que las imágenes se muestren correctamente.

### 3. Precisión de la Traducción
**Problema:** El contenido traducido no es preciso o requiere edición adicional.

**Solución:** Revisa el documento traducido y realiza las ediciones necesarias para mejorar la precisión y legibilidad.

**Pasos:**
1. Abre el documento traducido.
2. Revisa el contenido detenidamente.
3. Realiza las ediciones necesarias para mejorar la precisión de la traducción.
4. Guarda los cambios.

### 4. Problemas de Formato del Archivo
**Problema:** El formato del documento traducido es incorrecto. Esto puede ocurrir en tablas; aquí un ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` adicional abordará los problemas con las tablas.

**Pasos:**
1. Abre el documento traducido.
2. Compáralo con el documento original para identificar problemas de formato.
3. Ajusta el formato para que coincida con el documento original.
4. Guarda los cambios.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.