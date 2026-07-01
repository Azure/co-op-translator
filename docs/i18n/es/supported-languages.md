# Idiomas compatibles

Co-op Translator admite los siguientes códigos de idioma para las salidas de traducción de texto, cuadernos e imágenes.

Si desea agregar un nuevo idioma, actualice las asignaciones de idioma y fuente en `src/co_op_translator/fonts/` y pruebe el idioma antes de abrir una pull request.

| Language Code | Nombre del idioma | Font | Soporte RTL | Problemas conocidos |
| --- | --- | --- | --- | --- |
| en | Inglés | NotoSans-Medium.ttf | No | No |
| fr | Francés | NotoSans-Medium.ttf | No | No |
| es | Español | NotoSans-Medium.ttf | No | No |
| de | Alemán | NotoSans-Medium.ttf | No | No |
| ru | Ruso | NotoSans-Medium.ttf | No | No |
| ar | Árabe | NotoSansArabic-Medium.ttf | Sí | No |
| fa | Persa (Farsi) | NotoSansArabic-Medium.ttf | Sí | No |
| ur | Urdu | NotoSansArabic-Medium.ttf | Sí | No |
| zh-CN | Chino (Simplificado) | NotoSansCJK-Medium.ttc | No | No |
| zh-MO | Chino (Tradicional, Macao) | NotoSansCJK-Medium.ttc | No | No |
| zh-HK | Chino (Tradicional, Hong Kong) | NotoSansCJK-Medium.ttc | No | No |
| zh-TW | Chino (Tradicional, Taiwán) | NotoSansCJK-Medium.ttc | No | No |
| ja | Japonés | NotoSansCJK-Medium.ttc | No | No |
| ko | Coreano | NotoSansCJK-Medium.ttc | No | No |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | No | No |
| bn | Bengalí | NotoSansBengali-Medium.ttf | No | No |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | No | No |
| ne | Nepalí | NotoSansDevanagari-Medium.ttf | No | No |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | No | No |
| pt-PT | Portugués (Portugal) | NotoSans-Medium.ttf | No | No |
| pt-BR | Portugués (Brasil) | NotoSans-Medium.ttf | No | No |
| it | Italiano | NotoSans-Medium.ttf | No | No |
| lt | Lituano | NotoSans-Medium.ttf | No | No |
| pl | Polaco | NotoSans-Medium.ttf | No | No |
| tr | Turco | NotoSans-Medium.ttf | No | No |
| el | Griego | NotoSans-Medium.ttf | No | No |
| th | Tailandés | NotoSansThai-Medium.ttf | No | No |
| sv | Sueco | NotoSans-Medium.ttf | No | No |
| da | Danés | NotoSans-Medium.ttf | No | No |
| no | Noruego | NotoSans-Medium.ttf | No | No |
| fi | Finés | NotoSans-Medium.ttf | No | No |
| nl | Neerlandés | NotoSans-Medium.ttf | No | No |
| he | Hebreo | NotoSansHebrew-Medium.ttf | Sí | No |
| vi | Vietnamita | NotoSans-Medium.ttf | No | No |
| id | Indonesio | NotoSans-Medium.ttf | No | No |
| ms | Malayo | NotoSans-Medium.ttf | No | No |
| tl | Tagalo (Filipino) | NotoSans-Medium.ttf | No | No |
| sw | Swahili | NotoSans-Medium.ttf | No | No |
| hu | Húngaro | NotoSans-Medium.ttf | No | No |
| cs | Checo | NotoSans-Medium.ttf | No | No |
| sk | Eslovaco | NotoSans-Medium.ttf | No | No |
| ro | Rumano | NotoSans-Medium.ttf | No | No |
| bg | Búlgaro | NotoSans-Medium.ttf | No | No |
| sr | Serbio (Cirílico) | NotoSans-Medium.ttf | No | No |
| hr | Croata | NotoSans-Medium.ttf | No | No |
| sl | Esloveno | NotoSans-Medium.ttf | No | No |
| uk | Ucraniano | NotoSans-Medium.ttf | No | No |
| my | Birmano (Myanmar) | NotoSansMyanmar-Medium.ttf | No | No |
| ta | Tamil | NotoSansTamil-Medium.ttf | No | No |
| et | Estonio | NotoSans-Medium.ttf | No | No |
| pcm | Pidgin nigeriano | NotoSans-Medium.ttf | No | No |
| te | Telugu | NotoSans-Medium.ttf | No | No |
| ml | Malayalam | NotoSans-Medium.ttf | No | No |
| kn | Canarés | NotoSans-Medium.ttf | No | No |
| km | Jemer | NotoSansKhmer-Medium.ttf | No | No |

## Añadir un idioma

Para agregar soporte para un nuevo idioma:

1. Añada el código de idioma y el nombre para mostrar a las utilidades de idioma.
2. Agregue o asigne una fuente en `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Pruebe la salida de traducción de Markdown e imágenes.
4. Abra una pull request con el mapeo y las notas de validación.