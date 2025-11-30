<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T04:12:36+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "my"
}
-->
# အမိန့်များအကြောင်းအရာ

**Co-op Translator** CLI မှာ ဘာသာပြန်လုပ်ငန်းစဉ်ကို ကိုယ်တိုင်ပြင်ဆင်နိုင်ဖို့ ရွေးချယ်စရာအမျိုးမျိုးရှိပါတယ်။

အမိန့်                                       | ရှင်းလင်းချက်
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | သတ်မှတ်ထားတဲ့ ဘာသာစကားတွေကို သင့် project ကို ဘာသာပြန်ပေးပါမယ်။ ဥပမာ - translate -l "es fr de" ဆိုရင် စပိန်၊ ပြင်သစ်၊ ဂျာမန် ဘာသာပြန်ပေးပါမယ်။ translate -l "all" ဆိုရင် ပံ့ပိုးထားတဲ့ ဘာသာစကားအားလုံးကို ဘာသာပြန်ပေးပါမယ်။
translate -l "language_codes" -u              | ဘာသာပြန်ချက်တွေကို update လုပ်ပြီး ရှိပြီးသားတွေကို ဖျက်ပြီး ပြန်လည်ဖန်တီးပါမယ်။ သတိပေးချက် - သတ်မှတ်ထားတဲ့ ဘာသာစကားတွေအတွက် ရှိပြီးသား ဘာသာပြန်ချက်အားလုံးကို ဖျက်ပါမယ်။
translate -l "language_codes" -img            | ဓာတ်ပုံဖိုင်တွေကိုသာ ဘာသာပြန်ပါမယ်။
translate -l "language_codes" -md             | Markdown ဖိုင်တွေကိုသာ ဘာသာပြန်ပါမယ်။
translate -l "language_codes" -nb             | Jupyter notebook ဖိုင် (.ipynb) တွေကိုသာ ဘာသာပြန်ပါမယ်။
translate -l "language_codes" --fix           | အရည်အသွေးယုံကြည်မှုနိမ့်တဲ့ ဖိုင်တွေကို ပြန်လည်ဘာသာပြန်ပါမယ် (အရင်အကဲဖြတ်ရလဒ်အပေါ်မူတည်ပြီး)။
translate -l "language_codes" -d              | Debug mode ဖွင့်ပြီး အသေးစိတ် log တွေ ရယူနိုင်ပါတယ်။
translate -l "language_codes" --save-logs, -s | DEBUG-level log တွေကို <root_dir>/logs/ ထဲမှာ ဖိုင်အနေနဲ့ သိမ်းပါမယ် (console မှာတော့ -d နဲ့ ထိန်းချုပ်နိုင်ပါတယ်)
translate -l "language_codes" -r "root_dir"   | Project ရဲ့ root directory ကို သတ်မှတ်နိုင်ပါတယ်။
translate -l "language_codes" -f              | ဓာတ်ပုံဘာသာပြန်မှုအတွက် fast mode ကို သုံးပါမယ် (quality နဲ့ alignment နည်းနည်းလျော့နည်းပေမယ့် ၃ ဆအထိ မြန်မြန် plot လုပ်နိုင်ပါတယ်)။
translate -l "language_codes" -y              | Prompt အားလုံးကို အလိုအလျောက် အတည်ပြုပါမယ် (CI/CD pipeline တွေအတွက် အသုံးဝင်ပါတယ်)
translate -l "language_codes" --help          | CLI ထဲမှာ အသုံးပြုနိုင်တဲ့ command တွေကို ပြသပါမယ်
evaluate -l "language_code"                  | သတ်မှတ်ထားတဲ့ ဘာသာစကားအတွက် ဘာသာပြန်အရည်အသွေးကို အကဲဖြတ်ပြီး ယုံကြည်မှု score တွေ ပေးပါမယ်
evaluate -l "language_code" -c 0.8           | ယုံကြည်မှု threshold ကို ကိုယ်တိုင်သတ်မှတ်ပြီး ဘာသာပြန်ချက်တွေကို အကဲဖြတ်ပါမယ်
evaluate -l "language_code" -f               | Fast evaluation mode (rule-based သာ အသုံးပြုသည်၊ LLM မပါ)
evaluate -l "language_code" -D               | Deep evaluation mode (LLM-based သာ အသုံးပြုသည်၊ ပိုမိုအသေးစိတ်၊ ပိုနှေး)
evaluate -l "language_code" --save-logs, -s  | DEBUG-level log တွေကို <root_dir>/logs/ ထဲမှာ သိမ်းပါမယ်
migrate-links -l "language_codes"             | ဘာသာပြန်ပြီးသား Markdown ဖိုင်တွေကို ပြန်လည်လုပ်ပြီး notebook (.ipynb) link တွေ update လုပ်ပါမယ်။ ဘာသာပြန်ပြီးသား notebook ရှိရင် အဲဒါကို သုံးပြီး မရှိရင် မူရင်း notebook ကို fallback လုပ်နိုင်ပါတယ်။
migrate-links -l "language_codes" -r          | Project ရဲ့ root directory ကို သတ်မှတ်နိုင်ပါတယ် (default: လက်ရှိ directory)။
migrate-links -l "language_codes" --dry-run   | ဘယ်ဖိုင်တွေ ပြောင်းလဲမလဲ ပြသပေးမယ်၊ ပြောင်းလဲမှုမရှိပါ။
migrate-links -l "language_codes" --no-fallback-to-original | ဘာသာပြန်ပြီးသား notebook မရှိရင် မူရင်း notebook link ကို မပြန်ရေးပါနဲ့ (ဘာသာပြန်ပြီးသားရှိရင်သာ update လုပ်ပါမယ်)။
migrate-links -l "language_codes" -d          | Debug mode ဖွင့်ပြီး အသေးစိတ် log တွေ ရယူနိုင်ပါတယ်။
migrate-links -l "language_codes" --save-logs, -s | DEBUG-level log တွေကို <root_dir>/logs/ ထဲမှာ သိမ်းပါမယ်
migrate-links -l "all" -y                      | ဘာသာစကားအားလုံးကို process လုပ်ပြီး warning prompt ကို အလိုအလျောက် အတည်ပြုပါမယ်။

