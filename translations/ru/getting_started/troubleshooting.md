<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:22:20+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "ru"
}
-->
# Руководство по устранению неполадок Microsoft Co-op Translator


## Обзор
Microsoft Co-Op Translator — мощный инструмент для беспроблемного перевода документов в формате Markdown. Это руководство поможет вам решить распространённые проблемы при использовании этого инструмента.

## Распространённые проблемы и их решения

### 1. Проблема с тегом Markdown
**Проблема:** В переведённом документе Markdown вверху появляется тег `markdown`, из-за чего возникают ошибки отображения.

**Решение:** Чтобы исправить это, просто удалите тег `markdown` в начале файла. Это позволит корректно отобразить Markdown-документ.

**Шаги:**
1. Откройте переведённый файл Markdown (`.md`).
2. Найдите тег `markdown` в начале документа.
3. Удалите тег `markdown`.
4. Сохраните изменения в файле.
5. Откройте файл снова, чтобы убедиться, что он отображается корректно.

### 2. Проблема с URL встроенных изображений
**Проблема:** URL встроенных изображений не соответствуют языковой локали, из-за чего изображения отображаются неправильно или отсутствуют.

**Решение:** Проверьте URL встроенных изображений и убедитесь, что они соответствуют языковой локали. Все изображения находятся в папке `translated_images`, при этом в имени файла каждого изображения присутствует языковой тег.

**Шаги:**
1. Откройте переведённый документ Markdown.
2. Найдите встроенные изображения и их URL.
3. Проверьте, совпадает ли языковая локаль в имени файла изображения с языком документа.
4. При необходимости обновите URL.
5. Сохраните изменения и откройте документ снова, чтобы убедиться, что изображения отображаются правильно.

### 3. Точность перевода
**Проблема:** Переведённый текст неточен или требует доработки.

**Решение:** Проверьте переведённый документ и внесите необходимые правки для повышения точности и удобочитаемости.

**Шаги:**
1. Откройте переведённый документ.
2. Внимательно прочитайте содержимое.
3. Внесите нужные исправления для улучшения качества перевода.
4. Сохраните изменения.

### 4. Проблемы с форматированием файла
**Проблема:** Форматирование переведённого документа нарушено. Это может касаться таблиц — здесь дополнительный ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` поможет решить проблемы с таблицами.

**Шаги:**
1. Откройте переведённый документ.
2. Сравните его с оригиналом, чтобы выявить ошибки форматирования.
3. Отредактируйте форматирование так, чтобы оно соответствовало оригиналу.
4. Сохраните изменения.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.