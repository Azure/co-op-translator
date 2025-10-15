<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:30:08+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "nl"
}
-->
# Microsoft Co-op Translator Probleemoplossingsgids

## Overzicht
De Microsoft Co-Op Translator is een krachtig hulpmiddel om Markdown-documenten naadloos te vertalen. Deze gids helpt je bij het oplossen van veelvoorkomende problemen die je kunt tegenkomen bij het gebruik van de tool.

## Veelvoorkomende Problemen en Oplossingen

### 1. Markdown Tag Probleem
**Probleem:** Het vertaalde Markdown-document bevat een `markdown` tag bovenaan, wat zorgt voor weergaveproblemen.

**Oplossing:** Verwijder simpelweg de `markdown` tag bovenaan het bestand. Hierdoor wordt het Markdown-bestand correct weergegeven.

**Stappen:**
1. Open het vertaalde Markdown (`.md`) bestand.
2. Zoek de `markdown` tag bovenaan het document.
3. Verwijder de `markdown` tag.
4. Sla de wijzigingen op.
5. Open het bestand opnieuw om te controleren of het correct wordt weergegeven.

### 2. URL Probleem bij Ingesloten Afbeeldingen
**Probleem:** De URL’s van ingesloten afbeeldingen komen niet overeen met de taalinstelling, waardoor afbeeldingen niet correct of helemaal niet worden weergegeven.

**Oplossing:** Controleer de URL van ingesloten afbeeldingen en zorg dat deze overeenkomt met de taalinstelling. Alle afbeeldingen staan in de map `translated_images` en elke afbeelding heeft een taalcode in de bestandsnaam.

**Stappen:**
1. Open het vertaalde Markdown-document.
2. Zoek de ingesloten afbeeldingen en hun URL’s.
3. Controleer of de taalcode in de bestandsnaam overeenkomt met de taal van het document.
4. Pas de URL’s aan indien nodig.
5. Sla de wijzigingen op en open het document opnieuw om te controleren of de afbeeldingen correct worden weergegeven.

### 3. Nauwkeurigheid van Vertaling
**Probleem:** De vertaalde inhoud is niet accuraat of moet verder worden bewerkt.

**Oplossing:** Bekijk het vertaalde document en breng de nodige wijzigingen aan om de nauwkeurigheid en leesbaarheid te verbeteren.

**Stappen:**
1. Open het vertaalde document.
2. Bekijk de inhoud zorgvuldig.
3. Breng de nodige wijzigingen aan om de vertaling te verbeteren.
4. Sla de wijzigingen op.

## 4. Permission Error Redacted of 404

Als afbeeldingen of tekst niet naar de juiste taal worden vertaald en je krijgt een 401-foutmelding in debugmodus (-d), is er meestal sprake van een authenticatieprobleem—de sleutel is ongeldig, verlopen, of niet gekoppeld aan de regio van de endpoint.

Voer co-op translator uit met de [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) om meer inzicht te krijgen in de oorzaak.

