<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:40:07+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "tr"
}
-->
# Sadece Markdown Modu Kullanımı

## Giriş  
Sadece Markdown modu, projenizin yalnızca Markdown içeriğini çevirmek için tasarlanmıştır. Bu mod, resim çeviri sürecini atlar ve sadece metin içeriğine odaklanır; bu da resim çevirisinin gerekli olmadığı veya Bilgisayarlı Görü ile ilgili ortam değişkenlerinin ayarlanmadığı durumlar için idealdir.

## Ne Zaman Kullanılır  
- Bilgisayarlı Görü ile ilgili ortam değişkenleri yapılandırılmadığında.  
- Resim bağlantılarını güncellemeden sadece metin içeriğini çevirmek istediğinizde.  
- Kullanıcının `-md` komut satırı seçeneği ile açıkça belirttiği durumlarda.

## Nasıl Etkinleştirilir  
Sadece Markdown modunu etkinleştirmek için komutunuzda `-md` seçeneğini kullanın. Örneğin:  
```
translate -l "ko" -md
```

Ya da Bilgisayarlı Görü ile ilgili ortam değişkenleri yapılandırılmadıysa, `translate -l "ko"` komutunu çalıştırmak otomatik olarak sadece Markdown moduna geçer.

```
translate -l "ko"
```

Bu komut, Markdown içeriğini Korece'ye çevirir ve resim bağlantılarını orijinal yollarında tutar; onları çevrilmiş resim yollarına dönüştürmez.

## Davranış  
Sadece Markdown modunda:  
- Çeviri süreci resim çevirisi adımını atlar.  
- Markdown'daki resim bağlantıları değişmeden, orijinal yollarına işaret eder.

## Örnekler  
### Öncesi  
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.tr.png)
```  
### Sadece Markdown modu kullanıldıktan sonra  
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.tr.png)
```

## Sorun Giderme  
- `-md` seçeneğinin komutta doğru şekilde belirtildiğinden emin olun.  
- Hiçbir Bilgisayarlı Görü ortam değişkeninin sürece müdahale etmediğini doğrulayın.

## Sonuç  
Sadece Markdown modu, resim bağlantılarını değiştirmeden metin içeriğini çevirmek için sadeleştirilmiş bir yol sunar. Resim çevirisinin gereksiz olduğu veya Bilgisayarlı Görü kurulumu olmayan ortamlarda özellikle faydalıdır.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.