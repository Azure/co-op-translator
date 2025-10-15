<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:25:07+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "no"
}
-->
# Oversett prosjektet ditt med Co-op Translator

**Co-op Translator** er et kommandolinjeverktøy (CLI) som hjelper deg med å oversette markdown- og bildefiler i prosjektet ditt til flere språk. Denne delen forklarer hvordan du bruker verktøyet, går gjennom ulike CLI-valg, og gir eksempler for forskjellige bruksområder.

> [!NOTE]
> For en komplett liste over kommandoer og detaljerte beskrivelser, se [Command reference](./command-reference.md).

---

## Eksempelscenarier og kommandoer

Her er noen vanlige bruksområder for **Co-op Translator**, sammen med passende kommandoer du kan bruke.

### 1. Grunnleggende oversettelse (ett språk)

For å oversette hele prosjektet ditt (markdown-filer og bilder) til ett språk, for eksempel koreansk, bruk denne kommandoen:

```bash
translate -l "ko"
```

Denne kommandoen oversetter alle markdown- og bildefiler til koreansk, og legger til nye oversettelser uten å slette eksisterende.

> [!TIP]
>
> Vil du se hvilke språkkoder som er tilgjengelige i **Co-op Translator**? Besøk [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) i repoet for mer informasjon.

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

I **Phi-3 CookBook**, etter å ha hentet de siste endringene for å få med de nyeste commitene, brukte jeg følgende metode for å oversette nylig lagt til markdown-filer og bilder.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Det anbefales vanligvis å oversette ett språk om gangen, men i situasjoner som dette hvor spesifikke endringer må legges til, kan det være effektivt å oversette flere språk samtidig.

### 3. Oppdatere oversettelser (sletter eksisterende oversettelser)

For å oppdatere eksisterende oversettelser (dvs. slette nåværende oversettelser og erstatte dem med nye), bruk `-u`-valget. Dette vil slette alle eksisterende oversettelser for de valgte språkene og oversette dem på nytt.

```bash
translate -l "ko" -u
```

Advarsel: Denne kommandoen vil be om bekreftelse før den fortsetter med å slette eksisterende oversettelser.

#### Eksempel på Phi-3 CookBook

I **Phi-3 CookBook** brukte jeg følgende metode for å oppdatere alle oversatte filer på spansk. Jeg anbefaler å bruke denne metoden når det er store endringer i originalinnholdet på tvers av flere markdown-dokumenter. Hvis det bare er noen få oversatte markdown-filer som må oppdateres, er det mer effektivt å slette disse filene manuelt og deretter bruke `-a`-metoden for å legge til oppdaterte oversettelser.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Kun oversette bilder

For å kun oversette bildefilene i prosjektet ditt, bruk `-img`-valget:

```bash
translate -l "ko" -img
```

Denne kommandoen oversetter kun bildene til koreansk, uten å påvirke noen markdown-filer.

### 6. Kun oversette markdown-filer

For å kun oversette markdown-filene i prosjektet ditt, bruk `-md`-valget:

```bash
translate -l "ko" -md
```

#### Eksempel på Phi-3 CookBook

I **Phi-3 CookBook** brukte jeg følgende metode for å sjekke etter oversettelsesfeil i de koreanske filene og automatisk prøve å oversette på nytt for filer med oppdagede problemer.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Dette valget sjekker etter oversettelsesfeil. For øyeblikket, hvis forskjellen i linjeskift mellom originalen og den oversatte filen er mer enn seks, blir filen markert som å ha en oversettelsesfeil. Jeg planlegger å forbedre dette kriteriet for større fleksibilitet i fremtiden.

For eksempel er denne metoden nyttig for å oppdage manglende deler eller ødelagte oversettelser, og den vil automatisk prøve å oversette disse filene på nytt.

Men hvis du allerede vet hvilke filer som er problematiske, er det mer effektivt å slette disse filene manuelt og bruke `-a`-valget for å oversette dem på nytt.

### 8. Feilsøkingsmodus

For å aktivere detaljert logging for feilsøking, bruk `-d`-valget:

```bash
translate -l "ko" -d
```

Denne kommandoen kjører oversettelsen i feilsøkingsmodus, og gir ekstra logginformasjon som kan hjelpe deg med å finne problemer under oversettelsesprosessen.

#### Eksempel på Phi-3 CookBook

I **Phi-3 CookBook** støtte jeg på et problem der oversettelser med mange lenker i markdown-filer førte til formateringsfeil, som ødelagte oversettelser og ignorerte linjeskift. For å finne ut av dette problemet brukte jeg `-d`-valget for å se hvordan oversettelsesprosessen fungerte.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Oversette til alle språk

Hvis du vil oversette prosjektet til alle støttede språk, bruk nøkkelordet all.

> [!WARNING]
> Å oversette til alle språk samtidig kan ta mye tid, avhengig av prosjektets størrelse. For eksempel tok det omtrent 2 timer å oversette **Phi-3 CookBook** til spansk. Med tanke på omfanget, er det ikke praktisk for én person å håndtere 20 språk. Det anbefales å dele opp arbeidet mellom flere bidragsytere, der hver tar ansvar for ett eller to språk, og oppdaterer oversettelsene gradvis.

```bash
translate -l "all"
```

Denne kommandoen oversetter prosjektet til alle tilgjengelige språk. Hvis du fortsetter, kan oversettelsen ta lang tid avhengig av prosjektets størrelse.

> [!TIP]
>
> ### Slette oversatte filer manuelt (valgfritt)
> Oversatte filer blir nå automatisk oppdaget og ryddet opp når en kildefil oppdateres.
>
> Men hvis du vil oppdatere en oversettelse manuelt – for eksempel for å gjøre en fil på nytt eller overstyre systemets oppførsel – kan du bruke følgende kommando for å slette alle versjoner av filen på tvers av språkmapper.
>
> ### På Windows:
> 1. **Bruke Command Prompt**:
>    - Åpne Command Prompt.
>    - Naviger til mappen der filene ligger med `cd`-kommandoen.
>    - Bruk denne kommandoen for å slette filer:
>      ```
>      del /s *filename*
>      ```
>      Erstatt `filename` med den delen av filnavnet du leter etter. `/s`-valget søker i undermapper også.
>
> 2. **Bruke PowerShell**:
>    - Åpne PowerShell.
>    - Kjør denne kommandoen:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Erstatt `"C:\YourPath"` med mappestien og `filename` med det spesifikke navnet.
>
> ### På macOS/Linux:
> 1. **Bruke Terminal**:
>   - Åpne Terminal.
>   - Naviger til katalogen med `cd`.
>   - Bruk `find`-kommandoen:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Erstatt `filename` med det spesifikke navnet.
>
> Dobbeltsjekk alltid filene før du sletter for å unngå utilsiktet tap.
>
> Når du har slettet filene som skal erstattes, kjør bare `translate -l`-kommandoen din på nytt for å oppdatere de nyeste filendringene.

---

**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, må du være oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.