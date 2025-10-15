<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T04:07:02+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "hr"
}
-->
# Prevedite svoj projekt pomoću Co-op Translatora

**Co-op Translator** je alat za naredbeni redak (CLI) koji vam pomaže prevesti markdown i slikovne datoteke u vašem projektu na više jezika. Ovaj odjeljak objašnjava kako koristiti alat, opisuje različite CLI opcije i daje primjere za razne scenarije korištenja.

> [!NOTE]
> Za potpuni popis naredbi i njihova detaljna objašnjenja, pogledajte [Referencu naredbi](./command-reference.md).

---

## Primjeri scenarija i naredbi

Ovdje su neki uobičajeni primjeri korištenja **Co-op Translatora** s odgovarajućim naredbama.

### 1. Osnovni prijevod (jedan jezik)

Za prijevod cijelog projekta (markdown datoteka i slika) na jedan jezik, primjerice korejski, upotrijebite sljedeću naredbu:

```bash
translate -l "ko"
```

Ova naredba će prevesti sve markdown i slikovne datoteke na korejski, dodajući nove prijevode bez brisanja postojećih.

> [!TIP]
>
> Želite vidjeti koji su kodovi jezika dostupni u **Co-op Translatoru**? Posjetite odjeljak [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) u repozitoriju za više detalja.

#### Primjer na Phi-3 CookBooku

U **Phi-3 CookBooku** koristio/la sam sljedeću metodu za dodavanje korejskog prijevoda postojećih markdown datoteka i slika.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Prijevod na više jezika

Za prijevod vašeg projekta na više jezika (npr. španjolski, francuski i njemački), upotrijebite ovu naredbu:

```bash
translate -l "es fr de"
```

Ova naredba će prevesti projekt na španjolski, francuski i njemački, dodajući nove prijevode bez prepisivanja postojećih.

#### Primjer na Phi-3 CookBooku

U **Phi-3 CookBooku**, nakon povlačenja najnovijih promjena kako bi se odrazili najnoviji commitovi, koristio/la sam sljedeću metodu za prijevod novo dodanih markdown datoteka i slika.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Iako se općenito preporučuje prevoditi jedan jezik odjednom, u situacijama poput ove gdje treba dodati određene promjene, prijevod na više jezika odjednom može biti učinkovit.

### 3. Ažuriranje prijevoda (briše postojeće prijevode)

Za ažuriranje postojećih prijevoda (tj. brisanje trenutnih prijevoda i njihovu zamjenu novima), koristite opciju `-u`. Ovo će izbrisati sve postojeće prijevode za navedene jezike i ponovno ih prevesti.

```bash
translate -l "ko" -u
```

Upozorenje: Ova naredba će vas tražiti potvrdu prije nego što nastavi s brisanjem postojećih prijevoda.

#### Primjer na Phi-3 CookBooku

U **Phi-3 CookBooku** koristio/la sam sljedeću metodu za ažuriranje svih prevedenih datoteka na španjolski. Preporučujem ovu metodu kada postoje značajne promjene u izvornom sadržaju kroz više markdown dokumenata. Ako je potrebno ažurirati samo nekoliko prevedenih markdown datoteka, učinkovitije je ručno izbrisati te određene datoteke i zatim koristiti metodu `-a` za dodavanje ažuriranih prijevoda.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Prijevod samo slika

Za prijevod samo slikovnih datoteka u vašem projektu, koristite opciju `-img`:

```bash
translate -l "ko" -img
```

Ova naredba će prevesti samo slike na korejski, bez utjecaja na markdown datoteke.

### 6. Prijevod samo markdown datoteka

Za prijevod samo markdown datoteka u vašem projektu, koristite opciju `-md`:

```bash
translate -l "ko" -md
```

#### Primjer na Phi-3 CookBooku

