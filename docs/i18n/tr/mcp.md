# MCP Sunucusu

Co-op Translator, ajanlar, düzenleyiciler ve MCP-uyumlu istemciler için bir Model Context Protocol sunucusu içerir.

Varsayılan yerel kurulum için kullanıcıların ayrı bir sunucuyu elle çalıştırmaya devam etmeleri gerekmez. MCP istemcisini yapılandırırlar ve istemci, Co-op Translator araçlarına ihtiyaç duyduğunda `co-op-translator-mcp` işlemine `stdio` üzerinden otomatik olarak başlatır.

CLI, Python API ve MCP arasında karar veriyorsanız, [Çalışma Akışınızı Seçin](workflows.md) ile başlayın.

Bir ajan veya düzenleyici Co-op Translator'a doğrudan çağrı yapmalıysa MCP'yi kullanın:

| Kullanıcı hedefi | MCP araçları |
| --- | --- |
| Bir Markdown belgesini, not defterini veya resmi çevirin | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Host ajan modeli ile Markdown veya not defteri içeriğini çevirin | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Çıktı yolunu seçtikten sonra çevrilmiş Markdown veya not defteri bağlantılarını yeniden yazın | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| CLI gibi tam bir depoyu çevirin | `run_translation`, `translate_project` |
| LLM kimlik bilgileri olmadan çevrilmiş çıktıyı gözden geçirin | `run_review` |
| Yetkinlikleri ve ortam durumunu inceleyin | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

MCP sunucusu, [Python API](api.md) içinde belgelenen aynı genel Python API'sini sarar. Sağlayıcı destekli araçlar, CLI ve Python API ile aynı yapılandırılmış sağlayıcıları kullanır. Ajan destekli araçlar, MCP host ajanının çevirisi için parçaları hazırlar, ardından Co-op Translator'ı kullanarak nihai Markdown veya not defterini yeniden oluşturur.

## Adım 1: Co-op Translator'ı Yükleyin ve Yapılandırın

MCP istemcinizin kullanacağı Python ortamına Co-op Translator'ı yükleyin:

```bash
pip install co-op-translator
```

Bu depodan yerel geliştirme için, paketi düzenlenebilir modda yükleyin:

```bash
pip install -e .
```

MCP istemcinizin kullanacağı çeviri modunu seçin:

| Mod | Şunun için kullanın | Kimlik bilgileri |
| --- | --- | --- |
| Sağlayıcı destekli | Co-op Translator `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` veya `run_translation` çağrılarını yapar. | Markdown ve not defteri çevirileri Azure OpenAI veya OpenAI gerektirir. Resim çevirisi ayrıca Azure AI Vision gerektirir. |
| Ajan destekli | MCP host ajanı, `start_markdown_agent_translation` veya `start_notebook_agent_translation` tarafından döndürülen parçaları çevirir. | Markdown veya not defteri parçaları için Co-op Translator LLM sağlayıcı kimlik bilgileri gerekli değildir. Resim çevirisi henüz ajan destekli mod tarafından kapsanmamaktadır. |

Bir ajan içinde, örneğin Codex veya Claude Code gibi, Markdown veya not defteri çevirisiyle başlıyorsanız ajan destekli modla başlayın. Co-op Translator'ın yapılandırılmış sağlayıcılarınızı çağırmasını istediğinizde, resimleri çevirirken veya CLI gibi depo düzeyi çeviri çalıştırırken sağlayıcı destekli modu kullanın.

Yalnızca sağlayıcı destekli iş akışları için sağlayıcı kimlik bilgilerini yapılandırın:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Sağlayıcı destekli resim çevirisi ek olarak şunları gerektirir:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Ajan destekli mod şu anda Markdown ve not defteri Markdown hücrelerini kapsar. Resim çevirisi hala sağlayıcı destekli görüntü hattını kullanır ve OCR ile düzen bilgisine duyarlı render için Azure AI Vision gerektirir.

## Adım 2: MCP İstemcinizi Yapılandırın

Normal yerel `stdio` kurulumu için Co-op Translator'ı MCP istemci yapılandırmanıza ekleyin. İstemci işlemi otomatik olarak başlatıp durduracaktır.

