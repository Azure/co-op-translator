# CLI Reference

Co-op Translator ติดตั้ง entry points สำหรับบรรทัดคำสั่งดังต่อไปนี้:

- `translate`
- `evaluate`
- `migrate-links`
- `co-op-review`
- `co-op-translator-mcp`

คำสั่ง `translate`, `evaluate`, `migrate-links`, และ `co-op-review` จะถูกส่งผ่าน `co_op_translator.__main__` ซึ่งเลือกการใช้งานคำสั่งตามชื่อสคริปต์ที่ถูกเรียกใช้งาน เซิร์ฟเวอร์ MCP ใช้ `co_op_translator.mcp.server` โดยตรง

หากคุณกำลังตัดสินใจระหว่าง CLI, Python API, และ MCP ให้เริ่มจาก [Choose Your Workflow](workflows.md)

## First-Time CLI Flow

เริ่มที่นี่หากคุณกำลังใช้ Co-op Translator จากเทอร์มินัล:

1. กำหนดค่าผู้ให้บริการ LLM ตามที่อธิบายไว้ใน [Configuration](configuration.md)
2. เลือกประเภทเนื้อหาที่คุณต้องการแปล
3. เรียกคำสั่งแบบโฟกัสก่อน เช่น การแปลเฉพาะ Markdown
4. ใช้ `--dry-run` ก่อนทำการเปลี่ยนแปลงในรีโพขนาดใหญ่
5. ใช้ `co-op-review` หลังการแปลเพื่อตรวจสอบโครงสร้างและความสดใหม่

| Goal | Command to start with |
| --- | --- |
| Translate Markdown documents | `translate -l "ko" -md` |
| Translate notebooks | `translate -l "ko" -nb` |
| Translate image text | `translate -l "ko" -img` |
| Preview work without writing files | `translate -l "ko" -md --dry-run` |
| Review existing translations | `co-op-review -l "ko"` |
| Update notebook and Markdown links | `migrate-links -l "ko" --dry-run` |
| Expose tools to an MCP client | Configure the [MCP Server](mcp.md) instead of running CLI commands directly. |

## translate

แปลไฟล์ Markdown, โน้ตบุ๊ก, และข้อความในรูปภาพไปยังหนึ่งหรือหลายภาษาปลายทาง

```bash
translate -l "ko ja fr"
```

### Common examples

แปลเฉพาะ Markdown:

```bash
translate -l "de" -md
```

แปลเฉพาะโน้ตบุ๊ก:

```bash
translate -l "zh-CN" -nb
```

แปล Markdown และรูปภาพ:

```bash
translate -l "pt-BR" -md -img
```

อัปเดตการแปลที่มีอยู่โดยลบแล้วสร้างขึ้นใหม่:

```bash
translate -l "ko" -u
```

รันโดยไม่ต้องมี prompt โต้ตอบ:

```bash
translate -l "ko ja" -md -y
```

บันทึกล็อก:

