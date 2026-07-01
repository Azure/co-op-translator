# שרת MCP

Co-op Translator כולל שרת Model Context Protocol עבור סוכנים, עורכים, ולקוחות התואמים MCP.

בהתקנה מקומית ברירת המחדל, המשתמשים אינם משאירים שרת נפרד פועל באופן ידני. הם מגדירים את לקוח ה-MCP שלהם, והלקוח מפעיל אוטומטית את `co-op-translator-mcp` מעל `stdio` כאשר הוא זקוק לכלי Co-op Translator.

אם אתם מתלבטים בין CLI, ממשק Python, ו-MCP, התחילו עם [בחר את זרימת העבודה שלך](workflows.md).

השתמשו ב-MCP כאשר סוכן או עורך צריכים לקרוא ל-Co-op Translator ישירות:

| מטרה של המשתמש | כלי MCP |
| --- | --- |
| לתרגם מסמך Markdown, מחברת, או תמונה | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| לתרגם תוכן Markdown או מחברת בעזרת מודל הסוכן המארח | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| לשכתב קישורים מתורגמים ב-Markdown או במחברת לאחר בחירת נתיב פלט | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| לתרגם מאגר שלם כמו ה-CLI | `run_translation`, `translate_project` |
| לבחון פלט מתורגם ללא אישורי LLM | `run_review` |
| לבדוק יכולות ומצב סביבה | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

שרת ה-MCP עוטף את אותו ממשק Python ציבורי המתועד ב-[ממשק ה-Python](api.md). כלים הנתמכים על ידי ספקים משתמשים באותם ספקים המוגדרים כמו ב-CLI ובממשק ה-Python. כלים בעזרת סוכן מכינים חלקים עבור סוכן המארח של ה-MCP כדי לתרגם, ואז משתמשים ב-Co-op Translator כדי לשחזר את ה-Markdown או המחברת הסופיים.

## שלב 1: התקנה ותצורה של Co-op Translator

התקינו את Co-op Translator בסביבת ה-Python שבה לקוח ה-MCP שלכם ישתמש:

```bash
pip install co-op-translator
```

לעבודה מקומית מהמאגר הזה, התקינו את החבילה במצב ניתן לעריכה:

```bash
pip install -e .
```

בחרו את מצב התרגום שבו לקוח ה-MCP שלכם ישתמש:

| מצב | השתמש בזה ל- | אישורים |
| --- | --- | --- |
| Provider-backed | Co-op Translator קורא ל-`translate_markdown_content`, `translate_notebook_content`, `translate_image_content`, או `run_translation`. | תרגום Markdown ומחברת דורש Azure OpenAI או OpenAI. תרגום תמונות דורש גם Azure AI Vision. |
| Agent-assisted | סוכן המארח של ה-MCP מתרגם חלקים שמוחזרים על ידי `start_markdown_agent_translation` או `start_notebook_agent_translation`. | לא נדרשים אישורי ספק LLM של Co-op Translator עבור חלקי Markdown או מחברת. תרגום תמונות אינו נתמך עדיין במצב זה. |

אם אתם מתחילים בתרגום Markdown או מחברות בתוך סוכן כגון Codex או Claude Code, התחילו במצב Agent-assisted. השתמשו במצב Provider-backed כאשר אתם רוצים ש-Co-op Translator עצמו יקרא לספקים המוגדרים שלכם, כאשר אתם מתרגמים תמונות, או כאשר אתם מריצים תרגום ברמת המאגר כמו ב-CLI.

הגדירו אישורי ספקים רק בשביל תזרימי עבודה Provider-backed:

```bash
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

תרגום תמונות בעל גיבוי ספק דורש בנוסף:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    מצב Agent-assisted מכסה כיום Markdown ותאי Markdown במחברות. תרגום תמונות עדיין משתמש בצינור התמונות הנתמך על ידי ספק ודורש Azure AI Vision ל-OCR ולרינדור המודע לפריסה.

## שלב 2: הגדרת לקוח ה-MCP שלכם

בהגדרת `stdio` המקומית הרגילה, הוסיפו את Co-op Translator לתצורת לקוח ה-MCP שלכם. הלקוח יפעיל ויכבה את התהליך באופן אוטומטי.

תצורת החבילה המותקנת:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "co-op-translator-mcp",
      "args": []
    }
  }
}
```

