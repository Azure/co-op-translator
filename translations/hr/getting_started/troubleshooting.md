<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T04:06:30+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "hr"
}
-->
# Microsoft Co-op Translator Vodič za rješavanje problema

## Pregled
Microsoft Co-Op Translator je moćan alat za besprijekoran prijevod Markdown dokumenata. Ovaj vodič pomoći će vam riješiti najčešće probleme na koje možete naići prilikom korištenja alata.

## Najčešći problemi i rješenja

### 1. Problem s Markdown oznakom
**Problem:** Prevedeni Markdown dokument sadrži `markdown` oznaku na vrhu, što uzrokuje probleme s prikazom.

**Rješenje:** Da biste to riješili, jednostavno izbrišite `markdown` oznaku s vrha datoteke. Nakon toga će se Markdown datoteka ispravno prikazivati.

**Koraci:**
1. Otvorite prevedenu Markdown (`.md`) datoteku.
2. Pronađite `markdown` oznaku na vrhu dokumenta.
3. Izbrišite tu oznaku.
4. Spremite promjene u datoteci.
5. Ponovno otvorite datoteku i provjerite prikazuje li se ispravno.

### 2. Problem s URL-om ugrađenih slika
**Problem:** URL-ovi ugrađenih slika ne odgovaraju jezičnoj lokalizaciji, što dovodi do pogrešnih ili nedostajućih slika.

**Rješenje:** Provjerite URL-ove ugrađenih slika i osigurajte da odgovaraju jezičnoj lokalizaciji. Sve slike se nalaze u mapi `translated_images`, a svaka slika ima oznaku jezika u nazivu datoteke.

**Koraci:**
1. Otvorite prevedeni Markdown dokument.
2. Pronađite ugrađene slike i njihove URL-ove.
3. Provjerite odgovara li oznaka jezika u nazivu slike jeziku dokumenta.
4. Po potrebi ažurirajte URL-ove.
5. Spremite promjene i ponovno otvorite dokument kako biste provjerili prikazuju li se slike ispravno.

### 3. Točnost prijevoda
**Problem:** Prijevod nije dovoljno točan ili zahtijeva dodatne izmjene.

**Rješenje:** Pregledajte prevedeni dokument i napravite potrebne izmjene radi bolje točnosti i čitljivosti.

**Koraci:**
1. Otvorite prevedeni dokument.
2. Pažljivo pregledajte sadržaj.
3. Izmijenite dijelove koji zahtijevaju poboljšanje prijevoda.
4. Spremite promjene.

## 4. Dozvola odbijena ili 404

Ako slike ili tekst nisu prevedeni na ispravan jezik i u -d debug načinu rada dobijete 401 grešku, radi se o klasičnom problemu s autentikacijom—ključ je nevažeći, istekao je ili nije povezan s regijom endpointa.

Pokrenite co-op translator s [-d debug switch](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) za detaljnije informacije o uzroku problema.

