# Co-op Translator

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

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

**Začnite tu:** [Vyberte svoj pracovný postup](https://azure.github.io/co-op-translator/workflows/) | [Konfigurácia](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Podpora viacerých jazykov

#### Podporované [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabčina](../ar/README.md) | [Bengálčina](../bn/README.md) | [Bulharčina](../bg/README.md) | [Barmčina (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh-CN/README.md) | [Čínština (tradičná, Hong Kong)](../zh-HK/README.md) | [Čínština (tradičná, Macau)](../zh-MO/README.md) | [Čínština (tradičná, Taiwan)](../zh-TW/README.md) | [Chorvátčina](../hr/README.md) | [Čeština](../cs/README.md) | [Dánčina](../da/README.md) | [Nizozemčina](../nl/README.md) | [Estónčina](../et/README.md) | [Finština](../fi/README.md) | [Francúzština](../fr/README.md) | [Nemčina](../de/README.md) | [Gréčtina](../el/README.md) | [Hebrejčina](../he/README.md) | [Hindčina](../hi/README.md) | [Maďarčina](../hu/README.md) | [Indonézština](../id/README.md) | [Taliančina](../it/README.md) | [Japončina](../ja/README.md) | [Kannadčina](../kn/README.md) | [Khmerčina](../km/README.md) | [Kórejčina](../ko/README.md) | [Litovčina](../lt/README.md) | [Malajčina](../ms/README.md) | [Malajálamčina](../ml/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Nigerijská pidžinčina](../pcm/README.md) | [Nórčina](../no/README.md) | [Perzština (Farsi)](../fa/README.md) | [Poľština](../pl/README.md) | [Portugalčina (Brazília)](../pt-BR/README.md) | [Portugalčina (Portugalsko)](../pt-PT/README.md) | [Pundžábčina (Gurmukhi)](../pa/README.md) | [Rumunčina](../ro/README.md) | [Ruština](../ru/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Slovenčina](./README.md) | [Slovinčina](../sl/README.md) | [Španielčina](../es/README.md) | [Svahilčina](../sw/README.md) | [Švédčina](../sv/README.md) | [Tagalog (Filipíny)](../tl/README.md) | [Tamilčina](../ta/README.md) | [Telugčina](../te/README.md) | [Thajčina](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinčina](../uk/README.md) | [Urdčina](../ur/README.md) | [Vietnamčina](../vi/README.md)

> **Preferujete klonovanie lokálne?**
>
> Tento repozitár obsahuje 50+ jazykových prekladov, čo výrazne zväčšuje veľkosť sťahovania. Ak chcete klonovať bez prekladov, použite sparse checkout:
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
> Toto vám poskytne všetko, čo potrebujete na dokončenie kurzu s omnoho rýchlejším stiahnutím.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Prehľad

**Co-op Translator** vám pomáha lokalizovať váš vzdelávací obsah na GitHub-e do viacerých jazykov bez námahy. Keď aktualizujete svoje súbory Markdown, obrázky alebo notebooky, preklady zostávajú automaticky synchronizované, čo zaisťuje, že váš obsah zostane presný a aktuálny pre študentov po celom svete.

Používajte ho z CLI pre preklad repozitára, z Python API pre automatizáciu, alebo cez MCP server pre pracovné postupy s agentmi a editormi.

Príklad toho, ako je preložený obsah organizovaný:

![Príklad](../../imgs/translation-ex.png)

## Prečo Co-op Translator?

Preložiť jeden súbor je jednoduché. Udržiavať celý dokumentačný repozitár
preložený, prepojený a aktuálny je náročné.

| Problém | Ako vám Co-op Translator pomôže |
| --- | --- |
| Dlhé dokumenty nie sú jeden prompt | Veľké Markdown súbory sú rozdelené na časti, takže dlhé README nie je závislé od jednej krehkej odpovede modelu. Ak časť zlyhá, Co-op Translator môže skúsiť znova a znovu rozčleniť len neúspešnú časť. |
| Neúplné preklady by nemali byť označené ako aktuálne | Skrátený preklad by nikdy nemal byť uzavretý ako aktuálny. Co-op Translator kontroluje integritu prekladu pred uložením a dokáže zistiť štruktúrne neúplné existujúce preklady. |
| Odkazy by mali zodpovedať preloženej štruktúre repozitára | Manuálne preklady často nechávajú relatívne odkazy smerujúce späť do zdrojového stromu. Co-op Translator prepíše odkazy v Markdown, notebookoch, obrázkoch a README tak, aby zodpovedali štruktúre `translations/<lang>/...`. |
| Preklad by mal fungovať v celom repozitári | Co-op Translator spracováva súbory README, dokumentáciu, notebooky a text v obrázkoch ako súčasť jedného pracovného postupu repozitára, namiesto prekladu súborov jeden po druhom. |
| Udržiavanie prekladov je dôležitejšie než ich jednorazové vytvorenie | Hashy zdrojov a metadáta prekladov umožňujú Co-op Translatoru nájsť zastarané súbory, preskočiť nezmenené súbory a udržiavať preložený obsah synchronizovaný, keď sa zdrojový repozitár vyvíja. |

## Ako je spravovaný stav prekladu

Co-op Translator spravuje preložený obsah ako **verziované softvérové artefakty**,  
nie ako statické súbory.

Nástroj sleduje stav preloženého Markdownu, obrázkov a notebookov
pomocou **metadát viazaných na jazyk**.

Tento dizajn umožňuje Co-op Translatoru:

- Spoľahlivo zistiť zastarané preklady
- Zaobchádzať s Markdownom, obrázkami a notebookmi konzistentne
- Bezpečne škálovať naprieč veľkými, rýchlo sa meniacimi, viacjazyčnými repozitármi

Tým, že modeluje preklady ako spravované artefakty,
pracovné postupy prekladov sa prirodzene zladia s modernými
praktikami správy závislostí a artefaktov softvéru.

→ [Ako sa spravuje stav prekladu](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Súvisiace podrobné články

- [Oprava poškodeného Markdownu v AI preklade: Spevnenie produkčnej pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Začnite

Co-op Translator sa dá používať z CLI, Python API alebo MCP servera. Začnite s príručkou pracovného postupu, ak si vyberáte medzi lokálnym prekladom, automatizáciou, CI a integráciou s agentom/editorem.

- [Vyberte svoj pracovný postup](../../docs/workflows.md)
- [Nakonfigurujte poverenia](../../docs/configuration.md)
- [Prekladajte z CLI](../../docs/cli.md)
- [Automatizujte s Python API](../../docs/api.md)
- [Prepojte sa s MCP Serverom](../../docs/mcp.md)
- [Spúšťajte v GitHub Actions](../../docs/github-actions.md)

Minimálny príklad použitia CLI po konfigurácii:

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

Pre prvé spustenia na veľkých repozitároch používajte `--dry-run` pred zápisom preložených súborov. Pozrite si [CLI Reference](../../docs/cli.md) pre príznaky typov obsahu, logy, kontrolu a migráciu odkazov.

Rýchle spustenie v kontajneri s Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Rýchle spustenie v kontajneri s PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funkcie

- Automatizovaný preklad pre Markdown, notebooky a obrázky
- Udržiava preklady synchronizované so zdrojovými zmenami
- Funguje lokálne (CLI) alebo v CI (GitHub Actions)
- Zverejňuje nástroje pre Markdown, notebooky, obrázky, recenzie a projektové preklady cez MCP
- Používa Azure OpenAI alebo OpenAI ako poskytovateľa prekladov
- Umožňuje, aby MCP hosťoval agentov, ktorí prekladajú časti Markdownu a notebookov bez poverení LLM Co-op Translatora
- Používa Azure AI Vision pre extrakciu textu z obrázkov a jeho preklad
- Kontroluje štruktúru a čerstvosť prekladu pomocou deterministických kontrol
- Zachováva formátovanie a štruktúru Markdownu

## Dokumentácia

- [Web dokumentácie](https://azure.github.io/co-op-translator/)
- [Vyberte svoj pracovný postup](../../docs/workflows.md)
- [Konfigurácia](../../docs/configuration.md)
- [Nastavenie Azure AI](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Šablóna README jazykov](../../docs/readme-languages-template.md)
- [Podporované jazyky](../../docs/supported-languages.md)
- [Prispievanie](../../CONTRIBUTING.md)
- [Riešenie problémov](../../docs/troubleshooting.md)

### Microsoft-špecifický sprievodca
> [!NOTE]
> Len pre správcov repozitárov Microsoft “For Beginners”.

- [Aktualizácia zoznamu „other courses“ (len pre repozitáre MS Beginners)](../../docs/microsoft-beginners.md)

## Podporte nás a podporujte globálne vzdelávanie

Pridajte sa k nám v revolúcii zdieľania vzdelávacieho obsahu po celom svete! Dajte [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHub-e a podporte našu misiu odbúravať jazykové bariéry vo vzdelávaní a technológiách. Váš záujem a príspevky majú významný dopad! Kódové príspevky a návrhy funkcií sú vždy vítané.

### Objavte vzdelávací obsah Microsoftu vo vašom jazyku
- [LangChain4j pre začiatočníkov](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD pre začiatočníkov](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI pre začiatočníkov](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) pre začiatočníkov](https://github.com/microsoft/mcp-for-beginners)
- [AI agenti pre začiatočníkov](https://github.com/microsoft/ai-agents-for-beginners)
- [Generatívna AI pre začiatočníkov pomocou .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatívna AI pre začiatočníkov](https://github.com/microsoft/generative-ai-for-beginners)
- [Generatívna AI pre začiatočníkov pomocou Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [Strojové učenie pre začiatočníkov](https://aka.ms/ml-beginners)
- [Dátová veda pre začiatočníkov](https://aka.ms/datascience-beginners)
- [AI pre začiatočníkov](https://aka.ms/ai-beginners)
- [Kybernetická bezpečnosť pre začiatočníkov](https://github.com/microsoft/Security-101)
- [Webový vývoj pre začiatočníkov](https://aka.ms/webdev-beginners)
- [IoT pre začiatočníkov](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video presentations

👉 Kliknite na obrázok nižšie a pozrite si ho na YouTube.

- **Open at Microsoft**: Krátke 18-minútové predstavenie a rýchly sprievodca, ako používať Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contributing

Tento projekt víta príspevky a návrhy. Máte záujem prispieť k Azure Co-op Translator? Pozrite si, prosím, náš [CONTRIBUTING.md](../../CONTRIBUTING.md) pre pokyny, ako môžete pomôcť sprístupniť Co-op Translator.

## Contributors

[![prispievatelia co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pre viac informácií si pozrite [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) alebo kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) v prípade ďalších otázok alebo pripomienok.

## Responsible AI

Microsoft sa zaväzuje pomáhať našim zákazníkom používať naše AI produkty zodpovedne, zdieľať naše poznatky a budovať partnerstvá založené na dôvere prostredníctvom nástrojov ako Transparency Notes a Impact Assessments. Mnohé z týchto zdrojov nájdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Prístup Microsoftu k zodpovednej AI je založený na našich princípoch AI: spravodlivosť, spoľahlivosť a bezpečnosť, súkromie a ochrana, inkluzívnosť, transparentnosť a zodpovednosť.

Modely veľkého rozsahu pre prirodzený jazyk, obraz a reč — ako tie použité v tomto príklade — sa môžu potenciálne správať spôsobmi, ktoré sú nespravodlivé, nespolehlivé alebo urážlivé, čo môže spôsobiť škodu. Pre informácie o rizikách a obmedzeniach si pozrite [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).

Odporúčaným prístupom na zmiernenie týchto rizík je zahrnúť do svojej architektúry bezpečnostný systém, ktorý dokáže detegovať a zabrániť škodlivému správaniu. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislú ochrannú vrstvu, schopnú detegovať škodlivý obsah vytváraný používateľmi aj AI v aplikáciách a službách. Azure AI Content Safety obsahuje textové a obrazové API, ktoré vám umožnia detegovať materiál, ktorý je škodlivý. Máme tiež interaktívne Content Safety Studio, ktoré vám umožní prezerať, skúmať a vyskúšať vzorový kód na detekciu škodlivého obsahu naprieč rôznymi modalitami. Nasledujúca [quickstart dokumentácia](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás prevedie, ako robiť požiadavky na službu.

Ďalším aspektom, ktorý treba brať do úvahy, je celkový výkon aplikácie. Pri multimodálnych a viacmodelových aplikáciách považujeme výkon za to, že systém funguje tak, ako vy a vaši používatelia očakávate, vrátane toho, že negeneruje škodlivé výstupy. Je dôležité hodnotiť výkon celej aplikácie pomocou [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Svoju AI aplikáciu môžete vyhodnotiť vo vývojovom prostredí pomocou [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). S testovacím datasetom alebo cieľom sú generácie vašej generatívnej AI aplikácie kvantitatívne merané pomocou vstavaných evaluátorov alebo vlastných evaluátorov podľa vášho výberu. Ak chcete začať s prompt flow SDK na vyhodnotenie vášho systému, môžete postupovať podľa [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po vykonaní hodnotiaceho behu môžete [vizualizovať výsledky v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Tento projekt môže obsahovať ochranné známky alebo logá k projektom, produktom alebo službám. Autorizované použitie obchodných značiek alebo log Microsoftu podlieha a musí byť v súlade s
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Použitie obchodných značiek alebo log Microsoftu v upravených verziách tohto projektu nesmie spôsobovať zmätok alebo naznačovať, že Microsoft projekt sponzoruje.
Akékoľvek použitie ochranných známok alebo log tretích strán podlieha pravidlám týchto tretích strán.

## Getting Help

Ak sa zaseknete alebo máte otázky týkajúce sa vytvárania AI aplikácií, pripojte sa:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ak máte spätnú väzbu k produktu alebo sa vyskytli chyby počas vývoja, navštívte:

[![Fórum vývojárov Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)