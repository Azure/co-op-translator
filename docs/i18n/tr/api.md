# Python API

Kararlı halka açık Python API'si `co_op_translator.api`'den dışa aktarılır. Çoğu entegrasyon bu iş akışlarından birini kullanır:

| Senaryo | Ne zaman kullanılır | Ana API'ler |
| --- | --- | --- |
| Bireysel dosyaları veya belgeleri çevirin | Uygulamanız kaynak içeriği okur, çeviri için Co-op Translator'ı çağırır ve sonucu nereye kaydedeceğine karar verir. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Ana bilgisayar aracısı tarafından çeviri için içeriği hazırlayın | MCP ana bilgisayarınız veya uygulama modeliniz parçaları çevirecek, Co-op Translator ise parçalama ve yeniden birleştirmeyi yönetir. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Tüm bir depoyu çevirin | Python API'nin CLI gibi davranmasını ve keşif, çıktı yolları, meta veri, temizleme ve yazma işlemlerini gerçekleştirmesini istiyorsunuz. | `run_translation` |

`core`, `config`, `review` ve `utils` altındaki çoğu alt seviye modül, bu API giriş noktaları tarafından kullanılan uygulama ayrıntılarıdır.

MCP istemcileri aynı genel API'yi [MCP Sunucusu](mcp.md) aracılığıyla kullanır. Python'u doğrudan çağırırken bu sayfayı kullanın; Co-op Translator'ı bir ajana veya editöre açarken MCP kılavuzunu kullanın. CLI, Python API ve MCP arasında karar veriyorsanız [İş Akışınızı Seçin](workflows.md) ile başlayın.

## İlk Kez API Akışı

Python kodundan Co-op Translator'ı çağırıyorsanız buradan başlayın:

1. Yalnızca host-agent çevirisi için Markdown veya not defteri parçaları hazırlamıyorsanız, [Yapılandırma](configuration.md) bölümünde açıklandığı gibi bir LLM sağlayıcısı yapılandırın.
2. Uygulamanızın dosya giriş/çıkışını (I/O) yönetip yönetmeyeceğine karar verin.
3. Uygulamanız bireysel dosyaları okuyor ve yazıyorsa içerik API'lerini kullanın.
4. Co-op Translator'ın bir depoyu CLI gibi işlemesi gerektiğinde `run_translation`'ı kullanın.
5. Otomasyonda deterministik kontroller gerekiyorsa çeviriden sonra `run_review`'u kullanın.

| Hedef | Başlangıç için API |
| --- | --- |
| Bir Markdown dizesini veya dosyasını çevirin | `translate_markdown_content` |
| Bir not defteri içeriğini çevirin | `translate_notebook_content` |
| Bir resmi çevirin | `translate_image_content` |
| Bir host ajanının Markdown veya not defteri parçalarını çevirmesine izin verin | `start_markdown_agent_translation` veya `start_notebook_agent_translation` |
| Çıktı yolunu seçtikten sonra çevrilmiş bağlantıları yeniden yazın | `rewrite_markdown_paths` veya `rewrite_notebook_paths` |
| Tam bir depoyu çevirin | `run_translation` |
| Çevrilmiş çıktıyı gözden geçirin | `run_review` |

## Senaryo 1: Bireysel Dosyaları veya Belgeleri Çevirme

Zaten bir dosyanız, düzenleyici tamponunuz, not defteri içeriğiniz, MCP isteğiniz veya özel bir boru hattı girdiniz varsa bu iş akışını kullanın. Dosya G/Ç'si uygulamanıza aittir:

1. Kaynak içeriği okuyun.
2. Bir içerik çeviri API'si çağırın.
3. Çevrilmiş içerik bir proje çeviri klasörüne yazılacaksa isteğe bağlı olarak bir yol yeniden yazma API'si çağırın.
4. Sonucu uygulamanızdan kaydedin veya döndürün.

İçerik çeviri API'leri proje keşfi çalıştırmaz, meta veri yazmaz, feragatnameler eklemez ve bağlantıları otomatik olarak yeniden yazmaz.

### Markdown Dosyası

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

