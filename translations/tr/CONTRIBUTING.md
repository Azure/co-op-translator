<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:05:54+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tr"
}
-->
# Co-op Translator'a Katkıda Bulunma

Bu proje katkılara ve önerilere açıktır. Çoğu katkı için, katkınızı kullanma haklarını bize verdiğinizi beyan eden bir Katkıda Bulunan Lisans Sözleşmesi'ni (CLA) kabul etmeniz gerekir. Detaylar için https://cla.opensource.microsoft.com adresini ziyaret edin.

Bir pull request (PR) gönderdiğinizde, bir CLA botu otomatik olarak CLA sağlamanız gerekip gerekmediğini belirler ve PR'ı uygun şekilde işaretler (örneğin, durum kontrolü, yorum). Botun verdiği talimatları takip etmeniz yeterlidir. CLA'yı kullanan tüm depolarda bunu yalnızca bir kez yapmanız gerekir.

## Geliştirme Ortamı Kurulumu

Bu proje için geliştirme ortamını kurarken bağımlılıkları yönetmek için Poetry kullanmanızı öneririz. Proje bağımlılıklarını `pyproject.toml` dosyası ile yönetiyoruz, bu nedenle bağımlılıkları yüklemek için Poetry kullanmalısınız.

### Sanal Ortam Oluşturma

#### pip kullanarak

```bash
python -m venv .venv
```

#### Poetry kullanarak

```bash
poetry init
```

### Sanal Ortamı Aktifleştirme

#### pip ve Poetry için ortak

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry kullanarak

```bash
poetry shell
```

### Paket ve Gerekli Paketlerin Kurulumu

#### Poetry kullanarak (pyproject.toml'dan)

```bash
poetry install
```

### Manuel Test

Bir PR göndermeden önce, çeviri işlevselliğini gerçek dokümantasyonla test etmek önemlidir:

1. Kök dizinde bir test dizini oluşturun:
    ```bash
    mkdir test_docs
    ```

2. Çevirmek istediğiniz bazı markdown dokümanları ve resimleri test dizinine kopyalayın. Örneğin:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Paketi yerel olarak kurun:
    ```bash
    pip install -e .
    ```

4. Test belgelerinizde Co-op Translator'ı çalıştırın:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` ve `test_docs/translated_images` içindeki çevrilmiş dosyaları kontrol edin:
   - Çeviri kalitesi
   - Meta veri yorumlarının doğruluğu
   - Orijinal markdown yapısının korunması
   - Bağlantılar ve resimlerin düzgün çalışması

Bu manuel test, değişikliklerinizin gerçek dünya senaryolarında iyi çalıştığını garanti etmeye yardımcı olur.

### Ortam Değişkenleri

1. Kök dizinde `.env.template` dosyasını kopyalayarak `.env` dosyası oluşturun.
2. Ortam değişkenlerini verilen yönergelere göre doldurun.

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
> #### VS Code Dev Containers ile Yerel Çalıştırma
>
> ⚠️ Bu seçenek, Docker Desktop'unuzda en az 16 GB RAM ayrılmışsa çalışır. 16 GB'den az RAM varsa, [GitHub Codespaces seçeneğini](../..) deneyebilir veya [yerel kurulum yapabilirsiniz](../..).
>
> İlgili bir seçenek, projeyi yerel VS Code'da [Dev Containers uzantısı](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ile açan VS Code Dev Containers'dır:
>
> 1. Docker Desktop'u başlatın (yüklü değilse yükleyin)
> 2. Projeyi açın:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kod Stili

