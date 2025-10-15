<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:35:41+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "vi"
}
-->
# Hướng Dẫn Khắc Phục Sự Cố Microsoft Co-op Translator

## Tổng Quan
Microsoft Co-Op Translator là một công cụ mạnh mẽ giúp dịch các tài liệu Markdown một cách liền mạch. Hướng dẫn này sẽ giúp bạn xử lý các sự cố thường gặp khi sử dụng công cụ này.

## Các Sự Cố Thường Gặp và Cách Khắc Phục

### 1. Vấn Đề Thẻ Markdown
**Vấn đề:** Tài liệu Markdown đã dịch có thêm thẻ `markdown` ở đầu, gây lỗi hiển thị.

**Cách khắc phục:** Đơn giản chỉ cần xóa thẻ `markdown` ở đầu file. Sau đó file Markdown sẽ hiển thị đúng.

**Các bước:**
1. Mở file Markdown (`.md`) đã dịch.
2. Tìm thẻ `markdown` ở đầu tài liệu.
3. Xóa thẻ `markdown`.
4. Lưu lại file.
5. Mở lại file để kiểm tra hiển thị.

### 2. Vấn Đề URL Ảnh Nhúng
**Vấn đề:** URL của ảnh nhúng không đúng với ngôn ngữ, dẫn đến ảnh sai hoặc không hiển thị.

**Cách khắc phục:** Kiểm tra URL của ảnh nhúng và đảm bảo chúng đúng với ngôn ngữ của tài liệu. Tất cả ảnh nằm trong thư mục `translated_images` và mỗi ảnh có mã ngôn ngữ trong tên file.

**Các bước:**
1. Mở tài liệu Markdown đã dịch.
2. Xác định các ảnh nhúng và URL của chúng.
3. Kiểm tra mã ngôn ngữ trong tên file ảnh có khớp với ngôn ngữ tài liệu không.
4. Cập nhật lại URL nếu cần.
5. Lưu và mở lại tài liệu để xác nhận ảnh hiển thị đúng.

### 3. Độ Chính Xác Dịch Thuật
**Vấn đề:** Nội dung dịch chưa chính xác hoặc cần chỉnh sửa thêm.

**Cách khắc phục:** Xem lại tài liệu đã dịch và chỉnh sửa để tăng độ chính xác, dễ hiểu.

**Các bước:**
1. Mở tài liệu đã dịch.
2. Đọc kỹ nội dung.
3. Chỉnh sửa lại các phần chưa chính xác.
4. Lưu lại thay đổi.

## 4. Lỗi Quyền Truy Cập Bị Ẩn hoặc 404

Nếu ảnh hoặc văn bản không được dịch đúng ngôn ngữ và khi chạy ở chế độ -d debug bạn gặp lỗi 401. Đây là lỗi xác thực điển hình—có thể key không hợp lệ, đã hết hạn, hoặc không liên kết đúng vùng endpoint.

Chạy co-op translator với [tham số -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) để hiểu rõ nguyên nhân gốc.

