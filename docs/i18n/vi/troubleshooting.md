# Khắc phục sự cố

Use this page when a translation run succeeds unexpectedly, fails during configuration, or produces output that needs review.

## Bắt đầu tại đây

1. Chạy một lệnh tập trung trước, chẳng hạn như `translate -l "ko" -md`.
2. Thêm `-d` để ghi nhật ký gỡ lỗi trên console.
3. Thêm `-s` để lưu nhật ký gỡ lỗi dưới `<root-dir>/logs/`.
4. Chạy `co-op-review` sau khi dịch để kiểm tra độ tươi mới, cấu trúc, và liên kết cục bộ.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Lỗi cấu hình

### Không có nhà cung cấp mô hình ngôn ngữ

Lỗi:

```text
No language model configuration found.
```

Khắc phục:

- Cấu hình Azure OpenAI hoặc OpenAI.
- Xác minh các biến có trong môi trường nơi lệnh được chạy.
- Đối với sử dụng cục bộ, đặt chúng trong `.env` ở thư mục gốc của dự án.

See [Cấu hình](configuration.md).

### Dịch ảnh khi không có Azure AI Vision

Lỗi:

```text
Image translation requested but Azure AI Service is not configured.
```

Khắc phục:

- Thêm `AZURE_AI_SERVICE_API_KEY`.
- Thêm `AZURE_AI_SERVICE_ENDPOINT`.
- Hoặc chạy một lệnh chỉ văn bản như `translate -l "ko" -md`.

### Khóa hoặc điểm cuối không hợp lệ

Các triệu chứng có thể bao gồm `401`, lỗi quyền bị che giấu, hoặc lỗi truy cập điểm cuối.

Khắc phục:

- Xác nhận khóa thuộc cùng một tài nguyên Azure với điểm cuối.
- Xác nhận tài nguyên hỗ trợ Vision khi sử dụng `-img`.
- Xác nhận tên triển khai Azure OpenAI và phiên bản API khớp với triển khai của bạn.
- Chạy với nhật ký gỡ lỗi: `translate -l "ko" -md -d -s`.

## Không có tệp nào được dịch

Các nguyên nhân thường gặp:

- Các cờ được chọn không khớp với tệp của bạn.
- Các tệp đã dịch đã tồn tại.
- Các tệp nguồn nằm trong các thư mục bị loại trừ.
- Lệnh đang chạy từ thư mục gốc dự án sai.

Kiểm tra:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Use `--root-dir` when the command is run outside the project root.

## Hành vi liên kết bất ngờ

Việc viết lại liên kết phụ thuộc vào các loại nội dung được chọn:

- `-nb` included: notebook links can point to translated notebooks.
- `-nb` excluded: notebook links can remain pointed at source notebooks.
- `-img` included: image links can point to translated images.
- `-img` excluded: image links can remain pointed at source images.

Run a full content translation when all internal links should prefer translated outputs:

```bash
translate -l "ko" -md -nb -img
```

Run link review after translation:

```bash
co-op-review -l "ko"
```

## Sự cố hiển thị Markdown

If translated Markdown renders incorrectly:

- Kiểm tra rằng frontmatter bắt đầu và kết thúc bằng `---`.
- Kiểm tra rằng số lượng dấu phân cách khối mã (code fence) khớp giữa tệp nguồn và tệp đã dịch.
- Chạy `co-op-review` để bắt các vấn đề cấu trúc phổ biến.
- Dịch lại file cụ thể nếu đầu ra bị hỏng.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action đã chạy nhưng không có Pull Request được tạo

If `peter-evans/create-pull-request` reports that the branch is not ahead of base, the workflow found no files to commit.

Nguyên nhân có thể:

- Quá trình dịch không tạo ra thay đổi.
- `.gitignore` loại trừ `translations/`, `translated_images/`, hoặc các notebook đã dịch.
- `add-paths` không khớp với các thư mục đầu ra được tạo.
- Bước dịch đã kết thúc sớm.

Khắc phục:

1. Xác nhận các tệp được tạo tồn tại trong `translations/` hoặc `translated_images/`.
2. Xác nhận `.gitignore` không bỏ qua các đầu ra được tạo.
3. Use matching `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Temporarily add debug flags to the translate command:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirm workflow permissions include:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Chất lượng dịch

Các bản dịch máy có thể cần được xem xét bởi con người. Chỉ sử dụng `evaluate` khi bạn muốn điểm chất lượng mang tính thử nghiệm và các quy trình sửa chữa khi độ tin cậy thấp.

!!! warning "Thử nghiệm"
    `evaluate` có thể sử dụng các kiểm tra dựa trên quy tắc và dựa trên LLM, và mô hình chấm điểm cùng hành vi metadata của nó có thể thay đổi. Không đưa nó vào các cổng CI bắt buộc trừ khi quy trình làm việc của bạn đã sẵn sàng cho những thay đổi.

For deterministic CI checks, use `co-op-review` instead.