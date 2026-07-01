# পাইথন API

স্থায়ী পাবলিক পাইথন API `co_op_translator.api` থেকে রপ্তানি করা হয়। বেশিরভাগ ইন্টিগ্রেশন নিম্নলিখিত ওয়ার্কফ্লোগুলোর একটি ব্যবহার করে:

| Scenario | Use this when | Main APIs |
| --- | --- | --- |
| Translate individual files or documents | আপনার অ্যাপ্লিকেশন উৎস সামগ্রী পড়ে, অনুবাদের জন্য Co-op Translator কল করে, এবং সিদ্ধান্ত নেয় ফলাফল কোথায় সংরক্ষণ করা হবে। | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| Prepare content for host-agent translation | আপনার MCP হোস্ট বা অ্যাপ্লিকেশন মডেল চাঙ্কগুলো অনুবাদ করবে, যখন Co-op Translator চাঙ্কিং এবং পুনর্নির্মাণ পরিচালনা করবে। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Translate an entire repository | আপনি চান পাইথন API CLI-এর মতো আচরণ করুক এবং ডিসকভারি, আউটপুট পাথ, মেটাডাটা, ক্লিনআপ এবং লেখাগুলো পরিচালনা করুক। | `run_translation` |

`core`, `config`, `review`, এবং `utils` এর অধীনের বেশিরভাগ নিম্ন-স্তরের মডিউলগুলো এই API এন্ট্রি পয়েন্টগুলোর দ্বারা ব্যবহৃত বাস্তবায়ন বিবরণ।

MCP ক্লায়েন্ট একই পাবলিক API [MCP Server](mcp.md) এর মাধ্যমে ব্যবহার করে। পাইটন সরাসরি কল করার সময় এই পেজটি ব্যবহার করুন, এবং Co-op Translator একটি এজেন্ট বা এডিটরের কাছে প্রকাশ করার সময় MCP গাইডটি ব্যবহার করুন। যদি আপনি CLI, পাইথন API, এবং MCP এর মধ্যে সিদ্ধান্ত নিতে চান, তাহলে [Choose Your Workflow](workflows.md) থেকে শুরু করুন।

## প্রথমবারের জন্য API প্রবাহ

এখান থেকে শুরু করুন যদি আপনি পাইথন কোড থেকে Co-op Translator কল করছেন:

1. যদি আপনি শুধু Markdown বা নোটবুক চাঙ্কগুলো হোস্ট-এজেন্ট অনুবাদের জন্য প্রস্তুত না করে থাকেন, তাহলে [Configuration](configuration.md) এ বর্ণিতভাবে একটি LLM প্রদানকারী কনফিগার করুন।
2. সিদ্ধান্ত নিন যে আপনার অ্যাপ্লিকেশন ফাইল I/O এর মালিক কি না।
3. যখন আপনার অ্যাপ্লিকেশন পৃথক ফাইল পড়ে এবং লিখে, তখন কনটেন্ট API ব্যবহার করুন।
4. যখন Co-op Translator CLI-এর মতো একটি রিপোজিটরিটি প্রক্রিয়া করবে তখন `run_translation` ব্যবহার করুন।
5. যদি আপনি অটোমেশন এ নির্দিষ্ট চেক দরকার হয়, অনুবাদের পরে `run_review` ব্যবহার করুন।

| Goal | API to start with |
| --- | --- |
| Translate one Markdown string or file | `translate_markdown_content` |
| Translate one notebook payload | `translate_notebook_content` |
| Translate one image | `translate_image_content` |
| Let a host agent translate Markdown or notebook chunks | `start_markdown_agent_translation` or `start_notebook_agent_translation` |
| Rewrite translated links after choosing an output path | `rewrite_markdown_paths` or `rewrite_notebook_paths` |
| Translate a full repository | `run_translation` |
| Review translated output | `run_review` |

## দৃশ্য 1: পৃথক ফাইল বা ডকুমেন্ট অনুবাদ করুন

এটি ব্যবহার করুন যখন আপনার কাছে ইতিমধ্যেই একটি ফাইল, এডিটর বাফার, নোটবুক পে-লোড, MCP অনুরোধ, বা কাস্টম পাইপলাইন ইনপুট থাকে। আপনার কোড ফাইল I/O এর মালিক:

