<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dac6bc281667816537df51f724a0ff2c",
  "translation_date": "2025-11-30T11:44:21+00:00",
  "source_file": "README.md",
  "language_code": "vi"
}
-->
# Co-op Translator

_Dễ dàng tự động hóa việc dịch nội dung giáo dục trên GitHub của bạn sang nhiều ngôn ngữ để tiếp cận khán giả toàn cầu._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Hỗ trợ đa ngôn ngữ

#### Được hỗ trợ bởi [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Tiếng Ả Rập](../ar/README.md) | [Tiếng Bengal](../bn/README.md) | [Tiếng Bungari](../bg/README.md) | [Tiếng Miến Điện (Myanmar)](../my/README.md) | [Tiếng Trung (Giản thể)](../zh/README.md) | [Tiếng Trung (Phồn thể, Hồng Kông)](../hk/README.md) | [Tiếng Trung (Phồn thể, Macau)](../mo/README.md) | [Tiếng Trung (Phồn thể, Đài Loan)](../tw/README.md) | [Tiếng Croatia](../hr/README.md) | [Tiếng Séc](../cs/README.md) | [Tiếng Đan Mạch](../da/README.md) | [Tiếng Hà Lan](../nl/README.md) | [Tiếng Estonia](../et/README.md) | [Tiếng Phần Lan](../fi/README.md) | [Tiếng Pháp](../fr/README.md) | [Tiếng Đức](../de/README.md) | [Tiếng Hy Lạp](../el/README.md) | [Tiếng Do Thái](../he/README.md) | [Tiếng Hindi](../hi/README.md) | [Tiếng Hungary](../hu/README.md) | [Tiếng Indonesia](../id/README.md) | [Tiếng Ý](../it/README.md) | [Tiếng Nhật](../ja/README.md) | [Tiếng Kannada](../kn/README.md) | [Tiếng Hàn](../ko/README.md) | [Tiếng Litva](../lt/README.md) | [Tiếng Mã Lai](../ms/README.md) | [Tiếng Malayalam](../ml/README.md) | [Tiếng Marathi](../mr/README.md) | [Tiếng Nepal](../ne/README.md) | [Tiếng Pidgin Nigeria](../pcm/README.md) | [Tiếng Na Uy](../no/README.md) | [Tiếng Ba Tư (Farsi)](../fa/README.md) | [Tiếng Ba Lan](../pl/README.md) | [Tiếng Bồ Đào Nha (Brazil)](../br/README.md) | [Tiếng Bồ Đào Nha (Bồ Đào Nha)](../pt/README.md) | [Tiếng Punjabi (Gurmukhi)](../pa/README.md) | [Tiếng Romania](../ro/README.md) | [Tiếng Nga](../ru/README.md) | [Tiếng Serbia (Chữ Kirin)](../sr/README.md) | [Tiếng Slovakia](../sk/README.md) | [Tiếng Slovenia](../sl/README.md) | [Tiếng Tây Ban Nha](../es/README.md) | [Tiếng Swahili](../sw/README.md) | [Tiếng Thụy Điển](../sv/README.md) | [Tiếng Tagalog (Filipino)](../tl/README.md) | [Tiếng Tamil](../ta/README.md) | [Tiếng Telugu](../te/README.md) | [Tiếng Thái](../th/README.md) | [Tiếng Thổ Nhĩ Kỳ](../tr/README.md) | [Tiếng Ukraina](../uk/README.md) | [Tiếng Urdu](../ur/README.md) | [Tiếng Việt](./README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Tổng quan

**Co-op Translator** giúp bạn dễ dàng bản địa hóa nội dung giáo dục trên GitHub sang nhiều ngôn ngữ.
Khi bạn cập nhật các tệp Markdown, hình ảnh hoặc sổ tay, các bản dịch sẽ tự động đồng bộ, đảm bảo nội dung luôn chính xác và cập nhật cho người học trên toàn thế giới.

Ví dụ về cách tổ chức nội dung đã được dịch:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.vi.png)

## Bắt đầu nhanh

```bash
# Tạo và kích hoạt môi trường ảo (khuyến nghị)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Cài đặt gói
pip install co-op-translator
# Dịch
translate -l "ko ja fr" -md
```

Docker:

