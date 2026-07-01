# রক্ষণাবেক্ষক গাইড

এই পৃষ্ঠা সারসংক্ষেপ করে কিভাবে API, CLI, এবং ডকুমেন্টেশন সাইট একসাথে সংযুক্ত।

## পাবলিক API সীমানা

স্থিতিশীল Python API নিম্নলিখিত স্থান থেকে রপ্তানি করা হয়:

```python
co_op_translator.api
```

পাবলিক API গুলো কন্টেন্ট অনুবাদ সহায়ক, পাথ পুনঃলেখন সহায়ক, প্রকল্প সমন্বয়, এবং রিভিউ হিসেবে সংগঠিত:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

নতুন পাবলিক API যোগ করার সময়, আপডেট করুন:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- প্রাসঙ্গিক API টেস্টগুলো `tests/co_op_translator/`-এর অধীনে, যেমন `test_api.py` বা `test_review_api.py`

প্রকল্প যদি সরাসরি সেগুলো সমর্থন করার অভিপ্রায় না দেয়, তাহলে নীচের-স্তরের `core` মডিউলগুলিকে স্থিতিশীল API হিসেবে ডকুমেন্ট করা এড়িয়ে চলুন।

## CLI entry points

প্যাকেজটি নিম্নলিখিত Poetry স্ক্রিপ্টগুলি নির্ধারণ করে:

```toml
[tool.poetry.scripts]
translate = "co_op_translator.__main__:main"
evaluate = "co_op_translator.__main__:main"
migrate-links = "co_op_translator.__main__:main"
co-op-review = "co_op_translator.__main__:main"
co-op-translator-mcp = "co_op_translator.mcp.server:main"
```

`src/co_op_translator/__main__.py` স্ক্রিপ্ট নাম অনুযায়ী ডিসপ্যাচ করে:

- `translate` কল করে `co_op_translator.cli.translate.translate_command`
- `evaluate` কল করে `co_op_translator.cli.evaluate.evaluate_command`
- `migrate-links` কল করে `co_op_translator.cli.migrate_links.migrate_links_command`
- `co-op-review` কল করে `co_op_translator.cli.review.review_command`

`co-op-translator-mcp` `__main__.py` বাইপাস করে এবং সরাসরি `co_op_translator.mcp.server:main` কল করে।

CLI অপশন যোগ বা পরিবর্তন করার সময়, আপডেট করুন:

- প্রাসঙ্গিক `src/co_op_translator/cli/*.py` কমান্ড
- `docs/cli.md`
- CLI-সংক্রান্ত টেস্টগুলো, যদি আচরণ পরিবর্তিত হয়

## MCP server

MCP সার্ভারটি নিম্নলিখিত স্থানে বাস্তবায়িত:

```python
co_op_translator.mcp.server
```

সার্ভারটি ইচ্ছাকৃতভাবে পাবলিক Python API-কে র‍্যাপ করে, নীচের-স্তরের `core` মডিউলগুলো কল করার বদলে। এই সীমাকে অক্ষত রাখুন যাতে MCP ক্লায়েন্ট, Python কলাররা, এবং CLI একই আচরণ শেয়ার করে।

