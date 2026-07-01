# Servidor MCP

Co-op Translator incluye un servidor del Model Context Protocol para agentes, editores y clientes compatibles con MCP.

Para la configuración local predeterminada, los usuarios no mantienen un servidor separado en ejecución manualmente. Configuran su cliente MCP, y el cliente inicia `co-op-translator-mcp` automáticamente sobre `stdio` cuando necesita las herramientas de Co-op Translator.

Si está decidiendo entre CLI, Python API y MCP, comience con [Elija su flujo de trabajo](workflows.md).

Use MCP cuando un agente o editor deba llamar a Co-op Translator directamente:

| Objetivo del usuario | Herramientas MCP |
| --- | --- |
| Translate one Markdown document, notebook, or image | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Translate Markdown or notebook content with the host agent model | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Rewrite translated Markdown or notebook links after choosing the output path | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Translate a full repository like the CLI | `run_translation`, `translate_project` |
| Review translated output without LLM credentials | `run_review` |
| Inspect capabilities and environment status | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

El servidor MCP envuelve la misma API pública de Python documentada en [Python API](api.md). Las herramientas respaldadas por proveedores usan los mismos proveedores configurados que la CLI y la API de Python. Las herramientas asistidas por agentes preparan fragmentos para que el agente host de MCP los traduzca, y luego usan Co-op Translator para reconstruir el Markdown o el cuaderno final.

## Paso 1: Instalar y configurar Co-op Translator

Instale Co-op Translator en el entorno de Python que usará su cliente MCP:

```bash
pip install co-op-translator
```

Para desarrollo local desde este repositorio, instale el paquete en modo editable:

```bash
pip install -e .
```

Elija el modo de traducción que usará su cliente MCP:

