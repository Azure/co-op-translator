<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T14:12:14+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "tr"
}
-->
# Co-op Translator komut satırı arayüzü (CLI) nasıl kullanılır

## Ön Koşullar

- **Python 3.10 veya üzeri**: Co-op Translator'ı çalıştırmak için gereklidir.
- **Dil Modeli Kaynağı**:  
  - **Azure OpenAI** veya diğer LLM'ler. Detaylar için [desteklenen modeller ve servisler](../../../../README.md) bölümüne bakabilirsiniz.
- **Bilgisayar Görüşü Kaynağı** (isteğe bağlı):  
  - Görsel çeviri için. Eğer mevcut değilse, çevirmen [Markdown-only mode](../markdown-only-mode.md) modunda çalışır.  
  - **Azure Computer Vision**

## İçindekiler

1. [Kök dizinde '.env' dosyası oluşturma](./create-env-file.md)  
   - Seçilen dil modeli servisi için gerekli anahtarları ekleyin.  
   - Eğer Azure Computer Vision anahtarları eklenmez veya `-md` belirtilirse, çevirmen yalnızca Markdown modunda çalışacaktır.  
1. [Co-op translator paketini kurma](./install-package.md)  
1. [Projenizi Co-op Translator ile çevirme](./translator-your-project.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmemektedir.