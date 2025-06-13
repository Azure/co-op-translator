<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:27:26+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "sv"
}
-->
# Microsoft Co-op Translator Felsökningsguide


## Översikt
Microsoft Co-Op Translator är ett kraftfullt verktyg för att smidigt översätta Markdown-dokument. Denna guide hjälper dig att felsöka vanliga problem som kan uppstå vid användning av verktyget.

## Vanliga problem och lösningar

### 1. Problem med Markdown-taggar
**Problem:** Det översatta Markdown-dokumentet innehåller en `markdown`-tagg högst upp, vilket orsakar problem vid rendering.

**Lösning:** För att lösa detta, ta helt enkelt bort `markdown`-taggen högst upp i filen. Detta gör att Markdown-filen renderas korrekt.

**Steg:**
1. Öppna den översatta Markdown-filen (`.md`).
2. Leta upp `markdown`-taggen högst upp i dokumentet.
3. Ta bort `markdown`-taggen.
4. Spara ändringarna i filen.
5. Öppna filen igen för att säkerställa att den renderas korrekt.

### 2. Problem med URL:er för inbäddade bilder
**Problem:** URL:erna för inbäddade bilder matchar inte språkversionen, vilket leder till felaktiga eller saknade bilder.

**Lösning:** Kontrollera URL:erna för inbäddade bilder och se till att de stämmer överens med språkversionen. Alla bilder finns i `translated_images`-mappen och varje bildfil har en språkversionstagg i filnamnet.

**Steg:**
1. Öppna det översatta Markdown-dokumentet.
2. Identifiera de inbäddade bilderna och deras URL:er.
3. Kontrollera att språkversionen i bildfilens namn matchar dokumentets språk.
4. Uppdatera URL:erna vid behov.
5. Spara ändringarna och öppna dokumentet igen för att bekräfta att bilderna visas korrekt.

### 3. Översättningsnoggrannhet
**Problem:** Det översatta innehållet är inte korrekt eller behöver ytterligare redigering.

**Lösning:** Granska det översatta dokumentet och gör nödvändiga ändringar för att förbättra noggrannhet och läsbarhet.

**Steg:**
1. Öppna det översatta dokumentet.
2. Gå noggrant igenom innehållet.
3. Gör nödvändiga ändringar för att förbättra översättningens noggrannhet.
4. Spara ändringarna.

### 4. Problem med filformattering
**Problem:** Formateringen i det översatta dokumentet är felaktig. Detta kan förekomma i tabeller, där den extra ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` kan lösa tabellproblemen.

**Steg:**
1. Öppna det översatta dokumentet.
2. Jämför det med originaldokumentet för att identifiera formateringsproblem.
3. Justera formateringen så att den matchar originaldokumentet.
4. Spara ändringarna.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.