| Modo | Úselo para | Credenciales |
| --- | --- | --- |
| Provider-backed | Co-op Translator llama a `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, o `run_translation`. | La traducción de Markdown y cuadernos requiere Azure OpenAI o OpenAI. La traducción de imágenes también requiere Azure AI Vision. |
| Agent-assisted | El agente host de MCP traduce fragmentos devueltos por `start_markdown_agent_translation` o `start_notebook_agent_translation`. | No se requieren credenciales de proveedor LLM de Co-op Translator para fragmentos de Markdown o cuadernos. La traducción de imágenes aún no está cubierta por el modo asistido por agente. |

Si está comenzando con la traducción de Markdown o cuadernos dentro de un agente como Codex o Claude Code, comience con el modo asistido por agente. Use el modo con respaldo de proveedor cuando quiera que Co-op Translator llame a sus proveedores configurados, cuando esté traduciendo imágenes o cuando esté ejecutando traducción a nivel de repositorio como la CLI.

Configure las credenciales del proveedor solo para flujos de trabajo con respaldo de proveedor:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

La traducción de imágenes con respaldo de proveedor además necesita:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Agent-assisted mode currently covers Markdown and notebook Markdown cells. Image translation still uses the provider-backed image pipeline and requires Azure AI Vision for OCR and layout-aware rendering.

## Paso 2: Configure su cliente MCP

Para la configuración normal local `stdio`, agregue Co-op Translator a la configuración de su cliente MCP. El cliente iniciará y detendrá el proceso automáticamente.

Configuración del paquete instalado:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Configuración desde el código fuente en Windows:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

Configuración desde el código fuente en macOS o Linux:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

Después de cambiar la configuración del cliente MCP, reinicie o recargue el cliente para que pueda descubrir el nuevo servidor.

## Paso 3: Verificar el servidor en el cliente

Pida al cliente MCP que liste las herramientas disponibles, o llame primero a uno de los ayudantes de solo lectura:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Comprobaciones útiles iniciales:

| Herramienta | Qué comprobar |
| --- | --- |
| `get_api_overview` | Confirma que el servidor es accesible y muestra los flujos de trabajo disponibles. |
| `list_supported_languages` | Confirma que se pueden cargar los datos de idiomas incluidos. |
| `get_configuration_status` | Confirma la disponibilidad de proveedores LLM y Vision sin exponer valores secretos. |

## Paso 4: Elija un flujo de trabajo

### Traducir archivos o documentos individuales

Use las herramientas de contenido con respaldo de proveedor cuando el cliente MCP ya tenga contenido del documento o una ruta de imagen y Co-op Translator deba llamar a los proveedores de traducción configurados.

Para Markdown:

1. Llame a `translate_markdown_content` con `document`, `language_code` y opcionalmente `source_path`.
2. Si el resultado traducido se escribirá en un diseño de salida de Co-op Translator, llame a `rewrite_markdown_paths`.
3. Deje que el cliente escriba o devuelva el `content` final.

Para cuadernos:

1. Llame a `translate_notebook_content` con el JSON del cuaderno y `language_code`.
2. Llame a `rewrite_notebook_paths` si los enlaces del cuaderno traducido necesitan ajustarse para una ruta de destino.
3. Escriba o devuelva el JSON final del cuaderno.

Para imágenes:

1. Llame a `translate_image_content` con `image_path`, `language_code` y opcionalmente `root_dir` o `fast_mode`.
2. Lea el `data_base64` y el `mime_type` devueltos.
3. Si se proporciona `output_path`, la imagen traducida también se guarda en esa ruta.

Las herramientas de contenido no realizan descubrimiento de proyectos, actualizaciones de metadatos, avisos legales ni reescritura automática de rutas. Si desea que el agente host traduzca fragmentos de Markdown o cuadernos sin credenciales de proveedor LLM de Co-op Translator, use el flujo de trabajo asistido por agente a continuación.

### Traducir con el modelo del agente anfitrión

Use las herramientas asistidas por agente cuando quiera que el agente host de MCP, como un asistente de codificación, produzca el texto traducido en lugar de configurar Azure OpenAI o OpenAI para Co-op Translator.

En un cliente MCP basado en chat, normalmente no necesita escribir el JSON de la herramienta usted mismo. Pida al agente que use el flujo de trabajo asistido por agente:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Para cuadernos, use el mismo patrón:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Si su cliente MCP admite prompts del servidor, use `agent_assisted_markdown_translation_prompt` para que el cliente cargue las mismas instrucciones del flujo de trabajo.

Para Markdown:

1. Llame a `start_markdown_agent_translation` con `document`, `language_code` y opcionalmente `source_path`.
2. Traduzca cada fragmento devuelto en el agente host siguiendo el `prompt` del fragmento.
3. Llame a `finish_markdown_agent_translation` con el `job` original y fragmentos traducidos usando `chunk_id` y `translated_text`.
4. Si el contenido se escribirá en una ruta de destino traducida, llame a `rewrite_markdown_paths`.

Para cuadernos:

1. Llame a `start_notebook_agent_translation` con el JSON del cuaderno y `language_code`.
2. Traduzca cada fragmento devuelto en el agente host.
3. Llame a `finish_notebook_agent_translation` con el `job` original y los fragmentos traducidos.
4. Llame a `rewrite_notebook_paths` si los enlaces del cuaderno traducido necesitan ajuste de ruta de destino.

Las herramientas asistidas por agente no llaman a Azure OpenAI ni a OpenAI desde Co-op Translator. El agente host es responsable de traducir los fragmentos devueltos. Co-op Translator maneja el fraccionamiento de Markdown, la preservación de marcadores de posición, la reconstrucción del frontmatter, el reemplazo de celdas del cuaderno y la normalización posterior a la traducción.

### Traducir un repositorio completo

Use `run_translation` cuando el usuario quiera que Co-op Translator se comporte como la CLI `translate`.

La traducción de repositorios por defecto es `dry_run=true` para que un agente pueda inspeccionar el alcance antes de los cambios en archivos:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Para permitir escrituras, el llamador debe establecer tanto `dry_run=false` como `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` se expone como un alias de compatibilidad para `run_translation`.

### Revisar la salida traducida

Use `run_review` para comprobaciones deterministas que no requieren credenciales LLM o Vision:

!!! note "Beta"
    MCP exposes the beta `run_review` API. It is safe for read-only review workflows, but review checks and issue schemas may evolve.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

El resultado incluye la salida de texto capturada y un resumen estructurado de la revisión cuando está disponible.

## Ejecuciones manuales del servidor

Las ejecuciones manuales son principalmente para depuración o para transportes que se comportan como servidores de larga duración.

Depure el servidor stdio predeterminado:

```bash
co-op-translator-mcp
```

Ejecute desde una copia del código fuente:

```bash
python -m co_op_translator.mcp.server
```

Ejecute un servidor HTTP o SSE de larga duración:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Para integraciones locales con editores y agentes, prefiera la configuración `stdio` gestionada por el cliente en el Paso 2.

## Herramientas

| Herramienta | Propósito | Escribe archivos |
| --- | --- | --- |
| `translate_markdown_content` | Translate a Markdown string. | No |
| `translate_notebook_content` | Translate Markdown cells in notebook JSON. | No |
| `translate_image_content` | Translate text in one image and return base64 image data. | Optional, only when `output_path` is provided |
| `start_markdown_agent_translation` | Prepare Markdown chunks for the host agent to translate without Co-op Translator LLM credentials. | No |
| `finish_markdown_agent_translation` | Reconstruct Markdown from host-agent translated chunks. | No |
| `start_notebook_agent_translation` | Prepare notebook Markdown-cell chunks for the host agent to translate. | No |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON from host-agent translated chunks. | No |
| `rewrite_markdown_paths` | Rewrite Markdown body and frontmatter paths for a translated target. | No |
| `rewrite_notebook_paths` | Rewrite paths inside notebook Markdown cells. | No |
| `run_translation` | Run project-level translation like the CLI. | Yes when `dry_run=false` and `confirm_write=true` |
| `translate_project` | Compatibility alias for `run_translation`. | Yes when `dry_run=false` and `confirm_write=true` |
| `run_review` | Run deterministic review checks. | No |
| `get_configuration_status` | Report configured LLM and Vision providers without exposing secrets. | No |
| `list_supported_languages` | List supported target language codes. | No |
| `get_api_overview` | Describe available MCP workflows and tools. | No |

## Recursos

| Resource URI | Propósito |
| --- | --- |
| `co-op://api` | JSON overview of workflows and tools. |
| `co-op://supported-languages` | JSON list of supported language codes. |
| `co-op://configuration` | JSON provider availability summary without secrets. |

