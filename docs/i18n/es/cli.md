# Referencia de la CLI

Co-op Translator instala estos puntos de entrada de línea de comandos:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Los comandos `translate`, `evaluate`, `migrate-links` y `co-op-review` se despachan a través de `co_op_translator.__main__`, que selecciona la implementación del comando según el nombre del script invocado. El servidor MCP usa `co_op_translator.mcp.server` directamente.

Si está decidiendo entre la CLI, la API de Python y MCP, comience con [Elija su flujo de trabajo](workflows.md).

## Flujo inicial de la CLI

Comience aquí si está usando Co-op Translator desde una terminal:

1. Configure un proveedor LLM como se describe en [Configuración](configuration.md).
2. Elija el tipo de contenido que desea traducir.
3. Ejecute primero un comando enfocado, como la traducción solo de Markdown.
4. Use `--dry-run` antes de realizar cambios grandes en el repositorio.
5. Use `co-op-review` después de la traducción para comprobar la estructura y la actualidad.

| Objetivo | Comando para iniciar |
| --- | --- |
| Traducir documentos Markdown | `translate -l "ko" -md` |
| Traducir notebooks | `translate -l "ko" -nb` |
| Traducir texto de imágenes | `translate -l "ko" -img` |
| Previsualizar el trabajo sin escribir archivos | `translate -l "ko" -md --dry-run` |
| Revisar traducciones existentes | `co-op-review -l "ko"` |
| Actualizar enlaces de notebooks y Markdown | `migrate-links -l "ko" --dry-run` |
| Exponer herramientas a un cliente MCP | Configure el [Servidor MCP](mcp.md) en lugar de ejecutar los comandos de la CLI directamente. |

## translate

Traduce archivos Markdown, notebooks y texto de imágenes a uno o más idiomas de destino.

```bash
translate -l "ko ja fr"
```

### Ejemplos comunes

Traducir solo Markdown:

```bash
translate -l "de" -md
```

Traducir solo notebooks:

```bash
translate -l "zh-CN" -nb
```

Traducir Markdown e imágenes:

```bash
translate -l "pt-BR" -md -img
```

Actualizar traducciones existentes eliminándolas y recreándolas:

```bash
translate -l "ko" -u
```

Ejecutar sin avisos interactivos:

```bash
translate -l "ko ja" -md -y
```

Guardar registros:

```bash
translate -l "ko" -s
```

### Opciones

| Opción | Requerido | Descripción |
| --- | --- | --- |
| `-l`, `--language-codes` | Sí | Códigos de idioma separados por espacios, como `"es fr de"`, o `"all"`. |
| `-r`, `--root-dir` | No | Raíz del proyecto. Por defecto, el directorio actual. |
| `-u`, `--update` | No | Eliminar las traducciones existentes para los idiomas seleccionados y volver a crearlas. |
| `-img`, `--images` | No | Traducir solo archivos de imagen. |
| `-md`, `--markdown` | No | Traducir solo archivos Markdown. |
| `-nb`, `--notebook` | No | Traducir solo archivos de Jupyter Notebook. |
| `-d`, `--debug` | No | Habilitar registro de depuración en la consola. |
| `-s`, `--save-logs` | No | Guardar registros de nivel DEBUG en `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Retraducir archivos Markdown de baja confianza basándose en resultados de evaluaciones previas. |
| `-c`, `--min-confidence` | No | Umbral de confianza para `--fix`. Por defecto `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Agregar o suprimir avisos de traducción automática. Por defecto está habilitado en la CLI. |
| `-f`, `--fast` | No | Modo rápido de imágenes obsoleto. |
| `-y`, `--yes` | No | Confirmar automáticamente los avisos, útil en CI. |
| `--repo-url` | No | URL del repositorio utilizada en el aviso de sparse-checkout de la tabla de idiomas del README. |
| `--migrate-language-folders` | No | Renombrar carpetas alias heredadas, como `cn` o `tw`, a carpetas canónicas BCP 47. |
| `--dry-run` | No | Previsualizar la migración de carpetas de idioma y estimaciones de traducción sin escribir archivos. |

Si no se proporciona ningún indicador de tipo, `translate` procesa Markdown, notebooks e imágenes. La traducción de imágenes requiere la configuración de Azure AI Vision.

## evaluate

Evalúa la calidad de las traducciones de Markdown para un idioma.

!!! warning "Experimental"
    `evaluate` is experimental. It can use rule-based and LLM-based quality checks, writes evaluation results into translation metadata, and its scoring model and metadata behavior may change.

```bash
evaluate -l "ko"
```

### Ejemplos comunes

Usar un umbral de baja confianza más estricto:

```bash
evaluate -l "es" -c 0.8
```

Ejecutar solo comprobaciones basadas en reglas:

```bash
evaluate -l "fr" -f
```

Ejecutar solo comprobaciones basadas en LLM:

```bash
evaluate -l "ja" -D
```

### Opciones

