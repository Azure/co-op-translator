# আপনার ওয়ার্কফ্লো বেছে নিন

Co-op Translator তিনভাবে ব্যবহার করা যায়: CLI, Python API, এবং MCP সার্ভার। এগুলো একই অনুবাদ ক্ষমতা ভাগ করে, তবে প্রতিটি আলাদা ওয়ার্কফ্লো-এর উপযোগী।

এ পৃষ্ঠা ব্যবহার করুন যখন আপনি সিদ্ধান্ত নেবেন কোথা থেকে শুরু করবেন।

**If you edit translations by hand:** ডিফল্ট CLI এবং Actions ওয়ার্কফ্লোগুলো পরিবর্তিত সোর্স ফাইলগুলো সম্পূর্ণভাবে পুনরায় অনুবাদ করে, তাই সেগুলোর আপনার লেখা ওভাররাইট হতে পারে। আপডেট গ্রহণ করার আগে diff পর্যালোচনা করুন। গ্রহণকৃত সম্পাদনার Markdown ব্লক-স্তরের সংরক্ষণের জন্য, ঐচ্ছিক [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider) ব্যবহার করুন।

## দ্রুত সিদ্ধান্ত

| আপনি যদি চান... | ব্যবহার করুন | এখান থেকে শুরু করুন |
| --- | --- | --- |
| টার্মিনাল থেকে একটি রিপোজিটরি অনুবাদ বা পর্যালোচনা করতে | CLI | [CLI Reference](cli.md) |
| একটি Python স্ক্রিপ্ট, সার্ভিস, নোটবুক, বা CI জবে অনুবাদ যোগ করতে | Python API | [Python API](api.md) |
| একজন এজেন্ট, সম্পাদক, বা MCP-কম্প্যাটিবল ক্লায়েন্টকে আপনার জন্য কনটেন্ট অনুবাদ করতে দিন | MCP Server | [MCP Server](mcp.md) |
| একটি Markdown ডকুমেন্ট, নোটবুক, বা ইমেজ অনুবাদ করুন যা আপনার অ্যাপ ইতিমধ্যে লোড করেছে | Python API or MCP Server | [Python API](api.md) or [MCP Server](mcp.md) |
| সাধারণ আউটপুট ফোল্ডার এবং মেটাডেটা সহ একটি সম্পূর্ণ রিপোজিটরি অনুবাদ করতে | CLI or `run_translation` | [CLI Reference](cli.md) or [Python API](api.md) |

## CLI ব্যবহার করার সময়

CLI নির্বাচন করুন যখন একজন মানুষ বা CI জব শেল থেকে রিপোজিটরি অনুবাদ করে চালাচ্ছে।

যখন আপনি চান Co-op Translator প্রজেক্ট ফাইল আবিষ্কার করুক, অনূদিত আউটপুট তৈরি করুক, প্রজেক্ট লেআউট সংরক্ষণ করুক, মেটাডেটা আপডেট করুক, এবং রিভিউ কমান্ড চালাক— তখন CLI সবচেয়ে সরাসরি পথ।

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -md -nb
co-op-review -l "ko"
migrate-links -l "ko" --dry-run
```

এই উদাহরণটি Markdown এবং নোটবুক অনুবাদ করে। `-img` যোগ করবেন শুধুমাত্র [Azure AI Vision](configuration.md#azure-ai-vision) কনফিগার করার পর। শুধুমাত্র Markdown-এ প্রথম রান-এর জন্য, [Your first translation](first-translation.md) অনুসরণ করুন।

উপযুক্ত পরিস্থিতি:

- আপনি টার্মিনাল থেকে একটি রিপোজিটরি অনুবাদ করছেন।
- আপনি CI বা রিলিজ ওয়ার্কফ্লো-এর জন্য পুনরাবৃত্তিযোগ্য একটি কমান্ড চান।
- আপনি বিল্ট-ইন প্রজেক্ট ডিসকভারি, আউটপুট পাথ, মেটাডেটা, ক্লিনআপ, এবং রিভিউ চান।
- Python কোড লেখার চেয়ে আপনি কমান্ড ইন্টারফেসকে পছন্দ করেন।

## Python API ব্যবহার করার সময়

Python API নির্বাচন করুন যখন ওয়ার্কফ্লো আপনার নিজের কোড দ্বারা নিয়ন্ত্রিত হওয়া উচিত।

API অ্যাপ্লিকেশন, অটোমেশন স্ক্রিপ্ট, নোটবুক, সার্ভিস, এবং কাস্টম পাইপলাইনগুলোর জন্য উপকারী। এটি আপনাকে একক ফাইলগুলোর জন্য নিম্ন-স্তরের কন্টেন্ট অনুবাদ API কল করতে দেবে, অথবা CLI-তে ব্যবহৃত একই রিপোজিটরি-স্তরের অর্কেস্ট্রেশন চালাতে দেবে।

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
from co_op_translator.api import run_translation

run_translation(
    language_codes="ko",
    markdown=True,
    notebook=True,
    images=False,
    dry_run=True,
)
```

উপযুক্ত পরিস্থিতি:

