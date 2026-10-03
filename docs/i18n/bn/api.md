# পাইথন API

স্থিতিশীল পাবলিক পাইথন API `co_op_translator.api` থেকে রফতানি করা হয়। বেশিরভাগ ইন্টিগ্রেশন নিম্নলিখিত ওয়ার্কফ্লোগুলির একটি ব্যবহার করে:

| পরিস্থিতি | কখন এটি ব্যবহার করবেন | প্রধান API গুলি |
| --- | --- | --- |
| একক ফাইল বা ডকুমেন্ট অনুবাদ করুন | আপনার অ্যাপ্লিকেশন উৎস বিষয়বস্তু পড়ে, Co-op Translator-কে অনুবাদের জন্য কল করে, এবং ফলাফল কোথায় সংরক্ষণ করবেন তা নির্ধারণ করে। | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| হোস্ট-এজেন্ট অনুবাদের জন্য বিষয়বস্তু প্রস্তুত করুন | আপনার MCP হোস্ট বা অ্যাপ্লিকেশন মডেল চাঙ্কগুলো অনুবাদ করবে, আর Co-op Translator চাঙ্কিং এবং পুনর্গঠন পরিচালনা করবে। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| একটি সম্পূর্ণ রেপো অনুবাদ করুন | আপনি চাইলে পাইথন API CLI-এর মতো আচরণ করবে এবং ডিসকভারি, আউটপুট পাথ, মেটাডেটা, ক্লিনআপ এবং লেখাগুলি পরিচালনা করবে। | `run_translation` |

অধিকাংশ নিম্নস্তরের মডিউল যেমন `core`, `config`, `review`, এবং `utils` এগুলির API এন্ট্রি পয়েন্টগুলিতে ব্যবহৃত বাস্তবায়ন বিবরণ।

MCP ক্লায়েন্টরা একই পাবলিক API [MCP Server](mcp.md) -এর মাধ্যমে ব্যবহার করে। সরাসরি পাইথন কল করার সময় এই পৃষ্ঠা ব্যবহার করুন, এবং যদি আপনি Co-op Translator কে কোনো এজেন্ট বা এডিটরে উন্মুক্ত করেন তাহলে MCP গাইডটি দেখুন। CLI, পাইথন API, এবং MCP এর মধ্যে সিদ্ধান্ত নেওয়ার সময় [Choose Your Workflow](workflows.md) থেকে শুরু করুন।

## প্রথমবারের API প্রবাহ

যদি আপনি পাইথন কোড থেকে Co-op Translator কল করেন তাহলে এখান থেকেই শুরু করুন:

1. [Configuration](configuration.md) এ বর্ণিত হিসাবে একটি LLM প্রদানকারী কনফিগার করুন, যদি না আপনি কেবল Markdown বা নোটবুক চাঙ্কগুলো হোস্ট-এজেন্ট অনুবাদের জন্য প্রস্তুত করছেন।
2. সিদ্ধান্ত করুন আপনার অ্যাপ্লিকেশন কি ফাইল I/O পরিচালনা করবে।
3. যখন আপনার অ্যাপ্লিকেশন আলাদা ফাইল পড়ে এবং লেখে তখন কন্টেন্ট API ব্যবহার করুন।
4. যখন Co-op Translator-কে CLI-এর মতো একটি রেপো প্রসেস করতে দেবেন তখন `run_translation` ব্যবহার করুন।
5. স্বয়ংক্রিয়তায় নির্ধারিত যাচাই প্রয়োজন হলে অনুবাদের পরে `run_review` ব্যবহার করুন।

| লক্ষ্য | শুরু করার API |
| --- | --- |
| এক Markdown স্ট্রিং বা ফাইল অনুবাদ করুন | `translate_markdown_content` |
| একটি নোটবুক পে-লোড অনুবাদ করুন | `translate_notebook_content` |
| একটি ইমেজ অনুবাদ করুন | `translate_image_content` |
| হোস্ট এজেন্টকে Markdown বা নোটবুক চাঙ্ক অনুবাদ করতে দিন | `start_markdown_agent_translation` বা `start_notebook_agent_translation` |
| আউটপুট পাথ নির্ধারণের পরে অনুবাদ করা লিংকগুলো পুনরলিখন করুন | `rewrite_markdown_paths` বা `rewrite_notebook_paths` |
| একটি সম্পূর্ণ রেপো অনুবাদ করুন | `run_translation` |
| অনুবাদকৃত আউটপুট পর্যালোচনা করুন | `run_review` |

## পরিস্থিতি ১: পৃথক ফাইল বা ডকুমেন্ট অনুবাদ

এই ওয়ার্কফ্লোটি ব্যবহার করুন যখন আপনার কাছে ইতিমধ্যে একটি ফাইল, এডিটর বাফার, নোটবুক পে-লোড, MCP রিকোয়েস্ট, বা কাস্টম পাইপলাইন ইনপুট রয়েছে। আপনার কোড ফাইল I/O এর দায়িত্ব নেয়:

1. উৎস বিষয়বস্তু পড়ুন।
2. একটি কন্টেন্ট অনুবাদ API কল করুন।
3. যদি অনুবাদকৃত বিষয়বস্তু প্রকল্প অনুবাদ ফোল্ডারে লেখা হবে, তবে ঐচ্ছিকভাবে একটি পাথ পুনরলিখন API কল করুন।
4. আপনার অ্যাপ্লিকেশন থেকে ফলাফল সংরক্ষণ বা রিটার্ন করুন।

