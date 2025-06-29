"""
This module provides functionality for evaluating translations across a project.
"""

import logging
from pathlib import Path
from typing import List, Tuple
from tqdm import tqdm

from co_op_translator.core.llm.markdown_evaluator import MarkdownEvaluator
from co_op_translator.utils.common.metadata_utils import extract_metadata_from_content

logger = logging.getLogger(__name__)


class ProjectEvaluator:
    """
    Class for evaluating translations across an entire project.

    This class provides methods to find all translated files for a given language,
    evaluate their quality, and update metadata with evaluation results.
    """

    def __init__(
        self,
        root_dir: Path,
        translations_dir: Path,
        language_codes: list[str],
        excluded_dirs: list[str],
        markdown_evaluator: MarkdownEvaluator = None,
        use_llm: bool = True,
        use_rule: bool = True,
    ):
        """
        Initialize project evaluator.

        Args:
            root_dir: Root directory containing original files
            translations_dir: Directory for translated files
            language_codes: List of target language codes
            excluded_dirs: List of directories to exclude
            markdown_evaluator: Evaluator instance for markdown files (optional)
            use_llm: Whether to use LLM-based evaluation
            use_rule: Whether to use rule-based evaluation
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.language_codes = language_codes
        self.excluded_dirs = excluded_dirs
        self.use_llm = use_llm
        self.use_rule = use_rule

        # Use the create class method to initialize the MarkdownEvaluator
        self.markdown_evaluator = markdown_evaluator or MarkdownEvaluator.create(
            root_dir=root_dir, use_llm=self.use_llm, use_rule=self.use_rule
        )

    async def evaluate_project(self, language_code: str) -> Tuple[int, int, float]:
        """
        Evaluate translations for a specific language.

        Args:
            language_code: Language code to evaluate

        Returns:
            Tuple containing:
            - Total number of files evaluated
            - Number of files with issues
            - Average confidence score
        """
        logger.info(f"Starting evaluation for language: {language_code}")

        # Get all translated files for this language
        translation_pairs = await self._get_translation_pairs(language_code)

        if not translation_pairs:
            logger.warning(f"No translations found for language code '{language_code}'")
            return 0, 0, 0.0

        # Evaluate each translation
        total_files = len(translation_pairs)
        files_with_issues = 0
        total_confidence = 0.0

        # Determine evaluation mode based on flags
        if self.use_rule and self.use_llm:
            # DEFAULT MODE: Both Rule and LLM evaluation in sequence
            # First Step: Rule-based evaluation
            evaluation_results = {}

            # Create progress bar for rule-based evaluation
            rule_progress_bar = tqdm(
                total=total_files,
                desc=f"Rule-based evaluation for {language_code}",
                unit="files",
                ncols=100,
                bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
            )

            # Perform rule-based evaluation for all files
            for orig_file, trans_file in translation_pairs:
                try:
                    # Read original and translated content
                    with open(orig_file, "r", encoding="utf-8") as f:
                        original_content = f.read()

                    with open(trans_file, "r", encoding="utf-8") as f:
                        translated_content = f.read()

                    # Extract existing metadata
                    metadata = extract_metadata_from_content(translated_content)
                    if not metadata:
                        logger.warning(f"No metadata found in {trans_file}")
                        continue

                    # Store file info for later LLM evaluation
                    file_key = str(trans_file)
                    evaluation_results[file_key] = {
                        "orig_file": orig_file,
                        "trans_file": trans_file,
                        "metadata": metadata,
                        "original_content": original_content,
                        "translated_content": translated_content,
                    }

                    # Update progress bar with current file name
                    try:
                        rel_path = trans_file.relative_to(
                            self.translations_dir / language_code
                        )
                        display_name = str(rel_path)
                    except ValueError:
                        display_name = trans_file.name

                    rule_progress_bar.set_description_str(
                        f"Rule-based evaluation for {language_code}: {display_name}"
                    )

                except Exception as e:
                    logger.error(f"Error processing {trans_file}: {e}")

                rule_progress_bar.update(1)

            # Close the rule-based progress bar
            rule_progress_bar.close()

            # Second Step: LLM-based evaluation
            # Create progress bar for LLM-based evaluation
            llm_progress_bar = tqdm(
                total=len(evaluation_results),
                desc=f"LLM-based evaluation for {language_code}",
                unit="files",
                ncols=100,
                bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
            )

            # Perform LLM-based evaluation for all files
            for file_key, file_data in evaluation_results.items():
                trans_file = file_data["trans_file"]
                orig_file = file_data["orig_file"]

                logger.info(f"Evaluating with LLM: {trans_file}")
                (
                    evaluation_result,
                    success,
                ) = await self.markdown_evaluator.evaluate_markdown(
                    orig_file, trans_file, language_code
                )

                if success and evaluation_result:
                    confidence = evaluation_result.get("confidence_score", 0.0)
                    issues = evaluation_result.get("issues", [])

                    total_confidence += confidence

                    # Count file as problematic if confidence is below threshold
                    if confidence < 0.8:
                        files_with_issues += 1
                        logger.info(
                            f"Low confidence in {trans_file.name}: {confidence}"
                        )

                    # Log issues regardless of confidence score
                    if issues:
                        logger.info(f"Issues found in {trans_file.name}: {issues}")

                # Update progress bar with current file name
                try:
                    rel_path = trans_file.relative_to(
                        self.translations_dir / language_code
                    )
                    display_name = str(rel_path)
                except ValueError:
                    display_name = trans_file.name

                llm_progress_bar.set_description_str(
                    f"LLM-based evaluation for {language_code}: {display_name}"
                )
                llm_progress_bar.update(1)

            # Close the LLM-based progress bar
            llm_progress_bar.close()

        elif self.use_rule:
            # RULE-ONLY MODE: Only rule-based evaluation
            # Create progress bar for rule-based evaluation
            progress_bar = tqdm(
                total=total_files,
                desc=f"Evaluating {language_code} translations [Rule only]",
                unit="files",
                ncols=100,
                bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
            )

            for orig_file, trans_file in translation_pairs:
                logger.info(f"Evaluating: {trans_file}")
                (
                    evaluation_result,
                    success,
                ) = await self.markdown_evaluator.evaluate_markdown(
                    orig_file, trans_file, language_code
                )

                if success and evaluation_result:
                    confidence = evaluation_result.get("confidence_score", 0.0)
                    issues = evaluation_result.get("issues", [])

                    total_confidence += confidence

                    # Count file as problematic if confidence is below threshold
                    if confidence < 0.8:
                        files_with_issues += 1
                        logger.info(
                            f"Low confidence in {trans_file.name}: {confidence}"
                        )

                    # Log issues regardless of confidence score
                    if issues:
                        logger.info(f"Issues found in {trans_file.name}: {issues}")

                # Update progress bar with current file name
                try:
                    rel_path = trans_file.relative_to(
                        self.translations_dir / language_code
                    )
                    display_name = str(rel_path)
                except ValueError:
                    display_name = trans_file.name

                progress_bar.set_description_str(
                    f"Evaluating {language_code}: {display_name} [Rule only]"
                )
                progress_bar.update(1)

            progress_bar.close()

        elif self.use_llm:
            # LLM-ONLY MODE: Only LLM evaluation
            # Create progress bar for LLM evaluation
            progress_bar = tqdm(
                total=total_files,
                desc=f"Evaluating {language_code} translations [LLM only]",
                unit="files",
                ncols=100,
                bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
            )

            for orig_file, trans_file in translation_pairs:
                logger.info(f"Evaluating: {trans_file}")
                (
                    evaluation_result,
                    success,
                ) = await self.markdown_evaluator.evaluate_markdown(
                    orig_file, trans_file, language_code
                )

                if success and evaluation_result:
                    confidence = evaluation_result.get("confidence_score", 0.0)
                    issues = evaluation_result.get("issues", [])

                    total_confidence += confidence

                    # Count file as problematic if confidence is below threshold
                    if confidence < 0.8:
                        files_with_issues += 1
                        logger.info(
                            f"Low confidence in {trans_file.name}: {confidence}"
                        )

                    # Log issues regardless of confidence score
                    if issues:
                        logger.info(f"Issues found in {trans_file.name}: {issues}")

                # Update progress bar with current file name
                try:
                    rel_path = trans_file.relative_to(
                        self.translations_dir / language_code
                    )
                    display_name = str(rel_path)
                except ValueError:
                    display_name = trans_file.name

                progress_bar.set_description_str(
                    f"Evaluating {language_code}: {display_name} [LLM only]"
                )
                progress_bar.update(1)

            progress_bar.close()

        # Calculate average confidence score
        avg_confidence = total_confidence / total_files if total_files > 0 else 0.0

        logger.info(f"Evaluation complete for {language_code}:")
        logger.info(f"Total files evaluated: {total_files}")
        logger.info(f"Files with issues: {files_with_issues}")
        logger.info(f"Average confidence score: {avg_confidence:.2f}")

        return total_files, files_with_issues, avg_confidence

    async def _get_translation_pairs(
        self, language_code: str
    ) -> List[Tuple[Path, Path]]:
        """
        Get all original and translated file pairs for a specific language.

        Args:
            language_code: Language code to find translations for

        Returns:
            List of tuples containing (original_file_path, translated_file_path)
        """
        # Get all markdown files in the project
        markdown_files = self._get_markdown_files()

        # Find corresponding translations
        translation_pairs = []
        for orig_file in markdown_files:
            trans_file = self._get_translation_path(orig_file, language_code)
            if trans_file.exists():
                translation_pairs.append((orig_file, trans_file))

        return translation_pairs

    def _get_markdown_files(self) -> List[Path]:
        """
        Get all markdown files in the project root directory.

        Returns:
            List of Path objects for all markdown files
        """
        markdown_files = []
        for path in self.root_dir.rglob("*.md"):
            # Skip files in excluded directories
            if any(excluded in str(path) for excluded in self.excluded_dirs):
                continue
            if path.is_file():
                markdown_files.append(path)
        return markdown_files

    def _get_translation_path(self, original_file: Path, language_code: str) -> Path:
        """
        Get the path for a translated file based on the original file and language code.

        Args:
            original_file: Path to the original file
            language_code: Target language code

        Returns:
            Path to the corresponding translated file
        """
        # Calculate relative path from root
        try:
            rel_path = original_file.relative_to(self.root_dir)
            # Construct translation path
            translation_path = self.translations_dir / language_code / rel_path
            return translation_path
        except ValueError as e:
            logger.error(f"Error calculating translation path: {e}")
            # Fallback: use original file name in language directory
            return self.translations_dir / language_code / original_file.name

    async def get_low_confidence_translations(
        self, language_code: str, threshold: float = 0.7
    ) -> List[Tuple[Path, float]]:
        """
        Get a list of translations with confidence scores below a threshold.

        Args:
            language_code: Language code to check
            threshold: Confidence score threshold (translations below this will be returned)

        Returns:
            List of tuples containing (translated_file, confidence_score)
        """
        translation_pairs = await self._get_translation_pairs(language_code)
        low_confidence_translations = []

        for _, trans_file in translation_pairs:
            try:
                with open(trans_file, "r", encoding="utf-8") as f:
                    content = f.read()

                from co_op_translator.utils.common.metadata_utils import (
                    extract_metadata_from_content,
                )

                metadata = extract_metadata_from_content(content)

                if metadata and "evaluation" in metadata:
                    confidence = metadata["evaluation"].get("confidence_score", 1.0)
                    if confidence < threshold:
                        low_confidence_translations.append((trans_file, confidence))
            except Exception as e:
                logger.error(f"Error reading metadata from {trans_file}: {e}")

        return low_confidence_translations

    async def get_translations_with_issues(
        self, language_code: str
    ) -> List[Tuple[Path, float, List[str]]]:
        """
        Get a list of translations that have issues_found in their metadata.

        Args:
            language_code: Language code to check

        Returns:
            List of tuples containing (translated_file, confidence_score, issues_found)
        """
        translation_pairs = await self._get_translation_pairs(language_code)
        translations_with_issues = []

        for _, trans_file in translation_pairs:
            try:
                with open(trans_file, "r", encoding="utf-8") as f:
                    content = f.read()

                from co_op_translator.utils.common.metadata_utils import (
                    extract_metadata_from_content,
                )

                metadata = extract_metadata_from_content(content)

                if metadata and "evaluation" in metadata:
                    confidence = metadata["evaluation"].get("confidence_score", 1.0)
                    issues = metadata["evaluation"].get("issues_found", [])
                    if issues:  # Only include if there are issues
                        translations_with_issues.append(
                            (trans_file, confidence, issues)
                        )
            except Exception as e:
                logger.error(f"Error reading metadata from {trans_file}: {e}")

        return translations_with_issues

    async def get_problematic_translations(
        self, language_code: str, threshold: float = 0.7
    ) -> List[Tuple[Path, float, List[str]]]:
        """
        Get a list of translations that either have low confidence scores or issues found.

        Args:
            language_code: Language code to check
            threshold: Confidence score threshold

        Returns:
            List of tuples containing (translated_file, confidence_score, issues_found)
        """
        translation_pairs = await self._get_translation_pairs(language_code)
        problematic_translations = []

        for _, trans_file in translation_pairs:
            try:
                with open(trans_file, "r", encoding="utf-8") as f:
                    content = f.read()

                from co_op_translator.utils.common.metadata_utils import (
                    extract_metadata_from_content,
                )

                metadata = extract_metadata_from_content(content)

                if metadata and "evaluation" in metadata:
                    confidence = metadata["evaluation"].get("confidence_score", 1.0)
                    issues = metadata["evaluation"].get("issues_found", [])
                    # Include files with low confidence OR any issues
                    if confidence < threshold or issues:
                        problematic_translations.append(
                            (trans_file, confidence, issues)
                        )
            except Exception as e:
                logger.error(f"Error reading metadata from {trans_file}: {e}")

        return problematic_translations
