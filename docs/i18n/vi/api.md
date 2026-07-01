# API cho Python

API công khai ổn định cho Python được xuất khẩu từ `co_op_translator.api`. Hầu hết tích hợp sử dụng một trong các quy trình sau:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | Your application reads source content, calls Co-op Translator for translation, and decides where to save the result. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | Your MCP host or application model will translate chunks, while Co-op Translator handles chunking and reconstruction. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | You want the Python API to behave like the CLI and handle discovery, output paths, metadata, cleanup, and writes. | `run_translation` |

Hầu hết các module cấp thấp hơn dưới `core`, `config`, `review`, và `utils` là chi tiết triển khai được các điểm vào API này sử dụng.

Khách hàng MCP sử dụng cùng API công khai thông qua [MCP Server](mcp.md). Sử dụng trang này khi gọi Python trực tiếp, và hướng dẫn MCP khi mở Co-op Translator cho một agent hoặc trình soạn thảo. Nếu bạn đang quyết định giữa CLI, API Python, và MCP, hãy bắt đầu với [Choose Your Workflow](workflows.md).

## Luồng API lần đầu

Bắt đầu ở đây nếu bạn gọi Co-op Translator từ mã Python:

1. Cấu hình nhà cung cấp LLM như mô tả trong [Configuration](configuration.md), trừ khi bạn chỉ chuẩn bị các đoạn Markdown hoặc notebook cho dịch bởi host-agent.
2. Quyết định liệu ứng dụng của bạn có tự quản lý I/O file hay không.
3. Sử dụng các API nội dung khi ứng dụng của bạn đọc và ghi các file riêng lẻ.
4. Sử dụng `run_translation` khi Co-op Translator nên xử lý một repository giống như CLI.
5. Sử dụng `run_review` sau khi dịch nếu bạn cần kiểm tra xác định trong tự động hóa.

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

Sử dụng quy trình này khi bạn đã có một file, buffer trình soạn thảo, payload notebook, yêu cầu MCP, hoặc input pipeline tùy chỉnh. Mã của bạn tự quản lý I/O file:

1. Đọc nội dung nguồn.
2. Gọi một API dịch nội dung.
3. Tùy chọn gọi API viết lại đường dẫn nếu nội dung đã dịch sẽ được ghi vào thư mục dịch của dự án.
4. Lưu hoặc trả về kết quả từ ứng dụng của bạn.

Các API dịch nội dung không chạy khám phá dự án, không ghi metadata, không thêm tuyên bố từ chối trách nhiệm, và không tự động viết lại liên kết.

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

Nếu Markdown đã dịch sẽ không nằm trong bố cục dự án của Co-op Translator, bỏ qua `rewrite_markdown_paths` và lưu chuỗi đã dịch trực tiếp.

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

`translate_notebook_content` dịch các ô Markdown và giữ nguyên các ô không phải Markdown. Việc viết lại đường dẫn chỉ áp dụng cho các ô Markdown.

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

`translate_image_content` đọc hình ảnh nguồn và trả về một `PIL.Image.Image` đã render. Nó không ghi metadata hình ảnh đã dịch.

## Scenario 2: Translate an Entire Repository

Sử dụng quy trình này khi bạn muốn API Python hoạt động giống lệnh `translate` của CLI. `run_translation` khám phá các file được hỗ trợ, dịch các loại nội dung được chọn, viết lại đường dẫn, ghi các file đầu ra, cập nhật metadata, và thực hiện các tác vụ bảo trì dịch như dọn dẹp.

`run_translation` là điểm vào điều phối dự án được ưa thích. `translate_project` được xuất khẩu làm bí danh tương thích với cùng hành vi.

Dịch các file Markdown trong repository hiện tại sang tiếng Hàn và tiếng Nhật:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Chỉ dịch các notebook từ một root dự án cụ thể:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Xem trước khối lượng dịch mà không ghi file:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Dịch nhiều root nội dung trong một lần gọi:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Ghi các bản dịch vào các nhóm đầu ra cụ thể:

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

Sử dụng placeholder theo ngôn ngữ khi mỗi ngôn ngữ nên chứa một thư mục con lồng nhau:

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

Nếu không có `markdown`, `notebook`, hoặc `images` được đặt, API sẽ dịch tất cả các loại được hỗ trợ: Markdown, notebook, và hình ảnh.

## Review Translated Output

