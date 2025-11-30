<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T04:47:07+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "et"
}
-->
# Käskude viide

**Co-op Translator** CLI pakub mitmeid võimalusi tõlkeprotsessi kohandamiseks:

Käsk                                         | Kirjeldus
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Tõlgib sinu projekti määratud keeltesse. Näide: translate -l "es fr de" tõlgib hispaania, prantsuse ja saksa keelde. Kasuta translate -l "all", et tõlkida kõikidesse toetatud keeltesse.
translate -l "language_codes" -u              | Uuendab tõlkeid, kustutades olemasolevad ja luues need uuesti. Hoiatus: see kustutab kõik praegused tõlked määratud keeltes.
translate -l "language_codes" -img            | Tõlgib ainult pildifailid.
translate -l "language_codes" -md             | Tõlgib ainult Markdown-failid.
translate -l "language_codes" -nb             | Tõlgib ainult Jupyter notebook failid (.ipynb).
translate -l "language_codes" --fix           | Tõlgib uuesti failid, millel on madal usaldusväärsuse skoor varasemate hindamistulemuste põhjal.
translate -l "language_codes" -d              | Lülitab sisse silumisrežiimi detailse logimise jaoks.
translate -l "language_codes" --save-logs, -s | Salvestab DEBUG-taseme logid failidesse <root_dir>/logs/ (konsool jääb kontrolli alla -d)
translate -l "language_codes" -r "root_dir"   | Määrab projekti juurkataloogi
translate -l "language_codes" -f              | Kasutab kiiret režiimi pilditõlkes (kuni 3x kiirem joonistamine väikese kvaliteedi ja joondamise arvelt).
translate -l "language_codes" -y              | Kinnitab kõik küsimused automaatselt (kasulik CI/CD torujuhtmetes)
translate -l "language_codes" --help          | CLI-sisene abi, mis näitab saadaolevaid käske
evaluate -l "language_code"                  | Hindab tõlke kvaliteeti kindlas keeles ja annab usaldusväärsuse skoorid
evaluate -l "language_code" -c 0.8           | Hindab tõlkeid kohandatud usaldusväärsuse lävega
evaluate -l "language_code" -f               | Kiire hindamisrežiim (ainult reeglipõhine, ilma LLM-ita)
evaluate -l "language_code" -D               | Süvitsi hindamisrežiim (ainult LLM-põhine, põhjalikum, kuid aeglasem)
evaluate -l "language_code" --save-logs, -s  | Salvestab DEBUG-taseme logid failidesse <root_dir>/logs/
migrate-links -l "language_codes"             | Töötleb tõlgitud Markdown-faile uuesti, et uuendada viiteid notebookidele (.ipynb). Eelistab tõlgitud notebooke, kui need on olemas; muidu võib kasutada originaale.
migrate-links -l "language_codes" -r          | Määra projekti juurkataloog (vaikimisi: praegune kataloog).
migrate-links -l "language_codes" --dry-run   | Näitab, millised failid muutuksid, ilma muudatusi salvestamata.
migrate-links -l "language_codes" --no-fallback-to-original | Ei uuenda viiteid originaalnotebookidele, kui tõlgitud versioon puudub (uuendab ainult siis, kui tõlgitud on olemas).
migrate-links -l "language_codes" -d          | Lülitab sisse silumisrežiimi detailse logimise jaoks.
migrate-links -l "language_codes" --save-logs, -s | Salvestab DEBUG-taseme logid failidesse <root_dir>/logs/
migrate-links -l "all" -y                      | Töötleb kõiki keeli ja kinnitab hoiatuse automaatselt.

## Kasutusnäited

  1. Vaikimisi käitumine (lisab uusi tõlkeid ilma olemasolevaid kustutamata):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lisa ainult uusi korea pilditõlkeid (olemasolevaid ei kustutata):    translate -l "ko" -img

  3. Uuenda kõiki korea tõlkeid (Hoiatus: see kustutab kõik olemasolevad korea tõlked enne uuesti tõlkimist):    translate -l "ko" -u

  4. Uuenda ainult korea pilte (Hoiatus: see kustutab kõik olemasolevad korea pildid enne uuesti tõlkimist):    translate -l "ko" -img -u

  5. Lisa uusi markdown-tõlkeid korea keeles ilma teisi tõlkeid mõjutamata:    translate -l "ko" -md

  6. Paranda madala usaldusväärsusega tõlked varasemate hindamistulemuste põhjal: translate -l "ko" --fix

  7. Paranda madala usaldusväärsusega tõlked ainult kindlates failides (markdown): translate -l "ko" --fix -md

  8. Paranda madala usaldusväärsusega tõlked ainult kindlates failides (pildid): translate -l "ko" --fix -img

  9. Kasuta kiiret režiimi pilditõlkes:    translate -l "ko" -img -f

  10. Paranda madala usaldusväärsusega tõlked kohandatud lävega: translate -l "ko" --fix -c 0.8

  11. Silumisrežiimi näide: - translate -l "ko" -d: Lülita sisse silumislogimine.
  12. Salvesta logid failidesse: translate -l "ko" -s
  13. Konsooli DEBUG ja faili DEBUG: translate -l "ko" -d -s

  14. Notebooki viidete migratsioon korea tõlgetele (uuenda viiteid tõlgitud notebookidele, kui need on olemas):    migrate-links -l "ko"

  15. Viidete migratsioon kuivkäigul (faile ei kirjutata):    migrate-links -l "ko" --dry-run

  16. Uuenda viiteid ainult siis, kui tõlgitud notebookid on olemas (ära kasuta originaale):    migrate-links -l "ko" --no-fallback-to-original

  17. Töötle kõiki keeli koos kinnitusküsimusega:    migrate-links -l "all"

  18. Töötle kõiki keeli ja kinnita automaatselt:    migrate-links -l "all" -y
  19. Salvesta logid failidesse migrate-links jaoks:    migrate-links -l "ko ja" -s

### Hindamise näited

> [!WARNING]  
> **Beetafunktsioon**: Hindamise funktsionaalsus on hetkel beetaversioonis. See funktsioon avaldati tõlgitud dokumentide hindamiseks ning hindamismeetodid ja detailne teostus on veel arendamisel ja võivad muutuda.

  1. Hinda korea tõlkeid: evaluate -l "ko"

  2. Hinda kohandatud usaldusväärsuse lävega: evaluate -l "ko" -c 0.8

  3. Kiire hindamine (ainult reeglipõhine): evaluate -l "ko" -f

  4. Süvitsi hindamine (ainult LLM-põhine): evaluate -l "ko" -D

---

**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle algses keeles on autoriteetne allikas. Kriitilise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgendamise eest.