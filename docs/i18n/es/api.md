# API de Python

La API pública estable de Python se exporta desde `co_op_translator.api`. La mayoría de las integraciones usan uno de estos flujos de trabajo:

| Escenario | Úsalo cuando | APIs principales |
| --- | --- | --- |
| Traducir archivos o documentos individuales | Tu aplicación lee el contenido fuente, llama a Co-op Translator para la traducción y decide dónde guardar el resultado. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Preparar contenido para la traducción por el agente anfitrión | Tu host MCP o el modelo de la aplicación traducirá los fragmentos, mientras que Co-op Translator se encarga del fragmentado y la reconstrucción. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Traducir un repositorio completo | Quieres que la API de Python se comporte como la CLI y gestione el descubrimiento, rutas de salida, metadatos, limpieza y escrituras. | `run_translation` |

La mayoría de los módulos de bajo nivel bajo `core`, `config`, `review` y `utils` son detalles de implementación utilizados por estos puntos de entrada de la API.

Los clientes MCP usan la misma API pública a través del [Servidor MCP](mcp.md). Usa esta página cuando llames a Python directamente, y la guía MCP cuando expongas Co-op Translator a un agente o editor. Si estás decidiendo entre CLI, API de Python y MCP, comienza con [Elige tu flujo de trabajo](workflows.md).

## Flujo inicial de la API

Comienza aquí si llamas a Co-op Translator desde código Python:

1. Configure un proveedor de LLM como se describe en [Configuración](configuration.md), a menos que solo esté preparando fragmentos de Markdown o notebook para la traducción por el agente anfitrión.
2. Decide si tu aplicación se encarga de la E/S de archivos.
3. Usa las APIs de contenido cuando tu aplicación lea y escriba archivos individuales.
4. Usa `run_translation` cuando Co-op Translator deba procesar un repositorio como la CLI.
5. Usa `run_review` después de la traducción si necesitas verificaciones deterministas en la automatización.

| Objetivo | API con la que empezar |
| --- | --- |
| Traducir una cadena o archivo Markdown | `translate_markdown_content` |
| Traducir una carga útil de notebook | `translate_notebook_content` |
| Traducir una imagen | `translate_image_content` |
| Permitir que un agente anfitrión traduzca fragmentos de Markdown o notebook | `start_markdown_agent_translation` o `start_notebook_agent_translation` |
| Reescribir enlaces traducidos después de elegir una ruta de salida | `rewrite_markdown_paths` o `rewrite_notebook_paths` |
| Traducir un repositorio completo | `run_translation` |
| Revisar la salida traducida | `run_review` |

## Escenario 1: Traducir archivos o documentos individuales

Usa este flujo de trabajo cuando ya tengas un archivo, un búfer del editor, una carga útil de notebook, una solicitud MCP o una entrada de canalización personalizada. Tu código se encarga de la E/S de archivos:

1. Lee el contenido fuente.
2. Llama a una API de traducción de contenido.
3. Opcionalmente llama a una API de reescritura de rutas si el contenido traducido se va a escribir en una carpeta de traducción del proyecto.
4. Guarda o devuelve el resultado desde tu aplicación.

Las APIs de traducción de contenido no ejecutan el descubrimiento del proyecto, no escriben metadatos, no añaden descargos de responsabilidad y no reescriben enlaces automáticamente.

### Archivo Markdown

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


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
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Si el Markdown traducido no formará parte de la estructura de un proyecto de Co-op Translator, omite `rewrite_markdown_paths` y guarda la cadena traducida directamente.

### Archivo de notebook

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` traduce celdas Markdown y preserva las celdas no Markdown. La reescritura de rutas se aplica solo a las celdas Markdown.

### Archivo de imagen

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` lee la imagen fuente y devuelve una `PIL.Image.Image` renderizada. No escribe metadatos de la imagen traducida.

## Escenario 2: Traducir un repositorio completo

Usa este flujo de trabajo cuando quieras que la API de Python se comporte como la CLI `translate`. `run_translation` descubre los archivos compatibles, traduce los tipos de contenido seleccionados, reescribe rutas, escribe archivos de salida, actualiza metadatos y realiza tareas de mantenimiento de traducción como la limpieza.

`run_translation` es el punto de entrada preferido para la orquestación de proyectos. `translate_project` se exporta como un alias de compatibilidad con el mismo comportamiento.

