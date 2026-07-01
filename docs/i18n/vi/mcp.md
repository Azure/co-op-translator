# Máy chủ MCP

Co-op Translator bao gồm một máy chủ Model Context Protocol cho các agent, trình soạn thảo và các client tương thích MCP.

Đối với thiết lập cục bộ mặc định, người dùng không cần giữ một máy chủ riêng chạy bằng tay. Họ cấu hình client MCP của mình, và client sẽ tự động khởi động `co-op-translator-mcp` qua `stdio` khi cần các công cụ của Co-op Translator.

Nếu bạn đang phân vân giữa CLI, Python API và MCP, hãy bắt đầu với [Chọn Quy Trình Làm Việc](workflows.md).

Sử dụng MCP khi một agent hoặc trình soạn thảo nên gọi trực tiếp Co-op Translator:

| Mục tiêu người dùng | Công cụ MCP |
| --- | --- |
| Dịch một tài liệu Markdown, notebook, hoặc hình ảnh | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Dịch nội dung Markdown hoặc notebook bằng mô hình host agent | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Viết lại các liên kết Markdown hoặc notebook đã dịch sau khi chọn đường dẫn đầu ra | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Dịch toàn bộ repository như CLI | `run_translation`, `translate_project` |
| Xem lại đầu ra đã dịch mà không cần thông tin định danh LLM | `run_review` |
| Kiểm tra khả năng và trạng thái môi trường | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Máy chủ MCP bao bọc cùng API Python công khai được tài liệu trong [Python API](api.md). Các công cụ dựa trên nhà cung cấp sử dụng cùng các nhà cung cấp đã cấu hình như CLI và Python API. Các công cụ hỗ trợ bởi agent chuẩn bị các đoạn (chunks) để agent host MCP dịch, sau đó sử dụng Co-op Translator để tái tạo lại Markdown hoặc notebook cuối cùng.

## Bước 1: Cài đặt và Cấu hình Co-op Translator

Cài đặt Co-op Translator trong môi trường Python mà client MCP của bạn sẽ sử dụng:

```bash
pip install co-op-translator
```

Đối với phát triển cục bộ từ repository này, cài gói ở chế độ có thể chỉnh sửa:

```bash
pip install -e .
```

Chọn chế độ dịch mà client MCP của bạn sẽ sử dụng:

| Mode | Dùng cho | Thông tin đăng nhập |
| --- | --- | --- |
| Dựa trên nhà cung cấp | Co-op Translator gọi `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, hoặc `run_translation`. | Dịch Markdown và notebook yêu cầu Azure OpenAI hoặc OpenAI. Dịch ảnh còn yêu cầu Azure AI Vision. |
| Hỗ trợ agent | Agent host MCP dịch các đoạn trả về bởi `start_markdown_agent_translation` hoặc `start_notebook_agent_translation`. | Không yêu cầu thông tin định danh nhà cung cấp LLM của Co-op Translator cho các đoạn Markdown hoặc notebook. Chế độ hỗ trợ agent hiện chưa bao gồm dịch ảnh. |

Nếu bạn bắt đầu với dịch Markdown hoặc notebook bên trong một agent như Codex hoặc Claude Code, hãy bắt đầu với chế độ hỗ trợ agent. Sử dụng chế độ dựa trên nhà cung cấp khi bạn muốn chính Co-op Translator gọi các nhà cung cấp đã cấu hình, khi bạn đang dịch ảnh, hoặc khi bạn chạy dịch ở cấp repository như CLI.

Chỉ cấu hình thông tin định danh nhà cung cấp cho các luồng công việc dựa trên nhà cung cấp:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Dịch ảnh dựa trên nhà cung cấp còn cần thêm:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Chế độ hỗ trợ agent hiện bao gồm các ô Markdown trong notebook. Dịch ảnh vẫn sử dụng pipeline ảnh dựa trên nhà cung cấp và yêu cầu Azure AI Vision cho OCR và kết xuất nhận biết bố cục.

## Bước 2: Cấu hình Client MCP của bạn

Đối với thiết lập `stdio` cục bộ thông thường, thêm Co-op Translator vào cấu hình client MCP của bạn. Client sẽ tự động khởi động và dừng process.

Cấu hình khi cài đặt package:

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

Cấu hình checkout nguồn trên Windows:

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

Cấu hình checkout nguồn trên macOS hoặc Linux:

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

Sau khi thay đổi cấu hình client MCP, khởi động lại hoặc nạp lại client để nó có thể phát hiện máy chủ mới.

## Bước 3: Xác minh Máy chủ trong Client

Yêu cầu client MCP liệt kê các công cụ có sẵn, hoặc gọi một trong các trợ giúp chế độ chỉ đọc trước:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Các kiểm tra ban đầu hữu ích:

| Công cụ | Kiểm tra gì |
| --- | --- |
| `get_api_overview` | Xác nhận máy chủ có thể truy cập và hiển thị các luồng công việc có sẵn. |
| `list_supported_languages` | Xác nhận dữ liệu ngôn ngữ được gói có thể được tải. |
| `get_configuration_status` | Xác nhận khả dụng nhà cung cấp LLM và Vision mà không tiết lộ giá trị bí mật. |

## Bước 4: Chọn Quy Trình Công Việc

### Dịch các Tệp hoặc Tài liệu Riêng lẻ

Sử dụng các công cụ nội dung dựa trên nhà cung cấp khi client MCP đã có sẵn nội dung tài liệu hoặc đường dẫn hình ảnh và Co-op Translator nên gọi các nhà cung cấp dịch đã cấu hình.

Đối với Markdown:

1. Gọi `translate_markdown_content` với `document`, `language_code`, và tuỳ chọn `source_path`.
2. Nếu kết quả dịch sẽ được ghi vào layout đầu ra của Co-op Translator, gọi `rewrite_markdown_paths`.
3. Để client ghi hoặc trả về `content` cuối cùng.

Đối với notebook:

1. Gọi `translate_notebook_content` với JSON notebook và `language_code`.
2. Gọi `rewrite_notebook_paths` nếu các liên kết trong notebook đã dịch cần điều chỉnh cho đường dẫn đích.
3. Ghi hoặc trả về JSON notebook cuối cùng.

Đối với hình ảnh:

1. Gọi `translate_image_content` với `image_path`, `language_code`, và tuỳ chọn `root_dir` hoặc `fast_mode`.
2. Đọc `data_base64` và `mime_type` trả về.
3. Nếu `output_path` được cung cấp, ảnh đã dịch cũng được lưu vào đường dẫn đó.

Các công cụ nội dung không thực hiện khám phá dự án, cập nhật metadata, tuyên bố từ chối trách nhiệm, hoặc viết lại đường dẫn tự động. Nếu bạn muốn agent host dịch các đoạn Markdown hoặc notebook mà không cần thông tin định danh LLM của Co-op Translator, hãy sử dụng luồng công việc hỗ trợ agent bên dưới.

### Dịch với Mô hình Host Agent

Sử dụng các công cụ hỗ trợ agent khi bạn muốn agent host MCP, chẳng hạn như trợ lý lập trình, tạo ra văn bản đã dịch thay vì cấu hình Azure OpenAI hoặc OpenAI cho Co-op Translator.

Trong một client MCP dựa trên chat, bạn thường không cần tự viết JSON công cụ. Yêu cầu agent sử dụng luồng công việc hỗ trợ agent:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

Đối với notebook, sử dụng cùng mẫu:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

Nếu client MCP của bạn hỗ trợ server prompts, hãy sử dụng `agent_assisted_markdown_translation_prompt` để client tải cùng hướng dẫn luồng công việc.

Đối với Markdown:

1. Gọi `start_markdown_agent_translation` với `document`, `language_code`, và tuỳ chọn `source_path`.
2. Dịch từng đoạn trả về trong agent host theo `prompt` của đoạn.
3. Gọi `finish_markdown_agent_translation` với `job` ban đầu và các đoạn đã dịch sử dụng `chunk_id` và `translated_text`.
4. Nếu nội dung sẽ được ghi vào đường dẫn đích đã dịch, gọi `rewrite_markdown_paths`.

Đối với notebook:

1. Gọi `start_notebook_agent_translation` với JSON notebook và `language_code`.
2. Dịch từng đoạn trả về trong agent host.
3. Gọi `finish_notebook_agent_translation` với `job` ban đầu và các đoạn đã dịch.
4. Gọi `rewrite_notebook_paths` nếu các liên kết trong notebook đã dịch cần điều chỉnh theo đường dẫn đích.

Các công cụ hỗ trợ agent không gọi Azure OpenAI hoặc OpenAI từ Co-op Translator. Agent host chịu trách nhiệm dịch các đoạn trả về. Co-op Translator xử lý việc chia đoạn Markdown, bảo toàn chỗ dành (placeholders), tái tạo frontmatter, thay thế ô trong notebook, và chuẩn hoá sau khi dịch.

### Dịch Toàn bộ Repository

Sử dụng `run_translation` khi người dùng muốn Co-op Translator hoạt động giống CLI `translate`.

Dịch repository mặc định là `dry_run=true` để agent có thể kiểm tra phạm vi trước khi thay đổi tệp:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Để cho phép ghi, caller phải đặt cả `dry_run=false` và `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` được phơi bày như một bí danh tương thích cho `run_translation`.

### Xem lại Kết quả Dịch

Sử dụng `run_review` cho các kiểm tra xác định mà không yêu cầu thông tin định danh LLM hoặc Vision:

!!! note "Beta"
    MCP phơi bày API beta `run_review`. API này an toàn cho các luồng làm việc chỉ đọc để xem lại, nhưng các kiểm tra review và schema vấn đề có thể thay đổi.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Kết quả bao gồm đầu ra văn bản được ghi lại và một bản tóm tắt review có cấu trúc khi có sẵn.

## Chạy Máy chủ Thủ công

Chạy thủ công chủ yếu để gỡ lỗi hoặc cho các phương thức truyền mà hoạt động như máy chủ chạy lâu.

Gỡ lỗi máy chủ stdio mặc định:

```bash
co-op-translator-mcp
```

Chạy từ checkout nguồn:

```bash
python -m co_op_translator.mcp.server
```

Chạy một máy chủ HTTP hoặc SSE chạy lâu:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Đối với tích hợp trình soạn thảo và agent cục bộ, ưu tiên cấu hình `stdio` do client quản lý trong Bước 2.

## Công cụ

| Công cụ | Mục đích | Ghi tệp |
| --- | --- | --- |
| `translate_markdown_content` | Dịch một chuỗi Markdown. | Không |
| `translate_notebook_content` | Dịch các ô Markdown trong JSON notebook. | Không |
| `translate_image_content` | Dịch văn bản trong một hình ảnh và trả về dữ liệu ảnh base64. | Tùy chọn, chỉ khi `output_path` được cung cấp |
| `start_markdown_agent_translation` | Chuẩn bị các đoạn Markdown để agent host dịch mà không cần thông tin định danh LLM của Co-op Translator. | Không |
| `finish_markdown_agent_translation` | Tái tạo Markdown từ các đoạn do host-agent dịch. | Không |
| `start_notebook_agent_translation` | Chuẩn bị các đoạn ô Markdown của notebook để agent host dịch. | Không |
| `finish_notebook_agent_translation` | Tái tạo JSON notebook từ các đoạn do host-agent dịch. | Không |
| `rewrite_markdown_paths` | Viết lại nội dung Markdown và các đường dẫn frontmatter cho mục tiêu đã dịch. | Không |
| `rewrite_notebook_paths` | Viết lại các đường dẫn bên trong các ô Markdown của notebook. | Không |
| `run_translation` | Chạy dịch ở cấp dự án giống CLI. | Có khi `dry_run=false` và `confirm_write=true` |
| `translate_project` | Bí danh tương thích cho `run_translation`. | Có khi `dry_run=false` và `confirm_write=true` |
| `run_review` | Chạy các kiểm tra review xác định. | Không |
| `get_configuration_status` | Báo cáo nhà cung cấp LLM và Vision đã cấu hình mà không tiết lộ bí mật. | Không |
| `list_supported_languages` | Liệt kê mã ngôn ngữ đích được hỗ trợ. | Không |
| `get_api_overview` | Mô tả các luồng công việc và công cụ MCP có sẵn. | Không |

## Tài nguyên

| Resource URI | Mục đích |
| --- | --- |
| `co-op://api` | Tổng quan JSON về các luồng công việc và công cụ. |
| `co-op://supported-languages` | Danh sách JSON các mã ngôn ngữ được hỗ trợ. |
| `co-op://configuration` | Tóm tắt khả dụng nhà cung cấp dưới dạng JSON mà không bao gồm bí mật. |