Çevrilmiş Markdown, Co-op Translator proje düzeninde yaşamayacaksa `rewrite_markdown_paths`'i atlayın ve çevrilmiş dizeyi doğrudan kaydedin.

### Not Defteri Dosyası

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

### Resim Dosyası

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

`translate_image_content` kaynak resmi okur ve render edilmiş bir `PIL.Image.Image` döner. Çevrilmiş resim meta verisini yazmaz.

## Senaryo 2: Tüm Bir Depoyu Çevirme

Python API'nin `translate` CLI gibi davranmasını istiyorsanız bu iş akışını kullanın. `run_translation` desteklenen dosyaları keşfeder, seçili içerik türlerini çevirir, yolları yeniden yazar, çıktı dosyalarını yazar, meta veriyi günceller ve temizleme gibi çeviri bakım görevlerini gerçekleştirir.

`run_translation` tercih edilen proje orkestrasyonu giriş noktasıdır. `translate_project` aynı davranışla uyumluluk takma adı olarak dışa aktarılır.

Geçerli depodaki Markdown dosyalarını Korece ve Japoncaya çevirin:

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

Dosyaları yazmadan çeviri hacmini önizleyin:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Bir entegrasyon için yapılandırılmış ilerleme olaylarını kaydedin:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # İş-olay tablonuza veri yükünü kaydedin veya kullanıcı arayüzünüze akış olarak gönderin.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Olaylar sürümlenmiş şema `co-op.translation.event.v1`'i kullanır. Entegrasyonlar
`type` ve `stage_key` gibi kararlı alanlara dayanmalı, insanlara yönelik
konsol metnine veya `stage_label`'a değil.

Bir çağrıda birden çok içerik kökünü çevirin:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Çevirileri açık çıktı gruplarına yazın:

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

Her dilin içinde iç içe bir alt dizin bulunması gerektiğinde dil başına bir yer tutucu kullanın:

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

Eğer `markdown`, `notebook` veya `images`'den hiçbiri ayarlanmamışsa, API desteklenen tüm türleri çevirir: Markdown, not defterleri ve resimler.

### Kabul edilmiş insan düzenlemelerini bir çeviri durum sağlayıcısıyla koruyun

Varsayılan olarak, Co-op Translator mevcut dosya düzeyi davranışını korur: bir
Markdown kaynağı eskiyse, tüm çevrilmiş dosya yeniden üretilir. Barındırılan
entegrasyonlar, değişmemiş kaynak bloklarındaki insan
düzenlemelerini korumak için isteğe bağlı olarak bir `TranslationStateProvider` sağlayabilir.

Sağlayıcı, son kabul edilmiş kaynak/hedef çiftini sağlar ve her yeni
adayı kaydeder. Kabul etmek entegrasyonun sorumluluğu olarak kalır—örneğin,
bir çeviri pull isteği birleştirildikten sonra:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

Geçerli kabul edilmiş bir temeli (baseline) olan Markdown dosyaları için, Co-op Translator
üst düzey Markdown bloklarını hizalar. Değişmeyen kaynak blokları, insanlar tarafından yapılan
düzenlemeler dahil olmak üzere mevcut çevrilmiş blokları yeniden kullanır; değişen veya eklenen
kaynak blokları çeviri için gönderilir; silinen kaynak blokları kaldırılır. Hizalama belirsizse,
hedef yapı değiştiyse, bir blok çevirisi geçersizse veya bir temel satır yoksa,
Co-op Translator güvenli bir şekilde mevcut tam dosya
çeviri yoluna geri döner.

Bu API belge çeviri durumunu saklar, belgeler arası bir ifade veya
segment çeviri belleği (translation memory) değil. Şu anda Markdown proje
çevirisine uygulanır. Not defteri ve resim davranışı değişmemiştir. `update=True`
göndermek yine tam yeniden üretim talep eder.

Bir veya daha fazla dosya çevrilemezse, `run_translation` bir
`RuntimeError` yükseltir; proje iş akışı tamamlandıktan sonra eksik çıktı ile başarılı bir
çalıştırma raporlamak yerine. Entegrasyonlar bunu başarısız bir iş
olarak değerlendirmeli ve önceki kabul edilmiş çeviri durumunu korumalıdır.

