<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "220341925e9a67a0e467d1ba94d3cf7d",
  "translation_date": "2025-05-07T14:20:27+00:00",
  "source_file": "getting_started/set-up-azure-ai.md",
  "language_code": "vi"
}
-->
# Thiết lập Azure AI cho Co-op Translator (Azure OpenAI & Azure AI Vision)

Hướng dẫn này sẽ giúp bạn thiết lập Azure OpenAI để dịch ngôn ngữ và Azure Computer Vision để phân tích nội dung hình ảnh (sau đó có thể dùng cho dịch dựa trên hình ảnh) trong Azure AI Foundry.

**Yêu cầu trước:**
- Một tài khoản Azure với đăng ký đang hoạt động.
- Quyền đủ để tạo tài nguyên và triển khai trong đăng ký Azure của bạn.

## Tạo dự án Azure AI

Bạn sẽ bắt đầu bằng cách tạo một dự án Azure AI, nơi trung tâm để quản lý các tài nguyên AI của bạn.

1. Truy cập [https://ai.azure.com](https://ai.azure.com) và đăng nhập bằng tài khoản Azure của bạn.

1. Chọn **+Create** để tạo dự án mới.

1. Thực hiện các bước sau:
   - Nhập **Tên dự án** (ví dụ: `CoopTranslator-Project`).
   - Chọn **AI hub** (ví dụ: `CoopTranslator-Hub`) (Tạo mới nếu cần).

1. Nhấn "**Review and Create**" để thiết lập dự án. Bạn sẽ được chuyển đến trang tổng quan của dự án.

## Thiết lập Azure OpenAI cho Dịch ngôn ngữ

Trong dự án của bạn, bạn sẽ triển khai một mô hình Azure OpenAI làm backend cho việc dịch văn bản.

### Điều hướng đến dự án của bạn

Nếu chưa ở đó, mở dự án mới tạo (ví dụ: `CoopTranslator-Project`) trong Azure AI Foundry.

### Triển khai mô hình OpenAI

1. Trong menu bên trái của dự án, dưới "My assets", chọn "**Models + endpoints**".

1. Chọn **+ Deploy model**.

1. Chọn **Deploy Base Model**.

1. Một danh sách các mô hình có sẵn sẽ hiện ra. Lọc hoặc tìm kiếm mô hình GPT phù hợp. Chúng tôi khuyên dùng `gpt-4o`.

1. Chọn mô hình bạn muốn và nhấn **Confirm**.

1. Chọn **Deploy**.

### Cấu hình Azure OpenAI

Sau khi triển khai, bạn có thể chọn triển khai từ trang "**Models + endpoints**" để xem **REST endpoint URL**, **Key**, **Deployment name**, **Model name** và **API version**. Những thông tin này sẽ cần để tích hợp mô hình dịch vào ứng dụng của bạn.

## Thiết lập Azure Computer Vision cho Dịch hình ảnh

Để dịch văn bản trong hình ảnh, bạn cần lấy API Key và Endpoint của Azure AI Service.

1. Truy cập dự án Azure AI của bạn (ví dụ: `CoopTranslator-Project`). Đảm bảo bạn đang ở trang tổng quan dự án.

### Cấu hình Azure AI Service

Tìm API Key và Endpoint trong Azure AI Service.

1. Truy cập dự án Azure AI của bạn (ví dụ: `CoopTranslator-Project`). Đảm bảo bạn đang ở trang tổng quan dự án.

1. Tìm **API Key** và **Endpoint** trong tab Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Kết nối này cho phép các tính năng của tài nguyên Azure AI Services liên kết (bao gồm phân tích hình ảnh) có thể sử dụng trong dự án AI Foundry của bạn. Bạn có thể dùng kết nối này trong các notebook hoặc ứng dụng để trích xuất văn bản từ hình ảnh, sau đó gửi văn bản đó đến mô hình Azure OpenAI để dịch.

## Tổng hợp thông tin xác thực của bạn

Đến lúc này, bạn nên đã thu thập được các thông tin sau:

**Cho Azure OpenAI (Dịch văn bản):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (ví dụ: `gpt-4o`)
- Azure OpenAI Deployment Name (ví dụ: `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Cho Azure AI Services (Trích xuất văn bản từ hình ảnh qua Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Ví dụ: Cấu hình biến môi trường (Phiên bản thử nghiệm)

Sau này, khi xây dựng ứng dụng, bạn có thể cấu hình bằng các thông tin xác thực này. Ví dụ, bạn có thể thiết lập chúng dưới dạng biến môi trường như sau:

```bash
# Azure AI Service Credentials (Required for image translation)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # e.g., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Azure OpenAI Credentials (Required for text translation)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # e.g., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # e.g., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # e.g., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # e.g., 2024-02-01
```

---

### Tài liệu tham khảo thêm

- [How to Create a project in Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [How to Create Azure AI resources](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [How to Deploy OpenAI models in Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.