- আপনার অ্যাপ ইতোমধ্যে ফাইল, বাফার, নোটবুক, বা ইমেজ বাইট পড়ে।
- আপনার কাস্টম যাচাইকরণ, স্টোরেজ, লগিং, পুনরায় চেষ্টা, বা অনুমোদন ফ্লো দরকার।
- আপনি একটি ডকুমেন্ট, নোটবুক, বা ইমেজ অনুবাদ করতে চান পুরো রিপোজিটরি প্রক্রিয়াকরণ ছাড়া।
- আপনি রিপোজিটরি অনুবাদ চান, কিন্তু শেল কমান্ডের বদলে Python অটোমেশনের মাধ্যমে।

## MCP সার্ভার ব্যবহার করার সময়

MCP সার্ভার নির্বাচন করুন যখন একটি এজেন্ট, সম্পাদক, বা MCP-কম্প্যাটিবল ক্লায়েন্ট Co-op Translator টুলগুলি কল করবে।

সাধারণ লোকাল সেটআপে, ব্যবহারকারী ম্যানুয়ালি সার্ভার চালু রাখেন না। MCP ক্লায়েন্ট দরকার হলে `stdio`-এর মাধ্যমে `co-op-translator-mcp` শুরু করে।

এজেন্ট যা হ্যান্ডেল করতে পারে এমন উদাহরণ ব্যবহারকারীর অনুরোধ:

- "এই Markdown ফাইলটি কোরিয়ান ভাষায় অনুবাদ করুন এবং লিঙ্কগুলো সঠিক রাখুন."
- "এই Markdown ফাইলটি এজেন্ট-সহায়িত MCP ওয়ার্কফ্লো দিয়ে কোরিয়ানে অনুবাদ করুন, অনূদিত চাঙ্কগুলোর জন্য আপনার নিজের মডেল ব্যবহার করে."
- "এই নোটবুকটি কোরিয়ানে অনুবাদ করুন, কোড সেলগুলো সংরক্ষণ করুন, এবং নোটবুক পুনর্গঠন করতে Co-op Translator MCP ব্যবহার করুন."
- "এই ছবির টেক্সট জাপানিতে অনুবাদ করুন এবং ফলাফল সংরক্ষণ করুন."
- "রিপোজিটরি অনুবাদকে স্প্যানিশে ড্রাই-রান করুন এবং আমাকে বলুন কী পরিবর্তিত হবে."
- "কোরিয়ান অনুবাদ আউটপুট আপ টু ডেট কি না তা পর্যালোচনা করুন."

Markdown এবং নোটবুকের জন্য, MCP দুটি মোডে কাজ করতে পারে:

| মোড | কখন ব্যবহার করবেন | প্রধান টুল |
| --- | --- | --- |
| এজেন্ট-সহায়িত | MCP হোস্ট এজেন্ট নিজের মডেল দিয়ে চাঙ্কগুলো অনুবাদ করবে, Co-op Translator LLM প্রদানকারী ক্রেডেনশিয়াল ছাড়াই। | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| প্রোভাইডার-সমর্থিত | Co-op Translator সরাসরি Azure OpenAI, OpenAI, বা Anthropic কল করবে। | `translate_markdown_content`, `translate_notebook_content` |

MCP প্রোভাইডার-সমর্থিত Markdown টুল কলের ফরম্যাট:

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

MCP ইমেজ টুল কলের ফরম্যাট:

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

রিপোজিটরি অনুবাদ MCP-র মাধ্যমে ডিফল্টভাবে ড্রাই-রান হয়:

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

- আপনি এজেন্ট বা সম্পাদক অভ্যন্তরে প্রাকৃতিক-ভাষার অনুবাদ ওয়ার্কফ্লো চান।
- আপনি Markdown বা নোটবুক অনুবাদ চান যেখানে হোস্ট এজেন্ট মডেল প্রস্তুতকৃত চাঙ্কগুলো অনুবাদ করে।
- আপনি চান এজেন্ট নির্বাচিত কনটেন্ট অনুবাদ করুক সম্পূর্ণ রিপোজিটরি না করে।
- আপনি চান রিপোজিটরি-ব্যাপী লেখার আগে একটি অনুমোদন ধাপ থাকুক।
- আপনি চান একটি ইন্টারফেস যা Markdown, নোটবুক, ইমেজ, রিভিউ, এবং পাথ-রিরাইটিং টুলগুলো একসঙ্গে প্রকাশ করে।

## এগুলো কীভাবে একসাথে মেলে

CLI মানুষের দ্বারা রিপোজিটরি অনুবাদের জন্য সর্বোত্তম ডিফল্ট। Python API সেরা যখন ওয়ার্কফ্লো আপনার কোডের অধীন। MCP সার্ভার সেরা যখন এজেন্ট বা সম্পাদক ওয়ার্কফ্লো-এর দায়িত্বে।

এই তিনটি পথ একই পাবলিক Co-op Translator API ব্যবহার করে, সুতরাং আপনি CLI দিয়ে শুরু করতে পারেন, পরে Python দিয়ে অটোমেট করতে পারেন, এবং যখন এজেন্ট-চালিত ওয়ার্কফ্লো দরকার হবে তখন একই ক্ষমতাগুলো MCP ক্লায়েন্টদের কাছে প্রকাশ করতে পারেন।