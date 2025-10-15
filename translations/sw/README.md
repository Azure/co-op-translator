<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:44:55+00:00",
  "source_file": "README.md",
  "language_code": "sw"
}
-->
# Co-op Translator

_Rahisisha mchakato wa kutafsiri maudhui yako ya elimu kwenye GitHub kwa lugha nyingi ili kufikia hadhira ya kimataifa._

### 🌐 Msaada wa Lugha Nyingi

#### Inasaidiwa na [Co-op Translator](https://github.com/Azure/Co-op-Translator)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](./README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

## Muhtasari

**Co-op Translator** inakuwezesha kutafsiri maudhui yako ya elimu kwenye GitHub kwa haraka kwenda kwenye lugha nyingi, hivyo kufikia hadhira ya dunia bila usumbufu. Unapobadilisha faili zako za Markdown, picha, au daftari za Jupyter, tafsiri zinasasishwa moja kwa moja ili kuhakikisha maudhui yako ya elimu yanabaki kuwa ya kisasa na yanayofaa kwa watumiaji wa kimataifa.

Angalia jinsi Co-op Translator inavyopanga maudhui yaliyotafsiriwa kwenye GitHub:

![Mfano](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.sw.png)

## Jinsi ya kuanza haraka

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

## Mpangilio wa msingi

- Tengeneza `.env` kwa kutumia kigezo: [.env.template](../../.env.template)
- Sanidi mtoa huduma mmoja wa LLM (Azure OpenAI au OpenAI)
- Kwa tafsiri ya picha (`-img`), weka pia Azure AI Vision
- Inashauriwa: Ikiwa una tafsiri zilizotengenezwa na zana nyingine, safisha kwanza ili kuepuka mgongano (kwa mfano: `translations/`).
- Inashauriwa: Ongeza sehemu ya tafsiri kwenye README yako ukitumia [README languages template](./README_languages_template.md)
- Angalia: [Sanidi Azure AI](./getting_started/set-up-azure-ai.md)

## Matumizi

Tafsiri aina zote zinazosaidiwa:

```bash
translate -l "ko ja"
```

Markdown pekee:

```bash
translate -l "de" -md
```

Markdown + picha:

```bash
translate -l "pt" -md -img
```

Daftari pekee:

```bash
translate -l "zh" -nb
```

Bendera zaidi: [Marejeleo ya amri](./getting_started/command-reference.md)

## Vipengele

- Tafsiri ya kiotomatiki kwa Markdown, daftari, na picha
- Inahakikisha tafsiri zinasasishwa na mabadiliko ya chanzo
- Inafanya kazi kwenye kompyuta (CLI) au kwenye CI (GitHub Actions)
- Inatumia Azure OpenAI au OpenAI; Azure AI Vision kwa picha ni hiari
- Inahifadhi muundo na mpangilio wa Markdown

## Nyaraka

- [Mwongozo wa mstari wa amri](./getting_started/command-line-guide/command-line-guide.md)
- [Mwongozo wa GitHub Actions (Repo za umma & siri za kawaida)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Mwongozo wa GitHub Actions (Repo za shirika la Microsoft & mipangilio ya ngazi ya shirika)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Lugha zinazosaidiwa](./getting_started/supported-languages.md)
- [Kutatua matatizo](./getting_started/troubleshooting.md)

## Tuunge mkono na Kuendeleza Kujifunza Duniani

