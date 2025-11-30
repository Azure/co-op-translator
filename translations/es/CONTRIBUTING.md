<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T02:09:36+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "es"
}
-->
# Contribuir a Co-op Translator

Este proyecto da la bienvenida a contribuciones y sugerencias. La mayoría de las contribuciones requieren que aceptes un
Acuerdo de Licencia de Contribuyente (CLA), declarando que tienes el derecho de, y realmente otorgas,
los derechos para que usemos tu contribución. Para más detalles, visita https://cla.opensource.microsoft.com.

Cuando envíes un pull request, un bot de CLA determinará automáticamente si necesitas proporcionar
un CLA y marcará el PR apropiadamente (por ejemplo, con un estado o comentario). Simplemente sigue las instrucciones
que te indique el bot. Solo tendrás que hacer esto una vez para todos los repositorios que usen nuestro CLA.

## Configuración del entorno de desarrollo

Para configurar el entorno de desarrollo de este proyecto, recomendamos usar Poetry para gestionar las dependencias. Usamos `pyproject.toml` para administrar las dependencias del proyecto, por lo tanto, para instalarlas, debes usar Poetry.

### Crear un entorno virtual

#### Usando pip

```bash
python -m venv .venv
```

#### Usando Poetry

```bash
poetry init
```

### Activar el entorno virtual

#### Para pip y Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Usando Poetry

```bash
poetry shell
```

### Instalación del paquete y paquetes requeridos

#### Usando Poetry (desde pyproject.toml)

```bash
poetry install
```

### Pruebas manuales

Antes de enviar un PR, es importante probar la funcionalidad de traducción con documentación real:

1. Crea un directorio de prueba en el directorio raíz:
    ```bash
    mkdir test_docs
    ```

2. Copia algunos archivos markdown y las imágenes que quieras traducir en el directorio de prueba. Por ejemplo:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Instala el paquete localmente:
    ```bash
    pip install -e .
    ```

4. Ejecuta Co-op Translator en tus documentos de prueba:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Revisa los archivos traducidos en `test_docs/translations` y `test_docs/translated_images` para verificar:
   - La calidad de la traducción
   - Que los comentarios de metadatos sean correctos
   - Que la estructura original de markdown se conserve
   - Que los enlaces e imágenes funcionen correctamente

Estas pruebas manuales ayudan a asegurar que tus cambios funcionen bien en escenarios reales.

### Variables de entorno

1. Crea un archivo `.env` en el directorio raíz copiando el archivo `.env.template` proporcionado.
1. Completa las variables de entorno según las indicaciones.

