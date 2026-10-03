# Pag-aambag ng mga pagpapabuti sa wika

Ang iyong kaalaman sa wika ay makakatulong upang mapabuti ang Co-op Translator. Magsimula sa isang halimbawa, isang mungkahing pagwawasto, at isang paliwanag gamit ang [formularyo ng puna sa pagsasalin](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Hindi mo kailangang magsulat ng code o magbayad para sa pagpapatakbo ng modelo.

## Mula sa isang ulat hanggang sa isang pinagbahaging pagpapabuti

1. Nagbibigay ang isang kontribyutor ng isang sipi ng pinagmulan, ang pagsasalin nito, at ang konteksto.
2. Sinusuri ng tagasuri ng wika ang kahulugan, pagiging natural, at kung naka-depende ang mungkahi sa isang partikular na lokalidad o kurso.
3. Nagpapasya ang tagapanatili kung ang pagwawasto ay nararapat ilagay sa source na kurso, sa pinagbahaging instruksyon sa wika, sa konfigurasyon ng terminolohiya, o sa code ng pagsasalin.
4. Para sa isang pinagbahaging patakaran, inihahambing ng tagapanatili ang mga output bago at pagkatapos ng pagbabago para sa iniulat na halimbawa at sa hindi kaugnay na mga halimbawa. Maaaring suriin ng mga kontribyutor ang mga output na ito nang hindi na nila pinapatakbo ang tool.
5. Naglalaman ang nagresultang PR ng link ng ulat at kinikilala ang mga taong nagbigay ng mga halimbawa at nagsagawa ng pagsusuri. Ang deployment o muling pagbuo sa mga repositoryong gumagamit ay isang hiwalay na hakbang.

Ang isang ulat ay hindi awtomatikong nagbabago ng mga prompt o muling nagbuo ng mga pagsasalin ng kurso. Ang mga pagwawasto na partikular sa kurso ay dapat manatiling konektado sa repositoryo ng kurso. Huwag ipagpalagay na ang isang manual na pag-edit ay mananatili pagkatapos ng muling pagsasalin; tiyakin ang gawi para sa workflow na iyon.

## Umiiral na halimbawa: Mga Markdown link sa Hapones

Ang [file ng instruksyon sa Hapones](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) ay nagsasabi sa modelo na isalin ang teksto ng link habang pinapangalagaan ang sintaks ng Markdown at ang destinasyon ng link. Halimbawa, ang isang link na nakasulat bilang `[text](URL)` ay hindi dapat maging `「text」（URL）`.

Ito ay isang naka-pokus na halimbawa ng isang patakaran sa wika na sinusuportahan ng ilustrasyon ng tamang at maling output. Hindi ito ebidensya na ang mga instruksyon ng prompt lamang ang magagarantiya ng tamang Markdown.

Ang [tagabuo ng Markdown prompt](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) ay naglo-load ng `templates/language/<language_code>.md` gamit ang code ng wika na naka-lowercase at na-trim. Kung walang file, ginagamit nito ang pangkaraniwang mga instruksyon. Inilalarawan nito ang path ng Markdown prompt; huwag ipagpalagay na ang bawat imahe o ibang path ng pagsasalin ay gumagamit ng parehong mga instruksyon.

Sinusuri ng [prompt tests](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) na kasama ang mga instruksyon para sa Hapon. Pinatutunayan nito ang pagsasama ng prompt, hindi ang kalidad ng pagsasalin.

## Ano ang dapat nasa isang patakaran sa wika?

Magmungkahi ng isang makitid at paulit-ulit na pagwawasto na mayroong halimbawa mula sa pinagmulan, inaasahang pag-uugali, at isang kontra-halimbawa kung saan hindi dapat ilapat ang patakaran. Panatilihin ang kahulugan, mga placeholder, code, URL, at istraktura ng dokumento. Iwasang gawing pangkalahatan ang personal na kagustuhan sa estilo ng isang tao o ang terminolohiya ng isang kurso.

Pinoprotektahan ng kasalukuyang [implementasyon ng glosaryo](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) ang mga termino mula sa pagsasalin. Hindi ito isang diksyunaryo ng terminolohiya mula sa pinagmulan papunta sa target. Talakayin muna ang bagong pag-uugali ng terminolohiya bago ito ipangako sa mga kontribyutor.

## Halimbawang pang-komunidad: isang ulat tungkol sa pangalan ng produkto sa Hapones

Sa [report #527](https://github.com/Azure/co-op-translator/issues/527), tinukoy ni @hyoshioka0128 ang isang pagsasaling Hapones na binago ang pangalan ng produkto `Co-op Translator` sa `Co-op 翻訳`. Naglaman ang ulat ng link sa apektadong dokumento at isang screenshot, na nagpapadali sa paghahanap ng problema.

Nag-link din ang kontribyutor ng isang [related course PR](https://github.com/microsoft/AZD-for-beginners/pull/109). Sa talakayan ng isyu, kinilala ng tagapanatili ang ulat at iminungkahi na siyasatin kung bakit nagbago ang pangalan, kabilang ang proteksyon ng terminolohiya, ugali ng glosaryo, at ang path ng pagsasalin.

Ipinapakita nito kung paano ang isang maliit na ulat ay maaaring sumuporta sa pagsisiyasat na lampas sa isang indibidwal na pagwawasto ng pagkakasulat. Hindi ito isang beripikadong resulta bago/pagkatapos o ebidensya na ang mga instruksyon sa Japanese Markdown-link sa itaas ay nag-ayos ng isyu sa pangalan ng produkto.

Maaari kang mag-ambag sa parehong paraan: ibahagi ang orihinal na teksto, ang kasalukuyang pagsasalin, ang mungkahing pagwawasto, at kung bakit ito mahalaga. Magdagdag ng link sa dokumento o screenshot kapag kapaki-pakinabang. Hindi mo kailangang siyasatin ang sanhi o magsulat ng prompt bago iulat ito.

## Pagpapatunay bago tanggapin ang isang patakaran

Gamitin ang magkaparehong source samples, rebisyon ng tagasalin, provider/model, at mga setting ng pagbuo para sa baseline at kandidatong pagtakbo, na binabago lamang ang iminungkahing instruksyon. Itala ang aktwal na pagbabago sa prompt at mga output; ulitin ang mga halimbawa kapag kailangan upang makahiwalay ang isang pare-parehong epekto mula sa pagbabagu-bago ng output. Isama ang iniulat na pagkabigo, magkasalungat na mga konteksto, at mga halimbawa na tama nang isinasalin.

| Halimbawa | Pinagmulan/konteksto | Baseline na output | Output ng kandidato | Pagtatasa ng tagasuri |
| --- | --- | --- | --- | --- |
| Iniulat na pagkabigo | Ikokolekta | Hindi pinatakbo | Hindi pinatakbo | Nakahintay |
| Kontra-halimbawa | Ikokolekta | Hindi pinatakbo | Hindi pinatakbo | Nakahintay |
| Hindi apektadong halimbawa | Ikokolekta | Hindi pinatakbo | Hindi pinatakbo | Nakahintay |

Suriin ang mga structural invariant nang hiwalay mula sa mga lingguwistikong hatol. Ang matagumpay na prompt-loading test ay hindi isang evaluasyon ng kalidad, at ang isang eksaktong inaasahang pangungusap ay hindi ang nag-iisang wastong pagsasalin. Kung kulang ang konteksto, mga pagtakbo ng modelo, o pagsusuri ng wika, panatilihing nakabinbin ang panukala sa halip na igiit na naayos na ang isyu.