# Tham chiếu CLI

Co-op Translator cài các điểm vào dòng lệnh sau:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Các lệnh `translate`, `evaluate`, `migrate-links`, và `co-op-review` được chuyển qua `co_op_translator.__main__`, vốn chọn triển khai lệnh dựa trên tên script được gọi. Máy chủ MCP sử dụng trực tiếp `co_op_translator.mcp.server`.

Nếu bạn đang phân vân giữa CLI, Python API, và MCP, hãy bắt đầu với [Chọn quy trình làm việc của bạn](workflows.md).

## Luồng CLI lần đầu

Bắt đầu ở đây nếu bạn đang sử dụng Co-op Translator từ terminal:

1. Cấu hình một nhà cung cấp LLM như mô tả trong [Cấu hình](configuration.md).
2. Chọn loại nội dung bạn muốn dịch.
3. Chạy một lệnh tập trung trước, chẳng hạn như chỉ dịch Markdown.
4. Sử dụng `--dry-run` trước khi thay đổi lớn trong kho lưu trữ.
5. Dùng `co-op-review` sau khi dịch để kiểm tra cấu trúc và tính cập nhật.

| Mục tiêu | Lệnh để bắt đầu |
| --- | --- |
| Dịch tài liệu Markdown | `translate -l "ko" -md` |
| Dịch notebook | `translate -l "ko" -nb` |
| Dịch văn bản trong hình ảnh | `translate -l "ko" -img` |
| Xem trước công việc mà không ghi file | `translate -l "ko" -md --dry-run` |
| Xem lại các bản dịch hiện có | `co-op-review -l "ko"` |
| Cập nhật liên kết notebook và Markdown | `migrate-links -l "ko" --dry-run` |
| Mở công cụ cho client MCP | Cấu hình [Máy chủ MCP](mcp.md) thay vì chạy các lệnh CLI trực tiếp. |

## translate

Dịch các tệp Markdown, notebook và văn bản trong hình ảnh sang một hoặc nhiều ngôn ngữ đích.

```bash
translate -l "ko ja fr"
```

### Ví dụ phổ biến

Chỉ dịch Markdown:

```bash
translate -l "de" -md
```

Chỉ dịch notebook:

```bash
translate -l "zh-CN" -nb
```

Dịch Markdown và hình ảnh:

```bash
translate -l "pt-BR" -md -img
```

Cập nhật các bản dịch hiện có bằng cách xóa và tạo lại chúng:

```bash
translate -l "ko" -u
```

Chạy mà không có lời nhắc tương tác:

```bash
translate -l "ko ja" -md -y
```

Lưu nhật ký:

```bash
translate -l "ko" -s
```

### Tùy chọn

