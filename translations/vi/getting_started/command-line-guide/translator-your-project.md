<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33db54f4f3ca9f0321be05374b591f2b",
  "translation_date": "2025-05-06T18:01:35+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "vi"
}
-->
# Dịch dự án của bạn bằng Co-op Translator

**Co-op Translator** là một công cụ giao diện dòng lệnh (CLI) giúp bạn dịch các file markdown và hình ảnh trong dự án của mình sang nhiều ngôn ngữ khác nhau. Phần này giải thích cách sử dụng công cụ, các tùy chọn CLI khác nhau và cung cấp ví dụ cho các trường hợp sử dụng khác nhau.

> [!NOTE]
> Để xem danh sách đầy đủ các lệnh và mô tả chi tiết, vui lòng tham khảo [Command reference](./command-reference.md).

---

## Các tình huống và lệnh ví dụ

Dưới đây là một số trường hợp sử dụng phổ biến cho **Co-op Translator**, cùng với các lệnh tương ứng để chạy.

### 1. Dịch cơ bản (Một ngôn ngữ)

Để dịch toàn bộ dự án của bạn (file markdown và hình ảnh) sang một ngôn ngữ duy nhất, như tiếng Hàn, hãy sử dụng lệnh sau:

```bash
translate -l "ko"
```

Lệnh này sẽ dịch tất cả file markdown và hình ảnh sang tiếng Hàn, thêm bản dịch mới mà không xóa các bản dịch hiện có.

> [!TIP]
>
> Muốn xem các mã ngôn ngữ được hỗ trợ trong **Co-op Translator**? Hãy truy cập phần [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) trong kho lưu trữ để biết thêm chi tiết.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi đã sử dụng phương pháp sau để thêm bản dịch tiếng Hàn cho các file markdown và hình ảnh hiện có.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Dịch nhiều ngôn ngữ

Để dịch dự án của bạn sang nhiều ngôn ngữ (ví dụ: tiếng Tây Ban Nha, Pháp và Đức), hãy sử dụng lệnh này:

```bash
translate -l "es fr de"
```

Lệnh này sẽ dịch dự án sang tiếng Tây Ban Nha, Pháp và Đức, thêm bản dịch mới mà không ghi đè các bản dịch hiện có.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, sau khi kéo các thay đổi mới nhất để cập nhật các commit gần đây, tôi đã sử dụng phương pháp sau để dịch các file markdown và hình ảnh mới được thêm.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Mặc dù thường khuyên nên dịch từng ngôn ngữ một, trong những trường hợp như thế này khi cần thêm các thay đổi cụ thể, việc dịch nhiều ngôn ngữ cùng lúc có thể hiệu quả hơn.

### 3. Chỉ định thư mục gốc

Mặc định, trình dịch sẽ dùng thư mục làm việc hiện tại. Nếu dự án của bạn nằm ở vị trí khác, hãy chỉ định thư mục gốc với tùy chọn -r:

```bash
translate -l "es fr de" -r "./my_project"
```

Lệnh này dịch các file trong `./my_project` into Spanish, French, and German.

### 4. Updating Translations (Deletes Existing Translations)

To update existing translations (i.e., delete the current translations and replace them with new ones), use the `-u` tùy chọn. Điều này sẽ xóa tất cả các bản dịch hiện có cho các ngôn ngữ được chỉ định và dịch lại.

```bash
translate -l "ko" -u
```

Cảnh báo: Lệnh này sẽ yêu cầu bạn xác nhận trước khi tiến hành xóa các bản dịch hiện có.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi đã sử dụng phương pháp sau để cập nhật tất cả các file đã dịch sang tiếng Tây Ban Nha. Tôi khuyên dùng phương pháp này khi có nhiều thay đổi đáng kể trong nội dung gốc ở nhiều tài liệu markdown. Nếu chỉ có vài file markdown đã dịch cần cập nhật, việc xóa thủ công các file đó rồi dùng phương pháp `-a` để thêm bản dịch mới sẽ hiệu quả hơn.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. Chỉ dịch hình ảnh

Để chỉ dịch các file hình ảnh trong dự án, hãy sử dụng tùy chọn `-img`:

```bash
translate -l "ko" -img
```