1. উৎস সামগ্রী পড়ুন।
2. একটি কনটেন্ট অনুবাদ API কল করুন।
3. যদি অনুবাদ করা সামগ্রী প্রজেক্ট অনুবাদ ফোল্ডারে লেখা হবে তবে অপশনালি একটি পাথ রিরাইটিং API কল করুন।
4. আপনার অ্যাপ্লিকেশন থেকে ফলাফল সংরক্ষণ করুন বা ফেরত দিন।

কনটেন্ট অনুবাদ API গুলো প্রজেক্ট ডিসকভরি চালায় না, মেটাডাটা লিখে না, ডিসক্লেইমার যোগ করে না, এবং লিঙ্কগুলো স্বয়ংক্রিয়ভাবে রিরাইট করে না।

### মার্কডাউন ফাইল

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_markdown_paths,
    translate_markdown_content,
)


async def main() -> None:
    source_path = Path("docs/guide.md")
    target_path = Path("translations/ko/docs/guide.md")

    translated = await translate_markdown_content(
        source_path.read_text(encoding="utf-8"),
        "ko",
        {"source_path": source_path},
    )

    rewritten = rewrite_markdown_paths(
        translated,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

যদি অনূদিত Markdown একটি Co-op Translator প্রজেক্ট লেআউটে অবস্থান করবে না, তাহলে `rewrite_markdown_paths` ছেড়ে দিয়ে অনূদিত স্ট্রিং সরাসরি সংরক্ষণ করুন।

### নোটবুক ফাইল

```python
import asyncio
from pathlib import Path

from co_op_translator.api import (
    rewrite_notebook_paths,
    translate_notebook_content,
)


async def main() -> None:
    source_path = Path("docs/tutorial.ipynb")
    target_path = Path("translations/ja/docs/tutorial.ipynb")

    translated_json = await translate_notebook_content(
        source_path.read_text(encoding="utf-8"),
        "ja",
        {"source_path": source_path},
    )

    rewritten_json = rewrite_notebook_paths(
        translated_json,
        source_path=source_path,
        target_path=target_path,
        policy={
            "language_code": "ja",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["notebook", "images"],
        },
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten_json, encoding="utf-8")


asyncio.run(main())
```

`translate_notebook_content` Markdown সেলগুলো অনুবাদ করে এবং নন-Markdown সেলগুলো সংরক্ষণ করে। পাথ রিরাইটিং শুধুমাত্র Markdown সেলগুলোর উপর প্রয়োগ করা হয়।

### ইমেজ ফাইল

```python
from pathlib import Path

from co_op_translator.api import translate_image_content

source_path = Path("docs/images/hero.png")
target_path = Path("translated_images/fr/hero.png")

translated_image = translate_image_content(
    source_path,
    "fr",
    {
        "root_dir": ".",
        "fast_mode": False,
    },
)

target_path.parent.mkdir(parents=True, exist_ok=True)
translated_image.save(target_path)
```

`translate_image_content` উৎস ইমেজ পড়ে এবং একটি রেন্ডার করা `PIL.Image.Image` ফেরত দেয়। এটি অনূদিত ইমেজ মেটাডাটা লিখে না।

## দৃশ্য 2: একটি সম্পূর্ণ রিপোজিটরি অনুবাদ করুন

এই ওয়ার্কফ্লো ব্যবহার করুন যখন আপনি চান পাইথন API `translate` CLI-এর মতো আচরণ করুক। `run_translation` সমর্থিত ফাইলগুলো খুঁজে পাওয়া, নির্বাচিত কনটেন্ট টাইপ অনুবাদ, পাথ রিরাইট, আউটপুট ফাইল লেখালেখি, মেটাডাটা আপডেট, এবং ক্লিনআপের মতো অনুবাদ মেইনটেন্যান্স টাস্কগুলো করে।

`run_translation` প্রজেক্ট অর্কেস্ট্রেশনের পছন্দসই এন্ট্রি পয়েন্ট। `translate_project` একই আচরণের সাথে সমতা রক্ষা করার জন্য একটি সংগতিসাধক আলিয়া হিসেবে রপ্তানি করা হয়েছে।

বর্তমান রিপোজিটরির Markdown ফাইলগুলো কোরিয়ান ও জাপানি-তে অনুবাদ করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

নির্দিষ্ট একটি প্রজেক্ট রুট থেকে শুধুমাত্র নোটবুক অনুবাদ করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ফাইল লেখা ছাড়া অনুবাদের পরিমাণ প্রিভিউ করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

একটি কলেই একাধিক কনটেন্ট রুট অনুবাদ করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

স্পষ্ট আউটপুট গ্রুপগুলিতে অনুবাদ লিখুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ja",
    markdown=True,
    groups=[
        ("./course-a", "./localized/course-a"),
        ("./course-b", "./localized/course-b"),
    ],
)
```

প্রতিটি ভাষার নিচে একটি নেস্টেড সাবডাইর থাকা উচিত হলে প্রতিটি ভাষার জন্য একটি প্লেসহোল্ডার ব্যবহার করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    groups=[
        ("./course", "./translations/<lang>/course"),
    ],
)
```

