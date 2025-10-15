<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:22:05+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "da"
}
-->
# Microsoft Co-op Translator Fejlfindingsguide

## Oversigt
Microsoft Co-Op Translator er et effektivt værktøj til at oversætte Markdown-dokumenter uden besvær. Denne guide hjælper dig med at løse almindelige problemer, du kan støde på, når du bruger værktøjet.

## Almindelige problemer og løsninger

### 1. Markdown-tag problem
**Problem:** Det oversatte Markdown-dokument indeholder et `markdown`-tag øverst, hvilket giver visningsproblemer.

**Løsning:** For at løse dette skal du blot slette `markdown`-tagget øverst i filen. Så vil Markdown-filen blive vist korrekt.

**Trin:**
1. Åbn den oversatte Markdown (`.md`)-fil.
2. Find `markdown`-tagget øverst i dokumentet.
3. Slet `markdown`-tagget.
4. Gem filen.
5. Genåbn filen for at sikre, at den vises korrekt.

### 2. URL-problem med indlejrede billeder
**Problem:** URL’erne til indlejrede billeder matcher ikke sproget, hvilket giver forkerte eller manglende billeder.

**Løsning:** Tjek URL’en for indlejrede billeder og sørg for, at de matcher sproget. Alle billeder ligger i mappen `translated_images`, og hvert billede har et sprog-tag i filnavnet.

**Trin:**
1. Åbn det oversatte Markdown-dokument.
2. Find de indlejrede billeder og deres URL’er.
3. Tjek at sprogtagget i billedets filnavn matcher dokumentets sprog.
4. Opdater URL’erne om nødvendigt.
5. Gem og genåbn dokumentet for at sikre, at billederne vises korrekt.

### 3. Oversættelsesnøjagtighed
**Problem:** Den oversatte tekst er ikke nøjagtig eller kræver yderligere redigering.

**Løsning:** Gennemgå det oversatte dokument og ret det, så det bliver mere korrekt og letlæseligt.

**Trin:**
1. Åbn det oversatte dokument.
2. Læs teksten grundigt igennem.
3. Ret oversættelsen, så den bliver mere præcis.
4. Gem ændringerne.

## 4. Tilladelsesfejl Redacted eller 404

Hvis billeder eller tekst ikke oversættes til det rigtige sprog, og du i -d debug mode får en 401-fejl, skyldes det typisk en godkendelsesfejl—enten er nøglen ugyldig, udløbet eller ikke knyttet til den rigtige region.

Kør co-op translator med [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) for at få mere indsigt i årsagen.

