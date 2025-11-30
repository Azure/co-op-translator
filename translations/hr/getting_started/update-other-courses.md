<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:51:36+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "hr"
}
-->
# Ažurirajte odjeljak "Ostali tečajevi" (Microsoft Beginners repozitoriji)

Ovaj vodič objašnjava kako automatski sinkronizirati odjeljak "Ostali tečajevi" pomoću Co-op Translatora i kako ažurirati globalni predložak za sve repozitorije.

- Primjenjuje se na: samo Microsoft Beginners repozitorije
- Radi s: Co-op Translator CLI i GitHub Actions
- Izvor predloška: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Brzi početak: Omogućite automatsku sinkronizaciju u svom repozitoriju

Dodajte sljedeće oznake oko odjeljka "Ostali tečajevi" u vašem README-u. Co-op Translator će pri svakom pokretanju zamijeniti sve između ovih oznaka.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Svaki put kad se Co-op Translator pokrene — putem CLI-ja (npr. `translate -l "<language codes>"`) ili GitHub Actions — automatski ažurira odjeljak "Ostali tečajevi" koji je obuhvaćen ovim oznakama.

> [!NOTE]
> Ako već imate postojeću listu, samo je omotajte istim oznakama. Sljedeće pokretanje će je zamijeniti najnovijim standardiziranim sadržajem.

---

## Kako promijeniti globalni sadržaj

Ako želite ažurirati standardizirani sadržaj koji se pojavljuje u svim Beginners repozitorijima:

1. Uredite predložak: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Otvorite pull request u Co-op Translator repozitoriju sa svojim promjenama
3. Nakon što se PR spoji, verzija Co-op Translatora će biti ažurirana
4. Sljedeći put kad se Co-op Translator pokrene (CLI ili GitHub Action) u ciljnom repozitoriju, automatski će sinkronizirati ažurirani odjeljak

Ovo osigurava jedinstveni izvor istine za sadržaj "Ostali tečajevi" u svim Beginners repozitorijima.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazumevanja ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->