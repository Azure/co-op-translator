<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbc19abb46abfba90855f2b7bd01767",
  "translation_date": "2025-05-06T17:30:21+00:00",
  "source_file": "README.md",
  "language_code": "tr"
}
-->
![Logo](../../../../../../imgs/logo.png)

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

### Co-op Translator ile Desteklenen Diller

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](./README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](../vi/README.md)


[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
>
> **Güçlü Otomasyon**: Artık GitHub Actions desteğiyle! Depo değişiklikleri yapıldığında belgelerinizi otomatik olarak çevirin ve her şeyi zahmetsizce güncel tutun. [Daha fazlasını öğrenin](../..).

## Desteklenen Modeller ve Servisler

| Tür                    | İsim                           |
|------------------------|--------------------------------|
| Dil Modeli             | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Bilgisayarlı Görü      | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> Eğer bilgisayarlı görü servisi mevcut değilse, co-op translator [Markdown-only mode](./getting_started/markdown-only-mode.md) moduna geçecektir.

## Genel Bakış: Eğitim İçeriği Çevirinizi Kolaylaştırın

Dil engelleri, dünya çapındaki öğrenenler ve geliştiriciler için değerli eğitim kaynaklarına ve teknik bilgilere erişimi önemli ölçüde zorlaştırır. Bu durum katılımı sınırlar ve küresel inovasyon ile öğrenme hızını yavaşlatır.

**Co-op Translator**, Microsoft’un kendi büyük ölçekli eğitim serileri (örneğin "For Beginners" rehberleri) için verimsiz olan manuel çeviri sürecini çözmek amacıyla ortaya çıktı. Herkes için bu engelleri kaldırmayı hedefleyen, kullanımı kolay ve güçlü bir araca dönüştü. CLI ve GitHub Actions aracılığıyla yüksek kaliteli otomatik çeviriler sunarak, Co-op Translator eğitimcilerin, öğrencilerin, araştırmacıların ve geliştiricilerin dil bariyerleri olmadan bilgi paylaşmasını ve erişmesini sağlar.

Co-op Translator’ın çevrilmiş eğitim içeriklerini nasıl düzenlediğine göz atın:

![Örnek](../../../../../../imgs/translation-ex.png)

Markdown dosyaları ve görsel metinler otomatik olarak çevrilir ve dil bazlı klasörlerde düzenli şekilde saklanır.

**Co-op Translator ile eğitim içeriğinize küresel erişim sağlayın!**

## Microsoft’un Öğrenme Kaynakları için Küresel Erişimi Destekleme

Co-op Translator, küresel geliştirici topluluğuna hizmet eden depoların çeviri sürecini otomatikleştirerek Microsoft’un önemli eğitim girişimlerinde dil engelini azaltmaya yardımcı olur. Şu anda Co-op Translator kullanan örnekler:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## Temel Özellikler

- **Otomatik Çeviriler**: Metinleri zahmetsizce birden fazla dile çevirin.
- **GitHub Actions Entegrasyonu**: Çevirileri CI/CD hattınızın bir parçası olarak otomatikleştirin.
- **Markdown Koruması**: Çeviri sırasında doğru Markdown sözdizimini koruyun.
- **Görsel Metin Çevirisi**: Görsellerdeki metinleri çıkarıp çevirin.
- **Gelişmiş LLM Teknolojisi**: Yüksek kaliteli çeviriler için son teknoloji dil modellerini kullanın.
- **Kolay Entegrasyon**: Mevcut proje yapınıza sorunsuzca entegre edin.
- **Yerelleştirmeyi Basitleştirin**: Projenizi uluslararası pazarlara kolayca uyarlayın.

## Nasıl Çalışır

![Mimari](../../../../../../imgs/architecture_241019.png)

Co-op Translator, proje klasörünüzden Markdown dosyaları ve görselleri alır ve şu şekilde işler:

1. **Metin Çıkarımı**: Markdown dosyalarından ve yapılandırılmışsa (örneğin Azure Computer Vision ile) görsellerde gömülü metinlerden metni çıkarır.
1. **Yapay Zeka Çevirisi**: Çıkarılan metni yapılandırılmış LLM’ye (Azure OpenAI, OpenAI vb.) çeviri için gönderir.
1. **Sonuç Kaydetme**: Çevrilmiş Markdown dosyalarını ve görselleri (çevirilmiş metinle) dil bazlı klasörlere orijinal formatı koruyarak kaydeder.

## Başlarken

CLI ile hızlıca başlayın veya GitHub Actions ile tam otomasyonu kurun.

### Hızlı Başlangıç: Komut Satırı

Komut satırı kullanarak hızlı başlamak için:

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
    *(Depo içinde `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) değiştirin. Yerel kurulum gerekmez.
- Kılavuzlar:
  - [GitHub Actions Kılavuzu (Açık Depolar ve Standart Gizli Anahtarlar)](./getting_started/github-actions-guide/github-actions-guide-public.md) - Çoğu açık veya kişisel depo için standart depo gizli anahtarlarıyla kullanın.
  - [GitHub Actions Kılavuzu (Microsoft Organizasyon Depoları ve Organizasyon Seviyesi Kurulumlar)](./getting_started/github-actions-guide/github-actions-guide-org.md) - Microsoft GitHub organizasyonu içindeyseniz veya organizasyon seviyesinde gizli anahtarlar ya da runner’lar kullanmanız gerekiyorsa bu kılavuzu takip edin.

> [!NOTE]
> Bu öğretici Azure kaynaklarına odaklansa da, [desteklenen modeller ve servisler](../..) listesindeki herhangi bir dil modelini kullanabilirsiniz.

### Sorun Giderme ve İpuçları

- [Sorun Giderme Kılavuzu](./getting_started/troubleshooting.md)

### Ek Kaynaklar

- [Komut Referansı](./getting_started/command-reference.md): Tüm komutlar ve seçenekler için detaylı rehber.
- [Çok Dilli Destek Kurulumu](./getting_started/multi-language-support.md): README dosyanıza çevrilmiş sürümlere bağlantı ekleme tablosu nasıl eklenir.
- [Desteklenen Diller](./getting_started/supported-languages.md): Desteklenen diller listesi ve yeni dil ekleme talimatları.
- [Sadece Markdown Modu](./getting_started/markdown-only-mode.md): Sadece metni çevirme, görsel çevirisi olmadan nasıl yapılır.

## Video Sunumları

Co-op Translator hakkında daha fazla bilgi edinmek için sunumlarımızı izleyin _(Aşağıdaki görsele tıklayarak YouTube’da izleyebilirsiniz.)_:

- **Open at Microsoft**: Co-op Translator’ı kullanmaya dair 18 dakikalık kısa tanıtım ve hızlı rehber.

  [![Open at Microsoft](../../../../../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: Co-op Translator’ın ne olduğu, kurulumu ve etkili kullanımı ile canlı demo dahil bir saatlik ayrıntılı adım adım rehber.

  [![Microsoft Reactor](../../../../../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Bizi Destekleyin ve Küresel Öğrenmeyi Teşvik Edin

Eğitim içeriğinin dünya çapında paylaşımını dönüştürmek için bize katılın! [Co-op Translator](https://github.com/azure/co-op-translator)’a GitHub’da ⭐ verin ve öğrenme ile teknolojide dil engellerini kaldırma misyonumuza destek olun. İlginiz ve katkılarınız büyük fark yaratır! Kod katkıları ve özellik önerileri her zaman memnuniyetle karşılanır.

## Katkıda Bulunma

Bu proje katkı ve önerilere açıktır. Azure Co-op Translator’a katkıda bulunmak ister misiniz? Katkı sağlama rehberimiz için lütfen [CONTRIBUTING.md](./CONTRIBUTING.md) dosyasına bakın.

## Katkıda Bulunanlar

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Davranış Kuralları

Bu proje [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)’u benimsemiştir.
Daha fazla bilgi için [Code of Conduct SSS](https://opensource.microsoft.com/codeofconduct/faq/) sayfasına bakabilir veya
herhangi bir soru veya yorum için [opencode@microsoft.com](mailto:opencode@microsoft.com) adresiyle iletişime geçebilirsiniz.

## Sorumlu Yapay Zeka

Microsoft, müşterilerimizin yapay zeka ürünlerimizi sorumlu şekilde kullanmalarına yardımcı olmaya, öğrendiklerimizi paylaşmaya ve Transparency Notes ile Impact Assessments gibi araçlarla güvene dayalı ortaklıklar kurmaya kararlıdır. Bu kaynakların çoğuna [https://aka.ms/RAI](https://aka.ms/RAI) adresinden ulaşabilirsiniz.
Microsoft’un sorumlu yapay zeka yaklaşımı, adalet, güvenilirlik ve güvenlik, gizlilik ve güvenlik, kapsayıcılık, şeffaflık ve hesap verebilirlik gibi AI ilkelerimize dayanır.

Bu örnekte kullanılanlar gibi büyük ölçekli doğal dil, görüntü ve konuşma modelleri, haksız, güvenilmez veya rahatsız edici davranışlar sergileyerek zarar verebilir. Riskler ve sınırlamalar hakkında bilgi sahibi olmak için lütfen [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) sayfasını inceleyin.
Bu riskleri azaltmak için önerilen yaklaşım, mimarinizde zararlı davranışları tespit edip önleyebilen bir güvenlik sistemi dahil etmektir. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview), uygulamalarda ve servislerde kullanıcı tarafından oluşturulan ve yapay zeka tarafından üretilen zararlı içeriği tespit edebilen bağımsız bir koruma katmanı sağlar. Azure AI Content Safety, zararlı materyali tespit etmenizi sağlayan metin ve görüntü API'lerini içerir. Ayrıca, farklı modlarda zararlı içeriği tespit etmek için örnek kodları inceleyip deneyebileceğiniz etkileşimli bir Content Safety Studio sunuyoruz. Aşağıdaki [hızlı başlangıç dokümantasyonu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) servise istek yapma sürecinde size rehberlik eder.

Dikkate alınması gereken bir diğer konu ise genel uygulama performansıdır. Çok modlu ve çok model uygulamalarda performans, sistemin sizin ve kullanıcılarınızın beklentileri doğrultusunda çalışması, zararlı çıktı üretmemesi anlamına gelir. Genel uygulamanızın performansını [üretim kalitesi ve risk ile güvenlik metrikleri](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) kullanarak değerlendirmek önemlidir.

AI uygulamanızı geliştirme ortamınızda [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ile değerlendirebilirsiniz. Bir test veri seti veya hedef verildiğinde, üretken AI uygulamanızın çıktıları, yerleşik veya sizin seçtiğiniz özel değerlendiricilerle nicel olarak ölçülür. Sisteminizin değerlendirilmesine başlamak için [hızlı başlangıç kılavuzunu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) takip edebilirsiniz. Bir değerlendirme çalıştırması yaptıktan sonra, sonuçları [Azure AI Studio'da görselleştirebilirsiniz](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tescilli Markalar

Bu proje, projeler, ürünler veya servisler için tescilli markalar veya logolar içerebilir. Microsoft tescilli marka veya logolarının yetkili kullanımı, [Microsoft'un Marka ve Marka Yönergeleri](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) doğrultusunda olmalı ve bu kurallara uymalıdır. Bu projenin değiştirilmiş versiyonlarında Microsoft tescilli marka veya logolarının kullanımı, karışıklık yaratmamalı veya Microsoft sponsorluğunu ima etmemelidir. Üçüncü taraf tescilli marka veya logolarının kullanımı ise ilgili üçüncü tarafın politikalarına tabidir.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.