<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:34:49+00:00",
  "source_file": "README.md",
  "language_code": "vi"
}
-->
# Co-op Translator

_Tự động hóa việc dịch nội dung giáo dục trên GitHub của bạn sang nhiều ngôn ngữ để tiếp cận khán giả toàn cầu một cách dễ dàng._

### 🌐 Hỗ trợ đa ngôn ngữ

#### Được hỗ trợ bởi [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Tiếng Ả Rập](../ar/README.md) | [Tiếng Bengal](../bn/README.md) | [Tiếng Bulgaria](../bg/README.md) | [Tiếng Miến Điện (Myanmar)](../my/README.md) | [Tiếng Trung (Giản thể)](../zh/README.md) | [Tiếng Trung (Phồn thể, Hồng Kông)](../hk/README.md) | [Tiếng Trung (Phồn thể, Macau)](../mo/README.md) | [Tiếng Trung (Phồn thể, Đài Loan)](../tw/README.md) | [Tiếng Croatia](../hr/README.md) | [Tiếng Séc](../cs/README.md) | [Tiếng Đan Mạch](../da/README.md) | [Tiếng Hà Lan](../nl/README.md) | [Tiếng Estonia](../et/README.md) | [Tiếng Phần Lan](../fi/README.md) | [Tiếng Pháp](../fr/README.md) | [Tiếng Đức](../de/README.md) | [Tiếng Hy Lạp](../el/README.md) | [Tiếng Do Thái](../he/README.md) | [Tiếng Hindi](../hi/README.md) | [Tiếng Hungary](../hu/README.md) | [Tiếng Indonesia](../id/README.md) | [Tiếng Ý](../it/README.md) | [Tiếng Nhật](../ja/README.md) | [Tiếng Hàn](../ko/README.md) | [Tiếng Litva](../lt/README.md) | [Tiếng Mã Lai](../ms/README.md) | [Tiếng Marathi](../mr/README.md) | [Tiếng Nepal](../ne/README.md) | [Tiếng Na Uy](../no/README.md) | [Tiếng Ba Tư (Farsi)](../fa/README.md) | [Tiếng Ba Lan](../pl/README.md) | [Tiếng Bồ Đào Nha (Brazil)](../br/README.md) | [Tiếng Bồ Đào Nha (Bồ Đào Nha)](../pt/README.md) | [Tiếng Punjab (Gurmukhi)](../pa/README.md) | [Tiếng Romania](../ro/README.md) | [Tiếng Nga](../ru/README.md) | [Tiếng Serbia (Chữ Kirin)](../sr/README.md) | [Tiếng Slovak](../sk/README.md) | [Tiếng Slovenia](../sl/README.md) | [Tiếng Tây Ban Nha](../es/README.md) | [Tiếng Swahili](../sw/README.md) | [Tiếng Thụy Điển](../sv/README.md) | [Tiếng Tagalog (Philippines)](../tl/README.md) | [Tiếng Tamil](../ta/README.md) | [Tiếng Thái](../th/README.md) | [Tiếng Thổ Nhĩ Kỳ](../tr/README.md) | [Tiếng Ukraina](../uk/README.md) | [Tiếng Urdu](../ur/README.md) | [Tiếng Việt](./README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Tổng quan

**Co-op Translator** giúp bạn nhanh chóng dịch nội dung giáo dục trên GitHub sang nhiều ngôn ngữ, dễ dàng tiếp cận người dùng toàn cầu. Khi bạn cập nhật các tệp Markdown, hình ảnh hoặc notebook Jupyter, các bản dịch sẽ được đồng bộ tự động để đảm bảo nội dung giáo dục trên GitHub của bạn luôn mới và phù hợp với người dùng quốc tế.

Xem cách Co-op Translator tổ chức nội dung giáo dục đã dịch trên GitHub:

![Ví dụ](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.vi.png)

## Bắt đầu nhanh

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Thiết lập tối thiểu

