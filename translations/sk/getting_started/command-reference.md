<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T12:15:02+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sk"
}
-->
# Referencia príkazov

CLI nástroj **Co-op Translator** ponúka niekoľko možností na prispôsobenie prekladu:

Príkaz                                       | Popis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Preloží váš projekt do zadaných jazykov. Príklad: translate -l "es fr de" preloží do španielčiny, francúzštiny a nemčiny. Použite translate -l "all" pre preklad do všetkých podporovaných jazykov.
translate -l "language_codes" -u              | Aktualizuje preklady vymazaním existujúcich a ich opätovným vytvorením. Upozornenie: Týmto sa vymažú všetky aktuálne preklady pre zadané jazyky.
translate -l "language_codes" -img            | Preloží iba obrázkové súbory.
translate -l "language_codes" -md             | Preloží iba Markdown súbory.
translate -l "language_codes" -nb             | Preloží iba Jupyter notebook súbory (.ipynb).
translate -l "language_codes" --fix           | Preloží znova súbory s nízkou dôverou na základe predchádzajúcich hodnotení.
translate -l "language_codes" -d              | Zapne režim ladenia pre podrobné logovanie.
translate -l "language_codes" --save-logs, -s | Uloží DEBUG logy do súborov v <root_dir>/logs/ (konzola zostáva riadená parametrom -d)
translate -l "language_codes" -r "root_dir"   | Určí koreňový adresár projektu
translate -l "language_codes" -f              | Použije rýchly režim pre preklad obrázkov (až 3x rýchlejšie vykresľovanie za mierny kompromis v kvalite a zarovnaní).
translate -l "language_codes" -y              | Automaticky potvrdí všetky výzvy (užitočné pre CI/CD pipeline)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Povoliť alebo zakázať pridanie sekcie s upozornením o strojovom preklade do preložených markdownov a notebookov (predvolené: povolené).
translate -l "language_codes" --help          | Zobrazí pomoc s dostupnými príkazmi v CLI
evaluate -l "language_code"                  | Vyhodnotí kvalitu prekladu pre konkrétny jazyk a poskytne skóre dôvery
evaluate -l "language_code" -c 0.8           | Vyhodnotí preklady s vlastným prahom dôvery
evaluate -l "language_code" -f               | Rýchly režim hodnotenia (len pravidlá, bez LLM)
evaluate -l "language_code" -D               | Hlboké hodnotenie (len LLM, dôkladnejšie, ale pomalšie)
evaluate -l "language_code" --save-logs, -s  | Uloží DEBUG logy do súborov v <root_dir>/logs/
migrate-links -l "language_codes"             | Prepracuje preložené Markdown súbory a aktualizuje odkazy na notebooky (.ipynb). Preferuje preložené notebooky, ak sú dostupné; inak môže použiť originálne notebooky.
migrate-links -l "language_codes" -r          | Určí koreňový adresár projektu (predvolené: aktuálny adresár).
migrate-links -l "language_codes" --dry-run   | Ukáže, ktoré súbory by sa zmenili, bez zápisu zmien.
migrate-links -l "language_codes" --no-fallback-to-original | Neaktualizuje odkazy na originálne notebooky, ak chýbajú preložené verzie (aktualizuje len ak existuje preklad).
migrate-links -l "language_codes" -d          | Zapne režim ladenia pre podrobné logovanie.
migrate-links -l "language_codes" --save-logs, -s | Uloží DEBUG logy do súborov v <root_dir>/logs/
migrate-links -l "all" -y                      | Spracuje všetky jazyky a automaticky potvrdí výzvu na potvrdenie.

## Príklady použitia

  1. Predvolené správanie (pridá nové preklady bez mazania existujúcich):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Pridá iba nové kórejské preklady obrázkov (existujúce preklady sa nevymažú):    translate -l "ko" -img

  3. Aktualizuje všetky kórejské preklady (Upozornenie: Vymaže všetky existujúce kórejské preklady pred opätovným prekladom):    translate -l "ko" -u

  4. Aktualizuje iba kórejské obrázky (Upozornenie: Vymaže všetky existujúce kórejské obrázky pred opätovným prekladom):    translate -l "ko" -img -u

  5. Pridá nové markdown preklady pre kórejčinu bez ovplyvnenia ostatných prekladov:    translate -l "ko" -md

  6. Opraví preklady s nízkou dôverou na základe predchádzajúcich hodnotení: translate -l "ko" --fix

  7. Opraví preklady s nízkou dôverou len pre konkrétne súbory (markdown): translate -l "ko" --fix -md

  8. Opraví preklady s nízkou dôverou len pre konkrétne súbory (obrázky): translate -l "ko" --fix -img

  9. Použije rýchly režim pre preklad obrázkov:    translate -l "ko" -img -f

  10. Opraví preklady s nízkou dôverou s vlastným prahom: translate -l "ko" --fix -c 0.8

  11. Príklad režimu ladenia: - translate -l "ko" -d: Zapne debug logovanie.
  12. Uloží logy do súborov: translate -l "ko" -s
  13. DEBUG v konzole aj v súboroch: translate -l "ko" -d -s
  14. Preloží bez pridania upozornení o strojovom preklade: translate -l "ko" --no-disclaimer

  15. Migruje odkazy na notebooky pre kórejské preklady (aktualizuje odkazy na preložené notebooky, ak sú dostupné):    migrate-links -l "ko"

  15. Migruje odkazy s režimom suchého behu (bez zápisu zmien):    migrate-links -l "ko" --dry-run

  16. Aktualizuje odkazy len ak existujú preložené notebooky (nepoužíva originály):    migrate-links -l "ko" --no-fallback-to-original

  17. Spracuje všetky jazyky s výzvou na potvrdenie:    migrate-links -l "all"

  18. Spracuje všetky jazyky a automaticky potvrdí:    migrate-links -l "all" -y
  19. Uloží logy do súborov pre migrate-links:    migrate-links -l "ko ja" -s

### Príklady hodnotenia

> [!WARNING]  
> **Beta funkcia**: Funkcia hodnotenia je momentálne v beta verzii. Táto funkcia bola sprístupnená na hodnotenie preložených dokumentov, pričom metódy hodnotenia a detailná implementácia sú stále vo vývoji a môžu sa meniť.

  1. Vyhodnotí kórejské preklady: evaluate -l "ko"

  2. Vyhodnotí s vlastným prahom dôvery: evaluate -l "ko" -c 0.8

  3. Rýchle hodnotenie (len pravidlá): evaluate -l "ko" -f

  4. Hlboké hodnotenie (len LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->