`markdown`, `notebook`, বা `images` এর কোনোটাই সেট না করা থাকলে, API সব সমর্থিত টাইপ অনুবাদ করে: Markdown, নোটবুক, এবং ইমেজ।

## অনূদিত আউটপুট পর্যালোচনা

`run_review` LLM বা Vision ক্রেডেনশিয়াল ছাড়া নির্ধারিত অনুবাদ চেক চালায়।

!!! note "বেটা"
    `run_review` একটি বেটা নির্ধারিত রিভিউ API। এটি মডেল প্রদানকারীদের কল করে না বা ফাইল লেখে না, কিন্তু চেক এবং ইস্যু স্কিমা পরিবর্তিত হতে পারে।

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

বেস রেফের বিরুদ্ধে পরিবর্তিত শুধু ফাইলগুলো পর্যালোচনা করুন এবং GitHub-ফ্লেভার্ড আউটপুট প্রিন্ট করুন:

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    changed_from="origin/main",
    output_format="github",
)
```

## কপি-পেস্ট API উদাহরণ

ফাইল লেখা ছাড়া Markdown কনটেন্ট অনুবাদ করুন:

```python
import asyncio

from co_op_translator.api import translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "# Hello\n\nWelcome to the course.",
        "ko",
    )
    print(translated)


asyncio.run(main())
```

Markdown লিঙ্ক অনুবাদ এবং রিরাইট করুন:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
        "ko",
        {"source_path": "docs/guide.md"},
    )
    rewritten = rewrite_markdown_paths(
        translated,
        source_path="docs/guide.md",
        target_path="translations/ko/docs/guide.md",
        policy={
            "language_code": "ko",
            "root_dir": ".",
            "translations_dir": "translations",
            "translated_images_dir": "translated_images",
            "translation_types": ["markdown", "images"],
        },
    )
    print(rewritten)


asyncio.run(main())
```

পাইথন থেকে একটি রিপোজিটরি অনুবাদ করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    root_dir="./course",
    markdown=True,
    yes=True,
)
```

একাধিক রুট অনুবাদ করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=[
        "./docs",
        "./labs",
    ],
)
```

গ্লোসারি টার্মগুলো সংরক্ষণ করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    markdown=True,
    glossaries=[
        "Co-op Translator",
        "Azure AI Foundry",
        "GitHub Actions",
    ],
)
```

## পাবলিক এন্ট্রি পয়েন্টসমূহ

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    finish_markdown_agent_translation,
    finish_notebook_agent_translation,
    run_review,
    run_translation,
    rewrite_markdown_paths,
    rewrite_notebook_paths,
    start_markdown_agent_translation,
    start_notebook_agent_translation,
    translate_image_content,
    translate_markdown_content,
    translate_notebook_content,
    translate_project,
)
```

::: co_op_translator.api.translate_markdown_content

::: co_op_translator.api.translate_notebook_content

::: co_op_translator.api.translate_image_content

::: co_op_translator.api.start_markdown_agent_translation

::: co_op_translator.api.finish_markdown_agent_translation

::: co_op_translator.api.start_notebook_agent_translation

::: co_op_translator.api.finish_notebook_agent_translation

