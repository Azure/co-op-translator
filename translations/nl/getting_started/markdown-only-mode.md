<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:41:29+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "nl"
}
-->
# Gebruik van Alleen Markdown-modus

## Introductie
De alleen Markdown-modus is ontworpen om alleen de Markdown-inhoud van je project te vertalen. Deze modus slaat het vertalen van afbeeldingen over en richt zich uitsluitend op de tekstuele inhoud, wat ideaal is in situaties waarin het vertalen van afbeeldingen niet nodig is of wanneer de vereiste omgevingsvariabelen voor Computer Vision niet zijn ingesteld.

## Wanneer te gebruiken
- Wanneer de omgevingsvariabelen gerelateerd aan Computer Vision niet zijn geconfigureerd.
- Wanneer je alleen de tekstinhoud wilt vertalen zonder de afbeeldingslinks aan te passen.
- Wanneer dit expliciet door de gebruiker is aangegeven met de `-md` opdrachtregeloptie.

## Hoe te activeren
Om de alleen Markdown-modus te activeren, gebruik je de `-md` optie in je opdracht. Bijvoorbeeld:
```
translate -l "ko" -md
```

Of als de omgevingsvariabelen voor Computer Vision niet zijn ingesteld. Het uitvoeren van `translate -l "ko"` schakelt automatisch over naar alleen Markdown-modus.

```
translate -l "ko"
```

Deze opdracht vertaalt de Markdown-inhoud naar het Koreaans en laat de afbeeldingslinks naar hun originele paden wijzen, in plaats van ze aan te passen naar vertaalde afbeeldingspaden.

## Gedrag
In alleen Markdown-modus:
- Slaat het vertaalproces de stap voor het vertalen van afbeeldingen over.
- Blijven de afbeeldingslinks in de Markdown ongewijzigd en verwijzen ze naar hun originele paden.

## Voorbeelden
### Voor
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.nl.png)
```
### Na gebruik van alleen Markdown-modus
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.nl.png)
```

## Problemen oplossen
- Zorg ervoor dat de `-md` optie correct is opgegeven in de opdracht.
- Controleer of er geen Computer Vision-omgevingsvariabelen zijn die het proces verstoren.

## Conclusie
De alleen Markdown-modus biedt een eenvoudige manier om tekstinhoud te vertalen zonder afbeeldingslinks aan te passen. Het is vooral handig wanneer het vertalen van afbeeldingen niet nodig is of wanneer je werkt in omgevingen zonder Computer Vision-configuratie.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.