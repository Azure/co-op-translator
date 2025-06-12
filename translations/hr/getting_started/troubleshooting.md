<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:31:30+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "hr"
}
-->
# Microsoft Co-op Translator Vodič za Rješavanje Problema


## Pregled
Microsoft Co-Op Translator je moćan alat za besprijekorno prevođenje Markdown dokumenata. Ovaj vodič će vam pomoći u rješavanju uobičajenih problema koji se javljaju pri korištenju ovog alata.

## Uobičajeni Problemi i Rješenja

### 1. Problem s Markdown Oznakama
**Problem:** Prevedeni Markdown dokument sadrži `markdown` oznaku na vrhu, što uzrokuje probleme pri prikazu.

**Rješenje:** Za rješavanje ovog problema, jednostavno izbrišite `markdown` oznaku na vrhu datoteke. To će omogućiti ispravan prikaz Markdown datoteke.

**Koraci:**
1. Otvorite prevedenu Markdown (`.md`) datoteku.
2. Pronađite `markdown` oznaku na vrhu dokumenta.
3. Izbrišite `markdown` oznaku.
4. Spremite promjene u datoteku.
5. Ponovno otvorite datoteku kako biste provjerili ispravan prikaz.

### 2. Problem s URL-ovima Ugrađenih Slika
**Problem:** URL-ovi ugrađenih slika ne odgovaraju jezičnoj lokalizaciji, što dovodi do pogrešnih ili nedostajućih slika.

**Rješenje:** Provjerite URL-ove ugrađenih slika i osigurajte da odgovaraju jezičnoj lokalizaciji. Sve slike se nalaze u `translated_images` mapi, a svaka slika u nazivu datoteke sadrži oznaku jezične lokalizacije.

**Koraci:**
1. Otvorite prevedeni Markdown dokument.
2. Identificirajte ugrađene slike i njihove URL-ove.
3. Provjerite da je jezična lokalizacija u nazivu datoteke slike usklađena s jezikom dokumenta.
4. Ažurirajte URL-ove ako je potrebno.
5. Spremite promjene i ponovno otvorite dokument kako biste potvrdili ispravan prikaz slika.

### 3. Točnost Prijevoda
**Problem:** Prevedeni sadržaj nije točan ili zahtijeva dodatne ispravke.

**Rješenje:** Pregledajte prevedeni dokument i napravite potrebne izmjene kako biste poboljšali točnost i čitljivost.

**Koraci:**
1. Otvorite prevedeni dokument.
2. Pažljivo pregledajte sadržaj.
3. Napravite potrebne izmjene za poboljšanje točnosti prijevoda.
4. Spremite promjene.

### 4. Problemi s Formatiranjem Datoteke
**Problem:** Formatiranje prevedenog dokumenta nije ispravno. Ovo se može dogoditi u tablicama, ovdje dodatni ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` će riješiti probleme s tablicama.

**Koraci:**
1. Otvorite prevedeni dokument.
2. Usporedite ga s izvornim dokumentom kako biste identificirali probleme s formatiranjem.
3. Prilagodite formatiranje da odgovara izvornom dokumentu.
4. Spremite promjene.

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazumevanja ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.