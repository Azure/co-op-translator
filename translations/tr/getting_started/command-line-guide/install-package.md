<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:11:14+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "tr"
}
-->
# Co-op translator paketini yükleyin

**Co-op Translator**, projenizdeki tüm markdown dosyalarını ve görselleri birden fazla dile çevirmek için tasarlanmış bir komut satırı arayüzü (CLI) aracıdır. Bu eğitimde, çeviriciyi nasıl yapılandıracağınızı ve farklı kullanım senaryoları için nasıl çalıştıracağınızı öğreneceksiniz.

### Sanal ortam oluşturun

Sanal ortamı `pip` veya `Poetry` kullanarak oluşturabilirsiniz. Terminalinizde aşağıdaki komutlardan birini yazın.

#### pip ile

```bash
python -m venv .venv
```

#### Poetry ile

```bash
poetry init
```

### Sanal ortamı etkinleştirin

Sanal ortamı oluşturduktan sonra etkinleştirmeniz gerekir. Adımlar işletim sisteminize göre değişir. Terminalinizde aşağıdaki komutu yazın.

#### Hem pip hem de Poetry için

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry ile

1. Ortamı Poetry ile oluşturduysanız, etkinleştirmek için terminalinizde aşağıdaki komutu yazın.

    ```bash
    poetry shell
    ```

### Paketi ve gerekli paketleri yükleme

Sanal ortamınızı kurup etkinleştirdikten sonra, gerekli bağımlılıkları yüklemeniz gerekir.

### Hızlı kurulum

Co-Op Translator'ı pip ile yükleyin

```
pip install co-op-translator
```
Ya da 

Poetry ile yükleyin
```
poetry add co-op-translator
```

#### Bu repoyu klonladıysanız pip ile (requirements.txt üzerinden) 

> [!NOTE]
> Hızlı kurulum ile co-op translator yüklediyseniz lütfen bunu yapmayın.

1. pip kullanıyorsanız, terminalinizde aşağıdaki komutu yazın. Bu komut, `requirements.txt` dosyasında belirtilen gerekli paketleri otomatik olarak yükler:

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry ile (pyproject.toml üzerinden)

1. Poetry kullanıyorsanız, terminalinizde aşağıdaki komutu yazın. Bu komut, `pyproject.toml` dosyasında belirtilen gerekli paketleri otomatik olarak yükler:

    ```bash
    poetry install
    ```

---

**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar olabileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.