<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:54:39+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sk"
}
-->
# Referencia príkazov

**Co-op Translator** CLI ponúka viacero možností, ako prispôsobiť proces prekladu:

Príkaz                                       | Popis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Preloží váš projekt do zadaných jazykov. Príklad: translate -l "es fr de" preloží do španielčiny, francúzštiny a nemčiny. Použite translate -l "all" na preklad do všetkých podporovaných jazykov.
translate -l "language_codes" -u              | Aktualizuje preklady vymazaním existujúcich a ich opätovným vytvorením. Upozornenie: Týmto sa vymažú všetky aktuálne preklady pre zadané jazyky.
translate -l "language_codes" -img            | Prekladá iba obrazové súbory.
translate -l "language_codes" -md             | Prekladá iba Markdown súbory.
translate -l "language_codes" -nb             | Prekladá iba Jupyter notebooky (.ipynb).
translate -l "language_codes" --fix           | Opätovne prekladá súbory s nízkym skóre dôvery na základe predchádzajúcich výsledkov hodnotenia.
translate -l "language_codes" -d              | Zapne režim ladenia pre podrobné logovanie.
translate -l "language_codes" --save-logs, -s | Uloží DEBUG logy do súborov v <root_dir>/logs/ (konzola zostáva ovládaná cez -d)
translate -l "language_codes" -r "root_dir"   | Určí koreňový adresár projektu
translate -l "language_codes" -f              | Použije rýchly režim pre preklad obrázkov (až 3x rýchlejšie vykresľovanie s miernym kompromisom v kvalite a zarovnaní).
translate -l "language_codes" -y              | Automaticky potvrdí všetky výzvy (užitočné pre CI/CD pipeline)
translate -l "language_codes" --help          | Zobrazí pomoc priamo v CLI s dostupnými príkazmi
evaluate -l "language_code"                  | Vyhodnotí kvalitu prekladu pre konkrétny jazyk a poskytne skóre dôvery
evaluate -l "language_code" -c 0.8           | Vyhodnotí preklady s vlastným prahom dôvery
evaluate -l "language_code" -f               | Rýchly režim hodnotenia (iba pravidlá, bez LLM)
evaluate -l "language_code" -D               | Hĺbkové hodnotenie (iba LLM, dôkladnejšie, ale pomalšie)
evaluate -l "language_code" --save-logs, -s  | Uloží DEBUG logy do súborov v <root_dir>/logs/
migrate-links -l "language_codes"             | Prepracuje preložené Markdown súbory a aktualizuje odkazy na notebooky (.ipynb). Uprednostňuje preložené notebooky, ak sú dostupné; inak môže použiť pôvodné notebooky.
migrate-links -l "language_codes" -r          | Určí koreňový adresár projektu (predvolené: aktuálny adresár).
migrate-links -l "language_codes" --dry-run   | Zobrazí, ktoré súbory by sa zmenili, bez zapisovania zmien.
migrate-links -l "language_codes" --no-fallback-to-original | Neukladať odkazy na pôvodné notebooky, ak chýbajú preložené (aktualizuje len ak existuje preklad).
migrate-links -l "language_codes" -d          | Zapne režim ladenia pre podrobné logovanie.
migrate-links -l "language_codes" --save-logs, -s | Uloží DEBUG logy do súborov v <root_dir>/logs/
migrate-links -l "all" -y                      | Spracuje všetky jazyky a automaticky potvrdí varovnú výzvu.

## Príklady použitia

  1. Predvolené správanie (pridá nové preklady bez vymazania existujúcich):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Pridá iba nové kórejské preklady obrázkov (existujúce preklady sa nemažú):    translate -l "ko" -img

  3. Aktualizuje všetky kórejské preklady (Upozornenie: Vymaže všetky existujúce kórejské preklady pred opätovným prekladom):    translate -l "ko" -u

  4. Aktualizuje iba kórejské obrázky (Upozornenie: Vymaže všetky existujúce kórejské obrázky pred opätovným prekladom):    translate -l "ko" -img -u

  5. Pridá nové markdown preklady pre kórejčinu bez ovplyvnenia ostatných prekladov:    translate -l "ko" -md

  6. Opraví preklady s nízkou dôverou na základe predchádzajúcich hodnotení: translate -l "ko" --fix

  7. Opraví preklady s nízkou dôverou len pre konkrétne súbory (markdown): translate -l "ko" --fix -md

  8. Opraví preklady s nízkou dôverou len pre konkrétne súbory (obrázky): translate -l "ko" --fix -img

  9. Použije rýchly režim pre preklad obrázkov:    translate -l "ko" -img -f

  10. Opraví preklady s nízkou dôverou s vlastným prahom: translate -l "ko" --fix -c 0.8

  11. Príklad režimu ladenia: - translate -l "ko" -d: Zapne podrobné logovanie.
  12. Uloženie logov do súborov: translate -l "ko" -s
  13. Konzola DEBUG a súbor DEBUG: translate -l "ko" -d -s

  14. Migrácia odkazov na notebooky pre kórejské preklady (aktualizuje odkazy na preložené notebooky, ak sú dostupné):    migrate-links -l "ko"

  15. Migrácia odkazov s dry-run (bez zápisu do súborov):    migrate-links -l "ko" --dry-run

  16. Aktualizuje odkazy len ak existujú preložené notebooky (nepoužíva pôvodné):    migrate-links -l "ko" --no-fallback-to-original

  17. Spracuje všetky jazyky s potvrdením:    migrate-links -l "all"

  18. Spracuje všetky jazyky a automaticky potvrdí:    migrate-links -l "all" -y
  19. Uloží logy do súborov pre migrate-links:    migrate-links -l "ko ja" -s

### Príklady hodnotenia

> [!WARNING]  
> **Beta funkcia**: Funkcionalita hodnotenia je momentálne v beta verzii. Táto funkcia bola vydaná na hodnotenie preložených dokumentov, pričom metódy hodnotenia a detailná implementácia sa stále vyvíjajú a môžu sa meniť.

  1. Hodnotenie kórejských prekladov: evaluate -l "ko"

  2. Hodnotenie s vlastným prahom dôvery: evaluate -l "ko" -c 0.8

  3. Rýchle hodnotenie (iba pravidlá): evaluate -l "ko" -f

  4. Hĺbkové hodnotenie (iba LLM): evaluate -l "ko" -D

---

**Vyhlásenie o vylúčení zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj by sa mal považovať pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.