# Cấu hình

Co-op Translator yêu cầu một nhà cung cấp mô hình ngôn ngữ. Dịch ảnh còn yêu cầu Azure AI Vision.

Cấu hình được đọc từ biến môi trường. Với dự án cục bộ, đặt chúng trong tệp `.env` ở thư mục gốc của dự án.

Để thiết lập tài nguyên Azure, xem [Cài đặt Azure AI](azure-ai-setup.md).

## Thiết lập môi trường chạy cục bộ

Sử dụng môi trường ảo trước khi chạy CLI cục bộ. Co-op Translator hỗ trợ Python 3.10 đến 3.12.

Đối với việc sử dụng CLI thông thường, cài đặt gói đã xuất bản bên trong môi trường ảo:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

Để phát triển kho mã, hãy cài đặt các phụ thuộc từ thư mục gốc của dự án thay vào đó:

```bash
poetry install
poetry run translate --help
```

Sau khi CLI sẵn sàng, cấu hình một nhà cung cấp mô hình ngôn ngữ trong `.env`.

## Lựa chọn nhà cung cấp

Công cụ tự động phát hiện nhà cung cấp theo thứ tự sau:

1. Azure OpenAI
2. OpenAI

Nếu không nhà cung cấp nào được cấu hình, `translate`, `evaluate`, `migrate-links`, và `run_translation` sẽ thất bại trong quá trình kiểm tra cấu hình. `co-op-review` và `run_review` là các kiểm tra bảo trì mang tính xác định và không yêu cầu thông tin xác thực của nhà cung cấp.

## Azure OpenAI

Sử dụng Azure OpenAI khi mô hình của bạn được triển khai trong Azure AI Foundry hoặc Azure OpenAI Service.

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Kiểm tra kết nối sử dụng endpoint, API key, API version và deployment name trước khi bắt đầu dịch.

## OpenAI

Sử dụng OpenAI khi gọi trực tiếp API của OpenAI.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # tùy chọn
OPENAI_BASE_URL="..."        # tùy chọn
```

`OPENAI_CHAT_MODEL_ID` là bắt buộc vì trình dịch cần một mô hình chat rõ ràng cho các cuộc gọi API.

## Azure AI Vision

Dịch ảnh yêu cầu Azure AI Vision để công cụ có thể trích xuất văn bản từ ảnh trước khi dịch.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Nếu dịch ảnh được chọn bằng `-img`, `images=True`, hoặc không có bộ lọc content-type, công cụ sẽ xác thực cấu hình Vision trước khi bắt đầu dịch.

## Nhiều bộ thông tin xác thực

Lớp cấu hình hỗ trợ nhiều bộ thông tin xác thực bằng cách thêm hậu tố số chỉ mục giống nhau vào các biến:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

Mỗi bộ phải đầy đủ. Kiểm tra sức khỏe chọn một bộ đang hoạt động trước khi tiến hành dịch.

## Yêu cầu lệnh

| Lệnh hoặc API | Cần LLM | Cần Vision | Ghi chú |
| --- | --- | --- | --- |
| `translate -md` | Yes | No | Chỉ dịch Markdown. |
| `translate -nb` | Yes | No | Chỉ dịch notebook. |
| `translate -img` | Yes | Yes | Chỉ dịch ảnh. |
| `translate` with no type flags | Yes | Yes | Chế độ mặc định bao gồm Markdown, notebook và ảnh. |
| `evaluate` | Yes | No | Sử dụng đánh giá LLM trừ khi chọn `--fast`. |
| `migrate-links` | Yes | No | Thực hiện di chuyển liên kết, nhưng vẫn chạy các kiểm tra cấu hình chung. |
| `co-op-review` | No | No | Chạy các kiểm tra cấu trúc dịch xác định, độ mới, Markdown, notebook và liên kết cục bộ. |
| `run_translation(markdown=True)` | Yes | No | Dịch Markdown theo chương trình. |
| `run_translation(images=True)` | Yes | Yes | Dịch ảnh theo chương trình. |
| `run_review(...)` | No | No | Kiểm tra xác định theo chương trình. |

## Thư mục đầu ra

Đầu ra dịch văn bản mặc định:

```text
translations/<language-code>/<source-relative-path>
```

Đầu ra ảnh đã dịch mặc định:

```text
translated_images/<language-code>/<source-relative-path>
```

API Python có thể ghi đè các thư mục này bằng `translations_dir` và `image_dir`.