::: co_op_translator.api.rewrite_markdown_paths

::: co_op_translator.api.rewrite_notebook_paths

::: co_op_translator.api.MarkdownTranslationOptions

::: co_op_translator.api.NotebookTranslationOptions

::: co_op_translator.api.ImageTranslationOptions

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## কনটেন্ট অনুবাদ API গুলো

কনটেন্ট অনুবাদ API গুলো তাদের জন্য উপযুক্ত যারা ইতিমধ্যেই মেমরিতে কনটেন্ট আছে, যেমন একটি এডিটর এক্সটেনশন, MCP টুল, নোটবুক প্রসেসর, বা কাস্টম পাইপলাইন।

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. শুধুমাত্র Markdown কনটেন্ট অনুবাদ করে। এটি লিঙ্ক রিরাইট করে না, মেটাডাটা লিখে না, বা ডিসক্লেইমার যোগ করে না। |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown সেলগুলো অনুবাদ করে এবং নন-Markdown সেলগুলো সংরক্ষণ করে। এটি লিঙ্ক রিরাইট করে না, মেটাডাটা লিখে না, বা ডিসক্লেইমার যোগ করে না। |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. ইমেজ থেকে টেক্সট বের করে অনুবাদ করে, তারপর একটি রেন্ডার করা ইমেজ ফেরত দেয়। এটি অনূদিত ইমেজ মেটাডাটা সংরক্ষণ করে না। |

`translate_markdown_content` এবং `translate_notebook_content` তাদের অপশনগুলোর মাধ্যমে একটি ঐচ্ছিক `source_path` গ্রহন করে। পাথটি অনুবাদকের কাছে কনটেক্সট হিসেবে প্রেরিত হয়; কলাররা অনুবাদ শেষে যে কোনো প্রজেক্ট-নির্দিষ্ট পাথ রিরাইটিংয়ের জন্য দায়ী থাকেন।

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

একই অপশনগুলো ডিকশনারি হিসেবে পাঠানো যেতে পারে:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## এজেন্ট-সহায়ক অনুবাদ API গুলো

এজেন্ট-সহায়ক API গুলো Co-op Translator থেকে Azure OpenAI বা OpenAI কল করে না। এইগুলো Markdown বা নোটবুক চাঙ্কগুলো হোস্ট এজেন্ট অনুবাদের জন্য প্রস্তুত করে, তারপর অনূদিত চাঙ্কগুলো থেকে চূড়ান্ত কনটেন্ট পুনর্নির্মাণ করে।

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | চাঙ্ক, প্রম্পট, এবং পুনর্নির্মাণ স্টেটসহ একটি স্ব-সম্পূর্ণ Markdown জব ফেরত দেয়। |
| `finish_markdown_agent_translation` | একটি জব এবং হোস্ট-এজেন্ট অনূদিত চাঙ্কগুলো থেকে Markdown পুনর্নির্মাণ করে। |
| `start_notebook_agent_translation` | হোস্ট-এজেন্ট অনুবাদের জন্য Markdown-সেল চাঙ্কসমূহসহ একটি নোটবুক জব ফেরত দেয়। |
| `finish_notebook_agent_translation` | কোড সেল, আউটপুট, এবং মেটাডাটা সংরক্ষণ করে নোটবুক JSON পুনর্নির্মাণ করে। |

এই ওয়ার্কফ্লো প্রধানত MCP হোস্টদের জন্য উদ্দেশ্যপ্রণোদিত। যদি আপনি প্রোডাকশন রিপোজিটরি অনুবাদ চান যেখানে Co-op Translator প্রদানকারী কলগুলো পরিচালনা করে, তাহলে `translate_markdown_content`, `translate_notebook_content`, বা `run_translation` ব্যবহার করুন।

## পাথ রিরাইটিং API গুলো