## Prompts

| Prompt | Propósito |
| --- | --- |
| `translate_markdown_document_prompt` | Guide an MCP client through content translation plus optional path rewriting. |
| `agent_assisted_markdown_translation_prompt` | Guide an MCP client through host-agent Markdown translation without Co-op Translator LLM provider credentials. |
| `translate_repository_prompt` | Guide an MCP client through dry-run-first repository translation. |

## Ejemplos para copiar y pegar

Translate Markdown content:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Rewrite translated Markdown links:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Translate Markdown with the host agent model:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

After the host agent translates each returned chunk, finish the job with the complete `job` object returned by `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Preview repository translation:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Solución de problemas

| Problema | Qué intentar |
| --- | --- |
| The MCP client cannot find `co-op-translator-mcp`. | Use the absolute Python executable path and `["-m", "co_op_translator.mcp.server"]` source checkout configuration. |
| The server is listed but translation fails. | Call `get_configuration_status` and confirm an LLM provider is available. |
| You want Markdown or notebook translation without Azure OpenAI/OpenAI keys. | Use `start_markdown_agent_translation` / `finish_markdown_agent_translation` or the notebook equivalents so the host agent translates the chunks. |
| Image translation fails. | Confirm Azure AI Vision variables are set and call `get_configuration_status`. |
| Repository translation does not write files. | Set `dry_run=false` and `confirm_write=true` only after explicit user approval. |
| Changes to client config do not appear. | Restart or reload the MCP client. |

## Notas de seguridad

- Las llamadas a herramientas MCP están controladas por el modelo de la aplicación host, por lo que la traducción de repositorios es por defecto una ejecución de prueba.
- La traducción completa de repositorios puede crear, actualizar o eliminar muchos archivos. Requiera la aprobación explícita del usuario antes de establecer `confirm_write=true`.
- La herramienta de estado de configuración nunca devuelve claves API, endpoints u otros valores secretos.
- La traducción de imágenes devuelve datos de imagen en base64. Las imágenes grandes pueden producir respuestas de herramienta de gran tamaño.
- Las herramientas asistidas por agente devuelven fragmentos de origen y prompts al host MCP. Úselas solo con contenido que el usuario esté cómodo enviando a ese modelo de agente host.