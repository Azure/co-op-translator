# Řešení problémů

Použijte tuto stránku, když běh překladu nečekaně uspěje, selže během konfigurace nebo vygeneruje výstup, který je třeba zkontrolovat.

## Začněte zde

1. Spusťte nejprve zaměřený příkaz, například `translate -l "ko" -md`.
2. Přidejte `-d` pro ladicí logy v konzoli.
3. Přidejte `-s` pro uložení ladicích logů do `<root-dir>/logs/`.
4. Spusťte `co-op-review` po překladu pro kontrolu aktuálnosti, struktury a lokálních odkazů.

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

- Nakonfigurujte Azure OpenAI nebo OpenAI.
- Ověřte, že jsou proměnné v prostředí, kde se příkaz spouští.
- Pro lokální použití je umístěte do `.env` v kořenovém adresáři projektu.

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

### Neplatný klíč nebo endpoint

Příznaky mohou zahrnovat `401`, redigované chyby oprávnění nebo chyby přístupu k endpointu.

Oprava:

- Potvrďte, že klíč patří ke zdroji Azure odpovídajícímu endpointu.
- Potvrďte, že zdroj podporuje Vision při použití `-img`.
- Potvrďte, že název nasazení Azure OpenAI a verze API odpovídají vašemu nasazení.
- Spusťte s ladicími logy: `translate -l "ko" -md -d -s`.

## Žádné soubory nebyly přeloženy

Běžné příčiny:

- Vybrané přepínače neodpovídají vašim souborům.
- Přeložené soubory již existují.
- Zdrojové soubory jsou v vyloučených adresářích.
- Příkaz se spouští z nesprávného kořenového adresáře projektu.

Kontroly:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Použijte `--root-dir`, když je příkaz spuštěn mimo kořenový adresář projektu.

## Neočekávané chování odkazů

Přepisování odkazů závisí na vybraných typech obsahu:

- `-nb` zahrnuto: odkazy na notebooky mohou směřovat na přeložené notebooky.
- `-nb` vyloučeno: odkazy na notebooky mohou zůstat ukazovat na zdrojové notebooky.
- `-img` zahrnuto: odkazy na obrázky mohou směřovat na přeložené obrázky.
- `-img` vyloučeno: odkazy na obrázky mohou zůstat směřovat na zdrojové obrázky.

Proveďte úplný překlad obsahu, když by měly všechny interní odkazy preferovat přeložené výstupy:

```bash
translate -l "ko" -md -nb -img
```

Po překladu spusťte kontrolu odkazů:

```bash
co-op-review -l "ko"
```

## Problémy s vykreslováním Markdownu

Pokud se přeložený Markdown vykresluje nesprávně:

- Zkontrolujte, že frontmatter začíná a končí `---`.
- Zkontrolujte, že počet ohraničení kódu odpovídá mezi zdrojovými a přeloženými soubory.
- Spusťte `co-op-review` pro odhalení běžných strukturálních problémů.
- Přeložte znovu konkrétní soubor, pokud byl výstup poškozen.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action běžela, ale žádný Pull Request nebyl vytvořen

Pokud `peter-evans/create-pull-request` uvádí, že větev není vpředu oproti základní větvi (base), workflow nenašel žádné soubory ke commitnutí.

Možné příčiny:

- Běh překladu nevygeneroval žádné změny.
- `.gitignore` vylučuje `translations/`, `translated_images/` nebo přeložené notebooky.
- `add-paths` neodpovídá vygenerovaným výstupním adresářům.
- Krok překladu skončil předčasně.

Opravy:

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

5. Potvrďte, že workflow má následující oprávnění:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kvalita překladu

Strojové překlady mohou potřebovat lidskou kontrolu. Používejte `evaluate` pouze, když chcete experimentální skórování kvality a workflow oprav s nízkou jistotou.

!!! warning "Experimental"
    `evaluate` může používat kontrolní mechanismy založené na pravidlech i na LLM, a jeho hodnotící model a chování metadat se mohou změnit. Nepřidávejte jej do povinných CI bran, pokud váš workflow není připraven na změny.

Pro deterministické CI kontroly použijte místo toho `co-op-review`.