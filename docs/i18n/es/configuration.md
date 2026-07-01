# Configuración

Co-op Translator requiere un proveedor de modelo de lenguaje. La traducción de imágenes además requiere Azure AI Vision.

La configuración se lee de variables de entorno. Para proyectos locales, colócalas en un archivo `.env` en la raíz del proyecto.

Para la configuración de recursos de Azure, consulta [Configuración de Azure AI](azure-ai-setup.md).

## Configuración del entorno local

Usa un entorno virtual antes de ejecutar la CLI de forma local. Co-op Translator es compatible con Python 3.10 a 3.12.

Para el uso normal de la CLI, instala el paquete publicado dentro de un entorno virtual:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Para el desarrollo del repositorio, instala las dependencias desde la raíz del proyecto en su lugar:

```bash
poetry install
poetry run translate --help
```

Después de que la CLI esté disponible, configura un proveedor de modelo de lenguaje en `.env`.

## Selección de proveedor

La herramienta detecta automáticamente los proveedores en este orden:

1. Azure OpenAI
2. OpenAI

Si ningún proveedor está configurado, `translate`, `evaluate`, `migrate-links`, y `run_translation` fallan durante las comprobaciones de configuración. `co-op-review` y `run_review` son comprobaciones determinísticas de mantenimiento y no requieren credenciales de proveedor.

## Azure OpenAI

Usa Azure OpenAI cuando tu modelo esté desplegado en Azure AI Foundry o Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

La comprobación de conectividad utiliza el endpoint, la clave de API, la versión de la API y el nombre del despliegue antes de que comience la traducción.

## OpenAI

Usa OpenAI cuando llames a la API de OpenAI directamente.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # opcional
OPENAI_BASE_URL="..."        # opcional
```

`OPENAI_CHAT_MODEL_ID` es obligatorio porque el traductor necesita un modelo de chat explícito para las llamadas a la API.

## Azure AI Vision

La traducción de imágenes requiere Azure AI Vision para que la herramienta pueda extraer texto de las imágenes antes de traducirlo.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Si se selecciona la traducción de imágenes con `-img`, `images=True`, o sin filtro de tipo de contenido, la herramienta valida la configuración de Vision antes de que comience la traducción.

## Múltiples conjuntos de credenciales

La capa de configuración admite múltiples conjuntos de credenciales agregando un sufijo con el mismo índice a las variables:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Cada conjunto debe estar completo. La comprobación de estado selecciona un conjunto funcional antes de que continúe la traducción.

## Requisitos de los comandos

| Comando o API | LLM requerido | Vision requerida | Notas |
| --- | --- | --- | --- |
| `translate -md` | Sí | No | Traduce solo Markdown. |
| `translate -nb` | Sí | No | Traduce solo notebooks. |
| `translate -img` | Sí | Sí | Traduce solo imágenes. |
| `translate` with no type flags | Sí | Sí | El modo predeterminado incluye Markdown, notebooks e imágenes. |
| `evaluate` | Sí | No | Utiliza la evaluación por LLM a menos que se seleccione `--fast`. |
| `migrate-links` | Sí | No | Realiza la migración de enlaces, pero aún ejecuta las comprobaciones compartidas de configuración. |
| `co-op-review` | No | No | Ejecuta comprobaciones determinísticas de estructura de traducción, frescura, Markdown, notebooks y enlaces locales. |
| `run_translation(markdown=True)` | Sí | No | Traducción programática de Markdown. |
| `run_translation(images=True)` | Sí | Sí | Traducción programática de imágenes. |
| `run_review(...)` | No | No | Revisión determinística programática. |

## Directorios de salida

Salida predeterminada de traducción de texto:

```text
translations/<language-code>/<source-relative-path>
```

Salida predeterminada de imágenes traducidas:

```text
translated_images/<language-code>/<source-relative-path>
```

La API de Python puede sobrescribir estos directorios con `translations_dir` y `image_dir`.