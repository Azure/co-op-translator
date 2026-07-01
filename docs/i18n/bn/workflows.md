# আপনার ওয়ার্কফ্লো নির্বাচন করুন

Co-op Translator তিনভাবে ব্যবহার করা যায়: CLI, Python API, এবং MCP সার্ভার। এগুলো একই অনুবাদ ক্ষমতা শেয়ার করে, কিন্তু প্রতিটি আলাদা ওয়ার্কফ্লো’র সাথে মানায়।

কোথা থেকে শুরু করবেন তা সিদ্ধান্ত নেওয়ার সময় এই পৃষ্ঠা ব্যবহার করুন।

## দ্রুত সিদ্ধান্ত

| If you want to... | Use | Start here |
| --- | --- | --- |
| টার্মিনাল থেকে একটি রিপোজিটরি অনুবাদ বা পর্যালোচনা | CLI | [CLI রেফারেন্স](cli.md) |
| Python স্ক্রিপ্ট, সার্ভিস, নোটবুক, অথবা CI জবে অনুবাদ যোগ করা | Python API | [Python API](api.md) |
| একটি এজেন্ট, সম্পাদক, বা MCP-সমর্থ ক্লায়েন্টকে আপনার জন্য কন্টেন্ট অনুবাদ করতে দেওয়া | MCP সার্ভার | [MCP Server](mcp.md) |
| আপনার অ্যাপ আগে থেকেই লোড করা একটি Markdown ডকুমেন্ট, নোটবুক, বা ইমেজ অনুবাদ করা | Python API বা MCP সার্ভার | [Python API](api.md) or [MCP Server](mcp.md) |
| মানক আউটপুট ফোল্ডার এবং মেটাডেটা সহ একটি সম্পূর্ণ রিপোজিটরি অনুবাদ করা | CLI বা `run_translation` | [CLI রেফারেন্স](cli.md) or [Python API](api.md) |

## CLI ব্যবহার করুন যখন

যখন কেউ বা কোনো CI জব শেল থেকে রিপোজিটরি অনুবাদ চালাচ্ছে, তখন CLI নির্বাচন করুন।

CLI সবচেয়ে সরাসরি পথ যখন আপনি চান Co-op Translator প্রজেক্ট ফাইল আবিষ্কার করুক, অনূদিত আউটপুট তৈরি করুক, প্রজেক্ট লেআউট সংরক্ষণ করুক, মেটাডেটা আপডেট করুক, এবং রিভিউ কমান্ডগুলো চালাক।

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb -img
co-op-review -l "ko" -md -nb
migrate-links -l "ko" --dry-run
```

উপযুক্ত পরিস্থিতি:

- আপনি টার্মিনাল থেকে একটি রিপোজিটরি অনুবাদ করছেন।
- আপনি CI বা রিলিজ ওয়ার্কফ্লো-এর জন্য একটি পুনরাবৃত্তিযোগ্য কমান্ড চান।
- আপনি অন্তর্নির্মিত প্রজেক্ট ডিসকভারি, আউটপুট পাথ, মেটাডেটা, ক্লিনআপ, এবং রিভিউ চান।
- আপনি Python কোড লেখার বদলে একটি কমান্ড ইন্টারফেসকে প্রাধান্য দেন।

## Python API ব্যবহার করুন যখন

আপনার নিজস্ব কোড ওয়ার্কফ্লো নিয়ন্ত্রণ করা উচিত হলে Python API নির্বাচন করুন।

API অ্যাপ্লিকেশন, অটোমেশন স্ক্রিপ্ট, নোটবুক, সার্ভিস, এবং কাস্টম পাইপলাইনগুলোর জন্য কাজে লাগে। এটি আপনাকে পৃথক ফাইলের জন্য লো-লেভেল কন্টেন্ট অনুবাদ API কল করতে দেয়, অথবা CLI দ্বারা ব্যবহৃত একই রিপোজিটরি-স্তরের অর্কেস্ট্রেশন Python থেকে চালাতে দেয়।

একটি Markdown ডকুমেন্ট অনুবাদ করুন এবং কোথায় সংরক্ষণ করবেন তা নির্ধারণ করুন:

```python
import asyncio
from pathlib import Path

from co_op_translator.api import rewrite_markdown_paths, translate_markdown_content


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
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rewritten, encoding="utf-8")


asyncio.run(main())
```

Python থেকে একটি রিপোজিটরি অনুবাদ চালান:

```python
import asyncio

from co_op_translator.api import run_translation


async def main() -> None:
    await run_translation(
        language_codes=["ko"],
        translate_markdown=True,
        translate_notebooks=True,
        translate_images=False,
        dry_run=True,
    )


