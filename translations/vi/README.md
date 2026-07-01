# Co-op Translator

_Dễ dàng tự động hóa và duy trì bản dịch cho nội dung giáo dục trên GitHub của bạn sang nhiều ngôn ngữ khi dự án của bạn phát triển._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Gói Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![Giấy phép: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Lượt tải](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Lượt tải](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Phong cách mã: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Người đóng góp GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![Issue trên GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![Pull request trên GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![Chào đón PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Bắt đầu tại đây:** [Chọn quy trình làm việc của bạn](https://azure.github.io/co-op-translator/workflows/) | [Cấu hình](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 Hỗ trợ đa ngôn ngữ

#### Được hỗ trợ bởi [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Tiếng Ả Rập](../ar/README.md) | [Tiếng Bengal](../bn/README.md) | [Tiếng Bulgaria](../bg/README.md) | [Miến Điện (Myanmar)](../my/README.md) | [Tiếng Trung (Giản thể)](../zh-CN/README.md) | [Tiếng Trung (Phồn thể, Hồng Kông)](../zh-HK/README.md) | [Tiếng Trung (Phồn thể, Macau)](../zh-MO/README.md) | [Tiếng Trung (Phồn thể, Đài Loan)](../zh-TW/README.md) | [Tiếng Croatia](../hr/README.md) | [Tiếng Séc](../cs/README.md) | [Tiếng Đan Mạch](../da/README.md) | [Tiếng Hà Lan](../nl/README.md) | [Tiếng Estonia](../et/README.md) | [Tiếng Phần Lan](../fi/README.md) | [Tiếng Pháp](../fr/README.md) | [Tiếng Đức](../de/README.md) | [Tiếng Hy Lạp](../el/README.md) | [Tiếng Do Thái](../he/README.md) | [Tiếng Hindi](../hi/README.md) | [Tiếng Hungary](../hu/README.md) | [Tiếng Indonesia](../id/README.md) | [Tiếng Ý](../it/README.md) | [Tiếng Nhật](../ja/README.md) | [Tiếng Kannada](../kn/README.md) | [Tiếng Khmer](../km/README.md) | [Tiếng Hàn](../ko/README.md) | [Tiếng Litva](../lt/README.md) | [Tiếng Mã Lai](../ms/README.md) | [Tiếng Malayalam](../ml/README.md) | [Tiếng Marathi](../mr/README.md) | [Tiếng Nepal](../ne/README.md) | [Tiếng Pidgin Nigeria](../pcm/README.md) | [Tiếng Na Uy](../no/README.md) | [Tiếng Ba Tư (Farsi)](../fa/README.md) | [Tiếng Ba Lan](../pl/README.md) | [Tiếng Bồ Đào Nha (Brazil)](../pt-BR/README.md) | [Tiếng Bồ Đào Nha (Portugal)](../pt-PT/README.md) | [Tiếng Punjabi (Gurmukhi)](../pa/README.md) | [Tiếng Romania](../ro/README.md) | [Tiếng Nga](../ru/README.md) | [Tiếng Serbia (Chữ Cyrillic)](../sr/README.md) | [Tiếng Slovakia](../sk/README.md) | [Tiếng Slovenia](../sl/README.md) | [Tiếng Tây Ban Nha](../es/README.md) | [Tiếng Swahili](../sw/README.md) | [Tiếng Thụy Điển](../sv/README.md) | [Tiếng Tagalog (Filipino)](../tl/README.md) | [Tiếng Tamil](../ta/README.md) | [Tiếng Telugu](../te/README.md) | [Tiếng Thái](../th/README.md) | [Tiếng Thổ Nhĩ Kỳ](../tr/README.md) | [Tiếng Ukraina](../uk/README.md) | [Tiếng Urdu](../ur/README.md) | [Tiếng Việt](./README.md)

> **Thích sao chép về máy hơn?**
>
> Kho lưu trữ này bao gồm hơn 50 bản dịch ngôn ngữ, điều này làm tăng đáng kể kích thước tải xuống. Để clone mà không lấy phần bản dịch, hãy sử dụng sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Điều này cung cấp cho bạn mọi thứ cần thiết để hoàn thành khóa học với tốc độ tải xuống nhanh hơn nhiều.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![Người theo dõi GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Fork trên GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![Sao GitHub](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Mở trong GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Tổng quan

**Co-op Translator** giúp bạn bản địa hóa nội dung giáo dục trên GitHub của mình sang nhiều ngôn ngữ một cách dễ dàng.
Khi bạn cập nhật các tệp Markdown, hình ảnh hoặc sổ tay (notebook), các bản dịch sẽ tự động được đồng bộ, đảm bảo nội dung của bạn luôn chính xác và cập nhật cho người học trên toàn thế giới.

Sử dụng từ CLI để dịch repository, từ Python API để tự động hóa, hoặc qua MCP server cho các luồng công việc với agent và editor.

Ví dụ về cách tổ chức nội dung đã được dịch:

![Ví dụ](../../imgs/translation-ex.png)

## Tại sao dùng Co-op Translator?

Dịch một tệp thì dễ. Giữ cho toàn bộ kho tài liệu
được dịch, liên kết và cập nhật mới là phần khó.

| Vấn đề | Co-op Translator giúp như thế nào |
| --- | --- |
| Tài liệu dài không phải là một prompt duy nhất | Các tệp Markdown lớn được chia thành các phần nhỏ, vì vậy một README dài không phụ thuộc vào một phản hồi mô hình mong manh duy nhất. Nếu một phần bị lỗi, Co-op Translator có thể thử lại và chia lại chỉ phần bị lỗi đó. |
| Bản dịch không hoàn chỉnh không nên được đánh dấu là hiện tại | Một bản dịch bị cắt ngắn không bao giờ nên được đóng dấu là đã cập nhật. Co-op Translator kiểm tra tính toàn vẹn của bản dịch trước khi lưu và có thể phát hiện các bản dịch hiện có bị thiếu cấu trúc. |
| Các liên kết nên khớp với cấu trúc repo đã dịch | Các bản dịch thủ công thường để các liên kết tương đối trỏ về cây nguồn. Co-op Translator viết lại các liên kết Markdown, notebook, hình ảnh và README để khớp với cấu trúc `translations/<lang>/...`. |
| Dịch hoạt động trên toàn bộ repository | Co-op Translator xử lý các tệp README, docs, notebooks và văn bản trong hình ảnh như một phần của một luồng công việc repository, thay vì dịch từng tệp một. |
| Duy trì bản dịch quan trọng hơn là tạo ra chúng một lần | Băm nguồn và siêu dữ liệu bản dịch cho phép Co-op Translator tìm các tệp đã lỗi thời, bỏ qua các tệp không đổi và giữ nội dung dịch được đồng bộ khi repo nguồn phát triển. |

## Cách trạng thái bản dịch được quản lý

Co-op Translator quản lý nội dung đã dịch như các **artifact phần mềm có phiên bản**,  
không phải như các tệp tĩnh.

Công cụ theo dõi trạng thái của Markdown, hình ảnh và notebooks đã dịch
sử dụng **siêu dữ liệu theo ngôn ngữ**.

Thiết kế này cho phép Co-op Translator:

- Phát hiện đáng tin cậy các bản dịch đã lỗi thời
- Xem Markdown, hình ảnh và notebooks một cách nhất quán
- Mở rộng an toàn trên các repository lớn, di chuyển nhanh và đa ngôn ngữ

Bằng cách mô hình hóa bản dịch như các artifact được quản lý,
các luồng công việc dịch phù hợp tự nhiên với các
thực hành quản lý phụ thuộc và artifact phần mềm hiện đại.

→ [Cách trạng thái bản dịch được quản lý](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### Bài phân tích chuyên sâu liên quan

- [Khắc phục Markdown bị hỏng trong Dịch AI: Củng cố một pipeline sản xuất](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## Bắt đầu

Co-op Translator có thể được sử dụng từ CLI, Python API hoặc MCP server. Bắt đầu với hướng dẫn workflow nếu bạn đang chọn giữa dịch cục bộ, tự động hóa, CI, và tích hợp agent/editor.

- [Chọn quy trình làm việc của bạn](../../docs/workflows.md)
- [Cấu hình thông tin xác thực](../../docs/configuration.md)
- [Dịch từ CLI](../../docs/cli.md)
- [Tự động hóa với Python API](../../docs/api.md)
- [Kết nối với MCP Server](../../docs/mcp.md)
- [Chạy trong GitHub Actions](../../docs/github-actions.md)

Ví dụ CLI tối thiểu sau khi cấu hình:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

Đối với lần chạy đầu trên các repository lớn, hãy sử dụng `--dry-run` trước khi ghi các tệp đã dịch. Xem [CLI Reference](../../docs/cli.md) để biết các cờ loại nội dung, nhật ký, xem xét và di chuyển liên kết.

Chạy nhanh trong container với Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

Chạy nhanh trong container với PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## Tính năng

- Dịch tự động cho Markdown, notebooks và hình ảnh
- Giữ các bản dịch đồng bộ với các thay đổi nguồn
- Hoạt động cục bộ (CLI) hoặc trong CI (GitHub Actions)
- Cung cấp công cụ dịch Markdown, notebook, hình ảnh, xem xét và dịch dự án thông qua MCP
- Sử dụng Azure OpenAI hoặc OpenAI làm nhà cung cấp dịch
- Cho phép MCP host các agent dịch các đoạn Markdown và notebook mà không cần thông tin xác thực LLM của Co-op Translator
- Sử dụng Azure AI Vision để trích xuất và dịch văn bản trong hình ảnh
- Xem xét cấu trúc và độ mới của bản dịch bằng các kiểm tra xác định
- Bảo toàn định dạng và cấu trúc Markdown

## Tài liệu

- [Trang tài liệu](https://azure.github.io/co-op-translator/)
- [Chọn quy trình làm việc của bạn](../../docs/workflows.md)
- [Cấu hình](../../docs/configuration.md)
- [Thiết lập Azure AI](../../docs/azure-ai-setup.md)
- [CLI Reference](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [Mẫu README ngôn ngữ](../../docs/readme-languages-template.md)
- [Ngôn ngữ được hỗ trợ](../../docs/supported-languages.md)
- [Đóng góp](../../CONTRIBUTING.md)
- [Khắc phục sự cố](../../docs/troubleshooting.md)

### Hướng dẫn dành riêng cho Microsoft
> [!NOTE]
> Dành cho những người duy trì các kho “For Beginners” của Microsoft.

- [Cập nhật danh sách “other courses” (chỉ dành cho kho MS Beginners)](../../docs/microsoft-beginners.md)

## Ủng hộ chúng tôi và thúc đẩy việc học toàn cầu

Hãy cùng chúng tôi cách mạng hóa cách nội dung giáo dục được chia sẻ trên toàn cầu! Hãy cho [Co-op Translator](https://github.com/azure/co-op-translator) một ⭐ trên GitHub và ủng hộ sứ mệnh của chúng tôi trong việc xóa bỏ rào cản ngôn ngữ trong học tập và công nghệ. Sự quan tâm và đóng góp của bạn tạo ra ảnh hưởng đáng kể! Luôn hoan nghênh đóng góp mã và gợi ý tính năng.

### Khám phá nội dung giáo dục của Microsoft bằng ngôn ngữ của bạn
- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Bài thuyết trình video

👉 Nhấp vào hình ảnh bên dưới để xem trên YouTube.

- **Open at Microsoft**: Giới thiệu ngắn 18 phút và hướng dẫn nhanh cách sử dụng Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Đóng góp

Dự án này hoan nghênh các đóng góp và đề xuất. Quan tâm đến việc đóng góp cho Azure Co-op Translator? Vui lòng xem [CONTRIBUTING.md](../../CONTRIBUTING.md) của chúng tôi để biết hướng dẫn về cách bạn có thể giúp Co-op Translator trở nên dễ tiếp cận hơn.

## Những người đóng góp

[![những người đóng góp co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Quy tắc Ứng xử

Dự án này đã áp dụng [Bộ Quy tắc Ứng xử Mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/).
Để biết thêm thông tin, xem [Câu hỏi thường gặp về Bộ Quy tắc Ứng xử](https://opensource.microsoft.com/codeofconduct/faq/) hoặc
liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu bạn có thêm câu hỏi hoặc ý kiến.

## Trách nhiệm về AI

Microsoft cam kết giúp khách hàng sử dụng các sản phẩm AI của chúng tôi một cách có trách nhiệm, chia sẻ những bài học của chúng tôi và xây dựng các quan hệ đối tác dựa trên sự tin tưởng thông qua các công cụ như Transparency Notes và Impact Assessments. Nhiều tài nguyên này có thể được tìm thấy tại [https://aka.ms/RAI](https://aka.ms/RAI).
Cách tiếp cận của Microsoft đối với AI có trách nhiệm được dựa trên các nguyên tắc AI của chúng tôi: công bằng, đáng tin cậy và an toàn, quyền riêng tư và bảo mật, tính bao trùm, minh bạch và trách nhiệm giải trình.

Các mô hình ngôn ngữ, hình ảnh và giọng nói quy mô lớn - giống như những mô hình được sử dụng trong ví dụ này - có thể hành xử theo những cách không công bằng, không đáng tin cậy hoặc gây xúc phạm, từ đó gây ra những tác hại. Vui lòng tham khảo [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) để được thông tin về các rủi ro và hạn chế.

Cách tiếp cận được khuyến nghị để giảm thiểu các rủi ro này là bao gồm một hệ thống an toàn trong kiến trúc của bạn để có thể phát hiện và ngăn chặn hành vi có hại. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) cung cấp một lớp bảo vệ độc lập, có khả năng phát hiện nội dung do người dùng hoặc AI tạo ra có hại trong ứng dụng và dịch vụ. Azure AI Content Safety bao gồm các API văn bản và hình ảnh cho phép bạn phát hiện các tài liệu có hại. Chúng tôi cũng có một Content Safety Studio tương tác cho phép bạn xem, khám phá và thử các đoạn mã mẫu để phát hiện nội dung có hại trên các phương thức khác nhau. Tài liệu [khởi động nhanh sau đây](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) hướng dẫn bạn cách thực hiện các yêu cầu tới dịch vụ.

Một khía cạnh khác cần cân nhắc là hiệu năng tổng thể của ứng dụng. Với các ứng dụng đa phương thức và đa mô hình, chúng tôi coi hiệu năng là việc hệ thống hoạt động như bạn và người dùng mong đợi, bao gồm cả không tạo ra các kết quả có hại. Việc đánh giá hiệu năng của toàn bộ ứng dụng bằng [các chỉ số chất lượng sinh và chỉ số rủi ro và an toàn](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) là rất quan trọng.

Bạn có thể đánh giá ứng dụng AI của mình trong môi trường phát triển bằng cách sử dụng [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Dựa trên một bộ dữ liệu thử nghiệm hoặc một mục tiêu, các tác phẩm sinh của ứng dụng generative AI của bạn được đo định lượng bằng các bộ đánh giá tích hợp hoặc các bộ đánh giá tùy chỉnh do bạn lựa chọn. Để bắt đầu với prompt flow sdk nhằm đánh giá hệ thống của bạn, bạn có thể làm theo [hướng dẫn khởi động nhanh](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Sau khi bạn thực hiện một lần chạy đánh giá, bạn có thể [trực quan hóa kết quả trong Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Nhãn hiệu

Dự án này có thể chứa nhãn hiệu hoặc logo cho các dự án, sản phẩm hoặc dịch vụ. Việc sử dụng nhãn hiệu hoặc logo của Microsoft được ủy quyền phải tuân theo và phải phù hợp với
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Việc sử dụng nhãn hiệu hoặc logo của Microsoft trong các phiên bản đã chỉnh sửa của dự án này không được gây nhầm lẫn hoặc ngụ ý sự tài trợ của Microsoft.
Bất kỳ việc sử dụng nhãn hiệu hoặc logo của bên thứ ba nào đều phải tuân theo chính sách của bên thứ ba đó.

## Nhận trợ giúp

Nếu bạn gặp bế tắc hoặc có bất kỳ câu hỏi nào về việc xây dựng ứng dụng AI, hãy tham gia:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Nếu bạn có phản hồi về sản phẩm hoặc gặp lỗi khi phát triển, hãy truy cập:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)