# Co-op Translator

_Лако аутоматизујте и одржавајте преводе за ваш едукативни GitHub садржај на више језика како ваш пројекат расте._

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

**Почните овде:** [Choose your workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Подршка за више језика

#### Подржано од стране [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Арапски](../ar/README.md) | [Бенгалски](../bn/README.md) | [Бугарски](../bg/README.md) | [Бирмански (Мјанмар)](../my/README.md) | [Кинески (поједностављени)](../zh-CN/README.md) | [Кинески (традиционални, Хонг Конг)](../zh-HK/README.md) | [Кинески (традиционални, Макао)](../zh-MO/README.md) | [Кинески (традиционални, Тајван)](../zh-TW/README.md) | [Хрватски](../hr/README.md) | [Чешки](../cs/README.md) | [Дански](../da/README.md) | [Холандски](../nl/README.md) | [Естонски](../et/README.md) | [Фински](../fi/README.md) | [Француски](../fr/README.md) | [Немачки](../de/README.md) | [Грчки](../el/README.md) | [Хебрејски](../he/README.md) | [Хинди](../hi/README.md) | [Мађарски](../hu/README.md) | [Индонежански](../id/README.md) | [Италијански](../it/README.md) | [Јапански](../ja/README.md) | [Каннада](../kn/README.md) | [Кмерски](../km/README.md) | [Корејски](../ko/README.md) | [Литвански](../lt/README.md) | [Малајски](../ms/README.md) | [Малајалам](../ml/README.md) | [Марати](../mr/README.md) | [Непалски](../ne/README.md) | [Нигеријски пидгин](../pcm/README.md) | [Норвешки](../no/README.md) | [Персијски (фарси)](../fa/README.md) | [Пољски](../pl/README.md) | [Португалски (Бразил)](../pt-BR/README.md) | [Португалски (Португалија)](../pt-PT/README.md) | [Пуњаби (Гурумки)](../pa/README.md) | [Румунски](../ro/README.md) | [Руски](../ru/README.md) | [Српски (ћирилица)](./README.md) | [Словачки](../sk/README.md) | [Словеначки](../sl/README.md) | [Шпански](../es/README.md) | [Свахили](../sw/README.md) | [Шведски](../sv/README.md) | [Тагалог (Филипински)](../tl/README.md) | [Тамилски](../ta/README.md) | [Телугу](../te/README.md) | [Тајландски](../th/README.md) | [Турски](../tr/README.md) | [Украјински](../uk/README.md) | [Урду](../ur/README.md) | [Вијетнамски](../vi/README.md)

> **Преферирате да клонирате локално?**
>
> Овај репозиторјум садржи преко 50 превода што значајно повећава величину преузимања. Да бисте клонирали без превода, користите sparse checkout:
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
> Ово вам даје све што вам је потребно да завршите курс уз знатно брже преузимање.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Преглед

**Co-op Translator** вам помаже да локализујете ваш едукативни GitHub садржај на више језика без напора.
Када ажурирате Markdown датотеке, слике или бележнице, преводи остају аутоматски синхронизовани, осигуравајући да ваш садржај буде тачан и ажуран за ученике широм света.

Користите га из CLI за превод репозиторијума, из Python API за аутоматизацију или кроз MCP сервер за агентске и уређивачке токове рада.

Example of how translated content is organized:

![Example](../../imgs/translation-ex.png)

## Зашто Co-op Translator?

Превођење једне датотеке је лако. Одржавање целог репозиторијума документације
преведеног, повезаног и ажурног је тешки део.

| Problem | How Co-op Translator helps |
| --- | --- |
| Дуге документације нису један промпт | Велике Markdown датотеке се деле на делове, тако да дуг README не зависи од једног крхког одговора модела. Ако део не успе, Co-op Translator може поново покушати и поново протумачити само неуспели део. |
| Непотпуни преводи не би требало да буду означени као тренутни | Скраћени превод никада не би требало да буде означен као ажуран. Co-op Translator проверава интегритет превода пре чувања и може открити структурно непотпуне постојеће преводе. |
| Линкови треба да одговарају преведеном структури репозиторијума | Ручни преводи често остављају релативне линкове који упућују на изворно дрво. Co-op Translator преписује Markdown, бележнице, слике и README линкове да одговарају структури `translations/<lang>/...`. |
| Превод треба да функционише кроз цео репозиторијум | Co-op Translator обрађује README датотеке, документе, бележнице и текст на сликама као део једног радног тока репозиторијума, уместо да преводи датотеке једну по једну. |
| Одржавање превода је важније од једнократног креирања | Хешеви извора и метаподаци о преводу омогућавају Co-op Translator-у да пронађе застареле датотеке, прескочи непромењене датотеке и одржава преведени садржај синхронизован како се изворни репо развија. |

## Како се управља статусом превода

Co-op Translator управља преведеним садржајем као **верзионисаним софтверским артефактима**,  
а не као статичним датотекама.

Алат прати статус преведеног Markdown-а, слика и бележница
користећи **метаподаце по језику**.

Овај дизајн омогућава Co-op Translator-у да:

- Поуздано открије застареле преводе
- Третира Markdown, слике и бележнице доследно
- Безбедно скалира преко великих, брзо мењајућих се, вишечланских репозиторијума

Моделирањем превода као управљаних артефаката,
токови рада за превод природно се усклађују са модерним
практикама управљања зависностима и артефактима софтвера.

→ [Како се управља статусом превода](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Повезани детаљније анализе

- [Поправљање поквареног Markdown-а у AI преводу: Ојачавање продукцијског процеса](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Почните

Co-op Translator се може користити из CLI-а, Python API-ја или MCP сервера. Почните са водичем за ток рада ако бирате између локалног превода, аутоматизације, CI и интеграције агената/уредника.

- [Одаберите ваш ток рада](../../docs/workflows.md)
- [Конфигуришите акредитиве](../../docs/configuration.md)
- [Преведите из CLI-а](../../docs/cli.md)
- [Аутоматизујте са Python API-јем](../../docs/api.md)
- [Повежите се са MCP сервером](../../docs/mcp.md)
- [Покрените у GitHub Actions](../../docs/github-actions.md)

Минималан пример из CLI-а након конфигурације:

```bash
python -m venv .venv
# Виндоус
.venv\Scripts\activate
# макОС/Линукс
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

За прва покретања на великим репозиторијумима, користите `--dry-run` пре него што се преведене датотеке запишу. Погледајте [CLI Reference](../../docs/cli.md) за ознаке типова садржаја, логове, преглед и миграцију линкова.

Брзо покретање у контејнеру са Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Брзо покретање у контејнеру са PowerShell-ом:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Карактеристике

- Аутоматизован превод за Markdown, бележнице и слике
- Одржава преводе синхронизованим са променама извора
- Ради локално (CLI) или у CI-у (GitHub Actions)
- Обезбеђује алате за превођење Markdown-а, бележница, слика, прегледа и пројекта кроз MCP
- Користи Azure OpenAI или OpenAI као провајдере за превод
- Омогућава MCP-у да хостује агенте који преводе делове Markdown-а и бележница без Co-op Translator LLM акредитива
- Користи Azure AI Vision за екстраховање текста са слика и превод
- Прегледа структуру и свежину превода детерминистичким проверама
- Чува Markdown форматирање и структуру

## Документација

- [Документациони сајт](https://azure.github.io/co-op-translator/)
- [Одаберите ваш ток рада](../../docs/workflows.md)
- [Конфигурација](../../docs/configuration.md)
- [Azure AI Подешавање](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README шаблон за језике](../../docs/readme-languages-template.md)
- [Подржани језици](../../docs/supported-languages.md)
- [Учествовање](../../CONTRIBUTING.md)
- [Отстрањавање проблема](../../docs/troubleshooting.md)

### Водич специфичан за Microsoft
> [!NOTE]
> Само за одржаваоце Microsoft „For Beginners“ репозиторијума.

- [Ажурирање листе „other courses“ (само за MS Beginners репозиторијуме)](../../docs/microsoft-beginners.md)

## Подржите нас и подржите глобално учење

Придружите нам се у револуционисању начина на који се едукативни садржај дели глобално! Дајте [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ на GitHub-у и подржите нашу мисију смањења језичких баријера у учењу и технологији. Ваш интерес и доприноси имају значајан утицај! Кодни доприноси и предлози функција су увек добродошли.

### Истражите Microsoft едукативни садржај на вашем језику
- [LangChain4j за почетнике](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD за почетнике](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI за почетнике](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) за почетнике](https://github.com/microsoft/mcp-for-beginners)
- [AI агенти за почетнике](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI за почетнике користећи .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI за почетнике](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI за почетнике користећи Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML за почетнике](https://aka.ms/ml-beginners)
- [Data Science за почетнике](https://aka.ms/datascience-beginners)
- [AI за почетнике](https://aka.ms/ai-beginners)
- [Кибербезбедност за почетнике](https://github.com/microsoft/Security-101)
- [Веб развој за почетнике](https://aka.ms/webdev-beginners)
- [IoT за почетнике](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Видеопрезентације

👉 Кликните на слику испод да гледате на YouTube.

- **Отворено у Microsoft-у**: Кратак 18-минутни увод и брзи водич како да користите Co-op Translator.

  [![Отворено у Microsoft-у](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Доприноси

Овај пројекат поздравља доприносе и предлоге. Желите да допринесете Azure Co-op Translator-у? Погледајте наш [CONTRIBUTING.md](../../CONTRIBUTING.md) за смернице о томе како можете помоћи да Co-op Translator буде приступачнији.

## Сарадници

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс понашања

Овај пројекат је усвојио [Microsoft-ов кодекс понашања за отворени код](https://opensource.microsoft.com/codeofconduct/).
За више информација погледајте [Често постављана питања о кодексу понашања](https://opensource.microsoft.com/codeofconduct/faq/) или
контактирајте [opencode@microsoft.com](mailto:opencode@microsoft.com) за додатна питања или коментаре.

## Одговорна вештачка интелигенција

Microsoft је посвећен помагању нашим купцима да користе наше AI производе на одговоран начин, дељењу наших сазнања и изградњи партнерстава заснованих на поверењу кроз алате као што су Transparency Notes и Impact Assessments. Многи од ових ресурса могу се пронаћи на [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft-ов приступ одговорној вештачкој интелигенцији заснован је на нашим AI принципима праведности, поузданости и безбедности, приватности и сигурности, инклузивности, транспарентности и одговорности.

Великомасивни модели природног језика, слика и говора — као они који се користе у овом примеру — потенцијално могу да се понашају на начине који су неправедни, непоуздани или увредљиви, што може проузроковати штету. Молимо вас да консултујете [Напомену о транспарентности услуге Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) како бисте били информисани о ризицима и ограничењима.

Препоручени приступ за ублажавање ових ризика је укључивање безбедносног система у вашу архитектуру који може да открије и спречи штетно понашање. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) обезбеђује независни слој заштите, способан да открије штетни кориснички и AI генерисани садржај у апликацијама и услугама. Azure AI Content Safety укључује текстуалне и сликовне API-је који вам омогућавају да детектујете материјал који је штетан. Такође имамо интерактивни Content Safety Studio који вам омогућава да прегледате, истражите и испробате пример кода за откривање штетног садржаја у различитим модалитетима. Следећа [документација за брзи почетак](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) вас води кроз прављење захтева ка услузи.

Још један аспект који треба узети у обзир је укупна перформанса апликације. Код мултимодалних и апликација које користе више модела, перформанса подразумева да систем ради онако како ви и ваши корисници очекујете, укључујући и негенерисање штетних излаза. Важно је проценити перформансу ваше целокупне апликације користећи [метрике квалитета генерисања и метрике ризика и безбедности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Можете оцењивати вашу AI апликацију у развојном окружењу користећи [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Са тест скупом података или циљем, генерације ваше генеративне AI апликације квантитативно се мере уграђеним или прилагођеним евалуаторима по вашем избору. Да бисте започели са prompt flow sdk за процену вашег система, можете пратити [водич за брзи почетак](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Када извршите покретање евалуације, можете [визуализовати резултате у Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Заштитни знаци

Овај пројекат може да садржи заштићене називе или логотипе за пројекте, производе или услуге. Овлашћена употреба Microsoft-ових
заштитних знакова или логотипа подлеже и мора да се придржава
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Употреба Microsoft-ових заштићених назива или логотипа у модификованим верзијама овог пројекта не сме да изазове забуну нити да имплицира да Microsoft спонзорише пројекат.
Свака употреба трећепартних заштићених назива или логотипа подлеже правилима тих трећих страна.

## Добијање помоћи

Ако запнете или имате било каквих питања о прављењу AI апликација, придружите се:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ако имате повратне информације о производу или грешке током развоја посетите:

[![Форум програмера Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)