Traduce archivos Markdown en el repositorio actual a coreano y japonés:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Traduce solo notebooks de una raíz de proyecto específica:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Previsualiza el volumen de traducción sin escribir archivos:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Registra eventos de progreso estructurados para una integración:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Almacena la carga útil en la tabla de eventos de trabajo o transmítela a tu interfaz de usuario.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Los eventos usan el esquema versionado `co-op.translation.event.v1`. Las integraciones deberían
depender de campos estables como `type` y `stage_key`, no del texto mostrado a los usuarios en la consola
ni de `stage_label`.

Traduce múltiples raíces de contenido en una sola llamada:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Escribe traducciones en grupos de salida explícitos:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Usa un marcador por idioma cuando cada idioma deba contener un subdirectorio anidado:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

Si ninguno de `markdown`, `notebook` o `images` está configurado, la API traduce todos los tipos compatibles: Markdown, notebooks e imágenes.

### Conservar ediciones humanas aceptadas con un proveedor de estado de traducción

Por defecto, Co-op Translator mantiene su comportamiento existente a nivel de archivo: cuando un
fuente Markdown está obsoleta, se regenera todo el archivo traducido. Las integraciones alojadas
pueden opcionalmente pasar un `TranslationStateProvider` para conservar las ediciones humanas
en bloques fuente que no hayan cambiado.

El proveedor suministra el último par fuente/destino aceptado y registra cada nuevo
candidato. La aceptación sigue siendo responsabilidad de la integración—por ejemplo,
después de que se fusiona una solicitud de extracción de traducción:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

Para archivos Markdown con una línea base aceptada válida, Co-op Translator alinea
los bloques Markdown de nivel superior. Los bloques fuente sin cambios reutilizan los bloques traducidos actuales,
incluyendo las ediciones hechas por personas; los bloques fuente cambiados o añadidos se envían
para traducción; los bloques fuente eliminados se eliminan. Si la alineación es ambigua,
la estructura destino cambió, una traducción de bloque es inválida, o no hay una línea base
disponible, Co-op Translator recurre de forma segura a la ruta existente de
traducción de archivo completo.

Esta API almacena el estado de traducción del documento, no una memoria de
traducción de frases o segmentos entre documentos. Actualmente se aplica a la traducción de proyectos Markdown.
El comportamiento de notebooks e imágenes no cambia. Pasar `update=True`
sigue solicitando la regeneración completa.

Si uno o más archivos no se pueden traducir, `run_translation` lanza un
`RuntimeError` después de que el flujo de trabajo del proyecto finaliza en lugar de reportar una
ejecución exitosa con salida faltante. Las integraciones deberían tratar esto como un trabajo fallido y
conservar el estado de traducción aceptado previamente.

## Revisar la salida traducida

`run_review` ejecuta verificaciones de traducción deterministas sin credenciales de LLM o Vision.

