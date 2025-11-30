<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:29:56+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "no"
}
-->
# Kommandoreferanse

**Co-op Translator** CLI tilbyr flere alternativer for å tilpasse oversettelsesprosessen:

Kommando                                     | Beskrivelse
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Oversetter prosjektet ditt til angitte språk. Eksempel: translate -l "es fr de" oversetter til spansk, fransk og tysk. Bruk translate -l "all" for å oversette til alle støttede språk.
translate -l "language_codes" -u              | Oppdaterer oversettelser ved å slette eksisterende og opprette dem på nytt. Advarsel: Dette vil slette alle nåværende oversettelser for angitte språk.
translate -l "language_codes" -img            | Oversetter kun bildefiler.
translate -l "language_codes" -md             | Oversetter kun Markdown-filer.
translate -l "language_codes" -nb             | Oversetter kun Jupyter-notatbøker (.ipynb).
translate -l "language_codes" --fix           | Oversetter på nytt filer med lav tillitsvurdering basert på tidligere evalueringer.
translate -l "language_codes" -d              | Aktiverer feilsøkingsmodus for detaljert logging.
translate -l "language_codes" --save-logs, -s | Lagre DEBUG-nivå logger til filer under <root_dir>/logs/ (konsollen styres fortsatt av -d)
translate -l "language_codes" -r "root_dir"   | Angir prosjektets rotmappe
translate -l "language_codes" -f              | Bruker hurtigmodus for bildeoversettelse (opptil 3x raskere plotting med liten kvalitet- og justeringskostnad).
translate -l "language_codes" -y              | Bekrefter automatisk alle spørsmål (nyttig for CI/CD-pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Slå på eller av maskinoversettelsesansvarsfraskrivelse i oversatte markdown-filer og notatbøker (standard: på).
translate -l "language_codes" --help          | Hjelpedetaljer i CLI som viser tilgjengelige kommandoer
evaluate -l "language_code"                  | Evaluerer oversettelseskvalitet for et spesifikt språk og gir tillitsvurderinger
evaluate -l "language_code" -c 0.8           | Evaluerer oversettelser med egendefinert tillitsterskel
evaluate -l "language_code" -f               | Rask evalueringsmodus (kun regelbasert, ikke LLM)
evaluate -l "language_code" -D               | Dyp evalueringsmodus (kun LLM-basert, grundigere men tregere)
evaluate -l "language_code" --save-logs, -s  | Lagre DEBUG-nivå logger til filer under <root_dir>/logs/
migrate-links -l "language_codes"             | Behandler oversatte Markdown-filer på nytt for å oppdatere lenker til notatbøker (.ipynb). Foretrekker oversatte notatbøker når tilgjengelig; kan ellers falle tilbake til originale.
migrate-links -l "language_codes" -r          | Angi prosjektets rotmappe (standard: gjeldende mappe).
migrate-links -l "language_codes" --dry-run   | Vis hvilke filer som ville endres uten å skrive endringer.
migrate-links -l "language_codes" --no-fallback-to-original | Ikke omskriv lenker til originale notatbøker når oversatte mangler (oppdater kun når oversatt finnes).
migrate-links -l "language_codes" -d          | Aktiver feilsøkingsmodus for detaljert logging.
migrate-links -l "language_codes" --save-logs, -s | Lagre DEBUG-nivå logger til filer under <root_dir>/logs/
migrate-links -l "all" -y                      | Behandle alle språk og bekreft advarselsprompt automatisk.

## Brukseksempler

  1. Standard oppførsel (legg til nye oversettelser uten å slette eksisterende):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Legg kun til nye koreanske bildeoversettelser (ingen eksisterende oversettelser slettes):    translate -l "ko" -img

  3. Oppdater alle koreanske oversettelser (Advarsel: Sletter alle eksisterende koreanske oversettelser før ny oversettelse):    translate -l "ko" -u

  4. Oppdater kun koreanske bilder (Advarsel: Sletter alle eksisterende koreanske bilder før ny oversettelse):    translate -l "ko" -img -u

  5. Legg til nye markdown-oversettelser for koreansk uten å påvirke andre oversettelser:    translate -l "ko" -md

  6. Fiks oversettelser med lav tillit basert på tidligere evalueringer: translate -l "ko" --fix

  7. Fiks oversettelser med lav tillit for spesifikke filer (markdown): translate -l "ko" --fix -md

  8. Fiks oversettelser med lav tillit for spesifikke filer (bilder): translate -l "ko" --fix -img

  9. Bruk hurtigmodus for bildeoversettelse:    translate -l "ko" -img -f

  10. Fiks oversettelser med lav tillit med egendefinert terskel: translate -l "ko" --fix -c 0.8

  11. Eksempel på feilsøkingsmodus: - translate -l "ko" -d: Aktiver feilsøkingslogging.
  12. Lagre logger til filer: translate -l "ko" -s
  13. Konsoll DEBUG og fil DEBUG: translate -l "ko" -d -s
  14. Oversett uten å legge til ansvarsfraskrivelser for maskinoversettelse: translate -l "ko" --no-disclaimer

  15. Migrer notatboklenker for koreanske oversettelser (oppdater lenker til oversatte notatbøker når tilgjengelig):    migrate-links -l "ko"

  15. Migrer lenker med dry-run (ingen filskriving):    migrate-links -l "ko" --dry-run

  16. Oppdater kun lenker når oversatte notatbøker finnes (ikke fallback til originaler):    migrate-links -l "ko" --no-fallback-to-original

  17. Behandle alle språk med bekreftelsesprompt:    migrate-links -l "all"

  18. Behandle alle språk og bekreft automatisk:    migrate-links -l "all" -y
  19. Lagre logger til filer for migrate-links:    migrate-links -l "ko ja" -s

### Evaluerings-eksempler

> [!WARNING]  
> **Beta-funksjon**: Evalueringsfunksjonaliteten er for øyeblikket i beta. Denne funksjonen ble lansert for å evaluere oversatte dokumenter, og evalueringsmetoder og detaljert implementering er fortsatt under utvikling og kan endres.

  1. Evaluer koreanske oversettelser: evaluate -l "ko"

  2. Evaluer med egendefinert tillitsterskel: evaluate -l "ko" -c 0.8

  3. Rask evaluering (kun regelbasert): evaluate -l "ko" -f

  4. Dyp evaluering (kun LLM-basert): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->