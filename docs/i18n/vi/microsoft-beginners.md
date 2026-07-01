# Kho lưu trữ Dành cho Người mới bắt đầu của Microsoft

Trang này dành cho những người duy trì các kho lưu trữ "For Beginners" của Microsoft sử dụng phần README "Other Courses" được chia sẻ.

Hầu hết người dùng Co-op Translator không cần trang này.

## Tự động đồng bộ phần Other Courses

Thêm các dấu đánh dấu này xung quanh phần "Other Courses" trong README của bạn:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Mỗi khi Co-op Translator chạy qua CLI hoặc GitHub Actions, nó sẽ thay thế nội dung giữa các dấu đánh dấu bằng mẫu đã đóng gói.

## Cập nhật mẫu dùng chung

Nguồn mẫu nằm tại:

```text
src/co_op_translator/templates/other_courses.md
```

Để cập nhật nội dung dùng chung:

1. Chỉnh sửa mẫu.
2. Mở một pull request tới Co-op Translator.
3. Sau khi thay đổi được phát hành, chạy Co-op Translator trong kho lưu trữ đích.

## Lời khuyên về Sparse Checkout

Các kho khóa học lớn có thể tốn kém khi clone nếu chúng bao gồm nhiều đầu ra đã được dịch. Bạn có thể bao gồm lời khuyên này trong các phần ngôn ngữ được tạo:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```