- **Thông báo lỗi**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Nguyên nhân có thể**:
  - Subscription key bị ẩn hoặc sai trong request.
  - AI Services Key hoặc Subscription Key thuộc về một tài nguyên Azure khác (như Translator hoặc OpenAI) thay vì **Azure AI Vision**.

 **Loại tài nguyên**
  - Truy cập [Azure Portal](https://portal.azure.com) hoặc [Azure AI Foundry](https://ai.azure.com) và đảm bảo tài nguyên là loại `Azure AI services` → `Vision`.
  - Kiểm tra lại key và chắc chắn bạn dùng đúng key.

## 5. Lỗi Cấu Hình (Xử Lý Lỗi Mới)

Bắt đầu từ hệ thống dịch chọn lọc mới, Co-op Translator sẽ cung cấp thông báo lỗi rõ ràng khi thiếu cấu hình dịch vụ cần thiết.

### 5.1. Azure AI Service Chưa Cấu Hình Cho Dịch Ảnh

**Vấn đề:** Bạn yêu cầu dịch ảnh (cờ `-img`) nhưng Azure AI Service chưa được cấu hình đúng.

**Thông báo lỗi:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Cách khắc phục:**
1. **Cách 1**: Cấu hình Azure AI Service
   - Thêm `AZURE_AI_SERVICE_API_KEY` vào file `.env`
   - Thêm `AZURE_AI_SERVICE_ENDPOINT` vào file `.env`
   - Kiểm tra dịch vụ đã truy cập được

2. **Cách 2**: Bỏ yêu cầu dịch ảnh
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Thiếu Cấu Hình Bắt Buộc

**Vấn đề:** Thiếu cấu hình LLM cần thiết.

**Thông báo lỗi:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Cách khắc phục:**
1. Kiểm tra file `.env` có ít nhất một trong các cấu hình LLM sau:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` và `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Bạn chỉ cần cấu hình Azure OpenAI HOẶC OpenAI, không cần cả hai.

### 5.3. Nhầm Lẫn Dịch Chọn Lọc

**Vấn đề:** Không file nào được dịch dù lệnh đã chạy thành công.

**Nguyên nhân có thể:**
- Sai cờ loại file (`-md`, `-img`, `-nb`)
- Không có file phù hợp trong dự án
- Cấu trúc thư mục không đúng

**Cách khắc phục:**
1. **Dùng chế độ debug** để xem chi tiết:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Kiểm tra loại file** trong dự án:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Kiểm tra kết hợp cờ**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Chuyển Đổi Từ Hệ Thống Cũ

### 6.1. Chế Độ Chỉ Markdown Đã Bị Loại Bỏ

**Vấn đề:** Các lệnh dựa vào chế độ chỉ markdown tự động không còn hoạt động như trước.

**Hành vi cũ:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Hành vi mới:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Cách khắc phục:**
- **Chỉ rõ** loại file bạn muốn dịch:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Hành Vi Liên Kết Không Như Mong Đợi

**Vấn đề:** Các liên kết trong file dịch trỏ đến vị trí không mong muốn.

**Nguyên nhân:** Xử lý liên kết động thay đổi theo loại file đã chọn.

**Cách khắc phục:**
1. **Hiểu hành vi liên kết mới**:
   - Có `-nb`: Liên kết notebook trỏ đến bản dịch
   - Không có `-nb`: Liên kết notebook trỏ về file gốc
   - Có `-img`: Liên kết ảnh trỏ đến bản dịch
   - Không có `-img`: Liên kết ảnh trỏ về file gốc

2. **Chọn kết hợp phù hợp** với nhu cầu:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action chạy nhưng không tạo Pull Request (PR)

**Triệu chứng:** Nhật ký workflow cho `peter-evans/create-pull-request` hiển thị:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Nguyên nhân có thể:**
- **Không có thay đổi:** Bước dịch không tạo ra khác biệt nào (repo đã cập nhật).
- **Bỏ qua output:** `.gitignore` loại trừ các file bạn muốn commit (ví dụ: `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths không khớp:** Đường dẫn cung cấp cho action không đúng với vị trí output thực tế.
- **Logic/điều kiện workflow:** Bước dịch kết thúc sớm hoặc ghi ra thư mục không mong muốn.

**Cách kiểm tra/khắc phục:**
1. **Xác nhận output tồn tại:** Sau khi dịch, kiểm tra workspace có file mới/thay đổi trong `translations/` và/hoặc `translated_images/`.
   - Nếu dịch notebook, đảm bảo file `.ipynb` được ghi vào `translations/<lang>/...`.
2. **Kiểm tra `.gitignore`:** Không bỏ qua các output sinh ra. Đảm bảo KHÔNG bỏ qua:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (nếu dịch notebook)
3. **Đảm bảo add-paths khớp output:** Dùng giá trị nhiều dòng và bao gồm cả hai thư mục nếu cần:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Ép tạo PR để debug:** Tạm thời cho phép commit rỗng để kiểm tra wiring:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Chạy với debug:** Thêm `-d` vào lệnh dịch để in ra các file đã phát hiện và ghi.
6. **Quyền (GITHUB_TOKEN):** Đảm bảo workflow có quyền ghi để tạo commit và PR:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Danh Sách Kiểm Tra Khắc Phục Nhanh

Khi xử lý sự cố dịch thuật:

1. **Dùng chế độ debug**: Thêm cờ `-d` để xem log chi tiết
2. **Kiểm tra các cờ**: Đảm bảo `-md`, `-img`, `-nb` đúng với mục đích
3. **Kiểm tra cấu hình**: File `.env` có đủ key cần thiết
4. **Kiểm tra từng bước**: Bắt đầu với `-md` rồi thêm các loại khác
5. **Kiểm tra cấu trúc file**: Đảm bảo file nguồn tồn tại và truy cập được

Để biết thêm chi tiết về các lệnh và cờ, xem [Command Reference](./command-reference.md).

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.