<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:30:33+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "nl"
}
-->
# Vertaal je project met Co-op Translator

De **Co-op Translator** is een command-line interface (CLI) tool die je helpt om markdown- en afbeeldingsbestanden in je project naar meerdere talen te vertalen. In deze sectie lees je hoe je de tool gebruikt, welke CLI-opties er zijn en vind je voorbeelden voor verschillende situaties.

> [!NOTE]
> Voor een volledige lijst met commando’s en uitgebreide beschrijvingen, kijk bij de [Command reference](./command-reference.md).

---

## Voorbeelden en commando’s

Hieronder vind je een aantal veelvoorkomende toepassingen van de **Co-op Translator**, met de bijbehorende commando’s.

### 1. Basisvertaling (één taal)

Wil je je hele project (markdown-bestanden en afbeeldingen) naar één taal vertalen, bijvoorbeeld Koreaans? Gebruik dan het volgende commando:

```bash
translate -l "ko"
```

Dit commando vertaalt alle markdown- en afbeeldingsbestanden naar het Koreaans en voegt nieuwe vertalingen toe zonder bestaande te verwijderen.

> [!TIP]
>
> Benieuwd welke taalcodes beschikbaar zijn in **Co-op Translator**? Kijk dan bij [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) in de repository voor meer informatie.

#### Voorbeeld in Phi-3 CookBook

In de **Phi-3 CookBook** heb ik de volgende methode gebruikt om de Koreaanse vertaling toe te voegen voor de bestaande markdown-bestanden en afbeeldingen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Vertalen naar meerdere talen

Wil je je project naar meerdere talen vertalen (bijvoorbeeld Spaans, Frans en Duits)? Gebruik dan dit commando:

```bash
translate -l "es fr de"
```

Dit commando vertaalt het project naar Spaans, Frans en Duits en voegt nieuwe vertalingen toe zonder bestaande te overschrijven.

#### Voorbeeld in Phi-3 CookBook

In de **Phi-3 CookBook** heb ik, nadat ik de laatste wijzigingen had opgehaald om de nieuwste commits te verwerken, de volgende methode gebruikt om nieuw toegevoegde markdown-bestanden en afbeeldingen te vertalen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Het is meestal aan te raden om één taal tegelijk te vertalen, maar in situaties zoals deze, waarin specifieke wijzigingen moeten worden toegevoegd, kan het efficiënt zijn om meerdere talen tegelijk te vertalen.

### 3. Vertalingen bijwerken (verwijdert bestaande vertalingen)

Wil je bestaande vertalingen bijwerken (dus de huidige vertalingen verwijderen en vervangen door nieuwe)? Gebruik dan de `-u` optie. Hiermee worden alle bestaande vertalingen voor de opgegeven talen verwijderd en opnieuw vertaald.

```bash
translate -l "ko" -u
```

Let op: Dit commando vraagt om bevestiging voordat de bestaande vertalingen worden verwijderd.

#### Voorbeeld in Phi-3 CookBook

In de **Phi-3 CookBook** heb ik de volgende methode gebruikt om alle vertaalde bestanden in het Spaans bij te werken. Ik raad deze methode aan als er grote wijzigingen zijn in de originele inhoud over meerdere markdown-documenten. Als er maar een paar vertaalde markdown-bestanden zijn die je wilt bijwerken, is het efficiënter om die specifieke bestanden handmatig te verwijderen en daarna de `-a` methode te gebruiken om de bijgewerkte vertalingen toe te voegen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Alleen afbeeldingen vertalen

Wil je alleen de afbeeldingsbestanden in je project vertalen? Gebruik dan de `-img` optie:

```bash
translate -l "ko" -img
```

Dit commando vertaalt alleen de afbeeldingen naar het Koreaans, zonder de markdown-bestanden te wijzigen.

### 6. Alleen markdown-bestanden vertalen

Wil je alleen de markdown-bestanden in je project vertalen? Gebruik dan de `-md` optie:

```bash
translate -l "ko" -md
```

#### Voorbeeld in Phi-3 CookBook

