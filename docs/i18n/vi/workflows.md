# Chọn quy trình làm việc của bạn

Co-op Translator có thể được sử dụng theo ba cách: CLI, API Python và Máy chủ MCP. Chúng chia sẻ cùng khả năng dịch, nhưng mỗi cách phù hợp với một quy trình làm việc khác nhau.

Sử dụng trang này khi bạn đang quyết định bắt đầu từ đâu.

## Quyết định nhanh

| Nếu bạn muốn... | Sử dụng | Bắt đầu ở đây |
| --- | --- | --- |
| Dịch hoặc xem xét một kho lưu trữ từ một terminal | CLI | [Tham khảo CLI](cli.md) |
| Thêm bản dịch vào một script Python, dịch vụ, notebook, hoặc công việc CI | API Python | [API Python](api.md) |
| Cho phép một agent, trình soạn thảo, hoặc client tương thích MCP dịch nội dung cho bạn | Máy chủ MCP | [Máy chủ MCP](mcp.md) |
| Dịch một tài liệu Markdown, notebook, hoặc hình ảnh mà ứng dụng của bạn đã tải | API Python hoặc Máy chủ MCP | [API Python](api.md) hoặc [Máy chủ MCP](mcp.md) |
| Dịch toàn bộ kho lưu trữ với các thư mục đầu ra tiêu chuẩn và siêu dữ liệu | CLI hoặc `run_translation` | [Tham khảo CLI](cli.md) hoặc [API Python](api.md) |

## Sử dụng CLI khi

Chọn CLI khi một người hoặc một công việc CI điều khiển việc dịch kho lưu trữ từ một shell.

CLI là con đường trực tiếp nhất khi bạn muốn Co-op Translator tự động phát hiện các tệp dự án, tạo đầu ra đã dịch, giữ nguyên bố cục dự án, cập nhật siêu dữ liệu và chạy các lệnh xem xét.

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

Phù hợp:

- Bạn đang dịch một kho lưu trữ từ terminal.
- Bạn muốn một lệnh có thể lặp lại cho quy trình CI hoặc phát hành.
- Bạn muốn tính năng phát hiện dự án tích hợp sẵn, đường dẫn đầu ra, siêu dữ liệu, dọn dẹp và xem xét.
- Bạn thích giao diện lệnh hơn việc viết mã Python.

## Sử dụng API Python khi

Chọn API Python khi mã của bạn nên kiểm soát quy trình làm việc.

API hữu ích cho các ứng dụng, script tự động hóa, notebook, dịch vụ và đường ống tùy chỉnh. Nó cho phép bạn gọi các API dịch nội dung cấp thấp cho từng tệp, hoặc chạy cùng cơ chế điều phối ở cấp kho lưu trữ được CLI sử dụng.

Dịch một tài liệu Markdown và quyết định nơi lưu nó:

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

Chạy dịch một kho lưu trữ từ Python:

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

Phù hợp:

- Ứng dụng của bạn đã đọc các tệp, bộ đệm, notebook hoặc byte hình ảnh.
- Bạn cần xác thực tùy chỉnh, lưu trữ, ghi nhật ký, thử lại hoặc luồng phê duyệt.
- Bạn muốn dịch một tài liệu, notebook hoặc hình ảnh mà không xử lý toàn bộ kho lưu trữ.
- Bạn muốn dịch kho lưu trữ, nhưng từ tự động hóa Python thay vì một lệnh shell.

## Sử dụng Máy chủ MCP khi

Chọn máy chủ MCP khi một agent, trình soạn thảo, hoặc client tương thích MCP cần gọi các công cụ Co-op Translator.

Trong thiết lập cục bộ thông thường, người dùng không giữ một server chạy thủ công. MCP client khởi chạy `co-op-translator-mcp` qua `stdio` khi cần các công cụ.

Ví dụ các yêu cầu người dùng mà một agent có thể xử lý:

- "Dịch tệp Markdown này sang tiếng Hàn và giữ các liên kết cho đúng."
- "Dịch tệp Markdown này sang tiếng Hàn bằng quy trình MCP có hỗ trợ agent, sử dụng mô hình của bạn cho các đoạn được dịch."
- "Dịch notebook này sang tiếng Hàn, giữ nguyên các ô mã, và sử dụng Co-op Translator MCP để tái tạo notebook."
- "Dịch văn bản trong hình này sang tiếng Nhật và lưu kết quả."
- "Chạy thử (dry-run) dịch kho lưu trữ sang tiếng Tây Ban Nha và cho tôi biết những gì sẽ thay đổi."
- "Xem xét xem đầu ra dịch tiếng Hàn có phải là phiên bản mới nhất hay không."

Đối với Markdown và notebook, MCP có thể hoạt động ở hai chế độ:

| Chế độ | Sử dụng khi | Công cụ chính |
| --- | --- | --- |
| Có trợ giúp của agent | Agent chủ MCP nên dịch các đoạn với mô hình của nó, mà không cần thông tin đăng nhập nhà cung cấp LLM của Co-op Translator. | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Được nhà cung cấp hỗ trợ | Co-op Translator sẽ gọi trực tiếp Azure OpenAI hoặc OpenAI. | `translate_markdown_content`, `translate_notebook_content` |

Cấu trúc lời gọi công cụ Markdown khi MCP được nhà cung cấp hỗ trợ:

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

Cấu trúc lời gọi công cụ hình ảnh MCP:

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

Dịch kho lưu trữ mặc định là chạy thử (dry-run) qua MCP:

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

- Bạn muốn các quy trình dịch bằng ngôn ngữ tự nhiên bên trong một agent hoặc trình soạn thảo.
- Bạn muốn dịch Markdown hoặc notebook nơi mô hình agent chủ dịch các đoạn đã được chuẩn bị.
- Bạn muốn agent dịch nội dung được chọn thay vì toàn bộ kho lưu trữ.
- Bạn muốn có bước phê duyệt trước khi ghi thay đổi trên toàn bộ kho lưu trữ.
- Bạn muốn một giao diện duy nhất cung cấp các công cụ cho Markdown, notebook, hình ảnh, xem xét và viết lại đường dẫn.

## Cách chúng kết hợp

CLI là lựa chọn mặc định tốt nhất cho con người dịch kho lưu trữ. API Python là tốt nhất khi mã của bạn sở hữu quy trình làm việc. Máy chủ MCP là tốt nhất khi một agent hoặc trình soạn thảo sở hữu quy trình làm việc.

Cả ba con đường đều sử dụng cùng một API công khai của Co-op Translator, vì vậy bạn có thể bắt đầu với CLI, tự động hóa bằng Python sau, và phơi bày cùng các khả năng đó cho các client MCP khi bạn cần các quy trình do agent điều khiển.