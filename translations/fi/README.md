<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T11:32:22+00:00",
  "source_file": "README.md",
  "language_code": "fi"
}
-->
# Co-op Translator

_Helppo tapa automatisoida koulutussisältösi kääntäminen GitHubissa useille kielille ja tavoittaa maailmanlaajuinen yleisö._

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

### 🌐 Monikielinen tuki

#### Tuettu [Co-op Translatorin](https://github.com/Azure/Co-op-Translator) toimesta

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaria](../bg/README.md) | [Burma (Myanmar)](../my/README.md) | [Kiina (yksinkertaistettu)](../zh/README.md) | [Kiina (perinteinen, Hong Kong)](../hk/README.md) | [Kiina (perinteinen, Macao)](../mo/README.md) | [Kiina (perinteinen, Taiwan)](../tw/README.md) | [Kroatia](../hr/README.md) | [Tšekki](../cs/README.md) | [Tanska](../da/README.md) | [Hollanti](../nl/README.md) | [Viro](../et/README.md) | [Suomi](./README.md) | [Ranska](../fr/README.md) | [Saksa](../de/README.md) | [Kreikka](../el/README.md) | [Heprea](../he/README.md) | [Hindi](../hi/README.md) | [Unkari](../hu/README.md) | [Indonesia](../id/README.md) | [Italia](../it/README.md) | [Japani](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Liettua](../lt/README.md) | [Malaiji](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norja](../no/README.md) | [Persia (Farsi)](../fa/README.md) | [Puola](../pl/README.md) | [Portugali (Brasilia)](../br/README.md) | [Portugali (Portugali)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romania](../ro/README.md) | [Venäjä](../ru/README.md) | [Serbia (kyrillinen)](../sr/README.md) | [Slovakki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Espanja](../es/README.md) | [Swahili](../sw/README.md) | [Ruotsi](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkki](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Yleiskatsaus

**Co-op Translator** auttaa sinua lokalisoimaan koulutussisältösi GitHubissa useille kielille vaivattomasti. Kun päivität Markdown-tiedostojasi, kuvia tai muistikirjoja, käännökset pysyvät automaattisesti synkronoituna, varmistaen että sisältösi on tarkkaa ja ajan tasalla oppijoille ympäri maailmaa.

Esimerkki siitä, miten käännetty sisältö on järjestetty:

![Esimerkki](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.fi.png)

## Nopeasti käyntiin

```bash
# Luo ja aktivoi virtuaaliympäristö (suositeltavaa)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Asenna paketti
pip install co-op-translator
# Käännä
translate -l "ko ja fr" -md
```

Docker:

```bash
# Vedä julkinen kuva GHCR:stä
docker pull ghcr.io/azure/co-op-translator:latest
# Suorita nykyisellä kansiolla liitettynä ja .env-tiedosto annettuna (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimiasennus

1. Luo `.env`-tiedosto mallin pohjalta: [.env.template](../../.env.template)
2. Määritä yksi LLM-palveluntarjoaja (Azure OpenAI tai OpenAI)
3. (Valinnainen) Kuvien kääntämiseen (`-img`) määritä Azure AI Vision
4. (Suositeltavaa) Siivoa aiemmat käännökset ristiriitojen välttämiseksi (esim. `translations/`)
5. (Suositeltavaa) Lisää käännösosio README-tiedostoosi käyttäen [README kielimallia](./getting_started/README_languages_template.md)
6. Katso: [Azure AI:n käyttöönotto](./getting_started/set-up-azure-ai.md)

## Käyttö

Käännä kaikki tuetut tyypit:

```bash
translate -l "ko ja"
```

Vain Markdown:

```bash
translate -l "de" -md
```

Markdown + kuvat:

```bash
translate -l "pt" -md -img
```

Vain muistikirjat:

```bash
translate -l "zh" -nb
```

Lisää valitsimia: [Komentoviite](./getting_started/command-reference.md)

## Ominaisuudet

- Automaattinen käännös Markdownille, muistikirjoille ja kuville
- Pitää käännökset synkronoituna lähdemuutosten kanssa
- Toimii paikallisesti (CLI) tai CI:ssä (GitHub Actions)
- Käyttää Azure OpenAI:ta tai OpenAI:ta; valinnainen Azure AI Vision kuville
- Säilyttää Markdownin muotoilun ja rakenteen

## Dokumentaatio

- [Komentoriviohje](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions -opas (julkiset repositoriot & standard salaisuudet)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions -opas (Microsoft-organisaation repositoriot & organisaatiotason asetukset)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README kielimalli](./getting_started/README_languages_template.md)
- [Tuetut kielet](./getting_started/supported-languages.md)
- [Osallistuminen](./CONTRIBUTING.md)
- [Vianmääritys](./getting_started/troubleshooting.md)

### Microsoftille suunnattu opas
> [!NOTE]
> Vain Microsoftin “For Beginners” -repositorioiden ylläpitäjille.

- [“Other courses” -listan päivittäminen (vain MS Beginners -repositorioille)](./getting_started/update-other-courses.md)

## Tue meitä ja edistä maailmanlaajuista oppimista

Liity mukaan mullistamaan koulutussisällön jakamista maailmanlaajuisesti! Anna [Co-op Translatorille](https://github.com/azure/co-op-translator) ⭐ GitHubissa ja tue missiotamme poistaa kielimuurit oppimisessa ja teknologiassa. Kiinnostuksesi ja panoksesi ovat merkittäviä! Koodiparannukset ja ominaisuusehdotukset ovat aina tervetulleita.

### Tutustu Microsoftin koulutussisältöihin omalla kielelläsi

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

## Videoesitykset

👉 Klikkaa alla olevaa kuvaa katsoaksesi YouTubessa.

- **Open at Microsoft**: Lyhyt 18 minuutin esittely ja nopea opas Co-op Translatorin käyttöön.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.fi.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Osallistuminen

Tämä projekti toivottaa tervetulleiksi panokset ja ehdotukset. Haluatko osallistua Azure Co-op Translatorin kehitykseen? Katso ohjeet [CONTRIBUTING.md](./CONTRIBUTING.md) -tiedostosta, miten voit auttaa tekemään Co-op Translatorista entistä saavutettavamman.

## Tekijät

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Käyttäytymissäännöt

Tämä projekti on ottanut käyttöön [Microsoftin avoimen lähdekoodin käyttäytymissäännöt](https://opensource.microsoft.com/codeofconduct/).
Lisätietoja löytyy [Käyttäytymissääntöjen UKK](https://opensource.microsoft.com/codeofconduct/faq/) -osiosta tai ota yhteyttä osoitteeseen [opencode@microsoft.com](mailto:opencode@microsoft.com) lisäkysymyksissä tai palautteessa.

## Vastuullinen tekoäly

Microsoft sitoutuu auttamaan asiakkaitaan käyttämään tekoälytuotteitamme vastuullisesti, jakamaan oppejamme ja rakentamaan luottamukseen perustuvia kumppanuuksia työkalujen, kuten Transparency Notes ja Impact Assessments, avulla. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftin lähestymistapa vastuulliseen tekoälyyn perustuu tekoälyn periaatteisiin: oikeudenmukaisuus, luotettavuus ja turvallisuus, yksityisyys ja tietoturva, osallisuus, läpinäkyvyys ja vastuullisuus.

Laajamittaiset luonnollisen kielen, kuvan ja puheen mallit – kuten tässä esimerkissä käytetyt – voivat käyttäytyä tavoilla, jotka ovat epäoikeudenmukaisia, epäluotettavia tai loukkaavia, aiheuttaen haittoja. Tutustu [Azure OpenAI -palvelun Transparency noteen](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) saadaksesi tietoa riskeistä ja rajoituksista.
Suositeltu tapa vähentää näitä riskejä on sisällyttää arkkitehtuuriisi turvajärjestelmä, joka pystyy havaitsemaan ja estämään haitallisen käyttäytymisen. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> tarjoaa itsenäisen suojakerroksen, joka pystyy tunnistamaan haitallisen käyttäjän tuottaman ja tekoälyn luoman sisällön sovelluksissa ja palveluissa. Azure AI Content Safety sisältää tekstin ja kuvien API-rajapinnat, joiden avulla voit havaita haitallista materiaalia. Meillä on myös interaktiivinen Content Safety Studio, jonka avulla voit tarkastella, tutkia ja kokeilla esimerkkikoodeja haitallisen sisällön tunnistamiseen eri muodoissa. Seuraava <a href="https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest">aloitusopas</a> ohjaa sinua tekemään pyyntöjä palveluun.

Toinen huomioon otettava seikka on sovelluksen kokonaisvaltainen suorituskyky. Monimuotoisissa ja monimallipohjaisissa sovelluksissa suorituskyvyllä tarkoitetaan sitä, että järjestelmä toimii odotustesi ja käyttäjiesi odotusten mukaisesti, mukaan lukien haitallisten tulosten välttäminen. On tärkeää arvioida koko sovelluksesi suorituskykyä käyttämällä <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">generoinnin laatua sekä riski- ja turvallisuusmittareita</a>.

Voit arvioida tekoälysovellustasi kehitysympäristössäsi käyttämällä <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK:ta</a>. Olipa käytössäsi testiaineisto tai tavoite, generatiivisen tekoälysovelluksesi tuotokset mitataan määrällisesti sisäänrakennetuilla arvioijilla tai valitsemillasi mukautetuilla arvioijilla. Järjestelmän arvioinnin aloittamiseksi prompt flow SDK:lla voit seurata <a href="https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk">aloitusopasta</a>. Kun suoritat arviointikierroksen, voit <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">visualisoida tulokset Azure AI Studiossa</a>.

## Tavara- ja palvelumerkit

Tämä projekti saattaa sisältää tavara- tai palvelumerkkejä tai logoja projekteista, tuotteista tai palveluista. Microsoftin tavara- tai palvelumerkkien valtuutettu käyttö edellyttää ja noudattaa <a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">Microsoftin tavara- ja brändiohjeita</a>. Microsoftin tavara- tai palvelumerkkien käyttö muokatuissa versioissa tästä projektista ei saa aiheuttaa sekaannusta tai antaa vaikutelmaa Microsoftin sponsoroimasta. Kolmansien osapuolten tavara- tai palvelumerkkien käyttö on näiden osapuolten sääntöjen alaista.

## Apua saatavilla

Jos jäät jumiin tai sinulla on kysyttävää tekoälysovellusten rakentamisesta, liity:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jos sinulla on tuotepalautetta tai kohtaat virheitä rakentamisen aikana, käy:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->