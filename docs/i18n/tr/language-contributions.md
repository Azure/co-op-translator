# Dil geliştirmelerine katkıda bulunma

Dil bilginiz Co-op Translator'ın gelişmesine yardımcı olabilir. Bir örnek, önerilen bir düzeltme ve bir açıklama ile başlayın; bunu [çeviri geri bildirim formu](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml) kullanarak yapabilirsiniz. Kod yazmanıza veya bir model çalıştırmak için ödeme yapmanıza gerek yok.

## Bir rapordan ortak bir iyileştirmeye

1. Bir katkıda bulunan, kaynak bir alıntı, çevirisini ve bağlamı sağlar.
2. Bir dil inceleyicisi anlamı, doğallığı ve önerinin belirli bir yerel ayara veya kursa bağlı olup olmadığını kontrol eder.
3. Bir bakım sorumlusu düzeltmenin kaynak kursa, paylaşılan dil talimatına, terminoloji yapılandırmasına veya çeviri koduna ait olup olmadığına karar verir.
4. Paylaşılan bir kural için, bir bakım sorumlusu rapor edilen örnek ve alakasız örneklerde değişiklik öncesi ve sonrası çıktıları karşılaştırır. Katkıda bulunanlar bu çıktıları aracı kendileri çalıştırmadan inceleyebilir.
5. Ortaya çıkan PR rapora bağlantı verir ve örnekleri ve incelemeyi sağlayan kişilere kredi verir. Tüketen depolarda dağıtım veya yeniden oluşturma ayrı bir adımdır.

Bir rapor otomatik olarak istemleri değiştirmez veya kurs çevirilerini yeniden oluşturmaz. Kursa özgü düzeltmeler kurs deposuyla bağlı kalmalıdır. Manuel bir düzenlemenin sonraki yeniden çeviride korunacağını varsaymayın; bu iş akışı için davranışı doğrulayın.

## Varolan örnek: Japonca Markdown bağlantıları

Bu [Japon talimat dosyası](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) modelin bağlantı metnini çevirirken Markdown sözdizimini ve bağlantı hedefini korumasını söyler. Örneğin, `[text](URL)` olarak yazılmış bir bağlantı `「text」（URL）` olmamalıdır.

Bu, doğru ve yanlış çıktının bir örneğiyle desteklenen odaklanmış bir dil kuralı örneğidir. İstem talimatlarının tek başına doğru Markdown'u garanti ettiğine dair bir kanıt değildir.

[Markdown istem oluşturucu](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py), küçük harfe çevrilmiş ve kırpılmış bir dil kodu kullanarak `templates/language/<language_code>.md` yükler. Dosya yoksa ortak yönergeleri kullanır. Bu, Markdown istem yolunu açıklar; her görüntü veya diğer çeviri yollarının aynı yönergeleri kullandığını varsaymayın.

Bu [istem testleri](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) Japonca talimatların dahil olduğunu kontrol eder. Bu, istem derlemesini doğrular, çeviri kalitesini değil.

## Bir dil kuralında ne olmalı?

Kaynak örneği, beklenen davranış ve kuralın uygulanmaması gereken bir karşıörnek içeren dar, tekrarlanabilir bir düzeltme önerin. Anlamı, yer tutucuları, kodu, URL'leri ve belge yapısını koruyun. Bir kişinin stil tercihini veya bir kursun terminolojisini evrensel bir kurala dönüştürmekten kaçının.

Mevcut [sözlük uygulaması](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) terimleri çeviriden korur. Bu bir kaynak-hedef terminoloji sözlüğü değildir. Yeni terminoloji davranışını katkıda bulunanlara taahhüt etmeden önce tartışın.

## Topluluk örneği: Japonca ürün adı raporu

[rapor #527](https://github.com/Azure/co-op-translator/issues/527) içinde, @hyoshioka0128 ürün adını `Co-op Translator`'den `Co-op 翻訳`'ye değiştiren bir Japonca çeviri tespit etti. Rapor, etkilenen belgeye bir bağlantı ve bir ekran görüntüsü içeriyordu, bu da sorunun kolayca bulunmasını sağladı.

Katkıda bulunan ayrıca bir [ilişkili kurs PR'si](https://github.com/microsoft/AZD-for-beginners/pull/109) ekledi. Sorun tartışmasında, bakım sorumlusu raporu kabul etti ve adın neden değiştiğini araştırmayı önerdi; buna terminoloji koruma, sözlük davranışı ve çeviri yolu da dahildi.

Bu, küçük bir raporun bireysel bir ifade düzeltmesinin ötesinde bir araştırmayı nasıl destekleyebileceğini gösterir. Bu, doğrulanmış bir önce/sonra sonucu veya yukarıdaki Japonca Markdown-bağlantı talimatlarının bu ürün adı sorununu düzelttiğine dair kanıt değildir.

Aynı şekilde katkıda bulunabilirsiniz: orijinal metni, mevcut çeviriyi, önerilen düzeltmeyi ve neden önemli olduğunu paylaşın. Kullanışlı olduğunda belge bağlantısı veya ekran görüntüsü ekleyin. Nedeni teşhis etmeniz veya raporlamadan önce bir istem yazmanız gerekmez.

## Bir kuralı benimsemeden önce doğrulama

Aynı kaynak örneklerini, çevirmen revizyonunu, sağlayıcı/modeli ve üretim ayarlarını temel ve aday çalıştırmaları için kullanın, yalnızca önerilen talimatı değiştirin. Gerçek istem değişikliğini ve çıktıları kaydedin; tutarlı bir etkiyi çıktı değişkenliğinden ayırmak için gerektiğinde örnekleri tekrarlayın. Rapor edilen hatayı, karşıt bağlamları ve zaten doğru çevirilen örnekleri dahil edin.

| Örnek | Kaynak/bağlam | Temel çıktı | Aday çıktı | İnceleyici değerlendirmesi |
| --- | --- | --- | --- | --- |
| Rapor edilen hata | Toplanacak | Çalıştırılmadı | Çalıştırılmadı | Beklemede |
| Karşıörnek | Toplanacak | Çalıştırılmadı | Çalıştırılmadı | Beklemede |
| Etkilenmeyen örnek | Toplanacak | Çalıştırılmadı | Çalıştırılmadı | Beklemede |

Yapısal değişmezleri dilsel yargılardan ayrı olarak kontrol edin. Başarılı bir istem-yükleme testi kalite değerlendirmesi değildir ve tek bir tam beklenen cümle tek geçerli çeviri değildir. Bağlam, model çalıştırmaları veya dil incelemesi eksikse, sorunun çözüldüğünü iddia etmek yerine öneriyi beklemede tutun.