পাথ রিরাইটিং API গুলো কোনও অনুবাদ করে না। এগুলো কলাররা উৎস পাথ, অনূদিত লক্ষ্য পাথ, এবং প্রজেক্ট লেআউট জানার পরে লিঙ্ক এবং ফ্রন্টম্যাটার পাথ আপডেট করে।

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown body and frontmatter | অনূদিত লক্ষ্য জন্য Markdown লিঙ্ক এবং সমর্থিত ফ্রন্টম্যাটার পাথ ফিল্ডগুলো রিরাইট করে। |
| `rewrite_notebook_paths` | Markdown cells in notebook JSON | প্রতিটি Markdown সেলে Markdown পাথ রিরাইটিং প্রয়োগ করে এবং নন-Markdown সেলগুলো অপরিবর্তিত রেখে দেয়। |

`policy` আর্গুমেন্টটি একটি ডিকশনারি হতে পারে যার এই ফিল্ডসমূহ আছে:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | Yes | লক্ষ্য ভাষার কোড, যেমন `"ko"` বা `"pt-BR"`। |
| `root_dir` | No | উৎস প্রজেক্ট রুট। ডিফল্ট `"."`। |
| `translations_dir` | No | টেক্সট অনুবাদ আউটপুট ডিরেক্টরি। ডিফল্ট `root_dir` এর অধীনে `translations`। |
| `translated_images_dir` | No | অনূদিত ইমেজ আউটপুট ডিরেক্টরি। ডিফল্ট `root_dir` এর অধীনে `translated_images`। |
| `translation_types` | No | সক্রিয় অনুবাদ টাইপসমূহ। ডিফল্ট Markdown, নোটবুক, এবং ইমেজ। |
| `lang_subdir` | No | প্রতিটি ভাষা ফোল্ডারের অধীনে ঐচ্ছিক সাবডাইর। |

## প্রজেক্ট অনুবাদ প্যারামিটারসমূহ

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | স্পেস-সেপারেটেড লক্ষ্য ভাষার কোডসমূহ, যেমন `"ko ja fr"` বা `"all"`। এলিয়াস কোডগুলো ক্যানোনিকাল BCP 47 মানে নরমালাইজ করা হয়। |
| `root_dir` | `str` | `"."` | একক অনুবাদ টার্গেটের জন্য প্রজেক্ট রুট। যখন `root_dirs` বা `groups` সরবরাহ করা হয় তখন উপেক্ষা করা হয়। |
| `update` | `bool` | `False` | নির্বাচিত ভাষার জন্য বিদ্যমান অনুবাদ মুছে দিয়ে পুনরায় তৈরি করুন। |
| `images` | `bool` | `False` | ইমেজ অনুবাদ অন্তর্ভুক্ত করুন। Azure AI Vision কনফিগারেশন প্রয়োজন। |
| `markdown` | `bool` | `False` | Markdown অনুবাদ অন্তর্ভুক্ত করুন। |
| `notebook` | `bool` | `False` | Jupyter নোটবুক অনুবাদ অন্তর্ভুক্ত করুন। |
| `debug` | `bool` | `False` | ডিবাগ লগিং সক্ষম করুন। |
| `save_logs` | `bool` | `False` | রুট `logs/` ডিরেক্টরির অধীনে DEBUG-লেভেলের লগ ফাইল সংরক্ষণ করুন। |
| `yes` | `bool` | `True` | প্রোগ্রাম্যাটিক এবং CI ব্যবহারের জন্য প্রম্পটগুলো অটো-কনফার্ম করুন। |
| `add_disclaimer` | `bool` | `False` | অনূদিত Markdown এবং নোটবুকগুলিতে মেশিন অনুবাদ ডিসক্লেইমার যোগ করুন। |
| `translations_dir` | `str \| None` | `None` | কাস্টম টেক্সট অনুবাদ আউটপুট ডিরেক্টরি। রিলেটিভ পাথগুলো প্রতিটি রুটের বিরুদ্ধে রেজল্ভ করে। |
| `image_dir` | `str \| None` | `None` | কাস্টম অনূদিত ইমেজ আউটপুট ডিরেক্টরি। রিলেটিভ পাথগুলো প্রতিটি রুটের বিরুদ্ধে রেজল্ভ করে। |
| `root_dirs` | `Iterable[str] \| None` | `None` | একরকম আউটপুট সেটিংস শেয়ার করা একাধিক রুট। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | স্পষ্ট `(root_dir, translations_dir)` জোড়া। `root_dirs` এর উপরে অগ্রাধিকার গ্রহণ করে। |
| `repo_url` | `str \| None` | `None` | README ভাষা টেবিল নির্দেশনা রেন্ডার করার সময় ব্যবহৃত রিপোজিটরি URL। |
| `glossaries` | `Iterable[str] \| None` | `None` | অনুবাদের সময় সংরক্ষণ করার জন্য গ্লোসারি টার্মসমূহ। ডুপ্লিকেট এবং ফাঁকা টার্মগুলো নরমালাইজ করা হয়। |
| `dry_run` | `bool` | `False` | ফাইল না লিখে অনুবাদের পরিমাণ অনুমান করুন এবং মাইগ্রেশন আচরণ প্রিভিউ করুন। |

