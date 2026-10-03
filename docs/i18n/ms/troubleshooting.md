# Penyelesaian Masalah

Gunakan halaman ini apabila satu larian terjemahan berjaya secara tidak dijangka, gagal semasa konfigurasi, atau menghasilkan output yang memerlukan semakan.

## Mula Di Sini

1. Jalankan arahan fokus terlebih dahulu, seperti `translate -l "ko" -md`.
2. Tambah `-d` untuk log debug konsol.
3. Tambah `-s` untuk menyimpan log debug di bawah `<root-dir>/logs/`.
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

Pembetulan:

- Konfigurasikan Azure OpenAI, OpenAI, atau Anthropic.
- Sahkan pembolehubah berada dalam persekitaran tempat arahan dijalankan.
- Untuk penggunaan tempatan, letakkan dalam `.env` di akar projek.

Lihat [Konfigurasi](configuration.md).

### Terjemahan Imej Tanpa Azure AI Vision

Ralat:

```text
Image translation requested but Azure AI Service is not configured.
```

Pembetulan:

- Tambah `AZURE_AI_SERVICE_API_KEY`.
- Tambah `AZURE_AI_SERVICE_ENDPOINT`.
- Atau jalankan arahan teks sahaja seperti `translate -l "ko" -md`.

### Kunci atau Endpoint Tidak Sah

Gejala boleh termasuk `401`, ralat kebenaran yang dirahsiakan, atau ralat akses endpoint.

Pembetulan:

- Sahkan kunci itu milik sumber Azure yang sama seperti endpoint.
- Sahkan sumber menyokong Vision apabila menggunakan `-img`.
- Sahkan nama penyebaran Azure OpenAI dan versi API sepadan dengan penyebaran anda.
- Jalankan dengan log debug: `translate -l "ko" -md -d -s`.

## Tiada Fail Diterjemahkan

Punca biasa:

- Bendera yang dipilih tidak sepadan dengan fail anda.
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

Penulisan semula pautan bergantung pada jenis kandungan yang dipilih:

- `-nb` disertakan: pautan notebook boleh menunjuk ke notebook yang diterjemahkan.
- `-nb` dikecualikan: pautan notebook boleh kekal menunjuk ke notebook sumber.
- `-img` disertakan: pautan imej boleh menunjuk ke imej yang diterjemahkan.
- `-img` dikecualikan: pautan imej boleh kekal menunjuk ke imej sumber.

Jalankan terjemahan kandungan penuh apabila semua pautan dalaman sepatutnya mengutamakan keluaran yang diterjemahkan:

```bash
translate -l "ko" -md -nb -img
```

Jalankan semakan pautan selepas terjemahan:

```bash
co-op-review -l "ko"
```

## Isu Pemaparan Markdown

Jika Markdown yang diterjemah dipaparkan dengan tidak betul:

- Periksa bahawa frontmatter bermula dan berakhir dengan `---`.
- Periksa bahawa bilangan pagar kod sepadan antara fail sumber dan fail yang diterjemahkan.
- Jalankan `co-op-review` untuk menangkap isu struktur biasa.
- Terjemah semula fail tertentu jika outputnya rosak.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Berjalan tetapi Tiada Permintaan Tarik Dicipta

Jika `peter-evans/create-pull-request` melaporkan bahawa cawangan tidak mendahului asas, aliran kerja tidak menemui fail untuk dikomit.

Punca yang mungkin:

- Larian terjemahan tidak menghasilkan sebarang perubahan.
- `.gitignore` mengecualikan `translations/`, `translated_images/`, atau notebook yang diterjemahkan.
- `add-paths` tidak sepadan dengan direktori keluaran yang dihasilkan.
- Langkah terjemahan berhenti awal.

Pembetulan:

1. Sahkan fail yang dihasilkan wujud di `translations/` atau `translated_images/`.
2. Sahkan `.gitignore` tidak mengabaikan keluaran yang dihasilkan.
3. Gunakan `add-paths` yang sesuai:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Tambah sementara bendera debug pada arahan translate:

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

Terjemahan mesin mungkin memerlukan semakan manusia. Gunakan `evaluate` hanya apabila anda mahukan pemarkahan kualiti eksperimen dan aliran kerja pembaikan berkeyakinan rendah.

!!! warning "Eksperimental"
    `evaluate` boleh menggunakan pemeriksaan berasaskan peraturan dan berasaskan LLM, dan model pemarkahannya serta tingkah laku metadata mungkin berubah. Keluarkan ia daripada gerbang CI yang diwajibkan melainkan aliran kerja anda bersedia untuk perubahan.

Untuk semakan CI deterministik, gunakan `co-op-review` sebaliknya.