<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:10:24+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "tr"
}
-->
# Komut referansı

**Co-op Translator** CLI, çeviri sürecini özelleştirmek için çeşitli seçenekler sunar:

Komut                                       | Açıklama
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | Projenizi belirtilen dillere çevirir. Örnek: translate -l "es fr de" komutu İspanyolca, Fransızca ve Almanca'ya çeviri yapar. Tüm desteklenen dillere çevirmek için translate -l "all" kullanın.
translate -l "language_codes" -u             | Mevcut çevirileri silip yeniden oluşturarak çevirileri günceller. Uyarı: Bu işlem belirtilen dillerdeki tüm mevcut çevirileri siler.
translate -l "language_codes" -img           | Sadece görsel dosyalarını çevirir.
translate -l "language_codes" -md            | Sadece Markdown dosyalarını çevirir.
translate -l "language_codes" -nb            | Sadece Jupyter notebook dosyalarını (.ipynb) çevirir.
translate -l "language_codes" --fix          | Önceki değerlendirme sonuçlarına göre düşük güven puanına sahip dosyaları yeniden çevirir.
translate -l "language_codes" -d             | Ayrıntılı günlükler için hata ayıklama modunu etkinleştirir.
translate -l "language_codes" --save-logs, -s| DEBUG seviyesindeki günlükleri <root_dir>/logs/ altında dosyalara kaydeder (konsol -d ile kontrol edilir)
translate -l "language_codes" -r "root_dir"  | Projenin kök dizinini belirtir
translate -l "language_codes" -f             | Görsel çevirisi için hızlı modu kullanır (kalite ve hizalamada hafif bir kayıpla 3 kata kadar daha hızlı çizim).
translate -l "language_codes" -y             | Tüm onay istemlerini otomatik olarak kabul eder (CI/CD süreçleri için kullanışlı)
translate -l "language_codes" --help         | CLI içinde mevcut komutları gösteren yardım detayları
evaluate -l "language_code"                  | Belirli bir dilde çeviri kalitesini değerlendirir ve güven puanları sağlar
evaluate -l "language_code" -c 0.8           | Özel güven eşiği ile çevirileri değerlendirir
evaluate -l "language_code" -f               | Hızlı değerlendirme modu (sadece kural tabanlı, LLM yok)
evaluate -l "language_code" -D               | Derin değerlendirme modu (sadece LLM tabanlı, daha kapsamlı ama daha yavaş)
evaluate -l "language_code" --save-logs, -s  | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altında dosyalara kaydeder
migrate-links -l "language_codes"            | Çevrilmiş Markdown dosyalarını yeniden işleyerek notebook bağlantılarını (.ipynb) günceller. Çevrilmiş notebook varsa onu tercih eder; yoksa orijinal notebook'a dönebilir.
migrate-links -l "language_codes" -r         | Proje kök dizinini belirtir (varsayılan: mevcut dizin).
migrate-links -l "language_codes" --dry-run  | Hangi dosyaların değişeceğini gösterir, değişiklikleri yazmaz.
migrate-links -l "language_codes" --no-fallback-to-original | Çevrilmiş notebook yoksa bağlantıları orijinale yönlendirmez (sadece çevrilmiş varsa günceller).
migrate-links -l "language_codes" -d         | Ayrıntılı günlükler için hata ayıklama modunu etkinleştirir.
migrate-links -l "language_codes" --save-logs, -s | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altında dosyalara kaydeder
migrate-links -l "all" -y                    | Tüm dilleri işler ve uyarı istemini otomatik olarak onaylar.

## Kullanım örnekleri

  1. Varsayılan davranış (mevcut çevirileri silmeden yeni çeviriler ekler):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Sadece yeni Korece görsel çevirileri ekle (mevcut çeviriler silinmez):    translate -l "ko" -img

  3. Tüm Korece çevirileri güncelle (Uyarı: Bu işlem tüm mevcut Korece çevirileri siler ve yeniden çevirir):    translate -l "ko" -u

  4. Sadece Korece görselleri güncelle (Uyarı: Bu işlem tüm mevcut Korece görselleri siler ve yeniden çevirir):    translate -l "ko" -img -u

  5. Sadece Korece için yeni markdown çevirileri ekle, diğer çevirilere dokunma:    translate -l "ko" -md

  6. Önceki değerlendirme sonuçlarına göre düşük güvenli çevirileri düzelt: translate -l "ko" --fix

  7. Sadece belirli dosyalar için düşük güvenli çevirileri düzelt (markdown): translate -l "ko" --fix -md

  8. Sadece belirli dosyalar için düşük güvenli çevirileri düzelt (görseller): translate -l "ko" --fix -img

  9. Görsel çevirisi için hızlı modu kullan:    translate -l "ko" -img -f

  10. Özel eşik ile düşük güvenli çevirileri düzelt: translate -l "ko" --fix -c 0.8

  11. Hata ayıklama modu örneği: - translate -l "ko" -d: Hata ayıklama günlüklerini etkinleştirir.
  12. Günlükleri dosyaya kaydet: translate -l "ko" -s
  13. Konsol DEBUG ve dosya DEBUG: translate -l "ko" -d -s

  14. Korece çeviriler için notebook bağlantılarını taşı (çevrilmiş notebook varsa bağlantıyı güncelle):    migrate-links -l "ko"

  15. Dry-run ile bağlantı taşı (dosya yazılmaz):    migrate-links -l "ko" --dry-run

  16. Sadece çevrilmiş notebook varsa bağlantıyı güncelle (orijinale yönlendirme yok):    migrate-links -l "ko" --no-fallback-to-original

  17. Tüm diller için onay istemiyle işle:    migrate-links -l "all"

  18. Tüm diller için otomatik onayla işle:    migrate-links -l "all" -y
  19. migrate-links için günlükleri dosyaya kaydet:    migrate-links -l "ko ja" -s

### Değerlendirme Örnekleri

> [!WARNING]  
> **Beta Özellik**: Değerlendirme fonksiyonu şu anda beta aşamasındadır. Bu özellik, çevrilmiş belgeleri değerlendirmek için yayınlandı ve değerlendirme yöntemleri ile detaylı uygulama hâlâ geliştirilmektedir ve değişebilir.

  1. Korece çevirileri değerlendir: evaluate -l "ko"

  2. Özel güven eşiği ile değerlendir: evaluate -l "ko" -c 0.8

  3. Hızlı değerlendirme (sadece kural tabanlı): evaluate -l "ko" -f

  4. Derin değerlendirme (sadece LLM tabanlı): evaluate -l "ko" -D

---

**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar bulunabileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.