<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T02:14:46+00:00",
  "source_file": "README.md",
  "language_code": "ru"
}
-->
# Co-op Translator

_Автоматизируйте перевод вашего образовательного контента на GitHub на множество языков, чтобы сделать его доступным для мировой аудитории._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Многоязычная поддержка

#### Поддерживается [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Арабский](../ar/README.md) | [Бенгальский](../bn/README.md) | [Болгарский](../bg/README.md) | [Бирманский (Мьянма)](../my/README.md) | [Китайский (упрощённый)](../zh/README.md) | [Китайский (традиционный, Гонконг)](../hk/README.md) | [Китайский (традиционный, Макао)](../mo/README.md) | [Китайский (традиционный, Тайвань)](../tw/README.md) | [Хорватский](../hr/README.md) | [Чешский](../cs/README.md) | [Датский](../da/README.md) | [Нидерландский](../nl/README.md) | [Эстонский](../et/README.md) | [Финский](../fi/README.md) | [Французский](../fr/README.md) | [Немецкий](../de/README.md) | [Греческий](../el/README.md) | [Иврит](../he/README.md) | [Хинди](../hi/README.md) | [Венгерский](../hu/README.md) | [Индонезийский](../id/README.md) | [Итальянский](../it/README.md) | [Японский](../ja/README.md) | [Корейский](../ko/README.md) | [Литовский](../lt/README.md) | [Малайский](../ms/README.md) | [Маратхи](../mr/README.md) | [Непальский](../ne/README.md) | [Норвежский](../no/README.md) | [Персидский (фарси)](../fa/README.md) | [Польский](../pl/README.md) | [Португальский (Бразилия)](../br/README.md) | [Португальский (Португалия)](../pt/README.md) | [Панджаби (Гурмукхи)](../pa/README.md) | [Румынский](../ro/README.md) | [Русский](./README.md) | [Сербский (кириллица)](../sr/README.md) | [Словацкий](../sk/README.md) | [Словенский](../sl/README.md) | [Испанский](../es/README.md) | [Суахили](../sw/README.md) | [Шведский](../sv/README.md) | [Тагальский (Филиппины)](../tl/README.md) | [Тамильский](../ta/README.md) | [Тайский](../th/README.md) | [Турецкий](../tr/README.md) | [Украинский](../uk/README.md) | [Урду](../ur/README.md) | [Вьетнамский](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Обзор

**Co-op Translator** позволяет быстро переводить ваш образовательный контент на GitHub на разные языки, чтобы легко охватить международную аудиторию. Когда вы обновляете свои Markdown-файлы, изображения или Jupyter-ноутбуки, переводы автоматически синхронизируются, чтобы ваш образовательный контент на GitHub всегда был актуальным для пользователей по всему миру.

Посмотрите, как Co-op Translator организует переведённый образовательный контент на GitHub:

![Пример](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.ru.png)

## Быстрый старт

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

## Минимальная настройка

- Создайте файл `.env` по шаблону: [.env.template](../../.env.template)
- Настройте одного провайдера LLM (Azure OpenAI или OpenAI)
- Для перевода изображений (`-img`) также укажите Azure AI Vision
- Рекомендуется: если у вас есть переводы, созданные другими инструментами, сначала удалите их, чтобы избежать конфликтов (например: `translations/`).
- Рекомендуется: добавьте раздел с переводами в ваш README, используя [шаблон языков README](./README_languages_template.md)
- Подробнее: [Настройка Azure AI](./getting_started/set-up-azure-ai.md)

## Использование

Перевести все поддерживаемые типы:

```bash
translate -l "ko ja"
```

Только Markdown:

```bash
translate -l "de" -md
```

Markdown + изображения:

```bash
translate -l "pt" -md -img
```

Только ноутбуки:

```bash
translate -l "zh" -nb
```

Больше флагов: [Справочник команд](./getting_started/command-reference.md)

## Возможности

- Автоматический перевод Markdown, ноутбуков и изображений
- Сохраняет синхронизацию переводов с исходными изменениями
- Работает локально (CLI) и в CI (GitHub Actions)
- Использует Azure OpenAI или OpenAI; опционально Azure AI Vision для изображений
- Сохраняет форматирование и структуру Markdown

## Документация

- [Руководство по командной строке](./getting_started/command-line-guide/command-line-guide.md)
- [Руководство по GitHub Actions (Публичные репозитории и стандартные секреты)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Руководство по GitHub Actions (Репозитории организации Microsoft и настройки на уровне организации)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Поддерживаемые языки](./getting_started/supported-languages.md)
- [Устранение неполадок](./getting_started/troubleshooting.md)

## Поддержите нас и развивайте глобальное обучение

