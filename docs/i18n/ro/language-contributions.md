# Contribuții pentru îmbunătățiri lingvistice

Cunoștințele tale lingvistice pot contribui la îmbunătățirea Co-op Translator. Începe cu un exemplu, o corecție sugerată și o explicație folosind formularul de feedback pentru traduceri [translation feedback form](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Nu trebuie să scrii cod sau să plătești pentru o rulare a modelului.

## De la un raport la o îmbunătățire comună

1. Un contribuitor furnizează un fragment din sursă, traducerea sa și contextul.
2. Un revizor lingvistic verifică sensul, naturalitatea și dacă sugestia depinde de o anumită localizare sau de un anumit curs.
3. Un menținător decide dacă corecția aparține cursului sursă, unei instrucțiuni lingvistice partajate, configurării terminologiei sau codului de traducere.
4. Pentru o regulă partajată, un menținător compară rezultatele înainte și după schimbare pe exemplul raportat și pe exemple nelegate. Contribuitorii pot revizui aceste rezultate fără a rula instrumentul în mod direct.
5. PR-ul rezultat leagă raportul și creditează persoanele care au furnizat exemplele și revizuirea. Implementarea sau regenerarea în depozitele care le utilizează este un pas separat.

Un raport nu schimbă automat prompturile sau nu regenerează traducerile cursului. Corecțiile specifice unui curs ar trebui să rămână conectate la depozitul cursului. Nu presupuneți că o editare manuală va supraviețui unei retraduceri ulterioare; confirmați comportamentul pentru acel flux de lucru.

## Exemplu existent: linkuri Markdown în japoneză

Fișierul de instrucțiuni pentru japoneză [Japanese instruction file](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) spune modelului să traducă textul linkului păstrând sintaxa Markdown și destinația linkului. De exemplu, un link scris ca `[text](URL)` nu trebuie să devină `「text」（URL）`.

Acesta este un exemplu concret al unei reguli lingvistice, susținut de o ilustrare a ieșirii corecte și incorecte. Nu reprezintă o dovadă că instrucțiunile din prompt garantează singure un Markdown corect.

Generatorul de prompturi Markdown [Markdown prompt builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) încarcă `templates/language/<language_code>.md` folosind un cod de limbă scris cu litere mici și tăiat de spații. Dacă nu există niciun fișier, folosește instrucțiunile comune. Aceasta descrie calea promptului Markdown; nu presupuneți că fiecare imagine sau altă cale de traducere folosește aceleași instrucțiuni.

Testele de prompt [prompt tests](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) verifică că instrucțiunile pentru japoneză sunt incluse. Aceasta verifică asamblarea promptului, nu calitatea traducerii.

## Ce ar trebui să conțină o regulă lingvistică?

Propuneți o corecție îngustă și repetabilă, cu un exemplu din sursă, comportamentul așteptat și un contraexemplu în care regula nu trebuie aplicată. Păstrați sensul, placeholder-urile, codul, URL-urile și structura documentului. Evitați transformarea preferinței de stil a unei singure persoane sau a terminologiei unui singur curs într-o regulă universală.

Implementarea actuală a glosarului [glossary implementation](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) protejează termenii de la traducere. Nu este un dicționar de terminologie sursă–țintă. Discutați comportamentul noii terminologii înainte de a-l promite contribuitorilor.

## Exemplu din comunitate: un raport despre un nume de produs în japoneză

În [report #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 a identificat o traducere în japoneză care a schimbat numele produsului `Co-op Translator` în `Co-op 翻訳`. Raportul a inclus un link către documentul afectat și o captură de ecran, făcând problema ușor de localizat.

Contribuitorul a legat, de asemenea, un PR al cursului aferent [related course PR](https://github.com/microsoft/AZD-for-beginners/pull/109). În discuția din issue, menținătorul a recunoscut raportul și a propus investigarea motivului pentru care numele s-a schimbat, inclusiv protecția terminologiei, comportamentul glosarului și calea de traducere.

Aceasta arată cum un raport mic poate susține investigarea dincolo de o corecție de redactare individuală. Nu este un rezultat verificat înainte/după sau dovada că instrucțiunile pentru linkuri Markdown în japoneză de mai sus au rezolvat această problemă a numelui produsului.

Poți contribui în același mod: împărtășește textul original, traducerea curentă, corecția sugerată și de ce contează. Adaugă un link către document sau o captură de ecran când este util. Nu trebuie să diagnostichezi cauza sau să scrii un prompt înainte de a-l raporta.

## Validare înainte de adoptarea unei reguli

Folosiți aceleași mostre sursă, revizuirea traducătorului, furnizorul/modelul și setările de generare pentru execuțiile de bază și candidate, schimbând doar instrucțiunea propusă. Înregistrați schimbarea efectivă a promptului și rezultatele; repetați exemplele atunci când este nevoie pentru a distinge un efect consistent de variabilitatea ieșirii. Includeți eșecul raportat, contexte contrastante și exemple care deja se traduc corect.

| Exemplu | Sursă/context | Rezultat de referință | Rezultat candidat | Evaluarea recenzorului |
| --- | --- | --- | --- | --- |
| Eșec raportat | De colectat | Neexecutat | Neexecutat | În așteptare |
| Contraexemplu | De colectat | Neexecutat | Neexecutat | În așteptare |
| Exemplu neafectat | De colectat | Neexecutat | Neexecutat | În așteptare |

Verificați invariantele structurale separat de judecățile lingvistice. Un test reușit de încărcare a promptului nu este o evaluare a calității, iar o propoziție exactă așteptată nu este singura traducere validă. Dacă lipsesc contextul, rulările modelului sau revizuirea lingvistică, păstrați propunerea în așteptare în loc să afirmați că problema a fost rezolvată.