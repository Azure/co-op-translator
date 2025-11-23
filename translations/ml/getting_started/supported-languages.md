<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a7e2b0abab622ba4fea4bdce6ddaef89",
  "translation_date": "2025-11-23T02:21:01+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "ml"
}
-->
# പിന്തുണയുള്ള ഭാഷകൾ

**Co-op Translator** നിലവിൽ പിന്തുണയ്ക്കുന്ന ഭാഷകളുടെ പട്ടിക താഴെ നൽകിയിരിക്കുന്നു. ഇതിൽ ഭാഷാ കോഡുകൾ, ഭാഷാ പേരുകൾ, ഓരോ ഭാഷയുമായി ബന്ധപ്പെട്ട പ്രശ്നങ്ങൾ എന്നിവ ഉൾപ്പെടുന്നു. പുതിയ ഒരു ഭാഷയ്ക്ക് പിന്തുണ നൽകാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, `src/co_op_translator/fonts/` എന്ന സ്ഥലത്തുള്ള `font_language_mappings.yml` ഫയലിൽ അനുയോജ്യമായ ഫോണ്ട്, ഭാഷാ കോഡ്, ഭാഷാ പേര് എന്നിവ ചേർത്ത ശേഷം ടെസ്റ്റിംഗ് പൂർത്തിയാക്കിയ ശേഷം ഒരു പുൾ റിക്വസ്റ്റ് സമർപ്പിക്കുക.

| ഭാഷാ കോഡ് | ഭാഷയുടെ പേര്          | ഫോണ്ട്                              | RTL പിന്തുണ | അറിയാവുന്ന പ്രശ്നങ്ങൾ |
|------------|-----------------------|------------------------------------|-------------|-----------------------|
| en         | ഇംഗ്ലീഷ്               | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| fr         | ഫ്രഞ്ച്                | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| es         | സ്പാനിഷ്               | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| de         | ജർമ്മൻ                | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| ru         | റഷ്യൻ                 | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| ar         | അറബിക്                | NotoSansArabic-Medium.ttf         | ഉണ്ട്        | ഇല്ല                  |
| fa         | പർഷ്യൻ (ഫാർസി)      | NotoSansArabic-Medium.ttf         | ഉണ്ട്        | ഇല്ല                  |
| ur         | ഉർദു                  | NotoSansArabic-Medium.ttf         | ഉണ്ട്        | ഇല്ല                  |
| zh         | ചൈനീസ് (ലളിതമാക്കിയ) | NotoSansCJK-Medium.ttc            | ഇല്ല         | ഇല്ല                  |
| mo         | ചൈനീസ് (പരമ്പരാഗതം, മക്കാവു) | NotoSansCJK-Medium.ttc    | ഇല്ല         | ഇല്ല                  |
| hk         | ചൈനീസ് (പരമ്പരാഗതം, ഹോങ്കോങ്) | NotoSansCJK-Medium.ttc| ഇല്ല         | ഇല്ല                  |
| tw         | ചൈനീസ് (പരമ്പരാഗതം, തായ്‌വാൻ) | NotoSansCJK-Medium.ttc   | ഇല്ല         | ഇല്ല                  |
| ja         | ജാപ്പനീസ്              | NotoSansCJK-Medium.ttc            | ഇല്ല         | ഇല്ല                  |
| ko         | കൊറിയൻ               | NotoSansCJK-Medium.ttc            | ഇല്ല         | ഇല്ല                  |
| hi         | ഹിന്ദി                 | NotoSansDevanagari-Medium.ttf     | ഇല്ല         | ഇല്ല                  |
| bn         | ബംഗാളി                | NotoSansBengali-Medium.ttf        | ഇല്ല         | ഇല്ല                  |
| mr         | മറാത്തി                | NotoSansDevanagari-Medium.ttf     | ഇല്ല         | ഇല്ല                  |
| ne         | നേപ്പാളി               | NotoSansDevanagari-Medium.ttf     | ഇല്ല         | ഇല്ല                  |
| pa         | പഞ്ചാബി (ഗുര്മുഖി)    | NotoSansGurmukhi-Medium.ttf       | ഇല്ല         | ഇല്ല                  |
| pt         | പോർച്ചുഗീസ് (പോർച്ചുഗൽ) | NotoSans-Medium.ttf           | ഇല്ല         | ഇല്ല                  |
| br         | പോർച്ചുഗീസ് (ബ്രസീൽ) | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| it         | ഇറ്റാലിയൻ             | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| lt         | ലിത്വാനിയൻ            | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| pl         | പോളിഷ്               | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| tr         | തുർക്കിഷ്             | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| el         | ഗ്രീക്ക്                | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| th         | തായ്                  | NotoSansThai-Medium.ttf           | ഇല്ല         | ഇല്ല                  |
| sv         | സ്വീഡിഷ്              | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| da         | ഡാനിഷ്                | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| no         | നോർവീജിയൻ            | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| fi         | ഫിന്നിഷ്               | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| nl         | ഡച്ച്                  | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| he         | ഹീബ്രു                | NotoSansHebrew-Medium.ttf         | ഉണ്ട്        | ഇല്ല                  |
| vi         | വിയറ്റ്നാമീസ്           | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| id         | ഇൻഡോനേഷ്യൻ          | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| ms         | മലായ്                  | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| tl         | ടാഗലോഗ് (ഫിലിപ്പീൻ)   | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| sw         | സ്വാഹിലി               | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| hu         | ഹംഗേറിയൻ            | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| cs         | ചെക്ക്                 | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| sk         | സ്ലോവാക്               | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| ro         | റൊമാനിയൻ             | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| bg         | ബൾഗേറിയൻ            | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| sr         | സെർബിയൻ (സിറിലിക്)   | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| hr         | ക്രൊയേഷ്യൻ           | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| sl         | സ്ലോവേനിയൻ           | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| uk         | യുക്രെയ്നിയൻ          | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| my         | ബർമീസ് (മ്യാൻമാർ)    | NotoSansMyanmar-Medium.ttf        | ഇല്ല         | ഇല്ല                  |
| ta         | തമിഴ്                 | NotoSansTamil-Medium.ttf          | ഇല്ല         | ഇല്ല                  |
| et         | എസ്റ്റോണിയൻ            | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| pcm        | നൈജീരിയൻ പിഡ്ജിൻ     | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| te         | തെലുങ്ക്              | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |
| ml         | മലയാളം                | NotoSans-Medium.ttf               | ഇല്ല         | ഇല്ല                  |

## പുതിയ ഭാഷ ചേർക്കൽ

പുതിയ ഭാഷ ചേർക്കാൻ താൽപ്പര്യമുണ്ടോ? ദയവായി സംഭാവനാ മാർഗനിർദ്ദേശങ്ങൾ പിന്തുടരുക:

- സംഭാവന കാണുക: [പുതിയ ഭാഷ സംഭാവന ചെയ്യുക](../CONTRIBUTING.md#contribute-a-new-language)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:  
ഈ പ്രമാണം AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. പ്രമാണത്തിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ പതിപ്പ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->