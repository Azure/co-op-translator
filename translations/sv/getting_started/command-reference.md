<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:22:00+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sv"
}
-->
# Kommandoreferens

**Co-op Translator** CLI erbjuder flera alternativ för att anpassa översättningsprocessen:

Kommando                                     | Beskrivning
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Översätter ditt projekt till angivna språk. Exempel: translate -l "es fr de" översätter till spanska, franska och tyska. Använd translate -l "all" för att översätta till alla stödda språk.
translate -l "language_codes" -u              | Uppdaterar översättningar genom att ta bort befintliga och skapa dem på nytt. Varning: Detta raderar alla nuvarande översättningar för angivna språk.
translate -l "language_codes" -img            | Översätter endast bildfiler.
translate -l "language_codes" -md             | Översätter endast Markdown-filer.
translate -l "language_codes" -nb             | Översätter endast Jupyter-notebook-filer (.ipynb).
translate -l "language_codes" --fix           | Översätter om filer med lågt förtroendescore baserat på tidigare utvärderingsresultat.
translate -l "language_codes" -d              | Aktiverar felsökningsläge för detaljerad loggning.
translate -l "language_codes" --save-logs, -s | Sparar DEBUG-loggar till filer under <root_dir>/logs/ (konsolen styrs fortfarande av -d)
translate -l "language_codes" -r "root_dir"   | Anger projektets rotkatalog
translate -l "language_codes" -f              | Använder snabb läge för bildöversättning (upp till 3x snabbare rendering med liten kvalitets- och justeringsförlust).
translate -l "language_codes" -y              | Bekräftar automatiskt alla promptar (användbart för CI/CD-pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Aktiverar eller inaktiverar tillägg av maskinöversättningsansvarsfriskrivning i översatta markdown och notebooks (standard: aktiverat).
translate -l "language_codes" --help          | Hjälpdetaljer inom CLI som visar tillgängliga kommandon
evaluate -l "language_code"                  | Utvärderar översättningskvalitet för ett specifikt språk och ger förtroendescore
evaluate -l "language_code" -c 0.8           | Utvärderar översättningar med anpassad förtroendetröskel
evaluate -l "language_code" -f               | Snabb utvärderingsläge (endast regelbaserat, inget LLM)
evaluate -l "language_code" -D               | Djup utvärderingsläge (endast LLM-baserat, mer grundligt men långsammare)
evaluate -l "language_code" --save-logs, -s  | Sparar DEBUG-loggar till filer under <root_dir>/logs/
migrate-links -l "language_codes"             | Omprocessar översatta Markdown-filer för att uppdatera länkar till notebooks (.ipynb). Föredrar översatta notebooks när de finns; kan annars falla tillbaka på original.
migrate-links -l "language_codes" -r          | Anger projektets rotkatalog (standard: aktuell katalog).
migrate-links -l "language_codes" --dry-run   | Visar vilka filer som skulle ändras utan att skriva ändringar.
migrate-links -l "language_codes" --no-fallback-to-original | Skriver inte om länkar till originalnotebooks när översatta motsvarigheter saknas (uppdaterar endast när översatt finns).
migrate-links -l "language_codes" -d          | Aktiverar felsökningsläge för detaljerad loggning.
migrate-links -l "language_codes" --save-logs, -s | Sparar DEBUG-loggar till filer under <root_dir>/logs/
migrate-links -l "all" -y                      | Bearbetar alla språk och bekräftar varningsprompt automatiskt.

## Exempel på användning

  1. Standardbeteende (lägger till nya översättningar utan att ta bort befintliga):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lägg endast till nya koreanska bildöversättningar (inga befintliga översättningar tas bort):    translate -l "ko" -img

  3. Uppdatera alla koreanska översättningar (Varning: Detta raderar alla befintliga koreanska översättningar innan omöversättning):    translate -l "ko" -u

  4. Uppdatera endast koreanska bilder (Varning: Detta raderar alla befintliga koreanska bilder innan omöversättning):    translate -l "ko" -img -u

  5. Lägg till nya markdown-översättningar för koreanska utan att påverka andra översättningar:    translate -l "ko" -md

  6. Åtgärda översättningar med lågt förtroende baserat på tidigare utvärderingsresultat: translate -l "ko" --fix

  7. Åtgärda översättningar med lågt förtroende för specifika filer endast (markdown): translate -l "ko" --fix -md

  8. Åtgärda översättningar med lågt förtroende för specifika filer endast (bilder): translate -l "ko" --fix -img

  9. Använd snabb läge för bildöversättning:    translate -l "ko" -img -f

  10. Åtgärda översättningar med lågt förtroende med anpassad tröskel: translate -l "ko" --fix -c 0.8

  11. Exempel på felsökningsläge: - translate -l "ko" -d: Aktivera felsökningsloggning.
  12. Spara loggar till filer: translate -l "ko" -s
  13. Konsol DEBUG och fil DEBUG: translate -l "ko" -d -s
  14. Översätt utan att lägga till maskinöversättningsansvarsfriskrivningar i utdata: translate -l "ko" --no-disclaimer

  15. Migrera notebook-länkar för koreanska översättningar (uppdatera länkar till översatta notebooks när de finns):    migrate-links -l "ko"

  15. Migrera länkar med torrkörning (inga filändringar):    migrate-links -l "ko" --dry-run

  16. Uppdatera endast länkar när översatta notebooks finns (faller inte tillbaka på original):    migrate-links -l "ko" --no-fallback-to-original

  17. Bearbeta alla språk med bekräftelseprompt:    migrate-links -l "all"

  18. Bearbeta alla språk och bekräfta automatiskt:    migrate-links -l "all" -y
  19. Spara loggar till filer för migrate-links:    migrate-links -l "ko ja" -s

### Exempel på utvärdering

> [!WARNING]  
> **Beta-funktion**: Utvärderingsfunktionen är för närvarande i beta. Denna funktion släpptes för att utvärdera översatta dokument, och utvärderingsmetoder samt detaljerad implementering är fortfarande under utveckling och kan ändras.

  1. Utvärdera koreanska översättningar: evaluate -l "ko"

  2. Utvärdera med anpassad förtroendetröskel: evaluate -l "ko" -c 0.8

  3. Snabb utvärdering (endast regelbaserat): evaluate -l "ko" -f

  4. Djup utvärdering (endast LLM-baserat): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->