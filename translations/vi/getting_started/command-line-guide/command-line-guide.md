<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d8eec418d6325416b9fab19a2dfcbf41",
  "translation_date": "2025-05-06T17:53:16+00:00",
  "source_file": "getting_started/command-line-guide/command-line-guide.md",
  "language_code": "vi"
}
-->
# Cách sử dụng giao diện dòng lệnh (CLI) của Co-op Translator

## Yêu cầu trước

- **Python 3.10 trở lên**: Cần thiết để chạy Co-op Translator.
- **Nguồn mô hình ngôn ngữ**:  
  - **Azure OpenAI** hoặc các LLM khác. Chi tiết xem tại [supported models and services](../../../../README.md).
- **Nguồn Computer Vision** (tuỳ chọn):  
  - Dùng cho dịch ảnh. Nếu không có, trình dịch sẽ chuyển sang [Markdown-only mode](../markdown-only-mode.md).  
  - **Azure Computer Vision**

### Thiết lập ban đầu

Trước khi bắt đầu, hãy đảm bảo đã thiết lập các nguồn sau:

- [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)  
- [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md) (tuỳ chọn)

## Mục lục

1. [Tạo file '.env' trong thư mục gốc](./create-env-file.md)  
   - Bao gồm các khóa cần thiết cho dịch vụ mô hình ngôn ngữ đã chọn.  
   - Nếu không nhập khóa Azure Computer Vision hoặc `-md` được chỉ định, trình dịch sẽ chạy ở chế độ Markdown-only.  
3. [Cài đặt gói Co-op translator](./install-package.md)  
4. [Dịch dự án của bạn bằng Co-op Translator](./translator-your-project.md)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.