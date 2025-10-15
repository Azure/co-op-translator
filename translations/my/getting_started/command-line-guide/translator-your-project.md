<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T04:13:59+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "my"
}
-->
# Co-op Translator ကိုသုံးပြီး သင့် project ကို ဘာသာပြန်ပါ

**Co-op Translator** က command-line interface (CLI) tool တစ်ခုဖြစ်ပြီး သင့် project ထဲမှာရှိတဲ့ markdown နဲ့ image ဖိုင်တွေကို ဘာသာစုံအတွက် ဘာသာပြန်နိုင်အောင် ကူညီပေးပါတယ်။ ဒီအပိုင်းမှာ tool ကိုဘယ်လိုသုံးရမလဲ၊ CLI option တွေကဘာလဲ၊ အသုံးပြုနည်းနမူနာတွေကို ရှင်းပြထားပါတယ်။

---

## နမူနာအခြေအနေများနဲ့ အသုံးပြုနည်းများ

**Co-op Translator** ကို အသုံးပြုတဲ့ နေရာအချို့နဲ့ သင့် project မှာ အသုံးပြုနိုင်တဲ့ command တွေကို ဥပမာနဲ့တင်ပြထားပါတယ်။

### ၁။ အခြေခံဘာသာပြန် (Single Language)

သင့် project (markdown ဖိုင်နဲ့ image ဖိုင်) အားလုံးကို တစ်ခုတည်းသော ဘာသာ (ဥပမာ ကိုရီးယား) သို့ ဘာသာပြန်ချင်ရင် ဒီ command ကိုသုံးပါ။

```bash
translate -l "ko"
```

ဒီ command က markdown နဲ့ image ဖိုင်အားလုံးကို ကိုရီးယားဘာသာသို့ ဘာသာပြန်ပေးမှာဖြစ်ပြီး၊ ရှိပြီးသား ဘာသာပြန်ဖိုင်တွေကို မဖျက်ဘဲ အသစ်ထပ်ထည့်ပေးပါလိမ့်မယ်။

#### Phi-3 CookBook မှာ ဥပမာ

**Phi-3 CookBook** မှာ ရှိပြီးသား markdown ဖိုင်နဲ့ image တွေကို ကိုရီးယားဘာသာပြန်ထည့်ဖို့ ဒီနည်းကိုသုံးခဲ့ပါတယ်။

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### ၂။ ဘာသာစုံပြန်ခြင်း

သင့် project ကို ဘာသာစုံ (ဥပမာ စပိန်၊ ပြင်သစ်၊ ဂျာမန်) သို့ ဘာသာပြန်ချင်ရင် ဒီ command ကိုသုံးပါ။

```bash
translate -l "es fr de"
```

ဒီ command က project ကို စပိန်၊ ပြင်သစ်၊ ဂျာမန် ဘာသာသို့ ဘာသာပြန်ပေးမှာဖြစ်ပြီး၊ ရှိပြီးသား ဘာသာပြန်ဖိုင်တွေကို မဖျက်ဘဲ အသစ်ထပ်ထည့်ပေးပါလိမ့်မယ်။

#### Phi-3 CookBook မှာ ဥပမာ

**Phi-3 CookBook** မှာ နောက်ဆုံး commit တွေကို reflect လုပ်ပြီးနောက် အသစ်ထည့်ထားတဲ့ markdown ဖိုင်နဲ့ image တွေကို ဘာသာစုံပြန်ဖို့ ဒီနည်းကိုသုံးခဲ့ပါတယ်။

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

### ၃။ ဘာသာပြန်ဖိုင်များ Update လုပ်ခြင်း (Existing Translation များဖျက်ပြီး အသစ်ပြန်ပြန်ခြင်း)

ရှိပြီးသား ဘာသာပြန်ဖိုင်တွေကို update လုပ်ချင်ရင် `-u` option ကိုသုံးပါ။ ဒီ option က သတ်မှတ်ထားတဲ့ ဘာသာစုံအတွက် ရှိပြီးသား ဘာသာပြန်ဖိုင်တွေကို ဖျက်ပြီး အသစ်ပြန်ပြန်ပေးပါလိမ့်မယ်။

