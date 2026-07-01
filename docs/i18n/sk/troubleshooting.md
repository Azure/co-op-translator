# Riešenie problémov

Použite túto stránku, keď preklad prebehne neočakávane úspešne, zlyhá počas konfigurácie alebo vygeneruje výstup, ktorý je potrebné skontrolovať.

## Začnite tu

1. Spustite najskôr zameraný príkaz, napríklad `translate -l "ko" -md`.
2. Pridajte `-d` pre ladenie (debug) v konzole.
3. Pridajte `-s` na uloženie debug záznamov do `<root-dir>/logs/`.
4. Po preklade spustite `co-op-review` na kontrolu čerstvosti, štruktúry a lokálnych odkazov.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Chyby konfigurácie

### Žiadny poskytovateľ jazykového modelu

Chyba:

```text
No language model configuration found.
```

Riešenie:

- Nakonfigurujte Azure OpenAI alebo OpenAI.
- Overte, že premenné sú v prostredí, kde sa príkaz spúšťa.
- Pri lokálnom použití umiestnite ich do `.env` v koreňovom adresári projektu.

Pozrite si [Konfigurácia](configuration.md).

### Preklad obrázkov bez Azure AI Vision

Chyba:

```text
Image translation requested but Azure AI Service is not configured.
```

Riešenie:

- Pridajte `AZURE_AI_SERVICE_API_KEY`.
- Pridajte `AZURE_AI_SERVICE_ENDPOINT`.
- Alebo spustite len textový príkaz, napríklad `translate -l "ko" -md`.

### Neplatný kľúč alebo koncový bod

Príznaky môžu zahŕňať `401`, vymazané chyby oprávnení alebo chyby prístupu ku koncovému bodu.

Riešenie:

- Potvrďte, že kľúč patrí tomu istému Azure zdroju ako koncový bod.
- Potvrďte, že zdroj podporuje Vision pri použití `-img`.
- Potvrďte, že názov nasadenia Azure OpenAI a verzia API zodpovedajú vášmu nasadeniu.
- Spustite s ladením: `translate -l "ko" -md -d -s`.

## Žiadne súbory neboli preložené

Bežné príčiny:

- Vybrané prepínače nezodpovedajú vašim súborom.
- Už existujú preložené súbory.
- Zdrojové súbory sa nachádzajú vo vylúčených adresároch.
- Príkaz sa spúšťa z nesprávneho koreňového adresára projektu.

Kontroly:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Použite `--root-dir`, keď sa príkaz spúšťa mimo koreňa projektu.

## Neočakávané správanie odkazov

Prepísanie odkazov závisí od vybraných typov obsahu:

- `-nb` zahrnuté: odkazy na notebooky môžu smerovať na preložené notebooky.
- `-nb` vylúčené: odkazy na notebooky môžu zostať nasmerované na zdrojové notebooky.
- `-img` zahrnuté: odkazy na obrázky môžu smerovať na preložené obrázky.
- `-img` vylúčené: odkazy na obrázky môžu zostať nasmerované na zdrojové obrázky.

Spustite kompletný preklad obsahu, keď majú všetky vnútorné odkazy preferovať preložené výstupy:

```bash
translate -l "ko" -md -nb -img
```

Po preklade spustite kontrolu odkazov:

```bash
co-op-review -l "ko"
```

## Problémy s vykresľovaním Markdownu

Ak sa preložený Markdown vykresľuje nesprávne:

- Skontrolujte, či frontmatter začína a končí `---`.
- Skontrolujte, či sa počet ohraničení kódu zhoduje medzi zdrojovými a preloženými súbormi.
- Spustite `co-op-review` na zachytenie bežných problémov so štruktúrou.
- Znovu preložte konkrétny súbor, ak bol výstup poškodený.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action bežal, ale nebol vytvorený pull request

Ak `peter-evans/create-pull-request` hlási, že vetva nie je pred základnou vetvou, workflow nenašiel žiadne súbory na commit.

Pravdepodobné príčiny:

- Preklad nezaznamenal žiadne zmeny.
- `.gitignore` vylučuje `translations/`, `translated_images/` alebo preložené notebooky.
- `add-paths` nezodpovedá vygenerovaným výstupným adresárom.
- Krok prekladu sa predčasne ukončil.

Riešenia:

1. Potvrďte, že vygenerované súbory existujú v `translations/` alebo `translated_images/`.
2. Potvrďte, že `.gitignore` neignoruje vygenerované výstupy.
3. Použite zodpovedajúce `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Dočasne pridajte ladiace prepínače k príkazu translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Potvrďte, že oprávnenia workflow zahŕňajú:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kvalita prekladu

Strojové preklady môžu vyžadovať ľudskú kontrolu. Používajte `evaluate` len keď chcete experimentálne hodnotenie kvality a pracovné postupy opráv pri nízkej dôvere.

!!! warning "Experimentálne"
    `evaluate` môže používať pravidlové a LLM založené kontroly a jeho hodnotiaci model a správanie s metadátami sa môžu zmeniť. Nepoužívajte ho v povinných CI bránach, pokiaľ váš workflow nie je pripravený na zmeny.

Pre deterministické CI kontroly používajte namiesto toho `co-op-review`.