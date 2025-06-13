<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:50:43+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "no"
}
-->
# Oversett prosjektet ditt med Co-op Translator

**Co-op Translator** er et kommandolinjeverktøy (CLI) som hjelper deg med å oversette markdown- og bildefiler i prosjektet ditt til flere språk. Denne delen forklarer hvordan du bruker verktøyet, dekker de ulike CLI-alternativene, og gir eksempler på forskjellige brukstilfeller.

> [!NOTE]
> For en komplett liste over kommandoer og deres detaljerte beskrivelser, se [Command reference](./command-reference.md).

---

## Eksempelscenarier og kommandoer

Her er noen vanlige brukstilfeller for **Co-op Translator**, sammen med passende kommandoer du kan kjøre.

### 1. Grunnleggende oversettelse (ett språk)

For å oversette hele prosjektet ditt (markdown-filer og bilder) til ett språk, som koreansk, bruk følgende kommando:

```bash
translate -l "ko"
```

Denne kommandoen oversetter alle markdown- og bildefiler til koreansk, og legger til nye oversettelser uten å slette eksisterende.

> [!TIP]
>
> Vil du se hvilke språkkoder som er tilgjengelige i **Co-op Translator**? Besøk [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) seksjonen i repoet for mer informasjon.

#### Eksempel på Phi-3 CookBook

I **Phi-3 CookBook** brukte jeg følgende metode for å legge til koreansk oversettelse for eksisterende markdown-filer og bilder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Oversette til flere språk

For å oversette prosjektet ditt til flere språk (f.eks. spansk, fransk og tysk), bruk denne kommandoen:

```bash
translate -l "es fr de"
```

Denne kommandoen oversetter prosjektet til spansk, fransk og tysk, og legger til nye oversettelser uten å overskrive eksisterende.

#### Eksempel på Phi-3 CookBook

I **Phi-3 CookBook**, etter å ha hentet de siste endringene for å få med de nyeste commitene, brukte jeg følgende metode for å oversette nylig lagde markdown-filer og bilder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Selv om det vanligvis anbefales å oversette ett språk av gangen, kan det i situasjoner som denne, der spesifikke endringer må legges til, være effektivt å oversette flere språk samtidig.

### 3. Oppdatere oversettelser (sletter eksisterende oversettelser)

For å oppdatere eksisterende oversettelser (dvs. slette nåværende oversettelser og erstatte dem med nye), bruk `-u`-alternativet. Dette vil slette alle eksisterende oversettelser for de angitte språkene og oversette på nytt.

```bash
translate -l "ko" -u
```

Advarsel: Denne kommandoen vil be om bekreftelse før den sletter eksisterende oversettelser.

#### Eksempel på Phi-3 CookBook

I **Phi-3 CookBook** brukte jeg følgende metode for å oppdatere alle oversatte filer på spansk. Jeg anbefaler denne metoden når det er store endringer i originalinnholdet på tvers av flere markdown-dokumenter. Hvis det kun er noen få oversatte markdown-filer som skal oppdateres, er det mer effektivt å manuelt slette disse filene og deretter bruke `-a`-metoden for å legge til oppdaterte oversettelser.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Oversette kun bilder

For å oversette kun bildefilene i prosjektet ditt, bruk `-img`-alternativet:

```bash
translate -l "ko" -img
```

Denne kommandoen oversetter kun bildene til koreansk, uten å påvirke markdown-filene.

### 6. Oversette kun markdown-filer

For å oversette kun markdown-filene i prosjektet ditt, bruk `-md`-alternativet:

```bash
translate -l "ko" -md
```

### 7. Sjekke etter feil i oversatte filer

Hvis du vil sjekke oversatte filer for feil og prøve oversettelsen på nytt ved behov, bruk `-chk`-alternativet:

```bash
translate -l "ko" -chk
```

Denne kommandoen skanner de oversatte markdown-filene og prøver oversettelsen på nytt for filer med feil.

#### Eksempel på Phi-3 CookBook

I **Phi-3 CookBook** brukte jeg følgende metode for å sjekke etter oversettelsesfeil i de koreanske filene og automatisk prøve oversettelsen på nytt for filer med oppdagede problemer.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Dette alternativet sjekker etter oversettelsesfeil. For øyeblikket, hvis forskjellen i linjeskift mellom original- og oversatt fil er mer enn seks, blir filen merket som feil i oversettelsen. Jeg planlegger å forbedre dette kriteriet for mer fleksibilitet i fremtiden.

For eksempel er denne metoden nyttig for å oppdage manglende deler eller korrupte oversettelser, og den vil automatisk prøve oversettelsen på nytt for disse filene.

Men hvis du allerede vet hvilke filer som er problematiske, er det mer effektivt å manuelt slette disse filene og bruke `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`-alternativet:

```bash
translate -l "ko" -d
```

Denne kommandoen kjører oversettelsen i debug-modus, og gir ekstra logginformasjon som kan hjelpe deg å identifisere problemer under oversettelsesprosessen.

#### Eksempel på Phi-3 CookBook

I **Phi-3 CookBook** støtte jeg på et problem hvor oversettelser med mange lenker i markdown-filer førte til formateringsfeil, som ødelagte oversettelser og ignorerte linjeskift. For å diagnostisere dette problemet brukte jeg `-d`-alternativet for å se hvordan oversettelsesprosessen fungerte.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Oversette alle språk

Hvis du vil oversette prosjektet til alle støttede språk, bruk nøkkelordet all.

> [!WARNING]
> Å oversette alle språk samtidig kan ta betydelig tid, avhengig av prosjektets størrelse. For eksempel tok det omtrent 2 timer å oversette **Phi-3 CookBook** til spansk. Med en slik skala er det ikke praktisk at én person håndterer 20 språk. Det anbefales å dele arbeidet mellom flere bidragsytere, hvor hver tar ansvar for ett eller to språk, og oppdaterer oversettelsene gradvis.

```bash
translate -l "all"
```

Denne kommandoen oversetter prosjektet til alle tilgjengelige språk. Hvis du fortsetter, kan oversettelsen ta betydelig tid avhengig av prosjektets størrelse.

> [!TIP]
>
> ### Manuell sletting av oversatte filer (valgfritt)
> Oversatte filer blir nå automatisk oppdaget og ryddet opp når en kildefil oppdateres.
>
> Men hvis du ønsker å manuelt oppdatere en oversettelse – for eksempel for å gjøre en fil på nytt eller overstyre systemets oppførsel – kan du bruke følgende kommando for å slette alle versjoner av filen på tvers av språkmapper.
>
> ### På Windows:
> 1. **Bruke Kommandoprompt**:
>    - Åpne Kommandoprompt.
>    - Naviger til mappen der filene ligger med `cd`-kommandoen.
>    - Bruk følgende kommando for å slette filer:
>      ```
>      del /s *filename*
>      ```
>      `filename` with the specific part of the file name you're looking for. The `/s`-alternativet søker også i undermapper.
>
> 2. **Bruke PowerShell**:
>    - Åpne PowerShell.
>    - Kjør denne kommandoen:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Erstatt `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find`-kommandoen:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Erstatt `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l`-kommandoen for å oppdatere de nyeste filendringene.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.