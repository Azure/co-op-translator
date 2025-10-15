<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T02:11:07+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "es"
}
-->
# Traduce tu proyecto usando Co-op Translator

El **Co-op Translator** es una herramienta de línea de comandos (CLI) que te ayuda a traducir archivos markdown e imágenes de tu proyecto a varios idiomas. En esta sección se explica cómo usar la herramienta, se detallan las diferentes opciones de la CLI y se ofrecen ejemplos para distintos casos de uso.

> [!NOTE]
> Para ver la lista completa de comandos y sus descripciones detalladas, consulta la [Referencia de comandos](./command-reference.md).

---

## Escenarios de ejemplo y comandos

Aquí tienes algunos casos de uso comunes para el **Co-op Translator**, junto con los comandos adecuados para ejecutarlos.

### 1. Traducción básica (un solo idioma)

Para traducir todo tu proyecto (archivos markdown e imágenes) a un solo idioma, como coreano, usa el siguiente comando:

```bash
translate -l "ko"
```

Este comando traducirá todos los archivos markdown e imágenes al coreano, añadiendo nuevas traducciones sin eliminar las existentes.

> [!TIP]
>
> ¿Quieres ver qué códigos de idioma están disponibles en **Co-op Translator**? Visita la sección [Idiomas soportados](https://github.com/Azure/co-op-translator#supported-languages) en el repositorio para más detalles.

#### Ejemplo en Phi-3 CookBook

En el **Phi-3 CookBook**, utilicé el siguiente método para añadir la traducción al coreano de los archivos markdown e imágenes existentes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traducción a varios idiomas

Para traducir tu proyecto a varios idiomas (por ejemplo, español, francés y alemán), usa este comando:

```bash
translate -l "es fr de"
```

Este comando traducirá el proyecto al español, francés y alemán, añadiendo nuevas traducciones sin sobrescribir las existentes.

#### Ejemplo en Phi-3 CookBook

En el **Phi-3 CookBook**, después de descargar los últimos cambios para reflejar los commits más recientes, utilicé el siguiente método para traducir los archivos markdown e imágenes recién añadidos.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Aunque normalmente se recomienda traducir un idioma a la vez, en situaciones como esta donde hay que añadir cambios específicos, traducir varios idiomas a la vez puede ser eficiente.

### 3. Actualizar traducciones (elimina las traducciones existentes)

Para actualizar las traducciones existentes (es decir, eliminar las traducciones actuales y reemplazarlas por nuevas), usa la opción `-u`. Esto eliminará todas las traducciones existentes para los idiomas especificados y las volverá a traducir.

```bash
translate -l "ko" -u
```

Advertencia: Este comando te pedirá confirmación antes de continuar con la eliminación de las traducciones existentes.

#### Ejemplo en Phi-3 CookBook

En el **Phi-3 CookBook**, utilicé el siguiente método para actualizar todos los archivos traducidos al español. Recomiendo usar este método cuando hay cambios importantes en el contenido original en varios documentos markdown. Si solo hay unos pocos archivos traducidos que actualizar, es más eficiente eliminar manualmente esos archivos específicos y luego usar el método `-a` para añadir las traducciones actualizadas.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Traducir solo imágenes

Para traducir únicamente los archivos de imagen de tu proyecto, usa la opción `-img`:

```bash
translate -l "ko" -img
```

Este comando traducirá solo las imágenes al coreano, sin afectar los archivos markdown.

### 6. Traducir solo archivos Markdown

Para traducir únicamente los archivos markdown de tu proyecto, usa la opción `-md`:

```bash
translate -l "ko" -md
```

#### Ejemplo en Phi-3 CookBook

En el **Phi-3 CookBook**, utilicé el siguiente método para comprobar errores de traducción en los archivos coreanos y volver a intentar automáticamente la traducción de los archivos con problemas detectados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Esta opción comprueba si hay errores de traducción. Actualmente, si la diferencia en los saltos de línea entre el archivo original y el traducido es mayor de seis, el archivo se marca como erróneo. Planeo mejorar este criterio para que sea más flexible en el futuro.

Por ejemplo, este método es útil para detectar fragmentos faltantes o traducciones corruptas, y volverá a intentar automáticamente la traducción de esos archivos.

Sin embargo, si ya sabes qué archivos son problemáticos, es más eficiente eliminarlos manualmente y usar la opción `-a` para volver a traducirlos.

### 8. Modo depuración

Para activar el registro detallado y facilitar la resolución de problemas, usa la opción `-d`:

```bash
translate -l "ko" -d
```

Este comando ejecutará la traducción en modo depuración, proporcionando información adicional en los registros que puede ayudarte a identificar problemas durante el proceso de traducción.

#### Ejemplo en Phi-3 CookBook

En el **Phi-3 CookBook**, me encontré con un problema donde las traducciones con muchos enlaces en los archivos markdown causaban errores de formato, como traducciones rotas y saltos de línea ignorados. Para diagnosticar este problema, utilicé la opción `-d` para ver cómo funcionaba el proceso de traducción.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Traducir a todos los idiomas

Si quieres traducir el proyecto a todos los idiomas soportados, usa la palabra clave all.

> [!WARNING]
> Traducir a todos los idiomas a la vez puede llevar mucho tiempo dependiendo del tamaño del proyecto. Por ejemplo, traducir el **Phi-3 CookBook** al español tomó unas 2 horas. Dada la magnitud, no es práctico que una sola persona gestione 20 idiomas. Se recomienda dividir el trabajo entre varios colaboradores, cada uno encargándose de uno o dos idiomas, y actualizar las traducciones poco a poco.

```bash
translate -l "all"
```

Este comando traducirá el proyecto a todos los idiomas disponibles. Si continúas, la traducción puede tardar bastante dependiendo del tamaño del proyecto.

> [!TIP]
>
> ### Eliminar archivos traducidos manualmente (opcional)
> Ahora los archivos traducidos se detectan y limpian automáticamente cuando se actualiza un archivo fuente.
>
> Sin embargo, si quieres actualizar manualmente una traducción —por ejemplo, para rehacer un archivo específico o anular el comportamiento del sistema— puedes usar el siguiente comando para eliminar todas las versiones del archivo en las carpetas de idiomas.
>
> ### En Windows:
> 1. **Usando Command Prompt**:
>    - Abre Command Prompt.
>    - Navega a la carpeta donde están los archivos usando el comando `cd`.
>    - Usa el siguiente comando para eliminar archivos:
>      ```
>      del /s *filename*
>      ```
>      Sustituye `filename` por la parte específica del nombre del archivo que buscas. La opción `/s` busca en los subdirectorios.
>
> 2. **Usando PowerShell**:
>    - Abre PowerShell.
>    - Ejecuta este comando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Sustituye `"C:\YourPath"` por la ruta de la carpeta y `filename` por el nombre específico.
>
> ### En macOS/Linux:
> 1. **Usando Terminal**:
>   - Abre Terminal.
>   - Navega al directorio con `cd`.
>   - Usa el comando `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Sustituye `filename` por el nombre específico.
>
> Revisa siempre los archivos antes de eliminarlos para evitar pérdidas accidentales.
>
> Una vez que hayas eliminado los archivos que necesitas reemplazar, simplemente vuelve a ejecutar tu comando `translate -l` para actualizar los cambios más recientes del archivo.

---

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.