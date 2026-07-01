# Solución de problemas

Use esta página cuando una ejecución de traducción tenga éxito inesperadamente, falle durante la configuración, o produzca resultados que necesiten revisión.

## Comenzar aquí

1. Ejecute primero un comando focalizado, como `translate -l "ko" -md`.
2. Agregue `-d` para registros de depuración en la consola.
3. Agregue `-s` para guardar los registros de depuración en `<root-dir>/logs/`.
4. Ejecute `co-op-review` después de la traducción para comprobar la actualidad, la estructura y los enlaces locales.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Errores de configuración

### Sin proveedor de modelo de lenguaje

Error:

```text
No language model configuration found.
```

Solución:

- Configure Azure OpenAI u OpenAI.
- Verifique que las variables estén en el entorno donde se ejecuta el comando.
- Para uso local, colóquelas en `.env` en la raíz del proyecto.

Vea [Configuración](configuration.md).

### Traducción de imágenes sin Azure AI Vision

Error:

```text
Image translation requested but Azure AI Service is not configured.
```

Solución:

- Agregue `AZURE_AI_SERVICE_API_KEY`.
- Agregue `AZURE_AI_SERVICE_ENDPOINT`.
- O ejecute un comando solo de texto como `translate -l "ko" -md`.

### Clave o endpoint inválidos

Los síntomas pueden incluir `401`, errores de permisos redactados o errores de acceso al endpoint.

Solución:

- Confirme que la clave pertenezca al mismo recurso de Azure que el endpoint.
- Confirme que el recurso sea compatible con Vision al usar `-img`.
- Confirme que el nombre de despliegue de Azure OpenAI y la versión de la API coincidan con su despliegue.
- Ejecute con registros de depuración: `translate -l "ko" -md -d -s`.

## No se tradujeron archivos

Causas comunes:

- Las banderas seleccionadas no coinciden con sus archivos.
- Ya existen archivos traducidos.
- Los archivos fuente están en directorios excluidos.
- El comando se está ejecutando desde la raíz del proyecto equivocada.

Comprobaciones:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Use `--root-dir` cuando el comando se ejecute fuera de la raíz del proyecto.

## Comportamiento inesperado de los enlaces

La reescritura de enlaces depende de los tipos de contenido seleccionados:

- `-nb` incluido: los enlaces de notebooks pueden apuntar a notebooks traducidos.
- `-nb` excluido: los enlaces de notebooks pueden seguir apuntando a los notebooks de origen.
- `-img` incluido: los enlaces de imágenes pueden apuntar a imágenes traducidas.
- `-img` excluido: los enlaces de imágenes pueden seguir apuntando a las imágenes fuente.

Ejecute una traducción completa del contenido cuando todos los enlaces internos deban preferir los resultados traducidos:

```bash
translate -l "ko" -md -nb -img
```

Ejecute la revisión de enlaces después de la traducción:

```bash
co-op-review -l "ko"
```

## Problemas de renderizado de Markdown

Si el Markdown traducido se renderiza incorrectamente:

- Compruebe que el frontmatter comience y termine con `---`.
- Compruebe que el número de delimitadores de código coincida entre los archivos fuente y los traducidos.
- Ejecute `co-op-review` para detectar problemas comunes de estructura.
- Vuelva a traducir el archivo específico si la salida fue corrompida.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action se ejecutó pero no se creó una Pull Request

Si `peter-evans/create-pull-request` informa que la rama no está por delante de la base, el flujo de trabajo no encontró archivos para confirmar.

Causas probables:

- La ejecución de traducción no produjo cambios.
- `.gitignore` excluye `translations/`, `translated_images/` o notebooks traducidos.
- `add-paths` no coincide con los directorios de salida generados.
- El paso de traducción terminó antes de tiempo.

Soluciones:

1. Confirme que los archivos generados existan en `translations/` o `translated_images/`.
2. Confirme que `.gitignore` no ignore los resultados generados.
3. Use `add-paths` correspondiente:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Agregue temporalmente banderas de depuración al comando translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirme que los permisos del flujo de trabajo incluyan:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Calidad de la traducción

Las traducciones automáticas pueden necesitar revisión humana. Use `evaluate` solo cuando quiera puntuaciones de calidad experimentales y flujos de trabajo de reparación para traducciones de baja confianza.

!!! warning "Experimental"
    `evaluate` puede usar comprobaciones basadas en reglas y basadas en LLM, y su modelo de puntuación y el comportamiento de metadatos pueden cambiar. Manténgalo fuera de los controles CI obligatorios a menos que su flujo de trabajo esté preparado para los cambios.

Para comprobaciones de CI deterministas, use `co-op-review` en su lugar.