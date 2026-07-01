# Python API

Kararlı genel Python API'si `co_op_translator.api` üzerinden dışa aktarılır. Çoğu entegrasyon bu iş akışlarından birini kullanır:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Uygulamanız kaynak içeriği okur, Co-op Translator'ı çeviri için çağırır ve sonucu nereye kaydedeceğine karar verir. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | MCP ana bilgisayarınız veya uygulama modeli parçaları çevirecek, Co-op Translator ise parçalama ve yeniden birleştirmeyi yönetecektir. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | Python API'nin CLI gibi davranmasını ve keşif, çıktı yolları, meta veriler, temizlik ve yazmaları işlemesini istiyorsunuz. | `run_translation` |

`core`, `config`, `review` ve `utils` altındaki çoğu düşük seviyeli modül, bu API giriş noktaları tarafından kullanılan uygulama ayrıntılarıdır.

MCP istemcileri aynı genel API'yi [MCP Server](mcp.md) aracılığıyla kullanır. Python'u doğrudan çağırırken bu sayfayı, Co-op Translator'ı bir ajan veya düzenleyiciye açarken MCP kılavuzunu kullanın. CLI, Python API ve MCP arasında karar veriyorsanız [Choose Your Workflow](workflows.md) ile başlayın.

## First-Time API Flow

Python kodundan Co-op Translator'ı çağırıyorsanız buradan başlayın:

1. Sadece Markdown veya not defteri parçalarını ana bilgisayar ajanına hazırlamıyorsanız, [Configuration](configuration.md) bölümünde açıklandığı gibi bir LLM sağlayıcısı yapılandırın.
2. Uygulamanızın dosya G/Ç'sine sahip olup olmayacağına karar verin.
3. Uygulamanız bireysel dosyaları okuyor ve yazıyorsa içerik API'lerini kullanın.
4. Co-op Translator bir depo ile CLI gibi işlemeli ise `run_translation` kullanın.
5. Otomasyonda deterministik kontroller gerekiyorsa çeviriden sonra `run_review` kullanın.

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## Scenario 1: Translate Individual Files or Documents

Bu iş akışını, zaten bir dosyanız, düzenleyici tamponunuz, not defteri yükünüz, MCP isteğiniz veya özel boru hattı girdiniz olduğunda kullanın. Kodunuz dosya G/Ç'sinden sorumludur:

1. Kaynak içeriği okuyun.
2. Bir içerik çeviri API'si çağırın.
3. Tercüme edilmiş içerik bir proje çevirisi klasörüne yazılacaksa isteğe bağlı olarak yol yeniden yazma API'si çağırın.
4. Sonucu uygulamanızdan kaydedin veya döndürün.

İçerik çeviri API'leri proje keşfi çalıştırmaz, meta veri yazmaz, feragatnameler eklemez ve bağlantıları otomatik olarak yeniden yazmaz.

### Markdown File

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Çevrilmiş Markdown bir Co-op Translator proje düzeninde yaşamayacaksa, `rewrite_markdown_paths` atlayın ve çevrilmiş dizeyi doğrudan kaydedin.

### Notebook File

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` Markdown hücrelerini çevirir ve Markdown olmayan hücreleri korur. Yol yeniden yazma yalnızca Markdown hücrelerine uygulanır.

### Image File

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` kaynak görüntüyü okur ve render edilmiş bir `PIL.Image.Image` döndürür. Çevrilmiş görüntü meta verilerini yazmaz.

## Scenario 2: Translate an Entire Repository

Bu iş akışını, Python API'nin `translate` CLI gibi davranmasını istediğinizde kullanın. `run_translation` desteklenen dosyaları keşfeder, seçili içerik türlerini çevirir, yolları yeniden yazar, çıktı dosyalarını yazar, meta verileri günceller ve temizlik gibi çeviri bakım görevlerini gerçekleştirir.

`run_translation` tercih edilen proje orkestrasyon giriş noktasıdır. `translate_project` aynı davranışla uyumluluk takma adı olarak dışa aktarılır.

Mevcut depodaki Markdown dosyalarını Korece ve Japoncaya çevirin:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Belirli bir proje kökünden yalnızca not defterlerini çevirin:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Dosya yazmadan çeviri hacmini önizleyin:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Bir çağrıda birden fazla içerik kökünü çevirin:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Tercümeleri açık çıktı gruplarına yazın:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

Her dilin içereceği iç içe bir alt dizin olması gerektiğinde dil başına bir yer tutucu kullanın:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

`markdown`, `notebook` veya `images`'ten hiçbiri ayarlı değilse, API tüm desteklenen türleri çevirir: Markdown, not defterleri ve görüntüler.

## Review Translated Output

`run_review` deterministik çeviri kontrolleri çalıştırır; LLM veya Vision kimlik bilgileri gerektirmez.

