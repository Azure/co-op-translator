<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5eb9b53c81804f04bc9456160e79940",
  "translation_date": "2025-05-07T14:16:57+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "vi"
}
-->
# Cách sử dụng giao diện dòng lệnh (CLI) của Co-op Translator

## Yêu cầu trước

- **Python 3.10 trở lên**: Cần thiết để chạy Co-op Translator.
- **Nguồn tài nguyên Mô hình Ngôn ngữ**:  
  - **Azure OpenAI** hoặc các LLM khác. Chi tiết có thể xem tại [supported models and services](../../../../README.md).
- **Nguồn tài nguyên Thị giác Máy tính** (tùy chọn):  
  - Dùng để dịch hình ảnh. Nếu không có, trình dịch sẽ mặc định sang [Markdown-only mode](../markdown-only-mode.md).  
  - **Azure Computer Vision**

## Mục lục

1. [Tạo file '.env' trong thư mục gốc](./create-env-file.md)  
   - Bao gồm các khóa cần thiết cho dịch vụ mô hình ngôn ngữ đã chọn.  
   - Nếu bỏ qua khóa Azure Computer Vision hoặc chỉ định `-md`, trình dịch sẽ hoạt động ở chế độ Markdown-only.  
1. [Cài đặt gói Co-op translator](./install-package.md)  
1. [Dịch dự án của bạn bằng Co-op Translator](./translator-your-project.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được xem là nguồn thông tin chính xác nhất. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.