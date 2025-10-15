<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:55:11+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "sk"
}
-->
# Príručka na riešenie problémov s Microsoft Co-op Translatorom

## Prehľad
Microsoft Co-Op Translator je výkonný nástroj na bezproblémový preklad Markdown dokumentov. Táto príručka vám pomôže vyriešiť najčastejšie problémy, ktoré sa môžu vyskytnúť pri používaní tohto nástroja.

## Bežné problémy a ich riešenia

### 1. Problém s Markdown tagom
**Problém:** Preložený Markdown dokument obsahuje na začiatku tag `markdown`, čo spôsobuje problémy s vykresľovaním.

**Riešenie:** Jednoducho odstráňte tag `markdown` z vrchu súboru. Tým sa zabezpečí správne vykreslenie Markdown súboru.

**Postup:**
1. Otvorte preložený Markdown (`.md`) súbor.
2. Nájdite tag `markdown` na začiatku dokumentu.
3. Odstráňte tento tag.
4. Uložte zmeny v súbore.
5. Znovu otvorte súbor a skontrolujte, či sa správne zobrazuje.

### 2. Problém s URL obrázkov
**Problém:** URL vložených obrázkov nezodpovedajú jazykovej lokalite, čo vedie k nesprávnym alebo chýbajúcim obrázkom.

**Riešenie:** Skontrolujte URL vložených obrázkov a uistite sa, že zodpovedajú jazykovej lokalite. Všetky obrázky sa nachádzajú v priečinku `translated_images` a každý obrázok má v názve súboru jazykovú značku.

**Postup:**
1. Otvorte preložený Markdown dokument.
2. Identifikujte vložené obrázky a ich URL adresy.
3. Overte, či jazyková značka v názve obrázka zodpovedá jazyku dokumentu.
4. V prípade potreby upravte URL adresy.
5. Uložte zmeny a znovu otvorte dokument, aby ste sa presvedčili, že obrázky sa zobrazujú správne.

### 3. Presnosť prekladu
**Problém:** Preložený obsah nie je presný alebo si vyžaduje ďalšie úpravy.

**Riešenie:** Skontrolujte preložený dokument a vykonajte potrebné úpravy na zlepšenie presnosti a čitateľnosti.

**Postup:**
1. Otvorte preložený dokument.
2. Dôkladne si prečítajte obsah.
3. Vykonajte potrebné úpravy na zlepšenie presnosti prekladu.
4. Uložte zmeny.

## 4. Chyba povolení Redacted alebo 404

Ak obrázky alebo text nie sú preložené do správneho jazyka a pri spustení v debug móde (-d) sa zobrazí chyba 401, ide o klasické zlyhanie autentifikácie – buď je kľúč neplatný, expirovaný, alebo nie je priradený k správnemu regionálnemu endpointu.

Spustite co-op translator s [prepínačom -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md), aby ste získali viac informácií o príčine problému.

