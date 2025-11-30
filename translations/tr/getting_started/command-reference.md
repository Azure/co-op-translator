<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:08:16+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "tr"
}
-->
# Komut referansı

**Co-op Translator** CLI, çeviri sürecini özelleştirmek için çeşitli seçenekler sunar:

Komut                                       | Açıklama
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Projenizi belirtilen dillere çevirir. Örnek: translate -l "es fr de" İspanyolca, Fransızca ve Almanca'ya çevirir. Tüm desteklenen dillere çevirmek için translate -l "all" kullanın.
translate -l "language_codes" -u              | Mevcut çevirileri silip yeniden oluşturarak çevirileri günceller. Uyarı: Bu, belirtilen diller için tüm mevcut çevirileri silecektir.
translate -l "language_codes" -img            | Sadece resim dosyalarını çevirir.
translate -l "language_codes" -md             | Sadece Markdown dosyalarını çevirir.
translate -l "language_codes" -nb             | Sadece Jupyter notebook dosyalarını (.ipynb) çevirir.
translate -l "language_codes" --fix           | Önceki değerlendirme sonuçlarına göre düşük güven skoruna sahip dosyaları yeniden çevirir.
translate -l "language_codes" -d              | Ayrıntılı günlük kaydı için hata ayıklama modunu etkinleştirir.
translate -l "language_codes" --save-logs, -s | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altında dosyalara kaydeder (konsol -d ile kontrol edilir)
translate -l "language_codes" -r "root_dir"   | Projenin kök dizinini belirtir
translate -l "language_codes" -f              | Resim çevirisi için hızlı modu kullanır (kalite ve hizalamada hafif bir kayıpla 3 kata kadar daha hızlı çizim).
translate -l "language_codes" -y              | Tüm istemleri otomatik olarak onaylar (CI/CD boru hatları için kullanışlı)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Çevrilmiş markdown ve notebooklara makine çevirisi uyarısı eklemeyi etkinleştirir veya devre dışı bırakır (varsayılan: etkin).
translate -l "language_codes" --help          | CLI içindeki mevcut komutları gösteren yardım detayları
evaluate -l "language_code"                  | Belirli bir dil için çeviri kalitesini değerlendirir ve güven skorları sağlar
evaluate -l "language_code" -c 0.8           | Özel güven eşiği ile çevirileri değerlendirir
evaluate -l "language_code" -f               | Hızlı değerlendirme modu (yalnızca kural tabanlı, LLM yok)
evaluate -l "language_code" -D               | Derin değerlendirme modu (yalnızca LLM tabanlı, daha kapsamlı ancak daha yavaş)
evaluate -l "language_code" --save-logs, -s  | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altında dosyalara kaydeder
migrate-links -l "language_codes"             | Çevrilmiş Markdown dosyalarını yeniden işleyerek notebooklara (.ipynb) olan bağlantıları günceller. Çevrilmiş notebooklar mevcutsa onları tercih eder; yoksa orijinal notebooklara dönebilir.
migrate-links -l "language_codes" -r          | Proje kök dizinini belirtir (varsayılan: mevcut dizin).
migrate-links -l "language_codes" --dry-run   | Değişiklik yapılmadan hangi dosyaların değişeceğini gösterir.
migrate-links -l "language_codes" --no-fallback-to-original | Çevrilmiş karşılıklar yoksa orijinal notebook bağlantılarını yeniden yazmaz (sadece çevrilmiş varsa günceller).
migrate-links -l "language_codes" -d          | Ayrıntılı günlük kaydı için hata ayıklama modunu etkinleştirir.
migrate-links -l "language_codes" --save-logs, -s | DEBUG seviyesindeki günlükleri <root_dir>/logs/ altında dosyalara kaydeder
migrate-links -l "all" -y                      | Tüm dilleri işler ve uyarı istemini otomatik onaylar.

## Kullanım örnekleri

  1. Varsayılan davranış (mevcut çevirileri silmeden yeni çeviriler ekler):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Sadece yeni Korece resim çevirileri ekle (mevcut çeviriler silinmez):    translate -l "ko" -img

  3. Tüm Korece çevirileri güncelle (Uyarı: Bu, tüm mevcut Korece çevirileri silip yeniden çevirir):    translate -l "ko" -u

  4. Sadece Korece resimleri güncelle (Uyarı: Bu, tüm mevcut Korece resimleri silip yeniden çevirir):    translate -l "ko" -img -u

  5. Diğer çevirileri etkilemeden Korece için yeni markdown çevirileri ekle:    translate -l "ko" -md

  6. Önceki değerlendirme sonuçlarına göre düşük güvenli çevirileri düzelt: translate -l "ko" --fix

  7. Sadece belirli dosyalar için düşük güvenli çevirileri düzelt (markdown): translate -l "ko" --fix -md

  8. Sadece belirli dosyalar için düşük güvenli çevirileri düzelt (resimler): translate -l "ko" --fix -img

  9. Resim çevirisi için hızlı modu kullan:    translate -l "ko" -img -f

  10. Özel eşik ile düşük güvenli çevirileri düzelt: translate -l "ko" --fix -c 0.8

  11. Hata ayıklama modu örneği: - translate -l "ko" -d: Hata ayıklama günlüklerini etkinleştir.
  12. Günlükleri dosyalara kaydet: translate -l "ko" -s
  13. Konsol DEBUG ve dosya DEBUG: translate -l "ko" -d -s
  14. Çıktılara makine çevirisi uyarısı eklemeden çevir: translate -l "ko" --no-disclaimer

  15. Korece çeviriler için notebook bağlantılarını güncelle (çevrilmiş notebooklar varsa bağlantıları günceller):    migrate-links -l "ko"

  15. Değişiklik yapmadan bağlantıları göster (dry-run):    migrate-links -l "ko" --dry-run

  16. Sadece çevrilmiş notebooklar varsa bağlantıları güncelle (orijinal dosyalara dönme):    migrate-links -l "ko" --no-fallback-to-original

  17. Tüm dilleri onay istemi ile işle:    migrate-links -l "all"

  18. Tüm dilleri işle ve otomatik onayla:    migrate-links -l "all" -y
  19. migrate-links için günlükleri dosyalara kaydet:    migrate-links -l "ko ja" -s

### Değerlendirme Örnekleri

> [!WARNING]  
> **Beta Özelliği**: Değerlendirme işlevi şu anda beta aşamasındadır. Bu özellik, çevrilmiş belgeleri değerlendirmek için yayınlanmıştır ve değerlendirme yöntemleri ile detaylı uygulama hâlen geliştirilmekte olup değişiklik gösterebilir.

  1. Korece çevirileri değerlendir: evaluate -l "ko"

  2. Özel güven eşiği ile değerlendir: evaluate -l "ko" -c 0.8

  3. Hızlı değerlendirme (yalnızca kural tabanlı): evaluate -l "ko" -f

  4. Derin değerlendirme (yalnızca LLM tabanlı): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->