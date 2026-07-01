# Repositori Microsoft Untuk Pemula

Halaman ini untuk penyelenggara repositori Microsoft "For Beginners" yang menggunakan bahagian README "Other Courses" yang dikongsi.

Kebanyakan pengguna Co-op Translator tidak memerlukan halaman ini.

## Penyelarasan Automatik Bahagian "Other Courses"

Tambah penanda ini di sekeliling bahagian "Other Courses" dalam README anda:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Setiap kali Co-op Translator dijalankan melalui CLI atau GitHub Actions, ia akan menggantikan kandungan antara penanda tersebut dengan templat yang dibungkus.

## Kemas Kini Templat Dikongsi

Sumber templat terletak di:

```text
src/co_op_translator/templates/other_courses.md
```

Untuk mengemas kini kandungan yang dikongsi:

1. Sunting templat.
2. Buka pull request ke Co-op Translator.
3. Selepas perubahan dilepaskan, jalankan Co-op Translator dalam repositori sasaran.

## Nasihat Sparse Checkout

Repositori kursus yang besar boleh menjadi mahal untuk diklon apabila ia termasuk banyak output yang diterjemahkan. Anda boleh memasukkan nasihat ini dalam seksyen bahasa yang dijana:

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