MCP টুল যোগ বা পরিবর্তন করলে, আপডেট করুন:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` যদি পাবলিক API সারফেস পরিবর্তিত হয়

রিপোজিটরি অনুবাদ টুলগুলো MCP-এর মাধ্যমে মডেল-কল-যোগ্য এবং অনেক ফাইল লিখতে পারে। ডিফল্ট হিসেবে `dry_run=True` রাখুন এবং নন-ড্রাই-রান প্রকল্প অনুবাদের আগে `confirm_write=True` প্রয়োজন করুন।

## অনুবাদ প্রবাহ

উচ্চ-স্তরের প্রকল্প অনুবাদ প্রবাহ হলো:

1. CLI আর্গুমেন্ট বা API প্যারামিটার পার্স করুন।
2. LLM কনফিগারেশন `LLMConfig` দিয়ে যাচাই করুন।
3. ইমেজ অনুবাদ নির্বাচিত হলে Azure AI Vision যাচাই করুন।
4. ভাষা কোডগুলো সাধারণীকরণ করুন।
5. লিগ্যাসি ভাষা ফোল্ডার উপনামগুলি শনাক্ত করুন।
6. অনুবাদের পরিমাণ অনুমান করুন।
7. প্রযোজ্য হলে README-এর ভাষা/কোর্স সেকশনগুলো আপডেট করুন।
8. প্রকল্প অনুবাদ `ProjectTranslator`-কে হস্তান্তর করুন।
9. `ProjectTranslator` ফাইল প্রসেসিং `TranslationManager`-কে হস্তান্তর করে।

`TranslationManager` বিভিন্ন ফাইল-টাইপ মিক্সিন থেকে গঠিত:

- `ProjectMarkdownTranslationMixin` Markdown ফাইল পড়া, কনটেন্ট অনুবাদ, পাথ পুনঃলেখন, মেটাডেটা, ডিসক্লেইমার, এবং লেখাগুলো পরিচালনা করে।
- `ProjectNotebookTranslationMixin` নোটবুক ফাইল পড়া, Markdown-সেল অনুবাদ, পাথ পুনঃলেখন, মেটাডেটা, ডিসক্লেইমার, এবং লেখাগুলো পরিচালনা করে।
- `ProjectImageTranslationMixin` ইমেজ আবিষ্কার, টেক্সট নিষ্কাষণ/অনুবাদ, রেন্ডার করা ইমেজ লেখা, এবং মেটাডেটা পরিচালনা করে।

নীচ-স্তরের কনটেন্ট API গুলো প্রকল্প ওয়ার্কফ্লো এড়িয়ে যায়:

1. `translate_markdown_content` এবং `translate_notebook_content` শুধুমাত্র ইন-মেমরি কনটেন্ট অনুবাদ করে।
2. `translate_image_content` একটি একক ইমেজের টেক্সট অনুবাদ করে এবং একটি রেন্ডার করা ইমেজ অবজেক্ট রিটার্ন করে।
3. `rewrite_markdown_paths` এবং `rewrite_notebook_paths` স্পষ্ট পোস্ট-প্রসেসিং হেল্পার। এগুলো কোন অনুবাদ করে না এবং কোন প্রকল্প লেখাও করে না।

## রিভিউ প্রবাহ

নির্ধারিত রিভিউ প্রবাহ হলো:

1. CLI আর্গুমেন্ট বা API প্যারামিটার পার্স করুন।
2. অনুরোধকৃত ভাষা কোডগুলো সাধারণীকরণ করুন।
3. `root_dir`, `root_dirs`, বা `groups` থেকে এক বা একাধিক রিভিউ টার্গেট তৈরি করুন।
4. `--changed-from` দিয়ে ঐচ্ছিকভাবে সোর্স ফাইলগুলো সীমাবদ্ধ করুন।
5. স্ট্রাকচার, অনুবাদের সাম্প্রতিকতা, Markdown অখণ্ডতা, এবং স্থানীয় লিঙ্ক/ইমেজ পাথগুলোর জন্য নির্ধারিত চেক চালান।
6. টেক্সট আউটপুট অথবা GitHub-শৈলীর Markdown প্রিন্ট করুন।
7. রিভিউ ত্রুটি পাওয়া গেলে ব্যর্থতার সাথে এক্সিট করুন।

রিভিউ প্রবাহ API কী দাবি করে না এবং pull request CI-এর জন্য উপযুক্ত থাকা উচিত। pull request ওয়ার্কফ্লো প্রতিটি রান-এ একটি চেক সারাংশ লেখে এবং কেবলমাত্র `co-op-review` ব্যর্থ হলে একটি PR কমেন্ট পোস্ট করে।

## ডকুমেন্টেশন সাইট

ডকস সাইটটি নিচের দ্বারা কনফিগার করা হয়:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` ডিরেক্টরিটি হল প্রামাণিক ডকুমেন্টেশন সোর্স। প্রকল্প যদি সচেতনভাবে অন্য কোনো প্রকাশিত ডকুমেন্টেশন সারফেস চালু না করে, তাহলে এই ডিরেক্টরির বাইরে নতুন end-user গাইড যোগ করবেন না।

স্থানীয়ভাবে বিল্ড করুন:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

স্থানীয়ভাবে প্রিভিউ করুন:

```bash
python -m mkdocs serve
```

উত্পন্ন সাইটটি `site/`-এ লেখা হয়, যা git দ্বারা উপেক্ষিত।

## GitHub Pages ওয়ার্কফ্লো

`.github/workflows/docs.yml` পুল রিকুয়েস্টে সাইট বিল্ড করে এবং `main`-এ পুশ হলে ডেপ্লয় করে।

ওয়ার্কফ্লো ইনস্টল করে:

```bash
pip install -r requirements-docs.txt
```

ডক্স ওয়ার্কফ্লো শুধুমাত্র ডকুমেন্টেশন টুলচেইন ইনস্টল করে। `mkdocs.yml` `mkdocstrings`-কে `src/` নির্দেশ করে যাতে পাবলিক API পেজগুলি সোর্স ট্রি থেকে পুরো রানটাইম ডিপেনডেন্সি সেট ইনস্টল না করেই রেন্ডার করা যায়। ভবিষ্যতে যদি API ডকস বিল্ডের সময় ঐচ্ছিক রানটাইম প্রোভাইডার ইম্পোর্ট করার প্রয়োজন হয়, তাহলে `.github/workflows/docs.yml` এবং এই গাইড দুটোই একসাথে আপডেট করুন।

## ডকসের মানদণ্ড

ডকুমেন্টেশন পরিবর্তন মার্জ করার আগে, চালান:

```bash
python -m mkdocs build --strict
git diff --check
```

কঠোর বিল্ড ব্যবহার করুন যাতে ভাঙা লিঙ্ক, অবৈধ ন্যাভিগেশন এন্ট্রি, এবং API রেন্ডারিং সমস্যা দ্রুত ব্যর্থ হয়।