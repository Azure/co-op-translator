<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T04:09:32+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "sl"
}
-->
# Microsoft Co-op Translator Navodila za odpravljanje težav

## Pregled
Microsoft Co-Op Translator je zmogljivo orodje za brezhibno prevajanje Markdown dokumentov. Ta vodič vam bo pomagal odpraviti pogoste težave, na katere lahko naletite pri uporabi orodja.

## Pogoste težave in rešitve

### 1. Težava z Markdown oznako
**Težava:** Preveden Markdown dokument vsebuje oznako `markdown` na vrhu, kar povzroča težave pri prikazu.

**Rešitev:** Preprosto izbrišite oznako `markdown` na vrhu datoteke. Tako se bo Markdown datoteka pravilno prikazala.

**Koraki:**
1. Odprite prevedeno Markdown (`.md`) datoteko.
2. Poiščite oznako `markdown` na vrhu dokumenta.
3. Izbrišite oznako `markdown`.
4. Shranite spremembe v datoteko.
5. Ponovno odprite datoteko in preverite, ali se pravilno prikazuje.

### 2. Težava z URL-ji vdelanih slik
**Težava:** URL-ji vdelanih slik ne ustrezajo jezikovni lokalizaciji, kar vodi do napačnih ali manjkajočih slik.

**Rešitev:** Preverite URL-je vdelanih slik in zagotovite, da ustrezajo jezikovni lokalizaciji. Vse slike se nahajajo v mapi `translated_images`, vsaka slika ima oznako jezikovne lokalizacije v imenu datoteke.

**Koraki:**
1. Odprite preveden Markdown dokument.
2. Prepoznajte vdelane slike in njihove URL-je.
3. Preverite, ali oznaka jezikovne lokalizacije v imenu slike ustreza jeziku dokumenta.
4. Po potrebi posodobite URL-je.
5. Shranite spremembe in ponovno odprite dokument, da preverite, ali se slike pravilno prikazujejo.

### 3. Natančnost prevoda
**Težava:** Prevedena vsebina ni natančna ali zahteva dodatne popravke.

**Rešitev:** Preglejte preveden dokument in po potrebi uredite besedilo za boljšo natančnost in berljivost.

**Koraki:**
1. Odprite preveden dokument.
2. Natančno preglejte vsebino.
3. Po potrebi uredite besedilo za boljši prevod.
4. Shranite spremembe.

## 4. Napaka z dovoljenji Redacted ali 404

Če slike ali besedilo niso prevedeni v pravi jezik in pri zagonu v načinu -d debug prejmete napako 401, gre za klasično napako pri avtentikaciji – ključ je neveljaven, potekel ali ni povezan s pravilno regijo končne točke.

Za boljše razumevanje vzroka za napako zaženite co-op translator z [-d debug stikalom](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md).