In de **Phi-3 CookBook** heb ik de volgende methode gebruikt om vertaalfouten in de Koreaanse bestanden te controleren en automatisch opnieuw te vertalen voor bestanden waarbij problemen zijn gevonden.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Deze optie controleert op vertaalfouten. Op dit moment wordt een bestand als foutief gemarkeerd als het verschil in regelafbrekingen tussen het origineel en de vertaling groter is dan zes. Ik ben van plan om dit criterium in de toekomst flexibeler te maken.

Deze methode is bijvoorbeeld handig om ontbrekende stukken of corrupte vertalingen te detecteren, en zal automatisch opnieuw proberen te vertalen voor die bestanden.

Als je echter al weet welke bestanden problematisch zijn, is het efficiënter om die bestanden handmatig te verwijderen en de `-a` optie te gebruiken om ze opnieuw te vertalen.

### 8. Debugmodus

Wil je uitgebreide logging inschakelen voor het oplossen van problemen? Gebruik dan de `-d` optie:

```bash
translate -l "ko" -d
```

Dit commando voert de vertaling uit in debugmodus en geeft extra loginformatie die kan helpen om problemen tijdens het vertalen te vinden.

#### Voorbeeld in Phi-3 CookBook

In de **Phi-3 CookBook** kwam ik een probleem tegen waarbij vertalingen met veel links in markdown-bestanden formatteerfouten veroorzaakten, zoals kapotte vertalingen en genegeerde regelafbrekingen. Om dit probleem te onderzoeken, heb ik de `-d` optie gebruikt om te zien hoe het vertaalproces werkte.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Vertalen naar alle talen

Wil je het project naar alle ondersteunde talen vertalen? Gebruik dan het all keyword.

> [!WARNING]
> Alles in één keer vertalen kan veel tijd kosten, afhankelijk van de grootte van het project. Zo duurde het vertalen van de **Phi-3 CookBook** naar het Spaans ongeveer 2 uur. Gezien de omvang is het niet praktisch om als één persoon 20 talen te beheren. Het is aan te raden om het werk te verdelen over meerdere bijdragers, waarbij ieder één of twee talen beheert, en de vertalingen geleidelijk bij te werken.

```bash
translate -l "all"
```

Dit commando vertaalt het project naar alle beschikbare talen. Als je doorgaat, kan de vertaling veel tijd kosten, afhankelijk van de grootte van het project.

> [!TIP]
>
> ### Handmatig vertaalde bestanden verwijderen (optioneel)
> Vertaalde bestanden worden nu automatisch gedetecteerd en opgeschoond wanneer een bronbestand wordt bijgewerkt.
>
> Wil je toch handmatig een vertaling bijwerken – bijvoorbeeld om een specifiek bestand opnieuw te doen of het systeemgedrag te negeren – dan kun je met het volgende commando alle versies van het bestand in de taalmap verwijderen.
>
> ### Op Windows:
> 1. **Via Command Prompt**:
>    - Open Command Prompt.
>    - Navigeer naar de map waar de bestanden staan met het `cd` commando.
>    - Gebruik het volgende commando om bestanden te verwijderen:
>      ```
>      del /s *filename*
>      ```
>      Vervang `filename` door het specifieke deel van de bestandsnaam waar je naar zoekt. De `/s` optie zoekt ook in submappen.
>
> 2. **Via PowerShell**:
>    - Open PowerShell.
>    - Voer dit commando uit:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Vervang `"C:\YourPath"` door het map-pad en `filename` door de specifieke naam.
>
> ### Op macOS/Linux:
> 1. **Via Terminal**:
>   - Open Terminal.
>   - Navigeer naar de map met `cd`.
>   - Gebruik het `find` commando:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Vervang `filename` door de specifieke naam.
>
> Controleer altijd goed welke bestanden je verwijdert om per ongeluk verlies te voorkomen. 
>
> Nadat je de bestanden hebt verwijderd die je wilt vervangen, kun je gewoon opnieuw je `translate -l` commando uitvoeren om de nieuwste wijzigingen bij te werken.

---

**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.