<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T02:11:01+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "es"
}
-->
# Instala el paquete Co-op Translator

El **Co-op Translator** es una herramienta de línea de comandos (CLI) diseñada para ayudarte a traducir todos los archivos markdown e imágenes de tu proyecto a varios idiomas. Este tutorial te guiará para configurar el traductor y ejecutarlo en diferentes casos de uso.

### Crea un entorno virtual

Puedes crear un entorno virtual usando `pip` o `Poetry`. Escribe uno de los siguientes comandos en tu terminal.

#### Usando pip

```bash
python -m venv .venv
```

#### Usando Poetry

```bash
poetry init
```

### Activa el entorno virtual

Después de crear el entorno virtual, tendrás que activarlo. Los pasos varían según tu sistema operativo. Escribe el siguiente comando en tu terminal.

#### Para pip y Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Usando Poetry

1. Si creaste el entorno con Poetry, escribe el siguiente comando en tu terminal para activarlo.

    ```bash
    poetry shell
    ```

### Instalación del paquete y paquetes necesarios

Una vez que tu entorno virtual esté listo y activado, el siguiente paso es instalar las dependencias necesarias.

### Instalación rápida

Instala Co-Op Translator usando pip

```
pip install co-op-translator
```
O 

Instala usando poetry
```
poetry add co-op-translator
```

#### Usando pip (desde requirements.txt) si clonas este repositorio 

> [!NOTE]
> Por favor, NO hagas esto si instalas co-op translator usando la instalación rápida.

1. Si usas pip, escribe el siguiente comando en tu terminal. Instalará automáticamente los paquetes requeridos que se especifican en el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Usando Poetry (desde pyproject.toml)

1. Si usas Poetry, escribe el siguiente comando en tu terminal. Instalará automáticamente los paquetes requeridos que se especifican en el archivo `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.