## Çevrilmiş Çıktıyı Gözden Geçirme

`run_review` LLM veya Vision kimlik bilgileri olmadan deterministik çeviri kontrolleri çalıştırır.

!!! note "Beta"
    `run_review` beta deterministik bir inceleme API'sidir. Model sağlayıcılarını çağırmaz veya dosya yazmaz; ancak kontroller ve sorun şemaları değişebilir.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Sadece README çevirisinden sonra, inceleme için aynı kapsamı kullanın:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` sadece yapılandırılmış her kaynak kökünde `README.md`'yi inceler,
including custom `groups` and output directories. Other documents and nested
READMEs are excluded. A missing source README raises `ValueError`; failed
translation checks raise `RuntimeError`.

Yalnızca bir temel ref'e karşı değişen dosyaları inceleyin ve GitHub biçimli çıktı yazdırın:

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

## Kopyala-Yapıştır API Örnekleri

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
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

Bir depoyu Python'dan çevirin:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Birden fazla kökü çevirin:

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

## Genel Giriş Noktaları

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## İçerik Çeviri API'leri

İçerik çeviri API'leri, bir editör uzantısı, MCP aracı, notebook işlemcisi veya özel bir iş akışı gibi içeriği zaten bellekte olan entegrasyonlar için tasarlanmıştır.

| Fonksiyon | Girdi | Çıktı | Dosya G/Ç | Notlar |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | Hayır | Eşzamansız. Sadece Markdown içeriğini çevirir. Bağlantıları yeniden yazmaz, meta verileri yazmaz veya feragatnameler eklemez. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | Hayır | Eşzamansız. Markdown hücrelerini çevirir ve Markdown olmayan hücreleri korur. Bağlantıları yeniden yazmaz, meta verileri yazmaz veya feragatnameler eklemez. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Eşzamanlı. Görüntü metnini çıkarır ve çevirir, ardından render edilmiş bir görüntü döndürür. Çevrilmiş görüntü meta verilerini kaydetmez. |

`translate_markdown_content` ve `translate_notebook_content`, seçenekleri aracılığıyla isteğe bağlı bir `source_path` kabul eder. Yol çevirmene bağlam olarak geçirilir; çağıranlar çeviri sonrası proje-özgü yol yeniden yazımı sorumluluğunu taşımaya devam eder.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Aynı seçenekler sözlükler olarak geçirilebilir:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Ajan Destekli Çeviri API'leri

Ajan destekli API'ler Co-op Translator'dan yapılandırılmış LLM sağlayıcısını çağırmaz. Bir ev sahibi ajanın çevirmesi için Markdown veya notebook parçalarını hazırlarlar ve ardından çevrilmiş parçalarından nihai içeriği yeniden oluştururlar.

| Fonksiyon | Amaç |
| --- | --- |
| `start_markdown_agent_translation` | Küçük parçalar, istemler ve yeniden oluşturma durumu içeren kendi kendine yeten bir Markdown işi döndürür. |
| `finish_markdown_agent_translation` | Bir iş ve ev sahibi ajanın çevirdiği parçalarından Markdown'u yeniden oluşturur. |
| `start_notebook_agent_translation` | Ev sahibi ajanın çevirisi için Markdown hücresi parçaları içeren bir notebook işi döndürür. |
| `finish_notebook_agent_translation` | Kod hücrelerini, çıktıları ve meta verileri korurken notebook JSON'unu yeniden oluşturur. |

Bu iş akışı esasen MCP host'ları için tasarlanmıştır. Eğer Co-op Translator'ın sağlayıcı çağrılarını yönetmesiyle üretim deposu çevirisine ihtiyacınız varsa, `translate_markdown_content`, `translate_notebook_content` veya `run_translation` kullanın.

## Yol Yeniden Yazma API'leri

Yol yeniden yazma API'leri çeviri yapmaz. Çağıranlar kaynak yolu, çevrilmiş hedef yolu ve proje düzenini bildikten sonra bağlantıları ve frontmatter yollarını güncellerler.

