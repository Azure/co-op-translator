# Referencia de la CLI

Co-op Translator instala estos puntos de entrada de la línea de comandos:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Los comandos `translate`, `evaluate`, `migrate-links` y `co-op-review` se enrutan a través de `co_op_translator.__main__`, que selecciona la implementación del comando según el nombre del script invocado. El servidor MCP utiliza `co_op_translator.mcp.server` directamente.

Si dudas entre la CLI, la API de Python y MCP, comienza con [Elige tu flujo de trabajo](workflows.md).

## Salida de la consola

Los terminales interactivos usan el formato Rich para el encabezado del comando, el progreso y los resúmenes. La salida en CI y en entornos no interactivos vuelve automáticamente a texto plano.

Fija `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` para forzar salida en texto plano, o `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` para forzar salida Rich. Establece `CO_OP_TRANSLATOR_NO_PROGRESS=1` para mantener los resúmenes mientras se suprimen las barras de progreso en vivo.

Usa `translate --json-events progress.ndjson` cuando otro sistema necesite
progreso legible por máquina. La CLI sigue mostrando salida para humanos, mientras que
el archivo NDJSON recibe eventos versionados `co-op.translation.event.v1` con
campos estables como `type`, `stage_key`, `completed`, `total`, y
`current_path`.

## Flujo inicial de la CLI

Empieza aquí si usas Co-op Translator desde un terminal:

1. Configura un proveedor de LLM como se describe en [Configuración](configuration.md).
2. Elige el tipo de contenido que quieres traducir.
3. Ejecuta primero un comando enfocado, como la traducción solo de Markdown.
4. Usa `--dry-run` antes de hacer cambios grandes en el repositorio.
5. Usa `co-op-review` después de la traducción para comprobar la estructura y vigencia.

| Objetivo | Comando para empezar |
| --- | --- |
| Traducir documentos Markdown | `translate -l "ko" -md` |
| Traducir notebooks | `translate -l "ko" -nb` |
| Traducir texto de imágenes | `translate -l "ko" -img` |
| Previsualizar el trabajo sin escribir archivos | `translate -l "ko" -md --dry-run` |
| Revisar traducciones existentes | `co-op-review -l "ko"` |
| Actualizar enlaces de notebooks y Markdown | `migrate-links -l "ko" --dry-run` |
| Exponer herramientas a un cliente MCP | Configura el [Servidor MCP](mcp.md) en lugar de ejecutar comandos de la CLI directamente. |

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

Ejecutar sin solicitudes interactivas:

```bash
translate -l "ko ja" -md -y
```

Guardar registros:

```bash
translate -l "ko" -s
```

Escribir eventos de progreso estructurados:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Opciones

| Opción | Requerido | Descripción |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Códigos de idioma separados por espacios, como `"es fr de"`, o `"all"`. |
| `-r`, `--root-dir` | No | Directorio raíz del proyecto. Por defecto, el directorio actual. |
| `-u`, `--update` | No | Eliminar las traducciones existentes para los idiomas seleccionados y volver a crearlas. |
| `-img`, `--images` | No | Traducir solo archivos de imagen. |
| `-md`, `--markdown` | No | Traducir solo archivos Markdown. |
| `-nb`, `--notebook` | No | Traducir solo archivos Jupyter notebook. |
| `-d`, `--debug` | No | Habilitar el registro de depuración en la consola. |
| `-s`, `--save-logs` | No | Guardar registros de nivel DEBUG en `<root-dir>/logs/`. |
| `--json-events` | No | Escribir eventos de progreso de la traducción legibles por máquina como NDJSON. |
| `-x`, `--fix` | No | Retraducir archivos Markdown de baja confianza en base a resultados de evaluaciones previas. |
| `-c`, `--min-confidence` | No | Umbral de confianza para `--fix`. Por defecto `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Agregar o suprimir descargos de responsabilidad de traducción automática. Por defecto está habilitado en la CLI. |
| `-f`, `--fast` | No | Modo rápido de imágenes (obsoleto). |
| `-y`, `--yes` | No | Confirmar automáticamente las solicitudes; útil en CI. |
| `--repo-url` | No | URL del repositorio usada en el aviso de sparse-checkout de la tabla de idiomas del README. |
| `--migrate-language-folders` | No | Renombrar carpetas alias antiguas, como `cn` o `tw`, a carpetas canónicas BCP 47. |
| `--dry-run` | No | Previsualizar la migración de carpetas de idioma y las estimaciones de traducción sin escribir archivos. |

Si no se proporciona una bandera de tipo, `translate` procesa Markdown, notebooks e imágenes. La traducción de imágenes requiere configuración de Azure AI Vision.

## evaluate

Evaluar la calidad de las traducciones Markdown para un idioma.

!!! warning "Experimental"
    `evaluate` es experimental. Puede usar comprobaciones de calidad basadas en reglas y basadas en LLM, escribe los resultados de la evaluación en los metadatos de la traducción, y su modelo de puntuación y comportamiento de metadatos puede cambiar.

```bash
evaluate -l "ko"
```

### Ejemplos comunes

Usa un umbral de baja confianza más estricto:

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
| `-l`, `--language-code` | Yes | Código de idioma único a evaluar. Los códigos alias se normalizan. |
| `-r`, `--root-dir` | No | Directorio raíz del proyecto. Por defecto, el directorio actual. |
| `-c`, `--min-confidence` | No | Umbral usado al listar traducciones de baja confianza. Por defecto `0.7`. |
| `-d`, `--debug` | No | Habilitar registro de depuración. |
| `-s`, `--save-logs` | No | Guardar registros de nivel DEBUG en `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Solo evaluación basada en reglas. |
| `-D`, `--deep` | No | Solo evaluación basada en LLM. |

