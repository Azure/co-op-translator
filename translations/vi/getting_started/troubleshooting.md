<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:28:49+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "vi"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Tổng quan
Microsoft Co-Op Translator là công cụ mạnh mẽ giúp dịch các tài liệu Markdown một cách liền mạch. Hướng dẫn này sẽ giúp bạn khắc phục các sự cố phổ biến khi sử dụng công cụ.

## Các sự cố thường gặp và cách giải quyết

### 1. Vấn đề thẻ Markdown
**Vấn đề:** Tài liệu Markdown đã dịch có chứa thẻ `markdown` ở đầu, gây lỗi hiển thị.

**Giải pháp:** Để khắc phục, bạn chỉ cần xóa thẻ `markdown` ở đầu file. Điều này sẽ giúp tài liệu Markdown hiển thị đúng.

**Các bước:**
1. Mở file Markdown đã dịch (`.md`).
2. Tìm thẻ `markdown` ở đầu tài liệu.
3. Xóa thẻ `markdown`.
4. Lưu lại thay đổi.
5. Mở lại file để kiểm tra xem đã hiển thị đúng chưa.

### 2. Vấn đề URL hình ảnh nhúng
**Vấn đề:** URL của hình ảnh nhúng không khớp với ngôn ngữ của tài liệu, dẫn đến hình ảnh bị sai hoặc không hiển thị.

**Giải pháp:** Kiểm tra URL của hình ảnh nhúng và đảm bảo chúng phù hợp với ngôn ngữ của tài liệu. Tất cả hình ảnh nằm trong thư mục `translated_images`, mỗi hình có thẻ ngôn ngữ trong tên file.

**Các bước:**
1. Mở tài liệu Markdown đã dịch.
2. Xác định các hình ảnh nhúng và URL của chúng.
3. Kiểm tra xem thẻ ngôn ngữ trong tên file hình ảnh có khớp với ngôn ngữ tài liệu không.
4. Cập nhật URL nếu cần thiết.
5. Lưu lại và mở lại tài liệu để xác nhận hình ảnh hiển thị đúng.

### 3. Độ chính xác bản dịch
**Vấn đề:** Nội dung dịch không chính xác hoặc cần chỉnh sửa thêm.

**Giải pháp:** Xem lại tài liệu đã dịch và chỉnh sửa để nâng cao độ chính xác và dễ đọc.

**Các bước:**
1. Mở tài liệu đã dịch.
2. Đọc kỹ nội dung.
3. Thực hiện các chỉnh sửa cần thiết để cải thiện độ chính xác bản dịch.
4. Lưu lại thay đổi.

### 4. Vấn đề định dạng file
**Vấn đề:** Định dạng của tài liệu dịch không đúng. Điều này có thể xảy ra với bảng, ở đây thêm ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` sẽ giúp giải quyết vấn đề bảng.

**Các bước:**
1. Mở tài liệu đã dịch.
2. So sánh với tài liệu gốc để xác định lỗi định dạng.
3. Điều chỉnh định dạng cho giống tài liệu gốc.
4. Lưu lại thay đổi.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được xem là nguồn chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.