<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:51:27+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "nl"
}
-->
# Vertaal je project met Co-op Translator

De **Co-op Translator** is een command-line interface (CLI) tool die je helpt om markdown- en afbeeldingsbestanden in je project naar meerdere talen te vertalen. In deze sectie wordt uitgelegd hoe je de tool gebruikt, worden de verschillende CLI-opties behandeld en vind je voorbeelden voor diverse gebruikssituaties.

> [!NOTE]
> Voor een volledige lijst met commando’s en hun gedetailleerde beschrijvingen, zie de [Command reference](./command-reference.md).

---

## Voorbeeldscenario’s en commando’s

Hier zijn een paar veelvoorkomende gebruikssituaties voor de **Co-op Translator**, met de bijbehorende commando’s die je kunt uitvoeren.

### 1. Basisvertaling (één taal)

Om je hele project (markdown-bestanden en afbeeldingen) in één taal te vertalen, bijvoorbeeld Koreaans, gebruik je het volgende commando:

```bash
translate -l "ko"
```

Dit commando vertaalt alle markdown- en afbeeldingsbestanden naar het Koreaans, en voegt nieuwe vertalingen toe zonder bestaande te verwijderen.

> [!TIP]
>
> Wil je zien welke taalcodes beschikbaar zijn in **Co-op Translator**? Kijk dan in de sectie [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) in de repository voor meer informatie.

#### Voorbeeld in Phi-3 CookBook

In de **Phi-3 CookBook** heb ik de volgende methode gebruikt om de Koreaanse vertaling toe te voegen voor de bestaande markdown-bestanden en afbeeldingen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Vertalen naar meerdere talen

Om je project naar meerdere talen te vertalen (bijvoorbeeld Spaans, Frans en Duits), gebruik je dit commando:

```bash
translate -l "es fr de"
```

Dit commando vertaalt het project naar Spaans, Frans en Duits, en voegt nieuwe vertalingen toe zonder bestaande te overschrijven.

#### Voorbeeld in Phi-3 CookBook

In de **Phi-3 CookBook**, nadat ik de laatste wijzigingen had binnengehaald om de meest recente commits te verwerken, gebruikte ik de volgende methode om nieuw toegevoegde markdown-bestanden en afbeeldingen te vertalen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Hoewel het over het algemeen aan te raden is om één taal tegelijk te vertalen, kan het in situaties zoals deze, waarbij specifieke wijzigingen moeten worden toegevoegd, efficiënt zijn om meerdere talen tegelijk te vertalen.

### 3. Vertalingen bijwerken (bestaande vertalingen verwijderen)

Om bestaande vertalingen bij te werken (oftewel de huidige vertalingen te verwijderen en te vervangen door nieuwe), gebruik je de `-u` optie. Dit verwijdert alle bestaande vertalingen voor de opgegeven talen en vertaalt ze opnieuw.

```bash
translate -l "ko" -u
```

Waarschuwing: Dit commando vraagt om bevestiging voordat het de bestaande vertalingen verwijdert.

#### Voorbeeld in Phi-3 CookBook

In de **Phi-3 CookBook** gebruikte ik de volgende methode om alle vertaalde bestanden in het Spaans bij te werken. Ik raad deze methode aan wanneer er grote wijzigingen zijn in de originele inhoud over meerdere markdown-documenten. Als er maar een paar vertaalde markdown-bestanden bijgewerkt moeten worden, is het efficiënter om die specifieke bestanden handmatig te verwijderen en vervolgens de `-a` methode te gebruiken om de bijgewerkte vertalingen toe te voegen.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Alleen afbeeldingen vertalen

Om alleen de afbeeldingsbestanden in je project te vertalen, gebruik je de `-img` optie:

```bash
translate -l "ko" -img
```

Dit commando vertaalt alleen de afbeeldingen naar het Koreaans, zonder de markdown-bestanden aan te passen.

### 6. Alleen markdown-bestanden vertalen

Om alleen de markdown-bestanden in je project te vertalen, gebruik je de `-md` optie:

