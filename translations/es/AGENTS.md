<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:19:14+00:00",
  "source_file": "AGENTS.md",
  "language_code": "es"
}
-->
# Descripción general del proyecto

Co‑op Translator es una herramienta de línea de comandos en Python y un flujo de trabajo de GitHub Actions que traduce archivos Markdown, notebooks de Jupyter y texto en imágenes a varios idiomas. Organiza las salidas en carpetas específicas por idioma y mantiene las traducciones sincronizadas con el contenido original. El proyecto está estructurado como una librería gestionada con Poetry con puntos de entrada CLI.

### Descripción de la arquitectura

- Los puntos de entrada CLI (`translate`, `migrate-links`, `evaluate`) invocan una CLI unificada que distribuye a los flujos de traducción, migración de enlaces y evaluación.
- El cargador de configuración lee `.env` y detecta automáticamente el proveedor de LLM (Azure OpenAI u OpenAI) y, si se solicita, el proveedor de visión (Azure AI Service) para la extracción de texto de imágenes.
- El núcleo de traducción gestiona Markdown y notebooks; la canalización de visión extrae texto de imágenes cuando se usa `-img`.
- Las salidas se organizan en `translations/<lang>/` para texto y `translated_images/` para imágenes, preservando la estructura original.

### Tecnologías y frameworks clave

- Python 3.10–3.12, Poetry para empaquetado
- CLI: `click`
- SDKs de LLM/IA: Azure OpenAI, OpenAI
- Visión: Azure AI Service (Computer Vision)
- HTTP y datos: `httpx`, `pydantic`
- Imágenes: `pillow`, `opencv-python`, `matplotlib`
- Herramientas: `pytest`, `black`, `ruff`

## Comandos de configuración

### Requisitos previos

- Python 3.10–3.12
- Suscripción de Azure (opcional, para servicios de Azure AI)
- Acceso a Internet para APIs de LLM/Visión (por ejemplo, Azure OpenAI/OpenAI, Azure AI Vision)

### Opción A: Poetry (recomendado)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Opción B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## Uso para usuarios finales

### Docker (imagen publicada)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Notas:
- El punto de entrada predeterminado es `translate`. Sobrescribe con `--entrypoint migrate-links` para migración de enlaces.
- Asegúrate de que la visibilidad del paquete GHCR sea Pública para descargas anónimas.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Configuración del entorno

Crea un archivo `.env` en la raíz del repositorio y proporciona credenciales/endpoints para el modelo de lenguaje elegido y (opcionalmente) el servicio de visión. Para la configuración específica de cada proveedor, consulta `getting_started/set-up-azure-ai.md`.

### Variables de entorno requeridas

Debe configurarse al menos un proveedor de LLM. Para traducción de imágenes, también debe configurarse Azure AI Service.

- Azure OpenAI (traducción de texto):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (alternativa para traducción de texto):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (opcional)
  - `OPENAI_CHAT_MODEL_ID` (requerido al usar el proveedor OpenAI)
  - `OPENAI_BASE_URL` (opcional; por defecto `https://api.openai.com/v1`)