Projede tutarlı kod stili sağlamak için Python kod biçimlendiricisi olarak [Black](https://github.com/psf/black) kullanıyoruz. Black, Python kodunu otomatik olarak Black kod stiline uygun şekilde yeniden biçimlendiren tavizsiz bir biçimlendiricidir.

#### Konfigürasyon

Black konfigürasyonu `pyproject.toml` dosyamızda belirtilmiştir:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black Kurulumu

Black'i Poetry (önerilen) veya pip ile kurabilirsiniz:

##### Poetry kullanarak

Geliştirme ortamını kurduğunuzda Black otomatik olarak kurulur:
```bash
poetry install
```

##### pip kullanarak

pip kullanıyorsanız, Black'i doğrudan kurabilirsiniz:
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
> Kodunuzu kaydederken otomatik olarak Black ile biçimlendirmek için editörünüzü yapılandırmanızı öneririz. Çoğu modern editör bunu eklentiler veya uzantılar aracılığıyla destekler.

## Co-op Translator'ı Çalıştırma

Ortamınızda Poetry kullanarak Co-op Translator'ı çalıştırmak için şu adımları izleyin:

1. Çeviri testlerini yapmak istediğiniz dizine gidin veya test amaçlı geçici bir klasör oluşturun.

2. Aşağıdaki komutu çalıştırın. `-l ko` kısmını çevirmek istediğiniz dil kodu ile değiştirin. `-d` bayrağı hata ayıklama modunu belirtir.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Komutu çalıştırmadan önce Poetry ortamınızın aktif olduğundan emin olun (poetry shell).

## Yeni Bir Dil Katkısı

Yeni dillerin desteklenmesi için katkılarınızı memnuniyetle karşılıyoruz. PR açmadan önce sorunsuz bir inceleme için aşağıdaki adımları tamamlayın.

1. Dili font eşlemesine ekleyin
   - `src/co_op_translator/fonts/font_language_mappings.yml` dosyasını düzenleyin
   - Şu bilgileri içeren bir giriş ekleyin:
     - `code`: ISO benzeri dil kodu (örneğin, `vi`)
     - `name`: İnsan tarafından okunabilir gösterim adı
     - `font`: `src/co_op_translator/fonts/` içinde bulunan ve yazı tipini destekleyen bir font
     - `rtl`: Sağdan sola yazılan diller için `true`, aksi halde `false`

2. Gerekli font dosyalarını ekleyin (gerekirse)
   - Yeni bir font gerekiyorsa, açık kaynak dağıtımı için lisans uyumluluğunu doğrulayın
   - Font dosyasını `src/co_op_translator/fonts/` dizinine ekleyin

3. Yerel doğrulama
   - Küçük bir örnek üzerinde (Markdown, resimler ve notebooklar uygun şekilde) çevirileri çalıştırın
   - Çıktının doğru şekilde render edildiğini, fontların ve varsa RTL düzeninin düzgün olduğunu doğrulayın

4. Dokümantasyonu güncelleyin
   - Dili `getting_started/supported-languages.md` dosyasında görünür hale getirin
   - `getting_started/README_languages_template.md` dosyasında değişiklik yapmanıza gerek yoktur; bu dosya desteklenen diller listesinden otomatik oluşturulur

5. PR açın
   - Eklenen dili ve varsa font/lisanslama ile ilgili bilgileri açıklayın
   - Mümkünse render edilmiş çıktıların ekran görüntülerini ekleyin

Örnek YAML girişi:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Yeni Dili Test Etme

Yeni dili aşağıdaki komutu çalıştırarak test edebilirsiniz:

```bash
# Sanal bir ortam oluşturun ve etkinleştirin
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Geliştirme paketini yükleyin
pip install -e .
# Çeviriyi çalıştırın
translate -l "new_lang"
```

## Bakımcılar

### Commit Mesajı ve Birleştirme Stratejisi

Projemizin commit geçmişinde tutarlılık ve açıklık sağlamak için, **Squash and Merge** stratejisi kullanıldığında **son commit mesajı** için belirli bir format izliyoruz.

Bir pull request (PR) birleştirildiğinde, bireysel commitler tek bir committe birleştirilir. Son commit mesajı, temiz ve tutarlı bir geçmiş için aşağıdaki formatta olmalıdır.

#### Commit mesajı formatı (squash and merge için)

Commit mesajları için kullandığımız format:

```bash
<type>: <description> (#<PR numarası>)
```

- **type**: Commit kategorisini belirtir. Aşağıdaki tipleri kullanıyoruz:
  - `Docs`: Dokümantasyon güncellemeleri için.
  - `Build`: Yapı sistemi veya bağımlılıklar ile ilgili değişiklikler için; yapılandırma dosyaları, CI iş akışları veya Dockerfile güncellemeleri dahil.
  - `Core`: Projenin temel işlevselliği veya özellikleri ile ilgili değişiklikler için, özellikle `src/co_op_translator/core` dizinindeki dosyalar.

- **description**: Değişikliğin kısa özeti.
- **PR numarası**: Commit ile ilişkili pull request numarası.

**Örnekler**:

- `Docs: Kurulum talimatları güncellendi (#50)`
- `Core: Resim çevirisi işleyişi geliştirildi (#60)`

> [!NOTE]
> Şu anda, **`Docs`**, **`Core`** ve **`Build`** önekleri, değiştirilen kaynak koduna uygulanan etiketlere göre PR başlıklarına otomatik eklenmektedir. Doğru etiket uygulandığı sürece, genellikle PR başlığını manuel olarak güncellemeniz gerekmez. Sadece her şeyin doğru ve önekin uygun şekilde oluşturulduğunu kontrol etmeniz yeterlidir.

#### Birleştirme Stratejisi

Pull requestler için varsayılan stratejimiz **Squash and Merge**'dir. Bu strateji, bireysel commitler uygun formatta olmasa bile commit mesajlarının formatımıza uygun olmasını sağlar.

**Nedenleri**:

- Temiz, doğrusal bir proje geçmişi.
- Commit mesajlarında tutarlılık.
- Küçük commitlerden (örneğin, "yazım hatası düzeltme") kaynaklanan gürültünün azaltılması.

Birleştirirken, son commit mesajının yukarıda belirtilen commit mesajı formatına uygun olduğundan emin olun.

**Squash and Merge örneği**  
Bir PR aşağıdaki commitleri içeriyorsa:

- `fix typo`
- `update README`
- `adjust formatting`

Bunlar şu şekilde birleştirilmelidir:  
`Docs: Dokümantasyonun açıklığı ve biçimlendirmesi iyileştirildi (#65)`

### Sürüm Yayınlama Süreci

Bu bölüm, bakımcıların Co-op Translator için yeni bir sürüm yayınlamasının en basit yolunu açıklar.

#### 1. `pyproject.toml` dosyasındaki sürümü artırma

1. Bir sonraki sürüm numarasına karar verin (semantik sürümlemeyi takip ediyoruz: `MAJOR.MINOR.PATCH`).
2. `pyproject.toml` dosyasını açın ve `[tool.poetry]` altındaki `version` alanını güncelleyin.
3. Sadece sürüm numarasını (ve varsa otomatik güncellenen kilit/meta dosyalarını) değiştiren özel bir pull request açın.
4. İnceleme sonrası, **Squash and Merge** kullanarak birleştirin ve son commit mesajının yukarıda belirtilen formata uygun olduğundan emin olun.

#### 2. GitHub Sürümü Oluşturma

1. GitHub depo sayfasına gidin ve **Releases** → **Draft a new release** seçeneğini açın.
2. `main` dalından yeni bir etiket oluşturun (örneğin, `v0.13.0`).
3. Sürüm başlığını aynı sürüm numarası olarak ayarlayın (örneğin, `v0.13.0`).
4. Değişiklik günlüğünü otomatik doldurmak için **Generate release notes** butonuna tıklayın.
5. İsterseniz metni düzenleyin (örneğin, yeni desteklenen dilleri veya önemli değişiklikleri vurgulamak için).
6. Sürümü yayınlayın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->