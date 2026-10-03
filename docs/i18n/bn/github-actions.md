# GitHub Actions

যখন আপনি চান একটি রিপোজিটরি পরিবর্তিত ডকুমেন্টেশন স্বয়ংক্রিয়ভাবে অনুবাদ করবে এবং উত্পন্ন ফলাফলের সাথে একটি পুল রিকোয়েস্ট খুলবে, তখন GitHub Actions ব্যবহার করুন।

স্ট্যান্ডার্ড `GITHUB_TOKEN` সেটআপ দিয়ে শুরু করুন, সেইসাথে যেখানে নীতিমালা অনুমতিদানে সংগঠন-রিপোজিটরিগুলির জন্য। যখন আপনার সংগঠন একটি অ্যাপ আইডেন্টিটি দাবি করে বা স্বয়ংক্রিয় ডাউনস্ট্রীম ওয়ার্কফ্লো চালানোর প্রয়োজন হয়, তখন দেখুন [GitHub অ্যাপ সেটআপ](#github-app-setup)।

**Human edits:** এই ওয়ার্কফ্লো গুলো পরিবর্তিত সোর্স ফাইলগুলো সম্পূর্ণভাবে পুনঃঅনুবাদ করে এবং তাদের অনুবাদে মানুষের করা সম্পাদিত শব্দচয়ন ওভাররাইট করতে পারে। প্রতিটি PR মার্জ করার আগে পর্যালোচনা করুন। Markdown ব্লক-স্তরের সংরক্ষণের জন্য গ্রহণকৃত সম্পাদনার কাস্টম ইন্টিগ্রেশন দরকার [Python API translation state provider](api.md#preserve-accepted-human-edits-with-a-translation-state-provider)।

## আপনার প্রথম README অনুবাদ PR

একটি মূল `README.md` এবং একটি লক্ষ্য ভাষা দিয়ে শুরু করুন। এই ওয়ার্কফ্লো শুধুমাত্র Markdown অনুবাদ করে, তাই Azure AI Vision প্রয়োজন নয়।

1. আপনার অনুবাদ করতে চাওয়া রিপোজিটরিতে [translate-readme.yml](../../assets/workflows/translate-readme.yml) ([GitHub-এ টেমপ্লেটটি দেখুন](https://github.com/Azure/co-op-translator/blob/main/docs/assets/workflows/translate-readme.yml)) কপি করে `.github/workflows/translate-readme.yml` এ রাখুন এবং সেটি রিপোজিটরির ডিফল্ট ব্রাঞ্চে কমিট করুন। টেমপ্লেটটি root Action হিসেবে `Azure/co-op-translator@main` ব্যবহার করে, যা একই সোর্স রিফ থেকে CLI ইনস্টল করে। পুনরুৎপাদনযোগ্য রানগুলো নিশ্চিত করতে একটি পর্যালোচিত কমিট পিন করুন।
2. খুলুন **Actions > Translate README > Run workflow**, একটি ভাষা নির্বাচন করুন, এবং **Preview only** চেক করা রেখুন। প্রিভিউ ধাপে টোকেন অনুমান পর্যালোচনা করুন। প্রিভিউ কোন মডেল প্রোভাইডারকে কল করে না, অনুবাদ লেখে না, এবং PR তৈরি করে না।
3. একটি [টেক্সট প্রোভাইডারের](#prerequisites) জন্য সিক্রেটস যোগ করুন, এবং **Settings > Actions > General**-এ **GitHub Actions কে পুল রিকোয়েস্ট তৈরি ও অনুমোদন করার অনুমতি দিন** সক্রিয় করুন। টেমপ্লেটটি তার জব-এর জন্য `contents: write` এবং `pull-requests: write` অনুরোধ করে; প্রতিটি ওয়ার্কফ্লোর জন্য ডিফল্ট অনুমতিগুলো পরিবর্তন করার প্রয়োজন নেই। যদি সংগঠনের নীতিমালা এই অনুমতিগুলো বা সেটিংটি ব্লক করে, একটি অনুমোদিত [GitHub App](#github-app-setup) সম্পর্কে প্রশাসকের সঙ্গে আলোচনা করুন।
4. **Preview only** অনচেক করে ওয়ার্কফ্লোটি আবার রান করুন। এটি প্রিভিউ করে, অনুবাদ করে, `co-op-review --readme-only` চালায়, এবং কেবল অনুবাদ ও রিভিউ সফল হওয়ার পরই একটি অনুবাদ PR তৈরি বা আপডেট করে। ওয়ার্কফ্লো সারাংশ PR-এ লিংক করে।
5. PR-এ শব্দচয়ন এবং ফাইল পরিবর্তনগুলো পর্যালোচনা করুন, তারপর প্রস্তুত হলে মার্জ করুন। ওয়ার্কফ্লো স্বয়ংক্রিয়ভাবে মার্জ করে না।

PR-টিতে কেবল `translations/<language>/README.md` এবং তার ভাষা মেটাডাটা ফাইল থাকে। সোর্স README অপরিবর্তিত থাকে, এবং অন্যান্য ডকুমেন্টের লিঙ্কগুলো সোর্স ডকুমেন্টদের দিকে ইঙ্গিত করে থাকে। PR বডিতে পরিবর্তিত ফাইলগুলো এবং স্ট্রাকচারাল রিভিউ ফলাফল তালিকাভুক্ত থাকে। যদি অনুবাদ বা রিভিউ ব্যর্থ হয়, ওয়ার্কফ্লো সারাংশ এবং ব্যর্থ স্টেপ লগগুলো পরীক্ষা করুন; কোন PR তৈরি করা হয় না। যদি কোন পরিবর্তন না থাকে, নতুন PR-এর প্রয়োজন নেই।

**Organization and CI note:** একটি GitHub App ঐচ্ছিক, সংগঠন-অধিকার একটি শর্ত নয়। `GITHUB_TOKEN` ব্যবহার করে, PR খোলা, আপডেট করা বা পুনরায় খোলার জন্য pull-request ওয়ার্কফ্লোগুলোর জন্য একজন লিখনের অধিকার সম্পন্ন ব্যবহারকারীকে **Approve workflows to run** নির্বাচন করতে হয়। পুশ ওয়ার্কফ্লো এই টোকেন দিয়ে ট্রিগার হয় না। অনিয়ন্ত্রিত ডাউনস্ট্রীম CI-এর জন্য দেখুন [GitHub অ্যাপ সেটআপ](#github-app-setup) এবং GitHub-এর [ওয়ার্কফ্লো ট্রিগারিং নিয়ম](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)।

## পূর্বশর্ত

ওয়ার্কফ্লো তৈরি করার আগে আপনার অনুবাদ রান যে AI সার্ভিস সিক্রেটগুলো প্রয়োজন তা কনফিগার করুন।

টেক্সট অনুবাদের জন্য একটি ভাষা মডেল প্রোভাইডার প্রয়োজন:

- Azure OpenAI: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_MODEL_NAME`, `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_VERSION`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL_ID`, এছাড়াও ঐচ্ছিক `OPENAI_ORG_ID` এবং `OPENAI_BASE_URL`
- Anthropic: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, এছাড়াও ঐচ্ছিক `ANTHROPIC_BASE_URL`

ইমেজ অনুবাদের জন্য অতিরিক্তভাবে Azure AI Vision প্রয়োজন:

- `AZURE_AI_SERVICE_API_KEY`
- `AZURE_AI_SERVICE_ENDPOINT`

লোকাল কনফিগারেশনের বিস্তারিত জানার জন্য দেখুন [কনফিগারেশন](configuration.md) এবং [Azure AI সেটআপ](azure-ai-setup.md)।

## স্ট্যান্ডার্ড সেটআপ

README ওয়ার্কফ্লোটি চেষ্টা করার পর, এই সেটআপ ব্যবহার করে একটি রিপোজিটরির Markdown ফাইলগুলো বিভিন্ন ভাষায় অনুবাদ করুন। এটি PR খুলার আগে একটি Markdown রিভিউ চালায় এবং Azure AI Vision প্রয়োজন হয় না।

### ধাপ 1: রিপোজিটরির সিক্রেটস যোগ করুন

আপনার লক্ষ্য রিপোজিটরিতে, খুলুন **Settings** > **Secrets and variables** > **Actions**, তারপর আপনার ওয়ার্কফ্লো যে প্রোভাইডার সিক্রেটগুলো ব্যবহার করবে সেগুলো যোগ করুন।

![Actions সিক্রেটস নির্বাচন করুন](../../assets/github-actions/select-setting-action.png)

### ধাপ 2: ওয়ার্কফ্লো অনুমতিসমূহ সক্রিয় করুন

খুলুন **Settings** > **Actions** > **General**।

**Workflow permissions** এর অধীনে:

1. সক্রিয় করুন **GitHub Actions কে পুল রিকোয়েস্ট তৈরি ও অনুমোদন করার অনুমতি দিন**।
2. সেটিটি সেভ করুন।

নিচের জবটি স্পষ্টভাবে `contents: write` এবং `pull-requests: write` অনুরোধ করে। রিপোজিটরির ডিফল্ট ওয়ার্কফ্লো অনুমতিগুলো অপরিবর্তিত রাখুন। যদি সংগঠনের নীতি PR তৈরি ব্লক করে, একজন প্রশাসকের কাছে অনুমোদিত [GitHub অ্যাপ](#github-app-setup) সম্পর্কে জিজ্ঞাসা করুন।

### ধাপ 3: ওয়ার্কফ্লো যোগ করুন

তৈরি করুন `.github/workflows/co-op-translator.yml`:

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest
    env:
      TARGET_LANGUAGES: "es fr de"

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.11"

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          ANTHROPIC_MODEL: ${{ secrets.ANTHROPIC_MODEL }}
          ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
        run: |
          translate -l "$TARGET_LANGUAGES" -md -y

      - name: Review Markdown translations
        run: |
          python - <<'PY'
          import os
          from co_op_translator.api import run_review

          run_review(
              language_codes=os.environ["TARGET_LANGUAGES"].split(),
              markdown=True,
              notebook=False,
              output_format="github",
          )
          PY

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Update translations via Co-op Translator"
          title: "Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.
            Markdown structure, freshness, and local links were reviewed.
            Review translation wording before merging.

            Generated by Co-op Translator.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
```

আপনার প্রজেক্ট যেসব ভাষা চায় তা অনুযায়ী `TARGET_LANGUAGES` পরিবর্তন করুন। রিভিউটি Markdown-ই চেক করতে Python API ব্যবহার করে, যা অনুবাদ ধাপের সঙ্গে মিলে। অনুবাদ বা রিভিউ ত্রুটি PR তৈরি হওয়ার আগে জব বন্ধ করে দেয়। ওয়ার্কফ্লো PR স্বয়ংক্রিয়ভাবে মার্জ করে না। বড় রিপোজিটরির জন্য, `on.push` এর অধীনে একটি `paths:` ফিল্টার যোগ করুন যাতে ওয়ার্কফ্লো কেবল ডকুমেন্টেশন পরিবর্তিত হলে চালানো হয়।

### ঐচ্ছিক: নোটবুক এবং ইমেজ

নোটবুকগুলোর জন্য, অনুবাদ কমান্ডে `-nb` যোগ করুন এবং রিভিউ স্টেপে `notebook=True` সেট করুন। ইমেজ টেক্সটের জন্য, দুইটি [Azure AI Vision secrets](#prerequisites) কনফিগার করুন, সেগুলোকে অনুবাদ স্টেপের `env`-এ পাঠান, কমান্ডে `-img` যোগ করুন, এবং PR স্টেপের `add-paths`-এ `translated_images/` যোগ করুন। অনুবাদকৃত ইমেজগুলো ভিজ্যুয়ালি পর্যালোচনা করুন; নির্ধারণমূলক রিভিউ ইমেজ টেক্সট বা ভাষাগত সঠিকতা সনদীভূত করে না।

## GitHub অ্যাপ সেটআপ

আপনার সংগঠন যখন একটি অ্যাপ আইডেন্টিটি দাবি করে, অথবা যখন তৈরি হওয়া PR-কে `GITHUB_TOKEN` অনুমোদন ধাপ ছাড়া ডাউনস্ট্রীম CI ট্রিগার করতে হবে, তখন একটি অনুমোদিত GitHub App ব্যবহার করুন। একটি অ্যাপ সংগঠন নীতিকে বাইপাস করে না; প্রশাসকরা এখনও এর ইনস্টলেশন এবং অনুমতিগুলো নিয়ন্ত্রণ করে।

### ধাপ 1: একটি GitHub অ্যাপ তৈরি করুন বা ইনস্টল করুন

যদি উপলব্ধ থাকে তাহলে একটি বিদ্যমান সংগঠন-প্রদান করা অ্যাপ ব্যবহার করুন, অথবা **Contents** এবং **Pull requests**-এ রিড/রাইট অ্যাক্সেস সহ একটি অ্যাপ তৈরি করুন। প্রয়োজনীয় সংগঠন অনুমোদন নিয়ে সেটি লক্ষ্য রিপোজিটরিতে ইনস্টল করুন।

নোট করে রাখুন:

- অ্যাপ ID
- প্রাইভেট কী কন্টেন্টস

তাদের রিপোজিটরি সিক্রেটস হিসেবে সংরক্ষণ করুন:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

### ধাপ 2: একটি অ্যাপ টোকেন জেনারেট করুন

এই স্টেপটি বিদ্যমান পুল রিকোয়েস্ট স্টেপের ঠিক আগে যোগ করুন। README টেমপ্লেটের জন্য, একই সফলতা শর্ত ব্যবহার করুন যাতে প্রিভিউ এবং ব্যর্থ অনুবাদগুলো অ্যাপ টোকেন অনুরোধ না করে:

```yaml
      - name: Authenticate GitHub App
        id: generate_token
        if: ${{ !inputs.preview && steps.translate.outcome == 'success' && steps.review.outcome == 'success' }}
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.GH_APP_ID }}
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
```

তারপর কেবল বিদ্যমান পুল রিকোয়েস্ট স্টেপের `token` ইনপুটটি `${{ steps.generate_token.outputs.token }}` এ পরিবর্তন করুন। এর সফলতা শর্ত, ব্রাঞ্চ, PR বডি, এবং `add-paths` অপরিবর্তিত রাখুন। টোকেন ডিফল্টভাবে বর্তমান রিপোজিটরির সীমাবদ্ধ। README টেমপ্লেটের পরিবর্তে স্ট্যান্ডার্ড সেটআপ অভিযোজিত করার সময় উপরোক্ত `if` বাদ দিন: সেই ওয়ার্কফ্লো ডিফল্ট সফলতা শর্ত ব্যবহার করে, তাই টোকেন সৃষ্টিতে এবং PR তৈরিতে অনুবাদ ও রিভিউ সফল হওয়ার পরেই রান হয়।

ইনস্টলেশন এবং টোকেন অনুমতিগুলোর জন্য অফিসিয়াল [create-github-app-token Action](https://github.com/actions/create-github-app-token/tree/v2) দেখুন।

## রানার সীমা

GitHub-হোস্টেড রানারগুলোর একটি সর্বোচ্চ জব সময়সীমা আছে। বড় রিপোজিটরি বা অনেক লক্ষ্য ভাষা সেই সীমা ছাড়িয়ে যেতে পারে।

বড় অনুবাদ কাজের জন্য:

- প্রতিটি রানে কম ভাষা অনুবাদ করুন।
- `-md`, `-nb`, বা `-img` এর মতো কনটেন্ট ফ্ল্যাগ ব্যবহার করুন।
- যখন রিপোজিটরির আকার বা মডেলের ল্যাটেন্সি হোস্টেড রানারগুলোকে অনির্ভরযোগ্য করে, তখন সেল্ফ-হোস্টেড রানার ব্যবহার করুন।

## CI-এ পর্যালোচনা

যখন একটি পুল রিকোয়েস্ট তৈরি হওয়া অনুবাদগুলো LLM বা Vision প্রোভাইডারকে কল না করে যাচাইকরণ করা উচিত, তখন `co-op-review` ব্যবহার করুন।

```yaml
      - name: Review translated outputs
        run: |
          co-op-review --changed-from "origin/${{ github.base_ref }}" --format github
```

`co-op-review` একটি বিটা নির্ধারণমূলক রিভিউ কমান্ড। এর চেক এবং আউটপুট স্কিমা পরিবর্তিত হতে পারে, তবে এটি CI-এর জন্য নিরাপদ হওয়ার উদ্দেশ্যে ডিজাইন করা হয়েছে কারণ এটি ফাইল লেখে না বা মডেল প্রোভাইডারকে কল করে না।