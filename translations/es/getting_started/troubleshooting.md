<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-05-06T17:50:09+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "es"
}
-->
# Guía de solución de problemas de Microsoft Co-op Translator


## Visión general
Microsoft Co-Op Translator es una herramienta poderosa para traducir documentos Markdown de forma fluida. Esta guía te ayudará a solucionar problemas comunes al usar la herramienta.

## Problemas comunes y soluciones

### 1. Problema con la etiqueta Markdown
**Problema:** El documento Markdown traducido incluye una etiqueta `markdown` en la parte superior, lo que causa problemas al mostrarlo.

**Solución:** Para resolverlo, simplemente elimina la etiqueta `markdown` en la parte superior del archivo. Esto permitirá que el archivo Markdown se muestre correctamente.

**Pasos:**
1. Abre el archivo Markdown traducido (`.md`).
2. Ubica la etiqueta `markdown` en la parte superior del documento.
3. Elimina la etiqueta `markdown`.
4. Guarda los cambios en el archivo.
5. Vuelve a abrir el archivo para asegurarte de que se muestre correctamente.

### 2. Problema con las URL de imágenes incrustadas
**Problema:** Las URL de las imágenes incrustadas no coinciden con la configuración regional del idioma, lo que provoca imágenes incorrectas o que no se muestren.

**Solución:** Revisa la URL de las imágenes incrustadas y asegúrate de que coincidan con la configuración regional del idioma. Todas las imágenes están ubicadas en la carpeta `translated_images` y cada imagen tiene una etiqueta de configuración regional en el nombre del archivo.

**Pasos:**
1. Abre el documento Markdown traducido.
2. Identifica las imágenes incrustadas y sus URL.
3. Verifica que la configuración regional del idioma en el nombre del archivo de la imagen coincida con el idioma del documento.
4. Actualiza las URL si es necesario.
5. Guarda los cambios y vuelve a abrir el documento para confirmar que las imágenes se muestren correctamente.

### 3. Precisión de la traducción
**Problema:** El contenido traducido no es preciso o requiere más edición.

**Solución:** Revisa el documento traducido y realiza las ediciones necesarias para mejorar la precisión y legibilidad.

**Pasos:**
1. Abre el documento traducido.
2. Revisa el contenido cuidadosamente.
3. Realiza las ediciones necesarias para mejorar la precisión de la traducción.
4. Guarda los cambios.

### 4. Problemas de formato del archivo
**Problema:** El formato del documento traducido es incorrecto. Esto puede ocurrir en tablas; aquí un ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` adicional solucionará los problemas de tabla.

**Pasos:**
1. Abre el documento traducido.
2. Compáralo con el documento original para identificar problemas de formato.
3. Ajusta el formato para que coincida con el documento original.
4. Guarda los cambios.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.