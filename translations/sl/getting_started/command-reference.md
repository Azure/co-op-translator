<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "822238e4451d04bb152cebb1be6f13c2",
  "translation_date": "2025-11-30T12:37:45+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sl"
}
-->
# Referenca ukazov

Ukazna vrstica **Co-op Translator** ponuja več možnosti za prilagoditev procesa prevajanja:

Ukaz                                         | Opis
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prevede vaš projekt v določene jezike. Primer: translate -l "es fr de" prevede v španščino, francoščino in nemščino. Uporabite translate -l "all" za prevod v vse podprte jezike.
translate -l "language_codes" -u              | Posodobi prevode tako, da izbriše obstoječe in jih ponovno ustvari. Opozorilo: To bo izbrisalo vse trenutne prevode za določene jezike.
translate -l "language_codes" -img            | Prevede samo slikovne datoteke.
translate -l "language_codes" -md             | Prevede samo Markdown datoteke.
translate -l "language_codes" -nb             | Prevede samo Jupyter zvezke (.ipynb).
translate -l "language_codes" --fix           | Ponovno prevede datoteke z nizko stopnjo zaupanja na podlagi prejšnjih rezultatov ocenjevanja.
translate -l "language_codes" -d              | Omogoči način za odpravljanje napak za podrobno beleženje.
translate -l "language_codes" --save-logs, -s | Shrani dnevniške zapise na ravni DEBUG v datoteke pod <root_dir>/logs/ (konzola ostane pod nadzorom -d)
translate -l "language_codes" -r "root_dir"   | Določi korensko mapo projekta
translate -l "language_codes" -f              | Uporabi hiter način za prevajanje slik (do 3x hitrejše risanje z rahlo izgubo kakovosti in poravnave).
translate -l "language_codes" -y              | Samodejno potrdi vse pozive (uporabno za CI/CD cevovode)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Omogoči ali onemogoči dodajanje odstavka o strojno prevedenem besedilu v prevedene markdown in zvezke (privzeto: omogočeno).
translate -l "language_codes" --help          | Pomoč znotraj CLI, ki prikazuje razpoložljive ukaze
evaluate -l "language_code"                  | Ocenjuje kakovost prevoda za določen jezik in poda ocene zaupanja
evaluate -l "language_code" -c 0.8           | Ocenjuje prevode z lastnim pragom zaupanja
evaluate -l "language_code" -f               | Hiter način ocenjevanja (samo na podlagi pravil, brez LLM)
evaluate -l "language_code" -D               | Globoko ocenjevanje (samo na podlagi LLM, bolj temeljito, a počasneje)
evaluate -l "language_code" --save-logs, -s  | Shrani dnevniške zapise na ravni DEBUG v datoteke pod <root_dir>/logs/
migrate-links -l "language_codes"             | Ponovno obdela prevedene Markdown datoteke za posodobitev povezav do zvezkov (.ipynb). Prednost imajo prevedeni zvezki, če so na voljo; sicer lahko uporabi izvirne zvezke.
migrate-links -l "language_codes" -r          | Določi korensko mapo projekta (privzeto: trenutna mapa).
migrate-links -l "language_codes" --dry-run   | Prikaže, katere datoteke bi se spremenile, brez zapisovanja sprememb.
migrate-links -l "language_codes" --no-fallback-to-original | Ne prepiše povezav do izvirnih zvezkov, če prevedeni niso na voljo (posodobi samo, če prevedeni obstajajo).
migrate-links -l "language_codes" -d          | Omogoči način za odpravljanje napak za podrobno beleženje.
migrate-links -l "language_codes" --save-logs, -s | Shrani dnevniške zapise na ravni DEBUG v datoteke pod <root_dir>/logs/
migrate-links -l "all" -y                      | Obdelaj vse jezike in samodejno potrdi opozorilni poziv.

## Primeri uporabe

  1. Privzeto vedenje (dodaj nove prevode brez brisanja obstoječih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj samo nove korejske prevode slik (obstoječi prevodi niso izbrisani):    translate -l "ko" -img

  3. Posodobi vse korejske prevode (Opozorilo: To izbriše vse obstoječe korejske prevode pred ponovnim prevajanjem):    translate -l "ko" -u

  4. Posodobi samo korejske slike (Opozorilo: To izbriše vse obstoječe korejske slike pred ponovnim prevajanjem):    translate -l "ko" -img -u

  5. Dodaj nove prevode markdown za korejščino, ne da bi vplival na druge prevode:    translate -l "ko" -md

  6. Popravi prevode z nizko stopnjo zaupanja na podlagi prejšnjih rezultatov ocenjevanja: translate -l "ko" --fix

  7. Popravi prevode z nizko stopnjo zaupanja samo za določene datoteke (markdown): translate -l "ko" --fix -md

  8. Popravi prevode z nizko stopnjo zaupanja samo za določene datoteke (slike): translate -l "ko" --fix -img

  9. Uporabi hiter način za prevajanje slik:    translate -l "ko" -img -f

  10. Popravi prevode z nizko stopnjo zaupanja z lastnim pragom: translate -l "ko" --fix -c 0.8

  11. Primer načina za odpravljanje napak: - translate -l "ko" -d: Omogoči beleženje za odpravljanje napak.
  12. Shrani dnevnike v datoteke: translate -l "ko" -s
  13. DEBUG v konzoli in v datotekah: translate -l "ko" -d -s
  14. Prevedi brez dodajanja opozoril o strojno prevedenem besedilu: translate -l "ko" --no-disclaimer

  15. Migriraj povezave do zvezkov za korejske prevode (posodobi povezave do prevedenih zvezkov, če so na voljo):    migrate-links -l "ko"

  15. Migriraj povezave z dry-run (brez zapisovanja v datoteke):    migrate-links -l "ko" --dry-run

  16. Posodobi povezave samo, če prevedeni zvezki obstajajo (ne uporabi izvirnih):    migrate-links -l "ko" --no-fallback-to-original

  17. Obdelaj vse jezike s potrditvenim pozivom:    migrate-links -l "all"

  18. Obdelaj vse jezike in samodejno potrdi:    migrate-links -l "all" -y
  19. Shrani dnevnike v datoteke za migrate-links:    migrate-links -l "ko ja" -s

### Primeri ocenjevanja

> [!WARNING]  
> **Beta funkcija**: Funkcionalnost ocenjevanja je trenutno v beta fazi. Ta funkcija je bila izdana za ocenjevanje prevedenih dokumentov, metode ocenjevanja in podrobna implementacija pa so še v razvoju in se lahko spremenijo.

  1. Ocenjuj korejske prevode: evaluate -l "ko"

  2. Ocenjuj z lastnim pragom zaupanja: evaluate -l "ko" -c 0.8

  3. Hitra ocena (samo na podlagi pravil): evaluate -l "ko" -f

  4. Globoka ocena (samo na podlagi LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->