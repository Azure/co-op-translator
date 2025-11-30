<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:51:59+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "sl"
}
-->
# Posodobite razdelek "Drugi tečaji" (Microsoft Beginners repozitoriji)

Ta vodič pojasnjuje, kako omogočiti samodejno sinhronizacijo razdelka "Drugi tečaji" z uporabo Co-op Translatorja in kako posodobiti globalno predlogo za vse repozitorije.

- Velja za: samo Microsoft Beginners repozitorije
- Deluje z: Co-op Translator CLI in GitHub Actions
- Vir predloge: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Hiter začetek: Omogočite samodejno sinhronizacijo v vašem repozitoriju

Dodajte naslednje oznake okoli razdelka "Drugi tečaji" v vašem README. Co-op Translator bo ob vsakem zagonu zamenjal vse, kar je med tema oznakama.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Vsakič, ko se Co-op Translator zažene – preko CLI (npr. `translate -l "<jezikovni kodi>"`) ali GitHub Actions – samodejno posodobi razdelek "Drugi tečaji", ki je označen z tema oznakama.

> [!NOTE]
> Če že imate obstoječi seznam, ga preprosto obkrožite z enakima oznakama. Naslednji zagon bo vsebino nadomestil z najnovejšo standardizirano vsebino.

---

## Kako spremeniti globalno vsebino

Če želite posodobiti standardizirano vsebino, ki se pojavlja v vseh Beginners repozitorijih:

1. Uredite predlogo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Odprite pull request v Co-op Translator repozitorij s svojimi spremembami
3. Ko je PR združen, bo različica Co-op Translatorja posodobljena
4. Naslednjič, ko se Co-op Translator zažene (CLI ali GitHub Action) v ciljnem repozitoriju, bo samodejno sinhroniziral posodobljen razdelek

To zagotavlja en sam vir resnice za vsebino "Drugi tečaji" v vseh Beginners repozitorijih.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->