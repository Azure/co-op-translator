<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:55:32+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ro"
}
-->
# Tradu-ți proiectul folosind Co-op Translator

**Co-op Translator** este un instrument de linie de comandă (CLI) care te ajută să traduci fișiere markdown și imagini din proiectul tău în mai multe limbi. Această secțiune explică cum să folosești instrumentul, prezintă diversele opțiuni CLI și oferă exemple pentru diferite cazuri de utilizare.

> [!NOTE]
> Pentru o listă completă a comenzilor și descrierile detaliate ale acestora, te rugăm să consulți [Referința comenzilor](./command-reference.md).

---

## Scenarii și comenzi exemplu

Iată câteva cazuri comune de utilizare pentru **Co-op Translator**, împreună cu comenzile potrivite pentru a le rula.

### 1. Traducere de bază (o singură limbă)

Pentru a traduce întregul proiect (fișiere markdown și imagini) într-o singură limbă, cum ar fi coreeana, folosește comanda următoare:

```bash
translate -l "ko"
```

Această comandă va traduce toate fișierele markdown și imaginile în coreeană, adăugând noile traduceri fără a șterge pe cele existente.

> [!TIP]
>
> Vrei să vezi ce coduri de limbă sunt disponibile în **Co-op Translator**? Vizitează secțiunea [Limbi suportate](https://github.com/Azure/co-op-translator#supported-languages) din depozit pentru mai multe detalii.

#### Exemplu în Phi-3 CookBook

În **Phi-3 CookBook**, am folosit următoarea metodă pentru a adăuga traducerea în coreeană pentru fișierele markdown și imaginile existente.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traducerea în mai multe limbi

Pentru a traduce proiectul în mai multe limbi (de exemplu, spaniolă, franceză și germană), folosește această comandă:

```bash
translate -l "es fr de"
```

Această comandă va traduce proiectul în spaniolă, franceză și germană, adăugând noile traduceri fără a suprascrie pe cele existente.

#### Exemplu în Phi-3 CookBook

În **Phi-3 CookBook**, după ce am preluat ultimele modificări pentru a reflecta cele mai recente commit-uri, am folosit următoarea metodă pentru a traduce fișierele markdown și imaginile adăugate recent.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Deși, în general, este recomandat să traduci o limbă pe rând, în situații ca aceasta, când trebuie adăugate modificări specifice, traducerea în mai multe limbi simultan poate fi eficientă.

### 3. Actualizarea traducerilor (șterge traducerile existente)

Pentru a actualiza traducerile existente (adică să ștergi traducerile curente și să le înlocuiești cu altele noi), folosește opțiunea `-u`. Aceasta va șterge toate traducerile existente pentru limbile specificate și le va retraduce.

```bash
translate -l "ko" -u
```

Atenție: Această comandă îți va cere confirmarea înainte de a continua cu ștergerea traducerilor existente.

#### Exemplu în Phi-3 CookBook

În **Phi-3 CookBook**, am folosit următoarea metodă pentru a actualiza toate fișierele traduse în spaniolă. Recomand această metodă atunci când există modificări semnificative în conținutul original din mai multe fișiere markdown. Dacă sunt doar câteva fișiere traduse de actualizat, este mai eficient să ștergi manual acele fișiere specifice și apoi să folosești metoda `-a` pentru a adăuga traducerile actualizate.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Traducerea doar a imaginilor

Pentru a traduce doar fișierele de imagine din proiect, folosește opțiunea `-img`:

```bash
translate -l "ko" -img
```

Această comandă va traduce doar imaginile în coreeană, fără a afecta fișierele markdown.

### 6. Traducerea doar a fișierelor markdown

Pentru a traduce doar fișierele markdown din proiect, folosește opțiunea `-md`:

```bash
translate -l "ko" -md
```

### 7. Verificarea erorilor în fișierele traduse

Dacă vrei să verifici fișierele traduse pentru erori și să reîncerci traducerea dacă este necesar, folosește opțiunea `-chk`:

```bash
translate -l "ko" -chk
```

Această comandă va scana fișierele markdown traduse și va reîncerca traducerea pentru orice fișier cu erori.

#### Exemplu în Phi-3 CookBook

În **Phi-3 CookBook**, am folosit următoarea metodă pentru a verifica erorile de traducere în fișierele coreene și pentru a reîncerca automat traducerea pentru orice fișier cu probleme detectate.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Această opțiune verifică erorile de traducere. În prezent, dacă diferența în numărul de întreruperi de linie între fișierul original și cel tradus este mai mare de șase, fișierul este marcat ca având o eroare de traducere. Plănuiesc să îmbunătățesc acest criteriu pentru a oferi mai multă flexibilitate în viitor.

De exemplu, această metodă este utilă pentru detectarea fragmentelor lipsă sau a traducerilor corupte și va reîncerca automat traducerea pentru acele fișiere.

Totuși, dacă știi deja care fișiere sunt problematice, este mai eficient să le ștergi manual și să folosești opțiunea `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Această comandă va rula traducerea în modul debug, oferind informații suplimentare de logare care te pot ajuta să identifici problemele apărute în timpul procesului de traducere.

#### Exemplu în Phi-3 CookBook

În **Phi-3 CookBook**, am întâmpinat o problemă în care traducerile cu multe linkuri din fișierele markdown cauzau erori de formatare, cum ar fi traduceri rupte și întreruperi de linie ignorate. Pentru a diagnostica această problemă, am folosit opțiunea `-d` pentru a vedea cum funcționează procesul de traducere.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Traducerea tuturor limbilor

Dacă vrei să traduci proiectul în toate limbile suportate, folosește cuvântul cheie all.

> [!WARNING]
> Traducerea tuturor limbilor simultan poate dura mult timp, în funcție de dimensiunea proiectului. De exemplu, traducerea **Phi-3 CookBook** în spaniolă a durat aproximativ 2 ore. Având în vedere amploarea, nu este practic ca o singură persoană să se ocupe de 20 de limbi. Se recomandă să împărțiți munca între mai mulți colaboratori, fiecare gestionând una sau două limbi, și să actualizați traducerile treptat.

```bash
translate -l "all"
```

Această comandă va traduce proiectul în toate limbile disponibile. Dacă continui, traducerea poate dura mult timp, în funcție de dimensiunea proiectului.

> [!TIP]
>
> ### Ștergerea manuală a fișierelor traduse (opțional)
> Fișierele traduse sunt acum detectate și curățate automat atunci când un fișier sursă este actualizat.
>
> Totuși, dacă vrei să actualizezi manual o traducere - de exemplu, să refaci un fișier specific sau să suprascrii comportamentul sistemului - poți folosi comanda următoare pentru a șterge toate versiunile fișierului din toate folderele de limbă.
>
> ### Pe Windows:
> 1. **Folosind Command Prompt**:
>    - Deschide Command Prompt.
>    - Navighează la folderul unde se află fișierele folosind comanda `cd`.
>    - Folosește comanda următoare pentru a șterge fișierele:
>      ```
>      del /s *filename*
>      ```
>      Opțiunea `/s` caută și în subdirectoare.
>
> 2. **Folosind PowerShell**:
>    - Deschide PowerShell.
>    - Rulează această comandă:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Înlocuiește `"C:\YourPath"` cu calea ta către fișiere.
>    - Folosește comanda `cd` și `find` pentru a căuta fișiere:
>      ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>      Înlocuiește `filename` cu numele fișierului pe care vrei să îl ștergi.
>
> Folosește comanda `translate -l` pentru a actualiza cele mai recente modificări ale fișierelor.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.