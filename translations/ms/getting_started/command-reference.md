<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:31:25+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "ms"
}
-->
# Command reference
The **Co-op Translator** CLI предлагает несколько опций для настройки процесса перевода:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Переводит ваш проект на указанные языки. Пример: translate -l "es fr de" переводит на испанский, французский и немецкий. Используйте translate -l "all" для перевода на все поддерживаемые языки.
translate -l "language_codes" -u              | Обновляет переводы, удаляя существующие и создавая их заново. Внимание: это удалит все текущие переводы для указанных языков.
translate -l "language_codes" -img            | Переводит только файлы изображений.
translate -l "language_codes" -md             | Переводит только Markdown файлы.
translate -l "language_codes" -chk            | Проверяет переведённые файлы на ошибки и при необходимости повторяет перевод.
translate -l "language_codes" -d              | Включает режим отладки для подробного логирования.
translate -l "language_codes" -r "root_dir"   | Указывает корневую директорию проекта.
translate -l "language_codes" -f              | Использует быстрый режим для перевода изображений (до 3 раз быстрее, с небольшой потерей качества и точности).
translate -l "language_codes" -y              | Автоматически подтверждает все запросы (удобно для CI/CD).
translate -l "language_codes" --help          | Показывает справочную информацию по доступным командам.

### Примеры использования:

  1. Поведение по умолчанию (добавление новых переводов без удаления существующих):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Добавить только новые корейские переводы изображений (существующие переводы не удаляются):    translate -l "ko" -img

  3. Обновить все корейские переводы (Внимание: удаляются все текущие корейские переводы перед повторным переводом):    translate -l "ko" -u

  4. Обновить только корейские изображения (Внимание: удаляются все текущие корейские изображения перед повторным переводом):    translate -l "ko" -img -u

  5. Добавить новые переводы Markdown для корейского без изменения других переводов:    translate -l "ko" -md

  6. Проверить переведённые файлы на ошибки и при необходимости повторить перевод: translate -l "ko" -chk

  7. Проверить переведённые файлы на ошибки и повторить перевод (только Markdown): translate -l "ko" -chk -md

  8. Проверить переведённые файлы на ошибки и повторить перевод (только изображения): translate -l "ko" -chk -img

  9. Использовать быстрый режим для перевода изображений:    translate -l "ko" -img -f

  10. Пример режима отладки: - translate -l "ko" -d: Включить подробное логирование.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.