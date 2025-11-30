<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T02:09:54+00:00",
  "source_file": "README.md",
  "language_code": "es"
}
-->
# Co-op Translator

_Automatiza fácilmente la traducción de tu contenido educativo en GitHub a varios idiomas para llegar a una audiencia global._

[![Paquete de Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licencia: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Descargas](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Descargas](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Contenedor: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Estilo de código: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Colaboradores de GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Issues de GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull-requests de GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Soporte multilingüe

#### Compatible con [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengalí](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmano (Myanmar)](../my/README.md) | [Chino (Simplificado)](../zh/README.md) | [Chino (Tradicional, Hong Kong)](../hk/README.md) | [Chino (Tradicional, Macao)](../mo/README.md) | [Chino (Tradicional, Taiwán)](../tw/README.md) | [Croata](../hr/README.md) | [Checo](../cs/README.md) | [Danés](../da/README.md) | [Neerlandés](../nl/README.md) | [Estonio](../et/README.md) | [Finlandés](../fi/README.md) | [Francés](../fr/README.md) | [Alemán](../de/README.md) | [Griego](../el/README.md) | [Hebreo](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonesio](../id/README.md) | [Italiano](../it/README.md) | [Japonés](../ja/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malayo](../ms/README.md) | [Maratí](../mr/README.md) | [Nepalí](../ne/README.md) | [Noruego](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polaco](../pl/README.md) | [Portugués (Brasil)](../br/README.md) | [Portugués (Portugal)](../pt/README.md) | [Punyabí (Gurmukhi)](../pa/README.md) | [Rumano](../ro/README.md) | [Ruso](../ru/README.md) | [Serbio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Español](./README.md) | [Suajili](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalo (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Tailandés](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Observadores de GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Forks de GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Estrellas de GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Discord de Microsoft Azure AI Foundry](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Abrir en GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Descripción general

**Co-op Translator** te permite traducir rápidamente tu contenido educativo en GitHub a varios idiomas, llegando a una audiencia global sin esfuerzo. Cuando actualizas tus archivos Markdown, imágenes o notebooks de Jupyter, las traducciones se sincronizan automáticamente para que tu contenido educativo en GitHub se mantenga actualizado y relevante para usuarios internacionales.

Mira cómo Co-op Translator organiza el contenido educativo traducido en GitHub:

![Ejemplo](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.es.png)

## Inicio rápido

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configuración mínima

- Crea un archivo `.env` usando la plantilla: [.env.template](../../.env.template)
- Configura un proveedor LLM (Azure OpenAI u OpenAI)
- Para traducir imágenes (`-img`), también configura Azure AI Vision
- Recomendado: Si tienes traducciones generadas por otras herramientas, límpialas primero para evitar conflictos (por ejemplo: `translations/`).
- Recomendado: Añade una sección de traducciones a tu README usando la [plantilla de idiomas para README](./README_languages_template.md)
- Consulta: [Configura Azure AI](./getting_started/set-up-azure-ai.md)

## Uso

Traduce todos los tipos compatibles:

```bash
translate -l "ko ja"
```

Solo Markdown:

```bash
translate -l "de" -md
```

Markdown + imágenes:

```bash
translate -l "pt" -md -img
```

Solo notebooks:

```bash
translate -l "zh" -nb
```

Más opciones: [Referencia de comandos](./getting_started/command-reference.md)

## Características

- Traducción automática de Markdown, notebooks e imágenes
- Mantiene las traducciones sincronizadas con los cambios en el origen
- Funciona localmente (CLI) o en CI (GitHub Actions)
- Utiliza Azure OpenAI u OpenAI; Azure AI Vision opcional para imágenes
- Conserva el formato y la estructura de Markdown

## Documentación

- [Guía de línea de comandos](./getting_started/command-line-guide/command-line-guide.md)
- [Guía de GitHub Actions (Repositorios públicos y secretos estándar)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Guía de GitHub Actions (Repositorios de la organización Microsoft y configuraciones a nivel de organización)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Idiomas compatibles](./getting_started/supported-languages.md)
- [Solución de problemas](./getting_started/troubleshooting.md)

## Apóyanos y fomenta el aprendizaje global

¡Únete a nosotros para revolucionar la forma en que se comparte el contenido educativo en todo el mundo! Dale una ⭐ a [Co-op Translator](https://github.com/azure/co-op-translator) en GitHub y apoya nuestra misión de eliminar las barreras de idioma en el aprendizaje y la tecnología. ¡Tu interés y contribuciones marcan la diferencia! Las contribuciones de código y sugerencias de nuevas funciones siempre son bienvenidas.

### Explora contenido educativo de Microsoft en tu idioma

- [AZD para principiantes](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI para principiantes](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) para principiantes](https://github.com/microsoft/mcp-for-beginners)
- [Agentes de IA para principiantes](https://github.com/microsoft/ai-agents-for-beginners)
- [IA Generativa para principiantes usando .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [IA Generativa para principiantes](https://github.com/microsoft/generative-ai-for-beginners)
- [IA Generativa para principiantes usando Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML para principiantes](https://aka.ms/ml-beginners)
- [Ciencia de datos para principiantes](https://aka.ms/datascience-beginners)
- [IA para principiantes](https://aka.ms/ai-beginners)
- [Ciberseguridad para principiantes](https://github.com/microsoft/Security-101)
- [Desarrollo web para principiantes](https://aka.ms/webdev-beginners)
- [IoT para principiantes](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Presentaciones en video

Conoce más sobre Co-op Translator a través de nuestras presentaciones _(Haz clic en la imagen para ver en YouTube.)_:

- **Open at Microsoft**: Una breve introducción de 18 minutos y guía rápida sobre cómo usar Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.es.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuir

Este proyecto da la bienvenida a contribuciones y sugerencias. ¿Te interesa contribuir a Azure Co-op Translator? Consulta nuestro [CONTRIBUTING.md](./CONTRIBUTING.md) para ver las pautas sobre cómo puedes ayudar a que Co-op Translator sea más accesible.

## Colaboradores

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Código de conducta

Este proyecto ha adoptado el [Código de conducta de Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).
Para más información, consulta las [Preguntas frecuentes sobre el código de conducta](https://opensource.microsoft.com/codeofconduct/faq/) o
contacta a [opencode@microsoft.com](mailto:opencode@microsoft.com) si tienes preguntas o comentarios adicionales.

## IA responsable

Microsoft está comprometido a ayudar a nuestros clientes a usar nuestros productos de IA de manera responsable, compartiendo nuestros aprendizajes y construyendo relaciones de confianza a través de herramientas como Transparency Notes y Impact Assessments. Muchos de estos recursos están disponibles en [https://aka.ms/RAI](https://aka.ms/RAI).
El enfoque de Microsoft hacia la IA responsable se basa en nuestros principios de equidad, confiabilidad y seguridad, privacidad y protección, inclusión, transparencia y responsabilidad.

Los modelos de lenguaje natural, imagen y voz a gran escala, como los que se usan en este ejemplo, pueden comportarse de manera injusta, poco confiable u ofensiva, lo que puede causar daños. Consulta la [nota de transparencia del servicio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para estar informado sobre riesgos y limitaciones.

La forma recomendada de mitigar estos riesgos es incluir un sistema de seguridad en tu arquitectura que pueda detectar y prevenir comportamientos dañinos. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) proporciona una capa independiente de protección, capaz de detectar contenido dañino generado por usuarios y por IA en aplicaciones y servicios. Azure AI Content Safety incluye APIs de texto e imagen que te permiten detectar material dañino. También contamos con un Content Safety Studio interactivo que te permite ver, explorar y probar ejemplos de código para detectar contenido dañino en diferentes modalidades. La siguiente [documentación de inicio rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) te guía para realizar solicitudes al servicio.
Otro aspecto a considerar es el rendimiento general de la aplicación. En aplicaciones multimodales y con múltiples modelos, consideramos que el rendimiento significa que el sistema funciona como tú y tus usuarios esperan, incluyendo no generar resultados dañinos. Es importante evaluar el rendimiento de tu aplicación en general usando [métricas de calidad de generación y de riesgo y seguridad](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puedes evaluar tu aplicación de IA en tu entorno de desarrollo usando el [SDK de prompt flow](https://microsoft.github.io/promptflow/index.html). Ya sea con un conjunto de datos de prueba o un objetivo, las generaciones de tu aplicación de IA generativa se miden cuantitativamente con evaluadores integrados o personalizados según tu elección. Para comenzar a usar el SDK de prompt flow y evaluar tu sistema, puedes seguir la [guía de inicio rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una vez que ejecutes una evaluación, puedes [visualizar los resultados en Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas registradas

Este proyecto puede contener marcas registradas o logotipos de proyectos, productos o servicios. El uso autorizado de marcas registradas o logotipos de Microsoft está sujeto a y debe seguir las [Directrices de marca y marcas registradas de Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). El uso de marcas registradas o logotipos de Microsoft en versiones modificadas de este proyecto no debe causar confusión ni implicar patrocinio de Microsoft. Cualquier uso de marcas registradas o logotipos de terceros está sujeto a las políticas de esos terceros.

## Obtener ayuda

Si tienes dudas o te quedas atascado al crear aplicaciones de IA, únete a:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Si tienes comentarios sobre el producto o errores al desarrollar, visita:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.