תצורת סל המקור ב-Windows:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "C:\\Users\\you\\dev\\co-op-translator\\.venv\\Scripts\\python.exe",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "C:\\Users\\you\\dev\\co-op-translator"
    }
  }
}
```

תצורת סל המקור ב-macOS או Linux:

```json
{
  "mcpServers": {
    "co-op-translator": {
      "command": "/Users/you/dev/co-op-translator/.venv/bin/python",
      "args": ["-m", "co_op_translator.mcp.server"],
      "cwd": "/Users/you/dev/co-op-translator"
    }
  }
}
```

לאחר שינוי תצורת לקוח ה-MCP, אתחלו או רעננו את הלקוח כדי שיוכל לגלות את השרת החדש.

## שלב 3: אימות השרת בלקוח

בקשו מהלקוח של ה-MCP לרשום את הכלים הזמינים, או קראו לאחד העוזרים לקריאה בלבד קודם:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

בדיקות ראשוניות מועילות:

| כלי | מה לבדוק |
| --- | --- |
| `get_api_overview` | מבטיח שהשרת נגיש ומציג את זרימות העבודה הזמינות. |
| `list_supported_languages` | מבטיח שניתן לטעון את נתוני השפה המופקדים. |
| `get_configuration_status` | מאשר זמינות ספקי LLM ו-Vision מבלי לחשוף ערכים סודיים. |

## שלב 4: בחר זרימת עבודה

### תרגום קבצים או מסמכים בודדים

השתמשו בכלי התוכן בעל גיבוי ספק כאשר ללקוח ה-MCP כבר יש תוכן מסמך או נתיב תמונה ו-Co-op Translator אמור לקרוא לספקי התרגום המוגדרים.

לגבי Markdown:

1. קראו ל-`translate_markdown_content` עם `document`, `language_code`, ובאופן אופציונלי `source_path`.
2. אם התוצאה המתורגמת תכתב לתבנית פלט של Co-op Translator, קראו ל-`rewrite_markdown_paths`.
3. אפשרו ללקוח לכתוב או להחזיר את ה-`content` הסופי.

לגבי מחברות:

1. קראו ל-`translate_notebook_content` עם JSON של המחברת ו-`language_code`.
2. קראו ל-`rewrite_notebook_paths` אם יש צורך להתאים קישורים מתורגמים לנתיב יעד.
3. כתבו או החזירו את JSON של המחברת הסופית.

לגבי תמונות:

1. קראו ל-`translate_image_content` עם `image_path`, `language_code`, ואפשרות `root_dir` או `fast_mode`.
2. קראו את ה-`data_base64` ו-`mime_type` המוחזרים.
3. אם סופק `output_path`, התמונה המתורגמת גם נשמרת לאותו נתיב.

כלי התוכן אינם מבצעים גילוי פרויקטים, עדכוני מטא-דאטה, כתב-תנאי ויתורים, או שכתוב נתיבים אוטומטי. אם תרצו שסוכן המארח יתיר לתרגם חלקי Markdown או מחברת ללא אישורי ספק LLM של Co-op Translator, השתמשו בזרימת העבודה בעזרת סוכן להלן.

### תרגום בעזרת מודל הסוכן המארח

השתמשו בכלים בעזרת סוכן כאשר אתם רוצים שסוכן המארח של ה-MCP, כגון עוזר קידוד, יפיק את הטקסט המתורגם במקום להגדיר Azure OpenAI או OpenAI עבור Co-op Translator.

בלקוח MCP מבוסס צ'אט, בדרך כלל אין צורך לכתוב JSON של כלי בעצמכם. בקשו מהסוכן להשתמש בזרימת העבודה בעזרת סוכן:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

למחברות, השתמשו באותו דפוס:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

אם לקוח ה-MCP שלכם תומך בהנחיות שרת, השתמשו ב-`agent_assisted_markdown_translation_prompt` כדי שהלקוח יטען את הוראות זרימת העבודה הזהות.

לגבי Markdown:

1. קראו ל-`start_markdown_agent_translation` עם `document`, `language_code`, ובאופן אופציונלי `source_path`.
2. תרגמו כל חלק שמוחזר בסוכן המארח לפי ה-`prompt` של החלק.
3. קראו ל-`finish_markdown_agent_translation` עם ה-`job` המקורי והחלקים המתורגמים באמצעות `chunk_id` ו-`translated_text`.
4. אם התוכן ייכתב לנתיב יעד מתורגם, קראו ל-`rewrite_markdown_paths`.

לגבי מחברות:

1. קראו ל-`start_notebook_agent_translation` עם JSON של המחברת ו-`language_code`.
2. תרגמו כל חלק שמוחזר בסוכן המארח.
3. קראו ל-`finish_notebook_agent_translation` עם ה-`job` המקורי והחלקים המתורגמים.
4. קראו ל-`rewrite_notebook_paths` אם קישורים מתורגמים במחברת צריכים התאמה לנתיב יעד.

כלים בעזרת סוכן אינם קוראים ל-Azure OpenAI או OpenAI מתוך Co-op Translator. סוכן המארח אחראי על תרגום החלקים המוחזרים. Co-op Translator מטפל בחיתוך Markdown, שימור מחלקים זמניים (placeholders), שיחזור frontmatter, החלפת תאי מחברת, ונירמול לאחר התרגום.

### תרגום מאגר שלם

השתמשו ב-`run_translation` כאשר המשתמש רוצה ש-Co-op Translator יתנהג כמו פקודת `translate` של ה-CLI.

תרגום מאגר ברירת מחדל הוא `dry_run=true` כך שסוכן יכול לבדוק את היקף השינויים לפני שינויים בקבצים:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

כדי לאפשר כתיבה, הקורא חייב להגדיר גם `dry_run=false` וגם `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` נחשף ככינוי תאימות ל-`run_translation`.

### בדיקת הפלט המתורגם

השתמשו ב-`run_review` עבור בדיקות דטרמיניסטיות שאינן דורשות אישורי LLM או Vision:

!!! note "Beta"
    MCP חושף את ממשק ה-beta `run_review`. הוא בטוח לזרימות עבודה של סקירה לקריאה בלבד, אך בדיקות הסקירה וסכימות הבעיות עשויות להתפתח.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

התוצאה כוללת פלט טקסט שנתפס וסיכום סקירה מובנה כאשר זמין.

## הרצות שרת ידניות

הרצות ידניות מיועדות בעיקר לניפוי שגיאות או לתובענים המתנהגים כמו שרתים ארוכי-טווח.

ניפוי שגיאות של שרת stdio ברירת המחדל:

```bash
co-op-translator-mcp
```

הרצה מתוך סל המקור:

```bash
python -m co_op_translator.mcp.server
```

הפעלת שרת HTTP או SSE ארוך-טווח:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

לאינטגרציות מקומיות עם עורך וסוכן, העדיפו את תצורת `stdio` המנוהלת על ידי הלקוח בשלב 2.

## כלים

| כלי | מטרה | כותב קבצים |
| --- | --- | --- |
| `translate_markdown_content` | לתרגם מחרוזת Markdown. | לא |
| `translate_notebook_content` | לתרגם תאי Markdown ב-JSON של מחברת. | לא |
| `translate_image_content` | לתרגם טקסט בתמונה אחת ולהחזיר נתוני תמונה ב-base64. | אופציונלי, רק כאשר `output_path` מסופק |
| `start_markdown_agent_translation` | להכין חלקי Markdown לסוכן המארח לתרגום ללא אישורי ספק LLM של Co-op Translator. | לא |
| `finish_markdown_agent_translation` | לשחזר Markdown מתוך חלקים מתורגמים של סוכן המארח. | לא |
| `start_notebook_agent_translation` | להכין חלקי תאי Markdown במחברת לסוכן המארח לתרגום. | לא |
| `finish_notebook_agent_translation` | לשחזר JSON של מחברת מתוך חלקים מתורגמים של סוכן המארח. | לא |
| `rewrite_markdown_paths` | לשכתב נתיבים בגוף Markdown וב-frontmatter עבור יעד מתורגם. | לא |
| `rewrite_notebook_paths` | לשכתב נתיבים בתוך תאי Markdown במחברת. | לא |
| `run_translation` | להריץ תרגום ברמת הפרויקט כמו ב-CLI. | כן כאשר `dry_run=false` ו-`confirm_write=true` |
| `translate_project` | כינוי תאימות ל-`run_translation`. | כן כאשר `dry_run=false` ו-`confirm_write=true` |
| `run_review` | להריץ בדיקות סקירה דטרמיניסטיות. | לא |
| `get_configuration_status` | לדווח על ספקי LLM ו-Vision המוגדרים מבלי לחשוף סודות. | לא |
| `list_supported_languages` | לרשום קודי שפות יעד הנתמכים. | לא |
| `get_api_overview` | לתאר זרימות עבודה וכלי MCP הזמינים. | לא |

## משאבים

| Resource URI | Purpose |
| --- | --- |
| `co-op://api` | סקירת JSON של זרימות עבודה וכלים. |
| `co-op://supported-languages` | רשימת JSON של קודי שפות נתמכים. |
| `co-op://configuration` | סיכום זמינות ספקים ב-JSON ללא סודות. |

