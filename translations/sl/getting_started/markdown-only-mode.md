<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:44:07+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "sl"
}
-->
# Markdown-Only Mode භාවිතය

## හැඳින්වීම  
Markdown-only mode යනු ඔබගේ ව්‍යාපෘතියේ Markdown අන්තර්ගතය පමණක් පරිවර්තනය කිරීමට නිර්මාණය කර ඇති ක්‍රමයක් වේ. මෙම ක්‍රමය රූප පරිවර්තන ක්‍රියාවලිය අතහැර, පෙළ අන්තර්ගතය පමණක් මත අවධානය යොමු කරයි. මෙය රූප පරිවර්තනය අවශ්‍ය නොවන හෝ Computer Vision සඳහා අවශ්‍ය පරිසර චර පරාමිතීන් සකසා නොමැති අවස්ථාවන් සඳහා සුදුසු වේ.

## භාවිතා කළ යුතු අවස්ථා  
- Computer Vision සම්බන්ධ පරිසර චර පරාමිතීන් සකසා නොමැති විට.  
- රූප සබැඳි යාවත්කාලීන නොකර පෙළ අන්තර්ගතය පමණක් පරිවර්තනය කිරීමට අවශ්‍ය විට.  
- පරිශීලකයා විසින් `-md` විධාන රේඛා විකල්පය භාවිතා කර පවසා ඇති විට.

## ක්‍රියාත්මක කිරීම  
Markdown-only mode ක්‍රියාත්මක කිරීමට, ඔබේ විධානයේ `-md` විකල්පය භාවිතා කරන්න. උදාහරණයක් ලෙස:  
```
translate -l "ko" -md
```

හෝ Computer Vision සම්බන්ධ පරිසර චර පරාමිතීන් සකසා නොමැති විට `translate -l "ko"` ක්‍රියාවලිය ස්වයංක්‍රීයව Markdown-only mode වෙත මාරු වේ.  

```
translate -l "ko"
```

මෙම විධානය Markdown අන්තර්ගතය කොරියානු භාෂාවට පරිවර්තනය කරයි සහ රූප සබැඳි මුල් මාර්ග වලට යාවත්කාලීන කරයි, පරිවර්තනය කළ රූප මාර්ග වලට නොව.

## හැසිරීම  
Markdown-only mode තුළ:  
- පරිවර්තන ක්‍රියාවලිය රූප පරිවර්තන පියවර අතහැර යයි.  
- Markdown හි රූප සබැඳි වෙනස් නොවී, මුල් මාර්ග වලට පමණක් යොමු වේ.

## උදාහරණ  
### පෙර  
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.sl.png)
```  
### Markdown-only mode භාවිතයෙන් පසුව  
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.sl.png)
```

## ගැටළු විසඳුම්  
- විධානයේ `-md` විකල්පය නිවැරදිව සඳහන් කර ඇති බව තහවුරු කරන්න.  
- Computer Vision පරිසර චර පරාමිතීන් කිසිවක් ක්‍රියාවලියට බාධා නොවන්නේද යන්න පරීක්ෂා කරන්න.

## නිගමනය  
Markdown-only mode යනු රූප සබැඳි වෙනස් කිරීමකින් තොරව පෙළ අන්තර්ගතය පරිවර්තනය කිරීමට පහසු ක්‍රමයක් වේ. රූප පරිවර්තනය අවශ්‍ය නොවන හෝ Computer Vision සකසන පරිසර නොමැති අවස්ථාවන් සඳහා මෙය විශේෂයෙන් ප්‍රයෝජනවත් වේ.

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.