<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:43:38+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "tr"
}
-->
# "Diğer Kurslar" bölümünü güncelleme (Microsoft Başlangıç depoları)

Bu rehber, "Diğer Kurslar" bölümünün Co-op Translator kullanılarak otomatik senkronize edilmesini ve tüm depolar için global şablonun nasıl güncelleneceğini açıklar.

- Uygulanır: Sadece Microsoft Başlangıç depoları için
- Çalışır: Co-op Translator CLI ve GitHub Actions ile
- Şablon kaynağı: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Hızlı başlangıç: Depoda otomatik senkronizasyonu etkinleştirme

README dosyanızdaki "Diğer Kurslar" bölümünün etrafına aşağıdaki işaretleyicileri ekleyin. Co-op Translator, her çalıştırmada bu işaretleyiciler arasındaki her şeyi değiştirecektir.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator her çalıştırıldığında—CLI üzerinden (örneğin, `translate -l "<language codes>"`) veya GitHub Actions ile—bu işaretleyicilerle çevrelenmiş "Diğer Kurslar" bölümü otomatik olarak güncellenir.

> [!NOTE]
> Eğer mevcut bir listeniz varsa, sadece aynı işaretleyicilerle sarın. Sonraki çalıştırmada en güncel standart içerikle değiştirilecektir.

---

## Global içeriği nasıl değiştirirsiniz

Tüm Başlangıç depolarında görünen standart içeriği güncellemek isterseniz:

1. Şablonu düzenleyin: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Değişikliklerinizle birlikte Co-op Translator deposuna bir pull request açın
3. PR birleştirildikten sonra Co-op Translator sürümü güncellenecektir
4. Hedef depoda Co-op Translator (CLI veya GitHub Action) bir sonraki çalıştırmada güncellenmiş bölümü otomatik olarak senkronize edecektir

Bu, tüm Başlangıç depolarında "Diğer Kurslar" içeriği için tek bir doğru kaynak olmasını sağlar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->