<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:49:29+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "cs"
}
-->
# Aktualizace sekce "Jiné kurzy" (Microsoft Beginners repozitáře)

Tento návod vysvětluje, jak automaticky synchronizovat sekci "Jiné kurzy" pomocí Co-op Translatoru a jak aktualizovat globální šablonu pro všechny repozitáře.

- Platí pro: pouze Microsoft Beginners repozitáře
- Funguje s: Co-op Translator CLI a GitHub Actions
- Zdroj šablony: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Rychlý start: Povolení automatické synchronizace ve vašem repozitáři

Přidejte následující značky kolem sekce "Jiné kurzy" ve vašem README. Co-op Translator při každém spuštění nahradí vše mezi těmito značkami.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Pokaždé, když se Co-op Translator spustí – přes CLI (např. `translate -l "<language codes>"`) nebo GitHub Actions – automaticky aktualizuje sekci "Jiné kurzy" uzavřenou mezi těmito značkami.

> [!NOTE]
> Pokud už máte existující seznam, stačí ho obalit stejnými značkami. Při dalším spuštění bude nahrazen nejnovějším standardizovaným obsahem.

---

## Jak změnit globální obsah

Pokud chcete aktualizovat standardizovaný obsah, který se zobrazuje ve všech Beginners repozitářích:

1. Upravte šablonu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Otevřete pull request do repozitáře Co-op Translator s vašimi změnami
3. Po sloučení PR bude verze Co-op Translatoru aktualizována
4. Při dalším spuštění Co-op Translatoru (CLI nebo GitHub Action) v cílovém repozitáři se automaticky synchronizuje aktualizovaná sekce

Tím je zajištěn jediný zdroj pravdy pro obsah sekce "Jiné kurzy" ve všech Beginners repozitářích.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->