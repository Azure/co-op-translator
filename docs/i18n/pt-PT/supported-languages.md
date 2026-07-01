# Idiomas suportados

O Co-op Translator suporta os seguintes códigos de idioma para traduções de texto, notebooks e imagens.

Se quiser adicionar um novo idioma, atualize os mapeamentos de idioma e fontes em `src/co_op_translator/fonts/` e teste o idioma antes de abrir um pull request.

| Language Code | Language Name | Font | RTL Support | Known Issues |
| --- | --- | --- | --- | --- |
| en | Inglês | NotoSans-Medium.ttf | Não | Nenhum |
| fr | Francês | NotoSans-Medium.ttf | Não | Nenhum |
| es | Espanhol | NotoSans-Medium.ttf | Não | Nenhum |
| de | Alemão | NotoSans-Medium.ttf | Não | Nenhum |
| ru | Russo | NotoSans-Medium.ttf | Não | Nenhum |
| ar | Árabe | NotoSansArabic-Medium.ttf | Sim | Nenhum |
| fa | Persa (Farsi) | NotoSansArabic-Medium.ttf | Sim | Nenhum |
| ur | Urdu | NotoSansArabic-Medium.ttf | Sim | Nenhum |
| zh-CN | Chinês (Simplificado) | NotoSansCJK-Medium.ttc | Não | Nenhum |
| zh-MO | Chinês (Tradicional, Macau) | NotoSansCJK-Medium.ttc | Não | Nenhum |
| zh-HK | Chinês (Tradicional, Hong Kong) | NotoSansCJK-Medium.ttc | Não | Nenhum |
| zh-TW | Chinês (Tradicional, Taiwan) | NotoSansCJK-Medium.ttc | Não | Nenhum |
| ja | Japonês | NotoSansCJK-Medium.ttc | Não | Nenhum |
| ko | Coreano | NotoSansCJK-Medium.ttc | Não | Nenhum |
| hi | Hindi | NotoSansDevanagari-Medium.ttf | Não | Nenhum |
| bn | Bengalês | NotoSansBengali-Medium.ttf | Não | Nenhum |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Não | Nenhum |
| ne | Nepalês | NotoSansDevanagari-Medium.ttf | Não | Nenhum |
| pa | Punjabi (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Não | Nenhum |
| pt-PT | Português (Portugal) | NotoSans-Medium.ttf | Não | Nenhum |
| pt-BR | Português (Brasil) | NotoSans-Medium.ttf | Não | Nenhum |
| it | Italiano | NotoSans-Medium.ttf | Não | Nenhum |
| lt | Lituano | NotoSans-Medium.ttf | Não | Nenhum |
| pl | Polaco | NotoSans-Medium.ttf | Não | Nenhum |
| tr | Turco | NotoSans-Medium.ttf | Não | Nenhum |
| el | Grego | NotoSans-Medium.ttf | Não | Nenhum |
| th | Tailandês | NotoSansThai-Medium.ttf | Não | Nenhum |
| sv | Sueco | NotoSans-Medium.ttf | Não | Nenhum |
| da | Dinamarquês | NotoSans-Medium.ttf | Não | Nenhum |
| no | Norueguês | NotoSans-Medium.ttf | Não | Nenhum |
| fi | Finlandês | NotoSans-Medium.ttf | Não | Nenhum |
| nl | Holandês | NotoSans-Medium.ttf | Não | Nenhum |
| he | Hebraico | NotoSansHebrew-Medium.ttf | Sim | Nenhum |
| vi | Vietnamita | NotoSans-Medium.ttf | Não | Nenhum |
| id | Indonésio | NotoSans-Medium.ttf | Não | Nenhum |
| ms | Malaio | NotoSans-Medium.ttf | Não | Nenhum |
| tl | Tagalog (Filipino) | NotoSans-Medium.ttf | Não | Nenhum |
| sw | Suaíli | NotoSans-Medium.ttf | Não | Nenhum |
| hu | Húngaro | NotoSans-Medium.ttf | Não | Nenhum |
| cs | Checo | NotoSans-Medium.ttf | Não | Nenhum |
| sk | Eslovaco | NotoSans-Medium.ttf | Não | Nenhum |
| ro | Romeno | NotoSans-Medium.ttf | Não | Nenhum |
| bg | Búlgaro | NotoSans-Medium.ttf | Não | Nenhum |
| sr | Sérvio (Cirílico) | NotoSans-Medium.ttf | Não | Nenhum |
| hr | Croata | NotoSans-Medium.ttf | Não | Nenhum |
| sl | Esloveno | NotoSans-Medium.ttf | Não | Nenhum |
| uk | Ucraniano | NotoSans-Medium.ttf | Não | Nenhum |
| my | Birmanês (Myanmar) | NotoSansMyanmar-Medium.ttf | Não | Nenhum |
| ta | Tâmil | NotoSansTamil-Medium.ttf | Não | Nenhum |
| et | Estónio | NotoSans-Medium.ttf | Não | Nenhum |
| pcm | Pidgin Nigeriano | NotoSans-Medium.ttf | Não | Nenhum |
| te | Telugu | NotoSans-Medium.ttf | Não | Nenhum |
| ml | Malayalam | NotoSans-Medium.ttf | Não | Nenhum |
| kn | Canarês | NotoSans-Medium.ttf | Não | Nenhum |
| km | Khmer | NotoSansKhmer-Medium.ttf | Não | Nenhum |

## Adicionar um idioma

Para adicionar suporte a um novo idioma:

1. Adicione o código de idioma e o nome de exibição às utilidades de idioma.
2. Adicione ou mapeie uma fonte em `src/co_op_translator/fonts/font_language_mappings.yml`.
3. Teste a saída de tradução de Markdown e de imagem.
4. Abra um pull request com o mapeamento e as notas de validação.