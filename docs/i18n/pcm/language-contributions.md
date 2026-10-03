# How to help improve di language

Your language sabi fit help improve Co-op Translator. Start wit one example, one suggested correction, and small explanation usin di [translation feedback form](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). You no need write code or pay for model run.

## From report turn to shared improvement

1. One contributor go supply di source excerpt, di translation, and di context.
2. One language reviewer go check meaning, how natural e sound, and whether di suggestion depend on particular locale or course.
3. One maintainer go decide whether di fix suppose dey for di source course, a shared language instruction, terminology configuration, or translation code.
4. For a shared rule, one maintainer go compare outputs before and after di change on di reported example and on unrelated examples. Contributors fit review these outputs without runnin di tool by demself.
5. Di resulting PR go link di report and give credit to di people wey provide examples and do review. Deployment or regeneration for di repos wey consume am na separate step.

A report no go automatically change prompts or regenerate course translations. Course-specific corrections suppose remain connected to di course repository. No assume say manual edit go survive later retranslation; confirm how e go behave for dat workflow.

## Existing example: Japanese Markdown links

Di [Japanese instruction file](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) dey tell di model make e translate di link text while e still preserve Markdown syntax and di link destination. For example, link wey dem write as `[text](URL)` no suppose turn to `「text」（URL）`.

Dis na focused example of one language rule wey get illustration of correct and incorrect output. E no mean say prompt instructions alone go guarantee correct Markdown.

Di [Markdown prompt builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) dey load `templates/language/<language_code>.md` usin a lowercased, trimmed language code. If no file exist, e go use di common instructions. Dis one describe di Markdown prompt path; no assume say every image or oda translation path dey use di same instructions.

Di [prompt tests](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) dey check say di Japanese instructions dey included. Dat one verify prompt assembly, no be translation quality.

## Wetin suppose dey for language rule?

Propose small, repeatable correction wit source example, expected behavior, and one counterexample wey di rule no suppose apply. Preserve meaning, placeholders, code, URLs, and document structure. No turn one person style preference or one course terminology into universal rule.

Di current [glossary implementation](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) dey protect terms from translation. E no be source-to-target terminology dictionary. Discuss new terminology behavior before you promise am to contributors.

## Community example: one Japanese product-name report

For [report #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 notice one Japanese translation wey change di product name `Co-op Translator` to `Co-op 翻訳`. Di report include link to di affected document and one screenshot, wey make di problem easy to locate.

Di contributor also linked one [related course PR](https://github.com/microsoft/AZD-for-beginners/pull/109). For di issue discussion, di maintainer acknowledge di report and propose make dem investigate why di name change, includin terminology protection, glossary behavior, and di translation path.

Dis show how small report fit support investigation wey go beyond just one wording correction. E no be verified before/after result or proof say di Japanese Markdown-link instructions up there fix dis product-name issue.

You fit contribute di same way: share di original text, di current translation, di suggested correction, and why e matter. Add document link or screenshot when e useful. You no need diagnose di cause or write prompt before you report am.

## Validation before you adopt di rule

Use di same source samples, translator revision, provider/model, and generation settings for baseline and candidate runs, change only di proposed instruction. Record di actual prompt change and outputs; repeat examples when needed to separate consistent effect from output variability. Include di reported failure, contrasting contexts, and examples wey already translate correct.

| Sample | Source/context | Baseline output | Candidate output | Reviewer assessment |
| --- | --- | --- | --- | --- |
| Reported failure | To collect | Not run | Not run | Pending |
| Counterexample | To collect | Not run | Not run | Pending |
| Unaffected example | To collect | Not run | Not run | Pending |

Make sure say you check structural invariants separate from linguistic judgments. One successful prompt-loading test no be quality evaluation, and one exact expected sentence no be di only valid translation. If context, model runs, or language review dey missin, keep di proposal pending instead of claimin say di issue don fix.