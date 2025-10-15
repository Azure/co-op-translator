<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:38:36+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "id"
}
-->
# Terjemahkan proyek Anda dengan Co-op Translator

**Co-op Translator** adalah alat antarmuka baris perintah (CLI) yang membantu Anda menerjemahkan file markdown dan gambar dalam proyek Anda ke berbagai bahasa. Bagian ini menjelaskan cara menggunakan alat ini, membahas berbagai opsi CLI, dan memberikan contoh untuk berbagai skenario penggunaan.

> [!NOTE]
> Untuk daftar lengkap perintah dan penjelasan detailnya, silakan lihat [Referensi Perintah](./command-reference.md).

---

## Contoh Skenario dan Perintah

Berikut beberapa kasus penggunaan umum untuk **Co-op Translator**, beserta perintah yang sesuai untuk dijalankan.

### 1. Terjemahan Dasar (Satu Bahasa)

Untuk menerjemahkan seluruh proyek Anda (file markdown dan gambar) ke satu bahasa, misalnya Korea, gunakan perintah berikut:

```bash
translate -l "ko"
```

Perintah ini akan menerjemahkan semua file markdown dan gambar ke bahasa Korea, menambahkan terjemahan baru tanpa menghapus yang sudah ada.

> [!TIP]
>
> Ingin tahu kode bahasa apa saja yang tersedia di **Co-op Translator**? Kunjungi bagian [Bahasa yang Didukung](https://github.com/Azure/co-op-translator#supported-languages) di repositori untuk info lebih lanjut.

#### Contoh pada Phi-3 CookBook

Di **Phi-3 CookBook**, saya menggunakan metode berikut untuk menambahkan terjemahan bahasa Korea pada file markdown dan gambar yang sudah ada.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Menerjemahkan ke Banyak Bahasa

Untuk menerjemahkan proyek Anda ke beberapa bahasa sekaligus (misalnya Spanyol, Prancis, dan Jerman), gunakan perintah ini:

```bash
translate -l "es fr de"
```

Perintah ini akan menerjemahkan proyek ke bahasa Spanyol, Prancis, dan Jerman, menambahkan terjemahan baru tanpa menimpa yang sudah ada.

#### Contoh pada Phi-3 CookBook

Di **Phi-3 CookBook**, setelah menarik perubahan terbaru untuk mencerminkan commit terakhir, saya menggunakan metode berikut untuk menerjemahkan file markdown dan gambar yang baru ditambahkan.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Walaupun umumnya disarankan menerjemahkan satu bahasa dalam satu waktu, dalam situasi seperti ini di mana perubahan spesifik perlu ditambahkan, menerjemahkan beberapa bahasa sekaligus bisa lebih efisien.

### 3. Memperbarui Terjemahan (Menghapus Terjemahan Lama)

Untuk memperbarui terjemahan yang sudah ada (yaitu menghapus terjemahan saat ini dan menggantinya dengan yang baru), gunakan opsi `-u`. Opsi ini akan menghapus semua terjemahan yang ada untuk bahasa yang ditentukan dan menerjemahkan ulang.

```bash
translate -l "ko" -u
```

Peringatan: Perintah ini akan meminta konfirmasi sebelum melanjutkan penghapusan terjemahan yang sudah ada.

#### Contoh pada Phi-3 CookBook

Di **Phi-3 CookBook**, saya menggunakan metode berikut untuk memperbarui semua file terjemahan dalam bahasa Spanyol. Saya sarankan menggunakan metode ini jika ada perubahan besar pada konten asli di banyak dokumen markdown. Jika hanya ada beberapa file markdown terjemahan yang perlu diperbarui, lebih efisien untuk menghapus file tersebut secara manual lalu menggunakan metode `-a` untuk menambahkan terjemahan terbaru.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Menerjemahkan Hanya Gambar

Untuk menerjemahkan hanya file gambar dalam proyek Anda, gunakan opsi `-img`:

```bash
translate -l "ko" -img
```

Perintah ini akan menerjemahkan hanya gambar ke bahasa Korea, tanpa memengaruhi file markdown.

### 6. Menerjemahkan Hanya File Markdown

Untuk menerjemahkan hanya file markdown dalam proyek Anda, gunakan opsi `-md`:

```bash
translate -l "ko" -md
```

#### Contoh pada Phi-3 CookBook

Di **Phi-3 CookBook**, saya menggunakan metode berikut untuk memeriksa kesalahan terjemahan pada file Korea dan secara otomatis mencoba ulang terjemahan untuk file yang terdeteksi bermasalah.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Opsi ini memeriksa kesalahan terjemahan. Saat ini, jika perbedaan jumlah baris antara file asli dan terjemahan lebih dari enam, file tersebut dianggap bermasalah. Saya berencana memperbaiki kriteria ini agar lebih fleksibel di masa depan.

Misalnya, metode ini berguna untuk mendeteksi bagian yang hilang atau terjemahan yang rusak, dan akan otomatis mencoba ulang terjemahan untuk file tersebut.

Namun, jika Anda sudah tahu file mana yang bermasalah, lebih efisien untuk menghapus file tersebut secara manual dan menggunakan opsi `-a` untuk menerjemahkan ulang.

### 8. Mode Debug

Untuk mengaktifkan log detail guna pemecahan masalah, gunakan opsi `-d`:

```bash
translate -l "ko" -d
```

Perintah ini akan menjalankan proses terjemahan dalam mode debug, memberikan informasi log tambahan yang dapat membantu Anda mengidentifikasi masalah selama proses terjemahan.

#### Contoh pada Phi-3 CookBook

Di **Phi-3 CookBook**, saya mengalami masalah di mana terjemahan dengan banyak tautan pada file markdown menyebabkan kesalahan format, seperti terjemahan yang rusak dan baris yang terlewat. Untuk mendiagnosis masalah ini, saya menggunakan opsi `-d` untuk melihat bagaimana proses terjemahan berjalan.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Menerjemahkan ke Semua Bahasa

Jika Anda ingin menerjemahkan proyek ke semua bahasa yang didukung, gunakan kata kunci all.

> [!WARNING]
> Menerjemahkan ke semua bahasa sekaligus bisa memakan waktu lama tergantung ukuran proyek. Misalnya, menerjemahkan **Phi-3 CookBook** ke bahasa Spanyol memakan waktu sekitar 2 jam. Dengan skala seperti ini, tidak praktis jika satu orang menangani 20 bahasa. Disarankan untuk membagi pekerjaan ke beberapa kontributor, masing-masing mengelola satu atau dua bahasa, dan memperbarui terjemahan secara bertahap.

```bash
translate -l "all"
```

Perintah ini akan menerjemahkan proyek ke semua bahasa yang tersedia. Jika Anda melanjutkan, proses terjemahan bisa memakan waktu lama tergantung ukuran proyek.

> [!TIP]
>
> ### Menghapus File Terjemahan Secara Manual (Opsional)
> File terjemahan sekarang otomatis terdeteksi dan dibersihkan saat file sumber diperbarui.
>
> Namun, jika Anda ingin memperbarui terjemahan secara manual - misalnya untuk mengulang terjemahan file tertentu atau menimpa perilaku sistem - Anda bisa menggunakan perintah berikut untuk menghapus semua versi file di folder bahasa.
>
> ### Di Windows:
> 1. **Menggunakan Command Prompt**:
>    - Buka Command Prompt.
>    - Arahkan ke folder tempat file berada dengan perintah `cd`.
>    - Gunakan perintah berikut untuk menghapus file:
>      ```
>      del /s *filename*
>      ```
>      Ganti `filename` dengan bagian nama file yang Anda cari. Opsi `/s` akan mencari di subdirektori juga.
>
> 2. **Menggunakan PowerShell**:
>    - Buka PowerShell.
>    - Jalankan perintah ini:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Ganti `"C:\YourPath"` dengan path folder dan `filename` dengan nama spesifik.
>
> ### Di macOS/Linux:
> 1. **Menggunakan Terminal**:
>   - Buka Terminal.
>   - Arahkan ke direktori dengan `cd`.
>   - Gunakan perintah `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Ganti `filename` dengan nama spesifik.
>
> Selalu periksa file dengan teliti sebelum menghapus untuk menghindari kehilangan data secara tidak sengaja. 
>
> Setelah Anda menghapus file yang perlu diganti, cukup jalankan ulang perintah `translate -l` untuk memperbarui perubahan file terbaru.

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.