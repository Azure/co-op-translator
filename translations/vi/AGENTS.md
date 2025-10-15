<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:30:32+00:00",
  "source_file": "AGENTS.md",
  "language_code": "vi"
}
-->
## Tổng quan dự án

Co‑op Translator là một công cụ dòng lệnh Python và workflow GitHub Actions dùng để dịch các tệp Markdown, notebook Jupyter và văn bản trong ảnh sang nhiều ngôn ngữ khác nhau. Công cụ này tổ chức đầu ra vào các thư mục theo từng ngôn ngữ và giữ cho bản dịch luôn đồng bộ với nội dung gốc. Dự án được xây dựng dưới dạng thư viện quản lý bằng Poetry với các điểm vào CLI.

### Tổng quan kiến trúc

- Các điểm vào CLI (`translate`, `migrate-links`, `evaluate`) gọi một CLI thống nhất để điều phối các luồng dịch, di chuyển liên kết và đánh giá.
- Bộ tải cấu hình đọc `.env` và tự động phát hiện nhà cung cấp LLM (Azure OpenAI hoặc OpenAI) và, nếu được yêu cầu, nhà cung cấp vision (Azure AI Service) để trích xuất văn bản từ ảnh.
- Lõi dịch xử lý Markdown và notebook; pipeline vision trích xuất văn bản từ ảnh khi sử dụng `-img`.
- Đầu ra được tổ chức vào `translations/<lang>/` cho văn bản và `translated_images/` cho ảnh, giữ nguyên cấu trúc gốc.

### Công nghệ và framework chính

- Python 3.10–3.12, Poetry để đóng gói
- CLI: `click`
- SDK LLM/AI: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP và dữ liệu: `httpx`, `pydantic`
- Xử lý ảnh: `pillow`, `opencv-python`, `matplotlib`
- Công cụ: `pytest`, `black`, `ruff`

## Lệnh cài đặt

### Yêu cầu

- Python 3.10–3.12
- Tài khoản Azure (tùy chọn, cho dịch vụ Azure AI)
- Kết nối Internet để sử dụng API LLM/Vision (ví dụ: Azure OpenAI/OpenAI, Azure AI Vision)

### Cách A: Poetry (khuyến nghị)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Cách B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## Hướng dẫn sử dụng cho người dùng cuối

### Docker (image đã được phát hành)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Lưu ý:
- Điểm vào mặc định là `translate`. Ghi đè bằng `--entrypoint migrate-links` để di chuyển liên kết.
- Đảm bảo gói GHCR có chế độ Public để cho phép pull ẩn danh.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Cấu hình môi trường

Tạo tệp `.env` ở thư mục gốc của repo và cung cấp thông tin xác thực/endpoint cho mô hình ngôn ngữ bạn chọn và (nếu cần) dịch vụ vision. Để biết hướng dẫn cấu hình cụ thể cho từng nhà cung cấp, xem `getting_started/set-up-azure-ai.md`.

### Biến môi trường bắt buộc

Cần cấu hình ít nhất một nhà cung cấp LLM. Để dịch ảnh, cũng cần cấu hình Azure AI Service.

- Azure OpenAI (dịch văn bản):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (phương án thay thế dịch văn bản):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (tùy chọn)
  - `OPENAI_CHAT_MODEL_ID` (bắt buộc khi dùng OpenAI provider)
  - `OPENAI_BASE_URL` (tùy chọn; mặc định là `https://api.openai.com/v1`)

