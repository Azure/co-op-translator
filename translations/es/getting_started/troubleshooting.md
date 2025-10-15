<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:10:44+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "es"
}
-->
# Guía de solución de problemas del Traductor Microsoft Co-op

## Descripción general
El Traductor Microsoft Co-Op es una herramienta potente para traducir documentos Markdown de manera fluida. Esta guía te ayudará a resolver los problemas más comunes que pueden surgir al usar la herramienta.

## Problemas comunes y soluciones

### 1. Problema con la etiqueta Markdown
**Problema:** El documento Markdown traducido incluye una etiqueta `markdown` en la parte superior, lo que genera problemas de visualización.

**Solución:** Para solucionarlo, simplemente elimina la etiqueta `markdown` de la parte superior del archivo. Así el archivo Markdown se mostrará correctamente.

**Pasos:**
1. Abre el archivo Markdown (`.md`) traducido.
2. Busca la etiqueta `markdown` en la parte superior del documento.
3. Elimina la etiqueta `markdown`.
4. Guarda los cambios en el archivo.
5. Vuelve a abrir el archivo para asegurarte de que se visualiza correctamente.

### 2. Problema con la URL de imágenes incrustadas
**Problema:** Las URLs de las imágenes incrustadas no coinciden con el idioma del documento, lo que provoca imágenes incorrectas o que no se muestran.

**Solución:** Revisa la URL de las imágenes incrustadas y asegúrate de que coincidan con el idioma del documento. Todas las imágenes se encuentran en la carpeta `translated_images` y cada imagen tiene una etiqueta de idioma en el nombre del archivo.

**Pasos:**
1. Abre el documento Markdown traducido.
2. Identifica las imágenes incrustadas y sus URLs.
3. Verifica que la etiqueta de idioma en el nombre del archivo de la imagen coincida con el idioma del documento.
4. Actualiza las URLs si es necesario.
5. Guarda los cambios y vuelve a abrir el documento para confirmar que las imágenes se muestran correctamente.

### 3. Precisión de la traducción
**Problema:** El contenido traducido no es preciso o necesita más edición.

**Solución:** Revisa el documento traducido y realiza las ediciones necesarias para mejorar la precisión y la legibilidad.

**Pasos:**
1. Abre el documento traducido.
2. Revisa el contenido cuidadosamente.
3. Realiza las ediciones necesarias para mejorar la precisión de la traducción.
4. Guarda los cambios.

## 4. Error de permisos Redacted o 404

Si las imágenes o el texto no se traducen al idioma correcto y al ejecutar en modo -d debug aparece un error 401, se trata de un fallo de autenticación: la clave es inválida, ha expirado o no está vinculada a la región del endpoint.

Ejecuta el traductor co-op con el [interruptor -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) para entender mejor la causa raíz.

