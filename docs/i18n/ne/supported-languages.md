# समर्थित भाषाहरू

Co-op Translator ले तलका भाषा कोडहरूलाई पाठ, नोटबुक, र छवि अनुवाद आउटपुटहरूको लागि समर्थन गर्छ।

यदि तपाईं नयाँ भाषा थप्न चाहनुहुन्छ भने, `src/co_op_translator/fonts/` अन्तर्गत भाषा र फन्ट म्यापिङहरू अद्यावधिक गर्नुहोस् र पुल अनुरोध खोल्नु अघि भाषाको परीक्षण गर्नुहोस्।

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | अंग्रेजी | NotoSans-Medium.ttf | No | No |
| fr | फ्रान्सेली | NotoSans-Medium.ttf | No | No |
| es | स्पेनिश | NotoSans-Medium.ttf | No | No |
| de | जर्मन | NotoSans-Medium.ttf | No | No |
| ru | रूसी | NotoSans-Medium.ttf | No | No |
| ar | अरबी | NotoSansArabic-Medium.ttf | Yes | No |
| fa | पर्शियन (फारसी) | NotoSansArabic-Medium.ttf | Yes | No |
| ur | उर्दू | NotoSansArabic-Medium.ttf | Yes | No |
| zh-CN | चिनियाँ (सरलीकृत) | NotoSansCJK-Medium.ttc | No | No |
| zh-MO | चिनियाँ (परम्परागत, मकाउ) | NotoSansCJK-Medium.ttc | No | No |
| zh-HK | चिनियाँ (परम्परागत, हङकङ) | NotoSansCJK-Medium.ttc | No | No |
| zh-TW | चिनियाँ (परम्परागत, ताइवान) | NotoSansCJK-Medium.ttc | No | No |
| ja | जापानी | NotoSansCJK-Medium.ttc | No | No |
| ko | कोरियन | NotoSansCJK-Medium.ttc | No | No |
| hi | हिन्दी | NotoSansDevanagari-Medium.ttf | No | No |
| bn | बंगाली | NotoSansBengali-Medium.ttf | No | No |
| mr | मराठी | NotoSansDevanagari-Medium.ttf | No | No |
| ne | नेपाली | NotoSansDevanagari-Medium.ttf | No | No |
| pa | पञ्जाबी (गुरमुखी) | NotoSansGurmukhi-Medium.ttf | No | No |
| pt-PT | पोर्तुगाली (पोर्चुगल) | NotoSans-Medium.ttf | No | No |
| pt-BR | पोर्तुगाली (ब्राजिल) | NotoSans-Medium.ttf | No | No |
| it | इटालियन | NotoSans-Medium.ttf | No | No |
| lt | लिथुआनियाली | NotoSans-Medium.ttf | No | No |
| pl | पोलिश | NotoSans-Medium.ttf | No | No |
| tr | टर्की | NotoSans-Medium.ttf | No | No |
| el | यूनानी | NotoSans-Medium.ttf | No | No |
| th | थाई | NotoSansThai-Medium.ttf | No | No |
| sv | स्वीडिश | NotoSans-Medium.ttf | No | No |
| da | डेनिश | NotoSans-Medium.ttf | No | No |
| no | नर्वेजियन | NotoSans-Medium.ttf | No | No |
| fi | फिनिश | NotoSans-Medium.ttf | No | No |
| nl | डच | NotoSans-Medium.ttf | No | No |
| he | हिब्रू | NotoSansHebrew-Medium.ttf | Yes | No |
| vi | भियतनामी | NotoSans-Medium.ttf | No | No |
| id | इन्डोनेसियाली | NotoSans-Medium.ttf | No | No |
| ms | मलय | NotoSans-Medium.ttf | No | No |
| tl | टागालोग (फिलिपिनो) | NotoSans-Medium.ttf | No | No |
| sw | स्वाहिली | NotoSans-Medium.ttf | No | No |
| hu | हंगेरियन | NotoSans-Medium.ttf | No | No |
| cs | चेक | NotoSans-Medium.ttf | No | No |
| sk | स्लोवाक | NotoSans-Medium.ttf | No | No |
| ro | रोमानियन | NotoSans-Medium.ttf | No | No |
| bg | बुल्गेरियाई | NotoSans-Medium.ttf | No | No |
| sr | सर्बियाली (सिरिलिक) | NotoSans-Medium.ttf | No | No |
| hr | क्रोएशियाली | NotoSans-Medium.ttf | No | No |
| sl | स्लोभेनियाली | NotoSans-Medium.ttf | No | No |
| uk | यूक्रेनी | NotoSans-Medium.ttf | No | No |
| my | बर्मी (म्यानमार) | NotoSansMyanmar-Medium.ttf | No | No |
| ta | तमिल | NotoSansTamil-Medium.ttf | No | No |
| et | एस्टोनियाली | NotoSans-Medium.ttf | No | No |
| pcm | नाइजेरियन पिड्जिन | NotoSans-Medium.ttf | No | No |
| te | तेलुगु | NotoSans-Medium.ttf | No | No |
| ml | मलयालम | NotoSans-Medium.ttf | No | No |
| kn | कन्नड | NotoSans-Medium.ttf | No | No |
| km | खमेर | NotoSansKhmer-Medium.ttf | No | No |
| mni | मणिपुरी (मेइतेई मयेक) | NotoSansMeeteiMayek-Medium.ttf | No | No |

## भाषा थप्नुहोस्

नयाँ भाषाको समर्थन थप्न:

1. भाषा कोड र प्रदर्शन नामलाई भाषा उपयोगिताहरूमा थप्नुहोस्।
2. `src/co_op_translator/fonts/font_language_mappings.yml` मा फन्ट थप्नुहोस् वा म्याप गर्नुहोस्।
3. Markdown र छवि अनुवाद आउटपुट परीक्षण गर्नुहोस्।
4. म्यापिङ र मान्यकरण नोटहरूसँग पुल अनुरोध खोल्नुहोस्।