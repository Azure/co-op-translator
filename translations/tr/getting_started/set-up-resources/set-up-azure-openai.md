<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:15:59+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "tr"
}
-->
# Azure OpenAI dil çevirisi için kurulumu yapma

## Azure AI Foundry'de bir Azure OpenAI kaynağı oluşturma

Azure AI Foundry'de Azure OpenAI'yi kurmak için şu adımları izleyin:

### Hub Oluşturma

1. [Azure AI Foundry portalına](https://ai.azure.com) giriş yapın: Azure hesabınızla giriş yaptığınızdan emin olun.

2. Yönetim Merkezi'ne gidin: Ana sayfadan, sol menüden "Management Center" seçeneğini tıklayın.

3. Yeni Bir Hub Oluşturun: "+ New hub" butonuna tıklayın ve Abonelik, Kaynak Grubu ve Hub Adı gibi gerekli bilgileri girin. Hub'ı East US bölgesine konuşlandırmanızı öneririz; çünkü bu bölge Cognitive vision ve GPT modellerini desteklemektedir.

4. İnceleyin ve Oluşturun: Bilgileri gözden geçirin ve hub'ınızı oluşturmak için "Create" butonuna tıklayın.

### Proje Oluşturma

1. Ana Sayfaya Gidin: Henüz ana sayfada değilseniz, sayfanın sol üst köşesinden "Azure AI Foundry" seçeneğine tıklayarak ana sayfaya gidin.

2. Proje Oluşturun: "+ Create project" butonuna tıklayın ve projeniz için bir isim girin.

3. Bir Hub Seçin: Birden fazla hub varsa, kullanmak istediğiniz hub'ı seçin. Yeni bir hub oluşturmak isterseniz, bu adımda yapabilirsiniz.

4. Projeyi Yapılandırın: İhtiyaçlarınıza göre proje ayarlarını takip ederek yapılandırın.

5. Projeyi Oluşturun: Kurulumu tamamlamak için "Create" butonuna tıklayın.

### OpenAI modeli için Model ve Endpoint Dağıtımı

1. [Azure AI Foundry portalına](https://ai.azure.com) giriş yapın: Azure OpenAI Service kaynağınızın bulunduğu Azure aboneliği ile giriş yaptığınızdan emin olun.

2. Modeller ve Endpointlere gidin: Azure AI Foundry ana sayfasından, "Let's go." yazan kutucuğu bulun veya sol menüden Model and Endpoints seçeneğine tıklayın.

3. Henüz bir GPT modeli dağıtmadıysanız, model dağıt seçeneğine tıklayın: GPT-4o, GPT-4o-mini veya o3-mini modellerinden birini seçmenizi öneririz.

4. Kaynaklarınıza erişin: Mevcut Azure OpenAI Service kaynaklarınızı görmelisiniz. Birden fazla kaynağınız varsa, çalışmak istediğiniz kaynağı seçmek için seçiciyi kullanın.

Daha ayrıntılı talimatlar için resmi Azure AI Foundry dokümantasyonuna başvurabilirsiniz.

[How to Create a project](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[How to Create resources](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[How to use OpenAI Model in AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[OpenAI Services in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.