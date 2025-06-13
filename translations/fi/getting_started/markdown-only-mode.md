<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:41:18+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "fi"
}
-->
# Markdown-tilassa

## Johdanto
Markdown-tilaa käytetään kääntämään vain projektisi Markdown-sisältö. Tämä tila ohittaa kuvien käännösprosessin ja keskittyy pelkästään tekstisisältöön, mikä tekee siitä ihanteellisen tilanteisiin, joissa kuvien kääntäminen ei ole tarpeen tai tarvittavia ympäristömuuttujia Computer Visionille ei ole asetettu.

## Milloin käyttää
- Kun Computer Vision -ympäristömuuttujia ei ole määritetty.
- Kun haluat kääntää vain tekstisisällön ilman kuvien linkkien päivittämistä.
- Kun käyttäjä nimenomaisesti määrittää `-md` komentorivivaihtoehdolla.

## Kuinka ottaa käyttöön
Markdown-tilan aktivoimiseksi käytä komentosi yhteydessä `-md` -vaihtoehtoa. Esimerkiksi:
```
translate -l "ko" -md
```

Tai jos Computer Vision -ympäristömuuttujia ei ole asetettu, komento `translate -l "ko"` vaihtaa automaattisesti Markdown-tilaan.

```
translate -l "ko"
```

Tämä komento kääntää Markdown-sisällön koreaksi ja päivittää kuvien linkit niiden alkuperäisiin polkuihin sen sijaan, että muuttaisi ne käännettyjen kuvien poluiksi.

## Toiminta
Markdown-tilassa:
- Käännösprosessi ohittaa kuvien käännösvaiheen.
- Kuvien linkit Markdownissa pysyvät muuttumattomina ja osoittavat alkuperäisiin polkuihinsa.

## Esimerkit
### Ennen
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.fi.png)
```
### Markdown-tilan käytön jälkeen
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.fi.png)
```

## Vianetsintä
- Varmista, että `-md` -vaihtoehto on määritetty oikein komennossa.
- Tarkista, ettei mikään Computer Vision -ympäristömuuttuja häiritse prosessia.

## Yhteenveto
Markdown-tila tarjoaa yksinkertaisen tavan kääntää tekstisisältöä ilman, että kuvien linkkejä muutetaan. Se on erityisen hyödyllinen, kun kuvien kääntäminen ei ole tarpeen tai työskennellään ympäristöissä, joissa Computer Vision -asetuksia ei ole.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.