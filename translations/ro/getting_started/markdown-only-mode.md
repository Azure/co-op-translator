<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:43:21+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "ro"
}
-->
# Modul Doar Markdown

## Introducere
Modul doar Markdown este conceput pentru a traduce doar conținutul Markdown al proiectului tău. Acest mod ocolește procesul de traducere a imaginilor și se concentrează exclusiv pe conținutul textual, fiind ideal pentru situațiile în care traducerea imaginilor nu este necesară sau variabilele de mediu necesare pentru Computer Vision nu sunt configurate.

## Când să folosești
- Când variabilele de mediu legate de Computer Vision nu sunt configurate.
- Când dorești să traduci doar conținutul text fără a actualiza linkurile imaginilor.
- Când este specificat explicit de utilizator prin opțiunea de linie de comandă `-md`.

## Cum să activezi
Pentru a activa modul doar Markdown, folosește opțiunea `-md` în comanda ta. De exemplu:
```
translate -l "ko" -md
```

Sau dacă variabilele de mediu legate de Computer Vision nu sunt configurate. Rulând `translate -l "ko"` se va comuta automat în modul doar Markdown.

```
translate -l "ko"
```

Această comandă traduce conținutul Markdown în coreeană și actualizează linkurile imaginilor către căile lor originale, în loc să le modifice către căi traduse ale imaginilor.

## Comportament
În modul doar Markdown:
- Procesul de traducere ocolește pasul de traducere a imaginilor.
- Linkurile imaginilor din Markdown rămân neschimbate, indicând către căile lor originale.

## Exemple
### Înainte
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.ro.png)
```
### După folosirea modului doar Markdown
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.ro.png)
```

## Depanare
- Asigură-te că opțiunea `-md` este specificată corect în comandă.
- Verifică să nu existe variabile de mediu legate de Computer Vision care să interfereze cu procesul.

## Concluzie
Modul doar Markdown oferă o metodă simplificată de a traduce conținutul text fără a modifica linkurile imaginilor. Este deosebit de util când traducerea imaginilor nu este necesară sau când se lucrează în medii fără configurare Computer Vision.

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.