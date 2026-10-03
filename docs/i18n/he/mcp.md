# שרת MCP

Co-op Translator כולל שרת Model Context Protocol עבור סוכנים, עורכים ולקוחות תואמי MCP.

בהגדרת ברירת המחדל המקומית, המשתמשים אינם מריצים שרת נפרד באופן ידני. הם מגדירים את לקוח ה‑MCP שלהם, והלקוח מפעיל אוטומטית את `co-op-translator-mcp` דרך `stdio` כאשר הוא זקוק לכלי Co-op Translator.

אם אתם מחליטים בין CLI, Python API, ו‑MCP, התחילו עם [בחר את זרימת העבודה שלך](workflows.md).

השתמשו ב‑MCP כאשר סוכן או עורך צריכים לקרוא ל‑Co-op Translator ישירות:

| מטרת המשתמש | כלי MCP |
| --- | --- |
| לתרגם מסמך Markdown יחיד, מחברת או תמונה | `translate_markdown_content`, `translate_notebook_content`, `translate_image_content` |
| לתרגם תוכן Markdown או מחברת באמצעות מודל הסוכן המארח | `start_markdown_agent_translation`, `finish_markdown_agent_translation`, `start_notebook_agent_translation`, `finish_notebook_agent_translation` |
| לשכתב קישורים ב‑Markdown או במחברת המתורגמים לאחר בחירת נתיב הפלט | `rewrite_markdown_paths`, `rewrite_notebook_paths` |
| לתרגם מאגר שלם כמו ה‑CLI | `run_translation`, `translate_project` |
| לבחון את הפלט המתורגם ללא אישורי LLM | `run_review` |
| לבדוק יכולות ומצב הסביבה | `get_api_overview`, `list_supported_languages`, `get_configuration_status` |

שרת ה‑MCP עוטף את ממשק ה‑Python הציבורי המתועד ב[Python API](api.md). הכלים הנתמכים על‑ידי ספק משתמשים באותם ספקים המוגדרים כמו ב‑CLI וב‑Python API. כלים בסיוע סוכן מכינים חתיכות לסוכן המארח של ה‑MCP לתרגום, ואז משתמשים ב‑Co-op Translator כדי לשחזר את ה‑Markdown או המחברת הסופיים.

## שלב 1: התקן והגדר את Co-op Translator

התקן את Co-op Translator בסביבת ה‑Python שבה ישתמש לקוח ה‑MCP שלך:

```bash
pip install co-op-translator
```

להמשך פיתוח מקומי מהמאגר הזה, התקן את החבילה במצב ניתן לעריכה:

```bash
pip install -e .
```

בחר את מצב התרגום שבו ישתמש לקוח ה‑MCP שלך:

| מצב | מתאים ל־ | אישורים |
| --- | --- | --- |
| מבוסס ספק | Co-op Translator קורא ל־`translate_markdown_content`, `translate_notebook_content`, `translate_image_content` או `run_translation`. | התרגום דורש Azure OpenAI, OpenAI או Anthropic. תרגום תמונות דורש גם Azure AI Vision. |
| בסיוע סוכן | סוכן המארח של MCP מתרגם את החתיכות המוחזרות על‑ידי `start_markdown_agent_translation` או `start_notebook_agent_translation`. | אין צורך באישורי ספק LLM של Co-op Translator עבור חתיכות Markdown או מחברת. תרגום תמונות אינו נתמך עדיין במצב בסיוע סוכן. |

אם אתם מתחילים בתרגום Markdown או מחברת בתוך סוכן כמו Codex או Claude Code, התחילו במצב בסיוע סוכן. השתמשו במצב מבוסס ספק כאשר אתם רוצים ש‑Co-op Translator עצמו יקרא לספקים שהגדרתם, כאשר אתם מתרגמים תמונות, או כשאתם מריצים תרגום ברמת המאגר בדומה ל‑CLI.

הגדר ספק אחד עבור זרימות עבודה מבוססות ספק:

```bash
# אז'ור OpenAI
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# או OpenAI
OPENAI_API_KEY="..."
OPENAI_CHAT_MODEL_ID="gpt-4o"

# או Anthropic
ANTHROPIC_API_KEY="..."
ANTHROPIC_MODEL="claude-..."
```

תרגום תמונות במצב מבוסס ספק מצריך בנוסף:

