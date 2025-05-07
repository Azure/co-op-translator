<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-05-07T14:12:19+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "tr"
}
-->
# Kök dizinde *.env* dosyasını oluşturun

Bu eğitimde, Azure servisleri için ortam değişkenlerinizi *.env* dosyası kullanarak nasıl ayarlayacağınızı göstereceğiz. Ortam değişkenleri, API anahtarları gibi hassas kimlik bilgilerini kod tabanınıza doğrudan yazmadan güvenli bir şekilde yönetmenizi sağlar.

> [!IMPORTANT]
> - Sadece bir dil modeli servisi (Azure OpenAI veya OpenAI) yapılandırılmalıdır. Tercih ettiğiniz servis için ortam değişkenlerini doldurun. Birden fazla dil modeli için ortam değişkenleri ayarlanırsa, çeviri aracı önceliğe göre birini seçecektir.
> - Computer Vision ortam değişkenleri ayarlanmazsa, çeviri aracı otomatik olarak [Yalnızca Markdown modu](./markdown-only-mode.md)'na geçecektir.

> [!NOTE]
> Bu rehber öncelikle Azure servislerine odaklanmıştır, ancak [desteklenen modeller ve servisler listesi](../README.md#-supported-models-and-services) içinden istediğiniz dil modelini seçebilirsiniz.

## *.env* dosyasını oluşturun

Projenizin kök dizininde *.env* adında bir dosya oluşturun. Bu dosya, tüm ortam değişkenlerinizi basit bir formatta tutacaktır.

> [!WARNING]
> *.env* dosyanızı Git gibi sürüm kontrol sistemlerine göndermeyin. Kazara gönderimleri önlemek için *.env* dosyasını .gitignore dosyanıza ekleyin.

1. Projenizin kök dizinine gidin.

1. Projenizin kök dizininde *.env* dosyasını oluşturun.

1. *.env* dosyasını açın ve aşağıdaki şablonu yapıştırın:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
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

> [!NOTE]
> API anahtarlarınızı ve uç noktalarınızı bulmak için [set-up-azure-ai.md](../set-up-azure-ai.md) dosyasına bakabilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.