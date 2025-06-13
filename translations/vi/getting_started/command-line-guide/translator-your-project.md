<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:52:28+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "vi"
}
-->
# Dịch dự án của bạn bằng Co-op Translator

**Co-op Translator** là một công cụ dòng lệnh (CLI) giúp bạn dịch các tệp markdown và hình ảnh trong dự án sang nhiều ngôn ngữ khác nhau. Phần này giải thích cách sử dụng công cụ, trình bày các tùy chọn CLI và cung cấp các ví dụ cho các trường hợp sử dụng khác nhau.

> [!NOTE]
> Để xem danh sách đầy đủ các lệnh cùng mô tả chi tiết, vui lòng tham khảo [Command reference](./command-reference.md).

---

## Các Tình Huống và Lệnh Ví Dụ

Dưới đây là một số trường hợp sử dụng phổ biến của **Co-op Translator**, kèm theo các lệnh thích hợp để chạy.

### 1. Dịch Cơ Bản (Một Ngôn Ngữ)

Để dịch toàn bộ dự án của bạn (các tệp markdown và hình ảnh) sang một ngôn ngữ duy nhất, ví dụ tiếng Hàn, hãy dùng lệnh sau:

```bash
translate -l "ko"
```

Lệnh này sẽ dịch tất cả các tệp markdown và hình ảnh sang tiếng Hàn, thêm bản dịch mới mà không xóa bất kỳ bản dịch hiện có nào.

> [!TIP]
>
> Muốn biết các mã ngôn ngữ được hỗ trợ trong **Co-op Translator**? Hãy xem phần [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) trong kho lưu trữ để biết thêm chi tiết.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi đã dùng phương pháp sau để thêm bản dịch tiếng Hàn cho các tệp markdown và hình ảnh hiện có.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Dịch Nhiều Ngôn Ngữ

Để dịch dự án sang nhiều ngôn ngữ (ví dụ: tiếng Tây Ban Nha, tiếng Pháp và tiếng Đức), sử dụng lệnh này:

```bash
translate -l "es fr de"
```

Lệnh này sẽ dịch dự án sang tiếng Tây Ban Nha, Pháp và Đức, thêm bản dịch mới mà không ghi đè các bản dịch hiện có.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, sau khi kéo các thay đổi mới nhất để cập nhật các cam kết gần đây, tôi đã dùng phương pháp sau để dịch các tệp markdown và hình ảnh mới được thêm.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Mặc dù thường khuyến nghị dịch từng ngôn ngữ một, nhưng trong những trường hợp cần thêm các thay đổi cụ thể như thế này, việc dịch nhiều ngôn ngữ cùng lúc có thể hiệu quả hơn.

### 3. Cập Nhật Bản Dịch (Xóa Bản Dịch Hiện Có)

Để cập nhật các bản dịch hiện có (tức là xóa các bản dịch hiện tại và thay thế bằng bản mới), hãy dùng tùy chọn `-u`. Tùy chọn này sẽ xóa tất cả bản dịch hiện có của các ngôn ngữ được chỉ định và dịch lại.

```bash
translate -l "ko" -u
```

Cảnh báo: Lệnh này sẽ yêu cầu bạn xác nhận trước khi tiến hành xóa các bản dịch hiện có.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi đã dùng phương pháp sau để cập nhật tất cả các tệp đã dịch sang tiếng Tây Ban Nha. Tôi khuyên bạn nên dùng cách này khi có nhiều thay đổi lớn trong nội dung gốc trên nhiều tệp markdown. Nếu chỉ có vài tệp markdown đã dịch cần cập nhật, sẽ hiệu quả hơn khi xóa thủ công các tệp đó rồi dùng phương pháp `-a` để thêm bản dịch mới.

### 5. Chỉ Dịch Hình Ảnh

Để chỉ dịch các tệp hình ảnh trong dự án, dùng tùy chọn `-img`:

```bash
translate -l "ko" -img
```

Lệnh này chỉ dịch các hình ảnh sang tiếng Hàn mà không ảnh hưởng đến các tệp markdown.

### 6. Chỉ Dịch Các Tệp Markdown

Để chỉ dịch các tệp markdown trong dự án, dùng tùy chọn `-md`:

