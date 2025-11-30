<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T12:08:59+00:00",
  "source_file": "README.md",
  "language_code": "cs"
}
-->
# Co-op Translator

_Snadno automatizujte překlad svého vzdělávacího obsahu na GitHubu do více jazyků a oslovte tak globální publikum._

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

### 🌐 Podpora více jazyků

#### Podporováno [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabština](../ar/README.md) | [Bengálština](../bn/README.md) | [Bulharština](../bg/README.md) | [Barmština (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradiční, Hongkong)](../hk/README.md) | [Čínština (tradiční, Macao)](../mo/README.md) | [Čínština (tradiční, Tchaj-wan)](../tw/README.md) | [Chorvatština](../hr/README.md) | [Čeština](./README.md) | [Dánština](../da/README.md) | [Nizozemština](../nl/README.md) | [Estonština](../et/README.md) | [Finština](../fi/README.md) | [Francouzština](../fr/README.md) | [Němčina](../de/README.md) | [Řečtina](../el/README.md) | [Hebrejština](../he/README.md) | [Hindština](../hi/README.md) | [Maďarština](../hu/README.md) | [Indonéština](../id/README.md) | [Italština](../it/README.md) | [Japonština](../ja/README.md) | [Kannadština](../kn/README.md) | [Korejština](../ko/README.md) | [Litevština](../lt/README.md) | [Malajština](../ms/README.md) | [Malajalámština](../ml/README.md) | [Maráthština](../mr/README.md) | [Nepálština](../ne/README.md) | [Nigerijská pidžinština](../pcm/README.md) | [Norština](../no/README.md) | [Perština (Fársí)](../fa/README.md) | [Polština](../pl/README.md) | [Portugalština (Brazílie)](../br/README.md) | [Portugalština (Portugalsko)](../pt/README.md) | [Paňdžábština (Gurmukhí)](../pa/README.md) | [Rumunština](../ro/README.md) | [Ruština](../ru/README.md) | [Srbština (cyrilice)](../sr/README.md) | [Slovenština](../sk/README.md) | [Slovinština](../sl/README.md) | [Španělština](../es/README.md) | [Svahilština](../sw/README.md) | [Švédština](../sv/README.md) | [Tagalog (filipínština)](../tl/README.md) | [Tamilština](../ta/README.md) | [Telugština](../te/README.md) | [Thajština](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinština](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamština](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Přehled

**Co-op Translator** vám pomůže snadno lokalizovat váš vzdělávací obsah na GitHubu do více jazyků.
Když aktualizujete své Markdown soubory, obrázky nebo notebooky, překlady se automaticky synchronizují, takže váš obsah zůstává přesný a aktuální pro studenty po celém světě.

Příklad, jak je přeložený obsah organizován:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.cs.png)

## Rychlý start

```bash
# Vytvořte a aktivujte virtuální prostředí (doporučeno)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Nainstalujte balíček
pip install co-op-translator
# Přeložit
translate -l "ko ja fr" -md
```

Docker:

