# Hướng dẫn người bảo trì

Trang này tóm tắt cách API, CLI và trang tài liệu được kết nối với nhau.

## Ranh giới API công khai

API Python ổn định được xuất từ:

```python
co_op_translator.api
```

API công khai được tổ chức thành các trợ giúp dịch nội dung, trợ giúp viết lại đường dẫn, điều phối dự án, và rà soát:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

`TranslationStateProvider` là ranh giới lưu trữ lâu dài cho các tích hợp được lưu trữ.
Nó phải giữ các ứng viên được tạo ra tách biệt khỏi các baseline đã được chấp nhận để một
bản dịch chưa được gộp không thể trở thành nguồn sự thật.

Khi thêm API công khai mới, cập nhật:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- các bài kiểm tra API liên quan trong `tests/co_op_translator/`, chẳng hạn như `test_api.py` hoặc `test_review_api.py`

Tránh ghi tài liệu các mô-đun `core` ở mức thấp hơn là API ổn định trừ khi dự án có ý định hỗ trợ chúng trực tiếp.

## Điểm vào CLI

Gói định nghĩa các script Poetry sau:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` phân phối theo tên script:

- `translate` gọi `co_op_translator.cli.translate.translate_command`
- `evaluate` gọi `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` gọi `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` gọi `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` bỏ qua `__main__.py` và gọi trực tiếp `co_op_translator.mcp.server:main`.

Khi thêm hoặc thay đổi các tuỳ chọn CLI, cập nhật:

- lệnh tương ứng trong `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- các bài kiểm tra liên quan đến CLI, nếu hành vi thay đổi

## Máy chủ MCP

Máy chủ MCP được triển khai trong:

```python
co_op_translator.mcp.server
```

Máy chủ cố tình bao bọc API Python công khai thay vì gọi các mô-đun `core` mức thấp hơn. Giữ ranh giới này nguyên vẹn để các client MCP, các caller Python và CLI chia sẻ cùng một hành vi.

Khi thêm hoặc thay đổi các công cụ MCP, cập nhật:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` nếu bề mặt API công khai thay đổi

Các công cụ dịch trong kho lưu trữ có thể được gọi mô hình thông qua MCP và có thể ghi nhiều tệp. Giữ `dry_run=True` làm mặc định và yêu cầu `confirm_write=True` trước khi dịch dự án khi không phải dry-run.

## Luồng dịch

Luồng dịch dự án ở mức cao là:

1. Phân tích các đối số CLI hoặc tham số API.
2. Xác thực cấu hình LLM với `LLMConfig`.
3. Xác thực Azure AI Vision khi chọn dịch hình ảnh.
4. Chuẩn hóa mã ngôn ngữ.
5. Phát hiện các bí danh thư mục ngôn ngữ cũ.
6. Ước lượng khối lượng dịch.
7. Cập nhật các phần ngôn ngữ/khóa học trong README khi áp dụng.
8. Ủy quyền dịch dự án cho `ProjectTranslator`.
9. `ProjectTranslator` ủy quyền xử lý tệp cho `TranslationManager`.

`TranslationManager` được tạo thành từ các mixin tập trung theo loại tệp:

- `ProjectMarkdownTranslationMixin` xử lý việc đọc tệp Markdown, dịch nội dung, viết lại đường dẫn, metadata, tuyên bố từ chối trách nhiệm, và ghi tệp.
- `ProjectNotebookTranslationMixin` xử lý đọc tệp notebook, dịch ô Markdown, viết lại đường dẫn, metadata, tuyên bố từ chối trách nhiệm, và ghi tệp.
- `ProjectImageTranslationMixin` xử lý tìm kiếm hình ảnh, trích xuất/dịch văn bản, ghi hình ảnh đã render, và metadata.

Các API nội dung cấp thấp hơn bỏ qua quy trình làm việc dự án:

1. `translate_markdown_content` và `translate_notebook_content` chỉ dịch nội dung trong bộ nhớ.
2. `translate_image_content` dịch văn bản trong một hình ảnh và trả về một đối tượng hình ảnh đã được render.
3. `rewrite_markdown_paths` và `rewrite_notebook_paths` là các hàm trợ giúp xử lý hậu kỳ rõ ràng. Chúng không thực hiện dịch và không ghi dự án nào.

## Luồng rà soát

Luồng rà soát có tính xác định là:

1. Phân tích các đối số CLI hoặc tham số API.
2. Chuẩn hóa các mã ngôn ngữ được yêu cầu.
3. Xây dựng một hoặc nhiều mục tiêu rà soát từ `root_dir`, `root_dirs`, hoặc `groups`.
4. Tuỳ chọn giới hạn các tệp nguồn bằng `--changed-from`.
5. Chạy các kiểm tra xác định cho cấu trúc, độ mới của bản dịch, tính toàn vẹn của Markdown, và đường dẫn liên kết/hình ảnh cục bộ.
6. In ra kết quả dạng văn bản hoặc Markdown theo chuẩn GitHub.
7. Thoát với mã lỗi khi phát hiện lỗi rà soát.

Luồng rà soát không yêu cầu khóa API và vẫn có sẵn cho các kiểm tra cục bộ hoặc CI người dùng lựa chọn tham gia. Kho lưu trữ này không chạy `co-op-review` tự động trên mọi pull request.

## Trang tài liệu

Trang docs được cấu hình bởi:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Thư mục `docs/` là nguồn tài liệu chính thức. Đừng thêm các hướng dẫn dành cho người dùng cuối mới bên ngoài thư mục này trừ khi dự án cố tình giới thiệu một bề mặt tài liệu được xuất bản khác.

Xây dựng cục bộ:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

Xem trước cục bộ:

```bash
python -m mkdocs serve
```

Trang được sinh ra được ghi vào `site/`, thư mục này bị git bỏ qua.

## Luồng công việc GitHub Pages

`.github/workflows/docs.yml` xây dựng trang khi có pull request và triển khai khi đẩy lên `main`.

Luồng công việc cài đặt:

```bash
pip install -r requirements-docs.txt
```

Luồng công việc docs chỉ cài đặt chuỗi công cụ tài liệu. `mkdocs.yml` trỏ `mkdocstrings` đến `src/` để các trang API công khai có thể được kết xuất từ cây nguồn mà không cần cài đặt toàn bộ tập phụ thuộc runtime. Nếu tài liệu API trong tương lai yêu cầu import các nhà cung cấp runtime tuỳ chọn trong quá trình build, cập nhật cả `.github/workflows/docs.yml` và hướng dẫn này cùng lúc.

## Ngưỡng chất lượng tài liệu

Trước khi hợp nhất các thay đổi tài liệu, chạy:

```bash
python -m mkdocs build --strict
git diff --check
```

Sử dụng build nghiêm ngặt để các liên kết hỏng, mục điều hướng không hợp lệ và các vấn đề kết xuất API thất bại sớm.