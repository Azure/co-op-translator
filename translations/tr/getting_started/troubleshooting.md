<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-05-06T17:51:00+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "tr"
}
-->
# Microsoft Co-op Çeviri Sorun Giderme Rehberi

## Genel Bakış  
Microsoft Co-Op Translator, Markdown belgelerini sorunsuzca çevirmek için güçlü bir araçtır. Bu rehber, araç kullanılırken karşılaşılan yaygın sorunların çözümünde size yardımcı olacaktır.

## Yaygın Sorunlar ve Çözümleri

### 1. Markdown Etiketi Sorunu  
**Sorun:** Çevrilen Markdown belgesinin en üstünde `markdown` etiketi bulunuyor ve bu da görüntüleme sorunlarına yol açıyor.

**Çözüm:** Bu sorunu gidermek için, dosyanın en üstündeki `markdown` etiketini silmeniz yeterlidir. Böylece Markdown dosyası doğru şekilde görüntülenecektir.

**Adımlar:**  
1. Çevrilmiş Markdown (`.md`) dosyasını açın.  
2. Belgenin en üstündeki `markdown` etiketini bulun.  
3. `markdown` etiketini silin.  
4. Dosyayı kaydedin.  
5. Dosyayı tekrar açarak doğru görüntülendiğinden emin olun.

### 2. Gömülü Resimlerin URL Sorunu  
**Sorun:** Gömülü resimlerin URL’leri dil yerel ayarına uymuyor, bu da yanlış veya eksik resimlere neden oluyor.

**Çözüm:** Gömülü resimlerin URL’lerini kontrol edin ve dil yerel ayarına uygun olduklarından emin olun. Tüm resimler `translated_images` klasöründe bulunur ve her resim dosyasının isminde dil yerel etiketi vardır.

**Adımlar:**  
1. Çevrilmiş Markdown belgesini açın.  
2. Gömülü resimleri ve URL’lerini belirleyin.  
3. Resim dosya isminde yer alan dil yerel etiketinin belgenin diliyle uyumlu olup olmadığını kontrol edin.  
4. Gerekirse URL’leri güncelleyin.  
5. Değişiklikleri kaydedin ve dosyayı tekrar açarak resimlerin doğru görüntülendiğini doğrulayın.

### 3. Çeviri Doğruluğu  
**Sorun:** Çevrilen içerik doğru değil veya daha fazla düzenleme gerekiyor.

**Çözüm:** Çevrilmiş belgeyi gözden geçirin ve doğruluk ile okunabilirliği artırmak için gerekli düzenlemeleri yapın.

**Adımlar:**  
1. Çevrilmiş belgeyi açın.  
2. İçeriği dikkatlice inceleyin.  
3. Çeviri doğruluğunu artırmak için gerekli düzenlemeleri yapın.  
4. Değişiklikleri kaydedin.

### 4. Dosya Formatlama Sorunları  
**Sorun:** Çevrilen belgenin formatlaması yanlış. Bu, tablolar gibi alanlarda olabilir; burada ek ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` tablo sorunlarını çözecektir.

**Adımlar:**  
1. Çevrilmiş belgeyi açın.  
2. Orijinal belgeyle karşılaştırarak formatlama sorunlarını tespit edin.  
3. Formatlamayı orijinal belgeyle uyumlu olacak şekilde düzeltin.  
4. Değişiklikleri kaydedin.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.