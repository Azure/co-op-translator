<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-23T02:22:33+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "ml"
}
-->
# "മറ്റു കോഴ്സുകൾ" വിഭാഗം (Microsoft Beginners repos) അപ്ഡേറ്റ് ചെയ്യുക

ഈ ഗൈഡ് "മറ്റു കോഴ്സുകൾ" വിഭാഗം Co‑op Translator ഉപയോഗിച്ച് സ്വയം‑സമന്വയിപ്പിക്കാൻ എങ്ങനെ സജ്ജമാക്കാമെന്ന്, കൂടാതെ എല്ലാ repos-കർക്കും ഗ്ലോബൽ ടെംപ്ലേറ്റ് എങ്ങനെ അപ്ഡേറ്റ് ചെയ്യാമെന്ന് വിശദീകരിക്കുന്നു.

- ബാധകമായത്: Microsoft Beginners repositories മാത്രം
- പ്രവർത്തിക്കുന്നതും: Co‑op Translator CLI, GitHub Actions
- ടെംപ്ലേറ്റ് ഉറവിടം: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## ദ്രുത തുടക്കം: നിങ്ങളുടെ repo-യിൽ auto‑sync സജ്ജമാക്കുക

നിങ്ങളുടെ README-യിലെ "മറ്റു കോഴ്സുകൾ" വിഭാഗത്തിന് ചുറ്റും താഴെ കൊടുത്തിരിക്കുന്ന മാർക്കറുകൾ ചേർക്കുക. Co‑op Translator ഓരോ റൺ സമയത്തും ഈ മാർക്കറുകൾക്കിടയിലുള്ള എല്ലാം മാറ്റിസ്ഥാപിക്കും.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op Translator CLI (ഉദാ., `translate -l "<language codes>"`) അല്ലെങ്കിൽ GitHub Actions വഴി പ്രവർത്തിക്കുന്ന ഓരോ തവണയും, ഈ മാർക്കറുകൾ ചുറ്റുമുള്ള "മറ്റു കോഴ്സുകൾ" വിഭാഗം സ്വയം അപ്ഡേറ്റ് ചെയ്യും.

> [!NOTE]
> നിങ്ങൾക്ക് നിലവിലുള്ള ഒരു ലിസ്റ്റ് ഉണ്ടെങ്കിൽ, അതിനെ ഈ മാർക്കറുകൾ ഉപയോഗിച്ച് ചുറ്റുക. അടുത്ത റൺ സമയത്ത് ഇത് ഏറ്റവും പുതിയ സ്റ്റാൻഡേർഡൈസ്ഡ് ഉള്ളടക്കത്തോടെ മാറ്റിസ്ഥാപിക്കും.

---

## ഗ്ലോബൽ ഉള്ളടക്കം എങ്ങനെ മാറ്റാം

Beginners repos-കളിൽ കാണുന്ന സ്റ്റാൻഡേർഡൈസ്ഡ് ഉള്ളടക്കം നിങ്ങൾക്ക് അപ്ഡേറ്റ് ചെയ്യണമെങ്കിൽ:

1. ടെംപ്ലേറ്റ് എഡിറ്റ് ചെയ്യുക: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. നിങ്ങളുടെ മാറ്റങ്ങളോടെ Co-op Translator repo-യിലേക്ക് ഒരു pull request തുറക്കുക
3. PR മർജ് ചെയ്ത ശേഷം, Co‑op Translator പതിപ്പ് അപ്ഡേറ്റ് ചെയ്യും
4. ലക്ഷ്യ repo-യിൽ Co‑op Translator (CLI അല്ലെങ്കിൽ GitHub Action) അടുത്ത തവണ പ്രവർത്തിക്കുന്നപ്പോൾ, അപ്ഡേറ്റുചെയ്ത വിഭാഗം സ്വയം സമന്വയിപ്പിക്കും

ഇത് എല്ലാ Beginners repositories-ൽ "മറ്റു കോഴ്സുകൾ" ഉള്ളടക്കത്തിന് ഒരു ഏകീകൃത ഉറവിടം ഉറപ്പാക്കുന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് വിശ്വസനീയമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->