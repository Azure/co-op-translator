# Odstraňování problémů

Použijte tuto stránku, když běh překladu nečekaně uspěje, selže během konfigurace nebo vytvoří výstup, který je třeba zkontrolovat.

## Začněte zde

1. Nejprve spusťte zaměřený příkaz, například `translate -l "ko" -md`.
2. Přidejte `-d` pro ladicí záznamy v konzoli.
3. Přidejte `-s` pro uložení ladicích záznamů do `<root-dir>/logs/`.
4. Po překladu spusťte `co-op-review` pro kontrolu aktuálnosti, struktury a místních odkazů.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Chyby konfigurace

### Žádný poskytovatel jazykového modelu

Chyba:

```text
No language model configuration found.
```

Oprava:

- Nakonfigurujte Azure OpenAI, OpenAI nebo Anthropic.
- Ověřte, že proměnné jsou v prostředí, kde se příkaz spouští.
- Pro lokální použití umístěte je do `.env` v kořenovém adresáři projektu.

Viz [Konfigurace](configuration.md).

### Překlad obrázků bez Azure AI Vision

Chyba:

```text
Image translation requested but Azure AI Service is not configured.
```

Oprava:

- Přidejte `AZURE_AI_SERVICE_API_KEY`.
- Přidejte `AZURE_AI_SERVICE_ENDPOINT`.
- Nebo spusťte příkaz pouze pro text, například `translate -l "ko" -md`.

### Neplatný klíč nebo koncový bod

Příznaky mohou zahrnovat `401`, skryté chyby oprávnění nebo chyby přístupu ke koncovému bodu.

Oprava:

- Potvrďte, že klíč patří ke stejnému prostředku Azure jako koncový bod.
- Potvrďte, že prostředek podporuje Vision při použití `-img`.
- Potvrďte, že název nasazení Azure OpenAI a verze API odpovídají vašemu nasazení.
- Spusťte s ladicími záznamy: `translate -l "ko" -md -d -s`.

## Nebyly přeloženy žádné soubory

Běžné příčiny:

- Vybrané přepínače neodpovídají vašim souborům.
- Již existují přeložené soubory.
- Zdrojové soubory jsou ve vyloučených adresářích.
- Příkaz se spouští z nesprávného kořenového adresáře projektu.

Kontroly:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Použijte `--root-dir`, když je příkaz spuštěn mimo kořen projektu.

## Neočekávané chování odkazů

Přepisování odkazů závisí na vybraných typech obsahu:

- `-nb` zahrnuto: odkazy na notebooky mohou směřovat na přeložené notebooky.
- `-nb` vyloučeno: odkazy na notebooky mohou zůstat nasměrovány na zdrojové notebooky.
- `-img` zahrnuto: odkazy na obrázky mohou směřovat na přeložené obrázky.
- `-img` vyloučeno: odkazy na obrázky mohou zůstat nasměrovány na zdrojové obrázky.

Proveďte úplný překlad obsahu, když by všechny vnitřní odkazy měly upřednostňovat přeložené výstupy:

```bash
translate -l "ko" -md -nb -img
```

Proveďte kontrolu odkazů po překladu:

```bash
co-op-review -l "ko"
```

## Problémy s vykreslováním Markdownu

Pokud se přeložený Markdown vykresluje nesprávně:

- Zkontrolujte, že frontmatter začíná a končí `---`.
- Zkontrolujte, že počty code fence odpovídají mezi zdrojovými a přeloženými soubory.
- Spusťte `co-op-review` pro zachycení běžných strukturálních problémů.
- Přeložte daný soubor znovu, pokud byl výstup poškozen.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action se spustil, ale nebyl vytvořen žádný pull request

Pokud `peter-evans/create-pull-request` hlásí, že větev není před základní větví, workflow nenašel žádné soubory ke commitnutí.

Pravděpodobné příčiny:

- Běh překladu nevygeneroval žádné změny.
- `.gitignore` vylučuje `translations/`, `translated_images/` nebo přeložené notebooky.
- `add-paths` neodpovídá vygenerovaným výstupním adresářům.
- Krok překladu skončil dříve.

Řešení:

1. Potvrďte, že vygenerované soubory existují v `translations/` nebo `translated_images/`.
2. Potvrďte, že `.gitignore` neignoruje vygenerované výstupy.
3. Použijte odpovídající `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Dočasně přidejte ladicí přepínače k příkazu translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Potvrďte, že oprávnění workflow zahrnují:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kvalita překladu

Strojové překlady mohou vyžadovat lidskou revizi. Používejte `evaluate` pouze tehdy, když chcete experimentální hodnocení kvality a workflow pro opravy s nízkou důvěrou.

!!! warning "Experimental"
    `evaluate` může používat kontroly založené na pravidlech i na LLM, a jeho model skórování a chování metadat se mohou změnit. Nezařazujte jej do povinných CI bran, pokud váš pracovní postup není připraven na změny.

Pro deterministické CI kontroly místo toho použijte `co-op-review`.