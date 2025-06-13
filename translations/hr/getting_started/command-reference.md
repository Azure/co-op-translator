<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:34:06+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "hr"
}
-->
# Command reference
CLI alat **Co-op Translator** nudi nekoliko opcija za prilagodbu procesa prevođenja:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prevodi vaš projekt na navedene jezike. Primjer: translate -l "es fr de" prevodi na španjolski, francuski i njemački. Koristite translate -l "all" za prijevod na sve podržane jezike.
translate -l "language_codes" -u              | Ažurira prijevode tako da briše postojeće i ponovno ih stvara. Upozorenje: Ovo će izbrisati sve trenutne prijevode za navedene jezike.
translate -l "language_codes" -img            | Prevodi samo slikovne datoteke.
translate -l "language_codes" -md             | Prevodi samo Markdown datoteke.
translate -l "language_codes" -chk            | Provjerava prevedene datoteke na pogreške i po potrebi pokušava ponovno prevesti.
translate -l "language_codes" -d              | Omogućuje debug način za detaljno bilježenje.
translate -l "language_codes" -r "root_dir"   | Određuje root direktorij projekta
translate -l "language_codes" -f              | Koristi brzi način za prijevod slika (do 3x brže crtanje uz malu žrtvu kvalitete i poravnanja).
translate -l "language_codes" -y              | Automatski potvrđuje sve upite (korisno za CI/CD pipelineove)
translate -l "language_codes" --help          | prikaz pomoći unutar CLI-ja s dostupnim naredbama

### Primjeri korištenja:

  1. Zadano ponašanje (dodavanje novih prijevoda bez brisanja postojećih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodavanje samo novih prijevoda slika na korejski (bez brisanja postojećih prijevoda):    translate -l "ko" -img

  3. Ažuriranje svih prijevoda na korejski (Upozorenje: Ovo briše sve postojeće korejske prijevode prije ponovnog prevođenja):    translate -l "ko" -u

  4. Ažuriranje samo korejskih slika (Upozorenje: Ovo briše sve postojeće korejske slike prije ponovnog prevođenja):    translate -l "ko" -img -u

  5. Dodavanje novih prijevoda Markdown datoteka za korejski bez utjecaja na druge prijevode:    translate -l "ko" -md

  6. Provjera prevedenih datoteka na pogreške i ponovno pokušavanje prijevoda ako je potrebno: translate -l "ko" -chk

  7. Provjera prevedenih datoteka na pogreške i ponovno pokušavanje prijevoda (samo Markdown): translate -l "ko" -chk -md

  8. Provjera prevedenih datoteka na pogreške i ponovno pokušavanje prijevoda (samo slike): translate -l "ko" -chk -img

  9. Korištenje brzog načina za prijevod slika:    translate -l "ko" -img -f

  10. Primjer debug načina: - translate -l "ko" -d: Omogućuje debug bilježenje.

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.