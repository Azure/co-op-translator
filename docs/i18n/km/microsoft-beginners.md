# ឃ្លាំងកូដ Microsoft សម្រាប់អ្នកចាប់ផ្តើម

ទំព័រនេះសម្រាប់អ្នកថែទាំនៃឃ្លាំងកូដ Microsoft "For Beginners" ដែលប្រើផ្នែក README រួម "Other Courses"។

Most Co-op Translator users do not need this page.

## សមកតស្វ័យប្រវត្តិសម្រាប់ផ្នែក 'Other Courses'

Add these markers around the "Other Courses" section in your README:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Each time Co-op Translator runs through the CLI or GitHub Actions, it replaces the content between the markers with the packaged template.

## ធ្វើបច្ចុប្បន្នភាពពុម្ពរួម

The template source lives at:

```text
src/co_op_translator/templates/other_courses.md
```

To update the shared content:

1. Edit the template.
2. Open a pull request to Co-op Translator.
3. After the change is released, run Co-op Translator in the target repository.

## ការព្រមានសម្រាប់ Sparse Checkout

ឃ្លាំងកូដមុខវិជ្ជាធំៗ អាចមានការចំណាយខ្ពស់ក្នុងការទាញ (clone) ពេលពួកវាផ្ទុកលទ្ធផលបកប្រែជាច្រើន។ អ្នកអាចបញ្ចូលសេចក្តីព្រមាននេះក្នុងផ្នែកភាសាដែលបានបង្កើត៖

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