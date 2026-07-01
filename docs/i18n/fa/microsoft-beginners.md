# مخازن Microsoft برای مبتدیان

این صفحه برای نگهدارندگان مخازن Microsoft "For Beginners" است که از بخش مشترک "Other Courses" در README استفاده می‌کنند.

اکثر کاربران Co-op Translator نیازی به این صفحه ندارند.

## همگام‌سازی خودکار بخش Other Courses

این نشانگرها را در اطراف بخش "Other Courses" در README خود اضافه کنید:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

هر بار که Co-op Translator از طریق CLI یا GitHub Actions اجرا می‌شود، محتوای بین نشانگرها را با قالب بسته‌بندی‌شده جایگزین می‌کند.

## به‌روزرسانی قالب مشترک

منبع قالب در این مسیر قرار دارد:

```text
src/co_op_translator/templates/other_courses.md
```

برای به‌روزرسانی محتوای مشترک:

1. قالب را ویرایش کنید.
2. یک pull request به Co-op Translator باز کنید.
3. پس از انتشار تغییر، Co-op Translator را در مخزن هدف اجرا کنید.

## توصیه درباره Sparse Checkout

مخزن‌های بزرگ دوره می‌توانند وقتی شامل خروجی‌های ترجمه‌شده متعدد هستند، هزینه‌بر برای کلون شدن شوند. می‌توانید این توصیه را در بخش‌های زبانی تولیدشده وارد کنید:

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