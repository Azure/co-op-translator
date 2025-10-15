<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:36:01+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "vi"
}
-->
# Cài đặt gói Co-op Translator

**Co-op Translator** là một công cụ dòng lệnh (CLI) giúp bạn dịch tất cả các tệp markdown và hình ảnh trong dự án của mình sang nhiều ngôn ngữ khác nhau. Hướng dẫn này sẽ giúp bạn cấu hình trình dịch và chạy nó cho nhiều trường hợp sử dụng khác nhau.

### Tạo môi trường ảo

Bạn có thể tạo môi trường ảo bằng `pip` hoặc `Poetry`. Nhập một trong các lệnh sau trong terminal của bạn.

#### Sử dụng pip

```bash
python -m venv .venv
```

#### Sử dụng Poetry

```bash
poetry init
```

### Kích hoạt môi trường ảo

Sau khi tạo môi trường ảo, bạn cần kích hoạt nó. Các bước thực hiện sẽ khác nhau tùy vào hệ điều hành bạn đang sử dụng. Nhập lệnh sau trong terminal của bạn.

#### Dùng cho cả pip và Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Sử dụng Poetry

1. Nếu bạn đã tạo môi trường bằng Poetry, hãy nhập lệnh sau trong terminal để kích hoạt nó.

    ```bash
    poetry shell
    ```

### Cài đặt gói và các gói cần thiết

Sau khi thiết lập và kích hoạt môi trường ảo, bước tiếp theo là cài đặt các phụ thuộc cần thiết.

### Cài đặt nhanh

Cài đặt Co-Op Translator bằng pip

```
pip install co-op-translator
```
Hoặc

Cài đặt bằng poetry
```
poetry add co-op-translator
```

#### Sử dụng pip (từ requirements.txt) nếu bạn clone repo này

> [!NOTE]
> Vui lòng KHÔNG làm điều này nếu bạn đã cài đặt co-op translator bằng cách cài đặt nhanh.

1. Nếu bạn sử dụng pip, hãy nhập lệnh sau trong terminal. Lệnh này sẽ tự động cài đặt các gói cần thiết được chỉ định trong tệp `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Sử dụng Poetry (từ pyproject.toml)

1. Nếu bạn sử dụng Poetry, hãy nhập lệnh sau trong terminal. Lệnh này sẽ tự động cài đặt các gói cần thiết được chỉ định trong tệp `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.