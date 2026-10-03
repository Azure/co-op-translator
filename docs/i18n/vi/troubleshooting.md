# Khắc phục sự cố

Sử dụng trang này khi một lần chạy dịch thành công một cách không mong đợi, thất bại trong quá trình cấu hình, hoặc tạo ra đầu ra cần được xem xét.

## Bắt đầu ở đây

1. Chạy một lệnh tập trung trước, chẳng hạn `translate -l "ko" -md`.
2. Thêm `-d` để bật nhật ký gỡ lỗi trên console.
3. Thêm `-s` để lưu nhật ký gỡ lỗi vào `<root-dir>/logs/`.
4. Chạy `co-op-review` sau khi dịch để kiểm tra tính cập nhật, cấu trúc và các liên kết cục bộ.

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

- Cấu hình Azure OpenAI, OpenAI, hoặc Anthropic.
- Xác minh các biến tồn tại trong môi trường nơi lệnh được chạy.
- Đối với sử dụng cục bộ, đặt chúng trong `.env` ở thư mục gốc dự án.

Xem [Cấu hình](configuration.md).

### Dịch hình ảnh khi không có Azure AI Vision

Lỗi:

```text
Image translation requested but Azure AI Service is not configured.
```

Khắc phục:

- Thêm `AZURE_AI_SERVICE_API_KEY`.
- Thêm `AZURE_AI_SERVICE_ENDPOINT`.
- Hoặc chạy lệnh chỉ xử lý văn bản như `translate -l "ko" -md`.

### Khóa hoặc Endpoint không hợp lệ

Các triệu chứng có thể bao gồm `401`, lỗi quyền bị ẩn, hoặc lỗi truy cập endpoint.

Khắc phục:

- Xác nhận khóa thuộc cùng một tài nguyên Azure với endpoint.
- Xác nhận tài nguyên hỗ trợ Vision khi sử dụng `-img`.
- Xác nhận tên triển khai Azure OpenAI và phiên bản API khớp với triển khai của bạn.
- Chạy với nhật ký gỡ lỗi: `translate -l "ko" -md -d -s`.

## Không có tệp nào được dịch

Nguyên nhân thường gặp:

- Các cờ được chọn không khớp với tệp của bạn.
- Đã tồn tại các tệp đã được dịch.
- Các tệp nguồn nằm trong các thư mục bị loại trừ.
- Lệnh đang chạy từ thư mục gốc dự án sai.

Kiểm tra:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Sử dụng `--root-dir` khi lệnh được chạy bên ngoài thư mục gốc dự án.

## Hành vi liên kết bất ngờ

Việc viết lại liên kết phụ thuộc vào các loại nội dung được chọn:

- `-nb` được bao gồm: liên kết notebook có thể trỏ tới các notebook đã được dịch.
- `-nb` không được bao gồm: liên kết notebook có thể vẫn trỏ tới các notebook nguồn.
- `-img` được bao gồm: liên kết hình ảnh có thể trỏ tới các hình ảnh đã được dịch.
- `-img` không được bao gồm: liên kết hình ảnh có thể vẫn trỏ tới các hình ảnh nguồn.

Chạy dịch toàn bộ nội dung khi tất cả liên kết nội bộ nên ưu tiên đầu ra đã dịch:

```bash
translate -l "ko" -md -nb -img
```

Chạy kiểm tra liên kết sau khi dịch:

```bash
co-op-review -l "ko"
```

## Vấn đề hiển thị Markdown

Nếu Markdown đã dịch hiển thị không đúng:

- Kiểm tra rằng frontmatter bắt đầu và kết thúc bằng `---`.
- Kiểm tra rằng số lượng hàng rào mã (code fence) khớp giữa tệp nguồn và tệp đã dịch.
- Chạy `co-op-review` để phát hiện các vấn đề cấu trúc phổ biến.
- Dịch lại tệp cụ thể nếu đầu ra bị hỏng.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action đã chạy nhưng không tạo Pull Request

Nếu `peter-evans/create-pull-request` báo rằng nhánh không đứng trước base, workflow đã không tìm thấy tệp nào để commit.

Nguyên nhân có thể là:

- Lần chạy dịch không tạo thay đổi nào.
- `.gitignore` loại trừ `translations/`, `translated_images/`, hoặc các notebook đã dịch.
- `add-paths` không khớp với các thư mục đầu ra được tạo.
- Bước dịch đã thoát sớm.

Khắc phục:

1. Xác nhận các tệp được tạo tồn tại trong `translations/` hoặc `translated_images/`.
2. Xác nhận `.gitignore` không bỏ qua các đầu ra được tạo.
3. Sử dụng `add-paths` phù hợp:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Tạm thời thêm các cờ gỡ lỗi vào lệnh translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Xác nhận quyền của workflow bao gồm:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Chất lượng bản dịch

Bản dịch máy có thể cần được xem xét bởi con người. Chỉ dùng `evaluate` khi bạn muốn chấm điểm chất lượng mang tính thử nghiệm và các quy trình sửa chữa cho kết quả có độ tin cậy thấp.

!!! warning "Thử nghiệm"
    `evaluate` có thể sử dụng các kiểm tra dựa trên quy tắc và dựa trên LLM, và mô hình chấm điểm cùng hành vi metadata của nó có thể thay đổi. Không đưa nó vào các bước CI bắt buộc trừ khi workflow của bạn đã chuẩn bị cho những thay đổi.

Đối với các kiểm tra CI xác định, hãy sử dụng `co-op-review` thay vào đó.