<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc205495d4eace1fabcdee963024069f",
  "translation_date": "2025-06-12T11:05:02+00:00",
  "source_file": "SECURITY.md",
  "language_code": "mo"
}
-->
## Security

Microsoft က ကျွန်တော်တို့ software products နဲ့ services တွေရဲ့ security ကို အလွန်ပြင်းပြင်းထန်ထန် တန်ဖိုးထားပါတယ်၊ ဒီမှာ GitHub organizations တွေမှ ကျွန်တော်တို့ စီမံခန့်ခွဲတဲ့ source code repositories အားလုံးပါဝင်ပြီး၊ အဲဒါတွေကတော့ [Microsoft](https://github.com/Microsoft), [Azure](https://github.com/Azure), [DotNet](https://github.com/dotnet), [AspNet](https://github.com/aspnet) နဲ့ [Xamarin](https://github.com/xamarin) တို့ပါဝင်ပါတယ်။

Microsoft ပိုင် repository တစ်ခုခုမှာ [Microsoft ရဲ့ security vulnerability အဓိပ္ပာယ်](https://aka.ms/security.md/definition) နဲ့ ကိုက်ညီတဲ့ security vulnerability တစ်ခုတွေ့ရှိလိုက်ရင် ကျွန်တော်တို့ကို အောက်ပါအတိုင်း သတင်းပေးပါ။

## Reporting Security Issues

**security vulnerabilities တွေကို public GitHub issues မှတစ်ဆင့် မတင်ပြရပါ။**

အစား Microsoft Security Response Center (MSRC) ကို [https://msrc.microsoft.com/create-report](https://aka.ms/security.md/msrc/create-report) မှတစ်ဆင့် သတင်းပေးပါ။

login မလုပ်ချင်ရင် [secure@microsoft.com](mailto:secure@microsoft.com) ကို အီးမေးလ်ပို့ပါ။ ဖြစ်နိုင်ရင် ကျွန်တော်တို့ရဲ့ PGP key နဲ့ သင့်စာကို encrypt လုပ်ပေးပါ။ ဒါကို [Microsoft Security Response Center PGP Key page](https://aka.ms/security.md/msrc/pgp) မှာ ဒေါင်းလုပ်ဆွဲနိုင်ပါတယ်။

24 နာရီအတွင်း တုံ့ပြန်ချက် ရရှိမှာဖြစ်ပါတယ်။ မရရှိပါက ကျွန်တော်တို့ကို အီးမေးလ်ဖြင့် ပြန်လည်ဆက်သွယ်ပေးပါ။ နောက်ထပ်အချက်အလက်များကို [microsoft.com/msrc](https://www.microsoft.com/msrc) တွင် ရှာဖွေကြည့်နိုင်ပါသည်။

အောက်ပါ အချက်အလက်များကို (ဖြည့်စွက်နိုင်သမျှ) ထည့်သွင်းပေးပါက ကျွန်တော်တို့အနေဖြင့် ပြဿနာရဲ့ အမျိုးအစားနဲ့ အကျယ်အဝန်းကို ပိုမိုနားလည်နိုင်မှာ ဖြစ်ပါတယ်။

  * ပြဿနာအမျိုးအစား (ဥပမာ buffer overflow, SQL injection, cross-site scripting စသည်)
  * ပြဿနာပေါ်လာတဲ့ source file(s) ရဲ့ လမ်းကြောင်းအပြည့်အစုံ
  * ထိခိုက်နေတဲ့ source code ရဲ့ တည်နေရာ (tag/branch/commit သို့မဟုတ် တိုက်ရိုက် URL)
  * ပြဿနာကို ပြန်လည်ဖန်တီးဖို့ လိုအပ်တဲ့ အထူး configuration များ
  * ပြဿနာကို ပြန်လည်ဖန်တီးဖို့ အဆင့်ဆင့် လမ်းညွှန်ချက်များ
  * proof-of-concept သို့မဟုတ် exploit code (ဖြစ်နိုင်ပါက)
  * ပြဿနာရဲ့ သက်ရောက်မှု၊ attacker တစ်ဦးက ပြဿနာကို ဘယ်လို အသုံးချနိုင်မလဲ

ဒီအချက်အလက်တွေက ကျွန်တော်တို့ကို သင့်ရဲ့ အစီရင်ခံစာကို ပိုမိုမြန်ဆန်စွာ စစ်ဆေးနိုင်ဖို့ ကူညီပါလိမ့်မယ်။

bug bounty အတွက် သတင်းပေးရင် ပိုပြီး ပြည့်စုံတဲ့ အစီရင်ခံစာတွေက ပိုမိုမြင့်မားတဲ့ bounty ဆုကြေးငွေ ရရှိနိုင်ပါတယ်။ ကျွန်တော်တို့ရဲ့ [Microsoft Bug Bounty Program](https://aka.ms/security.md/msrc/bounty) စာမျက်နှာမှာ လက်ရှိ အစီအစဉ်တွေကို ကြည့်ရှုနိုင်ပါတယ်။

## Preferred Languages

ကျွန်တော်တို့ ဆက်သွယ်မှုအားလုံးကို အင်္ဂလိပ်ဘာသာဖြင့် ဆက်သွယ်ရန် ရွေးချယ်ပါတယ်။

## Policy

Microsoft က [Coordinated Vulnerability Disclosure](https://aka.ms/security.md/cvd) နည်းလမ်းကို လိုက်နာပါတယ်။

**Disclaimer**:  
Thiz documont haz been translaited uzing AI translaition serviz [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accurazy, pleez be aware that automayted translaitions may contain errors or inaccuraseez. The original documont in its native langwage shood be considered the authoritativ sourz. For critical informashun, professional human translaition is rekomended. We are not liable for any misunderstandings or misinterpretashuns arising from the use of this translaition.