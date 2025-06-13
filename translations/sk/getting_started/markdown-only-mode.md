<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:43:07+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "sk"
}
-->
# Používanie režimu iba s Markdownom

## Úvod
Režim iba s Markdownom je navrhnutý na prekladanie výhradne Markdown obsahu vášho projektu. Tento režim obchádza proces prekladu obrázkov a zameriava sa len na textový obsah, čo je ideálne v prípadoch, keď nie je potrebný preklad obrázkov alebo keď nie sú nastavené potrebné environmentálne premenné pre Computer Vision.

## Kedy použiť
- Keď nie sú nakonfigurované environmentálne premenné súvisiace s Computer Vision.
- Keď chcete preložiť iba textový obsah bez aktualizácie odkazov na obrázky.
- Keď je to explicitne určené používateľom pomocou príkazového riadku `-md`.

## Ako povoliť
Na aktiváciu režimu iba s Markdownom použite vo svojom príkaze možnosť `-md`. Napríklad:
```
translate -l "ko" -md
```

Alebo ak nie sú nakonfigurované environmentálne premenné súvisiace s Computer Vision. Spustením príkazu `translate -l "ko"` sa režim automaticky prepne na režim iba s Markdownom.

```
translate -l "ko"
```

Tento príkaz preloží obsah Markdown do kórejčiny a aktualizuje odkazy na obrázky na ich pôvodné cesty, namiesto ich zmeny na cesty k preloženým obrázkom.

## Správanie
V režime iba s Markdownom:
- Proces prekladu preskočí krok prekladu obrázkov.
- Odkazy na obrázky v Markdown zostávajú nezmenené a smerujú na ich pôvodné cesty.

## Príklady
### Pred
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.sk.png)
```
### Po použití režimu iba s Markdownom
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.sk.png)
```

## Riešenie problémov
- Skontrolujte, či je možnosť `-md` správne zadaná v príkaze.
- Overte, že žiadne environmentálne premenné Computer Vision nezasahujú do procesu.

## Záver
Režim iba s Markdownom poskytuje jednoduchý spôsob, ako prekladať textový obsah bez úpravy odkazov na obrázky. Je obzvlášť užitočný, keď preklad obrázkov nie je potrebný alebo keď pracujete v prostredí bez nastavenia Computer Vision.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.