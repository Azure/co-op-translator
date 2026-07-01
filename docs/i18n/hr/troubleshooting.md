# Rješavanje problema

Koristite ovu stranicu kada pokretanje prijevoda neočekivano uspije, ne uspije tijekom konfiguracije ili proizvede izlaz koji treba pregledati.

## Počnite ovdje

1. Prvo pokrenite fokusiranu naredbu, na primjer `translate -l "ko" -md`.
2. Dodajte `-d` za debug zapisnike konzole.
3. Dodajte `-s` da biste spremili debug zapisnike u `<root-dir>/logs/`.
4. Pokrenite `co-op-review` nakon prijevoda kako biste provjerili ažurnost, strukturu i lokalne poveznice.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Pogreške konfiguracije

### Nema pružatelja modela jezika

Pogreška:

```text
No language model configuration found.
```

Rješenje:

- Konfigurirajte Azure OpenAI ili OpenAI.
- Provjerite jesu li varijable u okruženju u kojem se naredba pokreće.
- Za lokalnu upotrebu stavite ih u `.env` u korijenu projekta.

Pogledajte [Konfiguracija](configuration.md).

### Prevođenje slika bez Azure AI Vision

Pogreška:

```text
Image translation requested but Azure AI Service is not configured.
```

Rješenje:

- Dodajte `AZURE_AI_SERVICE_API_KEY`.
- Dodajte `AZURE_AI_SERVICE_ENDPOINT`.
- Ili pokrenite naredbu samo za tekst, kao `translate -l "ko" -md`.

### Nevažeći ključ ili krajnja točka

Simptomi mogu uključivati `401`, prikrivene pogreške dopuštenja ili pogreške pristupa krajnjoj točki.

Rješenje:

- Potvrdite da ključ pripada istom Azure resursu kao i krajnja točka.
- Potvrdite da resurs podržava Vision pri korištenju `-img`.
- Potvrdite da ime Azure OpenAI deploymenta i verzija API-ja odgovaraju vašem deploymentu.
- Pokrenite s debug zapisnicima: `translate -l "ko" -md -d -s`.

## Nijedna datoteka nije prevedena

Uobičajeni uzroci:

- Odabrani parametri (flags) ne odgovaraju vašim datotekama.
- Već postoje prevedene datoteke.
- Izvorne datoteke nalaze se u izuzetim direktorijima.
- Naredba se pokreće iz pogrešnog korijena projekta.

Provjere:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Upotrijebite `--root-dir` kada se naredba pokreće izvan korijena projekta.

## Neočekivano ponašanje poveznica

Prepisivanje poveznica ovisi o odabranim vrstama sadržaja:

- `-nb` uključen: poveznice na bilježnice mogu upućivati na prevedene bilježnice.
- `-nb` isključen: poveznice na bilježnice mogu ostati usmjerene na izvorne bilježnice.
- `-img` uključen: poveznice na slike mogu pokazivati na prevedene slike.
- `-img` isključen: poveznice na slike mogu ostati usmjerene na izvorne slike.

Pokrenite potpuni prijevod sadržaja kada sve interne poveznice trebaju preferirati prevedene rezultate:

```bash
translate -l "ko" -md -nb -img
```

Pokrenite pregled poveznica nakon prijevoda:

```bash
co-op-review -l "ko"
```

## Problemi s prikazom Markdowna

Ako prevedeni Markdown nije ispravno prikazan:

- Provjerite počinje li i završava li frontmatter s `---`.
- Provjerite odgovaraju li brojevi ograda koda (code fences) između izvornih i prevedenih datoteka.
- Pokrenite `co-op-review` kako biste uhvatili uobičajene strukturne pogreške.
- Ponovno prevedite određenu datoteku ako je izlaz oštećen.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action je pokrenut, ali nije stvoren Pull Request

Ako `peter-evans/create-pull-request` prijavi da grana nije ispred baze, workflow nije pronašao datoteke za commit.

Vjerojatni uzroci:

- Pokretanje prijevoda nije proizvelo promjene.
- `.gitignore` isključuje `translations/`, `translated_images/` ili prevedene bilježnice.
- `add-paths` ne odgovara generiranim izlaznim direktorijima.
- Korak prijevoda je prerano završio.

Rješenja:

1. Potvrdite da generirane datoteke postoje u `translations/` ili `translated_images/`.
2. Potvrdite da `.gitignore` ne ignorira generirane izlaze.
3. Koristite odgovarajući `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Privremeno dodajte debug zastavice u naredbu za prijevod:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Potvrdite da dozvole workflowa uključuju:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kvaliteta prijevoda

Strojni prijevodi mogu zahtijevati ljudski pregled. Koristite `evaluate` samo kada želite eksperimentalno ocjenjivanje kvalitete i postupke popravka za nisku pouzdanost.

!!! warning "Eksperimentalno"
    `evaluate` može koristiti provjere temeljene na pravilima i provjere temeljene na LLM-u, a njegov model bodovanja i ponašanje metapodataka mogu se promijeniti. Ne uključujte ga u obvezne CI provjere osim ako vaš workflow nije pripremljen na promjene.

Za determinističke CI provjere umjesto toga koristite `co-op-review`.