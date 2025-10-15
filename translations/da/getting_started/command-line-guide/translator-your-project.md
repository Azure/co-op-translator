<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:22:32+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "da"
}
-->
# Oversæt dit projekt med Co-op Translator

**Co-op Translator** er et kommandolinjeværktøj (CLI), der hjælper dig med at oversætte markdown- og billedfiler i dit projekt til flere sprog. Denne sektion forklarer, hvordan du bruger værktøjet, gennemgår de forskellige CLI-muligheder og giver eksempler på forskellige anvendelser.

> [!NOTE]
> For en komplet liste over kommandoer og deres detaljerede beskrivelser, se venligst [Command reference](./command-reference.md).

---

## Eksempelscenarier og kommandoer

Her er nogle typiske anvendelser af **Co-op Translator** samt de relevante kommandoer.

### 1. Grundlæggende oversættelse (ét sprog)

Hvis du vil oversætte hele dit projekt (markdown-filer og billeder) til ét sprog, f.eks. koreansk, skal du bruge denne kommando:

```bash
translate -l "ko"
```

Denne kommando oversætter alle markdown- og billedfiler til koreansk og tilføjer nye oversættelser uden at slette eksisterende.

> [!TIP]
>
> Vil du se, hvilke sprogkoder der er tilgængelige i **Co-op Translator**? Besøg afsnittet [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) i repoet for flere detaljer.

#### Eksempel med Phi-3 CookBook

I **Phi-3 CookBook** brugte jeg følgende metode til at tilføje koreansk oversættelse af de eksisterende markdown-filer og billeder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Oversættelse til flere sprog

Hvis du vil oversætte dit projekt til flere sprog (f.eks. spansk, fransk og tysk), skal du bruge denne kommando:

```bash
translate -l "es fr de"
```

Denne kommando oversætter projektet til spansk, fransk og tysk og tilføjer nye oversættelser uden at overskrive eksisterende.

#### Eksempel med Phi-3 CookBook

I **Phi-3 CookBook**, efter at have hentet de seneste ændringer for at afspejle de nyeste commits, brugte jeg følgende metode til at oversætte nyligt tilføjede markdown-filer og billeder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Det anbefales generelt at oversætte ét sprog ad gangen, men i situationer som denne, hvor specifikke ændringer skal tilføjes, kan det være effektivt at oversætte flere sprog på én gang.

### 3. Opdatering af oversættelser (sletter eksisterende oversættelser)

Hvis du vil opdatere eksisterende oversættelser (dvs. slette de nuværende oversættelser og erstatte dem med nye), skal du bruge `-u`-muligheden. Dette vil slette alle eksisterende oversættelser for de valgte sprog og oversætte dem igen.

```bash
translate -l "ko" -u
```

Advarsel: Denne kommando vil bede dig om bekræftelse, før de eksisterende oversættelser slettes.

#### Eksempel med Phi-3 CookBook

I **Phi-3 CookBook** brugte jeg følgende metode til at opdatere alle oversatte filer på spansk. Jeg anbefaler at bruge denne metode, når der er væsentlige ændringer i originalindholdet på tværs af flere markdown-dokumenter. Hvis der kun er få oversatte markdown-filer, der skal opdateres, er det mere effektivt manuelt at slette de specifikke filer og derefter bruge `-a`-metoden til at tilføje de opdaterede oversættelser.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Kun oversættelse af billeder

Hvis du kun vil oversætte billedfilerne i dit projekt, skal du bruge `-img`-muligheden:

```bash
translate -l "ko" -img
```

Denne kommando oversætter kun billederne til koreansk uden at påvirke markdown-filerne.

### 6. Kun oversættelse af markdown-filer

Hvis du kun vil oversætte markdown-filerne i dit projekt, skal du bruge `-md`-muligheden:

```bash
translate -l "ko" -md
```

#### Eksempel med Phi-3 CookBook

