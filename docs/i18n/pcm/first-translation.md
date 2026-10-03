# Translate, edit, and review wan small project

Start with two short Markdown files and one target language. You go see where dem write translations, wetin dey happen when the source change, and how to check di result.

## Results wey dem record

Dem run dis example on September 19, 2026 with Co-op Translator 0.21.0 and Azure OpenAI (`gpt-5-mini`). Dem no modify the CLI commands; dem invoke am through Click's `CliRunner` using the built wheel and the existing Python dependencies.

| Step | Result |
| --- | --- |
| Preview | Exit 0; no model translation requested |
| Initial translation | Exit 0; 27.36 seconds |
| Initial review | Exit 0 |
| Edit README and review | Exit 1; dem detect say translation don stale |
| Update translation | Exit 0; 22.17 seconds |
| Review after update | Exit 0; no errors or warnings |
| Unchanged guide | Bytes remain di same before and after README update |
| Run again | Exit 0; all translation files get identical hashes |

Dis na measurements for each run, no be performance guarantees. Setup time no dey include; dem never measure provider billing. Even if run no change, e fit still do provider health check.

Inspect di [first translation](../../assets/demo/before.txt), [updated translation](../../assets/demo/after.txt), [complete translation diff](../../assets/demo/update.diff), [stale review](../../assets/demo/review-stale.txt), [final review](../../assets/demo/review-after.txt), and [run details](../../assets/demo/results.json). Full-file translation fit change other wording, like di captured diff show. Both text artifacts still dey carry di generated disclaimer.

Human review still matter: the captured update uses `[사용 가이드](guide.md)을`; the Korean particle should be `[사용 가이드](guide.md)를`. The text artifacts keep this output intact rather than presenting an edited translation as model output. The structural review pass despite this wording issue.

## 1. Prepare wan small folder

Use Python 3.11–3.14 and the [virtual environment setup](configuration.md#local-runtime-setup). Install di version wey dem use for dis example:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Download [README.txt](../../assets/demo/README.txt) and [guide.txt](../../assets/demo/guide.txt) into this folder, saving dem as `README.md` and `guide.md`. Dem na small fictional project documents; no need install any application.

Di README get code block and one link to `guide.md`. E final sentence na:

```text
Notes are saved locally.
```

Only keep these two source documents for this folder. All following commands run inside `translation-demo` and dem work in Bash and PowerShell.

## 2. Preview without credentials

```bash
translate -l "ko" -md --dry-run
```

Di preview dey estimate translation work without calling any model or writing translations. Token estimates no be billing quote. For di first run e suppose identify both Markdown files as new work.

## 3. Choose a provider and translate

Configure one provider using the [configuration guide](configuration.md): Azure OpenAI, OpenAI, or Anthropic. OpenAI and Anthropic text translation no need an Azure account. Image services no dey needed for dis example.

If you use a local `.env` file, add `.env` to this folder's `.gitignore`. Translation calls go use your provider account and fit incur charges.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Open `translations/ko/README.md` and `translations/ko/guide.md`. Check di Korean wording, di code block, and di link from di translated README to di translated guide. Output wording fit vary by model.

`co-op-review` checks freshness, structure, and local links. If e pass no mean say di language correct. Fix any reported errors before you continue.

Record di successful baseline with Git (configure your Git identity first if needed):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Change the source

For `README.md`, replace `Notes are saved locally.` with:

```text
Notes are saved locally as Markdown files.
```

Leave `guide.md` unchanged. Then run:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

Di review suppose report say di README translation don stale and e go exit unsuccessfully. Dis na di expected intermediate state. Di preview suppose identify work for di changed README.

## 5. Update and inspect di diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Inspect di real diff: di default CLI retranslate di changed file, so di model fit also revise other wording inside that file. Di guide wey no change suppose get no diff. Di review suppose no longer report di README as stale; investigate any other findings instead of ignoring dem.

To preserve human Markdown edits at block level you need an optional translation state provider in the [Python API](api.md). E no enable for these CLI commands.

## 6. Run again without changes

Commit di updated source and translation:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

With current translations and unchanged configuration, di translator go skip the files. Di final Git command suppose produce no diff and exit successfully.

## Next steps

- [Translate just a README and open a pull request](github-actions.md#your-first-readme-translation-pr).
- [Choose CLI, Python API, or MCP](workflows.md).
- [Report a translation problem without coding](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).