!!! note "Beta"
    `run_review` beta bir deterministik inceleme API'sidir. Model sağlayıcılarını çağırmaz veya dosya yazmaz, ancak kontroller ve issue şemaları değişebilir.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Sadece bir temel ref'e karşı değişen dosyaları inceleyin ve GitHub biçimli çıktı yazdırın:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## Copy-Paste API Examples

Dosya yazmadan Markdown içeriğini çevirin:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Markdown bağlantılarını çevirin ve yeniden yazın:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

Python'dan bir depoyu çevirin:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Birden çok kökü çevirin:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

Sözlük terimlerini koruyun:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## Public Entry Points

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## Content Translation APIs

İçerik çeviri API'leri, bir editör eklentisi, MCP aracı, not defteri işleyicisi veya özel boru hattı gibi zaten bellekte içeriğe sahip entegrasyonlar için tasarlanmıştır.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Hayır | Async. Yalnızca Markdown içeriğini çevirir. Bağlantıları yeniden yazmaz, meta veri yazmaz veya feragatname eklemez. |
| `translate_notebook_content` | Notebook JSON `str` veya `dict` | Notebook JSON `str` | Hayır | Async. Markdown hücrelerini çevirir ve Markdown olmayan hücreleri korur. Bağlantıları yeniden yazmaz, meta veri yazmaz veya feragatname eklemez. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Sadece kaynak görüntüyü okur | Senkron. Görüntü metnini çıkarır ve çevirir, ardından render edilmiş bir görüntü döndürür. Çevrilmiş görüntü meta verilerini kaydetmez. |

`translate_markdown_content` ve `translate_notebook_content` opsiyonları aracılığıyla isteğe bağlı bir `source_path` kabul eder. Yol, çevirmen için bağlam olarak geçirilir; çağıranlar çeviriden sonra proje özelindeki yol yeniden yazmalarından sorumludur.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Aynı seçenekler sözlükler olarak da geçilebilir:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Ajan destekli API'ler Co-op Translator'dan Azure OpenAI veya OpenAI çağırmaz. Markdown veya not defteri parçalarını bir ana bilgisayar ajanınca çevrilmek üzere hazırlar, sonra çevrilmiş parçalarla nihai içeriği yeniden oluşturur.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Parçalar, istemler ve yeniden yapılandırma durumuyla kendine yeten bir Markdown işi döndürür. |
| `finish_markdown_agent_translation` | Bir işi ve ana bilgisayar ajan tarafından çevrilmiş parçaları alarak Markdown'u yeniden oluşturur. |
| `start_notebook_agent_translation` | Ana bilgisayar ajan çevirisi için Markdown hücre parçalarına sahip bir not defteri işi döndürür. |
| `finish_notebook_agent_translation` | Kod hücrelerini, çıktıları ve meta verileri korurken not defteri JSON'unu yeniden oluşturur. |

Bu iş akışı esas olarak MCP ana bilgisayarları içindir. Co-op Translator'ın sağlayıcı çağrılarını yönettiği üretim depo çevirisine ihtiyacınız varsa `translate_markdown_content`, `translate_notebook_content` veya `run_translation` kullanın.

## Path Rewriting APIs

Yol yeniden yazma API'leri çeviri yapmaz. Kaynak yolunu, çevrilmiş hedef yolunu ve proje düzenini bildikten sonra bağlantıları ve frontmatter yollarını güncellerler.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown gövdesi ve frontmatter | Çevrilmiş bir hedef için Markdown bağlantılarını ve desteklenen frontmatter yol alanlarını yeniden yazar. |
| `rewrite_notebook_paths` | Notebook JSON içindeki Markdown hücreleri | Her Markdown hücresine Markdown yol yeniden yazmayı uygular ve Markdown olmayan hücreleri değiştirmez. |

