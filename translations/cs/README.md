# Co-op Translator

_Snadno automatizujte a udržujte překlady svého vzdělávacího obsahu na GitHubu do více jazyků, jak se váš projekt vyvíjí._

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

**Začněte zde:** [Vyberte pracovní postup](https://azure.github.io/co-op-translator/workflows/) | [Konfigurace](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Podpora více jazyků

#### Podporováno [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabština](../ar/README.md) | [Bengálština](../bn/README.md) | [Bulharština](../bg/README.md) | [Barmština (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh-CN/README.md) | [Čínština (tradiční, Hongkong)](../zh-HK/README.md) | [Čínština (tradiční, Macao)](../zh-MO/README.md) | [Čínština (tradiční, Tchaj-wan)](../zh-TW/README.md) | [Chorvatština](../hr/README.md) | [Čeština](./README.md) | [Dánština](../da/README.md) | [Nizozemština](../nl/README.md) | [Estonština](../et/README.md) | [Finština](../fi/README.md) | [Francouzština](../fr/README.md) | [Němčina](../de/README.md) | [Řečtina](../el/README.md) | [Hebrejština](../he/README.md) | [Hindština](../hi/README.md) | [Maďarština](../hu/README.md) | [Indonéština](../id/README.md) | [Italština](../it/README.md) | [Japonština](../ja/README.md) | [Kannadština](../kn/README.md) | [Khmerština](../km/README.md) | [Korejština](../ko/README.md) | [Litevština](../lt/README.md) | [Malajština](../ms/README.md) | [Malajálamština](../ml/README.md) | [Maráthština](../mr/README.md) | [Nepálština](../ne/README.md) | [Nigerijská pidžinština](../pcm/README.md) | [Norština](../no/README.md) | [Perština (Farsi)](../fa/README.md) | [Polština](../pl/README.md) | [Portugalština (Brazílie)](../pt-BR/README.md) | [Portugalština (Portugalsko)](../pt-PT/README.md) | [Paňdžábština (Gurmukhi)](../pa/README.md) | [Rumunština](../ro/README.md) | [Ruština](../ru/README.md) | [Srbština (cyrilice)](../sr/README.md) | [Slovenština](../sk/README.md) | [Slovinština](../sl/README.md) | [Španělština](../es/README.md) | [Svahilština](../sw/README.md) | [Švédština](../sv/README.md) | [Tagalog (filipínština)](../tl/README.md) | [Tamilština](../ta/README.md) | [Telugština](../te/README.md) | [Thajština](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinština](../uk/README.md) | [Urdština](../ur/README.md) | [Vietnamština](../vi/README.md)

> **Dáváte přednost klonování lokálně?**
>
> Tento repozitář obsahuje více než 50 překladů, což výrazně zvyšuje velikost stahování. Chcete‑li klonovat bez překladů, použijte sparse checkout:
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
> Toto vám poskytne vše potřebné k dokončení kurzu při mnohem rychlejším stažení.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Přehled

**Co-op Translator** vám pomáhá lokalizovat váš vzdělávací obsah na GitHubu do více jazyků bez námahy. Když aktualizujete své soubory Markdown, obrázky nebo notebooky, překlady zůstávají automaticky synchronizované, což zajišťuje, že váš obsah zůstane přesný a aktuální pro studenty po celém světě.

Používejte jej z CLI pro překlad repozitáře, z Python API pro automatizaci nebo přes MCP server pro pracovní postupy s agenty a editory.

Příklad, jak je přeložený obsah uspořádán:

![Příklad](../../imgs/translation-ex.png)

## Proč Co-op Translator?

Přeložit jeden soubor je snadné. Udržet celý dokumentační repozitář přeložený, propojený a aktuální je ta těžká část.

| Problém | Jak Co-op Translator pomáhá |
| --- | --- |
| Dlouhé dokumenty nejsou jedním promptem | Velké Markdown soubory jsou rozděleny do částí, takže dlouhý README není závislý na jedné náchylné odpovědi modelu. Pokud část selže, Co-op Translator může opakovat pokus a znovu rozdělit pouze selhanou část. |
| Neúplné překlady by neměly být označeny jako aktuální | Zkrácený překlad by nikdy neměl být označen jako aktuální. Co-op Translator kontroluje integritu překladu před uložením a dokáže detekovat strukturálně neúplné existující překlady. |
| Odkazy by měly odpovídat struktuře přeloženého repozitáře | Ruční překlady často nechávají relativní odkazy směřující zpět do zdrojového stromu. Co-op Translator přepisuje odkazy v Markdownu, noteboocích, obrázcích a README tak, aby odpovídaly struktuře `translations/<lang>/...`. |
| Překlad by měl fungovat v celém repozitáři | Co-op Translator zpracovává soubory README, dokumentaci, notebooky a text v obrázcích jako součást jednoho workflow repozitáře, místo aby překládal soubory jeden po druhém. |
| Udržování překladů je důležitější než jejich jednorázové vytvoření | Hashy zdrojů a metadata překladu umožňují Co-op Translatoru najít zastaralé soubory, přeskočit nezměněné soubory a udržovat přeložený obsah synchronizovaný, jak se zdrojový repozitář vyvíjí. |

## Jak se spravuje stav překladu

Co-op Translator spravuje přeložený obsah jako **verzionované softwarové artefakty**,  
nikoli jako statické soubory.

Nástroj sleduje stav přeloženého Markdownu, obrázků a notebooků pomocí **metadata specifických pro jazyk**.

Tento návrh umožňuje Co-op Translatoru:

- Spolehlivě detekovat zastaralé překlady
- Zpracovávat Markdown, obrázky a notebooky konzistentně
- Bezpečně škálovat napříč velkými, rychle se měnícími, vícejazyčnými repozitáři

Modelováním překladů jako spravovaných artefaktů
se pracovní postupy překladu přirozeně sladí s moderními
postupy správy závislostí a artefaktů v softwaru.

→ [Jak se spravuje stav překladu](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Související podrobné články

- [Oprava poškozeného Markdownu v AI překladu: Zesílení produkčního procesu](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Začněte

Co-op Translator lze používat z CLI, Python API nebo MCP serveru. Začněte průvodcem pracovních postupů, pokud vybíráte mezi lokálním překladem, automatizací, CI a integrací s agenty/editory.

- [Vyberte pracovní postup](../../docs/workflows.md)
- [Konfigurace oprávnění](../../docs/configuration.md)
- [Překládejte z CLI](../../docs/cli.md)
- [Automatizujte s Python API](../../docs/api.md)
- [Připojte se k MCP serveru](../../docs/mcp.md)
- [Spouštějte v GitHub Actions](../../docs/github-actions.md)

Minimální příklad CLI po konfiguraci:

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

Při prvních spuštěních na velkých repozitářích použijte `--dry-run` před tím, než zapíšete přeložené soubory. Podívejte se na [CLI Reference](../../docs/cli.md) pro přepínače typů obsahu, logy, revize a migraci odkazů.

Rychlé spuštění kontejneru v Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Rychlé spuštění kontejneru v PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funkce

- Automatizovaný překlad pro Markdown, notebooky a obrázky
- Udržuje překlady synchronizované se změnami ve zdroji
- Funguje lokálně (CLI) nebo v CI (GitHub Actions)
- Zveřejňuje nástroje pro překlad Markdownu, notebooků, obrázků, revize a projektů přes MCP
- Používá Azure OpenAI nebo OpenAI pro poskytovatelem zajištěné překlady
- Umožňuje, aby MCP hostil agenty překládající části Markdownu a notebooků bez přihlašovacích údajů LLM Co-op Translatoru
- Používá Azure AI Vision pro extrakci textu z obrázků a překládání
- Kontroluje strukturu a aktuálnost překladu s deterministickými kontrolami
- Zachovává formátování a strukturu Markdownu

## Dokumentace

- [Dokumentační stránka](https://azure.github.io/co-op-translator/)
- [Vyberte pracovní postup](../../docs/workflows.md)
- [Konfigurace](../../docs/configuration.md)
- [Nastavení Azure AI](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Šablona README pro jazyky](../../docs/readme-languages-template.md)
- [Podporované jazyky](../../docs/supported-languages.md)
- [Přispívání](../../CONTRIBUTING.md)
- [Řešení problémů](../../docs/troubleshooting.md)

### Microsoft-specifický průvodce
> [!NOTE]
> Pouze pro správce repozitářů Microsoft „For Beginners“.

- [Aktualizace seznamu „other courses“ (pouze pro repozitáře MS Beginners)](../../docs/microsoft-beginners.md)

## Podpořte nás a podpořte globální vzdělávání

Přidejte [Co-op Translator](https://github.com/azure/co-op-translator) hvězdičku ⭐ na GitHubu a podpořte naši misi odstraňovat jazykové bariéry ve vzdělávání a technologii. Váš zájem a příspěvky mají velký dopad! Kódové příspěvky a návrhy funkcí jsou vždy vítány.

### Prozkoumejte vzdělávací obsah Microsoftu ve svém jazyce
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

## Video prezentace

👉 Klikněte na obrázek níže a sledujte na YouTube.

- **Open at Microsoft**: Krátké 18minutové úvodní video a rychlý průvodce používáním Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Přispívání

Tento projekt vítá příspěvky a návrhy. Máte zájem přispět do Azure Co-op Translator? Přečtěte si prosím naše [CONTRIBUTING.md](../../CONTRIBUTING.md) pro pokyny, jak můžete pomoci zpřístupnit Co-op Translator.

## Přispěvatelé

[![přispěvatelé co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodex chování

Tento projekt přijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pro více informací viz [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) nebo kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s jakýmikoli dalšími dotazy či připomínkami.

## Zodpovědné AI

Microsoft se zavazuje pomáhat našim zákazníkům používat naše AI produkty zodpovědně, sdílet naše poznatky a budovat partnerství založená na důvěře prostřednictvím nástrojů jako Transparency Notes a Impact Assessments. Mnoho z těchto zdrojů najdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Přístup Microsoftu k zodpovědnému AI je založen na našich zásadách AI: férovost, spolehlivost a bezpečnost, soukromí a zabezpečení, inkluzivita, transparentnost a odpovědnost.

Velké modely pro zpracování přirozeného jazyka, obrazu a řeči — jako ty, které jsou použity v tomto příkladu — se mohou potenciálně chovat způsobem, který je nespravedlivý, nespolehlivý nebo urážlivý, což může způsobit škody. Pro informace o rizicích a omezeních si prosím přečtěte [Poznámku o transparentnosti služby Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).

Doporučený přístup k mitigaci těchto rizik je začlenit do vaší architektury bezpečnostní systém, který dokáže detekovat a předcházet škodlivému chování. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislou vrstvu ochrany, schopnou detekovat škodlivý obsah vytvářený uživateli i AI v aplikacích a službách. Azure AI Content Safety zahrnuje textové a obrazové API, která vám umožní detekovat škodlivý materiál. K dispozici je také interaktivní Content Safety Studio, které vám umožní zobrazit, prozkoumat a vyzkoušet ukázkový kód pro detekci škodlivého obsahu napříč různými modalitami. Následující [dokumentace pro rychlý start](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás provede vytvářením požadavků na službu.

Dalším aspektem, který je třeba vzít v úvahu, je celkový výkon aplikace. U multimodálních a multimodelových aplikací považujeme výkon za to, že systém funguje tak, jak očekáváte vy a vaši uživatelé, včetně toho, že negeneruje škodlivé výstupy. Je důležité hodnotit výkon vaší celé aplikace pomocí [metrik kvality generování a metrik rizika a bezpečnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Své AI řešení můžete vyhodnotit ve vašem vývojovém prostředí pomocí [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Ať už máte testovací datovou sadu nebo cíl, generace vaší generativní AI aplikace jsou kvantitativně měřeny vestavěnými evaluátory nebo vámi zvolenými vlastními evaluátory. Pokud chcete začít s prompt flow SDK pro vyhodnocení vašeho systému, můžete následovat [průvodce pro rychlý start](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Jakmile spustíte vyhodnocení, můžete [vizualizovat výsledky v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt může obsahovat ochranné známky nebo loga projektů, produktů nebo služeb. Autorizované použití ochranných známek nebo log Microsoftu podléhá a musí dodržovat [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Použití ochranných známek nebo log Microsoftu v upravených verzích tohoto projektu nesmí způsobit záměnu nebo naznačovat sponzorství Microsoftem.
Jakékoli použití ochranných známek nebo log třetích stran podléhá zásadám těchto třetích stran.

## Získání pomoci

Pokud si nevíte rady nebo máte jakékoli dotazy ohledně vytváření AI aplikací, připojte se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Pokud máte připomínky k produktu nebo narazíte na chyby během vývoje, navštivte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)