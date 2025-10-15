<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:36:08+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "vi"
}
-->
# Dịch dự án của bạn bằng Co-op Translator

**Co-op Translator** là một công cụ dòng lệnh (CLI) giúp bạn dịch các file markdown và hình ảnh trong dự án sang nhiều ngôn ngữ khác nhau. Phần này sẽ hướng dẫn cách sử dụng công cụ, giải thích các tùy chọn CLI, và cung cấp ví dụ cho các trường hợp sử dụng khác nhau.

> [!NOTE]
> Để xem danh sách đầy đủ các lệnh và mô tả chi tiết, hãy tham khảo [Command reference](./command-reference.md).

---

## Các trường hợp ví dụ và lệnh sử dụng

Dưới đây là một số trường hợp sử dụng phổ biến của **Co-op Translator** cùng với các lệnh phù hợp.

### 1. Dịch cơ bản (Một ngôn ngữ)

Để dịch toàn bộ dự án của bạn (file markdown và hình ảnh) sang một ngôn ngữ, ví dụ như tiếng Hàn, hãy dùng lệnh sau:

```bash
translate -l "ko"
```

Lệnh này sẽ dịch tất cả các file markdown và hình ảnh sang tiếng Hàn, thêm bản dịch mới mà không xóa các bản dịch đã có.

> [!TIP]
>
> Muốn biết mã ngôn ngữ nào có sẵn trong **Co-op Translator**? Hãy xem phần [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) trong kho lưu trữ để biết thêm chi tiết.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi đã dùng phương pháp sau để thêm bản dịch tiếng Hàn cho các file markdown và hình ảnh đã có.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Dịch nhiều ngôn ngữ

Để dịch dự án sang nhiều ngôn ngữ (ví dụ: tiếng Tây Ban Nha, tiếng Pháp và tiếng Đức), hãy dùng lệnh sau:

```bash
translate -l "es fr de"
```

Lệnh này sẽ dịch dự án sang tiếng Tây Ban Nha, tiếng Pháp và tiếng Đức, thêm bản dịch mới mà không ghi đè lên các bản dịch đã có.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, sau khi cập nhật các thay đổi mới nhất để phản ánh các commit gần đây, tôi đã dùng phương pháp sau để dịch các file markdown và hình ảnh mới được thêm vào.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Mặc dù thường nên dịch từng ngôn ngữ một, nhưng trong những trường hợp cần thêm các thay đổi cụ thể như thế này, dịch nhiều ngôn ngữ cùng lúc sẽ hiệu quả hơn.

### 3. Cập nhật bản dịch (Xóa bản dịch cũ)

Để cập nhật các bản dịch hiện có (tức là xóa các bản dịch hiện tại và thay thế bằng bản dịch mới), hãy dùng tùy chọn `-u`. Tùy chọn này sẽ xóa tất cả các bản dịch hiện có cho các ngôn ngữ được chỉ định và dịch lại từ đầu.

```bash
translate -l "ko" -u
```

Cảnh báo: Lệnh này sẽ yêu cầu bạn xác nhận trước khi tiến hành xóa các bản dịch hiện có.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi đã dùng phương pháp sau để cập nhật tất cả các file đã dịch sang tiếng Tây Ban Nha. Tôi khuyên bạn nên dùng cách này khi có nhiều thay đổi lớn trong nội dung gốc trên nhiều tài liệu markdown. Nếu chỉ có một vài file markdown đã dịch cần cập nhật, bạn nên xóa thủ công các file đó rồi dùng phương pháp `-a` để thêm bản dịch mới.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Chỉ dịch hình ảnh

Để chỉ dịch các file hình ảnh trong dự án, hãy dùng tùy chọn `-img`:

```bash
translate -l "ko" -img
```

Lệnh này sẽ chỉ dịch các hình ảnh sang tiếng Hàn mà không ảnh hưởng đến các file markdown.

### 6. Chỉ dịch file Markdown

Để chỉ dịch các file markdown trong dự án, hãy dùng tùy chọn `-md`:

