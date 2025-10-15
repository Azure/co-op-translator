<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:52:09+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "cs"
}
-->
# Průvodce řešením problémů s Microsoft Co-op Translator

## Přehled
Microsoft Co-Op Translator je výkonný nástroj pro bezproblémový překlad Markdown dokumentů. Tento průvodce vám pomůže vyřešit běžné problémy, na které můžete při používání nástroje narazit.

## Běžné problémy a jejich řešení

### 1. Problém s Markdown tagem
**Problém:** Přeložený Markdown dokument obsahuje na začátku tag `markdown`, což způsobuje problémy s vykreslením.

**Řešení:** Stačí odstranit tag `markdown` na začátku souboru. Tím zajistíte správné vykreslení Markdown souboru.

**Postup:**
1. Otevřete přeložený Markdown (`.md`) soubor.
2. Najděte tag `markdown` na začátku dokumentu.
3. Odstraňte tento tag.
4. Uložte změny v souboru.
5. Znovu otevřete soubor a ověřte správné vykreslení.

### 2. Problém s URL vložených obrázků
**Problém:** URL vložených obrázků neodpovídají jazykové lokalizaci, což vede k nesprávným nebo chybějícím obrázkům.

**Řešení:** Zkontrolujte URL vložených obrázků a ujistěte se, že odpovídají jazykové lokalizaci. Všechny obrázky jsou umístěny ve složce `translated_images` a každý obrázek má v názvu souboru jazykovou značku.

**Postup:**
1. Otevřete přeložený Markdown dokument.
2. Najděte vložené obrázky a jejich URL.
3. Ověřte, že jazyková značka v názvu obrázku odpovídá jazyku dokumentu.
4. V případě potřeby upravte URL.
5. Uložte změny a znovu otevřete dokument, abyste ověřili správné zobrazení obrázků.

### 3. Přesnost překladu
**Problém:** Přeložený obsah není přesný nebo vyžaduje další úpravy.

**Řešení:** Projděte přeložený dokument a proveďte potřebné úpravy pro zvýšení přesnosti a čitelnosti.

**Postup:**
1. Otevřete přeložený dokument.
2. Důkladně si projděte obsah.
3. Proveďte potřebné úpravy pro zvýšení přesnosti překladu.
4. Uložte změny.

## 4. Chyba oprávnění Redacted nebo 404

Pokud se obrázky nebo text nepřekládají do správného jazyka a při spuštění v režimu -d debug narazíte na chybu 401, jedná se o klasické selhání ověření – buď je klíč neplatný, vypršel, nebo není propojen s regionem koncového bodu.

Spusťte co-op translator s [přepínačem -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) pro podrobnější analýzu příčiny.

