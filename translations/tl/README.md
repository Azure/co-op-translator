<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:42:12+00:00",
  "source_file": "README.md",
  "language_code": "tl"
}
-->
# Co-op Translator

_Madali mong ma-automate ang pagsasalin ng iyong educational GitHub content sa iba’t ibang wika para maabot ang mas maraming tao sa buong mundo._

### 🌐 Suporta sa Maraming Wika

#### Sinusuportahan ng [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](./README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Pangkalahatang-ideya

Pinapadali ng **Co-op Translator** ang pagsasalin ng iyong educational GitHub content sa iba’t ibang wika, kaya mas madali mong maabot ang mga tao sa buong mundo. Kapag nag-update ka ng iyong Markdown files, images, o Jupyter notebooks, awtomatikong nasisynchronize ang mga salin para siguradong laging bago at relevant ang iyong educational GitHub content para sa mga international na user.

Tingnan kung paano inaayos ng Co-op Translator ang mga isinaling educational GitHub content:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.tl.png)

## Mabilisang Simula

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

## Minimal na Setup

- Gumawa ng `.env` gamit ang template: [.env.template](../../.env.template)
- I-configure ang isang LLM provider (Azure OpenAI o OpenAI)
- Para sa pagsasalin ng larawan (`-img`), i-set din ang Azure AI Vision
- Rekomendado: Kung may mga salin ka na galing sa ibang tools, linisin muna ito para maiwasan ang conflict (halimbawa: `translations/`).
- Rekomendado: Magdagdag ng translations section sa iyong README gamit ang [README languages template](./README_languages_template.md)
- Tingnan: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

## Paggamit

Isalin lahat ng suportadong uri:

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

Iba pang flags: [Command reference](./getting_started/command-reference.md)

## Mga Tampok

- Awtomatikong pagsasalin para sa Markdown, notebook, at mga larawan
- Laging updated ang mga salin kapag may pagbabago sa source
- Pwedeng gamitin local (CLI) o sa CI (GitHub Actions)
- Gumagamit ng Azure OpenAI o OpenAI; optional ang Azure AI Vision para sa mga larawan
- Pinapanatili ang format at structure ng Markdown

## Dokumentasyon

- [Command-line guide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions guide (Public repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions guide (Microsoft organization repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Mga suportadong wika](./getting_started/supported-languages.md)
- [Troubleshooting](./getting_started/troubleshooting.md)

## Suportahan Kami at Palaganapin ang Global na Pagkatuto

Samahan kami sa pagbabago kung paano naibabahagi ang educational content sa buong mundo! Bigyan ng ⭐ ang [Co-op Translator](https://github.com/azure/co-op-translator) sa GitHub at suportahan ang aming misyon na alisin ang hadlang sa wika sa pagkatuto at teknolohiya. Malaki ang epekto ng iyong interes at ambag! Bukas kami sa code contributions at mga suhestiyon sa features.

### Tuklasin ang Microsoft educational content sa iyong wika

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

## Mga Video Presentasyon

Alamin pa ang tungkol sa Co-op Translator sa aming mga presentasyon _(I-click ang larawan sa ibaba para panoorin sa YouTube.)_:

- **Open at Microsoft**: Maikling 18-minutong introduction at mabilisang gabay kung paano gamitin ang Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.tl.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Pagsali at Pag-aambag

Bukas ang proyektong ito sa mga ambag at suhestiyon. Interesado ka bang tumulong sa Azure Co-op Translator? Tingnan ang aming [CONTRIBUTING.md](./CONTRIBUTING.md) para sa mga gabay kung paano mo mapapadali ang Co-op Translator para sa lahat.

## Mga Contributor

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Ang proyektong ito ay sumusunod sa [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Para sa karagdagang impormasyon, tingnan ang [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o
makipag-ugnayan sa [opencode@microsoft.com](mailto:opencode@microsoft.com) para sa iba pang tanong o komento.

## Responsible AI

Ang Microsoft ay nakatuon sa pagtulong sa mga customer na gamitin ang aming AI products nang responsable, pagbabahagi ng aming mga natutunan, at pagbuo ng tiwala sa pamamagitan ng mga tools tulad ng Transparency Notes at Impact Assessments. Marami sa mga resources na ito ay makikita sa [https://aka.ms/RAI](https://aka.ms/RAI).
Ang approach ng Microsoft sa responsible AI ay nakabase sa aming AI principles: fairness, reliability at safety, privacy at security, inclusiveness, transparency, at accountability.

Ang malalaking natural language, image, at speech models—gaya ng ginagamit sa sample na ito—ay maaaring magpakita ng hindi patas, hindi maaasahan, o nakakasakit na ugali, na maaaring magdulot ng pinsala. Mangyaring basahin ang [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para malaman ang mga panganib at limitasyon.

Ang rekomendadong paraan para mabawasan ang mga panganib na ito ay ang paglalagay ng safety system sa iyong architecture na kayang mag-detect at pigilan ang harmful behavior. Ang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ay nagbibigay ng independent na proteksyon, na kayang mag-detect ng harmful user-generated at AI-generated content sa mga application at serbisyo. Kasama sa Azure AI Content Safety ang text at image APIs para matukoy ang mga mapanganib na materyal. Mayroon din kaming interactive Content Safety Studio kung saan pwede mong makita, i-explore, at subukan ang sample code para sa pag-detect ng harmful content sa iba’t ibang modality. Ang [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ay gagabay sa iyo kung paano mag-request sa serbisyo.
Isa pang aspeto na dapat isaalang-alang ay ang kabuuang performance ng application. Sa mga multi-modal at multi-model na application, ang ibig sabihin ng performance ay gumagana ang sistema ayon sa inaasahan mo at ng mga user mo, kabilang na ang hindi pag-generate ng mapanirang output. Mahalaga na suriin ang performance ng iyong buong application gamit ang [generation quality at risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Pwede mong i-evaluate ang iyong AI application sa development environment gamit ang [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Kapag may test dataset o target, ang mga generation ng iyong generative AI application ay sinusukat nang quantitative gamit ang built-in evaluators o custom evaluators na gusto mo. Para makapagsimula sa prompt flow sdk para i-evaluate ang iyong system, sundan ang [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kapag natapos mo na ang evaluation run, pwede mong [i-visualize ang resulta sa Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Mga Trademark

Ang proyektong ito ay maaaring naglalaman ng mga trademark o logo para sa mga proyekto, produkto, o serbisyo. Ang awtorisadong paggamit ng mga trademark o logo ng Microsoft ay dapat sumunod sa [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Ang paggamit ng mga trademark o logo ng Microsoft sa binagong bersyon ng proyektong ito ay hindi dapat magdulot ng kalituhan o magpahiwatig ng sponsorship ng Microsoft. Ang anumang paggamit ng trademark o logo ng third-party ay sakop ng patakaran ng third-party na iyon.

## Paano Humingi ng Tulong

Kung nahirapan ka o may tanong tungkol sa paggawa ng AI apps, sumali sa:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Kung may feedback ka sa produkto o nakaranas ng error habang gumagawa, bisitahin ang:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi eksaktong salin. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.