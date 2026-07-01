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

**Alusta siit:** [Choose your workflow](https://azure.github.io/co-op-translator/workflows/) | [Configuration](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](./README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
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
> This gives you everything you need to complete the course with a much faster download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Ülevaade

**Co-op Translator** aitab sul hõlpsalt lokaliseerida oma hariduslikku GitHub-sisu mitmesse keelde.
Kui uuendad oma Markdown-faile, pilte või notebook'e, jäävad tõlked automaatselt sünkroonis, tagades, et sinu sisu on õppijatele üle maailma täpne ja ajakohane.

Kasuta seda CLI kaudu hoidla tõlkimiseks, Python API-st automaatika jaoks või MCP serveri kaudu agentide ja toimetajate töövoogude jaoks.

Näide sellest, kuidas tõlgitud sisu on organiseeritud:

![Näide](../../imgs/translation-ex.png)

## Miks Co-op Translator?

Ühe faili tõlkimine on lihtne. Kogu dokumentatsioonihoidla
tõlkimine, linkimine ja ajakohasena hoidmine on keeruline.

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | Suured Markdown-failid jagatakse tükkideks, nii et pikk README ei sõltu ühest habrasest mudeli vastusest. Kui mõni tükk ebaõnnestub, saab Co-op Translator katsetada uuesti ja ümberjaotada ainult ebaõnnestunud osa. |
| Incomplete translations should not be marked current | Lõhkemata tõlgitud versioon ei tohiks kunagi olla märgitud ajakohasena. Co-op Translator kontrollib tõlke terviklikkust enne salvestamist ja suudab tuvastada struktuurselt mittetäielikke olemasolevaid tõlkeid. |
| Links should match the translated repo structure | Käsitsi tehtud tõlked jätavad tihti suhtelised lingid viitama tagasi lähtepuule. Co-op Translator üm kirjutab Markdowni, notebooki, pildi- ja README-lingid nii, et need vastavad `translations/<lang>/...` struktuurile. |
| Translation should work across an entire repo | Co-op Translator käsitleb README-faile, dokumente, notebook'e ja pilditekste kui osa ühest hoidla töövoost, selle asemel et tõlkida faile ükshaaval. |
| Maintaining translations matters more than creating them once | Allika räsid ja tõlke metaandmed võimaldavad Co-op Translatoril leida aegunud faile, vahele jätta muutumatuid faile ja hoida tõlgitud sisu sünkroonis, kui lähtehoidla areneb. |

## Kuidas tõlkeolekut hallatakse

Co-op Translator haldab tõlgitud sisu kui **versioonitud tarkvaraartefakte**,  
mitte kui staatilisi faile.

Tööriist jälgib tõlgitud Markdowni, piltide ja notebook'ide olekut
kasutades **keele-spetsiifilisi metaandmeid**.

See disain võimaldab Co-op Translatoril:

- Usaldusväärselt tuvastada aegunud tõlkeid
- Käsitleda Markdowni, pilte ja notebook'e järjepidevalt
- Skaleeruda turvaliselt suuretes, kiiresti muutuvates mitmekeelsel hoidlates

Tõlkeid modelleerides hallatavate artefaktidena,
seostuvad tõlke töövood loomulikult kaasaegsete
tarkvara sõltuvus- ja artefaktihalduse praktikatega.

→ [Kuidas tõlkeolekut hallatakse](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Seotud põhjalikud artiklid

- [Fixing Broken Markdown in AI Translation: Hardening a Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Alustamine

Co-op Translatorit saab kasutada CLI-st, Python API-st või MCP serverist. Alusta töövoo juhendiga, kui valid lokaalse tõlke, automaatika, CI või agent/toimetaja integratsiooni vahel.

- [Choose your workflow](../../docs/workflows.md)
- [Configure credentials](../../docs/configuration.md)
- [Translate from the CLI](../../docs/cli.md)
- [Automate with the Python API](../../docs/api.md)
- [Connect with the MCP Server](../../docs/mcp.md)
- [Run in GitHub Actions](../../docs/github-actions.md)

Minimaalne CLI-näide pärast seadistamist:

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

Suuremate hoidlate esimeste käivituste puhul kasuta enne tõlgitud failide kirjutamist `--dry-run`. Vaata [CLI Reference](../../docs/cli.md) sisu tüüpide lippude, logide, ülevaatuse ja linkide migratsiooni kohta.

Konteineri kiire käivitamine Bash/Zsh-iga:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Konteineri kiire käivitamine PowerShelliga:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Funktsioonid

- Automatiseeritud tõlge Markdownile, notebook'idele ja piltidele
- Hoiab tõlked sünkroonis lähtemuudatustega
- Töötab lokaalselt (CLI) või CI-s (GitHub Actions)
- Avaldab Markdowni, notebook'i, pildi, ülevaatuse ja projekti tõlke tööriistad MCP kaudu
- Kasutab Azure OpenAI või OpenAI pakkujapõhist tõlget
- Lubab MCP-l majutada agente, kes tõlgivad Markdowni ja notebook'i tükke ilma Co-op Translatori LLM-i mandaatideta
- Kasutab Azure AI Visioni pilditeksti eraldamiseks ja tõlkimiseks
- Kontrollib tõlke struktuuri ja ajakohasust deterministlike kontrollidega
- Säilitab Markdowni vormingu ja struktuuri

## Dokumentatsioon

- [Documentation site](https://azure.github.io/co-op-translator/)
- [Choose your workflow](../../docs/workflows.md)
- [Configuration](../../docs/configuration.md)
- [Azure AI Setup](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README languages template](../../docs/readme-languages-template.md)
- [Supported languages](../../docs/supported-languages.md)
- [Contributing](../../CONTRIBUTING.md)
- [Troubleshooting](../../docs/troubleshooting.md)

### Microsoft-spetsiifiline juhend
> [!NOTE]
> Ainult Microsofti “For Beginners” hoidlate hooldajatele.

- [Updating the “other courses” list (for MS Beginners repositories only)](../../docs/microsoft-beginners.md)

## Toeta meid ja edenda ülemaailmset õppimist

Liitu meiega, et muuta see, kuidas hariduslikku sisu maailmas jagatakse! Anna [Co-op Translator](https://github.com/azure/co-op-translator) projektile GitHubis ⭐ ja toeta meie missiooni murda keelebarjäärid õppimises ja tehnoloogias. Sinu huvi ja panused avaldavad märkimisväärset mõju! Koodipanused ja funktsioonisoovid on alati teretulnud.

### Avasta Microsofti hariduslikku sisu oma keeles
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

## Videopresentatsioonid

👉 Klõpsake alloleval pildil, et vaadata YouTube'is.

- **Open at Microsoft**: Lühike 18-minutiline sissejuhatus ja kiire juhend, kuidas kasutada Co-op Translatorit.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Panustamine

See projekt tervitab panuseid ja ettepanekuid. Kas tunnete huvi Azure Co-op Translatorisse panustamise vastu? Palun vaadake meie [CONTRIBUTING.md](../../CONTRIBUTING.md), et saada juhiseid, kuidas saate aidata muuta Co-op Translatori kättesaadavamaks.

## Panustajad

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Käitumiskoodeks

See projekt on võtnud kasutusele [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Lisateabe saamiseks vaadake [Käitumiskoodeksi KKK](https://opensource.microsoft.com/codeofconduct/faq/) või pöörduge lisaküsimuste või kommentaaride korral aadressile [opencode@microsoft.com](mailto:opencode@microsoft.com).

## Vastutustundlik tehisintellekt

Microsoft on pühendunud aitama meie kliente kasutada meie AI-tooteid vastutustundlikult, jagama oma õppetunde ja ehitama usaldusel põhinevaid partnerlusi tööriistade abil, nagu Transparency Notes ja Impact Assessments. Paljusid neist ressurssidest leiate aadressilt [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofti lähenemine vastutustundlikule tehisintellektile põhineb meie tehisintellekti põhimõtetel: õigluses, usaldusväärsuses ja turvalisuses, privaatsuses ja turvalisuses, kaasatuses, läbipaistvuses ja vastutuses.

Suurte süsteemide loomuliku keele, pildi ja kõne mudelid - nagu need, mida selles näites kasutatakse - võivad potentsiaalselt käituda ebaõiglaselt, ebakindlalt või solvavalt, mis omakorda võib põhjustada kahju. Palun tutvuge [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), et saada teavet riskide ja piirangute kohta.

Soovitatav lähenemine nende riskide leevendamiseks on lisada oma arhitektuuri turvasüsteem, mis suudab tuvastada ja takistada kahjulikku käitumist. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pakub sõltumatut kaitsekihi, mis suudab rakendustes ja teenustes tuvastada kasutaja- ja AI-tekkelist kahjulikku sisu. Azure AI Content Safety sisaldab teksti- ja pildi-API-sid, mis võimaldavad tuvastada kahjulikku materjali. Samuti on meil interaktiivne Content Safety Studio, mis võimaldab vaadata, uurida ja proovida näitekoodi kahjuliku sisu tuvastamiseks erinevates modaliteetides. Järgmine [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) juhendab teid teenusele päringute tegemisel.

Teine aspekt, mida arvesse võtta, on kogu rakenduse jõudlus. Mitme-modaliteedi ja mitme-mudeliga rakenduste puhul tähendab jõudlus seda, et süsteem toimib nii, nagu teie ja teie kasutajad ootavad, sealhulgas mitte genereerides kahjulikke väljundeid. Oluline on hinnata kogu teie rakenduse jõudlust, kasutades [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Saate hinnata oma AI-rakendust arenduskeskkonnas, kasutades [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Olenevalt kas testandmestikust või eesmärgist, mõõdetakse teie generatiivse AI-rakenduse genereeringud kvantitatiivselt sisseehitatud hindajate või teie valitud kohandatud hindajate abil. Alustamiseks, et hinnata oma süsteemi prompt flow SDK abil, võite järgida [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kui olete hindamisprotsessi läbi viinud, saate [visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Kaubamärgid

See projekt võib sisaldada projektide, toodete või teenuste kaubamärke või logosid. Microsofti kaubamärkide või logode autoriseeritud kasutamine peab toimuma vastavalt ja järgima [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Microsofti kaubamärkide või logode kasutamine muudetud versioonides sellest projektist ei tohi tekitada segadust ega jätta muljet Microsofti toetusest.
Kolmandate osapoolte kaubamärkide või logode kasutamine allub vastavate kolmandate osapoolte poliitikatele.

## Abi

Kui takerdute või teil on küsimusi AI-rakenduste loomise kohta, liituge:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kui teil on toodet puudutavat tagasisidet või ehitamise käigus ilmnevaid vigu, külastage:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)