```bash
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

!!! note
    מצב בסיוע סוכן מכסה כרגע Markdown ותאי Markdown במחברות. תרגום תמונות עדיין משתמש בצינור תמונות מבוסס‑ספק ודורש Azure AI Vision עבור OCR ורינדור המודע לפריסה.

## שלב 2: הגדר את לקוח ה‑MCP שלך

להגדרת `stdio` המקומית הרגילה, הוסף את Co-op Translator לתצורת לקוח ה‑MCP שלך. הלקוח יפעיל ויסגור את התהליך אוטומטית.

תצורת חבילה מותקנת:

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

תצורת source checkout ב‑Windows:

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

תצורת source checkout ב‑macOS או Linux:

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

אחרי שינוי תצורת לקוח ה‑MCP, אתחל מחדש או טען מחדש את הלקוח כדי שיוכל לגלות את השרת החדש.

## שלב 3: אמת את השרת בלקוח

בקש מהלקוח ה‑MCP לרשום את הכלים הזמינים, או קרא תחילה לאחד העזרים לקריאה בלבד:

```json
{
  "tool": "get_api_overview",
  "arguments": {}
}
```

בדיקות ראשוניות מועילות:

| כלי | מה לבדוק |
| --- | --- |
| `get_api_overview` | מאשר שהשרת נגיש ומציג את זרימות העבודה הזמינות. |
| `list_supported_languages` | מאשר שניתן לטעון את נתוני השפות המצורפים. |
| `get_configuration_status` | מאשר זמינות ספקי LLM ו‑Vision מבלי לחשוף ערכי סוד. |

## שלב 4: בחר זרימת עבודה

### תרגום קבצים או מסמכים בודדים

השתמש בכלי תוכן מבוססי‑ספק כאשר ללקוח ה‑MCP כבר יש תוכן מסמך או נתיב לתמונה ו‑Co-op Translator אמור לקרוא לספקי התרגום שהוגדרו.

עבור Markdown:

1. קרא ל‑`translate_markdown_content` עם `document`, `language_code` ובאופן אופציונלי `source_path`.
2. אם התוצאה המתורגמת תישמר בתבנית פלט של Co-op Translator, קרא ל‑`rewrite_markdown_paths`.
3. תן ללקוח לכתוב או להחזיר את ה־`content` הסופי.

עבור מחברות:

1. קרא ל‑`translate_notebook_content` עם JSON של המחברת ו‑`language_code`.
2. קרא ל‑`rewrite_notebook_paths` אם יש צורך להתאים קישורי המחברת המתורגמת עבור נתיב יעד.
3. כתוב או החזר את ה‑JSON הסופי של המחברת.

עבור תמונות:

1. קרא ל‑`translate_image_content` עם `image_path`, `language_code`, ובאופן אופציונלי `root_dir` או `fast_mode`.
2. קרא את ה‑`data_base64` ו‑`mime_type` המוחזרים.
3. אם מסופק `output_path`, התמונה המתורגמת נשמרת גם לנתיב זה.

כלי התוכן אינם מבצעים גילוי פרויקט, עדכוני מטא‑דטה, הצהרות או שכתוב נתיבים אוטומטי. אם ברצונך שסוכן המארח יתרגם חתיכות Markdown או מחברת ללא אישורי ספק LLM של Co-op Translator, השתמש בזרימת העבודה בסיוע סוכן למטה.

### תרגום עם מודל הסוכן המארח

השתמש בכלים בסיוע סוכן כאשר אתה רוצה שסוכן המארח של MCP, כגון עוזר קידוד, יפיק את הטקסט המתורגם במקום לקנפג ספק LLM עבור Co-op Translator.

בלקוח MCP מבוסס צ'אט, בדרך כלל אינך צריך לכתוב את JSON של הכלים בעצמך. בקש מהסוכן להשתמש בזרימת העבודה בסיוע סוכן:

```text
Translate this Markdown file to Korean with Co-op Translator MCP.
Use agent-assisted mode: call start_markdown_agent_translation, translate the returned chunks with your own model, then call finish_markdown_agent_translation.
Keep Markdown formatting, code blocks, and links intact.
```

עבור מחברות, השתמש באותו דפוס:

```text
Translate this notebook to Korean with Co-op Translator MCP.
Use start_notebook_agent_translation, translate the returned Markdown-cell chunks with your own model, then call finish_notebook_agent_translation.
Preserve code cells, outputs, and notebook metadata.
```

אם לקוח ה‑MCP שלך תומך בהנחיות שרת (server prompts), השתמש ב‑`agent_assisted_markdown_translation_prompt` כדי ש־הלקוח יטען את אותן הוראות זרימת עבודה.

עבור Markdown:

1. קרא ל‑`start_markdown_agent_translation` עם `document`, `language_code`, ובאופן אופציונלי `source_path`.
2. תרגם כל חתיכה מוחזרת בסוכן המארח על‑ידי ביצוע הוראות ה‑`prompt` של החתיכה.
3. קרא ל‑`finish_markdown_agent_translation` עם ה‑`job` המקורי והחתיכות המתורגמות באמצעות `chunk_id` ו־`translated_text`.
4. אם התוכן ייכתב לנתיב יעד מתורגם, קרא ל‑`rewrite_markdown_paths`.

עבור מחברות:

1. קרא ל‑`start_notebook_agent_translation` עם JSON של המחברת ו‑`language_code`.
2. תרגם כל חתיכה מוחזרת בסוכן המארח.
3. קרא ל‑`finish_notebook_agent_translation` עם ה‑`job` המקורי והחתיכות המתורגמות.
4. קרא ל‑`rewrite_notebook_paths` אם קישורי המחברת המתורגמים צריכים התאמה לנתיב יעד.

כלים בסיוע סוכן אינם קוראים לספק ה‑LLM המוגדר מתוך Co-op Translator. סוכן המארח אחראי לתרגום החתיכות המוחזרות. Co-op Translator מטפל בהפצלת Markdown לחתיכות, בשימור placeholders, בשחזור ה‑frontmatter, בהחלפת תאים במחברת, ובנירמול לאחר התרגום.

### תרגום מאגר שלם

השתמש ב‑`run_translation` כאשר המשתמש רוצה ש‑Co-op Translator יתנהג כמו ה‑CLI של `translate`.

תרגום מאגר ברירת המחדל הוא `dry_run=true` כך שסוכן יכול לבדוק היקף לפני שינויי קבצים:

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "dry_run": true
}
```

