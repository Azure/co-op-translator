<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:28:22+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "nl"
}
-->
# Microsoft Co-op Translator Probleemoplossingsgids

## Overzicht  
De Microsoft Co-Op Translator is een krachtig hulpmiddel voor het naadloos vertalen van Markdown-documenten. Deze gids helpt je bij het oplossen van veelvoorkomende problemen die je tegenkomt bij het gebruik van de tool.

## Veelvoorkomende problemen en oplossingen

### 1. Markdown-tag probleem  
**Probleem:** Het vertaalde Markdown-document bevat een `markdown`-tag bovenaan, wat zorgt voor weergaveproblemen.

**Oplossing:** Verwijder eenvoudigweg de `markdown`-tag bovenaan het bestand. Hierdoor wordt het Markdown-bestand correct weergegeven.

**Stappen:**  
1. Open het vertaalde Markdown (`.md`) bestand.  
2. Zoek de `markdown`-tag bovenaan het document.  
3. Verwijder de `markdown`-tag.  
4. Sla de wijzigingen in het bestand op.  
5. Open het bestand opnieuw om te controleren of het correct wordt weergegeven.

### 2. URL-probleem bij ingesloten afbeeldingen  
**Probleem:** De URL’s van ingesloten afbeeldingen komen niet overeen met de taalinstelling, wat leidt tot verkeerde of ontbrekende afbeeldingen.

**Oplossing:** Controleer de URL van ingesloten afbeeldingen en zorg dat deze overeenkomen met de taalinstelling. Alle afbeeldingen bevinden zich in de `translated_images`-map en elke afbeelding heeft een taalinstelling in de bestandsnaam.

**Stappen:**  
1. Open het vertaalde Markdown-document.  
2. Identificeer de ingesloten afbeeldingen en hun URL’s.  
3. Controleer of de taalinstelling in de bestandsnaam van de afbeelding overeenkomt met de taal van het document.  
4. Werk de URL’s indien nodig bij.  
5. Sla de wijzigingen op en open het document opnieuw om te bevestigen dat de afbeeldingen correct worden weergegeven.

### 3. Vertaalnauwkeurigheid  
**Probleem:** De vertaalde inhoud is niet nauwkeurig of vereist verdere bewerking.

**Oplossing:** Bekijk het vertaalde document en breng de nodige aanpassingen aan om de nauwkeurigheid en leesbaarheid te verbeteren.

**Stappen:**  
1. Open het vertaalde document.  
2. Bekijk de inhoud zorgvuldig.  
3. Breng de nodige aanpassingen aan om de vertaalnauwkeurigheid te verbeteren.  
4. Sla de wijzigingen op.

### 4. Problemen met bestandsopmaak  
**Probleem:** De opmaak van het vertaalde document is incorrect. Dit kan voorkomen bij tabellen; hier zal extra ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` de tabelproblemen aanpakken.

**Stappen:**  
1. Open het vertaalde document.  
2. Vergelijk het met het originele document om opmaakproblemen te identificeren.  
3. Pas de opmaak aan zodat deze overeenkomt met het originele document.  
4. Sla de wijzigingen op.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de originele taal geldt als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.