- **Chybové hlásenie:** `Access denied due to invalid subscription key or wrong API endpoint.`
- **Možné príčiny:**
  - Subscription key bol redigovaný alebo nesprávny v požiadavke.
  - AI Services Key alebo Subscription Key patrí inému Azure zdroju (napr. Translator alebo OpenAI) namiesto **Azure AI Vision** zdroja.

 **Typ zdroja**
  - Prejdite do [Azure Portal](https://portal.azure.com) alebo [Azure AI Foundry](https://ai.azure.com) a uistite sa, že zdroj je typu `Azure AI services` → `Vision`.
  - Overte kľúče a uistite sa, že používate správny kľúč.

## 5. Chyby konfigurácie (Nové spracovanie chýb)

Od zavedenia selektívneho prekladu Co-op Translator poskytuje explicitné chybové hlásenia, ak nie sú potrebné služby správne nastavené.

### 5.1. Azure AI Service nie je nastavená pre preklad obrázkov

**Problém:** Požiadali ste o preklad obrázkov (flag `-img`), ale Azure AI Service nie je správne nastavená.

**Chybové hlásenie:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Riešenie:**
1. **Možnosť 1:** Nastavte Azure AI Service
   - Pridajte `AZURE_AI_SERVICE_API_KEY` do vášho `.env` súboru
   - Pridajte `AZURE_AI_SERVICE_ENDPOINT` do vášho `.env` súboru
   - Overte, že služba je dostupná

2. **Možnosť 2:** Odstráňte požiadavku na preklad obrázkov
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Chýbajúca požadovaná konfigurácia

**Problém:** Chýba základná konfigurácia LLM.

**Chybové hlásenie:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Riešenie:**
1. Overte, že váš `.env` súbor obsahuje aspoň jednu z nasledujúcich LLM konfigurácií:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` a `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Potrebujete nastaviť buď Azure OpenAI ALEBO OpenAI, nie oboje.

### 5.3. Zmätok pri selektívnom preklade

**Problém:** Žiadne súbory neboli preložené, aj keď príkaz prebehol úspešne.

**Možné príčiny:**
- Nesprávne typy súborov (`-md`, `-img`, `-nb`)
- V projekte nie sú žiadne zodpovedajúce súbory
- Nesprávna štruktúra adresárov

**Riešenie:**
1. **Použite debug mód** na zistenie, čo sa deje:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Skontrolujte typy súborov** vo vašom projekte:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Overte kombinácie flagov**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migrácia zo starého systému

### 6.1. Markdown-only mód je zrušený

**Problém:** Príkazy, ktoré sa spoliehali na automatický fallback len na markdown, už nefungujú podľa očakávaní.

**Staré správanie:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Nové správanie:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Riešenie:**
- **Buďte explicitní** v tom, čo chcete prekladať:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Nečakané správanie odkazov

**Problém:** Odkazy v preložených súboroch smerujú na nečakané miesta.

**Príčina:** Dynamické spracovanie odkazov sa mení podľa zvolených typov súborov.

**Riešenie:**
1. **Porozumieť novému správaniu odkazov:**
   - `-nb` zahrnuté: Odkazy na notebooky smerujú na preložené verzie
   - `-nb` vylúčené: Odkazy na notebooky smerujú na pôvodné súbory
   - `-img` zahrnuté: Odkazy na obrázky smerujú na preložené verzie
   - `-img` vylúčené: Odkazy na obrázky smerujú na pôvodné súbory

2. **Vyberte správnu kombináciu** pre váš prípad použitia:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action prebehla, ale nevytvoril sa Pull Request (PR)

**Príznak:** Logy workflow pre `peter-evans/create-pull-request` zobrazujú:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Pravdepodobné príčiny:**
- **Neboli zistené žiadne zmeny:** Prekladová fáza nevytvorila žiadne rozdiely (repo už je aktuálne).
- **Ignorované výstupy:** `.gitignore` vylučuje súbory, ktoré chcete commitnúť (napr. `*.ipynb`, `translations/`, `translated_images/`).
- **Nesúlad add-paths:** Cesty zadané v akcii nezodpovedajú skutočným výstupným umiestneniam.
- **Logika/Podmienky workflow:** Prekladová fáza skončila predčasne alebo zapisovala do nečakaných adresárov.

**Ako opraviť / overiť:**
1. **Overte existenciu výstupov:** Po preklade skontrolujte, či workspace obsahuje nové/zmenené súbory v `translations/` a/alebo `translated_images/`.
   - Pri preklade notebookov sa uistite, že `.ipynb` súbory sú skutočne uložené pod `translations/<lang>/...`.
2. **Skontrolujte `.gitignore`:** Neignorujte generované výstupy. Uistite sa, že NEignorujete:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (ak prekladáte notebooky)
3. **Uistite sa, že add-paths zodpovedá výstupom:** Použite viacriadkovú hodnotu a zahrňte oba priečinky, ak je to potrebné:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Vynúťte PR na debugovanie:** Dočasne povoľte prázdne commity, aby ste overili správne nastavenie:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Spustite s debugom:** Pridajte `-d` k prekladovému príkazu, aby ste videli, aké súbory boli objavené a zapísané.
6. **Povolenia (GITHUB_TOKEN):** Uistite sa, že workflow má práva na zápis pre vytváranie commitov a PR:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Rýchly kontrolný zoznam na debugovanie

Pri riešení problémov s prekladom:

1. **Použite debug mód:** Pridajte flag `-d` pre podrobné logy
2. **Skontrolujte vaše flagy:** Uistite sa, že `-md`, `-img`, `-nb` zodpovedajú vašim zámerom
3. **Overte konfiguráciu:** Skontrolujte, či váš `.env` súbor obsahuje potrebné kľúče
4. **Testujte postupne:** Začnite len s `-md`, potom pridajte ďalšie typy
5. **Skontrolujte štruktúru súborov:** Uistite sa, že zdrojové súbory existujú a sú dostupné

Pre podrobnejšie informácie o dostupných príkazoch a flagoch si pozrite [Command Reference](./command-reference.md).

---

**Vyhlásenie o vylúčení zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj sa považuje pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.