```bash
translate -l "ko" -md
```

### 7. Kiểm Tra Lỗi Trong Các Tệp Đã Dịch

Nếu bạn muốn kiểm tra lỗi trong các tệp đã dịch và thử dịch lại nếu cần, dùng tùy chọn `-chk`:

```bash
translate -l "ko" -chk
```

Lệnh này sẽ quét các tệp markdown đã dịch và thử dịch lại những tệp có lỗi.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi đã dùng phương pháp sau để kiểm tra lỗi dịch trong các tệp tiếng Hàn và tự động thử dịch lại các tệp phát hiện có lỗi.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Tùy chọn này kiểm tra lỗi dịch. Hiện tại, nếu sự khác biệt về ngắt dòng giữa tệp gốc và tệp dịch vượt quá sáu dòng, tệp đó sẽ được đánh dấu là có lỗi dịch. Tôi dự định cải thiện tiêu chí này để linh hoạt hơn trong tương lai.

Ví dụ, cách này hữu ích để phát hiện các phần bị thiếu hoặc bản dịch bị lỗi, và nó sẽ tự động thử dịch lại các tệp đó.

Tuy nhiên, nếu bạn đã biết chính xác tệp nào gặp vấn đề, hiệu quả hơn khi xóa thủ công các tệp đó và dùng tùy chọn `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Lệnh này sẽ chạy bản dịch ở chế độ gỡ lỗi, cung cấp thêm thông tin ghi log giúp bạn xác định vấn đề trong quá trình dịch.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi gặp vấn đề khi các bản dịch có nhiều liên kết trong tệp markdown gây lỗi định dạng, như bản dịch bị lỗi hoặc bỏ qua ngắt dòng. Để chẩn đoán, tôi đã dùng tùy chọn `-d` để xem quá trình dịch hoạt động thế nào.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Dịch Tất Cả Ngôn Ngữ

Nếu bạn muốn dịch dự án sang tất cả các ngôn ngữ được hỗ trợ, hãy dùng từ khóa all.

> [!WARNING]
> Dịch tất cả ngôn ngữ cùng lúc có thể mất nhiều thời gian tùy theo kích thước dự án. Ví dụ, dịch **Phi-3 CookBook** sang tiếng Tây Ban Nha mất khoảng 2 giờ. Với quy mô này, không thực tế để một người xử lý 20 ngôn ngữ. Nên chia công việc cho nhiều người đóng góp, mỗi người quản lý một hoặc hai ngôn ngữ và cập nhật bản dịch dần dần.

```bash
translate -l "all"
```

Lệnh này sẽ dịch dự án sang tất cả các ngôn ngữ có sẵn. Nếu bạn tiếp tục, quá trình dịch có thể mất nhiều thời gian tùy thuộc vào kích thước dự án.

> [!TIP]
>
> ### Xóa Thủ Công Các Tệp Đã Dịch (Tùy Chọn)
> Các tệp đã dịch hiện được tự động phát hiện và dọn dẹp khi tệp nguồn được cập nhật.
>
> Tuy nhiên, nếu bạn muốn cập nhật bản dịch thủ công — ví dụ, để làm lại một tệp cụ thể hoặc ghi đè hành vi hệ thống — bạn có thể dùng lệnh sau để xóa tất cả các phiên bản của tệp đó trong các thư mục ngôn ngữ.
>
> ### Trên Windows:
> 1. **Dùng Command Prompt**:
>    - Mở Command Prompt.
>    - Điều hướng đến thư mục chứa các tệp bằng lệnh `cd`.
>    - Dùng lệnh sau để xóa tệp:
>      ```
>      del /s *filename*
>      ```
>      Tùy chọn `/s` tìm kiếm trong các thư mục con.
>
> 2. **Dùng PowerShell**:
>    - Mở PowerShell.
>    - Chạy lệnh này:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Thay thế `"C:\YourPath"` bằng đường dẫn thực tế.
>
>    - Lệnh `cd`.
>   - Use the `find`:
>      ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>
>    - Lệnh `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` để cập nhật các thay đổi tệp gần đây.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ bản địa nên được xem là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu nhầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.