<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:30:12+00:00",
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
translate -l "language_codes" -chk            | Controleert vertaalde bestanden op fouten en probeert vertalingen opnieuw als dat nodig is.  
translate -l "language_codes" -d              | Zet debugmodus aan voor gedetailleerde logging.  
translate -l "language_codes" -r "root_dir"   | Geeft de rootdirectory van het project op.  
translate -l "language_codes" -f              | Gebruikt snelle modus voor afbeeldingvertaling (tot 3x sneller, met een lichte afname in kwaliteit en uitlijning).  
translate -l "language_codes" -y              | Bevestigt automatisch alle prompts (handig voor CI/CD-pijplijnen).  
translate -l "language_codes" --help          | Toont helpdetails binnen de CLI met beschikbare commando’s.  

### Voorbeeldgebruik:  

1. Standaardgedrag (voegt nieuwe vertalingen toe zonder bestaande te verwijderen):  
   translate -l "ko"  
   translate -l "es fr de" -r "./my_project"  

2. Alleen nieuwe Koreaanse vertalingen voor afbeeldingen toevoegen (bestaande vertalingen blijven behouden):  
   translate -l "ko" -img  

3. Alle Koreaanse vertalingen bijwerken (Waarschuwing: Dit verwijdert alle bestaande Koreaanse vertalingen voordat opnieuw wordt vertaald):  
   translate -l "ko" -u  

4. Alleen Koreaanse afbeeldingen bijwerken (Waarschuwing: Dit verwijdert alle bestaande Koreaanse afbeeldingen voordat opnieuw wordt vertaald):  
   translate -l "ko" -img -u  

5. Nieuwe markdownvertalingen voor Koreaans toevoegen zonder andere vertalingen te beïnvloeden:  
   translate -l "ko" -md  

6. Vertaalde bestanden controleren op fouten en vertalingen opnieuw proberen indien nodig:  
   translate -l "ko" -chk  

7. Vertaalde bestanden controleren op fouten en vertalingen opnieuw proberen (alleen markdown):  
   translate -l "ko" -chk -md  

8. Vertaalde bestanden controleren op fouten en vertalingen opnieuw proberen (alleen afbeeldingen):  
   translate -l "ko" -chk -img  

9. Snelle modus gebruiken voor afbeeldingvertaling:  
   translate -l "ko" -img -f  

10. Voorbeeld debugmodus:  
    translate -l "ko" -d: Debuglogging inschakelen.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.