- **Foutmelding**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Mogelijke oorzaken**:
  - De subscription key is verwijderd of onjuist in het verzoek.
  - De AI Services Key of Subscription Key hoort bij een ander Azure-resource (zoals Translator of OpenAI) in plaats van een **Azure AI Vision** resource.

 **Resource Type**
  - Ga naar de [Azure Portal](https://portal.azure.com) of [Azure AI Foundry](https://ai.azure.com) en controleer of het resource van het type `Azure AI services` → `Vision` is.
  - Controleer de sleutels en zorg dat je de juiste sleutel gebruikt.

## 5. Configuratiefouten (Nieuwe Foutafhandeling)

Met het nieuwe selectieve vertaalsysteem geeft Co-op Translator nu duidelijke foutmeldingen als vereiste services niet zijn geconfigureerd.

### 5.1. Azure AI Service Niet Geconfigureerd voor Afbeeldingsvertaling

**Probleem:** Je hebt afbeeldingsvertaling aangevraagd (`-img` vlag) maar Azure AI Service is niet goed geconfigureerd.

**Foutmelding:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Oplossing:**
1. **Optie 1**: Configureer Azure AI Service
   - Voeg `AZURE_AI_SERVICE_API_KEY` toe aan je `.env` bestand
   - Voeg `AZURE_AI_SERVICE_ENDPOINT` toe aan je `.env` bestand
   - Controleer of de service bereikbaar is

2. **Optie 2**: Verwijder de aanvraag voor afbeeldingsvertaling
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Ontbrekende Vereiste Configuratie

**Probleem:** Essentiële LLM-configuratie ontbreekt.

**Foutmelding:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Oplossing:**
1. Controleer of je `.env` bestand ten minste één van de volgende LLM-configuraties bevat:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` en `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Je hebt óf Azure OpenAI óf OpenAI nodig, niet beide.

### 5.3. Verwarring bij Selectieve Vertaling

**Probleem:** Er zijn geen bestanden vertaald, terwijl het commando wel succesvol was.

**Mogelijke oorzaken:**
- Verkeerde bestandstype-vlaggen (`-md`, `-img`, `-nb`)
- Geen overeenkomende bestanden in het project
- Onjuiste mapstructuur

**Oplossing:**
1. **Gebruik debugmodus** om te zien wat er gebeurt:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Controleer bestandstypen** in je project:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Controleer vlagcombinaties**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migratie vanaf het Oude Systeem

### 6.1. Markdown-Only Mode Vervallen

**Probleem:** Commando’s die vertrouwden op automatische markdown-only fallback werken niet meer zoals verwacht.

**Oude gedrag:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Nieuwe gedrag:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Oplossing:**
- **Wees expliciet** over wat je wilt vertalen:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Onverwacht Linkgedrag

**Probleem:** Links in vertaalde bestanden verwijzen naar onverwachte locaties.

**Oorzaak:** Dynamische linkverwerking verandert afhankelijk van de gekozen bestandstypen.

**Oplossing:**
1. **Begrijp het nieuwe linkgedrag**:
   - `-nb` meegegeven: Notebook-links verwijzen naar vertaalde versies
   - `-nb` niet meegegeven: Notebook-links verwijzen naar originele bestanden
   - `-img` meegegeven: Afbeeldingslinks verwijzen naar vertaalde versies
   - `-img` niet meegegeven: Afbeeldingslinks verwijzen naar originele bestanden

2. **Kies de juiste combinatie** voor jouw situatie:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action uitgevoerd maar er is geen Pull Request (PR) aangemaakt

**Symptoom:** De workflow logs voor `peter-evans/create-pull-request` tonen:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Waarschijnlijke oorzaken:**
- **Geen wijzigingen gedetecteerd:** De vertaalstap heeft geen verschillen opgeleverd (repo is al up-to-date).
- **Genegeerde outputs:** `.gitignore` sluit bestanden uit die je wilt committen (bijv. `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths komt niet overeen:** De paden die aan de actie zijn meegegeven komen niet overeen met de daadwerkelijke outputlocaties.
- **Workflow logica/voorwaarden:** De vertaalstap is vroeg gestopt of heeft naar onverwachte mappen geschreven.

**Hoe te controleren / oplossen:**
1. **Controleer of outputs bestaan:** Kijk na het vertalen of er nieuwe/aangepaste bestanden zijn in `translations/` en/of `translated_images/`.
   - Als je notebooks vertaalt, controleer of `.ipynb` bestanden daadwerkelijk zijn geschreven onder `translations/<lang>/...`.
2. **Bekijk `.gitignore`:** Negeer geen gegenereerde outputs. Zorg dat je NIET negeert:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (als je notebooks vertaalt)
3. **Zorg dat add-paths overeenkomt met outputs:** Gebruik een waarde op meerdere regels en neem beide mappen op indien van toepassing:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Forceer een PR voor debugging:** Sta tijdelijk lege commits toe om te controleren of alles goed is aangesloten:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Voer uit met debug:** Voeg `-d` toe aan het vertaalcommando om te zien welke bestanden zijn gevonden en geschreven.
6. **Rechten (GITHUB_TOKEN):** Zorg dat de workflow schrijfrechten heeft om commits en PR’s aan te maken:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Snelle Debug Checklist

Bij het oplossen van vertaalproblemen:

1. **Gebruik debugmodus**: Voeg de `-d` vlag toe voor gedetailleerde logs
2. **Controleer je vlaggen**: Zorg dat `-md`, `-img`, `-nb` overeenkomen met je bedoeling
3. **Controleer configuratie**: Kijk of je `.env` bestand de vereiste sleutels bevat
4. **Test stapsgewijs**: Begin met alleen `-md`, voeg daarna andere typen toe
5. **Controleer bestandsstructuur**: Zorg dat bronbestanden bestaan en toegankelijk zijn

Voor meer gedetailleerde informatie over beschikbare commando’s en vlaggen, zie de [Command Reference](./command-reference.md).

---

**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.