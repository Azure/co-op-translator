<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "badae5ee6451cc1a6e367cfe5ba92efa",
  "translation_date": "2025-10-15T03:48:45+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "hu"
}
-->
# Támogatott nyelvek

Az alábbi táblázat felsorolja azokat a nyelveket, amelyeket jelenleg támogat a **Co-op Translator**. Megtalálható benne a nyelvkód, a nyelv neve, valamint az ismert problémák az adott nyelvhez kapcsolódóan. Ha szeretnél új nyelvet hozzáadni, írd be a megfelelő nyelvkódot, nevet és a szükséges betűtípust a `font_language_mappings.yml` fájlba, amely a `src/co_op_translator/fonts/` mappában található, majd tesztelés után küldj be egy pull requestet.

| Nyelvkód      | Nyelv neve                  | Betűtípus                         | RTL támogatás | Ismert problémák |
|---------------|-----------------------------|------------------------------------|---------------|------------------|
| en            | Angol                       | NotoSans-Medium.ttf                | Nem           | Nincs            |
| fr            | Francia                     | NotoSans-Medium.ttf                | Nem           | Nincs            |
| es            | Spanyol                     | NotoSans-Medium.ttf                | Nem           | Nincs            |
| de            | Német                       | NotoSans-Medium.ttf                | Nem           | Nincs            |
| ru            | Orosz                       | NotoSans-Medium.ttf                | Nem           | Nincs            |
| ar            | Arab                        | NotoSansArabic-Medium.ttf          | Igen          | Nincs            |
| fa            | Perzsa (Farsi)              | NotoSansArabic-Medium.ttf          | Igen          | Nincs            |
| ur            | Urdu                        | NotoSansArabic-Medium.ttf          | Igen          | Nincs            |
| zh            | Kínai (egyszerűsített)      | NotoSansCJK-Medium.ttc             | Nem           | Nincs            |
| mo            | Kínai (hagyományos, Makaó)  | NotoSansCJK-Medium.ttc             | Nem           | Nincs            |
| hk            | Kínai (hagyományos, Hongkong)| NotoSansCJK-Medium.ttc            | Nem           | Nincs            |
| tw            | Kínai (hagyományos, Tajvan) | NotoSansCJK-Medium.ttc             | Nem           | Nincs            |
| ja            | Japán                       | NotoSansCJK-Medium.ttc             | Nem           | Nincs            |
| ko            | Koreai                      | NotoSansCJK-Medium.ttc             | Nem           | Nincs            |
| hi            | Hindi                       | NotoSansDevanagari-Medium.ttf      | Nem           | Nincs            |
| bn            | Bengáli                     | NotoSansBengali-Medium.ttf         | Nem           | Nincs            |
| mr            | Maráthi                     | NotoSansDevanagari-Medium.ttf      | Nem           | Nincs            |
| ne            | Nepáli                      | NotoSansDevanagari-Medium.ttf      | Nem           | Nincs            |
| pa            | Pandzsábi (Gurmukhi)        | NotoSansGurmukhi-Medium.ttf        | Nem           | Nincs            |
| pt            | Portugál (Portugália)       | NotoSans-Medium.ttf                | Nem           | Nincs            |
| br            | Portugál (Brazília)         | NotoSans-Medium.ttf                | Nem           | Nincs            |
| it            | Olasz                       | NotoSans-Medium.ttf                | Nem           | Nincs            |
| lt            | Litván                      | NotoSans-Medium.ttf                | Nem           | Nincs            |
| pl            | Lengyel                     | NotoSans-Medium.ttf                | Nem           | Nincs            |
| tr            | Török                       | NotoSans-Medium.ttf                | Nem           | Nincs            |
| el            | Görög                       | NotoSans-Medium.ttf                | Nem           | Nincs            |
| th            | Thai                        | NotoSansThai-Medium.ttf            | Nem           | Nincs            |
| sv            | Svéd                        | NotoSans-Medium.ttf                | Nem           | Nincs            |
| da            | Dán                         | NotoSans-Medium.ttf                | Nem           | Nincs            |
| no            | Norvég                      | NotoSans-Medium.ttf                | Nem           | Nincs            |
| fi            | Finn                        | NotoSans-Medium.ttf                | Nem           | Nincs            |
| nl            | Holland                     | NotoSans-Medium.ttf                | Nem           | Nincs            |
| he            | Héber                       | NotoSansHebrew-Medium.ttf          | Igen          | Nincs            |
| vi            | Vietnámi                    | NotoSans-Medium.ttf                | Nem           | Nincs            |
| id            | Indonéz                     | NotoSans-Medium.ttf                | Nem           | Nincs            |
| ms            | Maláj                       | NotoSans-Medium.ttf                | Nem           | Nincs            |
| tl            | Tagalog (Filippínó)         | NotoSans-Medium.ttf                | Nem           | Nincs            |
| sw            | Szuahéli                    | NotoSans-Medium.ttf                | Nem           | Nincs            |
| hu            | Magyar                      | NotoSans-Medium.ttf                | Nem           | Nincs            |
| cs            | Cseh                        | NotoSans-Medium.ttf                | Nem           | Nincs            |
| sk            | Szlovák                     | NotoSans-Medium.ttf                | Nem           | Nincs            |
| ro            | Román                       | NotoSans-Medium.ttf                | Nem           | Nincs            |
| bg            | Bolgár                      | NotoSans-Medium.ttf                | Nem           | Nincs            |
| sr            | Szerb (cirill)              | NotoSans-Medium.ttf                | Nem           | Nincs            |
| hr            | Horvát                      | NotoSans-Medium.ttf                | Nem           | Nincs            |
| sl            | Szlovén                     | NotoSans-Medium.ttf                | Nem           | Nincs            |
| uk            | Ukrán                       | NotoSans-Medium.ttf                | Nem           | Nincs            |
| my            | Burmai (Mianmar)            | NotoSansMyanmar-Medium.ttf         | Nem           | Nincs            |
| ta            | Tamil                       | NotoSansTamil-Medium.ttf           | Nem           | Nincs            |
| et            | Észt                        | NotoSans-Medium.ttf                | Nem           | Nincs            |

## Új nyelv hozzáadása

Szeretnél új nyelvet hozzáadni? Kövesd az alábbi útmutatót:

- Lásd: Közreműködés: <a href="../CONTRIBUTING.md#contribute-a-new-language">Új nyelv hozzáadása</a>

---

**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.