Lệnh này sẽ chỉ dịch hình ảnh sang tiếng Hàn, không ảnh hưởng đến các file markdown.

### 7. Chỉ dịch file markdown

Để chỉ dịch các file markdown trong dự án, hãy sử dụng tùy chọn `-md`:

```bash
translate -l "ko" -md
```

### 8. Kiểm tra lỗi trong các file đã dịch

Nếu bạn muốn kiểm tra các file đã dịch có lỗi và thử dịch lại nếu cần, hãy sử dụng tùy chọn `-chk`:

```bash
translate -l "ko" -chk
```

Lệnh này sẽ quét các file markdown đã dịch và thử dịch lại những file bị lỗi.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi đã sử dụng phương pháp sau để kiểm tra lỗi dịch trong các file tiếng Hàn và tự động thử dịch lại các file có vấn đề.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Tùy chọn này kiểm tra lỗi dịch. Hiện tại, nếu sự khác biệt về xuống dòng giữa file gốc và file dịch vượt quá sáu, file đó sẽ bị đánh dấu là có lỗi dịch. Tôi dự định cải tiến tiêu chí này để linh hoạt hơn trong tương lai.

Ví dụ, phương pháp này hữu ích để phát hiện các phần bị thiếu hoặc bản dịch bị lỗi, và nó sẽ tự động thử dịch lại các file đó.

Tuy nhiên, nếu bạn đã biết file nào gặp vấn đề, việc xóa thủ công các file đó rồi dùng tùy chọn `-a` option to re-translate them.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` sẽ hiệu quả hơn:

```bash
translate -l "ko" -d
```

Lệnh này sẽ chạy dịch ở chế độ gỡ lỗi, cung cấp thêm thông tin ghi nhật ký giúp bạn xác định lỗi trong quá trình dịch.

#### Ví dụ trên Phi-3 CookBook

Trong **Phi-3 CookBook**, tôi gặp vấn đề khi các bản dịch có nhiều liên kết trong file markdown gây lỗi định dạng, như bản dịch bị lỗi và bỏ qua xuống dòng. Để chẩn đoán vấn đề này, tôi đã dùng tùy chọn `-d` để xem quá trình dịch hoạt động như thế nào.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. Dịch tất cả ngôn ngữ

Nếu bạn muốn dịch dự án sang tất cả các ngôn ngữ được hỗ trợ, hãy dùng từ khóa all.

> [!WARNING]
> Dịch tất cả ngôn ngữ cùng lúc có thể mất nhiều thời gian tùy thuộc vào quy mô dự án. Ví dụ, dịch **Phi-3 CookBook** sang tiếng Tây Ban Nha mất khoảng 2 giờ. Với quy mô này, không thực tế để một người đảm nhận 20 ngôn ngữ. Khuyến nghị chia công việc cho nhiều người đóng góp, mỗi người quản lý một hoặc hai ngôn ngữ và cập nhật bản dịch dần dần.

```bash
translate -l "all"
```

Lệnh này sẽ dịch dự án sang tất cả các ngôn ngữ có sẵn. Nếu bạn tiếp tục, việc dịch có thể mất khá nhiều thời gian tùy theo kích thước dự án.

> [!TIP]
>
> ### Xóa các file cần được cập nhật  
> Để cập nhật các file vừa thay đổi trong Pull Request, bước đầu tiên là xóa tất cả các phiên bản hiện có của file đó trong các thư mục bản dịch ngôn ngữ khác nhau. Bạn có thể làm điều này hàng loạt bằng cách dùng lệnh sau để xóa tất cả file có tên cụ thể trong các thư mục bản dịch.
>
> ### Trên Windows:
> 1. **Dùng Command Prompt**:
>    - Mở Command Prompt.
>    - Điều hướng đến thư mục chứa file bằng lệnh `cd`.
>    - Dùng lệnh sau để xóa file:
>      ```
>      del /s *filename*
>      ```
>      Tùy chọn `/s` tìm kiếm cả trong các thư mục con.
>
> 2. **Dùng PowerShell**:
>    - Mở PowerShell.
>    - Chạy lệnh này:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Thay thế `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` lệnh:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Thay thế `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` lệnh để cập nhật các thay đổi file gần đây.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn tham khảo chính xác nhất. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.