## রিভিউ প্যারামিটারসমূহ

`run_review` ইচ্ছাকৃতভাবে যেখানে সম্ভব `run_translation` সিগন্যেচারের অনুকরণ করে যাতে অটোমেশন অনুবাদ এবং রিভিউ ওয়ার্কফ্লোগুলোর মধ্যে ন্যূনতম শাখন করা ছাড়াই স্যুইচ করতে পারে।

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | রিভিউ করার লক্ষ্য ভাষা ফোল্ডারগুলো। স্পেস-সেপারেটেড স্ট্রিং এবং ইটারেবলগুলো গ্রহণযোগ্য। `"all"` প্রত্যেক আবিষ্কৃত অনুবাদ ভাষা রিভিউ করে। |
| `root_dir` | `str` | `"."` | একক রিভিউ টার্গেটের জন্য প্রজেক্ট রুট। যখন `root_dirs` বা `groups` সরবরাহ করা হয় তখন উপেক্ষা করা হয়। |
| `markdown` | `bool` | `False` | Markdown এবং MDX সোর্স ফাইলগুলো অন্তর্ভুক্ত করুন। |
| `notebook` | `bool` | `False` | Jupyter নোটবুক সোর্স ফাইলগুলো অন্তর্ভুক্ত করুন। |
| `images` | `bool` | `False` | অনুবাদ অপশনগুলোর সঙ্গে প্যারিটি রক্ষার জন্য সংরক্ষিত। Markdown থেকে ইমেজের লিঙ্ক রেফারেন্সগুলো চেক করা হয়। |
| `translations_dir` | `str \| None` | `None` | কাস্টম টেক্সট অনুবাদ আউটপুট ডিরেক্টরি। আপেক্ষিক পথগুলি প্রতিটি রুটের ভিত্তিতে সমাধান করা হবে। |
| `root_dirs` | `Iterable[str] \| None` | `None` | একাধিক রুট যা একই আউটপুট সেটিংস ভাগ করে। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | স্পষ্ট (root_dir, translations_dir) জোড়া। এটি `root_dirs`-এর উপর অগ্রাধিকার দেয়। |
| `changed_from` | `str \| None` | `None` | Git ref যা পরিবর্তিত উৎস ফাইলগুলির জন্য পর্যালোচনা সীমাবদ্ধ করতে ব্যবহৃত হয়। |
| `output_format` | `str` | `"text"` | রিভিউ আউটপুট ফরম্যাট। সমর্থিত মানগুলো হলো `"text"` এবং `"github"`। |
| `fail_on_warnings` | `bool` | `False` | সতর্কতাগুলিকে ত্রুটির পাশাপাশি ব্যর্থতা হিসেবে বিবেচনা করুন। |
| `debug` | `bool` | `False` | ডিবাগ লগিং সক্ষম করুন। |
| `save_logs` | `bool` | `False` | রুট `logs/` ডিরেক্টরির অধীনে DEBUG-স্তরের লগ ফাইল সংরক্ষণ করুন। |

If none of `markdown`, `notebook`, or `images` are set, the API reviews Markdown, notebooks, and image link references where applicable. Review does not call an LLM provider and does not require API keys.

## কনফিগারেশন প্রয়োজনীয়তা

প্রোভাইডার-সমর্থিত অনুবাদ API-গুলোকে অনুবাদ শুরু করার আগে প্রোভাইডার কনফিগারেশন প্রয়োজন:

- Markdown এবং নোটবুক অনুবাদের জন্য একটি LLM প্রদানকারী প্রয়োজন। Azure OpenAI বা OpenAI কোন একটিকে কনফিগার করুন।
- ইমেজ অনুবাদের জন্য LLM প্রদানকারীর পাশাপাশি Azure AI Vision প্রয়োজন।
- `run_translation` প্রকল্প অনুবাদ শুরু হওয়ার আগে হালকা সংযোগ পরীক্ষা চালায়।
- এজেন্ট-সহায়িত `start_*_agent_translation` এবং `finish_*_agent_translation` API-গুলো Co-op Translator LLM প্রদানকারীদের কল করে না। হোস্ট অ্যাপ্লিকেশন বা MCP এজেন্ট প্রস্তুত করা চাঙ্কগুলো অনুবাদ করে।
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, এবং `run_review` নির্ধারিত আচরণ এবং এগুলোর জন্য প্রদানকারী ক্রিডেনশিয়াল প্রয়োজন নেই।

Required Azure OpenAI variables:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Required OpenAI variables:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

Required Azure AI Vision variables for image translation:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` নির্ধারিত আচরণ এবং এর জন্য Azure OpenAI, OpenAI, বা Azure AI Vision কনফিগারেশন প্রয়োজন নেই।

## আচরণ নোট

- কনটেন্ট অনুবাদ API-গুলো অনুবাদকে প্রকল্প পাথ পুনঃলিখন থেকে আলাদা রাখে। যখন অনুবাদিত কনটেন্টে প্রকল্প-সাপেক্ষ লিঙ্কগুলো লক্ষ্য অবস্থানের জন্য সামঞ্জস্য করা প্রয়োজন, তখন স্পষ্টভাবে `rewrite_markdown_paths` বা `rewrite_notebook_paths` কল করুন।
- প্রকল্প অর্কেস্ট্রেশন API-গুলো কনটেন্ট অনুবাদের চারপাশে প্রকল্পের আচরণ যোগ করে, যার মধ্যে রয়েছে ফাইল সনাক্তকরণ, লিখন, পথ পুনঃলিখন, মেটাডেটা, ক্লিনআপ, এবং ঐচ্ছিক ডিসক্লেইমার।
- `run_translation` Click মারফত অগ্রগতি ও অনুমান সারসংক্ষেপ প্রিন্ট করে, CLI ব্যবহারকারীর অভিজ্ঞতার সাথে মেলে।
- `dry_run=True` ভার্চুয়াল README আপডেট ব্যবহার করে অনুমান গণনা করে, কিন্তু README বা অনুবাদ ফাইলগুলো লেখে না।
- `groups` ধারাবাহিকভাবে প্রক্রিয়াজাত করা হয়। কাজ শুরু হওয়ার আগে একটি একক সমষ্টিগত অনুমান প্রিন্ট করা হয়।
- ইমেজ অনুবাদ নির্বাচিত হলে, Vision কনফিগারেশন অনুপস্থিত থাকলে অনুবাদ শুরু হওয়ার আগে একটি ত্রুটি সৃষ্টি হয়।
- বিদ্যমান অ্যালিয়াস-ভিত্তিক ভাষা ফোল্ডারগুলি সনাক্ত করা হয় এবং রানটির অংশ হিসেবে এগুলো ক্যানোনিকাল ভাষা ফোল্ডার নামগুলিতে মাইগ্রেট করা যেতে পারে।
- `run_review` অনুবাদিত ফাইল অনুপস্থিত, অনুবাদ মেটাডেটা অনুপস্থিত বা স্টেল, ত্রুটিপূর্ণ Markdown frontmatter/code fences, এবং অবৈধ অনুবাদিত নোটবুক JSON-এর ক্ষেত্রে ব্যর্থ হয়।
- `run_review` ডিফল্টভাবে স্থানীয় Markdown এবং ইমেজ লিংক টার্গেট অনুপস্থিতিকে সতর্কতা হিসেবে রিপোর্ট করে।

## অভ্যন্তরীণ কল পথ

The API delegates to the same core implementation used by the CLI:

অনুবাদ:

1. `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, or `translate_image_content` ইন-মেমরি অনুবাদের জন্য।
2. `co_op_translator.api.translation.rewrite_markdown_paths` or `rewrite_notebook_paths` স্পষ্ট পথ পোস্ট-প্রসেসিংয়ের জন্য।
3. `co_op_translator.api.translation.run_translation` পূর্ণ প্রকল্প অর্কেস্ট্রেশনের জন্য।
4. `co_op_translator.config.Config`, `LLMConfig`, and `VisionConfig`.
5. `co_op_translator.core.project.ProjectTranslator`.
6. `co_op_translator.core.project.TranslationManager`.
7. ফোকাসড প্রকল্প অনুবাদ মিক্সইনগুলো Markdown, নোটবুক, এবং ইমেজের জন্য।
8. Markdown, নোটবুক, টেক্সট, এবং ইমেজ অনুবাদকরা `co_op_translator.core`-এর অধীনে।

