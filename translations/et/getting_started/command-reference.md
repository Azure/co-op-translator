<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T13:03:02+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "et"
}
-->
# Käskude viide

**Co-op Translator** CLI pakub mitmeid valikuid tõlkeprotsessi kohandamiseks:

Käsk                                         | Kirjeldus
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Tõlgib teie projekti määratud keeltesse. Näide: translate -l "es fr de" tõlgib hispaania, prantsuse ja saksa keelde. Kasutage translate -l "all", et tõlkida kõigisse toetatud keeltesse.
translate -l "language_codes" -u              | Uuendab tõlkeid, kustutades olemasolevad ja luues need uuesti. Hoiatus: see kustutab kõik praegused tõlked määratud keeltes.
translate -l "language_codes" -img            | Tõlgib ainult pildifaile.
translate -l "language_codes" -md             | Tõlgib ainult Markdown-faile.
translate -l "language_codes" -nb             | Tõlgib ainult Jupyteri märkmikefaile (.ipynb).
translate -l "language_codes" --fix           | Tõlgib uuesti faile, mille tõlke usaldusväärsuse skoor on madal, tuginedes varasematele hindamistulemustele.
translate -l "language_codes" -d              | Lülitab sisse silumisrežiimi üksikasjaliku logimise jaoks.
translate -l "language_codes" --save-logs, -s | Salvestab DEBUG-taseme logid failidesse kataloogi <root_dir>/logs/ (konsool jääb -d kontrolli alla)
translate -l "language_codes" -r "root_dir"   | Määrab projekti juurkataloogi
translate -l "language_codes" -f              | Kasutab piltide tõlkimiseks kiiret režiimi (kuni 3x kiirem joonistamine väikese kvaliteedi ja joondamise kadu hinnaga).
translate -l "language_codes" -y              | Kinnitab automaatselt kõik viited (kasulik CI/CD torujuhtmete jaoks)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Lülitab sisse või välja masina tõlke vastutuse välistamise lisamise tõlgitud markdowni ja märkmike puhul (vaikimisi: sisse lülitatud).
translate -l "language_codes" --help          | CLI-s kuvatavad abiteated ja saadaolevad käsud
evaluate -l "language_code"                  | Hindab tõlke kvaliteeti kindlas keeles ja annab usaldusväärsuse skoorid
evaluate -l "language_code" -c 0.8           | Hindab tõlkeid kohandatud usalduspiiriga
evaluate -l "language_code" -f               | Kiire hindamisrežiim (ainult reeglipõhine, ilma LLM-ita)
evaluate -l "language_code" -D               | Süva hindamisrežiim (ainult LLM-põhine, põhjalikum, kuid aeglasem)
evaluate -l "language_code" --save-logs, -s  | Salvestab DEBUG-taseme logid failidesse kataloogi <root_dir>/logs/
migrate-links -l "language_codes"             | Töötleb tõlgitud Markdown-faile uuesti, et uuendada linke märkmikele (.ipynb). Eelistab tõlgitud märkmikke, kui need on olemas; vastasel juhul võib kasutada originaalfaile.
migrate-links -l "language_codes" -r          | Määrab projekti juurkataloogi (vaikimisi: praegune kataloog).
migrate-links -l "language_codes" --dry-run   | Kuvab, millised failid muutuksid, ilma et muudatusi salvestataks.
migrate-links -l "language_codes" --no-fallback-to-original | Ei kirjuta linke ümber originaalsetele märkmikele, kui tõlgitud vasted puuduvad (uuendab ainult siis, kui tõlgitud versioon on olemas).
migrate-links -l "language_codes" -d          | Lülitab sisse silumisrežiimi üksikasjaliku logimise jaoks.
migrate-links -l "language_codes" --save-logs, -s | Salvestab DEBUG-taseme logid failidesse kataloogi <root_dir>/logs/
migrate-links -l "all" -y                      | Töötleb kõiki keeli ja kinnitab hoiatusviite automaatselt.

## Kasutusnäited

  1. Vaikimisi käitumine (lisab uusi tõlkeid, ilma olemasolevaid kustutamata):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lisab ainult uued korea pilditõlked (olemasolevaid tõlkeid ei kustutata):    translate -l "ko" -img

  3. Uuendab kõiki korea tõlkeid (Hoiatus: see kustutab kõik olemasolevad korea tõlked enne uuesti tõlkimist):    translate -l "ko" -u

  4. Uuendab ainult korea pilte (Hoiatus: see kustutab kõik olemasolevad korea pildid enne uuesti tõlkimist):    translate -l "ko" -img -u

  5. Lisab uued markdown-tõlked koreakeelsele, ilma teisi tõlkeid mõjutamata:    translate -l "ko" -md

  6. Parandab madala usaldusväärsusega tõlkeid varasemate hindamistulemuste põhjal: translate -l "ko" --fix

  7. Parandab madala usaldusväärsusega tõlkeid ainult kindlates failides (markdown): translate -l "ko" --fix -md

  8. Parandab madala usaldusväärsusega tõlkeid ainult kindlates failides (pildid): translate -l "ko" --fix -img

  9. Kasutab piltide tõlkimiseks kiiret režiimi:    translate -l "ko" -img -f

  10. Parandab madala usaldusväärsusega tõlkeid kohandatud lävega: translate -l "ko" --fix -c 0.8

  11. Silumisrežiimi näide: - translate -l "ko" -d: Lülitab sisse silumislogimise.
  12. Salvestab logid failidesse: translate -l "ko" -s
  13. Konsooli DEBUG ja faili DEBUG: translate -l "ko" -d -s
  14. Tõlgib ilma masina tõlke vastutuse välistust lisamata: translate -l "ko" --no-disclaimer

  15. Märkmike linkide migreerimine korea tõlgetes (uuendab linke tõlgitud märkmikele, kui need on olemas):    migrate-links -l "ko"

  15. Linkide migreerimine kuivjooksuga (failidesse kirjutamata):    migrate-links -l "ko" --dry-run

  16. Uuendab linke ainult siis, kui tõlgitud märkmikud on olemas (ei kasuta originaale):    migrate-links -l "ko" --no-fallback-to-original

  17. Töötleb kõiki keeli koos kinnituskäsuga:    migrate-links -l "all"

  18. Töötleb kõiki keeli ja kinnitab automaatselt:    migrate-links -l "all" -y
  19. Salvestab migrate-links logid failidesse:    migrate-links -l "ko ja" -s

### Hindamise näited

> [!WARNING]  
> **Beeta funktsioon**: Hindamisfunktsioon on hetkel beetaversioonis. See funktsioon avaldati tõlgitud dokumentide hindamiseks ning hindamismeetodid ja üksikasjalik teostus on veel arendamisel ja võivad muutuda.

  1. Hindab korea tõlkeid: evaluate -l "ko"

  2. Hindab kohandatud usalduslävega: evaluate -l "ko" -c 0.8

  3. Kiire hindamine (ainult reeglipõhine): evaluate -l "ko" -f

  4. Süva hindamine (ainult LLM-põhine): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->