<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:19:06+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "bg"
}
-->
# Поддържани езици

Таблицата по-долу показва езиците, които в момента се поддържат от **Co-op Translator**. Тя включва кодовете на езиците, имената им и известни проблеми, свързани с всеки език. Ако искате да добавите поддръжка за нов език, моля добавете съответния езиков код, име и подходящ шрифт във файла `font_language_mappings.yml`, намиращ се в `src/co_op_translator/fonts/`, и изпратете pull request след като го тествате.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | Английски            | NotoSans-Medium.ttf               | Не          | Не           |
| fr            | Френски              | NotoSans-Medium.ttf               | Не          | Не           |
| es            | Испански             | NotoSans-Medium.ttf               | Не          | Не           |
| de            | Немски               | NotoSans-Medium.ttf               | Не          | Не           |
| ru            | Руски                | NotoSans-Medium.ttf               | Не          | Не           |
| ar            | Арабски              | NotoSansArabic-Medium.ttf         | Да          | Не           |
| fa            | Персийски (Фарси)    | NotoSansArabic-Medium.ttf         | Не          | Не           |
| ur            | Урду                 | NotoSansArabic-Medium.ttf         | Не          | Не           |
| zh            | Китайски (опростен)  | NotoSansCJK-Medium.ttc            | Не          | Не           |
| mo            | Китайски (традиционен, Макао) | NotoSansCJK-Medium.ttc    | Не          | Не           |
| hk            | Китайски (традиционен, Хонконг) | NotoSansCJK-Medium.ttc| Не          | Не           |
| tw            | Китайски (традиционен, Тайван) | NotoSansCJK-Medium.ttc   | Не          | Не           |
| ja            | Японски              | NotoSansCJK-Medium.ttc            | Не          | Не           |
| ko            | Корейски             | NotoSansCJK-Medium.ttc            | Не          | Не           |
| hi            | Хинди                | NotoSansDevanagari-Medium.ttf     | Не          | Не           |
| bn            | Бенгалски            | NotoSansBengali-Medium.ttf        | Не          | Не           |
| mr            | Марати               | NotoSansDevanagari-Medium.ttf     | Не          | Не           |
| ne            | Непалски             | NotoSansDevanagari-Medium.ttf     | Не          | Не           |
| pa            | Пенджабски (Гурмукхи)| NotoSansGurmukhi-Medium.ttf       | Не          | Не           |
| pt            | Португалски (Португалия)| NotoSans-Medium.ttf             | Не          | Не           |
| br            | Португалски (Бразилия)| NotoSans-Medium.ttf               | Не          | Не           |
| it            | Италиански           | NotoSans-Medium.ttf               | Не          | Не           |
| pl            | Полски               | NotoSans-Medium.ttf               | Не          | Не           |
| tr            | Турски               | NotoSans-Medium.ttf               | Не          | Не           |
| el            | Гръцки               | NotoSans-Medium.ttf               | Не          | Не           |
| th            | Тайландски           | NotoSansThai-Medium.ttf           | Не          | Не           |
| sv            | Шведски              | NotoSans-Medium.ttf               | Не          | Не           |
| da            | Датски               | NotoSans-Medium.ttf               | Не          | Не           |
| no            | Норвежки             | NotoSans-Medium.ttf               | Не          | Не           |
| fi            | Фински               | NotoSans-Medium.ttf               | Не          | Не           |
| nl            | Холандски            | NotoSans-Medium.ttf               | Не          | Не           |
| he            | Иврит                | NotoSansHebrew-Medium.ttf         | Не          | Не           |
| vi            | Виетнамски           | NotoSans-Medium.ttf               | Не          | Не           |
| id            | Индонезийски         | NotoSans-Medium.ttf               | Не          | Не           |
| ms            | Малайски             | NotoSans-Medium.ttf               | Не          | Не           |
| tl            | Тагалог (Филипински) | NotoSans-Medium.ttf               | Не          | Не           |
| sw            | Свахили              | NotoSans-Medium.ttf               | Не          | Не           |
| hu            | Унгарски             | NotoSans-Medium.ttf               | Не          | Не           |
| cs            | Чешки                | NotoSans-Medium.ttf               | Не          | Не           |
| sk            | Словацки             | NotoSans-Medium.ttf               | Не          | Не           |
| ro            | Румънски             | NotoSans-Medium.ttf               | Не          | Не           |
| bg            | Български            | NotoSans-Medium.ttf               | Не          | Не           |
| sr            | Сърбски (кирилица)   | NotoSans-Medium.ttf               | Не          | Не           |
| hr            | Хърватски            | NotoSans-Medium.ttf               | Не          | Не           |
| sl            | Словенски            | NotoSans-Medium.ttf               | Не          | Не           |
| uk            | Украински            | NotoSans-Medium.ttf               | Не          | Не           |
| my            | Бирмански (Мианмар) | NotoSans-Medium.ttf               | Не          | Не           |

## Добавяне на нов език

За да добавите поддръжка за нов език:

1. Отидете на [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Добавете езиковия код, име и подходящото име на файла с шрифт. Уверете се, че сте включили атрибута `rtl`, ако езикът е с посока отдясно-наляво.
3. Ако трябва да използвате нов шрифт, уверете се, че той е безплатен за използване в проекти с отворен код, като проверите лиценза и авторските права. След проверка, добавете файла с шрифта в директорията `src/co_op_translator/fonts/`.
4. Тествайте промените локално, за да се уверите, че новият език е правилно поддържан.
5. Изпратете Pull Request с вашите промени и посочете добавянето на новия език в описанието на PR.

Пример:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.