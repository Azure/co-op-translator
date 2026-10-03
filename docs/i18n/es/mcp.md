# Servidor MCP

Co-op Translator incluye un servidor Model Context Protocol para agentes, editores y clientes compatibles con MCP.

En la configuración local predeterminada, los usuarios no mantienen un servidor separado ejecutándose manualmente. Configuran su cliente MCP, y el cliente inicia `co-op-translator-mcp` automáticamente por `stdio` cuando necesita las herramientas de Co-op Translator.

Si decides entre CLI, Python API y MCP, comienza con [Elige tu flujo de trabajo](workflows.md).

Usa MCP cuando un agente o editor deba llamar a Co-op Translator directamente:

| Objetivo del usuario | Herramientas MCP |
| --- | --- |
| Traducir un documento Markdown, cuaderno o imagen | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Traducir contenido Markdown o de cuaderno con el modelo agente anfitrión | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Reescribir enlaces traducidos de Markdown o cuaderno después de elegir la ruta de salida | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Traducir un repositorio completo como el CLI | `run_translation`, `translate_project` |
| Revisar la salida traducida sin credenciales de LLM | `run_review` |
| Inspeccionar capacidades y estado del entorno | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

El servidor MCP envuelve la misma API pública de Python documentada en [API de Python](api.md). Las herramientas respaldadas por proveedores usan los mismos proveedores configurados que el CLI y la API de Python. Las herramientas asistidas por agentes preparan fragmentos para que el agente anfitrión MCP los traduzca, y luego usan Co-op Translator para reconstruir el Markdown o el cuaderno final.

## Paso 1: Instalar y configurar Co-op Translator

Instala Co-op Translator en el entorno de Python que usará tu cliente MCP:

```bash
pip install co-op-translator
```

Para desarrollo local desde este repositorio, instala el paquete en modo editable:

```bash
pip install -e .
```

Elige el modo de traducción que usará tu cliente MCP:

