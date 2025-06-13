<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-06-12T19:21:09+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "es"
}
-->
# Uso de la acción Co-op Translator en GitHub (Configuración pública)

**Público objetivo:** Esta guía está dirigida a usuarios en la mayoría de repositorios públicos o privados donde los permisos estándar de GitHub Actions son suficientes. Utiliza el `GITHUB_TOKEN` integrado.

Automatiza la traducción de la documentación de tu repositorio de forma sencilla usando la acción Co-op Translator de GitHub. Esta guía te muestra cómo configurar la acción para crear automáticamente pull requests con traducciones actualizadas cada vez que cambien tus archivos Markdown fuente o imágenes.

> [!IMPORTANT]
>
> **Elección de la guía adecuada:**
>
> Esta guía detalla la **configuración más sencilla usando el `GITHUB_TOKEN` estándar**. Este es el método recomendado para la mayoría de usuarios, ya que no requiere gestionar claves privadas sensibles de la GitHub App.
>

## Requisitos previos

Antes de configurar la acción de GitHub, asegúrate de tener listas las credenciales necesarias del servicio de IA.

**1. Obligatorio: Credenciales del modelo de lenguaje de IA**  
Necesitas credenciales para al menos un modelo de lenguaje soportado:

- **Azure OpenAI**: Requiere Endpoint, clave API, nombres de modelo/despliegue y versión de API.  
- **OpenAI**: Requiere clave API, (Opcional: ID de organización, URL base, ID del modelo).  
- Consulta [Modelos y servicios soportados](../../../../README.md) para más detalles.

**2. Opcional: Credenciales de IA Vision (para traducción de imágenes)**

- Solo necesario si quieres traducir texto dentro de imágenes.  
- **Azure AI Vision**: Requiere Endpoint y clave de suscripción.  
- Si no se proporcionan, la acción usa por defecto el [modo solo Markdown](../markdown-only-mode.md).

## Configuración

Sigue estos pasos para configurar la acción Co-op Translator en tu repositorio usando el `GITHUB_TOKEN` estándar.

### Paso 1: Entender la autenticación (usando `GITHUB_TOKEN`)

Este flujo de trabajo usa el `GITHUB_TOKEN` integrado que proporciona GitHub Actions. Este token otorga automáticamente permisos al flujo para interactuar con tu repositorio según la configuración realizada en el **Paso 3**.

### Paso 2: Configurar los secretos del repositorio

Solo necesitas añadir las **credenciales de tu servicio de IA** como secretos cifrados en la configuración de tu repositorio.

1.  Navega al repositorio de GitHub destino.  
2.  Ve a **Settings** > **Secrets and variables** > **Actions**.  
3.  En **Repository secrets**, haz clic en **New repository secret** para cada secreto de servicio de IA requerido que se indica a continuación.

    ![Select setting action](../../../../translated_images/select-setting-action.32e2394813d09dc148494f34daea40724f24ff406de889f26cbbbf05f98ed621.es.png) *(Referencia de imagen: muestra dónde agregar secretos)*

**Secretos requeridos para servicios de IA (agrega TODOS los que correspondan según tus requisitos):**

| Nombre del secreto                  | Descripción                               | Fuente del valor                  |
| :-------------------------------- | :-------------------------------------- | :------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`                  | Clave para Azure AI Service (Computer Vision)  | Tu Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`                  | Endpoint para Azure AI Service (Computer Vision) | Tu Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`                  | Clave para el servicio Azure OpenAI              | Tu Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`                  | Endpoint para el servicio Azure OpenAI            | Tu Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`                  | Nombre de tu modelo Azure OpenAI                   | Tu Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`                 | Nombre de tu despliegue Azure OpenAI               | Tu Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`                 | Versión de API para Azure OpenAI                    | Tu Azure AI Foundry               |
| `OPENAI_API_KEY`                 | Clave API para OpenAI                               | Tu plataforma OpenAI             |
| `OPENAI_ORG_ID`                 | ID de organización OpenAI (Opcional)               | Tu plataforma OpenAI             |
| `OPENAI_CHAT_MODEL_ID`                 | ID de modelo específico OpenAI (Opcional)          | Tu plataforma OpenAI             |
| `OPENAI_BASE_URL`                 | URL base personalizada de la API OpenAI (Opcional) | Tu plataforma OpenAI             |

### Paso 3: Configurar permisos del flujo de trabajo

La acción de GitHub necesita permisos otorgados mediante el `GITHUB_TOKEN` para hacer checkout del código y crear pull requests.

1.  En tu repositorio, ve a **Settings** > **Actions** > **General**.  
2.  Desplázate hasta la sección **Workflow permissions**.  
3.  Selecciona **Read and write permissions**. Esto otorga al `GITHUB_TOKEN` los permisos necesarios de `contents: write` y `pull-requests: write` para este flujo.  
4.  Asegúrate de que la casilla **Allow GitHub Actions to create and approve pull requests** esté **marcada**.  
5.  Haz clic en **Save**.

![Permission setting](../../../../translated_images/permission-setting.cb1f57fdb5194f0743b1f6932f221e404ae2928ee88d77f1de39aba46fbf774a.es.png)

### Paso 4: Crear el archivo del flujo de trabajo

Finalmente, crea el archivo YAML que define el flujo automatizado usando `GITHUB_TOKEN`.

1.  En el directorio raíz de tu repositorio, crea el directorio `.github/workflows/` si no existe.  
2.  Dentro de `.github/workflows/`, crea un archivo llamado `co-op-translator.yml`.  
3.  Pega el siguiente contenido en `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```  
4.  **Personaliza el flujo de trabajo:**  
  - **[!IMPORTANT] Idiomas objetivo:** En el paso `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` modifica los idiomas si es necesario.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.