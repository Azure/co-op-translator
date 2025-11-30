<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:40:18+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "bn"
}
-->
# "অন্যান্য কোর্স" বিভাগ আপডেট করুন (Microsoft Beginners রিপোজিটোরি)

এই গাইডটি ব্যাখ্যা করে কিভাবে Co-op Translator ব্যবহার করে "অন্যান্য কোর্স" বিভাগটি স্বয়ংক্রিয়ভাবে সিঙ্ক্রোনাইজ করবেন, এবং কিভাবে সমস্ত রিপোজিটোরির জন্য গ্লোবাল টেমপ্লেট আপডেট করবেন।

- প্রযোজ্য: শুধুমাত্র Microsoft Beginners রিপোজিটোরিগুলোর জন্য
- কাজ করে: Co-op Translator CLI এবং GitHub Actions এর সাথে
- টেমপ্লেট উৎস: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## দ্রুত শুরু: আপনার রিপোতে অটো-সিঙ্ক চালু করুন

আপনার README-র "অন্যান্য কোর্স" বিভাগের চারপাশে নিচের মার্কারগুলো যোগ করুন। Co-op Translator প্রতিবার চালানোর সময় এই মার্কারগুলোর মধ্যে থাকা সবকিছু প্রতিস্থাপন করবে।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

প্রতি বার Co-op Translator চালানো হলে—CLI (যেমন, `translate -l "<language codes>"`) অথবা GitHub Actions এর মাধ্যমে—এই মার্কারগুলোর মধ্যে থাকা "অন্যান্য কোর্স" বিভাগটি স্বয়ংক্রিয়ভাবে আপডেট হবে।

> [!NOTE]
> যদি আপনার আগে থেকেই একটি তালিকা থাকে, তাহলে শুধু একই মার্কার দিয়ে সেটি ঘিরে দিন। পরবর্তী চালানোতে এটি সর্বশেষ মানসম্মত কন্টেন্ট দিয়ে প্রতিস্থাপিত হবে।

---

## গ্লোবাল কন্টেন্ট কিভাবে পরিবর্তন করবেন

যদি আপনি সমস্ত Beginners রিপোজিটোরিতে প্রদর্শিত মানসম্মত কন্টেন্ট আপডেট করতে চান:

1. টেমপ্লেটটি সম্পাদনা করুন: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. আপনার পরিবর্তনসহ Co-op Translator রিপোতে একটি pull request খুলুন
3. PR মার্জ হওয়ার পর Co-op Translator এর সংস্করণ আপডেট হবে
4. পরবর্তী বার Co-op Translator চালানো হলে (CLI বা GitHub Action এর মাধ্যমে) টার্গেট রিপোতে আপডেট হওয়া বিভাগটি স্বয়ংক্রিয়ভাবে সিঙ্ক হবে

এটি নিশ্চিত করে যে সমস্ত Beginners রিপোজিটোরির "অন্যান্য কোর্স" কন্টেন্টের জন্য একটি একক সত্যের উৎস রয়েছে।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->