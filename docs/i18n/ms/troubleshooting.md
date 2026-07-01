# Penyelesaian Masalah

Gunakan halaman ini apabila larian terjemahan berjaya secara tidak dijangka, gagal semasa konfigurasi, atau menghasilkan output yang memerlukan semakan.

## Mulakan Di Sini

1. Jalankan perintah terfokus terlebih dahulu, seperti `translate -l "ko" -md`.
2. Tambahkan `-d` untuk log debug konsol.
3. Tambahkan `-s` untuk menyimpan log debug di bawah `<root-dir>/logs/`.
4. Jalankan `co-op-review` selepas terjemahan untuk memeriksa kesegaran, struktur, dan pautan tempatan.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Ralat Konfigurasi

### Tiada Penyedia Model Bahasa

Ralat:

```text
No language model configuration found.
```

Pembaikan:

- Konfigurasikan Azure OpenAI atau OpenAI.
- Sahkan pembolehubah berada dalam persekitaran di mana arahan dijalankan.
- Untuk penggunaan tempatan, letakkan mereka dalam `.env` di akar projek.

Lihat [Konfigurasi](configuration.md).

### Terjemahan Imej Tanpa Azure AI Vision

Ralat:

```text
Image translation requested but Azure AI Service is not configured.
```

Pembaikan:

- Tambah `AZURE_AI_SERVICE_API_KEY`.
- Tambah `AZURE_AI_SERVICE_ENDPOINT`.
- Atau jalankan perintah hanya teks seperti `translate -l "ko" -md`.

### Kekunci atau Endpoint Tidak Sah

Gejala boleh termasuk `401`, ralat kebenaran yang disunting, atau ralat akses endpoint.

Pembaikan:

- Sahkan kunci milik sumber Azure yang sama seperti endpoint.
- Sahkan sumber menyokong Vision apabila menggunakan `-img`.
- Sahkan nama penyebaran Azure OpenAI dan versi API sepadan dengan penyebaran anda.
- Jalankan dengan log debug: `translate -l "ko" -md -d -s`.

## Tiada Fail Diterjemah

Sebab biasa:

- Flag yang dipilih tidak sepadan dengan fail anda.
- Fail terjemahan sedia ada sudah wujud.
- Fail sumber berada di bawah direktori yang dikecualikan.
- Arahan dijalankan dari akar projek yang salah.

Semakan:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Gunakan `--root-dir` apabila arahan dijalankan di luar akar projek.

## Tingkah Laku Pautan Tidak Dijangka

Penulisan semula pautan bergantung kepada jenis kandungan yang dipilih:

- `-nb` termasuk: pautan notebook boleh merujuk kepada notebook yang diterjemah.
- `-nb` dikecualikan: pautan notebook boleh kekal menunjuk ke notebook sumber.
- `-img` termasuk: pautan imej boleh merujuk kepada imej yang diterjemah.
- `-img` dikecualikan: pautan imej boleh kekal menunjuk ke imej sumber.

Jalankan terjemahan kandungan penuh apabila semua pautan dalaman sepatutnya memilih output terjemahan:

```bash
translate -l "ko" -md -nb -img
```

Jalankan semakan pautan selepas terjemahan:

```bash
co-op-review -l "ko"
```

## Isu Paparan Markdown

Jika Markdown yang diterjemah dipaparkan dengan tidak betul:

- Periksa bahawa frontmatter bermula dan berakhir dengan `---`.
- Periksa bahawa bilangan pagar kod sepadan antara fail sumber dan yang diterjemah.
- Jalankan `co-op-review` untuk mengesan isu struktur biasa.
- Terjemahkan semula fail tertentu jika output telah rosak.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Dijalankan tetapi Tiada Pull Request Dibuat

Jika `peter-evans/create-pull-request` melaporkan bahawa cawangan tidak mendahului base, aliran kerja tidak menemui fail untuk dikomit.

Punca yang mungkin:

- Larian terjemahan tidak menghasilkan sebarang perubahan.
- `.gitignore` mengecualikan `translations/`, `translated_images/`, atau notebook yang diterjemah.
- `add-paths` tidak sepadan dengan direktori output yang dijana.
- Langkah terjemahan berhenti lebih awal.

Pembaikan:

1. Sahkan fail yang dijana wujud dalam `translations/` atau `translated_images/`.
2. Sahkan `.gitignore` tidak mengabaikan output yang dijana.
3. Gunakan `add-paths` yang sepadan:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Tambah sementara flag debug pada arahan translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Sahkan kebenaran aliran kerja termasuk:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kualiti Terjemahan

Terjemahan mesin mungkin memerlukan semakan manusia. Gunakan `evaluate` hanya apabila anda mahukan penilaian kualiti eksperimental dan aliran kerja pembaikan berkeyakinan rendah.

!!! warning "Experimental"
    `evaluate` boleh menggunakan pemeriksaan berasaskan peraturan dan berasaskan LLM, dan model skor serta kelakuan metadata mungkin berubah. Jangan masukkan ia dalam gerbang CI yang diwajibkan melainkan aliran kerja anda bersedia untuk perubahan.

Untuk semakan CI yang deterministik, gunakan `co-op-review` sebaliknya.