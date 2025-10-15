<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:52:42+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "cs"
}
-->
# Překlad vašeho projektu pomocí Co-op Translatoru

**Co-op Translator** je nástroj pro příkazovou řádku (CLI), který vám pomůže překládat markdown soubory a obrázky ve vašem projektu do více jazyků. Tato sekce vysvětluje, jak nástroj používat, popisuje různé možnosti CLI a uvádí příklady pro různé situace.

> [!NOTE]
> Kompletní seznam příkazů a jejich podrobný popis najdete v [Referenci příkazů](./command-reference.md).

---

## Příklady scénářů a příkazů

Zde je několik běžných způsobů použití **Co-op Translatoru** spolu s příslušnými příkazy.

### 1. Základní překlad (jeden jazyk)

Pokud chcete přeložit celý projekt (markdown soubory a obrázky) do jednoho jazyka, například do korejštiny, použijte tento příkaz:

```bash
translate -l "ko"
```

Tímto příkazem přeložíte všechny markdown soubory a obrázky do korejštiny, přičemž se přidají nové překlady, aniž by se mazaly stávající.

> [!TIP]
>
> Chcete zjistit, jaké jazykové kódy jsou v **Co-op Translatoru** dostupné? Podívejte se do sekce [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) v repozitáři.

#### Příklad na Phi-3 CookBook

V **Phi-3 CookBook** jsem použil následující postup pro přidání korejského překladu ke stávajícím markdown souborům a obrázkům.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Překlad do více jazyků

Pokud chcete projekt přeložit do více jazyků (například španělštiny, francouzštiny a němčiny), použijte tento příkaz:

```bash
translate -l "es fr de"
```

Tímto příkazem přeložíte projekt do španělštiny, francouzštiny a němčiny, přičemž se přidají nové překlady bez přepsání těch stávajících.

#### Příklad na Phi-3 CookBook

V **Phi-3 CookBook** jsem po stažení nejnovějších změn, abych měl aktuální obsah, použil tento postup pro překlad nově přidaných markdown souborů a obrázků.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Obecně je doporučeno překládat jeden jazyk najednou, ale v situacích, kdy je potřeba přidat konkrétní změny, může být efektivní překládat více jazyků najednou.

### 3. Aktualizace překladů (maže stávající překlady)

Pokud potřebujete aktualizovat stávající překlady (tj. smazat aktuální překlady a nahradit je novými), použijte volbu `-u`. Tímto se smažou všechny existující překlady pro zvolené jazyky a provedou se nové překlady.

```bash
translate -l "ko" -u
```

Upozornění: Tento příkaz vás před smazáním stávajících překladů požádá o potvrzení.

#### Příklad na Phi-3 CookBook

V **Phi-3 CookBook** jsem použil tento postup pro aktualizaci všech přeložených souborů ve španělštině. Doporučuji tento způsob, pokud došlo k větším změnám v původním obsahu napříč více markdown dokumenty. Pokud je potřeba aktualizovat jen několik přeložených markdown souborů, je efektivnější tyto konkrétní soubory ručně smazat a pak použít metodu `-a` pro přidání nových překladů.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Překlad pouze obrázků

Pokud chcete přeložit pouze obrázky ve vašem projektu, použijte volbu `-img`:

```bash
translate -l "ko" -img
```

Tímto příkazem přeložíte pouze obrázky do korejštiny, aniž by se změnily markdown soubory.

### 6. Překlad pouze markdown souborů

Pokud chcete přeložit pouze markdown soubory ve vašem projektu, použijte volbu `-md`:

```bash
translate -l "ko" -md
```

#### Příklad na Phi-3 CookBook

V **Phi-3 CookBook** jsem použil tento postup pro kontrolu překladových chyb v korejských souborech a automatické opakování překladu u souborů, kde byly zjištěny problémy.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Tato volba kontroluje překladové chyby. V současnosti, pokud se počet zalomení řádků mezi originálem a překladem liší o více než šest, je soubor označen jako chybný. Plánuji toto kritérium do budoucna zpřesnit pro větší flexibilitu.

Tento postup je užitečný například pro detekci chybějících částí nebo poškozených překladů a automaticky znovu přeloží tyto soubory.

Pokud ale už víte, které soubory jsou problematické, je efektivnější je ručně smazat a použít volbu `-a` pro jejich opětovný překlad.

### 8. Režim ladění

Pokud potřebujete podrobné logování pro řešení problémů, použijte volbu `-d`:

```bash
translate -l "ko" -d
```

Tímto příkazem spustíte překlad v režimu ladění, což poskytne další informace v logu, které vám pomohou identifikovat případné problémy během překladu.

#### Příklad na Phi-3 CookBook

V **Phi-3 CookBook** jsem narazil na problém, kdy překlady s mnoha odkazy v markdown souborech způsobovaly chyby ve formátování, například rozbité překlady nebo ignorovaná zalomení řádků. Pro diagnostiku jsem použil volbu `-d`, abych zjistil, jak překladový proces funguje.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Překlad do všech jazyků

Pokud chcete projekt přeložit do všech podporovaných jazyků, použijte klíčové slovo all.

> [!WARNING]
> Překlad do všech jazyků najednou může trvat velmi dlouho v závislosti na velikosti projektu. Například překlad **Phi-3 CookBook** do španělštiny trval asi 2 hodiny. Vzhledem k rozsahu není praktické, aby jeden člověk zvládl 20 jazyků. Doporučujeme rozdělit práci mezi více přispěvatelů, každý si vezme jeden nebo dva jazyky, a překlady postupně aktualizovat.

```bash
translate -l "all"
```

Tímto příkazem přeložíte projekt do všech dostupných jazyků. Pokud budete pokračovat, překlad může trvat dlouho podle velikosti projektu.

> [!TIP]
>
> ### Ruční mazání přeložených souborů (volitelné)
> Přeložené soubory jsou nyní automaticky detekovány a vyčištěny, když je zdrojový soubor aktualizován.
>
> Pokud ale chcete překlad ručně aktualizovat – například znovu přeložit konkrétní soubor nebo přepsat chování systému – můžete použít následující příkaz pro smazání všech verzí souboru ve složkách s jazyky.
>
> ### Ve Windows:
> 1. **Použití příkazového řádku**:
>    - Otevřete příkazový řádek.
>    - Přejděte do složky, kde se soubory nacházejí, pomocí příkazu `cd`.
>    - Použijte tento příkaz pro smazání souborů:
>      ```
>      del /s *filename*
>      ```
>      Nahraďte `filename` konkrétní částí názvu souboru, kterou hledáte. Volba `/s` prohledává i podadresáře.
>
> 2. **Použití PowerShellu**:
>    - Otevřete PowerShell.
>    - Spusťte tento příkaz:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Nahraďte `"C:\YourPath"` cestou ke složce a `filename` konkrétním názvem.
>
> ### Na macOS/Linux:
> 1. **Použití terminálu**:
>   - Otevřete terminál.
>   - Přejděte do adresáře pomocí `cd`.
>   - Použijte příkaz `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Nahraďte `filename` konkrétním názvem.
>
> Před smazáním souborů si je vždy zkontrolujte, abyste předešli nechtěné ztrátě dat.
>
> Jakmile soubory smažete, které je potřeba nahradit, jednoduše znovu spusťte svůj příkaz `translate -l` pro aktualizaci nejnovějších změn.

---

**Prohlášení**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné výklady vzniklé v důsledku použití tohoto překladu.