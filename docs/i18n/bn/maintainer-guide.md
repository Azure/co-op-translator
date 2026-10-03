# রক্ষণাবেক্ষক নির্দেশিকা

এই পৃষ্ঠা সংক্ষেপে নির্দেশ করে কিভাবে API, CLI, এবং ডকুমেন্টেশন সাইট একসাথে সংযুক্ত।

## পাবলিক API সীমানা

স্থিতিশীল Python APIটি রপ্তানি করা হয়:

```python
co_op_translator.api
```

পাবলিক APIটি কনটেন্ট অনুবাদ সহায়ক, পাথ পুনর্লিখন সহায়ক, প্রজেক্ট অর্কেস্ট্রেশন, এবং রিভিউতে সংগঠিত:

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

`TranslationStateProvider` হোস্টেড ইন্টিগ্রেশনগুলোর জন্য পারসিস্টেন্স সীমানা।
এটি তৈরি করা প্রার্থীকে গ্রহণকৃত বেসলাইন থেকে পৃথক রাখতে হবে যাতে একটি
অমিলিত অনুবাদ সত্যের উৎস হয়ে ওঠে না।

নতুন পাবলিক API যোগ করার সময়, আপডেট করুন:

- `src/co_op_translator/api/__init__.py`
- `docs/api.md`
- প্রাসঙ্গিক API টেস্টসমূহ `tests/co_op_translator/` এর অধীনে, যেমন `test_api.py` বা `test_review_api.py`

প্রকল্প যদি সরাসরি সেগুলো সমর্থন করার ইচ্ছা না রাখে, তাহলে নিম্ন-স্তরের `core` মডিউলগুলোকে স্থিতিশীল API হিসেবে ডকুমেন্ট করা থেকে বিরত থাকুন।

## CLI এন্ট্রি পয়েন্টস

প্যাকেজটি এই Poetry স্ক্রিপ্টগুলো সংজ্ঞায়িত করে:

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

CLI অপশন যোগ বা পরিবর্তন করলে, আপডেট করুন:

- সংশ্লিষ্ট `src/co_op_translator/cli/*.py` কমান্ড
- `docs/cli.md`
- CLI-সংক্রান্ত টেস্টসমূহ, যদি আচরণ বদলে যায়

## MCP সার্ভার

MCP সার্ভারটি ইমপ্লিমেন্ট করা হয়েছে:

```python
co_op_translator.mcp.server
```

সার্ভারটি ইচ্ছাকৃতভাবে পাবলিক Python API-কে র‍্যাপ করে, নিম্ন-স্তরের `core` মডিউলগুলোকে কল করার বদলে। এই সীমানাটি অক্ষত রাখুন যাতে MCP ক্লায়েন্ট, Python কলার এবং CLI একই আচরণ শেয়ার করে।

MCP টুল যোগ বা পরিবর্তন করলে, আপডেট করুন:

- `src/co_op_translator/mcp/server.py`
- `tests/co_op_translator/test_mcp_server.py`
- `docs/mcp.md`
- `docs/api.md` যদি পাবলিক API সারফেস পরিবর্তিত হয়

রিপোজিটরি অনুবাদ টুলগুলো MCP মাধ্যমে মডেল-কলেবল এবং অনেক ফাইল লিখতে পারে। ডিফল্ট হিসেবে `dry_run=True` রাখুন এবং নন-ড্রাই-রান প্রকল্প অনুবাদের আগে `confirm_write=True` প্রয়োজন করুন।

## অনুবাদ প্রবাহ

উচ্চ-স্তরের প্রকল্প অনুবাদ প্রবাহ হলো:

1. CLI আর্গুমেন্ট বা API প্যারামিটার পার্স করুন।
2. `LLMConfig` দিয়ে LLM কনফিগারেশন যাচাই করুন।
3. ইমেজ অনুবাদ নির্বাচিত হলে Azure AI Vision যাচাই করুন।
4. ভাষা কোডগুলো স্বাভাবিক করুন।
5. লিগেসি ভাষা ফোল্ডার আলিয়াস সনাক্ত করুন।
6. অনুবাদ পরিমাণ অনুমান করুন।
7. প্রযোজ্য হলে README ভাষা/কোর্স সেকশন আপডেট করুন।
8. প্রকল্প অনুবাদ `ProjectTranslator`-কে ডেলিগেট করুন।
9. `ProjectTranslator` ফাইল প্রসেসিং `TranslationManager`-কে ডেলিগেট করে।

`TranslationManager` বিভিন্ন ফাইল-টাইপের মিক্সিন দিয়ে গঠিত:

- `ProjectMarkdownTranslationMixin` Markdown ফাইল রিড, কনটেন্ট অনুবাদ, পাথ পুনর্লিখন, মেটাডেটা, ডিসক্লেইমার, এবং লেখাগুলো পরিচালনা করে।
- `ProjectNotebookTranslationMixin` নোটবুক ফাইল রিড, Markdown-সেল অনুবাদ, পাথ পুনর্লিখন, মেটাডেটা, ডিসক্লেইমার, এবং লেখাগুলো পরিচালনা করে।
- `ProjectImageTranslationMixin` ইমেজ আবিষ্কার, টেক্সট এক্সট্র্যাকশন/অনুবাদ, রেন্ডার করা ইমেজ লেখালেখি, এবং মেটাডেটা পরিচালনা করে।

