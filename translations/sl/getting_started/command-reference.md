<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T04:09:00+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sl"
}
-->
# Referenca ukazov

CLI **Co-op Translator** ponuja več možnosti za prilagajanje postopka prevajanja:

Ukaz                                        | Opis
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | Prevede vaš projekt v izbrane jezike. Primer: translate -l "es fr de" prevede v španščino, francoščino in nemščino. Uporabite translate -l "all" za prevod v vse podprte jezike.
translate -l "language_codes" -u             | Posodobi prevode tako, da obstoječe izbriše in jih ponovno ustvari. Opozorilo: To bo izbrisalo vse trenutne prevode za izbrane jezike.
translate -l "language_codes" -img           | Prevede samo slikovne datoteke.
translate -l "language_codes" -md            | Prevede samo Markdown datoteke.
translate -l "language_codes" -nb            | Prevede samo Jupyter notebook datoteke (.ipynb).
translate -l "language_codes" --fix          | Ponovno prevede datoteke z nizko stopnjo zaupanja na podlagi prejšnjih rezultatov ocenjevanja.
translate -l "language_codes" -d             | Omogoči način za odpravljanje napak za podrobno beleženje.
translate -l "language_codes" --save-logs, -s| Shrani DEBUG dnevniške datoteke pod <root_dir>/logs/ (konzola ostane pod nadzorom -d)
translate -l "language_codes" -r "root_dir"  | Določi korensko mapo projekta
translate -l "language_codes" -f             | Uporabi hitri način za prevajanje slik (do 3x hitrejše risanje z rahlo slabšo kakovostjo in poravnavo).
translate -l "language_codes" -y             | Samodejno potrdi vsa vprašanja (uporabno za CI/CD procese)
translate -l "language_codes" --help         | Prikaže podrobnosti pomoči v CLI z razpoložljivimi ukazi
evaluate -l "language_code"                  | Ocenjuje kakovost prevoda za določen jezik in poda stopnjo zaupanja
evaluate -l "language_code" -c 0.8           | Ocenjuje prevode s prilagojenim pragom zaupanja
evaluate -l "language_code" -f               | Hitro ocenjevanje (samo na podlagi pravil, brez LLM)
evaluate -l "language_code" -D               | Globoko ocenjevanje (samo na podlagi LLM, bolj temeljito, a počasneje)
evaluate -l "language_code" --save-logs, -s  | Shrani DEBUG dnevniške datoteke pod <root_dir>/logs/
migrate-links -l "language_codes"            | Ponovno obdela prevedene Markdown datoteke za posodobitev povezav do notebookov (.ipynb). Prednost imajo prevedeni notebooki, če so na voljo; sicer se lahko uporabi izvirne.
migrate-links -l "language_codes" -r         | Določi korensko mapo projekta (privzeto: trenutna mapa).
migrate-links -l "language_codes" --dry-run  | Prikaže, katere datoteke bi se spremenile, brez dejanskega zapisovanja sprememb.
migrate-links -l "language_codes" --no-fallback-to-original | Ne prepiši povezav na izvirne notebooke, če prevedeni manjkajo (posodobi le, če prevedeni obstajajo).
migrate-links -l "language_codes" -d         | Omogoči način za odpravljanje napak za podrobno beleženje.
migrate-links -l "language_codes" --save-logs, -s | Shrani DEBUG dnevniške datoteke pod <root_dir>/logs/
migrate-links -l "all" -y                    | Obdelaj vse jezike in samodejno potrdi opozorilo.

## Primeri uporabe

  1. Privzeto vedenje (doda nove prevode brez brisanja obstoječih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj samo nove korejske prevode slik (obstoječi prevodi se ne izbrišejo):    translate -l "ko" -img

  3. Posodobi vse korejske prevode (Opozorilo: To izbriše vse obstoječe korejske prevode pred ponovnim prevajanjem):    translate -l "ko" -u

  4. Posodobi samo korejske slike (Opozorilo: To izbriše vse obstoječe korejske slike pred ponovnim prevajanjem):    translate -l "ko" -img -u

  5. Dodaj nove prevode Markdown za korejščino brez vpliva na druge prevode:    translate -l "ko" -md

  6. Popravi prevode z nizko stopnjo zaupanja na podlagi prejšnjih rezultatov ocenjevanja: translate -l "ko" --fix

  7. Popravi prevode z nizko stopnjo zaupanja samo za določene datoteke (Markdown): translate -l "ko" --fix -md

  8. Popravi prevode z nizko stopnjo zaupanja samo za določene datoteke (slike): translate -l "ko" --fix -img

  9. Uporabi hitri način za prevajanje slik:    translate -l "ko" -img -f

  10. Popravi prevode z nizko stopnjo zaupanja s prilagojenim pragom: translate -l "ko" --fix -c 0.8

  11. Primer načina za odpravljanje napak: - translate -l "ko" -d: Omogoči podrobno beleženje.
  12. Shranjevanje dnevnikov v datoteke: translate -l "ko" -s
  13. DEBUG na konzoli in v datotekah: translate -l "ko" -d -s

  14. Migracija povezav do notebookov za korejske prevode (posodobi povezave do prevedenih notebookov, če so na voljo):    migrate-links -l "ko"

  15. Migracija povezav s suhim zagonom (brez zapisovanja datotek):    migrate-links -l "ko" --dry-run

  16. Posodobi povezave le, če prevedeni notebooki obstajajo (ne uporabi izvirnih):    migrate-links -l "ko" --no-fallback-to-original

  17. Obdelaj vse jezike s potrditvenim vprašanjem:    migrate-links -l "all"

  18. Obdelaj vse jezike in samodejno potrdi:    migrate-links -l "all" -y
  19. Shranjevanje dnevnikov v datoteke za migrate-links:    migrate-links -l "ko ja" -s

### Primeri ocenjevanja

> [!WARNING]  
> **Beta funkcija**: Funkcionalnost ocenjevanja je trenutno v beta fazi. Ta funkcija je bila izdana za ocenjevanje prevedenih dokumentov, metode ocenjevanja in podrobna izvedba pa so še v razvoju in se lahko spremenijo.

  1. Ocenjevanje korejskih prevodov: evaluate -l "ko"

  2. Ocenjevanje s prilagojenim pragom zaupanja: evaluate -l "ko" -c 0.8

  3. Hitro ocenjevanje (samo na podlagi pravil): evaluate -l "ko" -f

  4. Globoko ocenjevanje (samo na podlagi LLM): evaluate -l "ko" -D

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden s pomočjo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvoru jeziku naj velja za avtoritativni vir. Za kritične informacije priporočamo strokoven človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.