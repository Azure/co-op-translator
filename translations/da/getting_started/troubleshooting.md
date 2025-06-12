<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:27:40+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "da"
}
-->
# Microsoft Co-op Translator Fejlfinding Guide

## Oversigt
Microsoft Co-Op Translator er et kraftfuldt værktøj til problemfrit at oversætte Markdown-dokumenter. Denne guide hjælper dig med at fejlfinde almindelige problemer, der kan opstå ved brug af værktøjet.

## Almindelige Problemer og Løsninger

### 1. Markdown Tag Problem
**Problem:** Det oversatte Markdown-dokument indeholder en `markdown` tag øverst, hvilket forårsager gengivelsesproblemer.

**Løsning:** For at løse dette skal du blot slette `markdown` tagget øverst i filen. Det vil sikre, at Markdown-filen gengives korrekt.

**Trin:**
1. Åbn den oversatte Markdown (`.md`) fil.
2. Find `markdown` tagget øverst i dokumentet.
3. Slet `markdown` tagget.
4. Gem ændringerne i filen.
5. Åbn filen igen for at sikre, at den gengives korrekt.

### 2. URL Problem med Indlejrede Billeder
**Problem:** URL’erne til de indlejrede billeder matcher ikke sproglokalet, hvilket fører til forkerte eller manglende billeder.

**Løsning:** Kontroller URL’erne til de indlejrede billeder og sørg for, at de matcher sproglokalet. Alle billeder ligger i `translated_images` mappen, og hvert billede har en sproglokale-tag i filnavnet.

**Trin:**
1. Åbn det oversatte Markdown-dokument.
2. Identificer de indlejrede billeder og deres URL’er.
3. Bekræft, at sproglokalet i billedfilens navn matcher dokumentets sprog.
4. Opdater URL’erne om nødvendigt.
5. Gem ændringerne og åbn dokumentet igen for at bekræfte, at billederne vises korrekt.

### 3. Oversættelsesnøjagtighed
**Problem:** Det oversatte indhold er ikke præcist eller kræver yderligere redigering.

**Løsning:** Gennemgå det oversatte dokument og foretag nødvendige rettelser for at forbedre nøjagtighed og læsbarhed.

**Trin:**
1. Åbn det oversatte dokument.
2. Gennemgå indholdet grundigt.
3. Foretag nødvendige rettelser for at forbedre oversættelsens nøjagtighed.
4. Gem ændringerne.

### 4. Problemer med Filformatering
**Problem:** Formateringen af det oversatte dokument er forkert. Dette kan ske i tabeller, hvor den ekstra ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` vil løse tabelproblemerne.

**Trin:**
1. Åbn det oversatte dokument.
2. Sammenlign det med det originale dokument for at identificere formateringsproblemer.
3. Juster formateringen, så den matcher det originale dokument.
4. Gem ændringerne.

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.