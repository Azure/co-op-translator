<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:49:02+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "hu"
}
-->
# Microsoft Co-op Translator hibaelhárítási útmutató

## Áttekintés
A Microsoft Co-Op Translator egy hatékony eszköz, amellyel Markdown dokumentumokat lehet zökkenőmentesen lefordítani. Ez az útmutató segít a leggyakoribb problémák megoldásában, amelyek az eszköz használata során felmerülhetnek.

## Gyakori problémák és megoldások

### 1. Markdown tag probléma
**Probléma:** A lefordított Markdown dokumentum tetején megjelenik egy `markdown` tag, ami megjelenítési hibákat okoz.

**Megoldás:** Egyszerűen törölje a dokumentum tetején lévő `markdown` taget. Így a Markdown fájl helyesen fog megjelenni.

**Lépések:**
1. Nyissa meg a lefordított Markdown (`.md`) fájlt.
2. Keresse meg a dokumentum tetején a `markdown` taget.
3. Törölje ezt a taget.
4. Mentse el a fájlt.
5. Nyissa meg újra, hogy ellenőrizze a helyes megjelenítést.

### 2. Beágyazott képek URL problémája
**Probléma:** A beágyazott képek URL-je nem egyezik a nyelvi lokalizációval, emiatt hibás vagy hiányzó képek jelennek meg.

**Megoldás:** Ellenőrizze a képek URL-jét, és győződjön meg róla, hogy megfelel a dokumentum nyelvének. Minden kép a `translated_images` mappában található, és a fájlnévben szerepel a nyelvi lokalizáció.

**Lépések:**
1. Nyissa meg a lefordított Markdown dokumentumot.
2. Keresse meg a beágyazott képeket és azok URL-jeit.
3. Ellenőrizze, hogy a képfájl nevében szereplő nyelvi kód egyezik-e a dokumentum nyelvével.
4. Szükség esetén módosítsa az URL-t.
5. Mentse el a változtatásokat, és ellenőrizze a képek helyes megjelenítését.

### 3. Fordítás pontossága
**Probléma:** A lefordított tartalom nem pontos, vagy további szerkesztést igényel.

**Megoldás:** Nézze át a lefordított dokumentumot, és javítsa, ahol szükséges, hogy pontosabb és olvashatóbb legyen.

**Lépések:**
1. Nyissa meg a lefordított dokumentumot.
2. Alaposan olvassa át a tartalmat.
3. Végezze el a szükséges javításokat.
4. Mentse el a módosításokat.

## 4. Jogosultsági hiba, Redacted vagy 404

Ha a képek vagy szövegek nem a megfelelő nyelvre fordulnak, és -d debug módban 401-es hibát kap, az általában hitelesítési hiba—vagy a kulcs érvénytelen, lejárt, vagy nem a megfelelő régióhoz tartozik.

Futtassa a co-op translator-t a [-d debug kapcsolóval](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md), hogy pontosabb képet kapjon a hiba okáról.