```bash
translate -l "ko" -s
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | รหัสภาษาที่คั่นด้วยช่องว่าง เช่น `"es fr de"` หรือ `"all"` |
| `-r`, `--root-dir` | No | รากของโปรเจกต์ ค่าเริ่มต้นคือไดเรกทอรีปัจจุบัน |
| `-u`, `--update` | No | ลบการแปลที่มีอยู่สำหรับภาษาที่เลือกแล้วสร้างใหม่ |
| `-img`, `--images` | No | แปลเฉพาะไฟล์รูปภาพ |
| `-md`, `--markdown` | No | แปลเฉพาะไฟล์ Markdown |
| `-nb`, `--notebook` | No | แปลเฉพาะไฟล์ Jupyter notebook |
| `-d`, `--debug` | No | เปิดการบันทึกแบบดีบักในคอนโซล |
| `-s`, `--save-logs` | No | บันทึกล็อกระดับ DEBUG ไว้ที่ `<root-dir>/logs/` |
| `-x`, `--fix` | No | แปลใหม่ไฟล์ Markdown ที่มีความมั่นใจต่ำตามผลการประเมินก่อนหน้า |
| `-c`, `--min-confidence` | No | เกณฑ์ความมั่นใจสำหรับ `--fix` ค่าเริ่มต้นคือ `0.7` |
| `--add-disclaimer`, `--no-disclaimer` | No | เพิ่มหรือระงับข้อความปฏิเสธความรับผิดชอบจากการแปลด้วยเครื่อง ค่าเริ่มต้นเปิดใช้งานใน CLI |
| `-f`, `--fast` | No | โหมดรูปภาพเร็ว (เลิกใช้) |
| `-y`, `--yes` | No | ยืนยันคำถามโดยอัตโนมัติ เหมาะสำหรับ CI |
| `--repo-url` | No | URL รีโพที่ใช้ในคำแนะนำ sparse-checkout ของตารางภาษา README |
| `--migrate-language-folders` | No | เปลี่ยนชื่อโฟลเดอร์ alias เก่า เช่น `cn` หรือ `tw` เป็นโฟลเดอร์ BCP 47 มาตรฐาน |
| `--dry-run` | No | ดูตัวอย่างการย้ายโฟลเดอร์ภาษาและประมาณการการแปลโดยไม่เขียนไฟล์ |

หากไม่ระบุ flag ประเภทใดๆ, `translate` จะประมวลผล Markdown, โน้ตบุ๊ก, และรูปภาพ รูปแบบการแปลภาพต้องการการกำหนดค่า Azure AI Vision

## evaluate

ประเมินคุณภาพการแปล Markdown สำหรับภาษาหนึ่งภาษา

!!! warning "Experimental"
    `evaluate` เป็นฟีเจอร์ทดลอง มันอาจใช้การตรวจสอบคุณภาพแบบกฎและแบบ LLM เขียนผลการประเมินลงในเมตาดาต้าการแปล และโมเดลการให้คะแนนรวมถึงพฤติกรรมเมตาดาต้าอาจเปลี่ยนแปลงได้

```bash
evaluate -l "ko"
```

### Common examples

ใช้เกณฑ์ความมั่นใจต่ำเข้มงวดขึ้น:

```bash
evaluate -l "es" -c 0.8
```

รันการตรวจสอบแบบกฎเท่านั้น:

```bash
evaluate -l "fr" -f
```

รันการตรวจสอบแบบ LLM เท่านั้น:

```bash
evaluate -l "ja" -D
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | Yes | รหัสภาษาตัวเดียวที่ต้องการประเมิน รหัส alias จะถูกทำให้เป็นมาตรฐาน |
| `-r`, `--root-dir` | No | รากของโปรเจกต์ ค่าเริ่มต้นคือไดเรกทอรีปัจจุบัน |
| `-c`, `--min-confidence` | No | เกณฑ์ที่ใช้เมื่อแสดงรายการการแปลที่มีความมั่นใจต่ำ ค่าเริ่มต้นคือ `0.7` |
| `-d`, `--debug` | No | เปิดการบันทึกแบบดีบัก |
| `-s`, `--save-logs` | No | บันทึกล็อกระดับ DEBUG ไว้ที่ `<root-dir>/logs/` |
| `-f`, `--fast` | No | ประเมินแบบกฎเท่านั้น |
| `-D`, `--deep` | No | ประเมินแบบ LLM เท่านั้น |

โดยค่าเริ่มต้น `evaluate` จะใช้ทั้งการประเมินแบบกฎและแบบ LLM ผลลัพธ์จะถูกเขียนลงในเมตาดาต้าการแปลและสรุปในคอนโซล

## co-op-review

รันการตรวจสอบการบำรุงรักษาการแปลแบบกำหนดผลได้โดยไม่ต้องใช้ข้อมูลประจำตัว API

!!! note "Beta"
    `co-op-review` เป็นคำสั่งตรวจสอบในสถานะเบต้าแบบกำหนดผลได้ มันจะไม่เรียกผู้ให้บริการโมเดลหรือเขียนไฟล์ แต่การตรวจสอบและรูปแบบผลปัญหาอาจมีการเปลี่ยนแปลงได้

```bash
co-op-review -l "ko"
```

### Common examples

ตรวจสอบการแปลภาษาเกาหลีและญี่ปุ่นจากไดเรกทอรีปัจจุบัน:

```bash
co-op-review -l "ko ja"
```

ตรวจสอบรากโปรเจกต์เฉพาะ:

```bash
co-op-review -l "fr" -r ./my-course
```

ตรวจสอบเฉพาะไฟล์ต้นทางที่เปลี่ยนแปลงเทียบกับ base ref:

```bash
co-op-review -l "ko" --changed-from origin/main
```

พิมพ์ผลลัพธ์เป็น GitHub-flavored Markdown สำหรับสรุป CI:

```bash
co-op-review -l "ko ja" --changed-from origin/main --format github
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-code` | No | รหัสภาษาที่ต้องการตรวจสอบ สามารถส่งหลายครั้งหรือเป็นค่าที่คั่นด้วยช่องว่าง ค่าเริ่มต้นคือทุกภาษาการแปลที่ค้นพบ |
| `-r`, `--root-dir` | No | รากของโปรเจกต์ ค่าเริ่มต้นคือไดเรกทอรีปัจจุบัน |
| `--changed-from` | No | Git ref ที่ใช้จำกัดการตรวจสอบเฉพาะไฟล์ต้นทางที่เปลี่ยนแปลง |
| `--format` | No | รูปแบบผลลัพธ์: `text` หรือ `github` ค่าเริ่มต้นคือ `text` |

`co-op-review` ในปัจจุบันจะตรวจสอบไฟล์แปลที่หายไป, เมตาดาต้าการแปลที่หายไปหรือเก่า, ความสมบูรณ์ของ frontmatter และ code fence ใน Markdown, JSON ของโน้ตบุ๊กที่แปลไม่ถูกต้อง, และเป้าหมายลิงก์ Markdown หรือรูปภาพในเครื่องที่หายไป ลิงก์ที่หายไปจะแสดงเป็นคำเตือนโดยค่าเริ่มต้น; ปัญหาเชิงโครงสร้างและความสดใหม่จะทำให้คำสั่งล้มเหลว