`run_review` chạy các kiểm tra dịch xác định mà không cần thông tin đăng nhập LLM hoặc Vision.

!!! note "Beta"
    `run_review` là một API đánh giá xác định ở giai đoạn beta. Nó không gọi nhà cung cấp mô hình hay ghi file, nhưng các schema kiểm tra và issue có thể thay đổi.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Chỉ xem xét các file thay đổi so với một ref cơ sở và in đầu ra theo định dạng GitHub-flavored:

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

## Ví dụ Copy-Paste API

Dịch nội dung Markdown mà không ghi file:

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

Dịch và viết lại liên kết Markdown:

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

Dịch một repository từ Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Dịch nhiều root:

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

Bảo toàn các thuật ngữ trong glossary:

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

## Điểm vào công khai

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

Các API dịch nội dung được thiết kế cho các tích hợp đã có nội dung trong bộ nhớ, chẳng hạn như mở rộng trình soạn thảo, công cụ MCP, bộ xử lý notebook, hoặc pipeline tùy chỉnh.

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Translates Markdown content only. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Translates Markdown cells and preserves non-Markdown cells. It does not rewrite links, write metadata, or append disclaimers. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. Extracts and translates image text, then returns a rendered image. It does not save translated image metadata. |

`translate_markdown_content` và `translate_notebook_content` chấp nhận một `source_path` tùy chọn thông qua các tùy chọn của chúng. Đường dẫn được truyền làm ngữ cảnh cho bộ dịch; các caller vẫn chịu trách nhiệm cho bất kỳ việc viết lại đường dẫn đặc thù dự án nào sau khi dịch.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Cùng các tùy chọn có thể được truyền dưới dạng dictionary:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## Agent-Assisted Translation APIs

Các API hỗ trợ agent không gọi Azure OpenAI hoặc OpenAI từ Co-op Translator. Chúng chuẩn bị các đoạn Markdown hoặc notebook để một host agent dịch, sau đó tái tạo nội dung cuối cùng từ các đoạn đã dịch.

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | Return a self-contained Markdown job with chunks, prompts, and reconstruction state. |
| `finish_markdown_agent_translation` | Reconstruct Markdown from a job and host-agent translated chunks. |
| `start_notebook_agent_translation` | Return a notebook job with Markdown-cell chunks for host-agent translation. |
| `finish_notebook_agent_translation` | Reconstruct notebook JSON while preserving code cells, outputs, and metadata. |

Quy trình này chủ yếu dành cho các host MCP. Nếu bạn cần dịch repository trong môi trường production với Co-op Translator quản lý các cuộc gọi nhà cung cấp, sử dụng `translate_markdown_content`, `translate_notebook_content`, hoặc `run_translation`.

## Path Rewriting APIs

Các API viết lại đường dẫn không thực hiện dịch nào. Chúng cập nhật liên kết và các đường dẫn frontmatter sau khi caller biết đường dẫn nguồn, đường dẫn mục tiêu đã dịch, và bố cục dự án.

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | Rewrites Markdown links and supported frontmatter path fields for a translated target. |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | Applies Markdown path rewriting to each Markdown cell and leaves non-Markdown cells unchanged. |

Đối số `policy` có thể là một dictionary với các trường sau:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | Target language code, such as `"ko"` or `"pt-BR"`. |
| `root_dir` | No | Source project root. Defaults to `"."`. |
| `translations_dir` | No | Text translation output directory. Defaults to `translations` under `root_dir`. |
| `translated_images_dir` | No | Translated image output directory. Defaults to `translated_images` under `root_dir`. |
| `translation_types` | No | Enabled translation types. Defaults to Markdown, notebooks, and images. |
| `lang_subdir` | No | Optional subdirectory under each language folder. |

