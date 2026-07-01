# Microsoft Yeni Başlayanlar Depoları

Bu sayfa, paylaşılan "Other Courses" README bölümünü kullanan Microsoft "For Beginners" depolarının bakımcıları içindir.

Çoğu Co-op Translator kullanıcısının bu sayfaya ihtiyacı yoktur.

## "Other Courses" Bölümünü Otomatik Eşitleme

README dosyanızdaki "Other Courses" bölümünün etrafına bu işaretçileri ekleyin:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator CLI veya GitHub Actions üzerinden her çalıştırıldığında, işaretçiler arasındaki içeriği paketlenmiş şablonla değiştirir.

## Paylaşılan Şablonu Güncelleme

Şablon kaynağı şu konumdadır:

```text
src/co_op_translator/templates/other_courses.md
```

Paylaşılan içeriği güncellemek için:

1. Şablonu düzenleyin.
2. Co-op Translator'a bir pull request açın.
3. Değişiklik yayımlandıktan sonra hedef depoda Co-op Translator'ı çalıştırın.

## Seyrek Checkout Uyarısı

Büyük ders depoları, birçok çevrilmiş çıktı içerdiğinde klonlamak pahalı hale gelebilir. Bu uyarıyı üretilen dil bölümlerine ekleyebilirsiniz:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```