<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-05-06T17:57:09+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "tr"
}
-->
# Co-op translator paketini yükleyin

**Co-op Translator**, projenizdeki tüm markdown dosyalarını ve resimleri birden fazla dile çevirmenize yardımcı olan bir komut satırı arayüzü (CLI) aracıdır. Bu rehber, çevirmeni yapılandırmanızı ve farklı kullanım senaryoları için çalıştırmanızı adım adım gösterecek.

### Sanal ortam oluşturma

Sanal ortamı `pip` veya `Poetry` kullanarak oluşturabilirsiniz. Terminalinize aşağıdaki komutlardan birini yazın.

#### Pip kullanarak

```bash
python -m venv .venv
```

#### Poetry kullanarak

```bash
poetry init
```

### Sanal ortamı etkinleştirme

Sanal ortamı oluşturduktan sonra etkinleştirmeniz gerekir. İşletim sisteminize göre adımlar farklıdır. Terminalinize aşağıdaki komutu yazın.

#### Hem pip hem de Poetry için

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry kullanarak

1. Ortamı Poetry ile oluşturduysanız, etkinleştirmek için terminalinize aşağıdaki komutu yazın.

    ```bash
    poetry shell
    ```

### Paket ve gerekli paketlerin kurulumu

Sanal ortamınız hazır ve etkinleştirildikten sonra, bir sonraki adım gerekli bağımlılıkları yüklemektir.

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

#### Bu depoyu klonladıysanız pip kullanarak (requirements.txt dosyasından)

![NOTE] Co-op translator'ı hızlı kurulum ile yüklüyorsanız, bunu yapmayın lütfen.

1. Pip kullanıyorsanız, terminalinize aşağıdaki komutu yazın. `requirements.txt` dosyasında belirtilen gerekli paketler otomatik olarak yüklenecektir:

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry kullanarak (pyproject.toml dosyasından)

1. Poetry kullanıyorsanız, terminalinize aşağıdaki komutu yazın. `pyproject.toml` dosyasında belirtilen gerekli paketler otomatik olarak yüklenecektir:

    ```bash
    poetry install
    ```

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalar nedeniyle sorumluluk kabul edilmemektedir.