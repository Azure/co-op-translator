<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:42:19+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "tl"
}
-->
# Paggamit ng Markdown-Only Mode

## Panimula  
Ang markdown-only mode ay dinisenyo upang isalin lamang ang Markdown na nilalaman ng iyong proyekto. Nilalaktawan nito ang proseso ng pagsasalin ng mga larawan at nakatuon lamang sa tekstwal na nilalaman, kaya't mainam ito para sa mga sitwasyong hindi kailangan ang pagsasalin ng mga larawan o kapag hindi naka-set ang mga kinakailangang environment variables para sa Computer Vision.

## Kailan Gagamitin  
- Kapag hindi naka-configure ang mga environment variables na may kinalaman sa Computer Vision.  
- Kapag nais mong isalin lamang ang tekstwal na nilalaman nang hindi ina-update ang mga link ng larawan.  
- Kapag tahasang tinukoy ng user gamit ang `-md` na command-line option.

## Paano I-activate  
Upang paganahin ang markdown-only mode, gamitin ang `-md` na option sa iyong command. Halimbawa:  
```
translate -l "ko" -md
```

O kung hindi naka-configure ang mga environment variables na may kinalaman sa Computer Vision. Ang pagpapatakbo ng `translate -l "ko"` ay awtomatikong maglilipat sa markdown-only mode.

```
translate -l "ko"
```

Isinasaad ng command na ito na isasalin ang nilalaman ng Markdown sa Korean at ia-update ang mga link ng larawan sa kanilang orihinal na mga path, sa halip na baguhin ito sa mga path ng isinaling larawan.

## Pag-uugali  
Sa markdown-only mode:  
- Nilalaktawan ng proseso ng pagsasalin ang hakbang ng pagsasalin ng mga larawan.  
- Nanatiling hindi nababago ang mga link ng larawan sa Markdown, na tumuturo sa kanilang orihinal na mga path.

## Mga Halimbawa  
### Bago  
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.tl.png)
```  
### Pagkatapos gamitin ang markdown-only mode  
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.tl.png)
```

## Pag-aayos ng Problema  
- Siguraduhing tama ang pagtukoy sa `-md` option sa command.  
- Tiyakin na walang mga environment variables ng Computer Vision na nakakaapekto sa proseso.

## Konklusyon  
Nagbibigay ang markdown-only mode ng mas pinadaling paraan upang isalin ang tekstwal na nilalaman nang hindi binabago ang mga link ng larawan. Partikular itong kapaki-pakinabang kapag hindi kailangan ang pagsasalin ng larawan o kapag nagtatrabaho sa mga environment na walang setup para sa Computer Vision.

**Pagsasalin**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.