- **Sporočilo o napaki**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Možni vzroki**:
  - Naročniški ključ je bil odstranjen ali napačen v zahtevi.
  - Ključ za AI Services ali naročniški ključ pripada drugemu Azure viru (npr. Translator ali OpenAI) namesto **Azure AI Vision** vira.

 **Vrsta vira**
  - Obiščite [Azure Portal](https://portal.azure.com) ali [Azure AI Foundry](https://ai.azure.com) in preverite, da je vir tipa `Azure AI services` → `Vision`.
  - Preverite ključe in zagotovite, da uporabljate pravi ključ.

## 5. Napake v konfiguraciji (novo ravnanje z napakami)

Z novim sistemom selektivnega prevajanja Co-op Translator zdaj izpiše jasna sporočila o napakah, če zahtevane storitve niso nastavljene.

### 5.1. Azure AI Service ni nastavljen za prevajanje slik

**Težava:** Zahtevali ste prevajanje slik (z zastavico `-img`), vendar Azure AI Service ni pravilno nastavljen.

**Sporočilo o napaki:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Rešitev:**
1. **Možnost 1**: Nastavite Azure AI Service
   - Dodajte `AZURE_AI_SERVICE_API_KEY` v vašo `.env` datoteko
   - Dodajte `AZURE_AI_SERVICE_ENDPOINT` v vašo `.env` datoteko
   - Preverite, da je storitev dostopna

2. **Možnost 2**: Odstranite zahtevo za prevajanje slik
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Manjkajoča zahtevana konfiguracija

**Težava:** Manjka osnovna konfiguracija LLM.

**Sporočilo o napaki:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Rešitev:**
1. Preverite, da vaša `.env` datoteka vsebuje vsaj eno od naslednjih LLM konfiguracij:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` in `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Potrebujete bodisi Azure OpenAI ALI OpenAI, ne obeh.

### 5.3. Zmeda pri selektivnem prevajanju

**Težava:** Nobena datoteka ni bila prevedena, čeprav je ukaz uspel.

**Možni vzroki:**
- Napačne zastavice za tipe datotek (`-md`, `-img`, `-nb`)
- V projektu ni ustreznih datotek
- Napačna struktura map

**Rešitev:**
1. **Uporabite debug način** za vpogled v dogajanje:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Preverite tipe datotek** v vašem projektu:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Preverite kombinacije zastavic**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migracija iz starega sistema

### 6.1. Način samo za Markdown ni več podprt

**Težava:** Ukazi, ki so se zanašali na samodejni preklop v način samo za Markdown, ne delujejo več kot prej.

**Staro obnašanje:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Novo obnašanje:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Rešitev:**
- **Bodite natančni** glede tega, kaj želite prevesti:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Nepričakovano obnašanje povezav

**Težava:** Povezave v prevedenih datotekah vodijo na nepričakovane lokacije.

**Vzrok:** Dinamična obdelava povezav se spreminja glede na izbrane tipe datotek.

**Rešitev:**
1. **Razumite novo obnašanje povezav**:
   - vključeno `-nb`: Povezave na zvezke vodijo na prevedene različice
   - izključeno `-nb`: Povezave na zvezke vodijo na izvirne datoteke
   - vključeno `-img`: Povezave na slike vodijo na prevedene slike
   - izključeno `-img`: Povezave na slike vodijo na izvirne slike

2. **Izberite pravo kombinacijo** za vaš primer uporabe:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action se je izvedel, a Pull Request (PR) ni bil ustvarjen

**Simptom:** Dnevnik poteka dela za `peter-evans/create-pull-request` prikaže:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Verjetni vzroki:**
- **Ni zaznanih sprememb:** Prevajalni korak ni povzročil razlik (repozitorij je že posodobljen).
- **Prezrti izhodi:** `.gitignore` izključuje datoteke, ki jih želite poslati (npr. `*.ipynb`, `translations/`, `translated_images/`).
- **Neskladje add-paths:** Poti, podane akciji, se ne ujemajo z dejanskimi izhodi.
- **Logika/pravila poteka dela:** Prevajalni korak se je končal prezgodaj ali je pisal v nepričakovane mape.

**Kako popraviti / preveriti:**
1. **Preverite, ali izhodi obstajajo:** Po prevajanju preverite, ali so v delovnem prostoru nove/spremenjene datoteke v `translations/` in/ali `translated_images/`.
   - Če prevajate zvezke, preverite, ali so `.ipynb` datoteke zapisane pod `translations/<lang>/...`.
2. **Preglejte `.gitignore`:** Ne ignorirajte generiranih izhodov. Prepričajte se, da NE ignorirate:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (če prevajate zvezke)
3. **Preverite, da add-paths ustreza izhodom:** Uporabite večvrstično vrednost in vključite obe mapi, če je potrebno:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Začasno prisilite PR za odpravljanje napak:** Dovolite prazne commite, da preverite, ali je povezava pravilna:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Zaženite z debug:** Dodajte `-d` ukazu za prevajanje, da izpišete, katere datoteke so bile odkrite in zapisane.
6. **Dovoljenja (GITHUB_TOKEN):** Preverite, da ima potek dela pravice za pisanje commitov in PR-jev:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Hiter kontrolni seznam za odpravljanje napak

Pri odpravljanju težav s prevajanjem:

1. **Uporabite debug način**: Dodajte zastavico `-d` za podrobne dnevnike
2. **Preverite zastavice**: Preverite, da `-md`, `-img`, `-nb` ustrezajo vašim željam
3. **Preverite konfiguracijo**: Preverite, da vaša `.env` datoteka vsebuje zahtevane ključe
4. **Testirajte postopoma**: Začnite samo z `-md`, nato dodajte druge tipe
5. **Preverite strukturo datotek**: Preverite, da izvorne datoteke obstajajo in so dostopne

Za več informacij o razpoložljivih ukazih in zastavicah glejte [Command Reference](./command-reference.md).

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden s pomočjo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvoru jeziku naj velja za avtoritativni vir. Za ključne informacije priporočamo strokoven človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.