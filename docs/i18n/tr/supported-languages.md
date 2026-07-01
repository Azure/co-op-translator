# Desteklenen Diller

Co-op Translator, metin, defter ve görüntü çeviri çıktıları için aşağıdaki dil kodlarını destekler.

Yeni bir dil eklemek istiyorsanız, `src/co_op_translator/fonts/` altındaki dil ve yazı tipi eşlemelerini güncelleyin ve pull request açmadan önce dili test edin.

| Dil Kodu | Dil Adı | Yazı Tipi | RTL Desteği | Bilinen Sorunlar |
| --- | --- | --- | --- | --- |
| en | İngilizce | NotoSans-Medium.ttf | Hayır | Yok |
| fr | Fransızca | NotoSans-Medium.ttf | Hayır | Yok |
| es | İspanyolca | NotoSans-Medium.ttf | Hayır | Yok |
| de | Almanca | NotoSans-Medium.ttf | Hayır | Yok |
| ru | Rusça | NotoSans-Medium.ttf | Hayır | Yok |
| ar | Arapça | NotoSansArabic-Medium.ttf | Evet | Yok |
| fa | Farsça (Farsi) | NotoSansArabic-Medium.ttf | Evet | Yok |
| ur | Urduca | NotoSansArabic-Medium.ttf | Evet | Yok |
| zh-CN | Çince (Basitleştirilmiş) | NotoSansCJK-Medium.ttc | Hayır | Yok |
| zh-MO | Çince (Geleneksel, Makao) | NotoSansCJK-Medium.ttc | Hayır | Yok |
| zh-HK | Çince (Geleneksel, Hong Kong) | NotoSansCJK-Medium.ttc | Hayır | Yok |
| zh-TW | Çince (Geleneksel, Tayvan) | NotoSansCJK-Medium.ttc | Hayır | Yok |
| ja | Japonca | NotoSansCJK-Medium.ttc | Hayır | Yok |
| ko | Korece | NotoSansCJK-Medium.ttc | Hayır | Yok |
| hi | Hintçe | NotoSansDevanagari-Medium.ttf | Hayır | Yok |
| bn | Bengalce | NotoSansBengali-Medium.ttf | Hayır | Yok |
| mr | Marathi | NotoSansDevanagari-Medium.ttf | Hayır | Yok |
| ne | Nepalce | NotoSansDevanagari-Medium.ttf | Hayır | Yok |
| pa | Pencapça (Gurmukhi) | NotoSansGurmukhi-Medium.ttf | Hayır | Yok |
| pt-PT | Portekizce (Portekiz) | NotoSans-Medium.ttf | Hayır | Yok |
| pt-BR | Portekizce (Brezilya) | NotoSans-Medium.ttf | Hayır | Yok |
| it | İtalyanca | NotoSans-Medium.ttf | Hayır | Yok |
| lt | Litvanca | NotoSans-Medium.ttf | Hayır | Yok |
| pl | Lehçe | NotoSans-Medium.ttf | Hayır | Yok |
| tr | Türkçe | NotoSans-Medium.ttf | Hayır | Yok |
| el | Yunanca | NotoSans-Medium.ttf | Hayır | Yok |
| th | Tayca | NotoSansThai-Medium.ttf | Hayır | Yok |
| sv | İsveççe | NotoSans-Medium.ttf | Hayır | Yok |
| da | Danca | NotoSans-Medium.ttf | Hayır | Yok |
| no | Norveççe | NotoSans-Medium.ttf | Hayır | Yok |
| fi | Fince | NotoSans-Medium.ttf | Hayır | Yok |
| nl | Flemenkçe | NotoSans-Medium.ttf | Hayır | Yok |
| he | İbranice | NotoSansHebrew-Medium.ttf | Evet | Yok |
| vi | Vietnamca | NotoSans-Medium.ttf | Hayır | Yok |
| id | Endonezce | NotoSans-Medium.ttf | Hayır | Yok |
| ms | Malayca | NotoSans-Medium.ttf | Hayır | Yok |
| tl | Tagalog (Filipince) | NotoSans-Medium.ttf | Hayır | Yok |
| sw | Svahili | NotoSans-Medium.ttf | Hayır | Yok |
| hu | Macarca | NotoSans-Medium.ttf | Hayır | Yok |
| cs | Çekçe | NotoSans-Medium.ttf | Hayır | Yok |
| sk | Slovakça | NotoSans-Medium.ttf | Hayır | Yok |
| ro | Rumence | NotoSans-Medium.ttf | Hayır | Yok |
| bg | Bulgarca | NotoSans-Medium.ttf | Hayır | Yok |
| sr | Sırpça (Kiril) | NotoSans-Medium.ttf | Hayır | Yok |
| hr | Hırvatça | NotoSans-Medium.ttf | Hayır | Yok |
| sl | Slovence | NotoSans-Medium.ttf | Hayır | Yok |
| uk | Ukraynaca | NotoSans-Medium.ttf | Hayır | Yok |
| my | Birmanca (Myanmar) | NotoSansMyanmar-Medium.ttf | Hayır | Yok |
| ta | Tamilce | NotoSansTamil-Medium.ttf | Hayır | Yok |
| et | Estonca | NotoSans-Medium.ttf | Hayır | Yok |
| pcm | Nijerya Pidgin | NotoSans-Medium.ttf | Hayır | Yok |
| te | Telugu | NotoSans-Medium.ttf | Hayır | Yok |
| ml | Malayalam | NotoSans-Medium.ttf | Hayır | Yok |
| kn | Kannada | NotoSans-Medium.ttf | Hayır | Yok |
| km | Kmerce | NotoSansKhmer-Medium.ttf | Hayır | Yok |

## Bir Dil Ekle

Yeni bir dil desteği eklemek için:

1. Dil kodunu ve görüntülenen adını dil yardımcı programlarına ekleyin.
2. Bir yazı tipini `src/co_op_translator/fonts/font_language_mappings.yml` dosyasına ekleyin veya eşleyin.
3. Markdown ve görüntü çeviri çıktısını test edin.
4. Eşleme ve doğrulama notlarıyla birlikte bir pull request açın.