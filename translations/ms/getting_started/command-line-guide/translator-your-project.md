<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:53:07+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ms"
}
-->
# Terjemahkan projek anda menggunakan Co-op Translator

**Co-op Translator** ialah alat antara muka baris arahan (CLI) yang membantu anda menterjemah fail markdown dan imej dalam projek anda ke dalam pelbagai bahasa. Bahagian ini menerangkan cara menggunakan alat ini, meliputi pelbagai pilihan CLI, dan menyediakan contoh untuk pelbagai kes penggunaan.

> [!NOTE]
> Untuk senarai lengkap arahan dan penerangan terperinci, sila rujuk [Command reference](./command-reference.md).

---

## Senario dan Arahan Contoh

Berikut adalah beberapa kes penggunaan biasa untuk **Co-op Translator**, bersama arahan yang sesuai untuk dijalankan.

### 1. Terjemahan Asas (Satu Bahasa)

Untuk menterjemah keseluruhan projek anda (fail markdown dan imej) ke dalam satu bahasa, seperti Bahasa Korea, gunakan arahan berikut:

```bash
translate -l "ko"
```

Arahan ini akan menterjemah semua fail markdown dan imej ke dalam Bahasa Korea, menambah terjemahan baru tanpa memadam terjemahan sedia ada.

> [!TIP]
>
> Nak tahu kod bahasa yang disokong dalam **Co-op Translator**? Lawati bahagian [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) dalam repositori untuk maklumat lanjut.

#### Contoh pada Phi-3 CookBook

Dalam **Phi-3 CookBook**, saya menggunakan kaedah berikut untuk menambah terjemahan Bahasa Korea bagi fail markdown dan imej yang sedia ada.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Menterjemah Pelbagai Bahasa

Untuk menterjemah projek anda ke dalam beberapa bahasa (contohnya, Sepanyol, Perancis, dan Jerman), gunakan arahan ini:

```bash
translate -l "es fr de"
```

Arahan ini akan menterjemah projek ke dalam bahasa Sepanyol, Perancis, dan Jerman, menambah terjemahan baru tanpa menulis ganti terjemahan sedia ada.

#### Contoh pada Phi-3 CookBook

Dalam **Phi-3 CookBook**, selepas memuat turun perubahan terkini untuk mencerminkan komit terbaru, saya menggunakan kaedah berikut untuk menterjemah fail markdown dan imej yang baru ditambah.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Walaupun biasanya disarankan menterjemah satu bahasa pada satu masa, dalam situasi seperti ini di mana perubahan khusus perlu ditambah, menterjemah pelbagai bahasa sekaligus boleh menjadi lebih cekap.

### 3. Mengemas kini Terjemahan (Memadam Terjemahan Sedia Ada)

Untuk mengemas kini terjemahan yang sedia ada (iaitu, memadam terjemahan semasa dan menggantikannya dengan yang baru), gunakan pilihan `-u`. Ini akan memadam semua terjemahan sedia ada untuk bahasa yang ditentukan dan menterjemah semula.

```bash
translate -l "ko" -u
```

Amaran: Arahan ini akan meminta pengesahan anda sebelum meneruskan pemadaman terjemahan sedia ada.

#### Contoh pada Phi-3 CookBook

Dalam **Phi-3 CookBook**, saya menggunakan kaedah berikut untuk mengemas kini semua fail terjemahan dalam Bahasa Sepanyol. Saya cadangkan menggunakan kaedah ini apabila terdapat perubahan ketara pada kandungan asal merentas beberapa dokumen markdown. Jika hanya beberapa fail terjemahan markdown perlu dikemas kini, lebih cekap untuk memadam fail tersebut secara manual dan kemudian gunakan kaedah `-a` untuk menambah terjemahan yang dikemas kini.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Menterjemah Hanya Imej

Untuk menterjemah hanya fail imej dalam projek anda, gunakan pilihan `-img`:

```bash
translate -l "ko" -img
```

Arahan ini akan menterjemah hanya imej ke dalam Bahasa Korea, tanpa mengubah fail markdown.

### 6. Menterjemah Hanya Fail Markdown