কন্টেন্ট অনুবাদ API গুলো প্রকল্প ডিসকভারি চালায় না, মেটাডেটা লিখে না, ডিসক্লেমার সংযুক্ত করে না, এবং স্বয়ংক্রিয়ভাবে লিংক পুনরলিখন করে না।

### Markdown ফাইল

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

যদি অনুবাদকৃত Markdown Co-op Translator প্রকল্প লেআউটে না থাকে, তাহলে `rewrite_markdown_paths` এড়িয়ে সরাসরি অনুবাদকৃত স্ট্রিং সেভ করুন।

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

`translate_notebook_content` Markdown সেলগুলো অনুবাদ করে এবং নন-Markdown সেলগুলো অক্ষুণ্ণ রাখে। পাথ পুনরলিখন কেবল Markdown সেলগুলিতেই প্রয়োগ করা হয়।

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

`translate_image_content` উৎস ইমেজ পড়ে এবং একটি রেন্ডার করা `PIL.Image.Image` রিটার্ন করে। এটি অনুবাদকৃত ইমেজ মেটাডেটা লিখে না।

## পরিস্থিতি ২: একটি সম্পূর্ণ রেপোসিটরি অনুবাদ করা

এই ওয়ার্কফ্লোটি ব্যবহার করুন যখন আপনি চাইবেন পাইথন API `translate` CLI-এর মতো আচরণ করুক। `run_translation` সমর্থিত ফাইলগুলো আবিষ্কার করে, নির্বাচিত কন্টেন্ট টাইপগুলো অনুবাদ করে, পাথ পুনরলিখন করে, আউটপুট ফাইলগুলো লেখে, মেটাডেটা আপডেট করে, এবং ক্লিনআপের মত অনুবাদ রক্ষণাবেক্ষণের কাজগুলি করে।

`run_translation` প্রজেক্ট অর্কেস্ট্রেশনের পছন্দসই এন্ট্রি পয়েন্ট। একই আচরণ সহ কম্প্যাটেবল এলিয়াস হিসাবে `translate_project` রফতানি করা হয়েছে।

বর্তমান রেপোতে Markdown ফাইলগুলো কোরিয়ান এবং জাপানি ভাষায় অনুবাদ করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko ja",
    markdown=True,
)
```

নির্দিষ্ট প্রজেক্ট রুট থেকে কেবল নোটবুকগুলো অনুবাদ করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="fr",
    root_dir="./my-course",
    notebook=True,
)
```

ফাইল না লিখে অনুবাদের পরিমাণ পূর্বদর্শন করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="es de",
    root_dir="./my-course",
    markdown=True,
    dry_run=True,
)
```

একটি ইন্টিগ্রেশনের জন্য কাঠামোবদ্ধ প্রগ্রেস ইভেন্ট রেকর্ড করুন:

```python
from co_op_translator.api import TranslationEvent, run_translation


def on_event(event: TranslationEvent) -> None:
    payload = event.to_dict()
    # পে-লোডটি আপনার জব-ইভেন্ট টেবিলে সংরক্ষণ করুন বা এটি আপনার UI-তে স্ট্রিম করুন।


run_translation(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
    progress_callback=on_event,
)
```

ইভেন্টগুলো ভার্সন-কৃত স্কিমা `co-op.translation.event.v1` ব্যবহার করে। ইন্টিগ্রেশনগুলোকে কনসোল টেক্সট বা `stage_label` নয়, বরং `type` এবং `stage_key` এর মত স্থিতিশীল ফিল্ডগুলোর উপর নির্ভর করতে বলা হয়।
depend on stable fields such as `type` and `stage_key`, not on human-facing
console text or `stage_label`.

এক কলেই একাধিক কন্টেন্ট রুট অনুবাদ করুন:

```python
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    root_dirs=["./docs", "./labs"],
)
```

অনুবাদগুলো স্পষ্ট আউটপুট গ্রুপে লিখুন:

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

প্রতিটি ভাষার জন্য একটি সাবডাইরেক্টরি থাকা উচিত হলে per-language প্লেসহোল্ডার ব্যবহার করুন:

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

যদি `markdown`, `notebook`, বা `images` এর কোনোটিই সেট না করা থাকে, তাহলে API সব সমর্থিত টাইপ অনুবাদ করে: Markdown, নোটবুক, এবং ইমেজ।

### একটি অনুবাদ স্টেট প্রদানকারীর মাধ্যমে গৃহীত মানব সম্পাদনা সংরক্ষণ করুন

ডিফল্টভাবে, Co-op Translator তার বিদ্যমান ফাইল-স্তরের আচরণ বজায় রাখে: যখন একটি Markdown উৎস স্টেইল হয়, সম্পূর্ণ অনুবাদকৃত ফাইলটি পুনরায় তৈরি করা হয়। হোস্টেড ইন্টিগ্রেশন ঐচ্ছিকভাবে একটি `TranslationStateProvider` পাস করতে পারে যাতে পরিবর্তন না হওয়া সোর্স ব্লকগুলোর মানব সম্পাদনা সংরক্ষিত থাকে।
Markdown উৎস যদি পুরনো থাকে, সম্পূর্ণ অনূদিত ফাইলটি পুনরায় তৈরি করা হয়। হোস্টেড
ইন্টিগ্রেশনগুলো ঐচ্ছিকভাবে একটি `TranslationStateProvider` পাস করতে পারে যাতে মানব
পরিবর্তিত নয় এমন সোর্স ব্লকগুলোর সম্পাদনা সংরক্ষিত থাকে।

প্রদানকারী শেষ গৃহীত সোর্স/টার্গেট জোড়া সরবরাহ করে এবং প্রতিটি নতুন প্রার্থী রেকর্ড করে।
গ্রহণ আরেকটি ইন্টিগ্রেশনের দায়িত্বেই থাকে—উদাহরণস্বরূপ,
অনুবাদ পুল রিকোয়েস্ট মার্জ হওয়ার পরে:

```python
from pathlib import Path

