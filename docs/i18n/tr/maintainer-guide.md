# Bakım Kılavuzu

Bu sayfa API, CLI ve dokümantasyon sitesinin nasıl birbirine bağlandığını özetler.

## Genel API sınırı

Kararlı Python API'si şu yerden dışa aktarılır:

```python
co_op_translator.api
```

Genel API, içerik çeviri yardımcıları, yol yeniden yazma yardımcıları, proje orkestrasyonu ve inceleme şeklinde düzenlenmiştir:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

`TranslationStateProvider` barındırılan entegrasyonlar için kalıcılık sınırıdır.
Oluşturulan adayları kabul edilmiş temel sürümlerden ayrı tutmalıdır, böylece bir
birleştirilmemiş çeviri gerçek kaynak haline gelemez.

Yeni genel API'ler eklerken güncelleyin:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- ilgili API testleri `tests/co_op_translator/` altında, örneğin `test_api.py` veya `test_review_api.py`

Proje bunları doğrudan desteklemeyi amaçlamıyorsa alt düzey `core` modüllerini kararlı API olarak belgelemeyin.

## CLI giriş noktaları

Paket şu Poetry betiklerini tanımlar:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` betik adına göre yönlendirir:

- `translate` `co_op_translator.cli.translate.translate_command`'ı çağırır
- `evaluate` `co_op_translator.cli.evaluate.evaluate_command`'ı çağırır
- `migrate-links` `co_op_translator.cli.migrate_links.migrate_links_command`'ı çağırır
- `co-op-review` `co_op_translator.cli.review.review_command`'ı çağırır

`co-op-translator-mcp` `__main__.py`'yi atlayarak doğrudan `co_op_translator.mcp.server:main`'i çağırır.

CLI seçenekleri eklerken veya değiştirirken güncelleyin:

- ilgili `src/co_op_translator/cli/*.py` komutu
- `docs/cli.md`
- Davranış değişirse CLI ile ilgili testler

## MCP sunucusu

MCP sunucusu şu dosyada uygulanmıştır:

```python
co_op_translator.mcp.server
```

Sunucu kasıtlı olarak alt düzey `core` modüllerini çağırmak yerine genel Python API'sini sarar. MCP istemcileri, Python çağıranlar ve CLI'nin aynı davranışı paylaşması için bu sınırı koruyun.

MCP araçları eklerken veya değiştirirken güncelleyin:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` (genel API yüzeyi değişirse)

Depo çeviri araçları MCP aracılığıyla modele çağrılabilir ve birçok dosya yazabilir. Varsayılan olarak `dry_run=True` bırakın ve dry-run olmayan proje çevirisi öncesinde `confirm_write=True` gerektirin.

## Çeviri akışı

Yüksek seviyeli proje çeviri akışı şu şekildedir:

1. CLI argümanlarını veya API parametrelerini ayrıştırın.
2. `LLMConfig` ile LLM yapılandırmasını doğrulayın.
3. Görüntü çevirisi seçildiğinde Azure AI Vision'ı doğrulayın.
4. Dil kodlarını normalleştirin.
5. Eski dil klasörü takma adlarını tespit edin.
6. Çeviri hacmini tahmin edin.
7. Uygun olduğunda README dil/kurs bölümlerini güncelleyin.
8. Proje çevirisini `ProjectTranslator`'a devredin.
9. `ProjectTranslator`, dosya işlemlerini `TranslationManager`'a devreder.

`TranslationManager` odaklanmış dosya türü mixin'lerinden oluşur:

- `ProjectMarkdownTranslationMixin` Markdown dosya okuma, içerik çevirisi, yol yeniden yazma, metadata, feragatnameler ve yazma işlemlerini ele alır.
- `ProjectNotebookTranslationMixin` notebook dosya okumaları, Markdown hücresi çevirisi, yol yeniden yazma, metadata, feragatnameler ve yazma işlemlerini ele alır.
- `ProjectImageTranslationMixin` görüntü keşfi, metin çıkarma/çeviri, oluşturulmuş görüntü yazmaları ve metadata işlemlerini ele alır.

Alt düzey içerik API'leri proje iş akışını atlar:

1. `translate_markdown_content` ve `translate_notebook_content` yalnızca bellekteki içeriği çevirir.
2. `translate_image_content` tek bir görüntüdeki metni çevirir ve oluşturulmuş bir görüntü nesnesi döndürür.
3. `rewrite_markdown_paths` ve `rewrite_notebook_paths` açıkça tanımlanmış son işlem yardımcılarıdır. Bunlar çeviri yapmaz ve proje yazımı gerçekleştirmez.

## İnceleme akışı

Deterministik inceleme akışı şu şekildedir:

1. CLI argümanlarını veya API parametrelerini ayrıştırın.
2. İstenen dil kodlarını normalleştirin.
3. `root_dir`, `root_dirs` veya `groups`'tan bir veya daha fazla inceleme hedefi oluşturun.
4. İsteğe bağlı olarak `--changed-from` ile kaynak dosyaları sınırlayın.
5. Yapı, çeviri tazeliği, Markdown bütünlüğü ve yerel bağlantı/görüntü yolları için deterministik kontrolleri çalıştırın.
6. Metin çıktısı veya GitHub uyumlu Markdown yazdırın.
7. İnceleme hataları bulunduğunda hata ile çıkış yapın.

İnceleme akışı API anahtarları gerektirmez ve yerel kontroller veya isteğe bağlı tüketici CI için kullanılabilir durumda kalır. Bu depo her pull request'te `co-op-review`'u otomatik olarak çalıştırmaz.

## Dokümantasyon sitesi

Doküman sitesi şu şekilde yapılandırılır:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` dizini kanonik dokümantasyon kaynağıdır. Proje kasıtlı olarak başka bir yayımlanmış dokümantasyon yüzeyi tanıtmadıkça bu dizinin dışına yeni son-kullanıcı kılavuzları eklemeyin.

Yerel olarak oluşturun:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Yerelde önizleyin:

```bash
python -m mkdocs serve
```

Oluşturulan site `site/` dizinine yazılır; bu dizin git tarafından yoksayılır.

## GitHub Pages iş akışı

`.github/workflows/docs.yml` dosyası pull request'lerde siteyi oluşturur ve `main`'e yapılan push'larda dağıtır.

İş akışı şunları kurar:

```bash
pip install -r requirements-docs.txt
```

Docs iş akışı yalnızca dokümantasyon araç zincirini kurar. `mkdocs.yml`, `mkdocstrings`'i `src/`'e işaret eder; böylece genel API sayfaları tam çalışma zamanı bağımlılık kümesini yüklemeden kaynak ağacından oluşturulabilir. Gelecekteki API dokümanlarının derleme sırasında isteğe bağlı çalışma zamanı sağlayıcılarını içe aktarmayı gerektirmesi durumunda, hem `.github/workflows/docs.yml`'i hem de bu kılavuzu birlikte güncelleyin.

## Doküman kalite eşiği

Dokümantasyon değişikliklerini birleştirmeden önce çalıştırın:

```bash
python -m mkdocs build --strict
git diff --check
```

Kırık bağlantılar, geçersiz gezinme girdileri ve API render hatalarının erken tespit edilmesi için katı derlemeler kullanın.