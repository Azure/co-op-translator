# Hibakeresés

Használja ezt az oldalt, ha egy fordítási futás váratlanul sikeres, konfiguráció közben hibát jelez, vagy olyan kimenetet hoz, amely felülvizsgálatot igényel.

## Kezdje itt

1. Futtasson először egy konkrét parancsot, például `translate -l "ko" -md`.
2. Adja hozzá a `-d` kapcsolót a konzol hibakeresési naplókhoz.
3. Adja hozzá a `-s` kapcsolót a hibakeresési naplók mentéséhez a `<root-dir>/logs/` alá.
4. Futtassa a `co-op-review`-t a fordítás után, hogy ellenőrizze a frissességet, a struktúrát és a helyi hivatkozásokat.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfigurációs hibák

### Nyelvi modell szolgáltató hiányzik

Hiba:

```text
No language model configuration found.
```

Megoldás:

- Konfigurálja az Azure OpenAI-t vagy az OpenAI-t.
- Ellenőrizze, hogy a változók ott vannak-e a környezetben, ahol a parancs fut.
- Helyi használat esetén helyezze őket a projekt gyökerében lévő `.env` fájlba.

Lásd: [Konfiguráció](configuration.md).

### Képfordítás Azure AI Vision nélkül

Hiba:

```text
Image translation requested but Azure AI Service is not configured.
```

Megoldás:

- Adja hozzá az `AZURE_AI_SERVICE_API_KEY`-t.
- Adja hozzá az `AZURE_AI_SERVICE_ENDPOINT`-t.
- Vagy futtasson egy csak szöveget fordító parancsot, például `translate -l "ko" -md`.

### Érvénytelen kulcs vagy végpont

A tünetek között szerepelhet `401`, elrejtett jogosultsági hibák vagy végponthoz való hozzáférési hibák.

Megoldás:

- Győződjön meg arról, hogy a kulcs ugyanahhoz az Azure-erőforráshoz tartozik, mint a végpont.
- Győződjön meg arról, hogy az erőforrás támogatja a Vision funkciót, ha a `-img` opciót használja.
- Ellenőrizze, hogy az Azure OpenAI telepítés neve és az API verzió megegyezik-e a telepítésével.
- Futtassa hibakeresési naplókkal: `translate -l "ko" -md -d -s`.

## Egy fájl sem lett lefordítva

Gyakori okok:

- A kiválasztott kapcsolók nem egyeznek a fájljaival.
- Már léteznek lefordított fájlok.
- A forrásfájlok kizárt könyvtárak alatt vannak.
- A parancsot a projekt nem megfelelő gyökérkönyvtárából futtatják.

Ellenőrzések:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Használja a `--root-dir` opciót, ha a parancsot a projekt gyökérkönyvtárán kívül futtatja.

## Váratlan hivatkozás viselkedés

A hivatkozások átírása a kiválasztott tartalomtípusoktól függ:

- `-nb` szerepel: a jegyzetfüzet-hivatkozások a lefordított jegyzetfüzetekre mutathatnak.
- `-nb` kizárva: a jegyzetfüzet-hivatkozások maradhatnak a forrás jegyzetfüzetekre mutatva.
- `-img` szerepel: a képhivatkozások a lefordított képekre mutathatnak.
- `-img` kizárva: a képhivatkozások maradhatnak a forrásképekre mutatva.

Futtasson teljes tartalomfordítást, ha minden belső hivatkozásnak a lefordított kimeneteket kell előnyben részesítenie:

```bash
translate -l "ko" -md -nb -img
```

Futtassa a hivatkozás-áttekintést a fordítás után:

```bash
co-op-review -l "ko"
```

## Markdown megjelenítési problémák

Ha a lefordított Markdown helytelenül jelenik meg:

- Ellenőrizze, hogy a frontmatter `---`-vel kezdődik és `---`-vel végződik.
- Ellenőrizze, hogy a kódkeretek (code fence) száma megegyezik-e a forrás- és a lefordított fájlokban.
- Futtassa a `co-op-review`-t a gyakori szerkezeti problémák észleléséhez.
- Fordítsa újra a konkrét fájlt, ha a kimenet megsérült.

```bash
co-op-review -l "ko" --format github
```

## A GitHub Action lefutott, de nem jött létre Pull Request

Ha a `peter-evans/create-pull-request` azt jelzi, hogy az ág nincs előrébb az alapnál, a munkafolyamat nem talált commitolható fájlokat.

Valószínű okok:

- A fordítási futás nem eredményezett változásokat.
- A `.gitignore` kizárja a `translations/`, `translated_images/` vagy a lefordított jegyzetfüzeteket.
- `add-paths` nem egyezik a generált kimeneti könyvtárakkal.
- A fordítási lépés korábban kilépett.

Javítások:

1. Ellenőrizze, hogy a generált fájlok léteznek-e a `translations/` vagy a `translated_images/` könyvtárban.
2. Ellenőrizze, hogy a `.gitignore` nem ignorálja a generált kimeneteket.
3. Használjon egyező `add-paths` beállítást:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Ideiglenesen adjon hozzá hibakeresési kapcsolókat a translate parancshoz:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Ellenőrizze, hogy a munkafolyamat jogosultságai tartalmazzák:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Fordítási minőség

A gépi fordítások emberi felülvizsgálatot igényelhetnek. Az `evaluate`-t csak akkor használja, ha kísérleti minőségértékelést és alacsony bizalmú javítási munkafolyamatokat szeretne.

!!! warning "Experimental"
    Az `evaluate` szabályalapú és LLM-alapú ellenőrzéseket használhat, és a pontozási modellje és a metaadatok viselkedése változhat. Ne tegye kötelező CI-feladatok részeként, hacsak a munkafolyamata nincs felkészítve a változásokra.

Determinikus CI-ellenőrzésekhez használja helyette a `co-op-review`-t.