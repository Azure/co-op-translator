<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:24:08+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "es"
}
-->
# Contribuyendo a Co-op Translator

Este proyecto acepta contribuciones y sugerencias. La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Contribuyente (CLA) declarando que tienes el derecho, y efectivamente otorgas, los derechos para que usemos tu contribución. Para más detalles, visita https://cla.opensource.microsoft.com.

Cuando envíes un pull request, un bot de CLA determinará automáticamente si necesitas proporcionar un CLA y marcará el PR adecuadamente (por ejemplo, verificación de estado, comentario). Solo debes seguir las instrucciones proporcionadas por el bot. Solo tendrás que hacer esto una vez para todos los repositorios que usen nuestro CLA.

## Configuración del entorno de desarrollo

Para configurar el entorno de desarrollo de este proyecto, recomendamos usar Poetry para gestionar las dependencias. Usamos `pyproject.toml` para manejar las dependencias del proyecto, por lo que para instalar las dependencias, debes usar Poetry.

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

2. Copia algunos documentos markdown y las imágenes que quieras traducir en el directorio de prueba. Por ejemplo:
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

5. Revisa los archivos traducidos en `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Completa las variables de entorno según las indicaciones.

> [!TIP]
>
> ### Opciones adicionales para el entorno de desarrollo
>
> Además de ejecutar el proyecto localmente, también puedes usar GitHub Codespaces o VS Code Dev Containers para una configuración alternativa del entorno de desarrollo.
>
> #### GitHub Codespaces
>
> Puedes ejecutar estos ejemplos virtualmente usando GitHub Codespaces sin necesidad de configuraciones adicionales.
>
> El botón abrirá una instancia de VS Code basada en web en tu navegador:
>
> 1. Abre la plantilla (esto puede tardar varios minutos):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Ejecución local usando VS Code Dev Containers
>
> ⚠️ Esta opción solo funcionará si Docker Desktop tiene asignados al menos 16 GB de RAM. Si tienes menos de 16 GB, puedes probar la opción de [GitHub Codespaces](../..) o [configurarlo localmente](../..).
>
> Una opción relacionada es VS Code Dev Containers, que abrirá el proyecto en tu VS Code local usando la [extensión Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Inicia Docker Desktop (instálalo si no está instalado)
> 2. Abre el proyecto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Estilo de código

Usamos [Black](https://github.com/psf/black) como formateador de código Python para mantener un estilo consistente en todo el proyecto. Black es un formateador inflexible que reformatea automáticamente el código Python para ajustarse al estilo Black.

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

Black se instala automáticamente cuando configuras el entorno de desarrollo:
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

1. Formatea todos los archivos Python en el proyecto:
    ```bash
    poetry run black .
    ```

2. Formatea un archivo o directorio específico:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Con pip

1. Formatea todos los archivos Python en el proyecto:
    ```bash
    black .
    ```

2. Formatea un archivo o directorio específico:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Recomendamos configurar tu editor para que formatee automáticamente el código con Black al guardar. La mayoría de los editores modernos soportan esto mediante extensiones o plugins.

## Ejecutando Co-op Translator

Para ejecutar Co-op Translator usando Poetry en tu entorno, sigue estos pasos:

1. Navega al directorio donde quieres realizar pruebas de traducción o crea una carpeta temporal para pruebas.

2. Ejecuta el siguiente comando. El flag `-l ko` with the language code you wish to translate into. The `-d` indica modo debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Asegúrate de que tu entorno Poetry esté activado (poetry shell) antes de ejecutar el comando.

## Mantenedores

### Mensaje de commit y estrategia de Merge

Para asegurar consistencia y claridad en el historial de commits de nuestro proyecto, seguimos un formato específico para el mensaje de commit **final** cuando usamos la estrategia **Squash and Merge**.

Cuando un pull request (PR) se fusiona, los commits individuales se combinarán en un solo commit. El mensaje de commit final debe seguir el formato que se muestra a continuación para mantener un historial limpio y consistente.

#### Formato del mensaje de commit (para squash and merge)

Usamos el siguiente formato para los mensajes de commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Especifica la categoría del commit. Usamos los siguientes tipos:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Actualizar instrucciones de instalación para mayor claridad (#50)`
- `Core: Mejorar manejo de traducción de imágenes (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `corregir error tipográfico`
- `actualizar README`
- `ajustar formato`

They should be squashed into:
`Docs: Mejorar claridad y formato de la documentación (#65)`

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.