<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "18318279bb851dc2c709bfc6a26f6e1d",
  "translation_date": "2025-05-07T14:16:01+00:00",
  "source_file": "README.md",
  "language_code": "vi"
}
-->
![Logo](../../imgs/logo.png)

# Co-op Translator: Tự động hóa việc dịch tài liệu giáo dục một cách dễ dàng

_Dễ dàng tự động hóa việc dịch tài liệu của bạn sang nhiều ngôn ngữ để tiếp cận đối tượng toàn cầu._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### Hỗ trợ ngôn ngữ được cung cấp bởi Co-op Translator

[Korean](../ko/README.md) | [Japanese](../ja/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Spanish](../es/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Portuguese (Brazil)](../br/README.md) | [Hindi](../hi/README.md) | [Russian](../ru/README.md) | [Turkish](../tr/README.md) | [Arabic](../ar/README.md) | [Indonesian](../id/README.md) | [Vietnamese](./README.md)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

> [!TIP]
> **Tự động hóa mạnh mẽ**: Giờ đây hỗ trợ GitHub Actions! Tự động dịch tài liệu của bạn mỗi khi có thay đổi trong kho lưu trữ, giúp mọi thứ luôn được cập nhật một cách dễ dàng. [Tìm hiểu thêm](../..).

## Các Mô Hình và Dịch Vụ Được Hỗ Trợ

