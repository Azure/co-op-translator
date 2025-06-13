<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:30:48+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "es"
}
-->
# Instalar el paquete Co-op translator

El **Co-op Translator** es una herramienta de línea de comandos (CLI) diseñada para ayudarte a traducir todos los archivos markdown e imágenes de tu proyecto a varios idiomas. Este tutorial te guiará para configurar el traductor y ejecutarlo en diferentes casos de uso.

### Crear un entorno virtual

Puedes crear un entorno virtual usando `pip` o `Poetry`. Escribe uno de los siguientes comandos en tu terminal.

#### Usando pip

```bash
python -m venv .venv
```

#### Usando Poetry

```bash
poetry init
```

### Activar el entorno virtual

Después de crear el entorno virtual, necesitarás activarlo. Los pasos varían según tu sistema operativo. Escribe el siguiente comando en tu terminal.

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

### Instalación del paquete y dependencias necesarias

Una vez que tu entorno virtual esté configurado y activado, el siguiente paso es instalar las dependencias necesarias.

### Instalación rápida

Instala Co-Op Translator vía pip

```
pip install co-op-translator
```
O 

Instala vía poetry
```
poetry add co-op-translator
```

#### Usando pip (desde requirements.txt) si clonas este repositorio

![NOTE] Por favor, NO hagas esto si instalaste co-op translator mediante la instalación rápida.

1. Si usas pip, escribe el siguiente comando en tu terminal. Esto instalará automáticamente los paquetes requeridos especificados en el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Usando Poetry (desde pyproject.toml)

1. Si usas Poetry, escribe el siguiente comando en tu terminal. Esto instalará automáticamente los paquetes requeridos especificados en el archivo `pyproject.toml`:

    ```bash
    poetry install
    ```

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.