# Підтримувані мови

Co-op Translator підтримує наступні коди мов для текстового, блокнотного та графічного перекладу.

Якщо ви хочете додати нову мову, оновіть відображення мов та відповідність шрифтів у `src/co_op_translator/fonts/` і протестуйте мову перед відкриттям pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Англійська | NotoSans-Medium.ttf | Ні | Ні |
| fr | Французька | NotoSans-Medium.ttf | Ні | Ні |
| es | Іспанська | NotoSans-Medium.ttf | Ні | Ні |
| de | Німецька | NotoSans-Medium.ttf | Ні | Ні |
| ru | Російська | NotoSans-Medium.ttf | Ні | Ні |
| ar | Арабська | NotoSansArabic-Medium.ttf | Так | Ні |
| fa | Перська (фарсі) | NotoSansArabic-Medium.ttf | Так | Ні |
| ur | Урду | NotoSansArabic-Medium.ttf | Так | Ні |
| zh-CN | Китайська (спрощена) | NotoSansCJK-Medium.ttc | Ні | Ні |
| zh-MO | Китайська (традиційна, Макао) | NotoSansCJK-Medium.ttc | Ні | Ні |
| zh-HK | Китайська (традиційна, Гонконг) | NotoSansCJK-Medium.ttc | Ні | Ні |
| zh-TW | Китайська (традиційна, Тайвань) | NotoSansCJK-Medium.ttc | Ні | Ні |
| ja | Японська | NotoSansCJK-Medium.ttc | Ні | Ні |
| ko | Корейська | NotoSansCJK-Medium.ttc | Ні | Ні |
| hi | Хінді | NotoSansDevanagari-Medium.ttf | Ні | Ні |
| bn | Бенгальська | NotoSansBengali-Medium.ttf | Ні | Ні |
| mr | Маратхі | NotoSansDevanagari-Medium.ttf | Ні | Ні |
| ne | Непальська | NotoSansDevanagari-Medium.ttf | Ні | Ні |
| pa | Пенджабі (гурмухі) | NotoSansGurmukhi-Medium.ttf | Ні | Ні |
| pt-PT | Португальська (Португалія) | NotoSans-Medium.ttf | Ні | Ні |
| pt-BR | Португальська (Бразилія) | NotoSans-Medium.ttf | Ні | Ні |
| it | Італійська | NotoSans-Medium.ttf | Ні | Ні |
| lt | Литовська | NotoSans-Medium.ttf | Ні | Ні |
| pl | Польська | NotoSans-Medium.ttf | Ні | Ні |
| tr | Турецька | NotoSans-Medium.ttf | Ні | Ні |
| el | Грецька | NotoSans-Medium.ttf | Ні | Ні |
| th | Тайська | NotoSansThai-Medium.ttf | Ні | Ні |
| sv | Шведська | NotoSans-Medium.ttf | Ні | Ні |
| da | Данська | NotoSans-Medium.ttf | Ні | Ні |
| no | Норвезька | NotoSans-Medium.ttf | Ні | Ні |
| fi | Фінська | NotoSans-Medium.ttf | Ні | Ні |
| nl | Нідерландська | NotoSans-Medium.ttf | Ні | Ні |
| he | Іврит | NotoSansHebrew-Medium.ttf | Так | Ні |
| vi | В'єтнамська | NotoSans-Medium.ttf | Ні | Ні |
| id | Індонезійська | NotoSans-Medium.ttf | Ні | Ні |
| ms | Малайська | NotoSans-Medium.ttf | Ні | Ні |
| tl | Тагальська (філіппінська) | NotoSans-Medium.ttf | Ні | Ні |
| sw | Суахілі | NotoSans-Medium.ttf | Ні | Ні |
| hu | Угорська | NotoSans-Medium.ttf | Ні | Ні |
| cs | Чеська | NotoSans-Medium.ttf | Ні | Ні |
| sk | Словацька | NotoSans-Medium.ttf | Ні | Ні |
| ro | Румунська | NotoSans-Medium.ttf | Ні | Ні |
| bg | Болгарська | NotoSans-Medium.ttf | Ні | Ні |
| sr | Сербська (кирилиця) | NotoSans-Medium.ttf | Ні | Ні |
| hr | Хорватська | NotoSans-Medium.ttf | Ні | Ні |
| sl | Словенська | NotoSans-Medium.ttf | Ні | Ні |
| uk | Українська | NotoSans-Medium.ttf | Ні | Ні |
| my | Бірманська (Мʼянма) | NotoSansMyanmar-Medium.ttf | Ні | Ні |
| ta | Тамільська | NotoSansTamil-Medium.ttf | Ні | Ні |
| et | Естонська | NotoSans-Medium.ttf | Ні | Ні |
| pcm | Нігерійський піджин | NotoSans-Medium.ttf | Ні | Ні |
| te | Телугу | NotoSans-Medium.ttf | Ні | Ні |
| ml | Малаялам | NotoSans-Medium.ttf | Ні | Ні |
| kn | Каннада | NotoSans-Medium.ttf | Ні | Ні |
| km | Кхмерська | NotoSansKhmer-Medium.ttf | Ні | Ні |

## Додати мову

Щоб додати підтримку нової мови:

1. Додайте код мови та назву для відображення до утиліт мови.
2. Додайте або зіставте шрифт у `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Протестуйте вивід перекладу для Markdown та зображень.
4. Відкрийте pull request з відповідністю та нотатками перевірки.