| Fonksiyon | Kapsam | Notlar |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown gövdesi ve frontmatter | Çevirilen hedef için Markdown bağlantılarını ve desteklenen frontmatter yol alanlarını yeniden yazar. |
| `rewrite_notebook_paths` | Notebook JSON içindeki Markdown hücreleri | Her Markdown hücresine Markdown yol yeniden yazımını uygular ve Markdown olmayan hücreleri değişmeden bırakır. |

`policy` argümanı şu alanları içeren bir sözlük olabilir:

| Alan | Gerekli | Amaç |
| --- | --- | --- |
| `language_code` | Evet | Hedef dil kodu, örneğin `"ko"` veya `"pt-BR"`. |
| `root_dir` | Hayır | Kaynak proje kökü. Varsayılan `"."`. |
| `translations_dir` | Hayır | Metin çeviri çıktı dizini. Varsayılan `translations` under `root_dir`. |
| `translated_images_dir` | Hayır | Çevrilmiş görüntü çıktı dizini. Varsayılan `translated_images` under `root_dir`. |
| `translation_types` | Hayır | Etkin çeviri türleri. Varsayılan olarak Markdown, notebook'lar ve görüntüler. |
| `lang_subdir` | Hayır | Her dil klasörünün altında isteğe bağlı alt dizin. |

## Proje Çeviri Parametreleri

| Parametre | Tür | Varsayılan | Amaç |
| --- | --- | --- | --- |
| `language_codes` | `str` | Gerekli | Boşlukla ayrılmış hedef dil kodları, örneğin `"ko ja fr"`, veya `"all"`. Takma ad kodları canonical BCP 47 değerlerine normalleştirilir. |
| `root_dir` | `str` | `"."` | Tek bir çeviri hedefi için proje kökü. `root_dirs` veya `groups` sağlandığında yoksayılır. |
| `update` | `bool` | `False` | Seçilen diller için mevcut çevirileri siler ve yeniden oluşturur. |
| `images` | `bool` | `False` | Görüntü çevirisini dahil et. Azure AI Vision yapılandırması gerektirir. |
| `markdown` | `bool` | `False` | Markdown çevirisini dahil et. |
| `notebook` | `bool` | `False` | Jupyter notebook çevirisini dahil et. |
| `debug` | `bool` | `False` | Hata ayıklama günlüklemesini etkinleştir. |
| `save_logs` | `bool` | `False` | Kök `logs/` dizini altında DEBUG düzeyinde günlük dosyalarını kaydet. |
| `yes` | `bool` | `True` | Programatik ve CI kullanımı için istemleri otomatik onaylar. |
| `add_disclaimer` | `bool` | `False` | Çevrilmiş Markdown ve not defterlerine makine çevirisi feragatnameleri ekler. |
| `translations_dir` | `str \| None` | `None` | Özel metin çevirisi çıktı dizini. Göreli yollar her köke göre çözülür. |
| `image_dir` | `str \| None` | `None` | Özel çevrilmiş görüntü çıktı dizini. Göreli yollar her köke göre çözülür. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Aynı çıktı ayarlarını paylaşan birden çok kök. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Açık `(root_dir, translations_dir)` çiftleri. `root_dirs` üzerinde öncelik tanır. |
| `repo_url` | `str \| None` | `None` | README dil tablosu yönergeleri oluşturulurken kullanılan depo URL'si. |
| `glossaries` | `Iterable[str] \| None` | `None` | Çeviri sırasında korunacak sözlük terimleri. Çoğaltmalar ve boş terimler normalize edilir. |
| `dry_run` | `bool` | `False` | Çeviri hacmini tahmin eder ve dosya yazmadan taşıma davranışını önizler. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Artımlı Markdown güncellemeleri için isteğe bağlı kabul edilmiş-temel ve aday kalıcılık adaptörü. Hariç tutulursa mevcut tüm dosya davranışı korunur. |

## İnceleme Parametreleri