| Modo | Úsalo para | Credenciales |
| --- | --- | --- |
| Respaldado por proveedor | Co-op Translator llama a `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, o `run_translation`. | La traducción requiere Azure OpenAI, OpenAI o Anthropic. La traducción de imágenes también requiere Azure AI Vision. |
| Asistido por agente | El agente anfitrión MCP traduce fragmentos devueltos por `start_markdown_agent_translation` o `start_notebook_agent_translation`. | No se requieren credenciales de proveedor LLM de Co-op Translator para fragmentos de Markdown o cuadernos. La traducción de imágenes aún no está cubierta por el modo asistido por agente. |

Si estás empezando con la traducción de Markdown o cuadernos dentro de un agente como Codex o Claude Code, comienza con el modo asistido por agente. Usa el modo respaldado por proveedor cuando quieras que Co-op Translator llame a tus proveedores configurados, cuando estés traduciendo imágenes, o cuando ejecutes traducción a nivel de repositorio como el CLI.

Configura un proveedor para los flujos de trabajo respaldados por proveedor:

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

La traducción de imágenes respaldada por proveedor además necesita:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    El modo asistido por agente actualmente cubre Markdown y las celdas Markdown de cuadernos. La traducción de imágenes todavía utiliza la canalización de imágenes respaldada por proveedores y requiere Azure AI Vision para OCR y representación con conciencia del diseño.

## Paso 2: Configurar tu cliente MCP

Para la configuración local normal por `stdio`, añade Co-op Translator a la configuración de tu cliente MCP. El cliente iniciará y detendrá el proceso automáticamente.

Configuración para paquete instalado:

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

Configuración para checkout de código fuente en Windows:

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

Configuración para checkout de código fuente en macOS o Linux:

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

Después de cambiar la configuración del cliente MCP, reinicia o recarga el cliente para que pueda descubrir el nuevo servidor.

## Paso 3: Verificar el servidor en el cliente

Pide al cliente MCP que liste las herramientas disponibles, o llama primero a uno de los auxiliares de solo lectura:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Comprobaciones útiles iniciales:

| Herramienta | Qué comprobar |
| --- | --- |
| `get_api_overview` | Confirma que el servidor sea accesible y muestra los flujos de trabajo disponibles. |
| `list_supported_languages` | Confirma que se puedan cargar los datos de idiomas empaquetados. |
| `get_configuration_status` | Confirma la disponibilidad de proveedores LLM y Vision sin exponer valores secretos. |

## Paso 4: Elegir un flujo de trabajo

### Traducir archivos o documentos individuales

Usa las herramientas de contenido respaldadas por proveedor cuando el cliente MCP ya tenga el contenido del documento o la ruta de una imagen y Co-op Translator deba llamar a los proveedores de traducción configurados.

Para Markdown:

1. Llama a `translate_markdown_content` con `document`, `language_code`, y opcionalmente `source_path`.
2. Si el resultado traducido se escribirá en un diseño de salida de Co-op Translator, llama a `rewrite_markdown_paths`.
3. Deja que el cliente escriba o devuelva el `content` final.

Para cuadernos:

1. Llama a `translate_notebook_content` con el JSON del cuaderno y `language_code`.
2. Llama a `rewrite_notebook_paths` si los enlaces del cuaderno traducido necesitan ajustarse a una ruta de destino.
3. Escribe o devuelve el JSON final del cuaderno.

Para imágenes:

1. Llama a `translate_image_content` con `image_path`, `language_code`, y opcionalmente `root_dir` o `fast_mode`.
2. Lee el `data_base64` y el `mime_type` devueltos.
3. Si se proporciona `output_path`, la imagen traducida también se guarda en esa ruta.

Las herramientas de contenido no realizan descubrimiento de proyecto, actualizaciones de metadatos, avisos ni reescritura automática de rutas. Si deseas que el agente anfitrión traduzca fragmentos de Markdown o de cuaderno sin credenciales de proveedor LLM de Co-op Translator, usa el flujo de trabajo asistido por agente a continuación.

### Traducir con el modelo agente anfitrión

Usa las herramientas asistidas por agente cuando quieras que el agente anfitrión MCP, como un asistente de codificación, produzca el texto traducido en lugar de configurar un proveedor LLM para Co-op Translator.

En un cliente MCP basado en chat, normalmente no necesitas escribir el JSON de la herramienta tú mismo. Pide al agente que use el flujo de trabajo asistido por agente:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Para cuadernos, usa el mismo patrón:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Si tu cliente MCP admite prompts de servidor, usa `agent_assisted_markdown_translation_prompt` para que el cliente cargue las mismas instrucciones del flujo de trabajo.

Para Markdown:

1. Llama a `start_markdown_agent_translation` con `document`, `language_code`, y opcionalmente `source_path`.
2. Traduce cada fragmento devuelto en el agente anfitrión siguiendo el `prompt` del fragmento.
3. Llama a `finish_markdown_agent_translation` con el `job` original y los fragmentos traducidos usando `chunk_id` y `translated_text`.
4. Si el contenido se escribirá en una ruta de destino traducida, llama a `rewrite_markdown_paths`.

Para cuadernos:

1. Llama a `start_notebook_agent_translation` con el JSON del cuaderno y `language_code`.
2. Traduce cada fragmento devuelto en el agente anfitrión.
3. Llama a `finish_notebook_agent_translation` con el `job` original y los fragmentos traducidos.
4. Llama a `rewrite_notebook_paths` si los enlaces del cuaderno traducido necesitan ajuste de ruta de destino.

Las herramientas asistidas por agente no llaman al proveedor LLM configurado desde Co-op Translator. El agente anfitrión es responsable de traducir los fragmentos devueltos. Co-op Translator maneja el fragmentado de Markdown, la preservación de marcadores de posición, la reconstrucción del frontmatter, la sustitución de celdas de cuaderno y la normalización posterior a la traducción.

### Traducir un repositorio completo

Usa `run_translation` cuando el usuario quiera que Co-op Translator se comporte como el CLI `translate`.

La traducción de repositorios tiene por defecto `dry_run=true` para que un agente pueda inspeccionar el alcance antes de los cambios en archivos:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

El resultado de `run_translation` incluye un arreglo `events` con eventos versionados
`co-op.translation.event.v1` de progreso. Los clientes MCP deben usar campos tales
como `type`, `stage_key`, `completed`, `total` y `current_path` en lugar de
analizar el texto capturado de la consola. Pasa `json_events_path` para escribir también esos eventos
en un archivo NDJSON.

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

Usa `run_review` para comprobaciones determinísticas que no requieren credenciales LLM o Vision:

!!! note "Beta"
    MCP expone la API beta `run_review`. Es segura para flujos de trabajo de revisión de solo lectura, pero las comprobaciones de revisión y los esquemas de problemas pueden evolucionar.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

El resultado incluye la salida de texto capturada y un resumen de revisión estructurado cuando está disponible.

## Ejecuciones manuales del servidor

Las ejecuciones manuales son principalmente para depuración o para transportes que se comportan como servidores de larga duración.

Depura el servidor stdio predeterminado:

```bash
co-op-translator-mcp
```

Ejecuta desde un checkout de código fuente:

```bash
python -m co_op_translator.mcp.server
```

Ejecuta un servidor HTTP o SSE de larga duración:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Para integraciones locales con editores y agentes, prefiere la configuración `stdio` gestionada por el cliente en el Paso 2.

## Herramientas

| Herramienta | Propósito | Escribe archivos |
| --- | --- | --- |
| `translate_markdown_content` | Traducir una cadena Markdown. | No |
| `translate_notebook_content` | Traducir celdas Markdown en el JSON del cuaderno. | No |
| `translate_image_content` | Traducir texto en una imagen y devolver datos de imagen en base64. | Opcional, solo cuando se proporciona `output_path` |
| `start_markdown_agent_translation` | Preparar fragmentos de Markdown para que el agente anfitrión los traduzca sin credenciales LLM de Co-op Translator. | No |
| `finish_markdown_agent_translation` | Reconstruir Markdown a partir de fragmentos traducidos por el agente anfitrión. | No |
| `start_notebook_agent_translation` | Preparar fragmentos de celdas Markdown de cuaderno para que el agente anfitrión los traduzca. | No |
| `finish_notebook_agent_translation` | Reconstruir el JSON del cuaderno a partir de fragmentos traducidos por el agente anfitrión. | No |
| `rewrite_markdown_paths` | Reescribir el cuerpo Markdown y las rutas del frontmatter para un destino traducido. | No |
| `rewrite_notebook_paths` | Reescribir rutas dentro de las celdas Markdown del cuaderno. | No |
| `run_translation` | Ejecutar la traducción a nivel de proyecto como el CLI. | Sí cuando `dry_run=false` y `confirm_write=true` |
| `translate_project` | Alias de compatibilidad para `run_translation`. | Sí cuando `dry_run=false` y `confirm_write=true` |
| `run_review` | Ejecutar comprobaciones de revisión determinísticas. | No |
| `get_configuration_status` | Informar sobre los proveedores LLM y Vision configurados sin exponer secretos. | No |
| `list_supported_languages` | Listar códigos de idioma objetivo soportados. | No |
| `get_api_overview` | Describir los flujos de trabajo y herramientas MCP disponibles. | No |

## Recursos

| URI del recurso | Propósito |
| --- | --- |
| `co-op://api` | Resumen JSON de flujos de trabajo y herramientas. |
| `co-op://supported-languages` | Lista JSON de códigos de idiomas soportados. |
| `co-op://configuration` | Resumen JSON de disponibilidad de proveedores sin secretos. |

