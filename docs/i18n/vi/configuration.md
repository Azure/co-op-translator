# Cấu hình

Co-op Translator yêu cầu một nhà cung cấp mô hình ngôn ngữ. Việc dịch hình ảnh còn yêu cầu Azure AI Vision.

Cấu hình được đọc từ các biến môi trường. Đối với dự án cục bộ, đặt chúng trong tệp `.env` ở thư mục gốc dự án.

Để thiết lập tài nguyên Azure, xem [Thiết lập Azure AI](azure-ai-setup.md).

## Thiết lập môi trường chạy cục bộ

Sử dụng môi trường ảo trước khi chạy CLI trên máy cục bộ. Co-op Translator hỗ trợ Python 3.11 đến 3.14.

Để sử dụng CLI thông thường, cài gói đã phát hành bên trong môi trường ảo:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### Phát triển kho

Đối với phát triển kho mã, cài các phụ thuộc từ thư mục gốc của dự án thay vào đó:

```bash
poetry install
poetry run translate --help
```

Sau khi CLI sẵn sàng, cấu hình một nhà cung cấp mô hình ngôn ngữ trong `.env`.

## Chọn nhà cung cấp

Công cụ tự phát hiện nhà cung cấp theo thứ tự sau:

1. Azure OpenAI
2. OpenAI
3. Anthropic

Việc dịch yêu cầu thông tin xác thực của nhà cung cấp, ngoại trừ các bản xem trước như `translate -l "ko" -md --dry-run`. `migrate-links`, `co-op-review`, và `run_review` là các thao tác bảo trì xác định trước và không yêu cầu thông tin xác thực của nhà cung cấp.

## Backend của client mô hình

Bắt đầu từ Co-op Translator 0.22.0, Azure OpenAI, OpenAI và Anthropic mặc định sử dụng Microsoft Agent Framework. Không yêu cầu thiết lập backend cho việc sử dụng thông thường.

Semantic Kernel vẫn tạm thời khả dụng để tương thích. Để chọn nó một cách rõ ràng, đặt:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Việc sử dụng Semantic Kernel sẽ phát ra cảnh báo lỗi thời. Gói này dự kiến sẽ chuyển Semantic Kernel thành một phụ thuộc tùy chọn trong 0.23.0 và loại bỏ tích hợp trong 0.24.0, tùy theo kết quả tương thích và phản hồi của người dùng. Anthropic yêu cầu `agent-framework`; việc chọn rõ ràng `semantic-kernel` với Anthropic sẽ thất bại với lỗi cấu hình. Các giá trị không hợp lệ sẽ gây lỗi trong quá trình khởi tạo bộ dịch dựa trên nhà cung cấp thay vì tự động chuyển về phương án khác. Theo dõi việc triển khai và báo cáo các trở ngại trong [vấn đề GitHub #543](https://github.com/Azure/co-op-translator/issues/543).

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

Sử dụng OpenAI khi gọi trực tiếp OpenAI API.

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` là bắt buộc vì bộ dịch cần một mô hình chat rõ ràng cho các gọi API.

Không thiết lập `OPENAI_ORG_ID` và `OPENAI_BASE_URL` cho cấu hình mặc định. Thêm ID tổ chức chỉ khi tài khoản của bạn cần, hoặc base URL chỉ khi dùng endpoint tùy chỉnh. Không sao chép các giá trị giữ chỗ cho các thiết lập tùy chọn.

## Anthropic Claude

Sử dụng Anthropic khi gọi trực tiếp Claude API. Tạo một [Khóa API Anthropic](https://platform.claude.com/docs/en/get-started) và chọn một [ID mô hình Claude](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) được hỗ trợ.

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` và `ANTHROPIC_MODEL` là bắt buộc. Bạn không cần thiết lập `CO_OP_TRANSLATOR_MODEL_CLIENT`; Agent Framework là backend mặc định.

Không thiết lập `ANTHROPIC_BASE_URL` cho Anthropic API. Chỉ đặt nó khi sử dụng endpoint tùy chỉnh.

`ANTHROPIC_MAX_TOKENS` mặc định là `8192`, đủ chỗ cho các kịch bản nhiều token như Meitei Mayek. Giảm giá trị này nếu mô hình của bạn hoặc endpoint tương thích Anthropic giới hạn đầu ra dưới mức đó.

## Azure AI Vision

Dịch ảnh yêu cầu Azure AI Vision để công cụ có thể trích xuất văn bản từ ảnh trước khi mô hình ngôn ngữ đã cấu hình dịch nó. Anthropic có thể dịch văn bản đã trích xuất giống như Azure OpenAI hoặc OpenAI.

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Nếu dịch ảnh được chọn bằng `-img`, `images=True`, hoặc không có bộ lọc loại nội dung, công cụ sẽ xác thực cấu hình Vision trước khi bắt đầu dịch.

## Nhiều bộ thông tin xác thực

Lớp cấu hình hỗ trợ nhiều bộ thông tin xác thực bằng cách thêm hậu tố chỉ mục giống nhau vào các biến:

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

Mỗi bộ phải đầy đủ. Kiểm tra sức khỏe sẽ chọn một bộ hoạt động trước khi tiến hành dịch.

OpenAI và Anthropic hỗ trợ cùng quy ước hậu tố. Giữ mọi biến trong một bộ thông tin xác thực cùng hậu tố, kể cả các giá trị tùy chọn như `OPENAI_BASE_URL_1` hoặc `ANTHROPIC_BASE_URL_1`.

## Yêu cầu lệnh

| Command or API | Yêu cầu LLM | Yêu cầu Vision | Ghi chú |
| --- | --- | --- | --- |
| `translate -md` | Có | Không | Chỉ dịch Markdown. |
| `translate -nb` | Có | Không | Chỉ dịch notebooks. |
| `translate -img` | Có | Có | Chỉ dịch hình ảnh. |
| `translate` with no type flags | Có | Có | Chế độ mặc định bao gồm Markdown, notebooks, và hình ảnh. |
| `evaluate` | Có | Không | Sử dụng đánh giá LLM trừ khi chọn `--fast`. |
| `migrate-links` | Không | Không | Thực hiện di chuyển liên kết cục bộ mà không gọi đến nhà cung cấp. |
| `co-op-review` | Không | Không | Chạy các kiểm tra xác định trước về cấu trúc dịch, độ mới, Markdown, notebook và liên kết cục bộ. |
| `run_translation(markdown=True)` | Có | Không | Dịch Markdown theo lập trình. |
| `run_translation(images=True)` | Có | Có | Dịch hình ảnh theo lập trình. |
| `run_review(...)` | Không | Không | Kiểm tra xác định trước theo lập trình. |

## Thư mục đầu ra

Đầu ra dịch văn bản mặc định:

```text
translations/<language-code>/<source-relative-path>
```

Đầu ra ảnh dịch mặc định:

```text
translated_images/<language-code>/<source-relative-path>
```

API Python có thể ghi đè các thư mục này bằng `translations_dir` và `image_dir`.