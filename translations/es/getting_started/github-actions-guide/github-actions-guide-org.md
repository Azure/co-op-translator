<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fac847815936ef6e6c8bfde6d191571",
  "translation_date": "2025-10-15T02:11:23+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-org.md",
  "language_code": "es"
}
-->
# Uso de la Acción de GitHub Co-op Translator (Guía para Organizaciones)

**Público objetivo:** Esta guía está dirigida a **usuarios internos de Microsoft** o **equipos que tengan acceso a las credenciales necesarias para la aplicación preconstruida Co-op Translator de GitHub** o que puedan crear su propia aplicación personalizada de GitHub.

Automatiza la traducción de la documentación de tu repositorio fácilmente usando la Acción de GitHub Co-op Translator. Esta guía te explica cómo configurar la acción para que cree automáticamente pull requests con traducciones actualizadas cada vez que cambien tus archivos Markdown fuente o imágenes.

> [!IMPORTANT]
> 
> **Eligiendo la guía adecuada:**
>
> Esta guía detalla la configuración usando un **ID de App de GitHub y una clave privada**. Normalmente necesitas este método de "Guía para Organizaciones" si: **`GITHUB_TOKEN` tiene permisos restringidos:** La configuración de tu organización o repositorio restringe los permisos por defecto otorgados al `GITHUB_TOKEN` estándar. Específicamente, si el `GITHUB_TOKEN` no tiene los permisos de `write` necesarios (como `contents: write` o `pull-requests: write`), el flujo de trabajo de la [Guía Pública](./github-actions-guide-public.md) fallará por permisos insuficientes. Usar una App de GitHub dedicada con permisos explícitos evita esta limitación.
>
> **Si lo anterior no aplica a tu caso:**
>
> Si el `GITHUB_TOKEN` estándar tiene permisos suficientes en tu repositorio (es decir, no tienes restricciones organizacionales), por favor usa la **[Guía Pública usando GITHUB_TOKEN](./github-actions-guide-public.md)**. La guía pública no requiere obtener ni gestionar IDs de App ni claves privadas, y se basa únicamente en el `GITHUB_TOKEN` estándar y los permisos del repositorio.

## Requisitos previos

Antes de configurar la Acción de GitHub, asegúrate de tener listas las credenciales necesarias del servicio de IA.

**1. Requerido: Credenciales del modelo de lenguaje de IA**
Necesitas credenciales para al menos uno de los modelos de lenguaje soportados:

