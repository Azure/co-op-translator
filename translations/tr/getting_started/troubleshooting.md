<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:26:40+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "tr"
}
-->
# Microsoft Co-op Çeviri Sorun Giderme Rehberi

## Genel Bakış  
Microsoft Co-Op Çevirmeni, Markdown belgelerini sorunsuzca çevirmek için güçlü bir araçtır. Bu rehber, araç kullanılırken karşılaşılan yaygın sorunların çözümüne yardımcı olacaktır.

## Yaygın Sorunlar ve Çözümleri

### 1. Markdown Etiketi Sorunu  
**Sorun:** Çevrilen Markdown belgesinin en üstünde `markdown` etiketi yer alıyor ve bu, görüntüleme sorunlarına yol açıyor.

**Çözüm:** Bu sorunu çözmek için, dosyanın en üstündeki `markdown` etiketini silmeniz yeterlidir. Böylece Markdown dosyası doğru şekilde görüntülenecektir.

**Adımlar:**  
1. Çevrilmiş Markdown (`.md`) dosyasını açın.  
2. Belgenin en üstündeki `markdown` etiketini bulun.  
3. `markdown` etiketini silin.  
4. Dosyayı kaydedin.  
5. Dosyayı yeniden açarak doğru görüntülendiğinden emin olun.

### 2. Gömülü Görsellerin URL Sorunu  
**Sorun:** Gömülü görsellerin URL’leri dil yerel ayarına uymuyor, bu da yanlış veya eksik görsellere neden oluyor.

**Çözüm:** Gömülü görsellerin URL’lerini kontrol edin ve dil yerel ayarıyla uyumlu olduklarından emin olun. Tüm görseller `translated_images` klasöründe yer alır ve her görsel dosya adında dil yerel ayar etiketi bulunur.

**Adımlar:**  
1. Çevrilmiş Markdown belgesini açın.  
2. Gömülü görselleri ve URL’lerini tespit edin.  
3. Görsel dosya adındaki dil yerel ayarının belgenin diliyle uyumlu olup olmadığını kontrol edin.  
4. Gerekirse URL’leri güncelleyin.  
5. Değişiklikleri kaydedin ve belgeyi yeniden açarak görsellerin doğru yüklendiğini doğrulayın.

### 3. Çeviri Doğruluğu  
**Sorun:** Çevrilen içerik doğru değil veya daha fazla düzenleme gerekiyor.

**Çözüm:** Çevrilmiş belgeyi gözden geçirin ve doğruluk ile okunabilirliği artırmak için gerekli düzenlemeleri yapın.

**Adımlar:**  
1. Çevrilmiş belgeyi açın.  
2. İçeriği dikkatlice inceleyin.  
3. Çeviri doğruluğunu artırmak için gerekli düzenlemeleri yapın.  
4. Değişiklikleri kaydedin.

### 4. Dosya Formatlama Sorunları  
**Sorun:** Çevrilen belgenin formatlaması yanlış. Bu, özellikle tabloda görülebilir; burada ek ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` tablo sorunlarını çözecektir.

**Adımlar:**  
1. Çevrilmiş belgeyi açın.  
2. Orijinal belge ile karşılaştırarak formatlama sorunlarını belirleyin.  
3. Formatlamayı orijinal belgeye uygun şekilde ayarlayın.  
4. Değişiklikleri kaydedin.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek herhangi bir yanlış anlama veya yorumlama nedeniyle sorumluluk kabul edilmemektedir.