<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:49:56+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "sv"
}
-->
# Översätt ditt projekt med Co-op Translator

**Co-op Translator** är ett kommandoradsverktyg (CLI) som hjälper dig att översätta markdown- och bildfiler i ditt projekt till flera språk. Den här sektionen förklarar hur du använder verktyget, går igenom olika CLI-alternativ och ger exempel för olika användningsområden.

> [!NOTE]
> För en komplett lista över kommandon och deras detaljerade beskrivningar, se [Command reference](./command-reference.md).

---

## Exempelscenarier och kommandon

Här är några vanliga användningsfall för **Co-op Translator** tillsammans med lämpliga kommandon att köra.

### 1. Grundläggande översättning (ett språk)

För att översätta hela ditt projekt (markdown-filer och bilder) till ett språk, till exempel koreanska, använd följande kommando:

```bash
translate -l "ko"
```

Det här kommandot översätter alla markdown- och bildfiler till koreanska och lägger till nya översättningar utan att ta bort några befintliga.

> [!TIP]
>
> Vill du se vilka språkkoder som finns tillgängliga i **Co-op Translator**? Besök avsnittet [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) i repot för mer information.

#### Exempel från Phi-3 CookBook

I **Phi-3 CookBook** använde jag följande metod för att lägga till koreansk översättning för befintliga markdown-filer och bilder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Översätta till flera språk

För att översätta ditt projekt till flera språk (t.ex. spanska, franska och tyska) använd detta kommando:

```bash
translate -l "es fr de"
```

Det här kommandot översätter projektet till spanska, franska och tyska och lägger till nya översättningar utan att skriva över befintliga.

#### Exempel från Phi-3 CookBook

I **Phi-3 CookBook**, efter att ha hämtat de senaste ändringarna för att återspegla de senaste committerna, använde jag följande metod för att översätta nyligen tillagda markdown-filer och bilder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Även om det generellt rekommenderas att översätta ett språk i taget, kan det i situationer som denna där specifika ändringar behöver läggas till vara effektivt att översätta flera språk samtidigt.

### 3. Uppdatera översättningar (tar bort befintliga översättningar)

För att uppdatera befintliga översättningar (dvs. ta bort nuvarande översättningar och ersätta dem med nya) använd `-u`-alternativet. Detta kommer att ta bort alla befintliga översättningar för angivna språk och översätta dem på nytt.

```bash
translate -l "ko" -u
```

Varning: Detta kommando kommer att be om bekräftelse innan det fortsätter med att ta bort befintliga översättningar.

#### Exempel från Phi-3 CookBook

I **Phi-3 CookBook** använde jag följande metod för att uppdatera alla översatta filer på spanska. Jag rekommenderar att använda denna metod när det finns betydande förändringar i originalinnehållet över flera markdown-dokument. Om det bara finns några få översatta markdown-filer att uppdatera är det mer effektivt att manuellt ta bort dessa specifika filer och sedan använda `-a`-metoden för att lägga till uppdaterade översättningar.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Översätta endast bilder

För att översätta endast bildfilerna i ditt projekt, använd `-img`-alternativet:

```bash
translate -l "ko" -img
```

Det här kommandot översätter endast bilderna till koreanska utan att påverka några markdown-filer.

### 6. Översätta endast markdown-filer

För att översätta endast markdown-filerna i ditt projekt, använd `-md`-alternativet:

```bash
translate -l "ko" -md
```

### 7. Kontrollera fel i översatta filer

Om du vill kontrollera översatta filer för fel och försöka översätta på nytt vid behov, använd `-chk`-alternativet:

```bash
translate -l "ko" -chk
```

Det här kommandot skannar de översatta markdown-filerna och försöker översätta på nytt för eventuella filer med fel.

#### Exempel från Phi-3 CookBook

I **Phi-3 CookBook** använde jag följande metod för att kontrollera översättningsfel i de koreanska filerna och automatiskt försöka översätta på nytt för filer där problem upptäcktes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Detta alternativ kontrollerar översättningsfel. För närvarande flaggas en fil som felaktig om skillnaden i radbrytningar mellan original- och översatt fil är mer än sex. Jag planerar att förbättra detta kriterium för större flexibilitet i framtiden.

Till exempel är denna metod användbar för att upptäcka saknade delar eller korrupta översättningar, och den försöker automatiskt översätta om dessa filer.

Men om du redan vet vilka filer som är problematiska är det mer effektivt att manuellt ta bort dessa filer och använda `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`-alternativet:

```bash
translate -l "ko" -d
```

Detta kommando kör översättningen i felsökningsläge och ger extra logginformation som kan hjälpa dig att identifiera problem under översättningsprocessen.

#### Exempel från Phi-3 CookBook

I **Phi-3 CookBook** stötte jag på ett problem där översättningar med många länkar i markdown-filer orsakade formateringsfel, såsom brutna översättningar och ignorerade radbrytningar. För att diagnostisera detta problem använde jag `-d`-alternativet för att se hur översättningsprocessen fungerar.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Översätta alla språk

Om du vill översätta projektet till alla stödda språk, använd nyckelordet all.

> [!WARNING]
> Att översätta alla språk samtidigt kan ta betydande tid beroende på projektets storlek. Till exempel tog det ungefär 2 timmar att översätta **Phi-3 CookBook** till spanska. Med tanke på omfattningen är det inte praktiskt för en person att hantera 20 språk. Det rekommenderas att dela upp arbetet mellan flera bidragsgivare, där varje ansvarar för ett eller två språk, och uppdaterar översättningarna successivt.

```bash
translate -l "all"
```

Det här kommandot översätter projektet till alla tillgängliga språk. Om du fortsätter kan översättningen ta mycket tid beroende på projektets storlek.

> [!TIP]
>
> ### Manuellt ta bort översatta filer (valfritt)
> Översatta filer upptäcks och rensas nu automatiskt när en källfil uppdateras.
>
> Om du däremot vill uppdatera en översättning manuellt – till exempel för att göra om en specifik fil eller åsidosätta systemets beteende – kan du använda följande kommando för att ta bort alla versioner av filen i språkmapparna.
>
> ### På Windows:
> 1. **Använda Kommandotolken**:
>    - Öppna Kommandotolken.
>    - Navigera till mappen där filerna finns med `cd`-kommandot.
>    - Använd följande kommando för att ta bort filer:
>      ```
>      del /s *filename*
>      ```
>      Alternativet `/s` söker även i undermappar.
>
> 2. **Använda PowerShell**:
>    - Öppna PowerShell.
>    - Kör detta kommando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Byt ut `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find`-kommandot:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Byt ut `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l`-kommandot för att uppdatera de senaste filändringarna.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.