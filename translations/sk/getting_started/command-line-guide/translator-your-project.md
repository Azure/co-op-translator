<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:55:09+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "sk"
}
-->
# Preložte svoj projekt pomocou Co-op Translator

**Co-op Translator** je nástroj s príkazovým riadkom (CLI), ktorý vám pomôže preložiť markdown a obrázkové súbory vo vašom projekte do viacerých jazykov. Táto časť vysvetľuje, ako nástroj používať, popisuje rôzne možnosti CLI a poskytuje príklady pre rôzne použitia.

> [!NOTE]
> Pre kompletný zoznam príkazov a ich podrobný popis si pozrite [Command reference](./command-reference.md).

---

## Príkladové scenáre a príkazy

Tu je niekoľko bežných prípadov použitia **Co-op Translator** spolu s vhodnými príkazmi.

### 1. Základný preklad (jeden jazyk)

Ak chcete preložiť celý projekt (markdown súbory a obrázky) do jedného jazyka, napríklad kórejčiny, použite nasledujúci príkaz:

```bash
translate -l "ko"
```

Tento príkaz preloží všetky markdown a obrázkové súbory do kórejčiny a pridá nové preklady bez odstránenia existujúcich.

> [!TIP]
>
> Chcete vedieť, ktoré jazykové kódy sú dostupné v **Co-op Translator**? Navštívte sekciu [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) v repozitári pre viac informácií.

#### Príklad na Phi-3 CookBook

V **Phi-3 CookBook** som použil nasledujúci spôsob na pridanie kórejského prekladu pre existujúce markdown súbory a obrázky.

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

V **Phi-3 CookBook**, po stiahnutí najnovších zmien, aby sa zohľadnili posledné commity, som použil nasledujúci spôsob na preklad novo pridaných markdown súborov a obrázkov.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Aj keď sa všeobecne odporúča prekladať jeden jazyk naraz, v situáciách, kde je potrebné pridať konkrétne zmeny, môže byť efektívnejšie prekladať viaceré jazyky naraz.

### 3. Aktualizácia prekladov (vymaže existujúce preklady)

Ak chcete aktualizovať existujúce preklady (t. j. vymazať súčasné preklady a nahradiť ich novými), použite možnosť `-u`. Táto možnosť vymaže všetky existujúce preklady pre zvolené jazyky a znovu ich preloží.

```bash
translate -l "ko" -u
```

Upozornenie: Tento príkaz vás pred vymazaním existujúcich prekladov vyzve na potvrdenie.

#### Príklad na Phi-3 CookBook

V **Phi-3 CookBook** som použil tento spôsob na aktualizáciu všetkých preložených súborov v španielčine. Odporúčam použiť túto metódu, keď sú výrazné zmeny v pôvodnom obsahu viacerých markdown dokumentov. Ak je potrebné aktualizovať len niekoľko preložených markdown súborov, je efektívnejšie tieto súbory manuálne vymazať a potom použiť metódu `-a` na pridanie aktualizovaných prekladov.

### 5. Preklad iba obrázkov

Ak chcete preložiť iba obrázkové súbory vo vašom projekte, použite možnosť `-img`:

```bash
translate -l "ko" -img
```

Tento príkaz preloží iba obrázky do kórejčiny bez zásahu do markdown súborov.

### 6. Preklad iba markdown súborov

Ak chcete preložiť iba markdown súbory vo vašom projekte, použite možnosť `-md`:

```bash
translate -l "ko" -md
```

### 7. Kontrola chýb v preložených súboroch

Ak chcete skontrolovať preložené súbory na chyby a v prípade potreby preklad zopakovať, použite možnosť `-chk`:

```bash
translate -l "ko" -chk
```

Tento príkaz prehľadá preložené markdown súbory a v prípade chýb v preklade ich automaticky znova preloží.

#### Príklad na Phi-3 CookBook

V **Phi-3 CookBook** som použil tento spôsob na kontrolu chýb v kórejských prekladoch a automatické opakovanie prekladu pre súbory s detegovanými problémami.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Táto možnosť kontroluje chyby v preklade. Momentálne, ak je rozdiel v počte zalomení riadkov medzi originálnym a preloženým súborom väčší ako šesť, súbor je označený ako chybný preklad. Plánujem tento kritérium v budúcnosti zlepšiť pre väčšiu flexibilitu.

Napríklad táto metóda je užitočná na detekciu chýbajúcich častí alebo poškodených prekladov a automaticky zopakuje preklad týchto súborov.

Ak však už viete, ktoré súbory sú problémové, je efektívnejšie tieto súbory manuálne vymazať a použiť možnosť `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Tento príkaz spustí preklad v debug móde, ktorý poskytuje ďalšie logovacie informácie, ktoré vám môžu pomôcť identifikovať problémy počas prekladu.

#### Príklad na Phi-3 CookBook

V **Phi-3 CookBook** som narazil na problém, kde preklady s mnohými odkazmi v markdown súboroch spôsobovali chyby formátovania, ako sú poškodené preklady a ignorované zalomenia riadkov. Na diagnostiku tohto problému som použil možnosť `-d`, aby som videl, ako prekladový proces funguje.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Preklad do všetkých jazykov

Ak chcete preložiť projekt do všetkých podporovaných jazykov, použite kľúčové slovo all.

> [!WARNING]
> Preklad všetkých jazykov naraz môže trvať výrazne dlho v závislosti od veľkosti projektu. Napríklad preklad **Phi-3 CookBook** do španielčiny trval približne 2 hodiny. Vzhľadom na rozsah nie je praktické, aby jedna osoba spravovala 20 jazykov. Odporúča sa rozdeliť prácu medzi viacerých prispievateľov, pričom každý spravuje jeden alebo dva jazyky a preklady sa aktualizujú postupne.

```bash
translate -l "all"
```

Tento príkaz preloží projekt do všetkých dostupných jazykov. Ak budete pokračovať, preklad môže trvať výrazne dlho v závislosti od veľkosti projektu.

> [!TIP]
>
> ### Manuálne vymazanie preložených súborov (voliteľné)
> Preložené súbory sú teraz automaticky detegované a vyčistené pri aktualizácii zdrojového súboru.
>
> Ak však chcete manuálne aktualizovať preklad – napríklad znovu preložiť konkrétny súbor alebo prepísať správanie systému – môžete použiť nasledujúci príkaz na vymazanie všetkých verzií súboru vo všetkých jazykových priečinkoch.
>
> ### Na Windows:
> 1. **Použitie Command Prompt**:
>    - Otvorte Command Prompt.
>    - Pomocou príkazu `cd` prejdite do priečinka, kde sa súbory nachádzajú.
>    - Použite nasledujúci príkaz na vymazanie súborov:
>      ```
>      del /s *filename*
>      ```
>      Voľba `/s` vyhľadáva aj v podpriečinkoch.
>
> 2. **Použitie PowerShell**:
>    - Otvorte PowerShell.
>    - Spustite tento príkaz:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Nahraďte `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` príkazom:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Nahraďte `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` príkazom na aktualizáciu najnovších zmien súborov.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.