# Microsoft নবাগতদের জন্য রেপোজিটরিগুলো

এই পাতা Microsoft-এর "For Beginners" রেপোজিটরির রক্ষণাবেক্ষকদের জন্য যারা শেয়ার করা "Other Courses" README সেকশনটি ব্যবহার করে।

অধিকাংশ Co-op Translator ব্যবহারকারীর জন্য এই পাতা প্রয়োজন হবে না।

## Other Courses সেকশনটি স্বয়ংক্রিয়ভাবে সিঙ্ক করুন

আপনার README-তে "Other Courses" সেকশনের চারপাশে এই মার্কারগুলো যোগ করুন:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

প্রতিবার Co-op Translator CLI বা GitHub Actions-এর মাধ্যমে চললে, এটি মার্কারগুলোর মধ্যে থাকা কনটেন্টকে প্যাকেজকৃত টেমপ্লেট দিয়ে প্রতিস্থাপন করে।

## শেয়ার করা টেমপ্লেট আপডেট করুন

টেমপ্লেট সোর্স অবস্থিত:

```text
src/co_op_translator/templates/other_courses.md
```

শেয়ার করা কনটেন্ট আপডেট করতে:

1. টেমপ্লেটটি সম্পাদনা করুন।
2. Co-op Translator-এ একটি pull request খুলুন।
3. পরিবর্তন রিলিজ হওয়ার পরে, লক্ষ্য রেপোজিটরিতে Co-op Translator চালান।

## Sparse Checkout পরামর্শ

বহু অনুবাদিত আউটপুট থাকলে বড় কোর্স রেপোজিটরিগুলো ক্লোন করা ব্যয়বহুল হয়ে পড়তে পারে। আপনি এই পরামর্শটি জেনারেট করা ভাষা সেকশনগুলিতে অন্তর্ভুক্ত করতে পারেন:

```markdown
> **Prefer to Clone Locally?**
>
> This repository includes many language translations, which can significantly increase download size. To clone without translations, use sparse checkout:
>
> ```bash
> git clone --filter=blob:none --sparse https://github.com/org/repo.git
> cd repo
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
```