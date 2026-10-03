# Dịch, chỉnh sửa và xem xét một dự án nhỏ

Bắt đầu với hai tệp Markdown ngắn và một ngôn ngữ đích. Bạn sẽ thấy nơi lưu bản dịch, điều gì xảy ra khi nguồn thay đổi, và cách kiểm tra kết quả.

## Kết quả ghi lại

Ví dụ được chạy vào ngày 19 tháng 9 năm 2026 với Co-op Translator 0.21.0 và Azure OpenAI (`gpt-5-mini`). Các lệnh CLI không chỉnh sửa được gọi thông qua `CliRunner` của Click sử dụng wheel đã build và các phụ thuộc Python hiện có.

| Bước | Kết quả |
| --- | --- |
| Xem trước | Exit 0; không yêu cầu dịch bằng mô hình |
| Dịch ban đầu | Exit 0; 27.36 giây |
| Đánh giá ban đầu | Exit 0 |
| Chỉnh sửa README và đánh giá | Exit 1; phát hiện bản dịch lỗi thời |
| Cập nhật bản dịch | Exit 0; 22.17 giây |
| Đánh giá sau cập nhật | Exit 0; không có lỗi hoặc cảnh báo |
| Hướng dẫn không thay đổi | Các byte giống hệt trước và sau khi cập nhật README |
| Chạy lại | Exit 0; hash giống hệt cho tất cả các tệp dịch |

Đây là các phép đo cho từng lần chạy, không phải cam kết hiệu năng. Thời gian thiết lập không được tính; chi phí của nhà cung cấp không được đo. Một lần chạy không thay đổi vẫn có thể thực hiện kiểm tra tình trạng nhà cung cấp.

Kiểm tra [bản dịch ban đầu](../../assets/demo/before.txt), [bản dịch đã cập nhật](../../assets/demo/after.txt), [diff dịch toàn bộ tệp](../../assets/demo/update.diff), [đánh giá lỗi thời](../../assets/demo/review-stale.txt), [đánh giá cuối cùng](../../assets/demo/review-after.txt), và [chi tiết chạy](../../assets/demo/results.json). Dịch toàn bộ tệp có thể thay đổi cách diễn đạt khác, như diff đã ghi lại cho thấy. Cả hai văn bản giữ lời từ chối trách nhiệm được sinh ra.

Việc xem xét bởi con người vẫn quan trọng: bản cập nhật được ghi lại sử dụng `[사용 가이드](guide.md)을`; hạt từ tiếng Hàn đúng phải là `[사용 가이드](guide.md)를`. Các văn bản giữ nguyên đầu ra này thay vì trình bày một bản dịch đã chỉnh sửa như kết quả của mô hình. Đánh giá về cấu trúc vẫn đạt mặc dù có vấn đề diễn đạt này.

## 1. Chuẩn bị một thư mục nhỏ

Sử dụng Python 3.11–3.14 và [thiết lập môi trường ảo](configuration.md#local-runtime-setup). Cài đặt phiên bản được sử dụng cho ví dụ này:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Tải [README.txt](../../assets/demo/README.txt) và [guide.txt](../../assets/demo/guide.txt) vào thư mục này, lưu chúng dưới tên `README.md` và `guide.md`. Chúng là các tài liệu dự án hư cấu nhỏ; không cần cài đặt ứng dụng.

README bao gồm một khối mã và một liên kết tới `guide.md`. Câu cuối cùng của nó là:

```text
Notes are saved locally.
```

Chỉ giữ hai tài liệu nguồn này trong thư mục. Tất cả các lệnh sau chạy trong `translation-demo` và hoạt động trên Bash và PowerShell.

## 2. Xem trước mà không có thông tin xác thực

```bash
translate -l "ko" -md --dry-run
```

Chế độ xem trước ước tính công việc dịch mà không gọi mô hình hay ghi bản dịch. Ước tính token không phải là báo giá thanh toán. Lần chạy đầu tiên nên nhận diện cả hai tệp Markdown là công việc mới.

## 3. Chọn nhà cung cấp và dịch

Cấu hình một nhà cung cấp theo [hướng dẫn cấu hình](configuration.md): Azure OpenAI, OpenAI hoặc Anthropic. Dịch văn bản bằng OpenAI và Anthropic không yêu cầu tài khoản Azure. Dịch vụ xử lý hình ảnh không cần cho ví dụ này.

Nếu bạn dùng tệp `.env` cục bộ, thêm `.env` vào `.gitignore` của thư mục này. Các cuộc gọi dịch sử dụng tài khoản của bạn tại nhà cung cấp và có thể phát sinh phí.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Mở `translations/ko/README.md` và `translations/ko/guide.md`. Kiểm tra cách diễn đạt tiếng Hàn, khối mã, và liên kết từ README đã dịch đến hướng dẫn đã dịch. Cách diễn đạt đầu ra khác nhau tùy mô hình.

`co-op-review` kiểm tra độ mới, cấu trúc và các liên kết nội bộ. Kết quả đạt không xác nhận độ chính xác ngôn ngữ. Hãy xử lý mọi lỗi được báo trước khi tiếp tục.

Ghi lại baseline thành công bằng Git (cấu hình danh tính Git của bạn trước nếu cần):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Thay đổi nguồn

Trong `README.md`, thay `Notes are saved locally.` bằng:

```text
Notes are saved locally as Markdown files.
```

Để `guide.md` không thay đổi. Sau đó chạy:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Kết quả đánh giá nên báo bản dịch README lỗi thời và thoát không thành công. Đây là trạng thái trung gian mong đợi. Chế độ xem trước nên nhận diện công việc cho README đã thay đổi.

## 5. Cập nhật và kiểm tra diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Kiểm tra diff thực: CLI mặc định dịch lại tệp đã thay đổi, nên mô hình cũng có thể chỉnh sửa các cách diễn đạt khác trong tệp đó. Hướng dẫn không thay đổi không nên có diff. Kết quả đánh giá không nên báo README lỗi thời nữa; hãy điều tra mọi phát hiện khác thay vì bỏ qua chúng.

Bảo toàn ở mức khối của các chỉnh sửa Markdown do con người yêu cầu một nhà cung cấp trạng thái dịch tùy chọn trong [Python API](api.md). Nó không được bật bởi các lệnh CLI này.

## 6. Chạy lại khi không có thay đổi

Ghi commit mã nguồn và bản dịch đã cập nhật:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Với các bản dịch hiện có và cấu hình không đổi, bộ dịch bỏ qua các tệp. Lệnh Git cuối cùng không nên tạo diff và nên thoát thành công.

## Bước tiếp theo

- [Chỉ dịch một README và mở một pull request](github-actions.md#your-first-readme-translation-pr).
- [Chọn CLI, Python API, hoặc MCP](workflows.md).
- [Báo cáo vấn đề bản dịch mà không cần mã hóa](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).