| Loại                  | Tên                           |
|-----------------------|--------------------------------|
| Language Model        | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-blue?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-green?style=flat-square&logo=openai) |
| Computer Vision       | ![Azure Computer Vision](https://img.shields.io/badge/Azure_Computer_Vision-blue?style=flat-square) |

> [!NOTE]
> Nếu dịch vụ computer vision không khả dụng, co-op translator sẽ chuyển sang [chế độ chỉ Markdown](./getting_started/markdown-only-mode.md).

## Tổng Quan: Tinh Giản Quá Trình Dịch Nội Dung Giáo Dục

Rào cản ngôn ngữ gây khó khăn lớn trong việc tiếp cận tài nguyên giáo dục và kiến thức kỹ thuật giá trị cho người học và nhà phát triển trên toàn thế giới. Điều này hạn chế sự tham gia và làm chậm tiến trình đổi mới và học hỏi toàn cầu.

**Co-op Translator** ra đời nhằm giải quyết quy trình dịch thủ công kém hiệu quả cho các chuỗi giáo dục quy mô lớn của Microsoft (như các hướng dẫn "For Beginners"). Công cụ này đã phát triển thành một giải pháp mạnh mẽ, dễ sử dụng, giúp phá bỏ các rào cản ngôn ngữ cho tất cả mọi người. Bằng cách cung cấp bản dịch tự động chất lượng cao qua CLI và GitHub Actions, Co-op Translator hỗ trợ giáo viên, sinh viên, nhà nghiên cứu và lập trình viên toàn cầu chia sẻ và tiếp cận kiến thức mà không bị giới hạn bởi ngôn ngữ.

Xem cách Co-op Translator tổ chức nội dung giáo dục đã được dịch:

![Example](../../imgs/translation-ex.png)

Các file Markdown và văn bản trong hình ảnh được dịch tự động và sắp xếp gọn gàng vào các thư mục theo ngôn ngữ.

**Mở khóa truy cập toàn cầu cho nội dung giáo dục của bạn với Co-op Translator ngay hôm nay!**

## Hỗ Trợ Truy Cập Toàn Cầu Cho Tài Nguyên Học Tập Của Microsoft

Co-op Translator giúp thu hẹp khoảng cách ngôn ngữ cho các sáng kiến giáo dục quan trọng của Microsoft, tự động hóa quy trình dịch cho các kho lưu trữ phục vụ cộng đồng lập trình viên toàn cầu. Một số ví dụ đang sử dụng Co-op Translator bao gồm:

[![ML-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ML-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ML-For-Beginners)
[![Generative-AI-for-beginners-dotnet](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=Generative-AI-for-beginners-dotnet&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[![AI-For-Beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=AI-For-Beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/AI-For-Beginners)
[![ai-agents-for-beginners](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=ai-agents-for-beginners&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/ai-agents-for-beginners)
[![PhiCookBook](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=PhiCookBook&bg_color=ffffff&title_color=0078D4&text_color=333333&border_color=c0d8f0&border_radius=10)](https://github.com/microsoft/PhiCookBook)

## Các Tính Năng Chính

- **Dịch tự động**: Dịch văn bản sang nhiều ngôn ngữ một cách dễ dàng.
- **Tích hợp GitHub Actions**: Tự động hóa dịch thuật như một phần của pipeline CI/CD.
- **Giữ nguyên định dạng Markdown**: Bảo toàn cú pháp Markdown chính xác trong quá trình dịch.
- **Dịch văn bản trong hình ảnh**: Trích xuất và dịch nội dung văn bản trong hình ảnh.
- **Công nghệ LLM tiên tiến**: Sử dụng các mô hình ngôn ngữ hiện đại để dịch chất lượng cao.
- **Dễ dàng tích hợp**: Kết nối mượt mà với cấu hình dự án hiện tại của bạn.
- **Đơn giản hóa việc bản địa hóa**: Tinh giản quy trình địa phương hóa dự án cho thị trường quốc tế.

## Cách Hoạt Động

![Architecture](../../imgs/architecture_241019.png)

Co-op Translator lấy các file Markdown và hình ảnh từ thư mục dự án của bạn và xử lý như sau:

1. **Trích xuất văn bản**: Trích xuất văn bản từ file Markdown và, nếu được cấu hình (ví dụ với Azure Computer Vision), cả văn bản nhúng trong hình ảnh.
1. **Dịch bằng AI**: Gửi văn bản đã trích xuất đến LLM được cấu hình (Azure OpenAI, OpenAI, v.v.) để dịch.
1. **Lưu kết quả**: Lưu các file Markdown và hình ảnh đã được dịch vào các thư mục theo ngôn ngữ, giữ nguyên định dạng gốc.

## Bắt Đầu

> [!NOTE]
> Mặc dù hướng dẫn này tập trung vào tài nguyên Azure, bạn có thể sử dụng bất kỳ mô hình ngôn ngữ nào được hỗ trợ trong danh sách [supported models and services](../..).

Bắt đầu nhanh với CLI hoặc thiết lập tự động hóa hoàn chỉnh với GitHub Actions.

### Thiết Lập Ban Đầu

- [Thiết lập Azure AI](./getting_started/set-up-azure-ai.md)

### Bắt Đầu Nhanh: Dòng Lệnh

Để bắt đầu nhanh với dòng lệnh:

1. Cài đặt gói:
    ```bash
    pip install co-op-translator
    ```
2. Cấu hình thông tin đăng nhập:
  - Tạo file `.env` file in your project's root directory.
  - Copy the contents from the [.env.template](../../.env.template) file into your new `.env` file.
  - Fill in the required API keys and endpoint information in your `.env` file.
3. Run Translation:
  - Navigate to your project's root directory in your terminal.
  - Execute the translate command, specifying target languages with the `-l` với cờ:
    ```bash
    translate -l "ko ja fr"
    ```
    *(Thay thế `"ko ja fr"` with your desired space-separated language codes)*

### Detailed Usage Guides

Choose the approach that best fits your workflow:

#### 1. Using the Command Line (CLI)

- Best for: One-time translations, manual control, or integration into custom scripts.
- Requires: Local installation of Python and the `co-op-translator` package.
- Guide: [Command Line Guide](./getting_started/command-line-guide/command-line-guide.md)

#### 2. Using GitHub Actions (Automation)

- Best for: Automatically translating content whenever changes are pushed to your repository. Keeps translations consistently up-to-date.
- Requires: Setting up a workflow file (`.github/workflows`) trong kho của bạn. Không cần cài đặt cục bộ.
- Hướng dẫn:
  - [GitHub Actions Guide (Public Repositories & Standard Secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md) - Dùng cho hầu hết các kho công khai hoặc cá nhân dựa trên bí mật kho chuẩn.
  - [GitHub Actions Guide (Microsoft Organization Repos & Org-Level Setups)](./getting_started/github-actions-guide/github-actions-guide-org.md) - Dùng khi làm việc trong tổ chức Microsoft GitHub hoặc cần sử dụng bí mật cấp tổ chức hoặc runner.

### Khắc Phục Sự Cố và Mẹo

- [Hướng dẫn khắc phục sự cố](./getting_started/troubleshooting.md)

### Tài Nguyên Bổ Sung

- [Tham khảo lệnh](./getting_started/command-reference.md): Hướng dẫn chi tiết tất cả các lệnh và tùy chọn có sẵn.
- [Thiết lập hỗ trợ đa ngôn ngữ](./getting_started/multi-language-support.md): Cách thêm bảng liên kết đến các phiên bản dịch trong README.
- [Ngôn ngữ được hỗ trợ](./getting_started/supported-languages.md): Kiểm tra danh sách các ngôn ngữ được hỗ trợ và hướng dẫn thêm ngôn ngữ mới.
- [Chế độ chỉ Markdown](./getting_started/markdown-only-mode.md): Cách dịch chỉ văn bản, không dịch hình ảnh.

## Video Trình Bày

Tìm hiểu thêm về Co-op Translator qua các bài trình bày của chúng tôi _(Nhấn vào hình để xem trên YouTube.)_:

- **Open at Microsoft**: Giới thiệu ngắn 18 phút và hướng dẫn nhanh cách sử dụng Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

- **Microsoft Reactor**: Hướng dẫn chi tiết một giờ, từng bước, bao gồm hiểu về Co-op Translator, thiết lập công cụ, sử dụng hiệu quả và demo trực tiếp tính năng.

  [![Microsoft Reactor](../../imgs/reactor-thumbnail.jpg)](https://www.youtube.com/watch?v=boTtKVPBLAc)

## Ủng Hộ Chúng Tôi và Thúc Đẩy Học Tập Toàn Cầu

Hãy cùng chúng tôi cách mạng hóa việc chia sẻ nội dung giáo dục trên toàn cầu! Hãy cho [Co-op Translator](https://github.com/azure/co-op-translator) một ⭐ trên GitHub và ủng hộ sứ mệnh phá bỏ rào cản ngôn ngữ trong học tập và công nghệ. Sự quan tâm và đóng góp của bạn tạo nên sự khác biệt lớn! Luôn hoan nghênh đóng góp mã nguồn và đề xuất tính năng.

## Đóng Góp

Dự án này hoan nghênh các đóng góp và đề xuất. Quan tâm tham gia phát triển Azure Co-op Translator? Vui lòng xem [CONTRIBUTING.md](./CONTRIBUTING.md) để biết hướng dẫn giúp làm cho Co-op Translator dễ tiếp cận hơn.

## Những Người Đóng Góp

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Quy Tắc Ứng Xử

Dự án này đã áp dụng [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Để biết thêm thông tin, xem [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) hoặc
liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu có câu hỏi hoặc góp ý thêm.

## Trách Nhiệm AI

Microsoft cam kết giúp khách hàng sử dụng sản phẩm AI một cách có trách nhiệm, chia sẻ kinh nghiệm và xây dựng các quan hệ đối tác dựa trên sự tin cậy thông qua các công cụ như Transparency Notes và Impact Assessments. Nhiều tài nguyên này có thể được tìm thấy tại [https://aka.ms/RAI](https://aka.ms/RAI).
Phương pháp của Microsoft về AI có trách nhiệm dựa trên các nguyên tắc AI về công bằng, độ tin cậy và an toàn, quyền riêng tư và bảo mật, tính bao trùm, minh bạch và trách nhiệm giải trình.
Các mô hình ngôn ngữ tự nhiên, hình ảnh và giọng nói quy mô lớn - như những mô hình được sử dụng trong ví dụ này - có thể hoạt động theo những cách không công bằng, không đáng tin cậy hoặc gây khó chịu, từ đó gây ra các tác hại. Vui lòng tham khảo [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) để được thông tin về các rủi ro và giới hạn.

Cách tiếp cận được khuyến nghị để giảm thiểu các rủi ro này là tích hợp một hệ thống an toàn trong kiến trúc của bạn, có thể phát hiện và ngăn chặn hành vi gây hại. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) cung cấp một lớp bảo vệ độc lập, có khả năng phát hiện nội dung do người dùng hoặc AI tạo ra có tính chất gây hại trong các ứng dụng và dịch vụ. Azure AI Content Safety bao gồm các API văn bản và hình ảnh cho phép bạn phát hiện các tài liệu có hại. Chúng tôi cũng có một công cụ tương tác Content Safety Studio giúp bạn xem, khám phá và thử nghiệm mã mẫu để phát hiện nội dung gây hại trên nhiều phương thức khác nhau. Tài liệu [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) dưới đây sẽ hướng dẫn bạn cách gửi yêu cầu đến dịch vụ.

Một khía cạnh khác cần xem xét là hiệu suất tổng thể của ứng dụng. Với các ứng dụng đa phương thức và đa mô hình, chúng tôi coi hiệu suất là việc hệ thống hoạt động đúng như bạn và người dùng mong đợi, bao gồm cả việc không tạo ra các kết quả gây hại. Việc đánh giá hiệu suất tổng thể của ứng dụng nên dựa trên [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Bạn có thể đánh giá ứng dụng AI của mình trong môi trường phát triển bằng cách sử dụng [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Với một bộ dữ liệu kiểm thử hoặc mục tiêu cụ thể, các kết quả tạo ra của ứng dụng AI sinh tạo sẽ được đo lường định lượng thông qua các bộ đánh giá tích hợp sẵn hoặc bộ đánh giá tùy chỉnh theo lựa chọn của bạn. Để bắt đầu với prompt flow sdk nhằm đánh giá hệ thống, bạn có thể theo dõi [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Sau khi thực hiện một lần chạy đánh giá, bạn có thể [trực quan hóa kết quả trong Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Dự án này có thể chứa các nhãn hiệu hoặc logo của các dự án, sản phẩm hoặc dịch vụ. Việc sử dụng nhãn hiệu hoặc logo của Microsoft được ủy quyền phải tuân thủ và theo [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Việc sử dụng nhãn hiệu hoặc logo của Microsoft trong các phiên bản sửa đổi của dự án này không được gây nhầm lẫn hoặc ngụ ý sự tài trợ của Microsoft. Mọi việc sử dụng nhãn hiệu hoặc logo của bên thứ ba phải tuân theo chính sách của bên thứ ba đó.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn tham khảo chính xác nhất. Đối với thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.