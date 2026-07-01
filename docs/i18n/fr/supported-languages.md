# Langues prises en charge

Co-op Translator prend en charge les codes de langues suivants pour les sorties de traduction de texte, de carnets et d'images.

Si vous souhaitez ajouter une nouvelle langue, mettez à jour les mappages de langue et de police sous `src/co_op_translator/fonts/` et testez la langue avant d'ouvrir une pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Anglais | NotoSans-Medium.ttf | Non | Non |
| fr | Français | NotoSans-Medium.ttf | Non | Non |
| es | Espagnol | NotoSans-Medium.ttf | Non | Non |
| de | Allemand | NotoSans-Medium.ttf | Non | Non |
| ru | Russe | NotoSans-Medium.ttf | Non | Non |
| ar | Arabe | NotoSansArabic-Medium.ttf | Oui | Non |
| fa | Persan (Farsi) | NotoSansArabic-Medium.ttf | Oui | Non |
| ur | Ourdou | NotoSansArabic-Medium.ttf | Oui | Non |
| zh-CN | Chinois (simplifié) | NotoSansCJK-Medium.ttc | Non | Non |
| zh-MO | Chinois (traditionnel, Macao) | NotoSansCJK-Medium.ttc | Non | Non |
| zh-HK | Chinois (traditionnel, Hong Kong) | NotoSansCJK-Medium.ttc | Non | Non |
| zh-TW | Chinois (traditionnel, Taïwan) | NotoSansCJK-Medium.ttc | Non | Non |
| ja | Japonais | NotoSansCJK-Medium.ttc | Non | Non |
| ko | Coréen | NotoSansCJK-Medium.ttc | Non | Non |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Non | Non |
| bn | Bengali | NotoSansBengali-Medium.ttf | Non | Non |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Non | Non |
| ne | Népalais | NotoSansDevanagari-Medium.ttf | Non | Non |
| pa | Pendjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Non | Non |
| pt-PT | Portugais (Portugal) | NotoSans-Medium.ttf | Non | Non |
| pt-BR | Portugais (Brésil) | NotoSans-Medium.ttf | Non | Non |
| it | Italien | NotoSans-Medium.ttf | Non | Non |
| lt | Lituanien | NotoSans-Medium.ttf | Non | Non |
| pl | Polonais | NotoSans-Medium.ttf | Non | Non |
| tr | Turc | NotoSans-Medium.ttf | Non | Non |
| el | Grec | NotoSans-Medium.ttf | Non | Non |
| th | Thaï | NotoSansThai-Medium.ttf | Non | Non |
| sv | Suédois | NotoSans-Medium.ttf | Non | Non |
| da | Danois | NotoSans-Medium.ttf | Non | Non |
| no | Norvégien | NotoSans-Medium.ttf | Non | Non |
| fi | Finnois | NotoSans-Medium.ttf | Non | Non |
| nl | Néerlandais | NotoSans-Medium.ttf | Non | Non |
| he | Hébreu | NotoSansHebrew-Medium.ttf | Oui | Non |
| vi | Vietnamien | NotoSans-Medium.ttf | Non | Non |
| id | Indonésien | NotoSans-Medium.ttf | Non | Non |
| ms | Malais | NotoSans-Medium.ttf | Non | Non |
| tl | Tagalog (philippin) | NotoSans-Medium.ttf | Non | Non |
| sw | Swahili | NotoSans-Medium.ttf | Non | Non |
| hu | Hongrois | NotoSans-Medium.ttf | Non | Non |
| cs | Tchèque | NotoSans-Medium.ttf | Non | Non |
| sk | Slovaque | NotoSans-Medium.ttf | Non | Non |
| ro | Roumain | NotoSans-Medium.ttf | Non | Non |
| bg | Bulgare | NotoSans-Medium.ttf | Non | Non |
| sr | Serbe (cyrillique) | NotoSans-Medium.ttf | Non | Non |
| hr | Croate | NotoSans-Medium.ttf | Non | Non |
| sl | Slovène | NotoSans-Medium.ttf | Non | Non |
| uk | Ukrainien | NotoSans-Medium.ttf | Non | Non |
| my | Birman (Myanmar) | NotoSansMyanmar-Medium.ttf | Non | Non |
| ta | Tamoul | NotoSansTamil-Medium.ttf | Non | Non |
| et | Estonien | NotoSans-Medium.ttf | Non | Non |
| pcm | Pidgin nigérian | NotoSans-Medium.ttf | Non | Non |
| te | Télougou | NotoSans-Medium.ttf | Non | Non |
| ml | Malayalam | NotoSans-Medium.ttf | Non | Non |
| kn | Kannada | NotoSans-Medium.ttf | Non | Non |
| km | Khmer | NotoSansKhmer-Medium.ttf | Non | Non |

## Ajouter une langue

Pour ajouter la prise en charge d'une nouvelle langue :

1. Ajoutez le code de langue et le nom d'affichage aux utilitaires de langues.
2. Ajoutez ou associez une police dans `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Testez la sortie de traduction pour Markdown et images.
4. Ouvrez une pull request avec le mappage et les notes de validation.