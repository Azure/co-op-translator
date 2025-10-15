<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:24:40+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "no"
}
-->
# Microsoft Co-op Translator Feilsøkingsguide

## Oversikt
Microsoft Co-Op Translator er et kraftig verktøy for å oversette Markdown-dokumenter sømløst. Denne guiden hjelper deg med å løse vanlige problemer du kan møte når du bruker verktøyet.

## Vanlige problemer og løsninger

### 1. Markdown-tag-problem
**Problem:** Det oversatte Markdown-dokumentet inneholder en `markdown`-tag øverst, noe som gir visningsproblemer.

**Løsning:** For å fikse dette, slett bare `markdown`-taggen øverst i filen. Da vil Markdown-filen vises riktig.

**Fremgangsmåte:**
1. Åpne den oversatte Markdown (`.md`)-filen.
2. Finn `markdown`-taggen øverst i dokumentet.
3. Slett `markdown`-taggen.
4. Lagre endringene i filen.
5. Åpne filen på nytt for å sjekke at den vises riktig.

### 2. URL-problem med innebygde bilder
**Problem:** URL-ene til innebygde bilder samsvarer ikke med språkinnstillingen, noe som gir feil eller manglende bilder.

**Løsning:** Sjekk URL-en til innebygde bilder og sørg for at de samsvarer med språkinnstillingen. Alle bilder ligger i mappen `translated_images`, og hvert bilde har en språk-tag i filnavnet.

**Fremgangsmåte:**
1. Åpne det oversatte Markdown-dokumentet.
2. Finn de innebygde bildene og deres URL-er.
3. Sjekk at språk-taggen i bildefilnavnet samsvarer med dokumentets språk.
4. Oppdater URL-ene om nødvendig.
5. Lagre endringene og åpne dokumentet på nytt for å sjekke at bildene vises riktig.

### 3. Oversettelsesnøyaktighet
**Problem:** Det oversatte innholdet er ikke nøyaktig eller trenger ytterligere redigering.

**Løsning:** Gå gjennom det oversatte dokumentet og gjør nødvendige endringer for å forbedre nøyaktighet og lesbarhet.

**Fremgangsmåte:**
1. Åpne det oversatte dokumentet.
2. Les gjennom innholdet nøye.
3. Gjør nødvendige endringer for å forbedre oversettelsen.
4. Lagre endringene.

## 4. Tillatelsesfeil Redacted eller 404

Hvis bilder eller tekst ikke oversettes til riktig språk, og du får 401-feil når du kjører i -d debug-modus, er dette en klassisk autentiseringsfeil—enten er nøkkelen ugyldig, utløpt, eller ikke knyttet til riktig region for endepunktet.

Kjør co-op translator med [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) for å få mer innsikt i årsaken.

