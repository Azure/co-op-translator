<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T03:51:39+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "cs"
}
-->
# Referenční příručka příkazů

CLI **Co-op Translator** nabízí několik možností, jak přizpůsobit proces překladu:

Příkaz                                       | Popis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "jazykové_kódy"                 | Přeloží váš projekt do zadaných jazyků. Příklad: translate -l "es fr de" přeloží do španělštiny, francouzštiny a němčiny. Použijte translate -l "all" pro překlad do všech podporovaných jazyků.
translate -l "jazykové_kódy" -u              | Aktualizuje překlady tím, že smaže stávající a vytvoří je znovu. Upozornění: Tímto smažete všechny aktuální překlady pro zadané jazyky.
translate -l "jazykové_kódy" -img            | Překládá pouze obrazové soubory.
translate -l "jazykové_kódy" -md             | Překládá pouze Markdown soubory.
translate -l "jazykové_kódy" -nb             | Překládá pouze Jupyter notebooky (.ipynb).
translate -l "jazykové_kódy" --fix           | Překládá znovu soubory s nízkým skóre jistoty na základě předchozích výsledků hodnocení.
translate -l "jazykové_kódy" -d              | Zapne režim ladění pro podrobné logování.
translate -l "jazykové_kódy" --save-logs, -s | Uloží DEBUG logy do souborů pod <root_dir>/logs/ (konzole zůstává řízena pomocí -d)
translate -l "jazykové_kódy" -r "root_dir"   | Určí kořenový adresář projektu
translate -l "jazykové_kódy" -f              | Použije rychlý režim pro překlad obrázků (až 3x rychlejší vykreslování s mírnou ztrátou kvality a zarovnání).
translate -l "jazykové_kódy" -y              | Automaticky potvrdí všechny výzvy (vhodné pro CI/CD)
translate -l "jazykové_kódy" --help          | Zobrazí nápovědu v CLI s dostupnými příkazy
evaluate -l "jazykový_kód"                  | Vyhodnotí kvalitu překladu pro konkrétní jazyk a zobrazí skóre jistoty
evaluate -l "jazykový_kód" -c 0.8           | Vyhodnotí překlady s vlastním prahem jistoty
evaluate -l "jazykový_kód" -f               | Rychlý režim hodnocení (pouze pravidla, bez LLM)
evaluate -l "jazykový_kód" -D               | Hloubkové hodnocení (pouze LLM, důkladnější, ale pomalejší)
evaluate -l "jazykový_kód" --save-logs, -s  | Uloží DEBUG logy do souborů pod <root_dir>/logs/
migrate-links -l "jazykové_kódy"             | Znovu zpracuje přeložené Markdown soubory a aktualizuje odkazy na notebooky (.ipynb). Preferuje přeložené notebooky, pokud jsou dostupné; jinak může použít původní notebooky.
migrate-links -l "jazykové_kódy" -r          | Určí kořenový adresář projektu (výchozí: aktuální adresář).
migrate-links -l "jazykové_kódy" --dry-run   | Ukáže, které soubory by se změnily, bez zápisu změn.
migrate-links -l "jazykové_kódy" --no-fallback-to-original | Nepřepisuje odkazy na původní notebooky, pokud chybí překlad (aktualizuje pouze, když existuje překlad).
migrate-links -l "jazykové_kódy" -d          | Zapne režim ladění pro podrobné logování.
migrate-links -l "jazykové_kódy" --save-logs, -s | Uloží DEBUG logy do souborů pod <root_dir>/logs/
migrate-links -l "all" -y                      | Zpracuje všechny jazyky a automaticky potvrdí varování.

## Příklady použití

  1. Výchozí chování (přidá nové překlady bez mazání stávajících):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Přidá pouze nové korejské překlady obrázků (stávající překlady se nemažou):    translate -l "ko" -img

  3. Aktualizuje všechny korejské překlady (Upozornění: Smaže všechny stávající korejské překlady před opětovným překladem):    translate -l "ko" -u

  4. Aktualizuje pouze korejské obrázky (Upozornění: Smaže všechny stávající korejské obrázky před opětovným překladem):    translate -l "ko" -img -u

  5. Přidá nové markdown překlady pro korejštinu bez ovlivnění ostatních překladů:    translate -l "ko" -md

  6. Opraví překlady s nízkou jistotou na základě předchozího hodnocení: translate -l "ko" --fix

  7. Opraví překlady s nízkou jistotou pouze pro konkrétní soubory (markdown): translate -l "ko" --fix -md

  8. Opraví překlady s nízkou jistotou pouze pro konkrétní soubory (obrázky): translate -l "ko" --fix -img

  9. Použije rychlý režim pro překlad obrázků:    translate -l "ko" -img -f

  10. Opraví překlady s nízkou jistotou s vlastním prahem: translate -l "ko" --fix -c 0.8

  11. Příklad režimu ladění: - translate -l "ko" -d: Zapne ladící logování.
  12. Uložení logů do souborů: translate -l "ko" -s
  13. DEBUG na konzoli i v souborech: translate -l "ko" -d -s

  14. Migrace odkazů na notebooky pro korejské překlady (aktualizuje odkazy na přeložené notebooky, pokud jsou dostupné):    migrate-links -l "ko"

  15. Migrace odkazů s dry-run (bez zápisu do souborů):    migrate-links -l "ko" --dry-run

  16. Aktualizuje odkazy pouze pokud existují přeložené notebooky (nepoužívá původní):    migrate-links -l "ko" --no-fallback-to-original

  17. Zpracuje všechny jazyky s potvrzovací výzvou:    migrate-links -l "all"

  18. Zpracuje všechny jazyky a automaticky potvrdí:    migrate-links -l "all" -y
  19. Uložení logů do souborů pro migrate-links:    migrate-links -l "ko ja" -s

### Příklady hodnocení

> [!WARNING]  
> **Beta funkce**: Funkcionalita hodnocení je aktuálně v beta verzi. Tato funkce byla vydána pro hodnocení přeložených dokumentů, přičemž metody hodnocení a detailní implementace se stále vyvíjejí a mohou se měnit.

  1. Hodnocení korejských překladů: evaluate -l "ko"

  2. Hodnocení s vlastním prahem jistoty: evaluate -l "ko" -c 0.8

  3. Rychlé hodnocení (pouze pravidla): evaluate -l "ko" -f

  4. Hloubkové hodnocení (pouze LLM): evaluate -l "ko" -D

---

**Prohlášení**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neneseme odpovědnost za jakékoli nedorozumění nebo nesprávné výklady vzniklé v důsledku použití tohoto překladu.