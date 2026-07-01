# Pemecahan Masalah

Gunakan halaman ini ketika proses terjemahan berhasil secara tak terduga, gagal selama konfigurasi, atau menghasilkan keluaran yang perlu ditinjau.

## Mulai Di Sini

1. Jalankan perintah fokus terlebih dahulu, seperti `translate -l "ko" -md`.
2. Tambahkan `-d` untuk log debug konsol.
3. Tambahkan `-s` untuk menyimpan log debug di bawah `<root-dir>/logs/`.
4. Jalankan `co-op-review` setelah terjemahan untuk memeriksa kebaruan, struktur, dan tautan lokal.

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

- Konfigurasikan Azure OpenAI atau OpenAI.
- Verifikasi variabel berada di lingkungan tempat perintah dijalankan.
- Untuk penggunaan lokal, taruh di `.env` di root proyek.

Lihat [Konfigurasi](configuration.md).

### Terjemahan Gambar Tanpa Azure AI Vision

Kesalahan:

```text
Image translation requested but Azure AI Service is not configured.
```

Perbaikan:

- Tambahkan `AZURE_AI_SERVICE_API_KEY`.
- Tambahkan `AZURE_AI_SERVICE_ENDPOINT`.
- Atau jalankan perintah hanya-teks seperti `translate -l "ko" -md`.

### Kunci atau Endpoint Tidak Valid

Gejalanya bisa termasuk `401`, kesalahan izin yang disamarkan, atau kesalahan akses endpoint.

Perbaikan:

- Konfirmasi kunci milik sumber daya Azure yang sama dengan endpoint.
- Konfirmasi sumber daya mendukung Vision saat menggunakan `-img`.
- Konfirmasi nama deployment Azure OpenAI dan versi API cocok dengan deployment Anda.
- Jalankan dengan log debug: `translate -l "ko" -md -d -s`.

## Tidak Ada File yang Diterjemahkan

Penyebab umum:

- Flag yang dipilih tidak cocok dengan file Anda.
- File terjemahan yang ada sudah ada.
- File sumber berada di bawah direktori yang dikecualikan.
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

- `-nb` disertakan: tautan notebook dapat mengarah ke notebook yang diterjemahkan.
- `-nb` dikecualikan: tautan notebook dapat tetap mengarah ke notebook sumber.
- `-img` disertakan: tautan gambar dapat mengarah ke gambar yang diterjemahkan.
- `-img` dikecualikan: tautan gambar dapat tetap mengarah ke gambar sumber.

Jalankan terjemahan konten penuh ketika semua tautan internal harus memilih keluaran terjemahan:

```bash
translate -l "ko" -md -nb -img
```

Jalankan tinjauan tautan setelah terjemahan:

```bash
co-op-review -l "ko"
```

## Masalah Perenderan Markdown

Jika Markdown yang diterjemahkan dirender tidak benar:

- Periksa bahwa frontmatter dimulai dan diakhiri dengan `---`.
- Periksa bahwa jumlah pembatas kode cocok antara file sumber dan terjemahan.
- Jalankan `co-op-review` untuk menangkap masalah struktur umum.
- Terjemahkan ulang file tertentu jika keluaran rusak.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Berjalan tetapi Tidak Ada Pull Request yang Dibuat

Jika `peter-evans/create-pull-request` melaporkan bahwa cabang tidak lebih maju dari base, workflow tidak menemukan file untuk dikomit.

Kemungkinan penyebab:

- Proses terjemahan tidak menghasilkan perubahan.
- `.gitignore` mengecualikan `translations/`, `translated_images/`, atau notebook yang diterjemahkan.
- `add-paths` tidak cocok dengan direktori keluaran yang dihasilkan.
- Langkah terjemahan keluar lebih awal.

Perbaikan:

1. Konfirmasi file yang dihasilkan ada di `translations/` atau `translated_images/`.
2. Konfirmasi `.gitignore` tidak mengabaikan keluaran yang dihasilkan.
3. Gunakan `add-paths` yang cocok:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Secara sementara tambahkan flag debug ke perintah translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Konfirmasi izin workflow mencakup:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kualitas Terjemahan

Terjemahan mesin mungkin memerlukan tinjauan manusia. Gunakan `evaluate` hanya ketika Anda menginginkan pemeringkatan kualitas eksperimental dan alur kerja perbaikan dengan keyakinan rendah.

!!! warning "Experimental"
    `evaluate` dapat menggunakan pemeriksaan berbasis aturan dan berbasis LLM, dan model pemeringkatan serta perilaku metadata-nya dapat berubah. Jangan masukkan ke dalam gate CI yang diwajibkan kecuali alur kerja Anda siap menghadapi perubahan.

Untuk pemeriksaan CI yang deterministik, gunakan `co-op-review` sebagai gantinya.