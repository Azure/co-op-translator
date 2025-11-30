<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T04:40:19+00:00",
  "source_file": "README.md",
  "language_code": "et"
}
-->
# Co-op Translator

_Automatiseeri oma haridusliku GitHubi sisu tõlkimine mitmesse keelde, et jõuda globaalse publikuni._

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

### 🌐 Mitmekeelne tugi

#### Toetab [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](./README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Ülevaade

**Co-op Translator** võimaldab sul kiiresti tõlkida oma haridusliku GitHubi sisu mitmesse keelde, jõudes hõlpsalt rahvusvahelise publikuni. Kui uuendad oma Markdown-faile, pilte või Jupyteri märkmikke, sünkroniseeritakse tõlked automaatselt, et sinu hariduslik GitHubi sisu oleks alati ajakohane ja asjakohane ka rahvusvahelistele kasutajatele.

Vaata, kuidas Co-op Translator korraldab tõlgitud haridusliku GitHubi sisu:

![Näide](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.et.png)

## Kiire alustamine

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

## Minimaalne seadistus

- Loo `.env` kasutades seda malli: [.env.template](../../.env.template)
- Sea üles üks LLM pakkuja (Azure OpenAI või OpenAI)
- Kui soovid tõlkida pilte (`-img`), lisa ka Azure AI Vision
- Soovituslik: Kui sul on varem teiste tööriistadega loodud tõlkeid, puhasta need enne, et vältida konflikte (näiteks: `translations/`).
- Soovituslik: Lisa oma README-sse tõlgete sektsioon, kasutades [README keelte malli](./README_languages_template.md)
- Vaata: [Azure AI seadistamine](./getting_started/set-up-azure-ai.md)

## Kasutamine

Tõlgi kõik toetatud tüübid:

```bash
translate -l "ko ja"
```

Ainult Markdown:

```bash
translate -l "de" -md
```

Markdown + pildid:

```bash
translate -l "pt" -md -img
```

Ainult märkmikud:

```bash
translate -l "zh" -nb
```

Rohkem lippusid: [Käsureferents](./getting_started/command-reference.md)

## Funktsioonid

- Automaatne tõlge Markdownile, märkmikele ja piltidele
- Hoiab tõlked allikaga sünkroonis
- Töötab kohapeal (CLI) või CI-s (GitHub Actions)
- Kasutab Azure OpenAI või OpenAI; piltide jaoks valikuline Azure AI Vision
- Säilitab Markdowni vormingu ja struktuuri

## Dokumentatsioon

- [Käsurea juhend](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions juhend (avalikud repositooriumid & standardsed saladused)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions juhend (Microsofti organisatsiooni repositooriumid & organisatsiooni tasemel seadistused)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Toetatud keeled](./getting_started/supported-languages.md)
- [Veaotsing](./getting_started/troubleshooting.md)

## Toeta meid ja edenda globaalset õppimist