Untuk menterjemah hanya fail markdown dalam projek anda, gunakan pilihan `-md`:

```bash
translate -l "ko" -md
```

### 7. Memeriksa Ralat dalam Fail Terjemahan

Jika anda mahu memeriksa fail terjemahan untuk ralat dan cuba semula terjemahan jika perlu, gunakan pilihan `-chk`:

```bash
translate -l "ko" -chk
```

Arahan ini akan mengimbas fail markdown yang diterjemah dan cuba semula terjemahan untuk fail yang mempunyai ralat.

#### Contoh pada Phi-3 CookBook

Dalam **Phi-3 CookBook**, saya menggunakan kaedah berikut untuk memeriksa ralat terjemahan dalam fail Bahasa Korea dan secara automatik cuba semula terjemahan untuk fail yang dikesan bermasalah.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Pilihan ini memeriksa ralat terjemahan. Pada masa ini, jika perbezaan dalam pemisah baris antara fail asal dan terjemahan melebihi enam, fail tersebut ditandakan sebagai mempunyai ralat terjemahan. Saya merancang untuk memperbaiki kriteria ini agar lebih fleksibel pada masa hadapan.

Contohnya, kaedah ini berguna untuk mengesan bahagian yang hilang atau terjemahan yang rosak, dan ia akan cuba semula terjemahan secara automatik untuk fail tersebut.

Namun, jika anda sudah tahu fail mana yang bermasalah, lebih cekap untuk memadam fail tersebut secara manual dan gunakan pilihan `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Arahan ini akan menjalankan terjemahan dalam mod debug, menyediakan maklumat log tambahan yang boleh membantu anda mengenal pasti isu semasa proses terjemahan.

#### Contoh pada Phi-3 CookBook

Dalam **Phi-3 CookBook**, saya menghadapi masalah di mana terjemahan dengan banyak pautan dalam fail markdown menyebabkan ralat format, seperti terjemahan yang rosak dan abaikan pemisah baris. Untuk mendiagnosis masalah ini, saya menggunakan pilihan `-d` untuk melihat bagaimana proses terjemahan berjalan.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Menterjemah Semua Bahasa

Jika anda mahu menterjemah projek ke semua bahasa yang disokong, gunakan kata kunci all.

> [!WARNING]
> Menterjemah semua bahasa sekaligus boleh mengambil masa yang lama bergantung pada saiz projek. Contohnya, menterjemah **Phi-3 CookBook** ke dalam Bahasa Sepanyol mengambil masa kira-kira 2 jam. Dengan skala sebegini, tidak praktikal untuk seorang sahaja mengendalikan 20 bahasa. Disarankan untuk membahagikan kerja kepada beberapa penyumbang, masing-masing mengurus satu atau dua bahasa, dan mengemas kini terjemahan secara berperingkat.

```bash
translate -l "all"
```

Arahan ini akan menterjemah projek ke semua bahasa yang tersedia. Jika anda teruskan, proses terjemahan mungkin mengambil masa yang lama bergantung pada saiz projek.

> [!TIP]
>
> ### Memadam Fail Terjemahan Secara Manual (Pilihan)
> Fail terjemahan kini dikesan dan dibersihkan secara automatik apabila fail sumber dikemas kini.
>
> Walau bagaimanapun, jika anda mahu mengemas kini terjemahan secara manual - contohnya, untuk buat semula fail tertentu atau menimpa tingkah laku sistem - anda boleh gunakan arahan berikut untuk memadam semua versi fail tersebut merentas folder bahasa.
>
> ### Di Windows:
> 1. **Menggunakan Command Prompt**:
>    - Buka Command Prompt.
>    - Navigasi ke folder tempat fail berada menggunakan arahan `cd`.
>    - Gunakan arahan berikut untuk memadam fail:
>      ```
>      del /s *filename*
>      ```
>      Pilihan `/s` akan mencari dalam subdirektori juga.
>
> 2. **Menggunakan PowerShell**:
>    - Buka PowerShell.
>    - Jalankan arahan ini:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Gantikan `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` dengan arahan:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Gantikan `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` untuk mengemas kini perubahan fail terkini.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.