U **Phi-3 CookBooku** koristio/la sam sljedeću metodu za provjeru pogrešaka u prijevodu u korejskim datotekama i automatsko ponovno prevođenje svih datoteka kod kojih su otkrivene pogreške.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Ova opcija provjerava pogreške u prijevodu. Trenutno, ako je razlika u broju prijeloma redaka između izvorne i prevedene datoteke veća od šest, datoteka se označava kao da ima pogrešku u prijevodu. Planiram poboljšati ovaj kriterij za veću fleksibilnost u budućnosti.

Na primjer, ova metoda je korisna za otkrivanje nedostajućih dijelova ili oštećenih prijevoda, a automatski će ponovno pokušati prevesti te datoteke.

Međutim, ako već znate koje su datoteke problematične, učinkovitije je ručno izbrisati te datoteke i koristiti opciju `-a` za njihovo ponovno prevođenje.

### 8. Način za otklanjanje grešaka (Debug Mode)

Za uključivanje detaljnog zapisivanja radi otklanjanja grešaka, koristite opciju `-d`:

```bash
translate -l "ko" -d
```

Ova naredba će pokrenuti prijevod u debug načinu, pružajući dodatne informacije u zapisima koje vam mogu pomoći u prepoznavanju problema tijekom procesa prevođenja.

#### Primjer na Phi-3 CookBooku

U **Phi-3 CookBooku** naišao/la sam na problem gdje su prijevodi s mnogo poveznica u markdown datotekama uzrokovali pogreške u formatiranju, poput prekinutih prijevoda i ignoriranih prijeloma redaka. Za dijagnosticiranje ovog problema koristio/la sam opciju `-d` kako bih vidio/la kako proces prevođenja funkcionira.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Prijevod na sve jezike

Ako želite prevesti projekt na sve podržane jezike, koristite ključnu riječ all.

> [!WARNING]
> Prijevod na sve jezike odjednom može potrajati znatno, ovisno o veličini projekta. Na primjer, prijevod **Phi-3 CookBooka** na španjolski trajao je oko 2 sata. S obzirom na opseg, nije praktično da jedna osoba obrađuje 20 jezika. Preporučuje se podijeliti posao među više suradnika, od kojih svaki upravlja jednim ili dva jezika, i postupno ažurirati prijevode.

```bash
translate -l "all"
```

Ova naredba će prevesti projekt na sve dostupne jezike. Ako nastavite, prijevod može potrajati znatno, ovisno o veličini projekta.

> [!TIP]
>
> ### Ručno brisanje prevedenih datoteka (opcionalno)
> Prevedene datoteke sada se automatski otkrivaju i čiste kada se izvorna datoteka ažurira.
>
> Međutim, ako želite ručno ažurirati prijevod – na primjer, ponovno prevesti određenu datoteku ili nadjačati ponašanje sustava – možete koristiti sljedeću naredbu za brisanje svih verzija datoteke u svim jezičnim mapama.
>
> ### Na Windowsu:
> 1. **Korištenje Command Prompt-a**:
>    - Otvorite Command Prompt.
>    - Navigirajte do mape u kojoj se nalaze datoteke pomoću naredbe `cd`.
>    - Koristite sljedeću naredbu za brisanje datoteka:
>      ```
>      del /s *filename*
>      ```
>      Zamijenite `filename` s dijelom imena datoteke koji tražite. Opcija `/s` pretražuje i poddirektorije.
>
> 2. **Korištenje PowerShell-a**:
>    - Otvorite PowerShell.
>    - Pokrenite ovu naredbu:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Zamijenite `"C:\YourPath"` s putanjom do mape i `filename` s određenim imenom.
>
> ### Na macOS/Linux:
> 1. **Korištenje Terminala**:
>   - Otvorite Terminal.
>   - Navigirajte do direktorija pomoću `cd`.
>   - Koristite naredbu `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Zamijenite `filename` s određenim imenom.
>
> Uvijek dvaput provjerite datoteke prije brisanja kako biste izbjegli slučajni gubitak podataka. 
>
> Nakon što izbrišete datoteke koje treba zamijeniti, jednostavno ponovno pokrenite svoju `translate -l` naredbu kako biste ažurirali najnovije promjene datoteka.

---

**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na svom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.