- **Fejlmeddelelse**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Mulige årsager**:
  - Subscription key blev redigeret eller er forkert i forespørgslen.
  - AI Services Key eller Subscription Key tilhører en anden Azure-ressource (som Translator eller OpenAI) i stedet for en **Azure AI Vision**-ressource.

 **Resourcetype**
  - Gå til [Azure Portal](https://portal.azure.com) eller [Azure AI Foundry](https://ai.azure.com) og tjek, at ressourcen er af typen `Azure AI services` → `Vision`.
  - Tjek nøglerne og sørg for, at den rigtige nøgle bruges.

## 5. Konfigurationsfejl (Ny fejlhåndtering)

Med det nye selektive oversættelsessystem giver Co-op Translator nu tydelige fejlmeddelelser, hvis nødvendige tjenester ikke er konfigureret.

### 5.1. Azure AI Service ikke konfigureret til billedoversættelse

**Problem:** Du har bedt om billedoversættelse (`-img` flag), men Azure AI Service er ikke konfigureret korrekt.

**Fejlmeddelelse:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Løsning:**
1. **Mulighed 1**: Konfigurer Azure AI Service
   - Tilføj `AZURE_AI_SERVICE_API_KEY` til din `.env`-fil
   - Tilføj `AZURE_AI_SERVICE_ENDPOINT` til din `.env`-fil
   - Tjek at tjenesten er tilgængelig

2. **Mulighed 2**: Fjern billedoversættelse fra kommandoen
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Manglende nødvendig konfiguration

**Problem:** Vigtig LLM-konfiguration mangler.

**Fejlmeddelelse:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Løsning:**
1. Tjek at din `.env`-fil har mindst én af følgende LLM-konfigurationer:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` og `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Du skal have enten Azure OpenAI ELLER OpenAI konfigureret, ikke begge.

### 5.3. Forvirring om selektiv oversættelse

**Problem:** Ingen filer blev oversat, selvom kommandoen lykkedes.

**Mulige årsager:**
- Forkerte filtype-flags (`-md`, `-img`, `-nb`)
- Ingen matchende filer i projektet
- Forkert mappestruktur

**Løsning:**
1. **Brug debug mode** for at se, hvad der sker:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Tjek filtyper** i dit projekt:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Tjek flag-kombinationer**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migration fra det gamle system

### 6.1. Markdown-only mode udfases

**Problem:** Kommandoer, der automatisk kun oversatte markdown, virker ikke længere som forventet.

**Tidligere opførsel:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Ny opførsel:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Løsning:**
- **Vær tydelig** om, hvad du vil oversætte:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Uventet link-opførsel

**Problem:** Links i oversatte filer peger på uventede steder.

**Årsag:** Dynamisk link-håndtering ændres afhængigt af valgte filtyper.

**Løsning:**
1. **Forstå den nye link-opførsel**:
   - `-nb` inkluderet: Notebook-links peger på oversatte versioner
   - `-nb` udeladt: Notebook-links peger på originale filer
   - `-img` inkluderet: Billedlinks peger på oversatte versioner
   - `-img` udeladt: Billedlinks peger på originale filer

2. **Vælg den rigtige kombination** til dit behov:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action kørte men der blev ikke oprettet Pull Request (PR)

**Symptom:** Workflow-loggen for `peter-evans/create-pull-request` viser:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Mulige årsager:**
- **Ingen ændringer fundet:** Oversættelsen gav ingen forskelle (repo er allerede opdateret).
- **Ignorerede outputs:** `.gitignore` udelukker filer, du forventer at committe (fx `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths mismatch:** Stierne til action matcher ikke de faktiske output-mapper.
- **Workflow-logik/betingelser:** Oversættelsen stoppede tidligt eller skrev til forkerte mapper.

**Sådan løser du det / tjekker:**
1. **Tjek outputs:** Efter oversættelse, tjek at der er nye/ændrede filer i `translations/` og/eller `translated_images/`.
   - Hvis du oversætter notebooks, tjek at `.ipynb`-filer faktisk ligger under `translations/<lang>/...`.
2. **Gennemgå `.gitignore`:** Ignorér ikke de genererede outputs. Sørg for at du IKKE ignorerer:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (hvis du oversætter notebooks)
3. **Sørg for at add-paths matcher outputs:** Brug en multilinje-værdi og inkluder begge mapper hvis nødvendigt:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Tving en PR for fejlsøgning:** Tillad midlertidigt tomme commits for at tjekke at alt virker:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Kør med debug:** Tilføj `-d` til oversættelseskommandoen for at se, hvilke filer der blev fundet og skrevet.
6. **Tilladelser (GITHUB_TOKEN):** Tjek at workflow har skriveadgang til at oprette commits og PRs:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Hurtig fejlsøgnings-tjekliste

Når du fejlsøger oversættelsesproblemer:

1. **Brug debug mode**: Tilføj `-d` for detaljerede logs
2. **Tjek dine flags**: Sørg for at `-md`, `-img`, `-nb` matcher dit formål
3. **Tjek konfigurationen**: Tjek at din `.env`-fil har de nødvendige nøgler
4. **Test trin for trin**: Start med kun `-md`, tilføj derefter andre typer
5. **Tjek filstrukturen**: Sørg for at kildefilerne findes og kan tilgås

For mere detaljeret information om tilgængelige kommandoer og flags, se [Command Reference](./command-reference.md).

---

**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.