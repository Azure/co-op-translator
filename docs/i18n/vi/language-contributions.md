# Đóng góp cải tiến ngôn ngữ

Kiến thức ngôn ngữ của bạn có thể giúp cải thiện Co-op Translator. Bắt đầu bằng một ví dụ, một đề xuất sửa, và một giải thích bằng cách sử dụng [mẫu phản hồi dịch thuật](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Bạn không cần phải viết mã hay trả tiền cho một lần chạy mô hình.

## Từ một báo cáo tới một cải tiến chung

1. Người đóng góp cung cấp một đoạn trích nguồn, bản dịch của nó, và ngữ cảnh.
2. Một người xem xét ngôn ngữ kiểm tra ý nghĩa, độ tự nhiên, và liệu đề xuất có phụ thuộc vào một vùng địa phương cụ thể hoặc một khóa học hay không.
3. Người bảo trì quyết định liệu sửa lỗi nên thuộc về khóa học nguồn, hướng dẫn ngôn ngữ chung, cấu hình thuật ngữ, hay mã dịch thuật.
4. Đối với một quy tắc chung, người bảo trì so sánh kết quả trước và sau khi thay đổi trên ví dụ được báo cáo và các ví dụ không liên quan. Người đóng góp có thể xem xét những kết quả này mà không cần tự chạy công cụ.
5. PR kết quả liên kết báo cáo và ghi nhận những người đã cung cấp ví dụ và đánh giá. Việc triển khai hoặc tái tạo trong các kho lưu trữ tiêu thụ là một bước riêng biệt.

Một báo cáo không tự động thay đổi các prompt hay tái tạo bản dịch khóa học. Các sửa đổi đặc thù cho khóa học nên được giữ liên kết với kho khóa học. Đừng cho rằng một sửa thủ công sẽ tồn tại khi tái dịch sau này; hãy xác nhận hành vi cho quy trình đó.

## Ví dụ hiện có: Liên kết Markdown tiếng Nhật

[Tệp hướng dẫn tiếng Nhật](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) hướng dẫn mô hình dịch văn bản liên kết đồng thời giữ nguyên cú pháp Markdown và đích liên kết. Ví dụ, một liên kết được viết là `[text](URL)` không được biến thành `「text」（URL）`.

Đây là một ví dụ tập trung về quy tắc ngôn ngữ được hỗ trợ bằng minh họa đầu ra đúng và sai. Nó không phải là bằng chứng rằng chỉ riêng các hướng dẫn prompt đảm bảo Markdown đúng.

[Trình tạo prompt Markdown](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) tải `templates/language/<language_code>.md` bằng mã ngôn ngữ viết thường và đã được cắt bớt khoảng trắng. Nếu không có tệp, nó sẽ sử dụng các hướng dẫn chung. Điều này mô tả đường dẫn prompt Markdown; đừng cho rằng mọi hình ảnh hoặc đường dẫn dịch khác đều sử dụng cùng các hướng dẫn.

Các [bài kiểm tra prompt](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) kiểm tra rằng các hướng dẫn bằng tiếng Nhật được bao gồm. Điều đó xác minh việc lắp ráp prompt, không phải chất lượng bản dịch.

## Điều gì nên có trong một quy tắc ngôn ngữ?

Đề xuất một chỉnh sửa hẹp, có thể lặp lại kèm ví dụ nguồn, hành vi mong đợi và một phản ví dụ mà trong đó quy tắc không được áp dụng. Giữ nguyên ý nghĩa, trình giữ chỗ, mã, URL và cấu trúc tài liệu. Tránh biến sở thích phong cách của một người hoặc thuật ngữ của một khóa học thành quy tắc chung.

Phần [triển khai bảng chú giải](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) hiện tại bảo vệ các thuật ngữ khỏi việc dịch. Nó không phải là một từ điển thuật ngữ từ nguồn sang đích. Thảo luận về hành vi thuật ngữ mới trước khi hứa hẹn điều đó với những người đóng góp.

## Ví dụ cộng đồng: báo cáo tên sản phẩm bằng tiếng Nhật

Trong [báo cáo #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 đã xác định một bản dịch tiếng Nhật đã thay đổi tên sản phẩm `Co-op Translator` thành `Co-op 翻訳`. Báo cáo bao gồm một liên kết đến tài liệu bị ảnh hưởng và một ảnh chụp màn hình, giúp dễ dàng tìm ra vấn đề.

Người đóng góp cũng đã liên kết một [PR khóa học liên quan](https://github.com/microsoft/AZD-for-beginners/pull/109). Trong cuộc thảo luận về vấn đề, người duy trì đã xác nhận báo cáo và đề xuất điều tra nguyên nhân tại sao tên bị thay đổi, bao gồm cơ chế bảo vệ thuật ngữ, hành vi của bảng chú giải và đường dẫn dịch.

Điều này cho thấy cách một báo cáo nhỏ có thể hỗ trợ việc điều tra vượt ra ngoài việc sửa một câu chữ riêng lẻ. Đây không phải là kết quả trước/sau đã được xác minh hay bằng chứng rằng các hướng dẫn Markdown liên kết bằng tiếng Nhật ở trên đã sửa lỗi tên sản phẩm này.

Bạn có thể đóng góp theo cách tương tự: chia sẻ văn bản gốc, bản dịch hiện tại, đề xuất chỉnh sửa, và lý do vì sao điều đó quan trọng. Thêm liên kết tài liệu hoặc ảnh chụp màn hình khi cần thiết. Bạn không cần phải chẩn đoán nguyên nhân hay viết một lời nhắc trước khi báo cáo nó.

## Xác minh trước khi áp dụng một quy tắc

Sử dụng cùng các mẫu nguồn, bản sửa đổi của người phiên dịch, nhà cung cấp/mô hình, và các thiết lập sinh cho các lần chạy cơ sở và ứng viên, chỉ thay đổi hướng dẫn được đề xuất. Ghi lại thay đổi lời nhắc thực tế và các đầu ra; lặp lại các ví dụ khi cần thiết để phân biệt một hiệu ứng nhất quán với biến động đầu ra. Bao gồm lỗi được báo cáo, các bối cảnh đối chiếu, và các ví dụ đã dịch đúng.

| Mẫu | Nguồn/ngữ cảnh | Kết quả cơ sở | Kết quả ứng viên | Đánh giá của người xem xét |
| --- | --- | --- | --- | --- |
| Lỗi được báo cáo | Đang thu thập | Chưa chạy | Chưa chạy | Đang chờ |
| Phản ví dụ | Đang thu thập | Chưa chạy | Chưa chạy | Đang chờ |
| Ví dụ không bị ảnh hưởng | Đang thu thập | Chưa chạy | Chưa chạy | Đang chờ |

Kiểm tra các bất biến cấu trúc tách biệt khỏi các đánh giá ngôn ngữ. Một bài kiểm tra tải prompt thành công không phải là một đánh giá chất lượng, và một câu mong đợi chính xác không phải là bản dịch duy nhất hợp lệ. Nếu thiếu ngữ cảnh, chạy mô hình, hoặc đánh giá ngôn ngữ, hãy để đề xuất ở trạng thái chờ thay vì cho rằng vấn đề đã được sửa.