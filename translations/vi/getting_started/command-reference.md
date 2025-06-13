<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:30:51+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "vi"
}
-->
# Tham khảo lệnh
CLI **Co-op Translator** cung cấp nhiều tùy chọn để tùy chỉnh quá trình dịch:

Lệnh                                         | Mô tả
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Dịch dự án của bạn sang các ngôn ngữ được chỉ định. Ví dụ: translate -l "es fr de" dịch sang tiếng Tây Ban Nha, Pháp và Đức. Dùng translate -l "all" để dịch sang tất cả các ngôn ngữ được hỗ trợ.
translate -l "language_codes" -u              | Cập nhật bản dịch bằng cách xóa các bản dịch hiện có và tạo lại. Cảnh báo: Lệnh này sẽ xóa tất cả bản dịch hiện tại cho các ngôn ngữ được chỉ định.
translate -l "language_codes" -img            | Chỉ dịch các tập tin hình ảnh.
translate -l "language_codes" -md             | Chỉ dịch các tập tin Markdown.
translate -l "language_codes" -chk            | Kiểm tra các tập tin đã dịch để tìm lỗi và thử dịch lại nếu cần.
translate -l "language_codes" -d              | Bật chế độ gỡ lỗi để ghi lại chi tiết.
translate -l "language_codes" -r "root_dir"   | Chỉ định thư mục gốc của dự án
translate -l "language_codes" -f              | Sử dụng chế độ nhanh cho dịch hình ảnh (tốc độ nhanh hơn đến 3 lần với một chút ảnh hưởng đến chất lượng và căn chỉnh).
translate -l "language_codes" -y              | Tự động xác nhận tất cả các yêu cầu (hữu ích cho CI/CD)
translate -l "language_codes" --help          | Hiển thị trợ giúp trong CLI với các lệnh có sẵn

### Ví dụ sử dụng:

  1. Hành vi mặc định (thêm bản dịch mới mà không xóa các bản dịch hiện có):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Chỉ thêm bản dịch hình ảnh mới cho tiếng Hàn (không xóa bản dịch hiện có):    translate -l "ko" -img

  3. Cập nhật tất cả bản dịch tiếng Hàn (Cảnh báo: Lệnh này sẽ xóa tất cả bản dịch tiếng Hàn hiện có trước khi dịch lại):    translate -l "ko" -u

  4. Chỉ cập nhật hình ảnh tiếng Hàn (Cảnh báo: Lệnh này sẽ xóa tất cả hình ảnh tiếng Hàn hiện có trước khi dịch lại):    translate -l "ko" -img -u

  5. Thêm bản dịch Markdown mới cho tiếng Hàn mà không ảnh hưởng đến các bản dịch khác:    translate -l "ko" -md

  6. Kiểm tra các tập tin đã dịch để tìm lỗi và thử dịch lại nếu cần: translate -l "ko" -chk

  7. Kiểm tra các tập tin đã dịch để tìm lỗi và thử dịch lại (chỉ Markdown): translate -l "ko" -chk -md

  8. Kiểm tra các tập tin đã dịch để tìm lỗi và thử dịch lại (chỉ hình ảnh): translate -l "ko" -chk -img

  9. Sử dụng chế độ nhanh cho dịch hình ảnh:    translate -l "ko" -img -f

  10. Ví dụ chế độ gỡ lỗi: - translate -l "ko" -d: Bật ghi log gỡ lỗi.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được xem là nguồn tham khảo chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.