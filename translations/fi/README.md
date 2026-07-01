# Co-op Translator

_Helposti automatisoi ja ylläpidä käännöksiä opetussisällöllesi GitHubissa useille kielille projektisi kehittyessä._

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

**Aloita tästä:** [Valitse työnkulku](https://azure.github.io/co-op-translator/workflows/) | [Konfigurointi](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Monikielinen tuki

#### Tuettu [Co-op Translatorin](https://github.com/Azure/co-op-translator) toimesta

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaria](../bg/README.md) | [Burma (Myanmar)](../my/README.md) | [Kiina (yksinkertaistettu)](../zh-CN/README.md) | [Kiina (perinteinen, Hongkong)](../zh-HK/README.md) | [Kiina (perinteinen, Macao)](../zh-MO/README.md) | [Kiina (perinteinen, Taiwan)](../zh-TW/README.md) | [Kroatia](../hr/README.md) | [Tšekki](../cs/README.md) | [Tanska](../da/README.md) | [Hollanti](../nl/README.md) | [Viro](../et/README.md) | [Suomi](./README.md) | [Ranska](../fr/README.md) | [Saksa](../de/README.md) | [Kreikka](../el/README.md) | [Heprea](../he/README.md) | [Hindi](../hi/README.md) | [Unkari](../hu/README.md) | [Indonesia](../id/README.md) | [Italia](../it/README.md) | [Japani](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korea](../ko/README.md) | [Liettua](../lt/README.md) | [Malaiji](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norja](../no/README.md) | [Persia (farsi)](../fa/README.md) | [Puola](../pl/README.md) | [Portugali (Brasilia)](../pt-BR/README.md) | [Portugali (Portugali)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romania](../ro/README.md) | [Venäjä](../ru/README.md) | [Serbia (kyrillinen)](../sr/README.md) | [Slovakki](../sk/README.md) | [Slovenia](../sl/README.md) | [Espanja](../es/README.md) | [Swahili](../sw/README.md) | [Ruotsi](../sv/README.md) | [Tagalog (filipino)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkki](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)

> **Haluatko mieluummin kloonata paikallisesti?**
>
> Tämä repositorio sisältää yli 50 käännöstä, mikä lisää latauksen kokoa merkittävästi. Jos haluat kloonata ilman käännöksiä, käytä sparse checkoutia:
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
> Tämä antaa sinulle kaiken tarvittavan kurssin suorittamiseen huomattavasti nopeammalla latauksella.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Yleiskatsaus

**Co-op Translator** auttaa lokalisoimaan opetussisältösi GitHubissa useille kielille vaivattomasti.
Kun päivität Markdown-tiedostojasi, kuvia tai muistikirjoja, käännökset pysyvät automaattisesti synkronoituina, varmistaen että sisältösi on tarkkaa ja ajan tasalla oppijoille ympäri maailmaa.

Käytä sitä CLI:stä repositorion kääntämiseen, Python-API:sta automaatioon tai MCP-palvelimen kautta agentti- ja editorityönkulkuihin.

Esimerkki siitä, miten käännetty sisältö on järjestetty:

![Esimerkki](../../imgs/translation-ex.png)

## Miksi Co-op Translator?

Yhden tiedoston kääntäminen on helppoa. Koko dokumentaatio­repositorion
pitämiseen käännettynä, linkitettynä ja ajan tasalla onkin se vaikea osa.

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | Suuret Markdown-tiedostot pilkotaan osiin, joten pitkä README ei riipu yhdestä hauraasta mallivastauksesta. Jos osa epäonnistuu, Co-op Translator voi yrittää uudelleen ja pilkkoa uudelleen vain epäonnistuneen osan. |
| Incomplete translations should not be marked current | Katkennutta käännöstä ei tulisi koskaan merkitä ajan tasalla olevaksi. Co-op Translator tarkistaa käännöksen eheyden ennen tallennusta ja voi havaita rakenteellisesti puutteelliset olemassa olevat käännökset. |
| Links should match the translated repo structure | Manuaaliset käännökset jättävät usein suhteellisia linkkejä osoittamaan takaisin lähdepuihin. Co-op Translator muokkaa Markdown-, muistikirja-, kuva- ja README-linkkejä vastaamaan `translations/<lang>/...` -rakennetta. |
| Translation should work across an entire repo | Co-op Translator käsittelee README-tiedostot, dokumentaation, muistikirjat ja kuvatekstit yhtenä repositorion työnkulkuna sen sijaan, että tiedostoja käännettäisiin yksi kerrallaan. |
| Maintaining translations matters more than creating them once | Lähde­tarkisteet ja käännös­metatiedot antavat Co-op Translatorille mahdollisuuden löytää vanhentuneet tiedostot, ohittaa muuttumattomat tiedostot ja pitää käännetyn sisällön synkronoituna lähderepositoryn kehittyessä. |

