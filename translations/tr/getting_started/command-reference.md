<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-05-06T17:42:17+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "tr"
}
-->
# Komut referansı
**Co-op Translator** CLI, çeviri sürecini özelleştirmek için çeşitli seçenekler sunar:

Komut                                        | Açıklama
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Projenizi belirtilen dillere çevirir. Örnek: translate -l "es fr de" İspanyolca, Fransızca ve Almanca'ya çevirir. Tüm desteklenen dillere çevirmek için translate -l "all" kullanın.
translate -l "language_codes" -u              | Mevcut çevirileri silip yeniden oluşturarak çevirileri günceller. Uyarı: Bu, belirtilen diller için tüm mevcut çevirileri silecektir.
translate -l "language_codes" -img            | Sadece resim dosyalarını çevirir.
translate -l "language_codes" -md             | Sadece Markdown dosyalarını çevirir.
translate -l "language_codes" -chk            | Çevrilen dosyaları hatalar için kontrol eder ve gerekirse çeviriyi tekrar dener.
translate -l "language_codes" -d              | Ayrıntılı kayıt için hata ayıklama modunu etkinleştirir.
translate -l "language_codes" -r "root_dir"   | Projenin kök dizinini belirtir
translate -l "language_codes" -f              | Resim çevirisi için hızlı modu kullanır (kalite ve hizalamada hafif bir kayıpla 3 kata kadar daha hızlı çizim).
translate -l "language_codes" -y              | Tüm onayları otomatik kabul eder (CI/CD boru hatları için kullanışlıdır)
translate -l "language_codes" --help          | CLI içinde mevcut komutları gösteren yardım detayları

### Kullanım örnekleri:

  1. Varsayılan davranış (mevcut çevirileri silmeden yeni çeviriler ekler):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Sadece yeni Korece resim çevirileri ekle (mevcut çeviriler silinmez):    translate -l "ko" -img

  3. Tüm Korece çevirileri güncelle (Uyarı: Bu, yeniden çevirmeden önce tüm mevcut Korece çevirileri siler):    translate -l "ko" -u

  4. Sadece Korece resimleri güncelle (Uyarı: Bu, yeniden çevirmeden önce tüm mevcut Korece resimleri siler):    translate -l "ko" -img -u

  5. Diğer çevirileri etkilemeden Korece için yeni markdown çevirileri ekle:    translate -l "ko" -md

  6. Çevrilen dosyaları hatalar için kontrol et ve gerekirse çeviriyi tekrar dene: translate -l "ko" -chk

  7. Çevrilen dosyaları hatalar için kontrol et ve gerekirse çeviriyi tekrar dene (sadece markdown): translate -l "ko" -chk -md

  8. Çevrilen dosyaları hatalar için kontrol et ve gerekirse çeviriyi tekrar dene (sadece resimler): translate -l "ko" -chk -img

  9. Resim çevirisi için hızlı modu kullan:    translate -l "ko" -img -f

  10. Hata ayıklama modu örneği: - translate -l "ko" -d: Hata ayıklama kayıtlarını etkinleştir.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.