```bash
# Kéo hình ảnh công khai từ GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Chạy với thư mục hiện tại được gắn và cung cấp .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Cài đặt tối giản

1. Tạo tệp `.env` dựa trên mẫu: [.env.template](../../.env.template)
2. Cấu hình một nhà cung cấp LLM (Azure OpenAI hoặc OpenAI)
3. (Tùy chọn) Để dịch hình ảnh (`-img`), cấu hình Azure AI Vision
4. (Khuyến nghị) Xóa các bản dịch cũ để tránh xung đột (ví dụ: `translations/`)
5. (Khuyến nghị) Thêm phần dịch ngôn ngữ vào README của bạn bằng mẫu [README languages template](./getting_started/README_languages_template.md)
6. Xem thêm: [Thiết lập Azure AI](./getting_started/set-up-azure-ai.md)

## Cách sử dụng

Dịch tất cả các loại được hỗ trợ:

```bash
translate -l "ko ja"
```

Chỉ Markdown:

```bash
translate -l "de" -md
```

Markdown + hình ảnh:

```bash
translate -l "pt" -md -img
```

Chỉ sổ tay:

```bash
translate -l "zh" -nb
```

Thêm các tùy chọn khác: [Tham khảo lệnh](./getting_started/command-reference.md)

## Tính năng

- Tự động dịch Markdown, sổ tay và hình ảnh
- Giữ bản dịch đồng bộ với các thay đổi nguồn
- Hoạt động cục bộ (CLI) hoặc trong CI (GitHub Actions)
- Sử dụng Azure OpenAI hoặc OpenAI; tùy chọn Azure AI Vision cho hình ảnh
- Giữ nguyên định dạng và cấu trúc Markdown

## Tài liệu

- [Hướng dẫn dòng lệnh](./getting_started/command-line-guide/command-line-guide.md)
- [Hướng dẫn GitHub Actions (Kho lưu trữ công khai & bí mật tiêu chuẩn)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Hướng dẫn GitHub Actions (Kho lưu trữ tổ chức Microsoft & thiết lập cấp tổ chức)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Mẫu ngôn ngữ README](./getting_started/README_languages_template.md)
- [Ngôn ngữ được hỗ trợ](./getting_started/supported-languages.md)
- [Đóng góp](./CONTRIBUTING.md)
- [Khắc phục sự cố](./getting_started/troubleshooting.md)

### Hướng dẫn dành riêng cho Microsoft
> [!NOTE]
> Dành cho người duy trì các kho lưu trữ “For Beginners” của Microsoft.

- [Cập nhật danh sách “khóa học khác” (chỉ dành cho kho lưu trữ MS Beginners)](./getting_started/update-other-courses.md)

## Hỗ trợ chúng tôi và thúc đẩy học tập toàn cầu

Hãy cùng chúng tôi cách mạng hóa cách chia sẻ nội dung giáo dục trên toàn cầu! Hãy cho [Co-op Translator](https://github.com/azure/co-op-translator) một ⭐ trên GitHub và ủng hộ sứ mệnh phá bỏ rào cản ngôn ngữ trong học tập và công nghệ. Sự quan tâm và đóng góp của bạn có ảnh hưởng lớn! Luôn hoan nghênh các đóng góp mã và đề xuất tính năng.

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

## Video thuyết trình

👉 Nhấn vào hình bên dưới để xem trên YouTube.

- **Open at Microsoft**: Giới thiệu ngắn 18 phút và hướng dẫn nhanh cách sử dụng Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.vi.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Đóng góp

Dự án này hoan nghênh các đóng góp và đề xuất. Bạn quan tâm đóng góp cho Azure Co-op Translator? Vui lòng xem [CONTRIBUTING.md](./CONTRIBUTING.md) để biết hướng dẫn giúp Co-op Translator trở nên dễ tiếp cận hơn.

## Những người đóng góp

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Quy tắc ứng xử

Dự án này đã áp dụng [Quy tắc ứng xử mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/).
Để biết thêm thông tin, xem [Câu hỏi thường gặp về Quy tắc ứng xử](https://opensource.microsoft.com/codeofconduct/faq/) hoặc
liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu có câu hỏi hoặc góp ý thêm.

## Trí tuệ nhân tạo có trách nhiệm

Microsoft cam kết giúp khách hàng sử dụng các sản phẩm AI của chúng tôi một cách có trách nhiệm, chia sẻ những bài học kinh nghiệm và xây dựng các quan hệ đối tác dựa trên sự tin tưởng thông qua các công cụ như Transparency Notes và Impact Assessments. Nhiều tài nguyên này có thể được tìm thấy tại [https://aka.ms/RAI](https://aka.ms/RAI).
Cách tiếp cận AI có trách nhiệm của Microsoft dựa trên các nguyên tắc AI về công bằng, độ tin cậy và an toàn, quyền riêng tư và bảo mật, tính bao trùm, minh bạch và trách nhiệm giải trình.

Các mô hình ngôn ngữ tự nhiên, hình ảnh và giọng nói quy mô lớn - như những mô hình được sử dụng trong ví dụ này - có thể có hành vi không công bằng, không đáng tin cậy hoặc gây xúc phạm, dẫn đến các tác hại. Vui lòng tham khảo [Transparency note của dịch vụ Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) để được thông tin về các rủi ro và giới hạn.
Cách tiếp cận được khuyến nghị để giảm thiểu các rủi ro này là bao gồm một hệ thống an toàn trong kiến trúc của bạn có thể phát hiện và ngăn chặn hành vi gây hại. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> cung cấp một lớp bảo vệ độc lập, có khả năng phát hiện nội dung do người dùng và AI tạo ra có hại trong các ứng dụng và dịch vụ. Azure AI Content Safety bao gồm các API văn bản và hình ảnh cho phép bạn phát hiện các tài liệu có hại. Chúng tôi cũng có một Content Safety Studio tương tác cho phép bạn xem, khám phá và thử mã mẫu để phát hiện nội dung có hại trên các phương thức khác nhau. Tài liệu <a href="https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest">bắt đầu nhanh</a> sau đây hướng dẫn bạn cách gửi yêu cầu đến dịch vụ.

Một khía cạnh khác cần lưu ý là hiệu suất tổng thể của ứng dụng. Với các ứng dụng đa phương thức và đa mô hình, chúng tôi xem hiệu suất là hệ thống hoạt động như bạn và người dùng mong đợi, bao gồm cả việc không tạo ra các kết quả có hại. Việc đánh giá hiệu suất của toàn bộ ứng dụng của bạn bằng cách sử dụng <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">các chỉ số chất lượng tạo ra và rủi ro an toàn</a> là rất quan trọng.

Bạn có thể đánh giá ứng dụng AI của mình trong môi trường phát triển bằng cách sử dụng <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK</a>. Với một bộ dữ liệu kiểm thử hoặc mục tiêu, các kết quả tạo ra của ứng dụng AI sinh tạo của bạn được đo lường định lượng bằng các bộ đánh giá tích hợp sẵn hoặc bộ đánh giá tùy chỉnh mà bạn chọn. Để bắt đầu với prompt flow sdk để đánh giá hệ thống của bạn, bạn có thể theo dõi <a href="https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk">hướng dẫn bắt đầu nhanh</a>. Khi bạn thực hiện một lần chạy đánh giá, bạn có thể <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">trực quan hóa kết quả trong Azure AI Studio</a>.

## Nhãn hiệu

Dự án này có thể chứa nhãn hiệu hoặc logo của các dự án, sản phẩm hoặc dịch vụ. Việc sử dụng nhãn hiệu hoặc logo của Microsoft được ủy quyền phải tuân theo và phải theo <a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">Hướng dẫn Nhãn hiệu & Thương hiệu của Microsoft</a>. Việc sử dụng nhãn hiệu hoặc logo của Microsoft trong các phiên bản sửa đổi của dự án này không được gây nhầm lẫn hoặc ngụ ý Microsoft tài trợ. Bất kỳ việc sử dụng nhãn hiệu hoặc logo của bên thứ ba nào đều phải tuân theo chính sách của bên thứ ba đó.

## Nhận trợ giúp

Nếu bạn gặp khó khăn hoặc có bất kỳ câu hỏi nào về việc xây dựng ứng dụng AI, hãy tham gia:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Nếu bạn có phản hồi về sản phẩm hoặc lỗi trong quá trình xây dựng, hãy truy cập:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn tham khảo chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->