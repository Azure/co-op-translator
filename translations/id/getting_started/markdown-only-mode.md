<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-05-06T17:44:33+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "id"
}
-->
# Menggunakan Mode Hanya Markdown

## Pendahuluan
Mode hanya Markdown dirancang untuk menerjemahkan hanya konten Markdown dari proyek Anda. Mode ini melewati proses penerjemahan gambar dan hanya fokus pada konten teks, membuatnya ideal untuk situasi di mana penerjemahan gambar tidak diperlukan atau variabel lingkungan yang diperlukan untuk Computer Vision belum disetel.

## Kapan Digunakan
- Ketika variabel lingkungan terkait Computer Vision belum dikonfigurasi.
- Ketika Anda hanya ingin menerjemahkan konten teks tanpa memperbarui tautan gambar.
- Ketika secara eksplisit ditentukan oleh pengguna menggunakan opsi baris perintah `-md`.

## Cara Mengaktifkan
Untuk mengaktifkan mode hanya Markdown, gunakan opsi `-md` dalam perintah Anda. Misalnya:
```
translate -l "ko" -md
```

Atau jika variabel lingkungan terkait Computer Vision belum dikonfigurasi. Menjalankan `translate -l "ko"` secara otomatis akan beralih ke mode hanya Markdown.

```
translate -l "ko"
```

Perintah ini menerjemahkan konten Markdown ke dalam bahasa Korea dan memperbarui tautan gambar ke jalur aslinya, bukan mengubahnya menjadi jalur gambar yang diterjemahkan.

## Perilaku
Dalam mode hanya Markdown:
- Proses penerjemahan melewati langkah penerjemahan gambar.
- Tautan gambar dalam Markdown tetap tidak berubah, mengarah ke jalur aslinya.

## Contoh
### Sebelum
```markdown
![Image](../../../getting_started/translated/path/to/image.png)
```
### Setelah menggunakan mode hanya Markdown
```markdown
![Image](../../../getting_started/original/path/to/image.png)
```

## Pemecahan Masalah
- Pastikan opsi `-md` sudah ditentukan dengan benar dalam perintah.
- Verifikasi bahwa tidak ada variabel lingkungan Computer Vision yang mengganggu proses.

## Kesimpulan
Mode hanya Markdown menawarkan cara yang efisien untuk menerjemahkan konten teks tanpa mengubah tautan gambar. Ini sangat berguna ketika penerjemahan gambar tidak diperlukan atau saat bekerja di lingkungan yang tidak memiliki pengaturan Computer Vision.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.