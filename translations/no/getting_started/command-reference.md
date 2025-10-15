<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:24:13+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "no"
}
-->
# Kommandoreferanse

**Co-op Translator** CLI tilbyr flere alternativer for å tilpasse oversettelsesprosessen:

Kommando                                       | Beskrivelse
-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                  | Oversetter prosjektet ditt til angitte språk. Eksempel: translate -l "es fr de" oversetter til spansk, fransk og tysk. Bruk translate -l "all" for å oversette til alle støttede språk.
translate -l "language_codes" -u               | Oppdaterer oversettelser ved å slette eksisterende og lage dem på nytt. Advarsel: Dette vil slette alle nåværende oversettelser for de angitte språkene.
translate -l "language_codes" -img             | Oversetter kun bildefiler.
translate -l "language_codes" -md              | Oversetter kun Markdown-filer.
translate -l "language_codes" -nb              | Oversetter kun Jupyter notebook-filer (.ipynb).
translate -l "language_codes" --fix            | Oversetter filer på nytt med lav selvtillit basert på tidligere evalueringsresultater.
translate -l "language_codes" -d               | Aktiverer feilsøkingsmodus for detaljert logging.
translate -l "language_codes" --save-logs, -s  | Lagre DEBUG-logger til filer under <root_dir>/logs/ (konsollen styres fortsatt av -d)
translate -l "language_codes" -r "root_dir"    | Angir rotmappen til prosjektet
translate -l "language_codes" -f               | Bruker rask modus for bildeoversettelse (opptil 3x raskere plotting, men litt lavere kvalitet og justering).
translate -l "language_codes" -y               | Bekreft alle spørsmål automatisk (nyttig for CI/CD-pipelines)
translate -l "language_codes" --help           | Hjelpedetaljer i CLI som viser tilgjengelige kommandoer
evaluate -l "language_code"                    | Evaluerer oversettelseskvalitet for et spesifikt språk og gir selvtillitspoeng
evaluate -l "language_code" -c 0.8             | Evaluerer oversettelser med tilpasset selvtillitsterskel
evaluate -l "language_code" -f                 | Rask evalueringsmodus (kun regelbasert, ingen LLM)
evaluate -l "language_code" -D                 | Dyp evalueringsmodus (kun LLM-basert, grundigere men tregere)
evaluate -l "language_code" --save-logs, -s    | Lagre DEBUG-logger til filer under <root_dir>/logs/
migrate-links -l "language_codes"              | Behandler oversatte Markdown-filer på nytt for å oppdatere lenker til notatbøker (.ipynb). Foretrekker oversatte notatbøker når de finnes; ellers kan den bruke originale notatbøker.
migrate-links -l "language_codes" -r           | Angi prosjektets rotmappe (standard: nåværende mappe).
migrate-links -l "language_codes" --dry-run    | Vis hvilke filer som ville blitt endret uten å skrive endringer.
migrate-links -l "language_codes" --no-fallback-to-original | Ikke omskriv lenker til originale notatbøker når oversatte mangler (oppdater kun når oversatt finnes).
migrate-links -l "language_codes" -d           | Aktiver feilsøkingsmodus for detaljert logging.
migrate-links -l "language_codes" --save-logs, -s | Lagre DEBUG-logger til filer under <root_dir>/logs/
migrate-links -l "all" -y                      | Behandle alle språk og bekreft advarsler automatisk.

## Brukseksempler

  1. Standard oppførsel (legg til nye oversettelser uten å slette eksisterende):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Legg kun til nye koreanske bildeoversettelser (ingen eksisterende oversettelser slettes):    translate -l "ko" -img

  3. Oppdater alle koreanske oversettelser (Advarsel: Dette sletter alle eksisterende koreanske oversettelser før ny oversettelse):    translate -l "ko" -u

  4. Oppdater kun koreanske bilder (Advarsel: Dette sletter alle eksisterende koreanske bilder før ny oversettelse):    translate -l "ko" -img -u

  5. Legg til nye markdown-oversettelser for koreansk uten å påvirke andre oversettelser:    translate -l "ko" -md

  6. Fiks oversettelser med lav selvtillit basert på tidligere evaluering: translate -l "ko" --fix

  7. Fiks oversettelser med lav selvtillit for kun spesifikke filer (markdown): translate -l "ko" --fix -md

  8. Fiks oversettelser med lav selvtillit for kun spesifikke filer (bilder): translate -l "ko" --fix -img

  9. Bruk rask modus for bildeoversettelse:    translate -l "ko" -img -f

  10. Fiks oversettelser med lav selvtillit med tilpasset terskel: translate -l "ko" --fix -c 0.8

  11. Eksempel på feilsøkingsmodus: - translate -l "ko" -d: Aktiver detaljert logging.
  12. Lagre logger til filer: translate -l "ko" -s
  13. Konsoll DEBUG og fil DEBUG: translate -l "ko" -d -s

  14. Migrer notatboklenker for koreanske oversettelser (oppdater lenker til oversatte notatbøker når tilgjengelig):    migrate-links -l "ko"

  15. Migrer lenker med dry-run (ingen filskriving):    migrate-links -l "ko" --dry-run

  16. Oppdater kun lenker når oversatte notatbøker finnes (ikke bruk originalene):    migrate-links -l "ko" --no-fallback-to-original

  17. Behandle alle språk med bekreftelsesspørsmål:    migrate-links -l "all"

  18. Behandle alle språk og bekreft automatisk:    migrate-links -l "all" -y
  19. Lagre logger til filer for migrate-links:    migrate-links -l "ko ja" -s

### Evaluerings-eksempler

> [!WARNING]  
> **Beta-funksjon**: Evalueringsfunksjonaliteten er for øyeblikket i beta. Denne funksjonen ble lansert for å evaluere oversatte dokumenter, og evalueringsmetodene og detaljert implementering er fortsatt under utvikling og kan endres.

  1. Evaluer koreanske oversettelser: evaluate -l "ko"

  2. Evaluer med tilpasset selvtillitsterskel: evaluate -l "ko" -c 0.8

  3. Rask evaluering (kun regelbasert): evaluate -l "ko" -f

  4. Dyp evaluering (kun LLM-basert): evaluate -l "ko" -D

---

**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, må du være oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.