| Tùy chọn | Bắt buộc | Mô tả |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Mã ngôn ngữ cách nhau bằng khoảng trắng, chẳng hạn `"es fr de"`, hoặc `"all"`. |
| `-r`, `--root-dir` | No | Thư mục gốc dự án. Mặc định là thư mục hiện tại. |
| `-u`, `--update` | No | Xóa các bản dịch hiện có cho các ngôn ngữ đã chọn và tạo lại chúng. |
| `-img`, `--images` | No | Chỉ dịch các tệp hình ảnh. |
| `-md`, `--markdown` | No | Chỉ dịch các tệp Markdown. |
| `-nb`, `--notebook` | No | Chỉ dịch các tệp Jupyter notebook. |
| `-d`, `--debug` | No | Bật ghi nhật ký debug trên console. |
| `-s`, `--save-logs` | No | Lưu nhật ký mức DEBUG vào `<root-dir>/logs/`. |
| `-x`, `--fix` | No | Dịch lại các tệp Markdown có độ tin cậy thấp dựa trên kết quả đánh giá trước đó. |
| `-c`, `--min-confidence` | No | Ngưỡng độ tin cậy cho `--fix`. Mặc định là `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | No | Thêm hoặc bỏ ghi chú về dịch máy. Mặc định được bật trong CLI. |
| `-f`, `--fast` | No | Chế độ hình ảnh nhanh (không còn được dùng). |
| `-y`, `--yes` | No | Tự động xác nhận lời nhắc, hữu ích trong CI. |
| `--repo-url` | No | URL kho lưu trữ được dùng trong lời khuyên sparse-checkout của bảng ngôn ngữ trong README. |
| `--migrate-language-folders` | No | Đổi tên thư mục bí danh cũ, chẳng hạn `cn` hoặc `tw`, thành các thư mục chuẩn BCP 47. |
| `--dry-run` | No | Xem trước việc di chuyển thư mục ngôn ngữ và ước tính dịch mà không ghi file. |

Nếu không có cờ loại nào được cung cấp, `translate` sẽ xử lý Markdown, notebook và hình ảnh. Dịch hình ảnh yêu cầu cấu hình Azure AI Vision.

## evaluate

Đánh giá chất lượng bản dịch Markdown cho một ngôn ngữ.

!!! warning "Thử nghiệm"
    `evaluate` đang trong giai đoạn thử nghiệm. Nó có thể sử dụng kiểm tra chất lượng dựa trên quy tắc và dựa trên LLM, ghi kết quả đánh giá vào siêu dữ liệu bản dịch, và mô hình chấm điểm cũng như hành vi siêu dữ liệu có thể thay đổi.

```bash
evaluate -l "ko"
```

### Ví dụ phổ biến

Sử dụng ngưỡng độ tin cậy thấp nghiêm ngặt hơn:

```bash
evaluate -l "es" -c 0.8
```

Chạy kiểm tra dựa trên quy tắc thôi:

```bash
evaluate -l "fr" -f
```

Chạy kiểm tra dựa trên LLM thôi:

```bash
evaluate -l "ja" -D
```

### Tùy chọn

| Tùy chọn | Bắt buộc | Mô tả |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | Một mã ngôn ngữ duy nhất để đánh giá. Các mã bí danh được chuẩn hóa. |
| `-r`, `--root-dir` | No | Thư mục gốc dự án. Mặc định là thư mục hiện tại. |
| `-c`, `--min-confidence` | No | Ngưỡng dùng khi liệt kê các bản dịch có độ tin cậy thấp. Mặc định là `0.7`. |
| `-d`, `--debug` | No | Bật ghi nhật ký debug. |
| `-s`, `--save-logs` | No | Lưu nhật ký mức DEBUG vào `<root-dir>/logs/`. |
| `-f`, `--fast` | No | Chỉ đánh giá dựa trên quy tắc. |
| `-D`, `--deep` | No | Chỉ đánh giá dựa trên LLM. |

Mặc định, `evaluate` sử dụng cả đánh giá dựa trên quy tắc và dựa trên LLM. Kết quả được ghi vào siêu dữ liệu bản dịch và tóm tắt trên console.

## co-op-review

Chạy các kiểm tra bảo trì dịch mang tính xác định mà không cần thông tin xác thực API.

!!! note "Beta"
    `co-op-review` là một lệnh đánh giá mang tính xác định ở trạng thái beta. Nó không gọi nhà cung cấp mô hình hay ghi file, nhưng các kiểm tra và schema đầu ra vấn đề có thể thay đổi.

```bash
co-op-review -l "ko"
```

### Ví dụ phổ biến

Xem lại các bản dịch tiếng Hàn và tiếng Nhật từ thư mục hiện tại:

```bash
co-op-review -l "ko ja"
```

Xem lại một thư mục gốc dự án cụ thể:

```bash
co-op-review -l "fr" -r ./my-course
```

Chỉ xem lại các tệp nguồn đã thay đổi so với ref cơ sở:

```bash
co-op-review -l "ko" --changed-from origin/main
```

In đầu ra Markdown kiểu GitHub cho tóm tắt CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Tùy chọn

| Tùy chọn | Bắt buộc | Mô tả |
| --- | --- | --- |
| `-l`, `--language-code` | No | Mã ngôn ngữ để xem lại. Có thể truyền nhiều lần hoặc dưới dạng giá trị cách nhau bởi khoảng trắng. Mặc định là tất cả các ngôn ngữ dịch được phát hiện. |
| `-r`, `--root-dir` | No | Thư mục gốc dự án. Mặc định là thư mục hiện tại. |
| `--changed-from` | No | Git ref dùng để giới hạn việc xem lại chỉ những tệp nguồn đã thay đổi. |
| `--format` | No | Định dạng đầu ra: `text` hoặc `github`. Mặc định là `text`. |

`co-op-review` hiện kiểm tra các tệp dịch bị thiếu, siêu dữ liệu bản dịch bị thiếu hoặc lỗi thời, tính toàn vẹn frontmatter Markdown và code fence, JSON notebook dịch không hợp lệ, và các mục tiêu liên kết Markdown hoặc hình ảnh cục bộ bị thiếu. Liên kết bị thiếu mặc định là cảnh báo; các vấn đề về cấu trúc và tính cập nhật sẽ làm lệnh thất bại.

## co-op-translator-mcp

Chạy máy chủ MCP của Co-op Translator cho các agents, trình chỉnh sửa và các client tương thích MCP.

```bash
co-op-translator-mcp
```

Phương thức truyền tải mặc định là `stdio`. Xem hướng dẫn [Máy chủ MCP](mcp.md) để cấu hình client, công cụ, tài nguyên và ghi chú an toàn.

### Tùy chọn

| Tùy chọn | Bắt buộc | Mô tả |
| --- | --- | --- |
| `--transport` | No | Giao thức MCP: `stdio`, `streamable-http`, hoặc `sse`. Mặc định là `stdio`. |

## migrate-links

Xử lý lại các tệp Markdown đã dịch và cập nhật liên kết notebook để chúng trỏ đến các notebook đã dịch khi có.

```bash
migrate-links -l "ko ja"
```

### Ví dụ phổ biến

Xem trước cập nhật liên kết:

```bash
migrate-links -l "ko" --dry-run
```

Xử lý tất cả các ngôn ngữ được hỗ trợ mà không cần xác nhận:

```bash
migrate-links -l "all" -y
```

Chỉ ghi lại liên kết khi notebook đã dịch tồn tại:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Tùy chọn

| Tùy chọn | Bắt buộc | Mô tả |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | Mã ngôn ngữ cách nhau bằng khoảng trắng, hoặc `"all"`. |
| `-r`, `--root-dir` | No | Thư mục gốc dự án. Mặc định là thư mục hiện tại. |
| `--image-dir` | No | Thư mục hình ảnh đã dịch so với thư mục gốc. Mặc định là `translated_images`. |
| `--dry-run` | No | Hiển thị các tệp sẽ thay đổi mà không ghi cập nhật. |
| `--fallback-to-original`, `--no-fallback-to-original` | No | Dùng liên kết notebook gốc khi notebook đã dịch bị thiếu. Mặc định được bật. |
| `-d`, `--debug` | No | Bật ghi nhật ký debug. |
| `-s`, `--save-logs` | No | Lưu nhật ký mức DEBUG vào `<root-dir>/logs/`. |
| `-y`, `--yes` | No | Tự động xác nhận lời nhắc khi xử lý tất cả ngôn ngữ. |

## Môi trường

Tất cả lệnh yêu cầu một nhà cung cấp LLM được cấu hình:

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
```

Dịch hình ảnh ngoài ra còn yêu cầu Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Bố cục đầu ra

Các bản dịch văn bản được ghi vào:

```text
translations/<language-code>/<original-path>
```

Đầu ra hình ảnh đã dịch được ghi vào:

```text
translated_images/<language-code>/<original-path>
```

Ví dụ, dịch `README.md` và `docs/setup.md` sang tiếng Hàn sẽ tạo ra:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Ví dụ CLI sao chép-dán

Dịch Markdown sang ba ngôn ngữ:

```bash
translate -l "ko ja fr" -md
```

Chỉ dịch notebook:

```bash
translate -l "zh-CN" -nb
```

Chỉ dịch hình ảnh:

```bash
translate -l "pt-BR" -img
```

Xem trước việc dịch Markdown mà không ghi file:

```bash
translate -l "de es" -md --dry-run
```

Sửa các bản dịch Markdown có độ tin cậy thấp:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

Chạy dịch Markdown thân thiện với CI:

```bash
translate -l "ko ja" -md -y -s
```

Xem lại đầu ra đã dịch:

```bash
co-op-review -l "ko ja"
```

Xem trước việc di chuyển liên kết:

```bash
migrate-links -l "ko" --dry-run
```