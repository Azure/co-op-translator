<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:29:00+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sv"
}
-->
# Kommandoreferens
**Co-op Translator** CLI erbjuder flera alternativ för att anpassa översättningsprocessen:

Kommando                                     | Beskrivning
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Översätter ditt projekt till angivna språk. Exempel: translate -l "es fr de" översätter till spanska, franska och tyska. Använd translate -l "all" för att översätta till alla stödda språk.
translate -l "language_codes" -u              | Uppdaterar översättningar genom att ta bort befintliga och skapa dem på nytt. Varning: Detta tar bort alla nuvarande översättningar för angivna språk.
translate -l "language_codes" -img            | Översätter endast bildfiler.
translate -l "language_codes" -md             | Översätter endast Markdown-filer.
translate -l "language_codes" -chk            | Kontrollerar översatta filer efter fel och försöker översätta igen vid behov.
translate -l "language_codes" -d              | Aktiverar debugläge för detaljerad loggning.
translate -l "language_codes" -r "root_dir"   | Anger projektets rotmapp
translate -l "language_codes" -f              | Använder snabb läge för bildöversättning (upp till 3x snabbare bearbetning med liten förlust i kvalitet och justering).
translate -l "language_codes" -y              | Bekräftar automatiskt alla promptar (användbart för CI/CD-pipelines)
translate -l "language_codes" --help          | Hjälpinformation inom CLI som visar tillgängliga kommandon

### Exempel på användning:

  1. Standardbeteende (lägg till nya översättningar utan att ta bort befintliga):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lägg bara till nya koreanska bildöversättningar (inga befintliga översättningar tas bort):    translate -l "ko" -img

  3. Uppdatera alla koreanska översättningar (Varning: Detta tar bort alla befintliga koreanska översättningar innan ny översättning):    translate -l "ko" -u

  4. Uppdatera endast koreanska bilder (Varning: Detta tar bort alla befintliga koreanska bilder innan ny översättning):    translate -l "ko" -img -u

  5. Lägg till nya markdown-översättningar för koreanska utan att påverka andra översättningar:    translate -l "ko" -md

  6. Kontrollera översatta filer efter fel och försök översätta igen vid behov: translate -l "ko" -chk

  7. Kontrollera översatta filer efter fel och försök översätta igen (endast markdown): translate -l "ko" -chk -md

  8. Kontrollera översatta filer efter fel och försök översätta igen (endast bilder): translate -l "ko" -chk -img

  9. Använd snabb läge för bildöversättning:    translate -l "ko" -img -f

  10. Exempel på debugläge: - translate -l "ko" -d: Aktivera debug-loggning.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.