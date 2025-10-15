<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:41:00+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ms"
}
-->
# Terjemahkan projek anda menggunakan Co-op Translator

**Co-op Translator** ialah alat antara muka baris arahan (CLI) yang membantu anda menterjemah fail markdown dan imej dalam projek anda ke dalam pelbagai bahasa. Bahagian ini menerangkan cara menggunakan alat ini, merangkumi pelbagai pilihan CLI, dan menyediakan contoh untuk pelbagai situasi penggunaan.

---

## Senario dan Arahan Contoh

Berikut adalah beberapa situasi biasa penggunaan **Co-op Translator**, bersama arahan yang sesuai untuk dijalankan.

### 1. Terjemahan Asas (Satu Bahasa)

Untuk menterjemah seluruh projek anda (fail markdown dan imej) ke dalam satu bahasa, seperti Bahasa Korea, gunakan arahan berikut:

```bash
translate -l "ko"
```

Arahan ini akan menterjemah semua fail markdown dan imej ke dalam Bahasa Korea, menambah terjemahan baru tanpa memadamkan yang sedia ada.

#### Contoh pada Phi-3 CookBook

Dalam **Phi-3 CookBook**, saya menggunakan kaedah berikut untuk menambah terjemahan Bahasa Korea bagi fail markdown dan imej yang sedia ada.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Menterjemah ke Pelbagai Bahasa

Untuk menterjemah projek anda ke dalam beberapa bahasa (contohnya, Sepanyol, Perancis, dan Jerman), gunakan arahan ini:

```bash
translate -l "es fr de"
```

Arahan ini akan menterjemah projek ke dalam Sepanyol, Perancis, dan Jerman, menambah terjemahan baru tanpa menulis ganti yang sedia ada.

#### Contoh pada Phi-3 CookBook

Dalam **Phi-3 CookBook**, selepas menarik perubahan terkini untuk mencerminkan komit terbaru, saya menggunakan kaedah berikut untuk menterjemah fail markdown dan imej yang baru ditambah.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

### 3. Mengemas Kini Terjemahan (Padam Terjemahan Sedia Ada)

Untuk mengemas kini terjemahan sedia ada (iaitu, memadam terjemahan semasa dan menggantikannya dengan yang baru), gunakan pilihan `-u`. Ini akan memadam semua terjemahan sedia ada untuk bahasa yang ditentukan dan menterjemah semula.

```bash
translate -l "ko" -u
```

Amaran: Arahan ini akan meminta pengesahan sebelum meneruskan pemadaman terjemahan sedia ada.

#### Contoh pada Phi-3 CookBook

Dalam **Phi-3 CookBook**, saya menggunakan kaedah berikut untuk mengemas kini semua fail terjemahan dalam Bahasa Sepanyol. Saya mengesyorkan kaedah ini apabila terdapat perubahan besar pada kandungan asal merentasi beberapa dokumen markdown. Jika hanya ada beberapa fail markdown terjemahan yang perlu dikemas kini, lebih efisien untuk memadam fail tersebut secara manual dan kemudian gunakan kaedah `-a` untuk menambah terjemahan yang dikemas kini.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Menterjemah Imej Sahaja

Untuk menterjemah hanya fail imej dalam projek anda, gunakan pilihan `-img`:

```bash
translate -l "ko" -img
```

Arahan ini akan menterjemah hanya imej ke dalam Bahasa Korea, tanpa menjejaskan mana-mana fail markdown.

### 6. Menterjemah Fail Markdown Sahaja

Untuk menterjemah hanya fail markdown dalam projek anda, gunakan pilihan `-md`:

```bash
translate -l "ko" -md
```

#### Contoh pada Phi-3 CookBook

Dalam **Phi-3 CookBook**, saya menggunakan kaedah berikut untuk menyemak ralat terjemahan dalam fail Bahasa Korea dan secara automatik mencuba semula terjemahan untuk mana-mana fail yang dikesan bermasalah.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Pilihan ini menyemak ralat terjemahan. Pada masa ini, jika perbezaan baris antara fail asal dan terjemahan melebihi enam, fail tersebut akan ditandakan sebagai mempunyai ralat terjemahan. Saya bercadang untuk menambah baik kriteria ini agar lebih fleksibel pada masa akan datang.

Sebagai contoh, kaedah ini berguna untuk mengesan bahagian yang hilang atau terjemahan yang rosak, dan ia akan secara automatik mencuba semula terjemahan untuk fail-fail tersebut.

Namun, jika anda sudah tahu fail mana yang bermasalah, lebih efisien untuk memadam fail tersebut secara manual dan gunakan pilihan `-a` untuk menterjemah semula.

### 8. Mod Nyahpepijat (Debug)

Untuk mengaktifkan log terperinci bagi tujuan penyelesaian masalah, gunakan pilihan `-d`:

```bash
translate -l "ko" -d
```

Arahan ini akan menjalankan terjemahan dalam mod debug, memberikan maklumat log tambahan yang boleh membantu anda mengenal pasti isu semasa proses terjemahan.

#### Contoh pada Phi-3 CookBook

Dalam **Phi-3 CookBook**, saya menghadapi isu di mana terjemahan dengan banyak pautan dalam fail markdown menyebabkan ralat format, seperti terjemahan yang rosak dan baris baru yang diabaikan. Untuk mendiagnosis masalah ini, saya menggunakan pilihan `-d` untuk melihat bagaimana proses terjemahan berjalan.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Menterjemah ke Semua Bahasa

Jika anda ingin menterjemah projek ke semua bahasa yang disokong, gunakan kata kunci all.

```bash
translate -l "all"
```

Arahan ini akan menterjemah projek ke semua bahasa yang tersedia. Jika anda meneruskan, proses terjemahan mungkin mengambil masa yang lama bergantung pada saiz projek.

> ### Padam Fail Terjemahan Secara Manual (Pilihan)
> Fail terjemahan kini dikesan dan dibersihkan secara automatik apabila fail sumber dikemas kini.
>
> Namun, jika anda ingin mengemas kini terjemahan secara manual - contohnya, untuk mengulangi semula fail tertentu atau menulis ganti tingkah laku sistem - anda boleh gunakan arahan berikut untuk memadam semua versi fail tersebut di semua folder bahasa.
>
> ### Di Windows:
> 1. **Menggunakan Command Prompt**:
>    - Buka Command Prompt.
>    - Navigasi ke folder di mana fail berada menggunakan arahan `cd`.
>    - Gunakan arahan berikut untuk memadam fail:
>      ```
>      del /s *filename*
>      ```
>      Gantikan `filename` dengan bahagian nama fail yang anda cari. Pilihan `/s` akan mencari dalam subdirektori juga.
>
> 2. **Menggunakan PowerShell**:
>    - Buka PowerShell.
>    - Jalankan arahan ini:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Gantikan `"C:\YourPath"` dengan laluan folder dan `filename` dengan nama tertentu.
>
> ### Di macOS/Linux:
> 1. **Menggunakan Terminal**:
>   - Buka Terminal.
>   - Navigasi ke direktori dengan `cd`.
>   - Gunakan arahan `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Gantikan `filename` dengan nama tertentu.
>
> Sentiasa semak fail dengan teliti sebelum memadam untuk mengelakkan kehilangan data secara tidak sengaja.
>
> Setelah anda memadam fail yang perlu diganti, jalankan semula arahan `translate -l` anda untuk mengemas kini perubahan fail terkini.

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.