নিম্ন-স্তরের কনটেন্ট API গুলো প্রকল্প কর্মপ্রবাহটি স্কিপ করে:

1. `translate_markdown_content` এবং `translate_notebook_content` শুধুমাত্র ইন-মেমরি কনটেন্ট অনুবাদ করে।
2. `translate_image_content` একটি একক ইমেজের মধ্যে টেক্সট অনুবাদ করে এবং একটি রেন্ডার করা ইমেজ অবজেক্ট ফেরত দেয়।
3. `rewrite_markdown_paths` এবং `rewrite_notebook_paths` স্পষ্ট পোস্ট-প্রসেসিং হেল্পার। এগুলো কোনো অনুবাদ বা প্রকল্প লেভেলে লেখালেখি করে না।

## রিভিউ প্রবাহ

নির্ধারিত রিভিউ প্রবাহ হলো:

1. CLI আর্গুমেন্ট বা API প্যারামিটার পার্স করুন।
2. অনুরোধকৃত ভাষা কোডগুলো স্বাভাবিক করুন।
3. `root_dir`, `root_dirs`, বা `groups` থেকে এক বা একাধিক রিভিউ টার্গেট তৈরি করুন।
4. ঐচ্ছিকভাবে `--changed-from` দিয়ে সোর্স ফাইলগুলো সীমাবদ্ধ করুন।
5. স্ট্রাকচার, অনুবাদের সতেজতা, Markdown অখণ্ডতা, এবং লোকাল লিঙ্ক/ইমেজ পাথের জন্য ডিটারমিনিস্টিক চেক চালান।
6. টেক্সট আউটপুট বা GitHub-ফ্লেভার্ড Markdown যে কোন একটি প্রিন্ট করুন।
7. রিভিউ ত্রুটি পাওয়া গেলে ব্যর্থ অবস্থায় এক্সিট করুন।

রিভিউ প্রবাহ API কী প্রয়োজন করে না এবং লোকাল চেক বা অপ্ট-ইন কনজিউমার CI-এর জন্য উপলব্ধ থাকে। এই রিপোজিটরি প্রতিটি পুল রিকোয়েস্টে স্বয়ংক্রিয়ভাবে `co-op-review` চালায় না।

## ডকুমেন্টেশন সাইট

ডকস সাইটটি নিম্নলিখিত দ্বারা কনফিগার করা হয়েছে:

```text
mkdocs.yml
requirements-docs.txt
docs/
```

`docs/` ডিরেক্টরি হলো আনুষ্ঠানিক ডকুমেন্টেশনের উৎস। এই ডিরেক্টরির বাইরে নতুন এন্ড-ইউজার গাইড যোগ করবেন না, যদি না প্রকল্প ইচ্ছাকৃতভাবে অন্য কোনো প্রকাশিত ডকুমেন্টেশন সারফেস পরিচয় করায়।

লোকালি বিল্ড করুন:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

লোকালি প্রিভিউ করুন:

```bash
python -m mkdocs serve
```

জেনারেট করা সাইটটি `site/` এ লেখা হয়, যা git দ্বারা ইগনোর করা হয়েছে।

## GitHub Pages ওয়ার্কফ্লো

`.github/workflows/docs.yml` পুল রিকোয়েস্টে সাইট বিল্ড করে এবং `main`-এ পুশ করলে ডিপ্লয় করে।

ওয়ার্কফ্লো ইনস্টল করে:

```bash
pip install -r requirements-docs.txt
```

ডকস ওয়ার্কফ্লো শুধুমাত্র ডকুমেন্টেশন টুলচেইন ইনস্টল করে। `mkdocs.yml` `mkdocstrings`-কে `src/` এর দিকে নির্দেশ করে যাতে পাবলিক API পেজগুলো সোর্স ট্রি থেকে সম্পূর্ণ রন্টটাইম ডিপেনডেন্সি সেট ইনস্টল না করেই রেন্ডার করা যায়। যদি ভবিষ্যতের API ডকস বিল্ডের সময় ঐচ্ছিক রন্টটাইম প্রোভাইডার ইনপোর্ট করা প্রয়োজন হয়, তাহলে `.github/workflows/docs.yml` এবং এই গাইড উভয়ই একসাথে আপডেট করুন।

## ডকস কোয়ালিটি বার

ডকুমেন্টেশন পরিবর্তন মার্জ করার আগে, চালান:

```bash
python -m mkdocs build --strict
git diff --check
```

কঠোর বিল্ড ব্যবহার করুন যাতে ভগ্ন লিংক, অকার্যকর নেভিগেশন এন্ট্রি, এবং API রেন্ডারিং সমস্যা শুরুতেই ব্যর্থ হয়।