<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:54:42+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "cs"
}
-->
# Překládejte svůj projekt pomocí Co-op Translator

**Co-op Translator** je nástroj s příkazovým řádkem (CLI), který vám pomůže přeložit markdown a obrazové soubory ve vašem projektu do více jazyků. Tato sekce vysvětluje, jak nástroj používat, popisuje různé možnosti příkazového řádku a poskytuje příklady pro různé scénáře.

> [!NOTE]
> Pro kompletní seznam příkazů a jejich podrobný popis si prosím přečtěte [Command reference](./command-reference.md).

---

## Příklady scénářů a příkazů

Zde jsou některé běžné případy použití **Co-op Translator** spolu s příslušnými příkazy.

### 1. Základní překlad (jeden jazyk)

Chcete-li přeložit celý projekt (markdown soubory a obrázky) do jednoho jazyka, například korejštiny, použijte tento příkaz:

```bash
translate -l "ko"
```

Tento příkaz přeloží všechny markdown a obrázkové soubory do korejštiny a přidá nové překlady, aniž by mazal ty stávající.

> [!TIP]
>
> Chcete zjistit, jaké jazykové kódy jsou v **Co-op Translator** dostupné? Navštivte sekci [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) v repozitáři pro více informací.

#### Příklad na Phi-3 CookBook

V **Phi-3 CookBook** jsem použil následující metodu k přidání korejského překladu pro existující markdown soubory a obrázky.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Překlad do více jazyků

Chcete-li přeložit projekt do více jazyků (např. španělštiny, francouzštiny a němčiny), použijte tento příkaz:

```bash
translate -l "es fr de"
```

Tento příkaz přeloží projekt do španělštiny, francouzštiny a němčiny a přidá nové překlady, aniž by přepsal ty stávající.

#### Příklad na Phi-3 CookBook

V **Phi-3 CookBook**, po stažení nejnovějších změn, jsem použil následující metodu k překladu nově přidaných markdown souborů a obrázků.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Obecně se doporučuje překládat po jednom jazyce, ale v situacích jako je tato, kdy je potřeba přidat konkrétní změny, může být efektivní překládat více jazyků najednou.

### 3. Aktualizace překladů (maže stávající překlady)

Chcete-li aktualizovat stávající překlady (tj. smazat současné překlady a nahradit je novými), použijte volbu `-u`. Tím se smažou všechny stávající překlady pro zadané jazyky a znovu přeloží.

```bash
translate -l "ko" -u
```

Upozornění: Tento příkaz vás před smazáním stávajících překladů vyzve k potvrzení.

#### Příklad na Phi-3 CookBook

V **Phi-3 CookBook** jsem použil tuto metodu k aktualizaci všech přeložených souborů ve španělštině. Doporučuji tento postup, pokud došlo k významným změnám v původním obsahu napříč více markdown dokumenty. Pokud je potřeba aktualizovat jen pár přeložených markdown souborů, je efektivnější tyto konkrétní soubory ručně smazat a pak použít metodu `-a` k přidání aktualizovaných překladů.

### 5. Překlad pouze obrázků

Chcete-li přeložit pouze obrazové soubory ve vašem projektu, použijte volbu `-img`:

```bash
translate -l "ko" -img
```

Tento příkaz přeloží pouze obrázky do korejštiny, aniž by ovlivnil markdown soubory.

### 6. Překlad pouze markdown souborů

Chcete-li přeložit pouze markdown soubory ve vašem projektu, použijte volbu `-md`:

```bash
translate -l "ko" -md
```

### 7. Kontrola chyb v přeložených souborech

Pokud chcete zkontrolovat přeložené soubory na chyby a případně překlad zopakovat, použijte volbu `-chk`:

```bash
translate -l "ko" -chk
```

Tento příkaz prohledá přeložené markdown soubory a znovu přeloží ty, u kterých byly nalezeny chyby.

#### Příklad na Phi-3 CookBook

V **Phi-3 CookBook** jsem použil následující metodu ke kontrole chyb překladu v korejských souborech a automatickému opakování překladu u souborů s detekovanými problémy.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Tato volba kontroluje chyby překladu. V současnosti je soubor označen jako chybný, pokud je rozdíl v počtu zalomení řádků mezi originálem a překladem větší než šest. Plánuji tento kriterium v budoucnu vylepšit pro větší flexibilitu.

Například tato metoda je užitečná k odhalení chybějících částí nebo poškozených překladů a automaticky u nich znovu spustí překlad.

Pokud ale už víte, které soubory jsou problematické, je efektivnější tyto soubory ručně smazat a použít volbu `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Tento příkaz spustí překlad v režimu ladění (debug), který poskytuje další informace v logu, jež vám pomohou odhalit problémy během překladu.

#### Příklad na Phi-3 CookBook

V **Phi-3 CookBook** jsem narazil na problém, kdy překlady s mnoha odkazy v markdown souborech způsobovaly chyby ve formátování, například poškozené překlady a ignorování zalomení řádků. K diagnostice tohoto problému jsem použil volbu `-d`, abych viděl, jak překladový proces funguje.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Překlad do všech jazyků

Pokud chcete přeložit projekt do všech podporovaných jazyků, použijte klíčové slovo all.

> [!WARNING]
> Překlad do všech jazyků najednou může zabrat značné množství času v závislosti na velikosti projektu. Například překlad **Phi-3 CookBook** do španělštiny trval asi 2 hodiny. Vzhledem k rozsahu není praktické, aby jednu osobu zvládla 20 jazyků. Doporučuje se rozdělit práci mezi více přispěvatelů, z nichž každý spravuje jeden nebo dva jazyky a překlady postupně aktualizuje.

```bash
translate -l "all"
```

Tento příkaz přeloží projekt do všech dostupných jazyků. Pokud budete pokračovat, překlad může trvat značnou dobu v závislosti na velikosti projektu.

> [!TIP]
>
> ### Ruční mazání přeložených souborů (volitelné)
> Přeložené soubory jsou nyní automaticky detekovány a odstraněny při aktualizaci zdrojového souboru.
>
> Pokud ale chcete překlad ručně aktualizovat – například znovu přeložit konkrétní soubor nebo přepsat chování systému – můžete použít následující příkaz k odstranění všech verzí souboru ve složkách jednotlivých jazyků.
>
> ### Ve Windows:
> 1. **Použití Příkazového řádku (Command Prompt)**:
>    - Otevřete Příkazový řádek.
>    - Přejděte do složky, kde se soubory nacházejí, pomocí příkazu `cd`.
>    - Použijte tento příkaz k odstranění souborů:
>      ```
>      del /s *filename*
>      ```
>      Volba `/s` zajistí vyhledávání i v podsložkách.
>
> 2. **Použití PowerShellu**:
>    - Otevřete PowerShell.
>    - Spusťte tento příkaz:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Nahraďte `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` příkazem:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Nahraďte `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` příkazem pro aktualizaci nejnovějších změn souborů.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.