Присоединяйтесь к нам, чтобы изменить подход к распространению образовательного контента по всему миру! Поставьте ⭐ [Co-op Translator](https://github.com/azure/co-op-translator) на GitHub и поддержите нашу миссию по преодолению языковых барьеров в обучении и технологиях. Ваш интерес и вклад действительно важны! Мы всегда рады вашим предложениям и участию в разработке.

### Изучайте образовательный контент Microsoft на вашем языке

- [AZD для начинающих](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI для начинающих](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) для начинающих](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents для начинающих](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI для начинающих на .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI для начинающих](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI для начинающих на Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML для начинающих](https://aka.ms/ml-beginners)
- [Data Science для начинающих](https://aka.ms/datascience-beginners)
- [AI для начинающих](https://aka.ms/ai-beginners)
- [Кибербезопасность для начинающих](https://github.com/microsoft/Security-101)
- [Web Dev для начинающих](https://aka.ms/webdev-beginners)
- [IoT для начинающих](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Видео-презентации

Узнайте больше о Co-op Translator из наших презентаций _(Нажмите на изображение ниже, чтобы посмотреть на YouTube.)_:

- **Open at Microsoft**: Краткое 18-минутное введение и быстрый гид по использованию Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.ru.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Вклад

Этот проект открыт для предложений и участия. Хотите внести вклад в Azure Co-op Translator? Ознакомьтесь с [CONTRIBUTING.md](./CONTRIBUTING.md), чтобы узнать, как вы можете помочь сделать Co-op Translator более доступным.

## Участники

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс поведения

В этом проекте действует [Кодекс поведения Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).
Подробнее см. [FAQ по кодексу поведения](https://opensource.microsoft.com/codeofconduct/faq/) или
свяжитесь с [opencode@microsoft.com](mailto:opencode@microsoft.com) по любым вопросам или комментариям.

## Ответственный ИИ

Microsoft стремится помогать клиентам использовать наши ИИ-продукты ответственно, делиться опытом и строить доверительные отношения с помощью таких инструментов, как Transparency Notes и Impact Assessments. Многие из этих ресурсов доступны по адресу [https://aka.ms/RAI](https://aka.ms/RAI).
Подход Microsoft к ответственному ИИ основан на принципах справедливости, надёжности и безопасности, конфиденциальности и защите, инклюзивности, прозрачности и ответственности.

Крупномасштабные модели обработки естественного языка, изображений и речи — такие, как используются в этом примере — могут вести себя несправедливо, ненадёжно или оскорбительно, что может привести к негативным последствиям. Ознакомьтесь с [Transparency note по Azure OpenAI service](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), чтобы узнать о рисках и ограничениях.

Рекомендуется включать систему безопасности в вашу архитектуру, чтобы обнаруживать и предотвращать вредоносное поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставляет независимый уровень защиты, способный обнаруживать вредоносный пользовательский и ИИ-контент в приложениях и сервисах. Azure AI Content Safety включает API для текста и изображений, которые позволяют выявлять опасные материалы. Также есть интерактивная Content Safety Studio, где можно просматривать, исследовать и тестировать примеры кода для обнаружения вредоносного контента в разных форматах. Следующая [документация по быстрому старту](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) поможет вам начать работу с сервисом.
Еще один важный аспект — это производительность приложения в целом. В случае мультимодальных и многомодельных приложений, под производительностью мы понимаем, что система работает так, как ожидаете вы и ваши пользователи, включая предотвращение вредоносных результатов. Важно оценивать производительность всего приложения с помощью <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">метрик качества генерации, рисков и безопасности</a>.

Вы можете оценить свое AI-приложение в среде разработки с помощью <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK</a>. Используя тестовый датасет или целевую задачу, генерации вашего генеративного AI-приложения количественно оцениваются встроенными или пользовательскими оценщиками на ваш выбор. Чтобы начать работу с prompt flow sdk для оценки вашей системы, следуйте <a href="https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk">руководству по быстрому старту</a>. После запуска оценки вы можете <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">визуализировать результаты в Azure AI Studio</a>.

## Товарные знаки

В этом проекте могут использоваться товарные знаки или логотипы проектов, продуктов или сервисов. Разрешенное использование товарных знаков или логотипов Microsoft регулируется и должно соответствовать <a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">Руководству по использованию товарных знаков и брендов Microsoft</a>. Использование товарных знаков или логотипов Microsoft в измененных версиях этого проекта не должно вводить в заблуждение или подразумевать спонсорство со стороны Microsoft. Любое использование товарных знаков или логотипов третьих сторон регулируется политиками этих сторон.

## Получение помощи

Если у вас возникли трудности или вопросы по созданию AI-приложений, присоединяйтесь к:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

Если у вас есть отзывы о продукте или возникли ошибки при разработке, посетите:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**Отказ от ответственности**:
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на стремление к точности, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несём ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.