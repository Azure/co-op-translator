# Přeložit, upravit a zkontrolovat malý projekt

Začněte se dvěma krátkými soubory Markdown a jedním cílovým jazykem. Uvidíte, kam se překlady zapisují, co se stane při změně zdroje a jak zkontrolovat výsledek.

## Zaznamenané výsledky

Příklad byl spuštěn 19. září 2026 s Co-op Translator 0.21.0 a Azure OpenAI (`gpt-5-mini`). Nemodifikované příkazy CLI byly volány přes Clickův `CliRunner` s použitím postaveného balíčku (wheel) a existujících Python závislostí.

| Krok | Výsledek |
| --- | --- |
| Náhled | Ukončení 0; nebyl vyžádán překlad modelem |
| Počáteční překlad | Ukončení 0; 27.36 sekund |
| Počáteční kontrola | Ukončení 0 |
| Upravit README a zkontrolovat | Ukončení 1; zjištěn zastaralý překlad |
| Aktualizovat překlad | Ukončení 0; 22.17 sekund |
| Kontrola po aktualizaci | Ukončení 0; žádné chyby ani varování |
| Neměnný návod | Identické bajty před a po aktualizaci README |
| Spustit znovu | Ukončení 0; identické hashe pro všechny překladové soubory |

Jedná se o měření jednotlivých běhů, nikoli o záruky výkonu. Doba nastavení není zahrnuta; fakturace poskytovatele nebyla měřena. Nezměněný běh může stále provést kontrolu stavu poskytovatele.

Prohlédněte si [počáteční překlad](../../assets/demo/before.txt), [aktualizovaný překlad](../../assets/demo/after.txt), [úplný diff překladu](../../assets/demo/update.diff), [zastaralou kontrolu](../../assets/demo/review-stale.txt), [konečnou kontrolu](../../assets/demo/review-after.txt) a [detaily běhu](../../assets/demo/results.json). Překlad celého souboru může změnit jiná slovní vyjádření, jak ukazuje zachycený diff. Obě textové artefakty si ponechávají vygenerované prohlášení o vyloučení odpovědnosti.

Lidská kontrola je stále důležitá: zachycená aktualizace používá `[사용 가이드](guide.md)을`; korejská částice by měla být `[사용 가이드](guide.md)를`. Textové artefakty tento výstup ponechávají nedotčený místo toho, aby prezentovaly upravený překlad jako výstup modelu. Strukturální kontrola projde navzdory tomuto problému s formulací.

## 1. Připravte malou složku

Použijte Python 3.11–3.14 a [nastavení virtuálního prostředí](configuration.md#local-runtime-setup). Nainstalujte verzi použitou v tomto příkladu:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Stáhněte [README.txt](../../assets/demo/README.txt) a [guide.txt](../../assets/demo/guide.txt) do této složky a uložte je jako `README.md` a `guide.md`. Jsou to malé fiktivní dokumenty projektu; není nutná instalace žádné aplikace.

README obsahuje blok kódu a odkaz na `guide.md`. Jeho poslední věta je:

```text
Notes are saved locally.
```

Ponechte v této složce pouze tyto dva zdrojové dokumenty. Všechny následující příkazy běží uvnitř `translation-demo` a fungují v Bashi i PowerShellu.

## 2. Náhled bez přihlašovacích údajů

```bash
translate -l "ko" -md --dry-run
```

Náhled odhaduje překladatelskou práci bez volání modelu nebo zápisu překladů. Odhady tokenů nejsou fakturačním odhadem. První běh by měl označit oba soubory Markdown jako novou práci.

## 3. Vyberte poskytovatele a přeložte

Nakonfigurujte jednoho poskytovatele pomocí [konfiguračního návodu](configuration.md): Azure OpenAI, OpenAI nebo Anthropic. Textový překlad OpenAI a Anthropic nevyžaduje účet Azure. Pro tento příklad nejsou potřeba služby pro obrázky.

Pokud používáte lokální soubor `.env`, přidejte `.env` do `.gitignore` této složky. Překladatelské volání používají účet vašeho poskytovatele a mohou způsobit poplatky.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Otevřete `translations/ko/README.md` a `translations/ko/guide.md`. Zkontrolujte korejské znění, blok kódu a odkaz z přeloženého README na přeložený návod. Znění výstupu se liší podle modelu.

`co-op-review` kontroluje aktuálnost, strukturu a lokální odkazy. Projít kontrolou neznamená potvrzení lingvistické přesnosti. Vyřešte všechny nahlášené chyby před pokračováním.

Zaznamenejte úspěšný základní stav do Gitu (nejprve případně nakonfigurujte svou Git identitu):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Změňte zdroj

V `README.md` nahraďte `Notes are saved locally.` tímto:

```text
Notes are saved locally as Markdown files.
```

Nechte `guide.md` beze změny. Poté spusťte:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Kontrola by měla nahlásit překlad README jako zastaralý a skončit neúspěšně. Toto je očekávaný mezistav. Náhled by měl identifikovat práci pro změněné README.

## 5. Aktualizujte a prohlédněte si diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Prohlédněte si skutečný diff: výchozí CLI překládá změněný soubor znovu, takže model může také upravit jiné znění v tom souboru. Neměnný návod by neměl mít žádný diff. Kontrola by již neměla hlásit README jako zastaralé; prozkoumejte jakékoli další zjištění, místo abyste je ignorovali.

Zachování úprav Markdownu na úrovni bloků vyžaduje volitelný poskytovatel stavu překladu v [Python API](api.md). Není tímto CLI příkazem povoleno.

## 6. Spusťte znovu bez změn

Proveďte commit aktualizovaného zdroje a překladu:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

S aktuálními překlady a nezměněnou konfigurací překladač soubory přeskočí. Závěrečný Git příkaz by neměl produkovat žádný diff a měl by skončit úspěšně.

## Další kroky

- [Přeložit pouze README a otevřít pull request](github-actions.md#your-first-readme-translation-pr).
- [Vyberte CLI, Python API nebo MCP](workflows.md).
- [Nahlásit problém s překladem bez psaní kódu](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).