`policy` argümanı şu alanlara sahip bir sözlük olabilir:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Hedef dil kodu, örneğin `"ko"` veya `"pt-BR"`. |
| `root_dir` | No | Kaynak proje kökü. Varsayılan `"."`. |
| `translations_dir` | No | Metin çevirisi çıktı dizini. Varsayılan `root_dir` altında `translations`. |
| `translated_images_dir` | No | Çevrilmiş görüntü çıktı dizini. Varsayılan `root_dir` altında `translated_images`. |
| `translation_types` | No | Etkinleştirilmiş çeviri türleri. Varsayılan olarak Markdown, not defterleri ve görüntüler. |
| `lang_subdir` | No | Her dil klasörünün altında isteğe bağlı alt dizin. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Boşlukla ayrılmış hedef dil kodları, örneğin `"ko ja fr"`, veya `"all"`. Takma ad kodlar kanonik BCP 47 değerlerine normalize edilir. |
| `root_dir` | `str` | `"."` | Tek bir çeviri hedefi için proje kökü. `root_dirs` veya `groups` sağlandığında göz ardı edilir. |
| `update` | `bool` | `False` | Seçilen diller için mevcut çevirileri siler ve yeniden oluşturur. |
| `images` | `bool` | `False` | Görüntü çevirisini dahil et. Azure AI Vision yapılandırması gerektirir. |
| `markdown` | `bool` | `False` | Markdown çevirisini dahil et. |
| `notebook` | `bool` | `False` | Jupyter not defteri çevirisini dahil et. |
| `debug` | `bool` | `False` | Hata ayıklama günlüklemesini etkinleştir. |
| `save_logs` | `bool` | `False` | Kök `logs/` dizini altında DEBUG düzeyinde günlük dosyalarını kaydet. |
| `yes` | `bool` | `True` | Programatik ve CI kullanımı için istemleri otomatik onayla. |
| `add_disclaimer` | `bool` | `False` | Çevrilmiş Markdown ve not defterlerine makine çevirisi feragatnameleri ekle. |
| `translations_dir` | `str \| None` | `None` | Özel metin çevirisi çıktı dizini. Göreli yollar her köke karşı çözümlenir. |
| `image_dir` | `str \| None` | `None` | Özel çevrilmiş görüntü çıktı dizini. Göreli yollar her köke karşı çözümlenir. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Aynı çıktı ayarlarını paylaşan birden fazla kök. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Açık `(root_dir, translations_dir)` çiftleri. `root_dirs` üzerinde öncelik alır. |
| `repo_url` | `str \| None` | `None` | README dil tablosu rehberliği oluşturulurken kullanılan depo URL'si. |
| `glossaries` | `Iterable[str] \| None` | `None` | Çeviri sırasında korunacak sözlük terimleri. Yinelemeler ve boş terimler normalize edilir. |
| `dry_run` | `bool` | `False` | Dosya yazmadan çeviri hacmini tahmin edin ve göç davranışını önizleyin. |

## Review Parameters

`run_review` otomasyonda çeviri ve inceleme iş akışları arasında mümkün olduğunca az dallanma ile geçiş yapılabilmesi için `run_translation` imza yapısını kasıtlı olarak yansıtır.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | İncelenecek hedef dil klasörleri. Boşluklu stringler ve iterable'lar kabul edilir. `"all"` bulunan tüm çeviri dillerini inceler. |
| `root_dir` | `str` | `"."` | Tek bir inceleme hedefi için proje kökü. `root_dirs` veya `groups` sağlandığında göz ardı edilir. |
| `markdown` | `bool` | `False` | Markdown ve MDX kaynak dosyalarını dahil et. |
| `notebook` | `bool` | `False` | Jupyter not defteri kaynak dosyalarını dahil et. |
| `images` | `bool` | `False` | Çeviri seçenekleri ile uyumluluk için ayrılmıştır. Görüntülere yapılan bağlantı başvuruları Markdown'dan kontrol edilir. |
| `translations_dir` | `str \| None` | `None` | Özelleştirilmiş metin çevirisi çıktı dizini. Göreli yollar her bir köke göre çözülür. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Aynı çıktı ayarlarını paylaşan birden çok kök. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Açıkça belirtilmiş `(root_dir, translations_dir)` çiftleri. Takes precedence over `root_dirs`. |
| `changed_from` | `str \| None` | `None` | İncelemeyi değişen kaynak dosyalarla sınırlamak için kullanılan Git ref'i. |
| `output_format` | `str` | `"text"` | İnceleme çıktı formatı. Desteklenen değerler `"text"` ve `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Uyarıları hatalara ek olarak başarısızlık olarak değerlendir. |
| `debug` | `bool` | `False` | Debug günlük kaydını etkinleştir. |
| `save_logs` | `bool` | `False` | DEBUG düzeyindeki günlük dosyalarını kök `logs/` dizini altında kaydet. |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## Yapılandırma Gereksinimleri

Sağlayıcı destekli çeviri API'leri çeviri yapmadan önce sağlayıcı yapılandırması gerektirir:

- Markdown ve not defteri çevirisi için bir LLM sağlayıcısı gereklidir. Azure OpenAI veya OpenAI'tan birini yapılandırın.
- Resim çevirisi için LLM sağlayıcısına ek olarak Azure AI Vision gereklidir.
- `run_translation` proje çevirisi başlamadan önce hafif bağlantı kontrolleri çalıştırır.
- Ajan destekli `start_*_agent_translation` ve `finish_*_agent_translation` API'leri Co-op Translator LLM sağlayıcılarını çağırmaz. Hazırlanan parçaları ana uygulama veya MCP ajanı çevirir.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` ve `run_review` deterministik olup sağlayıcı kimlik bilgileri gerektirmez.

