<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:35:15+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "vi"
}
-->
# Tham khảo lệnh

CLI **Co-op Translator** cung cấp nhiều tùy chọn để bạn tùy chỉnh quá trình dịch:

Lệnh                                         | Mô tả
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Dịch dự án của bạn sang các ngôn ngữ được chỉ định. Ví dụ: translate -l "es fr de" sẽ dịch sang tiếng Tây Ban Nha, Pháp và Đức. Sử dụng translate -l "all" để dịch sang tất cả các ngôn ngữ được hỗ trợ.
translate -l "language_codes" -u              | Cập nhật bản dịch bằng cách xóa các bản dịch hiện có và tạo lại. Cảnh báo: Thao tác này sẽ xóa toàn bộ bản dịch hiện tại cho các ngôn ngữ được chỉ định.
translate -l "language_codes" -img            | Chỉ dịch các tệp hình ảnh.
translate -l "language_codes" -md             | Chỉ dịch các tệp Markdown.
translate -l "language_codes" -nb             | Chỉ dịch các tệp Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Dịch lại các tệp có điểm tin cậy thấp dựa trên kết quả đánh giá trước đó.
translate -l "language_codes" -d              | Bật chế độ debug để ghi log chi tiết.
translate -l "language_codes" --save-logs, -s | Lưu log cấp DEBUG vào các tệp trong <root_dir>/logs/ (console vẫn được kiểm soát bởi -d)
translate -l "language_codes" -r "root_dir"   | Chỉ định thư mục gốc của dự án
translate -l "language_codes" -f              | Sử dụng chế độ nhanh cho dịch hình ảnh (tốc độ vẽ nhanh hơn gấp 3 lần, nhưng chất lượng và căn chỉnh có thể giảm nhẹ).
translate -l "language_codes" -y              | Tự động xác nhận tất cả các nhắc (hữu ích cho các pipeline CI/CD)
translate -l "language_codes" --help          | Hiển thị chi tiết trợ giúp trong CLI về các lệnh có sẵn
evaluate -l "language_code"                  | Đánh giá chất lượng bản dịch cho một ngôn ngữ cụ thể và cung cấp điểm tin cậy
evaluate -l "language_code" -c 0.8           | Đánh giá bản dịch với ngưỡng tin cậy tùy chỉnh
evaluate -l "language_code" -f               | Chế độ đánh giá nhanh (chỉ dựa trên quy tắc, không dùng LLM)
evaluate -l "language_code" -D               | Chế độ đánh giá sâu (chỉ dùng LLM, kỹ lưỡng hơn nhưng chậm hơn)
evaluate -l "language_code" --save-logs, -s  | Lưu log cấp DEBUG vào các tệp trong <root_dir>/logs/
migrate-links -l "language_codes"             | Xử lý lại các tệp Markdown đã dịch để cập nhật liên kết tới notebook (.ipynb). Ưu tiên notebook đã dịch nếu có; nếu không sẽ dùng notebook gốc.
migrate-links -l "language_codes" -r          | Chỉ định thư mục gốc của dự án (mặc định: thư mục hiện tại).
migrate-links -l "language_codes" --dry-run   | Hiển thị các tệp sẽ thay đổi mà không ghi thay đổi vào tệp.
migrate-links -l "language_codes" --no-fallback-to-original | Không chuyển liên kết về notebook gốc khi thiếu notebook đã dịch (chỉ cập nhật khi có bản dịch).
migrate-links -l "language_codes" -d          | Bật chế độ debug để ghi log chi tiết.
migrate-links -l "language_codes" --save-logs, -s | Lưu log cấp DEBUG vào các tệp trong <root_dir>/logs/
migrate-links -l "all" -y                      | Xử lý tất cả ngôn ngữ và tự động xác nhận cảnh báo.

## Ví dụ sử dụng

  1. Hành vi mặc định (thêm bản dịch mới mà không xóa bản dịch hiện có):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Chỉ thêm bản dịch hình ảnh tiếng Hàn mới (không xóa bản dịch hiện có):    translate -l "ko" -img

  3. Cập nhật toàn bộ bản dịch tiếng Hàn (Cảnh báo: Thao tác này sẽ xóa toàn bộ bản dịch tiếng Hàn hiện có trước khi dịch lại):    translate -l "ko" -u

  4. Chỉ cập nhật hình ảnh tiếng Hàn (Cảnh báo: Thao tác này sẽ xóa toàn bộ hình ảnh tiếng Hàn hiện có trước khi dịch lại):    translate -l "ko" -img -u

  5. Thêm bản dịch markdown mới cho tiếng Hàn mà không ảnh hưởng đến các bản dịch khác:    translate -l "ko" -md

  6. Sửa các bản dịch có điểm tin cậy thấp dựa trên kết quả đánh giá trước đó: translate -l "ko" --fix

  7. Sửa các bản dịch có điểm tin cậy thấp cho các tệp cụ thể (markdown): translate -l "ko" --fix -md

  8. Sửa các bản dịch có điểm tin cậy thấp cho các tệp cụ thể (hình ảnh): translate -l "ko" --fix -img

  9. Sử dụng chế độ nhanh cho dịch hình ảnh:    translate -l "ko" -img -f

  10. Sửa các bản dịch có điểm tin cậy thấp với ngưỡng tùy chỉnh: translate -l "ko" --fix -c 0.8

  11. Ví dụ chế độ debug: - translate -l "ko" -d: Bật ghi log debug.
  12. Lưu log vào tệp: translate -l "ko" -s
  13. Ghi log DEBUG trên console và tệp: translate -l "ko" -d -s

  14. Di chuyển liên kết notebook cho bản dịch tiếng Hàn (cập nhật liên kết tới notebook đã dịch nếu có):    migrate-links -l "ko"

  15. Di chuyển liên kết với chế độ dry-run (không ghi tệp):    migrate-links -l "ko" --dry-run

  16. Chỉ cập nhật liên kết khi có notebook đã dịch (không chuyển về bản gốc):    migrate-links -l "ko" --no-fallback-to-original

  17. Xử lý tất cả ngôn ngữ với nhắc xác nhận:    migrate-links -l "all"

  18. Xử lý tất cả ngôn ngữ và tự động xác nhận:    migrate-links -l "all" -y
  19. Lưu log vào tệp cho migrate-links:    migrate-links -l "ko ja" -s

### Ví dụ đánh giá

> [!WARNING]  
> **Tính năng Beta**: Chức năng đánh giá hiện đang ở giai đoạn beta. Tính năng này được phát hành để đánh giá các tài liệu đã dịch, và phương pháp đánh giá cũng như cách triển khai chi tiết vẫn đang được phát triển và có thể thay đổi.

  1. Đánh giá bản dịch tiếng Hàn: evaluate -l "ko"

  2. Đánh giá với ngưỡng tin cậy tùy chỉnh: evaluate -l "ko" -c 0.8

  3. Đánh giá nhanh (chỉ dựa trên quy tắc): evaluate -l "ko" -f

  4. Đánh giá sâu (chỉ dùng LLM): evaluate -l "ko" -D

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.