# GitHub Actions

Usa GitHub Actions cuando quieras que un repositorio traduzca automáticamente la documentación modificada y abra una pull request con los resultados generados.

Comienza con la configuración estándar de `GITHUB_TOKEN`, incluso para repositorios de organización cuando la política lo permita. Consulta [Configuración de la App de GitHub](#github-app-setup) cuando tu organización requiera una identidad de App o necesites ejecuciones automáticas de flujos de trabajo posteriores.

**Ediciones humanas:** estos flujos de trabajo retraducen los archivos fuente modificados por completo y pueden sobrescribir la redacción editada en sus traducciones. Revisa cada PR antes de fusionarla. La preservación a nivel de bloque de Markdown de las ediciones aceptadas requiere una integración personalizada con el [proveedor de estado de traducción de la API de Python](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Tu primera pull request de traducción del README

Comienza con un `README.md` raíz y un idioma objetivo. Este flujo de trabajo traduce solo Markdown, por lo que Azure AI Vision no es necesario.

1. Copia [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([ver la plantilla en GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) a `.github/workflows/translate-readme.yml` en el repositorio que quieras traducir, y haz commit en la rama predeterminada de ese repositorio. La plantilla usa la Action raíz en `Azure/co-op-translator@main`, que instala la CLI desde la misma referencia de origen. Fija un commit revisado para ejecuciones reproducibles.
2. Abre **Actions > Translate README > Run workflow**, elige un idioma y deja marcada la opción **Preview only**. Revisa la estimación de tokens en el paso de vista previa. La vista previa no llama a proveedores de modelos, no escribe traducciones ni crea una PR.
3. Añade los secretos para un [proveedor de texto](#prerequisites), y habilita **Permitir que GitHub Actions cree y apruebe solicitudes de extracción** en **Configuración > Acciones > General**. La plantilla solicita `contents: write` y `pull-requests: write` para su job; no necesitas cambiar los permisos predeterminados para cada flujo de trabajo. Si la política de la organización bloquea estos permisos o esta configuración, consulta con un administrador sobre una [App de GitHub](#github-app-setup) aprobada.
4. Ejecuta el flujo de trabajo de nuevo con **Preview only** sin marcar. Realiza la vista previa, traduce, ejecuta `co-op-review --readme-only` y crea o actualiza una PR de traducción solo después de que la traducción y la revisión tengan éxito. El resumen del flujo de trabajo enlaza a la PR.
5. Revisa la redacción y los cambios de archivos en la PR, y luego fusiónala cuando estés listo. El flujo de trabajo no fusiona automáticamente.

La PR contiene solo `translations/<language>/README.md` y su archivo de metadatos de idioma. El README fuente permanece sin cambios, y los enlaces a otros documentos siguen apuntando a los documentos fuente. El cuerpo de la PR lista los archivos cambiados y los resultados de la revisión estructural. Si la traducción o la revisión fallan, inspecciona el resumen del flujo de trabajo y los registros del paso fallido; no se crea ninguna PR. Si no hay cambios, no se necesita una nueva PR.

**Nota sobre organización y CI:** Una App de GitHub es opcional, no un requisito de la propiedad de la organización. Con `GITHUB_TOKEN`, los flujos de trabajo de pull request para abrir, actualizar o reabrir una PR requieren que un usuario con acceso de escritura seleccione **Approve workflows to run**. Los flujos de trabajo por push no se activan con este token. Para CI posterior sin supervisión, consulta [Configuración de la App de GitHub](#github-app-setup) y las [reglas de activación de flujos de trabajo](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) de GitHub.

## Requisitos previos

Antes de crear el flujo de trabajo, configura los secretos del servicio de IA que tu ejecución de traducción necesite.

La traducción de texto requiere un proveedor de modelos de lenguaje:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

La traducción de imágenes requiere además Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Consulta [Configuration](configuration.md) y [Azure AI Setup](azure-ai-setup.md) para detalles de configuración local.

## Configuración estándar

Después de probar el flujo de trabajo para el README, utiliza esta configuración para traducir los archivos Markdown de un repositorio a varios idiomas. Ejecuta una revisión de Markdown antes de abrir una PR y no requiere Azure AI Vision.

### Paso 1: Agregar secretos del repositorio

En tu repositorio de destino, abre **Settings** > **Secrets and variables** > **Actions**, luego agrega los secretos del proveedor que usará tu flujo de trabajo.

![Seleccionar secretos de Actions](../../assets/github-actions/select-setting-action.png)

### Paso 2: Habilitar permisos del flujo de trabajo

Abre **Settings** > **Actions** > **General**.

Bajo **Workflow permissions**:

1. Habilita **Permitir que GitHub Actions cree y apruebe solicitudes de extracción**.
2. Guarda la configuración.

El job abajo solicita `contents: write` y `pull-requests: write` explícitamente. Mantén sin cambios los permisos predeterminados de flujos de trabajo del repositorio. Si la política de la organización bloquea la creación de PR, pregunta a un administrador sobre una [App de GitHub](#github-app-setup) aprobada.

### Paso 3: Agregar el flujo de trabajo

Crea `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

Cambia `TARGET_LANGUAGES` a los idiomas que tu proyecto necesite. La revisión usa la API de Python para verificar solo Markdown, coincidiendo con el paso de traducción. Un error de traducción o de revisión detiene el job antes de la creación de la PR. El flujo de trabajo no fusiona la PR automáticamente. Para repositorios grandes, añade un filtro `paths:` bajo `on.push` para que el flujo de trabajo solo se ejecute cuando cambie la documentación.

### Opcional: notebooks e imágenes

Para notebooks, añade `-nb` al comando de traducción y establece `notebook=True` en el paso de revisión. Para texto en imágenes, configura los dos [secretos de Azure AI Vision](#prerequisites), pásalos en el `env` del paso de traducción, añade `-img` al comando y agrega `translated_images/` a `add-paths` del paso de PR. Revisa las imágenes traducidas visualmente; la revisión determinista no certifica la exactitud del texto de las imágenes ni la precisión lingüística.

## Configuración de la App de GitHub

Usa una App de GitHub aprobada cuando tu organización requiera una identidad de App, o cuando la PR generada necesite activar CI posterior sin el paso de aprobación de `GITHUB_TOKEN`. Una App no elude la política de la organización; los administradores siguen controlando su instalación y permisos.

### Paso 1: Crear o instalar una App de GitHub

Usa una App proporcionada por la organización cuando esté disponible, o crea una con acceso de lectura/escritura a **Contents** y **Pull requests**. Instálala en el repositorio de destino con la aprobación de la organización si se requiere.

Anota:

- ID de la App
- Contenido de la clave privada

Guárdalos como secretos del repositorio:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Paso 2: Generar un token de App

Añade este paso inmediatamente antes del paso existente de pull request. Para la plantilla del README, usa la misma condición de éxito para que las vistas previas y las traducciones fallidas no soliciten un token de App:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

Luego cambia solo la entrada `token` del paso de pull request existente a `${{ steps.generate_token.outputs.token }}`. Mantén su condición de éxito, rama, cuerpo de la PR y `add-paths` sin cambios. El token está limitado al repositorio actual por defecto. Al adaptar la configuración estándar en lugar de la plantilla del README, omite el `if` anterior: ese flujo de trabajo usa la condición de éxito predeterminada, por lo que la creación del token y la creación de la PR se ejecutan solo después de que la traducción y la revisión tengan éxito.

Consulta la [Action create-github-app-token](https://github.com/actions/create-github-app-token/tree/v2) oficial para la instalación y permisos del token.

## Límites de los runners

Los runners hospedados por GitHub tienen una duración máxima por job. Los repositorios grandes o muchos idiomas objetivo pueden exceder ese límite.

Para cargas de trabajo de traducción grandes:

- Traduce menos idiomas por ejecución.
- Usa flags de contenido como `-md`, `-nb` o `-img`.
- Usa un runner auto-hospedado cuando el tamaño del repositorio o la latencia del modelo haga que los runners hospedados sean poco fiables.

## Revisión en CI

Usa `co-op-review` cuando una pull request deba validar las traducciones generadas sin llamar a proveedores LLM o Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` es un comando de revisión determinista en beta. Sus comprobaciones y el esquema de salida pueden evolucionar, pero está diseñado para ser seguro para CI porque no escribe archivos ni llama a proveedores de modelos.