<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:57:19+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "sl"
}
-->
# Prevedite svoj projekt z orodjem Co-op Translator

**Co-op Translator** je orodje za ukazno vrstico (CLI), ki vam pomaga prevesti markdown in slikovne datoteke v vašem projektu v več jezikov. Ta razdelek pojasnjuje, kako uporabljati orodje, opisuje različne možnosti CLI in ponuja primere za različne primere uporabe.

> [!NOTE]
> Za popoln seznam ukazov in njihove podrobne opise si oglejte [Command reference](./command-reference.md).

---

## Primeri scenarijev in ukazi

Tukaj je nekaj pogostih primerov uporabe **Co-op Translator** skupaj z ustreznimi ukazi.

### 1. Osnovni prevod (en jezik)

Če želite prevesti celoten projekt (markdown datoteke in slike) v en jezik, na primer korejščino, uporabite naslednji ukaz:

```bash
translate -l "ko"
```

Ta ukaz bo prevedel vse markdown in slikovne datoteke v korejščino ter dodal nove prevode, ne da bi izbrisal obstoječe.

> [!TIP]
>
> Želite izvedeti, kateri jezikovni kodi so na voljo v **Co-op Translator**? Oglejte si razdelek [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) v repozitoriju za več podrobnosti.

#### Primer na Phi-3 CookBook

V **Phi-3 CookBook** sem uporabil naslednjo metodo za dodajanje korejskega prevoda obstoječih markdown datotek in slik.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Prevajanje več jezikov

Če želite prevesti svoj projekt v več jezikov (npr. španščino, francoščino in nemščino), uporabite ta ukaz:

```bash
translate -l "es fr de"
```

Ta ukaz bo prevedel projekt v španščino, francoščino in nemščino ter dodal nove prevode, ne da bi prepisal obstoječe.

#### Primer na Phi-3 CookBook

V **Phi-3 CookBook** sem po pridobitvi najnovejših sprememb za odraz zadnjih commitov uporabil naslednjo metodo za prevajanje novooddanih markdown datotek in slik.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Čeprav je običajno priporočljivo prevajati en jezik naenkrat, je v primerih, kot je ta, ko je treba dodati določene spremembe, lahko prevajanje več jezikov hkrati učinkovito.

### 3. Posodabljanje prevodov (izbriše obstoječe prevode)

Če želite posodobiti obstoječe prevode (tj. izbrisati trenutne prevode in jih nadomestiti z novimi), uporabite možnost `-u`. Ta izbriše vse obstoječe prevode za določene jezike in jih ponovno prevede.

```bash
translate -l "ko" -u
```

Opozorilo: Ta ukaz vas bo pred nadaljevanjem pozval k potrditvi brisanja obstoječih prevodov.

#### Primer na Phi-3 CookBook

V **Phi-3 CookBook** sem uporabil naslednjo metodo za posodobitev vseh prevedenih datotek v španščini. Priporočam uporabo te metode, kadar so večje spremembe v izvirni vsebini več markdown dokumentov. Če je treba posodobiti le nekaj prevedenih markdown datotek, je bolj učinkovito ročno izbrisati te specifične datoteke in nato uporabiti metodo `-a` za dodajanje posodobljenih prevodov.

### 5. Prevajanje samo slik

Če želite prevesti samo slikovne datoteke v projektu, uporabite možnost `-img`:

```bash
translate -l "ko" -img
```

Ta ukaz bo prevedel samo slike v korejščino, brez vpliva na markdown datoteke.

### 6. Prevajanje samo markdown datotek

Če želite prevesti samo markdown datoteke v projektu, uporabite možnost `-md`:

```bash
translate -l "ko" -md
```

### 7. Preverjanje napak v prevedenih datotekah

Če želite preveriti prevedene datoteke glede napak in po potrebi znova poskusiti prevod, uporabite možnost `-chk`:

```bash
translate -l "ko" -chk
```

Ta ukaz bo pregledal prevedene markdown datoteke in za vse datoteke z napakami poskusil prevod znova.

#### Primer na Phi-3 CookBook

V **Phi-3 CookBook** sem uporabil naslednjo metodo za preverjanje napak prevoda v korejskih datotekah in samodejno ponovno prevajanje za datoteke z zaznanimi težavami.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Ta možnost preverja napake prevoda. Trenutno, če je razlika v prelomih vrstic med izvirno in prevedeno datoteko več kot šest, se datoteka označi kot z napako prevoda. Načrtujem izboljšave tega kriterija za večjo prilagodljivost v prihodnosti.

Na primer, ta metoda je uporabna za odkrivanje manjkajočih delov ali poškodovanih prevodov in samodejno ponovi prevod za te datoteke.

Če pa že veste, katere datoteke povzročajo težave, je bolj učinkovito, da jih ročno izbrišete in uporabite možnost `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Ta ukaz bo zagnal prevajanje v načinu za odpravljanje napak, kar bo zagotovilo dodatne informacije v dnevniku, ki vam lahko pomagajo odkriti težave med prevajanjem.

#### Primer na Phi-3 CookBook

V **Phi-3 CookBook** sem naletel na težavo, kjer so prevodi z veliko povezavami v markdown datotekah povzročali napake pri oblikovanju, kot so pokvarjeni prevodi in prezrti prelomi vrstic. Za diagnostiko te težave sem uporabil možnost `-d`, da sem videl, kako poteka prevajanje.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Prevajanje vseh jezikov

Če želite prevesti projekt v vse podprte jezike, uporabite ključni izraz all.

> [!WARNING]
> Prevajanje vseh jezikov naenkrat lahko traja precej dolgo, odvisno od velikosti projekta. Na primer, prevajanje **Phi-3 CookBook** v španščino je trajalo približno 2 uri. Glede na obseg ni praktično, da bi ena oseba obdelovala 20 jezikov. Priporočljivo je delo razdeliti med več sodelavcev, kjer vsak upravlja enega ali dva jezika in prevode postopoma posodablja.

```bash
translate -l "all"
```

Ta ukaz bo prevedel projekt v vse razpoložljive jezike. Če nadaljujete, lahko prevajanje traja precej dolgo, odvisno od velikosti projekta.

> [!TIP]
>
> ### Ročno brisanje prevedenih datotek (neobvezno)
> Prevedene datoteke se zdaj samodejno zaznavajo in čistijo, ko je izvorna datoteka posodobljena.
>
> Če pa želite prevod ročno posodobiti – na primer, da ponovno naredite določeno datoteko ali preglasite sistemsko vedenje – lahko uporabite naslednji ukaz za brisanje vseh različic datoteke v vseh jezikovnih mapah.
>
> ### V sistemu Windows:
> 1. **Uporaba Command Prompt:**
>    - Odprite Command Prompt.
>    - Z ukazom `cd` se premaknite v mapo, kjer se datoteke nahajajo.
>    - Uporabite naslednji ukaz za brisanje datotek:
>      ```
>      del /s *filename*
>      ```
>      Opcija `/s` poišče tudi podmape.
>
> 2. **Uporaba PowerShell:**
>    - Odprite PowerShell.
>    - Zaženite ta ukaz:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Nadomestite `"C:\YourPath"` z ustrezno potjo.
>
> 3. **Ukaz `cd` in `find`:**
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>
> 4. **Ukaz `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l`:**
>    za posodobitev najnovejših sprememb datotek.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.