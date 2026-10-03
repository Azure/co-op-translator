# Máy chủ MCP

Co-op Translator bao gồm một máy chủ Model Context Protocol cho các agent, trình soạn thảo, và các khách hàng tương thích MCP.

Đối với cấu hình cục bộ mặc định, người dùng không cần chạy một máy chủ riêng bằng tay. Họ cấu hình khách hàng MCP của mình, và khách hàng sẽ khởi động `co-op-translator-mcp` tự động qua `stdio` khi cần các công cụ của Co-op Translator.

Nếu bạn đang cân nhắc giữa CLI, Python API và MCP, hãy bắt đầu với [Chọn quy trình làm việc](workflows.md).

Sử dụng MCP khi một agent hoặc trình soạn thảo cần gọi Co-op Translator trực tiếp:

| Mục tiêu người dùng | Công cụ MCP |
| --- | --- |
| Dịch một tài liệu Markdown, notebook, hoặc hình ảnh | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| Dịch nội dung Markdown hoặc notebook bằng mô hình đại lý máy chủ | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Viết lại các liên kết Markdown hoặc notebook đã dịch sau khi chọn đường dẫn đầu ra | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Dịch toàn bộ repository giống như CLI | `run_translation`, `translate_project` |
| Xem lại kết quả dịch mà không cần thông tin đăng nhập LLM | `run_review` |
| Kiểm tra khả năng và trạng thái môi trường | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

Máy chủ MCP bọc cùng một API Python công khai được mô tả trong [Python API](api.md). Các công cụ dựa trên nhà cung cấp sử dụng cùng các nhà cung cấp đã cấu hình như CLI và Python API. Các công cụ hỗ trợ bởi agent chuẩn bị các chunk để agent host MCP dịch, sau đó sử dụng Co-op Translator để tái tạo Markdown hoặc notebook cuối cùng.

## Bước 1: Cài đặt và cấu hình Co-op Translator

Cài đặt Co-op Translator vào môi trường Python mà khách hàng MCP của bạn sẽ sử dụng:

```bash
pip install co-op-translator
```

Đối với phát triển cục bộ từ kho mã này, cài đặt gói ở chế độ chỉnh sửa:

```bash
pip install -e .
```

Chọn chế độ dịch mà khách hàng MCP của bạn sẽ sử dụng:

