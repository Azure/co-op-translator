<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:29:43+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "nl"
}
-->
# Commandoreferentie

De **Co-op Translator** CLI biedt verschillende opties om het vertaalproces aan te passen:

Commando                                       | Beschrijving
-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                  | Vertaalt je project naar de opgegeven talen. Voorbeeld: translate -l "es fr de" vertaalt naar Spaans, Frans en Duits. Gebruik translate -l "all" om naar alle ondersteunde talen te vertalen.
translate -l "language_codes" -u               | Werkt vertalingen bij door bestaande te verwijderen en opnieuw aan te maken. Waarschuwing: Dit verwijdert alle huidige vertalingen voor de opgegeven talen.
translate -l "language_codes" -img             | Vertaalt alleen afbeeldingsbestanden.
translate -l "language_codes" -md              | Vertaalt alleen Markdown-bestanden.
translate -l "language_codes" -nb              | Vertaalt alleen Jupyter notebook-bestanden (.ipynb).
translate -l "language_codes" --fix            | Vertaalt bestanden opnieuw met lage vertrouwensscores op basis van eerdere evaluatieresultaten.
translate -l "language_codes" -d               | Schakelt debugmodus in voor gedetailleerde logging.
translate -l "language_codes" --save-logs, -s  | Sla DEBUG-logs op in bestanden onder <root_dir>/logs/ (console blijft geregeld door -d)
translate -l "language_codes" -r "root_dir"    | Geeft de hoofdmap van het project op
translate -l "language_codes" -f               | Gebruikt snelle modus voor afbeeldingvertaling (tot 3x sneller plotten met een kleine concessie aan kwaliteit en uitlijning).
translate -l "language_codes" -y               | Bevestigt automatisch alle prompts (handig voor CI/CD pipelines)
translate -l "language_codes" --help           | Helpdetails binnen de CLI met beschikbare commando's
evaluate -l "language_code"                    | Evalueert de vertaalkwaliteit voor een specifieke taal en geeft vertrouwensscores
evaluate -l "language_code" -c 0.8             | Evalueert vertalingen met een aangepaste vertrouwensdrempel
evaluate -l "language_code" -f                 | Snelle evaluatiemodus (alleen regelgebaseerd, geen LLM)
evaluate -l "language_code" -D                 | Diepe evaluatiemodus (alleen LLM-gebaseerd, grondiger maar langzamer)
evaluate -l "language_code" --save-logs, -s    | Sla DEBUG-logs op in bestanden onder <root_dir>/logs/
migrate-links -l "language_codes"              | Verwerkt vertaalde Markdown-bestanden opnieuw om links naar notebooks (.ipynb) bij te werken. Geeft de voorkeur aan vertaalde notebooks indien beschikbaar; anders kan worden teruggevallen op originele notebooks.
migrate-links -l "language_codes" -r           | Geef de hoofdmap van het project op (standaard: huidige map).
migrate-links -l "language_codes" --dry-run    | Laat zien welke bestanden zouden veranderen zonder wijzigingen op te slaan.
migrate-links -l "language_codes" --no-fallback-to-original | Schrijf links niet om naar originele notebooks als vertaalde versies ontbreken (alleen bijwerken als vertaalde bestaan).
migrate-links -l "language_codes" -d           | Schakel debugmodus in voor gedetailleerde logging.
migrate-links -l "language_codes" --save-logs, -s | Sla DEBUG-logs op in bestanden onder <root_dir>/logs/
migrate-links -l "all" -y                      | Verwerk alle talen en bevestig automatisch de waarschuwingsprompt.

## Voorbeelden van gebruik

  1. Standaardgedrag (nieuwe vertalingen toevoegen zonder bestaande te verwijderen):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Alleen nieuwe Koreaanse afbeeldingvertalingen toevoegen (bestaande vertalingen blijven behouden):    translate -l "ko" -img

  3. Alle Koreaanse vertalingen bijwerken (Waarschuwing: Dit verwijdert alle bestaande Koreaanse vertalingen voordat er opnieuw wordt vertaald):    translate -l "ko" -u

  4. Alleen Koreaanse afbeeldingen bijwerken (Waarschuwing: Dit verwijdert alle bestaande Koreaanse afbeeldingen voordat er opnieuw wordt vertaald):    translate -l "ko" -img -u

  5. Nieuwe markdownvertalingen voor Koreaans toevoegen zonder andere vertalingen te beïnvloeden:    translate -l "ko" -md

  6. Vertalingen met lage vertrouwensscores herstellen op basis van eerdere evaluatieresultaten: translate -l "ko" --fix

  7. Vertalingen met lage vertrouwensscores herstellen voor specifieke bestanden (markdown): translate -l "ko" --fix -md

  8. Vertalingen met lage vertrouwensscores herstellen voor specifieke bestanden (afbeeldingen): translate -l "ko" --fix -img

  9. Snelle modus gebruiken voor afbeeldingvertaling:    translate -l "ko" -img -f

  10. Vertalingen met lage vertrouwensscores herstellen met aangepaste drempel: translate -l "ko" --fix -c 0.8

  11. Voorbeeld debugmodus: - translate -l "ko" -d: Schakel debuglogging in.
  12. Logs opslaan in bestanden: translate -l "ko" -s
  13. Console DEBUG en bestand DEBUG: translate -l "ko" -d -s

  14. Notebooklinks migreren voor Koreaanse vertalingen (links bijwerken naar vertaalde notebooks indien beschikbaar):    migrate-links -l "ko"

  15. Links migreren met dry-run (geen bestanden worden aangepast):    migrate-links -l "ko" --dry-run

  16. Alleen links bijwerken als vertaalde notebooks bestaan (niet terugvallen op originelen):    migrate-links -l "ko" --no-fallback-to-original

  17. Alle talen verwerken met bevestigingsprompt:    migrate-links -l "all"

  18. Alle talen verwerken en automatisch bevestigen:    migrate-links -l "all" -y
  19. Logs opslaan in bestanden voor migrate-links:    migrate-links -l "ko ja" -s

### Voorbeelden van evaluatie

> [!WARNING]  
> **Bètafunctie**: De evaluatiefunctie is momenteel in bèta. Deze functie is uitgebracht om vertaalde documenten te evalueren, en de evaluatiemethoden en gedetailleerde implementatie zijn nog in ontwikkeling en kunnen veranderen.

  1. Koreaanse vertalingen evalueren: evaluate -l "ko"

  2. Evalueren met aangepaste vertrouwensdrempel: evaluate -l "ko" -c 0.8

  3. Snelle evaluatie (alleen regelgebaseerd): evaluate -l "ko" -f

  4. Diepe evaluatie (alleen LLM-gebaseerd): evaluate -l "ko" -D

---

**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.