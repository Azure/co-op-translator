<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:55:41+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "sk"
}
-->
# Preložte svoj projekt pomocou Co-op Translator

**Co-op Translator** je nástroj s príkazovým riadkom (CLI), ktorý vám pomôže preložiť markdown a obrazové súbory vo vašom projekte do viacerých jazykov. Táto sekcia vysvetľuje, ako nástroj používať, popisuje rôzne možnosti CLI a uvádza príklady pre rôzne situácie.

> [!NOTE]
> Kompletný zoznam príkazov a ich podrobné popisy nájdete v [Referencii príkazov](./command-reference.md).

---

## Príkladové scenáre a príkazy

Tu je niekoľko bežných spôsobov použitia **Co-op Translator** spolu s vhodnými príkazmi.

### 1. Základný preklad (jeden jazyk)

Ak chcete preložiť celý projekt (markdown súbory a obrázky) do jedného jazyka, napríklad kórejčiny, použite tento príkaz:

```bash
translate -l "ko"
```

Tento príkaz preloží všetky markdown a obrazové súbory do kórejčiny, pričom pridá nové preklady bez vymazania existujúcich.

> [!TIP]
>
> Chcete zistiť, aké jazykové kódy sú dostupné v **Co-op Translator**? Pozrite si sekciu [Podporované jazyky](https://github.com/Azure/co-op-translator#supported-languages) v repozitári pre viac informácií.

#### Príklad na Phi-3 CookBook

V **Phi-3 CookBook** som použil nasledujúci postup na pridanie kórejského prekladu existujúcich markdown súborov a obrázkov.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Preklad do viacerých jazykov

Ak chcete preložiť projekt do viacerých jazykov (napr. španielčiny, francúzštiny a nemčiny), použite tento príkaz:

```bash
translate -l "es fr de"
```

Tento príkaz preloží projekt do španielčiny, francúzštiny a nemčiny, pričom pridá nové preklady bez prepísania existujúcich.

#### Príklad na Phi-3 CookBook

V **Phi-3 CookBook** som po stiahnutí najnovších zmien, aby sa zohľadnili posledné commity, použil tento postup na preklad novo pridaných markdown súborov a obrázkov.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Vo všeobecnosti sa odporúča prekladať jeden jazyk naraz, ale v situáciách, keď je potrebné pridať konkrétne zmeny, môže byť efektívne prekladať viac jazykov naraz.

### 3. Aktualizácia prekladov (vymaže existujúce preklady)

Ak chcete aktualizovať existujúce preklady (t.j. vymazať aktuálne preklady a nahradiť ich novými), použite možnosť `-u`. Táto voľba vymaže všetky existujúce preklady pre zvolené jazyky a preloží ich nanovo.

```bash
translate -l "ko" -u
```

Upozornenie: Tento príkaz vás pred pokračovaním vyzve na potvrdenie vymazania existujúcich prekladov.

#### Príklad na Phi-3 CookBook

V **Phi-3 CookBook** som použil tento postup na aktualizáciu všetkých preložených súborov v španielčine. Odporúčam tento spôsob, ak došlo k výrazným zmenám v pôvodnom obsahu vo viacerých markdown dokumentoch. Ak je potrebné aktualizovať len niekoľko preložených markdown súborov, je efektívnejšie tieto konkrétne súbory manuálne vymazať a potom použiť metódu `-a` na pridanie aktualizovaných prekladov.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Preklad iba obrázkov

Ak chcete preložiť iba obrazové súbory vo vašom projekte, použite možnosť `-img`:

```bash
translate -l "ko" -img
```

Tento príkaz preloží iba obrázky do kórejčiny bez ovplyvnenia markdown súborov.

### 6. Preklad iba markdown súborov

Ak chcete preložiť iba markdown súbory vo vašom projekte, použite možnosť `-md`:

```bash
translate -l "ko" -md
```

#### Príklad na Phi-3 CookBook

V **Phi-3 CookBook** som použil tento postup na kontrolu chýb v preklade kórejských súborov a automatické opätovné preloženie súborov, kde boli zistené problémy.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Táto voľba kontroluje chyby v preklade. Momentálne, ak je rozdiel v počte zalomení riadkov medzi originálom a prekladom väčší ako šesť, súbor je označený ako chybný preklad. Plánujem toto kritérium v budúcnosti upraviť pre väčšiu flexibilitu.

Tento spôsob je užitočný na odhalenie chýbajúcich častí alebo poškodených prekladov a automaticky opätovne preloží tieto súbory.

Ak však už viete, ktoré súbory sú problematické, je efektívnejšie ich manuálne vymazať a použiť možnosť `-a` na ich opätovný preklad.

### 8. Režim ladenia (Debug Mode)

Ak chcete zapnúť podrobné logovanie pre účely diagnostiky, použite možnosť `-d`:

```bash
translate -l "ko" -d
```

Tento príkaz spustí preklad v debug režime a poskytne podrobnejšie informácie o priebehu, ktoré vám môžu pomôcť identifikovať problémy počas prekladu.

#### Príklad na Phi-3 CookBook

V **Phi-3 CookBook** som narazil na problém, kde preklady s veľkým počtom odkazov v markdown súboroch spôsobovali chyby vo formátovaní, napríklad rozbité preklady a ignorované zalomenia riadkov. Na diagnostiku som použil možnosť `-d`, aby som videl, ako preklad prebieha.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Preklad do všetkých jazykov

Ak chcete preložiť projekt do všetkých podporovaných jazykov, použite kľúčové slovo all.

> [!WARNING]
> Preklad do všetkých jazykov naraz môže trvať veľmi dlho v závislosti od veľkosti projektu. Napríklad preklad **Phi-3 CookBook** do španielčiny trval asi 2 hodiny. Pri takomto rozsahu nie je praktické, aby jeden človek spravoval 20 jazykov. Odporúča sa rozdeliť prácu medzi viacerých prispievateľov, pričom každý spravuje jeden alebo dva jazyky, a preklady aktualizovať postupne.

```bash
translate -l "all"
```

Tento príkaz preloží projekt do všetkých dostupných jazykov. Ak budete pokračovať, preklad môže trvať dlho v závislosti od veľkosti projektu.

> [!TIP]
>
> ### Manuálne vymazanie preložených súborov (voliteľné)
> Preložené súbory sa teraz automaticky detegujú a čistia, keď sa zdrojový súbor aktualizuje.
>
> Ak však chcete manuálne aktualizovať preklad – napríklad opätovne preložiť konkrétny súbor alebo prepísať systémové správanie – môžete použiť nasledujúci príkaz na vymazanie všetkých verzií súboru vo všetkých jazykových priečinkoch.
>
> ### Vo Windows:
> 1. **Použitie Command Prompt**:
>    - Otvorte Command Prompt.
>    - Prejdite do priečinka, kde sa súbory nachádzajú, pomocou príkazu `cd`.
>    - Použite nasledujúci príkaz na vymazanie súborov:
>      ```
>      del /s *filename*
>      ```
>      Nahraďte `filename` konkrétnou časťou názvu súboru, ktorú hľadáte. Voľba `/s` prehľadáva aj podpriečinky.
>
> 2. **Použitie PowerShell**:
>    - Otvorte PowerShell.
>    - Spustite tento príkaz:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Nahraďte `"C:\YourPath"` cestou k priečinku a `filename` konkrétnym názvom.
>
> ### Na macOS/Linux:
> 1. **Použitie Terminálu**:
>   - Otvorte Terminál.
>   - Prejdite do adresára pomocou `cd`.
>   - Použite príkaz `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Nahraďte `filename` konkrétnym názvom.
>
> Vždy si pred vymazaním súborov skontrolujte, čo mažete, aby ste predišli nechceným stratám.
>
> Po vymazaní súborov, ktoré chcete nahradiť, jednoducho znova spustite príkaz `translate -l`, aby ste aktualizovali najnovšie zmeny súborov.

---

**Vyhlásenie o vylúčení zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj sa považuje pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.