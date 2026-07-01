# Поддържани езици

Co-op Translator поддържа следните кодове на езици за текстови, notebook и изображенчески преводни резултати.

Ако искате да добавите нов език, актуализирайте езиковите и шрифтовите съпоставяния под `src/co_op_translator/fonts/` и тествайте езика преди да отворите pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Английски | NotoSans-Medium.ttf | Не | Не |
| fr | Френски | NotoSans-Medium.ttf | Не | Не |
| es | Испански | NotoSans-Medium.ttf | Не | Не |
| de | Немски | NotoSans-Medium.ttf | Не | Не |
| ru | Руски | NotoSans-Medium.ttf | Не | Не |
| ar | Арабски | NotoSansArabic-Medium.ttf | Да | Не |
| fa | Персийски (фарси) | NotoSansArabic-Medium.ttf | Да | Не |
| ur | Урду | NotoSansArabic-Medium.ttf | Да | Не |
| zh-CN | Китайски (опростен) | NotoSansCJK-Medium.ttc | Не | Не |
| zh-MO | Китайски (традиционен, Макао) | NotoSansCJK-Medium.ttc | Не | Не |
| zh-HK | Китайски (традиционен, Хонконг) | NotoSansCJK-Medium.ttc | Не | Не |
| zh-TW | Китайски (традиционен, Тайван) | NotoSansCJK-Medium.ttc | Не | Не |
| ja | Японски | NotoSansCJK-Medium.ttc | Не | Не |
| ko | Корейски | NotoSansCJK-Medium.ttc | Не | Не |
| hi | Хинди | NotoSansDevanagari-Medium.ttf | Не | Не |
| bn | Бенгалски | NotoSansBengali-Medium.ttf | Не | Не |
| mr | Марати | NotoSansDevanagari-Medium.ttf | Не | Не |
| ne | Непалски | NotoSansDevanagari-Medium.ttf | Не | Не |
| pa | Пенджаби (Гурмукхи) | NotoSansGurmukhi-Medium.ttf | Не | Не |
| pt-PT | Португалски (Португалия) | NotoSans-Medium.ttf | Не | Не |
| pt-BR | Португалски (Бразилия) | NotoSans-Medium.ttf | Не | Не |
| it | Италиански | NotoSans-Medium.ttf | Не | Не |
| lt | Литовски | NotoSans-Medium.ttf | Не | Не |
| pl | Полски | NotoSans-Medium.ttf | Не | Не |
| tr | Турски | NotoSans-Medium.ttf | Не | Не |
| el | Гръцки | NotoSans-Medium.ttf | Не | Не |
| th | Тайландски | NotoSansThai-Medium.ttf | Не | Не |
| sv | Шведски | NotoSans-Medium.ttf | Не | Не |
| da | Датски | NotoSans-Medium.ttf | Не | Не |
| no | Норвежки | NotoSans-Medium.ttf | Не | Не |
| fi | Фински | NotoSans-Medium.ttf | Не | Не |
| nl | Холандски | NotoSans-Medium.ttf | Не | Не |
| he | Иврит | NotoSansHebrew-Medium.ttf | Да | Не |
| vi | Виетнамски | NotoSans-Medium.ttf | Не | Не |
| id | Индонезийски | NotoSans-Medium.ttf | Не | Не |
| ms | Малайски | NotoSans-Medium.ttf | Не | Не |
| tl | Тагалог (Филипински) | NotoSans-Medium.ttf | Не | Не |
| sw | Суахили | NotoSans-Medium.ttf | Не | Не |
| hu | Унгарски | NotoSans-Medium.ttf | Не | Не |
| cs | Чешки | NotoSans-Medium.ttf | Не | Не |
| sk | Словашки | NotoSans-Medium.ttf | Не | Не |
| ro | Румънски | NotoSans-Medium.ttf | Не | Не |
| bg | Български | NotoSans-Medium.ttf | Не | Не |
| sr | Сръбски (кирилица) | NotoSans-Medium.ttf | Не | Не |
| hr | Хърватски | NotoSans-Medium.ttf | Не | Не |
| sl | Словенски | NotoSans-Medium.ttf | Не | Не |
| uk | Украински | NotoSans-Medium.ttf | Не | Не |
| my | Бирмански (Мианмар) | NotoSansMyanmar-Medium.ttf | Не | Не |
| ta | Тамилски | NotoSansTamil-Medium.ttf | Не | Не |
| et | Естонски | NotoSans-Medium.ttf | Не | Не |
| pcm | Нигерийски пиджин | NotoSans-Medium.ttf | Не | Не |
| te | Телугу | NotoSans-Medium.ttf | Не | Не |
| ml | Малаялам | NotoSans-Medium.ttf | Не | Не |
| kn | Каннада | NotoSans-Medium.ttf | Не | Не |
| km | Кмерски | NotoSansKhmer-Medium.ttf | Не | Не |

## Добавяне на език

За да добавите поддръжка за нов език:

1. Добавете кода на езика и показваното име в езиковите помощни програми.
2. Добавете или присъединете шрифт в `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Тествайте резултата от превода на Markdown и изображения.
4. Отворете pull request с мапинга и бележките за валидация.