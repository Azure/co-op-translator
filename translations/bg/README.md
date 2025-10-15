<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:59:39+00:00",
  "source_file": "README.md",
  "language_code": "bg"
}
-->
# Co-op Translator

_Автоматизирайте лесно превода на вашето образователно GitHub съдържание на множество езици, за да достигнете до глобална аудитория._

### 🌐 Многоезична поддръжка

#### Поддържани от [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Арабски](../ar/README.md) | [Бенгалски](../bn/README.md) | [Български](./README.md) | [Бирмански (Мианмар)](../my/README.md) | [Китайски (Опростен)](../zh/README.md) | [Китайски (Традиционен, Хонконг)](../hk/README.md) | [Китайски (Традиционен, Макао)](../mo/README.md) | [Китайски (Традиционен, Тайван)](../tw/README.md) | [Хърватски](../hr/README.md) | [Чешки](../cs/README.md) | [Датски](../da/README.md) | [Нидерландски](../nl/README.md) | [Естонски](../et/README.md) | [Фински](../fi/README.md) | [Френски](../fr/README.md) | [Немски](../de/README.md) | [Гръцки](../el/README.md) | [Иврит](../he/README.md) | [Хинди](../hi/README.md) | [Унгарски](../hu/README.md) | [Индонезийски](../id/README.md) | [Италиански](../it/README.md) | [Японски](../ja/README.md) | [Корейски](../ko/README.md) | [Литовски](../lt/README.md) | [Малайски](../ms/README.md) | [Марати](../mr/README.md) | [Непалски](../ne/README.md) | [Норвежки](../no/README.md) | [Персийски (Фарси)](../fa/README.md) | [Полски](../pl/README.md) | [Португалски (Бразилия)](../br/README.md) | [Португалски (Португалия)](../pt/README.md) | [Панджаби (Гурмуки)](../pa/README.md) | [Румънски](../ro/README.md) | [Руски](../ru/README.md) | [Сръбски (Кирилица)](../sr/README.md) | [Словашки](../sk/README.md) | [Словенски](../sl/README.md) | [Испански](../es/README.md) | [Суахили](../sw/README.md) | [Шведски](../sv/README.md) | [Тагалог (Филипински)](../tl/README.md) | [Тамил](../ta/README.md) | [Тайландски](../th/README.md) | [Турски](../tr/README.md) | [Украински](../uk/README.md) | [Урду](../ur/README.md) | [Виетнамски](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Общ преглед

**Co-op Translator** ви позволява бързо да превеждате вашето образователно GitHub съдържание на множество езици, така че лесно да достигнете до международна аудитория. Когато актуализирате вашите Markdown файлове, изображения или Jupyter тетрадки, преводите се синхронизират автоматично, за да гарантират, че съдържанието ви остава актуално и полезно за потребители от цял свят.

Вижте как Co-op Translator организира преведеното образователно съдържание в GitHub:

![Пример](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.bg.png)

## Бърз старт

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

## Минимална настройка

- Създайте `.env`, използвайки шаблона: [.env.template](../../.env.template)
- Конфигурирайте един LLM доставчик (Azure OpenAI или OpenAI)
- За превод на изображения (`-img`), настройте и Azure AI Vision
- Препоръчително: Ако имате преводи, генерирани с други инструменти, изчистете ги предварително, за да избегнете конфликти (например: `translations/`).
- Препоръчително: Добавете секция с преводи към вашия README, използвайки [README languages template](./README_languages_template.md)
- Вижте: [Настройка на Azure AI](./getting_started/set-up-azure-ai.md)

## Използване

Превод на всички поддържани типове:

```bash
translate -l "ko ja"
```

Само Markdown:

```bash
translate -l "de" -md
```

Markdown + изображения:

```bash
translate -l "pt" -md -img
```

Само тетрадки:

```bash
translate -l "zh" -nb
```

Още флагове: [Command reference](./getting_started/command-reference.md)

## Възможности

- Автоматизиран превод на Markdown, тетрадки и изображения
- Поддържа преводите в синхрон с промените в изходния файл
- Работи локално (CLI) или в CI (GitHub Actions)
- Използва Azure OpenAI или OpenAI; по желание Azure AI Vision за изображения
- Запазва форматирането и структурата на Markdown

## Документация

