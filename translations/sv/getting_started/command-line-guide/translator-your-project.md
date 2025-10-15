<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:19:56+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "sv"
}
-->
# Översätt ditt projekt med Co-op Translator

**Co-op Translator** är ett kommandoradsverktyg (CLI) som hjälper dig att översätta markdown- och bildfiler i ditt projekt till flera språk. Den här sektionen förklarar hur du använder verktyget, går igenom olika CLI-alternativ och ger exempel för olika användningsområden.

> [!NOTE]
> För en komplett lista över kommandon och deras detaljerade beskrivningar, se [Kommandoreferens](./command-reference.md).

---

## Exempelscenarier och kommandon

Här är några vanliga användningsområden för **Co-op Translator** tillsammans med lämpliga kommandon.

### 1. Grundläggande översättning (Ett språk)

För att översätta hela ditt projekt (markdown-filer och bilder) till ett språk, till exempel koreanska, använd följande kommando:

```bash
translate -l "ko"
```

Detta kommando översätter alla markdown- och bildfiler till koreanska och lägger till nya översättningar utan att ta bort befintliga.

> [!TIP]
>
> Vill du se vilka språkkoder som finns tillgängliga i **Co-op Translator**? Besök avsnittet [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) i repot för mer information.

#### Exempel i Phi-3 CookBook

I **Phi-3 CookBook** använde jag följande metod för att lägga till koreansk översättning för befintliga markdown-filer och bilder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Översätta till flera språk

För att översätta ditt projekt till flera språk (t.ex. spanska, franska och tyska), använd detta kommando:

```bash
translate -l "es fr de"
```

Detta kommando översätter projektet till spanska, franska och tyska och lägger till nya översättningar utan att skriva över befintliga.

#### Exempel i Phi-3 CookBook

I **Phi-3 CookBook**, efter att ha hämtat de senaste ändringarna för att få med de senaste commitarna, använde jag följande metod för att översätta nyligen tillagda markdown-filer och bilder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Det är oftast bäst att översätta ett språk i taget, men i situationer som denna där specifika ändringar behöver läggas till kan det vara effektivt att översätta flera språk samtidigt.

### 3. Uppdatera översättningar (Tar bort befintliga översättningar)

För att uppdatera befintliga översättningar (dvs. ta bort nuvarande översättningar och ersätta dem med nya), använd alternativet `-u`. Detta tar bort alla befintliga översättningar för de angivna språken och översätter dem på nytt.

```bash
translate -l "ko" -u
```

Varning: Detta kommando kommer att be dig bekräfta innan befintliga översättningar tas bort.

#### Exempel i Phi-3 CookBook

I **Phi-3 CookBook** använde jag följande metod för att uppdatera alla översatta filer på spanska. Jag rekommenderar att använda denna metod när det är stora ändringar i originalinnehållet över flera markdown-dokument. Om det bara är några få översatta markdown-filer som behöver uppdateras är det mer effektivt att manuellt ta bort just de filerna och sedan använda `-a`-metoden för att lägga till de uppdaterade översättningarna.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Endast översätta bilder

För att endast översätta bildfilerna i ditt projekt, använd alternativet `-img`:

```bash
translate -l "ko" -img
```

Detta kommando översätter endast bilderna till koreanska utan att påverka några markdown-filer.

### 6. Endast översätta markdown-filer

För att endast översätta markdown-filerna i ditt projekt, använd alternativet `-md`:

```bash
translate -l "ko" -md
```

#### Exempel i Phi-3 CookBook

I **Phi-3 CookBook** använde jag följande metod för att kontrollera översättningsfel i de koreanska filerna och automatiskt försöka översätta om de filer där fel upptäcktes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Detta alternativ kontrollerar översättningsfel. För närvarande, om skillnaden i radbrytningar mellan original- och översättningsfilen är mer än sex, flaggas filen som felaktigt översatt. Jag planerar att förbättra detta kriterium för större flexibilitet framöver.

Till exempel är denna metod användbar för att upptäcka saknade delar eller korrupta översättningar, och den försöker automatiskt översätta om dessa filer.

Men om du redan vet vilka filer som är problematiska är det mer effektivt att manuellt ta bort dessa filer och använda `-a`-alternativet för att översätta dem på nytt.

### 8. Felsökningsläge

För att aktivera detaljerad loggning för felsökning, använd alternativet `-d`:

```bash
translate -l "ko" -d
```

Detta kommando kör översättningen i felsökningsläge och ger extra logginformation som kan hjälpa dig att identifiera problem under översättningsprocessen.

#### Exempel i Phi-3 CookBook

I **Phi-3 CookBook** stötte jag på ett problem där översättningar med många länkar i markdown-filer orsakade formateringsfel, som trasiga översättningar och ignorerade radbrytningar. För att felsöka detta använde jag `-d`-alternativet för att se hur översättningsprocessen fungerade.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Översätta till alla språk

Om du vill översätta projektet till alla språk som stöds, använd nyckelordet all.

> [!WARNING]
> Att översätta till alla språk på en gång kan ta mycket lång tid beroende på projektets storlek. Till exempel tog det cirka 2 timmar att översätta **Phi-3 CookBook** till spanska. Med tanke på omfattningen är det inte rimligt att en person hanterar 20 språk. Det är bättre att dela upp arbetet mellan flera bidragsgivare, där varje person ansvarar för ett eller två språk, och uppdatera översättningarna gradvis.

```bash
translate -l "all"
```

Detta kommando översätter projektet till alla tillgängliga språk. Om du fortsätter kan översättningen ta lång tid beroende på projektets storlek.

> [!TIP]
>
> ### Ta bort översatta filer manuellt (valfritt)
> Översatta filer upptäcks och rensas nu automatiskt när en källfil uppdateras.
>
> Men om du vill uppdatera en översättning manuellt – till exempel för att göra om en specifik fil eller åsidosätta systemets beteende – kan du använda följande kommando för att ta bort alla versioner av filen i språkmapparna.
>
> ### På Windows:
> 1. **Med Kommandotolken**:
>    - Öppna Kommandotolken.
>    - Navigera till mappen där filerna finns med kommandot `cd`.
>    - Använd följande kommando för att ta bort filer:
>      ```
>      del /s *filename*
>      ```
>      Ersätt `filename` med den del av filnamnet du letar efter. `/s`-alternativet söker i undermappar också.
>
> 2. **Med PowerShell**:
>    - Öppna PowerShell.
>    - Kör detta kommando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Ersätt `"C:\YourPath"` med mappsökvägen och `filename` med det specifika namnet.
>
> ### På macOS/Linux:
> 1. **Med Terminalen**:
>   - Öppna Terminalen.
>   - Navigera till katalogen med `cd`.
>   - Använd kommandot `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Ersätt `filename` med det specifika namnet.
>
> Kontrollera alltid filerna noggrant innan du tar bort dem för att undvika oavsiktlig förlust.
>
> När du har tagit bort de filer som behöver ersättas, kör bara ditt `translate -l`-kommando igen för att uppdatera de senaste filändringarna.

---

**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.