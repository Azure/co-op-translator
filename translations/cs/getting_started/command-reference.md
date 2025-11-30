<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T12:10:40+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "cs"
}
-->
# Referenční příkazy

CLI nástroj **Co-op Translator** nabízí několik možností, jak přizpůsobit proces překladu:

Příkaz                                      | Popis
--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"               | Překládá váš projekt do zadaných jazyků. Příklad: translate -l "es fr de" přeloží do španělštiny, francouzštiny a němčiny. Použijte translate -l "all" pro překlad do všech podporovaných jazyků.
translate -l "language_codes" -u            | Aktualizuje překlady odstraněním stávajících a jejich novým vytvořením. Upozornění: Tímto se smažou všechny aktuální překlady pro zadané jazyky.
translate -l "language_codes" -img          | Překládá pouze obrazové soubory.
translate -l "language_codes" -md           | Překládá pouze Markdown soubory.
translate -l "language_codes" -nb           | Překládá pouze Jupyter notebooky (.ipynb).
translate -l "language_codes" --fix         | Překládá znovu soubory s nízkou důvěrou na základě předchozích výsledků hodnocení.
translate -l "language_codes" -d            | Zapne režim ladění pro podrobné logování.
translate -l "language_codes" --save-logs, -s | Uloží logy na úrovni DEBUG do souborů pod <root_dir>/logs/ (konzole zůstává řízena přepínačem -d)
translate -l "language_codes" -r "root_dir" | Určí kořenový adresář projektu
translate -l "language_codes" -f            | Použije rychlý režim pro překlad obrázků (až 3x rychlejší vykreslování za mírnou cenu kvality a zarovnání).
translate -l "language_codes" -y            | Automaticky potvrdí všechny výzvy (užitečné pro CI/CD pipeline)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Zapne nebo vypne přidání sekce s upozorněním o strojovém překladu do přeložených markdownů a notebooků (výchozí: zapnuto).
translate -l "language_codes" --help        | Zobrazí nápovědu s dostupnými příkazy v CLI
evaluate -l "language_code"                  | Vyhodnotí kvalitu překladu pro konkrétní jazyk a poskytne skóre důvěry
evaluate -l "language_code" -c 0.8           | Vyhodnotí překlady s vlastním prahem důvěry
evaluate -l "language_code" -f               | Rychlé hodnocení (pouze pravidla, bez LLM)
evaluate -l "language_code" -D               | Hloubkové hodnocení (pouze LLM, důkladnější, ale pomalejší)
evaluate -l "language_code" --save-logs, -s  | Uloží logy na úrovni DEBUG do souborů pod <root_dir>/logs/
migrate-links -l "language_codes"             | Zpracuje přeložené Markdown soubory a aktualizuje odkazy na notebooky (.ipynb). Preferuje přeložené notebooky, pokud jsou k dispozici; jinak může použít originální notebooky.
migrate-links -l "language_codes" -r          | Určí kořenový adresář projektu (výchozí: aktuální adresář).
migrate-links -l "language_codes" --dry-run   | Ukáže, které soubory by se změnily, aniž by provedl zápis.
migrate-links -l "language_codes" --no-fallback-to-original | Neaktualizuje odkazy na originální notebooky, pokud chybí přeložené verze (aktualizuje pouze, pokud přeložené existují).
migrate-links -l "language_codes" -d          | Zapne režim ladění pro podrobné logování.
migrate-links -l "language_codes" --save-logs, -s | Uloží logy na úrovni DEBUG do souborů pod <root_dir>/logs/
migrate-links -l "all" -y                      | Zpracuje všechny jazyky a automaticky potvrdí varovnou výzvu.

## Příklady použití

  1. Výchozí chování (přidá nové překlady bez mazání stávajících):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Přidá pouze nové korejské překlady obrázků (žádné stávající překlady nejsou smazány):    translate -l "ko" -img

  3. Aktualizuje všechny korejské překlady (Upozornění: Tím se smažou všechny stávající korejské překlady před novým překladem):    translate -l "ko" -u

  4. Aktualizuje pouze korejské obrázky (Upozornění: Tím se smažou všechny stávající korejské obrázky před novým překladem):    translate -l "ko" -img -u

  5. Přidá nové markdown překlady pro korejštinu, aniž by ovlivnil ostatní překlady:    translate -l "ko" -md

  6. Opraví překlady s nízkou důvěrou na základě předchozích výsledků hodnocení: translate -l "ko" --fix

  7. Opraví překlady s nízkou důvěrou pouze pro specifické soubory (markdown): translate -l "ko" --fix -md

  8. Opraví překlady s nízkou důvěrou pouze pro specifické soubory (obrázky): translate -l "ko" --fix -img

  9. Použije rychlý režim pro překlad obrázků:    translate -l "ko" -img -f

  10. Opraví překlady s nízkou důvěrou s vlastním prahem: translate -l "ko" --fix -c 0.8

  11. Příklad režimu ladění: - translate -l "ko" -d: Zapne ladicí logování.
  12. Uloží logy do souborů: translate -l "ko" -s
  13. DEBUG v konzoli i v souborech: translate -l "ko" -d -s
  14. Přeloží bez přidání upozornění o strojovém překladu do výstupů: translate -l "ko" --no-disclaimer

  15. Migruje odkazy na notebooky pro korejské překlady (aktualizuje odkazy na přeložené notebooky, pokud jsou k dispozici):    migrate-links -l "ko"

  15. Migruje odkazy s režimem dry-run (bez zápisu do souborů):    migrate-links -l "ko" --dry-run

  16. Aktualizuje odkazy pouze pokud existují přeložené notebooky (nepoužívá originály jako zálohu):    migrate-links -l "ko" --no-fallback-to-original

  17. Zpracuje všechny jazyky s potvrzovací výzvou:    migrate-links -l "all"

  18. Zpracuje všechny jazyky a automaticky potvrdí:    migrate-links -l "all" -y
  19. Uloží logy do souborů pro migrate-links:    migrate-links -l "ko ja" -s

### Příklady hodnocení

> [!WARNING]  
> **Beta funkce**: Funkce hodnocení je momentálně v beta verzi. Tato funkce byla vydána pro hodnocení přeložených dokumentů, metody hodnocení a podrobné implementace jsou stále ve vývoji a mohou se měnit.

  1. Hodnocení korejských překladů: evaluate -l "ko"

  2. Hodnocení s vlastním prahem důvěry: evaluate -l "ko" -c 0.8

  3. Rychlé hodnocení (pouze pravidla): evaluate -l "ko" -f

  4. Hloubkové hodnocení (pouze LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->