<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-05-06T17:44:19+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "tr"
}
-->
# Yalnızca Markdown Modunu Kullanma

## Giriş  
Yalnızca Markdown modu, projenizin sadece Markdown içeriğini çevirmek için tasarlanmıştır. Bu mod, resim çeviri sürecini atlar ve sadece metin içeriğine odaklanır; bu da resim çevirisinin gerekmediği veya Bilgisayarlı Görü ile ilgili ortam değişkenlerinin ayarlanmadığı durumlar için idealdir.

## Ne Zaman Kullanılır  
- Bilgisayarlı Görü ile ilgili ortam değişkenleri yapılandırılmadığında.  
- Resim bağlantılarını güncellemeden sadece metin içeriğini çevirmek istediğinizde.  
- Kullanıcının `-md` komut satırı seçeneğini açıkça belirtmesi durumunda.

## Nasıl Etkinleştirilir  
Yalnızca Markdown modunu etkinleştirmek için komutunuzda `-md` seçeneğini kullanın. Örneğin:  
```
translate -l "ko" -md
```

Ya da Bilgisayarlı Görü ile ilgili ortam değişkenleri yapılandırılmamışsa, `translate -l "ko"` komutunu çalıştırmak otomatik olarak Yalnızca Markdown moduna geçiş yapar.

```
translate -l "ko"
```

Bu komut, Markdown içeriğini Korece’ye çevirir ve resim bağlantılarını çevrilmiş resim yolları yerine orijinal yollarına göre günceller.

## Davranış  
Yalnızca Markdown modunda:  
- Çeviri süreci resim çeviri adımını atlar.  
- Markdown içindeki resim bağlantıları değişmeden kalır ve orijinal yollarına işaret eder.

## Örnekler  
### Öncesi  
```markdown
![Image](../../../getting_started/translated/path/to/image.png)
```  
### Yalnızca Markdown modu kullanıldıktan sonra  
```markdown
![Image](../../../getting_started/original/path/to/image.png)
```

## Sorun Giderme  
- `-md` seçeneğinin komutta doğru belirtildiğinden emin olun.  
- Bilgisayarlı Görü ortam değişkenlerinin sürece müdahale etmediğini doğrulayın.

## Sonuç  
Yalnızca Markdown modu, resim bağlantılarını değiştirmeden metin içeriğini çevirmek için sadeleştirilmiş bir yol sunar. Resim çevirisinin gereksiz olduğu veya Bilgisayarlı Görü kurulumu olmayan ortamlarda özellikle faydalıdır.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.