- **Chybová zpráva:** `Access denied due to invalid subscription key or wrong API endpoint.`
- **Možné příčiny:**
  - Klíč předplatného byl v požadavku redigován nebo je nesprávný.
  - Klíč AI Services nebo Subscription Key patří jinému Azure zdroji (např. Translator nebo OpenAI) místo **Azure AI Vision**.

 **Typ zdroje**
  - Přejděte do [Azure Portal](https://portal.azure.com) nebo [Azure AI Foundry](https://ai.azure.com) a ověřte, že zdroj je typu `Azure AI services` → `Vision`.
  - Ověřte klíče a ujistěte se, že používáte správný klíč.

## 5. Chyby konfigurace (Nové zpracování chyb)

Od nové selektivní překladové verze Co-op Translator nyní poskytuje explicitní chybové zprávy, pokud nejsou požadované služby správně nastaveny.

### 5.1. Azure AI Service není nastavena pro překlad obrázků

**Problém:** Požadovali jste překlad obrázků (přepínač `-img`), ale Azure AI Service není správně nastavena.

**Chybová zpráva:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Řešení:**
1. **Varianta 1:** Nastavte Azure AI Service
   - Přidejte `AZURE_AI_SERVICE_API_KEY` do souboru `.env`
   - Přidejte `AZURE_AI_SERVICE_ENDPOINT` do souboru `.env`
   - Ověřte dostupnost služby

2. **Varianta 2:** Odstraňte požadavek na překlad obrázků
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Chybějící požadovaná konfigurace

**Problém:** Chybí základní konfigurace LLM.

**Chybová zpráva:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Řešení:**
1. Ověřte, že váš soubor `.env` obsahuje alespoň jednu z následujících LLM konfigurací:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` a `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Potřebujete nastavit buď Azure OpenAI NEBO OpenAI, ne obojí.

### 5.3. Zmatek při selektivním překladu

**Problém:** Nebyly přeloženy žádné soubory, i když příkaz proběhl úspěšně.

**Možné příčiny:**
- Nesprávné typy souborů (`-md`, `-img`, `-nb`)
- V projektu nejsou žádné odpovídající soubory
- Nesprávná struktura složek

**Řešení:**
1. **Použijte debug mód** pro zjištění detailů:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Zkontrolujte typy souborů** ve vašem projektu:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Ověřte kombinace přepínačů:**
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migrace ze starého systému

### 6.1. Režim pouze Markdown je zrušen

**Problém:** Příkazy, které se spoléhaly na automatický fallback pouze pro markdown, již nefungují podle očekávání.

**Původní chování:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Nové chování:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Řešení:**
- **Buďte konkrétní** ohledně toho, co chcete překládat:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Neočekávané chování odkazů

**Problém:** Odkazy v přeložených souborech vedou na nečekaná místa.

**Příčina:** Dynamické zpracování odkazů se mění podle zvolených typů souborů.

**Řešení:**
1. **Pochopte nové chování odkazů:**
   - `-nb` zahrnuto: Odkazy na notebooky vedou na přeložené verze
   - `-nb` vyloučeno: Odkazy na notebooky vedou na původní soubory
   - `-img` zahrnuto: Odkazy na obrázky vedou na přeložené verze
   - `-img` vyloučeno: Odkazy na obrázky vedou na původní soubory

2. **Zvolte správnou kombinaci** pro váš případ použití:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action proběhla, ale nebyl vytvořen Pull Request (PR)

**Příznak:** Logy workflow pro `peter-evans/create-pull-request` zobrazují:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Pravděpodobné příčiny:**
- **Nebyly zjištěny žádné změny:** Překladová fáze nevyprodukovala žádné rozdíly (repo už je aktuální).
- **Ignorované výstupy:** `.gitignore` vylučuje soubory, které chcete commitnout (např. `*.ipynb`, `translations/`, `translated_images/`).
- **Nesoulad add-paths:** Cesty zadané akci neodpovídají skutečným výstupním umístěním.
- **Logika/Podmínky workflow:** Překladová fáze skončila předčasně nebo zapisovala do nečekaných složek.

**Jak opravit / ověřit:**
1. **Ověřte existenci výstupů:** Po překladu zkontrolujte, zda workspace obsahuje nové/upravené soubory v `translations/` a/nebo `translated_images/`.
   - Pokud překládáte notebooky, ověřte, že soubory `.ipynb` jsou skutečně zapsány pod `translations/<lang>/...`.
2. **Zkontrolujte `.gitignore`:** Neignorujte generované výstupy. Ujistěte se, že NEignorujete:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (pokud překládáte notebooky)
3. **Ověřte, že add-paths odpovídá výstupům:** Použijte vícerořádkovou hodnotu a zahrňte obě složky, pokud je to relevantní:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Vynucení PR pro ladění:** Dočasně povolte prázdné commity pro ověření správného propojení:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Spusťte s debug:** Přidejte `-d` k příkazu pro překlad, abyste viděli, jaké soubory byly nalezeny a zapsány.
6. **Oprávnění (GITHUB_TOKEN):** Ujistěte se, že workflow má práva pro zápis, aby mohl vytvářet commity a PR:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Rychlý kontrolní seznam pro ladění

Při řešení problémů s překladem:

1. **Použijte debug mód:** Přidejte přepínač `-d` pro detailní logy
2. **Zkontrolujte přepínače:** Ujistěte se, že `-md`, `-img`, `-nb` odpovídají vašemu záměru
3. **Ověřte konfiguraci:** Zkontrolujte, že váš soubor `.env` obsahuje potřebné klíče
4. **Testujte postupně:** Začněte pouze s `-md`, pak přidávejte další typy
5. **Zkontrolujte strukturu souborů:** Ujistěte se, že zdrojové soubory existují a jsou dostupné

Pro podrobnější informace o dostupných příkazech a přepínačích navštivte [Command Reference](./command-reference.md).

---

**Prohlášení**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neneseme odpovědnost za jakékoli nedorozumění nebo nesprávné výklady vzniklé v důsledku použití tohoto překladu.