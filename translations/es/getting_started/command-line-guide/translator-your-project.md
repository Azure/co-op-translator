<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33db54f4f3ca9f0321be05374b591f2b",
  "translation_date": "2025-05-06T17:59:17+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "es"
}
-->
# Traduce tu proyecto usando Co-op Translator

El **Co-op Translator** es una herramienta de línea de comandos (CLI) que te ayuda a traducir archivos markdown e imágenes de tu proyecto a varios idiomas. Esta sección explica cómo usar la herramienta, cubre las diferentes opciones de la CLI y proporciona ejemplos para distintos casos de uso.

> [!NOTE]
> Para una lista completa de comandos y sus descripciones detalladas, consulta la [Referencia de comandos](./command-reference.md).

---

## Escenarios y comandos de ejemplo

Aquí tienes algunos casos de uso comunes para el **Co-op Translator**, junto con los comandos apropiados para ejecutarlos.

### 1. Traducción básica (un solo idioma)

Para traducir todo tu proyecto (archivos markdown e imágenes) a un solo idioma, como coreano, usa el siguiente comando:

```bash
translate -l "ko"
```

Este comando traducirá todos los archivos markdown e imágenes al coreano, agregando nuevas traducciones sin eliminar las existentes.

> [!TIP]
>
> ¿Quieres saber qué códigos de idioma están disponibles en **Co-op Translator**? Visita la sección [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) en el repositorio para más detalles.

#### Ejemplo en Phi-3 CookBook

En el **Phi-3 CookBook**, usé el siguiente método para agregar la traducción al coreano de los archivos markdown e imágenes existentes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traducción a múltiples idiomas

Para traducir tu proyecto a varios idiomas (por ejemplo, español, francés y alemán), usa este comando:

```bash
translate -l "es fr de"
```

Este comando traducirá el proyecto a español, francés y alemán, agregando nuevas traducciones sin sobrescribir las existentes.

#### Ejemplo en Phi-3 CookBook

En el **Phi-3 CookBook**, después de descargar los últimos cambios para reflejar los commits más recientes, usé el siguiente método para traducir los archivos markdown e imágenes recién añadidos.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Aunque generalmente se recomienda traducir un idioma a la vez, en situaciones como esta, donde se deben agregar cambios específicos, traducir varios idiomas a la vez puede ser eficiente.

### 3. Especificar el directorio raíz

Por defecto, el traductor usa el directorio de trabajo actual. Si tu proyecto está en otra ubicación, especifica el directorio raíz con la opción -r:

```bash
translate -l "es fr de" -r "./my_project"
```

Este comando traduce los archivos en `./my_project` into Spanish, French, and German.

### 4. Updating Translations (Deletes Existing Translations)

To update existing translations (i.e., delete the current translations and replace them with new ones), use the `-u` opción. Esto eliminará todas las traducciones existentes para los idiomas especificados y las volverá a traducir.

```bash
translate -l "ko" -u
```

Advertencia: Este comando te pedirá confirmación antes de proceder a eliminar las traducciones existentes.

#### Ejemplo en Phi-3 CookBook

En el **Phi-3 CookBook**, usé el siguiente método para actualizar todos los archivos traducidos al español. Recomiendo usar este método cuando hay cambios significativos en el contenido original en varios documentos markdown. Si solo hay unos pocos archivos markdown traducidos para actualizar, es más eficiente eliminar manualmente esos archivos específicos y luego usar el método `-a` para agregar las traducciones actualizadas.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. Traducir solo imágenes

Para traducir solo los archivos de imagen en tu proyecto, usa la opción `-img`:

```bash
translate -l "ko" -img
```

Este comando traducirá solo las imágenes al coreano, sin afectar ningún archivo markdown.

### 7. Traducir solo archivos markdown

Para traducir solo los archivos markdown en tu proyecto, usa la opción `-md`:

```bash
translate -l "ko" -md
```

### 8. Verificar errores en archivos traducidos

Si quieres revisar los archivos traducidos en busca de errores y reintentar la traducción si es necesario, usa la opción `-chk`:

```bash
translate -l "ko" -chk
```

Este comando escaneará los archivos markdown traducidos y reintentará la traducción de cualquier archivo con errores.

#### Ejemplo en Phi-3 CookBook

En el **Phi-3 CookBook**, usé el siguiente método para verificar errores de traducción en los archivos coreanos y reintentar automáticamente la traducción de cualquier archivo con problemas detectados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Esta opción verifica errores de traducción. Actualmente, si la diferencia en saltos de línea entre el archivo original y el traducido es mayor a seis, el archivo se marca como con error de traducción. Planeo mejorar este criterio para mayor flexibilidad en el futuro.

Por ejemplo, este método es útil para detectar partes faltantes o traducciones corruptas, y reintentará automáticamente la traducción de esos archivos.

Sin embargo, si ya sabes qué archivos tienen problemas, es más eficiente eliminar manualmente esos archivos y usar la opción `-a` option to re-translate them.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Este comando ejecutará la traducción en modo depuración, proporcionando información adicional en los registros que puede ayudarte a identificar problemas durante el proceso de traducción.

#### Ejemplo en Phi-3 CookBook

En el **Phi-3 CookBook**, me encontré con un problema donde las traducciones con muchos enlaces en archivos markdown causaban errores de formato, como traducciones rotas y saltos de línea ignorados. Para diagnosticar este problema, usé la opción `-d` para ver cómo funcionaba el proceso de traducción.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. Traducir a todos los idiomas

Si quieres traducir el proyecto a todos los idiomas soportados, usa la palabra clave all.

> [!WARNING]
> Traducir todos los idiomas a la vez puede tomar una cantidad significativa de tiempo dependiendo del tamaño del proyecto. Por ejemplo, traducir el **Phi-3 CookBook** al español tomó alrededor de 2 horas. Dado el volumen, no es práctico que una sola persona maneje 20 idiomas. Se recomienda dividir el trabajo entre varios colaboradores, cada uno gestionando uno o dos idiomas, y actualizar las traducciones gradualmente.

```bash
translate -l "all"
```

Este comando traducirá el proyecto a todos los idiomas disponibles. Si continúas, la traducción puede tardar bastante dependiendo del tamaño del proyecto.

> [!TIP]
>
> ### Eliminar archivos que necesitan ser actualizados  
> Para actualizar archivos modificados recientemente en un Pull Request, el primer paso es eliminar todas las versiones existentes del archivo específico ubicadas en las distintas carpetas de traducción por idioma. Puedes hacer esto en masa usando el siguiente comando para borrar todos los archivos con un nombre específico dentro de las carpetas de traducción.
>
> ### En Windows:
> 1. **Usando Command Prompt**:
>    - Abre Command Prompt.
>    - Navega a la carpeta donde están los archivos usando el comando `cd`.
>    - Usa el siguiente comando para eliminar archivos:
>      ```
>      del /s *filename*
>      ```
>      La opción `/s` busca también en subdirectorios.
>
> 2. **Usando PowerShell**:
>    - Abre PowerShell.
>    - Ejecuta este comando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Reemplaza `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` comando:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Reemplaza `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` comando para actualizar los cambios más recientes en los archivos.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por un humano. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.