```bash
translate -l "ko" -md
```

### 7. Controleren op fouten in vertaalde bestanden

Als je vertaalde bestanden wilt controleren op fouten en indien nodig de vertaling opnieuw wilt proberen, gebruik je de `-chk` optie:

```bash
translate -l "ko" -chk
```

Dit commando scant de vertaalde markdown-bestanden en probeert de vertaling opnieuw voor bestanden met fouten.

#### Voorbeeld in Phi-3 CookBook

In de **Phi-3 CookBook** gebruikte ik de volgende methode om vertaalfouten in de Koreaanse bestanden te controleren en automatisch opnieuw te vertalen voor bestanden waarbij problemen werden gevonden.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Deze optie controleert op vertaalfouten. Momenteel wordt een bestand als foutief beschouwd als het verschil in regeleinden tussen het origineel en de vertaling groter is dan zes. Ik ben van plan deze criteria in de toekomst aan te passen voor meer flexibiliteit.

Deze methode is bijvoorbeeld handig om ontbrekende stukken of corrupte vertalingen te detecteren, en zal automatisch opnieuw vertalen voor die bestanden.

Als je echter al weet welke bestanden problemen geven, is het efficiënter om die bestanden handmatig te verwijderen en de `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` optie te gebruiken:

```bash
translate -l "ko" -d
```

Dit commando voert de vertaling uit in debug-modus en geeft extra loggegevens die kunnen helpen bij het opsporen van problemen tijdens het vertaalproces.

#### Voorbeeld in Phi-3 CookBook

In de **Phi-3 CookBook** kwam ik een probleem tegen waarbij vertalingen met veel links in markdown-bestanden voor formatteringsfouten zorgden, zoals verbroken vertalingen en genegeerde regeleinden. Om dit probleem te analyseren gebruikte ik de `-d` optie om te zien hoe het vertaalproces precies werkt.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Alle talen vertalen

Als je het project in alle ondersteunde talen wilt vertalen, gebruik dan het keyword all.

> [!WARNING]
> Het vertalen van alle talen tegelijk kan flink wat tijd kosten, afhankelijk van de grootte van het project. Bijvoorbeeld, het vertalen van de **Phi-3 CookBook** naar Spaans duurde ongeveer 2 uur. Gezien de omvang is het onpraktisch voor één persoon om 20 talen te beheren. Het is aan te raden het werk te verdelen over meerdere bijdragers, waarbij ieder één of twee talen beheert en de vertalingen geleidelijk bijwerkt.

```bash
translate -l "all"
```

Dit commando vertaalt het project naar alle beschikbare talen. Als je doorgaat, kan het vertalen flink wat tijd kosten, afhankelijk van de grootte van het project.

> [!TIP]
>
> ### Vertaalde bestanden handmatig verwijderen (optioneel)
> Vertaalde bestanden worden nu automatisch gedetecteerd en opgeschoond wanneer een bronbestand wordt bijgewerkt.
>
> Wil je echter handmatig een vertaling bijwerken – bijvoorbeeld om een specifiek bestand opnieuw te doen of het systeemgedrag te overrulen – dan kun je het volgende commando gebruiken om alle versies van het bestand in de taalmappen te verwijderen.
>
> ### Op Windows:
> 1. **Via Command Prompt**:
>    - Open Command Prompt.
>    - Navigeer met het `cd` commando naar de map waar de bestanden staan.
>    - Gebruik het volgende commando om bestanden te verwijderen:
>      ```
>      del /s *filename*
>      ```
>      De optie `/s` zoekt ook in submappen.
>
> 2. **Via PowerShell**:
>    - Open PowerShell.
>    - Voer dit commando uit:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Vervang `"C:\YourPath"` door het pad waar de bestanden staan.
>
> 3. **Gebruik `cd` en `find` commando’s**:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Vervang `filename` door de naam van het bestand dat je zoekt.
>
> 4. **Gebruik `translate -l` commando** om de meest recente wijzigingen in bestanden bij te werken.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.