<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:34:26+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "vi"
}
-->
# Đóng góp cho Co-op Translator

Dự án này hoan nghênh mọi đóng góp và ý kiến. Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận Cấp phép Người đóng góp (CLA), xác nhận rằng bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Để biết chi tiết, hãy truy cập https://cla.opensource.microsoft.com.

Khi bạn gửi một pull request, một bot CLA sẽ tự động xác định xem bạn có cần cung cấp CLA hay không và sẽ đánh dấu PR phù hợp (ví dụ: kiểm tra trạng thái, bình luận). Chỉ cần làm theo hướng dẫn của bot. Bạn chỉ cần thực hiện việc này một lần cho tất cả các kho sử dụng CLA của chúng tôi.

## Thiết lập môi trường phát triển

Để thiết lập môi trường phát triển cho dự án này, chúng tôi khuyến nghị sử dụng Poetry để quản lý các phụ thuộc. Chúng tôi sử dụng `pyproject.toml` để quản lý các phụ thuộc của dự án, do đó, để cài đặt các phụ thuộc, bạn nên dùng Poetry.

### Tạo môi trường ảo

#### Sử dụng pip

```bash
python -m venv .venv
```

#### Sử dụng Poetry

```bash
poetry init
```

### Kích hoạt môi trường ảo

#### Dành cho cả pip và Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Sử dụng Poetry

```bash
poetry shell
```

### Cài đặt gói và các gói cần thiết

#### Sử dụng Poetry (từ pyproject.toml)

```bash
poetry install
```

### Kiểm thử thủ công

Trước khi gửi PR, bạn nên kiểm tra chức năng dịch với tài liệu thực tế:

1. Tạo một thư mục kiểm thử ở thư mục gốc:
    ```bash
    mkdir test_docs
    ```

2. Sao chép một số tài liệu markdown và hình ảnh bạn muốn dịch vào thư mục kiểm thử. Ví dụ:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Cài đặt gói cục bộ:
    ```bash
    pip install -e .
    ```

4. Chạy Co-op Translator trên các tài liệu kiểm thử của bạn:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Kiểm tra các tệp đã dịch trong `test_docs/translations` và `test_docs/translated_images` để xác nhận:
   - Chất lượng bản dịch
   - Các chú thích metadata chính xác
   - Cấu trúc markdown gốc được giữ nguyên
   - Liên kết và hình ảnh hoạt động đúng

Việc kiểm thử thủ công này giúp đảm bảo các thay đổi của bạn hoạt động tốt trong các tình huống thực tế.

### Biến môi trường

1. Tạo tệp `.env` ở thư mục gốc bằng cách sao chép tệp `.env.template` được cung cấp.
1. Điền các biến môi trường theo hướng dẫn.

