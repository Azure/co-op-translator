# Contributing language improvements

Your language knowledge can help improve Co-op Translator. Start with an example, a suggested correction, and an explanation using the [translation feedback form](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). You do not need to write code or pay for a model run.

## From a report to a shared improvement

1. A contributor supplies a source excerpt, its translation, and context.
2. A language reviewer checks meaning, naturalness, and whether the suggestion depends on a particular locale or course.
3. A maintainer decides whether the fix belongs in the source course, a shared language instruction, terminology configuration, or translation code.
4. For a shared rule, a maintainer compares outputs before and after the change on the reported example and unrelated examples. Contributors can review these outputs without running the tool themselves.
5. The resulting PR links the report and credits the people who provided examples and review. Deployment or regeneration in consuming repositories is a separate step.

A report does not automatically change prompts or regenerate course translations. Course-specific corrections should remain connected to the course repository. Do not assume a manual edit will survive later retranslation; confirm the behavior for that workflow.

## Existing example: Japanese Markdown links

The [Japanese instruction file](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) tells the model to translate link text while preserving Markdown syntax and the link destination. For example, a link written as `[text](URL)` must not become `「text」（URL）`.

This is a focused example of a language rule backed by an illustration of correct and incorrect output. It is not evidence that prompt instructions alone guarantee correct Markdown.

The [Markdown prompt builder](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) loads `templates/language/<language_code>.md` using a lowercased, trimmed language code. If no file exists, it uses the common instructions. This describes the Markdown prompt path; do not assume every image or other translation path uses the same instructions.

The [prompt tests](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) check that the Japanese instructions are included. That verifies prompt assembly, not translation quality.

## What belongs in a language rule?

Propose a narrow, repeatable correction with a source example, expected behavior, and a counterexample where the rule must not apply. Preserve meaning, placeholders, code, URLs, and document structure. Avoid turning one person's style preference or one course's terminology into a universal rule.

The current [glossary implementation](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) protects terms from translation. It is not a source-to-target terminology dictionary. Discuss new terminology behavior before promising it to contributors.

## Community example: a Japanese product-name report

In [report #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 identified a Japanese translation that changed the product name `Co-op Translator` to `Co-op 翻訳`. The report included a link to the affected document and a screenshot, making the problem easy to locate.

The contributor also linked a [related course PR](https://github.com/microsoft/AZD-for-beginners/pull/109). In the issue discussion, the maintainer acknowledged the report and proposed investigating why the name changed, including terminology protection, glossary behavior, and the translation path.

This shows how a small report can support investigation beyond an individual wording correction. It is not a verified before/after result or evidence that the Japanese Markdown-link instructions above fixed this product-name issue.

You can contribute the same way: share the original text, current translation, suggested correction, and why it matters. Add a document link or screenshot when useful. You do not need to diagnose the cause or write a prompt before reporting it.

## Validation before adopting a rule

Use the same source samples, translator revision, provider/model, and generation settings for baseline and candidate runs, changing only the proposed instruction. Record the actual prompt change and outputs; repeat examples when needed to distinguish a consistent effect from output variability. Include the reported failure, contrasting contexts, and examples that already translate correctly.

| Sample | Source/context | Baseline output | Candidate output | Reviewer assessment |
| --- | --- | --- | --- | --- |
| Reported failure | To collect | Not run | Not run | Pending |
| Counterexample | To collect | Not run | Not run | Pending |
| Unaffected example | To collect | Not run | Not run | Pending |

Check structural invariants separately from linguistic judgments. A successful prompt-loading test is not a quality evaluation, and one exact expected sentence is not the only valid translation. If context, model runs, or language review are missing, keep the proposal pending rather than claiming the issue is fixed.
