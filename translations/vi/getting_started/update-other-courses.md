<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:47:06+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "vi"
}
-->
# Cập nhật phần "Khóa học khác" (kho lưu trữ Microsoft Beginners)

Hướng dẫn này giải thích cách để phần "Khóa học khác" tự động đồng bộ bằng Co-op Translator, và cách cập nhật mẫu toàn cục cho tất cả các kho lưu trữ.

- Áp dụng cho: Chỉ các kho lưu trữ Microsoft Beginners
- Hoạt động với: Co-op Translator CLI và GitHub Actions
- Nguồn mẫu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Bắt đầu nhanh: Bật tự động đồng bộ trong kho lưu trữ của bạn

Thêm các dấu hiệu sau quanh phần "Khóa học khác" trong README của bạn. Co-op Translator sẽ thay thế mọi thứ nằm giữa các dấu hiệu này mỗi lần chạy.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Mỗi lần Co-op Translator chạy — qua CLI (ví dụ, `translate -l "<language codes>"`) hoặc GitHub Actions — nó sẽ tự động cập nhật phần "Khóa học khác" được bao quanh bởi các dấu hiệu này.

> [!NOTE]
> Nếu bạn đã có danh sách hiện có, chỉ cần bao quanh nó bằng các dấu hiệu tương tự. Lần chạy tiếp theo sẽ thay thế bằng nội dung chuẩn mới nhất.

---

## Cách thay đổi nội dung toàn cục

Nếu bạn muốn cập nhật nội dung chuẩn xuất hiện trong tất cả các kho lưu trữ Beginners:

1. Chỉnh sửa mẫu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Mở pull request lên kho Co-op Translator với các thay đổi của bạn
3. Sau khi PR được hợp nhất, phiên bản Co-op Translator sẽ được cập nhật
4. Lần tiếp theo Co-op Translator chạy (CLI hoặc GitHub Action) trong kho mục tiêu, nó sẽ tự động đồng bộ phần đã cập nhật

Điều này đảm bảo một nguồn dữ liệu duy nhất cho nội dung "Khóa học khác" trên tất cả các kho lưu trữ Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->