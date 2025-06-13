<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:41:58+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "id"
}
-->
# Menggunakan Mode Hanya Markdown

## Pendahuluan
Mode hanya Markdown dirancang untuk menerjemahkan hanya konten Markdown dari proyek Anda. Mode ini melewati proses penerjemahan gambar dan hanya fokus pada konten teks, sehingga ideal untuk situasi di mana penerjemahan gambar tidak diperlukan atau variabel lingkungan yang dibutuhkan untuk Computer Vision belum diatur.

## Kapan Digunakan
- Saat variabel lingkungan terkait Computer Vision tidak dikonfigurasi.
- Saat Anda ingin menerjemahkan hanya konten teks tanpa memperbarui tautan gambar.
- Saat secara eksplisit ditentukan oleh pengguna menggunakan opsi baris perintah `-md`.

## Cara Mengaktifkan
Untuk mengaktifkan mode hanya Markdown, gunakan opsi `-md` dalam perintah Anda. Contohnya:
```
translate -l "ko" -md
```

Atau jika variabel lingkungan terkait Computer Vision tidak dikonfigurasi. Menjalankan `translate -l "ko"` secara otomatis akan beralih ke mode hanya Markdown.

```
translate -l "ko"
```

Perintah ini menerjemahkan konten Markdown ke dalam bahasa Korea dan memperbarui tautan gambar ke jalur aslinya, bukan mengubahnya ke jalur gambar yang diterjemahkan.

## Perilaku
Dalam mode hanya Markdown:
- Proses penerjemahan melewati langkah penerjemahan gambar.
- Tautan gambar dalam Markdown tetap tidak berubah, mengarah ke jalur aslinya.

## Contoh
### Sebelum
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.id.png)
```
### Setelah menggunakan mode hanya Markdown
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.id.png)
```

## Pemecahan Masalah
- Pastikan opsi `-md` sudah ditentukan dengan benar dalam perintah.
- Verifikasi bahwa tidak ada variabel lingkungan Computer Vision yang mengganggu proses.

## Kesimpulan
Mode hanya Markdown menawarkan cara yang lebih sederhana untuk menerjemahkan konten teks tanpa mengubah tautan gambar. Ini sangat berguna ketika penerjemahan gambar tidak diperlukan atau saat bekerja di lingkungan yang tidak memiliki pengaturan Computer Vision.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.