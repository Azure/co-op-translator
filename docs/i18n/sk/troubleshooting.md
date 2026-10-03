# Riešenie problémov

Použite túto stránku, keď preklad prebehne neočakávane úspešne, zlyhá počas konfigurácie alebo vygeneruje výstup, ktorý potrebuje kontrolu.

## Začnite tu

1. Najskôr spustite zameraný príkaz, napríklad `translate -l "ko" -md`.
2. Pridajte `-d` pre debug logy v konzole.
3. Pridajte `-s`, aby sa debug logy uložili do `<root-dir>/logs/`.
4. Po preklade spustite `co-op-review` na kontrolu aktuálnosti, štruktúry a lokálnych odkazov.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Konfiguračné chyby

### Žiadny poskytovateľ jazykového modelu

Chyba:

```text
No language model configuration found.
```

Riešenie:

- Nakonfigurujte Azure OpenAI, OpenAI alebo Anthropic.
- Skontrolujte, či sú premenné v prostredí, z ktorého sa príkaz spúšťa.
- Pre lokálne použitie vložte ich do `.env` v koreňovom adresári projektu.

Pozrite si [Konfigurácia](configuration.md).

### Preklad obrázkov bez Azure AI Vision

Chyba:

```text
Image translation requested but Azure AI Service is not configured.
```

Riešenie:

- Pridajte `AZURE_AI_SERVICE_API_KEY`.
- Pridajte `AZURE_AI_SERVICE_ENDPOINT`.
- Alebo spustite príkaz len s textom, napríklad `translate -l "ko" -md`.

### Neplatný kľúč alebo koncový bod

Príznaky môžu zahŕňať `401`, chyby oprávnení s odstránenými údajmi alebo chyby prístupu ku koncovému bodu.

Riešenie:

- Overte, či kľúč patrí rovnakému Azure zdroju ako koncový bod.
- Overte, či zdroj podporuje Vision pri použití `-img`.
- Overte, či názov nasadenia Azure OpenAI a verzia API zodpovedajú vášmu nasadeniu.
- Spustite s debug logmi: `translate -l "ko" -md -d -s`.

## Žiadne súbory neboli preložené

Bežné príčiny:

- Vybrané prepínače neodpovedajú vašim súborom.
- Už existujú preložené súbory.
- Zdrojové súbory sú v vylúčených adresároch.
- Príkaz sa spúšťa z nesprávneho koreňa projektu.

Kontroly:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Použite `--root-dir`, keď sa príkaz spúšťa mimo koreňa projektu.

## Neočakávané správanie odkazov

Prepisovanie odkazov závisí od vybraných typov obsahu:

- `-nb` zahrnuté: odkazy na notebooky môžu smerovať na preložené notebooky.
- `-nb` vylúčené: odkazy na notebooky môžu zostať nasmerované na zdrojové notebooky.
- `-img` zahrnuté: odkazy na obrázky môžu smerovať na preložené obrázky.
- `-img` vylúčené: odkazy na obrázky môžu zostať smerovať na zdrojové obrázky.

Spustite úplný preklad obsahu, ak majú všetky vnútorné odkazy uprednostňovať preložené výstupy:

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
- Spustite `co-op-review`, aby ste zachytili bežné štrukturálne problémy.
- Preložte konkrétny súbor znova, ak bol výstup poškodený.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action sa spustil, ale nebol vytvorený žiadny Pull Request

Ak `peter-evans/create-pull-request` hlási, že vetva nie je pred základnou vetvou, workflow nenašiel žiadne súbory na commitovanie.

Pravdepodobné príčiny:

- Prekladový beh nevygeneroval žiadne zmeny.
- `.gitignore` vylučuje `translations/`, `translated_images/` alebo preložené notebooky.
- `add-paths` nezodpovedá vygenerovaným výstupným adresárom.
- Prekladací krok sa ukončil predčasne.

Riešenia:

1. Overte, či vygenerované súbory existujú v `translations/` alebo `translated_images/`.
2. Overte, či `.gitignore` neignoruje vygenerované výstupy.
3. Použite zodpovedajúce `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Dočasne pridajte debug prepínače k príkazu translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Overte, či workflow povolenia zahŕňajú:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kvalita prekladu

Strojové preklady môžu vyžadovať ľudskú kontrolu. Používajte `evaluate` iba ak chcete experimentálne hodnotenie kvality a pracovné postupy oprav s nízkou dôverou.

!!! warning "Experimental"
    `evaluate` môže používať pravidlové a LLM-ové kontroly, a jeho model skórovania a správanie metadát sa môžu zmeniť. Nezahŕňajte ho do požadovaných CI brán, pokiaľ váš workflow nie je pripravený na zmeny.

Pre deterministické CI kontroly používajte namiesto toho `co-op-review`.