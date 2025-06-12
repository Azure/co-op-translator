<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:31:10+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "sr"
}
-->
# Microsoft Co-op Translator Vodič za rešavanje problema

## Pregled
Microsoft Co-Op Translator je moćan alat za besprekornu prevodjenje Markdown dokumenata. Ovaj vodič će vam pomoći da rešite uobičajene probleme koji se javljaju prilikom korišćenja ovog alata.

## Česti problemi i rešenja

### 1. Problem sa Markdown tagom
**Problem:** Prevedeni Markdown dokument sadrži `markdown` tag na vrhu, što izaziva probleme pri prikazu.

**Rešenje:** Da biste to rešili, jednostavno obrišite `markdown` tag na vrhu fajla. To će omogućiti ispravan prikaz Markdown fajla.

**Koraci:**
1. Otvorite prevedeni Markdown (`.md`) fajl.
2. Pronađite `markdown` tag na vrhu dokumenta.
3. Obrišite `markdown` tag.
4. Sačuvajte izmene u fajlu.
5. Ponovo otvorite fajl da biste proverili da li se pravilno prikazuje.

### 2. Problem sa URL-ovima ugrađenih slika
**Problem:** URL-ovi ugrađenih slika ne odgovaraju jezičkoj lokalizaciji, što dovodi do nepravilnih ili nedostajućih slika.

**Rešenje:** Proverite URL-ove ugrađenih slika i uverite se da odgovaraju jezičkoj lokalizaciji. Sve slike se nalaze u `translated_images` folderu, a svaka slika u nazivu fajla ima oznaku jezičke lokalizacije.

**Koraci:**
1. Otvorite prevedeni Markdown dokument.
2. Identifikujte ugrađene slike i njihove URL-ove.
3. Proverite da li jezička lokalizacija u nazivu slike odgovara jeziku dokumenta.
4. Ažurirajte URL-ove ako je potrebno.
5. Sačuvajte izmene i ponovo otvorite dokument da potvrdite da se slike pravilno prikazuju.

### 3. Tačnost prevoda
**Problem:** Prevedeni sadržaj nije tačan ili zahteva dodatne izmene.

**Rešenje:** Pregledajte prevedeni dokument i izvršite neophodne izmene kako biste poboljšali tačnost i čitljivost.

**Koraci:**
1. Otvorite prevedeni dokument.
2. Pažljivo pregledajte sadržaj.
3. Napravite potrebne izmene za poboljšanje tačnosti prevoda.
4. Sačuvajte izmene.

### 4. Problemi sa formatiranjem fajla
**Problem:** Formatiranje prevedenog dokumenta nije ispravno. Ovo se može desiti kod tabela, ovde dodatni ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` će rešiti probleme sa tabelama.

**Koraci:**
1. Otvorite prevedeni dokument.
2. Uporedite ga sa originalnim dokumentom da biste identifikovali probleme sa formatiranjem.
3. Prilagodite formatiranje da odgovara originalnom dokumentu.
4. Sačuvajte izmene.

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде прецизан, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која могу настати употребом овог превода.