# Idiomas Suportados

Co-op Translator suporta os seguintes códigos de idioma para as saídas de tradução de texto, notebooks e imagens.

Se você quiser adicionar um novo idioma, atualize os mapeamentos de idioma e fonte em `src/co_op_translator/fonts/` e teste o idioma antes de abrir um pull request.

| Código do Idioma | Nome do Idioma | Fonte | Suporte RTL | Problemas Conhecidos |
| --- | --- | --- | --- | --- |
| en | Inglês | NotoSans-Medium.ttf | Não | Não |
| fr | Francês | NotoSans-Medium.ttf | Não | Não |
| es | Espanhol | NotoSans-Medium.ttf | Não | Não |
| de | Alemão | NotoSans-Medium.ttf | Não | Não |
| ru | Russo | NotoSans-Medium.ttf | Não | Não |
| ar | Árabe | NotoSansArabic-Medium.ttf | Sim | Não |
| fa | Persa (Farsi) | NotoSansArabic-Medium.ttf | Sim | Não |
| ur | Urdu | NotoSansArabic-Medium.ttf | Sim | Não |
| zh-CN | Chinês (Simplificado) | NotoSansCJK-Medium.ttc | Não | Não |
| zh-MO | Chinês (Tradicional, Macau) | NotoSansCJK-Medium.ttc | Não | Não |
| zh-HK | Chinês (Tradicional, Hong Kong) | NotoSansCJK-Medium.ttc | Não | Não |
| zh-TW | Chinês (Tradicional, Taiwan) | NotoSansCJK-Medium.ttc | Não | Não |
| ja | Japonês | NotoSansCJK-Medium.ttc | Não | Não |
| ko | Coreano | NotoSansCJK-Medium.ttc | Não | Não |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Não | Não |
| bn | Bengalês | NotoSansBengali-Medium.ttf | Não | Não |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Não | Não |
| ne | Nepalês | NotoSansDevanagari-Medium.ttf | Não | Não |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Não | Não |
| pt-PT | Português (Portugal) | NotoSans-Medium.ttf | Não | Não |
| pt-BR | Português (Brasil) | NotoSans-Medium.ttf | Não | Não |
| it | Italiano | NotoSans-Medium.ttf | Não | Não |
| lt | Lituano | NotoSans-Medium.ttf | Não | Não |
| pl | Polonês | NotoSans-Medium.ttf | Não | Não |
| tr | Turco | NotoSans-Medium.ttf | Não | Não |
| el | Grego | NotoSans-Medium.ttf | Não | Não |
| th | Tailandês | NotoSansThai-Medium.ttf | Não | Não |
| sv | Sueco | NotoSans-Medium.ttf | Não | Não |
| da | Dinamarquês | NotoSans-Medium.ttf | Não | Não |
| no | Norueguês | NotoSans-Medium.ttf | Não | Não |
| fi | Finlandês | NotoSans-Medium.ttf | Não | Não |
| nl | Holandês | NotoSans-Medium.ttf | Não | Não |
| he | Hebraico | NotoSansHebrew-Medium.ttf | Sim | Não |
| vi | Vietnamita | NotoSans-Medium.ttf | Não | Não |
| id | Indonésio | NotoSans-Medium.ttf | Não | Não |
| ms | Malaio | NotoSans-Medium.ttf | Não | Não |
| tl | Tagalog (Filipino) | NotoSans-Medium.ttf | Não | Não |
| sw | Suaíli | NotoSans-Medium.ttf | Não | Não |
| hu | Húngaro | NotoSans-Medium.ttf | Não | Não |
| cs | Tcheco | NotoSans-Medium.ttf | Não | Não |
| sk | Eslovaco | NotoSans-Medium.ttf | Não | Não |
| ro | Romeno | NotoSans-Medium.ttf | Não | Não |
| bg | Búlgaro | NotoSans-Medium.ttf | Não | Não |
| sr | Sérvio (Cirílico) | NotoSans-Medium.ttf | Não | Não |
| hr | Croata | NotoSans-Medium.ttf | Não | Não |
| sl | Esloveno | NotoSans-Medium.ttf | Não | Não |
| uk | Ucraniano | NotoSans-Medium.ttf | Não | Não |
| my | Birmanês (Myanmar) | NotoSansMyanmar-Medium.ttf | Não | Não |
| ta | Tâmil | NotoSansTamil-Medium.ttf | Não | Não |
| et | Estoniano | NotoSans-Medium.ttf | Não | Não |
| pcm | Pidgin Nigeriano | NotoSans-Medium.ttf | Não | Não |
| te | Telugu | NotoSans-Medium.ttf | Não | Não |
| ml | Malayalam | NotoSans-Medium.ttf | Não | Não |
| kn | Canarês | NotoSans-Medium.ttf | Não | Não |
| km | Khmer | NotoSansKhmer-Medium.ttf | Não | Não |

## Adicionar um idioma

Para adicionar suporte a um novo idioma:

1. Adicione o código do idioma e o nome de exibição às utilidades de idioma.
2. Adicione ou mapeie uma fonte em `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Teste a saída de tradução de Markdown e imagens.
4. Abra um pull request com o mapeamento e notas de validação.