# Co-op Translator

_Eğitim amaçlı GitHub içeriğinizin çevirilerini proje geliştikçe birden çok dilde kolayca otomatikleştirin ve yönetin._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python paketi](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Lisans: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![İndirmeler](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![İndirmeler](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Konteyner: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Kod stili: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub katkıda bulunanlar](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub sorunları](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub çekme istekleri](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PR'ler hoş karşılanır](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Buradan başlayın:** [İş akışınızı seçin](https://azure.github.io/co-op-translator/workflows/) | [Yapılandırma](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Sunucusu](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Çok Dilli Destek

#### Co-op Translator tarafından desteklenmektedir

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arapça](../ar/README.md) | [Bengalce](../bn/README.md) | [Bulgarca](../bg/README.md) | [Burma (Myanmar)](../my/README.md) | [Çince (Basitleştirilmiş)](../zh-CN/README.md) | [Çince (Geleneksel, Hong Kong)](../zh-HK/README.md) | [Çince (Geleneksel, Makao)](../zh-MO/README.md) | [Çince (Geleneksel, Tayvan)](../zh-TW/README.md) | [Hırvatça](../hr/README.md) | [Çekçe](../cs/README.md) | [Danca](../da/README.md) | [Hollandaca](../nl/README.md) | [Estonca](../et/README.md) | [Fince](../fi/README.md) | [Fransızca](../fr/README.md) | [Almanca](../de/README.md) | [Yunanca](../el/README.md) | [İbranice](../he/README.md) | [Hintçe](../hi/README.md) | [Macarca](../hu/README.md) | [Endonezyaca](../id/README.md) | [İtalyanca](../it/README.md) | [Japonca](../ja/README.md) | [Kannada](../kn/README.md) | [Kmerce](../km/README.md) | [Korece](../ko/README.md) | [Litvanca](../lt/README.md) | [Malayca](../ms/README.md) | [Malayalamca](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalce](../ne/README.md) | [Nijerya Pidgincesi](../pcm/README.md) | [Norveççe](../no/README.md) | [Farsça (Farsi)](../fa/README.md) | [Lehçe](../pl/README.md) | [Portekizce (Brezilya)](../pt-BR/README.md) | [Portekizce (Portekiz)](../pt-PT/README.md) | [Pencapça (Gurmukhi)](../pa/README.md) | [Romence](../ro/README.md) | [Rusça](../ru/README.md) | [Sırpça (Kiril)](../sr/README.md) | [Slovakça](../sk/README.md) | [Slovence](../sl/README.md) | [İspanyolca](../es/README.md) | [Svahili](../sw/README.md) | [İsveççe](../sv/README.md) | [Tagalog (Filipince)](../tl/README.md) | [Tamilce](../ta/README.md) | [Telugu](../te/README.md) | [Tayca](../th/README.md) | [Türkçe](./README.md) | [Ukraynaca](../uk/README.md) | [Urduca](../ur/README.md) | [Vietnamca](../vi/README.md)

> **Tercihiniz yerel klonlama mı?**
>
> Bu depo 50+ dil çevirisini içerir ve indirme boyutunu önemli ölçüde artırır. Çeviriler olmadan klonlamak için sparse checkout kullanın:
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
> Bu size kursu tamamlamak için ihtiyacınız olan her şeyi çok daha hızlı bir indirme ile sağlar.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub izleyiciler](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forklar](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub yıldızlar](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![GitHub Codespaces'te Aç](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Genel Bakış

**Co-op Translator**, eğitim amaçlı GitHub içeriğinizi birden çok dile zahmetsizce yerelleştirmenize yardımcı olur. Markdown dosyalarınızı, görüntülerinizi veya notebook'larınızı güncellediğinizde, çeviriler otomatik olarak senkronize kalır ve içeriğinizin dünya çapındaki öğrenenler için doğru ve güncel olmasını sağlar.

Depo çevirisi için CLI'den, otomasyon için Python API'den veya ajan ve editör iş akışları için MCP sunucusu üzerinden kullanın.

Çevrilmiş içeriğin nasıl organize edildiğine örnek:

![Örnek](../../imgs/translation-ex.png)

## Neden Co-op Translator?

Bir dosyayı çevirmek kolaydır. Tüm bir dokümantasyon deposunu
çevrilmiş, bağlantılı ve güncel tutmak zordur.

| Problem | Co-op Translator nasıl yardımcı olur |
| --- | --- |
| Long docs are not one prompt | Uzun Markdown dosyaları parçalara ayrılır, böylece uzun bir README tek bir kırılgan model yanıtına bağlı olmaz. Eğer bir parça başarısız olursa, Co-op Translator yalnızca başarısız bölümü yeniden denemek ve yeniden parçalara ayırmak için imkan tanır. |
| Incomplete translations should not be marked current | Kısaltılmış bir çeviri asla güncel olarak işaretlenmemelidir. Co-op Translator kaydetmeden önce çeviri bütünlüğünü kontrol eder ve yapısal olarak eksik mevcut çevirileri tespit edebilir. |
| Links should match the translated repo structure | Manuel çeviriler genellikle göreli bağlantıları kaynak ağaca işaretli bırakır. Co-op Translator Markdown, notebook, görüntü ve README bağlantılarını `translations/<lang>/...` yapısına uyacak şekilde yeniden yazar. |
| Translation should work across an entire repo | Co-op Translator, dosyaları tek tek çevirmek yerine README dosyalarını, belgeleri, notebook'ları ve görüntü metinlerini tek bir depo iş akışının parçası olarak ele alır. |
| Maintaining translations matters more than creating them once | Kaynak hash'leri ve çeviri meta verileri Co-op Translator'ın eski dosyaları bulmasını, değişmeyen dosyaları atlamasını ve çevrilmiş içeriği kaynak depo geliştikçe senkronize tutmasını sağlar. |

## Çeviri durumu nasıl yönetilir

Co-op Translator, çevrilmiş içeriği **sürüm kontrollü yazılım eserleri** olarak,
statik dosyalar olarak değil yönetir.

Araç, çevrilmiş Markdown, görüntü ve notebook'ların durumunu
**dil kapsamlı meta veriler** kullanarak izler.

Bu tasarım Co-op Translator'a şunları yapma imkanı verir:

- Eski çevirileri güvenilir şekilde tespit etme
- Markdown, görüntü ve notebook'ları tutarlı şekilde ele alma
- Büyük, hızlı hareket eden çok dilli depolar çapında güvenli ölçeklenme

Çevirileri yönetilen eserler olarak modelleyerek,
çeviri iş akışları modern
yazılım bağımlılık ve eser yönetimi uygulamalarıyla doğal olarak hizalanır.

→ [Çeviri durumu nasıl yönetilir](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### İlgili derinlemesine incelemeler

- [AI Çevirisinde Bozuk Markdown'ı Düzeltme: Bir Üretim Boru Hattını Güçlendirmek](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Başlarken

Co-op Translator CLI, Python API veya MCP sunucusundan kullanılabilir. Yerel çeviri, otomasyon, CI ve ajan/editör entegrasyonu arasında seçim yapıyorsanız iş akışı kılavuzuyla başlayın.

- [İş akışınızı seçin](../../docs/workflows.md)
- [Kimlik bilgilerini yapılandırın](../../docs/configuration.md)
- [CLI ile çeviri yapın](../../docs/cli.md)
- [Python API ile otomatikleştirin](../../docs/api.md)
- [MCP Sunucusuna bağlanın](../../docs/mcp.md)
- [GitHub Actions'ta çalıştırın](../../docs/github-actions.md)

Yapılandırmadan sonra minimal CLI örneği:

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

Büyük depolarda ilk çalıştırmalar için çevirilmiş dosyaları yazmadan önce `--dry-run` kullanın. İçerik türü bayrakları, günlükler, inceleme ve bağlantı göçü için [CLI Referansı](../../docs/cli.md)'na bakın.

Bash/Zsh ile konteyner hızlı çalıştırma:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

PowerShell ile konteyner hızlı çalıştırma:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Özellikler

- Markdown, notebook'lar ve görüntüler için otomatik çeviri
- Çevirileri kaynak değişiklikleriyle senkron tutar
- Yerel olarak (CLI) veya CI'de (GitHub Actions) çalışır
- MCP aracılığıyla Markdown, notebook, görüntü, inceleme ve proje çeviri araçlarını sunar
- Sağlayıcı destekli çeviri için Azure OpenAI veya OpenAI kullanır
- MCP'nin, Co-op Translator LLM kimlik bilgileri olmadan ajanların Markdown ve notebook parçalarını çevirmesine izin verir
- Görüntü metni çıkarımı ve çevirisi için Azure AI Vision kullanır
- Çeviri yapısını ve güncelliğini deterministik kontrollerle denetler
- Markdown biçimlendirmesini ve yapısını korur

## Belgeler

- [Dokümantasyon sitesi](https://azure.github.io/co-op-translator/)
- [İş akışınızı seçin](../../docs/workflows.md)
- [Yapılandırma](../../docs/configuration.md)
- [Azure AI Kurulumu](../../docs/azure-ai-setup.md)
- [CLI Referansı](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Sunucusu](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [README dil şablonu](../../docs/readme-languages-template.md)
- [Desteklenen diller](../../docs/supported-languages.md)
- [Katkıda bulunma](../../CONTRIBUTING.md)
- [Sorun Giderme](../../docs/troubleshooting.md)

### Microsoft'a özel kılavuz
> [!NOTE]
> Sadece Microsoft “For Beginners” depolarının bakımını yapanlar içindir.

- [“Diğer kurslar” listesini güncelleme (yalnızca MS Beginners depoları için)](../../docs/microsoft-beginners.md)

## Bizi destekleyin ve küresel öğrenimi teşvik edin

Eğitim içeriğinin dünya çapında nasıl paylaşıldığını devrimleştirme çabamıza katılın! [Co-op Translator](https://github.com/azure/co-op-translator)'a GitHub üzerinde bir ⭐ verin ve öğrenme ile teknolojide dil engellerini yıkma misyonumuza destek olun. İlginiz ve katkılarınız büyük bir etki yaratır! Kod katkıları ve özellik önerileri her zaman memnuniyetle karşılanır.

### Microsoft eğitim içeriğini kendi dilinizde keşfedin
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

## Video sunumları

👉 YouTube'da izlemek için aşağıdaki görsele tıklayın.

- **Open at Microsoft**: Co-op Translator'ın nasıl kullanılacağına dair kısa, 18 dakikalık bir tanıtım ve hızlı kılavuz.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Katkıda Bulunma

Bu proje katkılara ve önerilere açıktır. Azure Co-op Translator'a katkıda bulunmakla ilgileniyor musunuz? Co-op Translator'ı daha erişilebilir hale getirmenize yardımcı olacak yönergeler için lütfen [CONTRIBUTING.md](../../CONTRIBUTING.md) dosyasına bakın.

## Katkıda Bulunanlar

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Davranış Kuralları

Bu proje [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/)'nı benimsemiştir. Daha fazla bilgi için [Davranış Kuralları SSS](https://opensource.microsoft.com/codeofconduct/faq/) bölümüne bakın veya ek soru ya da yorumlar için [opencode@microsoft.com](mailto:opencode@microsoft.com) ile iletişime geçin.

## Sorumlu Yapay Zeka

Microsoft, müşterilerimizin yapay zeka ürünlerimizi sorumlu bir şekilde kullanmalarına yardımcı olmaya, öğrenimlerimizi paylaşmaya ve Transparency Notes ve Impact Assessments gibi araçlar aracılığıyla güvene dayalı ortaklıklar kurmaya kararlıdır. Bu kaynakların birçoğunu [https://aka.ms/RAI](https://aka.ms/RAI) adresinde bulabilirsiniz.
Microsoft'un sorumlu yapay zeka yaklaşımı, adalet, güvenilirlik ve güvenlik, gizlilik ve emniyet, kapsayıcılık, şeffaflık ve hesap verebilirlik gibi yapay zeka ilkelerimize dayanmaktadır.

Bu örnekte kullanılanlar gibi büyük ölçekli doğal dil, görüntü ve konuşma modelleri haksız, güvenilmez veya saldırgan davranışlar sergileyebilir ve dolayısıyla zararlara yol açabilir. Riskler ve sınırlamalar hakkında bilgi edinmek için lütfen [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) belgesine bakın.

Bu riskleri azaltmak için önerilen yaklaşım, mimarinizde zararlı davranışı tespit edip engelleyebilen bir güvenlik sistemi bulundurmaktır. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) bağımsız bir koruma katmanı sağlar; uygulamalarda ve hizmetlerde zararlı kullanıcı ve yapay zeka kaynaklı içeriği tespit edebilir. Azure AI Content Safety, zararlı içeriği tespit etmenize olanak tanıyan metin ve görüntü API'lerini içerir. Ayrıca farklı modalitelerde zararlı içeriği tespit etmek için örnek kodları görüntülemenize, keşfetmenize ve denemenize olanak tanıyan etkileşimli bir Content Safety Studio'muz da bulunmaktadır. Aşağıdaki [hızlı başlangıç belgeleri](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) hizmete istek yapmanıza rehberlik eder.

Dikkate alınması gereken bir diğer husus genel uygulama performansıdır. Çok modlu ve çok modelli uygulamalarda, performansın anlamı sistemin sizin ve kullanıcılarınızın beklentileri doğrultusunda çalışmasıdır; buna zararlı çıktılar üretmemek de dahildir. Genel uygulamanızın performansını değerlendirmek için [üretim kalitesi ile risk ve güvenlik metriklerini](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) kullanarak değerlendirme yapmanız önemlidir.

Geliştirme ortamınızda AI uygulamanızı [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) kullanarak değerlendirebilirsiniz. Bir test veri kümesi veya bir hedef verildiğinde, üretken yapay zeka uygulamanızın üretimleri yerleşik değerlendiriciler veya tercih ettiğiniz özel değerlendiricilerle nicel olarak ölçülür. Sisteminizin değerlendirmesine başlamak için prompt flow SDK'sını kullanarak takip edebileceğiniz [hızlı başlangıç kılavuzunu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) inceleyebilirsiniz. Bir değerlendirme çalıştırmasını yürüttükten sonra, sonuçları [Azure AI Studio'da görselleştirebilirsiniz](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ticari Markalar

Bu proje, projeler, ürünler veya hizmetler için ticari markalar veya logolar içerebilir. Microsoft ticari markalarının veya logolarının yetkili kullanımı, [Microsoft'un Ticari Marka ve Marka Kılavuzları](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) uyarınca olmalı ve bu kurallara uymalıdır. Microsoft ticari markalarının veya logolarının bu projenin değiştirilmiş sürümlerinde kullanımı, karışıklığa yol açmamalı veya Microsoft sponsoru olduğunu ima etmemelidir. Üçüncü taraf ticari markalarının veya logolarının herhangi bir kullanımı ise ilgili üçüncü tarafın politikalarına tabidir.

## Yardım Alma

Takılırsanız veya yapay zeka uygulamaları geliştirme hakkında sorularınız varsa, katılın:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ürün geri bildiriminiz veya oluşturma sırasında karşılaştığınız hatalar için ziyaret edin:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)