```bash
translate -l "ko" -md
```

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi đã dùng phương pháp sau để kiểm tra lỗi dịch trong các file tiếng Hàn và tự động thử lại dịch cho các file phát hiện có vấn đề.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Tùy chọn này sẽ kiểm tra lỗi dịch. Hiện tại, nếu số dòng xuống giữa file gốc và file dịch khác nhau quá 6 dòng, file đó sẽ bị đánh dấu là có lỗi dịch. Tôi dự định sẽ cải thiện tiêu chí này để linh hoạt hơn trong tương lai.

Ví dụ, phương pháp này hữu ích để phát hiện các đoạn bị thiếu hoặc bản dịch bị lỗi, và sẽ tự động thử lại dịch cho các file đó.

Tuy nhiên, nếu bạn đã biết file nào có vấn đề, cách hiệu quả hơn là xóa thủ công các file đó rồi dùng tùy chọn `-a` để dịch lại.

### 8. Chế độ debug

Để bật ghi log chi tiết phục vụ việc kiểm tra lỗi, hãy dùng tùy chọn `-d`:

```bash
translate -l "ko" -d
```

Lệnh này sẽ chạy dịch ở chế độ debug, cung cấp thêm thông tin log giúp bạn xác định vấn đề trong quá trình dịch.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi gặp vấn đề khi dịch các file markdown có nhiều liên kết, dẫn đến lỗi định dạng như bản dịch bị hỏng và mất dòng xuống. Để kiểm tra nguyên nhân, tôi đã dùng tùy chọn `-d` để xem quá trình dịch hoạt động như thế nào.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Dịch tất cả ngôn ngữ

Nếu bạn muốn dịch dự án sang tất cả các ngôn ngữ hỗ trợ, hãy dùng từ khóa all.

> [!WARNING]
> Dịch tất cả ngôn ngữ cùng lúc có thể mất rất nhiều thời gian tùy vào kích thước dự án. Ví dụ, dịch **Phi-3 CookBook** sang tiếng Tây Ban Nha mất khoảng 2 tiếng. Với quy mô lớn, không thực tế để một người xử lý 20 ngôn ngữ. Nên chia nhỏ công việc cho nhiều người đóng góp, mỗi người quản lý một hoặc hai ngôn ngữ, và cập nhật bản dịch dần dần.

```bash
translate -l "all"
```

Lệnh này sẽ dịch dự án sang tất cả các ngôn ngữ có sẵn. Nếu bạn tiếp tục, quá trình dịch có thể mất nhiều thời gian tùy vào kích thước dự án.

> [!TIP]
>
> ### Xóa thủ công các file đã dịch (Tùy chọn)
> Các file đã dịch hiện được tự động phát hiện và dọn dẹp khi file nguồn được cập nhật.
>
> Tuy nhiên, nếu bạn muốn cập nhật bản dịch thủ công - ví dụ, để dịch lại một file cụ thể hoặc ghi đè hành vi hệ thống - bạn có thể dùng lệnh sau để xóa tất cả phiên bản của file đó trong các thư mục ngôn ngữ.
>
> ### Trên Windows:
> 1. **Dùng Command Prompt**:
>    - Mở Command Prompt.
>    - Di chuyển đến thư mục chứa file bằng lệnh `cd`.
>    - Dùng lệnh sau để xóa file:
>      ```
>      del /s *filename*
>      ```
>      Thay `filename` bằng phần tên file bạn muốn tìm. Tùy chọn `/s` sẽ tìm trong các thư mục con.
>
> 2. **Dùng PowerShell**:
>    - Mở PowerShell.
>    - Chạy lệnh này:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Thay `"C:\YourPath"` bằng đường dẫn thư mục và `filename` bằng tên cụ thể.
>
> ### Trên macOS/Linux:
> 1. **Dùng Terminal**:
>   - Mở Terminal.
>   - Di chuyển đến thư mục bằng `cd`.
>   - Dùng lệnh `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Thay `filename` bằng tên cụ thể.
>
> Luôn kiểm tra kỹ file trước khi xóa để tránh mất dữ liệu ngoài ý muốn. 
>
> Sau khi xóa các file cần thay thế, chỉ cần chạy lại lệnh `translate -l` để cập nhật các thay đổi mới nhất cho file.

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được xem là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.