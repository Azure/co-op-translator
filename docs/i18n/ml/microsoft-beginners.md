# Microsoft ആരംഭക്കാർക്കുള്ള റിപോസിറ്ററികൾ

ഈ പേജ് Microsoft "For Beginners" റിപോസിറ്ററികൾ പരിപാലിക്കുന്നവർക്കാണ്, അവയിൽ പങ്കുവെക്കപ്പെട്ട "Other Courses" README വിഭാഗം ഉപയോഗിക്കുന്നവർക്കായുള്ളത്.

മിക്ക Co-op Translator ഉപയോക്താക്കൾക്കും ഈ പേജ് ആവശ്യമായിട്ടില്ല.

## Other Courses വിഭാഗം ഓട്ടോ-സിങ്ക് ചെയ്യുക

README-യിലെ "Other Courses" വിഭാഗത്തിന്റെ ചുറ്റുമാണ് ഈ മാർക്കറുകൾ ചേർക്കുക:

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator CLI-യിലൂടെ അല്ലെങ്കിൽ GitHub Actions ഉപയോഗിച്ച് ഓടുമ്പോഴെല്ലാം, മാർക്കറുകൾക്കിടയിലെ ഉള്ളടക്കം പാക്കേജ് ചെയ്ത ടെംപ്ലേറ്റോടെ മാറ്റി വെക്കപ്പെടുന്നു.

## പങ്കിട്ട ടെംപ്ലേറ്റ് അപ്‌ഡേറ്റ് ചെയ്യുക

ടെംപ്ലേറ്റിന്റെ സോഴ്‌സ് ഇവിടെയാണ്:

```text
src/co_op_translator/templates/other_courses.md
```

പങ്കിട്ട ഉള്ളടക്കം അപ്‌ഡേറ്റ് ചെയ്യാൻ:

1. ടെംപ്ലേറ്റ് തിരുത്തുക.
2. Co-op Translator-ലേക്ക് ഒരു pull request തുറക്കുക.
3. മാറ്റം റിലീസ് പൂർത്തിയായതിനു ശേഷം, ലക്ഷ്യ റിപോസിറ്ററിയിൽ Co-op Translator ഓടിക്കുക.

## സ്പാർസ് ചെക്കൗട്ട് ഉപദേശം

വിവിധ ഭാഷകളിലെ ധാരാളം തർജ്ജമ ചെയ്യപ്പെട്ട ഔട്ട്പുട്ടുകൾ ഉൾപ്പെടുന്നപ്പോൾ, വലിയ കോഴ്സ് റിപോസിറ്ററികൾ ക്ലോൺ ചെയ്യുന്നത് ചെലവേറിയതാകാം. നിങ്ങൾ ഈ ഉപദേശം ജനറേറ്റ് ചെയ്ത ഭാഷാ വിഭാഗങ്ങളിൽ ഉൾപ്പെടുത്താവുന്നതാണ്:

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