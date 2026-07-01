# Co-op Translator

_Лесно автоматизирайте и поддържайте преводите на вашето образователно съдържание в GitHub на множество езици, докато проектът ви се развива._

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

**Започнете тук:** [Изберете вашия работен поток](https://azure.github.io/co-op-translator/workflows/) | [Конфигурация](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Поддръжка на множество езици

#### Поддържано от [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Арабски](../ar/README.md) | [Бенгалски](../bn/README.md) | [Български](./README.md) | [Бирмански (Мианмар)](../my/README.md) | [Китайски (опростен)](../zh-CN/README.md) | [Китайски (традиционен, Хонконг)](../zh-HK/README.md) | [Китайски (традиционен, Макао)](../zh-MO/README.md) | [Китайски (традиционен, Тайван)](../zh-TW/README.md) | [Хърватски](../hr/README.md) | [Чешки](../cs/README.md) | [Датски](../da/README.md) | [Нидерландски](../nl/README.md) | [Естонски](../et/README.md) | [Фински](../fi/README.md) | [Френски](../fr/README.md) | [Немски](../de/README.md) | [Гръцки](../el/README.md) | [Иврит](../he/README.md) | [Хинди](../hi/README.md) | [Унгарски](../hu/README.md) | [Индонезийски](../id/README.md) | [Италиански](../it/README.md) | [Японски](../ja/README.md) | [Каннада](../kn/README.md) | [Кхмерски](../km/README.md) | [Корейски](../ko/README.md) | [Литовски](../lt/README.md) | [Малайски](../ms/README.md) | [Малаялам](../ml/README.md) | [Марати](../mr/README.md) | [Непалски](../ne/README.md) | [Нигерийски пиджин](../pcm/README.md) | [Норвежки](../no/README.md) | [Персийски (фарси)](../fa/README.md) | [Полски](../pl/README.md) | [Португалски (Бразилия)](../pt-BR/README.md) | [Португалски (Португалия)](../pt-PT/README.md) | [Пенджабски (гурмукхи)](../pa/README.md) | [Румънски](../ro/README.md) | [Руски](../ru/README.md) | [Сръбски (кирилица)](../sr/README.md) | [Словашки](../sk/README.md) | [Словенски](../sl/README.md) | [Испански](../es/README.md) | [Суахили](../sw/README.md) | [Шведски](../sv/README.md) | [Тагалог (филипински)](../tl/README.md) | [Тамилски](../ta/README.md) | [Телугу](../te/README.md) | [Тайски](../th/README.md) | [Турски](../tr/README.md) | [Украински](../uk/README.md) | [Урду](../ur/README.md) | [Виетнамски](../vi/README.md)

> **Предпочитате да клонирате локално?**
>
> Това хранилище включва преводи на 50+ езика, които значително увеличават размера на изтеглянето. За да клонирате без преводи, използвайте sparse checkout:
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
> Това ви дава всичко необходимо за завършване на курса с много по-бързо изтегляне.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Преглед

**Co-op Translator** ви помага да локализирате вашето образователно съдържание в GitHub на множество езици без усилие.
Когато актуализирате Markdown файлове, изображения или notebooks, преводите остават автоматично синхронизирани, осигурявайки вашето съдържание да бъде точно и актуално за учащите по целия свят.

Използвайте го от CLI за превод на хранилища, от Python API за автоматизация или чрез MCP сървъра за работни потоци с агенти и редактори.

Пример за това как е организирано преведеното съдържание:

![Example](../../imgs/translation-ex.png)

## Защо Co-op Translator?

Преводът на един файл е лесен. Поддържането на цяло хранилище с докуменция
преведено, свързано и актуално е трудната част.

| Проблем | Как Co-op Translator помага |
| --- | --- |
| Long docs are not one prompt | Големите Markdown файлове се разделят на парчета, така че дълго README не зависи от един крехък отговор на модела. Ако парче се провали, Co-op Translator може да опита отново и да прераздели само неуспешната част. |
| Incomplete translations should not be marked current | Съкратен превод никога не трябва да се маркира като актуален. Co-op Translator проверява целостта на превода преди запис и може да открие структурно непълни съществуващи преводи. |
| Links should match the translated repo structure | Ръчните преводи често оставят относителни връзки, сочещи обратно към изходното дърво. Co-op Translator пренаписва връзките в Markdown, notebooks, изображения и README, за да съответстват на структурата `translations/<lang>/...`. |
| Translation should work across an entire repo | Co-op Translator обработва README файлове, документация, notebooks и текст в изображения като част от един работен поток на хранилището, вместо да превежда файловете един по един. |
| Maintaining translations matters more than creating them once | Хешовете на източника и метаданните за превод позволяват на Co-op Translator да намира остарели файлове, да пропуска непроменени файлове и да поддържа преведеното съдържание синхронизирано, докато изходното хранилище се развива. |

## Как се управлява състоянието на преводите

Co-op Translator управлява преведеното съдържание като **версионирани софтуерни артефакти**,  
не като статични файлове.

Инструментът проследява състоянието на преведения Markdown, изображения и notebooks
с помощта на **метаданни, обхващащи езика**.

Този дизайн позволява на Co-op Translator да:

- Надеждно открива остарели преводи
- Обработва Markdown, изображения и notebooks консистентно
- Масшабира безопасно в големи, бързо променящи се мултиезични хранилища

Чрез моделиране на преводите като управлявани артефакти,
работните потоци за превод естествено се съгласуват със съвременните
практики за управление на зависимости и артефакти в софтуера.

→ [How translation state is managed](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Свързани задълбочени материали

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Първи стъпки

Co-op Translator може да се използва от CLI, от Python API или от MCP сървъра. Започнете с ръководството за работни потоци, ако избирате между локален превод, автоматизация, CI и интеграция с агенти/редактори.

- [Изберете вашия работен поток](../../docs/workflows.md)
- [Конфигурирайте данните за достъп](../../docs/configuration.md)
- [Превеждайте от CLI](../../docs/cli.md)
- [Автоматизирайте с Python API](../../docs/api.md)
- [Свържете се с MCP Сървъра](../../docs/mcp.md)
- [Изпълнение в GitHub Actions](../../docs/github-actions.md)

Минимален пример за CLI след конфигурация:

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

За първите изпълнения на големи хранилища използвайте `--dry-run` преди записване на преведените файлове. Вижте [Ръководството за CLI](../../docs/cli.md) за флагове за тип съдържание, логове, преглед и миграция на връзки.

Бързо стартиране на контейнер с Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Бързо стартиране на контейнер с PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Характеристики

- Автоматизиран превод за Markdown, notebooks и изображения
- Поддържа преводите синхронизирани с промените в изходното съдържание
- Работи локално (CLI) или в CI (GitHub Actions)
- Предоставя инструменти за превод на Markdown, notebooks, изображения, преглед и проекти чрез MCP
- Използва Azure OpenAI или OpenAI за преводи, поддържани от доставчик
- Позволява на MCP да хоства агенти, които превеждат парчета от Markdown и notebooks без LLM учетни данни на Co-op Translator
- Използва Azure AI Vision за извличане и превод на текст от изображения
- Преглежда структурата и актуалността на преводите с детерминистични проверки
- Запазва форматирането и структурата на Markdown

## Документация

- [Сайт с документация](https://azure.github.io/co-op-translator/)
- [Изберете вашия работен поток](../../docs/workflows.md)
- [Конфигурация](../../docs/configuration.md)
- [Настройка на Azure AI](../../docs/azure-ai-setup.md)
- [Ръководство за CLI](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Сървър](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Шаблон за README езици](../../docs/readme-languages-template.md)
- [Поддържани езици](../../docs/supported-languages.md)
- [Приносване](../../CONTRIBUTING.md)
- [Отстраняване на проблеми](../../docs/troubleshooting.md)

### Ръководство, специфично за Microsoft
> [!NOTE]
> Само за поддържащите хранилищата на Microsoft „For Beginners“.

- [Актуализиране на списъка „other courses“ (само за MS Beginners хранилища)](../../docs/microsoft-beginners.md)

## Подкрепете ни и насърчете глобалното обучение

Присъединете се към нас в революцията на споделянето на образователно съдържание в световен мащаб! Дайте звезда на [Co-op Translator](https://github.com/azure/co-op-translator) в GitHub и подкрепете нашата мисия да премахнем езиковите бариери в обучението и технологиите. Вашият интерес и приноси имат значително въздействие! Приноси с код и предложения за функции винаги са добре дошли.

### Разгледайте образователното съдържание на Microsoft на вашия език
- [LangChain4j за начинаещи](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD за начинаещи](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI за начинаещи](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) за начинаещи](https://github.com/microsoft/mcp-for-beginners)
- [AI агенти за начинаещи](https://github.com/microsoft/ai-agents-for-beginners)
- [Генеративен AI за начинаещи с .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Генеративен AI за начинаещи](https://github.com/microsoft/generative-ai-for-beginners)
- [Генеративен AI за начинаещи с Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [Машинно обучение за начинаещи](https://aka.ms/ml-beginners)
- [Наука за данни за начинаещи](https://aka.ms/datascience-beginners)
- [Изкуствен интелект за начинаещи](https://aka.ms/ai-beginners)
- [Киберсигурност за начинаещи](https://github.com/microsoft/Security-101)
- [Уеб разработка за начинаещи](https://aka.ms/webdev-beginners)
- [IoT за начинаещи](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Видео презентации

👉 Кликнете върху изображението по-долу, за да гледате в YouTube.

- **Open at Microsoft**: Кратко 18-минутно въведение и бърз наръчник как да използвате Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Принос

Този проект приветства приноси и предложения. Заинтересовани ли сте да допринесете за Azure Co-op Translator? Моля, вижте нашия [CONTRIBUTING.md](../../CONTRIBUTING.md) за насоки как можете да помогнете Co-op Translator да бъде по-достъпен.

## Приносители

[![приносители на co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Код на поведение

Този проект е възприел [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
За повече информация вижте [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) или
свържете се с [opencode@microsoft.com](mailto:opencode@microsoft.com) за допълнителни въпроси или коментари.

## Отговорен изкуствен интелект

Microsoft се ангажира да помага на нашите клиенти да използват нашите AI продукти отговорно, да споделяме нашите уроци и да изграждаме партньорства, основани на доверие, чрез инструменти като Transparency Notes и Impact Assessments. Много от тези ресурси могат да бъдат намерени на [https://aka.ms/RAI](https://aka.ms/RAI).
Подходът на Microsoft към отговорния изкуствен интелект се основава на нашите принципи за AI: справедливост, надеждност и безопасност, поверителност и сигурност, приобщаване, прозрачност и отчетност.

Големи модели за естествен език, изображения и реч — като тези, използвани в този пример — потенциално могат да се държат по начини, които са несправедливи, ненадеждни или обидни, което от своя страна може да причини вреда. Моля, консултирайте се с [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), за да получите информация за рисковете и ограниченията.

Препоръчителният подход за смекчаване на тези рискове е да включите система за безопасност в архитектурата си, която може да открива и предотвратява вредно поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставя независим слой защита, способен да открива вредно съдържание, генерирано от потребители и от AI, в приложения и услуги. Azure AI Content Safety включва текстови и изображенчески API, които ви позволяват да откривате материал, който е вреден. Имаме също интерактивно Content Safety Studio, което ви позволява да преглеждате, изследвате и тествате примерен код за откриване на вредно съдържание в различни модалности. Следната [документация с бърз старт](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ви води през изпращането на заявки към услугата.

Друг аспект, който трябва да се вземе предвид, е общата производителност на приложението. При мултимодални и мултимоделови приложения разглеждаме производителността като това, че системата работи така, както вие и вашите потребители очакват, включително и да не генерира вредни изходи. Важно е да оцените производителността на цялото си приложение, използвайки [метрики за качество на генериране и за риск и безопасност](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Можете да оцените вашето AI приложение в развойната си среда, използвайки [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). С даден тестов набор от данни или цел, генериранията на вашето генеративно AI приложение се измерват количествено с вградени оценители или потребителски оценители по ваш избор. За да започнете с prompt flow sdk за оценка на вашата система, можете да следвате [ръководството за бърз старт](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). След като изпълните оценъчно изпълнение, можете да [визуализирате резултатите в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Търговски марки

Този проект може да съдържа търговски марки или логота за проекти, продукти или услуги. Употребата на търговски марки или логота на Microsoft е разрешена и трябва да следва
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Използването на търговски марки или логота на Microsoft в модифицирани версии на този проект не трябва да създава объркване или да предполага спонсорство от Microsoft.
Всяка употреба на търговски марки или логота на трети страни подлежи на политиките на тези трети страни.

## Получаване на помощ

Ако се блокирате или имате въпроси относно изграждането на AI приложения, присъединете се към:

[![Discord на Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ако имате обратна връзка за продукта или грешки по време на разработка посетете:

[![Форум за разработчици Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)