> [!TIP]
>
> ### Opciones adicionales para el entorno de desarrollo
>
> Además de ejecutar el proyecto localmente, también puedes usar GitHub Codespaces o los Dev Containers de VS Code como alternativas para configurar el entorno de desarrollo.
>
> #### GitHub Codespaces
>
> Puedes ejecutar estos ejemplos de forma virtual usando GitHub Codespaces, sin necesidad de configuraciones adicionales.
>
> El botón abrirá una instancia de VS Code basada en la web en tu navegador:
>
> 1. Abre la plantilla (esto puede tardar varios minutos):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Ejecución local usando Dev Containers de VS Code
>
> ⚠️ Esta opción solo funcionará si tu Docker Desktop tiene al menos 16 GB de RAM asignados. Si tienes menos de 16 GB de RAM, puedes probar la [opción de GitHub Codespaces](../..) o [configurarlo localmente](../..).
>
> Otra opción relacionada son los Dev Containers de VS Code, que abrirán el proyecto en tu VS Code local usando la [extensión Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Inicia Docker Desktop (instálalo si no lo tienes)
> 2. Abre el proyecto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Estilo de código

Usamos [Black](https://github.com/psf/black) como formateador de código Python para mantener un estilo consistente en todo el proyecto. Black es un formateador estricto que reformatea automáticamente el código Python para ajustarse a su estilo.

#### Configuración

La configuración de Black está especificada en nuestro `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalación de Black

Puedes instalar Black usando Poetry (recomendado) o pip:

##### Usando Poetry

Black se instala automáticamente al configurar el entorno de desarrollo:
```bash
poetry install
```

##### Usando pip

Si usas pip, puedes instalar Black directamente:
```bash
pip install black
```

#### Uso de Black

##### Con Poetry

1. Formatea todos los archivos Python del proyecto:
    ```bash
    poetry run black .
    ```

2. Formatea un archivo o directorio específico:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Con pip

1. Formatea todos los archivos Python del proyecto:
    ```bash
    black .
    ```

2. Formatea un archivo o directorio específico:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Recomendamos configurar tu editor para que formatee automáticamente el código con Black al guardar. La mayoría de los editores modernos lo soportan mediante extensiones o plugins.

## Ejecutar Co-op Translator

Para ejecutar Co-op Translator usando Poetry en tu entorno, sigue estos pasos:

1. Navega al directorio donde quieras realizar pruebas de traducción o crea una carpeta temporal para pruebas.

2. Ejecuta el siguiente comando. Reemplaza `-l ko` por el código de idioma al que quieras traducir. El flag `-d` indica modo debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Asegúrate de que tu entorno Poetry esté activado (poetry shell) antes de ejecutar el comando.

## Contribuir un nuevo idioma

Aceptamos contribuciones que añadan soporte para nuevos idiomas. Antes de abrir un PR, completa los siguientes pasos para facilitar la revisión.

1. Añade el idioma al mapeo de fuentes
   - Edita `src/co_op_translator/fonts/font_language_mappings.yml`
   - Añade una entrada con:
     - `code`: Código de idioma tipo ISO (por ejemplo, `vi`)
     - `name`: Nombre legible para humanos
     - `font`: Una fuente incluida en `src/co_op_translator/fonts/` que soporte el sistema de escritura
     - `rtl`: `true` si es de derecha a izquierda, de lo contrario `false`

2. Incluye los archivos de fuente necesarios (si aplica)
   - Si se requiere una fuente nueva, verifica la compatibilidad de la licencia para distribución open source
   - Añade el archivo de fuente a `src/co_op_translator/fonts/`

3. Verificación local
   - Ejecuta traducciones para una muestra pequeña (Markdown, imágenes y notebooks según corresponda)
   - Verifica que la salida se renderice correctamente, incluyendo fuentes y cualquier diseño RTL si aplica

4. Actualiza la documentación
   - Asegúrate de que el idioma aparezca en `getting_started/supported-languages.md`
   - No es necesario modificar `README_languages_template.md`; se genera a partir de la lista soportada

5. Abre un PR
   - Describe el idioma añadido y cualquier consideración sobre fuentes/licencias
   - Adjunta capturas de pantalla de los resultados renderizados si es posible

Ejemplo de entrada YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Mantenedores

### Mensaje de commit y estrategia de merge

Para asegurar consistencia y claridad en el historial de commits del proyecto, seguimos un formato específico de mensaje de commit **para el mensaje final** al usar la estrategia **Squash and Merge**.

Cuando se fusiona un pull request (PR), los commits individuales se agrupan en un solo commit. El mensaje final debe seguir el formato de abajo para mantener un historial limpio y consistente.

#### Formato de mensaje de commit (para squash and merge)

Usamos el siguiente formato para los mensajes de commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Especifica la categoría del commit. Usamos los siguientes tipos:
  - `Docs`: Para actualizaciones de documentación.
  - `Build`: Para cambios relacionados con el sistema de construcción o dependencias, incluyendo actualizaciones de archivos de configuración, flujos de trabajo de CI o el Dockerfile.
  - `Core`: Para modificaciones en la funcionalidad principal del proyecto, especialmente en archivos del directorio `src/co_op_translator/core`.

- **description**: Un resumen conciso del cambio.
- **PR number**: El número del pull request asociado al commit.

**Ejemplos**:

- `Docs: Actualizar instrucciones de instalación para mayor claridad (#50)`
- `Core: Mejorar el manejo de la traducción de imágenes (#60)`

> [!NOTE]
> Actualmente, los prefijos **`Docs`**, **`Core`** y **`Build`** se añaden automáticamente a los títulos de los PR según las etiquetas aplicadas al código fuente modificado. Mientras la etiqueta correcta esté aplicada, normalmente no necesitas actualizar el título del PR manualmente. Solo debes verificar que todo esté correcto y que el prefijo se haya generado adecuadamente.

#### Estrategia de merge

Usamos **Squash and Merge** como estrategia predeterminada para los pull requests. Esta estrategia asegura que los mensajes de commit sigan nuestro formato, incluso si los commits individuales no lo hacen.

**Razones**:

- Un historial de proyecto limpio y lineal.
- Consistencia en los mensajes de commit.
- Menos ruido por commits menores (por ejemplo, "fix typo").

Al fusionar, asegúrate de que el mensaje final siga el formato descrito arriba.

**Ejemplo de Squash and Merge**
Si un PR contiene los siguientes commits:

- `fix typo`
- `update README`
- `adjust formatting`

Deben agruparse en:
`Docs: Mejorar claridad y formato de la documentación (#65)`

---

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.