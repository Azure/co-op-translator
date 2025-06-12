<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:31:42+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "sl"
}
-->
# Microsoft Co-op Translator Troubleshooting Guide


## Overview
Microsoft Co-Op Translator je močan pripomoček za brezhibno prevajanje Markdown dokumentov. Ta vodič vam bo pomagal odpraviti pogoste težave, ki se pojavijo pri uporabi orodja.

## Common Issues and Solutions

### 1. Markdown Tag Issue
**Problem:** Prevedeni Markdown dokument vsebuje oznako `markdown` na vrhu, kar povzroča težave pri prikazu.

**Solution:** Za rešitev preprosto izbrišite oznako `markdown` na vrhu datoteke. To bo omogočilo pravilno prikazovanje Markdown datoteke.

**Steps:**
1. Odprite prevedeno Markdown (`.md`) datoteko.
2. Poiščite oznako `markdown` na vrhu dokumenta.
3. Izbrišite oznako `markdown`.
4. Shrani spremembe v datoteki.
5. Ponovno odprite datoteko, da preverite pravilno prikazovanje.

### 2. Embedded Images URL Issue
**Problem:** URL-ji vgrajenih slik ne ustrezajo jezikovni lokalizaciji, kar vodi do napačnih ali manjkajočih slik.

**Solution:** Preverite URL-je vgrajenih slik in zagotovite, da ustrezajo jezikovni lokalizaciji. Vse slike so v mapi `translated_images`, vsaka slika ima jezikovni lokalni tag v imenu datoteke.

**Steps:**
1. Odprite prevedeni Markdown dokument.
2. Prepoznajte vgrajene slike in njihove URL-je.
3. Preverite, da je jezikovni lokal v imenu datoteke slike skladen z jezikom dokumenta.
4. Po potrebi posodobite URL-je.
5. Shrani spremembe in ponovno odprite dokument, da potrdite pravilno prikazovanje slik.

### 3. Translation Accuracy
**Problem:** Prevedena vsebina ni natančna ali potrebuje dodatne popravke.

**Solution:** Preglejte prevedeni dokument in naredite potrebne popravke za izboljšanje natančnosti in berljivosti.

**Steps:**
1. Odprite prevedeni dokument.
2. Previdno preglejte vsebino.
3. Naredite potrebne popravke za izboljšanje natančnosti prevoda.
4. Shrani spremembe.

### 4. File Formatting Issues
**Problem:** Oblikovanje prevedenega dokumenta ni pravilno. To se lahko zgodi v tabelah, tukaj dodatni ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` bo rešil težave s tabelami.

**Steps:**
1. Odprite prevedeni dokument.
2. Primerjajte ga z izvirnim dokumentom, da ugotovite težave z oblikovanjem.
3. Prilagodite oblikovanje, da bo ustrezalo izvirniku.
4. Shrani spremembe.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.