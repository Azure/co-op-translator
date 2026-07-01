# Co-op Translator

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Pakete ng Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Lisensya: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Mga pag-download](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Mga pag-download](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Estilo ng code: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Mga contributor ng GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Mga isyu sa GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Mga pull request sa GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![Tinatanggap ang PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Magsimula rito:** [Piliin ang iyong workflow](https://azure.github.io/co-op-translator/workflows/) | [Kumpigurasyon](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Multi-Language Support

#### Sinusuportahan ng [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](./README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

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
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Pangkalahatang-ideya

**Co-op Translator** tumutulong sa iyo na i-localize ang iyong pang-edukasyong GitHub na nilalaman sa maraming wika nang walang kahirap-hirap.
Kapag na-update mo ang iyong mga Markdown file, mga larawan, o mga notebook, ang mga pagsasalin ay awtomatikong nananatiling naka-synchronize, tinitiyak na ang iyong nilalaman ay nananatiling tama at napapanahon para sa mga nag-aaral sa buong mundo.

Gamitin ito mula sa CLI para sa pagsasalin ng repositoryo, mula sa Python API para sa automation, o sa pamamagitan ng MCP server para sa mga workflow ng agent at editor.

Example of how translated content is organized:

![Example](../../imgs/translation-ex.png)

## Bakit Co-op Translator?

Madaling isalin ang isang file. Ang pagpapanatili ng buong dokumentasyon ng repositoryong
isinalin, naka-link, at napapanahon ang mahirap na bahagi.

| Problem | How Co-op Translator helps |
| --- | --- |
| Long docs are not one prompt | Hindi sapat ang isang prompt para sa mahahabang Markdown; hinahati ang malalaking Markdown file sa mga bahagi, kaya ang isang mahabang README ay hindi nakadepende sa isang madaling masira na tugon mula sa modelo. Kung mabigo ang isang bahagi, maaaring subukan muli ng Co-op Translator at muling hatiin ang nabigong bahagi lamang. |
| Incomplete translations should not be marked current | Hindi dapat ituring na kasalukuyan ang isang pinutol na pagsasalin. Sinusuri ng Co-op Translator ang integridad ng pagsasalin bago mag-save at maaaring matukoy ang mga estrukturang hindi kumpletong umiiral na pagsasalin. |
| Links should match the translated repo structure | Madalas na iniiwan ng manu-manong mga pagsasalin ang mga relative link pabalik sa source tree. Isinusulat muli ng Co-op Translator ang mga link sa Markdown, notebook, imahe, at README upang tumugma sa `translations/<lang>/...` na istruktura. |
| Translation should work across an entire repo | Pinangangasiwaan ng Co-op Translator ang mga README file, docs, notebook, at teksto ng larawan bilang bahagi ng isang repository workflow, sa halip na isalin ang mga file isa-isa. |
| Maintaining translations matters more than creating them once | Pinapayagan ka ng mga source hash at metadata ng pagsasalin ng Co-op Translator na mahanap ang mga lipas na file, laktawan ang mga hindi nagbago, at panatilihing naka-synchronize ang isinaling nilalaman habang umuunlad ang source repo. |

## Paano pinamamahalaan ang estado ng pagsasalin

Pinamamahalaan ng Co-op Translator ang isinaling nilalaman bilang **mga versioned software artifact**,  
hindi bilang mga static na file.

Sinusubaybayan ng tool ang estado ng isinaling Markdown, mga larawan, at mga notebook
gamit ang **language-scoped metadata**.

Ang disenyo na ito ay nagpapahintulot sa Co-op Translator na:

- Maaasahang matukoy ang mga lipas na pagsasalin
- Tratuhin nang pare-pareho ang Markdown, mga larawan, at mga notebook
- Lumaki nang ligtas sa malalaking, mabilis na umuusad, multi-wika na mga repositoryo

Sa pamamagitan ng pagmomodelo ng mga pagsasalin bilang mga pinangangasiwaang artifact,
ang mga workflow ng pagsasalin ay natural na naka-align sa moderno
na mga gawi sa pamamahala ng dependency at artifact ng software.

→ [Paano pinamamahalaan ang estado ng pagsasalin](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Mga Kaugnay na Malalim na Artikulo

- [Pag-aayos ng Sirang Markdown sa AI Translation: Pagpapalakas ng Production Pipeline](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Magsimula

Maaaring gamitin ang Co-op Translator mula sa CLI, ang Python API, o ang MCP server. Magsimula sa gabay ng workflow kung pumipili ka sa pagitan ng lokal na pagsasalin, automation, CI, at integrasyon ng agent/editor.

- [Piliin ang iyong workflow](../../docs/workflows.md)
- [I-configure ang mga kredensyal](../../docs/configuration.md)
- [Isalin mula sa CLI](../../docs/cli.md)
- [I-automate gamit ang Python API](../../docs/api.md)
- [Ikonekta sa MCP Server](../../docs/mcp.md)
- [Patakbuhin sa GitHub Actions](../../docs/github-actions.md)

Minimal na halimbawa ng CLI pagkatapos ng konfigurasyon:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS o Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

For first runs on large repositories, use `--dry-run` before writing translated files. See the [Sanggunian ng CLI](../../docs/cli.md) for content type flags, logs, review, and link migration.

Container quick run with Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Container quick run with PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Mga Tampok

- Awtomatikong pagsasalin para sa Markdown, mga notebook, at mga larawan
- Pinananatiling naka-sync ang mga pagsasalin sa mga pagbabago sa source
- Gumagana nang lokal (CLI) o sa CI (GitHub Actions)
- Inilalantad ang mga tool sa pagsasalin ng Markdown, notebook, imahe, review, at proyekto sa pamamagitan ng MCP
- Gumagamit ng Azure OpenAI o OpenAI para sa provider-backed na pagsasalin
- Pinapayagan ang MCP na mag-host ng mga agent upang isalin ang mga chunk ng Markdown at notebook nang walang Co-op Translator LLM credentials
- Gumagamit ng Azure AI Vision para sa pagkuha at pagsasalin ng teksto sa larawan
- Nirerepaso ang estruktura at pagiging sariwa ng pagsasalin gamit ang deterministikong mga tsek
- Pinapanatili ang format at estruktura ng Markdown

## Dokumentasyon

- [Site ng Dokumentasyon](https://azure.github.io/co-op-translator/)
- [Piliin ang iyong workflow](../../docs/workflows.md)
- [Kumpigurasyon](../../docs/configuration.md)
- [Pagsasaayos ng Azure AI](../../docs/azure-ai-setup.md)
- [Sanggunian ng CLI](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Template ng README para sa mga wika](../../docs/readme-languages-template.md)
- [Mga sinusuportahang wika](../../docs/supported-languages.md)
- [Pag-aambag](../../CONTRIBUTING.md)
- [Pagtutuwid ng Problema](../../docs/troubleshooting.md)

### Gabay na partikular sa Microsoft
> [!NOTE]
> For maintainers of the Microsoft “For Beginners” repositories only.

- [Updating the “other courses” list (for MS Beginners repositories only)](../../docs/microsoft-beginners.md)

## Suportahan kami at pagyamanin ang pandaigdigang pagkatuto

Sumali sa amin sa pagbabago ng paraan ng pagbabahagi ng pang-edukasyong nilalaman sa buong mundo! Bigyan ang [Co-op Translator](https://github.com/azure/co-op-translator) ng ⭐ sa GitHub at suportahan ang aming misyon na gibaing ang mga hadlang sa wika sa pagkatuto at teknolohiya. Malaki ang epekto ng iyong interes at mga kontribusyon! Laging tinatanggap ang mga kontribusyon sa code at mga mungkahi sa tampok.

### Tuklasin ang nilalamang pang-edukasyon ng Microsoft sa iyong wika
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

## Presentasyon sa Video

👉 I-click ang larawan sa ibaba upang panoorin sa YouTube.

- **Open at Microsoft**: Isang maikling 18-minutong pagpapakilala at mabilis na gabay kung paano gamitin ang Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Pag-aambag

Malugod na tinatanggap ng proyektong ito ang mga ambag at mungkahi. Interesado kang mag-ambag sa Azure Co-op Translator? Mangyaring tingnan ang aming [CONTRIBUTING.md](../../CONTRIBUTING.md) para sa mga alituntunin kung paano ka makakatulong gawing mas accessible ang Co-op Translator.

## Mga Nag-ambag

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodigo ng Pag-uugali

Inampon ng proyektong ito ang [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Para sa karagdagang impormasyon tingnan ang [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o kontakin ang [opencode@microsoft.com](mailto:opencode@microsoft.com) kung may karagdagang mga tanong o komento.

## Responsable na AI

Ang Microsoft ay nakatuon sa pagtulong sa aming mga customer na gamitin ang aming mga produktong AI nang may pananagutan, pagbabahagi ng aming mga natutunan, at pagbuo ng mga pakikipagtulungan na nakabatay sa tiwala sa pamamagitan ng mga tool tulad ng Transparency Notes at Impact Assessments. Marami sa mga kabansang ito ay matatagpuan sa [https://aka.ms/RAI](https://aka.ms/RAI).
Ang pamamaraan ng Microsoft sa responsable na AI ay nakaugat sa aming mga prinsipyo ng AI ng pagiging patas, pagiging maaasahan at kaligtasan, privacy at seguridad, pagiging inklusibo, pagiging malinaw, at pananagutan.

Ang malakihang mga modelong natural na wika, imahe, at pagsasalita - tulad ng mga ginamit sa sample na ito - ay maaaring kumilos sa mga paraan na hindi patas, hindi maaasahan, o nakakasakit, na maaaring magdulot ng pinsala. Mangyaring sumangguni sa [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) upang maging alam sa mga panganib at limitasyon.

Ang inirerekomendang pamamaraan upang mabawasan ang mga panganib na ito ay isama ang isang safety system sa iyong arkitektura na maaaring makatuklas at maiwasan ang mapanganib na pag-uugali. Nagbibigay ang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ng isang independiyenteng layer ng proteksyon, na kayang matukoy ang mapanganib na nilikha ng gumagamit at nilikha ng AI na nilalaman sa mga aplikasyon at serbisyo. Kasama sa Azure AI Content Safety ang mga text at image API na nagpapahintulot sa iyo na matukoy ang materyal na nakasasama. Mayroon din kaming interactive na Content Safety Studio na nagpapahintulot sa iyo na tingnan, galugarin, at subukan ang sample code para sa pagtuklas ng mapanganib na nilalaman sa iba't ibang modality. Ang sumusunod na [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ay gagabay sa iyo sa paggawa ng mga request sa serbisyo.

Isa pang aspeto na dapat isaalang-alang ay ang pangkalahatang pagganap ng aplikasyon. Sa mga multi-modal at multi-model na aplikasyon, itinuturing namin ang pagganap bilang ang sistema ay gumaganap ayon sa iyong at ng iyong mga gumagamit na inaasahan, kabilang ang hindi pagbuo ng mapanganib na output. Mahalaga na suriin ang pagganap ng iyong pangkalahatang aplikasyon gamit ang [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Maaari mong suriin ang iyong AI application sa iyong development environment gamit ang [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Sa pamamagitan ng isang test dataset o isang target, ang mga generative AI na output ng iyong aplikasyon ay nasusukat nang kwantitatibo gamit ang mga built-in na evaluator o mga custom evaluator na iyong pipiliin. Upang makapagsimula gamit ang prompt flow sdk upang suriin ang iyong sistema, maaari mong sundan ang [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kapag pinatakbo mo ang isang evaluation run, maaari mong [visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Mga Trademark

Maaaring maglaman ang proyektong ito ng mga trademark o logo para sa mga proyekto, produkto, o serbisyo. Ang awtorisadong paggamit ng mga trademark o logo ng Microsoft ay nakasalalay at dapat sumunod sa [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Ang paggamit ng mga trademark o logo ng Microsoft sa mga binagong bersyon ng proyektong ito ay hindi dapat magdulot ng kalituhan o magpahiwatig ng pagsuporta ng Microsoft. Anumang paggamit ng mga trademark o logo ng third-party ay nakasalalay sa mga patakaran ng nasabing third-party.

## Pagkuha ng Tulong

Kung ikaw ay maipit o may mga tanong tungkol sa paggawa ng mga AI app, sumali sa:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kung mayroon kang puna sa produkto o mga error habang nagtatayo, bisitahin:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)