Liitu meiega, et muuta haridusliku sisu jagamine üle maailma! Anna [Co-op Translatorile](https://github.com/azure/co-op-translator) ⭐ GitHubis ja toeta meie missiooni murda keelebarjääre õppimises ja tehnoloogias. Sinu huvi ja panus on väga oluline! Koodipanused ja uute funktsioonide ettepanekud on alati teretulnud.

### Avasta Microsofti hariduslikku sisu oma keeles

- [AZD algajatele](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI algajatele](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) algajatele](https://github.com/microsoft/mcp-for-beginners)
- [AI agendid algajatele](https://github.com/microsoft/ai-agents-for-beginners)
- [Generatiivne AI algajatele .NET-is](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatiivne AI algajatele](https://github.com/microsoft/generative-ai-for-beginners)
- [Generatiivne AI algajatele Java-s](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML algajatele](https://aka.ms/ml-beginners)
- [Andmeteadus algajatele](https://aka.ms/datascience-beginners)
- [AI algajatele](https://aka.ms/ai-beginners)
- [Küberkaitse algajatele](https://github.com/microsoft/Security-101)
- [Veebiarendus algajatele](https://aka.ms/webdev-beginners)
- [IoT algajatele](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Videopresentatsioonid

Õpi Co-op Translatori kohta rohkem meie ettekannetest _(Kliki alloleval pildil, et vaadata YouTube'is.)_:

- **Open at Microsoft**: Lühike 18-minutiline tutvustus ja kiire juhend Co-op Translatori kasutamiseks.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.et.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Kaasaaitamine

See projekt ootab panuseid ja ettepanekuid. Kas soovid aidata Azure Co-op Translatori arendamisel? Vaata meie [CONTRIBUTING.md](./CONTRIBUTING.md), et saada juhiseid, kuidas saad Co-op Translatori muuta veelgi kättesaadavamaks.

## Kaasautorid

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Käitumiskoodeks

See projekt järgib [Microsofti avatud lähtekoodiga käitumiskoodeksit](https://opensource.microsoft.com/codeofconduct/).
Lisainfo saamiseks vaata [Käitumiskoodeksi KKK](https://opensource.microsoft.com/codeofconduct/faq/) või
võta ühendust [opencode@microsoft.com](mailto:opencode@microsoft.com), kui sul on lisaküsimusi või kommentaare.

## Vastutustundlik AI

Microsoft on pühendunud sellele, et aidata klientidel kasutada meie AI-tooteid vastutustundlikult, jagada oma kogemusi ja luua usaldusel põhinevaid partnerlusi tööriistadega nagu Transparency Notes ja Impact Assessments. Paljud neist ressurssidest leiad aadressilt [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofti lähenemine vastutustundlikule AI-le põhineb meie AI põhimõtetel: õiglus, usaldusväärsus ja turvalisus, privaatsus ja turvalisus, kaasatus, läbipaistvus ja vastutus.

Suurte keelemudelite, pildimudelite ja kõnemudelite - nagu neid kasutatakse selles näites - käitumine võib olla ebaõiglane, ebausaldusväärne või solvav, mis võib põhjustada kahju. Palun tutvu [Azure OpenAI teenuse läbipaistvusmärkusega](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), et olla teadlik riskidest ja piirangutest.

Soovitatav viis nende riskide maandamiseks on lisada oma arhitektuuri turvasüsteem, mis suudab tuvastada ja ennetada kahjulikku käitumist. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pakub sõltumatut kaitsekihti, mis suudab tuvastada kahjulikku kasutaja- ja AI-genereeritud sisu rakendustes ja teenustes. Azure AI Content Safety sisaldab teksti- ja pildiliideseid, mis võimaldavad tuvastada kahjulikku materjali. Samuti on olemas interaktiivne Content Safety Studio, kus saad vaadata, uurida ja proovida näidiskoodi kahjuliku sisu tuvastamiseks erinevates vormides. Järgmine [kiirstardi dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) juhendab sind teenusele päringute tegemisel.


Teine oluline aspekt, mida arvestada, on rakenduse üldine jõudlus. Mitmeliigiliste ja mitmemudelitega rakenduste puhul tähendab jõudlus seda, et süsteem töötab nii, nagu sina ja sinu kasutajad ootavad, sealhulgas ei tekita kahjulikke väljundeid. Oluline on hinnata oma rakenduse üldist jõudlust, kasutades [generatsiooni kvaliteedi ning riski ja ohutuse mõõdikuid](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Saad oma tehisintellekti rakendust arenduskeskkonnas hinnata, kasutades [prompt flow SDK-d](https://microsoft.github.io/promptflow/index.html). Kasutades kas testandmestikku või sihtmärki, mõõdetakse sinu generatiivse AI rakenduse tulemusi kvantitatiivselt sisseehitatud või sinu valitud kohandatud hindajatega. Et alustada prompt flow SDK-ga oma süsteemi hindamist, järgi [kiirstardi juhendit](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kui oled hindamise käivitanud, saad [tulemusi visualiseerida Azure AI Studios](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Kaubamärgid

See projekt võib sisaldada kaubamärke või logosid, mis kuuluvad erinevatele projektidele, toodetele või teenustele. Microsofti kaubamärkide või logode volitatud kasutamine peab järgima [Microsofti kaubamärgi ja brändi juhiseid](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Microsofti kaubamärkide või logode kasutamine muudetud projektiversioonides ei tohi tekitada segadust ega jätta muljet, et Microsoft toetab projekti.
Kolmandate osapoolte kaubamärkide või logode kasutamine allub nende vastavatele reeglitele.

## Abi saamine

Kui jääd hätta või sul on küsimusi AI rakenduste loomise kohta, liitu:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Kui sul on tootetagasisidet või esineb vigu arendamisel, külasta:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle algses keeles on autoriteetne allikas. Kriitilise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgendamise eest.