# Rješavanje problema

Upotrijebite ovu stranicu kada pokušaj prevođenja neočekivano uspije, zakaže tijekom konfiguracije ili proizvede izlaz koji treba pregledati.

## Počnite ovdje

1. Pokrenite prvo fokusiranu naredbu, kao što je `translate -l "ko" -md`.
2. Dodajte `-d` za debug zapise u konzoli.
3. Dodajte `-s` za spremanje debug zapisa u `<root-dir>/logs/`.
4. Pokrenite `co-op-review` nakon prevođenja kako biste provjerili svježinu, strukturu i lokalne veze.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Pogreške konfiguracije

### Nema pružatelja jezičnog modela

Pogreška:

```text
No language model configuration found.
```

Rješenje:

- Konfigurirajte Azure OpenAI, OpenAI ili Anthropic.
- Provjerite jesu li varijable u okruženju u kojem se naredba izvršava.
- Za lokalno korištenje, stavite ih u `.env` u korijenu projekta.

Vidi [Konfiguracija](configuration.md).

### Prevođenje slika bez Azure AI Vision

Pogreška:

```text
Image translation requested but Azure AI Service is not configured.
```

Rješenje:

- Dodajte `AZURE_AI_SERVICE_API_KEY`.
- Dodajte `AZURE_AI_SERVICE_ENDPOINT`.
- Ili pokrenite naredbu samo za tekst, kao što je `translate -l "ko" -md`.

### Neispravan ključ ili endpoint

Simptomi mogu uključivati `401`, pogreške dopuštenja s prikrivenim podacima ili pogreške pristupa endpointu.

Rješenje:

- Potvrdite da ključ pripada istom Azure resursu kao i endpointu.
- Potvrdite da resurs podržava Vision kada koristite `-img`.
- Potvrdite da naziv Azure OpenAI deploymenta i verzija API-ja odgovaraju vašoj implementaciji.
- Pokrenite s debug zapisima: `translate -l "ko" -md -d -s`.

## Niti jedna datoteka nije prevedena

Uobičajeni uzroci:

- Odabrane opcije ne odgovaraju vašim datotekama.
- Već postoje prevedene datoteke.
- Izvorne datoteke su u isključenim direktorijima.
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

- `-nb` uključen: poveznice na bilježnice mogu voditi na prevedene bilježnice.
- `-nb` isključen: poveznice na bilježnice mogu ostati usmjerene na izvorne bilježnice.
- `-img` uključen: poveznice na slike mogu voditi na prevedene slike.
- `-img` isključen: poveznice na slike mogu ostati usmjerene na izvorne slike.

Pokrenite potpuno prevođenje sadržaja kada sve interne poveznice trebaju preferirati prevedene izlaze:

```bash
translate -l "ko" -md -nb -img
```

Pokrenite pregled poveznica nakon prevođenja:

```bash
co-op-review -l "ko"
```

## Problemi s prikazom Markdowna

Ako se prevedeni Markdown ne prikazuje ispravno:

- Provjerite da frontmatter počinje i završava s `---`.
- Provjerite da se brojevi code fence oznaka podudaraju između izvornika i prevedenih datoteka.
- Pokrenite `co-op-review` kako biste uočili uobičajene probleme sa strukturom.
- Ponovno prevedite određenu datoteku ako je izlaz oštećen.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action je pokrenut, ali nije stvoren Pull Request

Ako `peter-evans/create-pull-request` prijavi da grana nije ispred baze, radni tijek nije pronašao datoteke za commit.

Vjerojatni uzroci:

- Pokušaj prevođenja nije proizveo promjene.
- `.gitignore` isključuje `translations/`, `translated_images/` ili prevedene bilježnice.
- `add-paths` ne odgovara generiranim izlaznim direktorijima.
- Korak prevođenja je prerano završio.

Rješenja:

1. Potvrdite da generirane datoteke postoje u `translations/` ili `translated_images/`.
2. Potvrdite da `.gitignore` ne isključuje generirane izlaze.
3. Koristite odgovarajući `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Privremeno dodajte debug zastavice naredbi za prevođenje:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Potvrdite da dopuštenja workflowa uključuju:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kvaliteta prijevoda

Strojni prijevodi mogu zahtijevati ljudski pregled. Upotrijebite `evaluate` samo kada želite eksperimentalno ocjenjivanje kvalitete i radne tokove za popravak niske pouzdanosti.

!!! warning "Experimental"
    `evaluate` može koristiti provjeru baziranu na pravilima i LLM-u, a njegov model ocjenjivanja i ponašanje metapodataka mogu se promijeniti. Izbjegavajte ga u obveznim CI provjerama osim ako je vaš radni tijek pripremljen na promjene.

Za determinističke CI provjere, umjesto toga upotrijebite `co-op-review`.