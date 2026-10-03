# Pagsasaayos ng Problema

Gamitin ang pahinang ito kapag ang pagsasalin ay nagtapos nang hindi inaasahan, nabigo sa panahon ng konfigurasyon, o naglabas ng output na kailangan ng pagsusuri.

## Magsimula Dito

1. Patakbuhin muna ang isang nakatuong utos, tulad ng `translate -l "ko" -md`.
2. Idagdag ang `-d` para sa mga log ng debug sa console.
3. Idagdag ang `-s` upang i-save ang mga log ng debug sa `<root-dir>/logs/`.
4. Patakbuhin ang `co-op-review` pagkatapos ng pagsasalin upang suriin ang pagiging bago, istruktura, at mga lokal na link.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Mga Error sa Konfigurasyon

### Walang Tagapagbigay ng Language Model

Error:

```text
No language model configuration found.
```

Ayusin:

- I-configure ang Azure OpenAI, OpenAI, o Anthropic.
- Tiyakin na ang mga variable ay nasa environment kung saan pinapatakbo ang utos.
- Para sa lokal na paggamit, ilagay ang mga ito sa `.env` sa root ng proyekto.

Tingnan ang [Konfigurasyon](configuration.md).

### Pagsasalin ng Imahe Nang Walang Azure AI Vision

Error:

```text
Image translation requested but Azure AI Service is not configured.
```

Ayusin:

- Idagdag ang `AZURE_AI_SERVICE_API_KEY`.
- Idagdag ang `AZURE_AI_SERVICE_ENDPOINT`.
- O patakbuhin ang utos para sa text lamang tulad ng `translate -l "ko" -md`.

### Di-wastong Key o Endpoint

Maaaring kabilang sa mga sintomas ang `401`, na-redact na mga error sa permiso, o mga error sa pag-access ng endpoint.

Ayusin:

- Kumpirmahin na ang key ay kabilang sa parehong Azure resource tulad ng endpoint.
- Kumpirmahin na sinusuportahan ng resource ang Vision kapag gumagamit ng `-img`.
- Kumpirmahin na ang pangalan ng Azure OpenAI deployment at ang API version ay tumutugma sa iyong deployment.
- Patakbuhin na may mga log ng debug: `translate -l "ko" -md -d -s`.

## Walang Mga File na Naisalin

Mga karaniwang sanhi:

- Ang mga napiling flag ay hindi tumutugma sa iyong mga file.
- May umiiral na mga naisaling file.
- Ang mga source file ay nasa ilalim ng mga direktoryong hindi kasama.
- Ang utos ay pinapatakbo mula sa maling root ng proyekto.

Mga tseke:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Gamitin ang `--root-dir` kapag ang utos ay pinapatakbo sa labas ng root ng proyekto.

## Hindi Inaasahang Pag-uugali ng Link

Ang pag-rewrite ng mga link ay nakadepende sa mga napiling uri ng nilalaman:

- `-nb` kasama: ang mga link ng notebook ay maaaring tumuro sa mga naisaling notebook.
- `-nb` hindi kasama: ang mga link ng notebook ay maaaring manatiling nakaturo sa mga orihinal na notebook.
- `-img` kasama: ang mga link ng imahe ay maaaring tumuro sa mga naisaling imahe.
- `-img` hindi kasama: ang mga link ng imahe ay maaaring manatiling nakaturo sa mga orihinal na imahe.

Isagawa ang buong pagsasalin ng nilalaman kapag dapat na mas pinipili ng lahat ng internal na link ang mga naisaling output:

```bash
translate -l "ko" -md -nb -img
```

Patakbuhin ang pagsusuri ng mga link pagkatapos ng pagsasalin:

```bash
co-op-review -l "ko"
```

## Mga Isyu sa Pag-render ng Markdown

Kung ang naisaling Markdown ay nagre-render nang mali:

- Suriin na ang frontmatter ay nagsisimula at nagtatapos sa `---`.
- Suriin na ang bilang ng code fence ay tumutugma sa pagitan ng source at naisaling mga file.
- Patakbuhin ang `co-op-review` upang mahuli ang mga karaniwang isyu sa istruktura.
- Isalin muli ang partikular na file kung ang output ay nasira.

```bash
co-op-review -l "ko" --format github
```

## Tumakbo ang GitHub Action ngunit Walang Pull Request na Nalikha

Kung iniulat ng `peter-evans/create-pull-request` na ang branch ay hindi nauuna sa base, walang nahanap na mga file na ia-commit ng workflow.

Mga posibleng sanhi:

- Ang pagtakbo ng pagsasalin ay hindi nakabuo ng mga pagbabago.
- Nilalaktawan ng `.gitignore` ang `translations/`, `translated_images/`, o mga naisaling notebook.
- Ang `add-paths` ay hindi tumutugma sa mga direktoryo ng nalikhang output.
- Maagang tumigil ang hakbang ng pagsasalin.

Mga Pag-aayos:

1. Kumpirmahin na umiiral ang mga nalikhang file sa `translations/` o `translated_images/`.
2. Kumpirmahin na hindi ini-ignore ng `.gitignore` ang mga nalikhang output.
3. Gumamit ng tumutugmang `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Pansamantalang idagdag ang mga debug flag sa utos ng translate:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Kumpirmahin na kasama sa mga permiso ng workflow ang:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Kalidad ng Pagsasalin

Maaaring kailanganin ng mga machine translation ang pagsusuri ng tao. Gamitin ang `evaluate` lamang kapag gusto mo ng experimental na pagmamarka ng kalidad at mga workflow ng pag-aayos para sa mababang kumpiyansa.

!!! warning "Eksperimental"
    `evaluate` ay maaaring gumamit ng mga rule-based at LLM-based na pagsusuri, at ang modelo ng pagmamarka at pag-uugali ng metadata nito ay maaaring magbago. Huwag isama ito sa mga kinakailangang CI gate maliban kung handa ang iyong workflow sa mga pagbabago.

Para sa deterministic na tseke ng CI, gamitin na lamang ang `co-op-review`.