## הנחיות (Prompts)

| Prompt | Purpose |
| --- | --- |
| `translate_markdown_document_prompt` | להנחות לקוח MCP בתרגום תוכן פלוס שכתוב נתיבים אופציונלי. |
| `agent_assisted_markdown_translation_prompt` | להנחות לקוח MCP בתרגום Markdown באמצעות סוכן המארח ללא אישורי ספק LLM של Co-op Translator. |
| `translate_repository_prompt` | להנחות לקוח MCP בתרגום מאגר שמתחיל ב-dry-run. |

## דוגמאות להעתקה והדבקה

תרגום תוכן Markdown:

```json
{
  "tool": "translate_markdown_content",
  "arguments": {
    "document": "# Hello\n\nWelcome to the course.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

שכתוב קישורי Markdown מתורגמים:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](../../images/hero.png)",
    "source_path": "docs/guide.md",
    "target_path": "translations/ko/docs/guide.md",
    "policy": {
      "language_code": "ko",
      "root_dir": ".",
      "translations_dir": "translations",
      "translated_images_dir": "translated_images",
      "translation_types": ["markdown", "images"]
    }
  }
}
```

תרגום Markdown בעזרת מודל הסוכן המארח:

```json
{
  "tool": "start_markdown_agent_translation",
  "arguments": {
    "document": "# Hello\n\nUse `pip install` to get started.",
    "language_code": "ko",
    "source_path": "docs/guide.md"
  }
}
```