Yüklü paket yapılandırması:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

Windows üzerinde kaynak kontrol (source checkout) yapılandırması:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

macOS veya Linux üzerinde kaynak kontrol yapılandırması:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

MCP istemci yapılandırmasını değiştirdikten sonra, istemcinin yeni sunucuyu keşfedebilmesi için yeniden başlatın veya yeniden yükleyin.

## Adım 3: İstemcide Sunucuyu Doğrulayın

MCP istemcisinden kullanılabilir araçları listelemesini isteyin veya önce salt-okunur yardımcı araçlardan birini çağırın:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Kullanışlı ilk kontroller:

| Araç | Kontrol edilecekler |
| --- | --- |
| `get_api_overview` | Sunucunun erişilebilir olduğunu doğrular ve kullanılabilir iş akışlarını gösterir. |
| `list_supported_languages` | Paketlenmiş dil verilerinin yüklenebildiğini doğrular. |
| `get_configuration_status` | Gizli değerleri ifşa etmeden LLM ve Vision sağlayıcılarının kullanılabilirliğini doğrular. |

## Adım 4: Bir İş Akışı Seçin

### Bireysel Dosyaları veya Belgeleri Çevirme

MCP istemcisinin zaten belge içeriğine veya bir resim yoluna sahip olduğu ve Co-op Translator'ın yapılandırılmış çeviri sağlayıcılarını çağırması gerektiği durumlarda sağlayıcı destekli içerik araçlarını kullanın.

Markdown için:

1. `document`, `language_code` ve isteğe bağlı olarak `source_path` ile `translate_markdown_content` çağrın.
2. Çevrilmiş sonuç Co-op Translator çıktı düzenine yazılacaksa `rewrite_markdown_paths` çağırın.
3. İstemcinin nihai `content`'i yazmasına veya döndürmesine izin verin.

Not defterleri için:

1. Notebook JSON ile `translate_notebook_content` ve `language_code` çağrın.
2. Çevrilmiş not defteri bağlantılarının hedef yol için ayarlanması gerekiyorsa `rewrite_notebook_paths` çağrın.
3. Nihai not defteri JSON'unu yazın veya döndürün.

Resimler için:

1. `image_path`, `language_code` ve isteğe bağlı `root_dir` veya `fast_mode` ile `translate_image_content` çağrın.
2. Döndürülen `data_base64` ve `mime_type`'ı okuyun.
3. `output_path` sağlanmışsa, çevrilmiş resim ayrıca o yola kaydedilir.

İçerik araçları proje keşfi, meta verilerin güncellenmesi, feragatnameler veya otomatik yol yeniden yazımı yapmaz. Host ajanın Co-op Translator LLM sağlayıcı kimlik bilgisi olmadan Markdown veya not defteri parçalarını çevirmesini istiyorsanız aşağıdaki ajan destekli iş akışını kullanın.

### Host Ajan Modeli ile Çevirme

Co-op Translator için Azure OpenAI veya OpenAI yapılandırmak yerine, host ajanın (örneğin bir kod yardımcı programı) çevrilmiş metni üretmesini istediğinizde ajan destekli araçları kullanın.

Sohbet tabanlı bir MCP istemcisinde genellikle araç JSON'unu kendiniz yazmanız gerekmez. Ajanın ajan destekli iş akışını kullanmasını isteyin:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Not defterleri için aynı deseni kullanın:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

MCP istemciniz sunucu istemlerini destekliyorsa, istemcinin aynı iş akışı talimatlarını yüklemesi için `agent_assisted_markdown_translation_prompt` kullanın.

Markdown için:

1. `document`, `language_code` ve isteğe bağlı `source_path` ile `start_markdown_agent_translation` çağrın.
2. Host ajanda döndürülen her parçayı parça `prompt`unu izleyerek çevirin.
3. Orijinal `job` ve `chunk_id` ile `translated_text` kullanarak çevrilmiş parçalarla `finish_markdown_agent_translation` çağrın.
4. İçerik çevrilmiş hedef yola yazılacaksa `rewrite_markdown_paths` çağrın.