- [Ръководство за командния ред](./getting_started/command-line-guide/command-line-guide.md)
- [Ръководство за GitHub Actions (Публични репозитории и стандартни тайни)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Ръководство за GitHub Actions (Репозитории на Microsoft организация и настройки на ниво организация)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Поддържани езици](./getting_started/supported-languages.md)
- [Отстраняване на проблеми](./getting_started/troubleshooting.md)

## Подкрепете ни и насърчете глобалното обучение

Присъединете се към нас в революционизирането на споделянето на образователно съдържание по света! Дайте ⭐ на [Co-op Translator](https://github.com/azure/co-op-translator) в GitHub и подкрепете нашата мисия да премахнем езиковите бариери в обучението и технологиите. Вашият интерес и принос имат голямо значение! Винаги са добре дошли предложения за нови функции и кодови допълнения.

### Открийте образователно съдържание на Microsoft на вашия език

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

## Видео презентации

Научете повече за Co-op Translator чрез нашите презентации _(Кликнете върху изображението по-долу, за да гледате в YouTube.)_:

- **Open at Microsoft**: Кратко 18-минутно въведение и бързо ръководство за използване на Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.bg.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Принос

Този проект приветства предложения и допълнения. Искате да допринесете към Azure Co-op Translator? Вижте нашия [CONTRIBUTING.md](./CONTRIBUTING.md) за насоки как можете да помогнете Co-op Translator да стане по-достъпен.

## Сътрудници

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Етичен кодекс

Този проект е приел [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
За повече информация вижте [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) или
се свържете с [opencode@microsoft.com](mailto:opencode@microsoft.com) при допълнителни въпроси или коментари.

## Отговорен AI

Microsoft се ангажира да помага на клиентите си да използват AI продуктите отговорно, да споделя наученото и да изгражда доверие чрез инструменти като Transparency Notes и Impact Assessments. Много от тези ресурси са достъпни на [https://aka.ms/RAI](https://aka.ms/RAI).
Подходът на Microsoft към отговорния AI се основава на принципите ни за справедливост, надеждност и безопасност, поверителност и сигурност, приобщаване, прозрачност и отчетност.

Мащабните модели за естествен език, изображения и реч – като тези, използвани в този пример – могат понякога да се държат несправедливо, ненадеждно или обидно, което може да причини вреди. Моля, запознайте се с [Transparency note за Azure OpenAI service](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), за да сте информирани за рисковете и ограниченията.

Препоръчителният подход за намаляване на тези рискове е да включите система за безопасност във вашата архитектура, която да открива и предотвратява вредно поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставя независим слой защита, който може да открива вредно съдържание, генерирано от потребители и AI, в приложения и услуги. Azure AI Content Safety включва API за текст и изображения, които ви позволяват да откривате вредни материали. Имаме и интерактивно Content Safety Studio, където можете да разглеждате и тествате примерен код за откриване на вредно съдържание в различни формати. Следната [документация за бърз старт](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ще ви преведе през изпращането на заявки към услугата.


Друг аспект, който трябва да се вземе предвид, е цялостната производителност на приложението. При мултимодални и многомоделни приложения, производителността означава, че системата работи според очакванията на вас и вашите потребители, включително да не генерира вредни резултати. Важно е да оцените производителността на цялото си приложение с помощта на [метрики за качество на генериране, риск и безопасност](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Можете да оцените вашето AI приложение в средата за разработка с помощта на [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Като използвате тестов набор от данни или цел, генерираните резултати от вашето генеративно AI приложение се измерват количествено с вградени или персонализирани оценители по ваш избор. За да започнете с prompt flow sdk и да оцените системата си, следвайте [ръководството за бърз старт](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). След като изпълните оценка, можете да [визуализирате резултатите в Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Търговски марки

Този проект може да съдържа търговски марки или лога на проекти, продукти или услуги. Разрешената употреба на търговски марки или лога на Microsoft подлежи на и трябва да следва
[Указанията за търговски марки и бранд на Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Използването на търговски марки или лога на Microsoft в модифицирани версии на този проект не трябва да създава объркване или да внушава спонсорство от Microsoft.
Всяка употреба на търговски марки или лога на трети страни подлежи на политиките на съответната трета страна.

## Помощ

Ако се затрудните или имате въпроси относно създаването на AI приложения, присъединете се към:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ако имате обратна връзка за продукта или срещнете грешки по време на разработката, посетете:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Отказ от отговорност**:
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни тълкувания, произтичащи от използването на този превод.