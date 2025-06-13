<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:50:19+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "da"
}
-->
# Oversæt dit projekt med Co-op Translator

**Co-op Translator** er et kommandolinjeværktøj (CLI), der hjælper dig med at oversætte markdown- og billedfiler i dit projekt til flere sprog. Denne sektion forklarer, hvordan du bruger værktøjet, gennemgår de forskellige CLI-muligheder og giver eksempler på forskellige anvendelsessituationer.

> [!NOTE]
> For en komplet liste over kommandoer og deres detaljerede beskrivelser, se venligst [Command reference](./command-reference.md).

---

## Eksempelscenarier og kommandoer

Her er nogle almindelige brugssituationer for **Co-op Translator** sammen med de passende kommandoer.

### 1. Grundlæggende oversættelse (ét sprog)

For at oversætte hele dit projekt (markdown-filer og billeder) til ét sprog, som koreansk, brug følgende kommando:

```bash
translate -l "ko"
```

Denne kommando oversætter alle markdown- og billedfiler til koreansk og tilføjer nye oversættelser uden at slette eksisterende.

> [!TIP]
>
> Vil du se, hvilke sprogkoder der er tilgængelige i **Co-op Translator**? Besøg sektionen [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) i repository’et for flere oplysninger.

#### Eksempel fra Phi-3 CookBook

I **Phi-3 CookBook** brugte jeg følgende metode til at tilføje koreansk oversættelse til de eksisterende markdown-filer og billeder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Oversættelse til flere sprog

For at oversætte dit projekt til flere sprog (f.eks. spansk, fransk og tysk), brug denne kommando:

```bash
translate -l "es fr de"
```

Denne kommando oversætter projektet til spansk, fransk og tysk og tilføjer nye oversættelser uden at overskrive eksisterende.

#### Eksempel fra Phi-3 CookBook

I **Phi-3 CookBook**, efter at have hentet de seneste ændringer for at inkludere de nyeste commits, brugte jeg følgende metode til at oversætte nyligt tilføjede markdown-filer og billeder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Selvom det generelt anbefales at oversætte ét sprog ad gangen, kan det i situationer som denne, hvor specifikke ændringer skal tilføjes, være effektivt at oversætte flere sprog på én gang.

### 3. Opdatering af oversættelser (sletter eksisterende oversættelser)

For at opdatere eksisterende oversættelser (dvs. slette de nuværende oversættelser og erstatte dem med nye), brug `-u`-optionen. Dette sletter alle eksisterende oversættelser for de angivne sprog og oversætter dem igen.

```bash
translate -l "ko" -u
```

Advarsel: Denne kommando beder om bekræftelse, inden de eksisterende oversættelser slettes.

#### Eksempel fra Phi-3 CookBook

I **Phi-3 CookBook** brugte jeg følgende metode til at opdatere alle oversatte filer på spansk. Jeg anbefaler denne metode, når der er betydelige ændringer i det originale indhold på tværs af flere markdown-dokumenter. Hvis der kun er få oversatte markdown-filer, der skal opdateres, er det mere effektivt manuelt at slette de specifikke filer og derefter bruge `-a`-metoden til at tilføje de opdaterede oversættelser.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Oversættelse af kun billeder

For kun at oversætte billedfiler i dit projekt, brug `-img`-optionen:

```bash
translate -l "ko" -img
```

Denne kommando oversætter kun billeder til koreansk uden at påvirke markdown-filerne.

### 6. Oversættelse af kun markdown-filer

For kun at oversætte markdown-filer i dit projekt, brug `-md`-optionen:

```bash
translate -l "ko" -md
```

### 7. Tjek for fejl i oversatte filer

Hvis du vil tjekke oversatte filer for fejl og genoversætte om nødvendigt, brug `-chk`-optionen:

```bash
translate -l "ko" -chk
```

Denne kommando scanner de oversatte markdown-filer og prøver at oversætte igen for eventuelle filer med fejl.

#### Eksempel fra Phi-3 CookBook

I **Phi-3 CookBook** brugte jeg følgende metode til at tjekke for oversættelsesfejl i de koreanske filer og automatisk genoversætte filer med fundne problemer.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Denne option tjekker for oversættelsesfejl. I øjeblikket markeres en fil som fejlbehæftet, hvis forskellen i linjeskift mellem originalen og den oversatte fil er mere end seks. Jeg planlægger at forbedre denne kriterie for større fleksibilitet fremover.

For eksempel er denne metode nyttig til at opdage manglende dele eller korrupte oversættelser, og den vil automatisk forsøge at genoversætte de berørte filer.

Men hvis du allerede ved, hvilke filer der er problematiske, er det mere effektivt manuelt at slette disse filer og bruge `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`-optionen:

```bash
translate -l "ko" -d
```

Denne kommando kører oversættelsen i debug-tilstand og giver yderligere loginformation, som kan hjælpe dig med at identificere problemer under oversættelsesprocessen.

#### Eksempel fra Phi-3 CookBook

I **Phi-3 CookBook** oplevede jeg et problem, hvor oversættelser med mange links i markdown-filer forårsagede formateringsfejl, såsom brudte oversættelser og ignorerede linjeskift. For at diagnosticere dette problem brugte jeg `-d`-optionen for at se, hvordan oversættelsesprocessen fungerede.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Oversættelse til alle sprog

Hvis du vil oversætte projektet til alle understøttede sprog, brug nøgleordet all.

> [!WARNING]
> At oversætte alle sprog på én gang kan tage en betydelig mængde tid afhængigt af projektets størrelse. For eksempel tog det omkring 2 timer at oversætte **Phi-3 CookBook** til spansk. På grund af omfanget er det ikke praktisk for én person at håndtere 20 sprog. Det anbefales at dele arbejdet mellem flere bidragsydere, hvor hver styrer et eller to sprog, og opdaterer oversættelserne gradvist.

```bash
translate -l "all"
```

Denne kommando oversætter projektet til alle tilgængelige sprog. Hvis du fortsætter, kan oversættelsen tage lang tid afhængigt af projektets størrelse.

> [!TIP]
>
> ### Manuel sletning af oversatte filer (valgfrit)
> Oversatte filer opdages nu automatisk og ryddes op, når en kildefil opdateres.
>
> Men hvis du ønsker manuelt at opdatere en oversættelse – for eksempel for at lave en ny version af en specifik fil eller tilsidesætte systemets adfærd – kan du bruge følgende kommando til at slette alle versioner af filen på tværs af sprogmapper.
>
> ### På Windows:
> 1. **Brug af Command Prompt**:
>    - Åbn Command Prompt.
>    - Naviger til mappen, hvor filerne ligger, ved hjælp af `cd`-kommandoen.
>    - Brug følgende kommando til at slette filer:
>      ```
>      del /s *filename*
>      ```
>      `filename` with the specific part of the file name you're looking for. The `/s`-optionen søger også i undermapper.
>
> 2. **Brug af PowerShell**:
>    - Åbn PowerShell.
>    - Kør denne kommando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Erstat `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find`-kommandoen:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Erstat `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l`-kommandoen for at opdatere de seneste filændringer.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.