!!! note "Beta"
    `run_review` es una API de revisión determinista en beta. No llama a proveedores de modelos ni escribe archivos, pero las comprobaciones y los esquemas de incidencias pueden evolucionar.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Después de una traducción solo del README, use el mismo ámbito para la revisión:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` revisa solo `README.md` en cada raíz de origen configurada,
incluyendo `groups` personalizados y directorios de salida. Otros documentos y README
anidados quedan excluidos. Un README de origen ausente genera `ValueError`; las comprobaciones de
traducción fallidas generan `RuntimeError`.

Revisa únicamente archivos cambiados respecto a una referencia base e imprime salida con formato GitHub:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Ejemplos de API para copiar y pegar

Traduce contenido Markdown sin escribir archivos:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Traduce y reescribe enlaces Markdown:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Traduce un repositorio desde Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Traduce múltiples raíces:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Conservar términos del glosario:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Puntos de entrada públicos

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## APIs de traducción de contenido

Las APIs de traducción de contenido están destinadas a integraciones que ya tienen el contenido en memoria, como una extensión del editor, una herramienta MCP, un procesador de notebooks o una canalización personalizada.

| Función | Entrada | Salida | E/S de archivos | Notas |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Asíncrono. Traduce solo el contenido Markdown. No reescribe enlaces, no escribe metadatos ni añade descargos de responsabilidad. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Asíncrono. Traduce celdas Markdown y preserva las celdas no Markdown. No reescribe enlaces, no escribe metadatos ni añade descargos de responsabilidad. |
| `translate_image_content` | Ruta de la imagen | `PIL.Image.Image` | Lee solo la imagen de origen | Sincrónico. Extrae y traduce el texto de la imagen, luego devuelve una imagen renderizada. No guarda metadatos de imagen traducida. |

`translate_markdown_content` y `translate_notebook_content` aceptan un `source_path` opcional a través de sus opciones. La ruta se pasa como contexto al traductor; los llamadores siguen siendo responsables de cualquier reescritura de rutas específica del proyecto después de la traducción.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Las mismas opciones pueden pasarse como diccionarios:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## APIs de traducción asistida por agente

Las APIs asistidas por agente no llaman al proveedor LLM configurado en Co-op Translator. Preparan fragmentos de Markdown o de notebook para que un agente anfitrión los traduzca, y luego reconstruyen el contenido final a partir de los fragmentos traducidos.

| Función | Propósito |
| --- | --- |
| `start_markdown_agent_translation` | Devuelve un trabajo Markdown autocontenido con fragmentos, indicaciones y estado de reconstrucción. |
| `finish_markdown_agent_translation` | Reconstruye Markdown a partir de un trabajo y de fragmentos traducidos por el agente anfitrión. |
| `start_notebook_agent_translation` | Devuelve un trabajo de notebook con fragmentos de celdas Markdown para la traducción por el agente anfitrión. |
| `finish_notebook_agent_translation` | Reconstruye el JSON del notebook preservando las celdas de código, las salidas y los metadatos. |

Este flujo de trabajo está pensado principalmente para hosts MCP. Si necesita traducción de repositorios en producción con Co-op Translator gestionando las llamadas a proveedores, use `translate_markdown_content`, `translate_notebook_content` o `run_translation`.

## APIs de reescritura de rutas

Las APIs de reescritura de rutas no realizan traducción. Actualizan enlaces y rutas del frontmatter una vez que los llamadores conocen la ruta de origen, la ruta de destino traducida y la estructura del proyecto.

| Función | Alcance | Notas |
| --- | --- | --- |
| `rewrite_markdown_paths` | Cuerpo Markdown y frontmatter | Reescribe enlaces Markdown y campos de ruta del frontmatter soportados para un destino traducido. |
| `rewrite_notebook_paths` | Celdas Markdown en el JSON del notebook | Aplica la reescritura de rutas Markdown a cada celda Markdown y deja las celdas no Markdown sin cambios. |

El argumento `policy` puede ser un diccionario con estos campos:

| Campo | Requerido | Propósito |
| --- | --- | --- |
| `language_code` | Sí | Código de idioma objetivo, como `"ko"` o `"pt-BR"`. |
| `root_dir` | No | Raíz del proyecto fuente. Por defecto `"."`. |
| `translations_dir` | No | Directorio de salida de traducciones de texto. Por defecto `translations` bajo `root_dir`. |
| `translated_images_dir` | No | Directorio de salida de imágenes traducidas. Por defecto `translated_images` bajo `root_dir`. |
| `translation_types` | No | Tipos de traducción habilitados. Por defecto Markdown, notebooks e imágenes. |
| `lang_subdir` | No | Subdirectorio opcional bajo cada carpeta de idioma. |

## Parámetros de traducción del proyecto

| Parámetro | Tipo | Predeterminado | Propósito |
| --- | --- | --- | --- |
| `language_codes` | `str` | Obligatorio | Códigos de idioma objetivo separados por espacios, como `"ko ja fr"`, o `"all"`. Los códigos alias se normalizan a valores BCP 47 canónicos. |
| `root_dir` | `str` | `"."` | Raíz del proyecto para un solo objetivo de traducción. Se ignora cuando se proporcionan `root_dirs` o `groups`. |
| `update` | `bool` | `False` | Elimina y recrea las traducciones existentes para los idiomas seleccionados. |
| `images` | `bool` | `False` | Incluir traducción de imágenes. Requiere configuración de Azure AI Vision. |
| `markdown` | `bool` | `False` | Incluir traducción de Markdown. |
| `notebook` | `bool` | `False` | Incluir traducción de notebooks Jupyter. |
| `debug` | `bool` | `False` | Habilitar registros de depuración. |
| `save_logs` | `bool` | `False` | Guardar archivos de registro de nivel DEBUG en el directorio `logs/` raíz. |
| `yes` | `bool` | `True` | Confirmar automáticamente los avisos para uso programático y en CI. |
| `add_disclaimer` | `bool` | `False` | Agregar avisos de traducción automática a Markdown y cuadernos traducidos. |
| `translations_dir` | `str \| None` | `None` | Directorio de salida personalizado para traducciones de texto. Las rutas relativas se resuelven con respecto a cada raíz. |
| `image_dir` | `str \| None` | `None` | Directorio de salida personalizado para imágenes traducidas. Las rutas relativas se resuelven con respecto a cada raíz. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Múltiples raíces que comparten la misma configuración de salida. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pares explícitos `(root_dir, translations_dir)`. Tiene prioridad sobre `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL del repositorio utilizada al renderizar la guía de la tabla de idiomas del README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Términos del glosario para preservar durante la traducción. Los duplicados y términos en blanco se normalizan. |
| `dry_run` | `bool` | `False` | Estimar el volumen de traducción y previsualizar el comportamiento de migración sin escribir archivos. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Adaptador opcional de persistencia de línea base aceptada y candidato para actualizaciones incrementales de Markdown. Omitirlo conserva el comportamiento existente de archivo completo. |

