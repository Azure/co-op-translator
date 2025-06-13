<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:29:26+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "no"
}
-->
# Kommando referanse
**Co-op Translator** CLI tilbyr flere alternativer for å tilpasse oversettelsesprosessen:

Kommando                                     | Beskrivelse
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Oversetter prosjektet ditt til angitte språk. Eksempel: translate -l "es fr de" oversetter til spansk, fransk og tysk. Bruk translate -l "all" for å oversette til alle støttede språk.
translate -l "language_codes" -u              | Oppdaterer oversettelser ved å slette eksisterende og lage dem på nytt. Advarsel: Dette sletter alle nåværende oversettelser for angitte språk.
translate -l "language_codes" -img            | Oversetter kun bildefiler.
translate -l "language_codes" -md             | Oversetter kun Markdown-filer.
translate -l "language_codes" -chk            | Sjekker oversatte filer for feil og prøver å oversette på nytt om nødvendig.
translate -l "language_codes" -d              | Aktiverer debug-modus for detaljert logging.
translate -l "language_codes" -r "root_dir"   | Spesifiserer prosjektets rotkatalog
translate -l "language_codes" -f              | Bruker rask modus for bildeoversettelse (opptil 3 ganger raskere plotting med en liten kostnad for kvalitet og justering).
translate -l "language_codes" -y              | Bekrefter automatisk alle spørsmål (nyttig for CI/CD-pipelines)
translate -l "language_codes" --help          | hjelpdetaljer i CLI som viser tilgjengelige kommandoer

### Brukseksempler:

  1. Standard oppførsel (legg til nye oversettelser uten å slette eksisterende):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Legg til kun nye koreanske bildeoversettelser (ingen eksisterende oversettelser slettes):    translate -l "ko" -img

  3. Oppdater alle koreanske oversettelser (Advarsel: Dette sletter alle eksisterende koreanske oversettelser før ny oversettelse):    translate -l "ko" -u

  4. Oppdater kun koreanske bilder (Advarsel: Dette sletter alle eksisterende koreanske bilder før ny oversettelse):    translate -l "ko" -img -u

  5. Legg til nye markdown-oversettelser for koreansk uten å påvirke andre oversettelser:    translate -l "ko" -md

  6. Sjekk oversatte filer for feil og prøv oversettelse på nytt om nødvendig: translate -l "ko" -chk

  7. Sjekk oversatte filer for feil og prøv oversettelse på nytt (kun markdown): translate -l "ko" -chk -md

  8. Sjekk oversatte filer for feil og prøv oversettelse på nytt (kun bilder): translate -l "ko" -chk -img

  9. Bruk rask modus for bildeoversettelse:    translate -l "ko" -img -f

  10. Debug-modus eksempel: - translate -l "ko" -d: Aktiver debug-logging.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.