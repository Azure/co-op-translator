<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:41:48+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "vi"
}
-->
# Sử Dụng Chế Độ Chỉ Markdown

## Giới Thiệu
Chế độ chỉ Markdown được thiết kế để dịch riêng nội dung Markdown của dự án của bạn. Chế độ này bỏ qua quá trình dịch hình ảnh và chỉ tập trung vào nội dung văn bản, rất phù hợp trong các trường hợp không cần dịch hình ảnh hoặc các biến môi trường cần thiết cho Computer Vision chưa được thiết lập.

## Khi Nào Nên Sử Dụng
- Khi các biến môi trường liên quan đến Computer Vision chưa được cấu hình.
- Khi bạn chỉ muốn dịch nội dung văn bản mà không cập nhật liên kết hình ảnh.
- Khi người dùng chỉ định rõ bằng tùy chọn dòng lệnh `-md`.

## Cách Bật
Để kích hoạt chế độ chỉ Markdown, sử dụng tùy chọn `-md` trong lệnh của bạn. Ví dụ:
```
translate -l "ko" -md
```

Hoặc nếu các biến môi trường liên quan đến Computer Vision chưa được cấu hình. Chạy `translate -l "ko"` sẽ tự động chuyển sang chế độ chỉ Markdown.

```
translate -l "ko"
```

Lệnh này dịch nội dung Markdown sang tiếng Hàn và giữ nguyên liên kết hình ảnh đến đường dẫn gốc, thay vì thay đổi sang đường dẫn hình ảnh đã dịch.

## Hành Vi
Trong chế độ chỉ Markdown:
- Quá trình dịch bỏ qua bước dịch hình ảnh.
- Liên kết hình ảnh trong Markdown vẫn giữ nguyên, trỏ đến đường dẫn gốc.

## Ví Dụ
### Trước
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.vi.png)
```
### Sau khi dùng chế độ chỉ Markdown
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.vi.png)
```

## Khắc Phục Sự Cố
- Đảm bảo tùy chọn `-md` được chỉ định chính xác trong lệnh.
- Kiểm tra không có biến môi trường Computer Vision nào gây cản trở quá trình.

## Kết Luận
Chế độ chỉ Markdown cung cấp cách đơn giản để dịch nội dung văn bản mà không thay đổi liên kết hình ảnh. Chế độ này đặc biệt hữu ích khi không cần dịch hình ảnh hoặc khi làm việc trong môi trường chưa thiết lập Computer Vision.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được xem là nguồn thông tin chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.