# Guía del mantenedor

Esta página resume cómo se conectan la API, la CLI y el sitio de documentación.

## Límite de la API pública

La API estable de Python se exporta desde:

```python
co_op_translator.api
```

La API pública está organizada en ayudantes de traducción de contenido, ayudantes de reescritura de rutas, orquestación de proyectos y revisión:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` es el límite de persistencia para integraciones alojadas.
Debe mantener los candidatos generados separados de las líneas base aceptadas para que un
una traducción no fusionada se convierta en la fuente de la verdad.

Al agregar nuevas API públicas, actualice:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- pruebas de API relevantes bajo `tests/co_op_translator/`, como `test_api.py` o `test_review_api.py`

Evite documentar los módulos de bajo nivel `core` como API estable a menos que el proyecto pretenda soportarlos directamente.

## Puntos de entrada de la CLI

El paquete define estos scripts de Poetry:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` despacha según el nombre del script:

- `translate` llama a `co_op_translator.cli.translate.translate_command`
- `evaluate` llama a `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` llama a `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` llama a `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` omite `__main__.py` y llama directamente a `co_op_translator.mcp.server:main`.

Al agregar o cambiar opciones de la CLI, actualice:

- el comando relevante `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- Pruebas relacionadas con la CLI, si cambia el comportamiento

## Servidor MCP

El servidor MCP está implementado en:

```python
co_op_translator.mcp.server
```

El servidor envuelve intencionadamente la API pública de Python en lugar de llamar a los módulos de bajo nivel `core`. Mantenga esta separación intacta para que los clientes MCP, los llamadores de Python y la CLI compartan el mismo comportamiento.

Al agregar o cambiar herramientas MCP, actualice:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` si la superficie de la API pública cambia

Las herramientas de traducción del repositorio son invocables a través de MCP y pueden escribir muchos archivos. Mantenga `dry_run=True` como valor predeterminado y requiera `confirm_write=True` antes de una traducción de proyecto que no sea de prueba.

## Flujo de traducción

El flujo de traducción del proyecto a alto nivel es:

1. Analizar argumentos de la CLI o parámetros de la API.
2. Validar la configuración de LLM con `LLMConfig`.
3. Validar Azure AI Vision cuando se seleccione la traducción de imágenes.
4. Normalizar códigos de idioma.
5. Detectar alias de carpetas de idioma heredadas.
6. Estimar el volumen de traducción.
7. Actualizar las secciones de idioma/curso del README cuando corresponda.
8. Delegar la traducción del proyecto a `ProjectTranslator`.
9. `ProjectTranslator` delega el procesamiento de archivos a `TranslationManager`.

`TranslationManager` se compone de mixins enfocados por tipo de archivo:

- `ProjectMarkdownTranslationMixin` gestiona la lectura de archivos Markdown, la traducción de contenido, la reescritura de rutas, metadatos, descargos de responsabilidad y la escritura de archivos.
- `ProjectNotebookTranslationMixin` gestiona la lectura de archivos de notebook, la traducción de celdas Markdown, la reescritura de rutas, metadatos, descargos de responsabilidad y la escritura de archivos.
- `ProjectImageTranslationMixin` gestiona el descubrimiento de imágenes, la extracción/traducción de texto, la escritura de imágenes renderizadas y metadatos.

Las API de contenido de nivel inferior omiten el flujo de trabajo del proyecto:

1. `translate_markdown_content` y `translate_notebook_content` traducen contenido en memoria únicamente.
2. `translate_image_content` traduce texto en una sola imagen y devuelve un objeto de imagen renderizada.
3. `rewrite_markdown_paths` y `rewrite_notebook_paths` son ayudantes explícitos de postprocesamiento. No realizan traducción ni escrituras en el proyecto.

## Flujo de revisión

El flujo de revisión determinista es:

1. Analizar argumentos de la CLI o parámetros de la API.
2. Normalizar los códigos de idioma solicitados.
3. Construir uno o más objetivos de revisión a partir de `root_dir`, `root_dirs` o `groups`.
4. Opcionalmente limitar los archivos de origen con `--changed-from`.
5. Ejecutar comprobaciones deterministas para estructura, frescura de la traducción, integridad de Markdown y rutas locales de enlaces/imágenes.
6. Imprimir ya sea salida de texto o Markdown con formato GitHub.
7. Salir con error cuando se encuentren errores de revisión.

El flujo de revisión no requiere claves de API y está disponible para comprobaciones locales o CI de consumidor opt-in. Este repositorio no ejecuta `co-op-review` automáticamente en cada pull request.

## Sitio de documentación

El sitio de documentación se configura mediante:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

El directorio `docs/` es la fuente canónica de documentación. No añada nuevas guías para usuarios finales fuera de este directorio a menos que el proyecto introduzca intencionalmente otra superficie de documentación publicada.

Construir localmente:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Previsualizar localmente:

```bash
python -m mkdocs serve
```

El sitio generado se escribe en `site/`, que está ignorado por git.

## Flujo de trabajo de GitHub Pages

`.github/workflows/docs.yml` construye el sitio en pull requests y lo despliega en pushes a `main`.

El flujo de trabajo instala:

```bash
pip install -r requirements-docs.txt
```

El flujo de trabajo de la documentación instala solo la cadena de herramientas de documentación. `mkdocs.yml` apunta `mkdocstrings` a `src/` para que las páginas de la API pública puedan renderizarse desde el árbol de origen sin instalar el conjunto completo de dependencias de tiempo de ejecución. Si la documentación futura de la API requiere importar proveedores de tiempo de ejecución opcionales durante la compilación, actualice tanto `.github/workflows/docs.yml` como esta guía en conjunto.

## Estándar de calidad de la documentación

Antes de fusionar cambios en la documentación, ejecute:

```bash
python -m mkdocs build --strict
git diff --check
```

Utilice compilaciones estrictas para que los enlaces rotos, las entradas de navegación inválidas y los problemas de renderizado de la API se detecten temprano.