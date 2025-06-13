<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:32:24+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "hu"
}
-->
# Parancs referencia
A **Co-op Translator** CLI több lehetőséget kínál a fordítási folyamat testreszabására:

Parancs                                      | Leírás
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | A projektet a megadott nyelvekre fordítja. Példa: translate -l "es fr de" spanyolra, franciára és németre fordít. Használd a translate -l "all" parancsot az összes támogatott nyelvre történő fordításhoz.
translate -l "language_codes" -u             | Frissíti a fordításokat azzal, hogy törli a meglévőket, majd újra létrehozza őket. Figyelem: Ez törli az összes jelenlegi fordítást a megadott nyelveken.
translate -l "language_codes" -img           | Csak a képfájlokat fordítja.
translate -l "language_codes" -md            | Csak a Markdown fájlokat fordítja.
translate -l "language_codes" -chk           | Ellenőrzi a lefordított fájlokat hibák szempontjából, és szükség esetén újrapróbálja a fordítást.
translate -l "language_codes" -d             | Debug módot kapcsol be a részletes naplózáshoz.
translate -l "language_codes" -r "root_dir"  | Megadja a projekt gyökérkönyvtárát.
translate -l "language_codes" -f             | Gyors módot használ a képfájlok fordításához (akár 3-szor gyorsabb megjelenítés, enyhe minőség- és illeszkedésbeli kompromisszumokkal).
translate -l "language_codes" -y             | Automatikusan megerősít minden kérdést (hasznos CI/CD folyamatokhoz).
translate -l "language_codes" --help         | Súgó részletek a CLI-n belül, elérhető parancsokkal.

### Használati példák:

  1. Alapértelmezett viselkedés (új fordítások hozzáadása meglévők törlése nélkül):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Csak új koreai képfájl fordítások hozzáadása (a meglévő fordítások nem törlődnek):    translate -l "ko" -img

  3. Minden koreai fordítás frissítése (Figyelem: Ez törli az összes meglévő koreai fordítást az újrafordítás előtt):    translate -l "ko" -u

  4. Csak koreai képek frissítése (Figyelem: Ez törli az összes meglévő koreai képet az újrafordítás előtt):    translate -l "ko" -img -u

  5. Új markdown fordítások hozzáadása koreai nyelven anélkül, hogy a többi fordítást érintené:    translate -l "ko" -md

  6. A lefordított fájlok hibáinak ellenőrzése és szükség szerinti újrapróbálkozás: translate -l "ko" -chk

  7. A lefordított fájlok hibáinak ellenőrzése és újrapróbálkozás (csak markdown fájlok): translate -l "ko" -chk -md

  8. A lefordított fájlok hibáinak ellenőrzése és újrapróbálkozás (csak képek): translate -l "ko" -chk -img

  9. Gyors mód használata képfájl fordításhoz:    translate -l "ko" -img -f

  10. Debug mód példa: - translate -l "ko" -d: Debug naplózás engedélyezése.

**Nyilatkozat**:  
Ez a dokumentum az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk pontos fordítást nyújtani, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy félreértelmezésekért.