Not defterleri için:

1. Notebook JSON ve `language_code` ile `start_notebook_agent_translation` çağrın.
2. Host ajanda döndürülen her parçayı çevirin.
3. Orijinal `job` ve çevrilmiş parçalarla `finish_notebook_agent_translation` çağrın.
4. Çevrilmiş not defteri bağlantılarının hedef yol ayarlaması gerekiyorsa `rewrite_notebook_paths` çağrın.

Ajan destekli araçlar Co-op Translator'dan Azure OpenAI veya OpenAI çağrısı yapmaz. Döndürülen parçaların çevrilmesinden host ajan sorumludur. Co-op Translator Markdown bölümleme, yer tutucu koruma, frontmatter yeniden oluşturma, not defteri hücresi değişimi ve çeviri sonrası normalizasyon işlemlerini gerçekleştirir.

### Tüm Depoyu Çevirme

Kullanıcı Co-op Translator'ın `translate` CLI'sı gibi davranmasını istediğinde `run_translation` kullanın.

Depo çevirisi varsayılan olarak bir ajanın kapsamı inceleyebilmesi için `dry_run=true` olur:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Yazma izin vermek için çağıran hem `dry_run=false` hem de `confirm_write=true` ayarlamalıdır:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` `run_translation` için uyumluluk takma adı (alias) olarak sunulur.

### Çevrilmiş Çıktıyı İnceleme

LLM veya Vision kimlik bilgileri gerektirmeyen deterministik kontroller için `run_review` kullanın:

!!! note "Beta"
    MCP beta `run_review` API'sini açığa çıkarır. Salt-okunur inceleme iş akışları için güvenlidir, ancak inceleme kontrolleri ve sorun şemaları gelişebilir.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Sonuç, yakalanmış metin çıktısını ve mevcutsa yapılandırılmış bir inceleme özetini içerir.

## Manuel Sunucu Çalıştırmaları

Manuel çalıştırmalar esasen hata ayıklama veya uzun süre çalışan sunucular gibi davranan taşıyıcılar (transports) içindir.

Varsayılan stdio sunucusunu hata ayıklayın:

```bash
co-op-translator-mcp
```

Kaynak kontrolünden çalıştırın:

```bash
python -m co_op_translator.mcp.server
```

Uzun ömürlü bir HTTP veya SSE sunucusu çalıştırın:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Yerel editör ve ajan entegrasyonları için, Adım 2'deki istemci yönetimli `stdio` yapılandırmasını tercih edin.

## Araçlar

| Araç | Amaç | Dosya yazar mı |
| --- | --- | --- |
| `translate_markdown_content` | Bir Markdown stringini çevirir. | Hayır |
| `translate_notebook_content` | Not defteri JSON'undaki Markdown hücrelerini çevirir. | Hayır |
| `translate_image_content` | Bir resimdeki metni çevirir ve base64 resim verisi döndürür. | Opsiyonel, yalnızca `output_path` sağlandığında |
| `start_markdown_agent_translation` | Co-op Translator LLM sağlayıcı kimlik bilgileri olmadan host ajanın çevirmesi için Markdown parçaları hazırlar. | Hayır |
| `finish_markdown_agent_translation` | Host ajan tarafından çevrilmiş parçalarla Markdown'u yeniden oluşturur. | Hayır |
| `start_notebook_agent_translation` | Host ajanın çevirmesi için not defteri Markdown hücresi parçalarını hazırlar. | Hayır |
| `finish_notebook_agent_translation` | Host ajan tarafından çevrilmiş parçalarla not defteri JSON'unu yeniden oluşturur. | Hayır |
| `rewrite_markdown_paths` | Çevrilmiş hedef için Markdown gövdesi ve frontmatter yollarını yeniden yazar. | Hayır |
| `rewrite_notebook_paths` | Not defteri Markdown hücreleri içindeki yolları yeniden yazar. | Hayır |
| `run_translation` | CLI gibi proje düzeyi çeviri çalıştırır. | `dry_run=false` ve `confirm_write=true` olduğunda Evet |
| `translate_project` | `run_translation` için uyumluluk takma adı. | `dry_run=false` ve `confirm_write=true` olduğunda Evet |
| `run_review` | Deterministik inceleme kontrolleri çalıştırır. | Hayır |
| `get_configuration_status` | Gizli bilgileri ifşa etmeden yapılandırılmış LLM ve Vision sağlayıcılarını raporlar. | Hayır |
| `list_supported_languages` | Desteklenen hedef dil kodlarını listeler. | Hayır |
| `get_api_overview` | Kullanılabilir MCP iş akışlarını ve araçlarını açıklar. | Hayır |

## Kaynaklar

| Resource URI | Amaç |
| --- | --- |
| `co-op://api` | İş akışları ve araçların JSON genel görünümü. |
| `co-op://supported-languages` | Desteklenen dil kodlarının JSON listesi. |
| `co-op://configuration` | Gizli bilgileri içermeyen sağlayıcı kullanılabilirlik özetinin JSON'u. |

