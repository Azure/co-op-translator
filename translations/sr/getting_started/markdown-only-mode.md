<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:43:43+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "sr"
}
-->
# Korišćenje režima samo za Markdown

## Uvod
Režim samo za Markdown je osmišljen da prevodi isključivo Markdown sadržaj vašeg projekta. Ovaj režim preskače proces prevođenja slika i fokusira se samo na tekstualni sadržaj, što ga čini idealnim za situacije kada prevođenje slika nije potrebno ili kada nisu podešene potrebne promenljive okruženja za Computer Vision.

## Kada koristiti
- Kada promenljive okruženja vezane za Computer Vision nisu konfigurisane.
- Kada želite da prevedete samo tekstualni sadržaj bez ažuriranja linkova ka slikama.
- Kada korisnik eksplicitno navede opciju `-md` u komandnoj liniji.

## Kako omogućiti
Da biste aktivirali režim samo za Markdown, koristite opciju `-md` u svojoj komandi. Na primer:
```
translate -l "ko" -md
```

Ili, ako promenljive okruženja vezane za Computer Vision nisu podešene. Pokretanjem `translate -l "ko"` automatski se uključuje režim samo za Markdown.

```
translate -l "ko"
```

Ova komanda prevodi Markdown sadržaj na korejski i zadržava linkove ka slikama na njihovim originalnim putanjama, umesto da ih menja u prevedene putanje slika.

## Ponašanje
U režimu samo za Markdown:
- Proces prevođenja preskače korak prevođenja slika.
- Linkovi ka slikama u Markdown-u ostaju nepromenjeni i upućuju na originalne putanje.

## Primeri
### Pre
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.sr.png)
```
### Nakon korišćenja režima samo za Markdown
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.sr.png)
```

## Rešavanje problema
- Proverite da je opcija `-md` pravilno navedena u komandi.
- Uverite se da nijedna promenljiva okruženja vezana za Computer Vision ne ometa proces.

## Zaključak
Režim samo za Markdown pruža pojednostavljen način za prevođenje tekstualnog sadržaja bez menjanja linkova ka slikama. Posebno je koristan kada prevođenje slika nije neophodno ili kada se radi u okruženjima koja nemaju podešen Computer Vision.

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било какве неспоразуме или погрешне интерпретације настале коришћењем овог превода.