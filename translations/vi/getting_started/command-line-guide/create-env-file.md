<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53c99ea0ead7a3500149d4bb96be5811",
  "translation_date": "2025-05-06T17:55:36+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "vi"
}
-->
# Tạo file *.env* trong thư mục gốc

Trong hướng dẫn này, chúng tôi sẽ giúp bạn thiết lập các biến môi trường cho dịch vụ Azure bằng cách sử dụng file *.env*. Biến môi trường cho phép bạn quản lý an toàn các thông tin nhạy cảm như khóa API mà không cần ghi cứng vào mã nguồn.

> [!IMPORTANT]
> - Chỉ cần cấu hình một dịch vụ mô hình ngôn ngữ (Azure OpenAI hoặc OpenAI). Điền các biến môi trường cho dịch vụ bạn chọn. Nếu thiết lập biến môi trường cho nhiều mô hình ngôn ngữ, bộ dịch đồng bộ sẽ chọn một dựa trên thứ tự ưu tiên.
> - Nếu không thiết lập biến môi trường Computer Vision, bộ dịch sẽ tự động chuyển sang [chế độ chỉ Markdown](./markdown-only-mode.md).

> [!NOTE]
> Hướng dẫn này chủ yếu tập trung vào dịch vụ Azure, nhưng bạn có thể chọn bất kỳ mô hình ngôn ngữ nào được hỗ trợ trong [danh sách mô hình và dịch vụ được hỗ trợ](../README.md#-supported-models-and-services).

## Tạo file *.env*

Trong thư mục gốc của dự án, tạo một file có tên *.env*. File này sẽ lưu trữ tất cả biến môi trường của bạn dưới định dạng đơn giản.

> [!WARNING]
> Không commit file *.env* lên hệ thống quản lý phiên bản như Git. Thêm *.env* vào file .gitignore để tránh commit nhầm.

1. Điều hướng đến thư mục gốc của dự án.

1. Tạo file *.env* trong thư mục gốc của dự án.

    ![Tạo file *.env*.](../../../../imgs/create-env.png)

1. Mở file *.env* và dán mẫu sau vào:

    ```plaintext
    # Azure Credentials
    AZURE_SUBSCRIPTION_KEY="your_azure_AIServices_api_key"
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

## Thu thập thông tin xác thực Azure của bạn

Bạn cần chuẩn bị các thông tin xác thực Azure sau để cấu hình biến môi trường:

Bạn có thể lấy tất cả thông tin này từ trang tổng quan dự án trong [AI Foundry](https://ai.azure.com/build/overview)

![Tổng quan Foundry](../../../../imgs/foundry-overview.png)


### Đối với Azure AI Service:

    - Azure Subscription Key: Khóa API Azure AI Services của bạn, dùng để truy cập dịch vụ Azure AI.
    - Azure AI Service Endpoint: URL endpoint cho dịch vụ Azure AI cụ thể của bạn.

### Đối với Azure OpenAI Service:

    - Azure OpenAI API Key: Khóa API để truy cập dịch vụ Azure OpenAI.
    - Azure OpenAI Endpoint: URL endpoint cho dịch vụ Azure OpenAI của bạn.


1. Sao chép và dán khóa AI Services và Endpoint vào file *.env*.
2. Sao chép và dán Azure OpenAI API Key và Endpoint vào file *.env*.

### Thông tin Model

Chọn Model và Endpoints từ menu bên trái

![Các mô hình Foundry](../../../../imgs/gpt-models.png)

Bây giờ bạn cần chọn mô hình muốn sử dụng để lấy thông tin chi tiết về mô hình

![Chi tiết mô hình](../../../../imgs/model-deployment-name.png)

Đối với file .env, chúng ta cần các thông tin sau

    - Azure OpenAI Model Name: Tên mô hình bạn sẽ tương tác.
    - Azure OpenAI Name: Tên triển khai của bạn cho các mô hình Azure OpenAI.
    - Azure OpenAI API Version: Phiên bản API Azure OpenAI bạn đang sử dụng, nằm ở cuối chuỗi URL.

Để lấy những thông tin này, chọn triển khai mô hình

![Thông tin mô hình Foundry](../../../../imgs/foundry-model-info.png)

### Thêm biến môi trường Azure

3. Sao chép và dán Azure OpenAI **Name** và **Version** mô hình vào file *.env*.
4. Lưu file *.env*.
5. Bây giờ, bạn có thể truy cập các biến môi trường này để sử dụng **Co-op Translator** với dịch vụ Azure của bạn.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.