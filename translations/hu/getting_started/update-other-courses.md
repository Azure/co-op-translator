<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:49:02+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "hu"
}
-->
# A „További tanfolyamok” szakasz frissítése (Microsoft Beginners tárolók)

Ez az útmutató bemutatja, hogyan lehet a „További tanfolyamok” szakaszt automatikusan szinkronizálni a Co-op Translator segítségével, és hogyan lehet frissíteni az összes tárolóra vonatkozó globális sablont.

- Érvényes: csak Microsoft Beginners tárolókra
- Működik: Co-op Translator CLI-vel és GitHub Actions-szel
- Sablon forrása: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Gyors kezdés: Engedélyezd az automatikus szinkronizálást a tárolódban

Add hozzá a következő jelölőket a README „További tanfolyamok” szakasza köré. A Co-op Translator minden futtatáskor kicseréli a jelölők közötti tartalmat.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Minden alkalommal, amikor a Co-op Translator fut — akár CLI-n keresztül (pl. `translate -l "<language codes>"`), akár GitHub Actions-ben — automatikusan frissíti a jelölők közé zárt „További tanfolyamok” szakaszt.

> [!NOTE]
> Ha már van meglévő listád, egyszerűen csak csomagold be ugyanilyen jelölőkkel. A következő futtatás a legfrissebb, szabványosított tartalomra cseréli majd.

---

## Hogyan változtasd meg a globális tartalmat

Ha frissíteni szeretnéd a szabványosított tartalmat, amely az összes Beginners tárolóban megjelenik:

1. Szerkeszd a sablont: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Nyiss egy pull requestet a Co-op Translator tárolóba a módosításokkal
3. A PR egyesítése után a Co-op Translator verziója frissül
4. Amikor legközelebb a Co-op Translator fut (CLI vagy GitHub Action) egy célzott tárolóban, automatikusan szinkronizálja a frissített szakaszt

Ez biztosítja, hogy a „További tanfolyamok” tartalma minden Beginners tárolóban egységes és naprakész legyen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->