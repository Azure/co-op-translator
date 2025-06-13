<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:30:16+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "cs"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Overview
Microsoft Co-Op Translator es una herramienta potente para traducir documentos Markdown sin problemas. Esta guía te ayudará a resolver problemas comunes que se presentan al usar la herramienta.

## Common Issues and Solutions

### 1. Markdown Tag Issue
**Problem:** El documento Markdown traducido incluye una etiqueta `markdown` en la parte superior, causando problemas de renderizado.

**Solution:** Para solucionarlo, simplemente elimina la etiqueta `markdown` en la parte superior del archivo. Esto permitirá que el archivo Markdown se renderice correctamente.

**Steps:**
1. Abre el archivo Markdown traducido (`.md`).
2. Localiza la etiqueta `markdown` en la parte superior del documento.
3. Elimina la etiqueta `markdown`.
4. Guarda los cambios en el archivo.
5. Vuelve a abrir el archivo para asegurarte de que se renderice correctamente.

### 2. Embedded Images URL Issue
**Problem:** Las URLs de las imágenes incrustadas no coinciden con la configuración regional del idioma, lo que provoca imágenes incorrectas o faltantes.

**Solution:** Verifica la URL de las imágenes incrustadas y asegúrate de que coincidan con la configuración regional del idioma. Todas las imágenes están ubicadas en la carpeta `translated_images`; cada imagen tiene una etiqueta de configuración regional en el nombre del archivo.

**Steps:**
1. Abre el documento Markdown traducido.
2. Identifica las imágenes incrustadas y sus URLs.
3. Verifica que la configuración regional en el nombre del archivo de imagen coincida con el idioma del documento.
4. Actualiza las URLs si es necesario.
5. Guarda los cambios y vuelve a abrir el documento para confirmar que las imágenes se muestren correctamente.

### 3. Translation Accuracy
**Problem:** El contenido traducido no es preciso o requiere edición adicional.

**Solution:** Revisa el documento traducido y realiza las ediciones necesarias para mejorar la precisión y legibilidad.

**Steps:**
1. Abre el documento traducido.
2. Revisa el contenido cuidadosamente.
3. Realiza las ediciones necesarias para mejorar la precisión de la traducción.
4. Guarda los cambios.

### 4. File Formatting Issues
**Problem:** El formato del documento traducido es incorrecto. Esto puede ocurrir en tablas; aquí un ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` adicional abordará los problemas con las tablas.

**Steps:**
1. Abre el documento traducido.
2. Compáralo con el documento original para identificar problemas de formato.
3. Ajusta el formato para que coincida con el documento original.
4. Guarda los cambios.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.