<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f776df01855a3a659c8eb6f16a5de74",
  "translation_date": "2025-10-15T03:15:51+00:00",
  "source_file": "README.md",
  "language_code": "th"
}
-->
# Co-op Translator

_แปลเนื้อหาการศึกษาบน GitHub ของคุณเป็นหลายภาษาโดยอัตโนมัติ เพื่อเข้าถึงผู้คนทั่วโลกได้ง่ายขึ้น_

### 🌐 รองรับหลายภาษา

#### รองรับโดย [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](./README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ภาพรวม

**Co-op Translator** ช่วยให้คุณแปลเนื้อหาการศึกษาบน GitHub เป็นหลายภาษาได้อย่างรวดเร็ว เข้าถึงผู้ใช้ทั่วโลกได้ง่าย เมื่อคุณอัปเดตไฟล์ Markdown, รูปภาพ หรือ Jupyter notebooks ระบบจะแปลและซิงค์เนื้อหาโดยอัตโนมัติ เพื่อให้เนื้อหาของคุณทันสมัยและเหมาะกับผู้ใช้ต่างประเทศ

ดูตัวอย่างการจัดการเนื้อหาที่แปลแล้วด้วย Co-op Translator:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.th.png)

## เริ่มต้นใช้งานอย่างรวดเร็ว

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

## การตั้งค่าขั้นพื้นฐาน

- สร้างไฟล์ `.env` โดยใช้เทมเพลต: [.env.template](../../.env.template)
- ตั้งค่า LLM provider อย่างน้อยหนึ่งตัว (Azure OpenAI หรือ OpenAI)
- ถ้าต้องการแปลรูปภาพ (`-img`) ให้ตั้งค่า Azure AI Vision ด้วย
- แนะนำ: หากมีไฟล์แปลจากเครื่องมืออื่นอยู่แล้ว ควรลบออกก่อนเพื่อป้องกันปัญหา (เช่น `translations/`)
- แนะนำ: เพิ่มส่วนแปลภาษาใน README โดยใช้ [README languages template](./README_languages_template.md)
- ดูเพิ่มเติม: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

## วิธีใช้งาน

แปลทุกประเภทที่รองรับ:

```bash
translate -l "ko ja"
```

เฉพาะ Markdown:

```bash
translate -l "de" -md
```

Markdown + รูปภาพ:

```bash
translate -l "pt" -md -img
```

เฉพาะ notebooks:

```bash
translate -l "zh" -nb
```

ดูคำสั่งเพิ่มเติม: [Command reference](./getting_started/command-reference.md)

## จุดเด่น

- แปล Markdown, notebooks และรูปภาพโดยอัตโนมัติ
- ซิงค์เนื้อหาที่แปลกับต้นฉบับเมื่อมีการเปลี่ยนแปลง
- ใช้งานได้ทั้งแบบ local (CLI) และใน CI (GitHub Actions)
- รองรับ Azure OpenAI หรือ OpenAI และ Azure AI Vision สำหรับรูปภาพ (เลือกใช้)
- รักษารูปแบบและโครงสร้าง Markdown เดิม

## เอกสารประกอบ

