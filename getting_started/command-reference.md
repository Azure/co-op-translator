# Command reference

The canonical CLI reference now lives in the MkDocs documentation:

- [CLI reference](../docs/cli.md)
- [Configuration requirements](../docs/configuration.md)
- [Python API reference](../docs/api.md)
- [Examples](../docs/examples.md)

This page remains as a compatibility entry point for older README and tutorial links.

## Common commands

| Task | Command |
| --- | --- |
| Translate Markdown only | `translate -l "ko ja" -md` |
| Translate notebooks only | `translate -l "ko" -nb` |
| Translate images only | `translate -l "ko" -img` |
| Translate all supported content types | `translate -l "ko"` |
| Update existing translations | `translate -l "ko" -u` |
| Repair low-confidence Markdown translations | `translate -l "ko" --fix -c 0.8 -md` |
| Evaluate one language | `evaluate -l "ko"` |
| Run deterministic review checks | `co-op-review -l "ko ja"` |
| Review only changed source files | `co-op-review -l "ko" --changed-from origin/main` |
| Migrate translated notebook links | `migrate-links -l "ko"` |

For every option and behavior note, use the [CLI reference](../docs/cli.md). It is the source of truth for `translate`, `evaluate`, `co-op-review`, and `migrate-links`.