- **Hibaüzenet**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Lehetséges okok**:
  - A feliratkozási kulcs hibás vagy hiányzik a kérésben.
  - Az AI Services Key vagy Subscription Key más Azure erőforráshoz tartozik (pl. Translator vagy OpenAI), nem pedig **Azure AI Vision** erőforráshoz.

 **Erőforrás típusa**
  - Lépjen be az [Azure Portalra](https://portal.azure.com) vagy az [Azure AI Foundry](https://ai.azure.com) oldalra, és ellenőrizze, hogy az erőforrás típusa `Azure AI services` → `Vision`.
  - Ellenőrizze a kulcsokat, és győződjön meg róla, hogy a megfelelő kulcsot használja.

## 5. Konfigurációs hibák (Új hibaüzenetek)

Az új szelektív fordítási rendszerrel a Co-op Translator már egyértelmű hibaüzeneteket ad, ha a szükséges szolgáltatások nincsenek beállítva.

### 5.1. Azure AI Service nincs beállítva képfordításhoz

**Probléma:** Képfordítást kér (az `-img` kapcsolóval), de az Azure AI Service nincs megfelelően konfigurálva.

**Hibaüzenet:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Megoldás:**
1. **1. lehetőség**: Azure AI Service konfigurálása
   - Adja hozzá az `AZURE_AI_SERVICE_API_KEY` értéket a `.env` fájlhoz
   - Adja hozzá az `AZURE_AI_SERVICE_ENDPOINT` értéket a `.env` fájlhoz
   - Ellenőrizze, hogy a szolgáltatás elérhető

2. **2. lehetőség**: Képfordítási kérés eltávolítása
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Hiányzó kötelező konfiguráció

**Probléma:** Hiányzik a szükséges LLM konfiguráció.

**Hibaüzenet:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Megoldás:**
1. Ellenőrizze, hogy a `.env` fájlban legalább az alábbi LLM konfigurációk egyike szerepel:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` és `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Vagy Azure OpenAI-t, vagy OpenAI-t kell konfigurálni, nem mindkettőt.

### 5.3. Szelektív fordítás zavara

**Probléma:** Nem fordult le egyetlen fájl sem, pedig a parancs sikeresen lefutott.

**Lehetséges okok:**
- Rossz fájltípus kapcsolók (`-md`, `-img`, `-nb`)
- Nincs megfelelő fájl a projektben
- Hibás könyvtárstruktúra

**Megoldás:**
1. **Használja a debug módot**, hogy lássa, mi történik:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Ellenőrizze a fájltípusokat** a projektben:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Vizsgálja meg a kapcsolók kombinációját**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Átállás a régi rendszerről

### 6.1. Csak Markdown mód megszűnt

**Probléma:** Azok a parancsok, amelyek automatikusan csak Markdown fordításra támaszkodtak, már nem működnek a megszokott módon.

**Régi működés:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Új működés:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Megoldás:**
- **Legyen egyértelmű**, mit szeretne lefordítani:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Váratlan hivatkozás viselkedés

**Probléma:** A lefordított fájlokban lévő hivatkozások váratlan helyekre mutatnak.

**Ok:** A dinamikus hivatkozáskezelés a kiválasztott fájltípusok alapján változik.

**Megoldás:**
1. **Ismerje meg az új hivatkozáskezelést**:
   - Ha `-nb` van: a notebook hivatkozások a lefordított verziókra mutatnak
   - Ha nincs `-nb`: a notebook hivatkozások az eredeti fájlokra mutatnak
   - Ha `-img` van: a képhivatkozások a lefordított képekre mutatnak
   - Ha nincs `-img`: a képhivatkozások az eredeti képekre mutatnak

2. **Válassza ki a megfelelő kombinációt** az Ön esetére:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. Lefutott a GitHub Action, de nem jött létre Pull Request (PR)

**Tünet:** A `peter-evans/create-pull-request` workflow naplóiban ez látható:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Lehetséges okok:**
- **Nincs változás:** A fordítási lépés nem hozott létre eltérést (a repo már naprakész).
- **Kimenetek figyelmen kívül hagyva:** A `.gitignore` kizárja azokat a fájlokat, amelyeket commitolni szeretne (pl. `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths eltérés:** Az action-nek megadott útvonalak nem egyeznek a tényleges kimenetekkel.
- **Workflow logika/feltételek:** A fordítási lépés korán kilépett, vagy váratlan könyvtárba írt.

**Hogyan ellenőrizze / javítsa:**
1. **Ellenőrizze a kimeneteket:** Fordítás után nézze meg, hogy a workspace-ben vannak-e új vagy módosított fájlok a `translations/` és/vagy `translated_images/` mappában.
   - Ha notebookokat fordít, ellenőrizze, hogy a `.ipynb` fájlok valóban a `translations/<lang>/...` alatt jöttek-e létre.
2. **Nézze át a `.gitignore`-t:** Ne hagyja figyelmen kívül a generált kimeneteket. Ne ignorálja:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (ha notebookokat fordít)
3. **Győződjön meg róla, hogy az add-paths egyezik a kimenetekkel:** Használjon többsoros értéket, és mindkét mappát vegye fel, ha szükséges:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Kényszerített PR hibakereséshez:** Ideiglenesen engedélyezze az üres commitokat, hogy ellenőrizze a beállításokat:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Futtassa debug módban:** Adja hozzá a `-d` kapcsolót a fordítási parancshoz, hogy lássa, milyen fájlokat talált és írt ki.
6. **Jogosultságok (GITHUB_TOKEN):** Ellenőrizze, hogy a workflow-nak van írási jogosultsága commitok és PR-ek létrehozásához:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Gyors hibakeresési ellenőrzőlista

Fordítási problémák esetén:

1. **Használja a debug módot:** Adja hozzá a `-d` kapcsolót a részletes naplózáshoz
2. **Ellenőrizze a kapcsolókat:** Győződjön meg róla, hogy a `-md`, `-img`, `-nb` megfelel a szándékának
3. **Ellenőrizze a konfigurációt:** Nézze meg, hogy a `.env` fájlban minden szükséges kulcs szerepel
4. **Teszteljen lépésenként:** Kezdje csak a `-md` kapcsolóval, majd adja hozzá a többit
5. **Ellenőrizze a fájlstruktúrát:** Győződjön meg róla, hogy a forrásfájlok léteznek és elérhetők

További részletes információért a parancsokról és kapcsolókról lásd a [Command Reference](./command-reference.md) oldalt.

---

**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.