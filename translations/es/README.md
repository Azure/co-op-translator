<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "18318279bb851dc2c709bfc6a26f6e1d",
  "translation_date": "2025-05-07T14:03:19+00:00",
  "source_file": "README.md",
  "language_code": "es"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: Automatiza la Traducción de Documentación Educativa sin Esfuerzo

_Automatiza fácilmente la traducción de tu documentación a múltiples idiomas para alcanzar una audiencia global._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Soporte de Idiomas Potenciado por Co-op Translator

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](./README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **Automatización Potente**: ¡Ahora con soporte para GitHub Actions! Traduce automáticamente tu documentación cuando se realicen cambios en tu repositorio, manteniendo todo actualizado sin esfuerzo. [Más información](../..).

## Modelos y Servicios Soportados

| Tipo                  | Nombre                          |
|-----------------------|--------------------------------|
| Language Model        | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Computer Vision       | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> Si un servicio de visión por computadora no está disponible, el co-op translator cambiará al [modo solo Markdown](./getting_started/markdown-only-mode.md).

## Resumen: Optimiza la Traducción de tu Contenido Educativo

Las barreras del idioma dificultan significativamente el acceso a recursos educativos valiosos y conocimientos técnicos para estudiantes y desarrolladores en todo el mundo. Esto limita la participación y ralentiza el ritmo de la innovación y el aprendizaje global.

**Co-op Translator** nació de la necesidad de mejorar el proceso manual e ineficiente de traducción para la propia serie educativa a gran escala de Microsoft (como las guías "For Beginners"). Se ha convertido en una herramienta potente y fácil de usar, diseñada para derribar estas barreras para todos. Al ofrecer traducciones automáticas de alta calidad mediante CLI y GitHub Actions, Co-op Translator permite a educadores, estudiantes, investigadores y desarrolladores de todo el mundo compartir y acceder al conocimiento sin limitaciones de idioma.

Mira cómo Co-op Translator organiza el contenido educativo traducido:

![Ejemplo](../../imgs/translation-ex.png)

Los archivos Markdown y el texto de las imágenes se traducen automáticamente y se organizan ordenadamente en carpetas específicas por idioma.

**¡Accede globalmente a tu contenido educativo con Co-op Translator hoy mismo!**

## Apoyando el Acceso Global a los Recursos de Aprendizaje de Microsoft

Co-op Translator ayuda a cerrar la brecha del idioma para iniciativas educativas clave de Microsoft, automatizando el proceso de traducción para repositorios que sirven a una comunidad global de desarrolladores. Algunos ejemplos que ya usan Co-op Translator incluyen:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## Características Principales

- **Traducciones Automatizadas**: Traduce texto a múltiples idiomas sin complicaciones.
- **Integración con GitHub Actions**: Automatiza las traducciones como parte de tu pipeline CI/CD.
- **Preservación de Markdown**: Mantén la sintaxis correcta de Markdown durante la traducción.
- **Traducción de Texto en Imágenes**: Extrae y traduce el texto dentro de las imágenes.
- **Tecnología Avanzada LLM**: Utiliza modelos de lenguaje de última generación para traducciones de alta calidad.
- **Integración Sencilla**: Integra fácilmente con la configuración existente de tu proyecto.
- **Simplifica la Localización**: Optimiza el proceso de localizar tu proyecto para mercados internacionales.

## Cómo Funciona

![Arquitectura](../../imgs/architecture_241019.png)

Co-op Translator toma los archivos Markdown y las imágenes de tu carpeta de proyecto y los procesa de la siguiente manera:

1. **Extracción de Texto**: Extrae texto de archivos Markdown y, si está configurado (por ejemplo, con Azure Computer Vision), también del texto incrustado en imágenes.
1. **Traducción con IA**: Envía el texto extraído al LLM configurado (Azure OpenAI, OpenAI, etc.) para su traducción.
1. **Guardado del Resultado**: Guarda los archivos Markdown traducidos y las imágenes (con texto traducido) en carpetas específicas por idioma, preservando el formato original.

## Primeros Pasos

> [!NOTE]
> Aunque este tutorial se centra en recursos de Azure, puedes usar cualquier modelo de lenguaje soportado de la lista de [modelos y servicios soportados](../..).

Comienza rápidamente con la CLI o configura la automatización completa con GitHub Actions.

### Configuración Inicial

- [Configura Azure AI](./getting_started/set-up-azure-ai.md)

### Inicio Rápido: Línea de Comandos

Para comenzar rápido usando la línea de comandos:

1. Instala el paquete:
    ```bash
    pip install co-op-translator
    ```
2. Configura las Credenciales:
  - Crea un archivo `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` con la bandera:
    ```bash
    translate -l "ko ja fr"
    ```
    *(Reemplaza `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) en tu repositorio. No es necesaria instalación local.
- Guías:
  - [Guía de GitHub Actions (Repositorios Públicos y Secretos Estándar)](./getting_started/github-actions-guide/github-actions-guide-public.md) - Usa esta para la mayoría de repositorios públicos o personales que dependen de secretos estándar del repositorio.
  - [Guía de GitHub Actions (Repositorios de la Organización Microsoft y Configuraciones a Nivel de Org)](./getting_started/github-actions-guide/github-actions-guide-org.md) - Usa esta guía si trabajas dentro de la organización Microsoft en GitHub o necesitas usar secretos o runners a nivel de organización.

### Solución de Problemas y Consejos

- [Guía de Solución de Problemas](./getting_started/troubleshooting.md)

### Recursos Adicionales

- [Referencia de Comandos](./getting_started/command-reference.md): Guía detallada de todos los comandos y opciones disponibles.
- [Configuración de Soporte Multilenguaje](./getting_started/multi-language-support.md): Cómo añadir una tabla con enlaces a las versiones traducidas en tu README.
- [Idiomas Soportados](./getting_started/supported-languages.md): Consulta la lista de idiomas soportados e instrucciones para agregar nuevos.
- [Modo Solo Markdown](./getting_started/markdown-only-mode.md): Cómo traducir solo el texto, sin traducción de imágenes.

## Presentaciones en Video

Conoce más sobre Co-op Translator a través de nuestras presentaciones _(Haz clic en la imagen para ver en YouTube)_:

- **Open at Microsoft**: Una introducción breve de 18 minutos y guía rápida sobre cómo usar Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: Una guía detallada de una hora paso a paso que cubre desde qué es Co-op Translator, cómo configurarlo y usarlo efectivamente, hasta una demo en vivo mostrando sus capacidades en acción.

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Apóyanos y Fomenta el Aprendizaje Global

¡Únete a nosotros en la revolución para compartir contenido educativo a nivel mundial! Dale una ⭐ a [Co-op Translator](https://github.com/azure/co-op-translator) en GitHub y apoya nuestra misión de eliminar las barreras del idioma en el aprendizaje y la tecnología. ¡Tu interés y contribuciones tienen un impacto significativo! Siempre son bienvenidas las contribuciones de código y sugerencias de funciones.

## Contribuciones

Este proyecto acepta contribuciones y sugerencias. ¿Interesado en contribuir a Azure Co-op Translator? Por favor, consulta nuestro [CONTRIBUTING.md](./CONTRIBUTING.md) para conocer las pautas sobre cómo puedes ayudar a que Co-op Translator sea más accesible.

## Colaboradores

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Código de Conducta

Este proyecto ha adoptado el [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Para más información consulta las [Preguntas Frecuentes sobre el Código de Conducta](https://opensource.microsoft.com/codeofconduct/faq/) o contacta a [opencode@microsoft.com](mailto:opencode@microsoft.com) con cualquier pregunta o comentario adicional.

## IA Responsable

Microsoft se compromete a ayudar a nuestros clientes a usar nuestros productos de IA de manera responsable, compartiendo nuestras experiencias y construyendo asociaciones basadas en la confianza mediante herramientas como Transparency Notes e Impact Assessments. Muchos de estos recursos están disponibles en [https://aka.ms/RAI](https://aka.ms/RAI).
El enfoque de Microsoft hacia la IA responsable se basa en nuestros principios de IA: equidad, confiabilidad y seguridad, privacidad y protección, inclusión, transparencia y responsabilidad.
Los modelos a gran escala de lenguaje natural, imagen y voz, como los que se utilizan en este ejemplo, pueden comportarse de manera injusta, poco fiable u ofensiva, lo que a su vez puede causar daños. Por favor, consulta la [nota de transparencia del servicio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para informarte sobre los riesgos y limitaciones.

El enfoque recomendado para mitigar estos riesgos es incluir un sistema de seguridad en tu arquitectura que pueda detectar y prevenir comportamientos dañinos. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) proporciona una capa independiente de protección, capaz de detectar contenido dañino generado por usuarios y por IA en aplicaciones y servicios. Azure AI Content Safety incluye APIs de texto e imagen que te permiten detectar material dañino. También contamos con un Content Safety Studio interactivo que te permite ver, explorar y probar código de ejemplo para detectar contenido dañino en diferentes modalidades. La siguiente [documentación de inicio rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) te guía para hacer solicitudes al servicio.

Otro aspecto a tener en cuenta es el rendimiento general de la aplicación. En aplicaciones multimodales y con múltiples modelos, consideramos que el rendimiento significa que el sistema funciona como tú y tus usuarios esperan, incluyendo no generar resultados dañinos. Es importante evaluar el rendimiento de tu aplicación general utilizando [métricas de calidad de generación, riesgo y seguridad](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puedes evaluar tu aplicación de IA en tu entorno de desarrollo usando el [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Ya sea con un conjunto de datos de prueba o un objetivo, las generaciones de tu aplicación de IA generativa se miden cuantitativamente con evaluadores incorporados o evaluadores personalizados que elijas. Para comenzar con el prompt flow sdk y evaluar tu sistema, puedes seguir la [guía de inicio rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una vez que ejecutes una evaluación, puedes [visualizar los resultados en Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas Registradas

Este proyecto puede contener marcas registradas o logotipos de proyectos, productos o servicios. El uso autorizado de las marcas o logotipos de Microsoft está sujeto a y debe seguir las [Directrices de Marca y Marcas Registradas de Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). El uso de las marcas o logotipos de Microsoft en versiones modificadas de este proyecto no debe causar confusión ni implicar patrocinio de Microsoft. Cualquier uso de marcas o logotipos de terceros está sujeto a las políticas de esos terceros.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.