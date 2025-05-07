<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:55:09+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "tr"
}
-->
# Kök dizinde *.env* dosyasını oluşturun

Bu eğitimde, Azure servisleri için ortam değişkenlerinizi *.env* dosyası kullanarak nasıl ayarlayacağınızı göstereceğiz. Ortam değişkenleri, API anahtarları gibi hassas kimlik bilgilerini kod tabanınıza doğrudan yazmadan güvenli bir şekilde yönetmenizi sağlar.

> [!IMPORTANT]
> - Sadece bir dil modeli servisi (Azure OpenAI veya OpenAI) yapılandırmanız gerekir. Tercih ettiğiniz servisin ortam değişkenlerini doldurun. Birden fazla dil modeli için ortam değişkenleri ayarlanmışsa, co-op çevirmen önceliğe göre birini seçecektir.
> - Computer Vision ortam değişkenleri ayarlanmazsa, çevirmen otomatik olarak [Yalnızca Markdown modu](./markdown-only-mode.md) moduna geçecektir.

> [!NOTE]
> Bu rehber öncelikle Azure servislerine odaklanmıştır, ancak [desteklenen modeller ve servisler listesi](../README.md#-supported-models-and-services) içinden istediğiniz herhangi bir desteklenen dil modelini seçebilirsiniz.

## *.env* dosyasını oluşturun

Projenizin kök dizininde *.env* adında bir dosya oluşturun. Bu dosya, tüm ortam değişkenlerinizi basit bir formatta saklayacaktır.

> [!WARNING]
> *.env* dosyanızı Git gibi sürüm kontrol sistemlerine göndermeyin. Yanlışlıkla gönderilmesini önlemek için *.env* dosyasını .gitignore dosyanıza ekleyin.

1. Projenizin kök dizinine gidin.

1. Projenizin kök dizininde *.env* dosyasını oluşturun.

    ![Create *.env* file.](../../../../imgs/create-env.png)

1. *.env* dosyasını açın ve aşağıdaki şablonu yapıştırın:

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_AIServices_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

## Azure kimlik bilgilerinizi toplayın

Ortam değişkenlerini yapılandırmak için aşağıdaki Azure kimlik bilgilerine ihtiyacınız olacak:

Tüm detayları [AI Foundry](https://ai.azure.com/build/overview) içindeki proje genel bakış sayfasından alabilirsiniz.

![Foundry-overview](../../../../imgs/foundry-overview.png)

### Azure AI Servisi için:

    - Azure Abonelik Anahtarı: Azure AI servislerine erişmenizi sağlayan API anahtarınız.
    - Azure AI Servis Uç Noktası: Belirli Azure AI servisinize ait uç nokta URL'si.

### Azure OpenAI Servisi için:

    - Azure OpenAI API Anahtarı: Azure OpenAI servislerine erişim için API anahtarı.
    - Azure OpenAI Uç Noktası: Azure OpenAI servisinize ait uç nokta URL'si.

1. AI Servisleri anahtarınızı ve Uç Noktanızı *.env* dosyasına kopyalayıp yapıştırın.
2. Azure OpenAI API Anahtarınızı ve Uç Noktanızı *.env* dosyasına kopyalayıp yapıştırın.

### Model Detayları

Sol menüden Model ve Uç Noktaları seçin

![FoundryModels](../../../../imgs/gpt-models.png)

Şimdi kullanmak istediğiniz modeli seçip model detaylarını alın

![ModelDetails](../../../../imgs/model-deployment-name.png)

.env dosyası için aşağıdaki bilgilere ihtiyacımız var

    - Azure OpenAI Model Adı: Etkileşimde bulunacağınız modelin adı.
    - Azure OpenAI Adı: Azure OpenAI modelleriniz için dağıtımınızın adı.
    - Azure OpenAI API Sürümü: URL dizisinin sonunda bulunan Azure OpenAI API sürümü.

Bu bilgileri almak için model dağıtımını seçin

![FoundryModelinfo](../../../../imgs/foundry-model-info.png)

### Azure ortam değişkenlerini ekleyin

3. Azure OpenAI **Adı** ve model **Sürümü**nü *.env* dosyasına kopyalayıp yapıştırın.
4. *.env* dosyasını kaydedin.
5. Artık bu ortam değişkenlerine erişerek **Co-op Translator**’ı Azure servislerinizle kullanabilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.