תוצאת `run_translation` כוללת מערך `events` עם אירועי
`co-op.translation.event.v1` של התקדמות. לקוחות MCP צריכים להשתמש בשדות כגון
`type`, `stage_key`, `completed`, `total`, ו‑`current_path` במקום
לנתח טקסט שנתפס בקונסולה. העבר את `json_events_path` כדי גם לכתוב את האירועים האלה
לקובץ NDJSON.

כדי לאפשר כתיבה, המתקשר חייב להגדיר הן `dry_run=false` והן `confirm_write=true`:

```json
{
  "language_codes": "ko",
  "root_dir": ".",
  "markdown": true,
  "dry_run": false,
  "confirm_write": true
}
```

`translate_project` נחשף ככינוי תאימות ל־`run_translation`.

### סקירת הפלט המתורגם

השתמש ב־`run_review` לבדיקות דטרמיניסטיות שאינן דורשות אישורי LLM או Vision:

!!! note "Beta"
    MCP מציג את ה‑API הבטא `run_review`. הוא בטוח לזרימות עבודה של סקירה לקריאה בלבד, אך בדיקות הסקירה וסכמות הבעיות עשויות להתפתח.

```json
{
  "language_codes": "ko ja",
  "root_dir": ".",
  "markdown": true,
  "notebook": true
}
```

התוצאה כוללת פלט טקסט שנלכד וסיכום סקירה מובנה כאשר זמין.

## הרצות שרת ידניות

ההרצות הידניות מיועדות בעיקר לניפוי שגיאות או לטרנְספורטים שמתנהגים כשרתים ארוכי‑טווח.

ניפוי שגיאות של שרת ה‑stdio ברירת המחדל:

```bash
co-op-translator-mcp
```

הרצה מתוך source checkout:

```bash
python -m co_op_translator.mcp.server
```

הפעל שרת HTTP או SSE ארוך‑טווח:

```bash
co-op-translator-mcp --transport streamable-http
co-op-translator-mcp --transport sse
```

לאינטגרציות של עורך מקומי וסוכן, העדיפו את תצורת `stdio` שמנוהלת על‑ידי הלקוח בשלב 2.

## כלים

