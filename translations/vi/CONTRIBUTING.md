<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T11:43:40+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "vi"
}
-->
# Đóng góp cho Co-op Translator

Dự án này hoan nghênh các đóng góp và đề xuất. Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận Cấp phép Đóng góp (CLA) xác nhận rằng bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Chi tiết xem tại https://cla.opensource.microsoft.com.

Khi bạn gửi pull request, một bot CLA sẽ tự động xác định xem bạn có cần cung cấp CLA hay không và đánh dấu PR phù hợp (ví dụ: kiểm tra trạng thái, bình luận). Chỉ cần làm theo hướng dẫn của bot. Bạn chỉ cần làm điều này một lần cho tất cả các repo sử dụng CLA của chúng tôi.

## Thiết lập môi trường phát triển

Để thiết lập môi trường phát triển cho dự án này, chúng tôi khuyên bạn nên sử dụng Poetry để quản lý các phụ thuộc. Chúng tôi sử dụng `pyproject.toml` để quản lý phụ thuộc dự án, do đó, để cài đặt phụ thuộc, bạn nên dùng Poetry.

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

#### Dùng cho cả pip và Poetry

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

Trước khi gửi PR, bạn nên kiểm thử chức năng dịch với tài liệu thực tế:

1. Tạo thư mục test trong thư mục gốc:
    ```bash
    mkdir test_docs
    ```

2. Sao chép một số tài liệu markdown và hình ảnh bạn muốn dịch vào thư mục test. Ví dụ:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Cài đặt gói cục bộ:
    ```bash
    pip install -e .
    ```

4. Chạy Co-op Translator trên tài liệu test của bạn:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Kiểm tra các file dịch trong `test_docs/translations` và `test_docs/translated_images` để xác nhận:
   - Chất lượng bản dịch
   - Các bình luận metadata chính xác
   - Cấu trúc markdown gốc được giữ nguyên
   - Các liên kết và hình ảnh hoạt động đúng

Việc kiểm thử thủ công này giúp đảm bảo các thay đổi của bạn hoạt động tốt trong các tình huống thực tế.

### Biến môi trường

1. Tạo file `.env` trong thư mục gốc bằng cách sao chép file `.env.template` có sẵn.
1. Điền các biến môi trường theo hướng dẫn.

