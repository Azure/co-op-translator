<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T11:37:28+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "nl"
}
-->
# Commandoreferentie

De **Co-op Translator** CLI biedt verschillende opties om het vertaalproces aan te passen:

Command                                       | Beschrijving
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Vertaalt je project naar opgegeven talen. Voorbeeld: translate -l "es fr de" vertaalt naar Spaans, Frans en Duits. Gebruik translate -l "all" om naar alle ondersteunde talen te vertalen.
translate -l "language_codes" -u              | Werkt vertalingen bij door bestaande te verwijderen en opnieuw aan te maken. Waarschuwing: Dit verwijdert alle huidige vertalingen voor opgegeven talen.
translate -l "language_codes" -img            | Vertaalt alleen afbeeldingsbestanden.
translate -l "language_codes" -md             | Vertaalt alleen Markdown-bestanden.
translate -l "language_codes" -nb             | Vertaalt alleen Jupyter notebook-bestanden (.ipynb).
translate -l "language_codes" --fix           | Vertaalt opnieuw bestanden met lage betrouwbaarheidscores op basis van eerdere evaluatieresultaten.
translate -l "language_codes" -d              | Zet debugmodus aan voor gedetailleerde logging.
translate -l "language_codes" --save-logs, -s | Sla DEBUG-logs op in bestanden onder <root_dir>/logs/ (console blijft geregeld door -d)
translate -l "language_codes" -r "root_dir"   | Geeft de hoofdmap van het project op
translate -l "language_codes" -f              | Gebruikt snelle modus voor afbeeldingsvertaling (tot 3x sneller plotten met lichte concessies in kwaliteit en uitlijning).
translate -l "language_codes" -y              | Bevestigt automatisch alle prompts (handig voor CI/CD pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Schakelt het toevoegen van een machinevertalingsdisclaimer in of uit voor vertaalde markdown en notebooks (standaard: ingeschakeld).
translate -l "language_codes" --help          | Toont helpdetails binnen de CLI met beschikbare commando's
evaluate -l "language_code"                  | Evalueert de vertaalkwaliteit voor een specifieke taal en geeft betrouwbaarheidscores
evaluate -l "language_code" -c 0.8           | Evalueert vertalingen met een aangepaste betrouwbaarheidsdrempel
evaluate -l "language_code" -f               | Snelle evaluatiemodus (alleen op regels gebaseerd, geen LLM)
evaluate -l "language_code" -D               | Diepe evaluatiemodus (alleen LLM-gebaseerd, grondiger maar trager)
evaluate -l "language_code" --save-logs, -s  | Sla DEBUG-logs op in bestanden onder <root_dir>/logs/
migrate-links -l "language_codes"             | Verwerkt vertaalde Markdown-bestanden opnieuw om links naar notebooks (.ipynb) bij te werken. Geeft de voorkeur aan vertaalde notebooks indien beschikbaar; anders kan teruggevallen worden op originele notebooks.
migrate-links -l "language_codes" -r          | Specificeer de hoofdmap van het project (standaard: huidige map).
migrate-links -l "language_codes" --dry-run   | Laat zien welke bestanden zouden veranderen zonder wijzigingen weg te schrijven.
migrate-links -l "language_codes" --no-fallback-to-original | Herschrijf links naar originele notebooks niet wanneer vertaalde versies ontbreken (werk alleen bij als vertaalde versie bestaat).
migrate-links -l "language_codes" -d          | Zet debugmodus aan voor gedetailleerde logging.
migrate-links -l "language_codes" --save-logs, -s | Sla DEBUG-logs op in bestanden onder <root_dir>/logs/
migrate-links -l "all" -y                      | Verwerk alle talen en bevestig automatisch de waarschuwingsprompt.

## Voorbeelden van gebruik

  1. Standaardgedrag (voeg nieuwe vertalingen toe zonder bestaande te verwijderen):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Voeg alleen nieuwe Koreaanse afbeeldingsvertalingen toe (bestaande vertalingen blijven behouden):    translate -l "ko" -img

  3. Werk alle Koreaanse vertalingen bij (Waarschuwing: Dit verwijdert alle bestaande Koreaanse vertalingen voordat opnieuw vertaald wordt):    translate -l "ko" -u

  4. Werk alleen Koreaanse afbeeldingen bij (Waarschuwing: Dit verwijdert alle bestaande Koreaanse afbeeldingen voordat opnieuw vertaald wordt):    translate -l "ko" -img -u

  5. Voeg nieuwe markdownvertalingen voor Koreaans toe zonder andere vertalingen te beïnvloeden:    translate -l "ko" -md

  6. Herstel vertalingen met lage betrouwbaarheid op basis van eerdere evaluaties: translate -l "ko" --fix

  7. Herstel vertalingen met lage betrouwbaarheid voor specifieke bestanden alleen (markdown): translate -l "ko" --fix -md

  8. Herstel vertalingen met lage betrouwbaarheid voor specifieke bestanden alleen (afbeeldingen): translate -l "ko" --fix -img

  9. Gebruik snelle modus voor afbeeldingsvertaling:    translate -l "ko" -img -f

  10. Herstel vertalingen met lage betrouwbaarheid met aangepaste drempel: translate -l "ko" --fix -c 0.8

  11. Voorbeeld debugmodus: - translate -l "ko" -d: Zet debuglogging aan.
  12. Logs opslaan in bestanden: translate -l "ko" -s
  13. Console DEBUG en bestand DEBUG: translate -l "ko" -d -s
  14. Vertalen zonder machinevertalingsdisclaimers toe te voegen aan output: translate -l "ko" --no-disclaimer

  15. Migreer notebooklinks voor Koreaanse vertalingen (werk links bij naar vertaalde notebooks indien beschikbaar):    migrate-links -l "ko"

  15. Migreer links met dry-run (geen bestandswijzigingen):    migrate-links -l "ko" --dry-run

  16. Werk links alleen bij als vertaalde notebooks bestaan (geen terugval naar origineel):    migrate-links -l "ko" --no-fallback-to-original

  17. Verwerk alle talen met bevestigingsprompt:    migrate-links -l "all"

  18. Verwerk alle talen en bevestig automatisch:    migrate-links -l "all" -y
  19. Logs opslaan in bestanden voor migrate-links:    migrate-links -l "ko ja" -s

### Evaluatievoorbeelden

> [!WARNING]  
> **Bètafunctie**: De evaluatiefunctie is momenteel in bèta. Deze functie is uitgebracht om vertaalde documenten te evalueren, en de evaluatiemethoden en gedetailleerde implementatie zijn nog in ontwikkeling en kunnen veranderen.

  1. Evalueer Koreaanse vertalingen: evaluate -l "ko"

  2. Evalueer met aangepaste betrouwbaarheidsdrempel: evaluate -l "ko" -c 0.8

  3. Snelle evaluatie (alleen op regels gebaseerd): evaluate -l "ko" -f

  4. Diepe evaluatie (alleen LLM-gebaseerd): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->