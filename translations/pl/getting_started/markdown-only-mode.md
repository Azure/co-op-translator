<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:39:54+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "pl"
}
-->
# Tryb wyłącznie Markdown

## Wprowadzenie
Tryb wyłącznie Markdown został stworzony, aby tłumaczyć tylko zawartość Markdown Twojego projektu. Ten tryb pomija proces tłumaczenia obrazów i koncentruje się wyłącznie na treści tekstowej, co czyni go idealnym w sytuacjach, gdy tłumaczenie obrazów nie jest wymagane lub nie są ustawione odpowiednie zmienne środowiskowe dla Computer Vision.

## Kiedy używać
- Gdy zmienne środowiskowe związane z Computer Vision nie są skonfigurowane.
- Gdy chcesz przetłumaczyć tylko tekst bez aktualizacji linków do obrazów.
- Gdy użytkownik wyraźnie wskazuje to za pomocą opcji `-md` w wierszu poleceń.

## Jak włączyć
Aby aktywować tryb wyłącznie Markdown, użyj opcji `-md` w swoim poleceniu. Na przykład:
```
translate -l "ko" -md
```

Lub jeśli zmienne środowiskowe związane z Computer Vision nie są skonfigurowane. Uruchomienie `translate -l "ko"` automatycznie przełączy na tryb wyłącznie Markdown.

```
translate -l "ko"
```

To polecenie tłumaczy zawartość Markdown na język koreański i pozostawia linki do obrazów bez zmian, wskazując na ich oryginalne ścieżki, zamiast modyfikować je na ścieżki do przetłumaczonych obrazów.

## Zachowanie
W trybie wyłącznie Markdown:
- Proces tłumaczenia pomija etap tłumaczenia obrazów.
- Linki do obrazów w Markdown pozostają niezmienione, wskazując na oryginalne ścieżki.

## Przykłady
### Przed
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.pl.png)
```
### Po użyciu trybu wyłącznie Markdown
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.pl.png)
```

## Rozwiązywanie problemów
- Upewnij się, że opcja `-md` jest poprawnie podana w poleceniu.
- Sprawdź, czy żadna zmienna środowiskowa związana z Computer Vision nie zakłóca procesu.

## Podsumowanie
Tryb wyłącznie Markdown oferuje uproszczony sposób tłumaczenia treści tekstowej bez zmiany linków do obrazów. Jest szczególnie przydatny, gdy tłumaczenie obrazów nie jest potrzebne lub gdy pracujesz w środowiskach bez konfiguracji Computer Vision.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uważać za źródło autorytatywne. W przypadku istotnych informacji zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.