<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:43:56+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "hr"
}
-->
# Korištenje načina rada samo za Markdown

## Uvod
Način rada samo za Markdown dizajniran je za prevođenje isključivo Markdown sadržaja vašeg projekta. Ovaj način zaobilazi proces prevođenja slika i fokusira se samo na tekstualni sadržaj, što ga čini idealnim za situacije kada prevođenje slika nije potrebno ili kada nisu postavljene potrebne varijable okoline za Computer Vision.

## Kada koristiti
- Kada varijable okoline vezane uz Computer Vision nisu konfigurirane.
- Kada želite prevesti samo tekstualni sadržaj bez ažuriranja poveznica na slike.
- Kada korisnik izričito navede opciju `-md` u naredbenom retku.

## Kako omogućiti
Za aktivaciju načina rada samo za Markdown, upotrijebite opciju `-md` u svojoj naredbi. Na primjer:
```
translate -l "ko" -md
```

Ili ako varijable okoline vezane uz Computer Vision nisu konfigurirane. Pokretanjem `translate -l "ko"` automatski će se prebaciti na način rada samo za Markdown.

```
translate -l "ko"
```

Ova naredba prevodi Markdown sadržaj na korejski i ažurira poveznice na slike na njihove izvorne putanje, umjesto da ih mijenja u prevedene putanje slika.

## Ponašanje
U načinu rada samo za Markdown:
- Proces prevođenja preskače korak prevođenja slika.
- Poveznice na slike u Markdownu ostaju nepromijenjene i upućuju na svoje izvorne putanje.

## Primjeri
### Prije
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.hr.png)
```
### Nakon korištenja načina rada samo za Markdown
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.hr.png)
```

## Rješavanje problema
- Provjerite je li opcija `-md` ispravno navedena u naredbi.
- Provjerite da nijedna varijabla okoline vezana uz Computer Vision ne ometa proces.

## Zaključak
Način rada samo za Markdown nudi pojednostavljen način prevođenja tekstualnog sadržaja bez mijenjanja poveznica na slike. Posebno je koristan kada prevođenje slika nije potrebno ili kada se radi u okruženjima bez postavki za Computer Vision.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.