Gerekli Azure OpenAI değişkenleri:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Gerekli OpenAI değişkenleri:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Resim çevirisi için gerekli Azure AI Vision değişkenleri:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` deterministiktir ve Azure OpenAI, OpenAI veya Azure AI Vision yapılandırması gerektirmez.

## Davranış Notları

- İçerik çeviri API'leri çeviriyi proje yol yeniden yazımından ayrı tutar. Çevrilmiş içerikte proje göreli bağlantılar hedef konuma göre ayarlanması gerektiğinde `rewrite_markdown_paths` veya `rewrite_notebook_paths`'ı açıkça çağırın.
- Proje orkestrasyon API'leri, dosya keşfi, yazma, yol yeniden yazımı, meta veriler, temizleme ve isteğe bağlı feragatnameler dahil olmak üzere içerik çevirisi etrafında proje davranışı ekler.
- `run_translation`, CLI kullanıcı deneyimiyle eşleşecek şekilde ilerleme ve tahmin özetlerini Click aracılığıyla yazdırır.
- `dry_run=True`, sanal README güncellemeleri kullanarak tahminleri hesaplar, ancak README veya çeviri dosyalarını yazmaz.
- `groups` sıralı olarak işlenir. İş başlamadan önce tek bir toplam tahmin yazdırılır.
- Resim çevirisi seçildiğinde, eksik Vision yapılandırması çeviri başlamadan önce bir hata oluşturur.
- Var olan takma ad (alias) tabanlı dil klasörleri algılanır ve çalıştırmanın bir parçası olarak kanonik dil klasörü adlarına taşınabilir.
- `run_review`, eksik çevrilmiş dosyalar, eksik veya bayat çeviri meta verileri, bozuk Markdown frontmatter/kod çitlemeleri ve geçersiz çevrilmiş not defteri JSON'u durumunda başarısız olur.
- `run_review` varsayılan olarak eksik yerel Markdown ve resim bağlantı hedeflerini uyarı olarak raporlar.

## Dahili Çağrı Yolu

API, CLI tarafından kullanılan aynı çekirdek uygulamaya delege eder:

Çeviri:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` bellek içi çeviri için.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` açık yol sonrası işleme için.
3. `co_op_translator.api.translation.run_translation` tam proje orkestrasyonu için.
4. `co_op_translator.config.Config`, `LLMConfig`, ve `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, not defterleri ve resimler için odaklanmış proje çeviri mixin'leri.
8. `co_op_translator.core` altında Markdown, not defteri, metin ve resim çevirmenleri.

İnceleme:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` altındaki deterministik kontroller

Aşağıdaki sınıflar bakımcılar için kullanışlıdır, ancak paket düzeyindeki kararlı API olarak dışa aktarılmaz.

| Sınıf | Modül | Sorumluluk |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Proje düzeyinde çeviriyi, dizin yönetimini, dil başına meta veri normalizasyonunu ve Markdown, not defteri ve resim çevirmenlerine delege etmeyi koordine eder. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, not defterleri, resimler, bayat tespiti ve çeviri meta veri güncellemeleri için asenkron dosya işleme işlerini gerçekleştirir. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown dosya okuma, içerik çevirisi, yol yeniden yazımı, meta veriler, feragatnameler ve yazma işlemlerini koordine eder. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Not defteri dosyası okuma, Markdown hücresi çevirisi, yol yeniden yazımı, meta veriler, feragatnameler ve yazma işlemlerini koordine eder. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Kaynak resim keşfini, resim çevirisini, çıktı yollarını, meta verileri ve yazma işlemlerini koordine eder. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Çevrilmiş Markdown çiftlerini bulur, çeviri kalitesini değerlendirir ve düşük güvenilirlikli düzeltme iş akışları için güven meta verilerini okur. |
| `ReviewRunner` | `co_op_translator.review.runner` | Kaynak dosyalar, hedef diller ve yapılandırılmış çeviri kökleri genelinde deterministik inceleme kontrollerini koordine eder. |
| `ReviewTarget` | `co_op_translator.review.targets` | Bir kaynak kökü ve o kök için incelenen çeviri çıktı dizinini tanımlar. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Eski takma ad dil klasörlerini algılar ve kanonik BCP 47 klasör geçiş planlarını hazırlar. |
| `Config` | `co_op_translator.config.base_config` | `.env` dosyalarını yükler ve gerekli LLM ile isteğe bağlı Vision sağlayıcılarının yapılandırılıp yapılandırılmadığını kontrol eder. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI veya OpenAI'ı otomatik algılar, gerekli ortam değişkenlerini doğrular ve sağlayıcı bağlantı kontrollerini çalıştırır. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision yapılandırmasını algılar ve resim çevirisi için bağlantı kontrollerini çalıştırır. |