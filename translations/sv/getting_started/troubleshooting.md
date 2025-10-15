<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:19:33+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "sv"
}
-->
# Microsoft Co-op Translator Felsökningsguide

## Översikt
Microsoft Co-Op Translator är ett kraftfullt verktyg för att översätta Markdown-dokument smidigt. Den här guiden hjälper dig att lösa vanliga problem som kan uppstå när du använder verktyget.

## Vanliga problem och lösningar

### 1. Markdown-taggsproblem
**Problem:** Det översatta Markdown-dokumentet innehåller en `markdown`-tagg högst upp, vilket orsakar visningsproblem.

**Lösning:** Ta bort `markdown`-taggen högst upp i filen. Då kommer Markdown-filen att visas korrekt.

**Steg:**
1. Öppna den översatta Markdown-filen (`.md`).
2. Leta upp `markdown`-taggen högst upp i dokumentet.
3. Ta bort `markdown`-taggen.
4. Spara filen.
5. Öppna filen igen för att kontrollera att den visas korrekt.

### 2. Problem med bild-URL:er
**Problem:** URL:erna till inbäddade bilder matchar inte språkversionen, vilket leder till felaktiga eller saknade bilder.

**Lösning:** Kontrollera URL:erna till inbäddade bilder och se till att de matchar språkversionen. Alla bilder finns i mappen `translated_images` och varje bild har en språkmarkering i filnamnet.

**Steg:**
1. Öppna det översatta Markdown-dokumentet.
2. Identifiera de inbäddade bilderna och deras URL:er.
3. Kontrollera att språkmarkeringen i bildens filnamn stämmer med dokumentets språk.
4. Uppdatera URL:erna vid behov.
5. Spara och öppna dokumentet igen för att bekräfta att bilderna visas korrekt.

### 3. Översättningskvalitet
**Problem:** Den översatta texten är inte korrekt eller behöver redigeras.

**Lösning:** Gå igenom det översatta dokumentet och gör nödvändiga ändringar för att förbättra kvaliteten och läsbarheten.

**Steg:**
1. Öppna det översatta dokumentet.
2. Läs igenom innehållet noggrant.
3. Gör nödvändiga ändringar för att förbättra översättningen.
4. Spara filen.

## 4. Behörighetsfel Redacted eller 404

Om bilder eller text inte översätts till rätt språk och du får 401-fel i -d debug-läge är det ett klassiskt autentiseringsproblem—antingen är nyckeln ogiltig, har gått ut, eller är inte kopplad till rätt region.

Kör co-op translator med [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) för att få mer information om grundorsaken.

