# API Python

API Python công khai ổn định được xuất từ `co_op_translator.api`. Hầu hết các tích hợp sử dụng một trong các quy trình làm việc sau:

| Kịch bản | Sử dụng khi | API chính |
| --- | --- | --- |
| Dịch các tệp hoặc tài liệu riêng lẻ | Ứng dụng của bạn đọc nội dung nguồn, gọi Co-op Translator để dịch, và quyết định nơi lưu kết quả. | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Chuẩn bị nội dung cho dịch bởi host-agent | Máy chủ MCP hoặc mô hình ứng dụng của bạn sẽ dịch các đoạn, trong khi Co-op Translator xử lý phân đoạn và tái tạo. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Dịch toàn bộ một kho lưu trữ | Bạn muốn API Python hoạt động giống CLI và xử lý việc khám phá, đường dẫn đầu ra, metadata, dọn dẹp và ghi tệp. | `run_translation` |

Hầu hết các mô-đun cấp thấp hơn dưới `core`, `config`, `review`, và `utils` là chi tiết triển khai được các điểm nhập API này sử dụng.

Các client MCP sử dụng cùng API công khai thông qua [Máy chủ MCP](mcp.md). Sử dụng trang này khi gọi Python trực tiếp, và hướng dẫn MCP khi mở Co-op Translator cho một agent hoặc trình soạn thảo. Nếu bạn đang quyết định giữa CLI, API Python và MCP, hãy bắt đầu với [Chọn Quy trình làm việc](workflows.md).

## Luồng API lần đầu

Bắt đầu ở đây nếu bạn gọi Co-op Translator từ mã Python:

1. Cấu hình nhà cung cấp LLM như mô tả trong [Cấu hình](configuration.md), trừ khi bạn chỉ đang chuẩn bị các đoạn Markdown hoặc notebook cho dịch bởi host-agent.
2. Quyết định xem ứng dụng của bạn có quản lý I/O tệp hay không.
3. Sử dụng các API nội dung khi ứng dụng của bạn đọc và ghi các tệp riêng lẻ.
4. Sử dụng `run_translation` khi Co-op Translator nên xử lý một kho giống như CLI.
5. Sử dụng `run_review` sau khi dịch nếu bạn cần các kiểm tra xác định trong tự động hóa.

| Mục tiêu | API để bắt đầu |
| --- | --- |
| Dịch một chuỗi hoặc tệp Markdown | `translate_markdown_content` |
| Dịch một payload notebook | `translate_notebook_content` |
| Dịch một hình ảnh | `translate_image_content` |
| Để host agent dịch các đoạn Markdown hoặc notebook | `start_markdown_agent_translation` hoặc `start_notebook_agent_translation` |
| Viết lại liên kết đã dịch sau khi chọn đường dẫn đầu ra | `rewrite_markdown_paths` hoặc `rewrite_notebook_paths` |
| Dịch một kho đầy đủ | `run_translation` |
| Kiểm duyệt kết quả dịch | `run_review` |

## Kịch bản 1: Dịch tệp hoặc tài liệu riêng lẻ

Sử dụng quy trình này khi bạn đã có một tệp, bộ đệm trình soạn thảo, payload notebook, yêu cầu MCP, hoặc đầu vào pipeline tùy chỉnh. Mã của bạn chịu trách nhiệm I/O tệp:

1. Đọc nội dung nguồn.
2. Gọi API dịch nội dung.
3. Tùy chọn gọi API viết lại đường dẫn nếu nội dung đã dịch sẽ được ghi vào thư mục dịch của dự án.
4. Lưu hoặc trả kết quả từ ứng dụng của bạn.

Các API dịch nội dung không chạy khám phá dự án, không ghi metadata, không thêm tuyên bố miễn trừ, và không tự động viết lại liên kết.

### Tệp Markdown

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

Nếu Markdown đã dịch sẽ không nằm trong cấu trúc dự án của Co-op Translator, hãy bỏ qua `rewrite_markdown_paths` và lưu chuỗi đã dịch trực tiếp.

### Tệp Notebook

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

### Tệp hình ảnh

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

`translate_image_content` đọc ảnh nguồn và trả về một `PIL.Image.Image` đã được render. Nó không ghi metadata hình ảnh đã dịch.

## Kịch bản 2: Dịch toàn bộ kho lưu trữ

