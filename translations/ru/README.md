<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "18318279bb851dc2c709bfc6a26f6e1d",
  "translation_date": "2025-05-07T14:10:19+00:00",
  "source_file": "README.md",
  "language_code": "ru"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: Автоматизируйте перевод образовательной документации без усилий

_Легко автоматизируйте перевод вашей документации на несколько языков, чтобы охватить глобальную аудиторию._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Поддержка языков от Co-op Translator

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](./README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **Мощная автоматизация**: Теперь с поддержкой GitHub Actions! Автоматически переводите вашу документацию при изменениях в репозитории, легко поддерживая её в актуальном состоянии. [Узнайте больше](../..).

## Поддерживаемые модели и сервисы

| Тип                   | Название                       |
|-----------------------|--------------------------------|
| Языковая модель       | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Компьютерное зрение   | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> Если сервис компьютерного зрения недоступен, co-op translator переключится в [режим только Markdown](./getting_started/markdown-only-mode.md).

## Обзор: Оптимизация перевода образовательного контента

Языковые барьеры значительно ограничивают доступ к ценным образовательным ресурсам и техническим знаниям для учащихся и разработчиков по всему миру. Это снижает участие и замедляет темпы глобальных инноваций и обучения.

**Co-op Translator** был создан, чтобы решить проблему неэффективного ручного перевода масштабных образовательных серий Microsoft (например, руководств «Для начинающих»). Сейчас это простой и мощный инструмент, который помогает преодолевать эти барьеры для всех. Предоставляя качественные автоматические переводы через CLI и GitHub Actions, Co-op Translator даёт возможность преподавателям, студентам, исследователям и разработчикам по всему миру делиться знаниями и получать доступ к ним без языковых ограничений.

Посмотрите, как Co-op Translator организует переведённый образовательный контент:

![Пример](../../imgs/translation-ex.png)

Файлы Markdown и текст на изображениях автоматически переводятся и аккуратно структурируются в папки по языкам.

**Откройте глобальный доступ к вашему образовательному контенту с Co-op Translator уже сегодня!**

## Поддержка глобального доступа к образовательным ресурсам Microsoft

Co-op Translator помогает преодолевать языковой барьер для ключевых образовательных инициатив Microsoft, автоматизируя процесс перевода репозиториев, обслуживающих глобальное сообщество разработчиков. Примеры проектов, использующих Co-op Translator:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## Основные возможности

- **Автоматический перевод**: Легко переводите текст на множество языков.
- **Интеграция с GitHub Actions**: Автоматизируйте перевод в рамках вашего CI/CD.
- **Сохранение Markdown**: Поддержка корректного синтаксиса Markdown при переводе.
- **Перевод текста на изображениях**: Извлечение и перевод текста, содержащегося в изображениях.
- **Современные LLM-технологии**: Использование передовых языковых моделей для качественного перевода.
- **Простая интеграция**: Легко встраивается в существующую структуру проекта.
- **Упрощение локализации**: Оптимизация процесса локализации проекта для международных рынков.

## Как это работает

![Архитектура](../../imgs/architecture_241019.png)

Co-op Translator обрабатывает Markdown-файлы и изображения из папки вашего проекта следующим образом:

1. **Извлечение текста**: Извлекает текст из Markdown-файлов и, при настройке (например, с Azure Computer Vision), из изображений.
1. **Перевод с помощью ИИ**: Отправляет извлечённый текст в выбранную языковую модель (Azure OpenAI, OpenAI и др.) для перевода.
1. **Сохранение результатов**: Сохраняет переведённые Markdown-файлы и изображения (с переведённым текстом) в папки по языкам, сохраняя исходное форматирование.

## Начало работы

> [!NOTE]
> В этом руководстве сделан акцент на ресурсах Azure, но вы можете использовать любую поддерживаемую языковую модель из списка [поддерживаемых моделей и сервисов](../..).

Быстрый старт с CLI или настройка полной автоматизации с помощью GitHub Actions.

### Первоначальная настройка

- [Настройка Azure AI](./getting_started/set-up-azure-ai.md)

### Быстрый старт: командная строка

Для быстрого запуска через командную строку:

1. Установите пакет:
    ```bash
    pip install co-op-translator
    ```
2. Настройте учётные данные:
  - Создайте файл `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` с флагом:
    ```bash
    translate -l "ko ja fr"
    ```
    *(Замените `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) в вашем репозитории. Локальная установка не требуется.
- Руководства:
  - [Руководство по GitHub Actions (публичные репозитории и стандартные секреты)](./getting_started/github-actions-guide/github-actions-guide-public.md) — используйте для большинства публичных или личных репозиториев с обычными секретами репозитория.
  - [Руководство по GitHub Actions (репозитории Microsoft Organization и настройки на уровне организации)](./getting_started/github-actions-guide/github-actions-guide-org.md) — для работы внутри организации Microsoft GitHub или если нужны секреты и раннеры на уровне организации.

### Устранение неполадок и советы

- [Руководство по устранению неполадок](./getting_started/troubleshooting.md)

### Дополнительные ресурсы

- [Справочник команд](./getting_started/command-reference.md): Подробное описание всех доступных команд и опций.
- [Настройка поддержки нескольких языков](./getting_started/multi-language-support.md): Как добавить таблицу с ссылками на переводы в README.
- [Поддерживаемые языки](./getting_started/supported-languages.md): Список поддерживаемых языков и инструкции по добавлению новых.
- [Режим только Markdown](./getting_started/markdown-only-mode.md): Как переводить только текст без обработки изображений.

## Видеопрезентации

Узнайте больше о Co-op Translator из наших презентаций _(нажмите на изображение ниже для просмотра на YouTube)_:

- **Open at Microsoft**: Краткое 18-минутное введение и быстрое руководство по использованию Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: Подробное часовое руководство с пошаговым объяснением — от понимания, что такое Co-op Translator, настройки инструмента и эффективного использования до живой демонстрации возможностей.

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Поддержите нас и способствуйте глобальному обучению

Присоединяйтесь к революции в обмене образовательным контентом по всему миру! Поставьте ⭐ [Co-op Translator](https://github.com/azure/co-op-translator) на GitHub и поддержите нашу миссию по устранению языковых барьеров в обучении и технологиях. Ваш интерес и вклад имеют большое значение! Мы всегда рады вашим кодовым доработкам и предложениям по функциям.

## Вклад в проект

Проект приветствует ваши предложения и участие. Хотите помочь развитию Azure Co-op Translator? Ознакомьтесь с нашим [CONTRIBUTING.md](./CONTRIBUTING.md) для инструкций о том, как сделать Co-op Translator более доступным.

## Участники проекта

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс поведения

В проекте принят [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Подробнее смотрите в [FAQ по Кодексу поведения](https://opensource.microsoft.com/codeofconduct/faq/) или обращайтесь по адресу [opencode@microsoft.com](mailto:opencode@microsoft.com) с вопросами и комментариями.

## Ответственный ИИ

Microsoft стремится помогать клиентам использовать наши ИИ-продукты ответственно, делясь опытом и строя доверительные партнёрства с помощью инструментов, таких как Transparency Notes и Impact Assessments. Многие из этих ресурсов доступны по адресу [https://aka.ms/RAI](https://aka.ms/RAI).
Подход Microsoft к ответственному ИИ основан на принципах справедливости, надёжности и безопасности, конфиденциальности и безопасности, инклюзивности, прозрачности и подотчётности.
Модели крупного масштаба для обработки естественного языка, изображений и речи — такие, как те, что используются в этом примере — могут иногда вести себя несправедливо, ненадёжно или оскорбительно, что может привести к негативным последствиям. Пожалуйста, ознакомьтесь с [Примечанием по прозрачности службы Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), чтобы узнать о рисках и ограничениях.

Рекомендуемый способ снижения этих рисков — включить в архитектуру систему безопасности, способную выявлять и предотвращать вредоносное поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставляет независимый уровень защиты, который может обнаруживать вредоносный контент, созданный пользователями и ИИ, в приложениях и сервисах. Azure AI Content Safety включает API для работы с текстом и изображениями, позволяющие выявлять вредоносный материал. Также у нас есть интерактивная Content Safety Studio, которая позволяет просматривать, исследовать и тестировать пример кода для обнаружения вредоносного контента в разных форматах. Следующая [документация для быстрого старта](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) поможет вам сделать запросы к сервису.

Ещё один важный аспект — общая производительность приложения. В приложениях с мультимодальными и мультимодельными решениями под производительностью понимается выполнение системы в соответствии с вашими и ожиданиями пользователей, включая отсутствие генерации вредоносных результатов. Важно оценивать производительность вашего приложения с помощью [метрик качества генерации, риска и безопасности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Вы можете оценить ваше AI-приложение в среде разработки, используя [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Имея тестовый набор данных или цель, генерации вашего генеративного ИИ количественно оцениваются с помощью встроенных или пользовательских оценщиков на ваш выбор. Чтобы начать работу с prompt flow sdk для оценки вашей системы, следуйте [руководству быстрого старта](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). После выполнения оценки вы можете [визуализировать результаты в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торговые марки

В этом проекте могут использоваться торговые марки или логотипы проектов, продуктов или сервисов. Авторизованное использование торговых марок или логотипов Microsoft подчиняется и должно соответствовать [Руководству Microsoft по торговым маркам и брендам](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Использование торговых марок или логотипов Microsoft в изменённых версиях этого проекта не должно вводить в заблуждение или подразумевать спонсорство Microsoft. Использование торговых марок или логотипов третьих сторон регулируется политиками соответствующих третьих лиц.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.