לאחר שסוכן המארח מתרגם כל חלק שמוחזר, סיימו את העבודה עם אובייקט ה-`job` המלא המוחזר על ידי `start_markdown_agent_translation`:

```text
tool: finish_markdown_agent_translation
arguments:
  job: <the full job object returned by start_markdown_agent_translation>
  translated_chunks:
    - chunk_id: body:1
      translated_text: "# 안녕하세요\n\n시작하려면 `pip install`을 사용하세요."
```

תצוגה מקדימה של תרגום מאגר:

```json
{
  "tool": "run_translation",
  "arguments": {
    "language_codes": "ko",
    "root_dir": ".",
    "markdown": true,
    "dry_run": true
  }
}
```

## פתרון בעיות

| בעיה | מה לנסות |
| --- | --- |
| לקוח ה-MCP לא מוצא את `co-op-translator-mcp`. | השתמשו בנתיב המוחלט של הפייתון וב-`["-m", "co_op_translator.mcp.server"]` בתצורת סל המקור. |
| השרת מופיע אך התרגום נכשל. | קראו ל-`get_configuration_status` ואשרו שספק LLM זמין. |
| אתם רוצים תרגום Markdown או מחברת ללא מפתחות Azure OpenAI/OpenAI. | השתמשו ב-`start_markdown_agent_translation` / `finish_markdown_agent_translation` או בשקולים של המחברת כך שסוכן המארח יתרגם את החלקים. |
| תרגום תמונות נכשל. | אשרו שמשתני Azure AI Vision מוגדרים וקראו ל-`get_configuration_status`. |
| תרגום מאגר אינו כותב קבצים. | הגדרו `dry_run=false` ו-`confirm_write=true` רק לאחר אישור מפורש של המשתמש. |
| שינויים בתצורת הלקוח אינם מופיעים. | אתחלו או רעננו את לקוח ה-MCP. |

## הערות בטיחות

- קריאות לכלי MCP נמצאות בשליטת המודל על ידי יישום המארח, לכן תרגום מאגר הוא dry-run כברירת מחדל.
- תרגום מלא של מאגר יכול ליצור, לעדכן, או להסיר קבצים רבים. דרשו אישור מפורש של המשתמש לפני הגדרת `confirm_write=true`.
- כלי בדיקת מצב התצורה לעולם לא מחזיר מפתחות API, נקודות קצה, או ערכים סודיים אחרים.
- תרגום תמונות מחזיר נתוני תמונה ב-base64. תמונות גדולות עלולות לייצר תגובות כלי גדולות.
- כלים בעזרת סוכן מחזירים חלקי מקור והנחיות לסוכן ה-MCP המארח. השתמשו בהם רק עם תוכן שהמשתמש מרגיש בנוח לשלוח למודל הסוכן המארח ההוא.