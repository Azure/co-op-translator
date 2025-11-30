<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:35:57+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "ru"
}
-->
# Обновление раздела «Другие курсы» (репозитории Microsoft Beginners)

В этом руководстве объясняется, как сделать автоматическую синхронизацию раздела «Другие курсы» с помощью Co-op Translator и как обновить глобальный шаблон для всех репозиториев.

- Применимо к: только репозиториям Microsoft Beginners
- Работает с: Co-op Translator CLI и GitHub Actions
- Исходный шаблон: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Быстрый старт: включение авто-синхронизации в вашем репозитории

Добавьте следующие маркеры вокруг раздела «Другие курсы» в вашем README. Co-op Translator будет заменять всё между этими маркерами при каждом запуске.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Каждый раз при запуске Co-op Translator — через CLI (например, `translate -l "<language codes>"`) или GitHub Actions — автоматически обновляется раздел «Другие курсы», заключённый в эти маркеры.

> [!NOTE]
> Если у вас уже есть список, просто оберните его в те же маркеры. При следующем запуске он будет заменён на актуальное стандартизированное содержимое.

---

## Как изменить глобальное содержимое

Если вы хотите обновить стандартизированное содержимое, которое отображается во всех репозиториях Beginners:

1. Отредактируйте шаблон: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Создайте pull request с вашими изменениями в репозиторий Co-op Translator
3. После слияния PR версия Co-op Translator будет обновлена
4. При следующем запуске Co-op Translator (через CLI или GitHub Action) в целевом репозитории раздел будет автоматически синхронизирован с обновлённым содержимым

Это гарантирует единый источник правды для раздела «Другие курсы» во всех репозиториях Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->