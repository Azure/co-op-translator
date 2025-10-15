<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T02:47:16+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "bn"
}
-->
# Microsoft Co-op Translator সমস্যার সমাধান গাইড

## সারসংক্ষেপ
Microsoft Co-Op Translator একটি শক্তিশালী টুল, যা Markdown ডকুমেন্ট সহজে অনুবাদ করতে সাহায্য করে। এই গাইডটি ব্যবহার করার সময় সাধারণ যে সমস্যাগুলো দেখা যায়, সেগুলোর সমাধান এখানে দেওয়া হয়েছে।

## সাধারণ সমস্যা ও সমাধান

### ১. Markdown ট্যাগ সমস্যা
**সমস্যা:** অনুবাদ করা Markdown ডকুমেন্টের উপরে `markdown` ট্যাগ থাকায় রেন্ডারিং সমস্যা হচ্ছে।

**সমাধান:** এই সমস্যা সমাধানের জন্য, ফাইলের উপরের `markdown` ট্যাগটি মুছে ফেলুন। এতে Markdown ফাইলটি ঠিকভাবে রেন্ডার হবে।

**ধাপসমূহ:**
1. অনুবাদ করা Markdown (`.md`) ফাইলটি খুলুন।
2. ডকুমেন্টের উপরে `markdown` ট্যাগটি খুঁজে বের করুন।
3. `markdown` ট্যাগটি মুছে ফেলুন।
4. ফাইলটি সংরক্ষণ করুন।
5. আবার ফাইলটি খুলে দেখুন ঠিকভাবে রেন্ডার হচ্ছে কিনা।

### ২. এম্বেডেড ইমেজের URL সমস্যা
**সমস্যা:** এম্বেড করা ছবির URL ভাষার লোকেলের সাথে মিলছে না, ফলে ভুল বা ছবি দেখা যাচ্ছে না।

**সমাধান:** এম্বেড করা ছবির URL চেক করুন এবং ভাষার লোকেলের সাথে মিলিয়ে নিন। সব ছবি `translated_images` ফোল্ডারে থাকে এবং প্রতিটি ছবির ফাইল নামের মধ্যে ভাষার লোকেল ট্যাগ থাকে।

**ধাপসমূহ:**
1. অনুবাদ করা Markdown ডকুমেন্ট খুলুন।
2. এম্বেড করা ছবিগুলো ও তাদের URL চিহ্নিত করুন।
3. ছবির ফাইল নামের ভাষার লোকেল ডকুমেন্টের ভাষার সাথে মিলিয়ে দেখুন।
4. প্রয়োজন হলে URL আপডেট করুন।
5. পরিবর্তন সংরক্ষণ করুন এবং ডকুমেন্টটি আবার খুলে দেখুন ছবি ঠিকভাবে দেখা যাচ্ছে কিনা।

### ৩. অনুবাদের যথার্থতা
**সমস্যা:** অনুবাদ যথার্থ নয় বা আরও সম্পাদনা প্রয়োজন।

**সমাধান:** অনুবাদ করা ডকুমেন্টটি পর্যালোচনা করুন এবং যথার্থতা ও পাঠযোগ্যতা বাড়াতে প্রয়োজনীয় সম্পাদনা করুন।

**ধাপসমূহ:**
1. অনুবাদ করা ডকুমেন্ট খুলুন।
2. কনটেন্ট ভালোভাবে পর্যালোচনা করুন।
3. প্রয়োজনীয় সম্পাদনা করুন।
4. পরিবর্তন সংরক্ষণ করুন।

## ৪. অনুমতি সংক্রান্ত সমস্যা Redacted বা 404

যদি ছবি বা টেক্সট সঠিক ভাষায় অনুবাদ না হয় এবং -d ডিবাগ মোডে চালালে 401 এরর আসে, তাহলে এটি সাধারণত অথেন্টিকেশন সমস্যা—কী ভুল, মেয়াদোত্তীর্ণ, বা সঠিক অঞ্চলের সাথে সংযুক্ত নয়।

মূল কারণ জানতে co-op translator [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) দিয়ে চালান।