## Project Translation Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Space-separated target language codes, such as `"ko ja fr"`, or `"all"`. Alias codes are normalized to canonical BCP 47 values. |
| `root_dir` | `str` | `"."` | Project root for a single translation target. Ignored when `root_dirs` or `groups` are supplied. |
| `update` | `bool` | `False` | Delete and recreate existing translations for the selected languages. |
| `images` | `bool` | `False` | Include image translation. Requires Azure AI Vision configuration. |
| `markdown` | `bool` | `False` | Include Markdown translation. |
| `notebook` | `bool` | `False` | Include Jupyter notebook translation. |
| `debug` | `bool` | `False` | Enable debug logging. |
| `save_logs` | `bool` | `False` | Save DEBUG-level log files under the root `logs/` directory. |
| `yes` | `bool` | `True` | Auto-confirm prompts for programmatic and CI usage. |
| `add_disclaimer` | `bool` | `False` | Add machine translation disclaimers to translated Markdown and notebooks. |
| `translations_dir` | `str \| None` | `None` | Custom text translation output directory. Relative paths resolve against each root. |
| `image_dir` | `str \| None` | `None` | Custom translated image output directory. Relative paths resolve against each root. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Multiple roots that share the same output settings. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Explicit `(root_dir, translations_dir)` pairs. Takes precedence over `root_dirs`. |
| `repo_url` | `str \| None` | `None` | Repository URL used when rendering README language table guidance. |
| `glossaries` | `Iterable[str] \| None` | `None` | Glossary terms to preserve during translation. Duplicates and blank terms are normalized. |
| `dry_run` | `bool` | `False` | Estimate translation volume and preview migration behavior without writing files. |

## Tham số Review

`run_review` cố tình mô phỏng chữ ký của `run_translation` ở mức có thể để tự động hóa có thể chuyển đổi giữa quy trình dịch và đánh giá với ít nhánh mã nhất.

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Target language folders to review. Space-separated strings and iterables are accepted. `"all"` reviews every discovered translation language. |
| `root_dir` | `str` | `"."` | Project root for a single review target. Ignored when `root_dirs` or `groups` are supplied. |
| `markdown` | `bool` | `False` | Include Markdown and MDX source files. |
| `notebook` | `bool` | `False` | Include Jupyter notebook source files. |
| `images` | `bool` | `False` | Reserved for parity with translation options. Link references to images are checked from Markdown. |
| `translations_dir` | `str \| None` | `None` | Thư mục đầu ra tùy chỉnh cho bản dịch văn bản. Các đường dẫn tương đối được giải quyết theo từng thư mục gốc. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Nhiều thư mục gốc chia sẻ cùng cài đặt đầu ra. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Cặp rõ ràng `(root_dir, translations_dir)`. Ưu tiên hơn `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Tham chiếu Git dùng để giới hạn việc kiểm tra với các tệp nguồn đã thay đổi. |
| `output_format` | `str` | `"text"` | Định dạng đầu ra của kiểm tra. Các giá trị được hỗ trợ là `"text"` và `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Xem cảnh báo là thất bại bên cạnh các lỗi. |
| `debug` | `bool` | `False` | Bật ghi nhật ký debug. |
| `save_logs` | `bool` | `False` | Lưu các tệp nhật ký ở mức DEBUG dưới thư mục gốc `logs/`. |

Nếu không có `markdown`, `notebook`, hoặc `images` nào được đặt, API sẽ kiểm tra Markdown, notebook, và các tham chiếu liên kết hình ảnh khi có thể. Việc kiểm tra không gọi nhà cung cấp LLM và không yêu cầu khóa API.

## Yêu cầu cấu hình

Các API dịch được hỗ trợ bởi nhà cung cấp yêu cầu cấu hình nhà cung cấp trước khi dịch:

