<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:42:45+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "hu"
}
-->
# Markdown-only mód használata

## Bevezetés  
A Markdown-only mód arra szolgál, hogy csak a projekt Markdown tartalmát fordítsa le. Ez a mód kihagyja a képek fordítását, és kizárólag a szöveges tartalomra koncentrál, így ideális olyan esetekben, amikor nincs szükség a képek fordítására, vagy a Computer Vision-hoz szükséges környezeti változók nincsenek beállítva.

## Mikor használd  
- Ha a Computer Vision-hoz kapcsolódó környezeti változók nincsenek konfigurálva.  
- Ha csak a szöveges tartalmat szeretnéd lefordítani, anélkül, hogy a képlinkeket frissítenéd.  
- Ha a felhasználó kifejezetten az `-md` parancssori opció használatával jelzi ezt.

## Hogyan engedélyezd  
A Markdown-only mód aktiválásához használd az `-md` opciót a parancsban. Például:  
```
translate -l "ko" -md
```

Vagy ha a Computer Vision-hoz kapcsolódó környezeti változók nincsenek beállítva, a `translate -l "ko"` parancs automatikusan átvált Markdown-only módra.

```
translate -l "ko"
```

Ez a parancs a Markdown tartalmat koreaira fordítja, és a képlinkeket az eredeti útvonalukra hagyja, ahelyett, hogy lefordított képutakra módosítaná őket.

## Működés  
Markdown-only módban:  
- A fordítási folyamat kihagyja a képek fordítását.  
- A Markdownban szereplő képlinkek változatlanok maradnak, az eredeti útvonalra mutatnak.

## Példák  
### Előtte  
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.hu.png)
```  
### Markdown-only mód használata után  
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.hu.png)
```

## Hibakeresés  
- Ellenőrizd, hogy az `-md` opció helyesen van-e megadva a parancsban.  
- Győződj meg róla, hogy nincs olyan Computer Vision környezeti változó, ami zavarhatja a folyamatot.

## Összegzés  
A Markdown-only mód egyszerűsített módot kínál a szöveges tartalom fordítására anélkül, hogy a képlinkeket módosítaná. Különösen hasznos, ha nincs szükség a képek fordítására, vagy ha olyan környezetben dolgozol, ahol nincs beállítva a Computer Vision.

**Nyilatkozat:**  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk pontos fordítást biztosítani, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javasolunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.