Por defecto, `evaluate` usa tanto evaluación basada en reglas como basada en LLM. Los resultados se escriben en los metadatos de traducción y se resumen en la consola.

## co-op-review

Ejecuta comprobaciones deterministas de mantenimiento de traducciones sin credenciales de API.

!!! note "Beta"
    `co-op-review` es un comando de revisión determinista en beta. No llama a proveedores de modelos ni escribe archivos, pero sus comprobaciones y el esquema de salida de problemas pueden evolucionar.

```bash
co-op-review -l "ko"
```

### Ejemplos comunes

Revisar traducciones al coreano y al japonés desde el directorio actual:

```bash
co-op-review -l "ko ja"
```

Revisar un directorio raíz de proyecto específico:

```bash
co-op-review -l "fr" -r ./my-course
```

Revisar solo el README después de una traducción solo de README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` ignora otros documentos y READMEs anidados. Falla si falta el `README.md` raíz. Combinado con `--changed-from`, revisa solo el README cuando ese archivo fuente cambió. La traducción solo del README deja el README fuente sin cambios, incluyendo cualquier marcador de sección compartida.




Revisar únicamente archivos fuente cambiados respecto a una referencia base:

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
| `-l`, `--language-code` | No | Código de idioma a revisar. Puede pasarse varias veces o como un valor separado por espacios. Por defecto, todos los idiomas de traducción descubiertos. |
| `-r`, `--root-dir` | No | Directorio raíz del proyecto. Por defecto, el directorio actual. |
| `--changed-from` | No | Referencia Git usada para limitar la revisión a archivos fuente cambiados. |
| `--readme-only` | No | Revisar solo la traducción del `README.md` raíz. |
| `--format` | No | Formato de salida: `text` o `github`. Por defecto `text`. |

`co-op-review` actualmente comprueba archivos traducidos faltantes, metadatos de traducción faltantes o desactualizados, la integridad del frontmatter y de los bloques de código en Markdown, JSON de notebook traducido inválido y objetivos de enlaces locales de Markdown o imagen faltantes. Los enlaces faltantes son advertencias por defecto; los problemas de estructura y vigencia hacen que el comando falle.

## co-op-translator-mcp

Ejecuta el servidor MCP de Co-op Translator para agentes, editores y clientes compatibles con MCP.

```bash
co-op-translator-mcp
```

El transporte por defecto es `stdio`. Consulta la guía del [Servidor MCP](mcp.md) para la configuración del cliente, herramientas, recursos y notas de seguridad.

### Opciones

| Opción | Requerido | Descripción |
| --- | --- | --- |
| `--transport` | No | Transporte MCP: `stdio`, `streamable-http`, o `sse`. Por defecto `stdio`. |

## migrate-links

Reprocesa archivos Markdown traducidos y actualiza enlaces de notebooks para que apunten a notebooks traducidos cuando estén disponibles.

```bash
migrate-links -l "ko ja"
```

### Ejemplos comunes

Previsualizar actualizaciones de enlaces:

```bash
migrate-links -l "ko" --dry-run
```

Procesar todos los idiomas soportados sin confirmación:

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
| `-l`, `--language-codes` | Yes | Códigos de idioma separados por espacios, o `"all"`. |
| `-r`, `--root-dir` | No | Directorio raíz del proyecto. Por defecto, el directorio actual. |
| `--image-dir` | No | Directorio de imágenes traducidas relativo al directorio raíz. Por defecto `translated_images`. |
| `--dry-run` | No | Mostrar archivos que cambiarían sin escribir actualizaciones. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Usar enlaces de notebook originales cuando faltan notebooks traducidos. Habilitado por defecto. |
| `-d`, `--debug` | No | Habilitar registro de depuración. |
| `-s`, `--save-logs` | No | Guardar registros de nivel DEBUG en `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Confirmar automáticamente las solicitudes al procesar todos los idiomas. |

## Entorno

Cuando un comando requiere credenciales de proveedor, configura uno de estos conjuntos de proveedores. `translate --dry-run` y `co-op-review` no requieren credenciales de proveedor:

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

# O Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

La traducción de imágenes requiere además Azure AI Vision:

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

Ejecutar traducción de Markdown amigable para CI:

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