## Parámetros de revisión

`run_review` intencionalmente refleja la firma de `run_translation` cuando es posible para que la automatización pueda cambiar entre flujos de trabajo de traducción y revisión con la mínima ramificación.

| Parámetro | Tipo | Valor predeterminado | Propósito |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Carpetas de idiomas objetivo para revisar. Se aceptan cadenas separadas por espacios y iterables. `"all"` revisa todos los idiomas de traducción descubiertos. |
| `root_dir` | `str` | `"."` | Directorio raíz del proyecto para un único objetivo de revisión. Se ignora cuando se proporcionan `root_dirs` o `groups`. |
| `markdown` | `bool` | `False` | Incluir archivos fuente Markdown y MDX. |
| `notebook` | `bool` | `False` | Incluir archivos fuente de cuadernos Jupyter. |
| `images` | `bool` | `False` | Reservado para paridad con las opciones de traducción. Las referencias de enlace a imágenes se verifican desde Markdown. |
| `translations_dir` | `str \| None` | `None` | Directorio de salida personalizado para traducciones de texto. Las rutas relativas se resuelven con respecto a cada raíz. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Múltiples raíces que comparten la misma configuración de salida. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Pares explícitos `(root_dir, translations_dir)`. Tiene prioridad sobre `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Referencia Git utilizada para limitar la revisión a archivos fuente cambiados. |
| `readme_only` | `bool` | `False` | Revisar solo `README.md` bajo cada raíz de origen. Un README de origen faltante genera `ValueError`. |
| `output_format` | `str` | `"text"` | Formato de salida de la revisión. Los valores compatibles son `"text"` y `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Tratar las advertencias como fallos además de los errores. |
| `debug` | `bool` | `False` | Habilitar el registro de depuración. |
| `save_logs` | `bool` | `False` | Guardar archivos de registro a nivel DEBUG bajo el directorio raíz `logs/`. |

Si no se establecen `markdown`, `notebook` o `images`, la API revisa Markdown, cuadernos y referencias de enlaces de imágenes donde corresponda. La revisión no llama a un proveedor de LLM y no requiere claves de API.

## Requisitos de configuración

Las API de traducción respaldadas por proveedores requieren configuración del proveedor antes de traducir:

- La traducción de Markdown y cuadernos requiere un proveedor de LLM. Configure Azure OpenAI, OpenAI o Anthropic.
- La traducción de imágenes requiere Azure AI Vision además del proveedor de LLM.
- `run_translation` ejecuta comprobaciones de conectividad ligeras antes de que comience la traducción del proyecto.
- Las API asistidas por agente `start_*_agent_translation` y `finish_*_agent_translation` no llaman a los proveedores LLM de Co-op Translator. La aplicación anfitriona o el agente MCP traducen los fragmentos preparados.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` y `run_review` son deterministas y no requieren credenciales de proveedor.

Variables requeridas de Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Anthropic variables:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` y `ANTHROPIC_MAX_TOKENS` son opcionales. Microsoft Agent Framework es el cliente de modelo predeterminado para todos los proveedores a partir de Co-op Translator 0.22.0. Semantic Kernel todavía puede seleccionarse temporalmente con `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, pero al hacerlo se emitirá una advertencia de deprecación; consulte [configuración](configuration.md#model-client-backend) para el plan de eliminación escalonada.

Variables requeridas de Azure AI Vision para la traducción de imágenes:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` es determinista y no requiere configuración de LLM ni de Azure AI Vision.

