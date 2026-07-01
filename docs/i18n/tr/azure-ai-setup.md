# Azure AI Kurulumu

Bu kılavuzu, metin çevirisi için Azure OpenAI'ı ve görüntüden metin çıkarma için Azure AI Vision'ı yapılandırmak istediğinizde kullanın.

## Önkoşullar

- Bir Azure aboneliği.
- Azure AI kaynakları ve model dağıtımları oluşturma veya kullanma izni.
- Azure AI Foundry'de bir proje veya Azure OpenAI ve Azure AI Vision kaynaklarına eşdeğer erişim.

## Bir Azure AI Projesi Oluşturun

1. [Azure AI Foundry'yi](https://ai.azure.com) açın.
2. Bir proje oluşturun veya seçin.
3. Proje için bir AI hub oluşturun veya seçin.
4. Oluşturduktan sonra proje genel bakışını açın.

## Azure OpenAI Modeli Dağıtın

1. Projede, **Models + endpoints** öğesini açın.
2. **Deploy model** öğesini seçin.
3. `gpt-4o` gibi bir GPT modeli seçin.
4. Modeli dağıtın.
5. Uç noktayı, dağıtım adını, model adını, API anahtarını ve API sürümünü kaydedin.

!!! note
    Azure OpenAI API sürümü, Azure AI Foundry'de gösterilen model sürümünden ayrıdır. Dağıtımınız için desteklenen bir API sürümü seçin.

## Azure AI Vision'ı Yapılandırın

Görüntü çevirisi, metin çevrilmeden önce kaynak görüntülerden metin çıkarmak için Azure AI Vision'ı kullanır.

Azure AI projenizde Azure AI Services anahtarını ve uç noktasını bulun.

![Azure AI hizmeti bilgilerini bulun](../../assets/find-azure-ai-info.png)

Kaydedin:

- Azure AI Service uç noktası
- Azure AI Service API anahtarı

## Ortam Değişkenleri

Kimlik bilgilerini `.env` dosyanıza veya CI gizli değişkenlerine ekleyin.

```bash
# Görüntü çevirisi için gerekli Azure AI Vision
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Metin çevirisi için gerekli Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator ayrıca isteğe bağlı yedek kimlik bilgisi setlerini de destekler. Tam bir sağlayıcı setini `_1` veya `_2` gibi eklerle çoğaltın; bir yedek setindeki tüm değişkenlerin aynı eki paylaşması gerekir.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Sonraki Adımlar

- Yerel veya CI ortam değişkenlerini ayarlamak için [Yapılandırma](configuration.md) sayfasına dönün.
- Çeviri komutları için [CLI Referansı](cli.md) öğesini kullanın.
- Çeviri pull request'lerini otomatikleştirmek için [GitHub Actions](github-actions.md) kullanın.