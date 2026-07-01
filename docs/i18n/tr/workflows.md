# İş Akışınızı Seçin

Co-op Translator üç şekilde kullanılabilir: CLI, Python API ve MCP sunucusu. Hepsi aynı çeviri yeteneklerini paylaşır, ancak her biri farklı bir iş akışına uygundur.

Nereden başlayacağınıza karar verirken bu sayfayı kullanın.

## Hızlı Karar

| Eğer yapmak istiyorsanız... | Kullan | Buradan başlayın |
| --- | --- | --- |
| Bir depoyu terminalden çevirmek veya gözden geçirmek | CLI | [CLI Referansı](cli.md) |
| Bir Python betiğine, servise, notebook'a veya CI görevine çeviri eklemek | Python API | [Python API](api.md) |
| Bir ajanın, editörün veya MCP-uyumlu bir istemcinin içeriği sizin için çevirmesine izin verin | MCP Sunucusu | [MCP Sunucusu](mcp.md) |
| Uygulamanızın zaten yüklediği bir Markdown belgesini, notebook'u veya resmi çevirin | Python API veya MCP Sunucusu | [Python API](api.md) veya [MCP Sunucusu](mcp.md) |
| Standart çıktı klasörleri ve meta verilerle tüm bir depoyu çevirin | CLI veya `run_translation` | [CLI Referansı](cli.md) veya [Python API](api.md) |

## CLI'yi kullanın

Bir kişi veya CI işi çeviri işlemini bir kabuktan yürütüyorsa CLI'yi seçin.

Co-op Translator'ın proje dosyalarını keşfetmesini, çevrilmiş çıktılar oluşturmasını, proje düzenini korumasını, meta verileri güncellemesini ve inceleme komutlarını çalıştırmasını istediğinizde CLI en doğrudan yoldur.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Uygun durumlar:

- Bir depoyu terminalinizden çeviriyorsunuz.
- CI veya yayın iş akışları için tekrarlanabilir bir komut istiyorsunuz.
- Yerleşik proje keşfi, çıktı yolları, meta veriler, temizlik ve inceleme istiyorsunuz.
- Python kodu yazmak yerine komut satırı arayüzünü tercih ediyorsunuz.

## Python API'yi kullanın

Kendi kodunuz iş akışını kontrol etmeliyse Python API'yi seçin.

API, uygulamalar, otomasyon betikleri, notebook'lar, servisler ve özel boru hatları için kullanışlıdır. Bireysel dosyalar için düşük seviyeli içerik çeviri API'lerini çağırmanıza veya CLI tarafından kullanılan aynı depo düzeyindeki orkestrasyonu Python'dan çalıştırmanıza olanak tanır.

Bir Markdown belgesini çevirin ve nereye kaydedeceğinize karar verin:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


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
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Python'dan bir depo çevirisi çalıştırın:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

Uygun durumlar:

- Uygulamanız zaten dosyaları, tamponları, notebook'ları veya resim baytlarını okuyor.
- Özel doğrulama, depolama, günlük kaydı, yeniden deneme veya onay akışlarına ihtiyacınız var.
- Tüm depoyu işlemeye gerek kalmadan tek bir belgeyi, notebook'u veya resmi çevirmek istiyorsunuz.
- Depo çevirisini istiyorsunuz, ancak bir kabuk komutu yerine Python otomasyonu aracılığıyla.

## MCP Sunucusunu kullanın

Bir ajan, editör veya MCP-uyumlu bir istemci Co-op Translator araçlarını çağırmalıysa MCP sunucusunu seçin.

Normal yerel kurulumda kullanıcı manuel olarak bir sunucuyu çalışır durumda tutmaz. MCP istemcisi araçlara ihtiyaç duyduğunda `co-op-translator-mcp`'yi `stdio` üzerinden başlatır.

Bir ajanın ele alabileceği örnek kullanıcı istekleri:

- "Bu Markdown dosyasını Korece'ye çevirin ve bağlantıları doğru tutun."
- "Bu Markdown dosyasını ajan destekli MCP iş akışıyla Korece'ye çevirin; çevirilen parçalar için kendi modelinizi kullanın."
- "Bu notebook'u Korece'ye çevirin, kod hücrelerini koruyun ve notebook'u yeniden oluşturmak için Co-op Translator MCP'yi kullanın."
- "Bu resimdeki metni Japoncaya çevirin ve sonucu kaydedin."
- "Bir depo çevirisini İspanyolca için kuru çalıştırın ve neyin değişeceğini bana söyleyin."
- "Korece çeviri çıktısının güncel olup olmadığını gözden geçirin."

Markdown ve notebook'lar için, MCP iki modda çalışabilir:

| Mod | Ne zaman kullanılır | Ana araçlar |
| --- | --- | --- |
| Ajan destekli | MCP ana bilgisayar ajanı parçaları kendi modeliyle çevirmeli, Co-op Translator LLM sağlayıcı kimlik bilgileri olmadan. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Sağlayıcı destekli | Co-op Translator doğrudan Azure OpenAI veya OpenAI'ı çağırmalıdır. | `translate_markdown_content`, `translate_notebook_content` |

MCP sağlayıcı destekli Markdown araç çağrısı şekli:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP resim aracı çağrısı şekli:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

Depo çevirisi MCP üzerinden varsayılan olarak kuru çalıştırılır:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

Uygun durumlar:

- Bir ajan veya düzenleyici içinde doğal dil çeviri iş akışları istiyorsunuz.
- Ana bilgisayar ajan modelinin hazırlanmış parçaları çevirdiği Markdown veya notebook çevirisi istiyorsunuz.
- Ajanın tüm depo yerine seçili içeriği çevirmesini istiyorsunuz.
- Depo genelinde yazma işlemlerinden önce bir onay adımı istiyorsunuz.
- Markdown, notebook, resim, inceleme ve yol yeniden yazma araçlarını sunan tek bir arayüz istiyorsunuz.

## Birlikte Nasıl Uyum Sağlarlar

CLI, depoları çeviren insanlar için en iyi varsayılan seçenektir. Python API, iş akışına kodunuzun sahip olduğu durumlarda en iyisidir. MCP sunucusu, bir ajan veya editör iş akışa sahip olduğunda en iyisidir.

Üç yolun tamamı aynı genel Co-op Translator API'sini kullandığından, CLI ile başlayabilir, daha sonra Python ile otomatikleştirebilir ve gerektiğinde ajan tarafından yönlendirilen iş akışları için aynı yetenekleri MCP istemcilerine açabilirsiniz.