| Opción | Requerido | Descripción |
| --- | --- | --- |
| `-l`, `--language-code` | Sí | Código de idioma único a evaluar. Los códigos alias se normalizan. |
| `-r`, `--root-dir` | No | Raíz del proyecto. Por defecto, el directorio actual. |
| `-c`, `--min-confidence` | No | Umbral usado al listar traducciones de baja confianza. Por defecto `0.7`. |
| `-d`, `--debug` | No | Habilitar registro de depuración. |
| `-s`, `--save-logs` | No | Guardar registros de nivel DEBUG en `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Evaluación basada en reglas únicamente. |
| `-D`, `--deep` | No | Evaluación basada en LLM únicamente. |

Por defecto, `evaluate` usa tanto la evaluación basada en reglas como la basada en LLM. Los resultados se escriben en los metadatos de traducción y se resumen en la consola.

## co-op-review

Ejecuta comprobaciones deterministas de mantenimiento de traducciones sin credenciales de API.

!!! note "Beta"
    `co-op-review` is a beta deterministic review command. It does not call model providers or write files, but its checks and issue output schema may evolve.

```bash
co-op-review -l "ko"
```

### Ejemplos comunes

Revisar las traducciones al coreano y al japonés desde el directorio actual:

```bash
co-op-review -l "ko ja"
```

Revisar una raíz de proyecto específica:

```bash
co-op-review -l "fr" -r ./my-course
```

Revisar solo los archivos fuente cambiados respecto a una referencia base:

```bash
co-op-review -l "ko" --changed-from origin/main
```

Imprimir salida en Markdown con formato GitHub para resúmenes de CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Opciones

| Opción | Requerido | Descripción |
| --- | --- | --- |
| `-l`, `--language-code` | No | Código de idioma a revisar. Puede pasarse varias veces o como un valor separado por espacios. Por defecto, todos los idiomas de traducción detectados. |
| `-r`, `--root-dir` | No | Raíz del proyecto. Por defecto, el directorio actual. |
| `--changed-from` | No | Ref Git utilizada para limitar la revisión a archivos fuente cambiados. |
| `--format` | No | Formato de salida: `text` o `github`. Por defecto `text`. |

`co-op-review` actualmente comprueba archivos traducidos faltantes, metadatos de traducción faltantes o desactualizados, la integridad del frontmatter de Markdown y de los bloques de código, JSON de notebooks traducidos inválido y objetivos de enlaces locales de Markdown o imágenes faltantes. Los enlaces faltantes son advertencias por defecto; los problemas de estructura y actualidad hacen que el comando falle.

## co-op-translator-mcp

Ejecute el servidor MCP de Co-op Translator para agentes, editores y clientes compatibles con MCP.

```bash
co-op-translator-mcp
```

El transporte predeterminado es `stdio`. Consulte la guía [Servidor MCP](mcp.md) para la configuración del cliente, herramientas, recursos y notas de seguridad.

### Opciones

| Opción | Requerido | Descripción |
| --- | --- | --- |
| `--transport` | No | Transporte MCP: `stdio`, `streamable-http` o `sse`. Por defecto `stdio`. |

## migrate-links

Vuelva a procesar archivos Markdown traducidos y actualice los enlaces de notebooks para que apunten a notebooks traducidos cuando estén disponibles.

```bash
migrate-links -l "ko ja"
```

### Ejemplos comunes

Previsualizar actualizaciones de enlaces:

```bash
migrate-links -l "ko" --dry-run
```

Procesar todos los idiomas compatibles sin confirmación:

```bash
migrate-links -l "all" -y
```

Reescribir enlaces solo cuando existan notebooks traducidos:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Opciones

| Opción | Requerido | Descripción |
| --- | --- | --- |
| `-l`, `--language-codes` | Sí | Códigos de idioma separados por espacios, o `"all"`. |
| `-r`, `--root-dir` | No | Raíz del proyecto. Por defecto, el directorio actual. |
| `--image-dir` | No | Directorio de imágenes traducidas relativo a la raíz. Por defecto `translated_images`. |
| `--dry-run` | No | Mostrar archivos que cambiarían sin escribir actualizaciones. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Usar enlaces originales de notebooks cuando faltan notebooks traducidos. Habilitado por defecto. |
| `-d`, `--debug` | No | Habilitar registro de depuración. |
| `-s`, `--save-logs` | No | Guardar registros de nivel DEBUG en `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Confirmar automáticamente los avisos al procesar todos los idiomas. |

## Entorno

Todos los comandos requieren un proveedor LLM configurado:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# O OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

La traducción de imágenes además requiere Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Estructura de salida

Las traducciones de texto se escriben en:

```text
translations/<language-code>/<original-path>
```

La salida de imágenes traducidas se escribe en:

```text
translated_images/<language-code>/<original-path>
```

Por ejemplo, traducir `README.md` y `docs/setup.md` al coreano produce:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Ejemplos de CLI para copiar y pegar

Traducir Markdown a tres idiomas:

```bash
translate -l "ko ja fr" -md
```

Traducir solo notebooks:

```bash
translate -l "zh-CN" -nb
```

Traducir solo imágenes:

```bash
translate -l "pt-BR" -img
```

Previsualizar la traducción de Markdown sin escribir archivos:

```bash
translate -l "de es" -md --dry-run
```

Reparar traducciones Markdown de baja confianza:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Ejecutar traducción de Markdown adecuada para CI:

```bash
translate -l "ko ja" -md -y -s
```

Revisar la salida traducida:

```bash
co-op-review -l "ko ja"
```

Previsualizar la migración de enlaces:

```bash
migrate-links -l "ko" --dry-run
```