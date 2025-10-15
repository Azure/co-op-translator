<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T04:02:32+00:00",
  "source_file": "README.md",
  "language_code": "sr"
}
-->
# Ко-оп Преводилац

_Аутоматизујте превођење вашег едукативног GitHub садржаја на више језика и доприте до глобалне публике._

### 🌐 Подршка за више језика

#### Подржава [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Арапски](../ar/README.md) | [Бенгалски](../bn/README.md) | [Бугарски](../bg/README.md) | [Бурмански (Мјанмар)](../my/README.md) | [Кинески (поједностављени)](../zh/README.md) | [Кинески (традиционални, Хонг Конг)](../hk/README.md) | [Кинески (традиционални, Макао)](../mo/README.md) | [Кинески (традиционални, Тајван)](../tw/README.md) | [Хрватски](../hr/README.md) | [Чешки](../cs/README.md) | [Дански](../da/README.md) | [Холандски](../nl/README.md) | [Естонски](../et/README.md) | [Фински](../fi/README.md) | [Француски](../fr/README.md) | [Немачки](../de/README.md) | [Грчки](../el/README.md) | [Хебрејски](../he/README.md) | [Хинди](../hi/README.md) | [Мађарски](../hu/README.md) | [Индонежански](../id/README.md) | [Италијански](../it/README.md) | [Јапански](../ja/README.md) | [Корејски](../ko/README.md) | [Литвански](../lt/README.md) | [Малајски](../ms/README.md) | [Марати](../mr/README.md) | [Непалски](../ne/README.md) | [Норвешки](../no/README.md) | [Персијски (фарси)](../fa/README.md) | [Пољски](../pl/README.md) | [Португалски (Бразил)](../br/README.md) | [Португалски (Португалија)](../pt/README.md) | [Пунџаби (Гурмуки)](../pa/README.md) | [Румунски](../ro/README.md) | [Руски](../ru/README.md) | [Српски (ћирилица)](./README.md) | [Словачки](../sk/README.md) | [Словеначки](../sl/README.md) | [Шпански](../es/README.md) | [Свахили](../sw/README.md) | [Шведски](../sv/README.md) | [Тагалог (Филипински)](../tl/README.md) | [Тамилски](../ta/README.md) | [Тајландски](../th/README.md) | [Турски](../tr/README.md) | [Украјински](../uk/README.md) | [Урду](../ur/README.md) | [Вијетнамски](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Преглед

**Co-op Translator** вам омогућава да брзо преведете ваш едукативни GitHub садржај на више језика и лако допрете до светске публике. Када ажурирате ваше Markdown датотеке, слике или Jupyter свеске, преводи се аутоматски синхронизују како би ваш едукативни садржај увек био свеж и релевантан за кориснике широм света.

Погледајте како Co-op Translator организује преведени едукативни GitHub садржај:

![Пример](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.sr.png)

## Брзи почетак

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

## Минимална подешавања

- Креирајте `.env` користећи шаблон: [.env.template](../../.env.template)
- Подесите једног LLM провајдера (Azure OpenAI или OpenAI)
- За превођење слика (`-img`), подесите и Azure AI Vision
- Препорука: Ако већ имате преводе направљене другим алатима, прво их уклоните да избегнете конфликте (на пример: `translations/`).
- Препорука: Додајте секцију са преводима у ваш README користећи [README шаблон за језике](./README_languages_template.md)
- Погледајте: [Подешавање Azure AI](./getting_started/set-up-azure-ai.md)

## Коришћење

Преведите све подржане типове:

```bash
translate -l "ko ja"
```

Само Markdown:

```bash
translate -l "de" -md
```

Markdown + слике:

```bash
translate -l "pt" -md -img
```

Само свеске:

```bash
translate -l "zh" -nb
```

Више опција: [Референца команди](./getting_started/command-reference.md)

## Могућности

- Аутоматско превођење Markdown-а, свески и слика
- Држи преводе усклађене са изворним изменама
- Ради локално (CLI) или у CI (GitHub Actions)
- Користи Azure OpenAI или OpenAI; опционо Azure AI Vision за слике
- Чува Markdown формат и структуру

## Документација

- [Водич за командну линију](./getting_started/command-line-guide/command-line-guide.md)
- [Водич за GitHub Actions (Јавни репозиторијуми и стандардне лозинке)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Водич за GitHub Actions (Microsoft организациони репозиторијуми и организациона подешавања)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Подржани језици](./getting_started/supported-languages.md)
- [Решавање проблема](./getting_started/troubleshooting.md)

## Подржите нас и ширите глобално учење

