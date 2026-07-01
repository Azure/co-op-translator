# Repositorios "For Beginners" de Microsoft

Esta página es para los mantenedores de los repositorios "For Beginners" de Microsoft que utilizan la sección compartida "Other Courses" del README.

La mayoría de los usuarios de Co-op Translator no necesitan esta página.

## Sincronización automática de la sección "Other Courses"

Añade estos marcadores alrededor de la sección "Other Courses" en tu README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que Co-op Translator se ejecuta a través de la CLI o GitHub Actions, reemplaza el contenido entre los marcadores con la plantilla empaquetada.

## Actualizar la plantilla compartida

La fuente de la plantilla se encuentra en:

```text
src/co_op_translator/templates/other_courses.md
```

Para actualizar el contenido compartido:

1. Edita la plantilla.
2. Abre un pull request a Co-op Translator.
3. Después de que se publique el cambio, ejecuta Co-op Translator en el repositorio de destino.

## Aviso sobre Sparse Checkout

Los repositorios de cursos grandes pueden volverse costosos de clonar cuando incluyen muchas salidas traducidas. Puedes incluir este aviso en las secciones de idioma generadas:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```