| כלי | מטרה | כותב קבצים |
| --- | --- | --- |
| `translate_markdown_content` | לתרגם מחרוזת Markdown. | לא |
| `translate_notebook_content` | לתרגם תאי Markdown ב‑JSON של המחברת. | לא |
| `translate_image_content` | לתרגם טקסט בתמונה אחת ולהחזיר נתוני תמונה ב‑base64. | אופציונלי, רק כאשר מסופק `output_path` |
| `start_markdown_agent_translation` | להכין חתיכות Markdown לסוכן המארח כדי לתרגם ללא אישורי ספק LLM של Co-op Translator. | לא |
| `finish_markdown_agent_translation` | לשחזר Markdown מתוך חתיכות שתורגמו על‑ידי סוכן המארח. | לא |
| `start_notebook_agent_translation` | להכין חתיכות תאי Markdown במחברת לסוכן המארח לתרגום. | לא |
| `finish_notebook_agent_translation` | לשחזר JSON של המחברת מתוך חתיכות שתורגמו על‑ידי סוכן המארח. | לא |
| `rewrite_markdown_paths` | לשכתב נתיבים בגוף ה‑Markdown וב‑frontmatter עבור יעד מתורגם. | לא |
| `rewrite_notebook_paths` | לשכתב נתיבים בתוך תאי Markdown במחברת. | לא |
| `run_translation` | להריץ תרגום ברמת הפרויקט בדומה ל‑CLI. | כן כאשר `dry_run=false` ו־`confirm_write=true` |
| `translate_project` | כינוי תאימות ל־`run_translation`. | כן כאשר `dry_run=false` ו־`confirm_write=true` |
| `run_review` | להריץ בדיקות סקירה דטרמיניסטיות. | לא |
| `get_configuration_status` | להציג את ספקי LLM ו‑Vision המוגדרים מבלי לחשוף סודות. | לא |
| `list_supported_languages` | לרשום קודי שפות יעד נתמכות. | לא |
| `get_api_overview` | לתאר את זרימות העבודה והכלים הזמינים ב‑MCP. | לא |

## משאבים

| URI של משאב | מטרה |
| --- | --- |
| `co-op://api` | סקירת JSON של זרימות העבודה והכלים. |
| `co-op://supported-languages` | רשימת JSON של קודי השפות הנתמכות. |
| `co-op://configuration` | סיכום JSON של זמינות ספקים ללא סודות. |

## פרומפטים

| פרומפט | מטרה |
| --- | --- |
| `translate_markdown_document_prompt` | להנחות לקוח MCP בתרגום תוכן וכן בשכתוב נתיבים אופציונלי. |
| `agent_assisted_markdown_translation_prompt` | להנחות לקוח MCP בתרגום Markdown באמצעות סוכן מארח ללא אישורי ספק LLM של Co-op Translator. |
| `translate_repository_prompt` | להנחות לקוח MCP בתרגום מאגר כשהוא מתחיל ב‑dry‑run. |

## דוגמאות להעתקה והדבקה

תרגם תוכן Markdown:

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

שכתב קישורי Markdown מתורגמים:

```json
{
  "tool": "rewrite_markdown_paths",
  "arguments": {
    "content": "[Setup](../setup.md)\n\n![Hero](images/hero.png)",
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

תרגם Markdown עם מודל הסוכן המארח:

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

אחרי שסוכן המארח מתרגם כל חתיכה מוחזרת, סיים את העבודה עם אובייקט ה‑`job` המלא המוחזר על‑ידי `start_markdown_agent_translation`:

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
| The MCP client cannot find `co-op-translator-mcp`. | השתמש בנתיב המפעיל המלא של Python ובתצורת source checkout `["-m", "co_op_translator.mcp.server"]`. |
| השרת מופיע אך התרגום נכשל. | קרא ל־`get_configuration_status` ואשר שמצוי ספק LLM. |
| אתה רוצה תרגום של Markdown או של מחברת ללא אישורי ספק. | השתמש ב־`start_markdown_agent_translation` / `finish_markdown_agent_translation` או המקבילים למחברת כדי שסוכן המארח יתרגם את החתיכות. |
| Image translation fails. | אשר שמשתני Azure AI Vision מוגדרים וקרא ל־`get_configuration_status`. |
| תרגום המאגר אינו כותב קבצים. | הגדר `dry_run=false` ו־`confirm_write=true` רק לאחר אישור מפורש של המשתמש. |
| שינויים בקונפיגורציית הלקוח אינם מופיעים. | אתחל מחדש או טען מחדש את לקוח ה‑MCP. |

## הערות בטיחות

- קריאות לכלי MCP נשלטות על‑ידי היישום המארח, לכן תרגום מאגר הוא dry‑run כברירת מחדל.
- תרגום מאגר מלא יכול ליצור, לעדכן או להסיר קבצים רבים. דרוש אישור מפורש של המשתמש לפני הגדרת `confirm_write=true`.
- כלי מצב התצורה אף פעם לא מחזיר מפתחות API, נקודות קצה או ערכי סוד אחרים.
- תרגום תמונות מחזיר נתוני תמונה ב‑base64. תמונות גדולות יכולות ליצור תגובות כלי גדולות.
- כלים בסיוע סוכן מחזירים חתיכות מקור ופרומפטים לסוכן המארח של MCP. השתמש בהם רק עם תוכן שהמשתמש נוח לשלוח למודל הסוכן המארח.