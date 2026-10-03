# Odpravljanje težav

Uporabite to stran, kadar prevod teče nepričakovano uspešno, med konfiguracijo ne uspe ali ustvari izhod, ki potrebuje pregled.

## Začnite tukaj

1. Najprej zaženite osredotočen ukaz, na primer `translate -l "ko" -md`.
2. Dodajte `-d` za izpis debug sporočil v konzoli.
3. Dodajte `-s` za shranjevanje debug zapisov v `<root-dir>/logs/`.
4. Po prevodu zaženite `co-op-review`, da preverite ažurnost, strukturo in lokalne povezave.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfiguracijske napake

### Ni ponudnika jezikovnega modela

Napaka:

```text
No language model configuration found.
```

Rešitev:

- Konfigurirajte Azure OpenAI, OpenAI ali Anthropic.
- Preverite, da so spremenljivke v okolju, kjer se ukaz izvaja.
- Za lokalno uporabo jih postavite v `.env` v korenu projekta.

Oglejte si [Konfiguracija](configuration.md).

### Prevajanje slik brez Azure AI Vision

Napaka:

```text
Image translation requested but Azure AI Service is not configured.
```

Rešitev:

- Dodajte `AZURE_AI_SERVICE_API_KEY`.
- Dodajte `AZURE_AI_SERVICE_ENDPOINT`.
- Ali zaženite ukaz samo za besedilo, na primer `translate -l "ko" -md`.

### Neveljaven ključ ali končna točka

Simptomi lahko vključujejo `401`, napake dovoljenj z zamegljenimi podatki ali napake pri dostopu do končne točke.

Rešitev:

- Potrdite, da ključ pripada istemu Azure viru kot končna točka.
- Potrdite, da vir podpira Vision, če uporabljate `-img`.
- Potrdite, da se ime namestitve Azure OpenAI in različica API ujemata z vašo namestitvijo.
- Zaženite z debug zapisi: `translate -l "ko" -md -d -s`.

## Nobene datoteke niso bile prevedene

Pogosti vzroki:

- Izbrani parametri ne ustrezajo vašim datotekam.
- Obstajajo že prevedene datoteke.
- Izvorne datoteke so v izključenih imenikih.
- Ukaz se izvaja iz napačnega korena projekta.

Preverite:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Uporabite `--root-dir`, kadar se ukaz izvaja zunaj korena projekta.

## Nepričakovano vedenje povezav

Prepisovanje povezav je odvisno od izbranih vrst vsebine:

- `-nb` vključen: povezave do zvezkov lahko kažejo na prevedene zvezke.
- `-nb` izključen: povezave do zvezkov lahko ostanejo usmerjene na izvorne zvezke.
- `-img` vključen: povezave do slik lahko kažejo na prevedene slike.
- `-img` izključen: povezave do slik lahko ostanejo usmerjene na izvorne slike.

Zaženite celovit prevod vsebine, kadar naj vse notranje povezave dajejo prednost prevedenim izhodom:

```bash
translate -l "ko" -md -nb -img
```

Po prevodu zaženite pregled povezav:

```bash
co-op-review -l "ko"
```

## Težave pri upodabljanju Markdowna

Če se prevedeni Markdown prikaže nepravilno:

- Preverite, da frontmatter začne in konča z `---`.
- Preverite, da se število ograj za kodo ujema med izvorno in prevedeno datoteko.
- Zaženite `co-op-review`, da odkrijete pogoste strukturne težave.
- Ponovno prevedite specifično datoteko, če je bil izhod poškodovan.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action se je zagnal, vendar ni bil ustvarjen Pull Request

Če `peter-evans/create-pull-request` poroča, da veja ni pred osnovno vejo, delovni tok ni našel nobenih datotek za potrditev.

Verjetni vzroki:

- Prevajanje ni ustvarilo sprememb.
- `.gitignore` izključuje `translations/`, `translated_images/` ali prevedene zvezke.
- `add-paths` se ne ujema z generiranimi izhodnimi imeniki.
- Korak prevajanja je končal prezgodaj.

Rešitve:

1. Potrdite, da generirane datoteke obstajajo v `translations/` ali `translated_images/`.
2. Preverite, da `.gitignore` ne ignorira generiranih izhodov.
3. Uporabite ujemajoče se `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Začasno dodajte debug zastavice ukazu `translate`:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Potrdite, da dovoljenja delovnega toka vključujejo:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kakovost prevoda

Strojni prevodi lahko potrebujejo človeški pregled. `evaluate` uporabljajte le, kadar želite eksperimentalno ocenjevanje kakovosti in delovne tokove popravil za nizko zaupanje.

!!! warning "Eksperimentalno"
    `evaluate` lahko uporablja preverjanja, temelječa na pravilih in LLM, njegovo ocenjevalno modeliranje in obnašanje metapodatkov pa se lahko spremenita. Ne vključujte ga v obvezne CI prehode, razen če je vaš delovni tok pripravljen na spremembe.

Za deterministične CI preverjanja raje uporabite `co-op-review`.