# समर्थित भाषा

Co-op Translator खालील भाषा कोड्स मजकूर, नोटबुक, आणि प्रतिमा भाषांतर आउटपुटसाठी समर्थित करतो.

जर तुम्हाला नवीन भाषा जोडायची असेल, तर भाषा आणि फॉन्ट मॅपिंग `src/co_op_translator/fonts/` अंतर्गत अद्यतन करा आणि पुल रिक्वेस्ट उघडण्यापूर्वी भाषा चाचणी करा.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | इंग्रजी | NotoSans-Medium.ttf | नाही | नाही |
| fr | फ्रेंच | NotoSans-Medium.ttf | नाही | नाही |
| es | स्पॅनिश | NotoSans-Medium.ttf | नाही | नाही |
| de | जर्मन | NotoSans-Medium.ttf | नाही | नाही |
| ru | रशियन | NotoSans-Medium.ttf | नाही | नाही |
| ar | अरबी | NotoSansArabic-Medium.ttf | होय | नाही |
| fa | फारसी (फारसी) | NotoSansArabic-Medium.ttf | होय | नाही |
| ur | उर्दू | NotoSansArabic-Medium.ttf | होय | नाही |
| zh-CN | चीनी (सरलीकृत) | NotoSansCJK-Medium.ttc | नाही | नाही |
| zh-MO | चीनी (पारंपरिक, मकाऊ) | NotoSansCJK-Medium.ttc | नाही | नाही |
| zh-HK | चीनी (पारंपरिक, हाँगकाँग) | NotoSansCJK-Medium.ttc | नाही | नाही |
| zh-TW | चीनी (पारंपरिक, तैवान) | NotoSansCJK-Medium.ttc | नाही | नाही |
| ja | जपानी | NotoSansCJK-Medium.ttc | नाही | नाही |
| ko | कोरियन | NotoSansCJK-Medium.ttc | नाही | नाही |
| hi | हिंदी | NotoSansDevanagari-Medium.ttf | नाही | नाही |
| bn | बंगाली | NotoSansBengali-Medium.ttf | नाही | नाही |
| mr | मराठी | NotoSansDevanagari-Medium.ttf | नाही | नाही |
| ne | नेपाळी | NotoSansDevanagari-Medium.ttf | नाही | नाही |
| pa | पंजाबी (गुरमुखी) | NotoSansGurmukhi-Medium.ttf | नाही | नाही |
| pt-PT | पोर्तुगीज (पोर्तुगाल) | NotoSans-Medium.ttf | नाही | नाही |
| pt-BR | पोर्तुगीज (ब्राझील) | NotoSans-Medium.ttf | नाही | नाही |
| it | इटालियन | NotoSans-Medium.ttf | नाही | नाही |
| lt | लिथुआनियन | NotoSans-Medium.ttf | नाही | नाही |
| pl | पोलिश | NotoSans-Medium.ttf | नाही | नाही |
| tr | तुर्की | NotoSans-Medium.ttf | नाही | नाही |
| el | ग्रीक | NotoSans-Medium.ttf | नाही | नाही |
| th | थाई | NotoSansThai-Medium.ttf | नाही | नाही |
| sv | स्वीडिश | NotoSans-Medium.ttf | नाही | नाही |
| da | डॅनिश | NotoSans-Medium.ttf | नाही | नाही |
| no | नॉर्वेजियन | NotoSans-Medium.ttf | नाही | नाही |
| fi | फिनिश | NotoSans-Medium.ttf | नाही | नाही |
| nl | डच | NotoSans-Medium.ttf | नाही | नाही |
| he | हिब्रू | NotoSansHebrew-Medium.ttf | होय | नाही |
| vi | व्हिएतनामी | NotoSans-Medium.ttf | नाही | नाही |
| id | इंडोनेशियन | NotoSans-Medium.ttf | नाही | नाही |
| ms | मलय | NotoSans-Medium.ttf | नाही | नाही |
| tl | टागालोग (फिलिपिनो) | NotoSans-Medium.ttf | नाही | नाही |
| sw | स्वाहिली | NotoSans-Medium.ttf | नाही | नाही |
| hu | हंगेरियन | NotoSans-Medium.ttf | नाही | नाही |
| cs | झेक | NotoSans-Medium.ttf | नाही | नाही |
| sk | स्लोवाक | NotoSans-Medium.ttf | नाही | नाही |
| ro | रोमानियन | NotoSans-Medium.ttf | नाही | नाही |
| bg | बुल्गेरियन | NotoSans-Medium.ttf | नाही | नाही |
| sr | सर्बियन (सिरिलिक) | NotoSans-Medium.ttf | नाही | नाही |
| hr | क्रोएशियन | NotoSans-Medium.ttf | नाही | नाही |
| sl | स्लोव्हेनियन | NotoSans-Medium.ttf | नाही | नाही |
| uk | युक्रेनियन | NotoSans-Medium.ttf | नाही | नाही |
| my | बर्मीस (म्यानमार) | NotoSansMyanmar-Medium.ttf | नाही | नाही |
| ta | तमिळ | NotoSansTamil-Medium.ttf | नाही | नाही |
| et | एस्टोनियन | NotoSans-Medium.ttf | नाही | नाही |
| pcm | नायजीरियन पिजिन | NotoSans-Medium.ttf | नाही | नाही |
| te | तेलुगू | NotoSans-Medium.ttf | नाही | नाही |
| ml | मलयाळम | NotoSans-Medium.ttf | नाही | नाही |
| kn | कन्नड | NotoSans-Medium.ttf | नाही | नाही |
| km | खमेर | NotoSansKhmer-Medium.ttf | नाही | नाही |

## भाषा जोडा

To add support for a new language:

1. भाषा कोड आणि प्रदर्शन नाव language utilities मध्ये जोडा.
2. `src/co_op_translator/fonts/font_language_mappings.yml` मध्ये फॉन्ट जोडा किंवा मॅप करा.
3. Markdown आणि प्रतिमा भाषांतर आउटपुटची चाचणी करा.
4. मॅपिंग आणि पडताळणी नोट्ससह एक पुल रिक्वेस्ट उघडा.