# Támogatott nyelvek

A Co-op Translator a következő nyelvkódokat támogatja szöveg-, jegyzetfüzet- és képfordítási kimenetekhez.

Ha új nyelvet szeretnél hozzáadni, frissítsd a nyelv- és betűtípusleképezéseket a `src/co_op_translator/fonts/` alatt, és teszteld a nyelvet, mielőtt pull requestet nyitsz.

| Nyelvkód | Nyelv neve | Betűtípus | RTL támogatás | Ismert problémák |
| --- | --- | --- | --- | --- |
| en | angol | NotoSans-Medium.ttf | Nem | Nem |
| fr | francia | NotoSans-Medium.ttf | Nem | Nem |
| es | spanyol | NotoSans-Medium.ttf | Nem | Nem |
| de | német | NotoSans-Medium.ttf | Nem | Nem |
| ru | orosz | NotoSans-Medium.ttf | Nem | Nem |
| ar | arab | NotoSansArabic-Medium.ttf | Igen | Nem |
| fa | perzsa (fárszi) | NotoSansArabic-Medium.ttf | Igen | Nem |
| ur | urdu | NotoSansArabic-Medium.ttf | Igen | Nem |
| zh-CN | kínai (egyszerűsített) | NotoSansCJK-Medium.ttc | Nem | Nem |
| zh-MO | kínai (hagyományos, Makaó) | NotoSansCJK-Medium.ttc | Nem | Nem |
| zh-HK | kínai (hagyományos, Hongkong) | NotoSansCJK-Medium.ttc | Nem | Nem |
| zh-TW | kínai (hagyományos, Tajvan) | NotoSansCJK-Medium.ttc | Nem | Nem |
| ja | japán | NotoSansCJK-Medium.ttc | Nem | Nem |
| ko | koreai | NotoSansCJK-Medium.ttc | Nem | Nem |
| hi | hindi | NotoSansDevanagari-Medium.ttf | Nem | Nem |
| bn | bengáli | NotoSansBengali-Medium.ttf | Nem | Nem |
| mr | maráthi | NotoSansDevanagari-Medium.ttf | Nem | Nem |
| ne | nepáli | NotoSansDevanagari-Medium.ttf | Nem | Nem |
| pa | punjabi (gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nem | Nem |
| pt-PT | portugál (Portugália) | NotoSans-Medium.ttf | Nem | Nem |
| pt-BR | portugál (Brazília) | NotoSans-Medium.ttf | Nem | Nem |
| it | olasz | NotoSans-Medium.ttf | Nem | Nem |
| lt | litván | NotoSans-Medium.ttf | Nem | Nem |
| pl | lengyel | NotoSans-Medium.ttf | Nem | Nem |
| tr | török | NotoSans-Medium.ttf | Nem | Nem |
| el | görög | NotoSans-Medium.ttf | Nem | Nem |
| th | thai | NotoSansThai-Medium.ttf | Nem | Nem |
| sv | svéd | NotoSans-Medium.ttf | Nem | Nem |
| da | dán | NotoSans-Medium.ttf | Nem | Nem |
| no | norvég | NotoSans-Medium.ttf | Nem | Nem |
| fi | finn | NotoSans-Medium.ttf | Nem | Nem |
| nl | holland | NotoSans-Medium.ttf | Nem | Nem |
| he | héber | NotoSansHebrew-Medium.ttf | Igen | Nem |
| vi | vietnami | NotoSans-Medium.ttf | Nem | Nem |
| id | indonéz | NotoSans-Medium.ttf | Nem | Nem |
| ms | maláj | NotoSans-Medium.ttf | Nem | Nem |
| tl | tagalog (filippínó) | NotoSans-Medium.ttf | Nem | Nem |
| sw | svahili | NotoSans-Medium.ttf | Nem | Nem |
| hu | magyar | NotoSans-Medium.ttf | Nem | Nem |
| cs | cseh | NotoSans-Medium.ttf | Nem | Nem |
| sk | szlovák | NotoSans-Medium.ttf | Nem | Nem |
| ro | román | NotoSans-Medium.ttf | Nem | Nem |
| bg | bolgár | NotoSans-Medium.ttf | Nem | Nem |
| sr | szerb (cirill) | NotoSans-Medium.ttf | Nem | Nem |
| hr | horvát | NotoSans-Medium.ttf | Nem | Nem |
| sl | szlovén | NotoSans-Medium.ttf | Nem | Nem |
| uk | ukrán | NotoSans-Medium.ttf | Nem | Nem |
| my | burmai (Myanmar) | NotoSansMyanmar-Medium.ttf | Nem | Nem |
| ta | tamil | NotoSansTamil-Medium.ttf | Nem | Nem |
| et | észt | NotoSans-Medium.ttf | Nem | Nem |
| pcm | nigériai pidgin | NotoSans-Medium.ttf | Nem | Nem |
| te | telugu | NotoSans-Medium.ttf | Nem | Nem |
| ml | malajálam | NotoSans-Medium.ttf | Nem | Nem |
| kn | kannada | NotoSans-Medium.ttf | Nem | Nem |
| km | khmer | NotoSansKhmer-Medium.ttf | Nem | Nem |
| mni | manipuri (Meitei Mayek) | NotoSansMeeteiMayek-Medium.ttf | Nem | Nem |

## Nyelv hozzáadása

Új nyelv támogatásának hozzáadásához:

1. Add hozzá a nyelvkódot és megjelenítendő nevet a nyelvi segédprogramokhoz.
2. Adj hozzá vagy rendelj egy betűtípust a `src/co_op_translator/fonts/font_language_mappings.yml` fájlban.
3. Teszteld a Markdown és a kép fordítási kimenetét.
4. Nyiss egy pull requestet a leképezéssel és az ellenőrzési megjegyzésekkel.