# Thiết lập Azure AI

Sử dụng hướng dẫn này khi bạn muốn cấu hình Azure OpenAI để dịch văn bản và Azure AI Vision để trích xuất văn bản từ hình ảnh.

## Yêu cầu

- Một đăng ký Azure.
- Quyền để tạo hoặc sử dụng tài nguyên Azure AI và triển khai mô hình.
- Một dự án trong Azure AI Foundry hoặc quyền truy cập tương đương tới tài nguyên Azure OpenAI và Azure AI Vision.

## Tạo một dự án Azure AI

1. Mở [Azure AI Foundry](https://ai.azure.com).
2. Tạo hoặc chọn một dự án.
3. Tạo hoặc chọn một AI hub cho dự án.
4. Mở phần tổng quan dự án sau khi tạo.

## Triển khai một mô hình Azure OpenAI

1. Trong dự án, mở **Models + endpoints**.
2. Chọn **Deploy model**.
3. Chọn một mô hình GPT như `gpt-4o`.
4. Triển khai mô hình.
5. Ghi lại endpoint, tên triển khai, tên mô hình, khóa API và phiên bản API.

!!! note
    Phiên bản API Azure OpenAI khác với phiên bản mô hình hiển thị trong Azure AI Foundry. Hãy chọn một phiên bản API được hỗ trợ cho triển khai của bạn.

## Cấu hình Azure AI Vision

Việc dịch hình ảnh sử dụng Azure AI Vision để trích xuất văn bản từ hình ảnh nguồn trước khi văn bản được dịch.

Trong dự án Azure AI của bạn, tìm khóa và endpoint của Azure AI Services.

![Tìm thông tin dịch vụ Azure AI](../../assets/find-azure-ai-info.png)

Ghi lại:

- Endpoint dịch vụ Azure AI
- Khóa API dịch vụ Azure AI

## Biến môi trường

Thêm thông tin xác thực vào tệp `.env` của bạn hoặc bí mật CI.

```bash
# Azure AI Vision, cần thiết cho việc dịch hình ảnh
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, cần thiết cho việc dịch văn bản
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator cũng hỗ trợ các bộ thông tin xác thực dự phòng tùy chọn. Nhân đôi một bộ nhà cung cấp hoàn chỉnh với hậu tố như `_1` hoặc `_2`; tất cả các biến trong một bộ dự phòng phải dùng cùng hậu tố.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## Các bước tiếp theo

- Quay lại [Configuration](configuration.md) để thiết lập biến môi trường cục bộ hoặc CI.
- Sử dụng [CLI Reference](cli.md) cho các lệnh dịch.
- Sử dụng [GitHub Actions](github-actions.md) để tự động hóa pull request dịch.