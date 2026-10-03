# GitHub Actions

ใช้ GitHub Actions เมื่อคุณต้องการให้รีโพซิทอรีแปลเอกสารที่มีการเปลี่ยนแปลงโดยอัตโนมัติและเปิด pull request พร้อมผลลัพธ์ที่สร้างขึ้น

เริ่มจากการตั้งค่า `GITHUB_TOKEN` มาตรฐาน รวมถึงรีโพซิทอรีขององค์กรเมื่อโยบายอนุญาต ดู [GitHub App Setup](#github-app-setup) เมื่อองค์กรของคุณต้องการตัวตนของ App หรือคุณต้องการให้ workflow ด้านล่างทำงานโดยอัตโนมัติ

**Human edits:** workflow เหล่านี้จะแปลไฟล์ต้นฉบับที่เปลี่ยนแปลงใหม่ทั้งหมดและอาจเขียนทับข้อความที่มีการแก้ไขในคำแปลของพวกมัน ตรวจสอบแต่ละ PR ก่อนรวมเข้าไป การรักษาระดับบล็อกของ Markdown สำหรับการแก้ไขที่ยอมรับแล้วต้องการการผสานรวมที่กำหนดเองกับ [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)

## PR แรกของคุณสำหรับการแปล README

เริ่มจาก `README.md` หลักไฟล์เดียวและภาษาปลายทางหนึ่งภาษา Workflow นี้แปลเฉพาะ Markdown ดังนั้นไม่จำเป็นต้องใช้ Azure AI Vision

1. คัดลอก [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([ดูเทมเพลตบน GitHub](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) ไปยัง `.github/workflows/translate-readme.yml` ในรีโพซิทอรีที่คุณต้องการแปล แล้วคอมมิตไปยังสาขาเริ่มต้นของรีโพซิทอรีนั้น เทมเพลตใช้ Action หลักจาก `Azure/co-op-translator@main` ซึ่งติดตั้ง CLI จากแหล่งอ้างอิงเดียวกัน ให้ตรึงคอมมิตที่ตรวจสอบแล้วเพื่อให้การรันทำซ้ำได้
2. เปิด **Actions > Translate README > Run workflow**, เลือกภาษา และปล่อยให้ **Preview only** ถูกเลือก ตรวจสอบการประเมินโทเค็นในขั้นตอนพรีวิว พรีวิวจะไม่เรียกผู้ให้บริการโมเดล เขียนคำแปล หรือสร้าง PR
3. เพิ่มความลับสำหรับผู้ให้บริการ [ผู้ให้บริการข้อความ](#prerequisites) หนึ่งราย และเปิดใช้งาน **อนุญาตให้ GitHub Actions สร้างและอนุมัติคำขอดึง (pull requests)** ภายใต้ **การตั้งค่า > Actions > ทั่วไป** เทมเพลตขอ `contents: write` และ `pull-requests: write` สำหรับงานของมัน; คุณไม่จำเป็นต้องเปลี่ยนสิทธิ์เริ่มต้นสำหรับแต่ละเวิร์กโฟลว์ หากนโยบายขององค์กรบล็อกสิทธิ์เหล่านี้หรือการตั้งค่านี้ ให้สอบถามผู้ดูแลระบบเกี่ยวกับ [GitHub App](#github-app-setup) ที่ได้รับการอนุมัติ
4. รัน workflow อีกครั้งโดยเอาเครื่องหมายถูกที่ **Preview only** ออก มันพรีวิว แปล รัน `co-op-review --readme-only` และสร้างหรืออัปเดต PR การแปลเท่านั้นหลังจากการแปลและการตรวจสอบสำเร็จ สรุป workflow จะลิงก์ไปยัง PR
5. ตรวจสอบข้อความและการเปลี่ยนแปลงไฟล์ใน PR แล้วรวมเมื่อพร้อม Workflow จะไม่รวมอัตโนมัติ

PR จะมีเพียง `translations/<language>/README.md` และไฟล์เมตาเกี่ยวกับภาษาเท่านั้น README ต้นฉบับจะไม่ถูกเปลี่ยนแปลง และลิงก์ไปยังเอกสารอื่น ๆ ยังคงชี้ไปที่เอกสารต้นฉบับ เนื้อหาในตัว PR จะระบุไฟล์ที่เปลี่ยนแปลงและผลการตรวจสอบเชิงโครงสร้าง หากการแปลหรือการตรวจสอบล้มเหลว ให้ตรวจสอบสรุป workflow และบันทึกขั้นตอนที่ล้มเหลว; จะไม่มีการสร้าง PR หากไม่มีการเปลี่ยนแปลง จะไม่ต้องมี PR ใหม่

**Organization and CI note:** GitHub App เป็นทางเลือก ไม่ใช่ข้อบังคับของความเป็นเจ้าขององค์กร ด้วย `GITHUB_TOKEN` workflow ที่เกี่ยวกับ pull-request ในการเปิด อัปเดต หรือเปิดใหม่ PR ต้องการผู้ใช้ที่มีสิทธิ์เขียนเพื่อเลือก **Approve workflows to run** Workflow แบบ push จะไม่ถูกทริกเกอร์โดยโทเค็นนี้ สำหรับ CI ด้านล่างที่ไม่ต้องดูแล ให้ดู [GitHub App Setup](#github-app-setup) และ [workflow triggering rules](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow) ของ GitHub

## Prerequisites

ก่อนสร้าง workflow ให้กำหนดค่าความลับของบริการ AI ที่การรันการแปลของคุณต้องใช้

การแปลข้อความต้องการผู้ให้บริการโมเดลภาษาหนึ่งราย:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, plus optional `OPENAI_ORG_ID` and `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, plus optional `ANTHROPIC_BASE_URL`

การแปลภาพต้องการ Azure AI Vision เพิ่มเติม:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

ดู [Configuration](configuration.md) และ [Azure AI Setup](azure-ai-setup.md) สำหรับรายละเอียดการกำหนดค่าท้องถิ่น

## การตั้งค่ามาตรฐาน

หลังจากทดลอง workflow สำหรับ README แล้ว ให้ใช้การตั้งค่านี้เพื่อแปลไฟล์ Markdown ของรีโพซิทอรีเป็นหลายภาษา มันรันการตรวจสอบ Markdown ก่อนเปิด PR และไม่จำเป็นต้องใช้ Azure AI Vision

### ขั้นตอนที่ 1: เพิ่มความลับของที่เก็บ

ในรีโพซิทอรีเป้าหมายของคุณ เปิด **Settings** > **Secrets and variables** > **Actions**, แล้วเพิ่มความลับของผู้ให้บริการที่ workflow ของคุณจะใช้

![เลือกความลับของ Actions](../../assets/github-actions/select-setting-action.png)

### ขั้นตอนที่ 2: เปิดสิทธิ์ของ Workflow

เปิด **Settings** > **Actions** > **General**

ภายใต้ **Workflow permissions**:

1. เปิดใช้งาน **อนุญาตให้ GitHub Actions สร้างและอนุมัติคำขอดึง (pull requests)**
2. บันทึกการตั้งค่า

งานด้านล่างร้องขอ `contents: write` และ `pull-requests: write` อย่างชัดเจน รักษาสิทธิ์เริ่มต้นของรีโพซิทอรีสำหรับ workflow ให้ไม่เปลี่ยน หากนโยบายขององค์กรบล็อกการสร้าง PR ให้สอบถามผู้ดูแลระบบเกี่ยวกับ [GitHub App](#github-app-setup) ที่ได้รับการอนุมัติ

### ขั้นตอนที่ 3: เพิ่มเวิร์กโฟลว์

สร้าง `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

เปลี่ยน `TARGET_LANGUAGES` เป็นภาษาที่โครงการของคุณต้องการ การตรวจสอบใช้ Python API เพื่อตรวจสอบเฉพาะ Markdown ซึ่งตรงกับขั้นตอนการแปล ข้อผิดพลาดในการแปลหรือการตรวจสอบจะหยุดงานก่อนการสร้าง PR Workflow จะไม่รวม PR อัตโนมัติ สำหรับรีโพซิทอรีขนาดใหญ่ ให้เพิ่มตัวกรอง `paths:` ภายใต้ `on.push` เพื่อให้ workflow ทำงานเฉพาะเมื่อเอกสารมีการเปลี่ยนแปลง

### ไม่บังคับ: โน้ตบุ๊กและรูปภาพ

สำหรับ notebooks ให้เพิ่ม `-nb` ในคำสั่งแปลและตั้ง `notebook=True` ในขั้นตอนการตรวจสอบ สำหรับข้อความในภาพ ให้กำหนดค่าความลับสองตัวของ [Azure AI Vision](#prerequisites) ส่งพวกมันใน `env` ของขั้นตอนการแปล เพิ่ม `-img` ในคำสั่ง และเพิ่ม `translated_images/` ใน `add-paths` ของขั้นตอน PR ตรวจสอบภาพที่แปลด้วยสายตา; การตรวจสอบแบบกำหนดได้ไม่รับรองข้อความในภาพหรือความถูกต้องทางภาษา

## การตั้งค่า GitHub App

ใช้ GitHub App ที่ได้รับอนุมัติเมื่อองค์กรของคุณต้องการตัวตนของ App หรือเมื่อต้องการให้ PR ที่สร้างขึ้นไปทริกเกอร์ CI ด้านล่างโดยไม่ต้องมีขั้นตอนการอนุมัติ `GITHUB_TOKEN` App จะไม่ละเว้นนโยบายขององค์กร ผู้ดูแลระบบยังคงควบคุมการติดตั้งและสิทธิ์ของมัน

### ขั้นตอนที่ 1: สร้างหรือติดตั้ง GitHub App

ใช้ App ที่องค์กรจัดเตรียมไว้เมื่อมีให้ใช้งาน หรือสร้าง App ใหม่ที่มีสิทธิ์อ่าน/เขียนสำหรับ **Contents** และ **Pull requests** ติดตั้งบนรีโพซิทอรีเป้าหมายพร้อมการอนุมัติที่จำเป็นขององค์กร

บันทึก:

- App ID
- Private key contents

เก็บไว้เป็นความลับของรีโพซิทอรี:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### ขั้นตอนที่ 2: สร้างโทเค็นของแอป

เพิ่มขั้นตอนนี้ก่อนขั้นตอน pull request ที่มีอยู่ทันที สำหรับเทมเพลต README ให้ใช้เงื่อนไขความสำเร็จเดียวกันเพื่อให้พรีวิวและการแปลที่ล้มเหลวไม่ขอโทเค็นของ App:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

แล้วเปลี่ยนเพียง `token` input ของขั้นตอน pull request ที่มีอยู่เป็น `${{ steps.generate_token.outputs.token }}` รักษาเงื่อนไขความสำเร็จ สาขา เนื้อหา PR และ `add-paths` ไว้ตามเดิม โทเค็นจะถูกจำกัดขอบเขตไปยังรีโพซิทอรีปัจจุบันตามค่าเริ่มต้น เมื่อปรับใช้การตั้งค่ามาตรฐานแทนเทมเพลต README ให้ละ `if` ข้างต้น: workflow นั้นใช้เงื่อนไขความสำเร็จเริ่มต้น ดังนั้นการสร้างโทเค็นและการสร้าง PR จะทำเฉพาะหลังจากการแปลและการตรวจสอบสำเร็จเท่านั้น

ดู [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) อย่างเป็นทางการสำหรับการติดตั้งและสิทธิ์ของโทเค็น

## ข้อจำกัดของ Runner

GitHub-hosted runners มีระยะเวลาสูงสุดของงาน รีโพซิทอรีขนาดใหญ่หรือหลายภาษาปลายทางอาจเกินขีดจำกัดนั้นได้

สำหรับงานแปลขนาดใหญ่:

- แปลให้น้อยภาษาต่อการรันหนึ่งครั้ง
- ใช้แฟลกเนื้อหา เช่น `-md`, `-nb`, หรือ `-img`
- ใช้ runner ที่โฮสต์เองเมื่อขนาดรีโพซิทอรีหรือความหน่วงของโมเดลทำให้ runner ที่โฮสต์ไม่เสถียร

## ตรวจทานใน CI

ใช้ `co-op-review` เมื่อ pull request ควรตรวจสอบคำแปลที่สร้างขึ้นโดยไม่เรียก LLM หรือผู้ให้บริการ Vision

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` เป็นคำสั่งการตรวจสอบแบบกำหนดได้รุ่นเบต้า การตรวจสอบและสกีมาผลลัพธ์ของมันอาจพัฒนาไป แต่ถูกออกแบบให้ปลอดภัยสำหรับ CI เพราะมันไม่เขียนไฟล์หรือเรียกผู้ให้บริการโมเดล
