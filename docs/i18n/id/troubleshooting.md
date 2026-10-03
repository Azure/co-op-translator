# Pemecahan Masalah

Gunakan halaman ini ketika proses terjemahan berhasil secara tidak terduga, gagal saat konfigurasi, atau menghasilkan keluaran yang perlu ditinjau.

## Mulai Di Sini

1. Jalankan perintah yang terfokus terlebih dahulu, seperti `translate -l "ko" -md`.
2. Tambahkan `-d` untuk log debug konsol.
3. Tambahkan `-s` untuk menyimpan log debug di bawah `<root-dir>/logs/`.
4. Jalankan `co-op-review` setelah terjemahan untuk memeriksa kesegaran, struktur, dan tautan lokal.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Kesalahan Konfigurasi

### Tidak Ada Penyedia Model Bahasa

Kesalahan:

```text
No language model configuration found.
```

Perbaikan:

- Konfigurasikan Azure OpenAI, OpenAI, atau Anthropic.
- Pastikan variabel ada di lingkungan tempat perintah dijalankan.
- Untuk penggunaan lokal, letakkan di `.env` pada root proyek.

Lihat [Konfigurasi](configuration.md).

### Terjemahan Gambar Tanpa Azure AI Vision

Kesalahan:

```text
Image translation requested but Azure AI Service is not configured.
```

Perbaikan:

- Tambahkan `AZURE_AI_SERVICE_API_KEY`.
- Tambahkan `AZURE_AI_SERVICE_ENDPOINT`.
- Atau jalankan perintah teks saja seperti `translate -l "ko" -md`.

### Kunci atau Endpoint Tidak Valid

Gejala dapat termasuk `401`, kesalahan izin yang disamarkan, atau kesalahan akses endpoint.

Perbaikan:

- Pastikan kunci milik sumber daya Azure yang sama dengan endpoint.
- Pastikan sumber daya mendukung Vision saat menggunakan `-img`.
- Pastikan nama deployment Azure OpenAI dan versi API cocok dengan deployment Anda.
- Jalankan dengan log debug: `translate -l "ko" -md -d -s`.

## Tidak Ada Berkas yang Diterjemahkan

Penyebab umum:

- Flag yang dipilih tidak cocok dengan berkas Anda.
- Berkas terjemahan sudah ada.
- Berkas sumber berada di bawah direktori yang dikecualikan.
- Perintah dijalankan dari root proyek yang salah.

Pemeriksaan:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Gunakan `--root-dir` ketika perintah dijalankan di luar root proyek.

## Perilaku Tautan yang Tidak Terduga

Penulisan ulang tautan bergantung pada jenis konten yang dipilih:

- `-nb` disertakan: tautan notebook dapat menunjuk ke notebook yang diterjemahkan.
- `-nb` dikecualikan: tautan notebook dapat tetap menunjuk ke notebook sumber.
- `-img` disertakan: tautan gambar dapat menunjuk ke gambar yang diterjemahkan.
- `-img` dikecualikan: tautan gambar dapat tetap menunjuk ke gambar sumber.

Jalankan terjemahan konten penuh ketika semua tautan internal seharusnya mengarah ke keluaran yang diterjemahkan:

```bash
translate -l "ko" -md -nb -img
```

Jalankan peninjauan tautan setelah terjemahan:

```bash
co-op-review -l "ko"
```

## Masalah Perenderan Markdown

Jika Markdown terjemahan dirender tidak benar:

- Periksa bahwa frontmatter dimulai dan diakhiri dengan `---`.
- Periksa bahwa jumlah pagar kode (code fence) cocok antara berkas sumber dan terjemahan.
- Jalankan `co-op-review` untuk menangkap masalah struktur umum.
- Terjemahkan ulang berkas tertentu jika keluaran terkorupsi.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Berjalan tetapi Tidak Ada Pull Request yang Dibuat

Jika `peter-evans/create-pull-request` melaporkan bahwa cabang tidak lebih maju dari basis, alur kerja tidak menemukan berkas untuk dikomit.

Kemungkinan penyebab:

- Proses terjemahan tidak menghasilkan perubahan.
- `.gitignore` mengecualikan `translations/`, `translated_images/`, atau notebook yang diterjemahkan.
- `add-paths` tidak cocok dengan direktori keluaran yang dihasilkan.
- Langkah terjemahan berhenti lebih awal.

Perbaikan:

1. Pastikan berkas yang dihasilkan ada di `translations/` atau `translated_images/`.
2. Pastikan `.gitignore` tidak mengabaikan keluaran yang dihasilkan.
3. Gunakan `add-paths` yang sesuai:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Tambahkan flag debug sementara ke perintah translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Pastikan izin workflow mencakup:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kualitas Terjemahan

Terjemahan mesin mungkin memerlukan tinjauan manusia. Gunakan `evaluate` hanya ketika Anda menginginkan pemeringkatan kualitas eksperimental dan alur kerja perbaikan untuk hasil dengan kepercayaan rendah.

!!! warning "Eksperimental"
    `evaluate` dapat menggunakan pemeriksaan berbasis aturan dan berbasis LLM, dan model pemeringkatan serta perilaku metadata-nya dapat berubah. Hindari memasukkannya ke dalam gerbang CI yang diwajibkan kecuali alur kerja Anda siap menghadapi perubahan.

Untuk pemeriksaan CI yang deterministik, gunakan `co-op-review` sebagai gantinya.