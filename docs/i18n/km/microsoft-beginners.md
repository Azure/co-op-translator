# ឃ្លាំងកូដ Microsoft សម្រាប់អ្នកចាប់ផ្តើម

ទំព័រនេះសម្រាប់អ្នកថែទាំនៃឃ្លាំងកូដ Microsoft "For Beginners" ដែលប្រើផ្នែក README រួម "Other Courses"។

អ្នកប្រើប្រាស់ Co-op Translator ភាគច្រើនមិនត្រូវការទំព័រនេះទេ.

## សមកតស្វ័យប្រវត្តិសម្រាប់ផ្នែក 'Other Courses'

បន្ថែមម៉ាក័រទាំងនេះនៅជុំវិញផ្នែក "វគ្គផ្សេងទៀត" ក្នុង README របស់អ្នក:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

រាល់ពេលដែល Co-op Translator រត់តាម CLI ឬ GitHub Actions វានឹងជំនួសមាតិកាដែលនៅចន្លោះម៉ាក័រដោយពុម្ពដែលបានចងក្រង.

## ធ្វើបច្ចុប្បន្នភាពពុម្ពរួម

The template source lives at:

```text
src/co_op_translator/templates/other_courses.md
```

To update the shared content:

1. Edit the template.
2. បើក pull request ទៅកាន់ Co-op Translator.
3. បន្ទាប់ពីការផ្លាស់ប្តូរត្រូវបានចេញផ្សាយ សូមរត់ Co-op Translator នៅក្នុង repository គោលដៅ.

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