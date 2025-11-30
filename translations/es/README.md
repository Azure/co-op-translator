<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T09:45:05+00:00",
  "source_file": "README.md",
  "language_code": "es"
}
-->
# Traductor Co-op

_Automatiza fácilmente la traducción de tu contenido educativo en GitHub a múltiples idiomas para llegar a una audiencia global._

[![Paquete Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Licencia: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Descargas](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Descargas](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Contenedor: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Estilo de código: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Contribuidores en GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Issues en GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull requests en GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Bienvenidos](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Soporte Multilingüe

#### Soportado por [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengalí](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmano (Myanmar)](../my/README.md) | [Chino (Simplificado)](../zh/README.md) | [Chino (Tradicional, Hong Kong)](../hk/README.md) | [Chino (Tradicional, Macao)](../mo/README.md) | [Chino (Tradicional, Taiwán)](../tw/README.md) | [Croata](../hr/README.md) | [Checo](../cs/README.md) | [Danés](../da/README.md) | [Holandés](../nl/README.md) | [Estonio](../et/README.md) | [Finlandés](../fi/README.md) | [Francés](../fr/README.md) | [Alemán](../de/README.md) | [Griego](../el/README.md) | [Hebreo](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonesio](../id/README.md) | [Italiano](../it/README.md) | [Japonés](../ja/README.md) | [Kannada](../kn/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malayo](../ms/README.md) | [Malayalam](../ml/README.md) | [Maratí](../mr/README.md) | [Nepalí](../ne/README.md) | [Pidgin Nigeriano](../pcm/README.md) | [Noruego](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polaco](../pl/README.md) | [Portugués (Brasil)](../br/README.md) | [Portugués (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumano](../ro/README.md) | [Ruso](../ru/README.md) | [Serbio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Español](./README.md) | [Swahili](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalo (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Tailandés](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Seguidores en GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Seguir)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Forks en GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Estrellas en GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Estrella)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Abrir en GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Abrir&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Resumen

**Co-op Translator** te ayuda a localizar tu contenido educativo en GitHub en varios idiomas sin esfuerzo.
Cuando actualizas tus archivos Markdown, imágenes o notebooks, las traducciones se sincronizan automáticamente, asegurando que tu contenido esté siempre preciso y actualizado para estudiantes de todo el mundo.

Ejemplo de cómo se organiza el contenido traducido:

![Ejemplo](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.es.png)

## Inicio rápido

```bash
# Crear y activar un entorno virtual (recomendado)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instalar el paquete
pip install co-op-translator
# Traducir
translate -l "ko ja fr" -md
```

Docker:

```bash
# Extraer la imagen pública de GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Ejecutar con la carpeta actual montada y .env proporcionado (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configuración mínima

1. Crea un archivo `.env` usando la plantilla: [.env.template](../../.env.template)
2. Configura un proveedor LLM (Azure OpenAI o OpenAI)
3. (Opcional) Para traducción de imágenes (`-img`), configura Azure AI Vision
4. (Recomendado) Limpia cualquier traducción previa para evitar conflictos (por ejemplo, `translations/`)
5. (Recomendado) Añade una sección de traducción a tu README usando la [plantilla de idiomas para README](./getting_started/README_languages_template.md)
6. Consulta: [Configurar Azure AI](./getting_started/set-up-azure-ai.md)

## Uso

Traduce todos los tipos soportados:

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

- Traducción automática para Markdown, notebooks e imágenes
- Mantiene las traducciones sincronizadas con los cambios en el origen
- Funciona localmente (CLI) o en CI (GitHub Actions)
- Usa Azure OpenAI o OpenAI; opcionalmente Azure AI Vision para imágenes
- Preserva el formato y la estructura de Markdown

## Documentación

- [Guía de línea de comandos](./getting_started/command-line-guide/command-line-guide.md)
- [Guía de GitHub Actions (repositorios públicos y secretos estándar)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Guía de GitHub Actions (repositorios de organización Microsoft y configuraciones a nivel org)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Plantilla de idiomas para README](./getting_started/README_languages_template.md)
- [Idiomas soportados](./getting_started/supported-languages.md)
- [Contribuir](./CONTRIBUTING.md)
- [Solución de problemas](./getting_started/troubleshooting.md)

### Guía específica para Microsoft
> [!NOTE]
> Solo para mantenedores de los repositorios “Para Principiantes” de Microsoft.

- [Actualizar la lista de “otros cursos” (solo para repositorios MS Beginners)](./getting_started/update-other-courses.md)

## Apóyanos y fomenta el aprendizaje global

¡Únete a nosotros para revolucionar la forma en que se comparte contenido educativo a nivel mundial! Dale una ⭐ a [Co-op Translator](https://github.com/azure/co-op-translator) en GitHub y apoya nuestra misión de eliminar las barreras del idioma en el aprendizaje y la tecnología. ¡Tu interés y contribuciones tienen un impacto significativo! Las contribuciones de código y sugerencias de funciones son siempre bienvenidas.

### Explora contenido educativo de Microsoft en tu idioma

- [AZD para Principiantes](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI para Principiantes](https://github.com/microsoft/edgeai-for-beginners)
- [Protocolo de Contexto de Modelo (MCP) para Principiantes](https://github.com/microsoft/mcp-for-beginners)
- [Agentes de IA para Principiantes](https://github.com/microsoft/ai-agents-for-beginners)
- [IA Generativa para Principiantes usando .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [IA Generativa para Principiantes](https://github.com/microsoft/generative-ai-for-beginners)
- [IA Generativa para Principiantes usando Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML para Principiantes](https://aka.ms/ml-beginners)
- [Ciencia de Datos para Principiantes](https://aka.ms/datascience-beginners)
- [IA para Principiantes](https://aka.ms/ai-beginners)
- [Ciberseguridad para Principiantes](https://github.com/microsoft/Security-101)
- [Desarrollo Web para Principiantes](https://aka.ms/webdev-beginners)
- [IoT para Principiantes](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Presentaciones en video

👉 Haz clic en la imagen para ver en YouTube.

- **Open at Microsoft**: Una breve introducción de 18 minutos y guía rápida sobre cómo usar Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.es.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuciones

Este proyecto está abierto a contribuciones y sugerencias. ¿Interesado en contribuir a Azure Co-op Translator? Por favor, consulta nuestro [CONTRIBUTING.md](./CONTRIBUTING.md) para conocer las pautas sobre cómo ayudar a que Co-op Translator sea más accesible.

## Contribuidores

[![contribuidores de co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Código de Conducta

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/).
Para más información, consulta las [Preguntas frecuentes sobre el Código de Conducta](https://opensource.microsoft.com/codeofconduct/faq/) o
contacta a [opencode@microsoft.com](mailto:opencode@microsoft.com) para cualquier pregunta o comentario adicional.

## IA Responsable

Microsoft está comprometido a ayudar a nuestros clientes a usar nuestros productos de IA de manera responsable, compartiendo nuestras experiencias y construyendo asociaciones basadas en la confianza mediante herramientas como Notas de Transparencia y Evaluaciones de Impacto. Muchos de estos recursos están disponibles en [https://aka.ms/RAI](https://aka.ms/RAI).
El enfoque de Microsoft hacia la IA responsable se basa en nuestros principios de IA: equidad, confiabilidad y seguridad, privacidad y protección, inclusión, transparencia y responsabilidad.

Los modelos a gran escala de lenguaje natural, imagen y voz —como los usados en este ejemplo— pueden comportarse de maneras injustas, poco confiables u ofensivas, causando daños. Por favor, consulta la [nota de transparencia del servicio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para informarte sobre riesgos y limitaciones.
El enfoque recomendado para mitigar estos riesgos es incluir un sistema de seguridad en tu arquitectura que pueda detectar y prevenir comportamientos dañinos. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) proporciona una capa independiente de protección, capaz de detectar contenido dañino generado por usuarios y por IA en aplicaciones y servicios. Azure AI Content Safety incluye APIs de texto e imagen que te permiten detectar material perjudicial. También contamos con un Content Safety Studio interactivo que te permite ver, explorar y probar código de ejemplo para detectar contenido dañino en diferentes modalidades. La siguiente [documentación de inicio rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) te guía para realizar solicitudes al servicio.

Otro aspecto a tener en cuenta es el rendimiento general de la aplicación. En aplicaciones multimodales y con múltiples modelos, consideramos que el rendimiento significa que el sistema funciona como tú y tus usuarios esperan, incluyendo no generar salidas dañinas. Es importante evaluar el rendimiento de tu aplicación en general usando [métricas de calidad de generación y de riesgo y seguridad](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puedes evaluar tu aplicación de IA en tu entorno de desarrollo usando el [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dado un conjunto de datos de prueba o un objetivo, las generaciones de tu aplicación de IA generativa se miden cuantitativamente con evaluadores integrados o evaluadores personalizados de tu elección. Para comenzar con el prompt flow sdk y evaluar tu sistema, puedes seguir la [guía de inicio rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una vez que ejecutes una evaluación, puedes [visualizar los resultados en Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas Registradas

Este proyecto puede contener marcas registradas o logotipos de proyectos, productos o servicios. El uso autorizado de marcas o logotipos de Microsoft está sujeto a y debe seguir las [Directrices de Marca y Marcas Registradas de Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). El uso de marcas o logotipos de Microsoft en versiones modificadas de este proyecto no debe causar confusión ni implicar patrocinio por parte de Microsoft. Cualquier uso de marcas o logotipos de terceros está sujeto a las políticas de esos terceros.

## Obtener Ayuda

Si te quedas atascado o tienes alguna pregunta sobre cómo construir aplicaciones de IA, únete a:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Si tienes comentarios sobre el producto o encuentras errores durante el desarrollo, visita:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->