```bash
# Stáhněte veřejný obraz z GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Spusťte s připojenou aktuální složkou a poskytnutým .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimální nastavení

1. Vytvořte soubor `.env` podle šablony: [.env.template](../../.env.template)
2. Nakonfigurujte jednoho poskytovatele LLM (Azure OpenAI nebo OpenAI)
3. (Volitelné) Pro překlad obrázků (`-img`) nastavte Azure AI Vision
4. (Doporučeno) Odstraňte předchozí překlady, aby nedocházelo ke konfliktům (např. `translations/`)
5. (Doporučeno) Přidejte sekci s překlady do svého README pomocí [šablony jazyků README](./getting_started/README_languages_template.md)
6. Viz: [Nastavení Azure AI](./getting_started/set-up-azure-ai.md)

## Použití

Přeložte všechny podporované typy:

```bash
translate -l "ko ja"
```

Pouze Markdown:

```bash
translate -l "de" -md
```

Markdown + obrázky:

```bash
translate -l "pt" -md -img
```

Pouze notebooky:

```bash
translate -l "zh" -nb
```

Další přepínače: [Reference příkazů](./getting_started/command-reference.md)

## Funkce

- Automatický překlad Markdown, notebooků a obrázků
- Udržuje překlady synchronizované se zdrojovými změnami
- Funguje lokálně (CLI) nebo v CI (GitHub Actions)
- Používá Azure OpenAI nebo OpenAI; volitelně Azure AI Vision pro obrázky
- Zachovává formátování a strukturu Markdownu

## Dokumentace

- [Příručka příkazového řádku](./getting_started/command-line-guide/command-line-guide.md)
- [Příručka GitHub Actions (veřejné repozitáře a standardní tajné klíče)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Příručka GitHub Actions (repozitáře Microsoft organizace a nastavení na úrovni organizace)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Šablona jazyků README](./getting_started/README_languages_template.md)
- [Podporované jazyky](./getting_started/supported-languages.md)
- [Přispívání](./CONTRIBUTING.md)
- [Řešení problémů](./getting_started/troubleshooting.md)

### Průvodce specifický pro Microsoft
> [!NOTE]
> Pouze pro správce repozitářů Microsoft „Pro začátečníky“.

- [Aktualizace seznamu „ostatních kurzů“ (pouze pro repozitáře MS Beginners)](./getting_started/update-other-courses.md)

## Podpořte nás a podpořte globální vzdělávání

Přidejte se k nám v revoluci sdílení vzdělávacího obsahu po celém světě! Dejte [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHubu a podpořte naši misi překonávat jazykové bariéry ve vzdělávání a technologiích. Váš zájem a příspěvky mají velký význam! Kódové příspěvky a návrhy funkcí jsou vždy vítány.

### Prozkoumejte vzdělávací obsah Microsoftu ve svém jazyce

- [AZD pro začátečníky](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pro začátečníky](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) pro začátečníky](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents pro začátečníky](https://github.com/microsoft/ai-agents-for-beginners)
- [Generativní AI pro začátečníky s .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativní AI pro začátečníky](https://github.com/microsoft/generative-ai-for-beginners)
- [Generativní AI pro začátečníky s Javou](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML pro začátečníky](https://aka.ms/ml-beginners)
- [Data Science pro začátečníky](https://aka.ms/datascience-beginners)
- [AI pro začátečníky](https://aka.ms/ai-beginners)
- [Kybernetická bezpečnost pro začátečníky](https://github.com/microsoft/Security-101)
- [Webový vývoj pro začátečníky](https://aka.ms/webdev-beginners)
- [IoT pro začátečníky](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video prezentace

👉 Klikněte na obrázek níže pro sledování na YouTube.

- **Open at Microsoft**: Krátké 18minutové představení a rychlý průvodce, jak používat Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.cs.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Přispívání

Tento projekt vítá příspěvky a návrhy. Máte zájem přispět do Azure Co-op Translator? Podívejte se na náš [CONTRIBUTING.md](./CONTRIBUTING.md), kde najdete pokyny, jak pomoci zpřístupnit Co-op Translator širšímu publiku.

## Přispěvatelé

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodex chování

Tento projekt přijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pro více informací si přečtěte [Často kladené otázky k Kodexu chování](https://opensource.microsoft.com/codeofconduct/faq/) nebo
kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s dalšími dotazy či připomínkami.

## Odpovědné AI

Microsoft se zavazuje pomáhat svým zákazníkům používat naše AI produkty zodpovědně, sdílet naše poznatky a budovat důvěru prostřednictvím nástrojů jako Transparency Notes a Impact Assessments. Mnoho těchto zdrojů najdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Přístup Microsoftu k odpovědné AI je založen na našich principech AI: spravedlnost, spolehlivost a bezpečnost, ochrana soukromí a bezpečnost, inkluzivita, transparentnost a odpovědnost.

Velké modely pro přirozený jazyk, obrázky a řeč – jako ty použité v tomto příkladu – se mohou chovat způsobem, který je nespravedlivý, nespolehlivý nebo urážlivý, což může způsobit škody. Pro informace o rizicích a omezeních si prosím přečtěte [Transparency note služby Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).
Doporučený přístup k omezení těchto rizik je zahrnout do vaší architektury bezpečnostní systém, který dokáže detekovat a zabránit škodlivému chování. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislou vrstvu ochrany, která dokáže detekovat škodlivý obsah vytvářený uživateli i AI v aplikacích a službách. Azure AI Content Safety zahrnuje textové a obrazové API, která vám umožní detekovat škodlivý materiál. K dispozici je také interaktivní Content Safety Studio, které vám umožní zobrazit, prozkoumat a vyzkoušet ukázkový kód pro detekci škodlivého obsahu napříč různými modalitami. Následující [dokumentace rychlého startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás provede tím, jak posílat požadavky na službu.

Dalším aspektem, který je třeba vzít v úvahu, je celkový výkon aplikace. U multimodálních a multimodelových aplikací chápeme výkon tak, že systém funguje tak, jak vy a vaši uživatelé očekáváte, včetně toho, že nevytváří škodlivé výstupy. Je důležité zhodnotit výkon vaší celkové aplikace pomocí [metrik kvality generování a rizik a bezpečnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Své AI aplikace můžete hodnotit ve svém vývojovém prostředí pomocí [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Na základě testovacího datasetu nebo cíle jsou generace vaší generativní AI aplikace kvantitativně měřeny pomocí vestavěných nebo vlastních hodnotitelů dle vašeho výběru. Pro začátek s prompt flow SDK k hodnocení vašeho systému můžete sledovat [průvodce rychlým startem](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po spuštění hodnocení můžete [vizualizovat výsledky v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt může obsahovat ochranné známky nebo loga projektů, produktů či služeb. Autorizované použití ochranných známek nebo log Microsoftu podléhá a musí dodržovat [Pravidla pro ochranné známky a značky Microsoftu](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Použití ochranných známek nebo log Microsoftu v upravených verzích tohoto projektu nesmí způsobit záměnu ani naznačovat sponzorství Microsoftem. Jakékoli použití ochranných známek nebo log třetích stran podléhá pravidlům těchto třetích stran.

## Získání pomoci

Pokud narazíte na problém nebo máte otázky ohledně tvorby AI aplikací, připojte se na:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Pokud máte zpětnou vazbu k produktu nebo narazíte na chyby během vývoje, navštivte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->