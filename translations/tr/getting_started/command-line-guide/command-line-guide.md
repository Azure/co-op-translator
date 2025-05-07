<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:52:54+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "tr"
}
-->
# Co-op Translator komut satırı arayüzü (CLI) nasıl kullanılır

## Ön Koşullar

- **Python 3.10 veya üzeri**: Co-op Translator'ı çalıştırmak için gereklidir.
- **Dil Modeli Kaynağı**: 
  - **Azure OpenAI** veya diğer LLM’ler. Detaylar için [desteklenen modeller ve servisler](../../../../README.md) sayfasına bakabilirsiniz.
- **Bilgisayarlı Görü Kaynağı** (isteğe bağlı):
  - Görsel çeviri için. Kullanılamazsa, çevirmen [sadece Markdown modu](../markdown-only-mode.md) ile çalışır.
  - **Azure Computer Vision**

### İlk Kurulum

Başlamadan önce aşağıdaki kaynakları kurduğunuzdan emin olun:

- [Azure OpenAI kurulumu](../set-up-resources/set-up-azure-openai.md)
- [Azure Computer Vision kurulumu](../set-up-resources/set-up-azure-computer-vision.md) (isteğe bağlı)

## İçindekiler

1. [Kök dizinde '.env' dosyası oluşturun](./create-env-file.md)
   - Seçilen dil modeli servisi için gerekli anahtarları ekleyin.
   - Eğer Azure Computer Vision anahtarları eklenmez veya `-md` belirtilirse, çevirmen sadece Markdown modunda çalışacaktır.
3. [Co-op translator paketini kurun](./install-package.md)
4. [Projenizi Co-op Translator ile çevirin](./translator-your-project.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle oluşabilecek herhangi bir yanlış anlama veya yorum hatasından sorumlu değiliz.