## İstemler (Prompts)

| Prompt | Amaç |
| --- | --- |
| `translate_markdown_document_prompt` | Bir MCP istemcisini içerik çevirisi ve isteğe bağlı yol yeniden yazımı konusunda yönlendirir. |
| `agent_assisted_markdown_translation_prompt` | MCP istemcisini, Co-op Translator LLM sağlayıcı kimlik bilgileri olmadan host-ajanın Markdown çevirisini yapması için yönlendirir. |
| `translate_repository_prompt` | MCP istemcisini önce dry-run şeklinde depo çevirisi konusunda yönlendirir. |

## Kopyala-Yapıştır Örnekleri

Markdown içeriğini çevirin:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Çevrilmiş Markdown bağlantılarını yeniden yazın:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

Host ajan modeli ile Markdown çevirin:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

Host ajan her döndürülen parçayı çevirdikten sonra işi, `start_markdown_agent_translation` tarafından döndürülen tam `job` nesnesi ile bitirin:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Depo çevirisini önizleyin:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## Sorun Giderme

| Sorun | Denenecekler |
| --- | --- |
| MCP istemcisi `co-op-translator-mcp`'yi bulamıyor. | Mutlak Python yürütülebilir yolunu ve `["-m", "co_op_translator.mcp.server"]` kaynak kontrol yapılandırmasını kullanın. |
| Sunucu listeleniyor ama çeviri başarısız oluyor. | `get_configuration_status` çağırın ve bir LLM sağlayıcısının mevcut olduğunu doğrulayın. |
| Azure OpenAI/OpenAI anahtarları olmadan Markdown veya not defteri çevirisi istiyorsunuz. | Host ajanın parçaları çevirmesi için `start_markdown_agent_translation` / `finish_markdown_agent_translation` veya not defteri eşdeğerlerini kullanın. |
| Resim çevirisi başarısız oluyor. | Azure AI Vision değişkenlerinin ayarlı olduğunu doğrulayın ve `get_configuration_status` çağırın. |
| Depo çevirisi dosyaları yazmıyor. | `dry_run=false` ve `confirm_write=true` yalnızca açık kullanıcı onayından sonra ayarlayın. |
| İstemci yapılandırmasındaki değişiklikler görünmüyor. | MCP istemcisini yeniden başlatın veya yeniden yükleyin. |

## Güvenlik Notları

- MCP araç çağrıları host uygulama tarafından model kontrollüdür, bu nedenle depo çevirisi varsayılan olarak dry-run şeklindedir.
- Tam depo çevirisi birçok dosya oluşturabilir, güncelleyebilir veya kaldırabilir. `confirm_write=true` ayarlamadan önce açık kullanıcı onayı gerektirin.
- Yapılandırma durumu aracı API anahtarları, uç noktalar veya diğer gizli değerleri asla döndürmez.
- Resim çevirisi base64 resim verisi döndürür. Büyük resimler büyük araç yanıtları üretebilir.
- Ajan destekli araçlar kaynak parçaları ve istemleri host MCP ajana döndürür. Bunları yalnızca kullanıcının o içeriği host ajan modeline göndermekten memnun olduğu durumlarda kullanın.