# Troubleshooting

Használja ezt az oldalt, ha egy fordítási futtatás váratlanul sikeres, konfiguráció közben hibát jelez, vagy olyan kimenetet eredményez, amely felülvizsgálatot igényel.

## Kezdje itt

1. Először futtass egy célzott parancsot, például `translate -l "ko" -md`.
2. Add `-d` for console debug logs.
3. Add `-s` to save debug logs under `<root-dir>/logs/`.
4. Futtassa a `co-op-review`-t a fordítás után, hogy ellenőrizze a frissességet, a szerkezetet és a helyi hivatkozásokat.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfigurációs hibák

### Nincs nyelvi modell szolgáltató

Error:

```text
No language model configuration found.
```

Fix:

- Állítsa be az Azure OpenAI-t, az OpenAI-t vagy az Anthropic-ot.
- Ellenőrizze, hogy a változók ott vannak-e a parancsot futtató környezetben.
- Helyi használathoz helyezze őket a projekt gyökerében lévő `.env` fájlba.

See [Configuration](configuration.md).

### Képfordítás Azure AI Vision nélkül

Error:

```text
Image translation requested but Azure AI Service is not configured.
```

Fix:

- Adjon hozzá `AZURE_AI_SERVICE_API_KEY`.
- Adjon hozzá `AZURE_AI_SERVICE_ENDPOINT`.
- Vagy futtasson csak szöveget feldolgozó parancsot, például `translate -l "ko" -md`.

### Érvénytelen kulcs vagy végpont

A tünetek között szerepelhetnek a `401`, eltitkolt jogosultsági hibák vagy végpont-hozzáférési hibák.

Fix:

- Ellenőrizze, hogy a kulcs ugyanahhoz az Azure-erőforráshoz tartozik-e, mint a végpont.
- Ellenőrizze, hogy az erőforrás támogatja-e a Visiont, ha `-img`-et használ.
- Ellenőrizze, hogy az Azure OpenAI telepítés neve és az API verzió megegyezik-e a telepítésével.
- Futtassa debug naplókkal: `translate -l "ko" -md -d -s`.

## Egy fájl sem lett lefordítva

Common causes:

- A kiválasztott kapcsolók nem egyeznek a fájljaival.
- Már léteznek lefordított fájlok.
- A forrásfájlok kizárt könyvtárak alatt találhatók.
- A parancsot a rossz projektgyökérből futtatják.

Checks:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Használd `--root-dir`-t, ha a parancsot a projekt gyökérkönyvtárán kívül futtatod.

## Váratlan link viselkedés

A hivatkozások átírása a kiválasztott tartalomtípusoktól függ:

- `-nb` bekapcsolva: a jegyzetfüzet-hivatkozások a lefordított jegyzetfüzetekre mutathatnak.
- `-nb` kizárva: a jegyzetfüzet-hivatkozások továbbra is az eredeti jegyzetfüzetekre mutathatnak.
- `-img` bekapcsolva: a képhivatkozások a lefordított képekre mutathatnak.
- `-img` kizárva: a képhivatkozások továbbra is az eredeti képekre mutathatnak.

Végezzen teljes tartalomfordítást, ha minden belső hivatkozás a lefordított változatokat részesíti előnyben:

```bash
translate -l "ko" -md -nb -img
```

Run link review after translation:

```bash
co-op-review -l "ko"
```

## Markdown megjelenítési problémák

If translated Markdown renders incorrectly:

- Ellenőrizze, hogy a frontmatter `---`-rel kezdődik és végződik.
- Ellenőrizze, hogy a kódblokk határolók (``` ) száma megegyezik-e a forrás- és a lefordított fájlokban.
- Futtassa a `co-op-review`-t a gyakori szerkezeti hibák felderítéséhez.
- Fordítsa le újra a konkrét fájlt, ha a kimenet megsérült.

```bash
co-op-review -l "ko" --format github
```

## A GitHub Action lefutott, de nem lett létrehozva Pull Request

Ha a `peter-evans/create-pull-request` azt jelzi, hogy az ág nincs előrébb a bázisnál, a munkafolyamat nem talált commitolandó fájlokat.

Likely causes:

- A fordítási futtatás nem eredményezett változtatásokat.
- A `.gitignore` kizárja a `translations/`, `translated_images/` vagy a lefordított jegyzetfüzeteket.
- Az `add-paths` nem egyezik meg a generált kimeneti könyvtárakkal.
- A fordítási lépés korábban kilépett.

Fixes:

1. Confirm generated files exist in `translations/` or `translated_images/`.
2. Confirm `.gitignore` does not ignore generated outputs.
3. Use matching `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Ideiglenesen adj hibakeresési kapcsolókat a translate parancshoz:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirm workflow permissions include:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Fordítás minősége

A gépi fordítások emberi ellenőrzést igényelhetnek. A `evaluate`-t csak akkor használja, ha kísérleti minőségértékelést és alacsony megbízhatóságú javítási munkafolyamatokat szeretne.

!!! warning "Experimental"
    `evaluate` szabályalapú és LLM-alapú ellenőrzéseket használhat, és a pontozási modellje és a metaadatkezelése változhat. Ne tegye kötelező CI-fázisok részévé, hacsak a munkafolyamata nincs felkészítve a változásokra.

For deterministic CI checks, use `co-op-review` instead.