- **Mensaje de error:** `Access denied due to invalid subscription key or wrong API endpoint.`
- **Posibles causas:**
  - La clave de suscripción fue redactada o es incorrecta en la solicitud.
  - La clave de Servicios de IA o la clave de suscripción puede pertenecer a otro recurso de Azure (como Translator u OpenAI) en vez de un recurso de **Azure AI Vision**.

 **Tipo de recurso**
  - Ve al [Portal de Azure](https://portal.azure.com) o [Azure AI Foundry](https://ai.azure.com) y asegúrate de que el recurso sea de tipo `Azure AI services` → `Vision`.
  - Valida las claves y asegúrate de que se está usando la clave correcta.

## 5. Errores de configuración (Nuevo manejo de errores)

Con el nuevo sistema de traducción selectiva, Co-op Translator ahora muestra mensajes de error explícitos cuando los servicios requeridos no están configurados.

### 5.1. Servicio Azure AI no configurado para traducción de imágenes

**Problema:** Solicitaste traducción de imágenes (bandera `-img`) pero el servicio Azure AI no está configurado correctamente.

**Mensaje de error:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Solución:**
1. **Opción 1:** Configura el servicio Azure AI
   - Agrega `AZURE_AI_SERVICE_API_KEY` a tu archivo `.env`
   - Agrega `AZURE_AI_SERVICE_ENDPOINT` a tu archivo `.env`
   - Verifica que el servicio sea accesible

2. **Opción 2:** Elimina la solicitud de traducción de imágenes
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Falta configuración requerida

**Problema:** Falta la configuración esencial de LLM.

**Mensaje de error:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Solución:**
1. Verifica que tu archivo `.env` tenga al menos una de las siguientes configuraciones de LLM:
   - **Azure OpenAI:** `AZURE_OPENAI_API_KEY` y `AZURE_OPENAI_ENDPOINT`
   - **OpenAI:** `OPENAI_API_KEY`
   
   Necesitas tener configurado Azure OpenAI O OpenAI, no ambos.

### 5.3. Confusión con la traducción selectiva

**Problema:** No se tradujo ningún archivo aunque el comando se ejecutó correctamente.

**Posibles causas:**
- Banderas de tipo de archivo incorrectas (`-md`, `-img`, `-nb`)
- No hay archivos coincidentes en el proyecto
- Estructura de directorios incorrecta

**Solución:**
1. **Usa el modo debug** para ver qué está pasando:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Revisa los tipos de archivo** en tu proyecto:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Verifica las combinaciones de banderas**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migración desde el sistema anterior

### 6.1. Modo solo Markdown obsoleto

**Problema:** Los comandos que dependían del modo automático solo Markdown ya no funcionan como antes.

**Comportamiento anterior:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Nuevo comportamiento:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Solución:**
- **Sé explícito** sobre lo que quieres traducir:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Comportamiento inesperado de los enlaces

**Problema:** Los enlaces en los archivos traducidos apuntan a ubicaciones inesperadas.

**Causa:** El procesamiento dinámico de enlaces cambia según los tipos de archivo seleccionados.

**Solución:**
1. **Comprende el nuevo comportamiento de los enlaces:**
   - Si incluyes `-nb`: los enlaces a notebooks apuntan a las versiones traducidas
   - Si excluyes `-nb`: los enlaces a notebooks apuntan a los archivos originales
   - Si incluyes `-img`: los enlaces a imágenes apuntan a las versiones traducidas
   - Si excluyes `-img`: los enlaces a imágenes apuntan a los archivos originales

2. **Elige la combinación adecuada** para tu caso de uso:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. La acción de GitHub se ejecutó pero no se creó Pull Request (PR)

**Síntoma:** Los registros del flujo de trabajo para `peter-evans/create-pull-request` muestran:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Causas probables:**
- **No se detectaron cambios:** El paso de traducción no produjo diferencias (el repositorio ya está actualizado).
- **Salidas ignoradas:** `.gitignore` excluye archivos que esperabas subir (por ejemplo, `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths no coincide:** Las rutas proporcionadas a la acción no coinciden con las ubicaciones reales de salida.
- **Lógica/condiciones del flujo de trabajo:** El paso de traducción terminó antes de tiempo o escribió en directorios inesperados.

**Cómo solucionar / verificar:**
1. **Confirma que existen salidas:** Después de la traducción, revisa que el espacio de trabajo tenga archivos nuevos o modificados en `translations/` y/o `translated_images/`.
   - Si traduces notebooks, asegúrate de que los archivos `.ipynb` realmente se escriban bajo `translations/<lang>/...`.
2. **Revisa `.gitignore`:** No ignores las salidas generadas. Asegúrate de NO ignorar:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (si traduces notebooks)
3. **Asegúrate de que add-paths coincida con las salidas:** Usa un valor multilínea e incluye ambas carpetas si aplica:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Fuerza un PR para depuración:** Permite temporalmente commits vacíos para confirmar que la integración es correcta:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Ejecuta con debug:** Agrega `-d` al comando de traducción para imprimir qué archivos se descubrieron y escribieron.
6. **Permisos (GITHUB_TOKEN):** Asegúrate de que el flujo de trabajo tenga permisos de escritura para crear commits y PRs:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Lista rápida de verificación para depuración

Al solucionar problemas de traducción:

1. **Usa el modo debug:** Agrega la bandera `-d` para ver registros detallados
2. **Revisa tus banderas:** Asegúrate de que `-md`, `-img`, `-nb` coincidan con tu intención
3. **Verifica la configuración:** Revisa que tu archivo `.env` tenga las claves requeridas
4. **Haz pruebas incrementales:** Comienza solo con `-md` y luego agrega otros tipos
5. **Revisa la estructura de archivos:** Asegúrate de que los archivos fuente existan y sean accesibles

Para más información sobre los comandos y banderas disponibles, consulta la [Referencia de comandos](./command-reference.md).

---

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.