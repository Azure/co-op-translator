<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a52587a512e667f70d92db853d3c61d5",
  "translation_date": "2025-05-07T14:17:28+00:00",
  "source_file": "getting_started/github-actions-guide/github-actions-guide-public.md",
  "language_code": "vi"
}
-->
# Sử dụng Co-op Translator GitHub Action (Cài đặt Công khai)

**Đối tượng hướng tới:** Hướng dẫn này dành cho người dùng trong hầu hết các kho lưu trữ công khai hoặc riêng tư, nơi quyền hạn tiêu chuẩn của GitHub Actions là đủ. Nó sử dụng `GITHUB_TOKEN` tích hợp sẵn.

Tự động hóa việc dịch tài liệu trong kho của bạn một cách dễ dàng bằng Co-op Translator GitHub Action. Hướng dẫn này sẽ giúp bạn thiết lập action để tự động tạo pull request với bản dịch cập nhật mỗi khi các file Markdown nguồn hoặc hình ảnh thay đổi.

> [!IMPORTANT]
>
> **Lựa chọn Hướng dẫn phù hợp:**
>
> Hướng dẫn này trình bày **cách thiết lập đơn giản hơn bằng `GITHUB_TOKEN` tiêu chuẩn**. Đây là phương pháp được khuyến nghị cho hầu hết người dùng vì không cần quản lý các khóa riêng tư GitHub App nhạy cảm.
>

## Yêu cầu trước

Trước khi cấu hình GitHub Action, hãy đảm bảo bạn đã có các thông tin xác thực dịch vụ AI cần thiết.

**1. Bắt buộc: Thông tin xác thực Mô hình Ngôn ngữ AI**  
Bạn cần thông tin xác thực cho ít nhất một Mô hình Ngôn ngữ được hỗ trợ:

- **Azure OpenAI**: Cần Endpoint, API Key, Tên Model/Deployment, Phiên bản API.  
- **OpenAI**: Cần API Key, (Tùy chọn: Org ID, Base URL, Model ID).  
- Xem [Supported Models and Services](../../../../README.md) để biết chi tiết.

**2. Tùy chọn: Thông tin xác thực AI Vision (cho Dịch hình ảnh)**

- Chỉ cần nếu bạn muốn dịch văn bản trong hình ảnh.  
- **Azure AI Vision**: Cần Endpoint và Subscription Key.  
- Nếu không cung cấp, action sẽ mặc định ở [Markdown-only mode](../markdown-only-mode.md).

## Thiết lập và Cấu hình

Làm theo các bước sau để cấu hình Co-op Translator GitHub Action trong kho của bạn bằng `GITHUB_TOKEN` tiêu chuẩn.

### Bước 1: Hiểu về Xác thực (Sử dụng `GITHUB_TOKEN`)

Workflow này sử dụng `GITHUB_TOKEN` tích hợp sẵn do GitHub Actions cung cấp. Token này tự động cấp quyền cho workflow tương tác với kho của bạn dựa trên cài đặt trong **Bước 3**.

### Bước 2: Cấu hình Bí mật kho

Bạn chỉ cần thêm **thông tin xác thực dịch vụ AI** dưới dạng bí mật được mã hóa trong cài đặt kho.

1.  Truy cập kho GitHub mục tiêu của bạn.  
2.  Vào **Settings** > **Secrets and variables** > **Actions**.  
3.  Trong **Repository secrets**, nhấn **New repository secret** cho mỗi bí mật dịch vụ AI cần thiết dưới đây.

    ![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(Tham khảo hình ảnh: Vị trí thêm bí mật)*

**Bí mật Dịch vụ AI Bắt buộc (Thêm TẤT CẢ các bí mật phù hợp theo Yêu cầu trước):**

| Tên Bí mật                         | Mô tả                                   | Nguồn Giá trị                   |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_SUBSCRIPTION_KEY`            | Khóa cho Azure AI Service (Computer Vision)  | Azure AI Foundry của bạn               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint cho Azure AI Service (Computer Vision) | Azure AI Foundry của bạn               |
| `AZURE_OPENAI_API_KEY`              | Khóa cho dịch vụ Azure OpenAI              | Azure AI Foundry của bạn               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint cho dịch vụ Azure OpenAI         | Azure AI Foundry của bạn               |
| `AZURE_OPENAI_MODEL_NAME`           | Tên Model Azure OpenAI của bạn              | Azure AI Foundry của bạn               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Tên Deployment Azure OpenAI của bạn         | Azure AI Foundry của bạn               |
| `AZURE_OPENAI_API_VERSION`          | Phiên bản API cho Azure OpenAI              | Azure AI Foundry của bạn               |
| `OPENAI_API_KEY`                    | API Key cho OpenAI                        | Nền tảng OpenAI của bạn              |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (Tùy chọn)         | Nền tảng OpenAI của bạn              |
| `OPENAI_CHAT_MODEL_ID`              | ID mô hình OpenAI cụ thể (Tùy chọn)       | Nền tảng OpenAI của bạn              |
| `OPENAI_BASE_URL`                   | URL cơ sở API OpenAI tùy chỉnh (Tùy chọn)     | Nền tảng OpenAI của bạn              |

### Bước 3: Cấu hình Quyền cho Workflow

GitHub Action cần quyền được cấp qua `GITHUB_TOKEN` để lấy code và tạo pull request.

1.  Trong kho của bạn, vào **Settings** > **Actions** > **General**.  
2.  Kéo xuống phần **Workflow permissions**.  
3.  Chọn **Read and write permissions**. Điều này cấp cho `GITHUB_TOKEN` quyền `contents: write` và `pull-requests: write` cần thiết cho workflow này.  
4.  Đảm bảo ô **Allow GitHub Actions to create and approve pull requests** được đánh dấu.  
5.  Chọn **Save**.

![Permission setting](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### Bước 4: Tạo File Workflow

Cuối cùng, tạo file YAML định nghĩa workflow tự động sử dụng `GITHUB_TOKEN`.

1.  Trong thư mục gốc của kho, tạo thư mục `.github/workflows/` nếu chưa có.  
2.  Bên trong `.github/workflows/`, tạo file tên `co-op-translator.yml`.  
3.  Dán nội dung sau vào `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_SUBSCRIPTION_KEY: ${{ secrets.AZURE_SUBSCRIPTION_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```  
4.  **Tùy chỉnh Workflow:**  
  - **[!IMPORTANT] Ngôn ngữ mục tiêu:** Trong bước `Run Co-op Translator` step, you **MUST review and modify the list of language codes** within the `translate -l "..." -y` command to match your project's requirements. The example list (`ar de es...`) needs to be replaced or adjusted.
  - **Trigger (`on:`):** The current trigger runs on every push to `main`. For large repositories, consider adding a `paths:` filter (see commented example in the YAML) to run the workflow only when relevant files (e.g., source documentation) change, saving runner minutes.
  - **PR Details:** Customize the `commit-message`, `title`, `body`, `branch` name, and `labels` in the `Create Pull Request` nếu cần.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.