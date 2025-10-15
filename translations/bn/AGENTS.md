<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-15T04:24:06+00:00",
  "source_file": "AGENTS.md",
  "language_code": "bn"
}
-->
## প্রকল্পের সংক্ষিপ্ত বিবরণ

Co‑op Translator একটি পাইথন কমান্ড‑লাইন টুল এবং GitHub Actions ওয়ার্কফ্লো, যা Markdown ফাইল, Jupyter নোটবুক এবং ছবির টেক্সট একাধিক ভাষায় অনুবাদ করে। এটি আউটপুটগুলো ভাষাভিত্তিক ফোল্ডারে সাজিয়ে রাখে এবং সোর্স কনটেন্টের সাথে অনুবাদগুলো সমন্বিত রাখে। প্রকল্পটি Poetry‑পরিচালিত লাইব্রেরি হিসেবে গঠিত, CLI এন্ট্রি পয়েন্টসহ।

### স্থাপত্যের সংক্ষিপ্ত বিবরণ

- CLI এন্ট্রি পয়েন্ট (`translate`, `migrate-links`, `evaluate`) একটি একীভূত CLI-তে আহ্বান করে, যা অনুবাদ, লিংক মাইগ্রেশন এবং মূল্যায়ন প্রবাহে পাঠায়।
- কনফিগারেশন লোডার `.env` পড়ে এবং LLM প্রদানকারী (Azure OpenAI বা OpenAI) স্বয়ংক্রিয়ভাবে শনাক্ত করে, এবং অনুরোধ করলে ভিশন প্রদানকারী (Azure AI Service) ছবির টেক্সট বের করার জন্য।
- অনুবাদ কোর Markdown এবং নোটবুক পরিচালনা করে; ভিশন পাইপলাইন ছবির টেক্সট বের করে যখন `-img` ব্যবহার করা হয়।
- আউটপুটগুলো `translations/<lang>/`-এ টেক্সটের জন্য এবং `translated_images/`-এ ছবির জন্য সাজানো হয়, মূল কাঠামো বজায় রেখে।

### মূল প্রযুক্তি ও ফ্রেমওয়ার্ক

- Python 3.10–3.12, Poetry প্যাকেজিংয়ের জন্য
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP ও ডেটা: `httpx`, `pydantic`
- ইমেজিং: `pillow`, `opencv-python`, `matplotlib`
- টুলিং: `pytest`, `black`, `ruff`

## সেটআপ কমান্ড

### পূর্বশর্ত

- Python 3.10–3.12
- Azure সাবস্ক্রিপশন (ঐচ্ছিক, Azure AI সার্ভিসের জন্য)
- LLM/Vision API-র জন্য ইন্টারনেট সংযোগ (যেমন Azure OpenAI/OpenAI, Azure AI Vision)

### অপশন A: Poetry (সুপারিশকৃত)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### অপশন B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## শেষ ব্যবহারকারীর জন্য ব্যবহার

### Docker (প্রকাশিত ইমেজ)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

নোট:
- ডিফল্ট এন্ট্রি পয়েন্ট `translate`; লিংক মাইগ্রেশনের জন্য `--entrypoint migrate-links` দিয়ে ওভাররাইড করুন।
- GHCR প্যাকেজের ভিজিবিলিটি Public রাখুন যাতে অ্যানোনিমাস পুল সম্ভব হয়।

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### পরিবেশ কনফিগারেশন

রিপোজিটরির রুটে একটি `.env` ফাইল তৈরি করুন এবং আপনার নির্বাচিত ভাষার মডেল ও (ঐচ্ছিক) ভিশন সার্ভিসের জন্য ক্রেডেনশিয়াল/এন্ডপয়েন্ট দিন। প্রদানকারীভিত্তিক সেটআপের জন্য দেখুন `getting_started/set-up-azure-ai.md`।

### প্রয়োজনীয় পরিবেশ ভেরিয়েবল

কমপক্ষে একটি LLM প্রদানকারী কনফিগার করতে হবে। ছবির অনুবাদের জন্য Azure AI Service-ও কনফিগার করতে হবে।

- Azure OpenAI (টেক্সট অনুবাদ):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (টেক্সট অনুবাদের বিকল্প):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (ঐচ্ছিক)
  - `OPENAI_CHAT_MODEL_ID` (OpenAI প্রদানকারী ব্যবহার করলে আবশ্যক)
  - `OPENAI_BASE_URL` (ঐচ্ছিক; ডিফল্ট `https://api.openai.com/v1`)