- Azure AI Service để trích xuất văn bản từ ảnh (bắt buộc khi dùng `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (ưu tiên) hoặc `AZURE_SUBSCRIPTION_KEY` cũ
  - `AZURE_AI_SERVICE_ENDPOINT`

Ví dụ đoạn `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Lưu ý:

- Công cụ sẽ tự động phát hiện nhà cung cấp LLM khả dụng; cấu hình Azure OpenAI hoặc OpenAI.
- Dịch ảnh yêu cầu cả `AZURE_AI_SERVICE_API_KEY` và `AZURE_AI_SERVICE_ENDPOINT`.
- CLI sẽ báo lỗi rõ ràng nếu thiếu biến bắt buộc.

## Quy trình phát triển

- Mã nguồn nằm trong `src/co_op_translator`; kiểm thử trong `tests/`.
- Các CLI chính (cài đặt qua entry points):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Xem thêm tài liệu sử dụng trong `getting_started/`.

## Hướng dẫn kiểm thử

Chạy kiểm thử từ thư mục gốc của repo. Một số kiểm thử có thể cần thông tin API; bỏ qua nếu cần.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

Kiểm thử coverage (cần `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Quy tắc định dạng mã nguồn

- Định dạng: Black (cấu hình trong `pyproject.toml`, độ dài dòng 88)
- Linter: Ruff (cấu hình trong `pyproject.toml`, độ dài dòng 120)
- Kiểm tra kiểu: mypy (đã có cấu hình; bật nếu đã cài đặt)

Lệnh:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Tổ chức mã Python trong `src/`, kiểm thử trong `tests/`, và ưu tiên import rõ ràng trong namespace gói (`co_op_translator.*`).

## Xây dựng và triển khai

Artifact build được xuất ra `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Tự động hóa qua GitHub Actions được hỗ trợ; xem:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Image container (GHCR)

- Image chính thức: `ghcr.io/azure/co-op-translator:<tag>`
- Tag: `latest` (trên main), tag semantic như `vX.Y.Z`, và tag `sha`
- Multi-arch: hỗ trợ `linux/amd64, linux/arm64` qua Buildx
- Mẫu Dockerfile: build wheel dependency trong builder (với `build-essential` và `python3-dev`) và cài đặt từ wheelhouse cục bộ ở runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` build và đẩy lên GHCR

## Lưu ý bảo mật

- Giữ API key và endpoint trong `.env` hoặc kho bí mật CI; không bao giờ commit thông tin bí mật.
- Để dịch ảnh, cần có key/endpoint Azure AI Vision; nếu không thì bỏ qua `-img`.
- Kiểm tra quota/giới hạn tốc độ của nhà cung cấp khi chạy dịch số lượng lớn.

## Hướng dẫn Pull Request

### Trước khi gửi

1. **Kiểm thử thay đổi:**
   - Chạy toàn bộ notebook bị ảnh hưởng
   - Đảm bảo tất cả cell chạy không lỗi
   - Kiểm tra đầu ra phù hợp

2. **Cập nhật tài liệu:**
   - Cập nhật `README.md` nếu thêm khái niệm mới
   - Thêm chú thích trong notebook cho đoạn mã phức tạp
   - Đảm bảo cell markdown giải thích mục đích

3. **Thay đổi tệp:**
   - Tránh commit tệp `.env` (dùng `.env.example`)
   - Không commit thư mục `venv/` hoặc `__pycache__/`
   - Giữ đầu ra notebook khi cần minh họa
   - Xóa tệp tạm và notebook backup (`*-backup.ipynb`)

4. **Định dạng và style:**
   - Tuân thủ quy tắc style và định dạng
   - Chạy `poetry run black .` và `poetry run ruff check .` để kiểm tra style và định dạng

5. **Thêm/cập nhật kiểm thử và trợ giúp CLI:**
   - Thêm hoặc cập nhật kiểm thử khi thay đổi hành vi
   - Giữ trợ giúp CLI nhất quán với thay đổi


### Thông điệp commit và chiến lược merge

Chúng tôi sử dụng Squash and Merge mặc định. Thông điệp squash commit cuối cùng nên theo mẫu:

```bash
<type>: <description> (#<PR number>)
```

Các loại được phép:
- `Docs` — cập nhật tài liệu
- `Build` — hệ thống build, phụ thuộc, cấu hình/CI
- `Core` — chức năng và tính năng cốt lõi (ví dụ: `src/co_op_translator/core`)

Ví dụ:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Lưu ý:
- Tiêu đề PR thường được tự động thêm tiền tố dựa trên nhãn; kiểm tra lại tiền tố đã đúng chưa.

### Định dạng tiêu đề PR

Dùng tiêu đề rõ ràng, ngắn gọn. Ưu tiên cùng cấu trúc với squash commit cuối cùng:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Gỡ lỗi và xử lý sự cố

- Các vấn đề thường gặp và cách khắc phục: `getting_started/troubleshooting.md`
- Ngôn ngữ được hỗ trợ và lưu ý (bao gồm font/vấn đề đã biết): `getting_started/supported-languages.md`
- Nếu gặp vấn đề liên kết trong notebook, chạy lại: `migrate-links -l "all" -y`

## Lưu ý cho Agent

- Ưu tiên dùng Poetry để đảm bảo môi trường tái tạo; nếu không thì dùng `requirements.txt`.
- Khi gọi CLI trong CI, cung cấp bí mật cần thiết qua biến môi trường hoặc tiêm `.env`.
- Với người dùng monorepo, repo này hoạt động như một package độc lập; không cần phối hợp sub-package.

- Hướng dẫn multi-arch: giữ `linux/arm64` nếu có người dùng ARM (Apple Silicon/máy chủ ARM); nếu không thì chỉ cần `linux/amd64` cho đơn giản.
- Hướng dẫn người dùng đến Docker Quick Start trong `README.md` nếu họ thích dùng container; bao gồm cả biến thể Bash và PowerShell do khác biệt về dấu nháy.

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.