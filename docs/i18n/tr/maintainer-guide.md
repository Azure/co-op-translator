# Sürdürme Kılavuzu

Bu sayfa API, CLI ve dokümantasyon sitesinin nasıl birbirine bağlandığını özetler.

## Genel API sınırı

The stable Python API is exported from:

```python
co_op_translator.api
```

Genel API, içerik çeviri yardımcıları, yol yeniden yazma yardımcıları, proje orkestrasyonu ve inceleme şeklinde düzenlenmiştir:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

Yeni genel API'ler eklerken, güncelleyin:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- ilgili API testleri `tests/co_op_translator/` altında, örneğin `test_api.py` veya `test_review_api.py`

Projede doğrudan desteklemeyi amaçlamadıkça, daha düşük seviyeli `core` modüllerini kararlı API olarak belgelemekten kaçının.

## CLI entry points

Paket şu Poetry betiklerini tanımlar:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` script adına göre yönlendirir:

- `translate` `co_op_translator.cli.translate.translate_command`'i çağırır
- `evaluate` `co_op_translator.cli.evaluate.evaluate_command`'i çağırır
- `migrate-links` `co_op_translator.cli.migrate_links.migrate_links_command`'u çağırır
- `co-op-review` `co_op_translator.cli.review.review_command`'ı çağırır

`co-op-translator-mcp` `__main__.py`'yi atlar ve `co_op_translator.mcp.server:main`'i doğrudan çağırır.

CLI seçenekleri eklerken veya değiştirirken, güncelleyin:

- ilgili `src/co_op_translator/cli/*.py` komutu
- `docs/cli.md`
- CLI ile ilgili testler, davranış değişirse

## MCP server

The MCP server is implemented in:

```python
co_op_translator.mcp.server
```

Sunucu, kasıtlı olarak daha düşük seviyeli `core` modüllerini çağırmak yerine genel Python API'sini sarar. Bu sınırı koruyun ki MCP istemcileri, Python çağırıcıları ve CLI aynı davranışı paylaşsın.

MCP araçları eklerken veya değiştirirken, güncelleyin:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- genel API yüzeyi değişirse `docs/api.md`

Depo çeviri araçları MCP aracılığıyla modele çağrılabilir ve birçok dosya yazabilir. Varsayılan olarak `dry_run=True` tutun ve gerçek (non-dry-run) proje çevirisinden önce `confirm_write=True` gerektirin.

## Translation flow

Yüksek seviyeli proje çeviri akışı şöyledir:

1. CLI argümanlarını veya API parametrelerini ayrıştırın.
2. LLM yapılandırmasını `LLMConfig` ile doğrulayın.
3. Resim çevirisi seçildiğinde Azure AI Vision'ı doğrulayın.
4. Dil kodlarını normalleştirin.
5. Eski dil klasörü takma adlarını tespit edin.
6. Çeviri hacmini tahmin edin.
7. Uygunsa README dil/kurs bölümlerini güncelleyin.
8. Proje çevirisini `ProjectTranslator`'a devredin.
9. `ProjectTranslator` dosya işleme görevini `TranslationManager`'a devreder.

`TranslationManager` odaklanmış dosya-tipi mixin'lerinden oluşur:

- `ProjectMarkdownTranslationMixin` Markdown dosya okumalarını, içerik çevirisini, yol yeniden yazmayı, meta verileri, feragatnameleri ve yazma işlemlerini ele alır.
- `ProjectNotebookTranslationMixin` notebook dosya okumalarını, Markdown hücre çevirisini, yol yeniden yazmayı, meta verileri, feragatnameleri ve yazma işlemlerini ele alır.
- `ProjectImageTranslationMixin` resim keşfini, metin çıkarma/çeviriyi, oluşturulmuş resim yazımlarını ve meta verileri ele alır.

Daha düşük seviyeli içerik API'leri proje iş akışını atlar:

1. `translate_markdown_content` ve `translate_notebook_content` yalnızca bellekteki içeriği çevirir.
2. `translate_image_content` tek bir resimdeki metni çevirir ve oluşturulmuş bir resim nesnesi döndürür.
3. `rewrite_markdown_paths` ve `rewrite_notebook_paths` açık düzey sonrası işleme yardımcılarıdır. Hiç çeviri veya proje yazımı yapmazlar.

## Review flow

Deterministik inceleme akışı şudur:

1. CLI argümanlarını veya API parametrelerini ayrıştırın.
2. İstenen dil kodlarını normalleştirin.
3. Bir veya daha fazla inceleme hedefini `root_dir`, `root_dirs` veya `groups`'tan oluşturun.
4. İsteğe bağlı olarak kaynak dosyaları `--changed-from` ile sınırlayın.
5. Yapı, çeviri tazeliği, Markdown bütünlüğü ve yerel bağlantı/resim yolları için deterministik kontroller çalıştırın.
6. Metin çıktısı veya GitHub usulü Markdown yazdırın.
7. İnceleme hataları bulunduğunda başarısızlık ile çıkış yapın.

İnceleme akışı API anahtarları gerektirmez ve pull request CI için uygun kalmalıdır. Pull request iş akışı her çalıştırmada bir kontrol özeti yazar ve yalnızca `co-op-review` başarısız olduğunda bir PR yorumu gönderir.

## Documentation site

The docs site is configured by:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` dizini kanonik dokümantasyon kaynağıdır. Proje kasıtlı olarak başka bir yayımlanmış dokümantasyon yüzeyi tanıtmadıkça, bu dizinin dışına yeni son kullanıcı kılavuzları eklemeyin.

Build locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Preview locally:

```bash
python -m mkdocs serve
```

Oluşturulan site `site/`'ye yazılır; bu dizin git tarafından yoksayılır.

## GitHub Pages workflow

`.github/workflows/docs.yml` siteyi pull request'lerde oluşturur ve `main`'e push edildiğinde dağıtır.

The workflow installs:

```bash
pip install -r requirements-docs.txt
```

Dokümantasyon iş akışı yalnızca dokümantasyon araç zincirini kurar. `mkdocs.yml`, `mkdocstrings`'i `src/`'e yönlendirir, böylece genel API sayfaları tam çalışma zamanı bağımlılık setini kurmadan kaynak ağaçtan oluşturulabilir. Gelecekte API dokümantasyonunun derleme sırasında isteğe bağlı çalışma zamanı sağlayıcılarını içe aktarmayı gerektirmesi durumunda, hem `.github/workflows/docs.yml` hem de bu kılavuzu birlikte güncelleyin.

## Docs quality bar

Before merging documentation changes, run:

```bash
python -m mkdocs build --strict
git diff --check
```

Kırık bağlantılar, geçersiz gezinme girdileri ve API oluşturma sorunlarının erken başarısız olması için katı derlemeler kullanın.