> [!TIP]
>
> ### Các lựa chọn môi trường phát triển bổ sung
>
> Ngoài việc chạy dự án trên máy cục bộ, bạn cũng có thể sử dụng GitHub Codespaces hoặc VS Code Dev Containers để thiết lập môi trường phát triển thay thế.
>
> #### GitHub Codespaces
>
> Bạn có thể chạy các ví dụ này trực tuyến bằng GitHub Codespaces mà không cần cài đặt hoặc thiết lập thêm.
>
> Nút sau sẽ mở một phiên bản VS Code trên trình duyệt của bạn:
>
> 1. Mở template (có thể mất vài phút):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Chạy cục bộ bằng VS Code Dev Containers
>
> ⚠️ Tùy chọn này chỉ hoạt động nếu Docker Desktop của bạn được cấp ít nhất 16 GB RAM. Nếu bạn có ít hơn 16 GB RAM, hãy thử [tùy chọn GitHub Codespaces](../..) hoặc [thiết lập cục bộ](../..).
>
> Một lựa chọn liên quan là VS Code Dev Containers, sẽ mở dự án trong VS Code cục bộ của bạn bằng [tiện ích mở rộng Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Khởi động Docker Desktop (cài đặt nếu chưa có)
> 2. Mở dự án:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Quy tắc định dạng mã nguồn

Chúng tôi sử dụng [Black](https://github.com/psf/black) làm công cụ định dạng mã Python để duy trì phong cách mã nhất quán trên toàn dự án. Black là một trình định dạng mã tự động, giúp mã Python tuân thủ phong cách của Black.

#### Cấu hình

Cấu hình Black được chỉ định trong `pyproject.toml` của chúng tôi:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Cài đặt Black

Bạn có thể cài đặt Black bằng Poetry (khuyến nghị) hoặc pip:

##### Sử dụng Poetry

Black sẽ được cài đặt tự động khi bạn thiết lập môi trường phát triển:
```bash
poetry install
```

##### Sử dụng pip

Nếu bạn dùng pip, có thể cài đặt Black trực tiếp:
```bash
pip install black
```

#### Sử dụng Black

##### Với Poetry

1. Định dạng tất cả các tệp Python trong dự án:
    ```bash
    poetry run black .
    ```

2. Định dạng một tệp hoặc thư mục cụ thể:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Với pip

1. Định dạng tất cả các tệp Python trong dự án:
    ```bash
    black .
    ```

2. Định dạng một tệp hoặc thư mục cụ thể:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Chúng tôi khuyến nghị bạn thiết lập trình soạn thảo để tự động định dạng mã với Black khi lưu. Hầu hết các trình soạn thảo hiện đại đều hỗ trợ điều này qua tiện ích mở rộng hoặc plugin.

## Chạy Co-op Translator

Để chạy Co-op Translator bằng Poetry trong môi trường của bạn, hãy làm theo các bước sau:

1. Di chuyển đến thư mục nơi bạn muốn kiểm thử dịch hoặc tạo một thư mục tạm để kiểm thử.

2. Thực thi lệnh sau. Thay `-l ko` bằng mã ngôn ngữ bạn muốn dịch sang. Tham số `-d` dùng để bật chế độ debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Đảm bảo môi trường Poetry của bạn đã được kích hoạt (poetry shell) trước khi chạy lệnh.

## Đóng góp ngôn ngữ mới

Chúng tôi hoan nghênh các đóng góp bổ sung hỗ trợ ngôn ngữ mới. Trước khi mở PR, vui lòng hoàn thành các bước dưới đây để quá trình xét duyệt diễn ra suôn sẻ.

1. Thêm ngôn ngữ vào ánh xạ phông chữ
   - Sửa `src/co_op_translator/fonts/font_language_mappings.yml`
   - Thêm một mục với:
     - `code`: Mã ngôn ngữ dạng ISO (ví dụ: `vi`)
     - `name`: Tên hiển thị thân thiện
     - `font`: Một phông chữ có trong `src/co_op_translator/fonts/` hỗ trợ bộ ký tự đó
     - `rtl`: `true` nếu là ngôn ngữ viết từ phải sang trái, ngược lại là `false`

2. Bổ sung tệp phông chữ cần thiết (nếu có)
   - Nếu cần phông chữ mới, hãy kiểm tra giấy phép có phù hợp để phân phối mã nguồn mở không
   - Thêm tệp phông chữ vào `src/co_op_translator/fonts/`

3. Kiểm tra cục bộ
   - Chạy dịch thử với một mẫu nhỏ (Markdown, hình ảnh, và notebook nếu cần)
   - Kiểm tra kết quả xuất ra có hiển thị đúng không, bao gồm phông chữ và bố cục RTL nếu có

4. Cập nhật tài liệu
   - Đảm bảo ngôn ngữ xuất hiện trong `getting_started/supported-languages.md`
   - Không cần thay đổi `README_languages_template.md`; tệp này được tạo tự động từ danh sách hỗ trợ

5. Mở PR
   - Mô tả ngôn ngữ đã thêm và các lưu ý về phông chữ/giấy phép
   - Đính kèm ảnh chụp màn hình kết quả nếu có thể

Ví dụ mục YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Người duy trì

### Quy tắc đặt tên commit và chiến lược gộp

Để đảm bảo lịch sử commit của dự án rõ ràng và nhất quán, chúng tôi tuân theo một định dạng commit cụ thể **cho commit cuối cùng** khi sử dụng chiến lược **Squash and Merge**.

Khi một pull request (PR) được gộp, các commit riêng lẻ sẽ được gộp thành một commit duy nhất. Commit cuối cùng nên theo định dạng dưới đây để giữ lịch sử sạch sẽ và nhất quán.

#### Định dạng commit (cho squash and merge)

Chúng tôi sử dụng định dạng sau cho commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Chỉ loại commit. Chúng tôi sử dụng các loại sau:
  - `Docs`: Cập nhật tài liệu.
  - `Build`: Thay đổi liên quan đến hệ thống build hoặc phụ thuộc, bao gồm cập nhật tệp cấu hình, CI workflow, hoặc Dockerfile.
  - `Core`: Sửa đổi chức năng cốt lõi của dự án, đặc biệt là các tệp trong thư mục `src/co_op_translator/core`.

- **description**: Tóm tắt ngắn gọn về thay đổi.
- **PR number**: Số của pull request liên quan đến commit.

**Ví dụ**:

- `Docs: Cập nhật hướng dẫn cài đặt cho rõ ràng hơn (#50)`
- `Core: Cải thiện xử lý dịch hình ảnh (#60)`

> [!NOTE]
> Hiện tại, các tiền tố **`Docs`**, **`Core`**, và **`Build`** sẽ được tự động thêm vào tiêu đề PR dựa trên nhãn áp dụng cho mã nguồn đã sửa đổi. Miễn là nhãn đúng được áp dụng, bạn thường không cần cập nhật tiêu đề PR thủ công. Bạn chỉ cần kiểm tra mọi thứ đã đúng và tiền tố đã được tạo phù hợp.

#### Chiến lược gộp

Chúng tôi sử dụng **Squash and Merge** làm chiến lược mặc định cho pull request. Chiến lược này đảm bảo commit cuối cùng tuân theo định dạng của chúng tôi, ngay cả khi các commit riêng lẻ không đúng.

**Lý do**:

- Lịch sử dự án sạch, tuyến tính.
- Nhất quán trong thông điệp commit.
- Giảm nhiễu từ các commit nhỏ (ví dụ: "fix typo").

Khi gộp, hãy đảm bảo commit cuối cùng tuân theo định dạng commit đã mô tả ở trên.

**Ví dụ về Squash and Merge**
Nếu một PR có các commit sau:

- `fix typo`
- `update README`
- `adjust formatting`

Chúng sẽ được gộp thành:
`Docs: Cải thiện độ rõ ràng và định dạng tài liệu (#65)`

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.