asyncio.run(main())
```

উপযুক্ত পরিস্থিতি:

- আপনার অ্যাপ ইতোমধ্যেই ফাইল, বাফার, নোটবুক, বা ইমেজ বাইট পড়ে থাকে।
- আপনাকে কাস্টম ভ্যালিডেশন, স্টোরেজ, লগিং, রিট্রাই, বা অনুমোদন ফ্লো দরকার।
- আপনি একটি পুরো রিপোজিটরি প্রক্রিয়াকরণ না করে একটি ডকুমেন্ট, নোটবুক, বা ইমেজ অনুবাদ করতে চান।
- আপনি রিপোজিটরি অনুবাদ চান, কিন্তু শেল কমান্ডের বদলে Python অটোমেশনের মাধ্যমে।

## MCP সার্ভার ব্যবহার করুন যখন

যখন একটি এজেন্ট, সম্পাদক, বা MCP-সমর্থ ক্লায়েন্ট Co-op Translator টুলস কল করা উচিত, তখন MCP সার্ভার নির্বাচন করুন।

সাধারণ লোকাল সেটআপে, ব্যবহারকারী ম্যানুয়ালি সার্ভার চালিয়ে রাখে না। যখন টুলের প্রয়োজন হয়, তখন MCP ক্লায়েন্ট `co-op-translator-mcp` `stdio`-এর ওপর থেকে শুরু করে।

উদাহরণস্বরূপ ব্যবহারকারীর অনুরোধ যা একটি এজেন্ট হ্যান্ডেল করতে পারে:

- "এই Markdown ফাইলটি কোরিয়ান-এ অনুবাদ করুন এবং লিংকগুলো ঠিক রাখুন।"
- "এজেন্ট-সহায় MCP ওয়ার্কফ্লো ব্যবহার করে এই Markdown ফাইলটি কোরিয়ান-এ অনুবাদ করুন, অনূদিত খন্ডগুলোর জন্য আপনার নিজস্ব মডেল ব্যবহার করে।"
- "এই নোটবুকটি কোরিয়ান-এ অনুবাদ করুন, কোড সেলগুলো সংরক্ষণ করুন, এবং নোটবুকটি পুনর্গঠন করতে Co-op Translator MCP ব্যবহার করুন।"
- "এই ইমেজের টেক্সট জাপানি-তে অনুবাদ করুন এবং ফলাফল সংরক্ষণ করুন।"
- "স্প্যানিশ-এ একটি রিপোজিটরি অনুবাদের ড্রাই-রান করুন এবং আমাকে বলুন কী পরিবর্তন হবে।"
- "কোরিয়ান অনুবাদ আউটপুট আপ-টু-ডেট কিনা তা পর্যালোচনা করুন।"

Markdown এবং নোটবুকের জন্য, MCP দুটি মোডে কাজ করতে পারে:

| Mode | Use when | Main tools |
| --- | --- | --- |
| এজেন্ট-সহায়িত | MCP হোস্ট এজেন্ট তার নিজস্ব মডেল ব্যবহার করে চাংকগুলো অনুবাদ করবে, Co-op Translator LLM প্রদানকারীর ক্রেডেনশিয়াল ছাড়াই। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| Provider-backed | Co-op Translator সরাসরি Azure OpenAI বা OpenAI কল করা উচিত। | `translate_markdown_content`, `translate_notebook_content` |

MCP provider-backed Markdown টুল কল শেইপ:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Setup\n\nInstall Co-op Translator first.",
    "language_code": "ko",
    "options": {
      "source_path": "docs/setup.md"
    }
  }
}
```

MCP ইমেজ টুল কল শেইপ:

```json
{
  "tool": "translate_image_content",
  "arguments": {
    "image_path": "assets/architecture.png",
    "language_code": "ko",
    "output_path": "translated_images/ko/assets/architecture.png"
  }
}
```

MCP-এর মাধ্যমে রিপোজিটরি অনুবাদ ডিফল্টভাবে ড্রাই-রান করা হয়:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": ["ko"],
    "translate_markdown": true,
    "translate_notebooks": true,
    "translate_images": false,
    "dry_run": true
  }
}
```

উপযুক্ত পরিস্থিতি:

- আপনি একটি এজেন্ট বা সম্পাদককের ভিতরে প্রাকৃতিক ভাষার অনুবাদ ওয়ার্কফ্লো চান।
- আপনি এমন Markdown বা নোটবুক অনুবাদ চান যেখানে হোস্ট এজেন্ট মডেল প্রস্তুত করা চাংকগুলো অনুবাদ করে।
- আপনি চান এজেন্ট পুরো রিপোজিটরি না করে নির্বাচিত কন্টেন্ট অনুবাদ করুক।
- আপনি রিপোজিটরি-ব্যাপী লেখার আগে একটি অনুমোদন ধাপ চান।
- আপনি একটি এমন ইন্টারফেস চান যা Markdown, নোটবুক, ইমেজ, রিভিউ, এবং পাথ-রিরাইটিং টুলস একসাথে দেয়।

## এগুলো একসাথে কিভাবে মেলে

CLI মানুষের জন্য রিপোজিটরি অনুবাদে ডিফল্ট হিসেবে সবচেয়ে ভালো। Python API সবচেয়ে ভালো যখন আপনার কোড ওয়ার্কফ্লো-এর মালিক। MCP সার্ভার সবচেয়ে ভালো যখন একটি এজেন্ট বা সম্পাদক ওয়ার্কফ্লো-এর মালিক।

এই তিনটি পথই একই পাবলিক Co-op Translator API ব্যবহার করে, তাই আপনি CLI দিয়ে শুরু করতে পারেন, পরে Python দিয়ে অটোমেট করতে পারেন, এবং যখন এজেন্ট-চালিত ওয়ার্কফ্লো দরকার হবে তখন MCP ক্লায়েন্টদের একই ক্ষমতাগুলো উন্মুক্ত করতে পারেন।