- ছবির টেক্সট বের করার জন্য Azure AI Service ( `-img` ব্যবহার করলে আবশ্যক):
  - `AZURE_AI_SERVICE_API_KEY` (প্রেফার্ড) অথবা পুরনো `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

উদাহরণ `.env` স্নিপেট:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

নোট:

- টুলটি উপলব্ধ LLM প্রদানকারী স্বয়ংক্রিয়ভাবে শনাক্ত করে; Azure OpenAI বা OpenAI যেকোনো একটি কনফিগার করুন।
- ছবির অনুবাদের জন্য `AZURE_AI_SERVICE_API_KEY` এবং `AZURE_AI_SERVICE_ENDPOINT` দুটোই লাগবে।
- প্রয়োজনীয় ভেরিয়েবল না থাকলে CLI স্পষ্ট ত্রুটি দেখাবে।

## ডেভেলপমেন্ট ওয়ার্কফ্লো

- সোর্স কোড `src/co_op_translator`-এ, টেস্ট `tests/`-এ।
- প্রধান CLI-গুলো (এন্ট্রি পয়েন্ট দিয়ে ইনস্টল):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

আরও ব্যবহারবিধি দেখুন `getting_started/`-এ।

## টেস্টিং নির্দেশনা

রিপোজিটরির রুট থেকে টেস্ট চালান। কিছু টেস্ট API ক্রেডেনশিয়াল চাইতে পারে; প্রয়োজনে সেগুলো বাদ দিন।

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

ঐচ্ছিক কাভারেজ ( `coverage` লাগবে):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## কোড স্টাইল নির্দেশিকা

- ফরম্যাটার: Black (`pyproject.toml`-এ কনফিগার, লাইন দৈর্ঘ্য ৮৮)
- লিন্টার: Ruff (`pyproject.toml`-এ কনফিগার, লাইন দৈর্ঘ্য ১২০)
- টাইপ চেক: mypy (কনফিগারেশন আছে; ইনস্টল থাকলে চালু করুন)

কমান্ডসমূহ:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Python সোর্স `src/`-এ, টেস্ট `tests/`-এ রাখুন, এবং প্যাকেজ নেমস্পেস (`co_op_translator.*`) দিয়ে স্পষ্ট ইম্পোর্ট পছন্দ করুন।

## বিল্ড ও ডিপ্লয়মেন্ট

বিল্ড আর্টিফ্যাক্ট `dist/`-এ প্রকাশিত হয়।

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

GitHub Actions দিয়ে অটোমেশন সমর্থিত; দেখুন:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### কন্টেইনার ইমেজ (GHCR)

- অফিসিয়াল ইমেজ: `ghcr.io/azure/co-op-translator:<tag>`
- ট্যাগ: `latest` (main-এ), সেমান্টিক ট্যাগ যেমন `vX.Y.Z`, এবং `sha` ট্যাগ
- মাল্টি-আর্ক: `linux/amd64, linux/arm64` Buildx দিয়ে সমর্থিত
- Dockerfile প্যাটার্ন: বিল্ড ডিপেন্ডেন্সি হুইল বিল্ডারে ( `build-essential` ও `python3-dev` সহ) এবং রানটাইমে লোকাল হুইলহাউস থেকে ইনস্টল (`pip install --no-index --find-links=/wheels`)
- ওয়ার্কফ্লো: `.github/workflows/docker-publish.yml` GHCR-এ বিল্ড ও পুশ করে

## নিরাপত্তা বিবেচনা

- API কী ও এন্ডপয়েন্ট `.env` বা CI সিক্রেট স্টোরে রাখুন; কখনো সিক্রেট কমিট করবেন না।
- ছবির অনুবাদের জন্য Azure AI Vision কী/এন্ডপয়েন্ট লাগবে; না হলে `-img` বাদ দিন।
- বড় অনুবাদ ব্যাচ চালানোর সময় প্রদানকারীর কোটাস/রেট লিমিট যাচাই করুন।

## পুল রিকোয়েস্ট নির্দেশিকা

### জমা দেওয়ার আগে

1. **আপনার পরিবর্তন টেস্ট করুন:**
   - সংশ্লিষ্ট নোটবুক সম্পূর্ণ চালান
   - সব সেল কোনো ত্রুটি ছাড়া এক্সিকিউট হয় কিনা দেখুন
   - আউটপুট যথাযথ কিনা যাচাই করুন

2. **ডকুমেন্টেশন আপডেট:**
   - নতুন ধারণা যোগ করলে `README.md` আপডেট করুন
   - জটিল কোডের জন্য নোটবুকে মন্তব্য যোগ করুন
   - Markdown সেলে উদ্দেশ্য ব্যাখ্যা করুন

3. **ফাইল পরিবর্তন:**
   - `.env` ফাইল কমিট করবেন না (ব্যবহার করুন `.env.example`)
   - `venv/` বা `__pycache__/` ডিরেক্টরি কমিট করবেন না
   - ধারণা বোঝাতে নোটবুক আউটপুট রাখুন
   - অস্থায়ী ফাইল ও ব্যাকআপ নোটবুক (`*-backup.ipynb`) মুছে ফেলুন

4. **স্টাইল ও ফরম্যাটিং:**
   - স্টাইল ও ফরম্যাটিং নির্দেশিকা অনুসরণ করুন
   - `poetry run black .` এবং `poetry run ruff check .` চালিয়ে স্টাইল ও ফরম্যাটিং সমস্যা দেখুন

5. **টেস্ট ও CLI হেল্প যোগ/আপডেট:**
   - আচরণ পরিবর্তন করলে টেস্ট যোগ/আপডেট করুন
   - CLI হেল্প পরিবর্তনের সাথে সামঞ্জস্য রাখুন


### কমিট মেসেজ ও মার্জ কৌশল

আমরা Squash and Merge ডিফল্ট হিসেবে ব্যবহার করি। চূড়ান্ত squash কমিট মেসেজের কাঠামো:

```bash
<type>: <description> (#<PR number>)
```

অনুমোদিত টাইপ:
- `Docs` — ডকুমেন্টেশন আপডেট
- `Build` — বিল্ড সিস্টেম, ডিপেন্ডেন্সি, কনফিগারেশন/CI
- `Core` — মূল ফিচার ও কার্যকারিতা (যেমন `src/co_op_translator/core`)

উদাহরণ:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

নোট:
- PR টাইটেল প্রায়ই লেবেল অনুযায়ী অটো-প্রিফিক্সড হয়; জেনারেটেড প্রিফিক্স ঠিক আছে কিনা যাচাই করুন।

### PR টাইটেল ফরম্যাট

স্পষ্ট, সংক্ষিপ্ত টাইটেল ব্যবহার করুন। চূড়ান্ত squash কমিটের কাঠামো অনুসরণ করুন:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## ডিবাগিং ও সমস্যা সমাধান

- সাধারণ সমস্যা ও সমাধান: `getting_started/troubleshooting.md`
- সমর্থিত ভাষা ও নোট (ফন্ট/পরিচিত সমস্যা সহ): `getting_started/supported-languages.md`
- নোটবুকে লিংক সমস্যা হলে পুনরায় চালান: `migrate-links -l "all" -y`

## এজেন্টদের জন্য নোট

- পুনরুত্পাদনযোগ্য পরিবেশের জন্য Poetry পছন্দ করুন; না হলে `requirements.txt` ব্যবহার করুন।
- CI-তে CLI চালানোর সময় প্রয়োজনীয় সিক্রেট পরিবেশ ভেরিয়েবল বা `.env` ইনজেকশন দিয়ে দিন।
- মনোরেপো কনজিউমারদের জন্য, এই রিপো স্ট্যান্ডঅ্যালোন প্যাকেজ হিসেবে কাজ করে; কোনো সাব‑প্যাকেজ সমন্বয় দরকার নেই।

- মাল্টি-আর্ক নির্দেশনা: ARM ব্যবহারকারী (Apple Silicon/ARM সার্ভার) লক্ষ্য হলে `linux/arm64` রাখুন; না হলে শুধু `linux/amd64` সরলতার জন্য যথেষ্ট।
- কন্টেইনার ব্যবহার পছন্দ করলে `README.md`-এর Docker Quick Start দেখান; Bash ও PowerShell ভ্যারিয়েন্ট দিন, কারণ কোটিংয়ে পার্থক্য আছে।

---

**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতা বজায় রাখার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।