- **Felmeddelande**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Möjliga orsaker**:
  - Prenumerationsnyckeln var borttagen eller felaktig i begäran.
  - AI Services Key eller Subscription Key kan tillhöra en annan Azure-resurs (t.ex. Translator eller OpenAI) istället för en **Azure AI Vision**-resurs.

 **Resurstyp**
  - Gå till [Azure Portal](https://portal.azure.com) eller [Azure AI Foundry](https://ai.azure.com) och kontrollera att resursen är av typen `Azure AI services` → `Vision`.
  - Kontrollera nycklarna och se till att rätt nyckel används.

## 5. Konfigurationsfel (Ny felhantering)

Med det nya selektiva översättningssystemet ger Co-op Translator nu tydliga felmeddelanden när nödvändiga tjänster inte är konfigurerade.

### 5.1. Azure AI Service ej konfigurerad för bildöversättning

**Problem:** Du har begärt bildöversättning (`-img` flagga) men Azure AI Service är inte korrekt konfigurerad.

**Felmeddelande:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Lösning:**
1. **Alternativ 1**: Konfigurera Azure AI Service
   - Lägg till `AZURE_AI_SERVICE_API_KEY` i din `.env`-fil
   - Lägg till `AZURE_AI_SERVICE_ENDPOINT` i din `.env`-fil
   - Kontrollera att tjänsten är tillgänglig

2. **Alternativ 2**: Ta bort begäran om bildöversättning
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Saknad nödvändig konfiguration

**Problem:** Viktig LLM-konfiguration saknas.

**Felmeddelande:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Lösning:**
1. Kontrollera att din `.env`-fil har minst en av följande LLM-konfigurationer:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` och `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Du behöver antingen Azure OpenAI ELLER OpenAI konfigurerad, inte båda.

### 5.3. Förvirring kring selektiv översättning

**Problem:** Inga filer översattes trots att kommandot lyckades.

**Möjliga orsaker:**
- Felaktiga filtypsflaggor (`-md`, `-img`, `-nb`)
- Inga matchande filer i projektet
- Felaktig mappstruktur

**Lösning:**
1. **Använd debug-läge** för att se vad som händer:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Kontrollera filtyper** i ditt projekt:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Verifiera flaggkombinationer**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migrering från gamla systemet

### 6.1. Markdown-endast-läge borttaget

**Problem:** Kommandon som tidigare automatiskt översatte endast markdown fungerar inte längre som förväntat.

**Tidigare beteende:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Nytt beteende:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Lösning:**
- **Var tydlig** med vad du vill översätta:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Oväntat länkbeteende

**Problem:** Länkar i översatta filer pekar på oväntade platser.

**Orsak:** Dynamisk länkhantering ändras beroende på valda filtyper.

**Lösning:**
1. **Förstå det nya länkbeteendet**:
   - `-nb` inkluderat: Notebook-länkar pekar på översatta versioner
   - `-nb` exkluderat: Notebook-länkar pekar på originalfiler
   - `-img` inkluderat: Bildlänkar pekar på översatta versioner
   - `-img` exkluderat: Bildlänkar pekar på originalfiler

2. **Välj rätt kombination** för ditt behov:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action kördes men ingen Pull Request (PR) skapades

**Symptom:** Loggarna för workflow `peter-evans/create-pull-request` visar:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Troliga orsaker:**
- **Inga ändringar upptäckta:** Översättningssteget gav inga skillnader (repo redan uppdaterat).
- **Ignorerade utdata:** `.gitignore` utesluter filer du vill committa (t.ex. `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths mismatch:** Sökvägarna till actionen matchar inte faktiska utdata.
- **Workflow-logik/villkor:** Översättningssteget avslutades tidigt eller skrev till oväntade mappar.

**Så här åtgärdar du / verifierar:**
1. **Bekräfta att utdata finns:** Efter översättning, kontrollera att arbetsytan har nya/ändrade filer i `translations/` och/eller `translated_images/`.
   - Om du översätter notebooks, kontrollera att `.ipynb`-filer faktiskt skrivs under `translations/<lang>/...`.
2. **Granska `.gitignore`:** Ignorera inte genererade utdata. Kontrollera att du INTE ignorerar:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (om du översätter notebooks)
3. **Säkerställ att add-paths matchar utdata:** Använd ett flerradigt värde och inkludera båda mapparna om det behövs:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Tvinga fram en PR för felsökning:** Tillåt tillfälligt tomma commits för att bekräfta att allt är rätt kopplat:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Kör med debug:** Lägg till `-d` till translate-kommandot för att visa vilka filer som hittades och skrevs.
6. **Behörigheter (GITHUB_TOKEN):** Kontrollera att workflow har skrivbehörighet för att skapa commits och PR:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Snabb felsökningschecklista

När du felsöker översättningsproblem:

1. **Använd debug-läge**: Lägg till `-d`-flagga för detaljerade loggar
2. **Kontrollera dina flaggor**: Se till att `-md`, `-img`, `-nb` stämmer med din avsikt
3. **Verifiera konfigurationen**: Kontrollera att din `.env`-fil har nödvändiga nycklar
4. **Testa stegvis**: Börja med endast `-md`, lägg sedan till andra typer
5. **Kontrollera filstrukturen**: Se till att källfiler finns och är tillgängliga

För mer information om tillgängliga kommandon och flaggor, se [Command Reference](./command-reference.md).

---

**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.