| Chế độ | Dùng cho | Thông tin đăng nhập |
| --- | --- | --- |
| Dựa trên nhà cung cấp | Co-op Translator gọi `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, hoặc `run_translation`. | Việc dịch yêu cầu Azure OpenAI, OpenAI, hoặc Anthropic. Dịch hình ảnh cũng yêu cầu Azure AI Vision. |
| Hỗ trợ bởi agent | Agent host MCP dịch các chunk trả về bởi `start_markdown_agent_translation` hoặc `start_notebook_agent_translation`. | Không cần thông tin đăng nhập nhà cung cấp LLM cho Co-op Translator để dịch các chunk Markdown hoặc notebook. Dịch hình ảnh hiện chưa được bao phủ bởi chế độ hỗ trợ bởi agent. |

Nếu bạn bắt đầu với việc dịch Markdown hoặc notebook bên trong một agent như Codex hoặc Claude Code, hãy bắt đầu với chế độ hỗ trợ bởi agent. Sử dụng chế độ dựa trên nhà cung cấp khi bạn muốn chính Co-op Translator gọi các nhà cung cấp đã cấu hình, khi bạn dịch hình ảnh, hoặc khi bạn chạy dịch ở cấp repository giống như CLI.

Cấu hình một nhà cung cấp cho các workflow dựa trên nhà cung cấp:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Hoặc OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# Hoặc Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

Việc dịch hình ảnh dựa trên nhà cung cấp còn yêu cầu thêm:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    Chế độ hỗ trợ bởi agent hiện bao phủ Markdown và các ô Markdown trong notebook. Dịch hình ảnh vẫn sử dụng pipeline hình ảnh dựa trên nhà cung cấp và yêu cầu Azure AI Vision cho OCR và render có nhận thức bố cục.

## Bước 2: Cấu hình khách hàng MCP của bạn

Đối với thiết lập cục bộ `stdio` thông thường, thêm Co-op Translator vào cấu hình khách hàng MCP. Khách hàng sẽ tự động khởi động và dừng tiến trình.

Cấu hình khi cài đặt gói:

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

Cấu hình khi kiểm tra mã nguồn trên Windows:

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

Cấu hình khi kiểm tra mã nguồn trên macOS hoặc Linux:

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

Sau khi thay đổi cấu hình khách hàng MCP, khởi động lại hoặc tải lại khách hàng để nó có thể phát hiện máy chủ mới.

## Bước 3: Xác minh máy chủ trong khách hàng

Yêu cầu khách hàng MCP liệt kê các công cụ có sẵn, hoặc gọi một trong các trợ giúp chỉ đọc trước:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

Các kiểm tra ban đầu hữu ích:

| Công cụ | Kiểm tra gì |
| --- | --- |
| `get_api_overview` | Xác nhận máy chủ có thể truy cập được và hiển thị các workflow có sẵn. |
| `list_supported_languages` | Xác nhận dữ liệu ngôn ngữ đóng gói có thể được tải. |
| `get_configuration_status` | Xác nhận tính khả dụng của nhà cung cấp LLM và Vision mà không tiết lộ giá trị bí mật. |

## Bước 4: Chọn một quy trình làm việc

### Dịch các tệp hoặc tài liệu riêng lẻ

Sử dụng các công cụ nội dung dựa trên nhà cung cấp khi khách hàng MCP đã có nội dung tài liệu hoặc đường dẫn hình ảnh và Co-op Translator nên gọi các nhà cung cấp dịch đã cấu hình.

Đối với Markdown:

1. Gọi `translate_markdown_content` với `document`, `language_code`, và tùy chọn `source_path`.
2. Nếu kết quả đã dịch sẽ được ghi vào một layout đầu ra của Co-op Translator, gọi `rewrite_markdown_paths`.
3. Để khách hàng ghi hoặc trả về `content` cuối cùng.

Đối với notebook:

1. Gọi `translate_notebook_content` với JSON notebook và `language_code`.
2. Gọi `rewrite_notebook_paths` nếu các liên kết trong notebook đã dịch cần được điều chỉnh cho một đường dẫn đích.
3. Ghi hoặc trả về JSON notebook cuối cùng.

Đối với hình ảnh:

1. Gọi `translate_image_content` với `image_path`, `language_code`, và tùy chọn `root_dir` hoặc `fast_mode`.
2. Đọc `data_base64` và `mime_type` được trả về.
3. Nếu `output_path` được cung cấp, hình ảnh đã dịch cũng được lưu vào đường dẫn đó.

Các công cụ nội dung không thực hiện phát hiện dự án, cập nhật metadata, từ chối pháp lý, hoặc viết lại đường dẫn tự động. Nếu bạn muốn agent host dịch các chunk Markdown hoặc notebook mà không có thông tin đăng nhập nhà cung cấp LLM cho Co-op Translator, hãy sử dụng workflow hỗ trợ bởi agent bên dưới.

### Dịch với mô hình đại lý máy chủ

Sử dụng các công cụ hỗ trợ bởi agent khi bạn muốn agent host MCP, chẳng hạn một trợ lý lập trình, tạo ra văn bản đã dịch thay vì cấu hình nhà cung cấp LLM cho Co-op Translator.

Trong một khách hàng MCP dựa trên chat, bạn thường không cần tự viết JSON công cụ. Yêu cầu agent sử dụng workflow hỗ trợ bởi agent:

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

Nếu khách hàng MCP của bạn hỗ trợ server prompts, sử dụng `agent_assisted_markdown_translation_prompt` để khách hàng tải cùng các hướng dẫn workflow.

Đối với Markdown:

1. Gọi `start_markdown_agent_translation` với `document`, `language_code`, và tùy chọn `source_path`.
2. Dịch mỗi chunk trả về trong agent host bằng cách theo `prompt` của chunk.
3. Gọi `finish_markdown_agent_translation` với `job` ban đầu và các chunk đã dịch sử dụng `chunk_id` và `translated_text`.
4. Nếu nội dung sẽ được ghi vào một đường dẫn đích đã dịch, gọi `rewrite_markdown_paths`.

Đối với notebook:

1. Gọi `start_notebook_agent_translation` với JSON notebook và `language_code`.
2. Dịch mỗi chunk trả về trong agent host.
3. Gọi `finish_notebook_agent_translation` với `job` ban đầu và các chunk đã dịch.
4. Gọi `rewrite_notebook_paths` nếu các liên kết trong notebook đã dịch cần điều chỉnh đường dẫn đích.

Các công cụ hỗ trợ bởi agent không gọi nhà cung cấp LLM đã cấu hình từ Co-op Translator. Agent host chịu trách nhiệm dịch các chunk được trả về. Co-op Translator xử lý chia chunk Markdown, giữ nguyên placeholder, tái tạo frontmatter, thay thế ô trong notebook, và chuẩn hóa sau dịch.

### Dịch toàn bộ kho mã

Sử dụng `run_translation` khi người dùng muốn Co-op Translator hoạt động giống lệnh `translate` của CLI.

Việc dịch repository mặc định là `dry_run=true` để agent có thể xem xét phạm vi trước khi thay đổi tệp:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

Kết quả `run_translation` bao gồm một mảng `events` với các sự kiện tiến trình có phiên bản
`co-op.translation.event.v1`. Khách hàng MCP nên sử dụng các trường như
`type`, `stage_key`, `completed`, `total`, và `current_path` thay vì
phân tích văn bản console được ghi lại. Truyền `json_events_path` để cũng ghi các sự kiện đó
vào một tệp NDJSON.

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

### Xem lại kết quả dịch

Sử dụng `run_review` cho các kiểm tra có kết quả xác định mà không yêu cầu thông tin đăng nhập LLM hoặc Vision:

!!! note "Beta"
    MCP phơi bày API beta `run_review`. Nó an toàn cho các workflow xem xét chỉ đọc, nhưng các kiểm tra xem xét và schema vấn đề có thể thay đổi.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

Kết quả bao gồm văn bản đầu ra đã ghi và một tóm tắt xem xét có cấu trúc khi có sẵn.

## Chạy máy chủ thủ công

Chạy thủ công chủ yếu để gỡ lỗi hoặc cho các transport hành xử như các máy chủ chạy dài hạn.

Gỡ lỗi máy chủ stdio mặc định:

```bash
co-op-translator-mcp
```

Chạy từ source checkout:

```bash
python -m co_op_translator.mcp.server
```

Chạy một máy chủ HTTP hoặc SSE chạy lâu dài:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

Đối với tích hợp trình soạn thảo cục bộ và agent, ưu tiên cấu hình `stdio` do khách hàng quản lý ở Bước 2.

## Công cụ

| Công cụ | Mục đích | Ghi tệp |
| --- | --- | --- |
| `translate_markdown_content` | Dịch một chuỗi Markdown. | Không |
| `translate_notebook_content` | Dịch các ô Markdown trong JSON notebook. | Không |
| `translate_image_content` | Dịch văn bản trong một hình ảnh và trả về dữ liệu hình ảnh base64. | Tùy chọn, chỉ khi `output_path` được cung cấp |
| `start_markdown_agent_translation` | Chuẩn bị các chunk Markdown để agent host dịch mà không cần thông tin đăng nhập nhà cung cấp LLM của Co-op Translator. | Không |
| `finish_markdown_agent_translation` | Tái cấu trúc Markdown từ các chunk đã dịch bởi agent host. | Không |
| `start_notebook_agent_translation` | Chuẩn bị các chunk ô Markdown trong notebook để agent host dịch. | Không |
| `finish_notebook_agent_translation` | Tái cấu trúc JSON notebook từ các chunk đã dịch bởi agent host. | Không |
| `rewrite_markdown_paths` | Viết lại đường dẫn trong thân và frontmatter Markdown cho một đích đã dịch. | Không |
| `rewrite_notebook_paths` | Viết lại đường dẫn bên trong các ô Markdown của notebook. | Không |
| `run_translation` | Chạy dịch ở cấp dự án giống CLI. | Có khi `dry_run=false` và `confirm_write=true` |
| `translate_project` | Bí danh tương thích cho `run_translation`. | Có khi `dry_run=false` và `confirm_write=true` |
| `run_review` | Chạy các kiểm tra xác định. | Không |
| `get_configuration_status` | Báo cáo các nhà cung cấp LLM và Vision đã cấu hình mà không tiết lộ bí mật. | Không |
| `list_supported_languages` | Liệt kê các mã ngôn ngữ đích được hỗ trợ. | Không |
| `get_api_overview` | Mô tả các workflow và công cụ MCP có sẵn. | Không |

## Tài nguyên

| URI tài nguyên | Mục đích |
| --- | --- |
| `co-op://api` | Tổng quan JSON về các workflow và công cụ. |
| `co-op://supported-languages` | Danh sách JSON các mã ngôn ngữ được hỗ trợ. |
| `co-op://configuration` | Tóm tắt tính khả dụng của nhà cung cấp ở dạng JSON mà không có bí mật. |

