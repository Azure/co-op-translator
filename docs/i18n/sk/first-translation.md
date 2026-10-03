# Preložte, upravte a skontrolujte malý projekt

Začnite s dvoma krátkymi súbormi Markdown a jedným cieľovým jazykom. Uvidíte, kam sa preklady zapisujú, čo sa stane pri zmene zdroja a ako skontrolovať výsledok.

## Zaznamenané výsledky

Príklad bol spustený 19. septembra 2026 s Co-op Translator 0.21.0 a Azure OpenAI (`gpt-5-mini`). Nemodifikované príkazy CLI boli spustené cez `CliRunner` z Clicku pomocou zostaveného wheelu a existujúcich Python závislostí.

| Krok | Výsledok |
| --- | --- |
| Náhľad | Exit 0; nevyžadoval sa žiadny preklad modelom |
| Počiatočný preklad | Exit 0; 27.36 sekúnd |
| Počiatočné overenie | Exit 0 |
| Upravte README a skontrolujte | Exit 1; zistený zastaralý preklad |
| Aktualizovať preklad | Exit 0; 22.17 sekúnd |
| Kontrola po aktualizácii | Exit 0; žiadne chyby ani varovania |
| Nezmenený návod | Identické bajty pred a po aktualizácii README |
| Spustiť znova | Exit 0; identické haše pre všetky prekladové súbory |

Toto sú merania jednotlivých spustení, nie záruky výkonnosti. Čas nastavenia je vylúčený; fakturácia poskytovateľa nebola meraná. Spustenie bez zmien môže stále vykonať kontrolu stavu poskytovateľa.

Skontrolujte [počiatočný preklad](../../assets/demo/before.txt), [aktualizovaný preklad](../../assets/demo/after.txt), [úplný diff prekladu](../../assets/demo/update.diff), [zastaralé overenie](../../assets/demo/review-stale.txt), [konečné overenie](../../assets/demo/review-after.txt) a [detaily spustenia](../../assets/demo/results.json). Preklad celého súboru môže zmeniť ďalšie znenie, ako ukazuje zachytený diff. Obe textové artefakty si zachovávajú vygenerované zrieknutie sa zodpovednosti.

Ľudské overenie stále záleží: zachytená aktualizácia používa `[사용 가이드](guide.md)을`; kórejský partikula by mala byť `[사용 가이드](guide.md)를`. Textové artefakty tento výstup ponechávajú nedotknutý namiesto toho, aby predkladali upravený preklad ako výstup modelu. Štrukturálne overenie prejde napriek tomuto problému v znení.

## 1. Pripravte malú zložku

Použite Python 3.11–3.14 a [nastavenie virtuálneho prostredia](configuration.md#local-runtime-setup). Nainštalujte verziu použitú v tomto príklade:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Stiahnite [README.txt](../../assets/demo/README.txt) a [guide.txt](../../assets/demo/guide.txt) do tejto zložky a uložte ich ako `README.md` a `guide.md`. Sú to malé fiktívne dokumenty projektu; nie je potrebná inštalácia žiadnej aplikácie.

README obsahuje blok kódu a odkaz na `guide.md`. Jeho posledná veta je:

```text
Notes are saved locally.
```

V tejto zložke ponechajte iba tieto dva zdrojové dokumenty. Všetky nasledujúce príkazy sa spúšťajú v rámci `translation-demo` a fungujú v Bash aj PowerShell.

## 2. Náhľad bez poverení

```bash
translate -l "ko" -md --dry-run
```

Náhľad odhaduje prácu na preklade bez volania modelu alebo zápisu prekladov. Odhady tokenov nie sú fakturačná ponuka. Prvé spustenie by malo identifikovať oba Markdown súbory ako novú prácu.

## 3. Vyberte poskytovateľa a preložte

Nakonfigurujte jedného poskytovateľa podľa [návodu na konfiguráciu](configuration.md): Azure OpenAI, OpenAI alebo Anthropic. Preklad textu cez OpenAI a Anthropic nevyžaduje účet Azure. Služby pre obrázky nie sú pre tento príklad potrebné.

Ak používate lokálny súbor `.env`, pridajte `.env` do `.gitignore` tejto zložky. Volania prekladu používajú váš účet poskytovateľa a môžu byť spoplatnené.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Otvorte `translations/ko/README.md` a `translations/ko/guide.md`. Skontrolujte kórejské znenie, blok kódu a odkaz z preloženého README na preložený návod. Znenie výstupu sa líši podľa modelu.

`co-op-review` kontroluje aktuálnosť, štruktúru a lokálne odkazy. Prechodný výsledok nezaručuje jazykovú presnosť. Pred pokračovaním odstráňte všetky nahlásené chyby.

Zaznamenajte úspešnú východiskovú verziu pomocou Gitu (najprv nakonfigurujte svoju Git identitu, ak je to potrebné):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Zmeňte zdroj

V `README.md` nahraďte `Notes are saved locally.` textom:

```text
Notes are saved locally as Markdown files.
```

Nechajte `guide.md` nezmenený. Potom spustite:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Kontrola by mala nahlásiť, že preklad README je zastaraný a ukončiť sa s chybou. Toto je očakávaný medzistav. Náhľad by mal identifikovať prácu pre zmenené README.

## 5. Aktualizujte a skontrolujte diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Skontrolujte skutočný diff: predvolený CLI znovu preloží zmenený súbor, takže model môže tiež upraviť iné znenie v tom súbore. Nezmenený návod by nemal mať žiadny diff. Kontrola by už nemala hlásiť README ako zastarané; preverte akékoľvek ďalšie nálezy namiesto ich ignorovania.

Zachovanie úprav Markdown na úrovni blokov vyžaduje voliteľného poskytovateľa stavu prekladu v [Python API](api.md). Týmto CLI príkazom nie je povolený.

## 6. Spustite znova bez zmien

Commitnite aktualizovaný zdroj a preklad:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

S aktuálnymi prekladmi a nezmenenou konfiguráciou prekladač súbory preskočí. Záverečný Git príkaz by nemal vygenerovať žiadny diff a mal by sa úspešne ukončiť.

## Ďalšie kroky

- [Preložte iba README a otvorte pull request](github-actions.md#your-first-readme-translation-pr).
- [Vyberte CLI, Python API alebo MCP](workflows.md).
- [Nahláste problém s prekladom bez kódovania](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).