<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:19:53+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "tr"
}
-->
# Azure AI ile Co-op Translator Kurulumu (Azure OpenAI & Azure AI Vision)

Bu rehber, Azure AI Foundry içinde dil çevirisi için Azure OpenAI ve görüntü tabanlı çeviri için kullanılabilecek Azure Computer Vision hizmetini nasıl kuracağınızı adım adım anlatır.

**Gereksinimler:**
- Aktif aboneliğe sahip bir Azure hesabı.
- Azure aboneliğinizde kaynak ve dağıtım oluşturmak için yeterli izinler.

## Azure AI Projesi Oluşturma

AI kaynaklarınızı yönetmek için merkezi bir yer olan Azure AI Projesi oluşturarak başlayacaksınız.

1. [https://ai.azure.com](https://ai.azure.com) adresine gidin ve Azure hesabınızla giriş yapın.

1. Yeni bir proje oluşturmak için **+Create** seçeneğini tıklayın.

1. Aşağıdaki işlemleri gerçekleştirin:
   - Bir **Proje adı** girin (örneğin, `CoopTranslator-Project`).
   - **AI hub** seçin (örneğin, `CoopTranslator-Hub`) (Gerekirse yeni bir tane oluşturun).

1. Projenizi oluşturmak için "**Review and Create**" butonuna tıklayın. Projenizin genel bakış sayfasına yönlendirileceksiniz.

## Dil Çevirisi için Azure OpenAI Kurulumu

Projeniz içinde, metin çevirisi için arka uç olarak hizmet verecek bir Azure OpenAI modeli dağıtacaksınız.

### Projenize Gitme

Henüz açmadıysanız, Azure AI Foundry’de yeni oluşturduğunuz projeyi (örneğin, `CoopTranslator-Project`) açın.

### OpenAI Modeli Dağıtma

1. Projenizin sol menüsünden, "My assets" altında "**Models + endpoints**" seçeneğine tıklayın.

1. **+ Deploy model** seçeneğini seçin.

1. **Deploy Base Model** seçeneğini tıklayın.

1. Karşınıza çıkan model listesinden uygun bir GPT modeli arayın veya filtreleyin. Biz `gpt-4o` modelini öneriyoruz.

1. İstediğiniz modeli seçin ve **Confirm** butonuna basın.

1. Ardından **Deploy** seçeneğini tıklayın.

### Azure OpenAI yapılandırması

Model dağıtıldıktan sonra, "**Models + endpoints**" sayfasından dağıtımı seçerek **REST endpoint URL'si**, **Key**, **Deployment name**, **Model name** ve **API version** bilgilerine ulaşabilirsiniz. Bu bilgiler, çeviri modelini uygulamanıza entegre etmek için gereklidir.

## Görüntü Çevirisi için Azure Computer Vision Kurulumu

Görüntülerdeki metni çevirebilmek için Azure AI Hizmeti API Anahtarı ve Endpoint bilgilerini bulmanız gerekir.

1. Azure AI Projenize (örneğin, `CoopTranslator-Project`) gidin. Proje genel bakış sayfasında olduğunuzdan emin olun.

### Azure AI Hizmeti yapılandırması

Azure AI Hizmeti sekmesinden API Anahtarı ve Endpoint’i bulun.

1. Azure AI Projenize (örneğin, `CoopTranslator-Project`) gidin. Proje genel bakış sayfasında olduğunuzdan emin olun.

1. Azure AI Hizmeti sekmesinde **API Key** ve **Endpoint** bilgilerini bulun.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Bu bağlantı, bağlı Azure AI Hizmetleri kaynağının (görüntü analizi dahil) yeteneklerini AI Foundry projenize açar. Böylece bu bağlantıyı not defterlerinizde veya uygulamalarınızda kullanarak görüntülerden metin çıkarabilir ve ardından bu metni Azure OpenAI modeline çeviri için gönderebilirsiniz.

## Kimlik Bilgilerinizi Birleştirme

Şu ana kadar aşağıdaki bilgileri toplamış olmalısınız:

**Azure OpenAI için (Metin Çevirisi):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Adı (örneğin, `gpt-4o`)
- Azure OpenAI Deployment Adı (örneğin, `cooptranslator-gpt4o`)
- Azure OpenAI API Versiyonu

**Azure AI Hizmetleri için (Görüntü Metni Çıkarma - Vision ile):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Örnek: Ortam Değişkeni Yapılandırması (Önizleme)

Uygulamanızı geliştirirken muhtemelen bu kimlik bilgilerini ortam değişkenleri olarak yapılandıracaksınız. Örneğin:

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-02-01
```

---

### Daha Fazla Okuma

- [Azure AI Foundry'de Proje Oluşturma](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI kaynakları oluşturma](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry'de OpenAI modelleri dağıtma](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum farklılıklarından sorumlu değiliz.