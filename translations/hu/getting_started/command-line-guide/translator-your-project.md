<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:49:33+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "hu"
}
-->
# Fordítsd le a projektedet a Co-op Translator segítségével

A **Co-op Translator** egy parancssori eszköz (CLI), amely segít a projektedben található markdown és képfájlokat több nyelvre lefordítani. Ez a szakasz bemutatja az eszköz használatát, ismerteti a különböző CLI opciókat, és példákat ad különféle felhasználási esetekre.

> [!NOTE]
> Az összes parancs és részletes leírásuk teljes listájáért lásd a [Parancsreferencia](./command-reference.md) oldalt.

---

## Példa szcenáriók és parancsok

Íme néhány gyakori felhasználási eset a **Co-op Translator**-hoz, a megfelelő parancsokkal együtt.

### 1. Alapfordítás (egy nyelvre)

Ha a teljes projektedet (markdown fájlokat és képeket) egyetlen nyelvre, például koreaira szeretnéd lefordítani, használd a következő parancsot:

```bash
translate -l "ko"
```

Ez a parancs minden markdown és képfájlt lefordít koreaira, új fordításokat adva hozzá anélkül, hogy a meglévőket törölné.

> [!TIP]
>
> Szeretnéd tudni, hogy milyen nyelvkódok érhetők el a **Co-op Translator**-ban? Nézd meg a [Támogatott nyelvek](https://github.com/Azure/co-op-translator#supported-languages) szekciót a repóban a részletekért.

#### Példa a Phi-3 CookBook-ban

A **Phi-3 CookBook**-ban a következő módszert használtam, hogy hozzáadjam a koreai fordítást a meglévő markdown fájlokhoz és képekhez.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Fordítás több nyelvre

Ha a projektedet több nyelvre (például spanyolra, franciára és németre) szeretnéd lefordítani, használd ezt a parancsot:

```bash
translate -l "es fr de"
```

Ez a parancs lefordítja a projektet spanyolra, franciára és németre, új fordításokat adva hozzá anélkül, hogy a meglévőket felülírná.

#### Példa a Phi-3 CookBook-ban

A **Phi-3 CookBook**-ban, miután lehúztam a legfrissebb változtatásokat, hogy tükrözzék a legutóbbi commitokat, a következő módszert használtam az újonnan hozzáadott markdown fájlok és képek fordítására.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Bár általában ajánlott egyszerre csak egy nyelvre fordítani, ilyen esetekben, amikor konkrét változtatásokat kell hozzáadni, hatékony lehet több nyelvet egyszerre fordítani.

### 3. Fordítások frissítése (meglévő fordítások törlése)

Ha a meglévő fordításokat szeretnéd frissíteni (azaz törölni a jelenlegi fordításokat, és újakkal helyettesíteni), használd a `-u` opciót. Ez törli az összes meglévő fordítást a megadott nyelveken, majd újrafordítja őket.

```bash
translate -l "ko" -u
```

Figyelem: Ez a parancs megerősítést kér, mielőtt törölné a meglévő fordításokat.

#### Példa a Phi-3 CookBook-ban

A **Phi-3 CookBook**-ban a következő módszert használtam az összes spanyol fordítású fájl frissítésére. Ezt a módszert akkor ajánlom, ha jelentős változások történtek az eredeti tartalomban több markdown dokumentumban is. Ha csak néhány fordított markdown fájlt kell frissíteni, hatékonyabb manuálisan törölni azokat a fájlokat, majd az `-a` módszerrel hozzáadni a frissített fordításokat.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Csak képek fordítása

Ha csak a projekted képfájljait szeretnéd lefordítani, használd a `-img` opciót:

```bash
translate -l "ko" -img
```

Ez a parancs csak a képeket fordítja le koreaira, a markdown fájlokat nem érinti.

### 6. Csak markdown fájlok fordítása

Ha csak a markdown fájlokat szeretnéd lefordítani a projektedben, használd a `-md` opciót:

```bash
translate -l "ko" -md
```

#### Példa a Phi-3 CookBook-ban

A **Phi-3 CookBook**-ban a következő módszert használtam, hogy ellenőrizzem a fordítási hibákat a koreai fájlokban, és automatikusan újrapróbáljam a fordítást azoknál a fájloknál, ahol hibát találtam.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Ez az opció ellenőrzi a fordítási hibákat. Jelenleg, ha a sortörések száma az eredeti és a fordított fájl között több mint hat, a fájl hibásnak minősül. Ezt a feltételt a jövőben rugalmasabbá szeretném tenni.

Ez a módszer például hasznos hiányzó részek vagy sérült fordítások észlelésére, és automatikusan újrapróbálja a fordítást az érintett fájloknál.

Ha azonban már tudod, mely fájlok problémásak, hatékonyabb manuálisan törölni azokat, majd az `-a` opcióval újrafordítani őket.

### 8. Hibakeresési mód

Ha részletes naplózást szeretnél bekapcsolni a hibakereséshez, használd a `-d` opciót:

```bash
translate -l "ko" -d
```

Ez a parancs hibakeresési módban futtatja a fordítást, és további naplózási információkat ad, amelyek segíthetnek a fordítási folyamat során felmerülő problémák azonosításában.

#### Példa a Phi-3 CookBook-ban

A **Phi-3 CookBook**-ban olyan problémába ütköztem, hogy a sok linket tartalmazó markdown fájlok fordításánál formázási hibák jelentkeztek, például megszakadt fordítások és figyelmen kívül hagyott sortörések. Ennek diagnosztizálásához a `-d` opciót használtam, hogy lássam, hogyan működik a fordítási folyamat.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Fordítás minden nyelvre

Ha a projektet az összes támogatott nyelvre le szeretnéd fordítani, használd az all kulcsszót.

> [!WARNING]
> Az összes nyelvre történő fordítás egyszerre jelentős időt vehet igénybe a projekt méretétől függően. Például a **Phi-3 CookBook** spanyolra fordítása körülbelül 2 órát vett igénybe. Ekkora léptékben nem életszerű, hogy egy ember 20 nyelvet kezeljen. Ajánlott a munkát több közreműködő között megosztani, mindegyikük 1-2 nyelvet kezeljen, és fokozatosan frissítsék a fordításokat.

```bash
translate -l "all"
```

Ez a parancs a projektet az összes elérhető nyelvre lefordítja. Ha folytatod, a fordítás a projekt méretétől függően jelentős időt vehet igénybe.

> [!TIP]
>
> ### Fordított fájlok manuális törlése (opcionális)
> A fordított fájlokat mostantól automatikusan felismeri és tisztítja a rendszer, ha egy forrásfájl frissül.
>
> Ha azonban manuálisan szeretnéd frissíteni a fordítást – például egy adott fájlt újra lefordítani vagy felülírni a rendszer viselkedését –, a következő parancsokkal törölheted a fájl összes verzióját a nyelvi mappákból.
>
> ### Windows alatt:
> 1. **Parancssor használata**:
>    - Nyisd meg a Parancssort.
>    - Navigálj a fájlokat tartalmazó mappába a `cd` paranccsal.
>    - Használd a következő parancsot a fájlok törléséhez:
>      ```
>      del /s *filename*
>      ```
>      Cseréld ki a `filename` részt arra a fájlnévrészre, amit keresel. A `/s` opció az almappákban is keres.
>
> 2. **PowerShell használata**:
>    - Nyisd meg a PowerShellt.
>    - Futtasd ezt a parancsot:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Cseréld ki a `"C:\YourPath"` részt a mappa elérési útjára, a `filename`-t pedig a konkrét névre.
>
> ### macOS/Linux alatt:
> 1. **Terminál használata**:
>   - Nyisd meg a Terminált.
>   - Navigálj a könyvtárba a `cd` paranccsal.
>   - Használd a `find` parancsot:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Cseréld ki a `filename`-t a konkrét névre.
>
> Mindig ellenőrizd a fájlokat törlés előtt, hogy elkerüld a véletlen adatvesztést.
>
> Miután törölted a cserélendő fájlokat, egyszerűen futtasd újra a `translate -l` parancsodat, hogy frissítsd a legutóbbi fájlváltozásokat.

---

**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.