## အသုံးပြုနည်း ဥပမာများ

  1. Default အပြုအမူ (အသစ်ဘာသာပြန်ချက်တွေထည့်ပြီး ရှိပြီးသားတွေ မဖျက်):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. ကိုရီးယား ဓာတ်ပုံဘာသာပြန်ချက်အသစ်တွေထည့် (ရှိပြီးသားဘာသာပြန်ချက်တွေ မဖျက်):    translate -l "ko" -img

  3. ကိုရီးယား ဘာသာပြန်ချက်အားလုံးကို update (သတိပေးချက် - ရှိပြီးသားကိုရီးယားဘာသာပြန်ချက်အားလုံးကို ဖျက်ပြီး ပြန်ဘာသာပြန်):    translate -l "ko" -u

  4. ကိုရီးယား ဓာတ်ပုံတွေကိုသာ update (သတိပေးချက် - ရှိပြီးသားကိုရီးယားဓာတ်ပုံအားလုံးကို ဖျက်ပြီး ပြန်ဘာသာပြန်):    translate -l "ko" -img -u

  5. ကိုရီးယား markdown ဘာသာပြန်ချက်အသစ်တွေထည့် (အခြားဘာသာပြန်ချက်တွေ မထိခိုက်):    translate -l "ko" -md

  6. အရည်အသွေးယုံကြည်မှုနိမ့်တဲ့ ဘာသာပြန်ချက်တွေကို ပြင်ဆင်: translate -l "ko" --fix

  7. Markdown ဖိုင်တွေအတွက်သာ အရည်အသွေးနိမ့်တဲ့ ဘာသာပြန်ချက်တွေကို ပြင်ဆင်: translate -l "ko" --fix -md

  8. ဓာတ်ပုံဖိုင်တွေအတွက်သာ အရည်အသွေးနိမ့်တဲ့ ဘာသာပြန်ချက်တွေကို ပြင်ဆင်: translate -l "ko" --fix -img

  9. ဓာတ်ပုံဘာသာပြန်မှုအတွက် fast mode သုံး:    translate -l "ko" -img -f

  10. ကိုယ်တိုင် threshold သတ်မှတ်ပြီး အရည်အသွေးနိမ့်တဲ့ ဘာသာပြန်ချက်တွေကို ပြင်ဆင်: translate -l "ko" --fix -c 0.8

  11. Debug mode ဥပမာ: - translate -l "ko" -d: Debug logging ဖွင့်ပါ။
  12. Log တွေကို ဖိုင်ထဲသိမ်း: translate -l "ko" -s
  13. Console DEBUG နဲ့ file DEBUG: translate -l "ko" -d -s

  14. ကိုရီးယား ဘာသာပြန်ချက်တွေအတွက် notebook link တွေ migrate လုပ် (ဘာသာပြန်ပြီးသား notebook ရှိရင် link ကို update):    migrate-links -l "ko"

  15. Dry-run နဲ့ link migrate လုပ် (ဖိုင်မပြောင်း):    migrate-links -l "ko" --dry-run

  16. ဘာသာပြန်ပြီးသား notebook ရှိမှသာ link update လုပ် (မူရင်းကို fallback မလုပ်):    migrate-links -l "ko" --no-fallback-to-original

  17. ဘာသာစကားအားလုံးအတွက် confirmation prompt နဲ့ process လုပ်:    migrate-links -l "all"

  18. ဘာသာစကားအားလုံးအတွက် auto-confirm နဲ့ process လုပ်:    migrate-links -l "all" -y
  19. migrate-links အတွက် log တွေကို ဖိုင်ထဲသိမ်း:    migrate-links -l "ko ja" -s

### အကဲဖြတ်မှု ဥပမာများ

> [!WARNING]  
> **Beta Feature**: အကဲဖြတ်မှုလုပ်ဆောင်ချက်ဟာ လက်ရှိ beta ဖြစ်ပါတယ်။ ဘာသာပြန်ထားတဲ့စာရွက်စာတမ်းတွေကို အကဲဖြတ်ဖို့အတွက် release လုပ်ထားတာဖြစ်ပြီး၊ အကဲဖြတ်နည်းနဲ့ အသေးစိတ်လုပ်ဆောင်မှုတွေကတော့ တိုးတက်နေဆဲဖြစ်လို့ ပြောင်းလဲနိုင်ပါတယ်။

  1. ကိုရီးယား ဘာသာပြန်ချက်တွေကို အကဲဖြတ်: evaluate -l "ko"

  2. ကိုယ်တိုင် ယုံကြည်မှု threshold သတ်မှတ်ပြီး အကဲဖြတ်: evaluate -l "ko" -c 0.8

  3. Fast evaluation (rule-based သာ): evaluate -l "ko" -f

  4. Deep evaluation (LLM-based သာ): evaluate -l "ko" -D

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းသည် မူလဘာသာစကားဖြင့် အာဏာရှိသောရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များ၏ ဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာနိုင်သော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှုမှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။