<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:48:25+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "hu"
}
-->
# Parancs referencia

A **Co-op Translator** CLI számos lehetőséget kínál a fordítási folyamat testreszabására:

Parancs                                       | Leírás
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "nyelvkódok"                     | Lefordítja a projektet a megadott nyelvekre. Példa: translate -l "es fr de" lefordítja spanyolra, franciára és németre. A translate -l "all" paranccsal minden támogatott nyelvre fordíthat.
translate -l "nyelvkódok" -u                  | Frissíti a fordításokat: törli a meglévőket, majd újra létrehozza őket. Figyelem: Ez törli az összes jelenlegi fordítást a megadott nyelveken.
translate -l "nyelvkódok" -img                | Csak képfájlokat fordít.
translate -l "nyelvkódok" -md                 | Csak Markdown fájlokat fordít.
translate -l "nyelvkódok" -nb                 | Csak Jupyter notebook fájlokat (.ipynb) fordít.
translate -l "nyelvkódok" --fix               | Újrafordítja azokat a fájlokat, amelyeknél az előző értékelés alapján alacsony a bizalmi szint.
translate -l "nyelvkódok" -d                  | Részletes naplózáshoz bekapcsolja a hibakeresési módot.
translate -l "nyelvkódok" --save-logs, -s     | DEBUG szintű naplókat ment fájlokba a <root_dir>/logs/ mappába (a konzol naplózása továbbra is a -d paraméterrel szabályozható)
translate -l "nyelvkódok" -r "root_dir"       | Megadja a projekt gyökérkönyvtárát
translate -l "nyelvkódok" -f                  | Gyors módot használ képek fordításához (akár 3x gyorsabb ábrázolás, kis minőség- és igazításveszteséggel).
translate -l "nyelvkódok" -y                  | Automatikusan megerősíti az összes kérdést (hasznos CI/CD folyamatoknál)
translate -l "nyelvkódok" --help              | Súgó részletek a CLI-ben, elérhető parancsokkal
evaluate -l "nyelvkód"                        | Értékeli a fordítás minőségét egy adott nyelven, és bizalmi pontszámokat ad
evaluate -l "nyelvkód" -c 0.8                 | Fordítások értékelése egyedi bizalmi küszöbbel
evaluate -l "nyelvkód" -f                     | Gyors értékelési mód (csak szabályalapú, LLM nélkül)
evaluate -l "nyelvkód" -D                     | Mély értékelési mód (csak LLM-alapú, alaposabb, de lassabb)
evaluate -l "nyelvkód" --save-logs, -s        | DEBUG szintű naplókat ment fájlokba a <root_dir>/logs/ mappába
migrate-links -l "nyelvkódok"                 | Lefordított Markdown fájlok újrafeldolgozása, hogy frissítse a notebookokra (.ipynb) mutató hivatkozásokat. Előnyben részesíti a lefordított notebookokat, ha elérhetők; egyébként visszaállhat az eredetire.
migrate-links -l "nyelvkódok" -r              | Megadja a projekt gyökérkönyvtárát (alapértelmezett: aktuális könyvtár).
migrate-links -l "nyelvkódok" --dry-run       | Megmutatja, mely fájlok változnának, de nem írja felül őket.
migrate-links -l "nyelvkódok" --no-fallback-to-original | Nem írja át a hivatkozásokat az eredeti notebookokra, ha a lefordított verzió hiányzik (csak akkor frissít, ha van fordított).
migrate-links -l "nyelvkódok" -d              | Részletes naplózáshoz bekapcsolja a hibakeresési módot.
migrate-links -l "nyelvkódok" --save-logs, -s | DEBUG szintű naplókat ment fájlokba a <root_dir>/logs/ mappába
migrate-links -l "all" -y                      | Minden nyelvet feldolgoz, és automatikusan megerősíti a figyelmeztető kérdést.

## Használati példák

  1. Alapértelmezett működés (új fordítások hozzáadása a meglévők törlése nélkül):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Csak új koreai képfordítások hozzáadása (a meglévő fordítások nem törlődnek):    translate -l "ko" -img

  3. Minden koreai fordítás frissítése (Figyelem: Ez törli az összes koreai fordítást, mielőtt újrafordítaná):    translate -l "ko" -u

  4. Csak koreai képek frissítése (Figyelem: Ez törli az összes koreai képet, mielőtt újrafordítaná):    translate -l "ko" -img -u

  5. Új markdown fordítások hozzáadása koreai nyelven, a többi fordítás érintése nélkül:    translate -l "ko" -md

  6. Alacsony bizalmi szintű fordítások javítása az előző értékelés alapján: translate -l "ko" --fix

  7. Csak bizonyos fájlok (markdown) alacsony bizalmi szintű fordításainak javítása: translate -l "ko" --fix -md

  8. Csak bizonyos fájlok (képek) alacsony bizalmi szintű fordításainak javítása: translate -l "ko" --fix -img

  9. Gyors mód használata képfordításhoz:    translate -l "ko" -img -f

  10. Alacsony bizalmi szintű fordítások javítása egyedi küszöbbel: translate -l "ko" --fix -c 0.8

  11. Hibakeresési mód példa: - translate -l "ko" -d: Hibakeresési naplózás bekapcsolása.
  12. Naplók mentése fájlba: translate -l "ko" -s
  13. Konzol DEBUG és fájl DEBUG: translate -l "ko" -d -s

  14. Notebook hivatkozások migrálása koreai fordításokhoz (hivatkozások frissítése lefordított notebookokra, ha elérhetők):    migrate-links -l "ko"

  15. Hivatkozások migrálása próbaüzemben (nincs fájlírás):    migrate-links -l "ko" --dry-run

  16. Csak akkor frissít hivatkozásokat, ha létezik lefordított notebook (nem áll vissza az eredetire):    migrate-links -l "ko" --no-fallback-to-original

  17. Minden nyelv feldolgozása megerősítő kérdéssel:    migrate-links -l "all"

  18. Minden nyelv feldolgozása automatikus megerősítéssel:    migrate-links -l "all" -y
  19. Naplók mentése fájlba migrate-links esetén:    migrate-links -l "ko ja" -s

### Értékelési példák

> [!WARNING]  
> **Béta funkció**: Az értékelési funkció jelenleg béta verzióban érhető el. Ez a funkció a lefordított dokumentumok értékelésére szolgál, de az értékelési módszerek és a részletes megvalósítás még fejlesztés alatt állnak, és változhatnak.

  1. Koreai fordítások értékelése: evaluate -l "ko"

  2. Értékelés egyedi bizalmi küszöbbel: evaluate -l "ko" -c 0.8

  3. Gyors értékelés (csak szabályalapú): evaluate -l "ko" -f

  4. Mély értékelés (csak LLM-alapú): evaluate -l "ko" -D

---

**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.