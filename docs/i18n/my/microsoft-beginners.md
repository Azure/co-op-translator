# Microsoft Beginners Repositories

ဤစာမျက်နှာသည် Microsoft "For Beginners" repositories များတွင် shared "Other Courses" README အပိုင်းကို အသုံးပြုသော ထိန်းသိမ်းသူများအတွက် ဖြစ်သည်။

Most Co-op Translator users do not need this page.

## Auto-Sync the Other Courses Section

README အတွင်းရှိ "Other Courses" အပိုင်းပတ်လည်တွင် အောက်ပါ မှတ်သားချက်များကို ထည့်ပါ။

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator ကို CLI သို့မဟုတ် GitHub Actions မှတဆင့် run လိုက်တိုင်း အဆိုပါ မှတ်သားချက်များအကြားရှိ အကြောင်းအရာများကို packaged template ဖြင့် အစားထိုးပေးပါလိမ့်မည်။

## Update the Shared Template

Template ရဲ့ အရင်းအမြစ်ကို အောက်မှာ တွေ့နိုင်သည်။

```text
src/co_op_translator/templates/other_courses.md
```

မျှဝေထားသော အကြောင်းအရာကို အပ်ဒိတ်လုပ်ရန်:

1. Template ကို တည်းဖြတ်ပါ။
2. Co-op Translator သို့ pull request ကို ဖွင့်ပါ။
3. ပြောင်းလဲမှု ထုတ်ပြန်ပြီးနောက် ရည်မှန်းထားသော repository တွင် Co-op Translator ကို run လုပ်ပါ။

## Sparse Checkout Advisory

ဘာသာပြန်ထုတ်လွှင့်ထားသော output များစွာပါဝင်လျှင် course repository များကို clone လုပ်ရရန် ကုန်ကျစရိတ်များ မြင့်တက်နိုင်သည်။ ဤသတိပေးချက်ကို ဖန်တီးထားသော ဘာသာစကား အပိုင်းများတွင် ထည့်သွင်းနိုင်သည်။

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