<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:38:52+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "vi"
}
-->
# Góp phần vào Co-op Translator

Dự án này hoan nghênh các đóng góp và đề xuất. Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận Giấy phép Người đóng góp (CLA), xác nhận rằng bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Chi tiết xem tại https://cla.opensource.microsoft.com.

Khi bạn gửi pull request, bot CLA sẽ tự động xác định xem bạn có cần cung cấp CLA hay không và đánh dấu PR phù hợp (ví dụ: kiểm tra trạng thái, bình luận). Chỉ cần làm theo hướng dẫn do bot cung cấp. Bạn chỉ cần thực hiện điều này một lần cho tất cả các kho sử dụng CLA của chúng tôi.

## Thiết lập môi trường phát triển

Để thiết lập môi trường phát triển cho dự án này, chúng tôi khuyên bạn nên sử dụng Poetry để quản lý các phụ thuộc. Chúng tôi sử dụng `pyproject.toml` để quản lý phụ thuộc dự án, do đó, để cài đặt các phụ thuộc, bạn nên dùng Poetry.

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

### Cài đặt Package và các Package cần thiết

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

3. Cài đặt package cục bộ:
    ```bash
    pip install -e .
    ```

4. Chạy Co-op Translator trên các tài liệu test của bạn:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Kiểm tra các file đã dịch trong `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Điền các biến môi trường theo hướng dẫn.

> [!TIP]
>
> ### Các tùy chọn môi trường phát triển bổ sung
>
> Ngoài việc chạy dự án cục bộ, bạn cũng có thể sử dụng GitHub Codespaces hoặc VS Code Dev Containers để thiết lập môi trường phát triển thay thế.
>
> #### GitHub Codespaces
>
> Bạn có thể chạy mẫu này gần như trực tiếp bằng GitHub Codespaces mà không cần thiết lập hay cấu hình thêm.
>
> Nút bấm sẽ mở một phiên bản VS Code trên trình duyệt của bạn:
>
> 1. Mở mẫu (có thể mất vài phút):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Chạy cục bộ với VS Code Dev Containers
>
> ⚠️ Tùy chọn này chỉ hoạt động nếu Docker Desktop của bạn được cấp ít nhất 16 GB RAM. Nếu máy bạn có ít hơn 16 GB RAM, bạn có thể thử [GitHub Codespaces](../..) hoặc [thiết lập cục bộ](../..).
>
> Một tùy chọn liên quan là VS Code Dev Containers, sẽ mở dự án trong VS Code cục bộ của bạn bằng [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Khởi động Docker Desktop (cài nếu chưa có)
> 2. Mở dự án:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Quy tắc Code Style

Chúng tôi sử dụng [Black](https://github.com/psf/black) làm trình định dạng code Python để duy trì phong cách code nhất quán trong dự án. Black là trình định dạng code không khoan nhượng, tự động định dạng lại code Python theo chuẩn phong cách Black.

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

##### Dùng Poetry

Black sẽ được cài tự động khi bạn thiết lập môi trường phát triển:
```bash
poetry install
```

##### Dùng pip

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

2. Định dạng file hoặc thư mục cụ thể:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Với pip

1. Định dạng tất cả file Python trong dự án:
    ```bash
    black .
    ```

2. Định dạng file hoặc thư mục cụ thể:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Chúng tôi khuyên bạn thiết lập trình soạn thảo tự động định dạng code với Black khi lưu. Hầu hết các trình soạn thảo hiện đại đều hỗ trợ qua extension hoặc plugin.

## Chạy Co-op Translator

Để chạy Co-op Translator bằng Poetry trong môi trường của bạn, làm theo các bước sau:

1. Điều hướng đến thư mục nơi bạn muốn thử nghiệm dịch hoặc tạo thư mục tạm để thử nghiệm.

2. Thực thi lệnh sau. Tham số `-l ko` with the language code you wish to translate into. The `-d` chỉ chế độ gỡ lỗi.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Đảm bảo môi trường Poetry đã được kích hoạt (poetry shell) trước khi chạy lệnh.

## Người duy trì

### Tin nhắn commit và chiến lược Merge

Để đảm bảo sự nhất quán và rõ ràng trong lịch sử commit của dự án, chúng tôi tuân theo định dạng tin nhắn commit cụ thể **cho tin nhắn commit cuối cùng** khi sử dụng chiến lược **Squash and Merge**.

Khi một pull request (PR) được merge, các commit riêng lẻ sẽ được gộp thành một commit duy nhất. Tin nhắn commit cuối cùng cần theo định dạng dưới đây để giữ lịch sử sạch và nhất quán.

#### Định dạng tin nhắn commit (cho squash and merge)

Chúng tôi sử dụng định dạng sau cho tin nhắn commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Chỉ loại commit. Các loại được sử dụng gồm:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Cập nhật hướng dẫn cài đặt cho rõ ràng (#50)`
- `Core: Cải thiện xử lý dịch ảnh (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `sửa lỗi chính tả`
- `cập nhật README`
- `điều chỉnh định dạng`

They should be squashed into:
`Docs: Cải thiện sự rõ ràng và định dạng tài liệu (#65)`

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.