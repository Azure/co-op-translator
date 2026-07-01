# Co-op Translator

_ทำให้การแปลเนื้อหาเพื่อการศึกษาใน GitHub เป็นไปโดยอัตโนมัติและรักษาให้อัปเดตข้ามหลายภาษาได้อย่างง่ายดาย เมื่อโปรเจกต์ของคุณพัฒนาไป_

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![แพ็กเกจ Python](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![สิทธิ์ใช้งาน: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![การดาวน์โหลด](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![การดาวน์โหลด](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![คอนเทนเนอร์: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![รูปแบบโค้ด: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![ผู้ร่วมพัฒนา GitHub](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![ปัญหา GitHub](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![คำขอดึง GitHub](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![ยินดีรับ PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**เริ่มที่นี่:** [เลือกเวิร์กโฟลว์ของคุณ](https://azure.github.io/co-op-translator/workflows/) | [การกำหนดค่า](https://azure.github.io/co-op-translator/configuration/) | [CLI](https://azure.github.io/co-op-translator/cli/) | [Python API](https://azure.github.io/co-op-translator/api/) | [MCP Server](https://azure.github.io/co-op-translator/mcp/)

### 🌐 รองรับหลายภาษา

#### ได้รับการสนับสนุนโดย [Co-op Translator](https://github.com/Azure/co-op-translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[อาหรับ](../ar/README.md) | [เบงกาลี](../bn/README.md) | [บัลแกเรีย](../bg/README.md) | [พม่า (เมียนมาร์)](../my/README.md) | [จีน (ตัวย่อ)](../zh-CN/README.md) | [จีน (ตัวเต็ม, ฮ่องกง)](../zh-HK/README.md) | [จีน (ตัวเต็ม, มาเก๊า)](../zh-MO/README.md) | [จีน (ตัวเต็ม, ไต้หวัน)](../zh-TW/README.md) | [โครเอเชีย](../hr/README.md) | [เช็ก](../cs/README.md) | [เดนมาร์ก](../da/README.md) | [ดัตช์](../nl/README.md) | [เอสโตเนีย](../et/README.md) | [ฟินแลนด์](../fi/README.md) | [ฝรั่งเศส](../fr/README.md) | [เยอรมัน](../de/README.md) | [กรีก](../el/README.md) | [ฮีบรู](../he/README.md) | [ฮินดี](../hi/README.md) | [ฮังการี](../hu/README.md) | [อินโดนีเซีย](../id/README.md) | [อิตาลี](../it/README.md) | [ญี่ปุ่น](../ja/README.md) | [กันนาดา](../kn/README.md) | [เขมร](../km/README.md) | [เกาหลี](../ko/README.md) | [ลิทัวเนีย](../lt/README.md) | [มาเลย์](../ms/README.md) | [มาลายาลัม](../ml/README.md) | [มราฐี](../mr/README.md) | [เนปาล](../ne/README.md) | [ไนจีเรีย พิดจิน](../pcm/README.md) | [นอร์เวย์](../no/README.md) | [เปอร์เซีย (ฟาร์ซี)](../fa/README.md) | [โปแลนด์](../pl/README.md) | [โปรตุเกส (บราซิล)](../pt-BR/README.md) | [โปรตุเกส (โปรตุเกส)](../pt-PT/README.md) | [ปัญจาบี (กุรมุกี)](../pa/README.md) | [โรมาเนีย](../ro/README.md) | [รัสเซีย](../ru/README.md) | [เซอร์เบีย (คีริลลิก)](../sr/README.md) | [สโลวัก](../sk/README.md) | [สโลวีเนีย](../sl/README.md) | [สเปน](../es/README.md) | [สวาฮิลี](../sw/README.md) | [สวีเดน](../sv/README.md) | [ทากาล็อก (ฟิลิปปินส์)](../tl/README.md) | [ทมิฬ](../ta/README.md) | [เทลูกู](../te/README.md) | [ไทย](./README.md) | [ตุรกี](../tr/README.md) | [ยูเครน](../uk/README.md) | [อูรดู](../ur/README.md) | [เวียดนาม](../vi/README.md)

> **ต้องการโคลนไว้ในเครื่องหรือไม่?**
>
> ที่เก็บนี้มีการแปลมากกว่า 50 ภาษา ซึ่งทำให้ขนาดการดาวน์โหลดเพิ่มขึ้นอย่างมาก หากต้องการโคลนโดยไม่รวมการแปล ให้ใช้ sparse checkout:
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
> สิ่งนี้จะให้ทุกสิ่งที่คุณต้องการเพื่อทำคอร์สให้เสร็จโดยการดาวน์โหลดที่รวดเร็วขึ้นมาก
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![ผู้เฝ้าดู GitHub](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![Forks GitHub](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![ดาว GitHub](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ภาพรวม

**Co-op Translator** ช่วยให้คุณแปลเนื้อหาเพื่อการศึกษาบน GitHub เป็นหลายภาษาได้อย่างง่ายดาย
เมื่อคุณอัปเดตไฟล์ Markdown รูปภาพ หรือโน้ตบุ๊ก การแปลจะถูกซิงค์โดยอัตโนมัติ เพื่อให้แน่ใจว่าเนื้อหาของคุณถูกต้องและทันสมัยสำหรับผู้เรียนทั่วโลก

ใช้จาก CLI เพื่อแปลรีโปซิทอรี จาก Python API เพื่อการอัตโนมัติ หรือผ่าน MCP server สำหรับเวิร์กโฟลว์ของเอเจนต์และบรรณาธิการ

ตัวอย่างการจัดระเบียบเนื้อหาที่แปลแล้ว:

![ตัวอย่าง](../../imgs/translation-ex.png)

## ทำไมต้องใช้ Co-op Translator?

การแปลไฟล์เดียวทำได้ง่าย การรักษารีโปซิทอรีเอกสารทั้งหมด
ให้แปล เชื่อมโยง และทันสมัยเป็นเรื่องยาก

| ปัญหา | Co-op Translator ช่วยอย่างไร |
| --- | --- |
| เอกสารยาวไม่ใช่ prompt เดียว | ไฟล์ Markdown ขนาดใหญ่ถูกแบ่งเป็นชิ้น ทำให้ README ขนาดยาวไม่ขึ้นอยู่กับการตอบของโมเดลเพียงครั้งเดียวที่เปราะบาง หากชิ้นใดล้มเหลว Co-op Translator สามารถลองใหม่และแบ่งชิ้นเฉพาะส่วนที่ล้มเหลวได้ |
| การแปลที่ไม่สมบูรณ์ไม่ควรถูกทำเครื่องหมายว่าสมบูรณ์ | การแปลที่ถูกตัดทอนไม่ควรถูกทำเป็นอัปเดตล่าสุด Co-op Translator ตรวจสอบความสมบูรณ์ของการแปลก่อนบันทึกและสามารถตรวจจับการแปลที่โครงสร้างไม่สมบูรณ์ที่มีอยู่ได้ |
| ลิงก์ควรตรงกับโครงสร้างรีโปที่แปลแล้ว | การแปลด้วยมือมักจะทำให้ลิงก์สัมพัทธ์ชี้กลับไปยังต้นทาง Co-op Translator เขียน Markdown โน้ตบุ๊ก รูปภาพ และลิงก์ README ใหม่ให้ตรงกับโครงสร้าง `translations/<lang>/...` |
| การแปลควรทำงานทั่วทั้งรีโป | Co-op Translator จัดการไฟล์ README เอกสาร โน้ตบุ๊ก และข้อความในรูปภาพเป็นส่วนหนึ่งของเวิร์กโฟลว์รีโปเดียว แทนการแปลไฟล์ทีละไฟล์ |
| การรักษาการแปลมีความสำคัญกว่าการสร้างครั้งเดียว | แฮชต้นทางและเมตาดาต้าการแปลช่วยให้ Co-op Translator พบไฟล์ที่ล้าสมัย ข้ามไฟล์ที่ไม่เปลี่ยนแปลง และรักษาการซิงค์เนื้อหาที่แปลเมื่อรีโปต้นทางวิวัฒนาการ |

## วิธีการจัดการสถานะการแปล

Co-op Translator จัดการเนื้อหาที่แปลเป็นรูปแบบของ **อาร์ติแฟกต์ซอฟต์แวร์ที่มีเวอร์ชัน**,  
ไม่ใช่เป็นไฟล์นิ่ง

เครื่องมือติดตามสถานะของ Markdown รูปภาพ และโน้ตบุ๊กที่แปล
โดยใช้ **เมตาดาต้าที่มีขอบเขตตามภาษา**

การออกแบบนี้ช่วยให้ Co-op Translator:

- ตรวจจับการแปลที่ล้าสมัยได้อย่างเชื่อถือได้
- จัดการ Markdown รูปภาพ และโน้ตบุ๊กอย่างสอดคล้องกัน
- ขยายขนาดได้อย่างปลอดภัยในรีโปหลายภาษา ขนาดใหญ่ และเคลื่อนที่เร็ว

โดยการจำลองการแปลเป็นอาร์ติแฟกต์ที่ถูกจัดการ,
เวิร์กโฟลว์การแปลจึงสอดคล้องตามธรรมชาติกับการจัดการ
การพึ่งพาและอาร์ติแฟกต์ของซอฟต์แวร์สมัยใหม่

→ [วิธีการจัดการสถานะการแปล](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

### การเจาะลึกที่เกี่ยวข้อง

- [การแก้ไข Markdown เสียหายในงานแปลด้วย AI: การเสริมความแข็งแกร่งให้กับพาร์ไพล์ในสภาพแวดล้อมการผลิต](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/fixing-broken-markdown-in-ai-translation-hardening-a-production-pipeline/4511378)

## เริ่มต้น

Co-op Translator สามารถใช้งานได้จาก CLI, Python API, หรือ MCP server เริ่มด้วยคำแนะนำเวิร์กโฟลว์หากคุณกำลังเลือกระหว่างการแปลในเครื่อง การอัตโนมัติ CI และการรวมเอเจนต์/บรรณาธิการ

- [เลือกเวิร์กโฟลว์ของคุณ](../../docs/workflows.md)
- [กำหนดค่าข้อมูลรับรอง](../../docs/configuration.md)
- [แปลจาก CLI](../../docs/cli.md)
- [อัตโนมัติโดยใช้ Python API](../../docs/api.md)
- [เชื่อมต่อกับ MCP Server](../../docs/mcp.md)
- [เรียกใช้ใน GitHub Actions](../../docs/github-actions.md)

ตัวอย่าง CLI ขั้นพื้นฐานหลังจากการกำหนดค่า:

```bash
python -m venv .venv
# วินโดวส์
.venv\Scripts\activate
# แมคโอเอส/ลินุกซ์
source .venv/bin/activate

pip install co-op-translator
translate -l "ko" -md
co-op-review -l "ko"
```

สำหรับการรันครั้งแรกบนรีโปขนาดใหญ่ ให้ใช้ `--dry-run` ก่อนเขียนไฟล์ที่แปลแล้ว ดู [เอกสารอ้างอิง CLI](../../docs/cli.md) สำหรับธงชนิดเนื้อหา บันทึก การตรวจทาน และการย้ายลิงก์

การรันคอนเทนเนอร์อย่างรวดเร็วด้วย Bash/Zsh:

```bash
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

การรันคอนเทนเนอร์อย่างรวดเร็วด้วย PowerShell:

```powershell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "ko" -md
```

## คุณสมบัติ

- แปลอัตโนมัติสำหรับ Markdown โน้ตบุ๊ก และรูปภาพ
- รักษาการแปลให้ซิงค์กับการเปลี่ยนแปลงของต้นทาง
- ทำงานได้ในเครื่อง (CLI) หรือใน CI (GitHub Actions)
- เปิดเผยเครื่องมือการแปล Markdown โน้ตบุ๊ก รูปภาพ การตรวจทาน และโครงการผ่าน MCP
- ใช้ Azure OpenAI หรือ OpenAI สำหรับการแปลที่มีผู้ให้บริการสนับสนุน
- ให้ MCP โฮสต์เอเจนต์เพื่อแปลชิ้น Markdown และโน้ตบุ๊กโดยไม่ต้องมีข้อมูลรับรอง LLM ของ Co-op Translator
- ใช้ Azure AI Vision สำหรับการสกัดข้อความจากรูปภาพและการแปล
- ตรวจทานโครงสร้างการแปลและความสดใหม่ด้วยการตรวจสอบแบบกำหนดได้
- รักษารูปแบบและโครงสร้างของ Markdown

## เอกสาร

- [เว็บไซต์เอกสาร](https://azure.github.io/co-op-translator/)
- [เลือกเวิร์กโฟลว์ของคุณ](../../docs/workflows.md)
- [การกำหนดค่า](../../docs/configuration.md)
- [การตั้งค่า Azure AI](../../docs/azure-ai-setup.md)
- [เอกสารอ้างอิง CLI](../../docs/cli.md)
- [Python API](../../docs/api.md)
- [MCP Server](../../docs/mcp.md)
- [GitHub Actions](../../docs/github-actions.md)
- [เทมเพลตภาษาของ README](../../docs/readme-languages-template.md)
- [ภาษาที่รองรับ](../../docs/supported-languages.md)
- [การมีส่วนร่วม](../../CONTRIBUTING.md)
- [การแก้ปัญหา](../../docs/troubleshooting.md)

### คู่มือเฉพาะของไมโครซอฟท์
> [!NOTE]
> สำหรับผู้ดูแลรีโป “For Beginners” ของ Microsoft เท่านั้น

- [การอัพเดตรายการ “คอร์สอื่น ๆ” (สำหรับรีโปผู้เริ่มต้นของ MS เท่านั้น)](../../docs/microsoft-beginners.md)

## สนับสนุนเราและส่งเสริมการเรียนรู้ระดับโลก

เข้าร่วมกับเราในการปฏิวัติวิธีการแบ่งปันเนื้อหาการศึกษาในระดับโลก! ให้ดาว [Co-op Translator](https://github.com/azure/co-op-translator) บน GitHub และสนับสนุนภารกิจของเราในการลดอุปสรรคด้านภาษาในการเรียนรู้และเทคโนโลยี ความสนใจและการมีส่วนร่วมของคุณสร้างผลกระทบอย่างมาก! ยินดีรับการเสนอรหัสและแนวคิดฟีเจอร์เสมอ

### สำรวจเนื้อหาการศึกษาของไมโครซอฟท์ในภาษาของคุณ
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

## Video presentations

👉 คลิกที่รูปด้านล่างเพื่อชมบน YouTube

- **Open at Microsoft**: คำแนะนำสั้น ๆ ประมาณ 18 นาที และคู่มือฉบับย่อเกี่ยวกับวิธีการใช้ Co-op Translator

  [![เปิดที่ Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contributing

โปรเจกต์นี้ยินดีรับการมีส่วนร่วมและข้อเสนอแนะ หากคุณสนใจจะมีส่วนร่วมกับ Azure Co-op Translator โปรดดู [CONTRIBUTING.md](../../CONTRIBUTING.md) สำหรับแนวทางเกี่ยวกับวิธีที่คุณสามารถช่วยให้ Co-op Translator ใช้งานได้ง่ายขึ้น

## Contributors

[![ผู้ร่วมพัฒนา co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

โปรเจกต์นี้ได้ยอมรับ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
สำหรับข้อมูลเพิ่มเติม กรุณาดู [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) หรือ
ติดต่อ [opencode@microsoft.com](mailto:opencode@microsoft.com) หากมีคำถามหรือความคิดเห็นเพิ่มเติม

## Responsible AI

Microsoft มุ่งมั่นที่จะช่วยลูกค้าใช้ผลิตภัณฑ์ AI ของเราอย่างรับผิดชอบ แบ่งปันบทเรียน และสร้างความร่วมมือที่มีพื้นฐานจากความไว้วางใจผ่านเครื่องมือต่าง ๆ เช่น Transparency Notes และ Impact Assessments แหล่งข้อมูลจำนวนมากสามารถพบได้ที่ [https://aka.ms/RAI](https://aka.ms/RAI).
แนวทางของ Microsoft สำหรับ AI ที่มีความรับผิดชอบตั้งอยู่บนหลักการด้าน AI ของเราคือ ความเป็นธรรม, ความน่าเชื่อถือและความปลอดภัย, ความเป็นส่วนตัวและความมั่นคง, ความครอบคลุม, ความโปร่งใส และความรับผิดชอบ

โมเดลภาษาขนาดใหญ่, ภาพ และเสียง — เช่นโมเดลที่ใช้ในตัวอย่างนี้ — อาจมีพฤติกรรมที่ไม่เป็นธรรม, ไม่เชื่อถือได้, หรือหยาบคาย ส่งผลให้เกิดความเสียหายได้ กรุณาอ่าน [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) เพื่อทราบเกี่ยวกับความเสี่ยงและข้อจำกัด

แนวทางที่แนะนำเพื่อลดความเสี่ยงเหล่านี้คือการรวมระบบความปลอดภัยไว้ในสถาปัตยกรรมของคุณที่สามารถตรวจจับและป้องกันพฤติกรรมที่เป็นอันตรายได้ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ให้เลเยอร์ป้องกันอิสระที่สามารถตรวจจับเนื้อหาที่เป็นอันตรายซึ่งสร้างโดยผู้ใช้และที่สร้างโดย AI ในแอปพลิเคชันและบริการ Azure AI Content Safety มี API สำหรับข้อความและภาพที่ช่วยให้คุณตรวจจับเนื้อหาที่เป็นอันตราย เรายังมี Content Safety Studio แบบโต้ตอบที่ช่วยให้คุณดู สำรวจ และทดลองโค้ดตัวอย่างเพื่อการตรวจจับเนื้อหาที่เป็นอันตรายข้ามรูปแบบต่าง ๆ เอกสาร [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ต่อไปนี้จะแนะนำวิธีการส่งคำร้องขอไปยังบริการ

อีกประเด็นหนึ่งที่ต้องพิจารณาคือประสิทธิภาพโดยรวมของแอปพลิเคชัน สำหรับแอปพลิเคชันที่มีหลายรูปแบบและหลายโมเดล เราถือว่าประสิทธิภาพหมายถึงระบบทำงานตามที่คุณและผู้ใช้ของคุณคาดหวัง รวมถึงการไม่สร้างผลลัพธ์ที่เป็นอันตราย จึงสำคัญที่ต้องประเมินประสิทธิภาพของแอปพลิเคชันโดยรวมของคุณโดยใช้ [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)

คุณสามารถประเมินแอป AI ของคุณในสภาพแวดล้อมการพัฒนาด้วย [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) โดยให้ชุดข้อมูลทดสอบหรือเป้าหมาย การสร้างของแอป Generative AI ของคุณจะถูกวัดเชิงปริมาณด้วยตัวประเมินที่มีอยู่แล้วหรือผู้ประเมินแบบกำหนดเองที่คุณเลือก เพื่อเริ่มต้นกับ prompt flow sdk ในการประเมินระบบของคุณ คุณสามารถทำตาม [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) เมื่อคุณดำเนินการรันการประเมินแล้ว คุณสามารถ [แสดงผลลัพธ์ใน Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)

## Trademarks

โปรเจกต์นี้อาจมีเครื่องหมายการค้า หรือตราสินค้าสำหรับโปรเจกต์ ผลิตภัณฑ์ หรือบริการ การใช้เครื่องหมายการค้าหรือตราสินค้าของ Microsoft ที่ได้รับอนุญาตต้องเป็นไปตามและปฏิบัติตาม
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
การใช้เครื่องหมายการค้าหรือตราสินค้าของ Microsoft ในเวอร์ชันที่แก้ไขของโปรเจกต์นี้ต้องไม่ทำให้เกิดความสับสนหรือบ่งชี้ว่าได้รับการสนับสนุนจาก Microsoft
การใช้เครื่องหมายการค้าหรือตราสินค้าของบุคคลที่สามต้องเป็นไปตามนโยบายของบุคคลที่สามเหล่านั้น

## Getting Help

หากคุณติดขัดหรือมีคำถามเกี่ยวกับการสร้างแอป AI เข้าร่วมได้ที่:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

หากคุณมีคำติชมเกี่ยวกับผลิตภัณฑ์หรือพบข้อผิดพลาดขณะพัฒนา เยี่ยมชม:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)