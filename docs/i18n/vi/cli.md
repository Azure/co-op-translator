# Tham khảo CLI

Co-op Translator cài đặt các điểm entry dòng lệnh sau:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

Các lệnh `translate`, `evaluate`, `migrate-links`, và `co-op-review` được phân phối qua `co_op_translator.__main__`, vốn chọn triển khai lệnh dựa trên tên tập lệnh được gọi. Máy chủ MCP sử dụng trực tiếp `co_op_translator.mcp.server`.

Nếu bạn đang phân vân giữa CLI, API Python và MCP, hãy bắt đầu với [Chọn quy trình làm việc của bạn](workflows.md).

## Đầu ra console

Các terminal tương tác sử dụng định dạng Rich cho tiêu đề lệnh, tiến độ và tóm tắt. CI và đầu ra không tương tác tự động chuyển về văn bản thuần.

Đặt `CO_OP_TRANSLATOR_OUTPUT_STYLE=plain` để ép xuất ra dạng thuần, hoặc `CO_OP_TRANSLATOR_OUTPUT_STYLE=rich` để ép xuất Rich. Đặt `CO_OP_TRANSLATOR_NO_PROGRESS=1` để giữ các tóm tắt trong khi ẩn thanh tiến độ trực tiếp.

Dùng `translate --json-events progress.ndjson` khi một hệ thống khác cần
tiến trình có thể đọc bởi máy. CLI tiếp tục hiển thị đầu ra dành cho người dùng, trong khi
tệp NDJSON nhận các sự kiện có phiên bản `co-op.translation.event.v1` với
các trường ổn định như `type`, `stage_key`, `completed`, `total`, và
`current_path`.

## Quy trình CLI lần đầu

Bắt đầu ở đây nếu bạn đang sử dụng Co-op Translator từ dòng lệnh:

1. Cấu hình nhà cung cấp LLM như mô tả trong [Cấu hình](configuration.md).
2. Chọn loại nội dung bạn muốn dịch.
3. Chạy một lệnh tập trung trước, ví dụ chỉ dịch Markdown.
4. Sử dụng `--dry-run` trước khi thay đổi lớn trong kho.
5. Sử dụng `co-op-review` sau khi dịch để kiểm tra cấu trúc và độ mới.

| Mục tiêu | Lệnh để bắt đầu |
| --- | --- |
| Dịch tài liệu Markdown | `translate -l "ko" -md` |
| Dịch notebook | `translate -l "ko" -nb` |
| Dịch văn bản trong ảnh | `translate -l "ko" -img` |
| Xem trước công việc mà không ghi file | `translate -l "ko" -md --dry-run` |
| Xem lại các bản dịch hiện có | `co-op-review -l "ko"` |
| Cập nhật liên kết notebook và Markdown | `migrate-links -l "ko" --dry-run` |
| Cung cấp công cụ cho client MCP | Cấu hình [Máy chủ MCP](mcp.md) thay vì chạy các lệnh CLI trực tiếp. |

## translate

Dịch các tệp Markdown, notebook và văn bản trong ảnh sang một hoặc nhiều ngôn ngữ đích.

```bash
translate -l "ko ja fr"
```

### Ví dụ thường gặp

Chỉ dịch Markdown:

```bash
translate -l "de" -md
```

Chỉ dịch notebook:

```bash
translate -l "zh-CN" -nb
```

Dịch Markdown và ảnh:

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

Ghi các sự kiện tiến trình có cấu trúc:

```bash
translate -l "ko ja" -md --json-events progress.ndjson
```

### Tùy chọn

| Tùy chọn | Bắt buộc | Mô tả |
| --- | --- | --- |
| `-l`, `--language-codes` | Có | Các mã ngôn ngữ cách nhau bằng khoảng trắng, ví dụ `"es fr de"`, hoặc `"all"`. |
| `-r`, `--root-dir` | Không | Thư mục gốc dự án. Mặc định là thư mục hiện tại. |
| `-u`, `--update` | Không | Xóa các bản dịch hiện có cho các ngôn ngữ được chọn và tạo lại chúng. |
| `-img`, `--images` | Không | Chỉ dịch các tệp ảnh. |
| `-md`, `--markdown` | Không | Chỉ dịch các tệp Markdown. |
| `-nb`, `--notebook` | Không | Chỉ dịch các tệp Jupyter notebook. |
| `-d`, `--debug` | Không | Bật ghi nhật ký debug trên console. |
| `-s`, `--save-logs` | Không | Lưu nhật ký cấp DEBUG vào `<root-dir>/logs/`. |
| `--json-events` | Không | Ghi các sự kiện tiến trình dịch có thể đọc bởi máy dưới dạng NDJSON. |
| `-x`, `--fix` | Không | Dịch lại các tệp Markdown có độ tin cậy thấp dựa trên kết quả đánh giá trước đó. |
| `-c`, `--min-confidence` | Không | Ngưỡng độ tin cậy cho `--fix`. Mặc định là `0.7`. |
| `--add-disclaimer`, `--no-disclaimer` | Không | Thêm hoặc bỏ thông báo từ chối trách nhiệm cho dịch máy. Mặc định bật trong CLI. |
| `-f`, `--fast` | Không | Chế độ ảnh nhanh đã bị loại bỏ (deprecated). |
| `-y`, `--yes` | Không | Tự động xác nhận các lời nhắc, hữu ích trong CI. |
| `--repo-url` | Không | URL kho dùng trong lời khuyên sparse-checkout của bảng ngôn ngữ README. |
| `--migrate-language-folders` | Không | Đổi tên các thư mục bí danh cũ, như `cn` hoặc `tw`, thành các thư mục BCP 47 chuẩn. |
| `--dry-run` | Không | Xem trước việc di chuyển thư mục ngôn ngữ và ước tính dịch mà không ghi file. |

