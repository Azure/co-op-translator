<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:50:17+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "ro"
}
-->
# Actualizează secțiunea „Alte cursuri” (repositorii Microsoft Beginners)

Acest ghid explică cum să faci ca secțiunea „Alte cursuri” să se sincronizeze automat folosind Co-op Translator și cum să actualizezi șablonul global pentru toate repozitoriile.

- Se aplică pentru: doar repozitoriile Microsoft Beginners
- Funcționează cu: Co-op Translator CLI și GitHub Actions
- Sursa șablonului: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Pornire rapidă: Activează sincronizarea automată în repo-ul tău

Adaugă următorii markeri în jurul secțiunii „Alte cursuri” din README-ul tău. Co-op Translator va înlocui tot ce se află între acești markeri la fiecare rulare.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

De fiecare dată când Co-op Translator rulează — prin CLI (de exemplu, `translate -l "<language codes>"`) sau GitHub Actions — actualizează automat secțiunea „Alte cursuri” încadrată de acești markeri.

> [!NOTE]
> Dacă ai deja o listă existentă, pur și simplu încadreaz-o cu aceiași markeri. La următoarea rulare, aceasta va fi înlocuită cu conținutul standardizat cel mai recent.

---

## Cum să modifici conținutul global

Dacă vrei să actualizezi conținutul standardizat care apare în toate repozitoriile Beginners:

1. Editează șablonul: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Deschide un pull request în repo-ul Co-op Translator cu modificările tale
3. După ce PR-ul este acceptat, versiunea Co-op Translator va fi actualizată
4. Data viitoare când Co-op Translator rulează (CLI sau GitHub Action) într-un repo țintă, va sincroniza automat secțiunea actualizată

Astfel se asigură o sursă unică de adevăr pentru conținutul „Alte cursuri” în toate repozitoriile Beginners.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->