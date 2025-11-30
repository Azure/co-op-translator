<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-30T13:54:14+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "et"
}
-->
# Uuenda jaotist "Muud kursused" (Microsoft Beginners hoidlad)

See juhend selgitab, kuidas muuta jaotis "Muud kursused" automaatselt sünkroonitavaks Co-op Translatori abil ning kuidas uuendada globaalseid malle kõigi hoidlate jaoks.

- Kehtib ainult Microsoft Beginners hoidlatele
- Töötab koos: Co-op Translator CLI ja GitHub Actions
- Malle allikas: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Kiire algus: Luba automaatne sünkroonimine oma hoidlas

Lisa oma README-s jaotise "Muud kursused" ümber järgmised märgendid. Co-op Translator asendab iga käivitusega kõik nende märgendite vahel oleva sisu.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Iga kord, kui Co-op Translator käivitatakse – kas CLI kaudu (nt `translate -l "<language codes>"`) või GitHub Actions – uuendab see automaatselt nende märgendite vahel olevat jaotist "Muud kursused".

> [!NOTE]
> Kui sul on juba olemas nimekiri, siis lihtsalt ümbritse see samade märgenditega. Järgmine käivitamine asendab selle uusima standardiseeritud sisuga.

---

## Kuidas muuta globaalseid sisu

Kui soovid uuendada standardiseeritud sisu, mis kuvatakse kõigis Beginners hoidlates:

1. Muuda malli: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Ava pull request Co-op Translatori hoidlas oma muudatustega
3. Pärast PR-i ühendamist uuendatakse Co-op Translatori versioon
4. Järgmine kord, kui Co-op Translator käivitatakse (CLI või GitHub Action) sihthoidlas, sünkroonib see automaatselt uuendatud jaotise

See tagab "Muud kursused" sisu ühtse ja usaldusväärse allika kõigis Beginners hoidlates.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->