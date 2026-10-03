# কনফিগারেশন

Co-op Translator-এর জন্য এক ভাষা মডেল প্রদানকারী প্রয়োজন। ইমেজ অনুবাদের জন্য অতিরিক্তভাবে Azure AI Vision প্রয়োজন।

কনফিগারেশন পরিবেশ ভেরিয়েবল থেকে পড়া হয়। লোকাল প্রোজেক্টগুলোর জন্য, এগুলো প্রোজেক্ট রুটে `.env` ফাইলে রাখুন।

For Azure resource setup, see [Azure AI সেটআপ](azure-ai-setup.md).

## লোকাল রানটাইম সেটআপ

লোকালি CLI চালানোর আগে একটি ভার্চুয়াল এনভায়রনমেন্ট ব্যবহার করুন। Co-op Translator Python 3.11 থেকে 3.14 পর্যন্ত সমর্থন করে।

সাধারণ CLI ব্যবহারের জন্য, ভার্চুয়াল এনভায়রনমেন্টের ভিতরে প্রকাশিত প্যাকেজটি ইনস্টল করুন:

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install co-op-translator
translate --help
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install co-op-translator
translate --help
```

### রেপোজিটরি ডেভেলপমেন্ট

রেপোজিটরি ডেভেলপমেন্টের জন্য, পরিবর্তে প্রোজেক্ট রুট থেকে নির্ভরতা ইনস্টল করুন:

```bash
poetry install
poetry run translate --help
```

CLI উপলব্ধ হওয়ার পর `.env`-এ একটি ভাষা মডেল প্রদানকারী কনফিগার করুন।

## প্রদানকারী নির্বাচন

টুলটি নিম্নলিখিত ক্রমে প্রদানকারীদের স্বয়ংক্রিয়ভাবে সনাক্ত করে:

1. Azure OpenAI
2. OpenAI
3. Anthropic

অনুবাদের জন্য প্রদানকারীর ক্রেডেনশিয়াল প্রয়োজন, কেবল `translate -l "ko" -md --dry-run` মত পূর্বদর্শনগুলো ব্যতীত। `migrate-links`, `co-op-review`, এবং `run_review` ডিটারমিনিস্টিক রক্ষণাবেক্ষণ অপারেশন যা প্রদানকারী ক্রেডেনশিয়াল প্রয়োজন করে না।

## মডেল ক্লায়েন্ট ব্যাকএন্ড

Co-op Translator 0.22.0 থেকে শুরু করে, Azure OpenAI, OpenAI, এবং Anthropic ডিফল্টভাবে Microsoft Agent Framework ব্যবহার করে। সাধারণ ব্যবহারের জন্য কোনো ব্যাকএন্ড সেটিং প্রয়োজন নয়।

Semantic Kernel অস্থায়ীভাবে কম্প্যাটিবিলিটির জন্য উপলব্ধ রয়েছে। এটি স্পষ্টভাবে নির্বাচন করতে, সেট করুন:

```bash
CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"
```

Semantic Kernel ব্যবহার করলে ডিপ্রিকেটেশন সতর্কতা দেখানো হবে। প্যাকেজটি Semantic Kernel-কে 0.23.0-এ একটি ঐচ্ছিক নির্ভরশীলতা হিসেবে স্থানান্তর করার পরিকল্পনা রয়েছে এবং 0.24.0-এ ইন্টিগ্রেশনটি সরিয়ে নেওয়া হবে, যা কম্প্যাটিবিলিটি ফলাফল এবং ব্যবহারকারী প্রতিক্রিয়ার ওপর নির্ভরশীল। Anthropic `agent-framework` প্রয়োজন; Anthropic-এর ক্ষেত্রে স্পষ্টভাবে `semantic-kernel` নির্বাচন করলে কনফিগারেশন ত্রুটি দেখা দেবে। ভুল মানগুলির ক্ষেত্রে প্রদানকারী-সমর্থিত অনুবাদক ইনিশিয়ালাইজেশনের সময় ত্রুটি হবে, নীরবে fallback করার পরিবর্তে। রোলআউট অনুসরণ করুন এবং ব্লকারগুলো রিপোর্ট করুন [GitHub ইস্যু #543](https://github.com/Azure/co-op-translator/issues/543)।

## Azure OpenAI

আপনার মডেল Azure AI Foundry বা Azure OpenAI Service-এ ডিপ্লয় করা থাকলে Azure OpenAI ব্যবহার করুন।

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

কনেক্টিভিটি চেক অনুবাদ শুরু হওয়ার আগে endpoint, API key, API version, এবং deployment name ব্যবহার করে।

## OpenAI

OpenAI ব্যবহার করুন যখন OpenAI API সরাসরি কল করা হয়।

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

`OPENAI_CHAT_MODEL_ID` আবশ্যক কারণ অনুবাদককে API কলের জন্য একটি স্পষ্ট চ্যাট মডেল দরকার।

`OPENAI_ORG_ID` এবং `OPENAI_BASE_URL`-কে ডিফল্ট সেটআপের জন্য অপরিবর্তিত রাখুন। কেবল তখনই organization ID যোগ করুন যদি আপনার অ্যাকাউন্টে এটা দরকার হয়, বা কাস্টম endpoint ব্যবহার করলে শুধু তখনই base URL দিন। অপশনাল সেটিংসের জন্য প্লেসহোল্ডার মান কপি করবেন না।

## Anthropic Claude

Claude API-কে সরাসরি কল করলে Anthropic ব্যবহার করুন। একটি [Anthropic API কী](https://platform.claude.com/docs/en/get-started) তৈরি করুন এবং একটি সমর্থিত [Claude মডেল ID](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) নির্বাচন করুন।

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_API_KEY` এবং `ANTHROPIC_MODEL` আবশ্যক। আপনাকে `CO_OP_TRANSLATOR_MODEL_CLIENT` সেট করার প্রয়োজন নেই; Agent Framework ডিফল্ট ব্যাকএন্ড।

