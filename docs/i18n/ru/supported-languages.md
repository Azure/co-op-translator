# Поддерживаемые языки

Co-op Translator поддерживает следующие коды языков для вывода перевода текста, ноутбуков и изображений.

Если вы хотите добавить новый язык, обновите соответствия языка и шрифтов в `src/co_op_translator/fonts/` и протестируйте язык перед открытием pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Английский | NotoSans-Medium.ttf | Нет | Нет |
| fr | Французский | NotoSans-Medium.ttf | Нет | Нет |
| es | Испанский | NotoSans-Medium.ttf | Нет | Нет |
| de | Немецкий | NotoSans-Medium.ttf | Нет | Нет |
| ru | Русский | NotoSans-Medium.ttf | Нет | Нет |
| ar | Арабский | NotoSansArabic-Medium.ttf | Да | Нет |
| fa | Персидский (фарси) | NotoSansArabic-Medium.ttf | Да | Нет |
| ur | Урду | NotoSansArabic-Medium.ttf | Да | Нет |
| zh-CN | Китайский (упрощенный) | NotoSansCJK-Medium.ttc | Нет | Нет |
| zh-MO | Китайский (традиционный, Макао) | NotoSansCJK-Medium.ttc | Нет | Нет |
| zh-HK | Китайский (традиционный, Гонконг) | NotoSansCJK-Medium.ttc | Нет | Нет |
| zh-TW | Китайский (традиционный, Тайвань) | NotoSansCJK-Medium.ttc | Нет | Нет |
| ja | Японский | NotoSansCJK-Medium.ttc | Нет | Нет |
| ko | Корейский | NotoSansCJK-Medium.ttc | Нет | Нет |
| hi | Хинди | NotoSansDevanagari-Medium.ttf | Нет | Нет |
| bn | Бенгальский | NotoSansBengali-Medium.ttf | Нет | Нет |
| mr | Маратхи | NotoSansDevanagari-Medium.ttf | Нет | Нет |
| ne | Непальский | NotoSansDevanagari-Medium.ttf | Нет | Нет |
| pa | Пенджабский (гурмухи) | NotoSansGurmukhi-Medium.ttf | Нет | Нет |
| pt-PT | Португальский (Португалия) | NotoSans-Medium.ttf | Нет | Нет |
| pt-BR | Португальский (Бразилия) | NotoSans-Medium.ttf | Нет | Нет |
| it | Итальянский | NotoSans-Medium.ttf | Нет | Нет |
| lt | Литовский | NotoSans-Medium.ttf | Нет | Нет |
| pl | Польский | NotoSans-Medium.ttf | Нет | Нет |
| tr | Турецкий | NotoSans-Medium.ttf | Нет | Нет |
| el | Греческий | NotoSans-Medium.ttf | Нет | Нет |
| th | Тайский | NotoSansThai-Medium.ttf | Нет | Нет |
| sv | Шведский | NotoSans-Medium.ttf | Нет | Нет |
| da | Датский | NotoSans-Medium.ttf | Нет | Нет |
| no | Норвежский | NotoSans-Medium.ttf | Нет | Нет |
| fi | Финский | NotoSans-Medium.ttf | Нет | Нет |
| nl | Нидерландский | NotoSans-Medium.ttf | Нет | Нет |
| he | Иврит | NotoSansHebrew-Medium.ttf | Да | Нет |
| vi | Вьетнамский | NotoSans-Medium.ttf | Нет | Нет |
| id | Индонезийский | NotoSans-Medium.ttf | Нет | Нет |
| ms | Малайский | NotoSans-Medium.ttf | Нет | Нет |
| tl | Тагалог (филиппинский) | NotoSans-Medium.ttf | Нет | Нет |
| sw | Суахили | NotoSans-Medium.ttf | Нет | Нет |
| hu | Венгерский | NotoSans-Medium.ttf | Нет | Нет |
| cs | Чешский | NotoSans-Medium.ttf | Нет | Нет |
| sk | Словацкий | NotoSans-Medium.ttf | Нет | Нет |
| ro | Румынский | NotoSans-Medium.ttf | Нет | Нет |
| bg | Болгарский | NotoSans-Medium.ttf | Нет | Нет |
| sr | Сербский (кириллица) | NotoSans-Medium.ttf | Нет | Нет |
| hr | Хорватский | NotoSans-Medium.ttf | Нет | Нет |
| sl | Словенский | NotoSans-Medium.ttf | Нет | Нет |
| uk | Украинский | NotoSans-Medium.ttf | Нет | Нет |
| my | Бирманский (Мьянма) | NotoSansMyanmar-Medium.ttf | Нет | Нет |
| ta | Тамильский | NotoSansTamil-Medium.ttf | Нет | Нет |
| et | Эстонский | NotoSans-Medium.ttf | Нет | Нет |
| pcm | Нигерийский пиджин | NotoSans-Medium.ttf | Нет | Нет |
| te | Телугу | NotoSans-Medium.ttf | Нет | Нет |
| ml | Малаялам | NotoSans-Medium.ttf | Нет | Нет |
| kn | Каннада | NotoSans-Medium.ttf | Нет | Нет |
| km | Кхмерский | NotoSansKhmer-Medium.ttf | Нет | Нет |

## Добавить язык

Чтобы добавить поддержку нового языка:

1. Добавьте код языка и отображаемое имя в утилиты языков.
2. Добавьте или сопоставьте шрифт в `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Проверьте вывод перевода Markdown и изображений.
4. Откройте pull request с сопоставлением и заметками о валидации.