```bash
translate -l "ko" -u
```

သတိပေးချက် - ဒီ command ကို run လုပ်မယ်ဆိုရင် ရှိပြီးသား ဘာသာပြန်ဖိုင်တွေကို ဖျက်မယ်ဆိုတာကို အတည်ပြုဖို့ မေးမြန်းပါလိမ့်မယ်။

#### Phi-3 CookBook မှာ ဥပမာ

**Phi-3 CookBook** မှာ စပိန်ဘာသာပြန်ဖိုင်အားလုံးကို update လုပ်ဖို့ ဒီနည်းကိုသုံးခဲ့ပါတယ်။ မူလ content တွေမှာ အရေးကြီးပြောင်းလဲမှုများရှိရင် ဒီနည်းကိုသုံးဖို့ အကြံပြုပါတယ်။ သို့သော် update လုပ်ဖို့ markdown ဖိုင်အနည်းငယ်သာရှိရင်တော့ အဲဒီဖိုင်တွေကို ကိုယ်တိုင်ဖျက်ပြီး `-a` နည်းနဲ့ အသစ်ပြန်ထည့်တာပိုအဆင်ပြေပါတယ်။

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### ၅။ Image ဖိုင်များသာ ဘာသာပြန်ခြင်း

Project ထဲမှာရှိတဲ့ image ဖိုင်တွေကိုသာ ဘာသာပြန်ချင်ရင် `-img` option ကိုသုံးပါ။

```bash
translate -l "ko" -img
```

ဒီ command က image တွေကို ကိုရီးယားဘာသာသို့သာ ဘာသာပြန်ပေးမှာဖြစ်ပြီး markdown ဖိုင်တွေကို မထိပါဘူး။

### ၆။ Markdown ဖိုင်များသာ ဘာသာပြန်ခြင်း

Project ထဲမှာရှိတဲ့ markdown ဖိုင်တွေကိုသာ ဘာသာပြန်ချင်ရင် `-md` option ကိုသုံးပါ။

```bash
translate -l "ko" -md
```

#### Phi-3 CookBook မှာ ဥပမာ

**Phi-3 CookBook** မှာ ကိုရီးယားဘာသာပြန်ဖိုင်တွေမှာ ဘာသာပြန် error ရှိ/မရှိ စစ်ဆေးဖို့နဲ့ error တွေရှိတဲ့ဖိုင်တွေကို အလိုအလျောက် ပြန်ဘာသာပြန်ဖို့ ဒီနည်းကိုသုံးခဲ့ပါတယ်။

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

ဒီ option က ဘာသာပြန် error တွေကို စစ်ဆေးပေးပါတယ်။ လက်ရှိမှာ မူလဖိုင်နဲ့ ဘာသာပြန်ဖိုင်ကြားမှာ line break ကွာခြားမှု ၆ ခုထက်ပိုရင် error ဖြစ်တယ်လို့ flag လုပ်ပါတယ်။ အနာဂတ်မှာ criterion ကို ပိုပြောင်းလဲနိုင်အောင် စီစဉ်ထားပါတယ်။

ဥပမာအားဖြင့်, ဒီနည်းက ဘာသာပြန်ဖိုင်မှာ chunk ပျောက်တာ၊ translation corrupted ဖြစ်တာတွေကို ရှာဖွေနိုင်ပြီး အလိုအလျောက် ပြန်ဘာသာပြန်ပေးပါလိမ့်မယ်။

သို့သော်, မိမိသိပြီးသား error ဖြစ်တဲ့ဖိုင်တွေရှိရင် ကိုယ်တိုင်ဖျက်ပြီး `-a` option နဲ့ ပြန်ဘာသာပြန်တာပိုအဆင်ပြေပါတယ်။

### ၈။ Debug Mode

Troubleshooting အတွက် အသေးစိတ် log တွေလိုချင်ရင် `-d` option ကိုသုံးပါ။

```bash
translate -l "ko" -d
```