রিভিউ:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. ডিটারমিনিস্টিক চেকগুলো `co_op_translator.review.checks`-এর অধীনে

নীচের ক্লাসগুলো রক্ষণাবেক্ষকদের জন্য উপযোগী, তবে প্যাকেজ-স্তরের স্থিতিশীল API হিসেবে এক্সপোর্ট করা হয় না।

| ক্লাস | মডিউল | দায়িত্ব |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | প্রকল্প-স্তরের অনুবাদ, ডিরেক্টরি ব্যবস্থাপনা, প্রতি-ভাষার মেটাডেটা স্বাভাবিককরণ, এবং Markdown, নোটবুক, ও ইমেজ অনুবাদকদের কাছে কর্ম হস্তান্তর করে। |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, নোটবুক, ইমেজ, স্টেল সনাক্তকরণ, এবং অনুবাদ মেটাডেটা আপডেটগুলোর জন্য অ্যাসিঙ্ক ফাইল প্রক্রিয়াকরণ কাজগুলো করে। |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ফাইল পড়া, কনটেন্ট অনুবাদ, পথ পুনঃলিখন, মেটাডেটা, ডিসক্লেইমার, এবং লিখন সমন্বয় করে। |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | নোটবুক ফাইল পড়া, Markdown-সেল অনুবাদ, পথ পুনঃলিখন, মেটাডেটা, ডিসক্লেইমার, এবং লিখন সমন্বয় করে। |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | সোর্স ইমেজ আবিষ্কার, ইমেজ অনুবাদ, আউটপুট পথ, মেটাডেটা, এবং লিখন সমন্বয় করে। |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | অনুবাদকৃত Markdown জোড়া খুঁজে বের করে, অনুবাদের গুণমান মূল্যায়ন করে, এবং কম-কনফিডেন্স মেরামত ওয়ার্কফ্লোর জন্য কনফিডেন্স মেটাডেটা পড়ে। |
| `ReviewRunner` | `co_op_translator.review.runner` | সোর্স ফাইল, লক্ষ্য ভাষা, এবং কনফিগারকৃত অনুবাদ রুটগুলোর জুড়ে নির্ধারিত পর্যালোচনা চেকগুলো সমন্বয় করে। |
| `ReviewTarget` | `co_op_translator.review.targets` | একটি সোর্স রুট এবং সেই রুটের জন্য পর্যালোচিত অনুবাদ আউটপুট ডিরেক্টরির বর্ণনা দেয়। |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | লিগ্যাসি অ্যালিয়াস ভাষা ফোল্ডার সনাক্ত করে এবং ক্যানোনিকাল BCP 47 ফোল্ডার মাইগ্রেশন পরিকল্পনা প্রস্তুত করে। |
| `Config` | `co_op_translator.config.base_config` | `.env` ফাইল লোড করে এবং প্রয়োজনীয় LLM এবং ঐচ্ছিক Vision প্রদানকারীরা কনফিগার করা আছে কিনা যাচাই করে। |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI বা OpenAI স্বয়ংক্রিয়ভাবে সনাক্ত করে, প্রয়োজনীয় পরিবেশ পরিবর্তনশীলগুলি যাচাই করে, এবং প্রদানকারী সংযোগ পরীক্ষাগুলো চালায়। |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision কনফিগারেশন সনাক্ত করে এবং ইমেজ অনুবাদের জন্য সংযোগ পরীক্ষা চালায়। |