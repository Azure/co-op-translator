# Co-op Translator

_Просте автоматизоване підтримання перекладів вашого освітнього вмісту на GitHub кількома мовами в міру розвитку вашого проєкту._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Пакет Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Ліцензія: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Завантаження](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Завантаження](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Контейнер: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Стиль коду: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Співавтори GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Проблеми GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull-запити GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![ПР вітаються](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Почніть тут:** [Виберіть робочий процес](https://azure.github.io/co-op-translator/workflows/) | [Конфігурація](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Підтримка кількох мов

#### Підтримується [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Арабська](../ar/README.md) | [Бенгальська](../bn/README.md) | [Болгарська](../bg/README.md) | [Бірманська (М'янма)](../my/README.md) | [Китайська (спрощена)](../zh-CN/README.md) | [Китайська (традиційна, Гонконг)](../zh-HK/README.md) | [Китайська (традиційна, Макао)](../zh-MO/README.md) | [Китайська (традиційна, Тайвань)](../zh-TW/README.md) | [Хорватська](../hr/README.md) | [Чеська](../cs/README.md) | [Данська](../da/README.md) | [Нідерландська](../nl/README.md) | [Естонська](../et/README.md) | [Фінська](../fi/README.md) | [Французька](../fr/README.md) | [Німецька](../de/README.md) | [Грецька](../el/README.md) | [Іврит](../he/README.md) | [Хінді](../hi/README.md) | [Угорська](../hu/README.md) | [Індонезійська](../id/README.md) | [Італійська](../it/README.md) | [Японська](../ja/README.md) | [Каннада](../kn/README.md) | [Кхмерська](../km/README.md) | [Корейська](../ko/README.md) | [Литовська](../lt/README.md) | [Малайська](../ms/README.md) | [Малаялам](../ml/README.md) | [Маратхі](../mr/README.md) | [Непалі](../ne/README.md) | [Нігерійський підін](../pcm/README.md) | [Норвезька](../no/README.md) | [Перська (фарсі)](../fa/README.md) | [Польська](../pl/README.md) | [Португальська (Бразилія)](../pt-BR/README.md) | [Португальська (Португалія)](../pt-PT/README.md) | [Пенджабі (гурмухі)](../pa/README.md) | [Румунська](../ro/README.md) | [Російська](../ru/README.md) | [Сербська (кирилиця)](../sr/README.md) | [Словацька](../sk/README.md) | [Словенська](../sl/README.md) | [Іспанська](../es/README.md) | [Суахілі](../sw/README.md) | [Шведська](../sv/README.md) | [Тагальська (філіппінська)](../tl/README.md) | [Тамільська](../ta/README.md) | [Телугу](../te/README.md) | [Тайська](../th/README.md) | [Турецька](../tr/README.md) | [Українська](./README.md) | [Урду](../ur/README.md) | [В'єтнамська](../vi/README.md)

> **Віддаєте перевагу клонувати локально?**
>
> Цей репозиторій містить понад 50 перекладів мов, що значно збільшує розмір завантаження. Щоб клонувати без перекладів, використовуйте розріджене витягнення (sparse checkout):
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
> Це дає вам усе необхідне для завершення курсу з набагато швидшим завантаженням.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Спостерігачі GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Форки GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Зірки GitHub](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Огляд

**Co-op Translator** допомагає вам локалізувати ваш освітній вміст на GitHub кількома мовами без зусиль.
Коли ви оновлюєте свої Markdown-файли, зображення або ноутбуки, переклади автоматично синхронізуються, що забезпечує точність і актуальність вашого вмісту для студентів у всьому світі.

Використовуйте його з CLI для перекладу репозиторію, через Python API для автоматизації або через MCP server для робочих процесів з агентами та редакторами.

Приклад того, як організовано перекладений вміст:

![Приклад](../../imgs/translation-ex.png)

## Чому Co-op Translator?

Перекласти один файл — легко. Підтримувати перекладений, пов’язаний і актуальний цілий репозиторій документації — складніше.

| Проблема | Як Co-op Translator допомагає |
| --- | --- |
| Long docs are not one prompt | Великі Markdown-файли розбиваються на частини, тож довгий README не залежить від однієї крихкої відповіді моделі. Якщо частина не вдається, Co-op Translator може повторити спробу та повторно розбити лише невдалу частину. |
| Incomplete translations should not be marked current | Обрізаний переклад ніколи не повинен позначатися як актуальний. Co-op Translator перевіряє цілісність перекладу перед збереженням і може виявляти структурно некоректні існуючі переклади. |
| Links should match the translated repo structure | Ручні переклади часто залишають відносні посилання, що ведуть до джерельного дерева. Co-op Translator переписує посилання в Markdown, ноутбуках, зображеннях і README, щоб вони відповідали структурі `translations/<lang>/...`. |
| Translation should work across an entire repo | Co-op Translator обробляє README, документацію, ноутбуки та текст зображень як частину єдиного робочого процесу репозиторію, замість перекладу файлів по одному. |
| Maintaining translations matters more than creating them once | Хеші джерела та метадані перекладу дозволяють Co-op Translator знаходити застарілі файли, пропускати незмінені файли та підтримувати синхронізацію перекладеного вмісту в міру розвитку джерельного репозиторію. |

## Як керується стан перекладу

Co-op Translator керує перекладеним вмістом як **версійованими програмними артефактами**,  
а не як статичними файлами.

Інструмент відстежує стан перекладених Markdown, зображень і ноутбуків
використовуючи **метадані, обмежені мовою**.

Такий підхід дозволяє Co-op Translator:

- Надійно виявляти застарілі переклади
- Узгоджено обробляти Markdown, зображення та ноутбуки
- Масштабуватися безпечно по великих, швидкорухомих багатомовних репозиторіях

Моделюючи переклади як керовані артефакти,
робочі процеси перекладу природно узгоджуються з сучасними
практиками управління залежностями та артефактами програмного забезпечення.

→ [Як керується стан перекладу](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Пов'язані детальні матеріали

- [Виправлення зламаного Markdown в AI-перекладі: зміцнення виробничого конвеєра](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Початок роботи

Co-op Translator можна використовувати з CLI, через Python API або на MCP server. Почніть з посібника з робочих процесів, якщо ви обираєте між локальним перекладом, автоматизацією, CI та інтеграцією агентів/редакторів.

- [Виберіть робочий процес](../../docs/workflows.md)
- [Налаштування облікових даних](../../docs/configuration.md)
- [Переклад з CLI](../../docs/cli.md)
- [Автоматизація з Python API](../../docs/api.md)
- [Підключення до MCP Server](../../docs/mcp.md)
- [Запуск в GitHub Actions](../../docs/github-actions.md)

Мінімальний приклад CLI після налаштування:

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

Для перших запусків у великих репозиторіях використовуйте `--dry-run` перед записом перекладених файлів. Дивіться [Довідник CLI](../../docs/cli.md) щодо прапорців для типів вмісту, журналів, перегляду та міграції посилань.

Швидкий запуск контейнера з Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Швидкий запуск контейнера з PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Можливості

- Автоматизований переклад для Markdown, ноутбуків і зображень
- Підтримка синхронізації перекладів із змінами джерела
- Працює локально (CLI) або в CI (GitHub Actions)
- Надає інструменти для перекладу Markdown, ноутбуків, зображень, перегляду й проєктів через MCP
- Підтримує переклад з використанням Azure OpenAI або OpenAI
- Дозволяє MCP хостити агентів для перекладу частин Markdown і ноутбуків без облікових даних LLM Co-op Translator
- Використовує Azure AI Vision для витягання тексту із зображень та перекладу
- Перевіряє структуру та актуальність перекладів детерміністичними перевірками
- Зберігає форматування та структуру Markdown

## Документація

- [Сайт документації](https://azure.github.io/co-op-translator/)
- [Виберіть робочий процес](../../docs/workflows.md)
- [Конфігурація](../../docs/configuration.md)
- [Налаштування Azure AI](../../docs/azure-ai-setup.md)
- [Довідник CLI](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Шаблон README мов](../../docs/readme-languages-template.md)
- [Підтримувані мови](../../docs/supported-languages.md)
- [Участь у проєкті](../../CONTRIBUTING.md)
- [Усунення неполадок](../../docs/troubleshooting.md)

### Керівництво, специфічне для Microsoft
> [!NOTE]
> Тільки для супроводжувачів репозиторіїв Microsoft “For Beginners”.

- [Оновлення списку «інші курси» (лише для репозиторіїв MS Beginners)](../../docs/microsoft-beginners.md)

## Підтримайте нас та сприяйте глобальному навчанню

Приєднуйтесь до нас у революції обміну освітнім контентом у світі! Поставте ⭐ [Co-op Translator](https://github.com/azure/co-op-translator) на GitHub та підтримаєте нашу місію руйнування мовних бар’єрів у навчанні та технологіях. Ваш інтерес і внески мають велике значення! Внески в код і пропозиції щодо функцій завжди вітаються.

### Досліджуйте освітній контент Microsoft вашою мовою
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Відеопрезентації

👉 Натисніть на зображення нижче, щоб переглянути на YouTube.

- **Open at Microsoft**: коротке 18-хвилинне введення та швидкий посібник щодо того, як користуватися Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Участь у проєкті

Цей проєкт вітає внески та пропозиції. Бажаєте долучитися до Azure Co-op Translator? Будь ласка, перегляньте наш [CONTRIBUTING.md](../../CONTRIBUTING.md) для отримання вказівок про те, як ви можете допомогти зробити Co-op Translator більш доступним.

## Учасники

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс поведінки

Цей проєкт прийняв [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Для отримання додаткової інформації див. [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) або
зв’яжіться з [opencode@microsoft.com](mailto:opencode@microsoft.com) з будь-якими додатковими питаннями чи зауваженнями.

## Відповідальний ШІ

Microsoft прагне допомагати нашим клієнтам відповідально використовувати наші продукти на основі ШІ, ділитися нашим досвідом і будувати партнерські стосунки, засновані на довірі, за допомогою інструментів, таких як примітки про прозорість і оцінки впливу. Багато з цих ресурсів доступні за адресою [https://aka.ms/RAI](https://aka.ms/RAI).
Підхід Microsoft до відповідального ШІ ґрунтується на наших принципах ШІ: справедливість, надійність і безпека, конфіденційність і захист, інклюзивність, прозорість і підзвітність.

Великі моделі для обробки мови, зображень і мовлення — як ті, що використовуються в цьому прикладі — можуть потенційно поводитися несправедливо, ненадійно або образливо, що може призвести до шкоди. Будь ласка, ознайомтеся з [приміткою про прозорість служби Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), щоб дізнатися про ризики та обмеження.

Рекомендований підхід до зменшення цих ризиків — включити в архітектуру систему безпеки, яка може виявляти та запобігати шкідливій поведінці. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) забезпечує незалежний рівень захисту, здатний виявляти шкідливий контент, створений користувачами або штучним інтелектом, в додатках і службах. Azure AI Content Safety включає текстові та зображенні API, що дозволяють виявляти матеріали, які є шкідливими. У нас також є інтерактивний Content Safety Studio, який дозволяє переглядати, досліджувати та випробовувати приклади коду для виявлення шкідливого контенту в різних модальностях. Наступна [документація quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) проводить вас через процес надсилання запитів до служби.

Ще один аспект, який слід враховувати, — це загальна продуктивність застосунку. У багатомодальних і багатомодельних застосунках продуктивність означає, що система працює так, як ви та ваші користувачі очікуєте, включно з тим, щоб не генерувати шкідливі результати. Важливо оцінювати продуктивність вашого застосунку в цілому, використовуючи [метрики якості генерації та ризиків і безпеки](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Ви можете оцінити ваш AI-застосунок у середовищі розробки, використовуючи [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). За наявності тестового набору даних або цілі ваші генерації в генеративному AI-застосунку кількісно вимірюються вбудованими або користувацькими оцінювачами на ваш вибір. Щоб почати роботу з prompt flow SDK для оцінки вашої системи, ви можете слідувати [швидкому посібнику (quickstart guide)](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Після виконання запуску оцінки ви можете [візуалізувати результати в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торгові марки

Цей проєкт може містити торгові марки або логотипи проєктів, продуктів або послуг. Дозволене використання торгових марок або логотипів Microsoft підлягає умовам і має відповідати
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Використання торгових марок або логотипів Microsoft у змінених версіях цього проєкту не повинно вводити в оману або натякати на спонсорство Microsoft.
Будь-яке використання торгових марок або логотипів третіх сторін підпорядковується правилам відповідних третіх сторін.

## Отримання допомоги

Якщо ви застрягли або маєте питання щодо створення AI-додатків, приєднуйтесь:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Якщо у вас є відгуки про продукт або ви натрапили на помилки під час розробки, відвідайте:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)