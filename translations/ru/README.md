<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "329abbc9354793ea422f7e7ebf66be2c",
  "translation_date": "2025-05-07T01:55:49+00:00",
  "source_file": "README.md",
  "language_code": "ru"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: Автоматизация перевода образовательной документации без усилий

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

### Поддержка языков с помощью Co-op Translator

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](./README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
>
> **Мощная автоматизация**: теперь с поддержкой GitHub Actions! Автоматически переводите вашу документацию при внесении изменений в репозиторий, легко поддерживая её в актуальном состоянии. [Узнать больше](../..).

## Поддерживаемые модели и сервисы

| Тип                   | Название                        |
|-----------------------|--------------------------------|
| Language Model        | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Computer Vision       | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> Если сервис компьютерного зрения недоступен, co-op translator переключится в [режим только Markdown](./getting_started/markdown-only-mode.md).

## Обзор: оптимизация перевода образовательного контента

Языковые барьеры значительно затрудняют доступ к ценным образовательным ресурсам и техническим знаниям для учащихся и разработчиков по всему миру. Это ограничивает участие и замедляет темпы глобальных инноваций и обучения.

**Co-op Translator** появился из необходимости решить проблему неэффективного ручного перевода крупных образовательных серий Microsoft (например, руководств «Для начинающих»). Сейчас это удобный и мощный инструмент, созданный для устранения этих барьеров для всех. Предоставляя качественный автоматический перевод через CLI и GitHub Actions, Co-op Translator помогает преподавателям, студентам, исследователям и разработчикам по всему миру делиться знаниями и получать доступ к ним без языковых ограничений.

Посмотрите, как Co-op Translator организует переведённый образовательный контент:

![Пример](../../imgs/translation-ex.png)

Markdown-файлы и текст на изображениях автоматически переводятся и аккуратно структурируются по папкам для каждого языка.

**Откройте глобальный доступ к вашему образовательному контенту с Co-op Translator уже сегодня!**

## Поддержка глобального доступа к образовательным ресурсам Microsoft

Co-op Translator помогает преодолевать языковой барьер для ключевых образовательных инициатив Microsoft, автоматизируя процесс перевода репозиториев, которые обслуживают глобальное сообщество разработчиков. Примеры проектов, использующих Co-op Translator:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## Основные возможности

- **Автоматический перевод**: легко переводите текст на несколько языков.
- **Интеграция с GitHub Actions**: автоматизируйте переводы в рамках вашего CI/CD.
- **Сохранение Markdown**: поддерживайте корректный синтаксис Markdown при переводе.
- **Перевод текста на изображениях**: извлекайте и переводите текст, встроенный в изображения.
- **Современные технологии LLM**: используйте передовые языковые модели для качественного перевода.
- **Простая интеграция**: легко вписывается в вашу текущую структуру проекта.
- **Упрощение локализации**: оптимизируйте процесс адаптации проекта для международных рынков.

## Как это работает

![Архитектура](../../imgs/architecture_241019.png)

Co-op Translator берёт Markdown-файлы и изображения из папки проекта и обрабатывает их следующим образом:

1. **Извлечение текста**: извлекает текст из Markdown-файлов и, если настроено (например, с Azure Computer Vision), текст, встроенный в изображения.
1. **AI-перевод**: отправляет извлечённый текст в выбранную LLM (Azure OpenAI, OpenAI и др.) для перевода.
1. **Сохранение результата**: сохраняет переведённые Markdown-файлы и изображения (с переведённым текстом) в папки для соответствующих языков, сохраняя исходное форматирование.

## Начало работы

Быстрый старт с CLI или настройка полной автоматизации через GitHub Actions.

### Быстрый старт: командная строка

Для быстрого начала работы через командную строку:

1. Установите пакет:
    ```bash
    pip install co-op-translator
    ```
2. Настройте учётные данные:
  - Создайте `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` флаг:
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
  - [GitHub Actions Guide (публичные репозитории и стандартные секреты)](./getting_started/github-actions-guide/github-actions-guide-public.md) — используйте для большинства публичных или личных репозиториев с использованием стандартных секретов репозитория.
  - [GitHub Actions Guide (репозитории организации Microsoft и настройки на уровне организации)](./getting_started/github-actions-guide/github-actions-guide-org.md) — используйте, если вы работаете в организации Microsoft на GitHub или нужно использовать секреты и раннеры на уровне организации.

> [!NOTE]
> Хотя этот туториал ориентирован на ресурсы Azure, вы можете использовать любую поддерживаемую языковую модель из списка [supported models and services](../..).

### Устранение неполадок и советы

- [Руководство по устранению неполадок](./getting_started/troubleshooting.md)

### Дополнительные ресурсы

- [Справочник по командам](./getting_started/command-reference.md): подробное описание всех доступных команд и опций.
- [Настройка поддержки нескольких языков](./getting_started/multi-language-support.md): как добавить таблицу с ссылками на переводы в README.
- [Поддерживаемые языки](./getting_started/supported-languages.md): список поддерживаемых языков и инструкции по добавлению новых.
- [Режим только Markdown](./getting_started/markdown-only-mode.md): как переводить только текст без обработки изображений.

## Видеопрезентации

Узнайте больше о Co-op Translator из наших презентаций _(кликните по изображению, чтобы посмотреть на YouTube)_:

- **Open at Microsoft**: краткое 18-минутное введение и быстрый гайд по использованию Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: подробное часовое пошаговое руководство — от понимания, что такое Co-op Translator, до настройки и эффективного использования с живой демонстрацией возможностей.

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Поддержите нас и способствуйте глобальному обучению

Присоединяйтесь к революции в обмене образовательным контентом по всему миру! Поставьте ⭐ [Co-op Translator](https://github.com/azure/co-op-translator) на GitHub и поддержите нашу миссию по преодолению языковых барьеров в обучении и технологиях. Ваш интерес и вклад имеют огромное значение! Мы всегда рады вашим предложениям и коду.

## Участие в проекте

Этот проект открыт для предложений и вклада. Хотите помочь развитию Azure Co-op Translator? Ознакомьтесь с нашими рекомендациями в [CONTRIBUTING.md](./CONTRIBUTING.md), чтобы узнать, как сделать Co-op Translator более доступным.

## Участники проекта

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс поведения

В проекте принят [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Подробнее смотрите в [FAQ по кодексу поведения](https://opensource.microsoft.com/codeofconduct/faq/) или обращайтесь по адресу [opencode@microsoft.com](mailto:opencode@microsoft.com) с вопросами или комментариями.

## Ответственный ИИ

Microsoft стремится помогать своим клиентам использовать ИИ-продукты ответственно, делиться опытом и строить доверительные отношения через инструменты, такие как Transparency Notes и Impact Assessments. Многие из этих ресурсов доступны по адресу [https://aka.ms/RAI](https://aka.ms/RAI).
Подход Microsoft к ответственному ИИ основан на принципах справедливости, надёжности и безопасности, конфиденциальности и защите данных, инклюзивности, прозрачности и подотчётности.

Крупномасштабные модели для обработки естественного языка, изображений и речи — такие, как используемые в этом примере — могут иногда вести себя несправедливо, ненадёжно или оскорбительно, что может причинять вред. Пожалуйста, ознакомьтесь с [Transparency note сервиса Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), чтобы быть в курсе рисков и ограничений.
Рекомендуемый подход к снижению этих рисков — включить в архитектуру систему безопасности, которая может обнаруживать и предотвращать вредоносное поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) обеспечивает независимый уровень защиты, способный выявлять вредоносный контент, созданный пользователями и ИИ, в приложениях и сервисах. Azure AI Content Safety включает API для работы с текстом и изображениями, которые позволяют обнаруживать вредоносные материалы. Также у нас есть интерактивная Content Safety Studio, которая позволяет просматривать, исследовать и пробовать примеры кода для обнаружения вредоносного контента в различных форматах. Следующая [документация по быстрому старту](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) проведет вас через процесс отправки запросов к сервису.

Еще один аспект, который следует учитывать — общая производительность приложения. В многоформатных и многомодельных приложениях под производительностью понимается то, что система работает так, как ожидаете вы и ваши пользователи, включая отсутствие генерации вредоносных результатов. Важно оценивать производительность вашего приложения в целом с помощью [метрик качества генерации и рисков безопасности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Вы можете оценить свое AI-приложение в среде разработки с помощью [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Имея тестовый набор данных или целевой результат, генерации вашего генеративного AI приложения количественно измеряются с помощью встроенных или пользовательских оценщиков по вашему выбору. Чтобы начать работу с prompt flow sdk для оценки вашей системы, вы можете следовать [руководству по быстрому старту](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). После выполнения оценки вы можете [визуализировать результаты в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торговые марки

В этом проекте могут использоваться торговые марки или логотипы проектов, продуктов или сервисов. Авторизованное использование торговых марок или логотипов Microsoft подчиняется и должно соответствовать [Руководству по торговым маркам и брендам Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Использование торговых марок или логотипов Microsoft в измененных версиях этого проекта не должно вызывать путаницу или подразумевать спонсорство Microsoft. Любое использование торговых марок или логотипов третьих сторон подчиняется политикам этих третьих сторон.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.