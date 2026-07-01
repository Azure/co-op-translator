# Подржани језици

Co-op Translator подржава следеће кодове језика за текст, бележнице и излазе превода слика.

If you want to add a new language, update the language and font mappings under `src/co_op_translator/fonts/` and test the language before opening a pull request.

| Language Code | Назив језика | Font | Подршка за RTL | Познати проблеми |
| --- | --- | --- | --- | --- |
| en | Енглески | NotoSans-Medium.ttf | Не | Не |
| fr | Француски | NotoSans-Medium.ttf | Не | Не |
| es | Шпански | NotoSans-Medium.ttf | Не | Не |
| de | Немачки | NotoSans-Medium.ttf | Не | Не |
| ru | Руски | NotoSans-Medium.ttf | Не | Не |
| ar | Арапски | NotoSansArabic-Medium.ttf | Да | Не |
| fa | Персијски (фарси) | NotoSansArabic-Medium.ttf | Да | Не |
| ur | Урду | NotoSansArabic-Medium.ttf | Да | Не |
| zh-CN | Кинески (поједностављени) | NotoSansCJK-Medium.ttc | Не | Не |
| zh-MO | Кинески (традиционални, Макао) | NotoSansCJK-Medium.ttc | Не | Не |
| zh-HK | Кинески (традиционални, Хонг Конг) | NotoSansCJK-Medium.ttc | Не | Не |
| zh-TW | Кинески (традиционални, Тајван) | NotoSansCJK-Medium.ttc | Не | Не |
| ja | Јапански | NotoSansCJK-Medium.ttc | Не | Не |
| ko | Корејски | NotoSansCJK-Medium.ttc | Не | Не |
| hi | Хинди | NotoSansDevanagari-Medium.ttf | Не | Не |
| bn | Бенгалски | NotoSansBengali-Medium.ttf | Не | Не |
| mr | Марати | NotoSansDevanagari-Medium.ttf | Не | Не |
| ne | Непалски | NotoSansDevanagari-Medium.ttf | Не | Не |
| pa | Пенџабски (Гурмукхи) | NotoSansGurmukhi-Medium.ttf | Не | Не |
| pt-PT | Португалски (Португал) | NotoSans-Medium.ttf | Не | Не |
| pt-BR | Португалски (Бразил) | NotoSans-Medium.ttf | Не | Не |
| it | Италијански | NotoSans-Medium.ttf | Не | Не |
| lt | Литвански | NotoSans-Medium.ttf | Не | Не |
| pl | Пољски | NotoSans-Medium.ttf | Не | Не |
| tr | Турски | NotoSans-Medium.ttf | Не | Не |
| el | Грчки | NotoSans-Medium.ttf | Не | Не |
| th | Тајски | NotoSansThai-Medium.ttf | Не | Не |
| sv | Шведски | NotoSans-Medium.ttf | Не | Не |
| da | Дански | NotoSans-Medium.ttf | Не | Не |
| no | Норвешки | NotoSans-Medium.ttf | Не | Не |
| fi | Фински | NotoSans-Medium.ttf | Не | Не |
| nl | Холандски | NotoSans-Medium.ttf | Не | Не |
| he | Хебрејски | NotoSansHebrew-Medium.ttf | Да | Не |
| vi | Вијетнамски | NotoSans-Medium.ttf | Не | Не |
| id | Индонежански | NotoSans-Medium.ttf | Не | Не |
| ms | Малајски | NotoSans-Medium.ttf | Не | Не |
| tl | Тагалог (Филипински) | NotoSans-Medium.ttf | Не | Не |
| sw | Свахили | NotoSans-Medium.ttf | Не | Не |
| hu | Мађарски | NotoSans-Medium.ttf | Не | Не |
| cs | Чешки | NotoSans-Medium.ttf | Не | Не |
| sk | Словачки | NotoSans-Medium.ttf | Не | Не |
| ro | Румунски | NotoSans-Medium.ttf | Не | Не |
| bg | Бугарски | NotoSans-Medium.ttf | Не | Не |
| sr | Српски (ћирилица) | NotoSans-Medium.ttf | Не | Не |
| hr | Хрватски | NotoSans-Medium.ttf | Не | Не |
| sl | Словеначки | NotoSans-Medium.ttf | Не | Не |
| uk | Украјински | NotoSans-Medium.ttf | Не | Не |
| my | Бирмански (Мјанмар) | NotoSansMyanmar-Medium.ttf | Не | Не |
| ta | Тамилски | NotoSansTamil-Medium.ttf | Не | Не |
| et | Естонски | NotoSans-Medium.ttf | Не | Не |
| pcm | Нигеријски пидгин | NotoSans-Medium.ttf | Не | Не |
| te | Телугу | NotoSans-Medium.ttf | Не | Не |
| ml | Малајаламски | NotoSans-Medium.ttf | Не | Не |
| kn | Каннада | NotoSans-Medium.ttf | Не | Не |
| km | Кмерски | NotoSansKhmer-Medium.ttf | Не | Не |

## Додавање језика

To add support for a new language:

1. Додајте код језика и приказани назив у алатке за језике.
2. Додајте или мапирајте фонт у `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Тестирајте излаз превода Markdown-а и слика.
4. Отворите pull request са мапирањем и напоменама о валидацији.