- Tạo file `.env` dựa trên mẫu: [.env.template](../../.env.template)
- Cấu hình một nhà cung cấp LLM (Azure OpenAI hoặc OpenAI)
- Để dịch hình ảnh (`-img`), cần thiết lập thêm Azure AI Vision
- Khuyến nghị: Nếu bạn có các bản dịch được tạo bởi công cụ khác, hãy dọn dẹp trước để tránh xung đột (ví dụ: `translations/`).
- Khuyến nghị: Thêm mục ngôn ngữ dịch vào README của bạn bằng [mẫu README languages](./README_languages_template.md)
- Xem thêm: [Thiết lập Azure AI](./getting_started/set-up-azure-ai.md)

## Cách sử dụng

Dịch tất cả các loại được hỗ trợ:

```bash
translate -l "ko ja"
```

Chỉ dịch Markdown:

```bash
translate -l "de" -md
```

Markdown + hình ảnh:

```bash
translate -l "pt" -md -img
```

Chỉ dịch notebook:

```bash
translate -l "zh" -nb
```

Thêm tuỳ chọn: [Tham khảo lệnh](./getting_started/command-reference.md)

## Tính năng

- Tự động dịch Markdown, notebook và hình ảnh
- Giữ cho các bản dịch luôn đồng bộ với thay đổi nguồn
- Hoạt động trên máy cá nhân (CLI) hoặc CI (GitHub Actions)
- Sử dụng Azure OpenAI hoặc OpenAI; có thể dùng thêm Azure AI Vision cho hình ảnh
- Giữ nguyên định dạng và cấu trúc Markdown

## Tài liệu

- [Hướng dẫn dòng lệnh](./getting_started/command-line-guide/command-line-guide.md)
- [Hướng dẫn GitHub Actions (Kho công khai & secrets tiêu chuẩn)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Hướng dẫn GitHub Actions (Kho tổ chức Microsoft & thiết lập cấp tổ chức)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Các ngôn ngữ được hỗ trợ](./getting_started/supported-languages.md)
- [Khắc phục sự cố](./getting_started/troubleshooting.md)

## Ủng hộ chúng tôi và thúc đẩy học tập toàn cầu

