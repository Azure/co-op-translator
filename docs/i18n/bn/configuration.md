# কনফিগারেশন

Co-op Translator একটি ভাষা মডেল প্রোভাইডার প্রয়োজন। চিত্র অনুবাদের জন্য অতিরিক্তভাবে Azure AI Vision প্রয়োজন।

কনফিগারেশন পরিবেশ ভেরিয়েবল থেকে পড়া হয়। লোকাল প্রজেক্টগুলোর জন্য, প্রজেক্ট রুটে `.env` ফাইলটি রাখুন।

Azure রিসোর্স সেটআপের জন্য দেখুন [Azure AI সেটআপ](azure-ai-setup.md)।

## লোকাল রানটাইম সেটআপ

স্থানীয়ভাবে CLI চালানোর আগে একটি ভার্চুয়াল এনভায়রনমেন্ট ব্যবহার করুন। Co-op Translator Python 3.10 থেকে 3.12 পর্যন্ত সমর্থন করে।

সাধারণ CLI ব্যবহারের জন্য, একটি ভার্চুয়াল এনভায়রনমেন্টের ভিতরে প্রকাশিত প্যাকেজটি ইনস্টল করুন:

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    pip install co-op-translator
    translate --help
    ```

=== "macOS / Linux"

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install co-op-translator
    translate --help
    ```

রিপোজিটরি ডেভেলপমেন্টের জন্য, তার পরিবর্তে প্রজেক্ট রুট থেকে ডিপেন্ডেন্সিগুলো ইনস্টল করুন:

```bash
poetry install
poetry run translate --help
```

CLI উপলব্ধ হওয়ার পরে, `.env`-এ একটি ভাষা মডেল প্রোভাইডার কনফিগার করুন।

## প্রোভাইডার নির্বাচন

টুলটি নিম্নলিখিত ক্রমে প্রোভাইডারগুলো অটো-ডিটেক্ট করে:

1. Azure OpenAI
2. OpenAI

উভয় প্রোভাইডার কনফিগার করা না থাকলে, `translate`, `evaluate`, `migrate-links`, এবং `run_translation` কনফিগারেশন চেকগুলোর সময় ব্যর্থ হবে। `co-op-review` এবং `run_review` ডিটারমিনিস্টিক রক্ষণাবেক্ষণ চেক এবং এগুলো প্রোভাইডার ক্রেডেনশিয়াল প্রয়োজন করে না।

## Azure OpenAI

আপনার মডেলটি যদি Azure AI Foundry বা Azure OpenAI Service-এ ডিপ্লয় করা থাকে, তাহলে Azure OpenAI ব্যবহার করুন।

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

কনেক্টিভিটি চেক অনুবাদ শুরু হওয়ার আগেই endpoint, API key, API version, এবং deployment name ব্যবহার করে পরীক্ষা করে।

## OpenAI

OpenAI API সরাসরি কল করার সময় OpenAI ব্যবহার করুন।

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
OPENAI_ORG_ID="..."          # ঐচ্ছিক
OPENAI_BASE_URL="..."        # ঐচ্ছিক
```

`OPENAI_CHAT_MODEL_ID` প্রয়োজন কারণ ট্রান্সলেটর API কলের জন্য একটি স্পষ্ট chat model দরকার।

## Azure AI Vision

চিত্র অনুবাদের জন্য Azure AI Vision প্রয়োজন যাতে টুলটি অনুবাদের আগে চিত্র থেকে টেক্সট বের করতে পারে।

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

ইমেজ অনুবাদ `-img`, `images=True`, বা কোন content-type ফিল্টার না থাকলে নির্বাচিত হলে, টুলটি অনুবাদ শুরু হওয়ার আগে Vision কনফিগারেশন যাচাই করে।

## একাধিক ক্রেডেনশিয়াল সেট

কনফিগারেশন লেয়ার একই ইনডেক্স সহ ভেরিয়েবলগুলো suffix করে একাধিক ক্রেডেনশিয়াল সেট সমর্থন করে:

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

প্রতিটি সেট সম্পূর্ণ হতে হবে। হেলথ চেক অনুবাদ চালু হওয়ার আগে একটি কার্যকর সেট নির্বাচন করে।

## কমান্ড প্রয়োজনীয়তা

| Command or API | LLM required | Vision required | Notes |
| --- | --- | --- | --- |
| `translate -md` | হ্যাঁ | না | শুধুমাত্র Markdown অনুবাদ করে। |
| `translate -nb` | হ্যাঁ | না | শুধুমাত্র নোটবুক অনুবাদ করে। |
| `translate -img` | হ্যাঁ | হ্যাঁ | শুধুমাত্র চিত্র অনুবাদ করে। |
| `translate` with no type flags | হ্যাঁ | হ্যাঁ | ডিফল্ট মোডে Markdown, নোটবুক, এবং চিত্র অন্তর্ভুক্ত থাকে। |
| `evaluate` | হ্যাঁ | না | `--fast` নির্বাচিত না হলে LLM মূল্যায়ন ব্যবহার করে। |
| `migrate-links` | হ্যাঁ | না | লিঙ্ক মাইগ্রেশন করে, তবে এখনও শেয়ার করা কনফিগারেশন চেকগুলো চালায়। |
| `co-op-review` | না | না | ডিটারমিনিস্টিক অনুবাদ কাঠামো, তাজা বিষয়বস্তু, Markdown, নোটবুক, এবং লোকাল লিঙ্ক চেকগুলো চালায়। |
| `run_translation(markdown=True)` | হ্যাঁ | না | প্রোগ্রাম্যাটিক Markdown অনুবাদ। |
| `run_translation(images=True)` | হ্যাঁ | হ্যাঁ | প্রোগ্রাম্যাটিক চিত্র অনুবাদ। |
| `run_review(...)` | না | না | প্রোগ্রাম্যাটিক ডিটারমিনিস্টিক রিভিউ। |

## আউটপুট ডিরেক্টরিগুলি

ডিফল্ট টেক্সট অনুবাদ আউটপুট:

```text
translations/<language-code>/<source-relative-path>
```

ডিফল্ট অনূদিত চিত্র আউটপুট:

```text
translated_images/<language-code>/<source-relative-path>
```

Python API এই ডিরেক্টরিগুলো `translations_dir` এবং `image_dir` দিয়ে ওভাররাইড করতে পারে।