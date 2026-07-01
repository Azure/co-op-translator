# Co-op Translator

_Легко автоматизируйте и поддерживайте переводы вашего образовательного контента на GitHub на нескольких языках по мере развития проекта._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
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

**Начните здесь:** [Выберите рабочий процесс](https://azure.github.io/co-op-translator/workflows/) | [Конфигурация](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Поддержка нескольких языков

#### Поддерживается [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Арабский](../ar/README.md) | [Бенгальский](../bn/README.md) | [Болгарский](../bg/README.md) | [Бирманский (Мьянма)](../my/README.md) | [Китайский (упрощённый)](../zh-CN/README.md) | [Китайский (традиционный, Гонконг)](../zh-HK/README.md) | [Китайский (традиционный, Макао)](../zh-MO/README.md) | [Китайский (традиционный, Тайвань)](../zh-TW/README.md) | [Хорватский](../hr/README.md) | [Чешский](../cs/README.md) | [Датский](../da/README.md) | [Нидерландский](../nl/README.md) | [Эстонский](../et/README.md) | [Финский](../fi/README.md) | [Французский](../fr/README.md) | [Немецкий](../de/README.md) | [Греческий](../el/README.md) | [Иврит](../he/README.md) | [Хинди](../hi/README.md) | [Венгерский](../hu/README.md) | [Индонезийский](../id/README.md) | [Итальянский](../it/README.md) | [Японский](../ja/README.md) | [Каннада](../kn/README.md) | [Кхмерский](../km/README.md) | [Корейский](../ko/README.md) | [Литовский](../lt/README.md) | [Малайский](../ms/README.md) | [Малаялам](../ml/README.md) | [Маратхи](../mr/README.md) | [Непали](../ne/README.md) | [Нигерийский пиджин](../pcm/README.md) | [Норвежский](../no/README.md) | [Персидский (фарси)](../fa/README.md) | [Польский](../pl/README.md) | [Португальский (Бразилия)](../pt-BR/README.md) | [Португальский (Португалия)](../pt-PT/README.md) | [Пенджабский (Гурмукхи)](../pa/README.md) | [Румынский](../ro/README.md) | [Русский](./README.md) | [Сербский (кириллица)](../sr/README.md) | [Словацкий](../sk/README.md) | [Словенский](../sl/README.md) | [Испанский](../es/README.md) | [Суахили](../sw/README.md) | [Шведский](../sv/README.md) | [Тагалог (филиппинский)](../tl/README.md) | [Тамильский](../ta/README.md) | [Телугу](../te/README.md) | [Тайский](../th/README.md) | [Турецкий](../tr/README.md) | [Украинский](../uk/README.md) | [Урду](../ur/README.md) | [Вьетнамский](../vi/README.md)

> **Предпочитаете клонировать локально?**
>
> Этот репозиторий включает переводы более чем на 50 языков, что значительно увеличивает размер загрузки. Чтобы клонировать без переводов, используйте sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Это даст вам всё необходимое для завершения курса при гораздо более быстрой загрузке.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Обзор

**Co-op Translator** помогает вам локализовать ваш образовательный контент на GitHub на несколько языков без лишних усилий.
Когда вы обновляете Markdown-файлы, изображения или ноутбуки, переводы автоматически остаются синхронизированными, гарантируя, что ваш контент остаётся точным и актуальным для учащихся по всему миру.

Используйте его через CLI для перевода репозитория, через Python API для автоматизации или через MCP-сервер для рабочих процессов с агентами и редакторами.

Пример организации переведённого контента:

![Пример](../../imgs/translation-ex.png)

## Почему Co-op Translator?

Перевести один файл — просто. Поддерживать весь репозиторий документации
переведённым, связанным и актуальным — вот где сложность.

| Проблема | Как Co-op Translator помогает |
| --- | --- |
| Long docs are not one prompt | Большие Markdown-файлы разделяются на фрагменты, поэтому длинный README не зависит от одного уязвимого ответа модели. Если фрагмент не удаётся, Co-op Translator может повторить попытку и повторно разбить на фрагменты только неудачную часть. |
| Incomplete translations should not be marked current | Урезанный перевод никогда не должен считаться актуальным. Co-op Translator проверяет целостность перевода перед сохранением и может обнаруживать структурно неполные существующие переводы. |
| Links should match the translated repo structure | Ручные переводы часто оставляют относительные ссылки, указывающие обратно на дерево исходного репозитория. Co-op Translator переписывает ссылки в Markdown, ноутбуках, изображениях и README, чтобы они соответствовали структуре `translations/<lang>/...`. |
| Translation should work across an entire repo | Co-op Translator обрабатывает файлы README, docs, ноутбуки и текст на изображениях как часть единого рабочего процесса репозитория, вместо перевода файлов по одному. |
| Maintaining translations matters more than creating them once | Хеши исходников и метаданные перевода позволяют Co-op Translator находить устаревшие файлы, пропускать неизменённые файлы и поддерживать синхронизацию переведённого контента по мере развития исходного репозитория. |

## Как управляется состояние перевода

Co-op Translator управляет переведённым контентом как версионируемыми программными артефактами,  
а не как статическими файлами.

Инструмент отслеживает состояние переведённых Markdown-файлов, изображений и ноутбуков
с помощью **метаданных, привязанных к языку**.

Такая разработка позволяет Co-op Translator:

- Надёжно обнаруживать устаревшие переводы
- Обрабатывать Markdown, изображения и ноутбуки последовательно
- Безопасно масштабироваться в больших, быстро меняющихся, многоязычных репозиториях

Моделируя переводы как управляемые артефакты,
рабочие процессы перевода естественным образом согласуются с современными
практиками управления зависимостями и артефактами в разработке ПО.

→ [Как управляется состояние перевода](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Связанные подробные материалы

- [Исправление сломанного Markdown при AI-переводе: усиление рабочей конвейера для продакшена](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Начало работы

Co-op Translator можно использовать через CLI, Python API или MCP-сервер. Начните с руководства по рабочему процессу, если вы выбираете между локальным переводом, автоматизацией, CI и интеграцией с агентами/редакторами.

- [Выберите рабочий процесс](../../docs/workflows.md)
- [Настройка учётных данных](../../docs/configuration.md)
- [Перевод через CLI](../../docs/cli.md)
- [Автоматизация с Python API](../../docs/api.md)
- [Подключение к MCP Server](../../docs/mcp.md)
- [Запуск в GitHub Actions](../../docs/github-actions.md)

Минимальный пример использования CLI после настройки:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

Для первых запусков в больших репозиториях используйте `--dry-run` перед записью переведённых файлов. Смотрите [CLI Reference](../../docs/cli.md) для флагов типов контента, логов, обзора и миграции ссылок.

Быстрый запуск контейнера с Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Быстрый запуск контейнера с PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Возможности

- Автоматический перевод для Markdown, ноутбуков и изображений
- Поддерживает синхронизацию переводов с изменениями источника
- Работает локально (CLI) или в CI (GitHub Actions)
- Обеспечивает инструменты перевода Markdown, ноутбуков, изображений, обзора и проектов через MCP
- Использует Azure OpenAI или OpenAI в качестве поставщика перевода
- Позволяет MCP размещать агентов для перевода фрагментов Markdown и ноутбуков без учётных данных LLM Co-op Translator
- Использует Azure AI Vision для извлечения текста из изображений и перевода
- Проверяет структуру и актуальность перевода детерминированными проверками
- Сохраняет форматирование и структуру Markdown

## Документация

- [Сайт документации](https://azure.github.io/co-op-translator/)
- [Выберите рабочий процесс](../../docs/workflows.md)
- [Конфигурация](../../docs/configuration.md)
- [Настройка Azure AI](../../docs/azure-ai-setup.md)
- [Справочник CLI](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Шаблон языков в README](../../docs/readme-languages-template.md)
- [Поддерживаемые языки](../../docs/supported-languages.md)
- [Участие в проекте](../../CONTRIBUTING.md)
- [Поиск и устранение неполадок](../../docs/troubleshooting.md)

### Руководство, специфичное для Microsoft
> [!NOTE]
> Только для сопровождающих репозиториев Microsoft “For Beginners”.

- [Обновление списка “other courses” (только для репозиториев MS Beginners)](../../docs/microsoft-beginners.md)

## Поддержите нас и способствуйте глобальному обучению

Присоединяйтесь к нам в революционировании способов обмена образовательным контентом по всему миру! Поставьте [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ на GitHub и поддержите нашу миссию по устранению языковых барьеров в обучении и технологиях. Ваш интерес и вклад имеют большое значение! Вклады кода и предложения по функциям всегда приветствуются.

### Ознакомьтесь с образовательным контентом Microsoft на вашем языке
- [LangChain4j-для-начинающих](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD для начинающих](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI для начинающих](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) для начинающих](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents для начинающих](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI для начинающих с использованием .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI для начинающих](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI для начинающих с использованием Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML для начинающих](https://aka.ms/ml-beginners)
- [Data Science для начинающих](https://aka.ms/datascience-beginners)
- [AI для начинающих](https://aka.ms/ai-beginners)
- [Кибербезопасность для начинающих](https://github.com/microsoft/Security-101)
- [Веб-разработка для начинающих](https://aka.ms/webdev-beginners)
- [IoT для начинающих](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Видеопрезентации

👉 Нажмите на изображение ниже, чтобы посмотреть на YouTube.

- **Open at Microsoft**: Краткое 18‑минутное введение и быстрый гид по использованию Co-op Translator.

  [![Открыть в Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Участие

Этот проект приветствует вклад и предложения. Хотите внести вклад в Azure Co-op Translator? Пожалуйста, смотрите наш [CONTRIBUTING.md](../../CONTRIBUTING.md) для рекомендаций о том, как вы можете помочь сделать Co-op Translator более доступным.

## Участники

[![участники co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс поведения

В этом проекте принят [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Для получения дополнительной информации смотрите [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) или
свяжитесь с [opencode@microsoft.com](mailto:opencode@microsoft.com) по любым дополнительным вопросам или комментариям.

## Ответственный ИИ

Microsoft стремится помогать нашим клиентам использовать наши продукты ИИ ответственно, делиться полученными знаниями и выстраивать партнёрские отношения, основанные на доверии, с помощью таких инструментов, как Transparency Notes и Impact Assessments. Многие из этих ресурсов можно найти по адресу [https://aka.ms/RAI](https://aka.ms/RAI).
Подход Microsoft к ответственному использованию ИИ основывается на наших принципах ИИ: справедливость, надежность и безопасность, конфиденциальность и безопасность, инклюзивность, прозрачность и подотчетность.

Крупномасштабные модели для обработки естественного языка, изображений и речи — такие, как те, что используются в этом примере — могут потенциально вести себя несправедливо, ненадежно или оскорбительно, что, в свою очередь, может причинять вред. Пожалуйста, ознакомьтесь с [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), чтобы быть информированными о рисках и ограничениях.

Рекомендуемый подход к снижению этих рисков — включить в архитектуру систему безопасности, которая может обнаруживать и предотвращать вредоносное поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставляет независимый уровень защиты, способный обнаруживать вредоносный пользовательский и сгенерированный ИИ контент в приложениях и сервисах. Azure AI Content Safety включает текстовые и графические API, которые позволяют обнаруживать материал, представляющий опасность. У нас также есть интерактивная Content Safety Studio, которая позволяет просматривать, исследовать и опробовать примеры кода для обнаружения вредоносного контента в разных модальностях. Следующая [документация быстрого старта](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) проведёт вас через отправку запросов к сервису.

Другим аспектом, который следует учитывать, является общая производительность приложения. В мультимодальных и мульти-модельных приложениях под производительностью мы понимаем соответствие ожиданиям вас и ваших пользователей, включая отсутствие генерации вредоносных выводов. Важно оценивать производительность вашего приложения в целом, используя [метрики качества генерации и метрики рисков и безопасности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Вы можете оценить своё ИИ-приложение в среде разработки с помощью [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). При наличии тестового набора данных или целевого эталона, генерации вашего генеративного ИИ приложения количественно измеряются с помощью встроенных оценщиков или пользовательских оценщиков по вашему выбору. Чтобы начать работу с prompt flow SDK для оценки вашей системы, вы можете следовать [руководству по быстрому старту](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). После выполнения оценки вы можете [визуализировать результаты в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Товарные знаки

В этом проекте могут присутствовать товарные знаки или логотипы проектов, продуктов или сервисов. Авторизованное использование товарных знаков или логотипов Microsoft подчиняется и должно соответствовать [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Использование товарных знаков или логотипов Microsoft в изменённых версиях этого проекта не должно вводить в заблуждение или подразумевать спонсорство со стороны Microsoft.
Любое использование товарных знаков или логотипов третьих сторон подчиняется политикам этих третьих сторон.

## Получение помощи

Если вы застряли или у вас есть вопросы по созданию приложений ИИ, присоединяйтесь:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Если у вас есть отзывы о продукте или ошибки при разработке, посетите:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)