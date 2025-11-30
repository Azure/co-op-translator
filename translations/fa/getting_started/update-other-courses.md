<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:36:44+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "fa"
}
-->
# به‌روزرسانی بخش «دوره‌های دیگر» (مخازن Microsoft Beginners)

این راهنما توضیح می‌دهد چگونه بخش «دوره‌های دیگر» را با استفاده از Co‑op Translator به‌صورت خودکار همگام‌سازی کنید و چگونه قالب جهانی را برای همه مخازن به‌روزرسانی نمایید.

- مربوط به: فقط مخازن Microsoft Beginners
- کار با: Co‑op Translator CLI و GitHub Actions
- منبع قالب: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## شروع سریع: فعال‌سازی همگام‌سازی خودکار در مخزن شما

علامت‌های زیر را دور بخش «دوره‌های دیگر» در فایل README خود اضافه کنید. Co‑op Translator در هر اجرا، همه چیز بین این علامت‌ها را جایگزین می‌کند.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

هر بار که Co‑op Translator اجرا می‌شود — از طریق CLI (مثلاً `translate -l "<language codes>"`) یا GitHub Actions — به‌صورت خودکار بخش «دوره‌های دیگر» که بین این علامت‌ها قرار دارد را به‌روزرسانی می‌کند.

> [!NOTE]
> اگر فهرستی موجود دارید، کافی است آن را با همین علامت‌ها بپوشانید. اجرای بعدی آن را با محتوای استاندارد و به‌روز جایگزین خواهد کرد.

---

## چگونه محتوای جهانی را تغییر دهیم

اگر می‌خواهید محتوای استانداردی که در همه مخازن Beginners نمایش داده می‌شود را به‌روزرسانی کنید:

1. قالب را ویرایش کنید: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. یک درخواست pull به مخزن Co-op Translator با تغییرات خود باز کنید
3. پس از ادغام PR، نسخه Co‑op Translator به‌روزرسانی خواهد شد
4. دفعه بعد که Co‑op Translator (CLI یا GitHub Action) در مخزن هدف اجرا شود، بخش به‌روزرسانی شده را به‌صورت خودکار همگام‌سازی می‌کند

این کار منبع واحد و معتبری برای محتوای «دوره‌های دیگر» در تمام مخازن Beginners فراهم می‌کند.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->