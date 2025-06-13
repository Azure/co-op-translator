<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:56:50+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "hr"
}
-->
# Prevedite svoj projekt pomoću Co-op Translatora

**Co-op Translator** je alat za naredbeni redak (CLI) koji vam pomaže prevesti markdown i slikovne datoteke u vašem projektu na više jezika. Ovaj odjeljak objašnjava kako koristiti alat, obuhvaća različite CLI opcije i daje primjere za različite slučajeve upotrebe.

> [!NOTE]
> Za potpuni popis naredbi i njihovih detaljnih opisa, pogledajte [Command reference](./command-reference.md).

---

## Primjeri scenarija i naredbi

Evo nekoliko uobičajenih primjera upotrebe **Co-op Translatora**, zajedno s odgovarajućim naredbama za pokretanje.

### 1. Osnovni prijevod (jedan jezik)

Za prevođenje cijelog projekta (markdown datoteka i slika) na jedan jezik, poput korejskog, upotrijebite sljedeću naredbu:

```bash
translate -l "ko"
```

Ova naredba će prevesti sve markdown i slikovne datoteke na korejski, dodajući nove prijevode bez brisanja postojećih.

> [!TIP]
>
> Želite vidjeti koji su kodovi jezika dostupni u **Co-op Translatoru**? Posjetite odjeljak [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) u repozitoriju za više detalja.

#### Primjer na Phi-3 CookBooku

U **Phi-3 CookBooku** koristio sam sljedeću metodu za dodavanje korejskog prijevoda za postojeće markdown datoteke i slike.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Prevođenje na više jezika

Za prevođenje projekta na više jezika (npr. španjolski, francuski i njemački), upotrijebite ovu naredbu:

```bash
translate -l "es fr de"
```

Ova naredba će prevesti projekt na španjolski, francuski i njemački, dodajući nove prijevode bez prepisivanja postojećih.

#### Primjer na Phi-3 CookBooku

U **Phi-3 CookBooku**, nakon povlačenja najnovijih promjena za odražavanje najnovijih commitova, koristio sam sljedeću metodu za prevođenje novododanih markdown datoteka i slika.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Iako se općenito preporučuje prevođenje jednog jezika odjednom, u situacijama poput ove gdje je potrebno dodati specifične promjene, prevođenje više jezika odjednom može biti učinkovito.

### 3. Ažuriranje prijevoda (briše postojeće prijevode)

Za ažuriranje postojećih prijevoda (tj. brisanje trenutnih prijevoda i zamjenu novima), upotrijebite opciju `-u`. Ovo će izbrisati sve postojeće prijevode za navedene jezike i ponovno ih prevesti.

```bash
translate -l "ko" -u
```

Upozorenje: Ova naredba će vas zatražiti potvrdu prije nego što nastavi s brisanjem postojećih prijevoda.

#### Primjer na Phi-3 CookBooku

U **Phi-3 CookBooku** koristio sam sljedeću metodu za ažuriranje svih prevedenih datoteka na španjolskom. Preporučujem ovu metodu kad postoje značajne promjene u izvornom sadržaju kroz više markdown dokumenata. Ako je potrebno ažurirati samo nekoliko prevedenih markdown datoteka, učinkovitije je ručno izbrisati te specifične datoteke, a zatim koristiti metodu `-a` za dodavanje ažuriranih prijevoda.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Prevođenje samo slika

Za prevođenje samo slikovnih datoteka u vašem projektu, upotrijebite opciju `-img`:

```bash
translate -l "ko" -img
```

Ova naredba će prevesti samo slike na korejski, bez utjecaja na markdown datoteke.

### 6. Prevođenje samo markdown datoteka

Za prevođenje samo markdown datoteka u vašem projektu, upotrijebite opciju `-md`:

```bash
translate -l "ko" -md
```

### 7. Provjera pogrešaka u prevedenim datotekama

Ako želite provjeriti prevedene datoteke na pogreške i po potrebi ponoviti prijevod, upotrijebite opciju `-chk`:

```bash
translate -l "ko" -chk
```

Ova naredba će pregledati prevedene markdown datoteke i pokušati ponovno prevesti sve datoteke u kojima su pronađene pogreške.

#### Primjer na Phi-3 CookBooku

U **Phi-3 CookBooku** koristio sam sljedeću metodu za provjeru pogrešaka u prijevodu korejskih datoteka i automatsko ponovno prevođenje za sve datoteke s uočenim problemima.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Ova opcija provjerava pogreške u prijevodu. Trenutno, ako je razlika u prijelomima redaka između izvornog i prevedenog dokumenta veća od šest, datoteka se označava kao da ima pogrešku u prijevodu. Planiram poboljšati ovaj kriterij za veću fleksibilnost u budućnosti.

Na primjer, ova metoda je korisna za otkrivanje nedostajućih dijelova ili oštećenih prijevoda, a automatski će pokušati ponovno prevesti te datoteke.

Međutim, ako već znate koje su datoteke problematične, učinkovitije je ručno izbrisati te datoteke i koristiti opciju `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Ova naredba će pokrenuti prijevod u debug načinu rada, pružajući dodatne informacije o zapisima koje vam mogu pomoći u otkrivanju problema tijekom procesa prevođenja.

#### Primjer na Phi-3 CookBooku

U **Phi-3 CookBooku** naišao sam na problem gdje su prijevodi s mnogo poveznica u markdown datotekama uzrokovali pogreške u formatiranju, poput neispravnih prijevoda i zanemarivanja prijeloma redaka. Za dijagnosticiranje problema koristio sam opciju `-d` da vidim kako proces prevođenja funkcionira.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Prevođenje na sve jezike

Ako želite prevesti projekt na sve podržane jezike, upotrijebite ključnu riječ all.

> [!WARNING]
> Prevođenje na sve jezike odjednom može potrajati značajno dugo, ovisno o veličini projekta. Na primjer, prevođenje **Phi-3 CookBooka** na španjolski trajalo je oko 2 sata. S obzirom na opseg, nije praktično da jedna osoba obrađuje 20 jezika. Preporučuje se podijeliti posao među više suradnika, svaki neka upravlja jednim ili dva jezika i postupno ažurira prijevode.

```bash
translate -l "all"
```

Ova naredba će prevesti projekt na sve dostupne jezike. Ako nastavite, prijevod može potrajati značajno dugo, ovisno o veličini projekta.

> [!TIP]
>
> ### Ručno brisanje prevedenih datoteka (opcionalno)
> Prevedene datoteke se sada automatski prepoznaju i čiste kada se ažurira izvorna datoteka.
>
> Međutim, ako želite ručno ažurirati prijevod – na primjer, ponovno napraviti određenu datoteku ili nadjačati ponašanje sustava – možete koristiti sljedeću naredbu za brisanje svih verzija datoteke u svim jezičnim mapama.
>
> ### Na Windowsima:
> 1. **Korištenje Command Prompt-a**:
>    - Otvorite Command Prompt.
>    - Pređite u mapu gdje se datoteke nalaze pomoću naredbe `cd`.
>    - Koristite sljedeću naredbu za brisanje datoteka:
>      ```
>      del /s *filename*
>      ```
>      Opcija `/s` pretražuje i poddirektorije.
>
> 2. **Korištenje PowerShell-a**:
>    - Otvorite PowerShell.
>    - Pokrenite ovu naredbu:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Zamijenite `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` naredbu:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Zamijenite `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` naredbu za ažuriranje najnovijih promjena datoteka.

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.