- [คู่มือ command-line](./getting_started/command-line-guide/command-line-guide.md)
- [คู่มือ GitHub Actions (สำหรับ public repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [คู่มือ GitHub Actions (สำหรับ Microsoft organization repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [ภาษาที่รองรับ](./getting_started/supported-languages.md)
- [การแก้ไขปัญหา](./getting_started/troubleshooting.md)

## สนับสนุนเราและส่งเสริมการเรียนรู้ระดับโลก

มาร่วมเปลี่ยนแปลงการแบ่งปันเนื้อหาการศึกษาสู่ระดับโลก! กดดาว [Co-op Translator](https://github.com/azure/co-op-translator) บน GitHub และสนับสนุนภารกิจของเราในการขจัดอุปสรรคด้านภาษาในการเรียนรู้และเทคโนโลยี ความสนใจและการมีส่วนร่วมของคุณสร้างความเปลี่ยนแปลงได้จริง! ยินดีรับข้อเสนอแนะและการร่วมพัฒนาโค้ดเสมอ

### สำรวจเนื้อหาการศึกษาของ Microsoft ในภาษาของคุณ

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

## วิดีโอแนะนำ

เรียนรู้เพิ่มเติมเกี่ยวกับ Co-op Translator จากการนำเสนอของเรา _(คลิกที่ภาพด้านล่างเพื่อรับชมบน YouTube)_

- **Open at Microsoft**: แนะนำ Co-op Translator และวิธีใช้งานแบบสั้น ๆ ภายใน 18 นาที

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.th.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## การร่วมพัฒนา

โปรเจกต์นี้เปิดรับข้อเสนอแนะและการร่วมพัฒนา หากสนใจร่วมพัฒนา Azure Co-op Translator ดูรายละเอียดได้ที่ [CONTRIBUTING.md](./CONTRIBUTING.md) สำหรับแนวทางการมีส่วนร่วม

## ผู้ร่วมพัฒนา

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## จรรยาบรรณการใช้งาน

โปรเจกต์นี้ใช้ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
ดูข้อมูลเพิ่มเติมได้ที่ [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) หรือ
ติดต่อ [opencode@microsoft.com](mailto:opencode@microsoft.com) หากมีคำถามหรือข้อเสนอแนะเพิ่มเติม

## AI อย่างรับผิดชอบ

Microsoft มุ่งมั่นช่วยให้ลูกค้าใช้งาน AI อย่างรับผิดชอบ แบ่งปันประสบการณ์ และสร้างความไว้วางใจผ่านเครื่องมืออย่าง Transparency Notes และ Impact Assessments สามารถดูแหล่งข้อมูลเหล่านี้ได้ที่ [https://aka.ms/RAI](https://aka.ms/RAI)
แนวทาง AI อย่างรับผิดชอบของ Microsoft ยึดหลักความยุติธรรม ความน่าเชื่อถือและความปลอดภัย ความเป็นส่วนตัวและความปลอดภัย การมีส่วนร่วม ความโปร่งใส และความรับผิดชอบ

โมเดลขนาดใหญ่สำหรับภาษา รูปภาพ และเสียง - เช่นที่ใช้ในตัวอย่างนี้ - อาจมีพฤติกรรมที่ไม่ยุติธรรม ไม่น่าเชื่อถือ หรือไม่เหมาะสม ซึ่งอาจก่อให้เกิดผลกระทบได้ กรุณาอ่าน [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) เพื่อทราบถึงความเสี่ยงและข้อจำกัด

วิธีที่แนะนำในการลดความเสี่ยงเหล่านี้ คือการเพิ่มระบบความปลอดภัยในสถาปัตยกรรมของคุณ เพื่อช่วยตรวจจับและป้องกันพฤติกรรมที่เป็นอันตราย [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) เป็นชั้นป้องกันอิสระที่สามารถตรวจจับเนื้อหาที่เป็นอันตรายทั้งจากผู้ใช้และ AI ในแอปพลิเคชันและบริการ Azure AI Content Safety มี API สำหรับตรวจจับข้อความและรูปภาพที่เป็นอันตราย และมี Content Safety Studio สำหรับทดลองใช้งานและดูตัวอย่างโค้ดสำหรับตรวจจับเนื้อหาหลายรูปแบบ ดู [เอกสาร quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) สำหรับวิธีการใช้งานบริการนี้
อีกประเด็นหนึ่งที่ควรคำนึงถึงคือประสิทธิภาพโดยรวมของแอปพลิเคชัน สำหรับแอปพลิเคชันที่ใช้หลายโหมดและหลายโมเดล เราถือว่าประสิทธิภาพหมายถึงระบบทำงานได้ตามที่คุณและผู้ใช้คาดหวัง รวมถึงไม่สร้างผลลัพธ์ที่เป็นอันตรายด้วย การประเมินประสิทธิภาพของแอปพลิเคชันโดยรวมจึงเป็นสิ่งสำคัญ โดยสามารถใช้ [เกณฑ์คุณภาพการสร้างและตัวชี้วัดความเสี่ยงและความปลอดภัย](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)

คุณสามารถประเมินแอปพลิเคชัน AI ของคุณในสภาพแวดล้อมการพัฒนาได้โดยใช้ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ไม่ว่าจะใช้ชุดข้อมูลทดสอบหรือเป้าหมายใดก็ตาม การสร้างผลลัพธ์ของแอปพลิเคชัน AI ของคุณจะถูกวัดผลในเชิงปริมาณด้วยตัวประเมินที่มีให้ในระบบหรือจะสร้างตัวประเมินเองก็ได้ หากต้องการเริ่มต้นใช้งาน prompt flow sdk เพื่อประเมินระบบของคุณ สามารถดูได้ที่ [คู่มือเริ่มต้นใช้งาน](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) เมื่อคุณรันการประเมินแล้ว คุณสามารถ [ดูผลลัพธ์ได้ใน Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)

## เครื่องหมายการค้า

โปรเจกต์นี้อาจมีเครื่องหมายการค้าหรือโลโก้สำหรับโปรเจกต์ ผลิตภัณฑ์ หรือบริการต่าง ๆ การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft อย่างถูกต้องต้องเป็นไปตาม
[แนวทางการใช้เครื่องหมายการค้าและแบรนด์ของ Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)
การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft ในเวอร์ชันที่มีการแก้ไขของโปรเจกต์นี้ ต้องไม่ก่อให้เกิดความสับสนหรือสื่อว่า Microsoft เป็นผู้สนับสนุน
การใช้เครื่องหมายการค้าหรือโลโก้ของบุคคลที่สามใด ๆ ต้องเป็นไปตามนโยบายของเจ้าของเครื่องหมายนั้น

## ขอความช่วยเหลือ

หากคุณติดขัดหรือมีคำถามเกี่ยวกับการสร้างแอป AI เข้าร่วมได้ที่:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

หากคุณมีข้อเสนอแนะเกี่ยวกับผลิตภัณฑ์หรือพบข้อผิดพลาดขณะพัฒนา ดูได้ที่:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดขึ้นจากการใช้การแปลนี้