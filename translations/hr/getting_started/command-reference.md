<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T12:32:51+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "hr"
}
-->
# Referenca naredbi

CLI alat **Co-op Translator** nudi nekoliko opcija za prilagodbu procesa prevođenja:

Naredba                                      | Opis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prevodi vaš projekt na navedene jezike. Primjer: translate -l "es fr de" prevodi na španjolski, francuski i njemački. Koristite translate -l "all" za prevođenje na sve podržane jezike.
translate -l "language_codes" -u              | Ažurira prijevode brisanjem postojećih i njihovim ponovnim stvaranjem. Upozorenje: Ovo će izbrisati sve trenutne prijevode za navedene jezike.
translate -l "language_codes" -img            | Prevodi samo slikovne datoteke.
translate -l "language_codes" -md             | Prevodi samo Markdown datoteke.
translate -l "language_codes" -nb             | Prevodi samo Jupyter notebook datoteke (.ipynb).
translate -l "language_codes" --fix           | Ponovno prevodi datoteke s niskim ocjenama povjerenja na temelju prethodnih rezultata evaluacije.
translate -l "language_codes" -d              | Omogućuje debug način rada za detaljno zapisivanje.
translate -l "language_codes" --save-logs, -s | Sprema DEBUG razinu zapisa u datoteke unutar <root_dir>/logs/ (konzola ostaje pod kontrolom -d)
translate -l "language_codes" -r "root_dir"   | Navodi korijenski direktorij projekta
translate -l "language_codes" -f              | Koristi brzi način za prevođenje slika (do 3x brže iscrtavanje uz blagi gubitak kvalitete i poravnanja).
translate -l "language_codes" -y              | Automatski potvrđuje sve upite (korisno za CI/CD pipelineove)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Omogućuje ili onemogućuje dodavanje odjeljka s napomenom o strojnom prijevodu u prevedene markdown i notebook datoteke (zadano: omogućeno).
translate -l "language_codes" --help          | prikaz pomoći unutar CLI s dostupnim naredbama
evaluate -l "language_code"                  | Evaluira kvalitetu prijevoda za određeni jezik i daje ocjene povjerenja
evaluate -l "language_code" -c 0.8           | Evaluira prijevode s prilagođenim pragom povjerenja
evaluate -l "language_code" -f               | Brzi način evaluacije (samo na temelju pravila, bez LLM-a)
evaluate -l "language_code" -D               | Dubinska evaluacija (samo na temelju LLM-a, temeljitija ali sporija)
evaluate -l "language_code" --save-logs, -s  | Sprema DEBUG razinu zapisa u datoteke unutar <root_dir>/logs/
migrate-links -l "language_codes"             | Ponovno obrađuje prevedene Markdown datoteke kako bi ažurirao poveznice na notebookove (.ipynb). Preferira prevedene notebookove kad su dostupni; inače može koristiti originalne.
migrate-links -l "language_codes" -r          | Navodi korijenski direktorij projekta (zadano: trenutni direktorij).
migrate-links -l "language_codes" --dry-run   | Prikazuje koje bi se datoteke promijenile bez zapisivanja promjena.
migrate-links -l "language_codes" --no-fallback-to-original | Ne prepisuje poveznice na originalne notebookove kad nedostaju prevedene verzije (ažurira samo ako postoji prevedena verzija).
migrate-links -l "language_codes" -d          | Omogućuje debug način rada za detaljno zapisivanje.
migrate-links -l "language_codes" --save-logs, -s | Sprema DEBUG razinu zapisa u datoteke unutar <root_dir>/logs/
migrate-links -l "all" -y                      | Procesira sve jezike i automatski potvrđuje upozorenje.

## Primjeri korištenja

  1. Zadano ponašanje (dodaje nove prijevode bez brisanja postojećih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaje samo nove prijevode slika na korejski (ne brišu se postojeći prijevodi):    translate -l "ko" -img

  3. Ažurira sve korejske prijevode (Upozorenje: brišu se svi postojeći korejski prijevodi prije ponovnog prevođenja):    translate -l "ko" -u

  4. Ažurira samo korejske slike (Upozorenje: brišu se sve postojeće korejske slike prije ponovnog prevođenja):    translate -l "ko" -img -u

  5. Dodaje nove prijevode markdown datoteka za korejski bez utjecaja na ostale prijevode:    translate -l "ko" -md

  6. Popravlja prijevode s niskim povjerenjem na temelju prethodnih rezultata evaluacije: translate -l "ko" --fix

  7. Popravlja prijevode s niskim povjerenjem samo za određene datoteke (markdown): translate -l "ko" --fix -md

  8. Popravlja prijevode s niskim povjerenjem samo za određene datoteke (slike): translate -l "ko" --fix -img

  9. Koristi brzi način za prevođenje slika:    translate -l "ko" -img -f

  10. Popravlja prijevode s niskim povjerenjem s prilagođenim pragom: translate -l "ko" --fix -c 0.8

  11. Primjer debug načina rada: - translate -l "ko" -d: Omogućuje debug zapisivanje.
  12. Sprema zapise u datoteke: translate -l "ko" -s
  13. DEBUG u konzoli i u datotekama: translate -l "ko" -d -s
  14. Prevodi bez dodavanja napomena o strojnom prijevodu u izlaze: translate -l "ko" --no-disclaimer

  15. Migrira poveznice na notebookove za korejske prijevode (ažurira poveznice na prevedene notebookove kad su dostupni):    migrate-links -l "ko"

  15. Migrira poveznice s dry-run opcijom (bez zapisivanja u datoteke):    migrate-links -l "ko" --dry-run

  16. Ažurira poveznice samo kad postoje prevedeni notebookovi (ne koristi originalne kao zamjenu):    migrate-links -l "ko" --no-fallback-to-original

  17. Procesira sve jezike s potvrdom:    migrate-links -l "all"

  18. Procesira sve jezike i automatski potvrđuje:    migrate-links -l "all" -y
  19. Sprema zapise u datoteke za migrate-links:    migrate-links -l "ko ja" -s

### Primjeri evaluacije

> [!WARNING]  
> **Beta značajka**: Funkcionalnost evaluacije je trenutno u beta fazi. Ova značajka je objavljena za evaluaciju prevedenih dokumenata, a metode evaluacije i detaljna implementacija su još u razvoju i podložne su promjenama.

  1. Evaluira korejske prijevode: evaluate -l "ko"

  2. Evaluira s prilagođenim pragom povjerenja: evaluate -l "ko" -c 0.8

  3. Brza evaluacija (samo na temelju pravila): evaluate -l "ko" -f

  4. Dubinska evaluacija (samo na temelju LLM-a): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->