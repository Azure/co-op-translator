<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:30:22+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "bn"
}
-->
# Co-op Translator-এ অবদান রাখা

এই প্রকল্পে অবদান এবং পরামর্শ স্বাগত। বেশিরভাগ অবদানের জন্য আপনাকে একটি Contributor License Agreement (CLA)-তে সম্মত হতে হবে যা ঘোষণা করে যে আপনি আপনার অবদান ব্যবহারের অধিকার রাখেন এবং আমাদের সেই অধিকার প্রদান করছেন। বিস্তারিত জানতে https://cla.opensource.microsoft.com এ যান।

যখন আপনি একটি pull request জমা দেন, CLA বট স্বয়ংক্রিয়ভাবে নির্ধারণ করবে যে আপনাকে CLA প্রদান করতে হবে কিনা এবং PR-এ যথাযথভাবে নির্দেশনা যোগ করবে (যেমন, স্ট্যাটাস চেক, মন্তব্য)। বটের নির্দেশনা অনুসরণ করুন। আমাদের CLA ব্যবহার করা সব রেপোতে একবারই এটি করতে হবে।

## ডেভেলপমেন্ট পরিবেশ সেটআপ

এই প্রকল্পের ডেভেলপমেন্ট পরিবেশ সেটআপ করার জন্য আমরা Poetry ব্যবহারের পরামর্শ দিই ডিপেন্ডেন্সি ব্যবস্থাপনার জন্য। আমরা `pyproject.toml` ব্যবহার করি প্রকল্পের ডিপেন্ডেন্সি ম্যানেজ করতে, তাই ডিপেন্ডেন্সি ইনস্টল করতে Poetry ব্যবহার করা উচিত।

### ভার্চুয়াল এনভায়রনমেন্ট তৈরি

#### pip ব্যবহার করে

```bash
python -m venv .venv
```

#### Poetry ব্যবহার করে

```bash
poetry init
```

### ভার্চুয়াল এনভায়রনমেন্ট সক্রিয় করা

#### pip এবং Poetry উভয়ের জন্য

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry ব্যবহার করে

```bash
poetry shell
```

### প্যাকেজ এবং প্রয়োজনীয় প্যাকেজ ইনস্টল করা

#### Poetry ব্যবহার করে (pyproject.toml থেকে)

```bash
poetry install
```

### ম্যানুয়াল টেস্টিং

PR জমা দেওয়ার আগে, বাস্তব ডকুমেন্টেশন দিয়ে অনুবাদ ফাংশনালিটি পরীক্ষা করা গুরুত্বপূর্ণ:

1. রুট ডিরেক্টরিতে একটি টেস্ট ডিরেক্টরি তৈরি করুন:
    ```bash
    mkdir test_docs
    ```

2. কিছু মার্কডাউন ডকুমেন্টেশন এবং ছবি টেস্ট ডিরেক্টরিতে কপি করুন যেগুলো আপনি অনুবাদ করতে চান। উদাহরণস্বরূপ:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. প্যাকেজটি লোকালি ইনস্টল করুন:
    ```bash
    pip install -e .
    ```

4. আপনার টেস্ট ডকুমেন্টে Co-op Translator চালান:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. অনূদিত ফাইলগুলো `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` ফাইলে পরীক্ষা করুন।
1. নির্দেশনা অনুযায়ী environment ভেরিয়েবল পূরণ করুন।

