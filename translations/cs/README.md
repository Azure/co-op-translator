<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:51:05+00:00",
  "source_file": "README.md",
  "language_code": "cs"
}
-->
# Co-op Translator

_Jednoduše automatizujte překlad svého vzdělávacího obsahu na GitHubu do více jazyků a oslovte globální publikum._

### 🌐 Podpora více jazyků

#### Podporováno nástrojem [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabština](../ar/README.md) | [Bengálština](../bn/README.md) | [Bulharština](../bg/README.md) | [Barmština (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradiční, Hong Kong)](../hk/README.md) | [Čínština (tradiční, Macao)](../mo/README.md) | [Čínština (tradiční, Tchaj-wan)](../tw/README.md) | [Chorvatština](../hr/README.md) | [Čeština](./README.md) | [Dánština](../da/README.md) | [Holandština](../nl/README.md) | [Estonština](../et/README.md) | [Finština](../fi/README.md) | [Francouzština](../fr/README.md) | [Němčina](../de/README.md) | [Řečtina](../el/README.md) | [Hebrejština](../he/README.md) | [Hindština](../hi/README.md) | [Maďarština](../hu/README.md) | [Indonéština](../id/README.md) | [Italština](../it/README.md) | [Japonština](../ja/README.md) | [Korejština](../ko/README.md) | [Litevština](../lt/README.md) | [Malajština](../ms/README.md) | [Maráthština](../mr/README.md) | [Nepálština](../ne/README.md) | [Norština](../no/README.md) | [Perština (Fársí)](../fa/README.md) | [Polština](../pl/README.md) | [Portugalština (Brazílie)](../br/README.md) | [Portugalština (Portugalsko)](../pt/README.md) | [Pandžábština (Gurmukhi)](../pa/README.md) | [Rumunština](../ro/README.md) | [Ruština](../ru/README.md) | [Srbština (cyrilice)](../sr/README.md) | [Slovenština](../sk/README.md) | [Slovinština](../sl/README.md) | [Španělština](../es/README.md) | [Svahilština](../sw/README.md) | [Švédština](../sv/README.md) | [Tagalog (Filipínština)](../tl/README.md) | [Tamilština](../ta/README.md) | [Thajština](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinština](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamština](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Přehled

**Co-op Translator** vám umožní rychle překládat vzdělávací obsah na GitHubu do více jazyků a snadno tak oslovit uživatele po celém světě. Když aktualizujete své Markdown soubory, obrázky nebo Jupyter notebooky, překlady se automaticky synchronizují, aby váš vzdělávací obsah zůstal aktuální a relevantní pro mezinárodní publikum.

Podívejte se, jak Co-op Translator organizuje překlady vzdělávacího obsahu na GitHubu:

![Příklad](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.cs.png)

## Rychlý start

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

## Minimální nastavení

- Vytvořte soubor `.env` podle šablony: [.env.template](../../.env.template)
- Nastavte jednoho poskytovatele LLM (Azure OpenAI nebo OpenAI)
- Pro překlad obrázků (`-img`) nastavte také Azure AI Vision
- Doporučeno: Pokud máte překlady vytvořené jinými nástroji, nejprve je odstraňte, abyste předešli konfliktům (například: `translations/`).
- Doporučeno: Přidejte sekci překladů do svého README pomocí [šablony jazyků README](./README_languages_template.md)
- Viz: [Nastavení Azure AI](./getting_started/set-up-azure-ai.md)

## Použití

Překlad všech podporovaných typů:

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

Další volby: [Referenční příručka příkazů](./getting_started/command-reference.md)

## Funkce

- Automatizovaný překlad Markdownu, notebooků a obrázků
- Udržuje překlady synchronizované se změnami zdroje
- Funguje lokálně (CLI) i v CI (GitHub Actions)
- Používá Azure OpenAI nebo OpenAI; volitelně Azure AI Vision pro obrázky
- Zachovává formátování a strukturu Markdownu

## Dokumentace

- [Příručka příkazového řádku](./getting_started/command-line-guide/command-line-guide.md)
- [Příručka pro GitHub Actions (veřejné repozitáře & standardní tajemství)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Příručka pro GitHub Actions (repozitáře Microsoft organizace & nastavení na úrovni organizace)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Podporované jazyky](./getting_started/supported-languages.md)
- [Řešení problémů](./getting_started/troubleshooting.md)

## Podpořte nás a rozvíjejte globální vzdělávání

