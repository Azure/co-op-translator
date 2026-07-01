# Unterstützte Sprachen

Co-op Translator unterstützt die folgenden Sprachcodes für Text-, Notebook- und Bildübersetzungen.

Wenn Sie eine neue Sprache hinzufügen möchten, aktualisieren Sie die Sprach- und Schriftzuordnungen unter `src/co_op_translator/fonts/` und testen Sie die Sprache, bevor Sie einen Pull Request eröffnen.

| Sprachcode | Sprachname | Schriftart | RTL-Unterstützung | Bekannte Probleme |
| --- | --- | --- | --- | --- |
| en | Englisch | NotoSans-Medium.ttf | Nein | Nein |
| fr | Französisch | NotoSans-Medium.ttf | Nein | Nein |
| es | Spanisch | NotoSans-Medium.ttf | Nein | Nein |
| de | Deutsch | NotoSans-Medium.ttf | Nein | Nein |
| ru | Russisch | NotoSans-Medium.ttf | Nein | Nein |
| ar | Arabisch | NotoSansArabic-Medium.ttf | Ja | Nein |
| fa | Persisch (Farsi) | NotoSansArabic-Medium.ttf | Ja | Nein |
| ur | Urdu | NotoSansArabic-Medium.ttf | Ja | Nein |
| zh-CN | Chinesisch (vereinfacht) | NotoSansCJK-Medium.ttc | Nein | Nein |
| zh-MO | Chinesisch (traditionell, Macau) | NotoSansCJK-Medium.ttc | Nein | Nein |
| zh-HK | Chinesisch (traditionell, Hongkong) | NotoSansCJK-Medium.ttc | Nein | Nein |
| zh-TW | Chinesisch (traditionell, Taiwan) | NotoSansCJK-Medium.ttc | Nein | Nein |
| ja | Japanisch | NotoSansCJK-Medium.ttc | Nein | Nein |
| ko | Koreanisch | NotoSansCJK-Medium.ttc | Nein | Nein |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Nein | Nein |
| bn | Bengalisch | NotoSansBengali-Medium.ttf | Nein | Nein |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Nein | Nein |
| ne | Nepalesisch | NotoSansDevanagari-Medium.ttf | Nein | Nein |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Nein | Nein |
| pt-PT | Portugiesisch (Portugal) | NotoSans-Medium.ttf | Nein | Nein |
| pt-BR | Portugiesisch (Brasilien) | NotoSans-Medium.ttf | Nein | Nein |
| it | Italienisch | NotoSans-Medium.ttf | Nein | Nein |
| lt | Litauisch | NotoSans-Medium.ttf | Nein | Nein |
| pl | Polnisch | NotoSans-Medium.ttf | Nein | Nein |
| tr | Türkisch | NotoSans-Medium.ttf | Nein | Nein |
| el | Griechisch | NotoSans-Medium.ttf | Nein | Nein |
| th | Thailändisch | NotoSansThai-Medium.ttf | Nein | Nein |
| sv | Schwedisch | NotoSans-Medium.ttf | Nein | Nein |
| da | Dänisch | NotoSans-Medium.ttf | Nein | Nein |
| no | Norwegisch | NotoSans-Medium.ttf | Nein | Nein |
| fi | Finnisch | NotoSans-Medium.ttf | Nein | Nein |
| nl | Niederländisch | NotoSans-Medium.ttf | Nein | Nein |
| he | Hebräisch | NotoSansHebrew-Medium.ttf | Ja | Nein |
| vi | Vietnamesisch | NotoSans-Medium.ttf | Nein | Nein |
| id | Indonesisch | NotoSans-Medium.ttf | Nein | Nein |
| ms | Malaiisch | NotoSans-Medium.ttf | Nein | Nein |
| tl | Tagalog (Filipino) | NotoSans-Medium.ttf | Nein | Nein |
| sw | Suaheli | NotoSans-Medium.ttf | Nein | Nein |
| hu | Ungarisch | NotoSans-Medium.ttf | Nein | Nein |
| cs | Tschechisch | NotoSans-Medium.ttf | Nein | Nein |
| sk | Slowakisch | NotoSans-Medium.ttf | Nein | Nein |
| ro | Rumänisch | NotoSans-Medium.ttf | Nein | Nein |
| bg | Bulgarisch | NotoSans-Medium.ttf | Nein | Nein |
| sr | Serbisch (kyrillisch) | NotoSans-Medium.ttf | Nein | Nein |
| hr | Kroatisch | NotoSans-Medium.ttf | Nein | Nein |
| sl | Slowenisch | NotoSans-Medium.ttf | Nein | Nein |
| uk | Ukrainisch | NotoSans-Medium.ttf | Nein | Nein |
| my | Birmanisch (Myanmar) | NotoSansMyanmar-Medium.ttf | Nein | Nein |
| ta | Tamil | NotoSansTamil-Medium.ttf | Nein | Nein |
| et | Estnisch | NotoSans-Medium.ttf | Nein | Nein |
| pcm | Nigerianisches Pidgin | NotoSans-Medium.ttf | Nein | Nein |
| te | Telugu | NotoSans-Medium.ttf | Nein | Nein |
| ml | Malayalam | NotoSans-Medium.ttf | Nein | Nein |
| kn | Kannada | NotoSans-Medium.ttf | Nein | Nein |
| km | Khmer | NotoSansKhmer-Medium.ttf | Nein | Nein |

## Sprache hinzufügen

Um Unterstützung für eine neue Sprache hinzuzufügen:

1. Fügen Sie den Sprachcode und den Anzeigenamen zu den Sprach-Utilities hinzu.
2. Fügen Sie eine Schriftart hinzu oder ordnen Sie sie in `src/co_op_translator/fonts/font_language_mappings.yml` zu.
3. Testen Sie die Ausgabe von Markdown- und Bildübersetzungen.
4. Öffnen Sie einen Pull Request mit der Zuordnung und den Validierungsnotizen.