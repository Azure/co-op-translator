<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:36:05+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "vi"
}
-->
# Cài đặt gói Co-op translator

**Co-op Translator** là một công cụ dòng lệnh (CLI) được thiết kế để giúp bạn dịch tất cả các file markdown và hình ảnh trong dự án của mình sang nhiều ngôn ngữ khác nhau. Hướng dẫn này sẽ chỉ bạn cách cấu hình trình dịch và chạy nó cho các trường hợp sử dụng khác nhau.

### Tạo môi trường ảo

Bạn có thể tạo môi trường ảo bằng cách sử dụng `pip` hoặc `Poetry`. Nhập một trong các lệnh sau trong terminal của bạn.

#### Sử dụng pip

```bash
python -m venv .venv
```

#### Sử dụng Poetry

```bash
poetry init
```

### Kích hoạt môi trường ảo

Sau khi tạo môi trường ảo, bạn cần kích hoạt nó. Các bước sẽ khác nhau tùy theo hệ điều hành của bạn. Nhập lệnh sau trong terminal.

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

1. Nếu bạn tạo môi trường bằng Poetry, nhập lệnh sau trong terminal để kích hoạt.

    ```bash
    poetry shell
    ```

### Cài đặt gói và các gói cần thiết

Khi môi trường ảo đã được thiết lập và kích hoạt, bước tiếp theo là cài đặt các phụ thuộc cần thiết.

### Cài đặt nhanh

Cài đặt Co-Op Translator qua pip

```
pip install co-op-translator
```  
Hoặc  

Cài đặt qua poetry  
```
poetry add co-op-translator
```

#### Sử dụng pip (từ requirements.txt) nếu bạn clone repo này

![NOTE] Vui lòng KHÔNG làm điều này nếu bạn cài đặt co-op translator qua cài đặt nhanh.

1. Nếu bạn dùng pip, nhập lệnh sau trong terminal. Lệnh sẽ tự động cài đặt các gói cần thiết được chỉ định trong file `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Sử dụng Poetry (từ pyproject.toml)

1. Nếu bạn dùng Poetry, nhập lệnh sau trong terminal. Lệnh sẽ tự động cài đặt các gói cần thiết được chỉ định trong file `pyproject.toml`:

    ```bash
    poetry install
    ```

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được xem là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.