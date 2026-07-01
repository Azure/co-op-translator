# استكشاف الأخطاء وإصلاحها

Use this page when a translation run succeeds unexpectedly, fails during configuration, or produces output that needs review.

## ابدأ من هنا

1. شغّل أمرًا مركزًا أولاً، مثل `translate -l "ko" -md`.
2. أضف `-d` لسجلات تصحيح الأخطاء في وحدة التحكم.
3. أضف `-s` لحفظ سجلات التصحيح تحت `<root-dir>/logs/`.
4. شغّل `co-op-review` بعد الترجمة للتحقق من التحديث، البنية، والروابط المحلية.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## أخطاء التكوين

### لا مزود نموذج لغة

الخطأ:

```text
No language model configuration found.
```

الإصلاح:

- قم بتكوين Azure OpenAI أو OpenAI.
- تحقق أن المتغيرات موجودة في البيئة التي يُشغّل فيها الأمر.
- للاستخدام المحلي، ضعها في `.env` في جذر المشروع.

See [التكوين](configuration.md).

### ترجمة الصور بدون Azure AI Vision

الخطأ:

```text
Image translation requested but Azure AI Service is not configured.
```

الإصلاح:

- أضف `AZURE_AI_SERVICE_API_KEY`.
- أضف `AZURE_AI_SERVICE_ENDPOINT`.
- أو شغّل أمر نصّي فقط مثل `translate -l "ko" -md`.

### مفتاح أو نقطة نهاية غير صالحة

يمكن أن تشمل الأعراض `401`، أخطاء أذونات محجوبة، أو أخطاء وصول نقطة النهاية.

الإصلاح:

- تأكد أن المفتاح ينتمي لنفس مورد Azure كنقطة النهاية.
- تأكد أن المورد يدعم Vision عند استخدام `-img`.
- تأكد أن اسم نشر Azure OpenAI وإصدار API يتطابقان مع نشرِك.
- شغّل مع سجلات التصحيح: `translate -l "ko" -md -d -s`.

## لم يتم ترجمة أي ملفات

الأسباب الشائعة:

- العلامات المختارة لا تتطابق مع ملفاتك.
- توجد بالفعل ملفات مترجمة.
- ملفات المصدر تحت مجلدات مستبعدة.
- يتم تشغيل الأمر من جذر مشروع خاطئ.

التحققات:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

استخدم `--root-dir` عندما يُشغّل الأمر من خارج جذر المشروع.

## سلوك روابط غير متوقع

إعادة كتابة الروابط تعتمد على أنواع المحتوى المختارة:

- عند تضمين `-nb`: يمكن أن تشير روابط دفاتر الملاحظات إلى دفاتر مترجمة.
- عند استبعاد `-nb`: يمكن أن تظل روابط دفاتر الملاحظات تشير إلى دفاتر المصدر.
- عند تضمين `-img`: يمكن أن تشير روابط الصور إلى صور مترجمة.
- عند استبعاد `-img`: يمكن أن تظل روابط الصور تشير إلى صور المصدر.

شغّل ترجمة كاملة للمحتوى عندما يجب أن تفضل جميع الروابط الداخلية المخرجات المترجمة:

```bash
translate -l "ko" -md -nb -img
```

شغّل مراجعة الروابط بعد الترجمة:

```bash
co-op-review -l "ko"
```

## مشاكل عرض Markdown

إذا تم عرض Markdown المترجم بشكل غير صحيح:

- تحقق أن الـ frontmatter تبدأ وتنتهي بـ `---`.
- تحقق أن عدد أسوار الشيفرة يتطابق بين الملفات المصدر والمترجمة.
- شغّل `co-op-review` للقبض على مشاكل البنية الشائعة.
- أعد ترجمة الملف المحدد إذا تضرر المخرَج.

```bash
co-op-review -l "ko" --format github
```

## تشغيل GitHub Action ولكن لم يتم إنشاء طلب سحب

إذا أبلغ `peter-evans/create-pull-request` أن الفرع ليس متقدمًا على الأساس، فقد لم يعثر سير العمل على ملفات للالتزام.

الأسباب المحتملة:

- لم تنتج عملية الترجمة أي تغييرات.
- يستبعد `.gitignore` `translations/`، `translated_images/`، أو دفاتر ملاحظات مترجمة.
- لا يتطابق `add-paths` مع مجلدات المخرجات المولدة.
- خرجت خطوة الترجمة مبكرًا.

الإصلاحات:

1. تأكد أن الملفات المولدة موجودة في `translations/` أو `translated_images/`.
2. تأكد أن `.gitignore` لا يتجاهل المخرجات المولدة.
3. Use matching `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Temporarily add debug flags to the translate command:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirm workflow permissions include:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## جودة الترجمة

قد تتطلّب الترجمات الآلية مراجعة بشرية. استخدم `evaluate` فقط عندما تريد تقييم جودة تجريبيًا ومسارات عمل إصلاح للحالات منخفضة الثقة.

!!! warning "Experimental"
    يمكن أن يستخدم `evaluate` فحوصات مبنية على القواعد وLLM، وقد يتغير نموذج التقييم وسلوك البيانات الوصفية الخاصة به. أبْقِه خارج بوابات CI المطلوبة ما لم يكن سير عملك مُستعدًا للتغييرات.

للفحوصات الحتمية في CI، استخدم `co-op-review` بدلًا من ذلك.