`ANTHROPIC_BASE_URL` Anthropic API-এর জন্য অপরিবর্তিত রাখুন। কেবল কাস্টম endpoint ব্যবহার করলে সেট করুন।

`ANTHROPIC_MAX_TOKENS` ডিফল্টভাবে `8192`, যা Meitei Mayek-এর মতো token-ঘন স্ক্রিপ্টগুলির জন্য জায়গা রাখে। যদি আপনার মডেল বা Anthropic-কম্প্যাটিবল endpoint আউটপুটকে তার নিচে সীমাবদ্ধ করে, তাহলে এটি কমিয়ে দিন।

## Azure AI Vision

ইমেজ অনুবাদের জন্য Azure AI Vision প্রয়োজন যাতে টুলটি কনফিগার করা ভাষা মডেল অনুবাদ করার আগে ইমেজ থেকে টেক্সট বের করতে পারে। Anthropic বের করা টেক্সটকে Azure OpenAI বা OpenAI-এর মত অনুবাদ করতে পারে।

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

যদি ইমেজ অনুবাদ `-img`, `images=True`, বা কোন content-type ফিল্টার না দিয়ে নির্বাচিত হয়, টুলটি অনুবাদ শুরু হওয়ার আগে Vision কনফিগারেশন যাচাই করে।

## একাধিক ক্রেডেনশিয়াল সেট

কনফিগারেশন লেয়ার একই ইনডেক্স দিয়ে ভেরিয়েবলগুলির সাথে সাফিক্স যোগ করে একাধিক ক্রেডেনশিয়াল সেট সমর্থন করে:

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"

AZURE_OPENAI_API_KEY_2="..."
AZURE_OPENAI_ENDPOINT_2="https://<resource-2>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_2="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_2="<deployment-2>"
AZURE_OPENAI_API_VERSION_2="2024-12-01-preview"
```

প্রতি সেট পূর্ণাঙ্গ হতে হবে। হেলথ চেক অনুবাদ শুরু হওয়ার আগে একটি কার্যকর সেট নির্বাচন করে।

OpenAI এবং Anthropic একই সাফিক্স নিয়ম সমর্থন করে। একটি ক্রেডেনশিয়াল সেটের প্রতিটি ভেরিয়েবল একই সাফিক্সে রাখুন, `OPENAI_BASE_URL_1` বা `ANTHROPIC_BASE_URL_1` এর মতো অপশনাল মানগুলিকেও সহ।

## কমান্ড প্রয়োজনীয়তা

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | হ্যাঁ | না | শুধুমাত্র Markdown অনুবাদ করে। |
| `translate -nb` | হ্যাঁ | না | শুধুমাত্র নোটবুক অনুবাদ করে। |
| `translate -img` | হ্যাঁ | হ্যাঁ | শুধুমাত্র ইমেজ অনুবাদ করে। |
| `translate` with no type flags | হ্যাঁ | হ্যাঁ | ডিফল্ট মোডে Markdown, নোটবুক, এবং ইমেজ অন্তর্ভুক্ত। |
| `evaluate` | হ্যাঁ | না | `--fast` সিলেক্ট না করলে LLM মূল্যায়ন ব্যবহার করে। |
| `migrate-links` | না | না | প্রদানকারী কল ছাড়া লোকাল লিঙ্ক মাইগ্রেশন সম্পাদন করে। |
| `co-op-review` | না | না | ডিটারমিনিস্টিক অনুবাদ কাঠামো, নবীনতা, Markdown, নোটবুক, এবং লোকাল লিঙ্ক চেক চালায়। |
| `run_translation(markdown=True)` | হ্যাঁ | না | প্রোগ্রাম্যাটিক Markdown অনুবাদ। |
| `run_translation(images=True)` | হ্যাঁ | হ্যাঁ | প্রোগ্রাম্যাটিক ইমেজ অনুবাদ। |
| `run_review(...)` | না | না | প্রোগ্রাম্যাটিক ডিটারমিনিস্টিক রিভিউ। |

## আউটপুট ডিরেক্টরি

ডিফল্ট টেক্সট অনুবাদ আউটপুট:

```text
translations/<language-code>/<source-relative-path>
```

ডিফল্ট অনূদিত ইমেজ আউটপুট:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API এই ডিরেক্টরিগুলো `translations_dir` এবং `image_dir` দিয়ে ওভাররাইড করতে পারে।