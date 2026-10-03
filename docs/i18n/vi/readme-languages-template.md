# Mẫu README Ngôn ngữ

Co-op Translator có thể duy trì một bảng ngôn ngữ trong README cho các kho lưu trữ xuất bản nội dung đã được dịch.

Sử dụng các marker bên dưới khi bạn muốn Co-op Translator thay thế toàn bộ phần đó trong mỗi lần chạy dịch. Xóa các marker nếu bạn muốn duy trì một tập con tùy chỉnh theo cách thủ công.

Các thông tin ghi nhận và liên kết hướng dẫn bắt đầu ở phía trên các marker là tùy chọn. Chúng giúp người đọc biết cách các bản dịch được duy trì và cách dịch các kho lưu trữ của riêng họ. Giữ chúng ngoài các marker để các cập nhật bảng ngôn ngữ giữ nguyên chúng. Khi cập nhật một kho lưu trữ khác, hãy làm theo hướng dẫn đóng góp của nó và để những người duy trì quyết định liệu có nên bao gồm văn bản này hay không.

````markdown
### Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/co-op-translator)

Maintain your own documentation? [Start with one README and one language](https://github.com/Azure/co-op-translator/blob/main/docs/github-actions.md#your-first-readme-translation-pr).

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](./translations/ar/README.md) | [Bengali](./translations/bn/README.md) | [Bulgarian](./translations/bg/README.md) | [Burmese (Myanmar)](./translations/my/README.md) | [Chinese (Simplified)](./translations/zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](./translations/zh-HK/README.md) | [Chinese (Traditional, Macau)](./translations/zh-MO/README.md) | [Chinese (Traditional, Taiwan)](./translations/zh-TW/README.md) | [Croatian](./translations/hr/README.md) | [Czech](./translations/cs/README.md) | [Danish](./translations/da/README.md) | [Dutch](./translations/nl/README.md) | [Estonian](./translations/et/README.md) | [Finnish](./translations/fi/README.md) | [French](./translations/fr/README.md) | [German](./translations/de/README.md) | [Greek](./translations/el/README.md) | [Hebrew](./translations/he/README.md) | [Hindi](./translations/hi/README.md) | [Hungarian](./translations/hu/README.md) | [Indonesian](./translations/id/README.md) | [Italian](./translations/it/README.md) | [Japanese](./translations/ja/README.md) | [Kannada](./translations/kn/README.md) | [Khmer](./translations/km/README.md) | [Korean](./translations/ko/README.md) | [Lithuanian](./translations/lt/README.md) | [Malay](./translations/ms/README.md) | [Malayalam](./translations/ml/README.md) | [Manipuri (Meitei Mayek)](./translations/mni/README.md) | [Marathi](./translations/mr/README.md) | [Nepali](./translations/ne/README.md) | [Nigerian Pidgin](./translations/pcm/README.md) | [Norwegian](./translations/no/README.md) | [Persian (Farsi)](./translations/fa/README.md) | [Polish](./translations/pl/README.md) | [Portuguese (Brazil)](./translations/pt-BR/README.md) | [Portuguese (Portugal)](./translations/pt-PT/README.md) | [Punjabi (Gurmukhi)](./translations/pa/README.md) | [Romanian](./translations/ro/README.md) | [Russian](./translations/ru/README.md) | [Serbian (Cyrillic)](./translations/sr/README.md) | [Slovak](./translations/sk/README.md) | [Slovenian](./translations/sl/README.md) | [Spanish](./translations/es/README.md) | [Swahili](./translations/sw/README.md) | [Swedish](./translations/sv/README.md) | [Tagalog (Filipino)](./translations/tl/README.md) | [Tamil](./translations/ta/README.md) | [Telugu](./translations/te/README.md) | [Thai](./translations/th/README.md) | [Turkish](./translations/tr/README.md) | [Ukrainian](./translations/uk/README.md) | [Urdu](./translations/ur/README.md) | [Vietnamese](./translations/vi/README.md)

> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```

<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->
````

Cá nhân hóa URL repository sparse-checkout trong quá trình dịch:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

Nếu các marker có mặt, Co-op Translator có thể cập nhật bảng được tạo khi các ngôn ngữ được thêm hoặc thay đổi.

Đối với một README hiện có, bạn có thể thêm mục ghi nhận tùy chọn và liên kết hướng dẫn bắt đầu ở phía trên các marker của bảng ngôn ngữ mà không thay thế các liên kết ngôn ngữ hoặc nội dung khác. Trỏ các liên kết ngôn ngữ được hỗ trợ đến [hướng dẫn ngôn ngữ hiện tại](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md).