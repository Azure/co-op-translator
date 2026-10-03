# เทมเพลตภาษา README

Co-op Translator สามารถจัดการตารางภาษาของ README สำหรับรีโพซิทอรีที่เผยแพร่เนื้อหาที่แปลแล้ว

ใช้เครื่องหมายด้านล่างเมื่อคุณต้องการให้ Co-op Translator แทนที่ทั้งส่วนในการรันการแปลแต่ละครั้ง หากคุณต้องการดูแลเฉพาะส่วนด้วยตนเอง ให้ลบเครื่องหมายเหล่านั้นออก

การให้เครดิตและลิงก์เริ่มต้นที่อยู่เหนือเครื่องหมายเป็นทางเลือก ช่วยให้ผู้อ่านค้นพบว่าการแปลได้รับการดูแลอย่างไร และวิธีแปลรีโพซิทอรีของตนเอง เก็บไว้ให้นอกเครื่องหมายเพื่อให้การอัปเดตตารางภาษาเก็บข้อความเหล่านั้นไว้ เมื่ออัปเดตรีโพซิทอรีของผู้อื่น ให้ปฏิบัติตามแนวทางการร่วมส่งของโปรเจกต์นั้นและให้ผู้ดูแลตัดสินใจว่าจะรวมข้อความนี้หรือไม่

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

ปรับแต่ง URL ของ repository สำหรับ sparse-checkout ระหว่างการแปล:

```bash
translate -l "ko" --repo-url "https://github.com/org/repo.git"
```

หากมีเครื่องหมายอยู่ Co-op Translator สามารถอัปเดตตารางที่สร้างขึ้นเมื่อมีการเพิ่มหรือเปลี่ยนแปลงภาษา

สำหรับ README ที่มีอยู่แล้ว คุณสามารถเพิ่มการให้เครดิตและลิงก์เริ่มต้นแบบทางเลือกไว้เหนือเครื่องหมายตารางภาษาได้โดยไม่ต้องแทนที่ลิงก์ภาษาหรือเนื้อหาอื่นๆ ชี้ลิงก์ภาษาที่รองรับไปยัง [คู่มือภาษาปัจจุบัน](https://github.com/Azure/co-op-translator/blob/main/docs/supported-languages.md)