<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:21:35+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "da"
}
-->
# Kommandoreference

**Co-op Translator** CLI tilbyder flere muligheder for at tilpasse oversættelsesprocessen:

Kommando                                       | Beskrivelse
-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                  | Oversætter dit projekt til de angivne sprog. Eksempel: translate -l "es fr de" oversætter til spansk, fransk og tysk. Brug translate -l "all" for at oversætte til alle understøttede sprog.
translate -l "language_codes" -u               | Opdaterer oversættelser ved at slette eksisterende og genskabe dem. Advarsel: Dette sletter alle nuværende oversættelser for de angivne sprog.
translate -l "language_codes" -img             | Oversætter kun billedfiler.
translate -l "language_codes" -md              | Oversætter kun Markdown-filer.
translate -l "language_codes" -nb              | Oversætter kun Jupyter notebook-filer (.ipynb).
translate -l "language_codes" --fix            | Oversætter filer med lav selvtillidsscore igen baseret på tidligere evalueringsresultater.
translate -l "language_codes" -d               | Aktiverer debug-tilstand for detaljeret logning.
translate -l "language_codes" --save-logs, -s  | Gem DEBUG-niveau logs til filer under <root_dir>/logs/ (konsollen styres stadig af -d)
translate -l "language_codes" -r "root_dir"    | Angiver projektets rodmappe
translate -l "language_codes" -f               | Bruger hurtig tilstand for billedoversættelse (op til 3x hurtigere visning med en lille forringelse af kvalitet og justering).
translate -l "language_codes" -y               | Bekræfter automatisk alle prompts (nyttigt til CI/CD pipelines)
translate -l "language_codes" --help           | Hjælpedetaljer i CLI, der viser tilgængelige kommandoer
evaluate -l "language_code"                    | Evaluerer oversættelseskvaliteten for et bestemt sprog og giver selvtillidsscorer
evaluate -l "language_code" -c 0.8             | Evaluerer oversættelser med brugerdefineret selvtillidsgrænse
evaluate -l "language_code" -f                 | Hurtig evalueringstilstand (kun regelbaseret, ingen LLM)
evaluate -l "language_code" -D                 | Dybdegående evalueringstilstand (kun LLM-baseret, mere grundig men langsommere)
evaluate -l "language_code" --save-logs, -s    | Gem DEBUG-niveau logs til filer under <root_dir>/logs/
migrate-links -l "language_codes"              | Genbehandler oversatte Markdown-filer for at opdatere links til notebooks (.ipynb). Foretrækker oversatte notebooks, hvis de findes; ellers kan der linkes til de originale notebooks.
migrate-links -l "language_codes" -r           | Angiv projektets rodmappe (standard: nuværende mappe).
migrate-links -l "language_codes" --dry-run    | Vis hvilke filer der ville blive ændret uden at skrive ændringerne.
migrate-links -l "language_codes" --no-fallback-to-original | Omskriv ikke links til originale notebooks, når oversatte mangler (opdater kun, når oversatte findes).
migrate-links -l "language_codes" -d           | Aktiver debug-tilstand for detaljeret logning.
migrate-links -l "language_codes" --save-logs, -s | Gem DEBUG-niveau logs til filer under <root_dir>/logs/
migrate-links -l "all" -y                      | Behandl alle sprog og bekræft automatisk advarsels-prompten.

## Eksempler på brug

  1. Standardadfærd (tilføj nye oversættelser uden at slette eksisterende):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Tilføj kun nye koreanske billedoversættelser (ingen eksisterende oversættelser slettes):    translate -l "ko" -img

  3. Opdater alle koreanske oversættelser (Advarsel: Dette sletter alle eksisterende koreanske oversættelser før genoversættelse):    translate -l "ko" -u

  4. Opdater kun koreanske billeder (Advarsel: Dette sletter alle eksisterende koreanske billeder før genoversættelse):    translate -l "ko" -img -u

  5. Tilføj nye markdown-oversættelser for koreansk uden at påvirke andre oversættelser:    translate -l "ko" -md

  6. Ret oversættelser med lav selvtillid baseret på tidligere evalueringsresultater: translate -l "ko" --fix

  7. Ret oversættelser med lav selvtillid for specifikke filer (markdown): translate -l "ko" --fix -md

  8. Ret oversættelser med lav selvtillid for specifikke filer (billeder): translate -l "ko" --fix -img

  9. Brug hurtig tilstand for billedoversættelse:    translate -l "ko" -img -f

  10. Ret oversættelser med lav selvtillid med brugerdefineret grænse: translate -l "ko" --fix -c 0.8

  11. Eksempel på debug-tilstand: - translate -l "ko" -d: Aktiver debug-logning.
  12. Gem logs til filer: translate -l "ko" -s
  13. Konsol DEBUG og fil DEBUG: translate -l "ko" -d -s

  14. Migrer notebook-links for koreanske oversættelser (opdater links til oversatte notebooks, hvis de findes):    migrate-links -l "ko"

  15. Migrer links med dry-run (ingen filskrivning):    migrate-links -l "ko" --dry-run

  16. Opdater kun links når oversatte notebooks findes (brug ikke originaler som fallback):    migrate-links -l "ko" --no-fallback-to-original

  17. Behandl alle sprog med bekræftelses-prompt:    migrate-links -l "all"

  18. Behandl alle sprog og bekræft automatisk:    migrate-links -l "all" -y
  19. Gem logs til filer for migrate-links:    migrate-links -l "ko ja" -s

### Eksempler på evaluering

> [!WARNING]  
> **Beta-funktion**: Evalueringsfunktionen er i øjeblikket i beta. Denne funktion blev udgivet for at evaluere oversatte dokumenter, og evalueringsmetoderne samt den detaljerede implementering er stadig under udvikling og kan ændres.

  1. Evaluer koreanske oversættelser: evaluate -l "ko"

  2. Evaluer med brugerdefineret selvtillidsgrænse: evaluate -l "ko" -c 0.8

  3. Hurtig evaluering (kun regelbaseret): evaluate -l "ko" -f

  4. Dybdegående evaluering (kun LLM-baseret): evaluate -l "ko" -D

---

**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.