## Kuinka käännösten tila hallitaan

Co-op Translator käsittelee käännetyn sisällön kuin versionhallittuja ohjelmistoartefakteja,  
ei staattisina tiedostoina.

Työkalu seuraa käännettyjen Markdownien, kuvien ja muistikirjojen tilaa
käyttäen **kieleen sidottua metatietoa**.

Tämä suunnittelu mahdollistaa Co-op Translatorille:

- Luotettavan vanhentuneiden käännösten havaitsemisen
- Markdownin, kuvien ja muistikirjojen yhtenäisen käsittelyn
- Skaalautumisen turvallisesti suurissa, nopeasti kehittyvissä monikielisissä repositorioissa

Mallintamalla käännökset hallituiksi artefakteiksi,
käännöstyönkulut nivoutuvat luonnollisesti nykyaikaisiin
ohjelmistoriippuvuus- ja artefaktinhallintakäytäntöihin.

→ [Miten käännöstila hallitaan](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Lisäsyventävät artikkelit

- [Korjataan rikkinäisiä Markdown-tiedostoja AI-käännöksissä: tuotantoputken koventaminen](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Aloita

Co-op Translatoria voi käyttää CLI:stä, Python-API:sta tai MCP-palvelimelta. Aloita työnkulku-oppaan lukemisella, jos valintasi on paikallinen käännös, automaatio, CI tai agentti/editor -integraatio.

- [Valitse työnkulku](../../docs/workflows.md)
- [Konfigurointi](../../docs/configuration.md)
- [Käännä CLI:stä](../../docs/cli.md)
- [Automatisoi Python-API:lla](../../docs/api.md)
- [Yhdistä MCP-palvelimeen](../../docs/mcp.md)
- [Suorita GitHub Actionsissa](../../docs/github-actions.md)

Esimerkinomainen minimal CLI -komento konfiguroinnin jälkeen:

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

Suorita suurille repolle ensimmäisillä kerroilla `--dry-run` ennen käännettyjen tiedostojen kirjoittamista. Katso [CLI-viite](../../docs/cli.md) sisältötyyppien lipuista, lokeista, tarkastuksesta ja linkkimigraatiosta.

Konttipikatesti Bash/Zsh:llä:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Konttipikatesti PowerShellilla:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Ominaisuudet

- Automaattinen käännös Markdownille, muistikirjoille ja kuville
- Pitää käännökset synkronissa lähdemuutosten kanssa
- Toimii paikallisesti (CLI) tai CI:ssä (GitHub Actions)
- Altistaa Markdown-, muistikirja-, kuva-, tarkastus- ja projekti­käännöstyökalut MCP:n kautta
- Käyttää Azure OpenAI:ta tai OpenAI:ta tarjoajan tukemaan käännöstä
- Antaa MCP:n isännöimien agenttien kääntää Markdown- ja muistikirja-osioita ilman Co-op Translatorin LLM-tunnuksia
- Käyttää Azure AI Visionia kuvatekstien poimintaan ja käännökseen
- Tarkastaa käännösten rakenteen ja ajantasaisuuden deterministisilla tarkistuksilla
- Säilyttää Markdownin muotoilun ja rakenteen

## Dokumentaatio

- [Dokumentaatiosivusto](https://azure.github.io/co-op-translator/)
- [Valitse työnkulku](../../docs/workflows.md)
- [Konfigurointi](../../docs/configuration.md)
- [Azure AI -asetukset](../../docs/azure-ai-setup.md)
- [CLI-viite](../../docs/cli.md)
- [Python-API](../../docs/api.md)
- [MCP-palvelin](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README-kielten malli](../../docs/readme-languages-template.md)
- [Tuetut kielet](../../docs/supported-languages.md)
- [Osallistuminen](../../CONTRIBUTING.md)
- [Vianmääritys](../../docs/troubleshooting.md)

### Microsoftille tarkoitettu opas
> [!NOTE]
> Vain Microsoftin “For Beginners” -repositorioiden ylläpitäjille.

- [Päivitä “other courses” -lista (vain MS Beginners -repositorioille)](../../docs/microsoft-beginners.md)

## Tue meitä ja edistä maailmanlaajuista oppimista

Liity mukaan muuttamaan tapaa, jolla opetussisältöjä jaetaan globaalisti! Anna [Co-op Translator](https://github.com/azure/co-op-translator) -projektille ⭐ GitHubissa ja tue missiotamme poistaa kielimuurit oppimisessa ja teknologiassa. Kiinnostuksesi ja panoksesi vaikuttavat merkittävästi! Koodipanokset ja ominaisuusehdotukset ovat aina tervetulleita.

### Tutustu Microsoftin opetussisältöihin omalla kielelläsi
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

## Video presentations

👉 Napsauta alla olevaa kuvaa katsoaksesi YouTubessa.

- **Open at Microsoft**: Lyhyt 18 minuutin esittely ja pikaopas Co-op Translatorin käyttöön.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contributing

Tämä projekti ottaa mielellään vastaan kontribuutioita ja ehdotuksia. Haluatko osallistua Azure Co-op Translatorin kehittämiseen? Katso ohjeet [CONTRIBUTING.md](../../CONTRIBUTING.md) tiedostosta, josta löydät ohjeet siitä, miten voit auttaa tekemään Co-op Translatorista saavutettavamman.

## Contributors

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Tämä projekti on ottanut käyttöön [Microsoftin avoimen lähdekoodin toimintaperiaatteet](https://opensource.microsoft.com/codeofconduct/). Lisätietoja saat katsomalla [Toimintaperiaatteiden UKK](https://opensource.microsoft.com/codeofconduct/faq/) -sivun tai ottamalla yhteyttä osoitteeseen [opencode@microsoft.com](mailto:opencode@microsoft.com) jos sinulla on lisäkysymyksiä tai kommentteja.

## Responsible AI

Microsoft on sitoutunut auttamaan asiakkaitamme käyttämään tekoälytuotteitamme vastuullisesti, jakamaan oppimiamme ja rakentamaan luottamukseen perustuvia kumppanuuksia esimerkiksi Transparency Notes- ja Impact Assessments -työkalujen kautta. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftin lähestymistapa vastuulliseen tekoälyyn perustuu tekoälyn periaatteisiimme: oikeudenmukaisuus, luotettavuus ja turvallisuus, yksityisyys ja tietoturva, osallistavuus, läpinäkyvyys ja vastuullisuus.

Laajamittaiset luonnollisen kielen, kuva- ja puhemallit — kuten tässä esimerkissä käytetyt — voivat käyttäytyä tavoilla, jotka ovat epäoikeudenmukaisia, epäluotettavia tai loukkaavia, ja aiheuttaa vahinkoa. Tutustu [Azure OpenAI -palvelun läpinäkyvyysmuistioon](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) saadaksesi tietoa riskeistä ja rajoituksista.

Suositeltava tapa vähentää näitä riskejä on sisällyttää arkkitehtuuriisi turvallisuusjärjestelmä, joka voi tunnistaa ja estää haitallista käyttäytymistä. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tarjoaa itsenäisen suojaustason, joka pystyy havaitsemaan sovelluksissa ja palveluissa käyttäjän tai tekoälyn tuottamaa haitallista sisältöä. Azure AI Content Safety sisältää tekstin ja kuvan API:t, joiden avulla voit tunnistaa haitallista materiaalia. Meillä on myös interaktiivinen Content Safety Studio, jonka avulla voit tarkastella, tutkia ja kokeilla esimerkkikoodeja haitallisen sisällön tunnistamiseen eri modaliteeteissa. Seuraava [aloitusopas](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) opastaa tekemään pyyntöjä palveluun.

Toinen huomioon otettava seikka on koko sovelluksen suorituskyky. Monimodaalisissa ja monimalli-sovelluksissa suorituskyvyllä tarkoitamme sitä, että järjestelmä toimii odotetulla tavalla sinulle ja käyttäjillesi, mukaan lukien se, ettei se tuota haitallisia tulosteita. On tärkeää arvioida koko sovelluksesi suorituskykyä käyttämällä [generointilaatua sekä riski- ja turvallisuusmittareita](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Voit arvioida tekoälysovellustasi kehitysympäristössä käyttämällä [prompt flow -SDK:ta](https://microsoft.github.io/promptflow/index.html). Olipa käytössäsi testiaineisto tai tavoite, generatiivisen tekoälysovelluksesi tuotoksia mitataan kvantitatiivisesti sisäänrakennetuilla arvioijilla tai valitsemillasi mukautetuilla arvioijilla. Aloittaaksesi prompt flow -SDK:n käytön järjestelmäsi arviointiin, voit seurata [aloitusopasta](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kun suoritat arviointiajon, voit [visualisoida tulokset Azure AI Studiossa](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Tämä projekti saattaa sisältää tavaramerkkejä tai logoja projekteille, tuotteille tai palveluille. Microsoftin tavaramerkkien tai logojen luvallinen käyttö edellyttää noudattamista [Microsoftin tavaramerkki- ja brändiohjeita](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Microsoftin tavaramerkkien tai logojen käyttö tämän projektin muokatuissa versioissa ei saa aiheuttaa sekaannusta tai antaa vaikutelmaa Microsoftin sponsoroinnista. Kolmansien osapuolten tavaramerkkien tai logojen käyttöä ohjaavat kyseisten osapuolten käytännöt.

## Getting Help

Jos juudut tai sinulla on kysyttävää tekoälysovellusten rakentamisesta, liity:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jos sinulla on tuotepalautetta tai kohtaat virheitä rakentamisen aikana, vieraile:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)