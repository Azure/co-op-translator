<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:19:35+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "sr"
}
-->
# Podržani jezici

Tabela ispod prikazuje jezike koje trenutno podržava **Co-op Translator**. Uključuje kodove jezika, nazive jezika i poznate probleme vezane za svaki jezik. Ako želite da dodate podršku za novi jezik, molimo dodajte odgovarajući kod jezika, naziv i odgovarajući font u `font_language_mappings.yml` fajl koji se nalazi u `src/co_op_translator/fonts/` i pošaljite pull zahtev nakon testiranja.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | Engleski             | NotoSans-Medium.ttf               | Ne          | Ne           |
| fr            | Francuski            | NotoSans-Medium.ttf               | Ne          | Ne           |
| es            | Španski              | NotoSans-Medium.ttf               | Ne          | Ne           |
| de            | Nemački              | NotoSans-Medium.ttf               | Ne          | Ne           |
| ru            | Ruski                | NotoSans-Medium.ttf               | Ne          | Ne           |
| ar            | Arapski              | NotoSansArabic-Medium.ttf         | Da          | Ne           |
| fa            | Persijski (Farsi)    | NotoSansArabic-Medium.ttf         | Ne          | Ne           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Ne          | Ne           |
| zh            | Kineski (pojednostavljeni) | NotoSansCJK-Medium.ttc        | Ne          | Ne           |
| mo            | Kineski (tradicionalni, Makao) | NotoSansCJK-Medium.ttc    | Ne          | Ne           |
| hk            | Kineski (tradicionalni, Hong Kong) | NotoSansCJK-Medium.ttc| Ne          | Ne           |
| tw            | Kineski (tradicionalni, Tajvan) | NotoSansCJK-Medium.ttc     | Ne          | Ne           |
| ja            | Japanski             | NotoSansCJK-Medium.ttc            | Ne          | Ne           |
| ko            | Korejski             | NotoSansCJK-Medium.ttc            | Ne          | Ne           |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf     | Ne          | Ne           |
| bn            | Bengalski            | NotoSansBengali-Medium.ttf        | Ne          | Ne           |
| mr            | Maratski             | NotoSansDevanagari-Medium.ttf     | Ne          | Ne           |
| ne            | Nepalski             | NotoSansDevanagari-Medium.ttf     | Ne          | Ne           |
| pa            | Pandžapski (Gurmuki) | NotoSansGurmukhi-Medium.ttf       | Ne          | Ne           |
| pt            | Portugalski (Portugal) | NotoSans-Medium.ttf             | Ne          | Ne           |
| br            | Portugalski (Brazil) | NotoSans-Medium.ttf               | Ne          | Ne           |
| it            | Italijanski          | NotoSans-Medium.ttf               | Ne          | Ne           |
| pl            | Poljski              | NotoSans-Medium.ttf               | Ne          | Ne           |
| tr            | Turski               | NotoSans-Medium.ttf               | Ne          | Ne           |
| el            | Grčki                | NotoSans-Medium.ttf               | Ne          | Ne           |
| th            | Tajlandski           | NotoSansThai-Medium.ttf           | Ne          | Ne           |
| sv            | Švedski              | NotoSans-Medium.ttf               | Ne          | Ne           |
| da            | Danski               | NotoSans-Medium.ttf               | Ne          | Ne           |
| no            | Norveški             | NotoSans-Medium.ttf               | Ne          | Ne           |
| fi            | Finski               | NotoSans-Medium.ttf               | Ne          | Ne           |
| nl            | Holandski            | NotoSans-Medium.ttf               | Ne          | Ne           |
| he            | Hebrejski            | NotoSansHebrew-Medium.ttf         | Ne          | Ne           |
| vi            | Vijetnamski          | NotoSans-Medium.ttf               | Ne          | Ne           |
| id            | Indonezijski         | NotoSans-Medium.ttf               | Ne          | Ne           |
| ms            | Malezijski           | NotoSans-Medium.ttf               | Ne          | Ne           |
| tl            | Tagalog (Filipinski) | NotoSans-Medium.ttf               | Ne          | Ne           |
| sw            | Svahili              | NotoSans-Medium.ttf               | Ne          | Ne           |
| hu            | Mađarski             | NotoSans-Medium.ttf               | Ne          | Ne           |
| cs            | Češki                | NotoSans-Medium.ttf               | Ne          | Ne           |
| sk            | Slovački             | NotoSans-Medium.ttf               | Ne          | Ne           |
| ro            | Rumunski             | NotoSans-Medium.ttf               | Ne          | Ne           |
| bg            | Bugarski             | NotoSans-Medium.ttf               | Ne          | Ne           |
| sr            | Srpski (ćirilica)    | NotoSans-Medium.ttf               | Ne          | Ne           |
| hr            | Hrvatski             | NotoSans-Medium.ttf               | Ne          | Ne           |
| sl            | Slovenački           | NotoSans-Medium.ttf               | Ne          | Ne           |
| uk            | Ukrajinski           | NotoSans-Medium.ttf               | Ne          | Ne           |
| my            | Burmanski (Myanmar)  | NotoSans-Medium.ttf               | Ne          | Ne           |

## Dodavanje novog jezika

Da biste dodali podršku za novi jezik:

1. Idite na [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Dodajte kod jezika, naziv i odgovarajuće ime font fajla. Obavezno uključite `rtl` atribut ako je jezik sa desna na levo.
3. Ako treba da koristite novi font, proverite da li je font slobodan za korišćenje u open-source projektima tako što ćete proveriti licence i autorska prava. Nakon potvrde, dodajte font fajl u direktorijum `src/co_op_translator/fonts/`.
4. Testirajte izmene lokalno da biste bili sigurni da je novi jezik ispravno podržan.
5. Pošaljite Pull Request sa vašim izmenama i navedite dodavanje novog jezika u opisu PR-a.

Primer:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било какве неспоразуме или погрешна тумачења која произилазе из употребе овог превода.