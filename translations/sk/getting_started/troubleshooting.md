<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:30:26+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "sk"
}
-->
# Sprievodca riešením problémov s Microsoft Co-op Translatorom

## Prehľad
Microsoft Co-Op Translator je výkonný nástroj na bezproblémový preklad Markdown dokumentov. Tento sprievodca vám pomôže vyriešiť bežné problémy, ktoré sa môžu pri používaní tohto nástroja vyskytnúť.

## Bežné problémy a riešenia

### 1. Problém s Markdown tagom
**Problém:** Preložený Markdown dokument obsahuje tag `markdown` na začiatku, čo spôsobuje problémy s vykresľovaním.

**Riešenie:** Na vyriešenie jednoducho odstráňte tag `markdown` na začiatku súboru. Tým sa zabezpečí správne zobrazenie Markdown súboru.

**Kroky:**
1. Otvorte preložený Markdown (`.md`) súbor.
2. Nájdite tag `markdown` na začiatku dokumentu.
3. Odstráňte tag `markdown`.
4. Uložte zmeny v súbore.
5. Znovu otvorte súbor, aby ste sa uistili, že sa správne vykresľuje.

### 2. Problém s URL vložených obrázkov
**Problém:** URL vložených obrázkov nezodpovedajú jazykovej lokalizácii, čo vedie k nesprávnym alebo chýbajúcim obrázkom.

**Riešenie:** Skontrolujte URL vložených obrázkov a uistite sa, že zodpovedajú jazykovej lokalizácii. Všetky obrázky sú uložené v priečinku `translated_images`, pričom každý obrázok má v názve súboru označenie jazykovej lokality.

**Kroky:**
1. Otvorte preložený Markdown dokument.
2. Identifikujte vložené obrázky a ich URL.
3. Overte, či jazyková lokalita v názve súboru obrázka zodpovedá jazyku dokumentu.
4. V prípade potreby aktualizujte URL.
5. Uložte zmeny a znovu otvorte dokument, aby ste potvrdili správne zobrazenie obrázkov.

### 3. Presnosť prekladu
**Problém:** Preložený obsah nie je presný alebo vyžaduje ďalšie úpravy.

**Riešenie:** Prezrite si preložený dokument a vykonajte potrebné úpravy na zlepšenie presnosti a čitateľnosti.

**Kroky:**
1. Otvorte preložený dokument.
2. Dôkladne si prezrite obsah.
3. Upravte preklad tak, aby bol presnejší.
4. Uložte zmeny.

### 4. Problémy s formátovaním súboru
**Problém:** Formátovanie preloženého dokumentu je nesprávne. Toto sa môže vyskytnúť napríklad v tabuľkách, kde ďalší ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` rieši problémy s tabuľkami.

**Kroky:**
1. Otvorte preložený dokument.
2. Porovnajte ho s originálnym dokumentom, aby ste identifikovali problémy s formátovaním.
3. Upravte formátovanie tak, aby zodpovedalo originálu.
4. Uložte zmeny.

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.