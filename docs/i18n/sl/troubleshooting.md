# Odpravljanje težav

Uporabite to stran, ko prevodno izvajanje nepričakovano uspe, se med konfiguracijo zruši ali ustvari izhod, ki potrebuje pregled.

## Začni tukaj

1. Najprej zaženite osredotočen ukaz, na primer `translate -l "ko" -md`.
2. Dodajte `-d` za debug izpis v konzoli.
3. Dodajte `-s` za shranjevanje debug zapisov v `<root-dir>/logs/`.
4. Po prevodu zaženite `co-op-review`, da preverite svežino, strukturo in lokalne povezave.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Napake konfiguracije

### Ni ponudnika jezikovnega modela

Napaka:

```text
No language model configuration found.
```

Rešitev:

- Konfigurirajte Azure OpenAI ali OpenAI.
- Preverite, da so spremenljivke v okolju, kjer se ukaz izvaja.
- Za lokalno uporabo jih shranite v `.env` v korenu projekta.

Oglejte si [Konfiguracija](configuration.md).

### Prevodi slik brez Azure AI Vision

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

- Potrdite, da ključ pripada isti Azure storitvi kot končna točka.
- Potrdite, da storitev podpira Vision, ko uporabljate `-img`.
- Potrdite, da ime nameščenja Azure OpenAI in različica API ustrezata vaši nameščeni instanci.
- Zaženite z debug zapisi: `translate -l "ko" -md -d -s`.

## Nobene datoteke niso bile prevedene

Pogosti vzroki:

- Izbrane zastavice (flags) ne ustrezajo vašim datotekam.
- Prevedene datoteke že obstajajo.
- Izvorne datoteke so v izključenih imenikih.
- Ukaz se izvaja iz napačnega korena projekta.

Preverite:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Uporabite `--root-dir`, ko je ukaz zagnan zunaj korena projekta.

## Nepričakovano vedenje povezav

Prepisovanje povezav je odvisno od izbranih vrst vsebin:

- `-nb` vključeno: povezave do zvezkov (notebook) lahko kažejo na prevedene zvezke.
- `-nb` izključeno: povezave do zvezkov lahko ostanejo usmerjene na izvorne zvezke.
- `-img` vključeno: povezave do slik lahko kažejo na prevedene slike.
- `-img` izključeno: povezave do slik lahko ostanejo usmerjene na izvorne slike.

Zaženite popoln prevod vsebine, kadar naj vse notranje povezave raje kažejo na prevedene izhodne vsebine:

```bash
translate -l "ko" -md -nb -img
```

Po prevodu zaženite pregled povezav:

```bash
co-op-review -l "ko"
```

## Težave pri upodabljanju Markdowna

Če prevedeni Markdown ni pravilno upodobljen:

- Preverite, da frontmatter začne in konča z `---`.
- Preverite, da se število ograj za kodo (code fences) ujema med izvorno in prevedeno datoteko.
- Zaženite `co-op-review`, da zajamete pogoste strukturne težave.
- Ponovno prevedite določeno datoteko, če je bil izhod poškodovan.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action se je zagnal, vendar ni bila ustvarjena pull request

Če `peter-evans/create-pull-request` poroča, da veja ni pred osnovno, to pomeni, da delovni tok ni našel nobenih datotek za commit.

Verjetni vzroki:

- Prevodno izvajanje ni ustvarilo nobenih sprememb.
- `.gitignore` izključuje `translations/`, `translated_images/` ali prevedene zvezke.
- `add-paths` se ne ujema z ustvarjenimi izhodnimi imeniki.
- Korak prevajanja se je predčasno zaključil.

Rešitve:

1. Potrdite, da ustvarjene datoteke obstajajo v `translations/` ali `translated_images/`.
2. Potrdite, da `.gitignore` ne ignorira ustvarjenih izhodov.
3. Uporabite ujemajoče se `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Zaradi testiranja začasno dodajte debug zastavice (flags) ukazu translate:

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

Strojni prevodi lahko potrebujejo človeški pregled. Uporabite `evaluate` le, ko želite eksperimentalno ocenjevanje kakovosti in delovne tokove popravil z nizko zanesljivostjo.

!!! warning "Experimental"
    `evaluate` lahko uporablja preverjanja na osnovi pravil in LLM, njegovo modeliranje ocenjevanja in vedenje metapodatkov pa se lahko spremenita. Ne vključujte ga v obvezne CI-preverke, razen če je vaš delovni tok pripravljen na spremembe.

Za deterministične CI-preverjanja namesto tega uporabite `co-op-review`.