## Lời nhắc

| Lời nhắc | Mục đích |
| --- | --- |
| `translate_markdown_document_prompt` | Hướng dẫn một khách hàng MCP qua việc dịch nội dung và viết lại đường dẫn tùy chọn. |
| `agent_assisted_markdown_translation_prompt` | Hướng dẫn một khách hàng MCP qua việc agent host dịch Markdown mà không cần thông tin đăng nhập nhà cung cấp LLM cho Co-op Translator. |
| `translate_repository_prompt` | Hướng dẫn một khách hàng MCP qua việc dịch repository bắt đầu bằng dry-run. |

## Ví dụ sao chép-dán

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
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

Dịch Markdown với mô hình agent host:

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

Sau khi agent host dịch mỗi chunk trả về, hoàn tất công việc với đối tượng `job` đầy đủ được trả về bởi `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

Xem trước việc dịch repository:

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
| Khách hàng MCP không thể tìm thấy `co-op-translator-mcp`. | Sử dụng đường dẫn thực thi Python tuyệt đối và cấu hình source checkout `["-m", "co_op_translator.mcp.server"]`. |
| Máy chủ được liệt kê nhưng việc dịch thất bại. | Gọi `get_configuration_status` và xác nhận có nhà cung cấp LLM khả dụng. |
| Bạn muốn dịch Markdown hoặc notebook mà không có thông tin đăng nhập nhà cung cấp. | Sử dụng `start_markdown_agent_translation` / `finish_markdown_agent_translation` hoặc các tương đương cho notebook để agent host dịch các chunk. |
| Dịch hình ảnh thất bại. | Xác nhận các biến Azure AI Vision đã được thiết lập và gọi `get_configuration_status`. |
| Dịch repository không ghi tệp. | Chỉ đặt `dry_run=false` và `confirm_write=true` sau khi có sự chấp thuận rõ ràng của người dùng. |
| Thay đổi cấu hình khách hàng không xuất hiện. | Khởi động lại hoặc tải lại khách hàng MCP. |

## Ghi chú an toàn

- Các lời gọi công cụ MCP được điều khiển bởi mô hình của ứng dụng chủ, vì vậy việc dịch repository mặc định là chạy thử (dry-run).
- Việc dịch toàn bộ repository có thể tạo, cập nhật, hoặc xóa nhiều tệp. Yêu cầu sự chấp thuận rõ ràng của người dùng trước khi đặt `confirm_write=true`.
- Công cụ trạng thái cấu hình không bao giờ trả về API keys, endpoints, hoặc các giá trị bí mật khác.
- Dịch hình ảnh trả về dữ liệu hình ảnh base64. Hình ảnh lớn có thể tạo ra phản hồi công cụ lớn.
- Các công cụ hỗ trợ bởi agent trả về các chunk nguồn và prompt cho agent host MCP. Chỉ sử dụng chúng với nội dung mà người dùng cảm thấy thoải mái khi gửi tới mô hình agent host đó.