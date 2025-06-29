<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:32:04+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "uk"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Огляд
Microsoft Co-Op Translator — це потужний інструмент для бездоганного перекладу документів у форматі Markdown. Цей посібник допоможе вам усунути поширені проблеми, що виникають під час використання інструменту.

## Поширені проблеми та рішення

### 1. Проблема з тегом Markdown
**Проблема:** Перекладений документ Markdown містить тег `markdown` на початку, що спричиняє проблеми з відображенням.

**Рішення:** Щоб виправити це, просто видаліть тег `markdown` на початку файлу. Це дозволить коректно відобразити файл Markdown.

**Кроки:**
1. Відкрийте перекладений файл Markdown (`.md`).
2. Знайдіть тег `markdown` на початку документа.
3. Видаліть тег `markdown`.
4. Збережіть зміни у файлі.
5. Знову відкрийте файл, щоб переконатися, що він відображається правильно.

### 2. Проблема з URL вбудованих зображень
**Проблема:** URL вбудованих зображень не відповідають мовній локалі, через що зображення відображаються неправильно або відсутні.

**Рішення:** Перевірте URL вбудованих зображень і переконайтеся, що вони відповідають мовній локалі. Усі зображення розміщені у папці `translated_images`, кожне зображення має мовний тег у назві файлу.

**Кроки:**
1. Відкрийте перекладений документ Markdown.
2. Знайдіть вбудовані зображення та їхні URL.
3. Переконайтеся, що мовна локаль у назві файлу зображення відповідає мові документа.
4. За потреби оновіть URL.
5. Збережіть зміни та знову відкрийте документ, щоб переконатися, що зображення відображаються правильно.

### 3. Точність перекладу
**Проблема:** Перекладений текст неточний або потребує додаткового редагування.

**Рішення:** Перегляньте перекладений документ і внесіть необхідні правки для покращення точності та читабельності.

**Кроки:**
1. Відкрийте перекладений документ.
2. Уважно перегляньте зміст.
3. Внесіть необхідні правки для покращення точності перекладу.
4. Збережіть зміни.

### 4. Проблеми з форматуванням файлу
**Проблема:** Форматування перекладеного документа неправильне. Це може траплятися з таблицями, тут додатковий ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` допоможе вирішити проблеми з таблицями.

**Кроки:**
1. Відкрийте перекладений документ.
2. Порівняйте його з оригінальним документом, щоб виявити проблеми з форматуванням.
3. Відкоригуйте форматування відповідно до оригіналу.
4. Збережіть зміни.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, просимо враховувати, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.