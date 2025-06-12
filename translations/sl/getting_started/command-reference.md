<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:34:17+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "sl"
}
-->
# Command reference
The **Co-op Translator** CLI nudi več možnosti za prilagoditev procesa prevajanja:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prevede vaš projekt v določene jezike. Primer: translate -l "es fr de" prevede v španščino, francoščino in nemščino. Uporabite translate -l "all" za prevod v vse podprte jezike.
translate -l "language_codes" -u              | Posodobi prevode z brisanjem obstoječih in njihovo ponovnim ustvarjanjem. Warning: To bo izbrisalo vse trenutne prevode za določene jezike.
translate -l "language_codes" -img            | Prevede samo slikovne datoteke.
translate -l "language_codes" -md             | Prevede samo Markdown datoteke.
translate -l "language_codes" -chk            | Preveri prevedene datoteke za napake in po potrebi ponovi prevajanje.
translate -l "language_codes" -d              | Omogoči debug način za podrobno beleženje.
translate -l "language_codes" -r "root_dir"   | Določi korensko mapo projekta
translate -l "language_codes" -f              | Uporabi hiter način za prevajanje slik (do 3x hitrejše risanje z rahlim vplivom na kakovost in poravnavo).
translate -l "language_codes" -y              | Samodejno potrdi vse pozive (uporabno za CI/CD pipeline)
translate -l "language_codes" --help          | podrobnosti pomoči znotraj CLI, ki prikazujejo razpoložljive ukaze

### Usage examples:

  1. Privzeto vedenje (dodaj nove prevode brez brisanja obstoječih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj samo nove korejske slikovne prevode (obstoječi prevodi niso izbrisani):    translate -l "ko" -img

  3. Posodobi vse korejske prevode (Warning: To izbriše vse obstoječe korejske prevode pred ponovnim prevajanjem):    translate -l "ko" -u

  4. Posodobi samo korejske slike (Warning: To izbriše vse obstoječe korejske slike pred ponovnim prevajanjem):    translate -l "ko" -img -u

  5. Dodaj nove markdown prevode za korejščino brez vpliva na druge prevode:    translate -l "ko" -md

  6. Preveri prevedene datoteke za napake in po potrebi ponovi prevajanje: translate -l "ko" -chk

  7. Preveri prevedene datoteke za napake in po potrebi ponovi prevajanje (samo markdown): translate -l "ko" -chk -md

  8. Preveri prevedene datoteke za napake in po potrebi ponovi prevajanje (samo slike): translate -l "ko" -chk -img

  9. Uporabi hiter način za prevajanje slik:    translate -l "ko" -img -f

  10. Primer debug načina: - translate -l "ko" -d: Omogoči debug beleženje.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.