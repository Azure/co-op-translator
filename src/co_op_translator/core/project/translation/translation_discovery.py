from __future__ import annotations

from pathlib import Path
from typing import List

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.utils.common.file_utils import filter_files
from co_op_translator.utils.common.token_estimation import estimate_translation_tokens


class TranslationDiscoveryMixin:
    def estimate_tokens(self, update: bool = False) -> dict:
        """Estimate tokens for the upcoming translation run.

        Backward-compatible shim that delegates token-estimation breakdown
        calculation to shared estimation utilities.
        """
        return estimate_translation_tokens(self, update=update)

    def _gather_pending_markdown(self, update: bool) -> List[Path]:
        pending: List[Path] = []
        markdown_files = filter_files(self.root_dir, self.excluded_dirs)
        for md_file_path in markdown_files:
            md_file_path = md_file_path.resolve()
            if md_file_path.suffix.lower() in SUPPORTED_MARKDOWN_EXTENSIONS:
                for language_code in self.language_codes:
                    relative_path = md_file_path.relative_to(self.root_dir)
                    translated_md_path = (
                        self._get_language_root(language_code) / relative_path
                    )
                    if not update and translated_md_path.exists():
                        continue
                    pending.append(md_file_path)
        return pending

    def _gather_pending_notebooks(self, update: bool) -> List[Path]:
        pending: List[Path] = []
        notebook_files: List[Path] = []
        for ext in self.supported_notebook_extensions:
            notebook_files.extend(filter_files(self.root_dir, self.excluded_dirs, ext))
        for notebook_file_path in notebook_files:
            notebook_file_path = notebook_file_path.resolve()
            for language_code in self.language_codes:
                relative_path = notebook_file_path.relative_to(self.root_dir)
                translated_notebook_path = (
                    self._get_language_root(language_code) / relative_path
                )
                if translated_notebook_path.exists() and not update:
                    # Existing notebook translations are handled separately by the
                    # outdated-translation pass, so the pending bucket should
                    # only include notebooks that do not have a translation yet.
                    continue
                pending.append(notebook_file_path)
        return pending
