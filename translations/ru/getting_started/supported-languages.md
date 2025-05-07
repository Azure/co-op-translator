<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ba33aa8d5da0d3dd14322b77fcb63deb",
  "translation_date": "2025-05-06T17:48:23+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "ru"
}
-->
# Поддерживаемые языки

В таблице ниже перечислены языки, которые в настоящее время поддерживаются **Co-op Translator**. В ней указаны коды языков, их названия и известные проблемы, связанные с каждым языком. Если вы хотите добавить поддержку нового языка, добавьте соответствующий код языка, название и подходящий шрифт в файл `font_language_mappings.yml`, расположенный в `src/co_op_translator/fonts/`, и отправьте pull request после тестирования.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | Английский           | NotoSans-Medium.ttf               | Нет         | Нет          |
| fr            | Французский          | NotoSans-Medium.ttf               | Нет         | Нет          |
| es            | Испанский            | NotoSans-Medium.ttf               | Нет         | Нет          |
| de            | Немецкий             | NotoSans-Medium.ttf               | Нет         | Нет          |
| ru            | Русский              | NotoSans-Medium.ttf               | Нет         | Нет          |
| ar            | Арабский             | NotoSansArabic-Medium.ttf         | Да          | Нет          |
| fa            | Персидский (Фарси)   | NotoSansArabic-Medium.ttf         | Да          | Нет          |
| ur            | Урду                 | NotoSansArabic-Medium.ttf         | Да          | Нет          |
| zh            | Китайский (упрощённый) | NotoSansCJK-Medium.ttc          | Нет         | Нет          |
| mo            | Китайский (традиционный, Макао) | NotoSansCJK-Medium.ttc | Нет         | Нет          |
| hk            | Китайский (традиционный, Гонконг) | NotoSansCJK-Medium.ttc | Нет         | Нет          |
| tw            | Китайский (традиционный, Тайвань) | NotoSansCJK-Medium.ttc  | Нет         | Нет          |
| ja            | Японский             | NotoSansCJK-Medium.ttc            | Нет         | Нет          |
| ko            | Корейский            | NotoSansCJK-Medium.ttc            | Нет         | Нет          |
| hi            | Хинди                | NotoSansDevanagari-Medium.ttf     | Нет         | Нет          |
| bn            | Бенгальский          | NotoSansBengali-Medium.ttf        | Нет         | Нет          |
| mr            | Маратхи              | NotoSansDevanagari-Medium.ttf     | Нет         | Нет          |
| ne            | Непальский           | NotoSansDevanagari-Medium.ttf     | Нет         | Нет          |
| pa            | Пенджаби (Гурмухи)   | NotoSansGurmukhi-Medium.ttf       | Нет         | Нет          |
| pt            | Португальский (Португалия) | NotoSans-Medium.ttf          | Нет         | Нет          |
| br            | Португальский (Бразилия) | NotoSans-Medium.ttf            | Нет         | Нет          |
| it            | Итальянский          | NotoSans-Medium.ttf               | Нет         | Нет          |
| pl            | Польский             | NotoSans-Medium.ttf               | Нет         | Нет          |
| tr            | Турецкий             | NotoSans-Medium.ttf               | Нет         | Нет          |
| el            | Греческий            | NotoSans-Medium.ttf               | Нет         | Нет          |
| th            | Тайский              | NotoSansThai-Medium.ttf           | Нет         | Нет          |
| sv            | Шведский             | NotoSans-Medium.ttf               | Нет         | Нет          |
| da            | Датский              | NotoSans-Medium.ttf               | Нет         | Нет          |
| no            | Норвежский           | NotoSans-Medium.ttf               | Нет         | Нет          |
| fi            | Финский              | NotoSans-Medium.ttf               | Нет         | Нет          |
| nl            | Голландский          | NotoSans-Medium.ttf               | Нет         | Нет          |
| he            | Иврит                | NotoSansHebrew-Medium.ttf         | Да          | Нет          |
| vi            | Вьетнамский          | NotoSans-Medium.ttf               | Нет         | Нет          |
| id            | Индонезийский        | NotoSans-Medium.ttf               | Нет         | Нет          |
| ms            | Малайский            | NotoSans-Medium.ttf               | Нет         | Нет          |
| tl            | Тагальский (филиппинский) | NotoSans-Medium.ttf          | Нет         | Нет          |
| sw            | Суахили              | NotoSans-Medium.ttf               | Нет         | Нет          |
| hu            | Венгерский           | NotoSans-Medium.ttf               | Нет         | Нет          |
| cs            | Чешский              | NotoSans-Medium.ttf               | Нет         | Нет          |
| sk            | Словацкий            | NotoSans-Medium.ttf               | Нет         | Нет          |
| ro            | Румынский            | NotoSans-Medium.ttf               | Нет         | Нет          |
| bg            | Болгарский           | NotoSans-Medium.ttf               | Нет         | Нет          |
| sr            | Сербский (кириллица) | NotoSans-Medium.ttf               | Нет         | Нет          |
| hr            | Хорватский           | NotoSans-Medium.ttf               | Нет         | Нет          |
| sl            | Словенский           | NotoSans-Medium.ttf               | Нет         | Нет          |

## Добавление нового языка

Чтобы добавить поддержку нового языка:

1. Перейдите в [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Добавьте код языка, его название и имя подходящего файла шрифта. Убедитесь, что указали атрибут `rtl`, если язык пишется справа налево.
3. Если нужно использовать новый шрифт, убедитесь, что он свободен для использования в open-source проектах, проверив лицензионные и авторские права. После этого добавьте файл шрифта в каталог `src/co_op_translator/fonts/`.
4. Проверьте изменения локально, чтобы убедиться, что новый язык поддерживается корректно.
5. Отправьте Pull Request с вашими изменениями и укажите в описании PR добавление нового языка.

Пример:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.