<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:16:24+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "vi"
}
-->
# Thiết lập Azure OpenAI cho dịch ngôn ngữ

## Tạo một tài nguyên Azure OpenAI trong Azure AI Foundry

Để thiết lập Azure OpenAI trong Azure AI Foundry, làm theo các bước sau:

### Tạo một Hub

1. Đăng nhập vào [cổng Azure AI Foundry](https://ai.azure.com): Đảm bảo bạn đã đăng nhập bằng tài khoản Azure của mình.

2. Điều hướng đến Trung tâm Quản lý: Từ trang chủ, chọn "Management Center" trong menu bên trái.

3. Tạo Hub Mới: Nhấp vào "+ New hub" và nhập các thông tin cần thiết như Subscription, Resource Group và Hub Name, chúng tôi khuyến nghị triển khai hub tại East US vì khu vực này hỗ trợ Cognitive vision và các mô hình GPT.

4. Xem lại và Tạo: Xem lại thông tin và nhấp "Create" để thiết lập hub của bạn.

### Tạo một Dự án

1. Vào Trang Chủ: Nếu bạn chưa ở đó, chọn "Azure AI Foundry" ở góc trên bên trái của trang để về trang chủ.

2. Tạo Dự án: Nhấp vào "+ Create project" và nhập tên cho dự án của bạn.

3. Chọn một Hub: Nếu bạn có nhiều hub, chọn hub bạn muốn sử dụng. Nếu muốn tạo hub mới, bạn có thể làm điều đó trong bước này.

4. Cấu hình Dự án: Làm theo hướng dẫn để cấu hình dự án theo nhu cầu của bạn.

5. Tạo Dự án: Nhấp "Create" để hoàn tất thiết lập.

### Triển khai Mô hình và Endpoint cho mô hình OpenAI

1. Đăng nhập vào [cổng Azure AI Foundry](https://ai.azure.com): Đảm bảo bạn đã đăng nhập với subscription Azure có tài nguyên Azure OpenAI Service.

2. Điều hướng đến Models and Endpoints: Từ trang chủ Azure AI Foundry, tìm ô có nội dung " và chọn "Let's go." hoặc Model and Endpoints trong menu bên trái.

3. Nếu bạn chưa có mô hình GPT nào được triển khai, chọn deploy model: chọn một mô hình GPT, chúng tôi khuyên dùng GPT-4o, GPT-4o-mini hoặc o3-mini.

4. Truy cập tài nguyên của bạn: Bạn sẽ thấy các tài nguyên Azure OpenAI Service hiện có. Nếu có nhiều tài nguyên, sử dụng bộ chọn để chọn tài nguyên bạn muốn làm việc cùng.

Để biết hướng dẫn chi tiết hơn, bạn có thể tham khảo tài liệu chính thức của Azure AI Foundry.

[How to Create a project](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[How to Create resources](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[How to use OpenAI Model in AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[OpenAI Services in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn chính thức. Đối với thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.