- **Poruka o grešci**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Mogući uzroci**:
  - Subscription key je redaktiran ili netočan u zahtjevu.
  - AI Services Key ili Subscription Key pripada drugom Azure resursu (npr. Translator ili OpenAI) umjesto **Azure AI Vision** resursa.

 **Vrsta resursa**
  - Idite na [Azure Portal](https://portal.azure.com) ili [Azure AI Foundry](https://ai.azure.com) i provjerite je li resurs tipa `Azure AI services` → `Vision`.
  - Provjerite ključeve i osigurajte da koristite ispravan ključ.

## 5. Konfiguracijske greške (Novo rukovanje greškama)

S novim sustavom selektivnog prevođenja, Co-op Translator sada daje jasne poruke o greškama kad potrebne usluge nisu konfigurirane.

### 5.1. Azure AI Service nije konfiguriran za prijevod slika

**Problem:** Zatražili ste prijevod slika (`-img` zastavica), ali Azure AI Service nije ispravno konfiguriran.

**Poruka o grešci:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Rješenje:**
1. **Opcija 1**: Konfigurirajte Azure AI Service
   - Dodajte `AZURE_AI_SERVICE_API_KEY` u vašu `.env` datoteku
   - Dodajte `AZURE_AI_SERVICE_ENDPOINT` u vašu `.env` datoteku
   - Provjerite je li usluga dostupna

2. **Opcija 2**: Uklonite zahtjev za prijevod slika
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Nedostaje potrebna konfiguracija

**Problem:** Nedostaje osnovna LLM konfiguracija.

**Poruka o grešci:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Rješenje:**
1. Provjerite da vaša `.env` datoteka sadrži barem jednu od sljedećih LLM konfiguracija:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` i `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Potrebno je konfigurirati ili Azure OpenAI ILI OpenAI, ne oba.

### 5.3. Zbunjenost oko selektivnog prevođenja

**Problem:** Nijedna datoteka nije prevedena iako je naredba uspješno izvršena.

**Mogući uzroci:**
- Pogrešne zastavice za tip datoteke (`-md`, `-img`, `-nb`)
- Nema odgovarajućih datoteka u projektu
- Pogrešna struktura direktorija

**Rješenje:**
1. **Koristite debug način** za uvid u procese:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Provjerite tipove datoteka** u projektu:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Provjerite kombinacije zastavica**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migracija sa starog sustava

### 6.1. Markdown-only način više nije podržan

**Problem:** Naredbe koje su se oslanjale na automatski markdown-only fallback više ne rade kao prije.

**Staro ponašanje:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Novo ponašanje:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Rješenje:**
- **Budite eksplicitni** oko onoga što želite prevesti:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Neočekivano ponašanje linkova

**Problem:** Linkovi u prevedenim datotekama vode na neočekivane lokacije.

**Uzrok:** Dinamička obrada linkova mijenja se ovisno o odabranim tipovima datoteka.

**Rješenje:**
1. **Razumite novo ponašanje linkova**:
   - `-nb` uključeno: Linkovi na noteboocima vode na prevedene verzije
   - `-nb` isključeno: Linkovi na noteboocima vode na originalne datoteke
   - `-img` uključeno: Linkovi na slike vode na prevedene verzije
   - `-img` isključeno: Linkovi na slike vode na originalne datoteke

2. **Odaberite pravu kombinaciju** za svoj slučaj:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action je prošao, ali nije kreiran Pull Request (PR)

**Simptom:** U workflow logovima za `peter-evans/create-pull-request` piše:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Mogući uzroci:**
- **Nema promjena:** Korak prevođenja nije proizveo razlike (repo je već ažuriran).
- **Ignorirani outputi:** `.gitignore` isključuje datoteke koje očekujete da budu commitane (npr. `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths ne odgovara outputima:** Putanje navedene u akciji ne odgovaraju stvarnim lokacijama outputa.
- **Logika/uvjeti workflowa:** Korak prevođenja je završio ranije ili je zapisivao u neočekivane direktorije.

**Kako popraviti / provjeriti:**
1. **Provjerite postoje li outputi:** Nakon prevođenja, provjerite ima li novih/promijenjenih datoteka u `translations/` i/ili `translated_images/`.
   - Ako prevodite notebooke, provjerite jesu li `.ipynb` datoteke zapisane pod `translations/<lang>/...`.
2. **Pregledajte `.gitignore`:** Nemojte ignorirati generirane outpute. Provjerite da NE ignorirate:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (ako prevodite notebooke)
3. **Provjerite da add-paths odgovara outputima:** Koristite višerednu vrijednost i uključite obje mape ako je potrebno:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Prisilite PR radi debugiranja:** Privremeno dopustite prazne commitove kako biste provjerili je li povezivanje ispravno:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Pokrenite s debugom:** Dodajte `-d` u naredbu za prevođenje kako biste vidjeli koje su datoteke pronađene i zapisane.
6. **Dozvole (GITHUB_TOKEN):** Provjerite ima li workflow dozvole za pisanje commitova i PR-ova:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Brzi popis za debugiranje

Kod rješavanja problema s prevođenjem:

1. **Koristite debug način:** Dodajte `-d` zastavicu za detaljne logove
2. **Provjerite zastavice:** Osigurajte da `-md`, `-img`, `-nb` odgovaraju vašoj namjeri
3. **Provjerite konfiguraciju:** Provjerite ima li vaša `.env` datoteka potrebne ključeve
4. **Testirajte postupno:** Krenite samo s `-md`, pa dodajte ostale tipove
5. **Provjerite strukturu datoteka:** Provjerite postoje li izvorne datoteke i jesu li dostupne

Za više informacija o dostupnim naredbama i zastavicama pogledajte [Command Reference](./command-reference.md).

---

**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na svom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.