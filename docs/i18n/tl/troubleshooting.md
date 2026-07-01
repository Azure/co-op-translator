# Troubleshooting

Gamitin ang pahinang ito kapag ang isang pagtakbo ng pagsasalin ay nagtagumpay nang hindi inaasahan, nabigo sa panahon ng konfigurasyon, o gumawa ng output na kailangan ng pagsusuri.

## Start Here

1. Patakbuhin muna ang isang tinukoy na utos, tulad ng `translate -l "ko" -md`.
2. Idagdag `-d` para sa console debug logs.
3. Idagdag `-s` para i-save ang mga debug log sa ilalim ng `<root-dir>/logs/`.
4. Patakbuhin ang `co-op-review` pagkatapos ng pagsasalin upang suriin ang pagiging bago, istruktura, at mga lokal na link.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Configuration Errors

### No Language Model Provider

Error:

```text
No language model configuration found.
```

Fix:

- I-configure ang Azure OpenAI o OpenAI.
- Suriin na ang mga variable ay nasa kapaligiran kung saan tumatakbo ang utos.
- Para sa lokal na paggamit, ilagay ang mga ito sa `.env` sa root ng proyekto.

Tingnan ang [Konfigurasyon](configuration.md).

### Image Translation Without Azure AI Vision

Error:

```text
Image translation requested but Azure AI Service is not configured.
```

Fix:

- Magdagdag ng `AZURE_AI_SERVICE_API_KEY`.
- Magdagdag ng `AZURE_AI_SERVICE_ENDPOINT`.
- O magpatakbo ng utos na text-only tulad ng `translate -l "ko" -md`.

### Invalid Key or Endpoint

Maaaring kabilang sa mga sintomas ang `401`, naka-redact na mga error sa permiso, o mga error sa pag-access ng endpoint.

Fix:

- Kumpirmahin na ang key ay kabilang sa parehong Azure resource gaya ng endpoint.
- Kumpirmahin na sinusuportahan ng resource ang Vision kapag gumagamit ng `-img`.
- Kumpirmahin na tumutugma ang pangalan ng Azure OpenAI deployment at bersyon ng API sa iyong deployment.
- Patakbuhin na may debug logs: `translate -l "ko" -md -d -s`.

## No Files Were Translated

Common causes:

- Ang mga napiling flag ay hindi tumutugma sa iyong mga file.
- May mga umiiral nang naisaling file.
- Ang mga source file ay nasa loob ng mga direktoryong hindi kasama.
- Ang utos ay pinapatakbo mula sa maling root ng proyekto.

Checks:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Gamitin ang `--root-dir` kapag ang utos ay pinapatakbo sa labas ng root ng proyekto.

## Unexpected Link Behavior

Ang pagrerewrite ng link ay nakadepende sa mga napiling uri ng nilalaman:

- `-nb` included: ang mga link ng notebook ay maaaring tumuro sa naisaling notebook.
- `-nb` excluded: ang mga link ng notebook ay maaaring manatiling tumutukoy sa mga source notebook.
- `-img` included: ang mga link ng imahe ay maaaring tumuro sa naisaling mga imahe.
- `-img` excluded: ang mga link ng imahe ay maaaring manatiling tumutukoy sa mga source na imahe.

Magsagawa ng buong pagsasalin ng nilalaman kapag lahat ng internal na link ay dapat mas piliin ang mga naisaling output:

```bash
translate -l "ko" -md -nb -img
```

Patakbuhin ang pag-review ng mga link pagkatapos ng pagsasalin:

```bash
co-op-review -l "ko"
```

## Markdown Rendering Issues

Kung mali ang pag-render ng naisaling Markdown:

- Suriin na nagsisimula at nagtatapos ang frontmatter sa `---`.
- Suriin na tumutugma ang bilang ng code fence sa pagitan ng source at naisaling mga file.
- Patakbuhin ang `co-op-review` upang masalo ang mga karaniwang isyu sa istruktura.
- Isalin muli ang partikular na file kung ang output ay nasira.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action Ran but No Pull Request Was Created

Kung nag-uulat ang `peter-evans/create-pull-request` na ang branch ay hindi nangunguna sa base, hindi nakakita ang workflow ng mga file na iko-commit.

Mga posibleng sanhi:

- Ang pagsasalin ay hindi nagresulta ng mga pagbabago.
- Ang `.gitignore` ay naka-exclude ng `translations/`, `translated_images/`, o mga naisaling notebook.
- `add-paths` ay hindi tumutugma sa mga generated output directory.
- Maagang nagtapos ang hakbang ng pagsasalin.

Fixes:

1. Kumpirmahin na umiiral ang mga generated na file sa `translations/` o `translated_images/`.
2. Kumpirmahin na ang `.gitignore` ay hindi nag-i-ignore ng mga generated output.
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

5. Kumpirmahin na kasama sa workflow permissions ang:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Translation Quality

Maaaring kailanganin ng mga machine translation ang pagsusuri ng tao. Gamitin ang `evaluate` lamang kapag gusto mong magkaroon ng experimental na pagskor ng kalidad at mga workflow para sa pag-aayos ng mababang kumpiyansang output.

!!! warning "Experimental"
    `evaluate` can use rule-based and LLM-based checks, and its scoring model and metadata behavior may change. Keep it out of required CI gates unless your workflow is prepared for changes.

Para sa deterministic na pagsusuri sa CI, gamitin sa halip ang `co-op-review`.