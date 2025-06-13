<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:41:07+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "no"
}
-->
# Bruke Markdown-Only-modus

## Introduksjon
Markdown-only-modus er designet for å kun oversette Markdown-innholdet i prosjektet ditt. Denne modusen hopper over bildeoversettelsesprosessen og fokuserer kun på tekstinnholdet, noe som gjør den ideell i situasjoner der bildeoversettelse ikke er nødvendig eller de nødvendige miljøvariablene for Computer Vision ikke er satt.

## Når du bør bruke den
- Når miljøvariabler relatert til Computer Vision ikke er konfigurert.
- Når du kun ønsker å oversette tekstinnhold uten å oppdatere bildefilene.
- Når det eksplisitt er spesifisert av brukeren ved bruk av `-md` kommandolinjealternativet.

## Hvordan aktivere
For å aktivere Markdown-only-modus, bruk `-md`-alternativet i kommandoen din. For eksempel:
```
translate -l "ko" -md
```

Eller hvis miljøvariabler relatert til Computer Vision ikke er konfigurert. Å kjøre `translate -l "ko"` vil automatisk bytte til Markdown-only-modus.

```
translate -l "ko"
```

Denne kommandoen oversetter Markdown-innholdet til koreansk og oppdaterer bildefilene til deres opprinnelige stier, i stedet for å endre dem til oversatte bildefilstier.

## Oppførsel
I Markdown-only-modus:
- Oversettelsesprosessen hopper over steget med bildeoversettelse.
- Bildefilene i Markdown forblir uendret og peker til sine opprinnelige stier.

## Eksempler
### Før
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.no.png)
```
### Etter bruk av Markdown-only-modus
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.no.png)
```

## Feilsøking
- Sørg for at `-md`-alternativet er korrekt angitt i kommandoen.
- Kontroller at ingen Computer Vision-miljøvariabler forstyrrer prosessen.

## Konklusjon
Markdown-only-modus tilbyr en effektiv måte å oversette tekstinnhold uten å endre bildefilene. Det er spesielt nyttig når bildeoversettelse ikke er nødvendig eller når man jobber i miljøer uten Computer Vision-oppsett.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.