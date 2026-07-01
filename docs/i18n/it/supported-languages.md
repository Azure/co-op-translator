# Lingue supportate

Co-op Translator supporta i seguenti codici lingua per le traduzioni di testo, notebook e immagini.

Se vuoi aggiungere una nuova lingua, aggiorna le mappature di lingua e font sotto `src/co_op_translator/fonts/` e testa la lingua prima di aprire una pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Inglese | NotoSans-Medium.ttf | No | No |
| fr | Francese | NotoSans-Medium.ttf | No | No |
| es | Spagnolo | NotoSans-Medium.ttf | No | No |
| de | Tedesco | NotoSans-Medium.ttf | No | No |
| ru | Russo | NotoSans-Medium.ttf | No | No |
| ar | Arabo | NotoSansArabic-Medium.ttf | Sì | No |
| fa | Persiano (Farsi) | NotoSansArabic-Medium.ttf | Sì | No |
| ur | Urdu | NotoSansArabic-Medium.ttf | Sì | No |
| zh-CN | Cinese (semplicificato) | NotoSansCJK-Medium.ttc | No | No |
| zh-MO | Cinese (tradizionale, Macao) | NotoSansCJK-Medium.ttc | No | No |
| zh-HK | Cinese (tradizionale, Hong Kong) | NotoSansCJK-Medium.ttc | No | No |
| zh-TW | Cinese (tradizionale, Taiwan) | NotoSansCJK-Medium.ttc | No | No |
| ja | Giapponese | NotoSansCJK-Medium.ttc | No | No |
| ko | Coreano | NotoSansCJK-Medium.ttc | No | No |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | No | No |
| bn | Bengalese | NotoSansBengali-Medium.ttf | No | No |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | No | No |
| ne | Nepalese | NotoSansDevanagari-Medium.ttf | No | No |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | No | No |
| pt-PT | Portoghese (Portogallo) | NotoSans-Medium.ttf | No | No |
| pt-BR | Portoghese (Brasile) | NotoSans-Medium.ttf | No | No |
| it | Italiano | NotoSans-Medium.ttf | No | No |
| lt | Lituano | NotoSans-Medium.ttf | No | No |
| pl | Polacco | NotoSans-Medium.ttf | No | No |
| tr | Turco | NotoSans-Medium.ttf | No | No |
| el | Greco | NotoSans-Medium.ttf | No | No |
| th | Thailandese | NotoSansThai-Medium.ttf | No | No |
| sv | Svedese | NotoSans-Medium.ttf | No | No |
| da | Danese | NotoSans-Medium.ttf | No | No |
| no | Norvegese | NotoSans-Medium.ttf | No | No |
| fi | Finlandese | NotoSans-Medium.ttf | No | No |
| nl | Olandese | NotoSans-Medium.ttf | No | No |
| he | Ebraico | NotoSansHebrew-Medium.ttf | Sì | No |
| vi | Vietnamita | NotoSans-Medium.ttf | No | No |
| id | Indonesiano | NotoSans-Medium.ttf | No | No |
| ms | Malese | NotoSans-Medium.ttf | No | No |
| tl | Tagalog (Filippino) | NotoSans-Medium.ttf | No | No |
| sw | Swahili | NotoSans-Medium.ttf | No | No |
| hu | Ungherese | NotoSans-Medium.ttf | No | No |
| cs | Ceco | NotoSans-Medium.ttf | No | No |
| sk | Slovacco | NotoSans-Medium.ttf | No | No |
| ro | Rumeno | NotoSans-Medium.ttf | No | No |
| bg | Bulgaro | NotoSans-Medium.ttf | No | No |
| sr | Serbo (Cirillico) | NotoSans-Medium.ttf | No | No |
| hr | Croato | NotoSans-Medium.ttf | No | No |
| sl | Sloveno | NotoSans-Medium.ttf | No | No |
| uk | Ucraino | NotoSans-Medium.ttf | No | No |
| my | Birmano (Myanmar) | NotoSansMyanmar-Medium.ttf | No | No |
| ta | Tamil | NotoSansTamil-Medium.ttf | No | No |
| et | Estone | NotoSans-Medium.ttf | No | No |
| pcm | Pidgin nigeriano | NotoSans-Medium.ttf | No | No |
| te | Telugu | NotoSans-Medium.ttf | No | No |
| ml | Malayalam | NotoSans-Medium.ttf | No | No |
| kn | Kannada | NotoSans-Medium.ttf | No | No |
| km | Khmer | NotoSansKhmer-Medium.ttf | No | No |

## Aggiungere una lingua

Per aggiungere il supporto per una nuova lingua:

1. Aggiungi il codice lingua e il nome visualizzato alle utility delle lingue.
2. Aggiungi o mappa un font in `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Testa l'output della traduzione per Markdown e immagini.
4. Apri una pull request con la mappatura e le note di convalida.