<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:09:55+00:00",
  "source_file": "README.md",
  "language_code": "tr"
}
-->
# Co-op Translator

_Eğitsel GitHub içeriğinizi kolayca birden fazla dile otomatik olarak çevirin ve küresel bir kitleye ulaşın._

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

### 🌐 Çok Dilli Destek

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) tarafından desteklenen diller

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](./README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Genel Bakış

**Co-op Translator**, eğitsel GitHub içeriğinizi hızlıca birden fazla dile çevirmenizi sağlar ve küresel bir kitleye kolayca ulaşmanıza yardımcı olur. Markdown dosyalarınızı, görsellerinizi veya Jupyter defterlerinizi güncellediğinizde, çeviriler otomatik olarak senkronize edilir ve böylece eğitsel GitHub içeriğiniz uluslararası kullanıcılar için güncel ve alakalı kalır.

Co-op Translator'ın çevrilmiş eğitsel GitHub içeriğini nasıl organize ettiğini inceleyin:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.tr.png)

## Hızlı Başlangıç

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

## Minimum Kurulum

- [.env.template](../../.env.template) şablonunu kullanarak bir `.env` dosyası oluşturun
- Bir LLM sağlayıcısı yapılandırın (Azure OpenAI veya OpenAI)
- Görsel çevirisi için (`-img`), ayrıca Azure AI Vision ayarlayın
- Tavsiye: Başka araçlarla oluşturulmuş çevirileriniz varsa, çakışmaları önlemek için önce bunları temizleyin (örneğin: `translations/`).
- Tavsiye: README dosyanıza [README diller şablonunu](./README_languages_template.md) kullanarak bir çeviri bölümü ekleyin
- Bakınız: [Azure AI Kurulumu](./getting_started/set-up-azure-ai.md)

## Kullanım

Tüm desteklenen türleri çevirin:

```bash
translate -l "ko ja"
```

Sadece Markdown:

```bash
translate -l "de" -md
```

Markdown + görseller:

```bash
translate -l "pt" -md -img
```

Sadece defterler:

```bash
translate -l "zh" -nb
```

Daha fazla bayrak: [Komut referansı](./getting_started/command-reference.md)

## Özellikler

- Markdown, defterler ve görseller için otomatik çeviri
- Çevirileri kaynak değişiklikleriyle senkronize tutar
- Yerel olarak (CLI) veya CI'da (GitHub Actions) çalışır
- Azure OpenAI veya OpenAI kullanır; görseller için isteğe bağlı Azure AI Vision
- Markdown biçimlendirmesini ve yapısını korur

## Belgeler

- [Komut satırı rehberi](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions rehberi (Genel depolar & standart gizli anahtarlar)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions rehberi (Microsoft organizasyon depoları & organizasyon düzeyi kurulumlar)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Desteklenen diller](./getting_started/supported-languages.md)
- [Sorun giderme](./getting_started/troubleshooting.md)

## Bizi Destekleyin ve Küresel Öğrenimi Teşvik Edin

Eğitsel içeriğin küresel olarak paylaşılma şeklini birlikte değiştirelim! [Co-op Translator](https://github.com/azure/co-op-translator) projesine GitHub'da ⭐ vererek öğrenme ve teknolojideki dil engellerini kaldırma misyonumuzu destekleyin. İlginiz ve katkılarınız büyük fark yaratıyor! Kod katkıları ve özellik önerileri her zaman memnuniyetle karşılanır.

### Microsoft'un eğitsel içeriklerini kendi dilinizde keşfedin

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

## Video Sunumlar

Co-op Translator hakkında daha fazla bilgi edinin _(Aşağıdaki görsele tıklayarak YouTube'da izleyebilirsiniz.)_:

- **Open at Microsoft**: Co-op Translator'ın nasıl kullanılacağına dair 18 dakikalık kısa bir tanıtım ve hızlı rehber.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.tr.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Katkıda Bulunma

Bu proje katkı ve önerilere açıktır. Azure Co-op Translator'a katkıda bulunmak ister misiniz? [CONTRIBUTING.md](./CONTRIBUTING.md) dosyamıza göz atarak Co-op Translator'ı daha erişilebilir hale getirmek için nasıl yardımcı olabileceğinizi öğrenebilirsiniz.

## Katkıda Bulunanlar

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Davranış Kuralları

Bu proje [Microsoft Açık Kaynak Davranış Kuralları'nı](https://opensource.microsoft.com/codeofconduct/) benimsemiştir.
Daha fazla bilgi için [Davranış Kuralları SSS](https://opensource.microsoft.com/codeofconduct/faq/) sayfasına bakabilir veya
ek sorularınız ve yorumlarınız için [opencode@microsoft.com](mailto:opencode@microsoft.com) adresine ulaşabilirsiniz.

## Sorumlu Yapay Zeka

Microsoft, müşterilerimizin yapay zeka ürünlerimizi sorumlu bir şekilde kullanmalarına yardımcı olmaya, öğrendiklerimizi paylaşmaya ve Şeffaflık Notları ve Etki Değerlendirmeleri gibi araçlarla güvene dayalı ortaklıklar kurmaya kararlıdır. Bu kaynakların birçoğuna [https://aka.ms/RAI](https://aka.ms/RAI) adresinden ulaşabilirsiniz.
Microsoft'un sorumlu yapay zeka yaklaşımı; adalet, güvenilirlik ve güvenlik, gizlilik ve güvenlik, kapsayıcılık, şeffaflık ve hesap verebilirlik ilkelerine dayanmaktadır.

Bu örnekte kullanılanlar gibi büyük ölçekli doğal dil, görsel ve konuşma modelleri; adil olmayan, güvenilmez veya saldırgan davranışlar sergileyebilir ve bu da zararlara yol açabilir. Riskler ve sınırlamalar hakkında bilgi sahibi olmak için lütfen [Azure OpenAI hizmeti Şeffaflık Notu'na](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) başvurun.

Bu riskleri azaltmak için önerilen yaklaşım, mimarinizde zararlı davranışları tespit edip önleyebilecek bir güvenlik sistemi bulundurmaktır. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview), uygulama ve hizmetlerde kullanıcı veya yapay zeka tarafından üretilen zararlı içerikleri tespit edebilen bağımsız bir koruma katmanı sunar. Azure AI Content Safety, zararlı materyalleri tespit etmenizi sağlayan metin ve görsel API'leri içerir. Ayrıca, farklı modlarda zararlı içerik tespiti için örnek kodları görebileceğiniz, keşfedebileceğiniz ve deneyebileceğiniz etkileşimli bir Content Safety Studio'ya da sahibiz. Aşağıdaki [hızlı başlangıç dokümantasyonu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) hizmete istek göndermeyi adım adım anlatır.
Dikkate alınması gereken bir diğer konu ise genel uygulama performansıdır. Çok modlu ve çok modellerli uygulamalarda, performanstan kastımız sistemin sizin ve kullanıcılarınızın beklentilerini karşılaması, zararlı çıktılar üretmemesi de dahil olmak üzere, beklenen şekilde çalışmasıdır. Uygulamanızın genel performansını [üretim kalitesi ile risk ve güvenlik metrikleri](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) kullanarak değerlendirmeniz önemlidir.

Yapay zeka uygulamanızı geliştirme ortamınızda [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ile değerlendirebilirsiniz. Bir test veri seti veya hedef verildiğinde, üretici yapay zeka uygulamanızın çıktıları, yerleşik değerlendiriciler veya sizin seçeceğiniz özel değerlendiriciler ile nicel olarak ölçülür. Sisteminizi değerlendirmek için prompt flow sdk ile başlamak isterseniz, [hızlı başlangıç rehberini](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) takip edebilirsiniz. Bir değerlendirme çalıştırması yaptıktan sonra, [sonuçları Azure AI Studio'da görselleştirebilirsiniz](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ticari Markalar

Bu projede projelere, ürünlere veya hizmetlere ait ticari markalar veya logolar bulunabilir. Microsoft ticari markalarının veya logolarının yetkili kullanımı, [Microsoft'un Ticari Marka ve Marka Yönergeleri](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) ile uyumlu olmalı ve bu yönergeleri takip etmelidir. Bu projenin değiştirilmiş sürümlerinde Microsoft ticari markalarının veya logolarının kullanımı, karışıklığa yol açmamalı veya Microsoft'un sponsorluğunu ima etmemelidir. Üçüncü taraf ticari markalarının veya logolarının kullanımı ise ilgili üçüncü tarafın politikalarına tabidir.

## Yardım Alma

Takılırsanız veya yapay zeka uygulamaları geliştirme hakkında sorularınız olursa, katılın:

< a href="https://aka.ms/foundry/discord" title="Azure AI Foundry Discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

Ürünle ilgili geri bildiriminiz veya geliştirme sırasında hatalarınız varsa, ziyaret edin:

< a href="https://aka.ms/foundry/forum" title="Azure AI Foundry Developer Forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar olabileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.