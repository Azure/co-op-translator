<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:32:58+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sk"
}
-->
# Referencia príkazov
CLI **Co-op Translator** ponúka niekoľko možností na prispôsobenie procesu prekladu:

Príkaz                                       | Popis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Preloží váš projekt do zadaných jazykov. Príklad: translate -l "es fr de" preloží do španielčiny, francúzštiny a nemčiny. Použite translate -l "all" pre preklad do všetkých podporovaných jazykov.
translate -l "language_codes" -u              | Aktualizuje preklady vymazaním existujúcich a ich opätovným vytvorením. Warning: Týmto sa vymažú všetky aktuálne preklady pre zadané jazyky.
translate -l "language_codes" -img            | Prekladá iba obrazové súbory.
translate -l "language_codes" -md             | Prekladá iba Markdown súbory.
translate -l "language_codes" -chk            | Kontroluje preložené súbory na chyby a v prípade potreby opakuje preklad.
translate -l "language_codes" -d              | Aktivuje režim ladenia pre podrobné zaznamenávanie.
translate -l "language_codes" -r "root_dir"   | Špecifikuje koreňový adresár projektu.
translate -l "language_codes" -f              | Používa rýchly režim pre preklad obrázkov (až 3x rýchlejšie vykresľovanie za mierny kompromis v kvalite a zarovnaní).
translate -l "language_codes" -y              | Automaticky potvrdzuje všetky výzvy (užitočné pre CI/CD pipeline).
translate -l "language_codes" --help          | Zobrazenie nápovedy v CLI s dostupnými príkazmi.

### Príklady použitia:

  1. Predvolené správanie (pridá nové preklady bez mazania existujúcich):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Pridanie iba nových kórejských prekladov obrázkov (existujúce preklady sa nevymažú):    translate -l "ko" -img

  3. Aktualizácia všetkých kórejských prekladov (Warning: Vymaže všetky existujúce kórejské preklady pred opätovným prekladom):    translate -l "ko" -u

  4. Aktualizácia iba kórejských obrázkov (Warning: Vymaže všetky existujúce kórejské obrázky pred opätovným prekladom):    translate -l "ko" -img -u

  5. Pridanie nových markdown prekladov pre kórejčinu bez ovplyvnenia ostatných prekladov:    translate -l "ko" -md

  6. Kontrola preložených súborov na chyby a opakovanie prekladu, ak je to potrebné: translate -l "ko" -chk

  7. Kontrola preložených súborov na chyby a opakovanie prekladu (len markdown): translate -l "ko" -chk -md

  8. Kontrola preložených súborov na chyby a opakovanie prekladu (len obrázky): translate -l "ko" -chk -img

  9. Použitie rýchleho režimu pre preklad obrázkov:    translate -l "ko" -img -f

  10. Príklad režimu ladenia: - translate -l "ko" -d: Aktivuje podrobné zaznamenávanie.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím berte na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.