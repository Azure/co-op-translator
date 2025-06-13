<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0788d7ebe4876c9be89132f48e09b26d",
  "translation_date": "2025-06-12T12:30:00+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "hu"
}
-->
# Microsoft Co-op Translator Hibakeresési Útmutató

## Áttekintés  
A Microsoft Co-Op Translator egy hatékony eszköz Markdown dokumentumok zökkenőmentes fordítására. Ez az útmutató segít a leggyakoribb problémák megoldásában, amelyek a használat során előfordulhatnak.

## Gyakori problémák és megoldások

### 1. Markdown címke probléma  
**Probléma:** A lefordított Markdown dokumentum elején megjelenik egy `markdown` címke, ami megjelenítési hibákat okoz.

**Megoldás:** Egyszerűen töröld a `markdown` címkét a fájl tetejéről, így a Markdown fájl helyesen fog megjelenni.

**Lépések:**  
1. Nyisd meg a lefordított Markdown (`.md`) fájlt.  
2. Keresd meg a dokumentum tetején a `markdown` címkét.  
3. Töröld a `markdown` címkét.  
4. Mentsd el a fájlt.  
5. Nyisd meg újra, hogy ellenőrizd a helyes megjelenést.

### 2. Beágyazott képek URL problémája  
**Probléma:** A beágyazott képek URL-je nem egyezik meg a nyelvi helyi beállítással, ezért a képek helytelenül vagy egyáltalán nem jelennek meg.

**Megoldás:** Ellenőrizd a beágyazott képek URL-jét, és győződj meg róla, hogy megfelel a nyelvi helyi beállításnak. Minden kép a `translated_images` mappában található, és a fájlnevekben szerepel a nyelvi helyi címke.

**Lépések:**  
1. Nyisd meg a lefordított Markdown dokumentumot.  
2. Azonosítsd a beágyazott képeket és azok URL-jeit.  
3. Ellenőrizd, hogy a kép fájlnevében szereplő nyelvi helyi címke megegyezik-e a dokumentum nyelvével.  
4. Ha szükséges, frissítsd az URL-eket.  
5. Mentsd el a változtatásokat, majd nyisd meg újra a dokumentumot, hogy meggyőződj a képek helyes megjelenéséről.

### 3. Fordítás pontossága  
**Probléma:** A lefordított tartalom nem pontos vagy további szerkesztést igényel.

**Megoldás:** Nézd át a lefordított dokumentumot, és végezz el szükséges módosításokat a pontosság és olvashatóság javítása érdekében.

**Lépések:**  
1. Nyisd meg a lefordított dokumentumot.  
2. Alaposan ellenőrizd a tartalmat.  
3. Végezze el a szükséges szerkesztéseket a fordítás pontosságának javításához.  
4. Mentsd el a változtatásokat.

### 4. Fájlformázási problémák  
**Probléma:** A lefordított dokumentum formázása helytelen. Ez előfordulhat táblázatok esetén is, itt egy további ``` are added.

**Solution:** Adjust the formatting of the document to match the original structure. Simply deleting the ``` segít a táblázat problémáinak megoldásában.

**Lépések:**  
1. Nyisd meg a lefordított dokumentumot.  
2. Hasonlítsd össze az eredeti dokumentummal a formázási hibák azonosításához.  
3. Állítsd be a formázást, hogy megfeleljen az eredeti dokumentumnak.  
4. Mentsd el a változtatásokat.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.