Hãy cùng chúng tôi thay đổi cách chia sẻ nội dung giáo dục trên toàn thế giới! Hãy cho [Co-op Translator](https://github.com/azure/co-op-translator) một ⭐ trên GitHub và ủng hộ sứ mệnh phá bỏ rào cản ngôn ngữ trong học tập và công nghệ. Sự quan tâm và đóng góp của bạn tạo nên sự khác biệt lớn! Luôn hoan nghênh đóng góp mã nguồn và đề xuất tính năng mới.

### Khám phá nội dung giáo dục Microsoft bằng ngôn ngữ của bạn

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

## Video giới thiệu

Tìm hiểu thêm về Co-op Translator qua các bài thuyết trình của chúng tôi _(Nhấn vào hình bên dưới để xem trên YouTube.)_:

- **Open at Microsoft**: Giới thiệu ngắn 18 phút và hướng dẫn nhanh cách sử dụng Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.vi.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Đóng góp

Dự án này hoan nghênh mọi đóng góp và ý kiến. Bạn muốn đóng góp cho Azure Co-op Translator? Vui lòng xem [CONTRIBUTING.md](./CONTRIBUTING.md) để biết hướng dẫn cách giúp Co-op Translator trở nên dễ tiếp cận hơn.

## Những người đóng góp

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Quy tắc ứng xử

Dự án này tuân theo [Quy tắc Ứng xử Mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/).
Để biết thêm thông tin, xem [Câu hỏi thường gặp về Quy tắc Ứng xử](https://opensource.microsoft.com/codeofconduct/faq/) hoặc
liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu bạn có thêm câu hỏi hoặc ý kiến.

## AI có trách nhiệm

Microsoft cam kết giúp khách hàng sử dụng sản phẩm AI một cách có trách nhiệm, chia sẻ kinh nghiệm và xây dựng quan hệ đối tác dựa trên sự tin tưởng thông qua các công cụ như Transparency Notes và Impact Assessments. Nhiều tài nguyên này có tại [https://aka.ms/RAI](https://aka.ms/RAI).
Cách tiếp cận AI có trách nhiệm của Microsoft dựa trên các nguyên tắc về công bằng, độ tin cậy và an toàn, quyền riêng tư và bảo mật, tính bao trùm, minh bạch và trách nhiệm giải trình.

Các mô hình ngôn ngữ, hình ảnh và giọng nói quy mô lớn - như những mô hình được sử dụng trong ví dụ này - có thể có hành vi không công bằng, không đáng tin cậy hoặc gây phản cảm, dẫn đến những tác hại nhất định. Vui lòng tham khảo [Ghi chú minh bạch dịch vụ Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) để hiểu rõ về rủi ro và giới hạn.

Cách khuyến nghị để giảm thiểu các rủi ro này là tích hợp hệ thống an toàn vào kiến trúc của bạn để phát hiện và ngăn chặn hành vi gây hại. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) cung cấp một lớp bảo vệ độc lập, có thể phát hiện nội dung do người dùng hoặc AI tạo ra có tính chất gây hại trong ứng dụng và dịch vụ. Azure AI Content Safety bao gồm API cho văn bản và hình ảnh giúp bạn phát hiện nội dung độc hại. Chúng tôi cũng có Content Safety Studio tương tác cho phép bạn xem, khám phá và thử mã mẫu để phát hiện nội dung gây hại trên nhiều loại dữ liệu khác nhau. [Tài liệu hướng dẫn nhanh](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) sẽ hướng dẫn bạn cách gửi yêu cầu tới dịch vụ này.
Một khía cạnh khác cần lưu ý là hiệu năng tổng thể của ứng dụng. Với các ứng dụng đa phương thức và đa mô hình, hiệu năng được hiểu là hệ thống hoạt động đúng như bạn và người dùng mong đợi, bao gồm cả việc không tạo ra các kết quả gây hại. Việc đánh giá hiệu năng của toàn bộ ứng dụng bằng [các chỉ số chất lượng sinh và rủi ro, an toàn](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) là rất quan trọng.

Bạn có thể đánh giá ứng dụng AI của mình trong môi trường phát triển bằng [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Với một bộ dữ liệu kiểm thử hoặc mục tiêu, các kết quả sinh ra từ ứng dụng AI của bạn sẽ được đo lường định lượng bằng các bộ đánh giá tích hợp sẵn hoặc bộ đánh giá tùy chỉnh do bạn chọn. Để bắt đầu sử dụng prompt flow sdk để đánh giá hệ thống, bạn có thể làm theo [hướng dẫn nhanh](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Sau khi thực hiện một lần đánh giá, bạn có thể [trực quan hóa kết quả trên Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Thương hiệu

Dự án này có thể chứa các thương hiệu hoặc logo của các dự án, sản phẩm hoặc dịch vụ. Việc sử dụng hợp lệ thương hiệu hoặc logo của Microsoft phải tuân thủ
[Hướng dẫn về Thương hiệu & Nhãn hiệu của Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Việc sử dụng thương hiệu hoặc logo của Microsoft trong các phiên bản đã chỉnh sửa của dự án này không được gây nhầm lẫn hoặc ám chỉ sự bảo trợ của Microsoft.
Việc sử dụng thương hiệu hoặc logo của bên thứ ba phải tuân theo chính sách của bên thứ ba đó.

## Hỗ trợ

Nếu bạn gặp khó khăn hoặc có câu hỏi về việc xây dựng ứng dụng AI, hãy tham gia:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Nếu bạn có phản hồi về sản phẩm hoặc gặp lỗi khi xây dựng, hãy truy cập:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được xem là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.