Sử dụng quy trình này khi bạn muốn API Python hoạt động giống lệnh `translate` của CLI. `run_translation` khám phá các tệp được hỗ trợ, dịch các loại nội dung được chọn, viết lại đường dẫn, ghi tệp đầu ra, cập nhật metadata và thực hiện các tác vụ bảo trì dịch như dọn dẹp.

`run_translation` là điểm vào điều phối dự án được ưa thích. `translate_project` được xuất dưới dạng bí danh tương thích với cùng hành vi.

Dịch các tệp Markdown trong kho hiện tại sang tiếng Hàn và tiếng Nhật:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

Chỉ dịch notebook từ một thư mục gốc dự án cụ thể:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

Xem trước khối lượng dịch mà không ghi tệp:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

Ghi lại các sự kiện tiến trình có cấu trúc cho một tích hợp:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # Lưu payload vào bảng job-event của bạn hoặc truyền trực tiếp nó đến giao diện người dùng của bạn.


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

Events use the versioned schema `co-op.translation.event.v1`. Integrations should
depend on stable fields such as `type` and `stage_key`, not on human-facing
console text or `stage_label`.

Dịch nhiều thư mục nội dung trong một lần gọi:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

Ghi bản dịch vào các nhóm đầu ra cụ thể:

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

Sử dụng một ký hiệu thay thế cho mỗi ngôn ngữ khi mỗi ngôn ngữ nên chứa một thư mục con lồng nhau:

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

Nếu không có `markdown`, `notebook`, hoặc `images` nào được đặt, API sẽ dịch tất cả các loại được hỗ trợ: Markdown, notebooks và images.

### Giữ lại các chỉnh sửa do con người chấp nhận với một TranslationStateProvider

Theo mặc định, Co-op Translator giữ hành vi ở cấp tệp hiện tại của nó: khi một
nguồn Markdown đã lỗi thời, toàn bộ tệp dịch được tạo lại. Các tích hợp được lưu trữ
có thể tùy chọn truyền một `TranslationStateProvider` để bảo tồn các chỉnh sửa do con người
thực hiện trong các khối nguồn chưa thay đổi.

Nhà cung cấp cung cấp cặp nguồn/đích đã được chấp nhận lần cuối và ghi lại mỗi ứng viên mới.
Việc chấp nhận vẫn là trách nhiệm của tích hợp—for example,
sau khi một pull request dịch được hợp nhất:

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

Đối với các tệp Markdown có một baseline đã chấp nhận hợp lệ, Co-op Translator căn chỉnh
các khối Markdown cấp cao. Các khối nguồn không thay đổi tái sử dụng các
khối đã dịch hiện tại, bao gồm các chỉnh sửa do con người thực hiện; các khối nguồn bị thay đổi hoặc thêm mới sẽ được gửi
để dịch; các khối nguồn bị xóa sẽ bị loại bỏ. Nếu việc căn chỉnh không rõ ràng,
cấu trúc đích thay đổi, một bản dịch khối không hợp lệ, hoặc không có cơ sở
sẵn có, Co-op Translator sẽ an toàn quay về
đường dẫn dịch toàn bộ tệp hiện có.

API này lưu trạng thái dịch tài liệu, không phải bộ nhớ dịch cụm từ/phân đoạn xuyên tài liệu.
Nó hiện áp dụng cho dịch dự án Markdown.
Notebook và hành vi hình ảnh không thay đổi. Truyền `update=True`
vẫn yêu cầu tái tạo toàn bộ.

Nếu một hoặc nhiều tệp không thể dịch được, `run_translation` sẽ ném ra một
`RuntimeError` sau khi luồng dự án kết thúc thay vì báo cáo một
chạy thành công nhưng thiếu đầu ra. Các tích hợp nên xem đây là một công việc thất bại
và giữ lại trạng thái dịch đã được chấp nhận trước đó.

## Kiểm duyệt kết quả dịch

`run_review` thực hiện các kiểm tra dịch xác định mà không cần thông tin xác thực LLM hoặc Vision.

!!! note "Beta"
    `run_review` là một API đánh giá xác định bản beta. Nó không gọi nhà cung cấp mô hình hoặc ghi tệp, nhưng các kiểm tra và lược đồ vấn đề có thể thay đổi.

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

