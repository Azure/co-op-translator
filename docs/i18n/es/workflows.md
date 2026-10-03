# Elija su flujo de trabajo

Co-op Translator se puede usar de tres maneras: la CLI, la API de Python y el servidor MCP. Comparten las mismas capacidades de traducción, pero cada una se adapta a un flujo de trabajo diferente.

Utilice esta página cuando decida por dónde empezar.

**Si edita traducciones manualmente:** los flujos de trabajo predeterminados de CLI y Actions vuelven a traducir por completo los archivos fuente modificados, por lo que su redacción en esos archivos puede sobrescribirse. Revise el diff antes de aceptar una actualización. Para la preservación a nivel de bloque de Markdown de las ediciones aceptadas, utilice el opcional [proveedor de estado de traducción de la API de Python](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Decisión rápida

| Si desea... | Usar | Comience aquí |
| --- | --- | --- |
| Traducir o revisar un repositorio desde un terminal | CLI | [Referencia de la CLI](cli.md) |
| Agregar traducción a un script de Python, servicio, notebook o tarea de CI | Python API | [API de Python](api.md) |
| Permitir que un agente, editor o cliente compatible con MCP traduzca contenido por usted | MCP Server | [Servidor MCP](mcp.md) |
| Traducir un documento Markdown, notebook o imagen que su aplicación ya haya cargado | Python API or MCP Server | [API de Python](api.md) or [Servidor MCP](mcp.md) |
| Traducir un repositorio completo con carpetas de salida y metadatos estándar | CLI or `run_translation` | [Referencia de la CLI](cli.md) or [API de Python](api.md) |

## Utilice la CLI cuando

Elija la CLI cuando una persona o un trabajo de CI esté ejecutando la traducción del repositorio desde una terminal.

La CLI es la vía más directa cuando desea que Co-op Translator descubra archivos del proyecto, cree salidas traducidas, preserve la estructura del proyecto, actualice metadatos y ejecute comandos de revisión.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Este ejemplo traduce Markdown y notebooks. Agregue `-img` solo después de configurar [Azure AI Vision](configuration.md#azure-ai-vision). Para una primera ejecución únicamente con Markdown, siga [Su primera traducción](first-translation.md).

Encaja bien en:

- Está traduciendo un repositorio desde su terminal.
- Desea un comando repetible para flujos de trabajo de CI o de publicación.
- Desea descubrimiento de proyecto incorporado, rutas de salida, metadatos, limpieza y revisión.
- Prefiere una interfaz por comandos en lugar de escribir código Python.

## Utilice la API de Python cuando

Elija la API de Python cuando su propio código deba controlar el flujo de trabajo.

La API es útil para aplicaciones, scripts de automatización, notebooks, servicios y canalizaciones personalizadas. Le permite llamar a APIs de traducción de contenido de bajo nivel para archivos individuales o ejecutar la misma orquestación a nivel de repositorio que usa la CLI.

Traduce un documento Markdown y decide dónde guardarlo:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Ejecute la traducción de un repositorio desde Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Encaja bien:

- Su aplicación ya lee archivos, buffers, notebooks o bytes de imagen.
- Necesita validación personalizada, almacenamiento, registros, reintentos o flujos de aprobación.
- Desea traducir un documento, notebook o imagen sin procesar todo un repositorio.
- Desea la traducción de repositorios, pero mediante automatización en Python en lugar de un comando de shell.

## Utilice el servidor MCP cuando

Elija el servidor MCP cuando un agente, editor o cliente compatible con MCP deba llamar a las herramientas de Co-op Translator.

En la configuración local normal, el usuario no mantiene manualmente el servidor en ejecución. El cliente MCP inicia `co-op-translator-mcp` sobre `stdio` cuando necesita las herramientas.

Ejemplos de solicitudes de usuario que un agente podría manejar:

- "Traduce este archivo Markdown al coreano y mantén los enlaces correctos."
- "Traduce este archivo Markdown al coreano con el flujo de trabajo MCP asistido por agente, usando tu propio modelo para los fragmentos traducidos."
- "Traduce este notebook al coreano, preserva las celdas de código y usa Co-op Translator MCP para reconstruir el notebook."
- "Traduce el texto de esta imagen al japonés y guarda el resultado."
- "Simula una traducción de repositorio a español y dime qué cambiaría."
- "Revisa si la salida de la traducción al coreano está actualizada."

Para Markdown y notebooks, MCP puede funcionar en dos modos:

| Modo | Usar cuando | Herramientas principales |
| --- | --- | --- |
| Asistido por agente | El agente host de MCP debería traducir los fragmentos con su propio modelo, sin credenciales de proveedor LLM de Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Respaldado por proveedor | Co-op Translator debería llamar directamente a Azure OpenAI, OpenAI o Anthropic. | `translate_markdown_content`, `translate_notebook_content` |

Formato de llamada de la herramienta Markdown respaldada por proveedor de MCP:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

Formato de llamada de la herramienta de imagen de MCP:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

La traducción del repositorio se ejecuta en modo simulación (dry-run) por defecto a través de MCP:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Encaja bien:

- Desea flujos de trabajo de traducción en lenguaje natural dentro de un agente o editor.
- Desea traducción de Markdown o notebooks donde el modelo del agente host traduzca fragmentos preparados.
- Desea que el agente traduzca contenido seleccionado en lugar de todo un repositorio.
- Desea un paso de aprobación antes de escrituras en todo el repositorio.
- Desea una interfaz que exponga herramientas para Markdown, notebooks, imágenes, revisión y reescritura de rutas.

## Cómo encajan entre sí

La CLI es la mejor opción predeterminada para las personas que traducen repositorios. La API de Python es mejor cuando su código controla el flujo de trabajo. El servidor MCP es mejor cuando un agente o editor controla el flujo de trabajo.

Las tres vías usan la misma API pública de Co-op Translator, por lo que puede empezar con la CLI, automatizar con Python más adelante y exponer las mismas capacidades a los clientes MCP cuando necesite flujos de trabajo dirigidos por agentes.