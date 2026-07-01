# הגדרת Azure AI

השתמש במדריך זה כשתרצה להגדיר את Azure OpenAI לתרגום טקסט ואת Azure AI Vision לחילוץ טקסט מתמונות.

## דרישות מוקדמות

- מנוי Azure.
- הרשאה ליצור או להשתמש במשאבי Azure AI ובהצבות מודלים.
- פרויקט ב-Azure AI Foundry או גישה שוות ערך למשאבי Azure OpenAI ו-Azure AI Vision.

## יצירת פרויקט Azure AI

1. פתח את [Azure AI Foundry](https://ai.azure.com).
2. צור או בחר פרויקט.
3. צור או בחר AI hub עבור הפרויקט.
4. פתח את סקירת הפרויקט לאחר יצירתו.

## פריסת מודל Azure OpenAI

1. בפרויקט, פתח את **Models + endpoints**.
2. בחר **Deploy model**.
3. בחר מודל GPT כגון `gpt-4o`.
4. פרוס את המודל.
5. תעד את נקודת הקצה, שם ההצבה, שם המודל, מפתח ה-API וגרסת ה-API.

!!! note
    גרסת ה-API של Azure OpenAI נפרדת מגרסת המודל המוצגת ב-Azure AI Foundry. בחר גרסת API שנתמכת להצבה שלך.

## קביעת תצורה של Azure AI Vision

תרגום תמונות משתמש ב-Azure AI Vision לחילוץ טקסט מתמונות מקור לפני שהטקסט מתורגם.

בפרויקט Azure AI שלך, מצא את המפתח ונקודת הקצה של Azure AI Services.

![מצא מידע על שירות Azure AI](../../assets/find-azure-ai-info.png)

תעד:

- נקודת הקצה של שירות Azure AI
- מפתח ה-API של שירות Azure AI

## משתני סביבה

הוסף את אישורי הגישה לקובץ `.env` שלך או לסודות ב-CI.

```bash
# Azure AI Vision, נדרש לתרגום תמונות
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

# Azure OpenAI, נדרש לתרגום טקסטים
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

Co-op Translator תומך גם בערכות אישורי גיבוי אופציונליות. שכפל ערכת ספק שלמה עם סיומות כמו `_1` או `_2`; כל המשתנים בערכת גיבוי חייבים לשתף את אותה הסיומת.

```bash
AZURE_OPENAI_API_KEY_1="..."
AZURE_OPENAI_ENDPOINT_1="https://<resource-1>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME_1="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME_1="<deployment-1>"
AZURE_OPENAI_API_VERSION_1="2024-12-01-preview"
```

## השלבים הבאים

- חזור אל [תצורה](configuration.md) כדי להגדיר משתני סביבה מקומיים או ב-CI.
- השתמש ב-[מדריך ה-CLI](cli.md) עבור פקודות תרגום.
- השתמש ב-[GitHub Actions](github-actions.md) כדי לאוטומט את בקשות המשיכה של התרגום.