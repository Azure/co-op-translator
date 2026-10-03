# Configuración

Co-op Translator requiere un proveedor de modelos de lenguaje. La traducción de imágenes además requiere Azure AI Vision.

La configuración se lee de variables de entorno. Para proyectos locales, colóquelas en un archivo `.env` en la raíz del proyecto.

Para la configuración de recursos de Azure, consulte [Configuración de Azure AI](azure-ai-setup.md).

## Configuración del entorno local

Use un entorno virtual antes de ejecutar la CLI localmente. Co-op Translator es compatible con Python 3.11 a 3.14.

Para el uso normal de la CLI, instale el paquete publicado dentro de un entorno virtual:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Desarrollo del repositorio

Para el desarrollo del repositorio, instale las dependencias desde la raíz del proyecto en su lugar:

```bash
poetry install
poetry run translate --help
```

Una vez que la CLI esté disponible, configure un proveedor de modelos de lenguaje en `.env`.

## Selección de proveedor

La herramienta detecta automáticamente los proveedores en este orden:

1. Azure OpenAI
2. OpenAI
3. Anthropic

La traducción requiere credenciales del proveedor, exceptuando vistas previas como `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review` y `run_review` son operaciones de mantenimiento deterministas y no requieren credenciales del proveedor.

## Backend del cliente de modelo

A partir de Co-op Translator 0.22.0, Azure OpenAI, OpenAI y Anthropic utilizan Microsoft Agent Framework por defecto. No se requiere una configuración de backend para el uso normal.

Semantic Kernel permanece disponible temporalmente por compatibilidad. Para seleccionarlo explícitamente, establezca:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

El uso de Semantic Kernel genera una advertencia de desaprobación. Está previsto que el paquete mueva Semantic Kernel a una dependencia opcional en 0.23.0 y elimine la integración en 0.24.0, sujeto a los resultados de compatibilidad y comentarios de los usuarios. Anthropic requiere `agent-framework`; seleccionar explícitamente `semantic-kernel` con Anthropic falla con un error de configuración. Los valores inválidos fallan durante la inicialización del traductor respaldado por el proveedor en lugar de retroceder silenciosamente. Siga el despliegue e informe bloqueos en [Incidencia de GitHub #543](https://github.com/Azure/co-op-translator/issues/543).

## Azure OpenAI

Use Azure OpenAI cuando su modelo esté desplegado en Azure AI Foundry o en Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

La comprobación de conectividad utiliza el endpoint, la clave de API, la versión de la API y el nombre de despliegue antes de que comience la traducción.

## OpenAI

Use OpenAI cuando llame a la API de OpenAI directamente.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` es obligatorio porque el traductor necesita un modelo de chat explícito para las llamadas a la API.

Deje `OPENAI_ORG_ID` y `OPENAI_BASE_URL` sin configurar para la configuración predeterminada. Añada un ID de organización solo si su cuenta lo necesita, o una URL base solo cuando use un endpoint personalizado. No copie valores de marcador de posición para ajustes opcionales.

## Anthropic Claude

Use Anthropic cuando llame a la API de Claude directamente. Cree una [clave de API de Anthropic](https://platform.claude.com/docs/en/get-started) y elija un [ID de modelo Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) compatible.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` y `ANTHROPIC_MODEL` son obligatorios. No necesita establecer `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework es el backend por defecto.

Deje `ANTHROPIC_BASE_URL` sin configurar para la API de Anthropic. Establézcalo solo cuando utilice un endpoint personalizado.

`ANTHROPIC_MAX_TOKENS` por defecto es `8192`, lo que deja espacio para guiones ricos en tokens como Meitei Mayek. Redúzcalo si su modelo o endpoint compatible con Anthropic limita la salida por debajo de eso.

## Azure AI Vision

La traducción de imágenes requiere Azure AI Vision para que la herramienta pueda extraer texto de las imágenes antes de que el modelo de lenguaje configurado lo traduzca. Anthropic puede traducir el texto extraído al igual que Azure OpenAI u OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Si la traducción de imágenes se selecciona con `-img`, `images=True`, o sin filtro de tipo de contenido, la herramienta valida la configuración de Vision antes de que comience la traducción.

## Conjuntos de credenciales múltiples

La capa de configuración admite múltiples conjuntos de credenciales añadiendo un sufijo con el mismo índice a las variables:

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

OpenAI y Anthropic admiten la misma convención de sufijos. Mantenga cada variable en un conjunto de credenciales con el mismo sufijo, incluidos valores opcionales como `OPENAI_BASE_URL_1` o `ANTHROPIC_BASE_URL_1`.

## Requisitos de comando

| Comando o API | LLM requerido | Visión requerida | Notas |
| --- | --- | --- | --- |
| `translate -md` | Sí | No | Traduce solo Markdown. |
| `translate -nb` | Sí | No | Traduce solo cuadernos. |
| `translate -img` | Sí | Sí | Traduce solo imágenes. |
| `translate` with no type flags | Sí | Sí | El modo predeterminado incluye Markdown, cuadernos y imágenes. |
| `evaluate` | Sí | No | Utiliza evaluación por LLM a menos que se seleccione `--fast`. |
| `migrate-links` | No | No | Realiza la migración de enlaces local sin llamadas al proveedor. |
| `co-op-review` | No | No | Ejecuta comprobaciones deterministas de estructura de traducción, frescura, Markdown, notebooks y enlaces locales. |
| `run_translation(markdown=True)` | Sí | No | Traducción de Markdown programática. |
| `run_translation(images=True)` | Sí | Sí | Traducción de imágenes programática. |
| `run_review(...)` | No | No | Revisión determinista programática. |

## Directorios de salida

Salida predeterminada de traducción de texto:

```text
translations/<language-code>/<source-relative-path>
```

Salida predeterminada de imágenes traducidas:

```text
translated_images/<language-code>/<source-relative-path>
```

La API de Python puede anular estos directorios con `translations_dir` y `image_dir`.