Nếu không cung cấp cờ loại, `translate` sẽ xử lý Markdown, notebook và ảnh. Dịch ảnh yêu cầu cấu hình Azure AI Vision.

## evaluate

Đánh giá chất lượng bản dịch Markdown cho một ngôn ngữ.

!!! warning "Thử nghiệm"
    `evaluate` là tính năng thử nghiệm. Nó có thể sử dụng các kiểm tra chất lượng theo quy tắc và dựa trên LLM, ghi kết quả đánh giá vào siêu dữ liệu bản dịch, và mô hình chấm điểm cùng hành vi siêu dữ liệu của nó có thể thay đổi.

```bash
evaluate -l "ko"
```

### Ví dụ thường gặp

Sử dụng ngưỡng độ tin cậy thấp nghiêm ngặt hơn:

```bash
evaluate -l "es" -c 0.8
```

Chỉ chạy các kiểm tra theo quy tắc:

```bash
evaluate -l "fr" -f
```

Chỉ chạy các kiểm tra dựa trên LLM:

```bash
evaluate -l "ja" -D
```

### Tùy chọn

| Tùy chọn | Bắt buộc | Mô tả |
| --- | --- | --- |
| `-l`, `--language-code` | Có | Mã ngôn ngữ đơn để đánh giá. Các mã bí danh được chuẩn hóa. |
| `-r`, `--root-dir` | Không | Thư mục gốc dự án. Mặc định là thư mục hiện tại. |
| `-c`, `--min-confidence` | Không | Ngưỡng dùng khi liệt kê các bản dịch có độ tin cậy thấp. Mặc định `0.7`. |
| `-d`, `--debug` | Không | Bật ghi nhật ký debug. |
| `-s`, `--save-logs` | Không | Lưu nhật ký cấp DEBUG vào `<root-dir>/logs/`. |
| `-f`, `--fast` | Không | Chỉ đánh giá theo quy tắc. |
| `-D`, `--deep` | Không | Chỉ đánh giá dựa trên LLM. |

Mặc định, `evaluate` sử dụng cả hai phương pháp đánh giá theo quy tắc và dựa trên LLM. Kết quả được ghi vào metadata bản dịch và tóm tắt trên console.

## co-op-review

Chạy các kiểm tra bảo trì dịch có tính xác định mà không cần thông tin xác thực API.

!!! note "Beta"
    `co-op-review` là một lệnh rà soát mang tính xác định ở giai đoạn beta. Nó không gọi nhà cung cấp mô hình hay ghi tệp, nhưng các kiểm tra và lược đồ đầu ra của các vấn đề có thể thay đổi.

```bash
co-op-review -l "ko"
```

### Ví dụ thường gặp

Xem lại các bản dịch tiếng Hàn và tiếng Nhật từ thư mục hiện tại:

```bash
co-op-review -l "ko ja"
```

Xem lại một thư mục gốc dự án cụ thể:

```bash
co-op-review -l "fr" -r ./my-course
```

Chỉ xem lại README sau khi dịch chỉ README:

```bash
translate -l "ko" --readme-only -y
co-op-review -l "ko" --readme-only --format github
```

`--readme-only` bỏ qua các tài liệu khác và các README lồng nhau. Nó sẽ thất bại nếu README gốc
`README.md` bị thiếu. Kết hợp với `--changed-from`, nó chỉ xem lại README
khi tệp nguồn đó thay đổi. Việc dịch chỉ README để lại README nguồn
không thay đổi, bao gồm bất kỳ dấu hiệu phần chia sẻ nào.

Chỉ xem lại các tệp nguồn đã thay đổi so với ref cơ sở:

```bash
co-op-review -l "ko" --changed-from origin/main
```

