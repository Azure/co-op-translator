<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:40:47+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "sv"
}
-->
# Använda Endast Markdown-läge

## Introduktion
Endast Markdown-läge är utformat för att endast översätta Markdown-innehållet i ditt projekt. Detta läge hoppar över bildöversättningsprocessen och fokuserar enbart på den textuella innehållet, vilket gör det idealiskt i situationer där bildöversättning inte krävs eller när nödvändiga miljövariabler för Computer Vision inte är inställda.

## När man ska använda
- När miljövariabler relaterade till Computer Vision inte är konfigurerade.
- När du endast vill översätta textinnehållet utan att uppdatera bildlänkar.
- När det uttryckligen anges av användaren med hjälp av `-md` kommandoradsalternativet.

## Hur man aktiverar
För att aktivera endast Markdown-läge, använd alternativet `-md` i ditt kommando. Till exempel:
```
translate -l "ko" -md
```

Eller om miljövariabler relaterade till Computer Vision inte är konfigurerade. Att köra `translate -l "ko"` kommer automatiskt att växla till endast Markdown-läge.

```
translate -l "ko"
```

Detta kommando översätter Markdown-innehållet till koreanska och uppdaterar bildlänkar till deras ursprungliga sökvägar, istället för att ändra dem till översatta bildvägar.

## Beteende
I endast Markdown-läge:
- Översättningsprocessen hoppar över bildöversättningssteget.
- Bildlänkar i Markdown förblir oförändrade och pekar på deras ursprungliga sökvägar.

## Exempel
### Före
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.sv.png)
```
### Efter att ha använt endast Markdown-läge
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.sv.png)
```

## Felsökning
- Säkerställ att alternativet `-md` är korrekt angivet i kommandot.
- Verifiera att inga miljövariabler för Computer Vision stör processen.

## Slutsats
Endast Markdown-läge erbjuder ett smidigt sätt att översätta textinnehåll utan att ändra bildlänkar. Det är särskilt användbart när bildöversättning är onödig eller när man arbetar i miljöer utan uppsättning för Computer Vision.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.