- **Feilmelding**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Mulige årsaker**:
  - Abonnementsnøkkelen ble redigert bort eller er feil i forespørselen.
  - AI Services Key eller Subscription Key tilhører en annen Azure-ressurs (som Translator eller OpenAI) i stedet for en **Azure AI Vision**-ressurs.

 **Ressurstype**
  - Gå til [Azure Portal](https://portal.azure.com) eller [Azure AI Foundry](https://ai.azure.com) og sjekk at ressursen er av typen `Azure AI services` → `Vision`.
  - Sjekk nøklene og sørg for at riktig nøkkel brukes.

## 5. Konfigurasjonsfeil (Ny feilhåndtering)

Med det nye systemet for selektiv oversettelse gir Co-op Translator nå tydelige feilmeldinger når nødvendige tjenester ikke er konfigurert.

### 5.1. Azure AI Service ikke konfigurert for bildeoversettelse

**Problem:** Du har bedt om bildeoversettelse (`-img` flagg), men Azure AI Service er ikke riktig konfigurert.

**Feilmelding:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Løsning:**
1. **Alternativ 1**: Konfigurer Azure AI Service
   - Legg til `AZURE_AI_SERVICE_API_KEY` i `.env`-filen din
   - Legg til `AZURE_AI_SERVICE_ENDPOINT` i `.env`-filen din
   - Sjekk at tjenesten er tilgjengelig

2. **Alternativ 2**: Fjern forespørsel om bildeoversettelse
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Manglende nødvendig konfigurasjon

**Problem:** Viktig LLM-konfigurasjon mangler.

**Feilmelding:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Løsning:**
1. Sjekk at `.env`-filen din har minst én av følgende LLM-konfigurasjoner:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` og `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Du trenger enten Azure OpenAI ELLER OpenAI konfigurert, ikke begge.

### 5.3. Forvirring rundt selektiv oversettelse

**Problem:** Ingen filer ble oversatt selv om kommandoen fullførte.

**Mulige årsaker:**
- Feil filtype-flagg (`-md`, `-img`, `-nb`)
- Ingen matchende filer i prosjektet
- Feil mappestruktur

**Løsning:**
1. **Bruk debug-modus** for å se hva som skjer:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Sjekk filtyper** i prosjektet ditt:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Sjekk flaggkombinasjoner**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migrering fra gammelt system

### 6.1. Markdown-only-modus avviklet

**Problem:** Kommandoer som tidligere automatisk falt tilbake til kun markdown fungerer ikke lenger som forventet.

**Gammel oppførsel:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Ny oppførsel:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Løsning:**
- **Vær tydelig** på hva du vil oversette:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Uventet lenkeoppførsel

**Problem:** Lenker i oversatte filer peker til uventede steder.

**Årsak:** Dynamisk lenkehåndtering endres basert på valgte filtyper.

**Løsning:**
1. **Forstå den nye lenkeoppførselen**:
   - `-nb` inkludert: Notebook-lenker peker til oversatte versjoner
   - `-nb` utelatt: Notebook-lenker peker til originalfiler
   - `-img` inkludert: Bildelenker peker til oversatte versjoner
   - `-img` utelatt: Bildelenker peker til originalfiler

2. **Velg riktig kombinasjon** for ditt behov:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action kjørte, men ingen Pull Request (PR) ble opprettet

**Symptom:** Workflow-loggene for `peter-evans/create-pull-request` viser:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Sannsynlige årsaker:**
- **Ingen endringer oppdaget:** Oversettelsestrinnet ga ingen forskjeller (repo allerede oppdatert).
- **Ignorerte utdata:** `.gitignore` ekskluderer filer du forventer å legge til (f.eks. `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths mismatch:** Stiene som er oppgitt til action stemmer ikke med faktiske utdata.
- **Workflow-logikk/betingelser:** Oversettelsestrinnet avsluttet tidlig eller skrev til uventede mapper.

**Slik fikser du / sjekker:**
1. **Bekreft at utdata finnes:** Etter oversettelse, sjekk at arbeidsområdet har nye/endrede filer i `translations/` og/eller `translated_images/`.
   - Hvis du oversetter notebooks, sjekk at `.ipynb`-filer faktisk er skrevet under `translations/<lang>/...`.
2. **Se over `.gitignore`:** Ikke ignorer genererte utdata. Sørg for at du IKKE ignorerer:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (hvis du oversetter notebooks)
3. **Sjekk at add-paths stemmer med utdata:** Bruk en multilinje-verdi og inkluder begge mapper om nødvendig:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Tving frem en PR for feilsøking:** Tillat midlertidig tomme commits for å sjekke at alt er koblet riktig:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Kjør med debug:** Legg til `-d` i oversettelseskommandoen for å vise hvilke filer som ble funnet og skrevet.
6. **Tillatelser (GITHUB_TOKEN):** Sjekk at workflow har skrivetilgang for å opprette commits og PR-er:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Rask feilsøkingsliste

Når du feilsøker oversettelsesproblemer:

1. **Bruk debug-modus**: Legg til `-d`-flagget for detaljerte logger
2. **Sjekk flaggene dine**: Sørg for at `-md`, `-img`, `-nb` samsvarer med det du ønsker
3. **Sjekk konfigurasjonen**: Sjekk at `.env`-filen har nødvendige nøkler
4. **Test trinnvis**: Start med kun `-md`, og legg til andre typer etter hvert
5. **Sjekk filstrukturen**: Sørg for at kildefilene finnes og er tilgjengelige

For mer detaljert informasjon om tilgjengelige kommandoer og flagg, se [Command Reference](./command-reference.md).

---

**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, må du være oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.