In đầu ra Markdown theo chuẩn GitHub cho tóm tắt CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Tùy chọn

| Tùy chọn | Bắt buộc | Mô tả |
| --- | --- | --- |
| `-l`, `--language-code` | Không | Mã ngôn ngữ để xem lại. Có thể truyền nhiều lần hoặc dưới dạng giá trị cách nhau bằng khoảng trắng. Mặc định là tất cả các ngôn ngữ dịch được phát hiện. |
| `-r`, `--root-dir` | Không | Thư mục gốc dự án. Mặc định là thư mục hiện tại. |
| `--changed-from` | Không | Git ref dùng để giới hạn việc xem lại chỉ các tệp nguồn đã thay đổi. |
| `--readme-only` | Không | Chỉ xem lại bản dịch `README.md` gốc. |
| `--format` | Không | Định dạng đầu ra: `text` hoặc `github`. Mặc định là `text`. |

`co-op-review` hiện tại kiểm tra việc thiếu tệp dịch, metadata dịch bị thiếu hoặc cũ, tính toàn vẹn frontmatter Markdown và hàng rào mã, JSON notebook dịch không hợp lệ, và các mục tiêu liên kết Markdown hoặc hình ảnh cục bộ bị thiếu. Các liên kết bị thiếu mặc định là cảnh báo; các vấn đề về cấu trúc và độ mới sẽ khiến lệnh thất bại.

## co-op-translator-mcp

Chạy máy chủ MCP của Co-op Translator cho agents, editors và các client tương thích MCP.

```bash
co-op-translator-mcp
```

Giao thức vận chuyển mặc định là `stdio`. Xem hướng dẫn [Máy chủ MCP](mcp.md) để biết cấu hình client, công cụ, tài nguyên và ghi chú an toàn.

### Tùy chọn

| Tùy chọn | Bắt buộc | Mô tả |
| --- | --- | --- |
| `--transport` | Không | Giao thức MCP: `stdio`, `streamable-http`, hoặc `sse`. Mặc định là `stdio`. |

## migrate-links

Xử lý lại các tệp Markdown đã dịch và cập nhật liên kết notebook để chúng trỏ tới notebook dịch khi có sẵn.

```bash
migrate-links -l "ko ja"
```

### Ví dụ thường gặp

Xem trước cập nhật liên kết:

```bash
migrate-links -l "ko" --dry-run
```

Xử lý tất cả các ngôn ngữ được hỗ trợ mà không cần xác nhận:

```bash
migrate-links -l "all" -y
```

Chỉ viết lại liên kết khi tồn tại notebook đã dịch:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Tùy chọn

| Tùy chọn | Bắt buộc | Mô tả |
| --- | --- | --- |
| `-l`, `--language-codes` | Có | Các mã ngôn ngữ cách nhau bằng khoảng trắng, hoặc `"all"`. |
| `-r`, `--root-dir` | Không | Thư mục gốc dự án. Mặc định là thư mục hiện tại. |
| `--image-dir` | Không | Thư mục ảnh đã dịch tương đối so với thư mục gốc. Mặc định là `translated_images`. |
| `--dry-run` | Không | Hiển thị các tệp sẽ thay đổi mà không ghi cập nhật. |
| `--fallback-to-original`, `--no-fallback-to-original` | Không | Sử dụng liên kết notebook gốc khi notebook đã dịch bị thiếu. Mặc định được bật. |
| `-d`, `--debug` | Không | Bật ghi nhật ký debug. |
| `-s`, `--save-logs` | Không | Lưu nhật ký cấp DEBUG vào `<root-dir>/logs/`. |
| `-y`, `--yes` | Không | Tự động xác nhận lời nhắc khi xử lý tất cả ngôn ngữ. |

## Môi trường

Khi một lệnh yêu cầu thông tin xác thực nhà cung cấp, hãy cấu hình một trong các bộ nhà cung cấp này. `translate --dry-run` và `co-op-review` không yêu cầu thông tin xác thực nhà cung cấp:

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

Dịch ảnh ngoài ra còn yêu cầu Azure AI Vision:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Bố cục đầu ra

Các bản dịch văn bản được ghi vào:

```text
translations/<language-code>/<original-path>
```

Đầu ra ảnh đã dịch được ghi vào:

```text
translated_images/<language-code>/<original-path>
```

Ví dụ, dịch `README.md` và `docs/setup.md` sang tiếng Hàn tạo ra:

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

Chỉ dịch ảnh:

```bash
translate -l "pt-BR" -img
```

Xem trước việc dịch Markdown mà không ghi file:

```bash
translate -l "de es" -md --dry-run
```

Sửa các bản dịch Markdown độ tin cậy thấp:

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

Xem trước di chuyển liên kết:

```bash
migrate-links -l "ko" --dry-run
```