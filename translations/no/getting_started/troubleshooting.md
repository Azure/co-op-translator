<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:27:54+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "no"
}
-->
# Microsoft Co-op Translator Feilsøkingsguide


## Oversikt
Microsoft Co-Op Translator er et kraftig verktøy for sømløs oversettelse av Markdown-dokumenter. Denne guiden hjelper deg med å feilsøke vanlige problemer som kan oppstå ved bruk av verktøyet.

## Vanlige problemer og løsninger

### 1. Problem med Markdown-tagger
**Problem:** Den oversatte Markdown-filen inneholder en `markdown`-tagg øverst, noe som forårsaker problemer med visningen.

**Løsning:** For å løse dette, fjern bare `markdown`-taggen øverst i filen. Dette vil gjøre at Markdown-filen vises korrekt.

**Trinn:**
1. Åpne den oversatte Markdown-filen (`.md`).
2. Finn `markdown`-taggen øverst i dokumentet.
3. Slett `markdown`-taggen.
4. Lagre endringene i filen.
5. Åpne filen på nytt for å sikre at den vises riktig.

### 2. Problem med URL-er til innebygde bilder
**Problem:** URL-ene til innebygde bilder samsvarer ikke med språkinnstillingen, noe som fører til feil eller manglende bilder.

**Løsning:** Sjekk URL-ene til de innebygde bildene og sørg for at de stemmer overens med språkinnstillingen. Alle bilder ligger i `translated_images`-mappen, og hvert bilde har en språkinnstillingskode i filnavnet.

**Trinn:**
1. Åpne det oversatte Markdown-dokumentet.
2. Identifiser de innebygde bildene og deres URL-er.
3. Kontroller at språkinnstillingen i bildefilnavnet samsvarer med dokumentets språk.
4. Oppdater URL-ene om nødvendig.
5. Lagre endringene og åpne dokumentet på nytt for å bekrefte at bildene vises riktig.

### 3. Nøyaktighet i oversettelsen
**Problem:** Den oversatte teksten er unøyaktig eller trenger ytterligere redigering.

**Løsning:** Gå gjennom den oversatte teksten og gjør nødvendige endringer for å forbedre nøyaktighet og lesbarhet.

**Trinn:**
1. Åpne den oversatte teksten.
2. Gå nøye gjennom innholdet.
3. Gjør nødvendige endringer for å forbedre oversettelsens nøyaktighet.
4. Lagre endringene.

### 4. Problemer med filformatering
**Problem:** Formateringen i den oversatte filen er feil. Dette kan skje i tabeller – her vil ekstra ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` hjelpe med tabellproblemene.

**Trinn:**
1. Åpne den oversatte filen.
2. Sammenlign med originaldokumentet for å finne formateringsfeil.
3. Juster formateringen slik at den samsvarer med originalen.
4. Lagre endringene.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.