<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:19:06+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sv"
}
-->
# Kommandoreferens

**Co-op Translator** CLI erbjuder flera alternativ för att anpassa översättningsprocessen:

Kommando                                       | Beskrivning
-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                  | Översätter ditt projekt till angivna språk. Exempel: translate -l "es fr de" översätter till spanska, franska och tyska. Använd translate -l "all" för att översätta till alla språk som stöds.
translate -l "language_codes" -u               | Uppdaterar översättningar genom att ta bort befintliga och skapa nya. Varning: Detta tar bort alla nuvarande översättningar för angivna språk.
translate -l "language_codes" -img             | Översätter endast bildfiler.
translate -l "language_codes" -md              | Översätter endast Markdown-filer.
translate -l "language_codes" -nb              | Översätter endast Jupyter notebook-filer (.ipynb).
translate -l "language_codes" --fix            | Översätter om filer med låg tillförlitlighet baserat på tidigare utvärderingsresultat.
translate -l "language_codes" -d               | Aktiverar felsökningsläge för detaljerad loggning.
translate -l "language_codes" --save-logs, -s  | Spara DEBUG-loggar till filer under <root_dir>/logs/ (konsolen styrs fortfarande av -d)
translate -l "language_codes" -r "root_dir"    | Anger projektets rotmapp
translate -l "language_codes" -f               | Använder snabb läge för bildöversättning (upp till 3x snabbare plottning med viss försämring av kvalitet och justering).
translate -l "language_codes" -y               | Bekräfta automatiskt alla frågor (användbart för CI/CD-pipelines)
translate -l "language_codes" --help           | Hjälpdetaljer i CLI som visar tillgängliga kommandon
evaluate -l "language_code"                    | Utvärderar översättningskvalitet för ett specifikt språk och ger tillförlitlighetspoäng
evaluate -l "language_code" -c 0.8             | Utvärderar översättningar med anpassad tillförlitlighetströskel
evaluate -l "language_code" -f                 | Snabb utvärdering (endast regelbaserad, ingen LLM)
evaluate -l "language_code" -D                 | Djup utvärdering (endast LLM-baserad, mer noggrann men långsammare)
evaluate -l "language_code" --save-logs, -s    | Spara DEBUG-loggar till filer under <root_dir>/logs/
migrate-links -l "language_codes"              | Bearbetar översatta Markdown-filer för att uppdatera länkar till notebooks (.ipynb). Föredrar översatta notebooks när de finns; annars kan originalen användas.
migrate-links -l "language_codes" -r           | Ange projektets rotmapp (standard: nuvarande mapp).
migrate-links -l "language_codes" --dry-run    | Visa vilka filer som skulle ändras utan att skriva ändringar.
migrate-links -l "language_codes" --no-fallback-to-original | Skriv inte om länkar till originalnotebooks när översatta saknas (uppdatera endast när översatt finns).
migrate-links -l "language_codes" -d           | Aktivera felsökningsläge för detaljerad loggning.
migrate-links -l "language_codes" --save-logs, -s | Spara DEBUG-loggar till filer under <root_dir>/logs/
migrate-links -l "all" -y                      | Bearbeta alla språk och bekräfta varningsfrågan automatiskt.

## Exempel på användning

  1. Standardbeteende (lägg till nya översättningar utan att ta bort befintliga):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lägg endast till nya koreanska bildöversättningar (inga befintliga översättningar tas bort):    translate -l "ko" -img

  3. Uppdatera alla koreanska översättningar (Varning: Detta tar bort alla befintliga koreanska översättningar innan de översätts igen):    translate -l "ko" -u

  4. Uppdatera endast koreanska bilder (Varning: Detta tar bort alla befintliga koreanska bilder innan de översätts igen):    translate -l "ko" -img -u

  5. Lägg till nya markdown-översättningar för koreanska utan att påverka andra översättningar:    translate -l "ko" -md

  6. Åtgärda översättningar med låg tillförlitlighet baserat på tidigare utvärderingsresultat: translate -l "ko" --fix

  7. Åtgärda översättningar med låg tillförlitlighet för specifika filer (markdown): translate -l "ko" --fix -md

  8. Åtgärda översättningar med låg tillförlitlighet för specifika filer (bilder): translate -l "ko" --fix -img

  9. Använd snabb läge för bildöversättning:    translate -l "ko" -img -f

  10. Åtgärda översättningar med låg tillförlitlighet med anpassad tröskel: translate -l "ko" --fix -c 0.8

  11. Exempel på felsökningsläge: - translate -l "ko" -d: Aktivera felsökningsloggning.
  12. Spara loggar till filer: translate -l "ko" -s
  13. Konsol DEBUG och fil DEBUG: translate -l "ko" -d -s

  14. Migrera notebook-länkar för koreanska översättningar (uppdatera länkar till översatta notebooks när de finns):    migrate-links -l "ko"

  15. Migrera länkar med dry-run (inga filändringar):    migrate-links -l "ko" --dry-run

  16. Uppdatera endast länkar när översatta notebooks finns (använd inte originalen):    migrate-links -l "ko" --no-fallback-to-original

  17. Bearbeta alla språk med bekräftelsefråga:    migrate-links -l "all"

  18. Bearbeta alla språk och bekräfta automatiskt:    migrate-links -l "all" -y
  19. Spara loggar till filer för migrate-links:    migrate-links -l "ko ja" -s

### Exempel på utvärdering

> [!WARNING]  
> **Beta-funktion**: Utvärderingsfunktionen är för närvarande i beta. Denna funktion har släppts för att utvärdera översatta dokument, och utvärderingsmetoder samt detaljerad implementation är fortfarande under utveckling och kan komma att ändras.

  1. Utvärdera koreanska översättningar: evaluate -l "ko"

  2. Utvärdera med anpassad tillförlitlighetströskel: evaluate -l "ko" -c 0.8

  3. Snabb utvärdering (endast regelbaserad): evaluate -l "ko" -f

  4. Djup utvärdering (endast LLM-baserad): evaluate -l "ko" -D

---

**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.