`run_review` kasıtlı olarak `run_translation` imzasını mümkün olduğunca yansıtır, böylece otomasyon çeviri ve inceleme iş akışları arasında minimum dallanma ile geçiş yapabilir.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | İncelenecek hedef dil klasörleri. Boşlukla ayrılmış dizeler ve yineleyiciler kabul edilir. `"all"` bulunan her çeviri dilini inceler. |
| `root_dir` | `str` | `"."` | Tek inceleme hedefi için proje kökü. `root_dirs` veya `groups` sağlandığında göz ardı edilir. |
| `markdown` | `bool` | `False` | Markdown ve MDX kaynak dosyalarını dahil et. |
| `notebook` | `bool` | `False` | Jupyter notebook kaynak dosyalarını dahil et. |
| `images` | `bool` | `False` | Çeviri seçenekleriyle uyumluluk için ayrılmıştır. Görüntülere yönelik bağlantı referansları Markdown'dan kontrol edilir. |
| `translations_dir` | `str \| None` | `None` | Özel metin çevirisi çıktı dizini. Göreli yollar her köke göre çözülür. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Aynı çıktı ayarlarını paylaşan birden çok kök. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Açık `(root_dir, translations_dir)` çiftleri. `root_dirs` üzerinde öncelik tanır. |
| `changed_from` | `str \| None` | `None` | İncelemeyi değişen kaynak dosyalarla sınırlamak için kullanılan Git ref'i. |
| `readme_only` | `bool` | `False` | Her kaynak kök altında yalnızca `README.md`'yi inceleyin. Eksik bir kaynak README `ValueError` yükseltir. |
| `output_format` | `str` | `"text"` | İnceleme çıktı biçimi. Desteklenen değerler `"text"` ve `"github"`'dur. |
| `fail_on_warnings` | `bool` | `False` | Uyarıları hataların yanı sıra başarısızlık olarak kabul et. |
| `debug` | `bool` | `False` | Hata ayıklama günlüklemesini etkinleştir. |
| `save_logs` | `bool` | `False` | Kök `logs/` dizini altında DEBUG düzeyinde günlük dosyalarını kaydet. |

Eğer `markdown`, `notebook` veya `images` hiçbirisi ayarlı değilse, API uygun yerlerde Markdown, notebook'ları ve görüntü bağlantı referanslarını inceler. İnceleme bir LLM sağlayıcısını çağırmaz ve API anahtarları gerektirmez.

## Yapılandırma Gereksinimleri

Sağlayıcı destekli çeviri API'leri çevirmeden önce sağlayıcı yapılandırması gerektirir:

- Markdown ve not defteri çevirisi bir LLM sağlayıcısı gerektirir. Azure OpenAI, OpenAI veya Anthropic yapılandırın.
- Görüntü çevirisi, LLM sağlayıcısına ek olarak Azure AI Vision gerektirir.
- `run_translation` proje çevirisi başlamadan önce hafif bağlantı kontrolleri çalıştırır.
- Ajan destekli `start_*_agent_translation` ve `finish_*_agent_translation` API'leri Co-op Translator LLM sağlayıcılarını çağırmaz. Hazırlanan parçaları host uygulama veya MCP ajanı çevirir.
- `rewrite_markdown_paths`, `rewrite_notebook_paths` ve `run_review` deterministiktir ve sağlayıcı kimlik bilgileri gerektirmez.

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

Gerekli Anthropic değişkenleri:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` ve `ANTHROPIC_MAX_TOKENS` isteğe bağlıdır. Microsoft Agent Framework, Co-op Translator 0.22.0'dan itibaren tüm sağlayıcılar için varsayılan model istemcisidir. Semantic Kernel yine de geçici olarak `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` ile seçilebilir, ancak bu bir kullanım dışı bırakma uyarısı verir; aşamalı kaldırma planı için [yapılandırma](configuration.md#model-client-backend) bölümüne bakın.

Görüntü çevirisi için gerekli Azure AI Vision değişkenleri:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` deterministiktir ve LLM veya Azure AI Vision yapılandırması gerektirmez.

## Davranış Notları

