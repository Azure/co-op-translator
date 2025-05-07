<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-05-06T17:22:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tr"
}
-->
# Co-op Translator’a Katkıda Bulunma

Bu proje katkı ve önerilere açıktır. Çoğu katkı için, katkınızı kullanma hakkını bize verdiğinizi ve gerçekten verdiğinizi beyan eden bir Katkı Sağlayıcı Lisans Anlaşması’na (CLA) onay vermeniz gerekir. Detaylar için https://cla.opensource.microsoft.com adresini ziyaret edin.

Bir pull request (PR) gönderdiğinizde, bir CLA botu otomatik olarak CLA sağlamanız gerekip gerekmediğini belirler ve PR’ı uygun şekilde işaretler (örneğin, durum kontrolü, yorum). Botun verdiği talimatları takip etmeniz yeterlidir. Tüm CLA kullanan depolar için bunu yalnızca bir kez yapmanız yeterlidir.

## Geliştirme Ortamı Kurulumu

Bu projenin geliştirme ortamını kurmak için bağımlılıkları yönetmede Poetry kullanmanızı öneriyoruz. Proje bağımlılıklarını yönetmek için `pyproject.toml` kullanıyoruz; bu yüzden bağımlılıkları yüklemek için Poetry kullanmalısınız.

### Sanal Ortam Oluşturma

#### pip Kullanarak

```bash
python -m venv .venv
```

#### Poetry Kullanarak

```bash
poetry init
```

### Sanal Ortamı Aktifleştirme

#### pip ve Poetry için

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry Kullanarak

```bash
poetry shell
```

### Paket ve Gerekli Paketlerin Kurulumu

#### Poetry Kullanarak (pyproject.toml’dan)

```bash
poetry install
```

### Manuel Test

Bir PR göndermeden önce, çeviri işlevini gerçek dokümantasyonla test etmek önemlidir:

1. Kök dizinde bir test dizini oluşturun:
    ```bash
    mkdir test_docs
    ```

2. Çevirmek istediğiniz bazı markdown dokümantasyon ve resimleri test dizinine kopyalayın. Örneğin:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Paketi yerel olarak kurun:
    ```bash
    pip install -e .
    ```

4. Test belgelerinizde Co-op Translator’ı çalıştırın:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` dosyasındaki çevrilmiş dosyaları kontrol edin.
1. Ortam değişkenlerini verilen yönergelere göre doldurun.

> [!TIP]
>
> ### Ek geliştirme ortamı seçenekleri
>
> Projeyi yerel olarak çalıştırmanın yanı sıra, alternatif geliştirme ortamı kurulumu için GitHub Codespaces veya VS Code Dev Containers kullanabilirsiniz.
>
> #### GitHub Codespaces
>
> Bu örnekleri GitHub Codespaces kullanarak sanal ortamda çalıştırabilirsiniz; ek ayar veya kurulum gerekmez.
>
> Buton, tarayıcınızda web tabanlı bir VS Code örneği açacaktır:
>
> 1. Şablonu açın (birkaç dakika sürebilir):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers ile Yerelde Çalıştırma
>
> ⚠️ Bu seçenek, Docker Desktop’unuzda en az 16 GB RAM tahsis edilmişse çalışır. 16 GB RAM’den azsa, [GitHub Codespaces seçeneğini](../..) deneyebilir veya [yerelde kurulum yapabilirsiniz](../..).
>
> İlgili seçenek, projeyi yerel VS Code’da [Dev Containers uzantısı](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ile açan VS Code Dev Containers’dır:
>
> 1. Docker Desktop’u başlatın (yüklü değilse yükleyin)
> 2. Projeyi açın:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kod Stili

Projede tutarlı kod stili sağlamak için Python kod formatlayıcısı olarak [Black](https://github.com/psf/black) kullanıyoruz. Black, Python kodunu otomatik olarak Black kod stili kurallarına göre biçimlendiren tavizsiz bir formatlayıcıdır.

#### Yapılandırma

Black yapılandırması `pyproject.toml` dosyamızda belirtilmiştir:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black Kurulumu

Black’i Poetry (önerilen) veya pip ile kurabilirsiniz:

##### Poetry Kullanarak

Geliştirme ortamını kurduğunuzda Black otomatik olarak kurulur:
```bash
poetry install
```

##### pip Kullanarak

pip kullanıyorsanız, Black’i doğrudan kurabilirsiniz:
```bash
pip install black
```

#### Black Kullanımı

##### Poetry ile

1. Projedeki tüm Python dosyalarını biçimlendirin:
    ```bash
    poetry run black .
    ```

2. Belirli bir dosya veya dizini biçimlendirin:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip ile

1. Projedeki tüm Python dosyalarını biçimlendirin:
    ```bash
    black .
    ```

2. Belirli bir dosya veya dizini biçimlendirin:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Kodunuzu kaydederken Black ile otomatik biçimlendirme için editörünüzü yapılandırmanızı öneririz. Çoğu modern editör bunu eklentilerle destekler.

## Co-op Translator’ı Çalıştırma

Ortamınızda Poetry kullanarak Co-op Translator’ı çalıştırmak için şu adımları izleyin:

1. Çeviri testlerini yapmak istediğiniz dizine gidin veya test amaçlı geçici bir klasör oluşturun.

2. Aşağıdaki komutu çalıştırın. `-l ko` with the language code you wish to translate into. The `-d` bayrağı hata ayıklama modunu gösterir.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Komutu çalıştırmadan önce Poetry ortamınızın (poetry shell) aktif olduğundan emin olun.

## Bakımcılar

### Commit mesajı ve Birleştirme stratejisi

Projemizin commit geçmişinde tutarlılık ve netlik sağlamak için, **Squash and Merge** stratejisi kullanıldığında **son commit mesajı** için belirli bir format izliyoruz.

Bir pull request (PR) birleştirildiğinde, bireysel commit’ler tek bir commit’te birleştirilir. Temiz ve tutarlı bir geçmiş için son commit mesajı aşağıdaki formata uygun olmalıdır.

#### Commit mesajı formatı (squash and merge için)

Commit mesajları için şu formatı kullanıyoruz:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Commit kategorisini belirtir. Aşağıdaki tipleri kullanıyoruz:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.