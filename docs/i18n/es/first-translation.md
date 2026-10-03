# Traducir, editar y revisar un pequeño proyecto

Comience con dos archivos Markdown breves y un idioma de destino. Verá dónde se escriben las traducciones, qué ocurre cuando cambia la fuente y cómo comprobar el resultado.

## Resultados registrados

El ejemplo se ejecutó el 19 de septiembre de 2026 con Co-op Translator 0.21.0 y Azure OpenAI (`gpt-5-mini`). Los comandos de CLI no modificados se invocaron mediante Click's `CliRunner` usando la rueda construida y las dependencias de Python existentes.

| Step | Result |
| --- | --- |
| Preview | Salida 0; no se solicitó traducción del modelo |
| Initial translation | Salida 0; 27.36 segundos |
| Initial review | Salida 0 |
| Edit README and review | Salida 1; se detectó traducción obsoleta |
| Update translation | Salida 0; 22.17 segundos |
| Review after update | Salida 0; sin errores ni advertencias |
| Unchanged guide | Bytes idénticos antes y después de la actualización del README |
| Run again | Salida 0; hashes idénticos para todos los archivos de traducción |

Estas son mediciones de ejecuciones individuales, no garantías de rendimiento. No se incluye el tiempo de configuración; no se midió la facturación del proveedor. Una ejecución sin cambios aún puede realizar una comprobación de estado del proveedor.

Inspeccione la [traducción inicial](../../assets/demo/before.txt), [traducción actualizada](../../assets/demo/after.txt), [diff de la traducción completa](../../assets/demo/update.diff), [revisión obsoleta](../../assets/demo/review-stale.txt), [revisión final](../../assets/demo/review-after.txt), y [detalles de la ejecución](../../assets/demo/results.json). La traducción de archivo completo puede cambiar otras formulaciones, como muestra el diff capturado. Ambos artefactos de texto conservan el descargo de responsabilidad generado.

La revisión humana sigue siendo importante: la actualización capturada usa `[사용 가이드](guide.md)을`; la partícula coreana debería ser `[사용 가이드](guide.md)를`. Los artefactos de texto mantienen esta salida intacta en lugar de presentar una traducción editada como resultado del modelo. La revisión estructural aprueba a pesar de este problema de redacción.

## 1. Prepare una carpeta pequeña

Utilice Python 3.11–3.14 y la [configuración del entorno virtual](configuration.md#local-runtime-setup). Instale la versión empleada en este ejemplo:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Descargue [README.txt](../../assets/demo/README.txt) y [guide.txt](../../assets/demo/guide.txt) en esta carpeta, guardándolos como `README.md` y `guide.md`. Son documentos pequeños de un proyecto ficticio; no se necesita instalar ninguna aplicación.

El README incluye un bloque de código y un enlace a `guide.md`. Su frase final es:

```text
Notes are saved locally.
```

Mantenga solo estos dos documentos fuente en esta carpeta. Todos los comandos siguientes se ejecutan dentro de `translation-demo` y funcionan en Bash y PowerShell.

## 2. Vista previa sin credenciales

```bash
translate -l "ko" -md --dry-run
```

La vista previa estima el trabajo de traducción sin llamar a un modelo ni escribir traducciones. Las estimaciones de tokens no son una cotización de facturación. La primera ejecución debería identificar ambos archivos Markdown como trabajo nuevo.

## 3. Elija un proveedor y traduzca

Configure un proveedor usando la [guía de configuración](configuration.md): Azure OpenAI, OpenAI o Anthropic. La traducción de texto con OpenAI y Anthropic no requiere una cuenta de Azure. No se necesitan servicios de imágenes para este ejemplo.

Si usa un archivo `.env` local, añada `.env` al `.gitignore` de esta carpeta. Las llamadas de traducción usan la cuenta de su proveedor y pueden generar cargos.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Abra `translations/ko/README.md` y `translations/ko/guide.md`. Verifique la redacción en coreano, el bloque de código y el enlace desde el README traducido hacia la guía traducida. La redacción de la salida varía según el modelo.

`co-op-review` comprueba la vigencia, la estructura y los enlaces locales. Un resultado aprobado no certifica la exactitud lingüística. Solucione cualquier error informado antes de continuar.

Registre la línea base exitosa con Git (configure su identidad de Git primero si es necesario):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Cambiar la fuente

En `README.md`, reemplace `Notes are saved locally.` por:

```text
Notes are saved locally as Markdown files.
```

Deje `guide.md` sin cambios. Luego ejecute:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

La revisión debería informar que la traducción del README está obsoleta y finalizar con error. Este es el estado intermedio esperado. La vista previa debería identificar trabajo para el README cambiado.

## 5. Actualizar e inspeccionar el diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Inspeccione el diff real: la CLI predeterminada retraduce el archivo cambiado, por lo que el modelo también puede revisar otras redacciones en ese archivo. La guía sin cambios no debería tener diff. La revisión ya no debería informar que el README está obsoleto; investigue cualquier otro hallazgo en lugar de ignorarlo.

La preservación a nivel de bloque de las ediciones humanas de Markdown requiere un proveedor opcional de estado de traducción en la [API de Python](api.md). No está habilitado por estos comandos de la CLI.

## 6. Ejecute de nuevo sin cambios

Confirme el código fuente y la traducción actualizados:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Con las traducciones actuales y la configuración sin cambios, el traductor omite los archivos. El comando Git final no debería producir diff y debería finalizar con éxito.

## Próximos pasos

- [Traducir solo un README y abrir un pull request](github-actions.md#your-first-readme-translation-pr).
- [Elija CLI, API de Python o MCP](workflows.md).
- [Reportar un problema de traducción sin programar](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).