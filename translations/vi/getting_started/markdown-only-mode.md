<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-05-06T17:44:39+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "vi"
}
-->
# Sử Dụng Chế Độ Chỉ Markdown

## Giới thiệu  
Chế độ chỉ Markdown được thiết kế để dịch riêng nội dung Markdown của dự án của bạn. Chế độ này bỏ qua quá trình dịch hình ảnh và chỉ tập trung vào nội dung văn bản, rất phù hợp cho những trường hợp không cần dịch hình ảnh hoặc khi các biến môi trường cần thiết cho Computer Vision chưa được thiết lập.

## Khi nào sử dụng  
- Khi các biến môi trường liên quan đến Computer Vision chưa được cấu hình.  
- Khi bạn chỉ muốn dịch nội dung văn bản mà không cập nhật các liên kết hình ảnh.  
- Khi người dùng chỉ định rõ bằng tùy chọn dòng lệnh `-md`.

## Cách kích hoạt  
Để bật chế độ chỉ Markdown, sử dụng tùy chọn `-md` trong lệnh của bạn. Ví dụ:  
```
translate -l "ko" -md
```

Hoặc nếu các biến môi trường liên quan đến Computer Vision chưa được cấu hình, chạy `translate -l "ko"` sẽ tự động chuyển sang chế độ chỉ Markdown.

```
translate -l "ko"
```

Lệnh này dịch nội dung Markdown sang tiếng Hàn và giữ nguyên các liên kết hình ảnh về đường dẫn gốc, thay vì thay đổi chúng thành đường dẫn hình ảnh đã dịch.

## Hành vi  
Trong chế độ chỉ Markdown:  
- Quá trình dịch bỏ qua bước dịch hình ảnh.  
- Các liên kết hình ảnh trong Markdown không thay đổi, vẫn trỏ đến đường dẫn gốc.

## Ví dụ  
### Trước  
```markdown
![Image](../../../getting_started/translated/path/to/image.png)
```  
### Sau khi dùng chế độ chỉ Markdown  
```markdown
![Image](../../../getting_started/original/path/to/image.png)
```

## Khắc phục sự cố  
- Đảm bảo tùy chọn `-md` được chỉ định chính xác trong lệnh.  
- Kiểm tra để chắc chắn không có biến môi trường Computer Vision nào gây ảnh hưởng đến quá trình.

## Kết luận  
Chế độ chỉ Markdown cung cấp cách dịch nội dung văn bản một cách đơn giản mà không thay đổi liên kết hình ảnh. Nó đặc biệt hữu ích khi không cần dịch hình ảnh hoặc khi làm việc trong môi trường chưa thiết lập Computer Vision.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.