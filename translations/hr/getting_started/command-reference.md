<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T04:06:03+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "hr"
}
-->
# Referenca naredbi

**Co-op Translator** CLI nudi nekoliko opcija za prilagodbu procesa prevođenja:

Naredba                                       | Opis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prevede vaš projekt na navedene jezike. Primjer: translate -l "es fr de" prevodi na španjolski, francuski i njemački. Koristite translate -l "all" za prijevod na sve podržane jezike.
translate -l "language_codes" -u              | Ažurira prijevode brisanjem postojećih i ponovnim kreiranjem. Upozorenje: Ovo briše sve trenutne prijevode za navedene jezike.
translate -l "language_codes" -img            | Prevodi samo slikovne datoteke.
translate -l "language_codes" -md             | Prevodi samo Markdown datoteke.
translate -l "language_codes" -nb             | Prevodi samo Jupyter notebook datoteke (.ipynb).
translate -l "language_codes" --fix           | Ponovno prevodi datoteke s niskim ocjenama povjerenja na temelju prethodnih rezultata evaluacije.
translate -l "language_codes" -d              | Omogućuje debug način rada za detaljno zapisivanje.
translate -l "language_codes" --save-logs, -s | Sprema DEBUG zapisnike u datoteke pod <root_dir>/logs/ (konzola ostaje kontrolirana s -d)
translate -l "language_codes" -r "root_dir"   | Određuje korijenski direktorij projekta
translate -l "language_codes" -f              | Koristi brzi način za prijevod slika (do 3x brže crtanje uz malu žrtvu kvalitete i poravnanja).
translate -l "language_codes" -y              | Automatski potvrđuje sve upite (korisno za CI/CD procese)
translate -l "language_codes" --help          | prikazuje detalje o dostupnim naredbama unutar CLI-a
evaluate -l "language_code"                  | Procjenjuje kvalitetu prijevoda za određeni jezik i daje ocjene povjerenja
evaluate -l "language_code" -c 0.8           | Procjenjuje prijevode s prilagođenim pragom povjerenja
evaluate -l "language_code" -f               | Brzi način evaluacije (samo pravila, bez LLM-a)
evaluate -l "language_code" -D               | Dubinska evaluacija (samo LLM, temeljitije ali sporije)
evaluate -l "language_code" --save-logs, -s  | Sprema DEBUG zapisnike u datoteke pod <root_dir>/logs/
migrate-links -l "language_codes"             | Ponovno obrađuje prevedene Markdown datoteke radi ažuriranja linkova na bilježnice (.ipynb). Preferira prevedene bilježnice kad su dostupne; inače može koristiti originalne bilježnice.
migrate-links -l "language_codes" -r          | Određuje korijenski direktorij projekta (zadano: trenutni direktorij).
migrate-links -l "language_codes" --dry-run   | Prikazuje koje bi se datoteke promijenile bez zapisivanja promjena.
migrate-links -l "language_codes" --no-fallback-to-original | Ne prepisuje linkove na originalne bilježnice kad prevedene nedostaju (ažurira samo kad prevedene postoje).
migrate-links -l "language_codes" -d          | Omogućuje debug način rada za detaljno zapisivanje.
migrate-links -l "language_codes" --save-logs, -s | Sprema DEBUG zapisnike u datoteke pod <root_dir>/logs/
migrate-links -l "all" -y                      | Obradi sve jezike i automatski potvrdi upozorenje.

## Primjeri korištenja

  1. Zadano ponašanje (dodaje nove prijevode bez brisanja postojećih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaje samo nove korejske prijevode slika (postojeći prijevodi se ne brišu):    translate -l "ko" -img

  3. Ažurira sve korejske prijevode (Upozorenje: Briše sve postojeće korejske prijevode prije ponovnog prevođenja):    translate -l "ko" -u

  4. Ažurira samo korejske slike (Upozorenje: Briše sve postojeće korejske slike prije ponovnog prevođenja):    translate -l "ko" -img -u

  5. Dodaje nove markdown prijevode za korejski bez utjecaja na ostale prijevode:    translate -l "ko" -md

  6. Popravlja prijevode s niskim povjerenjem na temelju prethodnih rezultata evaluacije: translate -l "ko" --fix

  7. Popravlja prijevode s niskim povjerenjem samo za određene datoteke (markdown): translate -l "ko" --fix -md

  8. Popravlja prijevode s niskim povjerenjem samo za određene datoteke (slike): translate -l "ko" --fix -img

  9. Koristi brzi način za prijevod slika:    translate -l "ko" -img -f

  10. Popravlja prijevode s niskim povjerenjem s prilagođenim pragom: translate -l "ko" --fix -c 0.8

  11. Primjer debug načina: - translate -l "ko" -d: Omogućuje debug zapisivanje.
  12. Spremanje zapisnika u datoteke: translate -l "ko" -s
  13. DEBUG na konzoli i u datotekama: translate -l "ko" -d -s

  14. Migracija linkova na bilježnice za korejske prijevode (ažurira linkove na prevedene bilježnice kad su dostupne):    migrate-links -l "ko"

  15. Migracija linkova s dry-run opcijom (bez zapisivanja u datoteke):    migrate-links -l "ko" --dry-run

  16. Ažurira linkove samo kad prevedene bilježnice postoje (ne koristi originalne):    migrate-links -l "ko" --no-fallback-to-original

  17. Obradi sve jezike s upitom za potvrdu:    migrate-links -l "all"

  18. Obradi sve jezike i automatski potvrdi:    migrate-links -l "all" -y
  19. Spremi zapisnike za migrate-links:    migrate-links -l "ko ja" -s

### Primjeri evaluacije

> [!WARNING]  
> **Beta značajka**: Funkcionalnost evaluacije je trenutno u beta fazi. Ova značajka je objavljena za procjenu prevedenih dokumenata, a metode evaluacije i detaljna implementacija su još u razvoju i mogu se mijenjati.

  1. Procjena korejskih prijevoda: evaluate -l "ko"

  2. Procjena s prilagođenim pragom povjerenja: evaluate -l "ko" -c 0.8

  3. Brza evaluacija (samo pravila): evaluate -l "ko" -f

  4. Dubinska evaluacija (samo LLM): evaluate -l "ko" -D

---

**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja nastala korištenjem ovog prijevoda.