- Azure AI Service para extracción de texto en imágenes (requerido al usar `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (preferido) o el legado `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Ejemplo de fragmento `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Notas:

- La herramienta detecta automáticamente el proveedor de LLM disponible; configura Azure OpenAI u OpenAI.
- La traducción de imágenes requiere tanto `AZURE_AI_SERVICE_API_KEY` como `AZURE_AI_SERVICE_ENDPOINT`.
- La CLI mostrará un error claro si faltan variables requeridas.

## Flujo de trabajo de desarrollo

- El código fuente está en `src/co_op_translator`; las pruebas en `tests/`.
- CLIs principales (instalados vía entry points):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Consulta documentación adicional de uso en `getting_started/`.

## Instrucciones de pruebas

Ejecuta las pruebas desde la raíz del repositorio. Algunas pruebas pueden requerir credenciales de API; omite esas cuando sea necesario.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Cobertura opcional (requiere `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Guía de estilo de código

- Formateador: Black (configurado en `pyproject.toml`, longitud de línea 88)
- Linter: Ruff (configurado en `pyproject.toml`, longitud de línea 120)
- Chequeos de tipo: mypy (configuración presente; habilita si está instalado)

Comandos:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Organiza los fuentes de Python bajo `src/`, las pruebas bajo `tests/`, y prefiere imports explícitos dentro del espacio de nombres del paquete (`co_op_translator.*`).

## Construcción y despliegue

Los artefactos de construcción se publican en `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Se soporta automatización vía GitHub Actions; consulta:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Imagen de contenedor (GHCR)

- Imagen oficial: `ghcr.io/azure/co-op-translator:<tag>`
- Etiquetas: `latest` (en main), etiquetas semánticas como `vX.Y.Z`, y una etiqueta `sha`
- Multi-arquitectura: `linux/amd64, linux/arm64` soportadas vía Buildx
- Patrón de Dockerfile: construye ruedas de dependencias en el builder (con `build-essential` y `python3-dev`) e instala desde la wheelhouse local en runtime (`pip install --no-index --find-links=/wheels`)
- Flujo de trabajo: `.github/workflows/docker-publish.yml` construye y sube a GHCR

## Consideraciones de seguridad

- Mantén las claves API y endpoints en `.env` o en el almacén de secretos de tu CI; nunca subas secretos.
- Para traducción de imágenes, se requieren claves/endpoints de Azure AI Vision; de lo contrario, omite `-img`.
- Valida cuotas/límites del proveedor al ejecutar lotes grandes de traducción.

## Guía para Pull Requests

### Antes de enviar

1. **Prueba tus cambios:**
   - Ejecuta completamente los notebooks afectados
   - Verifica que todas las celdas se ejecuten sin errores
   - Revisa que las salidas sean apropiadas

2. **Actualizaciones de documentación:**
   - Actualiza `README.md` si agregas nuevos conceptos
   - Añade comentarios en notebooks para código complejo
   - Asegúrate de que las celdas markdown expliquen el propósito

3. **Cambios de archivos:**
   - Evita subir archivos `.env` (usa `.env.example`)
   - No subas directorios `venv/` o `__pycache__/`
   - Mantén las salidas de notebooks cuando demuestren conceptos
   - Elimina archivos temporales y notebooks de respaldo (`*-backup.ipynb`)

4. **Estilo y formato:**
   - Sigue las guías de estilo y formato
   - Ejecuta `poetry run black .` y `poetry run ruff check .` para revisar estilo y formato

5. **Añade/actualiza pruebas y ayuda de CLI:**
   - Añade o actualiza pruebas al cambiar comportamiento
   - Mantén la ayuda de CLI consistente con los cambios


### Mensaje de commit y estrategia de merge

Usamos Squash and Merge por defecto. El mensaje final del squash commit debe seguir:

```bash
<type>: <description> (#<PR number>)
```

Tipos permitidos:
- `Docs` — actualizaciones de documentación
- `Build` — sistema de construcción, dependencias, configuración/CI
- `Core` — funcionalidad y características principales (por ejemplo, `src/co_op_translator/core`)

Ejemplos:
- `Docs: Actualizar instrucciones de instalación para mayor claridad (#50)`
- `Core: Mejorar el manejo de traducción de imágenes (#60)`

Notas:
- Los títulos de PR suelen tener prefijo automático según las etiquetas; verifica que el prefijo generado sea correcto.

### Formato del título del PR

Usa títulos claros y concisos. Prefiere la misma estructura que el commit squash final:
- `Docs: Actualizar instrucciones de instalación para mayor claridad`
- `Core: Mejorar el manejo de traducción de imágenes`

## Depuración y solución de problemas

- Problemas comunes y soluciones: `getting_started/troubleshooting.md`
- Idiomas soportados y notas (incluyendo fuentes/problemas conocidos): `getting_started/supported-languages.md`
- Para problemas de enlaces en notebooks, vuelve a ejecutar: `migrate-links -l "all" -y`

## Notas para agentes

- Prefiere Poetry para entornos reproducibles; de lo contrario, usa `requirements.txt`.
- Al invocar CLIs en CI, proporciona los secretos requeridos vía variables de entorno o inyección de `.env`.
- Para consumidores en monorepo, este repositorio actúa como un paquete independiente; no se requiere coordinación de sub-paquetes.

- Guía multi-arquitectura: mantén `linux/arm64` cuando usuarios ARM (Apple Silicon/servidores ARM) sean un objetivo; de lo contrario, solo `linux/amd64` es aceptable por simplicidad.
- Indica a los usuarios el inicio rápido con Docker en `README.md` si prefieren uso en contenedor; incluye variantes Bash y PowerShell por diferencias en comillas.

---

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.