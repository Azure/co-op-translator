<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:54:16+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "hu"
}
-->
# Projekted fordítása a Co-op Translatorral

A **Co-op Translator** egy parancssoros eszköz (CLI), amely segít a projekted markdown és képfájljainak több nyelvre történő fordításában. Ebben a részben bemutatjuk az eszköz használatát, ismertetjük a különböző CLI opciókat, és példákat adunk különféle felhasználási esetekre.

> [!NOTE]
> A parancsok teljes listájáért és részletes leírásáért kérjük, tekintsd meg a [Command reference](./command-reference.md) dokumentumot.

---

## Példák és parancsok

Az alábbiakban néhány gyakori használati esetet mutatunk be a **Co-op Translator** eszközhöz, valamint a megfelelő parancsokat.

### 1. Alap fordítás (egy nyelv)

Ha az egész projektedet (markdown fájlok és képek) egyetlen nyelvre, például koreaira szeretnéd fordítani, használd a következő parancsot:

```bash
translate -l "ko"
```

Ez a parancs minden markdown és képfájlt lefordít koreaira, miközben megőrzi a meglévő fordításokat, és hozzáadja az újakokat.

> [!TIP]
>
> Szeretnéd látni, milyen nyelvkódok érhetők el a **Co-op Translator**-ban? Nézd meg a [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) szekciót a tárolóban további részletekért.

#### Példa a Phi-3 CookBook-on

A **Phi-3 CookBook** esetében a következő módszert használtam a koreai fordítás hozzáadására a meglévő markdown fájlokhoz és képekhez.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Több nyelv fordítása

Ha a projektedet több nyelvre (például spanyolra, franciára és németre) szeretnéd fordítani, használd ezt a parancsot:

```bash
translate -l "es fr de"
```

Ez a parancs a projektet spanyolra, franciára és németre fordítja, miközben megőrzi a meglévő fordításokat, és hozzáadja az újakokat.

#### Példa a Phi-3 CookBook-on

A **Phi-3 CookBook** esetében, miután lehúztam a legfrissebb változtatásokat, a következő módszert alkalmaztam az újonnan hozzáadott markdown fájlok és képek fordítására.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Általánosságban ajánlott egy nyelvet egyszerre fordítani, de olyan helyzetekben, amikor specifikus változtatásokat kell hozzáadni, hatékony lehet több nyelv egyszerre történő fordítása.

### 3. Fordítások frissítése (meglévő fordítások törlése)

Ha a meglévő fordításokat szeretnéd frissíteni (azaz törölni a jelenlegi fordításokat, és újakkal helyettesíteni őket), használd a `-u` opciót. Ez törli az adott nyelvek összes meglévő fordítását, majd újrafordítja azokat.

```bash
translate -l "ko" -u
```

Figyelem: Ez a parancs megerősítést kér, mielőtt törölné a meglévő fordításokat.

#### Példa a Phi-3 CookBook-on

A **Phi-3 CookBook** esetében a következő módszert használtam az összes spanyol fordított fájl frissítésére. Ezt a módszert ajánlom, ha jelentős változások történtek az eredeti tartalomban több markdown dokumentumban. Ha csak néhány fordított markdown fájlt kell frissíteni, hatékonyabb, ha kézzel törlöd az adott fájlokat, majd az `-a` módszerrel hozzáadod az új fordításokat.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Csak képek fordítása

Ha csak a projekt képfájljait szeretnéd lefordítani, használd a `-img` opciót:

```bash
translate -l "ko" -img
```

Ez a parancs csak a képeket fordítja koreaira, anélkül, hogy a markdown fájlokat érintené.

### 6. Csak markdown fájlok fordítása

Ha csak a markdown fájlokat szeretnéd lefordítani, használd a `-md` opciót:

```bash
translate -l "ko" -md
```

### 7. Fordított fájlok hibáinak ellenőrzése

Ha szeretnéd ellenőrizni a fordított fájlokat hibák után, és szükség esetén újrapróbálni a fordítást, használd a `-chk` opciót:

```bash
translate -l "ko" -chk
```

Ez a parancs átvizsgálja a fordított markdown fájlokat, és újrapróbálja a fordítást azoknál, amelyek hibát jeleznek.

#### Példa a Phi-3 CookBook-on

A **Phi-3 CookBook** esetében a következő módszert használtam a koreai fájlok fordítási hibáinak ellenőrzésére, és automatikusan újrapróbáltam a fordítást az érintett fájloknál.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Ez az opció fordítási hibákat keres. Jelenleg, ha az eredeti és a fordított fájl sorainak törése közötti különbség több mint hat, a fájlt fordítási hibával jelöli meg. Ezt a kritériumot a jövőben tervezem rugalmasabbá tenni.

Például ez a módszer hasznos hiányzó részek vagy sérült fordítások felismerésére, és automatikusan újrapróbálja az ilyen fájlok fordítását.

Ha azonban már tudod, mely fájlok problémásak, hatékonyabb kézzel törölni azokat, majd az `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` opcióval futtatni a fordítást:

```bash
translate -l "ko" -d
```

Ez a parancs debug módban futtatja a fordítást, további naplózási információkat szolgáltatva, amelyek segíthetnek az esetleges problémák azonosításában.

#### Példa a Phi-3 CookBook-on

A **Phi-3 CookBook** esetében előfordult olyan probléma, hogy a sok linket tartalmazó markdown fájlok fordításánál formázási hibák jelentkeztek, például törött fordítások és figyelmen kívül hagyott sortörések. A probléma diagnosztizálásához a `-d` opciót használtam, hogy lássam, hogyan működik a fordítási folyamat.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Minden nyelv fordítása

Ha a projektet az összes támogatott nyelvre szeretnéd lefordítani, használd az all kulcsszót.

> [!WARNING]
> Az összes nyelv egyszerre történő fordítása jelentős időt vehet igénybe a projekt méretétől függően. Például a **Phi-3 CookBook** spanyol fordítása körülbelül 2 órát vett igénybe. Figyelembe véve a méretet, nem praktikus, hogy egyetlen személy kezelje a 20 nyelvet. Ajánlott a munkát több közreműködőre bontani, akik egy-egy vagy két nyelvet kezelnek, és fokozatosan frissítik a fordításokat.

```bash
translate -l "all"
```

Ez a parancs a projektet az összes elérhető nyelvre lefordítja. Ha folytatod, a fordítás jelentős időt vehet igénybe a projekt méretétől függően.

> [!TIP]
>
> ### Fordított fájlok kézi törlése (opcionális)
> A fordított fájlok most automatikusan felismerésre és törlésre kerülnek, amikor egy forrásfájl frissül.
>
> Ha azonban manuálisan szeretnél frissíteni egy fordítást – például egy adott fájl újrafordításához vagy a rendszer viselkedésének felülírásához – használhatod a következő parancsot az adott fájl összes nyelvi mappában történő törlésére.
>
> ### Windows rendszeren:
> 1. **Parancssor használata**:
>    - Nyisd meg a Parancssort.
>    - Navigálj a fájlok helyére a `cd` paranccsal.
>    - Használd a következő parancsot a fájlok törléséhez:
>      ```
>      del /s *filename*
>      ```
>      A `filename` with the specific part of the file name you're looking for. The `/s` opció a almappákban is keres.
>
> 2. **PowerShell használata**:
>    - Nyisd meg a PowerShell-t.
>    - Futtasd ezt a parancsot:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      A `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` parancs:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     A `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` parancs az utolsó fájlváltozások frissítésére szolgál.

**Felelősségkizárás**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy téves értelmezésekért.