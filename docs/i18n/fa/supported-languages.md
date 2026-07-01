# زبان‌های پشتیبانی‌شده

Co-op Translator از کدهای زبان زیر برای خروجی‌های ترجمهٔ متن، نوت‌بوک و تصویر پشتیبانی می‌کند.

اگر می‌خواهید یک زبان جدید اضافه کنید، نقشه‌های زبان و فونت را در `src/co_op_translator/fonts/` به‌روزرسانی کنید و قبل از باز کردن یک pull request زبان را آزمایش کنید.

| Language Code | نام زبان | Font | پشتیبانی راست‌به‌چپ | مشکلات شناخته‌شده |
| --- | --- | --- | --- | --- |
| en | انگلیسی | NotoSans-Medium.ttf | خیر | خیر |
| fr | فرانسوی | NotoSans-Medium.ttf | خیر | خیر |
| es | اسپانیایی | NotoSans-Medium.ttf | خیر | خیر |
| de | آلمانی | NotoSans-Medium.ttf | خیر | خیر |
| ru | روسی | NotoSans-Medium.ttf | خیر | خیر |
| ar | عربی | NotoSansArabic-Medium.ttf | بله | خیر |
| fa | فارسی | NotoSansArabic-Medium.ttf | بله | خیر |
| ur | اردو | NotoSansArabic-Medium.ttf | بله | خیر |
| zh-CN | چینی (ساده‌شده) | NotoSansCJK-Medium.ttc | خیر | خیر |
| zh-MO | چینی (سنتی، ماکائو) | NotoSansCJK-Medium.ttc | خیر | خیر |
| zh-HK | چینی (سنتی، هنگ‌کنگ) | NotoSansCJK-Medium.ttc | خیر | خیر |
| zh-TW | چینی (سنتی، تایوان) | NotoSansCJK-Medium.ttc | خیر | خیر |
| ja | ژاپنی | NotoSansCJK-Medium.ttc | خیر | خیر |
| ko | کره‌ای | NotoSansCJK-Medium.ttc | خیر | خیر |
| hi | هندی | NotoSansDevanagari-Medium.ttf | خیر | خیر |
| bn | بنگالی | NotoSansBengali-Medium.ttf | خیر | خیر |
| mr | مراکشی | NotoSansDevanagari-Medium.ttf | خیر | خیر |
| ne | نپالی | NotoSansDevanagari-Medium.ttf | خیر | خیر |
| pa | پنجابی (گورموخی) | NotoSansGurmukhi-Medium.ttf | خیر | خیر |
| pt-PT | پرتغالی (پرتغال) | NotoSans-Medium.ttf | خیر | خیر |
| pt-BR | پرتغالی (برزیل) | NotoSans-Medium.ttf | خیر | خیر |
| it | ایتالیایی | NotoSans-Medium.ttf | خیر | خیر |
| lt | لیتوانیایی | NotoSans-Medium.ttf | خیر | خیر |
| pl | لهستانی | NotoSans-Medium.ttf | خیر | خیر |
| tr | ترکی | NotoSans-Medium.ttf | خیر | خیر |
| el | یونانی | NotoSans-Medium.ttf | خیر | خیر |
| th | تایلندی | NotoSansThai-Medium.ttf | خیر | خیر |
| sv | سوئدی | NotoSans-Medium.ttf | خیر | خیر |
| da | دانمارکی | NotoSans-Medium.ttf | خیر | خیر |
| no | نروژی | NotoSans-Medium.ttf | خیر | خیر |
| fi | فنلاندی | NotoSans-Medium.ttf | خیر | خیر |
| nl | هلندی | NotoSans-Medium.ttf | خیر | خیر |
| he | عبری | NotoSansHebrew-Medium.ttf | بله | خیر |
| vi | ویتنامی | NotoSans-Medium.ttf | خیر | خیر |
| id | اندونزیایی | NotoSans-Medium.ttf | خیر | خیر |
| ms | مالایی | NotoSans-Medium.ttf | خیر | خیر |
| tl | تاگالوگ (فیلیپینی) | NotoSans-Medium.ttf | خیر | خیر |
| sw | سواحیلی | NotoSans-Medium.ttf | خیر | خیر |
| hu | مجارستانی | NotoSans-Medium.ttf | خیر | خیر |
| cs | چکی | NotoSans-Medium.ttf | خیر | خیر |
| sk | اسلواکی | NotoSans-Medium.ttf | خیر | خیر |
| ro | رومانیایی | NotoSans-Medium.ttf | خیر | خیر |
| bg | بلغاری | NotoSans-Medium.ttf | خیر | خیر |
| sr | صربی (سیریلیک) | NotoSans-Medium.ttf | خیر | خیر |
| hr | کرواتی | NotoSans-Medium.ttf | خیر | خیر |
| sl | اسلوونیایی | NotoSans-Medium.ttf | خیر | خیر |
| uk | اوکراینی | NotoSans-Medium.ttf | خیر | خیر |
| my | برمه‌ای (میانمار) | NotoSansMyanmar-Medium.ttf | خیر | خیر |
| ta | تامیلی | NotoSansTamil-Medium.ttf | خیر | خیر |
| et | استونیایی | NotoSans-Medium.ttf | خیر | خیر |
| pcm | پیدج (نیجریایی) | NotoSans-Medium.ttf | خیر | خیر |
| te | تلگو | NotoSans-Medium.ttf | خیر | خیر |
| ml | مالایالم | NotoSans-Medium.ttf | خیر | خیر |
| kn | کانّادا | NotoSans-Medium.ttf | خیر | خیر |
| km | خمری | NotoSansKhmer-Medium.ttf | خیر | خیر |

## افزودن یک زبان

برای اضافه کردن پشتیبانی از یک زبان جدید:

1. کد زبان و نام نمایشی را به ابزارهای زبان اضافه کنید.
2. یک فونت اضافه کنید یا آن را در `src/co_op_translator/fonts/font_language_mappings.yml` نگاشت کنید.
3. خروجی ترجمهٔ Markdown و تصویر را آزمایش کنید.
4. یک pull request حاوی نگاشت و یادداشت‌های اعتبارسنجی باز کنید.