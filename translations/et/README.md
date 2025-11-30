<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T13:01:14+00:00",
  "source_file": "README.md",
  "language_code": "et"
}
-->
# Co-op Tõlkija

_Lihtsalt automatiseeri oma haridusliku GitHubi sisu tõlkimine mitmesse keelde, et jõuda ülemaailmse publikuni._

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

#### Toetatud [Co-op Translator](https://github.com/Azure/Co-op-Translator) poolt

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Araabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Hiina (lihtsustatud)](../zh/README.md) | [Hiina (traditsiooniline, Hongkong)](../hk/README.md) | [Hiina (traditsiooniline, Macau)](../mo/README.md) | [Hiina (traditsiooniline, Taiwan)](../tw/README.md) | [Horvaadi](../hr/README.md) | [Tšehhi](../cs/README.md) | [Taani](../da/README.md) | [Hollandi](../nl/README.md) | [Eesti](./README.md) | [Soome](../fi/README.md) | [Prantsuse](../fr/README.md) | [Saksa](../de/README.md) | [Kreeka](../el/README.md) | [Heebrea](../he/README.md) | [Hindi](../hi/README.md) | [Ungari](../hu/README.md) | [Indoneesia](../id/README.md) | [Itaalia](../it/README.md) | [Jaapani](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Leedu](../lt/README.md) | [Malai](../ms/README.md) | [Malajalami](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeeria pidžin](../pcm/README.md) | [Norra](../no/README.md) | [Pärsia (Farsi)](../fa/README.md) | [Poola](../pl/README.md) | [Portugali (Brasiilia)](../br/README.md) | [Portugali (Portugal)](../pt/README.md) | [Pandžabi (Gurmukhi)](../pa/README.md) | [Rumeenia](../ro/README.md) | [Vene](../ru/README.md) | [Serbia (kirillitsa)](../sr/README.md) | [Slovaki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Hispaania](../es/README.md) | [Suaheli](../sw/README.md) | [Rootsi](../sv/README.md) | [Tagalogi (Filipino)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Tai](../th/README.md) | [Türgi](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Ülevaade

**Co-op Tõlkija** aitab sul hõlpsasti lokaliseerida oma hariduslikku GitHubi sisu mitmesse keelde.
Kui uuendad oma Markdown-faile, pilte või märkmikke, siis tõlked sünkroonitakse automaatselt, tagades, et sinu sisu on õppijatele üle maailma täpne ja ajakohane.

Näide, kuidas tõlgitud sisu on organiseeritud:

![Näide](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.et.png)

## Kiire algus

```bash
# Loo ja aktiveeri virtuaalne keskkond (soovitatav)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Paigalda pakett
pip install co-op-translator
# Tõlgi
translate -l "ko ja fr" -md
```

Docker:

```bash
# Tõmba avalik pilt GHCR-ist
docker pull ghcr.io/azure/co-op-translator:latest
# Käivita koos praeguse kaustaga ja .env failiga (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimaalne seadistus

1. Loo `.env` fail kasutades mallina: [.env.template](../../.env.template)
2. Sea sisse üks LLM pakkuja (Azure OpenAI või OpenAI)
3. (Valikuline) Piltide tõlkimiseks (`-img`) seadista Azure AI Vision
4. (Soovitatav) Puhasta varasemad tõlked konfliktide vältimiseks (nt `translations/`)
5. (Soovitatav) Lisa tõlke sektsioon oma README-sse kasutades [README keelte malli](./getting_started/README_languages_template.md)
6. Vaata: [Azure AI seadistamine](./getting_started/set-up-azure-ai.md)

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

Rohkem lippe: [Käsurea viide](./getting_started/command-reference.md)

## Omadused

- Automaatne tõlkimine Markdowni, märkmike ja piltide jaoks
- Hoiab tõlked allikamuudatustega sünkroonis
- Töötab lokaalselt (CLI) või CI-s (GitHub Actions)
- Kasutab Azure OpenAI või OpenAI; piltide jaoks valikuline Azure AI Vision
- Säilitab Markdowni vorminduse ja struktuuri

## Dokumentatsioon

- [Käsurea juhend](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions juhend (avalikud hoidlad & standard salajased võtmed)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions juhend (Microsofti organisatsiooni hoidlad & organisatsiooni tasandi seadistused)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README keelte mall](./getting_started/README_languages_template.md)
- [Toetatud keeled](./getting_started/supported-languages.md)
- [Panustamine](./CONTRIBUTING.md)
- [Veaotsing](./getting_started/troubleshooting.md)

### Microsofti-spetsiifiline juhend
> [!NOTE]
> Ainult Microsofti “Algajatele” hoidlate hooldajatele.

- [“Muud kursused” nimekirja uuendamine (ainult MS Algajate hoidlate jaoks)](./getting_started/update-other-courses.md)

## Toeta meid ja edenda ülemaailmset õppimist

Liitu meiega haridusliku sisu ülemaailmse jagamise revolutsioonis! Anna [Co-op Translatorile](https://github.com/azure/co-op-translator) GitHubis ⭐ ja toeta meie missiooni murda keelebarjääre õppimises ja tehnoloogias. Sinu huvi ja panused on väga olulised! Koodipanused ja funktsioonisoovitused on alati teretulnud.

### Avastage Microsofti hariduslikku sisu oma keeles

- [AZD algajatele](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI algajatele](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) algajatele](https://github.com/microsoft/mcp-for-beginners)
- [AI agendid algajatele](https://github.com/microsoft/ai-agents-for-beginners)
- [Generatiivne AI algajatele .NETiga](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatiivne AI algajatele](https://github.com/microsoft/generative-ai-for-beginners)
- [Generatiivne AI algajatele Java abil](https://github.com/microsoft/generative-ai-for-beginners-java)
- [Masinõpe algajatele](https://aka.ms/ml-beginners)
- [Andmeteadus algajatele](https://aka.ms/datascience-beginners)
- [Tehisintellekt algajatele](https://aka.ms/ai-beginners)
- [Küberjulgeolek algajatele](https://github.com/microsoft/Security-101)
- [Veebiarendus algajatele](https://aka.ms/webdev-beginners)
- [IoT algajatele](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Videopresentatsioonid

👉 Klõpsa alloleval pildil, et vaadata YouTube'is.

- **Open at Microsoft**: Lühike 18-minutiline sissejuhatus ja kiire juhend Co-op Tõlkija kasutamiseks.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.et.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Panustamine

See projekt ootab panuseid ja ettepanekuid. Kas soovid aidata Azure Co-op Translatori arendamisel? Palun vaata meie [CONTRIBUTING.md](./CONTRIBUTING.md) juhiseid, kuidas saad aidata muuta Co-op Tõlkija kättesaadavamaks.

## Panustajad

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Käitumisjuhend

See projekt on võtnud kasutusele [Microsofti avatud lähtekoodi käitumisjuhendi](https://opensource.microsoft.com/codeofconduct/).
Lisainfo leiad [Käitumisjuhendi KKK-st](https://opensource.microsoft.com/codeofconduct/faq/) või võta ühendust aadressil [opencode@microsoft.com](mailto:opencode@microsoft.com) küsimuste või kommentaaride korral.

## Vastutustundlik tehisintellekt

Microsoft on pühendunud aitama klientidel kasutada meie tehisintellekti tooteid vastutustundlikult, jagades oma kogemusi ja luues usaldusel põhinevaid partnerlussuhteid tööriistadega nagu Transparency Notes ja Impact Assessments. Paljud neist ressurssidest on leitavad aadressil [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofti lähenemine vastutustundlikule tehisintellektile põhineb meie tehisintellekti põhimõtetel: õiglus, usaldusväärsus ja ohutus, privaatsus ja turvalisus, kaasatus, läbipaistvus ja vastutus.

Suurte keele-, pildi- ja kõnemudelite puhul – nagu neid selles näites kasutatakse – võib esineda ebaõiglaseid, usaldamatuid või solvavaid käitumisviise, mis võivad põhjustada kahju. Palun tutvu [Azure OpenAI teenuse läbipaistvuse märkusega](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), et olla teadlik riskidest ja piirangutest.
Soovitatav lähenemine nende riskide vähendamiseks on lisada oma arhitektuuri turvasüsteem, mis suudab tuvastada ja takistada kahjulikku käitumist. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pakub sõltumatut kaitsekihi, mis suudab rakendustes ja teenustes tuvastada kahjulikku kasutajate ja tehisintellekti loodud sisu. Azure AI Content Safety sisaldab teksti- ja pildirakendusliideseid, mis võimaldavad tuvastada kahjulikku materjali. Samuti on meil interaktiivne Content Safety Studio, mis võimaldab teil vaadata, uurida ja proovida näidiskoodi kahjuliku sisu tuvastamiseks erinevates vormingutes. Järgmine [kiirjuhendi dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) juhendab teid teenusele päringute tegemisel.

Teine oluline aspekt on kogu rakenduse jõudlus. Mitme modaaliga ja mitme mudeliga rakenduste puhul mõistame jõudluse all seda, et süsteem töötab nii, nagu teie ja teie kasutajad ootavad, sealhulgas ei genereeri kahjulikke väljundeid. Oluline on hinnata kogu rakenduse jõudlust, kasutades [generatsiooni kvaliteedi ning riski- ja turvameetmeid](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Saate oma tehisintellekti rakendust hinnata arenduskeskkonnas, kasutades [prompt flow SDK-d](https://microsoft.github.io/promptflow/index.html). Kasutades kas testandmestikku või sihtmärki, mõõdetakse teie generatiivse tehisintellekti rakenduse väljundeid kvantitatiivselt sisseehitatud või teie valitud kohandatud hindajatega. Prompt flow SDK-ga alustamiseks ja süsteemi hindamiseks võite järgida [kiirjuhendi](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kui olete hindamise käivitanud, saate [tulemusi visualiseerida Azure AI Studios](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Kaubamärgid

See projekt võib sisaldada kaubamärke või logosid projektide, toodete või teenuste jaoks. Microsofti kaubamärkide või logode autoriseeritud kasutamine peab vastama ja järgima [Microsofti kaubamärgi- ja brändijuhiseid](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Microsofti kaubamärkide või logode kasutamine selle projekti muudetud versioonides ei tohi tekitada segadust ega viidata Microsofti sponsorlusele. Kolmandate osapoolte kaubamärkide või logode kasutamine allub nende kolmandate osapoolte poliitikatele.

## Abi saamine

Kui teil tekib takistusi või küsimusi tehisintellekti rakenduste loomisel, liituge:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kui teil on toote tagasisidet või ehitamisel esineb vigu, külastage:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->