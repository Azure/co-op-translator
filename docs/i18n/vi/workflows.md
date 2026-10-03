# Chọn Luồng Công Việc Của Bạn

Co-op Translator có thể được sử dụng theo ba cách: CLI, Python API, và MCP server. Chúng chia sẻ cùng khả năng dịch, nhưng mỗi cách phù hợp với một quy trình làm việc khác nhau.

Sử dụng trang này khi bạn đang quyết định bắt đầu từ đâu.

**Nếu bạn chỉnh sửa bản dịch bằng tay:** các workflow mặc định của CLI và Actions sẽ dịch lại toàn bộ các tệp nguồn đã thay đổi, vì vậy cách diễn đạt của bạn trong những tệp đó có thể bị ghi đè. Xem xét diff trước khi chấp nhận cập nhật. Để bảo toàn cấp khối Markdown của các chỉnh sửa đã được chấp nhận, hãy sử dụng [nhà cung cấp trạng thái dịch thuật Python tùy chọn](api.md#preserve-accepted-human-edits-with-a-translation-state-provider).

## Quyết Định Nhanh

| Nếu bạn muốn... | Sử dụng | Bắt đầu tại đây |
| --- | --- | --- |
| Dịch hoặc xem lại một kho lưu trữ từ terminal | CLI | [Tham khảo CLI](cli.md) |
| Thêm việc dịch vào một script Python, dịch vụ, notebook, hoặc job CI | Python API | [Python API](api.md) |
| Cho phép một agent, trình soạn thảo, hoặc client tương thích MCP dịch nội dung cho bạn | MCP Server | [MCP Server](mcp.md) |
| Dịch một tài liệu Markdown, notebook, hoặc hình ảnh mà ứng dụng của bạn đã tải | Python API hoặc MCP Server | [Python API](api.md) hoặc [MCP Server](mcp.md) |
| Dịch toàn bộ kho lưu trữ với các thư mục đầu ra và metadata chuẩn | CLI hoặc `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## Sử dụng CLI khi

Chọn CLI khi một người hoặc job CI điều khiển việc dịch kho lưu trữ từ shell.

CLI là con đường trực tiếp nhất khi bạn muốn Co-op Translator phát hiện các tệp dự án, tạo đầu ra đã dịch, giữ nguyên bố cục dự án, cập nhật metadata và chạy các lệnh xem xét.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

Ví dụ này dịch Markdown và notebook. Thêm `-img` chỉ sau khi cấu hình [Azure AI Vision](configuration.md#azure-ai-vision). Đối với lần chạy đầu chỉ với Markdown, làm theo [Bản dịch đầu tiên của bạn](first-translation.md).

Phù hợp:

- Bạn đang dịch một kho lưu trữ từ terminal của mình.
- Bạn muốn một lệnh có thể lặp lại cho các quy trình CI hoặc phát hành.
- Bạn muốn tính năng phát hiện dự án tích hợp, đường dẫn đầu ra, metadata, dọn dẹp và xem xét.
- Bạn thích giao diện lệnh hơn là viết mã Python.

## Sử dụng Python API khi

Chọn Python API khi mã của bạn cần kiểm soát quy trình làm việc.

API hữu ích cho các ứng dụng, script tự động hóa, notebook, dịch vụ và pipeline tùy chỉnh. Nó cho phép bạn gọi các API dịch nội dung cấp thấp cho từng tệp, hoặc chạy cùng orchestration ở cấp kho lưu trữ mà CLI sử dụng.

Dịch một tài liệu Markdown và quyết định lưu nó ở đâu:

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

Chạy việc dịch một kho lưu trữ từ Python:

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

Phù hợp:

- Ứng dụng của bạn đã đọc tệp, bộ đệm, notebook, hoặc byte hình ảnh.
- Bạn cần xác thực tùy chỉnh, lưu trữ, ghi nhật ký, thử lại, hoặc luồng phê duyệt.
- Bạn muốn dịch một tài liệu, notebook, hoặc hình ảnh mà không xử lý toàn bộ kho lưu trữ.
- Bạn muốn dịch kho lưu trữ, nhưng từ tự động hóa Python thay vì lệnh shell.

## Sử dụng MCP Server khi

Chọn MCP server khi một agent, trình soạn thảo, hoặc client tương thích MCP nên gọi các công cụ của Co-op Translator.

Trong cấu hình cục bộ thông thường, người dùng không giữ một server chạy thủ công. MCP client khởi động `co-op-translator-mcp` qua `stdio` khi nó cần các công cụ.

Ví dụ các yêu cầu người dùng mà một agent có thể xử lý:

- "Dịch tệp Markdown này sang tiếng Hàn và giữ các liên kết chính xác."
- "Dịch tệp Markdown này sang tiếng Hàn bằng quy trình MCP hỗ trợ agent, sử dụng mô hình của bạn cho các đoạn được dịch."
- "Dịch notebook này sang tiếng Hàn, giữ nguyên các ô mã, và sử dụng Co-op Translator MCP để tái tạo notebook."
- "Dịch văn bản trong hình này sang tiếng Nhật và lưu kết quả."
- "Chạy thử dịch kho lưu trữ sang tiếng Tây Ban Nha và cho tôi biết sẽ thay đổi gì."
- "Xem xét liệu đầu ra bản dịch tiếng Hàn có được cập nhật hay không."

Đối với Markdown và notebook, MCP có thể hoạt động ở hai chế độ:

| Chế độ | Sử dụng khi | Công cụ chính |
| --- | --- | --- |
| Agent-assisted | Máy chủ agent MCP nên dịch các đoạn bằng mô hình riêng của nó, không cần thông tin xác thực nhà cung cấp LLM của Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator nên gọi trực tiếp Azure OpenAI, OpenAI, hoặc Anthropic. | `translate_markdown_content`, `translate_notebook_content` |

Cấu trúc cuộc gọi công cụ Markdown khi MCP hỗ trợ bởi nhà cung cấp:

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

Cấu trúc cuộc gọi công cụ hình ảnh MCP:

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

Việc dịch kho lưu trữ mặc định là chạy thử (dry-run) qua MCP:

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

Phù hợp:

- Bạn muốn các quy trình dịch bằng ngôn ngữ tự nhiên bên trong agent hoặc trình soạn thảo.
- Bạn muốn dịch Markdown hoặc notebook mà mô hình agent chủ dịch các đoạn đã được chuẩn bị.
- Bạn muốn agent dịch các nội dung được chọn thay vì toàn bộ kho lưu trữ.
- Bạn muốn một bước phê duyệt trước khi ghi trên toàn kho lưu trữ.
- Bạn muốn một giao diện duy nhất cung cấp các công cụ cho Markdown, notebook, hình ảnh, xem xét và viết lại đường dẫn.

## Cách Chúng Phù Hợp Với Nhau

CLI là lựa chọn mặc định tốt nhất cho con người khi dịch kho lưu trữ. Python API là tốt nhất khi mã của bạn sở hữu quy trình làm việc. MCP server là tốt nhất khi một agent hoặc trình soạn thảo sở hữu quy trình làm việc.

Cả ba con đường đều sử dụng cùng một API công khai của Co-op Translator, vì vậy bạn có thể bắt đầu với CLI, tự động hóa bằng Python sau, và phơi bày cùng khả năng đó cho các client MCP khi bạn cần các quy trình làm việc do agent điều khiển.