Sau khi chỉ dịch README, sử dụng cùng phạm vi để kiểm duyệt:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` chỉ kiểm duyệt `README.md` dưới mỗi thư mục nguồn đã được cấu hình,
bao gồm `groups` tùy chỉnh và các thư mục đầu ra. Các tài liệu khác và README lồng nhau
bị loại trừ. Thiếu README nguồn sẽ gây ra `ValueError`; các kiểm tra dịch không thành công
gây ra `RuntimeError`.

Chỉ kiểm duyệt các tệp thay đổi so với base ref và in đầu ra theo định dạng GitHub:

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

## Ví dụ API để sao chép-dán

Dịch nội dung Markdown mà không ghi tệp:

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

Dịch một kho từ Python:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

Dịch nhiều thư mục gốc:

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

Giữ nguyên thuật ngữ trong bảng thuật ngữ:

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

## API Dịch Nội dung

Các API dịch nội dung dành cho các tích hợp đã có nội dung trong bộ nhớ, chẳng hạn như tiện ích mở rộng trình soạn thảo, công cụ MCP, bộ xử lý notebook, hoặc pipeline tùy chỉnh.

| Hàm | Đầu vào | Đầu ra | I/O tệp | Ghi chú |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Không đồng bộ. Dịch nội dung Markdown thôi. Nó không viết lại liên kết, không ghi metadata, và không thêm tuyên bố miễn trừ. |
| `translate_notebook_content` | Notebook JSON `str` hoặc `dict` | Notebook JSON `str` | No | Không đồng bộ. Dịch các ô Markdown và giữ nguyên các ô không phải Markdown. Nó không viết lại liên kết, không ghi metadata, và không thêm tuyên bố miễn trừ. |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Đồng bộ. Trích xuất và dịch văn bản trong ảnh, sau đó trả về một ảnh đã render. Nó không lưu metadata ảnh đã dịch. |

`translate_markdown_content` và `translate_notebook_content` chấp nhận một `source_path` tùy chọn thông qua các tùy chọn của chúng. Đường dẫn được truyền làm ngữ cảnh cho bộ dịch; người gọi vẫn chịu trách nhiệm cho bất kỳ việc viết lại đường dẫn đặc thù dự án sau khi dịch.

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

Các tùy chọn giống nhau có thể được truyền dưới dạng từ điển:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## API Dịch được Hỗ trợ bởi Agent

Các API hỗ trợ bởi agent không gọi nhà cung cấp LLM đã cấu hình từ Co-op Translator. Chúng chuẩn bị các đoạn Markdown hoặc notebook để host agent dịch, sau đó tái tạo nội dung cuối cùng từ các đoạn đã dịch.

| Hàm | Mục đích |
| --- | --- |
| `start_markdown_agent_translation` | Trả về một công việc Markdown tự chứa với các đoạn, lời nhắc, và trạng thái tái tạo. |
| `finish_markdown_agent_translation` | Tái tạo Markdown từ một công việc và các đoạn đã được host-agent dịch. |
| `start_notebook_agent_translation` | Trả về một công việc notebook với các đoạn ô Markdown cho host-agent dịch. |
| `finish_notebook_agent_translation` | Tái tạo JSON notebook trong khi giữ nguyên các ô mã, output và metadata. |

Quy trình này chủ yếu dành cho các host MCP. Nếu bạn cần dịch kho ở môi trường production với Co-op Translator quản lý các cuộc gọi tới nhà cung cấp, hãy sử dụng `translate_markdown_content`, `translate_notebook_content`, hoặc `run_translation`.

## API Viết lại Đường dẫn

Các API viết lại đường dẫn không thực hiện dịch. Chúng cập nhật liên kết và các đường dẫn frontmatter sau khi người gọi biết đường dẫn nguồn, đường dẫn đích đã dịch, và cấu trúc dự án.

| Hàm | Phạm vi | Ghi chú |
| --- | --- | --- |
| `rewrite_markdown_paths` | Thân Markdown và frontmatter | Viết lại liên kết Markdown và các trường frontmatter đường dẫn được hỗ trợ cho một đích đã dịch. |
| `rewrite_notebook_paths` | Các ô Markdown trong JSON notebook | Áp dụng viết lại đường dẫn Markdown cho mỗi ô Markdown và giữ nguyên các ô không phải Markdown. |

Đối số `policy` có thể là một từ điển với các trường sau:

| Trường | Bắt buộc | Mục đích |
| --- | --- | --- |
| `language_code` | Yes | Mã ngôn ngữ đích, chẳng hạn như `"ko"` hoặc `"pt-BR"`. |
| `root_dir` | No | Thư mục gốc dự án nguồn. Mặc định là `"."`. |
| `translations_dir` | No | Thư mục đầu ra dịch văn bản. Mặc định là `translations` dưới `root_dir`. |
| `translated_images_dir` | No | Thư mục đầu ra ảnh đã dịch. Mặc định là `translated_images` dưới `root_dir`. |
| `translation_types` | No | Các loại dịch được bật. Mặc định là Markdown, notebooks, và images. |
| `lang_subdir` | No | Thư mục con tùy chọn dưới mỗi thư mục ngôn ngữ. |

## Tham số Dịch Dự án

| Tham số | Kiểu | Mặc định | Mục đích |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | Mã ngôn ngữ đích cách nhau bằng dấu cách, chẳng hạn `"ko ja fr"`, hoặc `"all"`. Các mã bí danh được chuẩn hóa về giá trị BCP 47 chuẩn. |
| `root_dir` | `str` | `"."` | Thư mục gốc dự án cho một mục tiêu dịch duy nhất. Bị bỏ qua khi `root_dirs` hoặc `groups` được cung cấp. |
| `update` | `bool` | `False` | Xóa và tạo lại các bản dịch hiện có cho các ngôn ngữ được chọn. |
| `images` | `bool` | `False` | Bao gồm dịch hình ảnh. Yêu cầu cấu hình Azure AI Vision. |
| `markdown` | `bool` | `False` | Bao gồm dịch Markdown. |
| `notebook` | `bool` | `False` | Bao gồm dịch Jupyter notebook. |
| `debug` | `bool` | `False` | Bật ghi log ở chế độ debug. |
| `save_logs` | `bool` | `False` | Lưu các tệp log cấp DEBUG dưới thư mục gốc `logs/`. |
| `yes` | `bool` | `True` | Tự động xác nhận các lời nhắc cho việc sử dụng theo chương trình và CI. |
| `add_disclaimer` | `bool` | `False` | Thêm tuyên bố từ chối trách nhiệm cho bản dịch máy vào Markdown và notebook. |
| `translations_dir` | `str \| None` | `None` | Thư mục đầu ra tùy chỉnh cho bản dịch văn bản. Các đường dẫn tương đối được giải quyết dựa trên mỗi thư mục gốc. |
| `image_dir` | `str \| None` | `None` | Thư mục đầu ra tùy chỉnh cho ảnh đã dịch. Các đường dẫn tương đối được giải quyết dựa trên mỗi thư mục gốc. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Nhiều thư mục gốc chia sẻ cùng cài đặt đầu ra. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Các cặp rõ ràng `(root_dir, translations_dir)`. Ưu tiên hơn `root_dirs`. |
| `repo_url` | `str \| None` | `None` | URL kho lưu trữ được sử dụng khi hiển thị hướng dẫn bảng ngôn ngữ trong README. |
| `glossaries` | `Iterable[str] \| None` | `None` | Các thuật ngữ trong bảng chú giải cần được giữ nguyên khi dịch. Các mục trùng lặp và trống sẽ được chuẩn hóa. |
| `dry_run` | `bool` | `False` | Ước tính khối lượng dịch và xem trước hành vi di chuyển mà không ghi tệp. |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | Bộ điều hợp lưu trữ tùy chọn cho accepted-baseline và candidate để cập nhật Markdown theo từng bước. Nếu bỏ qua, sẽ giữ hành vi hiện tại là cập nhật toàn file. |

## Tham số đánh giá

`run_review` cố ý phản chiếu chữ ký của `run_translation` khi có thể để tự động hóa có thể chuyển giữa các luồng công việc dịch và đánh giá với sự phân nhánh tối thiểu.

| Tham số | Kiểu | Mặc định | Mục đích |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | Các thư mục ngôn ngữ mục tiêu để đánh giá. Chấp nhận chuỗi phân tách bằng dấu cách và iterable. `"all"` đánh giá mọi ngôn ngữ dịch được tìm thấy. |
| `root_dir` | `str` | `"."` | Thư mục gốc dự án cho một mục tiêu đánh giá duy nhất. Bị bỏ qua khi `root_dirs` hoặc `groups` được cung cấp. |
| `markdown` | `bool` | `False` | Bao gồm các tệp nguồn Markdown và MDX. |
| `notebook` | `bool` | `False` | Bao gồm các tệp nguồn Jupyter notebook. |
| `images` | `bool` | `False` | Dự trữ để tương ứng với các tuỳ chọn dịch. Tham chiếu liên kết đến hình ảnh được kiểm tra từ Markdown. |
| `translations_dir` | `str \| None` | `None` | Thư mục đầu ra tùy chỉnh cho bản dịch văn bản. Các đường dẫn tương đối được giải quyết dựa trên mỗi thư mục gốc. |
| `root_dirs` | `Iterable[str] \| None` | `None` | Nhiều thư mục gốc chia sẻ cùng cài đặt đầu ra. |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | Các cặp rõ ràng `(root_dir, translations_dir)`. Ưu tiên hơn `root_dirs`. |
| `changed_from` | `str \| None` | `None` | Tham chiếu Git được sử dụng để giới hạn đánh giá chỉ những tệp nguồn đã thay đổi. |
| `readme_only` | `bool` | `False` | Chỉ đánh giá `README.md` dưới mỗi thư mục nguồn. Thiếu README nguồn sẽ gây ra `ValueError`. |
| `output_format` | `str` | `"text"` | Định dạng đầu ra của đánh giá. Các giá trị hỗ trợ là `"text"` và `"github"`. |
| `fail_on_warnings` | `bool` | `False` | Xem cảnh báo là thất bại ngoài các lỗi. |
| `debug` | `bool` | `False` | Bật ghi nhật ký debug. |
| `save_logs` | `bool` | `False` | Lưu các tệp nhật ký mức DEBUG dưới thư mục gốc `logs/`. |

Nếu không có tùy chọn `markdown`, `notebook`, hoặc `images` nào được bật, API sẽ đánh giá Markdown, notebook và các tham chiếu liên kết hình ảnh khi có thể. Đánh giá không gọi nhà cung cấp LLM và không yêu cầu khóa API.

## Yêu cầu cấu hình

Các API dịch dựa trên nhà cung cấp yêu cầu cấu hình nhà cung cấp trước khi dịch:

- Dịch Markdown và notebook yêu cầu một nhà cung cấp LLM. Cấu hình Azure OpenAI, OpenAI, hoặc Anthropic.
- Dịch ảnh yêu cầu Azure AI Vision bên cạnh nhà cung cấp LLM.
- `run_translation` chạy các kiểm tra kết nối nhẹ trước khi bắt đầu dịch dự án.
- Các API hỗ trợ bởi agent `start_*_agent_translation` và `finish_*_agent_translation` không gọi các nhà cung cấp LLM của Co-op Translator. Ứng dụng chủ hoặc agent MCP sẽ dịch các đoạn đã chuẩn bị.
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, và `run_review` có hành vi xác định và không yêu cầu thông tin xác thực nhà cung cấp.

Các biến bắt buộc cho Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Các biến bắt buộc cho OpenAI:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Các biến bắt buộc cho Anthropic:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` và `ANTHROPIC_MAX_TOKENS` là tùy chọn. Microsoft Agent Framework là client mô hình mặc định cho tất cả nhà cung cấp bắt đầu từ Co-op Translator 0.22.0. Semantic Kernel vẫn có thể được chọn tạm thời với `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"`, nhưng làm vậy sẽ phát ra cảnh báo ngưng hỗ trợ; xem [configuration](configuration.md#model-client-backend) để biết kế hoạch loại bỏ theo giai đoạn.

Các biến bắt buộc của Azure AI Vision cho việc dịch ảnh:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` có hành vi xác định và không yêu cầu cấu hình LLM hay Azure AI Vision.

## Ghi chú về hành vi

- Các API dịch nội dung giữ việc dịch tách biệt khỏi việc viết lại đường dẫn dự án. Gọi `rewrite_markdown_paths` hoặc `rewrite_notebook_paths` một cách rõ ràng khi nội dung đã dịch cần điều chỉnh các liên kết theo đường dẫn tương đối của dự án cho vị trí mục tiêu.
- Các API điều phối dự án thêm hành vi ở mức dự án xung quanh việc dịch nội dung, bao gồm tìm tệp, ghi tệp, viết lại đường dẫn, metadata, dọn dẹp, và các tuyên bố miễn trừ tùy chọn.
- `run_translation` in ra tiến trình và tóm tắt ước tính thông qua cùng bộ báo cáo dựa trên Rich được CLI sử dụng. Đầu ra không tương tác sẽ quay về dạng văn bản thuần.
- `dry_run=True` tính toán ước lượng bằng cách sử dụng cập nhật README ảo, nhưng không ghi README hoặc các tệp dịch.
- `groups` được xử lý theo trình tự. Một ước lượng tổng hợp duy nhất được in trước khi công việc bắt đầu.
- Khi chọn dịch ảnh, thiếu cấu hình Vision sẽ gây lỗi trước khi bắt đầu dịch.
- Các thư mục ngôn ngữ hiện có dựa trên bí danh được phát hiện và có thể được di chuyển sang tên thư mục ngôn ngữ chuẩn như một phần của lần chạy.
- `run_review` sẽ thất bại khi thiếu các tệp đã dịch, metadata dịch bị thiếu hoặc lỗi thời, frontmatter/fence code Markdown bị hỏng, và JSON notebook đã dịch không hợp lệ.
- `run_review` báo cáo các mục tiêu liên kết Markdown và hình ảnh địa phương bị thiếu như cảnh báo theo mặc định.

## Đường dẫn gọi nội bộ

API ủy quyền cho cùng một triển khai lõi được CLI sử dụng:

Dịch:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` cho dịch trong bộ nhớ.
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` cho xử lý hậu kỳ đường dẫn rõ ràng.
3. `co_op_translator.api.translation.run_translation` cho điều phối dự án toàn diện.
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. Các mixin dịch dự án tập trung cho Markdown, notebook, và hình ảnh.
8. Các bộ dịch Markdown, notebook, văn bản và hình ảnh dưới `co_op_translator.core`.

Đánh giá:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. Kiểm tra có hành vi xác định dưới `co_op_translator.review.checks`

Các lớp sau hữu ích cho người duy trì, nhưng không được xuất ra như API ổn định ở cấp gói.

| Lớp | Mô-đun | Trách nhiệm |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | Điều phối dịch ở mức dự án, quản lý thư mục, chuẩn hóa metadata theo ngôn ngữ, và phân công cho các bộ dịch Markdown, notebook, và hình ảnh. |
| `TranslationManager` | `co_op_translator.core.project.translation` | Thực hiện công việc xử lý tệp bất đồng bộ cho Markdown, notebook, hình ảnh, phát hiện lỗi thời, và cập nhật metadata dịch. |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Điều phối việc đọc tệp Markdown, dịch nội dung, viết lại đường dẫn, metadata, tuyên bố miễn trừ, và ghi tệp. |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | Điều phối việc đọc tệp notebook, dịch các ô Markdown, viết lại đường dẫn, metadata, tuyên bố miễn trừ, và ghi tệp. |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | Điều phối việc tìm nguồn hình ảnh, dịch hình ảnh, đường dẫn đầu ra, metadata, và ghi tệp. |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | Tìm các cặp Markdown đã dịch, đánh giá chất lượng dịch, và đọc metadata độ tin cậy cho các luồng sửa chữa khi độ tin cậy thấp. |
| `ReviewRunner` | `co_op_translator.review.runner` | Điều phối các kiểm tra đánh giá có hành vi xác định trên các tệp nguồn, ngôn ngữ mục tiêu, và các thư mục gốc dịch đã cấu hình. |
| `ReviewTarget` | `co_op_translator.review.targets` | Mô tả một thư mục nguồn và thư mục đầu ra dịch được đánh giá cho thư mục đó. |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | Phát hiện các thư mục ngôn ngữ bí danh cũ và chuẩn bị kế hoạch di chuyển sang tên thư mục BCP 47 chuẩn. |
| `Config` | `co_op_translator.config.base_config` | Tải các tệp `.env` và kiểm tra xem các nhà cung cấp LLM bắt buộc và Vision tùy chọn có được cấu hình hay không. |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Tự động phát hiện Azure OpenAI, OpenAI, hoặc Anthropic, xác thực các biến môi trường bắt buộc, và chạy kiểm tra kết nối với nhà cung cấp. |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Phát hiện cấu hình Azure AI Vision và chạy kiểm tra kết nối cho dịch ảnh. |