<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:09:32+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tr"
}
-->
# Co-op Translator'a Katkıda Bulunmak

Bu projeye katkı ve önerileriniz memnuniyetle karşılanır. Çoğu katkı için, bize katkınızın haklarını kullanma izni verdiğinizi ve bu haklara sahip olduğunuzu beyan eden bir Katkı Sağlayıcı Lisans Sözleşmesi (CLA) kabul etmeniz gerekir. Detaylar için https://cla.opensource.microsoft.com adresini ziyaret edebilirsiniz.

Bir pull request gönderdiğinizde, bir CLA botu otomatik olarak CLA gerekip gerekmediğini belirler ve PR'ı uygun şekilde işaretler (örneğin, durum kontrolü, yorum). Botun verdiği talimatları takip etmeniz yeterlidir. Bunu, CLA kullanan tüm repolarda yalnızca bir kez yapmanız gerekir.

## Geliştirme ortamı kurulumu

Bu proje için geliştirme ortamını kurarken, bağımlılık yönetimi için Poetry kullanmanızı öneriyoruz. Proje bağımlılıklarını yönetmek için `pyproject.toml` dosyasını kullanıyoruz, bu nedenle bağımlılıkları yüklemek için Poetry kullanmalısınız.

### Sanal ortam oluşturma

#### pip ile

```bash
python -m venv .venv
```

#### Poetry ile

```bash
poetry init
```

### Sanal ortamı etkinleştirme

#### Hem pip hem de Poetry için

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry ile

```bash
poetry shell
```

### Paketi ve gerekli paketleri yükleme

#### Poetry ile (pyproject.toml'dan)

```bash
poetry install
```

### Manuel test

PR göndermeden önce, çeviri işlevini gerçek dokümantasyonla test etmek önemlidir:

1. Kök dizinde bir test klasörü oluşturun:
    ```bash
    mkdir test_docs
    ```

2. Çevirmek istediğiniz bazı markdown dokümanlarını ve görselleri test klasörüne kopyalayın. Örneğin:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Paketi yerel olarak yükleyin:
    ```bash
    pip install -e .
    ```

4. Test belgelerinizde Co-op Translator'ı çalıştırın:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` ve `test_docs/translated_images` klasörlerindeki çevrilmiş dosyaları kontrol edin ve şunları doğrulayın:
   - Çeviri kalitesi
   - Meta veri yorumlarının doğruluğu
   - Orijinal markdown yapısının korunması
   - Bağlantıların ve görsellerin düzgün çalışması

Bu manuel test, yaptığınız değişikliklerin gerçek dünyada sorunsuz çalıştığından emin olmanıza yardımcı olur.

### Ortam değişkenleri

1. Kök dizinde, sağlanan `.env.template` dosyasını kopyalayarak bir `.env` dosyası oluşturun.
1. Ortam değişkenlerini yönergeler doğrultusunda doldurun.

> [!TIP]
>
> ### Ek geliştirme ortamı seçenekleri
>
> Projeyi yerel olarak çalıştırmanın yanı sıra, alternatif geliştirme ortamı olarak GitHub Codespaces veya VS Code Dev Containers da kullanabilirsiniz.
>
> #### GitHub Codespaces
>
> Bu örnekleri GitHub Codespaces ile sanal olarak çalıştırabilirsiniz ve ek bir ayar veya kurulum gerekmez.
>
> Buton, tarayıcınızda web tabanlı bir VS Code oturumu açacaktır:
>
> 1. Şablonu açın (bu birkaç dakika sürebilir):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Yerel olarak VS Code Dev Containers ile çalıştırma
>
> ⚠️ Bu seçenek yalnızca Docker Desktop en az 16 GB RAM'e ayrılmışsa çalışır. 16 GB'tan az RAM'iniz varsa [GitHub Codespaces seçeneğini](../..) veya [yerel kurulum](../..) yöntemini deneyebilirsiniz.
>
> İlgili bir seçenek de VS Code Dev Containers'dır; proje, [Dev Containers uzantısı](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ile yerel VS Code'unuzda açılır:
>
> 1. Docker Desktop'ı başlatın (yüklü değilse yükleyin)
> 2. Projeyi açın:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kod Stili

