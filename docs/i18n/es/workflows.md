# Elige tu flujo de trabajo

Co-op Translator se puede usar de tres maneras: la CLI, la API de Python y el servidor MCP. Comparten las mismas capacidades de traducción, pero cada una se adapta a un flujo de trabajo diferente.

Usa esta página cuando estés decidiendo por dónde empezar.

## Decisión rápida

| Si quieres... | Usar | Empieza aquí |
| --- | --- | --- |
| Traducir o revisar un repositorio desde un terminal | CLI | [Referencia del CLI](cli.md) |
| Agregar traducción a un script de Python, servicio, notebook o trabajo de CI | API de Python | [API de Python](api.md) |
| Permitir que un agente, editor o cliente compatible con MCP traduzca contenido por ti | Servidor MCP | [Servidor MCP](mcp.md) |
| Traducir un documento Markdown, notebook o imagen que tu aplicación ya cargó | API de Python o Servidor MCP | [API de Python](api.md) o [Servidor MCP](mcp.md) |
| Traducir un repositorio entero con carpetas de salida estándar y metadatos | CLI o `run_translation` | [Referencia del CLI](cli.md) o [API de Python](api.md) |

## Usa la CLI cuando

Elige la CLI cuando una persona o un trabajo de CI esté realizando la traducción del repositorio desde un shell.

La CLI es la vía más directa cuando quieres que Co-op Translator descubra los archivos del proyecto, cree salidas traducidas, preserve la estructura del proyecto, actualice metadatos y ejecute comandos de revisión.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Apropiado para:

- Estás traduciendo un repositorio desde tu terminal.
- Quieres un comando repetible para flujos de trabajo de CI o de publicación.
- Quieres descubrimiento de proyectos integrado, rutas de salida, metadatos, limpieza y revisión.
- Prefieres una interfaz de comandos en lugar de escribir código Python.

## Usa la API de Python cuando

Elige la API de Python cuando tu propio código deba controlar el flujo de trabajo.

La API es útil para aplicaciones, scripts de automatización, notebooks, servicios y canalizaciones personalizadas. Te permite llamar a APIs de traducción de contenido de bajo nivel para archivos individuales o ejecutar la misma orquestación a nivel de repositorio que usa la CLI.

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

Ejecuta la traducción de un repositorio desde Python:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Apropiado para:

- Tu aplicación ya lee archivos, buffers, notebooks o bytes de imágenes.
- Necesitas validación personalizada, almacenamiento, registro, reintentos o flujos de aprobación.
- Quieres traducir un solo documento, notebook o imagen sin procesar todo un repositorio.
- Quieres traducción de repositorios, pero desde automatización en Python en lugar de un comando de shell.

## Usa el servidor MCP cuando

Elige el servidor MCP cuando un agente, editor o cliente compatible con MCP deba llamar a las herramientas de Co-op Translator.

En la configuración local habitual, el usuario no mantiene manualmente un servidor en ejecución. El cliente MCP inicia `co-op-translator-mcp` sobre `stdio` cuando necesita las herramientas.

Ejemplos de solicitudes de usuario que un agente podría manejar:

- "Traduce este archivo Markdown al coreano y conserva los enlaces correctos."
- "Traduce este archivo Markdown al coreano con el flujo de trabajo MCP asistido por agente, usando tu propio modelo para los fragmentos traducidos."
- "Traduce este notebook al coreano, preserva las celdas de código y usa Co-op Translator MCP para reconstruir el notebook."
- "Traduce el texto en esta imagen al japonés y guarda el resultado."
- "Realiza una ejecución simulada de una traducción de repositorio al español y dime qué cambiaría."
- "Revisa si la salida de la traducción al coreano está actualizada."

Para Markdown y notebooks, MCP puede funcionar en dos modos:

| Modo | Úsalo cuando | Herramientas principales |
| --- | --- | --- |
| Asistido por agente | El agente host de MCP debe traducir fragmentos con su propio modelo, sin credenciales del proveedor LLM de Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Respaldado por proveedor | Co-op Translator debe llamar a Azure OpenAI u OpenAI directamente. | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown tool call shape:

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

MCP image tool call shape:

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

La traducción de repositorios se ejecuta por defecto como dry-run a través de MCP:

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

Apropiado para:

- Quieres flujos de trabajo de traducción en lenguaje natural dentro de un agente o editor.
- Quieres traducción de Markdown o notebooks donde el modelo del agente host traduce fragmentos preparados.
- Quieres que el agente traduzca contenido seleccionado en lugar de un repositorio entero.
- Quieres un paso de aprobación antes de las escrituras en todo el repositorio.
- Quieres una única interfaz que exponga herramientas para Markdown, notebooks, imágenes, revisión y reescritura de rutas.

## Cómo encajan

La CLI es la mejor opción por defecto para personas que traducen repositorios. La API de Python es mejor cuando tu código es el responsable del flujo de trabajo. El servidor MCP es mejor cuando un agente o editor es el responsable del flujo de trabajo.

Las tres vías usan la misma API pública de Co-op Translator, por lo que puedes empezar con la CLI, automatizar con Python después y exponer las mismas capacidades a clientes MCP cuando necesites flujos de trabajo impulsados por agentes.