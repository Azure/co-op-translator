<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T12:06:31+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "hu"
}
-->
# Parancs referencia

A **Co-op Translator** CLI több lehetőséget kínál a fordítási folyamat testreszabására:

Parancs                                      | Leírás
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | A projektet a megadott nyelvekre fordítja. Példa: translate -l "es fr de" spanyolra, franciára és németre fordít. Használd a translate -l "all" parancsot az összes támogatott nyelvre történő fordításhoz.
translate -l "language_codes" -u             | Frissíti a fordításokat azzal, hogy törli a meglévőket és újra létrehozza őket. Figyelem: Ez törli az adott nyelvek összes jelenlegi fordítását.
translate -l "language_codes" -img           | Csak a képfájlokat fordítja.
translate -l "language_codes" -md            | Csak a Markdown fájlokat fordítja.
translate -l "language_codes" -nb            | Csak a Jupyter notebook fájlokat (.ipynb) fordítja.
translate -l "language_codes" --fix          | Újrafordítja az alacsony bizalmi szintű fájlokat a korábbi értékelési eredmények alapján.
translate -l "language_codes" -d             | Hibakeresési módot engedélyez részletes naplózáshoz.
translate -l "language_codes" --save-logs, -s| DEBUG szintű naplókat ment fájlokba a <root_dir>/logs/ könyvtárba (a konzol továbbra is a -d kapcsoló vezérlése alatt marad)
translate -l "language_codes" -r "root_dir"  | Megadja a projekt gyökérkönyvtárát
translate -l "language_codes" -f             | Gyors módot használ a képfájlok fordításához (akár 3x gyorsabb ábrázolás, enyhe minőség- és illesztésveszteség árán).
translate -l "language_codes" -y             | Automatikusan megerősít minden kérdést (hasznos CI/CD folyamatokhoz)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Engedélyezi vagy letiltja a gépi fordításra vonatkozó figyelmeztető szakasz hozzáadását a lefordított markdown és notebook fájlokhoz (alapértelmezett: engedélyezett).
translate -l "language_codes" --help         | Segítség a CLI-n belül, elérhető parancsok megjelenítése
evaluate -l "language_code"                   | Egy adott nyelv fordítási minőségének értékelése és bizalmi pontszámok megadása
evaluate -l "language_code" -c 0.8            | Egyéni bizalmi küszöbértékkel értékeli a fordításokat
evaluate -l "language_code" -f                | Gyors értékelési mód (csak szabályalapú, nem LLM)
evaluate -l "language_code" -D                | Mély értékelési mód (csak LLM alapú, alaposabb, de lassabb)
evaluate -l "language_code" --save-logs, -s   | DEBUG szintű naplókat ment fájlokba a <root_dir>/logs/ könyvtárba
migrate-links -l "language_codes"              | Újrafeldolgozza a lefordított Markdown fájlokat, hogy frissítse a notebookokra (.ipynb) mutató hivatkozásokat. Előnyben részesíti a lefordított notebookokat, ha elérhetők; egyébként visszatérhet az eredeti notebookokra.
migrate-links -l "language_codes" -r           | Megadja a projekt gyökérkönyvtárát (alapértelmezett: aktuális könyvtár).
migrate-links -l "language_codes" --dry-run    | Megmutatja, mely fájlok változnának, de nem írja át őket.
migrate-links -l "language_codes" --no-fallback-to-original | Nem írja át a hivatkozásokat az eredeti notebookokra, ha a lefordított megfelelőik hiányoznak (csak akkor frissít, ha lefordított létezik).
migrate-links -l "language_codes" -d           | Hibakeresési mód engedélyezése részletes naplózáshoz.
migrate-links -l "language_codes" --save-logs, -s | DEBUG szintű naplókat ment fájlokba a <root_dir>/logs/ könyvtárba
migrate-links -l "all" -y                       | Minden nyelv feldolgozása és a figyelmeztető kérdés automatikus megerősítése.

## Használati példák

  1. Alapértelmezett viselkedés (új fordítások hozzáadása a meglévők törlése nélkül):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Csak új koreai képfordítások hozzáadása (a meglévő fordítások nem törlődnek):    translate -l "ko" -img

  3. Minden koreai fordítás frissítése (Figyelem: Ez törli az összes meglévő koreai fordítást az újrafordítás előtt):    translate -l "ko" -u

  4. Csak a koreai képek frissítése (Figyelem: Ez törli az összes meglévő koreai képet az újrafordítás előtt):    translate -l "ko" -img -u

  5. Új markdown fordítások hozzáadása koreai nyelven anélkül, hogy más fordításokat érintene:    translate -l "ko" -md

  6. Alacsony bizalmi szintű fordítások javítása korábbi értékelési eredmények alapján: translate -l "ko" --fix

  7. Alacsony bizalmi szintű fordítások javítása csak bizonyos fájloknál (markdown): translate -l "ko" --fix -md

  8. Alacsony bizalmi szintű fordítások javítása csak bizonyos fájloknál (képek): translate -l "ko" --fix -img

  9. Gyors mód használata képfordításhoz:    translate -l "ko" -img -f

  10. Alacsony bizalmi szintű fordítások javítása egyéni küszöbértékkel: translate -l "ko" --fix -c 0.8

  11. Hibakeresési mód példa: - translate -l "ko" -d: Hibakeresési naplózás engedélyezése.
  12. Naplók mentése fájlokba: translate -l "ko" -s
  13. Konzol DEBUG és fájl DEBUG: translate -l "ko" -d -s
  14. Fordítás gépi fordítási figyelmeztetés nélkül: translate -l "ko" --no-disclaimer

  15. Notebook hivatkozások migrálása koreai fordításokhoz (frissíti a hivatkozásokat a lefordított notebookokra, ha elérhetők):    migrate-links -l "ko"

  15. Migrálás dry-run módban (nem ír fájlokat):    migrate-links -l "ko" --dry-run

  16. Csak akkor frissíti a hivatkozásokat, ha lefordított notebookok léteznek (nem tér vissza az eredetiekhez):    migrate-links -l "ko" --no-fallback-to-original

  17. Minden nyelv feldolgozása megerősítő kérdéssel:    migrate-links -l "all"

  18. Minden nyelv feldolgozása automatikus megerősítéssel:    migrate-links -l "all" -y
  19. Naplók mentése migrate-links esetén:    migrate-links -l "ko ja" -s

### Értékelési példák

> [!WARNING]  
> **Béta funkció**: Az értékelési funkció jelenleg béta állapotban van. Ez a funkció a lefordított dokumentumok értékelésére szolgál, az értékelési módszerek és a részletes megvalósítás még fejlesztés alatt állnak, és változhatnak.

  1. Koreai fordítások értékelése: evaluate -l "ko"

  2. Egyéni bizalmi küszöbértékkel történő értékelés: evaluate -l "ko" -c 0.8

  3. Gyors értékelés (csak szabályalapú): evaluate -l "ko" -f

  4. Mély értékelés (csak LLM alapú): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->