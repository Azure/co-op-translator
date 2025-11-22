<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a7150216aa3c2d191135358fa6dd21",
  "translation_date": "2025-11-22T05:59:01+00:00",
  "source_file": "getting_started/update-other-courses.md",
  "language_code": "te"
}
-->
# "ఇతర కోర్సులు" విభాగాన్ని నవీకరించండి (Microsoft Beginners repos)

ఈ గైడ్ "ఇతర కోర్సులు" విభాగాన్ని Co‑op Translator ఉపయోగించి ఆటో‑సింక్రనైజ్ చేయడం ఎలా చేయాలో మరియు అన్ని repos కోసం గ్లోబల్ టెంప్లేట్‌ను ఎలా నవీకరించాలో వివరిస్తుంది.

- వర్తిస్తుంది: Microsoft Beginners repositories మాత్రమే
- పనిచేస్తుంది: Co‑op Translator CLI మరియు GitHub Actions
- టెంప్లేట్ మూలం: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## త్వరిత ప్రారంభం: మీ repo లో ఆటో‑సింక్‌ను ప్రారంభించండి

మీ README లో "ఇతర కోర్సులు" విభాగం చుట్టూ క్రింది మార్కర్లను జోడించండి. Co‑op Translator ప్రతి రన్ లో ఈ మార్కర్ల మధ్య ఉన్న ప్రతిదాన్ని మార్చుతుంది.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ప్రతి సారి Co‑op Translator CLI (ఉదాహరణకు, `translate -l "<language codes>"`) లేదా GitHub Actions ద్వారా రన్ చేసినప్పుడు, ఈ మార్కర్లతో చుట్టబడిన "ఇతర కోర్సులు" విభాగాన్ని ఆటోమేటిక్‌గా నవీకరిస్తుంది.

> [!NOTE]
> మీకు ఇప్పటికే ఉన్న జాబితా ఉంటే, దానిని అదే మార్కర్లతో చుట్టండి. తదుపరి రన్ తాజా ప్రమాణీకృత కంటెంట్‌తో దానిని మార్చుతుంది.

---

## గ్లోబల్ కంటెంట్‌ను ఎలా మార్చాలి

అన్ని Beginners repos లో కనిపించే ప్రమాణీకృత కంటెంట్‌ను మీరు నవీకరించాలనుకుంటే:

1. టెంప్లేట్‌ను ఎడిట్ చేయండి: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. మీ మార్పులతో Co-op Translator repo కు ఒక pull request ఓపెన్ చేయండి
3. PR మర్జ్ అయిన తర్వాత, Co‑op Translator వెర్షన్ నవీకరించబడుతుంది
4. టార్గెట్ repo లో Co‑op Translator (CLI లేదా GitHub Action) తదుపరి రన్ సమయంలో, నవీకరించిన విభాగం ఆటోమేటిక్‌గా సింక్ అవుతుంది

ఇది అన్ని Beginners repositories లో "ఇతర కోర్సులు" కంటెంట్ కోసం ఒకే మూలం సత్యాన్ని నిర్ధారిస్తుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:  
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏదైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->