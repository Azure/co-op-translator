<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T11:55:58+00:00",
  "source_file": "README.md",
  "language_code": "tl"
}
-->
# Co-op Translator

_Madaling i-automate ang pagsasalin ng iyong pang-edukasyong nilalaman sa GitHub sa iba't ibang wika upang maabot ang pandaigdigang madla._

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

### 🌐 Suporta sa Maramihang Wika

#### Sinusuportahan ng [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](./README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Pangkalahatang-ideya

**Co-op Translator** ay tumutulong sa iyo na i-localize ang iyong pang-edukasyong nilalaman sa GitHub sa maraming wika nang madali.
Kapag in-update mo ang iyong mga Markdown file, mga larawan, o mga notebook, awtomatikong naka-synchronize ang mga pagsasalin, na tinitiyak na ang iyong nilalaman ay nananatiling tama at napapanahon para sa mga mag-aaral sa buong mundo.

Halimbawa kung paano nakaayos ang isinaling nilalaman:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.tl.png)

## Mabilis na pagsisimula

```bash
# Gumawa at i-activate ang isang virtual na kapaligiran (inirerekomenda)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# I-install ang package
pip install co-op-translator
# Isalin
translate -l "ko ja fr" -md
```

Docker:

```bash
# Kunin ang pampublikong imahe mula sa GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Patakbuhin na may kasalukuyang folder na naka-mount at .env na ibinigay (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Pinakamababang setup

1. Gumawa ng `.env` file gamit ang template: [.env.template](../../.env.template)
2. I-configure ang isang LLM provider (Azure OpenAI o OpenAI)
3. (Opsyonal) Para sa pagsasalin ng larawan (`-img`), i-configure ang Azure AI Vision
4. (Inirerekomenda) Linisin ang anumang dating mga pagsasalin upang maiwasan ang mga salungatan (hal., `translations/`)
5. (Inirerekomenda) Magdagdag ng seksyon ng pagsasalin sa iyong README gamit ang [README languages template](./getting_started/README_languages_template.md)
6. Tingnan: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

## Paggamit

Isalin ang lahat ng suportadong uri:

```bash
translate -l "ko ja"
```

Markdown lang:

```bash
translate -l "de" -md
```

Markdown + mga larawan:

```bash
translate -l "pt" -md -img
```

Notebook lang:

```bash
translate -l "zh" -nb
```

Iba pang mga flag: [Command reference](./getting_started/command-reference.md)

## Mga Tampok

- Awtomatikong pagsasalin para sa Markdown, mga notebook, at mga larawan
- Pinananatiling naka-sync ang mga pagsasalin sa mga pagbabago sa pinagmulan
- Gumagana nang lokal (CLI) o sa CI (GitHub Actions)
- Gumagamit ng Azure OpenAI o OpenAI; opsyonal ang Azure AI Vision para sa mga larawan
- Pinapanatili ang format at istruktura ng Markdown

## Dokumentasyon

- [Gabay sa command-line](./getting_started/command-line-guide/command-line-guide.md)
- [Gabay sa GitHub Actions (Pampublikong mga repositoryo at karaniwang mga sikreto)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Gabay sa GitHub Actions (Microsoft organization repositories at org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Mga suportadong wika](./getting_started/supported-languages.md)
- [Pagsusumite ng kontribusyon](./CONTRIBUTING.md)
- [Pag-aayos ng problema](./getting_started/troubleshooting.md)

### Gabay na partikular sa Microsoft
> [!NOTE]
> Para lamang sa mga tagapangasiwa ng Microsoft “For Beginners” repositories.

- [Pag-update ng listahan ng “other courses” (para lamang sa MS Beginners repositories)](./getting_started/update-other-courses.md)

## Suportahan kami at paunlarin ang pandaigdigang pagkatuto

Sama-sama nating baguhin kung paano ibinabahagi ang pang-edukasyong nilalaman sa buong mundo! Bigyan ng ⭐ ang [Co-op Translator](https://github.com/azure/co-op-translator) sa GitHub at suportahan ang aming misyon na alisin ang mga hadlang sa wika sa pag-aaral at teknolohiya. Malaki ang epekto ng iyong interes at mga kontribusyon! Palaging malugod ang mga code contributions at mungkahi para sa mga tampok.

### Tuklasin ang pang-edukasyong nilalaman ng Microsoft sa iyong wika

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

## Mga presentasyong video

👉 I-click ang larawan sa ibaba upang panoorin sa YouTube.

- **Open at Microsoft**: Isang maikling 18-minutong pagpapakilala at mabilis na gabay kung paano gamitin ang Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.tl.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Pagsusumite ng kontribusyon

Malugod na tinatanggap ng proyektong ito ang mga kontribusyon at mungkahi. Interesado kang tumulong sa Azure Co-op Translator? Pakitingnan ang aming [CONTRIBUTING.md](./CONTRIBUTING.md) para sa mga patnubay kung paano mo mapapabuti ang accessibility ng Co-op Translator.

## Mga Kontribyutor

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Inampon ng proyektong ito ang [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Para sa karagdagang impormasyon, tingnan ang [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o
makipag-ugnayan sa [opencode@microsoft.com](mailto:opencode@microsoft.com) para sa anumang karagdagang tanong o komento.

## Responsible AI

Nangangako ang Microsoft na tulungan ang aming mga customer na gamitin nang responsable ang aming mga AI na produkto, ibahagi ang aming mga natutunan, at bumuo ng mga partnership na nakabase sa tiwala sa pamamagitan ng mga kasangkapang tulad ng Transparency Notes at Impact Assessments. Marami sa mga ito ay matatagpuan sa [https://aka.ms/RAI](https://aka.ms/RAI).
Ang pamamaraan ng Microsoft sa responsible AI ay nakabatay sa aming mga prinsipyo ng AI na katarungan, pagiging maaasahan at kaligtasan, privacy at seguridad, pagiging inklusibo, transparency, at pananagutan.

Ang mga malalaking modelo sa natural na wika, larawan, at pagsasalita - tulad ng mga ginamit sa sample na ito - ay maaaring kumilos sa mga paraan na hindi patas, hindi maaasahan, o nakakasakit, na maaaring magdulot ng pinsala. Mangyaring sumangguni sa [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) upang maging maalam tungkol sa mga panganib at limitasyon.
Ang inirerekomendang paraan upang mabawasan ang mga panganib na ito ay ang pagsama ng isang safety system sa iyong arkitektura na kayang tuklasin at pigilan ang mapanganib na pag-uugali. Nagbibigay ang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ng isang independiyenteng layer ng proteksyon, na kayang tuklasin ang mapanganib na nilalaman na ginawa ng mga user at AI sa mga aplikasyon at serbisyo. Kasama sa Azure AI Content Safety ang mga text at image API na nagpapahintulot sa iyo na matukoy ang mga materyal na mapanganib. Mayroon din kaming interactive Content Safety Studio na nagpapahintulot sa iyo na makita, tuklasin, at subukan ang sample code para sa pagtuklas ng mapanganib na nilalaman sa iba't ibang modality. Ang sumusunod na [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ay gagabay sa iyo sa paggawa ng mga request sa serbisyo.

Isa pang aspeto na dapat isaalang-alang ay ang pangkalahatang performance ng aplikasyon. Sa mga multi-modal at multi-model na aplikasyon, ang performance ay nangangahulugang gumagana ang sistema ayon sa inaasahan mo at ng iyong mga user, kabilang ang hindi paglikha ng mapanganib na output. Mahalaga na suriin ang performance ng iyong pangkalahatang aplikasyon gamit ang [generation quality at risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Maaari mong suriin ang iyong AI application sa iyong development environment gamit ang [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Sa pamamagitan ng isang test dataset o target, ang mga generative AI application generations mo ay sinusukat nang kwantitatibo gamit ang built-in evaluators o custom evaluators na iyong pinili. Upang makapagsimula gamit ang prompt flow sdk para suriin ang iyong sistema, maaari mong sundan ang [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kapag naisagawa mo na ang evaluation run, maaari mong [ipakita ang mga resulta sa Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Mga Trademark

Maaaring naglalaman ang proyektong ito ng mga trademark o logo para sa mga proyekto, produkto, o serbisyo. Ang awtorisadong paggamit ng mga trademark o logo ng Microsoft ay napapailalim at dapat sumunod sa [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Ang paggamit ng mga trademark o logo ng Microsoft sa mga binagong bersyon ng proyektong ito ay hindi dapat magdulot ng kalituhan o magpahiwatig ng sponsorship ng Microsoft. Anumang paggamit ng mga trademark o logo ng third-party ay napapailalim sa mga patakaran ng mga third-party na iyon.

## Pagkuha ng Tulong

Kung ikaw ay nahihirapan o may mga tanong tungkol sa paggawa ng AI apps, sumali sa:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kung mayroon kang feedback sa produkto o mga error habang nagde-develop, bisitahin ang:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->