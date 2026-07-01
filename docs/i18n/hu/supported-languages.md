# Támogatott nyelvek

A Co-op Translator a következő nyelvkódokat támogatja szöveg-, jegyzetfüzet- és képfordítási kimenetekhez.

Ha új nyelvet szeretnél hozzáadni, frissítsd a nyelv- és betűtípusleképezéseket a `src/co_op_translator/fonts/` alatt, és teszteld a nyelvet, mielőtt pull requestet nyitsz.

| Nyelvkód | Nyelv neve | Betűtípus | RTL támogatás | Ismert problémák |
| --- | --- | --- | --- | --- |
| en | Angol | NotoSans-Medium.ttf | Nem | Nincs |
| fr | Francia | NotoSans-Medium.ttf | Nem | Nincs |
| es | Spanyol | NotoSans-Medium.ttf | Nem | Nincs |
| de | Német | NotoSans-Medium.ttf | Nem | Nincs |
| ru | Orosz | NotoSans-Medium.ttf | Nem | Nincs |
| ar | Arab | NotoSansArabic-Medium.ttf | Igen | Nincs |
| fa | Perzsa (fárszi) | NotoSansArabic-Medium.ttf | Igen | Nincs |
| ur | Urdu | NotoSansArabic-Medium.ttf | Igen | Nincs |
| zh-CN | Kínai (egyszerűsített) | NotoSansCJK-Medium.ttc | Nem | Nincs |
| zh-MO | Kínai (hagyományos, Makaó) | NotoSansCJK-Medium.ttc | Nem | Nincs |
| zh-HK | Kínai (hagyományos, Hongkong) | NotoSansCJK-Medium.ttc | Nem | Nincs |
| zh-TW | Kínai (hagyományos, Tajvan) | NotoSansCJK-Medium.ttc | Nem | Nincs |
| ja | Japán | NotoSansCJK-Medium.ttc | Nem | Nincs |
| ko | Koreai | NotoSansCJK-Medium.ttc | Nem | Nincs |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Nem | Nincs |
| bn | Bengáli | NotoSansBengali-Medium.ttf | Nem | Nincs |
| mr | Maráthi | NotoSansDevanagari-Medium.ttf | Nem | Nincs |
| ne | Nepáli | NotoSansDevanagari-Medium.ttf | Nem | Nincs |
| pa | Pandzsábi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nem | Nincs |
| pt-PT | Portugál (Portugália) | NotoSans-Medium.ttf | Nem | Nincs |
| pt-BR | Portugál (Brazília) | NotoSans-Medium.ttf | Nem | Nincs |
| it | Olasz | NotoSans-Medium.ttf | Nem | Nincs |
| lt | Litván | NotoSans-Medium.ttf | Nem | Nincs |
| pl | Lengyel | NotoSans-Medium.ttf | Nem | Nincs |
| tr | Török | NotoSans-Medium.ttf | Nem | Nincs |
| el | Görög | NotoSans-Medium.ttf | Nem | Nincs |
| th | Thai | NotoSansThai-Medium.ttf | Nem | Nincs |
| sv | Svéd | NotoSans-Medium.ttf | Nem | Nincs |
| da | Dán | NotoSans-Medium.ttf | Nem | Nincs |
| no | Norvég | NotoSans-Medium.ttf | Nem | Nincs |
| fi | Finn | NotoSans-Medium.ttf | Nem | Nincs |
| nl | Holland | NotoSans-Medium.ttf | Nem | Nincs |
| he | Héber | NotoSansHebrew-Medium.ttf | Igen | Nincs |
| vi | Vietnámi | NotoSans-Medium.ttf | Nem | Nincs |
| id | Indonéz | NotoSans-Medium.ttf | Nem | Nincs |
| ms | Maláj | NotoSans-Medium.ttf | Nem | Nincs |
| tl | Tagalog (filippínó) | NotoSans-Medium.ttf | Nem | Nincs |
| sw | Szuahéli | NotoSans-Medium.ttf | Nem | Nincs |
| hu | Magyar | NotoSans-Medium.ttf | Nem | Nincs |
| cs | Cseh | NotoSans-Medium.ttf | Nem | Nincs |
| sk | Szlovák | NotoSans-Medium.ttf | Nem | Nincs |
| ro | Román | NotoSans-Medium.ttf | Nem | Nincs |
| bg | Bolgár | NotoSans-Medium.ttf | Nem | Nincs |
| sr | Szerb (cirill) | NotoSans-Medium.ttf | Nem | Nincs |
| hr | Horvát | NotoSans-Medium.ttf | Nem | Nincs |
| sl | Szlovén | NotoSans-Medium.ttf | Nem | Nincs |
| uk | Ukrán | NotoSans-Medium.ttf | Nem | Nincs |
| my | Burmai (Myanmar) | NotoSansMyanmar-Medium.ttf | Nem | Nincs |
| ta | Tamil | NotoSansTamil-Medium.ttf | Nem | Nincs |
| et | Észt | NotoSans-Medium.ttf | Nem | Nincs |
| pcm | Nigériai pidgin | NotoSans-Medium.ttf | Nem | Nincs |
| te | Telugu | NotoSans-Medium.ttf | Nem | Nincs |
| ml | Malayalam | NotoSans-Medium.ttf | Nem | Nincs |
| kn | Kannada | NotoSans-Medium.ttf | Nem | Nincs |
| km | Khmer | NotoSansKhmer-Medium.ttf | Nem | Nincs |

## Nyelv hozzáadása

A támogatás hozzáadásához egy új nyelvhez:

1. Add hozzá a nyelvkódot és a megjelenítendő nevet a nyelvi segédprogramokhoz.
2. Adj hozzá vagy rendelj hozzá egy betűtípust a `src/co_op_translator/fonts/font_language_mappings.yml`-ben.
3. Teszteld a Markdown és a képfordítás kimenetét.
4. Nyiss egy pull requestet a leképezéssel és az érvényesítési megjegyzésekkel.