<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:52:55+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "uk"
}
-->
# Оновлення розділу "Інші курси" (репозиторії Microsoft Beginners)

Цей посібник пояснює, як зробити автоматичну синхронізацію розділу "Інші курси" за допомогою Co-op Translator, а також як оновити глобальний шаблон для всіх репозиторіїв.

- Застосовується до: лише репозиторіїв Microsoft Beginners
- Працює з: Co-op Translator CLI та GitHub Actions
- Джерело шаблону: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Швидкий старт: Увімкнення авто-синхронізації у вашому репозиторії

Додайте наступні маркери навколо розділу "Інші курси" у вашому README. Co-op Translator замінюватиме все між цими маркерами при кожному запуску.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Кожного разу, коли запускається Co-op Translator — через CLI (наприклад, `translate -l "<language codes>"`) або GitHub Actions — він автоматично оновлює розділ "Інші курси", обгорнутий цими маркерами.

> [!NOTE]
> Якщо у вас вже є існуючий список, просто обгорніть його тими ж маркерами. Наступний запуск замінить його на останній стандартизований вміст.

---

## Як змінити глобальний вміст

Якщо ви хочете оновити стандартизований вміст, який з’являється у всіх репозиторіях Beginners:

1. Відредагуйте шаблон: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Відкрийте pull request у репозиторій Co-op Translator зі своїми змінами
3. Після злиття PR версія Co-op Translator буде оновлена
4. Наступного разу, коли Co-op Translator запуститься (через CLI або GitHub Action) у цільовому репозиторії, він автоматично синхронізує оновлений розділ

Це гарантує єдине джерело правди для вмісту розділу "Інші курси" у всіх репозиторіях Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->