## Notas de comportamiento

- Las API de traducción de contenido mantienen la traducción separada de la reescritura de rutas del proyecto. Llame a `rewrite_markdown_paths` o `rewrite_notebook_paths` explícitamente cuando el contenido traducido necesite que los enlaces relativos al proyecto se ajusten para una ubicación objetivo.
- Las API de orquestación de proyectos añaden comportamiento de proyecto alrededor de la traducción de contenido, incluyendo el descubrimiento de archivos, las escrituras, la reescritura de rutas, los metadatos, la limpieza y los avisos opcionales.
- `run_translation` imprime resúmenes de progreso y estimaciones a través del mismo sistema de informes respaldado por Rich que usa la CLI. La salida no interactiva vuelve a texto sin formato.
- `dry_run=True` calcula estimaciones utilizando actualizaciones virtuales del README, pero no escribe el README ni los archivos de traducción.
- `groups` se procesan de forma secuencial. Se imprime una estimación agregada única antes de que comience el trabajo.
- Cuando se selecciona la traducción de imágenes, la falta de configuración de Vision genera un error antes de que comience la traducción.
- Se detectan las carpetas de idioma existentes basadas en alias y pueden migrarse a nombres de carpetas de idioma canónicos como parte de la ejecución.
- `run_review` falla con archivos traducidos faltantes, metadatos de traducción faltantes u obsoletos, frontmatter/bloques de código Markdown malformados y JSON de notebook traducido inválido.
- `run_review` informa como advertencias los objetivos locales de enlaces de Markdown e imágenes faltantes por defecto.

## Ruta de llamadas internas

La API delega en la misma implementación central utilizada por la CLI:

Traducción:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content` o `translate_image_content` para traducción en memoria.
2. `co_op_translator.api.translation.rewrite_markdown_paths` o `rewrite_notebook_paths` para el posprocesamiento explícito de rutas.
3. `co_op_translator.api.translation.run_translation` para la orquestación completa del proyecto.
4. `co_op_translator.config.Config`, `LLMConfig` y `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Mixins de traducción de proyecto centrados en Markdown, cuadernos e imágenes.
8. Traductores de Markdown, cuadernos, texto e imágenes bajo `co_op_translator.core`.

Revisión:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Comprobaciones deterministas bajo `co_op_translator.review.checks`

Las siguientes clases son útiles para los mantenedores, pero no se exportan como la API estable a nivel de paquete.

| Clase | Módulo | Responsabilidad |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Coordina la traducción a nivel de proyecto, la gestión de directorios, la normalización de metadatos por idioma y la delegación a los traductores de Markdown, cuadernos e imágenes. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Realiza el trabajo de procesamiento de archivos asíncrono para Markdown, cuadernos, imágenes, detección de obsolescencia y actualizaciones de metadatos de traducción. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Orquesta las lecturas de archivos Markdown, la traducción de contenido, la reescritura de rutas, los metadatos, los avisos y las escrituras. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Orquesta la lectura de archivos de cuadernos, la traducción de celdas Markdown, la reescritura de rutas, los metadatos, los avisos y las escrituras. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Orquesta el descubrimiento de imágenes fuente, la traducción de imágenes, las rutas de salida, los metadatos y las escrituras. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Encuentra pares de Markdown traducidos, evalúa la calidad de la traducción y lee metadatos de confianza para flujos de trabajo de reparación de baja confianza. |
| `ReviewRunner` | `co_op_translator.review.runner` | Coordina comprobaciones deterministas de revisión a través de archivos fuente, idiomas objetivo y raíces de traducción configuradas. |
| `ReviewTarget` | `co_op_translator.review.targets` | Describe una raíz de origen y el directorio de salida de traducción revisado para esa raíz. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Detecta carpetas de idioma legado basadas en alias y prepara planes de migración a nombres de carpeta canónicos BCP 47. |
| `Config` | `co_op_translator.config.base_config` | Carga archivos `.env` y verifica si los proveedores LLM requeridos y los proveedores Vision opcionales están configurados. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Detecta automáticamente Azure OpenAI, OpenAI o Anthropic, valida las variables de entorno requeridas y ejecuta comprobaciones de conectividad del proveedor. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Detecta la configuración de Azure AI Vision y ejecuta comprobaciones de conectividad para la traducción de imágenes. |