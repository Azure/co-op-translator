# সমর্থিত ভাষাসমূহ

Co-op Translator নিম্নলিখিত ভাষা কোডগুলোকে টেক্সট, নোটবুক, এবং চিত্র অনুবাদ আউটপুটগুলোর জন্য সমর্থন করে।

If you want to add a new language, update the language and font mappings under `src/co_op_translator/fonts/` and test the language before opening a pull request.

| Language Code | ভাষা নাম | Font | আরটিএল সমর্থন | পরিচিত সমস্যা |
| --- | --- | --- | --- | --- |
| en | ইংরেজি | NotoSans-Medium.ttf | না | না |
| fr | ফরাসি | NotoSans-Medium.ttf | না | না |
| es | স্প্যানিশ | NotoSans-Medium.ttf | না | না |
| de | জার্মান | NotoSans-Medium.ttf | না | না |
| ru | রাশিয়ান | NotoSans-Medium.ttf | না | না |
| ar | আরবি | NotoSansArabic-Medium.ttf | হ্যাঁ | না |
| fa | পার্সিয়ান (ফারসি) | NotoSansArabic-Medium.ttf | হ্যাঁ | না |
| ur | উর্দু | NotoSansArabic-Medium.ttf | হ্যাঁ | না |
| zh-CN | চীনা (সরলীকৃত) | NotoSansCJK-Medium.ttc | না | না |
| zh-MO | চীনা (ঐতিহ্যবাহী, ম্যাকাও) | NotoSansCJK-Medium.ttc | না | না |
| zh-HK | চীনা (ঐতিহ্যবাহী, হংকং) | NotoSansCJK-Medium.ttc | না | না |
| zh-TW | চীনা (ঐতিহ্যবাহী, তাইওয়ান) | NotoSansCJK-Medium.ttc | না | না |
| ja | জাপানি | NotoSansCJK-Medium.ttc | না | না |
| ko | কোরিয়ান | NotoSansCJK-Medium.ttc | না | না |
| hi | হিন্দি | NotoSansDevanagari-Medium.ttf | না | না |
| bn | বাংলা | NotoSansBengali-Medium.ttf | না | না |
| mr | মারাঠি | NotoSansDevanagari-Medium.ttf | না | না |
| ne | নেপালি | NotoSansDevanagari-Medium.ttf | না | না |
| pa | পাঞ্জাবি (গুরুমুখি) | NotoSansGurmukhi-Medium.ttf | না | না |
| pt-PT | পর্তুগিজ (পর্তুগাল) | NotoSans-Medium.ttf | না | না |
| pt-BR | পর্তুগিজ (ব্রাজিল) | NotoSans-Medium.ttf | না | না |
| it | ইতালিয়ান | NotoSans-Medium.ttf | না | না |
| lt | লিথুয়ানীয় | NotoSans-Medium.ttf | না | না |
| pl | পোলিশ | NotoSans-Medium.ttf | না | না |
| tr | তুর্কি | NotoSans-Medium.ttf | না | না |
| el | গ্রিক | NotoSans-Medium.ttf | না | না |
| th | থাই | NotoSansThai-Medium.ttf | না | না |
| sv | সুইডিশ | NotoSans-Medium.ttf | না | না |
| da | ডেনিশ | NotoSans-Medium.ttf | না | না |
| no | নরওয়েজিয়ান | NotoSans-Medium.ttf | না | না |
| fi | ফিনিশ | NotoSans-Medium.ttf | না | না |
| nl | ডাচ | NotoSans-Medium.ttf | না | না |
| he | হিব্রু | NotoSansHebrew-Medium.ttf | হ্যাঁ | না |
| vi | ভিয়েতনামী | NotoSans-Medium.ttf | না | না |
| id | ইন্দোনেশিয়ান | NotoSans-Medium.ttf | না | না |
| ms | মালয় | NotoSans-Medium.ttf | না | না |
| tl | তাগালগ (ফিলিপিনো) | NotoSans-Medium.ttf | না | না |
| sw | সোয়াহিলি | NotoSans-Medium.ttf | না | না |
| hu | হাঙ্গেরীয় | NotoSans-Medium.ttf | না | না |
| cs | চেক | NotoSans-Medium.ttf | না | না |
| sk | স্লোভাক | NotoSans-Medium.ttf | না | না |
| ro | রোমানিয়ান | NotoSans-Medium.ttf | না | না |
| bg | বুলগেরীয় | NotoSans-Medium.ttf | না | না |
| sr | সার্বিয়ান (সিরিলিক) | NotoSans-Medium.ttf | না | না |
| hr | ক্রোয়েশিয়ান | NotoSans-Medium.ttf | না | না |
| sl | স্লোভেনিয়ান | NotoSans-Medium.ttf | না | না |
| uk | ইউক্রেনীয় | NotoSans-Medium.ttf | না | না |
| my | বার্মিজ (মিয়ানমার) | NotoSansMyanmar-Medium.ttf | না | না |
| ta | তামিল | NotoSansTamil-Medium.ttf | না | না |
| et | এস্তোনীয় | NotoSans-Medium.ttf | না | না |
| pcm | নাইজেরিয়ান পিজিন | NotoSans-Medium.ttf | না | না |
| te | তেলুগু | NotoSans-Medium.ttf | না | না |
| ml | মালায়ালাম | NotoSans-Medium.ttf | না | না |
| kn | কন্নড় | NotoSans-Medium.ttf | না | না |
| km | খমের | NotoSansKhmer-Medium.ttf | না | না |

## একটি ভাষা যোগ করুন

To add support for a new language:

1. Add the language code and display name to the language utilities.
2. Add or map a font in `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Test Markdown and image translation output.
4. Open a pull request with the mapping and validation notes.