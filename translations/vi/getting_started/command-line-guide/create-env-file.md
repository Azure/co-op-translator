<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-05-07T14:17:05+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "vi"
}
-->
# Tạo file *.env* trong thư mục gốc

Trong hướng dẫn này, chúng tôi sẽ giúp bạn thiết lập biến môi trường cho các dịch vụ Azure bằng cách sử dụng file *.env*. Biến môi trường cho phép bạn quản lý an toàn các thông tin nhạy cảm như khóa API mà không cần phải ghi cứng chúng vào mã nguồn.

> [!IMPORTANT]
> - Chỉ cần cấu hình một dịch vụ mô hình ngôn ngữ (Azure OpenAI hoặc OpenAI). Điền các biến môi trường cho dịch vụ bạn chọn. Nếu có biến môi trường cho nhiều mô hình ngôn ngữ được thiết lập, trình dịch hợp tác sẽ chọn một theo thứ tự ưu tiên.
> - Nếu không thiết lập biến môi trường cho Computer Vision, trình dịch sẽ tự động chuyển sang [chế độ chỉ Markdown](./markdown-only-mode.md).

> [!NOTE]
> Hướng dẫn này chủ yếu tập trung vào các dịch vụ Azure, nhưng bạn có thể chọn bất kỳ mô hình ngôn ngữ nào được hỗ trợ trong [danh sách mô hình và dịch vụ được hỗ trợ](../README.md#-supported-models-and-services).

## Tạo file *.env*

Trong thư mục gốc của dự án, tạo một file có tên *.env*. File này sẽ lưu trữ tất cả biến môi trường của bạn dưới định dạng đơn giản.

> [!WARNING]
> Không được commit file *.env* vào hệ thống quản lý phiên bản như Git. Thêm *.env* vào file .gitignore để tránh commit nhầm.

1. Điều hướng đến thư mục gốc của dự án.

1. Tạo file *.env* trong thư mục gốc của dự án.

1. Mở file *.env* và dán mẫu sau vào:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> Nếu bạn muốn tìm khóa API và endpoint, bạn có thể tham khảo [set-up-azure-ai.md](../set-up-azure-ai.md).

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn thông tin chính thức. Đối với những thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu nhầm hay diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.