# Hướng dẫn dành cho người duy trì

Trang này tóm tắt cách API, CLI và trang tài liệu được kết nối với nhau.

## Ranh giới API công khai

API Python ổn định được xuất từ:

```python
co_op_translator.api
```

API công khai được tổ chức thành các trợ giúp dịch nội dung, trợ giúp ghi lại đường dẫn, điều phối dự án và đánh giá:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
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

Khi thêm API công khai mới, cập nhật:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- các bài kiểm tra API liên quan dưới `tests/co_op_translator/`, chẳng hạn như `test_api.py` hoặc `test_review_api.py`

Tránh tài liệu hóa các mô-đun `core` cấp thấp hơn như API ổn định trừ khi dự án dự định hỗ trợ chúng trực tiếp.

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

`src/co_op_translator/__main__.py` chuyển hướng theo tên script:

- `translate` gọi `co_op_translator.cli.translate.translate_command`
- `evaluate` gọi `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` gọi `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` gọi `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` bỏ qua `__main__.py` và gọi trực tiếp `co_op_translator.mcp.server:main`.

Khi thêm hoặc thay đổi tùy chọn CLI, cập nhật:

- lệnh tương ứng `src/co_op_translator/cli/*.py`
- `docs/cli.md`
- các bài kiểm tra liên quan đến CLI, nếu hành vi thay đổi

## Máy chủ MCP

Máy chủ MCP được triển khai trong:

```python
co_op_translator.mcp.server
```

Máy chủ cố ý bao bọc API Python công khai thay vì gọi các mô-đun `core` cấp thấp hơn. Giữ ranh giới này nguyên vẹn để các client MCP, caller Python và CLI chia sẻ cùng hành vi.

Khi thêm hoặc thay đổi công cụ MCP, cập nhật:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` nếu bề mặt API công khai thay đổi

Các công cụ dịch kho lưu trữ có thể được gọi mô hình thông qua MCP và có thể ghi nhiều tệp. Giữ `dry_run=True` làm mặc định và yêu cầu `confirm_write=True` trước khi dịch dự án không ở chế độ dry-run.

## Quy trình dịch

Quy trình dịch dự án ở mức cao là:

1. Phân tích đối số CLI hoặc tham số API.
2. Xác thực cấu hình LLM với `LLMConfig`.
3. Xác thực Azure AI Vision khi chọn dịch ảnh.
4. Chuẩn hóa mã ngôn ngữ.
5. Phát hiện bí danh thư mục ngôn ngữ cũ.
6. Ước tính khối lượng dịch.
7. Cập nhật các phần ngôn ngữ/khoá học trong README khi thích hợp.
8. Ủy quyền dịch dự án cho `ProjectTranslator`.
9. `ProjectTranslator` ủy quyền xử lý tệp cho `TranslationManager`.

`TranslationManager` được cấu thành từ các mixin chuyên biệt theo loại tệp:

- `ProjectMarkdownTranslationMixin` xử lý đọc tệp Markdown, dịch nội dung, ghi lại đường dẫn, siêu dữ liệu, các tuyên bố từ chối trách nhiệm và ghi tệp.
- `ProjectNotebookTranslationMixin` xử lý đọc tệp notebook, dịch ô Markdown, ghi lại đường dẫn, siêu dữ liệu, các tuyên bố từ chối trách nhiệm và ghi tệp.
- `ProjectImageTranslationMixin` xử lý khám phá hình ảnh, trích xuất/dịch văn bản, ghi ảnh đã kết xuất và siêu dữ liệu.

Các API nội dung cấp thấp hơn bỏ qua luồng công việc dự án:

1. `translate_markdown_content` và `translate_notebook_content` chỉ dịch nội dung trong bộ nhớ.
2. `translate_image_content` dịch văn bản trong một ảnh đơn lẻ và trả về một đối tượng ảnh đã kết xuất.
3. `rewrite_markdown_paths` và `rewrite_notebook_paths` là các trợ giúp xử lý hậu kỳ rõ ràng. Chúng không thực hiện dịch và không ghi tệp dự án.

## Quy trình đánh giá

Quy trình đánh giá mang tính xác định như sau:

1. Phân tích đối số CLI hoặc tham số API.
2. Chuẩn hóa các mã ngôn ngữ được yêu cầu.
3. Xây dựng một hoặc nhiều mục tiêu đánh giá từ `root_dir`, `root_dirs`, hoặc `groups`.
4. Tùy chọn giới hạn tệp nguồn với `--changed-from`.
5. Chạy các kiểm tra có tính quyết định về cấu trúc, độ tươi của bản dịch, tính toàn vẹn của Markdown và các đường dẫn liên kết/ảnh cục bộ.
6. In ra đầu ra dạng văn bản hoặc Markdown theo chuẩn GitHub.
7. Thoát với trạng thái thất bại khi tìm thấy lỗi đánh giá.

Quy trình đánh giá không yêu cầu khoá API và nên vẫn phù hợp cho CI của pull request. Luồng công việc pull request ghi một tóm tắt kiểm tra ở mỗi lần chạy và chỉ đăng một bình luận PR khi `co-op-review` thất bại.

## Trang tài liệu

Trang tài liệu được cấu hình bởi:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

Thư mục `docs/` là nguồn tài liệu chính thức. Không thêm hướng dẫn cho người dùng cuối mới ngoài thư mục này trừ khi dự án có chủ ý giới thiệu một bề mặt tài liệu công khai khác.

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

## Quy trình GitHub Pages

.github/workflows/docs.yml xây dựng trang trên pull request và triển khai nó khi có push lên `main`.

Quy trình cài đặt:

```bash
pip install -r requirements-docs.txt
```

Luồng công việc tài liệu chỉ cài đặt chuỗi công cụ tài liệu. `mkdocs.yml` trỏ `mkdocstrings` vào `src/` để các trang API công khai có thể được kết xuất từ cây nguồn mà không cần cài đặt đầy đủ tập phụ thuộc runtime. Nếu tài liệu API trong tương lai yêu cầu nhập các nhà cung cấp runtime tùy chọn trong quá trình xây dựng, hãy cập nhật cả `.github/workflows/docs.yml` và hướng dẫn này cùng lúc.

## Tiêu chuẩn chất lượng tài liệu

Trước khi gộp các thay đổi tài liệu, chạy:

```bash
python -m mkdocs build --strict
git diff --check
```

Sử dụng chế độ build nghiêm ngặt để các liên kết hỏng, mục điều hướng không hợp lệ và các vấn đề kết xuất API bị phát hiện sớm.