- Dịch Markdown và notebook yêu cầu một nhà cung cấp LLM. Cấu hình Azure OpenAI hoặc OpenAI.
- Dịch hình ảnh yêu cầu Azure AI Vision bên cạnh nhà cung cấp LLM.
- `run_translation` thực hiện các kiểm tra kết nối nhẹ trước khi bắt đầu dịch dự án.
- Các API hỗ trợ bởi agent `start_*_agent_translation` và `finish_*_agent_translation` không gọi nhà cung cấp LLM của Co-op Translator. Ứng dụng chủ hoặc agent MCP dịch các đoạn đã chuẩn bị.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, và `run_review` mang tính quyết định và không yêu cầu thông tin đăng nhập nhà cung cấp.

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` là thao tác có tính xác định và không yêu cầu cấu hình Azure OpenAI, OpenAI, hoặc Azure AI Vision.

## Ghi chú hành vi

- Các API dịch nội dung giữ việc dịch tách biệt với việc viết lại đường dẫn dự án. Gọi `rewrite_markdown_paths` hoặc `rewrite_notebook_paths` một cách rõ ràng khi nội dung đã dịch cần điều chỉnh các liên kết theo vị trí tương đối của dự án cho vị trí đích.
- Các API điều phối dự án thêm các hành vi dự án xung quanh việc dịch nội dung, bao gồm phát hiện tệp, ghi tệp, viết lại đường dẫn, siêu dữ liệu, dọn dẹp và tuyên bố miễn trừ tùy chọn.
- `run_translation` hiển thị tiến độ và tóm tắt ước lượng thông qua Click, khớp với trải nghiệm người dùng CLI.
- `dry_run=True` tính toán ước lượng bằng cách sử dụng cập nhật README ảo, nhưng không ghi README hoặc các tệp dịch.
- `groups` được xử lý tuần tự. Một ước lượng tổng hợp duy nhất được in trước khi công việc bắt đầu.
- Khi chọn dịch hình ảnh, việc thiếu cấu hình Vision sẽ gây lỗi trước khi bắt đầu dịch.
- Các thư mục ngôn ngữ dựa trên bí danh hiện có được phát hiện và có thể được di chuyển sang tên thư mục ngôn ngữ chuẩn như một phần của quá trình chạy.
- `run_review` thất bại khi thiếu các tệp đã dịch, thiếu hoặc siêu dữ liệu dịch lỗi thời, frontmatter/khung mã Markdown bị sai định dạng, và JSON notebook đã dịch không hợp lệ.
- `run_review` báo cáo các mục tiêu liên kết Markdown và hình ảnh cục bộ bị thiếu như cảnh báo theo mặc định.

## Đường dẫn gọi nội bộ

API ủy quyền cho cùng một triển khai lõi được CLI sử dụng:

Dịch:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` cho việc dịch trong bộ nhớ.
2. `co_op_translator.api.translation.rewrite_markdown_paths` hoặc `rewrite_notebook_paths` cho xử lý hậu kỳ đường dẫn rõ ràng.
3. `co_op_translator.api.translation.run_translation` cho điều phối dự án toàn diện.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Các mixin dịch dự án tập trung cho Markdown, notebook, và hình ảnh.
8. Các bộ dịch Markdown, notebook, văn bản và hình ảnh nằm dưới `co_op_translator.core`.

Kiểm tra:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Các kiểm tra có tính xác định dưới `co_op_translator.review.checks`

Các lớp sau hữu ích cho người bảo trì, nhưng không được xuất khẩu như API ổn định cấp gói.

| Lớp | Mô-đun | Trách nhiệm |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Phối hợp dịch cấp dự án, quản lý thư mục, chuẩn hóa siêu dữ liệu theo ngôn ngữ, và ủy quyền cho các bộ dịch Markdown, notebook, và hình ảnh. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Thực hiện công việc xử lý tệp bất đồng bộ cho Markdown, notebook, hình ảnh, phát hiện lỗi thời, và cập nhật siêu dữ liệu dịch. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Điều phối việc đọc tệp Markdown, dịch nội dung, viết lại đường dẫn, siêu dữ liệu, tuyên bố miễn trừ, và ghi tệp. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Điều phối việc đọc tệp notebook, dịch ô Markdown, viết lại đường dẫn, siêu dữ liệu, tuyên bố miễn trừ, và ghi tệp. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Điều phối việc phát hiện hình ảnh nguồn, dịch hình ảnh, đường dẫn đầu ra, siêu dữ liệu, và ghi tệp. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Tìm các cặp Markdown đã dịch, đánh giá chất lượng bản dịch, và đọc siêu dữ liệu độ tin cậy cho quy trình sửa chữa khi độ tin cậy thấp. |
| `ReviewRunner` | `co_op_translator.review.runner` | Phối hợp các kiểm tra đánh giá có tính xác định trên các tệp nguồn, ngôn ngữ đích, và các thư mục gốc dịch đã cấu hình. |
| `ReviewTarget` | `co_op_translator.review.targets` | Mô tả một thư mục nguồn và thư mục đầu ra bản dịch được đánh giá cho thư mục đó. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Phát hiện các thư mục ngôn ngữ bí danh cũ và chuẩn bị kế hoạch di chuyển sang thư mục BCP 47 chính thức. |
| `Config` | `co_op_translator.config.base_config` | Tải các tệp `.env` và kiểm tra xem các nhà cung cấp LLM bắt buộc và Vision tùy chọn đã được cấu hình hay chưa. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Tự động phát hiện Azure OpenAI hoặc OpenAI, xác thực các biến môi trường bắt buộc, và chạy các kiểm tra kết nối nhà cung cấp. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Phát hiện cấu hình Azure AI Vision và chạy các kiểm tra kết nối cho dịch hình ảnh. |