- **Azure OpenAI**: Requiere Endpoint, API Key, nombres de modelo/despliegue, versión de la API.
- **OpenAI**: Requiere API Key, (Opcional: Org ID, Base URL, Model ID).
- Consulta [Modelos y servicios soportados](../../../../README.md) para más detalles.
- Guía de configuración: [Configurar Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. Opcional: Credenciales de Computer Vision (para traducción de imágenes)**

- Solo es necesario si necesitas traducir texto dentro de imágenes.
- **Azure Computer Vision**: Requiere Endpoint y Subscription Key.
- Si no se proporciona, la acción funcionará en [modo solo Markdown](../markdown-only-mode.md).
- Guía de configuración: [Configurar Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## Configuración

Sigue estos pasos para configurar la Acción de GitHub Co-op Translator en tu repositorio:

### Paso 1: Instala y configura la autenticación de la App de GitHub

El flujo de trabajo utiliza la autenticación de App de GitHub para interactuar de forma segura con tu repositorio (por ejemplo, crear pull requests) en tu nombre. Elige una opción:

#### **Opción A: Instalar la App preconstruida Co-op Translator (para uso interno de Microsoft)**

1. Ve a la página de la [App de GitHub Co-op Translator](https://github.com/apps/co-op-translator).

1. Selecciona **Install** y elige la cuenta u organización donde está tu repositorio objetivo.

    ![Instalar app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.es.png)

1. Elige **Only select repositories** y selecciona tu repositorio objetivo (por ejemplo, `PhiCookBook`). Haz clic en **Install**. Es posible que debas autenticarte.

    ![Instalar autorizar](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.es.png)

1. **Obtén las credenciales de la App (proceso interno requerido):** Para permitir que el flujo de trabajo se autentique como la app, necesitas dos datos proporcionados por el equipo de Co-op Translator:
  - **App ID:** El identificador único de la app Co-op Translator. El App ID es: `1164076`.
  - **Private Key:** Debes obtener el **contenido completo** del archivo de clave privada `.pem` del contacto responsable. **Trata esta clave como una contraseña y mantenla segura.**

1. Continúa con el Paso 2.

#### **Opción B: Usa tu propia App personalizada de GitHub**

- Si lo prefieres, puedes crear y configurar tu propia App de GitHub. Asegúrate de que tenga acceso de lectura y escritura a Contents y Pull requests. Necesitarás su App ID y una clave privada generada.

### Paso 2: Configura los secretos del repositorio

Debes agregar las credenciales de la App de GitHub y las credenciales de tu servicio de IA como secretos cifrados en la configuración de tu repositorio.

1. Ve a tu repositorio objetivo en GitHub (por ejemplo, `PhiCookBook`).

1. Ve a **Settings** > **Secrets and variables** > **Actions**.

1. En **Repository secrets**, haz clic en **New repository secret** para cada secreto de la lista a continuación.

   ![Seleccionar configuración de acción](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.es.png)

**Secretos requeridos (para autenticación de la App de GitHub):**

| Nombre del secreto   | Descripción                                      | Fuente del valor                                 |
| :------------------- | :----------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | El App ID de la App de GitHub (del Paso 1).      | Configuración de la App de GitHub                |
| `GH_APP_PRIVATE_KEY` | El **contenido completo** del archivo `.pem` descargado. | Archivo `.pem` (del Paso 1)                  |

**Secretos del servicio de IA (agrega TODOS los que apliquen según tus requisitos):**

| Nombre del secreto                    | Descripción                                   | Fuente del valor                  |
| :------------------------------------ | :-------------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Clave para Azure AI Service (Computer Vision) | Azure AI Foundry                  |
| `AZURE_AI_SERVICE_ENDPOINT`           | Endpoint para Azure AI Service (Computer Vision) | Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`                | Clave para el servicio Azure OpenAI           | Azure AI Foundry                  |
| `AZURE_OPENAI_ENDPOINT`               | Endpoint para el servicio Azure OpenAI        | Azure AI Foundry                  |
| `AZURE_OPENAI_MODEL_NAME`             | Nombre de tu modelo de Azure OpenAI           | Azure AI Foundry                  |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`   | Nombre de despliegue de Azure OpenAI          | Azure AI Foundry                  |
| `AZURE_OPENAI_API_VERSION`            | Versión de la API de Azure OpenAI             | Azure AI Foundry                  |
| `OPENAI_API_KEY`                      | API Key para OpenAI                           | OpenAI Platform                   |
| `OPENAI_ORG_ID`                       | ID de organización de OpenAI                  | OpenAI Platform                   |
| `OPENAI_CHAT_MODEL_ID`                | ID específico del modelo de OpenAI            | OpenAI Platform                   |
| `OPENAI_BASE_URL`                     | Base URL personalizada de la API de OpenAI    | OpenAI Platform                   |

![Ingresar nombre de variable de entorno](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.es.png)

### Paso 3: Crea el archivo de flujo de trabajo

Por último, crea el archivo YAML que define el flujo de trabajo automatizado.

1. En el directorio raíz de tu repositorio, crea el directorio `.github/workflows/` si no existe.

1. Dentro de `.github/workflows/`, crea un archivo llamado `co-op-translator.yml`.

1. Pega el siguiente contenido en co-op-translator.yml.

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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
  - **[!IMPORTANT] Idiomas objetivo:** En el paso `Run Co-op Translator`, **DEBES revisar y modificar la lista de códigos de idioma** dentro del comando `translate -l "..." -y` para que coincida con los requisitos de tu proyecto. La lista de ejemplo (`ar de es...`) debe ser reemplazada o ajustada.
  - **Disparador (`on:`):** El disparador actual se ejecuta en cada push a `main`. Para repositorios grandes, considera agregar un filtro `paths:` (ver ejemplo comentado en el YAML) para ejecutar el flujo de trabajo solo cuando cambien archivos relevantes (por ejemplo, documentación fuente), ahorrando minutos de ejecución.
  - **Detalles del PR:** Personaliza el `commit-message`, `title`, `body`, nombre de la `branch` y `labels` en el paso `Create Pull Request` si lo necesitas.

## Gestión y renovación de credenciales

- **Seguridad:** Guarda siempre las credenciales sensibles (API keys, claves privadas) como secretos de GitHub Actions. Nunca las expongas en tu archivo de flujo de trabajo ni en el código del repositorio.
- **[!IMPORTANT] Renovación de claves (usuarios internos de Microsoft):** Ten en cuenta que la clave de Azure OpenAI utilizada dentro de Microsoft puede tener una política de renovación obligatoria (por ejemplo, cada 5 meses). Asegúrate de actualizar los secretos correspondientes de GitHub (`AZURE_OPENAI_...`) **antes de que expiren** para evitar fallos en el flujo de trabajo.

## Ejecución del flujo de trabajo

> [!WARNING]  
> **Límite de tiempo de los runners alojados por GitHub:**  
> Los runners alojados por GitHub como `ubuntu-latest` tienen un **límite máximo de ejecución de 6 horas**.  
> Para repositorios de documentación grandes, si el proceso de traducción supera las 6 horas, el flujo de trabajo se terminará automáticamente.  
> Para evitar esto, considera:  
> - Usar un **runner autohospedado** (sin límite de tiempo)  
> - Reducir el número de idiomas objetivo por ejecución

Una vez que el archivo `co-op-translator.yml` se fusione en tu rama principal (o la rama especificada en el disparador `on:`), el flujo de trabajo se ejecutará automáticamente cada vez que se hagan cambios en esa rama (y coincidan con el filtro `paths`, si está configurado).

Si se generan o actualizan traducciones, la acción creará automáticamente un Pull Request con los cambios, listo para tu revisión y fusión.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.