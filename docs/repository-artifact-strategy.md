# Repository Artifact Strategy

This page defines how Co-op Translator should store large generated assets, especially translated image outputs, without making the Git repository hard to clone or maintain.

## Goals

- Keep the default clone friendly for contributors and CI.
- Preserve a small, reviewable sample of generated outputs in Git.
- Make larger generated bundles available through channels that fit their retention and distribution needs.
- Avoid surprise storage or bandwidth costs for maintainers.

## Constraints

- GitHub recommends keeping repositories ideally under 1 GB and strongly recommends staying under 5 GB.
- GitHub warns on files larger than 50 MiB and blocks files larger than 100 MiB in normal Git history.
- GitHub release assets can hold large downloadable bundles, with up to 1000 assets per release and a 2 GiB limit per asset.
- GitHub Actions artifacts are temporary by design. Public repositories keep them for up to 90 days unless a shorter retention period is configured.
- Git LFS requires an extra client install and uses metered storage and bandwidth, so every large download has an ongoing cost.

## Decision table

| Asset type | Default home | Why |
| --- | --- | --- |
| Source docs, code, config, tests | Git | Small, reviewed, versioned source-of-truth content. |
| Tiny generated fixtures used in tests or docs | Git | Needed for review and stable examples. Keep these intentionally curated. |
| Full translated image bundles tied to a release | GitHub Releases | Versioned, public, durable, and better suited than Git history for large downloads. |
| Nightly or PR preview bundles | GitHub Actions artifacts | Good for short-lived inspection and validation, not long-term distribution. |
| Always-on public browsing of many generated images | CDN or blob storage | Better fit when assets must stay online outside GitHub release pages. |
| Large binary assets that must remain versioned in-repo | Git LFS, sparingly | Use only when release assets or external storage are not acceptable. |

## Recommended policy

1. Do not keep bulk `translated_images/` output in normal Git history.
2. Keep only a small sample subset in Git for docs, screenshots, regression fixtures, and manual review.
3. Publish full generated image packs as release assets when they need long-lived public download links.
4. Use Actions artifacts for CI previews, evaluation bundles, or one-off verification outputs.
5. Consider CDN or blob storage only if the project needs stable, always-on browsing of many generated outputs.
6. Treat Git LFS as an exception path, not the default path, because it adds contributor setup and recurring storage and bandwidth cost.

## Immediate next steps

1. Freeze growth of tracked generated image output outside the curated sample set.
2. Define the sample set explicitly, for example:
   - one or two representative documents
   - one notebook-linked image case
   - one multilingual right-to-left rendering case
3. Add a release process step that packages the full generated image output as a zip asset when maintainers want to publish it.
4. Add a short-lived CI artifact upload only for workflows that need preview bundles.
5. Revisit Git history cleanup only after the project agrees on the steady-state storage model.

## Review checklist for maintainers

Before merging a PR that adds or regenerates many assets, confirm:

- Is this file needed in Git for tests, docs, or code review?
- Could this bundle live in a release asset instead?
- Could this output expire as an Actions artifact instead?
- Will this increase clone cost for every contributor?
- If Git LFS is proposed, who owns the storage and bandwidth budget?

## Suggested release pattern

When a release needs full translated image output:

1. Generate the full asset bundle in CI or on a maintainer machine.
2. Upload a versioned archive such as `translated-images-vX.Y.Z.zip` to the GitHub release.
3. Keep only the curated in-repo sample set on `main`.
4. Link the release asset from docs or release notes when users need the full bundle.

## Optional tooling

- Run `git-sizer` periodically to catch repository growth before it becomes painful.
- Set a shorter retention window for preview artifacts than the repository default when possible.
- Add a PR template checkbox for large generated assets if asset-heavy changes become frequent.

## References

- [GitHub Docs: About large files on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)
- [GitHub Docs: About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [GitHub Docs: Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)
- [GitHub Docs: Git LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs)