Придружите нам се у револуционисању начина на који се едукативни садржај дели широм света! Дајте [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ на GitHub-у и подржите нашу мисију рушења језичких баријера у учењу и технологији. Ваш интересовање и доприноси имају велики значај! Доприноси у коду и предлози за нове функције су увек добродошли.

### Истражите Microsoft едукативни садржај на вашем језику

- [AZD за почетнике](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI за почетнике](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) за почетнике](https://github.com/microsoft/mcp-for-beginners)
- [AI агенти за почетнике](https://github.com/microsoft/ai-agents-for-beginners)
- [Генеративни AI за почетнике уз .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Генеративни AI за почетнике](https://github.com/microsoft/generative-ai-for-beginners)
- [Генеративни AI за почетнике уз Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [Машинско учење за почетнике](https://aka.ms/ml-beginners)
- [Наука о подацима за почетнике](https://aka.ms/datascience-beginners)
- [AI за почетнике](https://aka.ms/ai-beginners)
- [Кибер безбедност за почетнике](https://github.com/microsoft/Security-101)
- [Веб развој за почетнике](https://aka.ms/webdev-beginners)
- [IoT за почетнике](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Видео презентације

Сазнајте више о Co-op Translator-у кроз наше презентације _(Кликните на слику испод да гледате на YouTube.)_:

- **Open at Microsoft**: Кратак 18-минутни увод и брзи водич за коришћење Co-op Translator-а.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.sr.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Допринос

Овај пројекат је отворен за доприносе и предлоге. Желите да допринесете Azure Co-op Translator-у? Погледајте наш [CONTRIBUTING.md](./CONTRIBUTING.md) за смернице како можете помоћи да Co-op Translator буде приступачнији.

## Доприносиоци

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс понашања

Овај пројекат је усвојио [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
За више информација погледајте [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) или
контактирајте [opencode@microsoft.com](mailto:opencode@microsoft.com) за додатна питања или коментаре.

## Одговорна AI

Microsoft је посвећен томе да помогне корисницима да одговорно користе наше AI производе, дели наша искуства и гради партнерства заснована на поверењу кроз алате као што су Transparency Notes и Impact Assessments. Многи од ових ресурса су доступни на [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft-ов приступ одговорној AI заснива се на нашим AI принципима: правичност, поузданост и безбедност, приватност и сигурност, инклузивност, транспарентност и одговорност.

Велики језички, сликовни и говорни модели – као они који се користе у овом примеру – могу понекад да се понашају непредвидиво, непоуздано или увредљиво, што може довести до штетних последица. Молимо вас да прочитате [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) како бисте били информисани о ризицима и ограничењима.

Препоручени начин за ублажавање ових ризика је да у архитектуру укључите систем безбедности који може да открије и спречи штетно понашање. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) пружа независан слој заштите, способан да открије штетан садржај који генеришу корисници или AI у апликацијама и сервисима. Azure AI Content Safety укључује API-је за текст и слике који вам омогућавају да откријете штетан материјал. Такође имамо интерактивни Content Safety Studio који вам омогућава да видите, истражите и испробате пример кода за откривање штетног садржаја у различитим форматима. Следећа [брза документација](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) води вас кроз слање захтева сервису.

Још један аспект који треба узети у обзир је укупне перформансе апликације. Код мултимодалних и мултимоделских апликација, под перформансама подразумевамо да систем ради онако како ви и ваши корисници очекујете, укључујући и то да не генерише штетне излазе. Важно је да процените перформансе ваше апликације користећи [метрике квалитета генерисања, ризика и безбедности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Своју AI апликацију можете проценити у развојном окружењу користећи [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). На основу тест скупа података или циља, генерисања ваше генеративне AI апликације се квантитативно мере уграђеним или прилагођеним евалуаторима по вашем избору. Да бисте започели са prompt flow sdk-ом за евалуацију вашег система, можете пратити [брзи водич](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Када покренете евалуацију, можете [визуелизовати резултате у Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Жигови

Овај пројекат може садржати жигове или логотипе пројеката, производа или услуга. Овлашћена употреба Microsoft жигова или логотипа подлеже и мора бити у складу са [Microsoft смерницама за жигове и бренд](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Употреба Microsoft жигова или логотипа у измењеним верзијама овог пројекта не сме изазвати забуну или имплицирати да је Microsoft спонзор. Свака употреба жигова или логотипа трећих страна подлеже политикама тих трећих страна.

## Помоћ

Ако запнете или имате питања у вези са развојем AI апликација, придружите се:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ако имате повратне информације о производу или наиђете на грешке током развоја, посетите:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења настала употребом овог превода.