Jiunge nasi kubadilisha jinsi maudhui ya elimu yanavyoshirikishwa duniani! Toa ⭐ kwa [Co-op Translator](https://github.com/azure/co-op-translator) kwenye GitHub na saidia dhamira yetu ya kuondoa vikwazo vya lugha katika kujifunza na teknolojia. Mchango wako na ushiriki wako vina maana kubwa! Mchango wa msimbo na mapendekezo ya vipengele yanakaribishwa kila wakati.

### Gundua maudhui ya elimu ya Microsoft kwa lugha yako

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

## Uwasilishaji wa Video

Jifunze zaidi kuhusu Co-op Translator kupitia uwasilishaji wetu _(Bonyeza picha hapa chini kutazama kwenye YouTube.)_:

- **Open at Microsoft**: Utangulizi mfupi wa dakika 18 na mwongozo wa haraka jinsi ya kutumia Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.sw.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Kuchangia

Mradi huu unakaribisha michango na mapendekezo. Unapenda kuchangia kwenye Azure Co-op Translator? Tafadhali angalia [CONTRIBUTING.md](./CONTRIBUTING.md) kwa mwongozo wa jinsi unavyoweza kusaidia kufanya Co-op Translator iweze kufikiwa na wengi.

## Wachangiaji

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kanuni za Maadili

Mradi huu umechukua [Kanuni za Maadili za Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).
Kwa maelezo zaidi angalia [Maswali ya Kanuni za Maadili](https://opensource.microsoft.com/codeofconduct/faq/) au
wasiliana na [opencode@microsoft.com](mailto:opencode@microsoft.com) kwa maswali au maoni zaidi.

## AI yenye Uwajibikaji

Microsoft imejikita kusaidia wateja wetu kutumia bidhaa zetu za AI kwa uwajibikaji, kushiriki tunachojifunza, na kujenga ushirikiano wa kuaminiana kupitia zana kama Transparency Notes na Impact Assessments. Rasilimali nyingi zinapatikana kwenye [https://aka.ms/RAI](https://aka.ms/RAI).
Mbinu ya Microsoft kuhusu AI yenye uwajibikaji inategemea kanuni zetu za AI: usawa, kutegemewa na usalama, faragha na usalama, ujumuishaji, uwazi, na uwajibikaji.

Mifano mikubwa ya lugha asilia, picha, na sauti - kama ile inayotumika kwenye sampuli hii - inaweza kufanya mambo yasiyo ya haki, yasiyoaminika, au ya kukera, na hivyo kusababisha madhara. Tafadhali soma [Ujumbe wa uwazi wa huduma ya Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ili ujue hatari na mipaka.

Njia inayopendekezwa ya kupunguza hatari hizi ni kujumuisha mfumo wa usalama kwenye usanifu wako ambao unaweza kugundua na kuzuia tabia hatarishi. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) inatoa safu huru ya ulinzi, inayoweza kugundua maudhui hatarishi yaliyotengenezwa na mtumiaji au AI kwenye programu na huduma. Azure AI Content Safety ina API za maandishi na picha zinazokuwezesha kugundua maudhui hatarishi. Pia kuna Content Safety Studio ya kujaribu na kuona mifano ya msimbo wa kugundua maudhui hatarishi kwenye njia tofauti. [Nyaraka za kuanza haraka](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) zinakuongoza jinsi ya kutuma maombi kwenye huduma.
Jambo lingine la kuzingatia ni utendaji wa jumla wa programu. Kwa programu zinazotumia miundo na njia nyingi, utendaji unamaanisha kuwa mfumo unafanya kazi kama wewe na watumiaji wako mnavyotarajia, ikiwemo kutozalisha matokeo hatarishi. Ni muhimu kutathmini utendaji wa programu yako kwa kutumia [viwango vya ubora wa kizazi na vipimo vya hatari na usalama](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Unaweza kutathmini programu yako ya AI katika mazingira ya maendeleo kwa kutumia [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Ukiwa na seti ya data ya majaribio au lengo, matokeo ya programu yako ya AI yanapimwa kwa njia ya namba kwa kutumia vipimaji vilivyojengwa ndani au vile vya chaguo lako. Ili kuanza kutumia prompt flow sdk kutathmini mfumo wako, unaweza kufuata [mwongozo wa haraka](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Baada ya kufanya tathmini, unaweza [kuona matokeo kwenye Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Alama za Biashara

Mradi huu unaweza kuwa na alama za biashara au nembo za miradi, bidhaa, au huduma. Matumizi yaliyoidhinishwa ya alama za biashara au nembo za Microsoft yanapaswa kufuata
[Mwongozo wa Alama za Biashara na Bidhaa wa Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Matumizi ya alama za biashara au nembo za Microsoft kwenye matoleo yaliyobadilishwa ya mradi huu hayapaswi kusababisha mkanganyiko au kuashiria udhamini wa Microsoft.
Matumizi yoyote ya alama za biashara au nembo za wahusika wengine yanategemea sera za wahusika hao.

## Kupata Msaada

Ukikwama au una maswali kuhusu kutengeneza programu za AI, jiunge na:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Kama una maoni kuhusu bidhaa au unakutana na makosa wakati wa kutengeneza, tembelea:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Kanusho**:
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya mtafsiri wa kibinadamu mwenye ujuzi. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.