<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:58:23+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ro"
}
-->
# Traduce-ți proiectul folosind Co-op Translator

**Co-op Translator** este un instrument de tip linie de comandă (CLI) care te ajută să traduci fișierele markdown și imaginile din proiectul tău în mai multe limbi. Această secțiune explică cum să folosești instrumentul, prezintă opțiunile CLI disponibile și oferă exemple pentru diverse scenarii de utilizare.

> [!NOTE]
> Pentru lista completă de comenzi și descrierile lor detaliate, consultă [Referința de comenzi](./command-reference.md).

---

## Exemple de scenarii și comenzi

Mai jos găsești câteva situații comune în care poți folosi **Co-op Translator**, împreună cu comenzile potrivite.

### 1. Traducere de bază (o singură limbă)

Pentru a traduce întregul proiect (fișiere markdown și imagini) într-o singură limbă, de exemplu coreeană, folosește comanda de mai jos:

```bash
translate -l "ko"
```

Această comandă va traduce toate fișierele markdown și imaginile în coreeană, adăugând traduceri noi fără a șterge cele existente.

> [!TIP]
>
> Vrei să vezi ce coduri de limbă sunt disponibile în **Co-op Translator**? Vizitează secțiunea [Limbi suportate](https://github.com/Azure/co-op-translator#supported-languages) din depozit pentru mai multe detalii.

#### Exemplu pe Phi-3 CookBook

În **Phi-3 CookBook**, am folosit metoda de mai jos pentru a adăuga traducerea în coreeană pentru fișierele markdown și imaginile existente.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traducere în mai multe limbi

Pentru a traduce proiectul în mai multe limbi (de exemplu, spaniolă, franceză și germană), folosește această comandă:

```bash
translate -l "es fr de"
```

Comanda va traduce proiectul în spaniolă, franceză și germană, adăugând traduceri noi fără a suprascrie cele existente.

#### Exemplu pe Phi-3 CookBook

În **Phi-3 CookBook**, după ce am preluat ultimele modificări pentru a reflecta cele mai recente commit-uri, am folosit metoda de mai jos pentru a traduce fișierele markdown și imaginile nou adăugate.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> De obicei, este recomandat să traduci o limbă pe rând, dar în situații ca aceasta, unde trebuie adăugate modificări specifice, traducerea simultană în mai multe limbi poate fi eficientă.

### 3. Actualizarea traducerilor (șterge traducerile existente)

Pentru a actualiza traducerile existente (adică să ștergi traducerile curente și să le înlocuiești cu unele noi), folosește opțiunea `-u`. Aceasta va șterge toate traducerile existente pentru limbile specificate și le va retraduce.

```bash
translate -l "ko" -u
```

Atenție: Comanda va cere confirmarea înainte de a șterge traducerile existente.

#### Exemplu pe Phi-3 CookBook

În **Phi-3 CookBook**, am folosit metoda de mai jos pentru a actualiza toate fișierele traduse în spaniolă. Recomand această metodă când există modificări semnificative în conținutul original din mai multe documente markdown. Dacă ai doar câteva fișiere traduse de actualizat, e mai eficient să le ștergi manual și apoi să folosești metoda `-a` pentru a adăuga traducerile actualizate.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Traducerea doar a imaginilor

Pentru a traduce doar fișierele imagine din proiect, folosește opțiunea `-img`:

```bash
translate -l "ko" -img
```

Comanda va traduce doar imaginile în coreeană, fără a afecta fișierele markdown.

### 6. Traducerea doar a fișierelor Markdown

Pentru a traduce doar fișierele markdown din proiect, folosește opțiunea `-md`:

```bash
translate -l "ko" -md
```

#### Exemplu pe Phi-3 CookBook

În **Phi-3 CookBook**, am folosit metoda de mai jos pentru a verifica erorile de traducere în fișierele coreene și pentru a retraduce automat fișierele cu probleme detectate.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Această opțiune verifică erorile de traducere. În prezent, dacă diferența de linii între fișierul original și cel tradus este mai mare de șase, fișierul este marcat ca având o eroare de traducere. Plănuiesc să îmbunătățesc acest criteriu pentru mai multă flexibilitate pe viitor.

De exemplu, această metodă este utilă pentru a detecta fragmente lipsă sau traduceri corupte și va retraduce automat acele fișiere.

Totuși, dacă știi deja care fișiere sunt problematice, e mai eficient să le ștergi manual și să folosești opțiunea `-a` pentru a le retraduce.

### 8. Modul de depanare (Debug Mode)

Pentru a activa logarea detaliată pentru depanare, folosește opțiunea `-d`:

```bash
translate -l "ko" -d
```

Comanda va rula traducerea în modul debug, oferind informații suplimentare care te pot ajuta să identifici problemele apărute în procesul de traducere.

#### Exemplu pe Phi-3 CookBook

În **Phi-3 CookBook**, am întâmpinat o problemă în care traducerile cu multe linkuri în fișierele markdown generau erori de formatare, cum ar fi traduceri incomplete sau linii ignorate. Pentru a diagnostica problema, am folosit opțiunea `-d` ca să văd cum funcționează procesul de traducere.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Traducerea în toate limbile

Dacă vrei să traduci proiectul în toate limbile suportate, folosește cuvântul cheie all.

> [!WARNING]
> Traducerea în toate limbile simultan poate dura mult timp, în funcție de dimensiunea proiectului. De exemplu, traducerea **Phi-3 CookBook** în spaniolă a durat aproximativ 2 ore. Având în vedere amploarea, nu este practic ca o singură persoană să gestioneze 20 de limbi. Recomand să împarți munca între mai mulți colaboratori, fiecare ocupându-se de una sau două limbi, și să actualizezi traducerile treptat.

```bash
translate -l "all"
```

Comanda va traduce proiectul în toate limbile disponibile. Dacă continui, traducerea poate dura mult timp, în funcție de dimensiunea proiectului.

> [!TIP]
>
> ### Ștergerea manuală a fișierelor traduse (opțional)
> Fișierele traduse sunt acum detectate automat și curățate când un fișier sursă este actualizat.
>
> Totuși, dacă vrei să actualizezi manual o traducere – de exemplu, să refaci un fișier anume sau să suprascrii comportamentul sistemului – poți folosi comanda de mai jos pentru a șterge toate versiunile fișierului din folderele de limbi.
>
> ### Pe Windows:
> 1. **Folosind Command Prompt**:
>    - Deschide Command Prompt.
>    - Navighează la folderul unde se află fișierele folosind comanda `cd`.
>    - Folosește comanda de mai jos pentru a șterge fișierele:
>      ```
>      del /s *filename*
>      ```
>      Înlocuiește `filename` cu partea specifică din numele fișierului pe care îl cauți. Opțiunea `/s` caută și în subfoldere.
>
> 2. **Folosind PowerShell**:
>    - Deschide PowerShell.
>    - Rulează această comandă:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Înlocuiește `"C:\YourPath"` cu calea folderului și `filename` cu numele specific.
>
> ### Pe macOS/Linux:
> 1. **Folosind Terminal**:
>   - Deschide Terminal.
>   - Navighează la director cu `cd`.
>   - Folosește comanda `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Înlocuiește `filename` cu numele specific.
>
> Verifică întotdeauna fișierele înainte de a le șterge ca să eviți pierderile accidentale. 
>
> După ce ai șters fișierele care trebuie înlocuite, rulează din nou comanda `translate -l` pentru a actualiza modificările recente ale fișierelor.

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.