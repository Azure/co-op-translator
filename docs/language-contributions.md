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

The [Japanese instruction file](../src/co_op_translator/templates/language/ja.md) tells the model to translate link text while preserving Markdown syntax and the link destination. For example, a link written as `[text](URL)` must not become `「text」（URL）`.

This is a focused example of a language rule backed by an illustration of correct and incorrect output. It is not evidence that prompt instructions alone guarantee correct Markdown.

The [Markdown prompt builder](../src/co_op_translator/utils/markdown/prompts.py) loads `templates/language/<language_code>.md` using a lowercased, trimmed language code. If no file exists, it uses the common instructions. This describes the Markdown prompt path; do not assume every image or other translation path uses the same instructions.

The [prompt tests](../tests/co_op_translator/utils/markdown/test_prompts.py) check that the Japanese instructions are included. That verifies prompt assembly, not translation quality.

## What belongs in a language rule?

Propose a narrow, repeatable correction with a source example, expected behavior, and a counterexample where the rule must not apply. Preserve meaning, placeholders, code, URLs, and document structure. Avoid turning one person's style preference or one course's terminology into a universal rule.

The current [glossary implementation](../src/co_op_translator/glossary.py) protects terms from translation. It is not a source-to-target terminology dictionary. Discuss new terminology behavior before promising it to contributors.

## First Korean review exercise: particles around placeholders

[Report #243](https://github.com/Azure/co-op-translator/issues/243), submitted by @braintrue, provides this example:

| Item | Reported text |
| --- | --- |
| Source | `Excluding {days}` |
| Current translation | `{days} 제외하고` |
| Suggested correction | `{days}를 제외하고` |

This is a contributor's proposed correction, not a measured before/after result from the current version. The report does not establish a recurring failure across models or provide enough surrounding context to choose a universal particle rule. No Korean prompt change is introduced with this guide.

Three small contributions can help evaluate it:

- **Add context:** provide the source file and surrounding sentence, and explain what `{days}` represents. Completion means a reviewer can understand how the text is used without guessing.
- **Review alternatives:** explain when the proposed correction is appropriate and supply at least one contrasting example. Keep placeholder spelling intact; do not apply a blanket rule that appends `를` to every placeholder.
- **Review a comparison:** after a maintainer supplies baseline and candidate outputs, check meaning, particles, placeholder preservation, and unaffected examples. Record disagreements as well as improvements.

## Validation before adopting a rule

Use the same source samples, translator revision, provider/model, and generation settings for baseline and candidate runs, changing only the proposed instruction. Record the actual prompt change and outputs; repeat examples when needed to distinguish a consistent effect from output variability. Include the reported failure, contrasting contexts, and examples that already translate correctly.

| Sample | Source/context | Baseline output | Candidate output | Reviewer assessment |
| --- | --- | --- | --- | --- |
| Reported failure | To collect | Not run | Not run | Pending |
| Counterexample | To collect | Not run | Not run | Pending |
| Unaffected example | To collect | Not run | Not run | Pending |

Check structural invariants separately from linguistic judgments. A successful prompt-loading test is not a quality evaluation, and one exact expected sentence is not the only valid translation. If context, model runs, or language review are missing, keep the proposal pending rather than claiming the issue is fixed.