Projede tutarlı bir kod stili sağlamak için Python kod biçimlendiricisi olarak [Black](https://github.com/psf/black) kullanıyoruz. Black, Python kodunu otomatik olarak kendi kod stiline uygun şekilde biçimlendirir.

#### Yapılandırma

Black yapılandırması `pyproject.toml` dosyamızda belirtilmiştir:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black'i yükleme

Black'i Poetry (önerilen) veya pip ile yükleyebilirsiniz:

##### Poetry ile

Geliştirme ortamını kurduğunuzda Black otomatik olarak yüklenir:
```bash
poetry install
```

##### pip ile

pip kullanıyorsanız Black'i doğrudan yükleyebilirsiniz:
```bash
pip install black
```

#### Black kullanımı

##### Poetry ile

1. Projedeki tüm Python dosyalarını biçimlendirin:
    ```bash
    poetry run black .
    ```

2. Belirli bir dosya veya klasörü biçimlendirin:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip ile

1. Projedeki tüm Python dosyalarını biçimlendirin:
    ```bash
    black .
    ```

2. Belirli bir dosya veya klasörü biçimlendirin:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Kodunuzu kaydederken Black ile otomatik biçimlendirme için editörünüzü ayarlamanızı öneririz. Çoğu modern editör bunu eklenti veya uzantılarla destekler.

## Co-op Translator'ı Çalıştırmak

Poetry ile Co-op Translator'ı ortamınızda çalıştırmak için şu adımları izleyin:

1. Çeviri testleri yapmak istediğiniz dizine gidin veya test amaçlı geçici bir klasör oluşturun.

2. Aşağıdaki komutu çalıştırın. `-l ko` kısmını çevirmek istediğiniz dil kodu ile değiştirin. `-d` bayrağı debug modunu belirtir.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Komutu çalıştırmadan önce Poetry ortamınızın etkin olduğundan emin olun (poetry shell).

## Yeni bir dil eklemek için katkı

Yeni dillerin eklenmesini memnuniyetle karşılıyoruz. PR açmadan önce aşağıdaki adımları tamamlayarak inceleme sürecinin sorunsuz olmasını sağlayın.

1. Dili font eşlemesine ekleyin
   - `src/co_op_translator/fonts/font_language_mappings.yml` dosyasını düzenleyin
   - Şu bilgileri ekleyin:
     - `code`: ISO benzeri dil kodu (ör. `vi`)
     - `name`: İnsan dostu görünen ad
     - `font`: İlgili yazıyı destekleyen ve `src/co_op_translator/fonts/` içinde bulunan bir font
     - `rtl`: Sağdan sola ise `true`, değilse `false`

2. Gerekli font dosyalarını ekleyin (gerekiyorsa)
   - Yeni bir font gerekiyorsa, açık kaynak dağıtımı için lisans uyumluluğunu doğrulayın
   - Font dosyasını `src/co_op_translator/fonts/` klasörüne ekleyin

3. Yerel doğrulama
   - Küçük bir örnek üzerinde çeviri çalıştırın (Markdown, görseller ve uygun ise notebooklar)
   - Çıktının doğru şekilde göründüğünü doğrulayın; fontlar ve varsa RTL düzeni dahil

4. Dokümantasyonu güncelleyin
   - Dilin `getting_started/supported-languages.md` dosyasında göründüğünden emin olun
   - `README_languages_template.md` dosyasında değişiklik yapmanıza gerek yoktur; bu dosya desteklenen listeye göre oluşturulur

5. PR açın
   - Eklediğiniz dili ve varsa font/lisans ile ilgili hususları açıklayın
   - Mümkünse çıktıların ekran görüntülerini ekleyin

Örnek YAML girişi:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Sürdürücüler

### Commit mesajı ve Birleştirme stratejisi

Proje commit geçmişimizin tutarlı ve anlaşılır olması için, **Squash and Merge** stratejisi kullanılırken **son commit mesajı** için belirli bir format izliyoruz.

Bir pull request (PR) birleştirildiğinde, bireysel commitler tek bir committe birleştirilir. Son commit mesajı, temiz ve tutarlı bir geçmiş için aşağıdaki formata uygun olmalıdır.

#### Commit mesajı formatı (squash and merge için)

Commit mesajlarında şu formatı kullanıyoruz:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Commitin kategorisini belirtir. Şu türleri kullanıyoruz:
  - `Docs`: Dokümantasyon güncellemeleri için.
  - `Build`: Derleme sistemi veya bağımlılıklar ile ilgili değişiklikler için; yapılandırma dosyaları, CI iş akışları veya Dockerfile güncellemeleri dahil.
  - `Core`: Projenin temel işlevselliği veya özellikleriyle ilgili değişiklikler için; özellikle `src/co_op_translator/core` dizinindeki dosyalar.

- **description**: Değişikliğin kısa özeti.
- **PR number**: Commit ile ilişkili pull request numarası.

**Örnekler**:

- `Docs: Kurulum talimatlarını daha anlaşılır hale getir (#50)`
- `Core: Görsel çevirisinde iyileştirme yapıldı (#60)`

> [!NOTE]
> Şu anda **`Docs`**, **`Core`** ve **`Build`** önekleri, değiştirilen kaynak koduna uygulanan etiketlere göre PR başlıklarına otomatik olarak eklenir. Doğru etiket uygulandığı sürece genellikle PR başlığını manuel olarak güncellemenize gerek yoktur. Sadece her şeyin doğru olduğundan ve önekin uygun şekilde oluşturulduğundan emin olmanız gerekir.

#### Birleştirme stratejisi

Pull requestler için varsayılan stratejimiz **Squash and Merge**'dir. Bu strateji, commit mesajlarının formatımıza uygun olmasını sağlar; bireysel commitler uygun olmasa bile.

**Nedenler**:

- Temiz, doğrusal bir proje geçmişi.
- Commit mesajlarında tutarlılık.
- Küçük commitlerden (ör. "düzeltme yazım hatası") kaynaklanan gereksiz karmaşanın azalması.

Birleştirirken, son commit mesajının yukarıda açıklanan formata uygun olduğundan emin olun.

**Squash and Merge örneği**
Bir PR şu commitleri içeriyorsa:

- `fix typo`
- `update README`
- `adjust formatting`

Şu şekilde birleştirilmelidir:
`Docs: Dokümantasyonun açıklığı ve biçimlendirmesi iyileştirildi (#65)`

---

**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar olabileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.