Přidejte se k nám a pomozte změnit způsob sdílení vzdělávacího obsahu po celém světě! Dejte [Co-op Translatoru](https://github.com/azure/co-op-translator) ⭐ na GitHubu a podpořte naši misi bourat jazykové bariéry ve vzdělávání a technologiích. Váš zájem a příspěvky mají velký význam! Přispěvky do kódu i návrhy funkcí jsou vždy vítány.

### Prozkoumejte vzdělávací obsah Microsoftu ve svém jazyce

- [AZD pro začátečníky](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pro začátečníky](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) pro začátečníky](https://github.com/microsoft/mcp-for-beginners)
- [AI agenti pro začátečníky](https://github.com/microsoft/ai-agents-for-beginners)
- [Generativní AI pro začátečníky s .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativní AI pro začátečníky](https://github.com/microsoft/generative-ai-for-beginners)
- [Generativní AI pro začátečníky v Javě](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML pro začátečníky](https://aka.ms/ml-beginners)
- [Data Science pro začátečníky](https://aka.ms/datascience-beginners)
- [AI pro začátečníky](https://aka.ms/ai-beginners)
- [Kybernetická bezpečnost pro začátečníky](https://github.com/microsoft/Security-101)
- [Webový vývoj pro začátečníky](https://aka.ms/webdev-beginners)
- [IoT pro začátečníky](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video prezentace

Zjistěte více o Co-op Translatoru prostřednictvím našich prezentací _(Klikněte na obrázek níže pro sledování na YouTube.)_:

- **Open at Microsoft**: Krátké 18minutové představení a rychlý průvodce používáním Co-op Translatoru.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.cs.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Přispívání

Tento projekt vítá příspěvky a návrhy. Máte zájem přispět do Azure Co-op Translatoru? Podívejte se na [CONTRIBUTING.md](./CONTRIBUTING.md) pro pokyny, jak můžete pomoci zpřístupnit Co-op Translator širšímu publiku.

## Přispěvatelé

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodex chování

Tento projekt přijal [Kodex chování Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).
Více informací najdete v [FAQ ke kodexu chování](https://opensource.microsoft.com/codeofconduct/faq/) nebo
kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s dalšími dotazy či komentáři.

## Odpovědná AI

Microsoft se zavazuje pomáhat svým zákazníkům používat naše AI produkty odpovědně, sdílet naše zkušenosti a budovat důvěru prostřednictvím nástrojů jako Transparency Notes a Impact Assessments. Mnoho těchto zdrojů najdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Přístup Microsoftu k odpovědné AI je založen na našich principech AI: spravedlnost, spolehlivost a bezpečnost, soukromí a zabezpečení, inkluzivita, transparentnost a odpovědnost.

Velké jazykové, obrazové a hlasové modely – jako ty použité v tomto příkladu – se mohou chovat nespravedlivě, nespolehlivě nebo urážlivě, což může způsobit škody. Přečtěte si [Transparency note ke službě Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), abyste byli informováni o rizicích a omezeních.

Doporučený způsob, jak tato rizika zmírnit, je zahrnout do své architektury bezpečnostní systém, který dokáže detekovat a zabránit škodlivému chování. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislou ochrannou vrstvu, která dokáže detekovat škodlivý obsah generovaný uživateli i AI v aplikacích a službách. Azure AI Content Safety zahrnuje API pro text i obrázky, které umožňují detekovat škodlivý materiál. K dispozici je také interaktivní Content Safety Studio, kde si můžete prohlédnout, vyzkoušet a otestovat ukázkový kód pro detekci škodlivého obsahu v různých modalitách. Následující [dokumentace pro rychlý start](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás provede odesláním požadavků na službu.
Dalším aspektem, na který je třeba myslet, je celkový výkon aplikace. U aplikací, které využívají více modalit a modelů, považujeme za výkon to, že systém funguje podle očekávání vás i vašich uživatelů, včetně toho, že negeneruje škodlivé výstupy. Je důležité hodnotit výkon celé vaší aplikace pomocí [metrik kvality generování a metrik rizik a bezpečnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Svoji AI aplikaci můžete vyhodnotit ve svém vývojovém prostředí pomocí [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Na základě testovací datové sady nebo cíle jsou generace vaší generativní AI aplikace kvantitativně měřeny pomocí vestavěných nebo vlastních hodnotících nástrojů dle vašeho výběru. Pokud chcete začít s prompt flow SDK pro vyhodnocení vašeho systému, můžete postupovat podle [rychlého průvodce](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Jakmile spustíte hodnotící běh, můžete [vizualizovat výsledky v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt může obsahovat ochranné známky nebo loga projektů, produktů či služeb. Povolené použití ochranných známek nebo log společnosti Microsoft podléhá a musí se řídit
[Pokyny pro používání ochranných známek a značky Microsoftu](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Použití ochranných známek nebo log Microsoftu v upravených verzích tohoto projektu nesmí vyvolávat záměnu nebo naznačovat sponzorství ze strany Microsoftu.
Jakékoli použití ochranných známek nebo log třetích stran podléhá zásadám těchto třetích stran.

## Získání pomoci

Pokud si nevíte rady nebo máte dotazy ohledně tvorby AI aplikací, připojte se:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Pokud máte zpětnou vazbu k produktu nebo narazíte na chyby při vývoji, navštivte:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Prohlášení**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.