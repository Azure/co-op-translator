<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:34:28+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "tr"
}
-->
# Co-op çevirmen paketini kurma

**Co-op Translator**, projenizdeki tüm markdown dosyalarını ve görselleri birden fazla dile çevirmeye yardımcı olan bir komut satırı arayüzü (CLI) aracıdır. Bu rehber, çevirmeni yapılandırmanızı ve farklı kullanım senaryoları için çalıştırmanızı adım adım gösterecektir.

### Sanal ortam oluşturma

Sanal ortamı `pip` veya `Poetry` kullanarak oluşturabilirsiniz. Terminalinize aşağıdaki komutlardan birini yazın.

#### pip kullanarak

```bash
python -m venv .venv
```

#### Poetry kullanarak

```bash
poetry init
```

### Sanal ortamı etkinleştirme

Sanal ortamı oluşturduktan sonra etkinleştirmeniz gerekir. İşletim sisteminize göre adımlar farklılık gösterir. Terminalinize aşağıdaki komutu yazın.

#### Hem pip hem Poetry için

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry kullanarak

1. Sanal ortamı Poetry ile oluşturduysanız, etkinleştirmek için terminalinize aşağıdaki komutu yazın.

    ```bash
    poetry shell
    ```

### Paket ve gerekli bağımlılıkların kurulumu

Sanal ortamınız kurulduktan ve etkinleştirildikten sonra, bir sonraki adım gerekli bağımlılıkları yüklemektir.

### Hızlı kurulum

Co-Op Translator'ı pip ile kurun

```
pip install co-op-translator
```
Veya

Poetry ile kurun
```
poetry add co-op-translator
```

#### Eğer bu depoyu klonladıysanız pip kullanarak (requirements.txt dosyasından)

![NOTE] Co-op translator'ı hızlı kurulum ile yüklüyorsanız, bunu yapmayın.

1. Pip kullanıyorsanız, terminalinize aşağıdaki komutu yazın. Bu komut, `requirements.txt` dosyasında belirtilen gerekli paketleri otomatik olarak yükleyecektir:

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry kullanarak (pyproject.toml dosyasından)

1. Poetry kullanıyorsanız, terminalinize aşağıdaki komutu yazın. Bu komut, `pyproject.toml` dosyasında belirtilen gerekli paketleri otomatik olarak yükleyecektir:

    ```bash
    poetry install
    ```

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstermemize rağmen, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.