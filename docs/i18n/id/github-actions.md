# GitHub Actions

Gunakan GitHub Actions ketika Anda ingin sebuah repositori menerjemahkan dokumentasi yang diubah secara otomatis dan membuka pull request dengan keluaran yang dihasilkan.

Mulailah dengan pengaturan standar `GITHUB_TOKEN`, termasuk untuk repositori organisasi jika kebijakan mengizinkannya. Lihat [GitHub App Setup](#github-app-setup) jika organisasi Anda mengharuskan identitas App atau Anda membutuhkan jalannya workflow downstream otomatis.

**Suntingan manusia:** workflow ini menerjemahkan ulang file sumber yang diubah secara penuh dan dapat menimpa redaksi yang telah disunting dalam terjemahannya. Tinjau setiap PR sebelum digabung. Pelestarian tingkat-blok Markdown untuk suntingan yang diterima memerlukan integrasi khusus dengan [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## PR terjemahan README pertama Anda

Mulailah dengan satu berkas root `README.md` dan satu bahasa target. Workflow ini menerjemahkan hanya Markdown, jadi Azure AI Vision tidak diperlukan.

1. Salin [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([lihat template di GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) ke `.github/workflows/translate-readme.yml` di repositori yang ingin Anda terjemahkan, lalu commit ke cabang default repositori tersebut. Template menggunakan root Action di `Azure/co-op-translator@main`, yang menginstal CLI dari referensi sumber yang sama. Pin commit yang telah ditinjau untuk menjalankan yang dapat direproduksi.
2. Buka **Actions > Translate README > Run workflow**, pilih bahasa, dan biarkan **Preview only** tercentang. Tinjau estimasi token pada langkah pratinjau. Pratinjau tidak memanggil penyedia model, menulis terjemahan, atau membuat PR.
3. Tambahkan secret untuk satu [penyedia teks](#prerequisites), dan aktifkan **Izinkan GitHub Actions untuk membuat dan menyetujui pull request** di bawah **Pengaturan > Actions > Umum**. Template meminta `contents: write` dan `pull-requests: write` untuk job-nya; Anda tidak perlu mengubah izin default untuk setiap alur kerja. Jika kebijakan organisasi memblokir izin atau pengaturan ini, tanyakan kepada administrator tentang [Aplikasi GitHub](#github-app-setup) yang disetujui.
4. Jalankan workflow lagi dengan **Preview only** tidak dicentang. Workflow menampilkan pratinjau, menerjemahkan, menjalankan `co-op-review --readme-only`, dan membuat atau memperbarui PR terjemahan hanya setelah terjemahan dan peninjauan berhasil. Ringkasan workflow menautkan ke PR.
5. Tinjau redaksi dan perubahan berkas dalam PR, lalu merge ketika siap. Workflow tidak menggabungkan secara otomatis.

PR hanya berisi `translations/<language>/README.md` dan berkas metadata bahasanya. README sumber tetap tidak berubah, dan tautan ke dokumen lain tetap menunjuk pada dokumen sumber. Isi PR mencantumkan berkas yang berubah dan hasil peninjauan struktural. Jika terjemahan atau peninjauan gagal, periksa ringkasan workflow dan log langkah yang gagal; tidak ada PR yang dibuat. Jika tidak ada perubahan, tidak diperlukan PR baru.

**Catatan Organisasi dan CI:** GitHub App bersifat opsional, bukan persyaratan kepemilikan organisasi. Dengan `GITHUB_TOKEN`, workflow pull-request untuk membuka, memperbarui, atau membuka kembali PR memerlukan pengguna dengan akses tulis untuk memilih **Approve workflows to run**. Workflow push tidak dipicu oleh token ini. Untuk CI downstream tanpa pengawasan, lihat [GitHub App Setup](#github-app-setup) dan GitHub's [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow).

## Prasyarat

Sebelum membuat workflow, konfigurasikan secret layanan AI yang diperlukan oleh proses terjemahan Anda.

Terjemahan teks membutuhkan satu penyedia model bahasa:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

Terjemahan gambar juga memerlukan Azure AI Vision:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

Lihat [Configuration](configuration.md) dan [Azure AI Setup](azure-ai-setup.md) untuk detail konfigurasi lokal.

## Pengaturan Standar

Setelah mencoba workflow README, gunakan pengaturan ini untuk menerjemahkan berkas Markdown repositori ke beberapa bahasa. Ia menjalankan peninjauan Markdown sebelum membuka PR dan tidak memerlukan Azure AI Vision.

### Langkah 1: Tambahkan Secret Repositori

Di repositori target Anda, buka **Settings** > **Secrets and variables** > **Actions**, lalu tambahkan secret penyedia yang akan digunakan workflow Anda.

![Pilih secret Actions](../../assets/github-actions/select-setting-action.png)

### Langkah 2: Aktifkan Izin Workflow

Buka **Settings** > **Actions** > **General**.

Di bawah **Workflow permissions**:

1. Aktifkan **Izinkan GitHub Actions untuk membuat dan menyetujui pull request**.
2. Simpan pengaturan.

Job di bawah meminta `contents: write` dan `pull-requests: write` secara eksplisit. Biarkan permission workflow default repositori tidak berubah. Jika kebijakan organisasi memblokir pembuatan PR, tanyakan kepada administrator tentang sebuah [GitHub App](#github-app-setup) yang disetujui.

### Langkah 3: Tambahkan Workflow

Buat `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

Ubah `TARGET_LANGUAGES` ke bahasa yang dibutuhkan proyek Anda. Peninjauan menggunakan Python API untuk memeriksa hanya Markdown, sesuai dengan langkah terjemahan. Kesalahan terjemahan atau peninjauan menghentikan job sebelum pembuatan PR. Workflow tidak menggabungkan PR secara otomatis. Untuk repositori besar, tambahkan filter `paths:` di bawah `on.push` sehingga workflow hanya berjalan saat dokumentasi berubah.

### Opsional: notebook dan gambar

Untuk notebook, tambahkan `-nb` ke perintah terjemahan dan set `notebook=True` pada langkah peninjauan. Untuk teks gambar, konfigurasikan dua [Azure AI Vision secrets](#prerequisites), teruskan keduanya di `env` langkah terjemahan, tambahkan `-img` ke perintah, dan tambahkan `translated_images/` ke `add-paths` langkah PR. Tinjau gambar terjemahan secara visual; peninjauan deterministik tidak menjamin teks gambar atau akurasi linguistik.

## Pengaturan GitHub App

Gunakan GitHub App yang disetujui ketika organisasi Anda mengharuskan identitas App, atau ketika PR yang dihasilkan perlu memicu CI downstream tanpa langkah persetujuan `GITHUB_TOKEN`. Sebuah App tidak mem-bypass kebijakan organisasi; administrator tetap mengendalikan instalasi dan izinnya.

### Langkah 1: Buat atau Pasang GitHub App

Gunakan App yang disediakan organisasi jika tersedia, atau buat satu dengan akses baca/tulis ke **Contents** dan **Pull requests**. Pasang di repositori target dengan persetujuan organisasi jika diperlukan.

Catat:

- App ID
- Isi private key

Simpan sebagai secret repositori:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### Langkah 2: Hasilkan Token App

Tambahkan langkah ini tepat sebelum langkah pull request yang sudah ada. Untuk template README, gunakan kondisi sukses yang sama sehingga pratinjau dan terjemahan yang gagal tidak meminta token App:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

Lalu ubah hanya input `token` pada langkah pull request yang ada menjadi `${{ steps.generate_token.outputs.token }}`. Biarkan kondisi sukses, branch, isi PR, dan `add-paths` tidak berubah. Token ini secara default dibatasi ke repositori saat ini. Saat menyesuaikan pengaturan standar alih-alih template README, hilangkan `if` di atas: workflow tersebut menggunakan kondisi sukses default, jadi pembuatan token dan pembuatan PR berjalan hanya setelah terjemahan dan peninjauan berhasil.

Lihat [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) resmi untuk instalasi dan izin token.

## Batasan Runner

Runner yang di-host GitHub memiliki durasi job maksimum. Repositori besar atau banyak bahasa target dapat melebihi batas tersebut.

Untuk beban kerja terjemahan besar:

- Terjemahkan lebih sedikit bahasa per run.
- Gunakan flag konten seperti `-md`, `-nb`, atau `-img`.
- Gunakan runner self-hosted ketika ukuran repositori atau latensi model membuat runner yang di-host tidak dapat diandalkan.

## Peninjauan di CI

Gunakan `co-op-review` ketika sebuah pull request harus memvalidasi terjemahan yang dihasilkan tanpa memanggil penyedia LLM atau Vision.

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` adalah perintah peninjauan deterministik beta. Pemeriksaan dan skema keluaran dapat berkembang, tetapi dirancang aman untuk CI karena tidak menulis berkas atau memanggil penyedia model.