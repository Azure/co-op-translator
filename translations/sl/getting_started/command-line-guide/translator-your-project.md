<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T04:10:02+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "sl"
}
-->
# Prevedite svoj projekt z orodjem Co-op Translator

**Co-op Translator** je orodje za ukazno vrstico (CLI), ki vam pomaga prevesti markdown in slikovne datoteke v vašem projektu v več jezikov. V tem poglavju je razložena uporaba orodja, predstavljene so različne možnosti CLI in podani primeri za različne primere uporabe.

> [!NOTE]
> Za popoln seznam ukazov in njihove podrobne opise si oglejte [Referenco ukazov](./command-reference.md).

---

## Primeri uporabe in ukazi

Tukaj je nekaj pogostih primerov uporabe **Co-op Translatorja** skupaj z ustreznimi ukazi.

### 1. Osnovno prevajanje (en jezik)

Če želite prevesti celoten projekt (markdown datoteke in slike) v en jezik, na primer korejščino, uporabite naslednji ukaz:

```bash
translate -l "ko"
```

Ta ukaz bo prevedel vse markdown in slikovne datoteke v korejščino ter dodal nove prevode, ne da bi izbrisal obstoječe.

> [!TIP]
>
> Vas zanima, katere jezikovne kode so na voljo v **Co-op Translatorju**? Obiščite razdelek [Podprti jeziki](https://github.com/Azure/co-op-translator#supported-languages) v repozitoriju za več podrobnosti.

#### Primer v Phi-3 CookBook

V **Phi-3 CookBook** sem uporabil naslednjo metodo za dodajanje korejskega prevoda obstoječih markdown datotek in slik.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Prevajanje v več jezikov

Če želite svoj projekt prevesti v več jezikov (npr. španščino, francoščino in nemščino), uporabite ta ukaz:

```bash
translate -l "es fr de"
```

Ta ukaz bo projekt prevedel v španščino, francoščino in nemščino ter dodal nove prevode, ne da bi prepisal obstoječe.

#### Primer v Phi-3 CookBook

V **Phi-3 CookBook** sem po pridobitvi najnovejših sprememb, da sem zajel zadnje commit-e, uporabil naslednjo metodo za prevod na novo dodanih markdown datotek in slik.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Čeprav je običajno priporočljivo prevajati en jezik naenkrat, je v takšnih primerih, ko je treba dodati določene spremembe, prevajanje v več jezikov hkrati lahko učinkovito.

### 3. Posodabljanje prevodov (izbriše obstoječe prevode)

Za posodobitev obstoječih prevodov (torej izbris trenutnih prevodov in njihovo zamenjavo z novimi) uporabite možnost `-u`. Ta možnost bo izbrisala vse obstoječe prevode za izbrane jezike in jih ponovno prevedla.

```bash
translate -l "ko" -u
```

Opozorilo: Ta ukaz vas bo pred nadaljevanjem vprašal za potrditev izbrisa obstoječih prevodov.

#### Primer v Phi-3 CookBook

V **Phi-3 CookBook** sem uporabil naslednjo metodo za posodobitev vseh prevedenih datotek v španščini. To metodo priporočam, kadar pride do večjih sprememb v izvirni vsebini v več markdown dokumentih. Če je treba posodobiti le nekaj prevedenih markdown datotek, je bolj učinkovito, da te datoteke ročno izbrišete in nato uporabite metodo `-a` za dodajanje posodobljenih prevodov.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Prevajanje samo slik

Če želite prevesti samo slikovne datoteke v projektu, uporabite možnost `-img`:

```bash
translate -l "ko" -img
```

Ta ukaz bo prevedel samo slike v korejščino, ne da bi vplival na markdown datoteke.

### 6. Prevajanje samo markdown datotek

Če želite prevesti samo markdown datoteke v projektu, uporabite možnost `-md`:

```bash
translate -l "ko" -md
```

#### Primer v Phi-3 CookBook

V **Phi-3 CookBook** sem uporabil naslednjo metodo za preverjanje napak v prevodih korejskih datotek in samodejno ponovitev prevoda za vse datoteke, kjer so bile odkrite težave.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Ta možnost preveri napake v prevodih. Trenutno, če je razlika v prelomih vrstic med izvirno in prevedeno datoteko večja od šest, je datoteka označena kot problematična. V prihodnje nameravam to merilo izboljšati za večjo prilagodljivost.

Na primer, ta metoda je uporabna za odkrivanje manjkajočih delov ali pokvarjenih prevodov, in samodejno ponovno prevede te datoteke.

Če pa že veste, katere datoteke so problematične, je bolj učinkovito, da jih ročno izbrišete in uporabite možnost `-a` za ponovni prevod.

### 8. Način za odpravljanje napak

Za vklop podrobnega beleženja za odpravljanje težav uporabite možnost `-d`:

```bash
translate -l "ko" -d
```

Ta ukaz bo zagnal prevajanje v načinu za odpravljanje napak in prikazal dodatne informacije, ki vam lahko pomagajo pri iskanju težav med prevajanjem.

#### Primer v Phi-3 CookBook

V **Phi-3 CookBook** sem naletel na težavo, kjer so prevodi z veliko povezavami v markdown datotekah povzročili napake v oblikovanju, kot so pokvarjeni prevodi in prezrti prelomi vrstic. Za diagnosticiranje te težave sem uporabil možnost `-d`, da sem videl, kako poteka postopek prevajanja.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Prevajanje v vse jezike

Če želite projekt prevesti v vse podprte jezike, uporabite ključno besedo all.

> [!WARNING]
> Prevajanje v vse jezike hkrati lahko traja zelo dolgo, odvisno od velikosti projekta. Na primer, prevod **Phi-3 CookBook** v španščino je trajal približno 2 uri. Glede na obseg ni praktično, da ena oseba prevaja v 20 jezikov. Priporočljivo je, da delo razdelite med več sodelavcev, vsak naj prevaja enega ali dva jezika, in prevode posodabljate postopoma.

```bash
translate -l "all"
```

Ta ukaz bo projekt prevedel v vse razpoložljive jezike. Če nadaljujete, lahko prevajanje traja precej dolgo, odvisno od velikosti projekta.

> [!TIP]
>
> ### Ročno brisanje prevedenih datotek (neobvezno)
> Prevedene datoteke se zdaj samodejno zaznajo in počistijo, ko se izvorna datoteka posodobi.
>
> Če pa želite ročno posodobiti prevod – na primer, če želite ponovno prevesti določeno datoteko ali preglasiti sistemsko vedenje – lahko uporabite naslednji ukaz za izbris vseh različic datoteke v jezikovnih mapah.
>
> ### Na Windows:
> 1. **Uporaba Command Prompt**:
>    - Odprite Command Prompt.
>    - Pomaknite se v mapo, kjer so datoteke, z ukazom `cd`.
>    - Uporabite naslednji ukaz za izbris datotek:
>      ```
>      del /s *filename*
>      ```
>      Zamenjajte `filename` z delom imena datoteke, ki ga iščete. Možnost `/s` išče tudi po podmapah.
>
> 2. **Uporaba PowerShell**:
>    - Odprite PowerShell.
>    - Zaženite ta ukaz:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Zamenjajte `"C:\YourPath"` s potjo do mape in `filename` z želenim imenom.
>
> ### Na macOS/Linux:
> 1. **Uporaba Terminala**:
>   - Odprite Terminal.
>   - Pomaknite se v mapo z ukazom `cd`.
>   - Uporabite ukaz `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Zamenjajte `filename` z želenim imenom.
>
> Pred brisanjem vedno dvakrat preverite datoteke, da ne bi po nesreči izgubili pomembnih podatkov.
>
> Ko izbrišete datoteke, ki jih želite zamenjati, preprosto ponovno zaženite svoj ukaz `translate -l`, da posodobite najnovejše spremembe datotek.

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden s pomočjo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvoru jeziku naj velja za avtoritativni vir. Za kritične informacije priporočamo strokoven človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.