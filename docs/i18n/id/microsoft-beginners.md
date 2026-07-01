# Repositori Microsoft untuk Pemula

Halaman ini ditujukan untuk pemelihara repositori Microsoft "For Beginners" yang menggunakan bagian README bersama "Other Courses".

Kebanyakan pengguna Co-op Translator tidak memerlukan halaman ini.

## Sinkron Otomatis Bagian "Other Courses"

Tambahkan penanda-penanda berikut di sekitar bagian "Other Courses" dalam README Anda:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Setiap kali Co-op Translator dijalankan melalui CLI atau GitHub Actions, ia menggantikan konten di antara penanda dengan template yang dipaketkan.

## Perbarui Template Bersama

Sumber template berada di:

```text
src/co_op_translator/templates/other_courses.md
```

Untuk memperbarui konten bersama:

1. Sunting template.
2. Buka pull request ke Co-op Translator.
3. Setelah perubahan dirilis, jalankan Co-op Translator di repositori target.

## Peringatan Sparse Checkout

Repositori kursus yang besar bisa menjadi mahal untuk di-clone ketika berisi banyak output terjemahan. Anda dapat menyertakan peringatan ini dalam bagian bahasa yang dihasilkan:

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