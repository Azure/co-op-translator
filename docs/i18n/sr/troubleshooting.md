# Решавање проблема

Use this page when a translation run succeeds unexpectedly, fails during configuration, or produces output that needs review.

## Почните овде

1. Run a focused command first, such as `translate -l "ko" -md`.
2. Add `-d` for console debug logs.
3. Add `-s` to save debug logs under `<root-dir>/logs/`.
4. Run `co-op-review` after translation to check freshness, structure, and local links.

```bash
translate -l "ko" -md -d -s
co-op-review -l "ko"
```

## Грешке у конфигурацији

### Није обезбеђен провајдер језичког модела

Грешка:

```text
No language model configuration found.
```

Решење:

- Конфигуришите Azure OpenAI или OpenAI.
- Потврдите да су променљиве у окружењу у коме команда ради.
- За локалну употребу ставите их у `.env` у корену пројекта.

Погледајте [Конфигурацију](configuration.md).

### Превод слика без Azure AI Vision

Грешка:

```text
Image translation requested but Azure AI Service is not configured.
```

Решење:

- Додајте `AZURE_AI_SERVICE_API_KEY`.
- Додајте `AZURE_AI_SERVICE_ENDPOINT`.
- Или покрените команду само за текст као што је `translate -l "ko" -md`.

### Неважећи кључ или крајња тачка

Симптоми могу укључивати `401`, уклоњене поруке о дозволи или грешке при приступу крајњој тачки.

Решење:

- Потврдите да кључ припада истом Azure ресурсу као и крајња тачка.
- Потврдите да ресурс подржава Vision када користите `-img`.
- Потврдите да име Azure OpenAI размештања и верзија API-ја одговарају вашем размештању.
- Покрените са debug логовима: `translate -l "ko" -md -d -s`.

## Ниједна датотека није преведена

Чести узроци:

- Изабране ознаке (flags) се не поклапају са вашим датотекама.
- Постојеће преведене датотеке су већ присутне.
- Изворне датотеке се налазе у изузетим директоријумима.
- Команда се покреће из погрешног корена пројекта.

Провере:

```bash
translate -l "ko" -md --dry-run
translate -l "ko" -nb --dry-run
translate -l "ko" -img --dry-run
```

Use `--root-dir` when the command is run outside the project root.

## Неочекивано понашање веза

Преусмеравање веза зависи од изабраних типова садржаја:

- `-nb` укључен: везе ка notebook-овима могу упућивати на преведене notebook-ове.
- `-nb` искључен: везе ка notebook-овима могу остати усмерене на оригиналне notebook-ове.
- `-img` укључен: везе ка сликама могу упућивати на преведене слике.
- `-img` искључен: везе ка сликама могу остати усмерене на оригиналне слике.

Покрените потпуни превод садржаја када све интерне везе треба да преферирају преведене излазне датотеке:

```bash
translate -l "ko" -md -nb -img
```

Run link review after translation:

```bash
co-op-review -l "ko"
```

## Проблеми са рендеровањем Markdown-а

Ако преведени Markdown не рендерује правилно:

- Проверите да frontmatter почиње и завршава се са `---`.
- Проверите да број ограда за код (code fence) одговара између извора и преведених датотека.
- Покрените `co-op-review` да открије уобичајене проблеме у структури.
- Поново преведите одређену датотеку ако је излаз оштећен.

```bash
co-op-review -l "ko" --format github
```

## GitHub Action се покренуо али није направљен Pull Request

Ако `peter-evans/create-pull-request` пријави да грана није испред базе, workflow није пронашла датотеке за комитовање.

Могући узроци:

- Преводна рунда није произвела измене.
- `.gitignore` искључује `translations/`, `translated_images/` или преведене notebook-ове.
- `add-paths` се не поклапа са генерисаним директоријумима излаза.
- Корак превођења је раније завршен.

Решења:

1. Потврдите да генерисане датотеке постоје у `translations/` или `translated_images/`.
2. Потврдите да `.gitignore` не игнорише генерисане излазе.
3. Use matching `add-paths`:

   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```

4. Temporarily add debug flags to the translate command:

   ```bash
   translate -l "ko" -md -d -s
   ```

5. Confirm workflow permissions include:

   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```

## Квалитет превода

Машински преводи могу захтевати људску ревизију. Користите `evaluate` само када желите експериментално оцењивање квалитета и радне токове за исправке ниског поверења.

!!! warning "Експериментално"
    `evaluate` може користити проверe засноване на правилима и LLM-у, и његов модел бодовања и понашање метаподатака се могу променити. Држите га ван обавезних CI провера осим ако ваш радни ток није припремљен за промене.

За детерминистичке CI провере, уместо тога користите `co-op-review`.