I **Phi-3 CookBook** brugte jeg følgende metode til at tjekke for oversættelsesfejl i de koreanske filer og automatisk forsøge at oversætte igen for de filer, hvor der blev fundet problemer.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Denne mulighed tjekker for oversættelsesfejl. Lige nu bliver en fil markeret som fejlbehæftet, hvis forskellen i linjeskift mellem originalen og oversættelsen er mere end seks. Jeg planlægger at forbedre dette kriterium for større fleksibilitet fremover.

For eksempel er denne metode nyttig til at opdage manglende stykker eller ødelagte oversættelser, og den vil automatisk forsøge at oversætte de pågældende filer igen.

Men hvis du allerede ved, hvilke filer der er problematiske, er det mere effektivt manuelt at slette de filer og bruge `-a`-muligheden til at oversætte dem igen.

### 8. Fejlsøgningsmode

Hvis du vil aktivere detaljeret logning til fejlfinding, skal du bruge `-d`-muligheden:

```bash
translate -l "ko" -d
```

Denne kommando kører oversættelsen i fejlsøgningsmode og giver ekstra loginformation, som kan hjælpe dig med at identificere problemer under oversættelsen.

#### Eksempel med Phi-3 CookBook

I **Phi-3 CookBook** stødte jeg på et problem, hvor oversættelser med mange links i markdown-filerne gav formateringsfejl, såsom ødelagte oversættelser og ignorerede linjeskift. For at diagnosticere dette problem brugte jeg `-d`-muligheden for at se, hvordan oversættelsesprocessen fungerede.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Oversættelse til alle sprog

Hvis du vil oversætte projektet til alle understøttede sprog, skal du bruge nøgleordet all.

> [!WARNING]
> Oversættelse til alle sprog på én gang kan tage lang tid, afhængigt af projektets størrelse. For eksempel tog det omkring 2 timer at oversætte **Phi-3 CookBook** til spansk. Givet omfanget er det ikke realistisk for én person at håndtere 20 sprog. Det anbefales at dele arbejdet mellem flere bidragsydere, hvor hver tager ansvar for et eller to sprog og opdaterer oversættelserne gradvist.

```bash
translate -l "all"
```

Denne kommando oversætter projektet til alle tilgængelige sprog. Hvis du fortsætter, kan oversættelsen tage lang tid, afhængigt af projektets størrelse.

> [!TIP]
>
> ### Manuel sletning af oversatte filer (valgfrit)
> Oversatte filer bliver nu automatisk opdaget og ryddet op, når en kildefil opdateres.
>
> Men hvis du vil opdatere en oversættelse manuelt – f.eks. for at lave en fil om eller tilsidesætte systemets opførsel – kan du bruge følgende kommando til at slette alle versioner af filen på tværs af sprogmapper.
>
> ### På Windows:
> 1. **Brug af Command Prompt**:
>    - Åbn Command Prompt.
>    - Naviger til mappen, hvor filerne ligger, med `cd`-kommandoen.
>    - Brug denne kommando til at slette filer:
>      ```
>      del /s *filename*
>      ```
>      Erstat `filename` med den del af filnavnet, du leder efter. `/s`-muligheden søger i undermapper.
>
> 2. **Brug af PowerShell**:
>    - Åbn PowerShell.
>    - Kør denne kommando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Erstat `"C:\YourPath"` med mappestien og `filename` med det specifikke navn.
>
> ### På macOS/Linux:
> 1. **Brug af Terminal**:
>   - Åbn Terminal.
>   - Naviger til mappen med `cd`.
>   - Brug `find`-kommandoen:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Erstat `filename` med det specifikke navn.
>
> Tjek altid filerne grundigt, før du sletter, for at undgå utilsigtet tab.
>
> Når du har slettet de filer, der skal erstattes, skal du blot køre din `translate -l`-kommando igen for at opdatere de seneste filændringer.

---

**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.