## Lời nhắc

| Lời nhắc | Mục đích |
| --- | --- |
| `translate_markdown_document_prompt` | Hướng dẫn client MCP thông qua việc dịch nội dung và tùy chọn viết lại đường dẫn. |
| `agent_assisted_markdown_translation_prompt` | Hướng dẫn client MCP thông qua việc agent host dịch Markdown mà không cần thông tin định danh LLM của Co-op Translator. |
| `translate_repository_prompt` | Hướng dẫn client MCP thông qua việc dịch repository bắt đầu bằng dry-run. |

## Ví dụ Sao chép-Dán

Dịch nội dung Markdown:

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

Viết lại các liên kết Markdown đã dịch:

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

Dịch Markdown với mô hình host agent:

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

Sau khi agent host dịch từng đoạn trả về, hoàn tất công việc với đối tượng `job` đầy đủ được trả về bởi `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Xem trước bản dịch repository:

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

## Khắc phục sự cố

| Vấn đề | Nên thử |
| --- | --- |
| Client MCP không tìm thấy `co-op-translator-mcp`. | Sử dụng đường dẫn thực thi Python tuyệt đối và cấu hình checkout nguồn `["-m", "co_op_translator.mcp.server"]`. |
| Máy chủ được liệt kê nhưng dịch thất bại. | Gọi `get_configuration_status` và xác nhận nhà cung cấp LLM có sẵn. |
| Bạn muốn dịch Markdown hoặc notebook mà không có khóa Azure OpenAI/OpenAI. | Sử dụng `start_markdown_agent_translation` / `finish_markdown_agent_translation` hoặc các tương đương cho notebook để agent host dịch các đoạn. |
| Dịch ảnh thất bại. | Xác nhận các biến Azure AI Vision đã được đặt và gọi `get_configuration_status`. |
| Dịch repository không ghi tệp. | Đặt `dry_run=false` và `confirm_write=true` chỉ sau khi có sự chấp thuận rõ ràng của người dùng. |
| Thay đổi cấu hình client không hiển thị. | Khởi động lại hoặc nạp lại client MCP. |

## Ghi chú An toàn

- Các cuộc gọi công cụ MCP được điều khiển bởi mô hình ứng dụng host, vì vậy dịch repository mặc định là dry-run.
- Dịch toàn bộ repository có thể tạo, cập nhật hoặc xóa nhiều tệp. Yêu cầu sự chấp thuận rõ ràng của người dùng trước khi đặt `confirm_write=true`.
- Công cụ trạng thái cấu hình không bao giờ trả về API keys, endpoints, hoặc các giá trị bí mật khác.
- Dịch ảnh trả về dữ liệu ảnh base64. Ảnh lớn có thể tạo ra phản hồi công cụ rất lớn.
- Các công cụ hỗ trợ agent trả về các đoạn nguồn và lời nhắc tới host MCP. Chỉ sử dụng chúng với nội dung mà người dùng thoải mái gửi tới mô hình agent host đó.