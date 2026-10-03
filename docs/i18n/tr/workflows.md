# İş Akışınızı Seçin

Co-op Translator üç şekilde kullanılabilir: CLI, Python API ve MCP sunucusu. Aynı çeviri yeteneklerini paylaşırlar, ancak her biri farklı bir iş akışına uygundur.

Nereden başlayacağınıza karar verirken bu sayfayı kullanın.

**Eğer çevirileri elle düzenliyorsanız:** varsayılan CLI ve Actions iş akışları değişen kaynak dosyaları tamamen yeniden çevirir, bu nedenle bu dosyalardaki ifadeleriniz üzerine yazılabilir. Bir güncellemeyi kabul etmeden önce farkı inceleyin. Kabul edilen düzenlemelerin Markdown blok düzeyinde korunması için isteğe bağlı [Python API çeviri durum sağlayıcısını](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) kullanın.

## Hızlı Karar

| Şunu yapmak istiyorsanız... | Kullan | Buradan başlayın |
| --- | --- | --- |
| Bir depoyu terminalden çevirin veya gözden geçirin | CLI | [CLI Referansı](cli.md) |
| Bir Python betiğine, servise, notebook'a veya CI işine çeviri ekleyin | Python API | [Python API](api.md) |
| Bir ajan, editör veya MCP-uyumlu bir istemcinin sizin için içeriği çevirmesini sağlayın | MCP Sunucusu | [MCP Sunucusu](mcp.md) |
| Uygulamanızın zaten yüklediği bir Markdown belgesini, notebook'u veya görüntüyü çevirin | Python API veya MCP Sunucusu | [Python API](api.md) veya [MCP Sunucusu](mcp.md) |
| Standart çıktı klasörleri ve meta verileri ile tüm bir depoyu çevirin | CLI veya `run_translation` | [CLI Referansı](cli.md) veya [Python API](api.md) |

## CLI'yi şu durumlarda kullanın

Bir kişi veya CI işi depoyu bir kabuk üzerinden çeviriyorsa CLI'yi seçin.

Co-op Translator'ın proje dosyalarını keşfetmesini, çevrilmiş çıktılar oluşturmasını, proje düzenini korumasını, meta verileri güncellemesini ve inceleme komutlarını çalıştırmasını istediğinizde CLI en doğrudan yoldur.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Bu örnek Markdown ve notebook'ları çevirir. `-img` öğesini yalnızca [Azure AI Vision](configuration.md#azure-ai-vision) yapılandırıldıktan sonra ekleyin. Yalnızca Markdown içeren ilk çalıştırma için [İlk çeviriniz](first-translation.md) bölümünü izleyin.

Uygun durumlar:

- Bir depoyu terminalinizden çeviriyorsunuz.
- CI veya sürüm iş akışları için yinelenebilir bir komut istiyorsunuz.
- Yerleşik proje keşfi, çıktı yolları, meta veriler, temizlik ve inceleme istiyorsunuz.
- Python kodu yazmaya kıyasla komut arayüzünü tercih ediyorsunuz.

## Python API'yi şu durumlarda kullanın

İş akışını kendi kodunuzun kontrol etmesini istiyorsanız Python API'yi seçin.

API, uygulamalar, otomasyon betikleri, notebook'lar, servisler ve özel boru hatları için kullanışlıdır. Bireysel dosyalar için düşük seviyeli içerik çeviri API'lerini çağırmanıza veya CLI tarafından kullanılan aynı depo düzeyinde orkestrasyonu çalıştırmanıza olanak tanır.

Tek bir Markdown belgesini çevirin ve nereye kaydedeceğinize karar verin:

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

Uygun durumlar:

- Uygulamanız zaten dosyaları, tamponları, notebook'ları veya görüntü baytlarını okuyor.
- Özel doğrulama, depolama, günlükleme, yeniden deneme veya onay akışlarına ihtiyacınız var.
- Tüm bir depoyu işleme koymadan tek bir belgeyi, notebook'u veya görüntüyü çevirmek istiyorsunuz.
- Depo çevirisi istiyorsunuz, ancak bir kabuk komutu yerine Python otomasyonu ile.

## MCP Sunucusunu şu durumlarda kullanın

Bir ajan, editör veya MCP-uyumlu bir istemci Co-op Translator araçlarını çağıracaksa MCP sunucusunu seçin.

Normal yerel kurulumda kullanıcı sunucuyu elle sürekli çalışır durumda tutmaz. MCP istemcisi araçlara ihtiyaç duyduğunda `co-op-translator-mcp`'yi `stdio` üzerinden başlatır.

Bir ajanın kullanıcının isteğini işleyebileceği örnek talepler:

- "Bu Markdown dosyasını Koreceye çevirin ve bağlantıları doğru tutun."
- "Bu Markdown dosyasını ajan destekli MCP iş akışı ile Koreceye çevirin; çevrilen parçalar için kendi modelinizi kullanın."
- "Bu notebook'u Koreceye çevirin, kod hücrelerini koruyun ve notebook'u yeniden oluşturmak için Co-op Translator MCP'yi kullanın."
- "Bu görüntüdeki metni Japoncaya çevirin ve sonucu kaydedin."
- "Bir depo çevirisini İspanyolcaya kuru çalıştırın ve neyin değişeceğini bana söyleyin."
- "Korece çeviri çıktısının güncel olup olmadığını gözden geçirin."

Markdown ve notebook'lar için MCP iki modda çalışabilir:

| Mod | Ne zaman kullanılır | Ana araçlar |
| --- | --- | --- |
| Ajan destekli | MCP ana bilgisayar ajanı, Co-op Translator LLM sağlayıcı kimlik bilgileri olmadan parçaları kendi modeliyle çevirmelidir. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Sağlayıcı destekli | Co-op Translator doğrudan Azure OpenAI, OpenAI veya Anthropic'i çağırmalıdır. | `translate_markdown_content`, `translate_notebook_content` |

MCP sağlayıcı destekli Markdown araç çağrı biçimi:

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

MCP görüntü aracı çağrı biçimi:

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

- Bir ajan veya editör içinde doğal dil çeviri iş akışları istiyorsunuz.
- Ana bilgisayar ajan modelinin hazırlanmış parçaları çevirdiği Markdown veya notebook çevirisi istiyorsunuz.
- Ajanın tüm depo yerine seçili içeriği çevirmesini istiyorsunuz.
- Depo geneli yazılardan önce bir onay adımı istiyorsunuz.
- Markdown, notebook, görüntü, inceleme ve yol-yeniden-yazma araçlarını açığa çıkaran tek bir arayüz istiyorsunuz.

## Birlikte Nasıl Uyum Sağlarlar

CLI, depoları çeviren insanlar için en iyi varsayılandır. Python API, iş akışının kodunuz tarafından yönetilmesi gerektiğinde en iyisidir. MCP sunucusu ise bir ajan veya editör iş akışa sahip olduğunda en uygunudur.

Üç yolun tamamı aynı genel Co-op Translator API'sini kullandığından, CLI ile başlayabilir, daha sonra Python ile otomatikleştirebilir ve ajan odaklı iş akışlarına ihtiyaç duyduğunuzda aynı yetenekleri MCP istemcilerine sunabilirsiniz.