- İçerik çeviri API'leri çeviriyi proje yol yeniden yazımından ayrı tutar. Çevrilmiş içerikte hedef konuma göre proje-bağıl bağlantıların ayarlanması gerektiğinde `rewrite_markdown_paths` veya `rewrite_notebook_paths` açıkça çağrılmalıdır.
- Proje orkestrasyon API'leri dosya keşfi, yazmalar, yol yeniden yazımı, meta veriler, temizleme ve isteğe bağlı feragatnameler dahil içeriğin çevrilmesi etrafında proje davranışı ekler.
- `run_translation` ilerleme ve tahmin özetlerini CLI tarafından kullanılan Rich destekli raporlayıcı aracılığıyla yazdırır. Etkileşimsiz çıktı düz metne geri döner.
- `dry_run=True` sanal README güncellemeleri kullanarak tahminleri hesaplar, ancak README veya çeviri dosyalarını yazmaz.
- `groups` sıralı olarak işlenir. Çalışma başlamadan önce tek bir toplu tahmin yazdırılır.
- Görüntü çevirisi seçildiğinde, eksik Vision yapılandırması çeviri başlamadan önce bir hata yükseltir.
- Mevcut takma ad tabanlı dil klasörleri algılanır ve çalışmanın bir parçası olarak kanonik dil klasörü adlarına taşınabilir.
- `run_review` eksik çevrilmiş dosyalar, eksik veya eskimiş çeviri meta verisi, bozuk Markdown frontmatter/kod çitleri ve geçersiz çevrilmiş not defteri JSON'u durumunda başarısız olur.
- `run_review` varsayılan olarak eksik yerel Markdown ve görüntü bağlantı hedeflerini uyarı olarak raporlar.

## Dahili Çağrı Yolu

API, CLI tarafından kullanılan aynı çekirdek uygulamaya devreder:

Çeviri:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, veya `translate_image_content` bellek içi çeviri için.
2. `co_op_translator.api.translation.rewrite_markdown_paths` veya `rewrite_notebook_paths` açık yol sonrası işleme için.
3. `co_op_translator.api.translation.run_translation` tam proje orkestrasyonu için.
4. `co_op_translator.config.Config`, `LLMConfig`, ve `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Markdown, not defterleri ve görüntüler için odaklanmış proje çeviri karışımları.
8. `co_op_translator.core` altındaki Markdown, not defteri, metin ve görüntü çevirmenleri.

İnceleme:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks` altındaki deterministik kontroller

Aşağıdaki sınıflar bakımcılar için yararlıdır, ancak paket düzeyinde kararlı API olarak dışa aktarılmaz.

| Class | Module | Responsibility |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Proje düzeyinde çeviriyi, dizin yönetimini, dil başına meta veri normalizasyonunu ve Markdown, notebook ve görüntü çevirmenlerine delege etmeyi koordine eder. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, notebook'lar, görüntüler, eskimiş tespiti ve çeviri meta veri güncellemeleri için asenkron dosya işleme çalışmalarını yürütür. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown dosyası okuma, içerik çevirisi, yol yeniden yazımı, meta veriler, feragatnameler ve yazma işlemlerini düzenler. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Not defteri dosyası okuma, Markdown hücresi çevirisi, yol yeniden yazımı, meta veriler, feragatnameler ve yazma işlemlerini düzenler. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Kaynak görüntü keşfini, görüntü çevirisini, çıktı yollarını, meta verileri ve yazma işlemlerini düzenler. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Çevrilmiş Markdown çiftlerini bulur, çeviri kalitesini değerlendirir ve düşük güvenilirlik onarım iş akışları için güven skoruna ait meta verileri okur. |
| `ReviewRunner` | `co_op_translator.review.runner` | Kaynak dosyalar, hedef diller ve yapılandırılmış çeviri kökleri genelinde deterministik inceleme kontrollerini koordine eder. |
| `ReviewTarget` | `co_op_translator.review.targets` | Bir kaynak kökü ve o kök için incelenen çeviri çıktı dizinini tanımlar. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Eski takma ad dil klasörlerini algılar ve kanonik BCP 47 klasör taşıma planları hazırlar. |
| `Config` | `co_op_translator.config.base_config` | `.env` dosyalarını yükler ve gerekli LLM ile isteğe bağlı Vision sağlayıcılarının yapılandırılıp yapılandırılmadığını kontrol eder. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI veya Anthropic'i otomatik algılar, gerekli ortam değişkenlerini doğrular ve sağlayıcı bağlantı kontrolleri çalıştırır. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision yapılandırmasını algılar ve görüntü çevirisi için bağlantı kontrolleri çalıştırır. |