> [!TIP]
>
> ### অতিরিক্ত ডেভেলপমেন্ট পরিবেশ অপশন
>
> প্রকল্পটি লোকালি চালানোর পাশাপাশি, বিকল্প ডেভেলপমেন্ট পরিবেশ সেটআপের জন্য GitHub Codespaces বা VS Code Dev Containers ব্যবহার করতে পারেন।
>
> #### GitHub Codespaces
>
> GitHub Codespaces ব্যবহার করে এই স্যাম্পলগুলো ভার্চুয়ালি চালানো যায় এবং অতিরিক্ত কোন সেটআপের দরকার নেই।
>
> বোতামটি আপনার ব্রাউজারে একটি ওয়েব-ভিত্তিক VS Code ইন্সট্যান্স খুলবে:
>
> 1. টেমপ্লেটটি খুলুন (কিছু মিনিট সময় লাগতে পারে):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers ব্যবহার করে লোকালি চালানো
>
> ⚠️ এই অপশনটি কেবল তখনই কাজ করবে যখন আপনার Docker Desktop কমপক্ষে 16 GB RAM বরাদ্দ পেয়েছে। যদি আপনার RAM 16 GB এর কম হয়, তাহলে [GitHub Codespaces অপশন](../..) ব্যবহার করতে পারেন অথবা [লোকালি সেটআপ করুন](../..)।
>
> একটি সংশ্লিষ্ট অপশন হলো VS Code Dev Containers, যা আপনার লোকাল VS Code-এ [Dev Containers এক্সটেনশন](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ব্যবহার করে প্রকল্পটি খুলবে:
>
> 1. Docker Desktop চালু করুন (যদি না থাকে তাহলে ইনস্টল করুন)
> 2. প্রকল্পটি খুলুন:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### কোড স্টাইল

আমরা প্রকল্পে সামঞ্জস্যপূর্ণ কোড স্টাইল বজায় রাখতে Python কোড ফরম্যাটারের জন্য [Black](https://github.com/psf/black) ব্যবহার করি। Black একটি কঠোর কোড ফরম্যাটার যা স্বয়ংক্রিয়ভাবে Python কোডকে Black কোড স্টাইল অনুযায়ী রিফরম্যাট করে।

#### কনফিগারেশন

আমাদের Black কনফিগারেশন `pyproject.toml` এ উল্লেখ করা আছে:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black ইনস্টল করা

আপনি Poetry (প্রস্তাবিত) অথবা pip ব্যবহার করে Black ইনস্টল করতে পারেন:

##### Poetry ব্যবহার করে

ডেভেলপমেন্ট পরিবেশ সেটআপ করার সময় Black স্বয়ংক্রিয়ভাবে ইনস্টল হয়:
```bash
poetry install
```

##### pip ব্যবহার করে

pip ব্যবহার করলে সরাসরি Black ইনস্টল করতে পারেন:
```bash
pip install black
```

#### Black ব্যবহার করা

##### Poetry এর মাধ্যমে

1. প্রকল্পের সব Python ফাইল ফরম্যাট করুন:
    ```bash
    poetry run black .
    ```

2. নির্দিষ্ট ফাইল বা ডিরেক্টরি ফরম্যাট করুন:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip এর মাধ্যমে

1. প্রকল্পের সব Python ফাইল ফরম্যাট করুন:
    ```bash
    black .
    ```

2. নির্দিষ্ট ফাইল বা ডিরেক্টরি ফরম্যাট করুন:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> আমরা সুপারিশ করি আপনার এডিটর এমনভাবে সেট করুন যাতে Black দিয়ে কোড সেভ করার সময় স্বয়ংক্রিয়ভাবে ফরম্যাট হয়। অধিকাংশ আধুনিক এডিটর এক্সটেনশন বা প্লাগইন এর মাধ্যমে এই সুবিধা দেয়।

## Co-op Translator চালানো

আপনার পরিবেশে Poetry ব্যবহার করে Co-op Translator চালাতে নিচের ধাপগুলো অনুসরণ করুন:

1. এমন ডিরেক্টরিতে যান যেখানে আপনি অনুবাদ পরীক্ষা করতে চান অথবা একটি টেম্পোরারি ফোল্ডার তৈরি করুন টেস্টের জন্য।

2. নিচের কমান্ডটি চালান। `-l ko` with the language code you wish to translate into. The `-d` ফ্ল্যাগ ডিবাগ মোড নির্দেশ করে।

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> কমান্ড চালানোর আগে নিশ্চিত করুন আপনার Poetry পরিবেশ সক্রিয় আছে (poetry shell)।

## রক্ষণাবেক্ষক

### কমিট মেসেজ এবং মার্জ স্ট্র্যাটেজি

আমাদের প্রকল্পের কমিট ইতিহাসে ধারাবাহিকতা এবং স্পষ্টতা নিশ্চিত করতে, আমরা **Squash and Merge** স্ট্র্যাটেজি ব্যবহারের সময় **চূড়ান্ত কমিট মেসেজের জন্য** একটি নির্দিষ্ট কমিট মেসেজ ফরম্যাট অনুসরণ করি।

যখন একটি pull request (PR) মার্জ হয়, তখন আলাদা আলাদা কমিটগুলো একত্রিত হয়ে একটি কমিটে পরিণত হয়। পরিষ্কার এবং ধারাবাহিক ইতিহাস বজায় রাখতে চূড়ান্ত কমিট মেসেজ নিচের ফরম্যাট অনুসরণ করবে।

#### কমিট মেসেজ ফরম্যাট (squash and merge এর জন্য)

আমরা কমিট মেসেজের জন্য নিম্নলিখিত ফরম্যাট ব্যবহার করি:

```bash
<type>: <description> (#<PR number>)
```

- **type**: কমিটের শ্রেণীবিভাগ নির্ধারণ করে। আমরা নিম্নলিখিত টাইপগুলো ব্যবহার করি:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**দ্রষ্টব্য**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় সর্বোত্তম উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।