## Indicaciones

| Prompt | Propósito |
| --- | --- |
| `translate_markdown_document_prompt` | Guiar a un cliente MCP a través de la traducción de contenido más la reescritura opcional de rutas. |
| `agent_assisted_markdown_translation_prompt` | Guiar a un cliente MCP a través de la traducción de Markdown por el agente anfitrión sin credenciales de proveedor LLM de Co-op Translator. |
| `translate_repository_prompt` | Guiar a un cliente MCP a través de la traducción de repositorios empezando por un dry-run. |

## Ejemplos para copiar y pegar

Traducir contenido Markdown:

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

Reescribir enlaces Markdown traducidos:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

Traducir Markdown con el modelo agente anfitrión:

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

Después de que el agente anfitrión traduzca cada fragmento devuelto, finaliza el trabajo con el objeto `job` completo devuelto por `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Vista previa de la traducción del repositorio:

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

| Problema | Qué probar |
| --- | --- |
| El cliente MCP no puede encontrar `co-op-translator-mcp`. | Usa la ruta absoluta del ejecutable de Python y la configuración de checkout de código fuente `["-m", "co_op_translator.mcp.server"]`. |
| El servidor aparece en la lista pero la traducción falla. | Llama a `get_configuration_status` y confirma que haya un proveedor LLM disponible. |
| Deseas traducción de Markdown o de cuaderno sin credenciales de proveedor. | Usa `start_markdown_agent_translation` / `finish_markdown_agent_translation` o los equivalentes para cuadernos para que el agente anfitrión traduzca los fragmentos. |
| La traducción de imágenes falla. | Confirma que las variables de Azure AI Vision estén configuradas y llama a `get_configuration_status`. |
| La traducción del repositorio no escribe archivos. | Establece `dry_run=false` y `confirm_write=true` solo después de la aprobación explícita del usuario. |
| Los cambios en la configuración del cliente no aparecen. | Reinicia o recarga el cliente MCP. |

## Notas de seguridad

- Las llamadas a herramientas MCP están controladas por el modelo de la aplicación anfitriona, por lo que la traducción de repositorios es dry-run por defecto.
- La traducción completa del repositorio puede crear, actualizar o eliminar muchos archivos. Requiere aprobación explícita del usuario antes de establecer `confirm_write=true`.
- La herramienta de estado de configuración nunca devuelve claves API, endpoints u otros valores secretos.
- La traducción de imágenes devuelve datos de imagen en base64. Las imágenes grandes pueden producir respuestas de herramienta de gran tamaño.
- Las herramientas asistidas por agente devuelven fragmentos de origen y prompts al anfitrión MCP. Úsalas solo con contenido que el usuario esté cómodo enviando a ese modelo de agente anfitrión.