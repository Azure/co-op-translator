<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-05-06T17:51:24+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "vi"
}
-->
# Hướng Dẫn Khắc Phục Sự Cố Microsoft Co-op Translator

## Tổng Quan  
Microsoft Co-Op Translator là một công cụ mạnh mẽ giúp dịch các tài liệu Markdown một cách liền mạch. Hướng dẫn này sẽ giúp bạn khắc phục những sự cố phổ biến khi sử dụng công cụ.

## Các Sự Cố Thường Gặp và Cách Khắc Phục

### 1. Vấn Đề Thẻ Markdown  
**Vấn đề:** Tài liệu Markdown đã dịch bao gồm thẻ `markdown` ở đầu file, gây ra lỗi hiển thị.

**Cách khắc phục:** Để sửa lỗi này, chỉ cần xóa thẻ `markdown` ở đầu file. Điều này sẽ giúp file Markdown hiển thị đúng.

**Các bước thực hiện:**  
1. Mở file Markdown đã dịch (`.md`).  
2. Tìm thẻ `markdown` ở đầu tài liệu.  
3. Xóa thẻ `markdown`.  
4. Lưu lại thay đổi.  
5. Mở lại file để đảm bảo hiển thị đúng.

### 2. Vấn Đề URL Ảnh Nhúng  
**Vấn đề:** URL của các ảnh nhúng không khớp với ngôn ngữ bản địa, dẫn đến ảnh bị sai hoặc không hiển thị.

**Cách khắc phục:** Kiểm tra URL của ảnh nhúng và đảm bảo chúng phù hợp với ngôn ngữ bản địa. Tất cả ảnh nằm trong thư mục `translated_images`, mỗi ảnh có thẻ ngôn ngữ trong tên file ảnh.

**Các bước thực hiện:**  
1. Mở tài liệu Markdown đã dịch.  
2. Xác định các ảnh nhúng và URL của chúng.  
3. Kiểm tra xem thẻ ngôn ngữ trong tên file ảnh có khớp với ngôn ngữ tài liệu không.  
4. Cập nhật URL nếu cần thiết.  
5. Lưu lại và mở lại tài liệu để xác nhận ảnh hiển thị đúng.

### 3. Độ Chính Xác Bản Dịch  
**Vấn đề:** Nội dung dịch không chính xác hoặc cần chỉnh sửa thêm.

**Cách khắc phục:** Xem lại tài liệu đã dịch và chỉnh sửa cần thiết để nâng cao độ chính xác và dễ hiểu.

**Các bước thực hiện:**  
1. Mở tài liệu đã dịch.  
2. Xem xét kỹ nội dung.  
3. Chỉnh sửa để cải thiện độ chính xác bản dịch.  
4. Lưu lại thay đổi.

### 4. Vấn Đề Định Dạng File  
**Vấn đề:** Định dạng của tài liệu dịch không đúng. Điều này có thể xảy ra với bảng, ở đây thêm ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` sẽ giúp xử lý các vấn đề về bảng.

**Các bước thực hiện:**  
1. Mở tài liệu đã dịch.  
2. So sánh với tài liệu gốc để phát hiện lỗi định dạng.  
3. Điều chỉnh định dạng cho khớp với tài liệu gốc.  
4. Lưu lại thay đổi.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được xem là nguồn tham khảo chính xác nhất. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.