> [!TIP]
>
> ### Các lựa chọn môi trường phát triển bổ sung
>
> Ngoài việc chạy dự án cục bộ, bạn cũng có thể sử dụng GitHub Codespaces hoặc VS Code Dev Containers để thiết lập môi trường phát triển thay thế.
>
> #### GitHub Codespaces
>
> Bạn có thể chạy các mẫu này ảo bằng GitHub Codespaces mà không cần cài đặt hay cấu hình thêm.
>
> Nút bấm sẽ mở một phiên bản VS Code trên trình duyệt của bạn:
>
> 1. Mở mẫu (có thể mất vài phút):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Chạy cục bộ bằng VS Code Dev Containers
>
> ⚠️ Tùy chọn này chỉ hoạt động nếu Docker Desktop của bạn được cấp ít nhất 16 GB RAM. Nếu bạn có dưới 16 GB RAM, bạn có thể thử [GitHub Codespaces](../..) hoặc [thiết lập cục bộ](../..).
>
> Một lựa chọn liên quan là VS Code Dev Containers, sẽ mở dự án trong VS Code cục bộ của bạn bằng [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Khởi động Docker Desktop (cài đặt nếu chưa có)
> 2. Mở dự án:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Kiểu mã nguồn

Chúng tôi sử dụng [Black](https://github.com/psf/black) làm trình định dạng mã Python để duy trì phong cách mã nhất quán trong dự án. Black là trình định dạng mã không khoan nhượng, tự động định dạng lại mã Python theo phong cách của Black.

#### Cấu hình

Cấu hình Black được chỉ định trong `pyproject.toml` của chúng tôi:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Cài đặt Black

Bạn có thể cài Black bằng Poetry (khuyến nghị) hoặc pip:

##### Sử dụng Poetry

Black được cài tự động khi bạn thiết lập môi trường phát triển:
```bash
poetry install
```

##### Sử dụng pip

Nếu dùng pip, bạn có thể cài Black trực tiếp:
```bash
pip install black
```

#### Sử dụng Black

##### Với Poetry

1. Định dạng tất cả file Python trong dự án:
    ```bash
    poetry run black .
    ```

2. Định dạng một file hoặc thư mục cụ thể:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Với pip

1. Định dạng tất cả file Python trong dự án:
    ```bash
    black .
    ```

2. Định dạng một file hoặc thư mục cụ thể:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Chúng tôi khuyên bạn nên thiết lập trình soạn thảo tự động định dạng mã với Black khi lưu file. Hầu hết trình soạn thảo hiện đại hỗ trợ điều này qua các tiện ích mở rộng hoặc plugin.

## Chạy Co-op Translator

Để chạy Co-op Translator bằng Poetry trong môi trường của bạn, làm theo các bước sau:

1. Điều hướng đến thư mục bạn muốn thực hiện kiểm thử dịch hoặc tạo thư mục tạm để thử nghiệm.

2. Thực thi lệnh sau. Thay `-l ko` bằng mã ngôn ngữ bạn muốn dịch sang. Cờ `-d` chỉ chế độ gỡ lỗi.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Đảm bảo môi trường Poetry của bạn đã được kích hoạt (poetry shell) trước khi chạy lệnh.

## Đóng góp ngôn ngữ mới

Chúng tôi hoan nghênh các đóng góp thêm hỗ trợ ngôn ngữ mới. Trước khi mở PR, vui lòng hoàn thành các bước dưới đây để đảm bảo quá trình xem xét suôn sẻ.

1. Thêm ngôn ngữ vào ánh xạ font
   - Chỉnh sửa `src/co_op_translator/fonts/font_language_mappings.yml`
   - Thêm mục với:
     - `code`: mã ngôn ngữ kiểu ISO (ví dụ: `vi`)
     - `name`: tên hiển thị thân thiện
     - `font`: font được cung cấp trong `src/co_op_translator/fonts/` hỗ trợ bộ chữ
     - `rtl`: `true` nếu viết từ phải sang trái, ngược lại `false`

2. Bao gồm các file font cần thiết (nếu có)
   - Nếu cần font mới, kiểm tra tính tương thích giấy phép để phân phối mã nguồn mở
   - Thêm file font vào `src/co_op_translator/fonts/`

3. Kiểm tra cục bộ
   - Chạy dịch cho một mẫu nhỏ (Markdown, hình ảnh, notebook tùy trường hợp)
   - Xác nhận kết quả hiển thị đúng, bao gồm font và bố cục RTL nếu có

4. Cập nhật tài liệu
   - Đảm bảo ngôn ngữ xuất hiện trong `getting_started/supported-languages.md`
   - Không cần thay đổi `getting_started/README_languages_template.md`; nó được tạo tự động từ danh sách hỗ trợ

5. Mở PR
   - Mô tả ngôn ngữ thêm và các lưu ý về font/giấy phép
   - Đính kèm ảnh chụp màn hình kết quả nếu có thể

Ví dụ mục YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Kiểm thử ngôn ngữ mới

Bạn có thể kiểm thử ngôn ngữ mới bằng cách chạy lệnh sau:

```bash
# Tạo và kích hoạt môi trường ảo
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Cài đặt gói phát triển
pip install -e .
# Chạy bản dịch
translate -l "new_lang"
```

## Người duy trì

### Tin nhắn commit và chiến lược Merge

Để đảm bảo sự nhất quán và rõ ràng trong lịch sử commit của dự án, chúng tôi tuân theo định dạng tin nhắn commit cụ thể **cho tin nhắn commit cuối cùng** khi sử dụng chiến lược **Squash and Merge**.

Khi một pull request (PR) được merge, các commit riêng lẻ sẽ được gộp thành một commit duy nhất. Tin nhắn commit cuối cùng nên theo định dạng dưới đây để giữ lịch sử sạch và nhất quán.

#### Định dạng tin nhắn commit (cho squash and merge)

Chúng tôi sử dụng định dạng sau cho tin nhắn commit:

```bash
<type>: <description> (#<Số PR>)
```

- **type**: Chỉ loại commit. Các loại dùng gồm:
  - `Docs`: Cập nhật tài liệu.
  - `Build`: Thay đổi liên quan đến hệ thống build hoặc phụ thuộc, bao gồm cập nhật file cấu hình, workflow CI, hoặc Dockerfile.
  - `Core`: Thay đổi chức năng hoặc tính năng cốt lõi của dự án, đặc biệt các file trong thư mục `src/co_op_translator/core`.

- **description**: Tóm tắt ngắn gọn về thay đổi.
- **PR number**: Số pull request liên quan đến commit.

**Ví dụ**:

- `Docs: Cập nhật hướng dẫn cài đặt cho rõ ràng hơn (#50)`
- `Core: Cải thiện xử lý dịch hình ảnh (#60)`

> [!NOTE]
> Hiện tại, các tiền tố **`Docs`**, **`Core`**, và **`Build`** được tự động thêm vào tiêu đề PR dựa trên nhãn áp dụng cho mã nguồn đã sửa đổi. Miễn là nhãn đúng được áp dụng, bạn thường không cần chỉnh sửa tiêu đề PR thủ công. Bạn chỉ cần kiểm tra mọi thứ đúng và tiền tố đã được tạo phù hợp.

#### Chiến lược Merge

Chúng tôi sử dụng **Squash and Merge** làm chiến lược mặc định cho pull request. Chiến lược này đảm bảo tin nhắn commit tuân theo định dạng của chúng tôi, ngay cả khi các commit riêng lẻ không làm vậy.

**Lý do**:

- Lịch sử dự án sạch, tuyến tính.
- Nhất quán trong tin nhắn commit.
- Giảm tiếng ồn từ các commit nhỏ (ví dụ: "fix typo").

Khi merge, đảm bảo tin nhắn commit cuối cùng theo định dạng đã mô tả ở trên.

**Ví dụ Squash and Merge**
Nếu PR có các commit sau:

- `fix typo`
- `update README`
- `adjust formatting`

Chúng sẽ được gộp thành:
`Docs: Cải thiện rõ ràng và định dạng tài liệu (#65)`

### Quy trình phát hành

Phần này mô tả cách đơn giản nhất để người duy trì phát hành phiên bản mới của Co-op Translator.

#### 1. Tăng phiên bản trong `pyproject.toml`

1. Quyết định số phiên bản tiếp theo (chúng tôi theo semantic versioning: `MAJOR.MINOR.PATCH`).
2. Chỉnh sửa `pyproject.toml` và cập nhật trường `version` trong `[tool.poetry]`.
3. Mở pull request riêng chỉ thay đổi phiên bản (và các file khóa/metadata tự động cập nhật nếu có).
4. Sau khi xem xét, dùng **Squash and Merge** và đảm bảo tin nhắn commit cuối cùng theo định dạng đã mô tả.

#### 2. Tạo GitHub Release

1. Vào trang repo trên GitHub, mở **Releases** → **Draft a new release**.
2. Tạo tag mới (ví dụ, `v0.13.0`) từ nhánh `main`.
3. Đặt tiêu đề release trùng với phiên bản (ví dụ, `v0.13.0`).
4. Nhấn **Generate release notes** để tự động điền changelog.
5. Có thể chỉnh sửa nội dung (ví dụ, để nhấn mạnh ngôn ngữ mới hỗ trợ hoặc thay đổi quan trọng).
6. Xuất bản release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->