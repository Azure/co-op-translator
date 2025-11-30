<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:35:11+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "es"
}
-->
# Actualizar la sección "Otros cursos" (repositorios de Microsoft para principiantes)

Esta guía explica cómo hacer que la sección "Otros cursos" se sincronice automáticamente usando Co-op Translator, y cómo actualizar la plantilla global para todos los repositorios.

- Aplica a: solo repositorios de Microsoft para principiantes
- Funciona con: Co-op Translator CLI y GitHub Actions
- Fuente de la plantilla: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Inicio rápido: Habilitar la sincronización automática en tu repositorio

Agrega los siguientes marcadores alrededor de la sección "Otros cursos" en tu README. Co-op Translator reemplazará todo lo que esté entre estos marcadores en cada ejecución.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Cada vez que Co-op Translator se ejecute — ya sea por CLI (por ejemplo, `translate -l "<códigos de idioma>"`) o GitHub Actions — actualizará automáticamente la sección "Otros cursos" que esté entre estos marcadores.

> [!NOTE]
> Si ya tienes una lista existente, solo envuélvela con los mismos marcadores. La próxima ejecución la reemplazará con el contenido estandarizado más reciente.

---

## Cómo cambiar el contenido global

Si quieres actualizar el contenido estandarizado que aparece en todos los repositorios para principiantes:

1. Edita la plantilla: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Abre un pull request en el repositorio de Co-op Translator con tus cambios
3. Después de que se fusione el PR, la versión de Co-op Translator se actualizará
4. La próxima vez que Co-op Translator se ejecute (CLI o GitHub Action) en un repositorio objetivo, sincronizará automáticamente la sección actualizada

Esto garantiza una única fuente de verdad para el contenido de "Otros cursos" en todos los repositorios para principiantes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->