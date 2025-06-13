<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-06-12T18:27:54+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "he"
}
-->
# צור את הקובץ *.env* בתיקיית השורש

במדריך זה נלווה אותך בתהליך הגדרת משתני הסביבה לשירותי Azure באמצעות קובץ *.env*. משתני סביבה מאפשרים לך לנהל בצורה מאובטחת פרטי גישה רגישים, כמו מפתחות API, מבלי לקודד אותם ישירות בקוד שלך.

> [!IMPORTANT]
> - יש להגדיר רק שירות מודל שפה אחד (Azure OpenAI או OpenAI). מלא את משתני הסביבה עבור השירות המועדף עליך. אם מוגדרים משתני סביבה עבור מספר מודלי שפה, המתרגם המשולב יבחר אחד מהם לפי סדר עדיפות.
> - אם משתני הסביבה של Computer Vision לא מוגדרים, המתרגם יעבור אוטומטית ל[מצב Markdown בלבד](./markdown-only-mode.md).

> [!NOTE]
> מדריך זה מתמקד בעיקר בשירותי Azure, אך ניתן לבחור כל מודל שפה נתמך מתוך [רשימת המודלים והשירותים הנתמכים](../README.md#-supported-models-and-services).

## צור את הקובץ *.env*

בתיקיית השורש של הפרויקט שלך, צור קובץ בשם *.env*. קובץ זה יאחסן את כל משתני הסביבה שלך בפורמט פשוט.

> [!WARNING]
> אל תבצע commit לקובץ *.env* במערכות בקרת גרסאות כמו Git. הוסף את *.env* לקובץ .gitignore שלך כדי למנוע commits בטעות.

1. עבור לתיקיית השורש של הפרויקט שלך.

1. צור קובץ *.env* בתיקיית השורש של הפרויקט שלך.

1. פתח את קובץ *.env* והדבק את התבנית הבאה:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> אם ברצונך למצוא את מפתחות ה-API והנקודות הקצה שלך, תוכל לעיין ב-[set-up-azure-ai.md](../set-up-azure-ai.md).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. עבור מידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.