<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:33:48+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sr"
}
-->
# Reference komandi
**Co-op Translator** CLI nudi nekoliko opcija za prilagođavanje procesa prevođenja:

Komanda                                      | Opis
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prevodi vaš projekat na navedene jezike. Primer: translate -l "es fr de" prevodi na španski, francuski i nemački. Koristite translate -l "all" za prevođenje na sve podržane jezike.
translate -l "language_codes" -u              | Ažurira prevode brisanjem postojećih i njihovim ponovnim kreiranjem. Upozorenje: Ovo će obrisati sve trenutne prevode za navedene jezike.
translate -l "language_codes" -img            | Prevodi samo fajlove sa slikama.
translate -l "language_codes" -md             | Prevodi samo Markdown fajlove.
translate -l "language_codes" -chk            | Proverava prevedene fajlove na greške i ponovo pokušava prevođenje ako je potrebno.
translate -l "language_codes" -d              | Omogućava debug režim za detaljno beleženje.
translate -l "language_codes" -r "root_dir"   | Navodi korenski direktorijum projekta
translate -l "language_codes" -f              | Koristi brzi režim za prevođenje slika (do 3x brže prikazivanje uz blagi pad kvaliteta i poravnanja).
translate -l "language_codes" -y              | Automatski potvrđuje sve upite (korisno za CI/CD pipeline-ove)
translate -l "language_codes" --help          | prikaz pomoći unutar CLI sa dostupnim komandama

### Primeri korišćenja:

  1. Podrazumevano ponašanje (dodavanje novih prevoda bez brisanja postojećih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodavanje samo novih korejskih prevoda slika (bez brisanja postojećih prevoda):    translate -l "ko" -img

  3. Ažuriranje svih korejskih prevoda (Upozorenje: Ovo briše sve postojeće korejske prevode pre ponovnog prevođenja):    translate -l "ko" -u

  4. Ažuriranje samo korejskih slika (Upozorenje: Ovo briše sve postojeće korejske slike pre ponovnog prevođenja):    translate -l "ko" -img -u

  5. Dodavanje novih markdown prevoda za korejski bez uticaja na ostale prevode:    translate -l "ko" -md

  6. Provera prevedenih fajlova na greške i ponovni pokušaj prevođenja ako je potrebno: translate -l "ko" -chk

  7. Provera prevedenih fajlova na greške i ponovni pokušaj prevođenja (samo markdown): translate -l "ko" -chk -md

  8. Provera prevedenih fajlova na greške i ponovni pokušaj prevođenja (samo slike): translate -l "ko" -chk -img

  9. Korišćenje brzog režima za prevođenje slika:    translate -l "ko" -img -f

  10. Primer debug režima: - translate -l "ko" -d: Omogućava debug beleženje.

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из употребе овог превода.