from co_op_translator.api import (
    TranslationBaseline,
    TranslationUpdate,
    run_translation,
)


class DatabaseTranslationState:
    def load_baseline(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
    ) -> TranslationBaseline | None:
        row = load_accepted_translation(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
        )
        if row is None:
            return None
        return TranslationBaseline(
            source_text=row.source_text,
            target_text=row.target_text,
            revision=row.accepted_revision,
        )

    def record_candidate(
        self,
        *,
        source_path: Path,
        translation_path: Path,
        language_code: str,
        source_text: str,
        target_text: str,
        update: TranslationUpdate,
    ) -> None:
        save_translation_candidate(
            source_path=source_path,
            translation_path=translation_path,
            language_code=language_code,
            source_text=source_text,
            target_text=target_text,
            mode=update.mode,
            fallback_reason=update.fallback_reason,
        )


run_translation(
    language_codes="ko",
    root_dir="./course",
    markdown=True,
    translation_state_provider=DatabaseTranslationState(),
)
```

যেসব Markdown ফাইলের একটি বৈধ অনুমোদিত বেসলাইন আছে, Co-op Translator সমন্বয় করে
শীর্ষ-স্তরের Markdown ব্লকগুলিকে। অপরিবর্তিত সোর্স ব্লকগুলি বর্তমান অনূদিত
ব্লকগুলো, মানুষের করা সম্পাদনাসহ; পরিবর্তিত বা যোগ করা সোর্স ব্লকগুলো অনুবাদের জন্য পাঠানো হয়
অনুবাদের জন্য; মুছে ফেলা সোর্স ব্লকগুলো মুছে ফেলা হয়। যদি সামঞ্জস্য অস্পষ্ট হয়,
টার্গেট কাঠামো পরিবর্তিত হয়েছে, কোনো ব্লক অনুবাদ অবৈধ, অথবা কোনো বেসলাইন
উপলব্ধ না থাকে, Co-op Translator নিরাপদভাবে বিদ্যমান সম্পূর্ণ-ফাইল
অনুবাদ পথ।

এই API ডকুমেন্ট অনুবাদের অবস্থা সংরক্ষণ করে, ক্রস-ডকুমেন্ট ফ্রেজ বা
সেগমেন্ট অনুবাদ মেমরি। এটি বর্তমানে Markdown প্রকল্প
অনুবাদ। নোটবুক এবং চিত্রের আচরণ অপরিবর্তিত আছে। পাস করলে `update=True`
এখনও সম্পূর্ণ পুনরায় তৈরি করার অনুরোধ করে।

যদি এক বা একাধিক ফাইল অনুবাদ করা না যায়, `run_translation` একটি
`RuntimeError` উত্থাপন করে প্রকল্পের ওয়ার্কফ্লো শেষ হওয়ার পরে, রিপোর্ট করার পরিবর্তে একটি
সফল রান যেখানে আউটপুট অনুপস্থিত। ইন্টিগ্রেশনগুলোকে এটিকে একটি ব্যর্থ
কাজ হিসেবে গণ্য করতে হবে এবং পূর্বে গৃহীত অনুবাদ অবস্থা বজায় রাখতে হবে।

## অনুবাদকৃত আউটপুট পর্যালোচনা

`run_review` LLM বা Vision ক্রেডেনশিয়াল ছাড়াই নির্ধারিত অনুবাদ চেক চালায়।

!!! note "বেটা"
    `run_review` একটি বেটা নির্ধারিত রিভিউ API। এটি মডেল প্রদানকারীদের কল করে না বা ফাইল লেখে না, তবে চেক এবং ইস্যু স্কিমাগুলো পরিবর্তিত হতে পারে।

```python
from co_op_translator.api import run_review

run_review(
    language_codes="ko ja",
    root_dir="./my-course",
    markdown=True,
    notebook=True,
)
```

README-কে কেবল অনুবাদ করার পরে, পর্যালোচনার জন্য একই স্কোপ ব্যবহার করুন:

```python
run_review(language_codes="ko", root_dir="./my-course", readme_only=True)
```

`readme_only=True` কনফিগার করা प्रत्येक সোর্স রুটের অধীনে কেবল `README.md` রিভিউ করে, কাস্টম `groups` এবং আউটপুট ডিরেক্টরিগুলো সহ। অন্যান্য ডকুমেন্ট এবং নেস্টেড README-গুলো বাদ দেয়া হয়। একটি অনুপস্থিত সোর্স README `ValueError` উত্থাপন করে; ব্যর্থ অনুবাদ চেকগুলো `RuntimeError` উত্থাপন করে।
including custom `groups` and output directories. Other documents and nested
READMEs are excluded. A missing source README raises `ValueError`; failed
translation checks raise `RuntimeError`.

শুধুমাত্র সেই ফাইলগুলো পর্যালোচনা করুন যেগুলো একটি বেস রেফের বিরুদ্ধে পরিবর্তিত হয়েছে এবং GitHub-শৈলীর আউটপুট প্রিন্ট করুন:

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

ফাইল লেখা ছাড়া Markdown কন্টেন্ট অনুবাদ করুন:

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

Markdown লিংক অনুবাদ এবং পুনরলিখন করুন:

```python
import asyncio

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


