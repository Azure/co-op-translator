# Wnoszenie poprawek językowych

Twoja znajomość języka może pomóc ulepszyć Co-op Translator. Zacznij od przykładu, proponowanej poprawki i wyjaśnienia za pomocą [formularza opinii o tłumaczeniu](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). Nie musisz pisać kodu ani opłacać uruchomienia modelu.

## Od zgłoszenia do wspólnej poprawy

1. Współautor dostarcza fragment źródłowy, jego tłumaczenie i kontekst.
2. Recenzent językowy sprawdza znaczenie, naturalność oraz czy sugestia zależy od konkretnej lokalizacji lub kursu.
3. Opiekun decyduje, czy poprawka należy do kursu źródłowego, wspólnej instrukcji językowej, konfiguracji terminologii czy kodu tłumaczeń.
4. Dla reguły wspólnej opiekun porównuje wyniki przed i po zmianie na zgłoszonym przykładzie oraz na niezwiązanych przykładach. Współautorzy mogą przejrzeć te wyniki bez uruchamiania narzędzia samodzielnie.
5. Powstały PR łączy raport i wyróżnia osoby, które dostarczyły przykłady i przeprowadziły recenzję. Wdrożenie lub regeneracja w repozytoriach korzystających to osobny krok.

Zgłoszenie nie powoduje automatycznej zmiany promptów ani regeneracji tłumaczeń kursu. Poprawki specyficzne dla kursu powinny pozostać powiązane z repozytorium kursu. Nie zakładaj, że ręczna edycja przetrwa późniejsze ponowne tłumaczenie; potwierdź zachowanie dla tego przebiegu pracy.

## Istniejący przykład: japońskie linki Markdown

Plik instrukcji japońskiego](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) nakazuje modelowi tłumaczyć tekst linku przy zachowaniu składni Markdown i docelowego adresu linku. Na przykład, link zapisany jako `[text](URL)` nie powinien stać się `「text」（URL）`.

To jest skoncentrowany przykład reguły językowej poparty ilustracją poprawnego i błędnego wyniku. Nie jest to dowód, że same instrukcje w promptach gwarantują poprawny Markdown.

Kreator promptów Markdown](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) ładuje `templates/language/<language_code>.md` używając kodu języka zapisanego małymi literami i pozbawionego spacji. Jeśli plik nie istnieje, używa instrukcji wspólnych. To opisuje ścieżkę promptu Markdown; nie zakładaj, że każdy obraz lub inna ścieżka tłumaczenia używa tych samych instrukcji.

Testy promptów](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) sprawdzają, czy instrukcje japońskie zostały dołączone. To weryfikuje składanie promptu, a nie jakość tłumaczenia.

## Co należy uwzględnić w regule językowej?

Zaproponuj wąską, powtarzalną poprawkę z przykładem źródłowym, oczekiwanym zachowaniem oraz kontrprzykładem, w którym reguła nie powinna mieć zastosowania. Zachowaj znaczenie, znaczniki zastępcze, kod, adresy URL i strukturę dokumentu. Unikaj przekształcania czyjejś preferencji stylu lub terminologii jednego kursu w regułę uniwersalną.

Aktualna implementacja glosariusza](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) chroni terminy przed tłumaczeniem. Nie jest to słownik tłumaczeń terminologii (źródło→cel). Omów nowe zachowanie terminologii zanim obiecasz je współautorom.

## Przykład od społeczności: japońskie zgłoszenie dotyczące nazwy produktu

W [raporcie #527](https://github.com/Azure/co-op-translator/issues/527) @hyoshioka0128 zidentyfikował japońskie tłumaczenie, które zmieniło nazwę produktu `Co-op Translator` na `Co-op 翻訳`. Raport zawierał link do dotkniętego dokumentu i zrzut ekranu, co ułatwiło zlokalizowanie problemu.

Współautor dołączył także [powiązany PR kursu](https://github.com/microsoft/AZD-for-beginners/pull/109). W dyskusji w sprawie opiekun potwierdził otrzymanie raportu i zaproponował zbadanie, dlaczego nazwa się zmieniła, włączając ochronę terminologii, zachowanie glosariusza oraz ścieżkę tłumaczenia.

To pokazuje, jak mały raport może wspierać badania wykraczające poza pojedynczą korektę sformułowania. Nie jest to zweryfikowany wynik przed/po ani dowód, że powyższe instrukcje dotyczące japońskich linków Markdown naprawiły problem z nazwą produktu.

Możesz przyczynić się w ten sam sposób: udostępnij oryginalny tekst, aktualne tłumaczenie, proponowaną poprawkę i wyjaśnienie, dlaczego to ma znaczenie. Dodaj link do dokumentu lub zrzut ekranu, gdy to przydatne. Nie musisz diagnozować przyczyny ani pisać promptu przed zgłoszeniem.

## Walidacja przed przyjęciem reguły

Używaj tych samych próbek źródłowych, rewizji tłumacza, dostawcy/modelu i ustawień generowania dla przebiegów bazowych i kandydujących, zmieniając jedynie proponowaną instrukcję. Zarejestruj rzeczywistą zmianę promptu i wyniki; powtarzaj przykłady w razie potrzeby, aby odróżnić stały efekt od zmienności wyników. Dołącz zgłoszoną awarię, kontrastujące konteksty oraz przykłady, które już tłumaczą się poprawnie.

| Przykład | Źródło/kontekst | Wynik bazowy | Wynik kandydujący | Ocena recenzenta |
| --- | --- | --- | --- | --- |
| Zgłoszony błąd | Do zebrania | Nie uruchomiono | Nie uruchomiono | Oczekuje |
| Kontrprzykład | Do zebrania | Nie uruchomiono | Nie uruchomiono | Oczekuje |
| Przykład niepodlegający zmianie | Do zebrania | Nie uruchomiono | Nie uruchomiono | Oczekuje |

Sprawdzaj niezmienniki strukturalne oddzielnie od sądów językowych. Udany test ładowania promptu nie jest oceną jakości, a jedno dokładne oczekiwane zdanie nie jest jedynym poprawnym tłumaczeniem. Jeśli brakuje kontekstu, uruchomień modelu lub przeglądu językowego, zostaw propozycję w stanie oczekującym, zamiast twierdzić, że problem został rozwiązany.