ဒီ command က ဘာသာပြန်လုပ်စဉ်မှာ debug mode နဲ့ run လုပ်ပေးပြီး, ဘာသာပြန်လုပ်စဉ်မှာ ဖြစ်ပေါ်နိုင်တဲ့ ပြဿနာတွေကို ရှာဖွေရန် log အချက်အလက်များ ပိုမိုပေးပါလိမ့်မယ်။

#### Phi-3 CookBook မှာ ဥပမာ

**Phi-3 CookBook** မှာ markdown ဖိုင်ထဲမှာ link များများပါဝင်တဲ့ translation တွေမှာ format error (translation ပျက်၊ line break ပျက်) ဖြစ်တာတွေ့ခဲ့ပါတယ်။ ဒီပြဿနာကို diagnosis လုပ်ဖို့ `-d` option ကိုသုံးပြီး ဘာသာပြန်လုပ်စဉ်ကို ကြည့်ခဲ့ပါတယ်။

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### ၉။ ဘာသာစုံအားလုံးသို့ ဘာသာပြန်ခြင်း

Project ကို support လုပ်ထားတဲ့ ဘာသာစုံအားလုံးသို့ ဘာသာပြန်ချင်ရင် all keyword ကိုသုံးပါ။

```bash
translate -l "all"
```

ဒီ command က project ကို support လုပ်ထားတဲ့ ဘာသာစုံအားလုံးသို့ ဘာသာပြန်ပေးပါလိမ့်မယ်။ Project size ပေါ်မူတည်ပြီး ဘာသာပြန်လုပ်စဉ်မှာ အချိန်ကြာနိုင်ပါတယ်။

#### Manually ဖိုင်ဖျက်ခြင်း (Optional)

Source ဖိုင် update လုပ်တဲ့အခါ ဘာသာပြန်ဖိုင်တွေကို အလိုအလျောက် detect လုပ်ပြီး cleanup လုပ်ပေးပါတယ်။

သို့သော်, တစ်ခါတစ်လေ translation ကို ကိုယ်တိုင် update လုပ်ချင်ရင် (ဥပမာ ဖိုင်တစ်ခုကို ပြန်လုပ်ချင်တာ၊ system behavior ကို override လုပ်ချင်တာ) အောက်ပါ command တွေသုံးပြီး ဘာသာစုံ folder တွေထဲက ဖိုင်အားလုံးကို ဖျက်နိုင်ပါတယ်။

#### Windows မှာ

၁။ **Command Prompt သုံးခြင်း**:
   - Command Prompt ကိုဖွင့်ပါ။
   - `cd` command နဲ့ ဖိုင်တွေရှိတဲ့ folder ကိုသွားပါ။
   - အောက်ပါ command ကိုသုံးပါ:
>      ```
>      del /s *filename*
>      ```
>      `filename` ကို ဖျက်ချင်တဲ့ ဖိုင်နာမည်အစိတ်အပိုင်းနဲ့ အစားထိုးပါ။ `/s` option က subdirectory တွေထဲကိုပါ ရှာပေးပါတယ်။

၂။ **PowerShell သုံးခြင်း**:
   - PowerShell ကိုဖွင့်ပါ။
   - အောက်ပါ command ကို run ပါ:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"` ကို folder path နဲ့ `filename` ကို ဖိုင်နာမည်နဲ့ အစားထိုးပါ။

#### macOS/Linux မှာ

၁။ **Terminal သုံးခြင်း**:
   - Terminal ကိုဖွင့်ပါ။
   - `cd` နဲ့ directory ကိုသွားပါ။
   - `find` command ကိုသုံးပါ:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename` ကို ဖိုင်နာမည်နဲ့ အစားထိုးပါ။

ဖိုင်ဖျက်မယ်ဆိုရင် မလိုလားအပ်တဲ့ data ပျောက်ဆုံးမှုမဖြစ်အောင် အရင်စစ်ကြည့်ပါ။

ဖျက်လိုတဲ့ ဖိုင်တွေဖျက်ပြီးပြီဆိုရင် `translate -l` command ကို ပြန် run လုပ်ပြီး နောက်ဆုံး file changes တွေ update လုပ်နိုင်ပါတယ်။

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းသည် မူလဘာသာစကားဖြင့် အာဏာပိုင်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။