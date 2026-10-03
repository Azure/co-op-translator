# Isalin, i-edit, at repasuhin ang isang maliit na proyekto

Magsimula sa dalawang maikling Markdown na file at isang target na wika. Makikita mo kung saan sinusulat ang mga salin, kung ano ang nangyayari kapag nagbago ang pinagmulan, at kung paano suriin ang resulta.

## Naitala na mga resulta

Pinatakbo ang halimbawa noong Setyembre 19, 2026 gamit ang Co-op Translator 0.21.0 at Azure OpenAI (`gpt-5-mini`). Ang hindi binagong mga utos ng CLI ay pinatakbo sa pamamagitan ng Click's `CliRunner` gamit ang binuong wheel at umiiral na mga dependency ng Python.

| Hakbang | Resulta |
| --- | --- |
| Paunang-suri | Exit 0; walang hiniling na pagsasalin mula sa modelo |
| Paunang pagsasalin | Exit 0; 27.36 segundo |
| Paunang pagsusuri | Exit 0 |
| I-edit ang README at repasuhin | Exit 1; natukoy na luma ang salin |
| I-update ang pagsasalin | Exit 0; 22.17 segundo |
| Pagsusuri pagkatapos ng pag-update | Exit 0; walang mga error o babala |
| Hindi nabagong gabay | Magkaparehong bytes bago at pagkatapos ng pag-update ng README |
| Patakbuhin muli | Exit 0; magkaparehong mga hash para sa lahat ng mga file ng pagsasalin |

Ito ay mga indibidwal na pagsukat ng pagtakbo, hindi garantiya ng pagganap. Hindi kasama ang oras ng pagsasaayos; hindi sinukat ang pagsingil ng provider. Maaaring magsagawa pa rin ng health check ng provider ang isang hindi nagbago na pagtakbo.

Inspeksyunin ang [paunang pagsasalin](../../assets/demo/before.txt), [na-update na pagsasalin](../../assets/demo/after.txt), [kumpletong diff ng pagsasalin](../../assets/demo/update.diff), [lumang pagsusuri](../../assets/demo/review-stale.txt), [pinal na pagsusuri](../../assets/demo/review-after.txt), at [mga detalye ng pagtakbo](../../assets/demo/results.json). Maaaring magbago ang iba pang mga salita sa buong file na pagsasalin, gaya ng ipinapakita ng nakuha na diff. Parehong napananatili ang awtomatikong paunawa sa mga text artifact.

Mahalaga pa rin ang pagsusuring tao: ang na-capture na pag-update ay gumagamit ng `[사용 가이드](guide.md)을`; ang Korean particle ay dapat `[사용 가이드](guide.md)를`. Pinananatili ng mga text artifact ang output na ito nang buo sa halip na ipakita ang na-edit na pagsasalin bilang output ng modelo. Pumapasa ang structural review sa kabila ng isyung ito sa pagkakasulat.

## 1. Ihanda ang isang maliit na folder

Gumamit ng Python 3.11–3.14 at ang [virtual environment setup](configuration.md#local-runtime-setup). I-install ang bersyon na ginamit sa halimbawang ito:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

I-download ang [README.txt](../../assets/demo/README.txt) at [guide.txt](../../assets/demo/guide.txt) papunta sa folder na ito, at i-save ang mga ito bilang `README.md` at `guide.md`. Maliit na kathang-isip na dokumento ng proyekto ang mga ito; hindi kailangan ng pag-install ng aplikasyon.

Ang README ay naglalaman ng isang code block at isang link sa `guide.md`. Ang huling pangungusap nito ay:

```text
Notes are saved locally.
```

Panatilihin lamang ang dalawang source na dokumentong ito sa folder na ito. Lahat ng sumusunod na mga utos ay patatakbuhin sa loob ng `translation-demo` at gagana sa Bash at PowerShell.

## 2. Paunang-suri nang walang kredensyal

```bash
translate -l "ko" -md --dry-run
```

Tinataya ng preview ang trabaho ng pagsasalin nang hindi tumatawag ng modelo o nagsusulat ng mga salin. Ang pagtatantya ng token ay hindi isang pahayag ng pagsingil. Dapat kilalanin ng unang pagtakbo ang parehong Markdown na mga file bilang bagong gawain.

## 3. Pumili ng provider at isalin

I-configure ang isang provider gamit ang [configuration guide](configuration.md): Azure OpenAI, OpenAI, o Anthropic. Hindi nangangailangan ng Azure account ang pagsasalin ng teksto gamit ang OpenAI at Anthropic. Hindi kailangan ang mga image service para sa halimbawang ito.

Kung gagamit ka ng lokal na `.env` na file, idagdag ang `.env` sa `.gitignore` ng folder na ito. Gumagamit ang mga tawag sa pagsasalin ng iyong provider account at maaaring magdulot ng singil.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Buksan ang `translations/ko/README.md` at `translations/ko/guide.md`. Suriin ang pagbabaybay sa Korean, ang code block, at ang link mula sa naisaling README papunta sa naisaling guide. Nag-iiba-iba ang tekstong output depende sa modelo.

`co-op-review` sinusuri ang pagiging sariwa, estruktura, at lokal na mga link. Ang pumapasa na resulta ay hindi nagpapatunay ng linggwistikong katumpakan. Ayusin ang anumang naiulat na mga error bago magpatuloy.

I-record ang matagumpay na baseline gamit ang Git (i-configure muna ang iyong Git identity kung kailangan):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Baguhin ang pinagmulan

Sa `README.md`, palitan ang `Notes are saved locally.` ng:

```text
Notes are saved locally as Markdown files.
```

Huwag baguhin ang `guide.md`. Pagkatapos patakbuhin:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Dapat iulat ng pagsusuri na luma na ang pagsasalin ng README at mag-exit nang hindi matagumpay. Ito ang inaasahang pansamantalang estado. Dapat matukoy ng preview ang gawain para sa nagbagong README.

## 5. I-update at suriin ang diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Suriin ang totoong diff: ang default na CLI ay muling isinasalin ang binagong file, kaya maaaring baguhin din ng modelo ang ibang mga salita sa file na iyon. Dapat walang diff ang hindi nabagong gabay. Hindi na dapat iulat ng pagsusuri na luma ang README; imbestigahan ang anumang iba pang natuklasan sa halip na balewalain ang mga ito.

Ang pagpapanatili sa antas-block ng mga manu-manong edit sa Markdown ay nangangailangan ng opsyonal na translation state provider sa [Python API](api.md). Hindi ito naka-enable ng mga utos na CLI na ito.

## 6. Patakbuhin muli nang walang mga pagbabago

I-commit ang na-update na source at pagsasalin:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Sa kasalukuyang mga pagsasalin at hindi nagbago na configuration, nilalaktawan ng tagasalin ang mga file. Ang huling utos ng Git ay hindi dapat makagawa ng diff at dapat mag-exit nang matagumpay.

## Mga susunod na hakbang

- [Isalin lamang ang isang README at magbukas ng pull request](github-actions.md#your-first-readme-translation-pr).
- [Pumili ng CLI, Python API, o MCP](workflows.md).
- [I-report ang isang problema sa pagsasalin nang hindi nagko-code](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).