- **Error Message**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **সম্ভাব্য কারণ:**
  - সাবস্ক্রিপশন কী অনুরোধে ভুল বা গোপন করা হয়েছে।
  - AI Services Key বা Subscription Key হয়তো অন্য Azure রিসোর্সের (যেমন Translator বা OpenAI) জন্য, **Azure AI Vision** রিসোর্সের জন্য নয়।

 **Resource Type**
  - [Azure Portal](https://portal.azure.com) বা [Azure AI Foundry](https://ai.azure.com) তে যান এবং নিশ্চিত করুন রিসোর্সের টাইপ `Azure AI services` → `Vision`।
  - কী যাচাই করুন এবং সঠিক কী ব্যবহার হচ্ছে কিনা নিশ্চিত করুন।

## ৫. কনফিগারেশন সংক্রান্ত সমস্যা (নতুন Error Handling)

নতুন selective translation সিস্টেমে, Co-op Translator এখন পরিষ্কার error message দেয় যদি প্রয়োজনীয় সার্ভিস কনফিগার করা না থাকে।

### ৫.১. ইমেজ অনুবাদের জন্য Azure AI Service কনফিগার করা নেই

**সমস্যা:** আপনি ইমেজ অনুবাদ (`-img` flag) চেয়েছেন, কিন্তু Azure AI Service ঠিকভাবে কনফিগার করা নেই।

**Error Message:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**সমাধান:**
1. **Option 1**: Azure AI Service কনফিগার করুন
   - `.env` ফাইলে `AZURE_AI_SERVICE_API_KEY` যোগ করুন
   - `.env` ফাইলে `AZURE_AI_SERVICE_ENDPOINT` যোগ করুন
   - সার্ভিস অ্যাক্সেসযোগ্য কিনা যাচাই করুন

2. **Option 2**: ইমেজ অনুবাদ অনুরোধ বাদ দিন
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### ৫.২. প্রয়োজনীয় কনফিগারেশন নেই

**সমস্যা:** গুরুত্বপূর্ণ LLM কনফিগারেশন নেই।

**Error Message:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**সমাধান:**
1. `.env` ফাইলে অন্তত একটি LLM কনফিগারেশন আছে কিনা যাচাই করুন:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` এবং `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Azure OpenAI অথবা OpenAI—একটি কনফিগার করা থাকতে হবে, দুটো নয়।

### ৫.৩. Selective Translation বিভ্রান্তি

**সমস্যা:** কোনো ফাইল অনুবাদ হয়নি, অথচ কমান্ড সফল হয়েছে।

**সম্ভাব্য কারণ:**
- ভুল ফাইল টাইপ ফ্ল্যাগ (`-md`, `-img`, `-nb`)
- প্রজেক্টে মিলছে না এমন ফাইল নেই
- ডিরেক্টরি স্ট্রাকচার ভুল

**সমাধান:**
1. **ডিবাগ মোড ব্যবহার করুন**:
   ```bash
   translate -l "ko" -md -d
   ```

2. **প্রজেক্টে ফাইল টাইপ চেক করুন**:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **ফ্ল্যাগ কম্বিনেশন যাচাই করুন**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## ৬. পুরাতন সিস্টেম থেকে মাইগ্রেশন

### ৬.১. Markdown-Only মোড বাতিল

**সমস্যা:** আগের মতো markdown-only fallback কমান্ড আর কাজ করছে না।

**পুরাতন আচরণ:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**নতুন আচরণ:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**সমাধান:**
- **স্পষ্টভাবে** বলুন কী অনুবাদ করতে চান:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### ৬.২. অপ্রত্যাশিত লিংক আচরণ

**সমস্যা:** অনুবাদ করা ফাইলে লিংক অপ্রত্যাশিত জায়গায় যাচ্ছে।

**কারণ:** নির্বাচিত ফাইল টাইপের উপর ভিত্তি করে ডাইনামিক লিংক প্রসেসিং পরিবর্তিত হয়।

**সমাধান:**
1. **নতুন লিংক আচরণ বুঝুন**:
   - `-nb` থাকলে: নোটবুক লিংক অনুবাদ করা ভার্সনে যায়
   - `-nb` না থাকলে: নোটবুক লিংক মূল ফাইলে যায়
   - `-img` থাকলে: ইমেজ লিংক অনুবাদ করা ভার্সনে যায়
   - `-img` না থাকলে: ইমেজ লিংক মূল ফাইলে যায়

2. **আপনার প্রয়োজন অনুযায়ী সঠিক কম্বিনেশন বেছে নিন**:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## ৭. GitHub Action চলেছে কিন্তু কোনো Pull Request (PR) তৈরি হয়নি

**লক্ষণ:** `peter-evans/create-pull-request` এর workflow লগে দেখা যায়:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**সম্ভাব্য কারণ:**
- **কোনো পরিবর্তন নেই:** অনুবাদ ধাপে কোনো পার্থক্য হয়নি (রিপো ইতিমধ্যে আপডেটেড)।
- **আউটপুট উপেক্ষিত:** `.gitignore` আপনি যে ফাইল কমিট করতে চান তা বাদ দিয়েছে (যেমন, `*.ipynb`, `translations/`, `translated_images/`)।
- **add-paths mismatch:** অ্যাকশনে দেওয়া path আসল আউটপুট লোকেশনের সাথে মিলছে না।
- **Workflow লজিক/শর্ত:** অনুবাদ ধাপ আগেভাগে শেষ হয়েছে বা অপ্রত্যাশিত ডিরেক্টরিতে লিখেছে।

**কিভাবে ঠিক করবেন / যাচাই করবেন:**
1. **আউটপুট আছে কিনা নিশ্চিত করুন:** অনুবাদের পর, workspace-এ `translations/` এবং/অথবা `translated_images/`-এ নতুন/পরিবর্তিত ফাইল আছে কিনা দেখুন।
   - নোটবুক অনুবাদ করলে, `.ipynb` ফাইল `translations/<lang>/...`-এ লেখা হচ্ছে কিনা দেখুন।
2. **`.gitignore` পর্যালোচনা করুন:** জেনারেটেড আউটপুট বাদ দেবেন না। নিশ্চিত করুন আপনি বাদ দিচ্ছেন না:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (নোটবুক অনুবাদ করলে)
3. **add-paths আউটপুটের সাথে মিলছে কিনা নিশ্চিত করুন:** মাল্টিলাইন ভ্যালু ব্যবহার করুন এবং দুই ফোল্ডারই দিন যদি প্রয়োজন হয়:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **ডিবাগিংয়ের জন্য জোর করে PR দিন:** wiring ঠিক আছে কিনা দেখতে সাময়িকভাবে empty commit অনুমতি দিন:
   ```yaml
   with:
     commit-empty: true
   ```
5. **ডিবাগ মোডে চালান:** translate কমান্ডে `-d` যোগ করুন, কোন ফাইল পাওয়া গেছে ও লেখা হয়েছে তা দেখতে।
6. **Permissions (GITHUB_TOKEN):** workflow-এ কমিট ও PR তৈরির জন্য write permission আছে কিনা নিশ্চিত করুন:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## দ্রুত ডিবাগিং চেকলিস্ট

অনুবাদ সংক্রান্ত সমস্যা সমাধানে:

1. **ডিবাগ মোড ব্যবহার করুন:** বিস্তারিত লগ দেখতে `-d` ফ্ল্যাগ দিন
2. **ফ্ল্যাগ চেক করুন:** `-md`, `-img`, `-nb` আপনার উদ্দেশ্যের সাথে মিলছে কিনা দেখুন
3. **কনফিগারেশন যাচাই করুন:** `.env` ফাইলে প্রয়োজনীয় কী আছে কিনা দেখুন
4. **ধাপে ধাপে টেস্ট করুন:** শুধু `-md` দিয়ে শুরু করুন, পরে অন্য টাইপ যোগ করুন
5. **ফাইল স্ট্রাকচার চেক করুন:** সোর্স ফাইল আছে ও অ্যাক্সেসযোগ্য কিনা নিশ্চিত করুন

আরও বিস্তারিত কমান্ড ও ফ্ল্যাগের তথ্যের জন্য [Command Reference](./command-reference.md) দেখুন।

---

**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতা বজায় রাখার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।