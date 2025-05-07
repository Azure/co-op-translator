<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "18318279bb851dc2c709bfc6a26f6e1d",
  "translation_date": "2025-05-07T14:11:41+00:00",
  "source_file": "README.md",
  "language_code": "tr"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: Eğitim Dokümantasyonunun Çevirisini Kolayca Otomatikleştirin

_Dokümantasyonunuzu birden fazla dile kolayca otomatik çevirerek küresel bir kitleye ulaşın._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Co-op Translator ile Sağlanan Dil Desteği

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](./README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
>
> **Güçlü Otomasyon**: Artık GitHub Actions desteğiyle! Depo değişiklikleri yapıldığında belgelerinizi otomatik olarak çevirin ve her şeyi zahmetsizce güncel tutun. [Daha fazla bilgi](../..).

## Desteklenen Modeller ve Servisler

| Tür                    | İsim                           |
|------------------------|--------------------------------|
| Dil Modeli             | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Bilgisayarlı Görü      | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> Eğer bilgisayarlı görü servisi kullanılamıyorsa, co-op translator [Markdown-only mode](./getting_started/markdown-only-mode.md) moduna geçer.

## Genel Bakış: Eğitim İçeriği Çevirinizi Kolaylaştırın

Dil engelleri, dünya çapında öğrenenlerin ve geliştiricilerin değerli eğitim kaynaklarına ve teknik bilgilere erişimini önemli ölçüde kısıtlar. Bu durum katılımı sınırlar ve küresel yenilik ile öğrenme hızını yavaşlatır.

**Co-op Translator**, Microsoft’un kendi büyük ölçekli eğitim serileri (örneğin "Yeni Başlayanlar İçin" rehberleri) için manuel çeviri sürecinin verimsizliğini gidermek amacıyla ortaya çıktı. Herkes için bu engelleri kaldıracak, kullanımı kolay ve güçlü bir araç haline geldi. CLI ve GitHub Actions üzerinden yüksek kaliteli otomatik çeviriler sunarak, Co-op Translator dünya genelindeki eğitimcilerin, öğrencilerin, araştırmacıların ve geliştiricilerin bilgi paylaşmasını ve dil engelleri olmadan erişim sağlamasını mümkün kılar.

Co-op Translator’ın çevrilmiş eğitim içeriğini nasıl düzenlediğine göz atın:

![Örnek](../../imgs/translation-ex.png)

Markdown dosyaları ve resim içi metinler otomatik olarak çevrilir ve dil bazlı klasörlerde düzenli şekilde saklanır.

**Eğitim içeriğinize Co-op Translator ile bugün küresel erişim sağlayın!**

## Microsoft’un Öğrenme Kaynakları İçin Küresel Erişimi Desteklemek

Co-op Translator, küresel geliştirici topluluğuna hizmet veren önemli Microsoft eğitim girişimleri için dil bariyerlerini aşmaya yardımcı olur ve depo çeviri süreçlerini otomatikleştirir. Şu anda Co-op Translator kullanan örnekler şunlardır:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## Temel Özellikler

- **Otomatik Çeviriler**: Metni birçok dile zahmetsizce çevirin.
- **GitHub Actions Entegrasyonu**: Çevirileri CI/CD sürecinizin parçası olarak otomatikleştirin.
- **Markdown Koruma**: Çeviri sırasında doğru Markdown sözdizimini koruyun.
- **Resim Metni Çevirisi**: Resim içindeki metni çıkarıp çevirin.
- **Gelişmiş LLM Teknolojisi**: Yüksek kaliteli çeviriler için son teknoloji dil modellerini kullanın.
- **Kolay Entegrasyon**: Mevcut proje yapınıza sorunsuzca entegre edin.
- **Yerelleştirmeyi Basitleştirin**: Projenizin uluslararası pazarlara uyarlanma sürecini hızlandırın.

## Nasıl Çalışır

![Mimari](../../imgs/architecture_241019.png)

Co-op Translator, proje klasörünüzdeki Markdown dosyaları ve resimleri alır ve şu şekilde işler:

1. **Metin Çıkarma**: Markdown dosyalarından ve yapılandırılmışsa (örneğin Azure Computer Vision ile) resim içindeki gömülü metinden metni çıkarır.
1. **AI Çevirisi**: Çıkarılan metni yapılandırılmış LLM’ye (Azure OpenAI, OpenAI vb.) gönderir ve çevirisini alır.
1. **Sonuç Kaydetme**: Çevrilmiş Markdown dosyalarını ve metni çevrilmiş resimleri, orijinal biçimlendirmeyi koruyarak dil bazlı klasörlere kaydeder.

## Başlarken

> [!NOTE]
> Bu eğitimde Azure kaynakları odaklanılmıştır, ancak [desteklenen modeller ve servisler](../..) listesindeki herhangi bir dil modeli kullanılabilir.

CLI ile hızlıca başlayın veya GitHub Actions ile tam otomasyon kurun.

### İlk Kurulum

- [Azure AI Kurulumu](./getting_started/set-up-azure-ai.md)

### Hızlı Başlangıç: Komut Satırı

Komut satırı kullanarak hızlıca başlamak için:

1. Paketi yükleyin:
    ```bash
    pip install co-op-translator
    ```
2. Kimlik Bilgilerini Yapılandırın:
  - `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` bayrağı oluşturun:
    ```bash
    translate -l "ko ja fr"
    ```
    *(Deponuzdaki `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) dosyasını değiştirin. Yerel kurulum gerekmez.
- Rehberler:
  - [GitHub Actions Rehberi (Açık Depolar ve Standart Gizli Anahtarlar)](./getting_started/github-actions-guide/github-actions-guide-public.md) - Standart depo gizli anahtarlarına dayanan çoğu açık veya kişisel depo için kullanın.
  - [GitHub Actions Rehberi (Microsoft Organizasyon Depoları ve Organizasyon Düzeyi Kurulumlar)](./getting_started/github-actions-guide/github-actions-guide-org.md) - Microsoft GitHub organizasyonunda çalışıyorsanız veya organizasyon düzeyi gizli anahtarlar ya da koşucular kullanmanız gerekiyorsa bu rehberi kullanın.

### Sorun Giderme ve İpuçları

- [Sorun Giderme Rehberi](./getting_started/troubleshooting.md)

### Ek Kaynaklar

- [Komut Referansı](./getting_started/command-reference.md): Tüm komutlar ve seçenekler için ayrıntılı rehber.
- [Çok Dilli Destek Kurulumu](./getting_started/multi-language-support.md): README dosyanıza çevrilmiş sürümlere bağlantı tablosu ekleme.
- [Desteklenen Diller](./getting_started/supported-languages.md): Desteklenen diller listesi ve yeni dil ekleme talimatları.
- [Sadece Markdown Modu](./getting_started/markdown-only-mode.md): Sadece metin çevirisi yapma, resim çevirisi olmadan.

## Video Sunumlar

Co-op Translator hakkında daha fazla bilgi edinin _(Aşağıdaki görsele tıklayarak YouTube’da izleyin.)_:

- **Open at Microsoft**: Co-op Translator’ı kullanmaya hızlı bir giriş ve 18 dakikalık kısa tanıtım.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: Co-op Translator’ın ne olduğu, kurulumu, kullanımı ve canlı demo dahil detaylı 1 saatlik adım adım rehber.

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Bize Destek Olun ve Küresel Öğrenmeyi Teşvik Edin

Eğitim içeriğinin dünya çapında paylaşım şeklini değiştirmemize katılın! [Co-op Translator](https://github.com/azure/co-op-translator)’a GitHub’da ⭐ verin ve öğrenme ile teknolojide dil engellerini kaldırma misyonumuzu destekleyin. İlginiz ve katkılarınız büyük fark yaratır! Kod katkıları ve özellik önerileri her zaman memnuniyetle karşılanır.

## Katkıda Bulunma

Bu proje katkı ve önerilere açıktır. Azure Co-op Translator’a katkıda bulunmak ister misiniz? Katkı yapma rehberimiz için lütfen [CONTRIBUTING.md](./CONTRIBUTING.md) dosyasına bakın.

## Katılımcılar

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Davranış Kuralları

Bu proje [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/)’nu benimsemiştir. Daha fazla bilgi için [Davranış Kuralları SSS](https://opensource.microsoft.com/codeofconduct/faq/) sayfasına bakabilir veya ek sorularınız için [opencode@microsoft.com](mailto:opencode@microsoft.com) adresiyle iletişime geçebilirsiniz.

## Sorumlu Yapay Zeka

Microsoft, müşterilerimizin yapay zeka ürünlerimizi sorumlu şekilde kullanmalarına yardımcı olmaya, deneyimlerimizi paylaşmaya ve Transparency Notes ve Etki Değerlendirmeleri gibi araçlarla güvene dayalı ortaklıklar kurmaya kararlıdır. Bu kaynakların çoğuna [https://aka.ms/RAI](https://aka.ms/RAI) adresinden ulaşabilirsiniz.  
Microsoft’un sorumlu yapay zeka yaklaşımı, adalet, güvenilirlik ve güvenlik, gizlilik ve emniyet, kapsayıcılık, şeffaflık ve hesap verebilirlik gibi yapay zeka ilkelerimize dayanmaktadır.
Büyük ölçekli doğal dil, görüntü ve konuşma modelleri - bu örnekte kullanılanlar gibi - haksız, güvenilmez veya saldırgan davranışlar sergileyebilir ve bu da zararlar doğurabilir. Riskler ve sınırlamalar hakkında bilgi edinmek için lütfen [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) sayfasını inceleyin.

Bu riskleri azaltmak için önerilen yaklaşım, mimarinizde zararlı davranışları tespit edip önleyebilen bir güvenlik sistemi bulundurmaktır. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview), uygulamalarda ve hizmetlerde kullanıcı ve yapay zeka tarafından oluşturulan zararlı içerikleri tespit edebilen bağımsız bir koruma katmanı sağlar. Azure AI Content Safety, zararlı materyalleri tespit etmenizi sağlayan metin ve görüntü API’lerini içerir. Ayrıca, farklı modalitelerde zararlı içeriği tespit etmek için örnek kodları görüntüleyip deneyebileceğiniz etkileşimli bir Content Safety Studio da bulunmaktadır. Aşağıdaki [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) hizmete istek yapma sürecinde size rehberlik eder.

Dikkate alınması gereken bir diğer husus ise genel uygulama performansıdır. Çoklu modalite ve çoklu model uygulamalarda, performans sistemin sizin ve kullanıcılarınızın beklentilerine uygun şekilde çalışması, zararlı çıktı üretmemesi anlamına gelir. Genel uygulama performansınızı değerlendirmek için [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) kullanmanız önemlidir.

AI uygulamanızı geliştirme ortamınızda [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ile değerlendirebilirsiniz. Bir test veri seti veya hedef verildiğinde, üretken AI uygulamanızın çıktıları yerleşik veya sizin seçiminize bağlı özel değerlendiricilerle nicel olarak ölçülür. Sisteminizi değerlendirmek için prompt flow sdk ile başlamak üzere [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) rehberini takip edebilirsiniz. Bir değerlendirme çalışması gerçekleştirdikten sonra sonuçları [Azure AI Studio’da görselleştirebilirsiniz](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Bu proje, projeler, ürünler veya hizmetler için ticari markalar veya logolar içerebilir. Microsoft ticari markalarının veya logolarının yetkili kullanımı, [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) kurallarına tabi olup bu kurallara uygun olmalıdır. Microsoft ticari markalarının veya logolarının bu projenin değiştirilmiş sürümlerinde kullanımı karışıklığa yol açmamalı veya Microsoft sponsorluğunu ima etmemelidir. Üçüncü taraf ticari marka veya logolarının kullanımı ise ilgili üçüncü taraf politikalarına tabidir.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorumlamalardan sorumlu değiliz.