## co-op-translator-mcp

รันเซิร์ฟเวอร์ Co-op Translator MCP สำหรับเอเย่นต์, บรรณาธิการ, และไคลเอนต์ที่รองรับ MCP

```bash
co-op-translator-mcp
```

การขนส่งเริ่มต้นคือ `stdio` ดูคู่มือ [MCP Server](mcp.md) สำหรับการกำหนดค่าไคลเอนต์, เครื่องมือ, ทรัพยากร, และข้อควรระวังด้านความปลอดภัย

### Options

| Option | Required | Description |
| --- | --- | --- |
| `--transport` | No | การขนส่ง MCP: `stdio`, `streamable-http`, หรือ `sse` ค่าเริ่มต้นคือ `stdio` |

## migrate-links

ประมวลผลไฟล์ Markdown ที่แปลแล้วอีกครั้งและอัปเดตลิงก์ในโน้ตบุ๊กเพื่อให้ชี้ไปยังโน้ตบุ๊กที่แปลแล้วเมื่อมีให้ใช้งาน

```bash
migrate-links -l "ko ja"
```

### Common examples

แสดงตัวอย่างการอัปเดตลิงก์:

```bash
migrate-links -l "ko" --dry-run
```

ประมวลผลทุกภาษาที่รองรับโดยไม่ต้องยืนยัน:

```bash
migrate-links -l "all" -y
```

เขียนลิงก์ใหม่เฉพาะเมื่อมีโน้ตบุ๊กที่แปลแล้วเท่านั้น:

```bash
migrate-links -l "ko" --no-fallback-to-original
```

### Options

| Option | Required | Description |
| --- | --- | --- |
| `-l`, `--language-codes` | Yes | รหัสภาษาที่คั่นด้วยช่องว่าง หรือ `"all"` |
| `-r`, `--root-dir` | No | รากของโปรเจกต์ ค่าเริ่มต้นคือไดเรกทอรีปัจจุบัน |
| `--image-dir` | No | ไดเรกทอรีรูปภาพที่แปลแล้วเทียบกับราก ค่าเริ่มต้นคือ `translated_images` |
| `--dry-run` | No | แสดงไฟล์ที่จะเปลี่ยนแปลงโดยไม่เขียนการอัปเดต |
| `--fallback-to-original`, `--no-fallback-to-original` | No | ใช้ลิงก์โน้ตบุ๊กต้นฉบับเมื่อไม่มีโน้ตบุ๊กที่แปลแล้ว ค่าเริ่มต้นเปิดใช้งาน |
| `-d`, `--debug` | No | เปิดการบันทึกแบบดีบัก |
| `-s`, `--save-logs` | No | บันทึกล็อกระดับ DEBUG ไว้ที่ `<root-dir>/logs/` |
| `-y`, `--yes` | No | ยืนยันคำถามโดยอัตโนมัติเมื่อประมวลผลทุกภาษา |

## Environment

คำสั่งทั้งหมดต้องการผู้ให้บริการ LLM อย่างน้อยหนึ่งรายการที่กำหนดค่าไว้:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# หรือ OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

การแปลภาพต้องการ Azure AI Vision เพิ่มเติม:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

## Output layout

การแปลข้อความจะถูกเขียนไว้ใต้:

```text
translations/<language-code>/<original-path>
```

ผลลัพธ์รูปภาพที่แปลแล้วจะถูกเขียนไว้ใต้:

```text
translated_images/<language-code>/<original-path>
```

ตัวอย่างเช่น การแปล `README.md` และ `docs/setup.md` เป็นภาษาเกาหลีจะได้ผลลัพธ์:

```text
translations/ko/README.md
translations/ko/docs/setup.md
```

## Copy-Paste CLI Examples

แปล Markdown เป็นสามภาษา:

```bash
translate -l "ko ja fr" -md
```

แปลเฉพาะโน้ตบุ๊ก:

```bash
translate -l "zh-CN" -nb
```

แปลเฉพาะรูปภาพ:

```bash
translate -l "pt-BR" -img
```

พรีวิวการแปล Markdown โดยไม่เขียนไฟล์:

```bash
translate -l "de es" -md --dry-run
```

แก้ไขการแปล Markdown ที่มีความมั่นใจต่ำ:

```bash
evaluate -l "ko" -c 0.8
translate -l "ko" --fix -c 0.8 -md
```

รันการแปล Markdown ที่เหมาะกับ CI:

```bash
translate -l "ko ja" -md -y -s
```

ตรวจสอบผลการแปล:

```bash
co-op-review -l "ko ja"
```

พรีวิวการย้ายลิงก์:

```bash
migrate-links -l "ko" --dry-run
```