async def main() -> None:
    translated = await translate_markdown_content(
        "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

পাইথন থেকে একটি রেপো অনুবাদ করুন:

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

গ্লসারি টার্ম সংরক্ষণ করুন:

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

## পাবলিক এন্ট্রি পয়েন্ট

```python
from co_op_translator.api import (
    ImageTranslationOptions,
    MarkdownTranslationOptions,
    NotebookTranslationOptions,
    TranslationBaseline,
    TranslationStateProvider,
    TranslationUpdate,
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

::: co_op_translator.api.TranslationBaseline

::: co_op_translator.api.TranslationStateProvider

::: co_op_translator.api.TranslationUpdate

::: co_op_translator.api.run_translation

::: co_op_translator.api.translate_project

::: co_op_translator.api.run_review

## কন্টেন্ট অনুবাদ API গুলি

কন্টেন্ট অনুবাদ API গুলো সেই ইন্টিগ্রেশনগুলোর জন্য উদ্দেশ্যভিত্তিক যা ইতিমধ্যে মেমরিতে কন্টেন্ট রাখে, যেমন একটি এডিটর এক্সটেনশন, MCP টুল, নোটবুক প্রসেসর, বা কাস্টম পাইপলাইন।

| Function | Input | Output | File I/O | Notes |
| --- | --- | --- | --- | --- |
| `translate_markdown_content` | Markdown `str` | Markdown `str` | No | Async. Markdown কন্টেন্টই অনুবাদ করে। এটি লিংক পুনরলিখন করে না, মেটাডেটা লিখে না, বা ডিসক্লেমার যুক্ত করে না। |
| `translate_notebook_content` | Notebook JSON `str` or `dict` | Notebook JSON `str` | No | Async. Markdown সেলগুলো অনুবাদ করে এবং নন-Markdown সেলগুলো অক্ষুণ্ণ রাখে। এটি লিংক পুনরলিখন করে না, মেটাডেটা লিখে না, বা ডিসক্লেমার যুক্ত করে না। |
| `translate_image_content` | Image path | `PIL.Image.Image` | Reads source image only | Synchronous. ইমেজ টেক্সট বের করে অনুবাদ করে, তারপর একটি রেন্ডার করা ইমেজ রিটার্ন করে। এটি অনুবাদকৃত ইমেজ মেটাডেটা সেভ করে না। |

`translate_markdown_content` এবং `translate_notebook_content` তাদের অপশনগুলোর মাধ্যমে ঐচ্ছিক `source_path` গ্রহণ করে। পাথটি অনুবাদককে প্রসঙ্গ হিসেবে পাঠানো হয়; কলকারীরা অনুবাদের পরে প্রকল্প-নির্দিষ্ট পাথ পুনরলিখনের জন্য দায়ী থাকে।

```python
from co_op_translator.api import MarkdownTranslationOptions, translate_markdown_content

translated = await translate_markdown_content(
    document,
    "ko",
    MarkdownTranslationOptions(source_path="docs/guide.md"),
)
```

একই অপশনগুলো ডিকশনারি হিসেবে দেওয়া যেতে পারে:

```python
translated = await translate_markdown_content(
    document,
    "ko",
    {"source_path": "docs/guide.md"},
)
```

## এজেন্ট-সহায়ক অনুবাদ API গুলি

এজেন্ট-সহায়ক API গুলো Co-op Translator থেকে কনফিগারকৃত LLM প্রদানকারীকে কল করে না। এগুলো হোস্ট এজেন্টকে অনুবাদ করার জন্য Markdown বা নোটবুক চাঙ্কগুলো প্রস্তুত করে, তারপর অনুবাদ করা চাঙ্কগুলো থেকে চূড়ান্ত কন্টেন্ট পুনর্গঠন করে।

| Function | Purpose |
| --- | --- |
| `start_markdown_agent_translation` | চাঙ্ক, প্রম্পট, এবং পুনর্গঠন স্টেট সহ একটি স্ব-স্বতন্ত্র Markdown জব রিটার্ন করে। |
| `finish_markdown_agent_translation` | একটি জব এবং হোস্ট-এজেন্ট অনুবাদ করা চাঙ্ক থেকে Markdown পুনর্গঠন করে। |
| `start_notebook_agent_translation` | হোস্ট-এজেন্ট অনুবাদের জন্য Markdown-সেল চাঙ্ক সহ একটি নোটবুক জব রিটার্ন করে। |
| `finish_notebook_agent_translation` | কোড সেল, আউটপুট, এবং মেটাডেটা অক্ষুণ্ণ রেখে নোটবুক JSON পুনর্গঠন করে। |

এই ওয়ার্কফ্লোটি মূলত MCP হোস্টগুলোর জন্য উদ্দেশ্যভিত্তিক। যদি আপনি Co-op Translator পরিচালিত প্রদানকারী কল সহ প্রোডাকশন রেপো অনুবাদ চান, তাহলে `translate_markdown_content`, `translate_notebook_content`, বা `run_translation` ব্যবহার করুন।

## পাথ পুনরলিখন API গুলি

পাথ পুনরলিখন API গুলো কোনো অনুবাদ করে না। কলকারীরা যখন সোর্স পাথ, অনুবাদকৃত টার্গেট পাথ, এবং প্রকল্প লেআউট জানে তখন এগুলো লিংক এবং frontmatter পাথ আপডেট করে।

| Function | Scope | Notes |
| --- | --- | --- |
| `rewrite_markdown_paths` | Markdown বডি এবং frontmatter | অনুবাদকৃত টার্গেটের জন্য Markdown লিংক এবং সমর্থিত frontmatter পাথ ফিল্ডগুলো পুনরলিখন করে। |
| `rewrite_notebook_paths` | নোটবুক JSON-এ Markdown সেলগুলো | প্রতিটি Markdown সেলে Markdown পাথ পুনরলিখন প্রয়োগ করে এবং নন-Markdown সেলগুলো অপরিবর্তিত রাখে। |

`policy` আর্গুমেন্টটি একটি ডিকশনারি হতে পারে যা এই ফিল্ডগুলো রয়েছে:

| Field | Required | Purpose |
| --- | --- | --- |
| `language_code` | হ্যাঁ | টার্গেট ভাষার কোড, যেমন `"ko"` বা `"pt-BR"`। |
| `root_dir` | না | সোর্স প্রকল্প রুট। ডিফল্ট `"."`। |
| `translations_dir` | না | টেক্সট অনুবাদ আউটপুট ডিরেক্টরি। ডিফল্ট `root_dir`-এর অধীনে `translations`। |
| `translated_images_dir` | না | অনুবাদকৃত ইমেজ আউটপুট ডিরেক্টরি। ডিফল্ট `root_dir`-এর অধীনে `translated_images`। |
| `translation_types` | না | সক্রিয় অনুবাদ টাইপগুলো। ডিফল্ট হলে Markdown, নোটবুক, এবং ইমেজ। |
| `lang_subdir` | না | প্রতিটি ভাষা ফোল্ডারের অধীনে ঐচ্ছিক সাবডাইরেক্টরি। |

## প্রজেক্ট অনুবাদ প্যারামিটার

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `language_codes` | `str` | Required | স্পেস-বিভক্ত টার্গেট ভাষা কোড, যেমন `"ko ja fr"`, বা `"all"`। এলিয়াস কোডগুলো ক্যানোনিকাল BCP 47 মানে নর্মালাইজ করা হয়। |
| `root_dir` | `str` | `"."` | একক অনুবাদ টার্গেটের জন্য প্রজেক্ট রুট। `root_dirs` বা `groups` সরবরাহ করলে উপেক্ষা করা হয়। |
| `update` | `bool` | `False` | নির্বাচিত ভাষাগুলোর বিদ্যমান অনুবাদগুলি মুছে ফেলে এবং পুনরায় তৈরি করে। |
| `images` | `bool` | `False` | ইমেজ অনুবাদ অন্তর্ভুক্ত করুন। Azure AI Vision কনফিগারেশন প্রয়োজন। |
| `markdown` | `bool` | `False` | Markdown অনুবাদ অন্তর্ভুক্ত করুন। |
| `notebook` | `bool` | `False` | Jupyter নোটবুক অনুবাদ অন্তর্ভুক্ত করুন। |
| `debug` | `bool` | `False` | ডিবাগ লগিং সক্রিয় করুন। |
| `save_logs` | `bool` | `False` | রুট `logs/` ডিরেক্টরির অধীনে DEBUG-লেভেলের লগ ফাইল সেভ করুন। |
| `yes` | `bool` | `True` | প্রোগ্রাম্যাটিক এবং CI ব্যবহারের ক্ষেত্রে প্রম্পটগুলো স্বয়ংক্রিয়ভাবে নিশ্চিত করে। |
| `add_disclaimer` | `bool` | `False` | অনুবাদকৃত Markdown এবং নোটবুকগুলিতে মেশিন অনুবাদ ডিসক্লেইমার যোগ করুন। |
| `translations_dir` | `str \| None` | `None` | কাস্টম টেক্সট অনুবাদ আউটপুট ডিরেক্টরি। আপেক্ষিক পথগুলো প্রতিটি root-এর বিরুদ্ধে সমাধান করা হয়। |
| `image_dir` | `str \| None` | `None` | কাস্টম অনূদীত ইমেজ আউটপুট ডিরেক্টরি। আপেক্ষিক পথগুলো প্রতিটি root-এর বিরুদ্ধে সমাধান করা হয়। |
| `root_dirs` | `Iterable[str] \| None` | `None` | একাধিক root যা একই আউটপুট সেটিংস শেয়ার করে। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | স্পষ্ট `(root_dir, translations_dir)` জোড়া। এটি `root_dirs`-এর উপর অগ্রাধিকার পায়। |
| `repo_url` | `str \| None` | `None` | README ভাষা টেবিল নির্দেশনা রেন্ডার করার সময় ব্যবহৃত Repository URL। |
| `glossaries` | `Iterable[str] \| None` | `None` | অনুবাদের সময় অপরিবর্তিত রাখার জন্য গ্লসারি টার্ম। পুনরাবৃত্তি এবং খালি টার্মগুলো স্বাভাবিকীকরণ করা হয়। |
| `dry_run` | `bool` | `False` | ফাইল লেখার ছাড়াই অনুবাদ পরিমাণ অনুমান করে এবং মাইগ্রেশন আচরণ প্রিভিউ করে। |
| `translation_state_provider` | `TranslationStateProvider \| None` | `None` | ইনক্রিমেন্টাল Markdown আপডেটগুলোর জন্য ঐচ্ছিক accepted-baseline এবং candidate persistence অ্যাডাপ্টার। এটিকে বাদ দিলে বিদ্যমান সম্পূর্ণ-ফাইল আচরণ বজায় থাকে। |

## পর্যালোচনা পরামিতি

`run_review` যেখানে সম্ভব `run_translation` সিগনেচারের অনুকরণ করে, যাতে অটোমেশন সামান্য শাখা-বিভাগে অনুবাদ এবং পর্যালোচনা ওয়ার্কফ্লোর মধ্যে স্যুইচ করতে পারে।

| প্যারামিটার | টাইপ | ডিফল্ট | উদ্দেশ্য |
| --- | --- | --- | --- |
| `language_codes` | `str \| Iterable[str]` | `"all"` | পর্যালোচনার লক্ষ্য ভাষা ফোল্ডারসমূহ। স্পেস-দ্বারা আলাদা করা স্ট্রিং এবং iterable গ্রহণ করা হয়। `"all"` সন্ধানকৃত প্রতিটি অনুবাদ ভাষা পর্যালোচনা করে। |
| `root_dir` | `str` | `"."` | একক পর্যালোচনা টার্গেটের জন্য প্রজেক্ট root। `root_dirs` বা `groups` সরবরাহ করা হলে উপেক্ষা করা হয়। |
| `markdown` | `bool` | `False` | Markdown এবং MDX সোর্স ফাইলগুলো অন্তর্ভুক্ত করুন। |
| `notebook` | `bool` | `False` | Jupyter নোটবুক সোর্স ফাইলগুলো অন্তর্ভুক্ত করুন। |
| `images` | `bool` | `False` | অনুবাদ অপশনগুলোর সমতা বজায় রাখার জন্য সংরক্ষিত। ছবির লিংক রেফারেন্সগুলো Markdown থেকে পরীক্ষা করা হয়। |
| `translations_dir` | `str \| None` | `None` | কাস্টম টেক্সট অনুবাদ আউটপুট ডিরেক্টরি। আপেক্ষিক পথগুলো প্রতিটি root-এর বিরুদ্ধে সমাধান করা হয়। |
| `root_dirs` | `Iterable[str] \| None` | `None` | একাধিক root যা একই আউটপুট সেটিংস শেয়ার করে। |
| `groups` | `Iterable[tuple[str, str \| None]] \| None` | `None` | স্পষ্ট `(root_dir, translations_dir)` জোড়া। এটি `root_dirs`-এর উপর অগ্রাধিকার পায়। |
| `changed_from` | `str \| None` | `None` | পর্যালোচনা সীমাবদ্ধ করার জন্য ব্যবহার করা Git ref, যা কেবল পরিবর্তিত সোর্স ফাইলগুলোকে পর্যালোচনা করে। |
| `readme_only` | `bool` | `False` | প্রতিটি সোর্স root-এর অধীনে শুধু `README.md` পর্যালোচনা করুন। একটি অনুপস্থিত সোর্স README হলে `ValueError` উত্থাপিত হয়। |
| `output_format` | `str` | `"text"` | পর্যালোচনা আউটপুট ফরম্যাট। সমর্থিত মানগুলো হল `"text"` এবং `"github"`। |
| `fail_on_warnings` | `bool` | `False` | সতর্কতাগুলোকেও ত্রুটির সাথে মিলিয়ে ব্যর্থতা হিসেবে গণ্য করুন। |
| `debug` | `bool` | `False` | ডিবাগ লগিং সক্রিয় করুন। |
| `save_logs` | `bool` | `False` | রুট `logs/` ডিরেক্টরির অধীনে DEBUG-স্তরের লগ ফাইলগুলো সংরক্ষণ করুন। |

`markdown`, `notebook`, বা `images` যেগুলোর কোনোটিই সেট না থাকলে, API যেখানে প্রযোজ্য সেখানে Markdown, নোটবুক এবং ইমেজ লিংক রেফারেন্সগুলো পর্যালোচনা করে। পর্যালোচনা কোনো LLM প্রদানকারীকে কল করে না এবং API কী প্রয়োজন পড়ে না।

## কনফিগারেশন প্রয়োজনীয়তা

প্রোভাইডার-সমর্থিত অনুবাদ API-গুলিকে অনুবাদ শুরু করার আগে প্রোভাইডার কনফিগারেশন প্রয়োজন:

- Markdown এবং নোটবুক অনুবাদের জন্য একটি LLM প্রদানকারী প্রয়োজন। Azure OpenAI, OpenAI, বা Anthropic কনফিগার করুন।
- ইমেজ অনুবাদের জন্য LLM প্রদানকারীর পাশাপাশি Azure AI Vision প্রয়োজন।
- `run_translation` প্রজেক্ট অনুবাদ শুরু হওয়ার আগে হালকা-ওজনের কানেক্টিভিটি চেক চালায়।
- এজেন্ট-সহায়িত `start_*_agent_translation` এবং `finish_*_agent_translation` API গুলো Co-op Translator LLM প্রদানকারীদের কল করে না। হোস্ট অ্যাপলিকেশন বা MCP এজেন্ট প্রস্তুত করা চাঙ্কগুলো অনুবাদ করে।
- `rewrite_markdown_paths`, `rewrite_notebook_paths`, এবং `run_review` নির্ণায়ক এবং প্রদানকারী ক্রেডেনশিয়াল প্রয়োজন হয় না।

প্রয়োজনীয় Azure OpenAI ভ্যারিয়েবলসমূহ:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

প্রয়োজনীয় OpenAI ভ্যারিয়েবলসমূহ:

```bash
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"
```

প্রয়োজনীয় Anthropic ভ্যারিয়েবলসমূহ:

```bash
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

`ANTHROPIC_BASE_URL` এবং `ANTHROPIC_MAX_TOKENS` ঐচ্ছিক। Co-op Translator 0.22.0 থেকে শুরু করে সব প্রোভাইডারের জন্য ডিফল্ট মডেল ক্লায়েন্ট হল Microsoft Agent Framework। Semantic Kernel সাময়িকভাবে `CO_OP_TRANSLATOR_MODEL_CLIENT="semantic-kernel"` দিয়ে এখনও নির্বাচন করা যায়, কিন্তু তা করলে একটি ডিপ্রিকেশন সতর্কবার্তা প্রদর্শিত হয়; পর্যায়ক্রমিক অপসারণ পরিকল্পনার জন্য [configuration](configuration.md#model-client-backend) দেখুন।

ইমেজ অনুবাদের জন্য প্রয়োজনীয় Azure AI Vision ভ্যারিয়েবলসমূহ:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

`run_review` নির্ণায়ক এবং LLM বা Azure AI Vision কনফিগারেশন প্রয়োজন হয় না।

## আচরণ সম্পর্কিত নোট

- কনটেন্ট অনুবাদ API গুলো অনুবাদকে প্রকল্প পাথ পুনঃলিখন থেকে আলাদা রাখে। অনুবাদকৃত কনটেন্টে লক্ষ্য স্থানের জন্য প্রকল্প-সংক্রান্ত লিঙ্ক সমন্বয় করতে হলে স্পষ্টভাবে `rewrite_markdown_paths` বা `rewrite_notebook_paths` কল করুন।
- প্রজেক্ট অর্কেস্ট্রেশন API গুলো কনটেন্ট অনুবাদের চারপাশে প্রজেক্ট আচরণ যোগ করে, যার মধ্যে ফাইল আবিষ্কার, লেখার কাজ, পাথ পুনঃলিখন, মেটাডেটা, ক্লিনআপ এবং ঐচ্ছিক ডিসক্লেইমার অন্তর্ভুক্ত।
- `run_translation` CLI দ্বারা ব্যবহৃত একই Rich-backed রিপোর্টার দিয়ে অগ্রগতি এবং অনুমান সংক্ষিপ্তসার প্রিন্ট করে। নন-ইন্টারঅ্যাকটিভ আউটপুট প্লেইন টেক্সটে ফিরে আসে।
- `dry_run=True` ভার্চুয়াল README আপডেট ব্যবহার করে অনুমান গণনা করে, কিন্তু README বা অনুবাদ ফাইলগুলো লেখে না।
- `groups` ক্রমান্বয়ে প্রক্রিয়াকৃত হয়। কাজ শুরু হওয়ার আগে একটি একক সমষ্টিগত অনুমান প্রিন্ট করা হয়।
- ইমেজ অনুবাদ নির্বাচিত হলে, Vision কনফিগারেশন অনুপস্থিত থাকলে অনুবাদ শুরু হওয়ার আগে একটি ত্রুটি উত্তোলিত হয়।
- বিদ্যমান অ্যালিয়াস-ভিত্তিক ভাষা ফোল্ডারগুলো সনাক্ত করা হয় এবং রান চক্রের অংশ হিসেবে ক্যাননিক্যাল ভাষা ফোল্ডার নামগুলিতে মাইগ্রেট করা যেতে পারে।
- `run_review` অনুবাদিত ফাইল অনুপস্থিত, অনুবাদ মেটাডেটা অনুপস্থিত বা পুরনো, বিকৃত Markdown frontmatter/code fences, এবং অবৈধ অনূদীত নোটবুক JSON এর ক্ষেত্রে ব্যর্থ হয়।
- `run_review` ডিফল্টরূপে লোকাল Markdown এবং ইমেজ লিংক টার্গেটগুলোর অনুপস্থিতি সতর্কতা হিসেবে রিপোর্ট করে।

## অভ্যন্তরীণ কল পথ

API CLI দ্বারা ব্যবহৃত একই কোর ইমপ্লিমেন্টেশনের কাছে ডেলিগেট করে:

অনুবাদ:

1. মেমরিতে অনুবাদের জন্য `co_op_translator.api.translation.translate_markdown_content`, `translate_notebook_content`, অথবা `translate_image_content`।
2. স্পষ্ট পাথ পোস্ট-প্রসেসিং-এর জন্য `co_op_translator.api.translation.rewrite_markdown_paths` বা `rewrite_notebook_paths`।
3. সম্পূর্ণ প্রজেক্ট অর্কেস্ট্রেশনের জন্য `co_op_translator.api.translation.run_translation`।
4. `co_op_translator.config.Config`, `LLMConfig`, এবং `VisionConfig`।
5. `co_op_translator.core.project.ProjectTranslator`।
6. `co_op_translator.core.project.TranslationManager`।
7. Markdown, নোটবুক, এবং ইমেজগুলোর জন্য ফোকাসড প্রজেক্ট অনুবাদ মিক্সিন।
8. `co_op_translator.core`-এর অধীনে Markdown, নোটবুক, টেক্সট, এবং ইমেজ ট্রান্সলেটর।

পর্যালোচনা:

1. `co_op_translator.api.review.run_review`
2. `co_op_translator.review.targets.build_review_targets`
3. `co_op_translator.review.runner.ReviewRunner`
4. `co_op_translator.review.checks`-এর অধীনে নির্ণায়ক চেক।

নিচের ক্লাসগুলো রক্ষণাবেক্ষণের জন্য উপযোগী, কিন্তু প্যাকেজ-স্তরের স্থিতিশীল API হিসেবে রপ্তানি করা হয় না।

| ক্লাস | মডিউল | দায়িত্ব |
| --- | --- | --- |
| `ProjectTranslator` | `co_op_translator.core.project.project_translator` | প্রজেক্ট-স্তরের অনুবাদ, ডিরেক্টরি ব্যবস্থাপনা, প্রতিটি-ভাষার মেটাডেটা স্বাভাবিকীকরণ, এবং Markdown, নোটবুক, এবং ইমেজ ট্রান্সলেটরদের কাছে দায়িত্ব ভাগ করে। |
| `TranslationManager` | `co_op_translator.core.project.translation` | Markdown, নোটবুক, ইমেজ, স্টেল ডিটেকশন, এবং অনুবাদ মেটাডেটা আপডেটগুলির জন্য অ্যাসিঙ্ক ফাইল প্রসেসিং কাজ সম্পাদন করে। |
| `ProjectMarkdownTranslationMixin` | `co_op_translator.core.project.translation.project_markdown_translation` | Markdown ফাইল রিড, কনটেন্ট অনুবাদ, পাথ পুনঃলিখন, মেটাডেটা, ডিসক্লেইমার, এবং লেখাগুলো সমন্বয় করে। |
| `ProjectNotebookTranslationMixin` | `co_op_translator.core.project.translation.project_notebook_translation` | নোটবুক ফাইল রিড, Markdown-সেল অনুবাদ, পাথ পুনঃলিখন, মেটাডেটা, ডিসক্লেইমার, এবং লেখাগুলো সমন্বয় করে। |
| `ProjectImageTranslationMixin` | `co_op_translator.core.project.translation.project_image_translation` | সোর্স ইমেজ আবিষ্কার, ইমেজ অনুবাদ, আউটপুট পাথ, মেটাডেটা, এবং লেখাগুলো সমন্বয় করে। |
| `ProjectEvaluator` | `co_op_translator.core.project.project_evaluator` | অনুবাদকৃত Markdown জোড়া খুঁজে বের করে, অনুবাদের গুণমান মূল্যায়ন করে, এবং কম-বিশ্বাসযোগ্যতা রিপেয়ার ওয়ার্কফ্লো জন্য confidence মেটাডেটা পড়ে। |
| `ReviewRunner` | `co_op_translator.review.runner` | উৎস ফাইল, লক্ষ্য ভাষা, এবং কনফিগার করা অনুবাদ root-গুলোর মধ্যে নির্ণায়ক পর্যালোচনা চেক সমন্বয় করে। |
| `ReviewTarget` | `co_op_translator.review.targets` | একটি সোর্স root এবং ঐ root-এর জন্য পর্যালোচনা করা অনুবাদ আউটপুট ডিরেক্টরি বর্ণনা করে। |
| `LanguageFolderMigrator` | `co_op_translator.core.project.language_migrator` | লিগ্যাসি অ্যালিয়াস ভাষা ফোল্ডার সনাক্ত করে এবং ক্যাননিক্যাল BCP 47 ফোল্ডার মাইগ্রেশন পরিকল্পনা প্রস্তুত করে। |
| `Config` | `co_op_translator.config.base_config` | `.env` ফাইল লোড করে এবং পরীক্ষা করে যে প্রয়োজনীয় LLM এবং ঐচ্ছিক Vision প্রদানকারীরা কনফিগার করা আছে কি না। |
| `LLMConfig` | `co_op_translator.config.llm_config.config` | Azure OpenAI, OpenAI, বা Anthropic স্বয়ংক্রিয়ভাবে সনাক্ত করে, প্রয়োজনীয় এনভায়রনমেন্ট ভ্যারিয়েবল বৈধতা করে, এবং প্রদানকারী কানেক্টিভিটি চেক চালায়। |
| `VisionConfig` | `co_op_translator.config.vision_config.config` | Azure AI Vision কনফিগারেশন সনাক্ত করে এবং ইমেজ অনুবাদের জন্য কানেক্টিভিটি চেক চালায়। |